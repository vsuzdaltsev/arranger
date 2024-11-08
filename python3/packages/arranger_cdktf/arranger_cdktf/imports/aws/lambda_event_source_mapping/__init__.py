'''
# `aws_lambda_event_source_mapping`

Refer to the Terraform Registory for docs: [`aws_lambda_event_source_mapping`](https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping).
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


class LambdaEventSourceMapping(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lambdaEventSourceMapping.LambdaEventSourceMapping",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping aws_lambda_event_source_mapping}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        function_name: builtins.str,
        amazon_managed_kafka_event_source_config: typing.Optional[typing.Union["LambdaEventSourceMappingAmazonManagedKafkaEventSourceConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        batch_size: typing.Optional[jsii.Number] = None,
        bisect_batch_on_function_error: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        destination_config: typing.Optional[typing.Union["LambdaEventSourceMappingDestinationConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        event_source_arn: typing.Optional[builtins.str] = None,
        filter_criteria: typing.Optional[typing.Union["LambdaEventSourceMappingFilterCriteria", typing.Dict[builtins.str, typing.Any]]] = None,
        function_response_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        maximum_batching_window_in_seconds: typing.Optional[jsii.Number] = None,
        maximum_record_age_in_seconds: typing.Optional[jsii.Number] = None,
        maximum_retry_attempts: typing.Optional[jsii.Number] = None,
        parallelization_factor: typing.Optional[jsii.Number] = None,
        queues: typing.Optional[typing.Sequence[builtins.str]] = None,
        self_managed_event_source: typing.Optional[typing.Union["LambdaEventSourceMappingSelfManagedEventSource", typing.Dict[builtins.str, typing.Any]]] = None,
        self_managed_kafka_event_source_config: typing.Optional[typing.Union["LambdaEventSourceMappingSelfManagedKafkaEventSourceConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        source_access_configuration: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LambdaEventSourceMappingSourceAccessConfiguration", typing.Dict[builtins.str, typing.Any]]]]] = None,
        starting_position: typing.Optional[builtins.str] = None,
        starting_position_timestamp: typing.Optional[builtins.str] = None,
        topics: typing.Optional[typing.Sequence[builtins.str]] = None,
        tumbling_window_in_seconds: typing.Optional[jsii.Number] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping aws_lambda_event_source_mapping} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param function_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#function_name LambdaEventSourceMapping#function_name}.
        :param amazon_managed_kafka_event_source_config: amazon_managed_kafka_event_source_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#amazon_managed_kafka_event_source_config LambdaEventSourceMapping#amazon_managed_kafka_event_source_config}
        :param batch_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#batch_size LambdaEventSourceMapping#batch_size}.
        :param bisect_batch_on_function_error: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#bisect_batch_on_function_error LambdaEventSourceMapping#bisect_batch_on_function_error}.
        :param destination_config: destination_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#destination_config LambdaEventSourceMapping#destination_config}
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#enabled LambdaEventSourceMapping#enabled}.
        :param event_source_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#event_source_arn LambdaEventSourceMapping#event_source_arn}.
        :param filter_criteria: filter_criteria block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#filter_criteria LambdaEventSourceMapping#filter_criteria}
        :param function_response_types: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#function_response_types LambdaEventSourceMapping#function_response_types}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#id LambdaEventSourceMapping#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param maximum_batching_window_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#maximum_batching_window_in_seconds LambdaEventSourceMapping#maximum_batching_window_in_seconds}.
        :param maximum_record_age_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#maximum_record_age_in_seconds LambdaEventSourceMapping#maximum_record_age_in_seconds}.
        :param maximum_retry_attempts: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#maximum_retry_attempts LambdaEventSourceMapping#maximum_retry_attempts}.
        :param parallelization_factor: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#parallelization_factor LambdaEventSourceMapping#parallelization_factor}.
        :param queues: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#queues LambdaEventSourceMapping#queues}.
        :param self_managed_event_source: self_managed_event_source block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#self_managed_event_source LambdaEventSourceMapping#self_managed_event_source}
        :param self_managed_kafka_event_source_config: self_managed_kafka_event_source_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#self_managed_kafka_event_source_config LambdaEventSourceMapping#self_managed_kafka_event_source_config}
        :param source_access_configuration: source_access_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#source_access_configuration LambdaEventSourceMapping#source_access_configuration}
        :param starting_position: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#starting_position LambdaEventSourceMapping#starting_position}.
        :param starting_position_timestamp: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#starting_position_timestamp LambdaEventSourceMapping#starting_position_timestamp}.
        :param topics: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#topics LambdaEventSourceMapping#topics}.
        :param tumbling_window_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#tumbling_window_in_seconds LambdaEventSourceMapping#tumbling_window_in_seconds}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__203b8d75a05a96a2c4242d28dbea347c739933bb98ad80e2101ea3ff8b7039c4)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = LambdaEventSourceMappingConfig(
            function_name=function_name,
            amazon_managed_kafka_event_source_config=amazon_managed_kafka_event_source_config,
            batch_size=batch_size,
            bisect_batch_on_function_error=bisect_batch_on_function_error,
            destination_config=destination_config,
            enabled=enabled,
            event_source_arn=event_source_arn,
            filter_criteria=filter_criteria,
            function_response_types=function_response_types,
            id=id,
            maximum_batching_window_in_seconds=maximum_batching_window_in_seconds,
            maximum_record_age_in_seconds=maximum_record_age_in_seconds,
            maximum_retry_attempts=maximum_retry_attempts,
            parallelization_factor=parallelization_factor,
            queues=queues,
            self_managed_event_source=self_managed_event_source,
            self_managed_kafka_event_source_config=self_managed_kafka_event_source_config,
            source_access_configuration=source_access_configuration,
            starting_position=starting_position,
            starting_position_timestamp=starting_position_timestamp,
            topics=topics,
            tumbling_window_in_seconds=tumbling_window_in_seconds,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAmazonManagedKafkaEventSourceConfig")
    def put_amazon_managed_kafka_event_source_config(
        self,
        *,
        consumer_group_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param consumer_group_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#consumer_group_id LambdaEventSourceMapping#consumer_group_id}.
        '''
        value = LambdaEventSourceMappingAmazonManagedKafkaEventSourceConfig(
            consumer_group_id=consumer_group_id
        )

        return typing.cast(None, jsii.invoke(self, "putAmazonManagedKafkaEventSourceConfig", [value]))

    @jsii.member(jsii_name="putDestinationConfig")
    def put_destination_config(
        self,
        *,
        on_failure: typing.Optional[typing.Union["LambdaEventSourceMappingDestinationConfigOnFailure", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param on_failure: on_failure block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#on_failure LambdaEventSourceMapping#on_failure}
        '''
        value = LambdaEventSourceMappingDestinationConfig(on_failure=on_failure)

        return typing.cast(None, jsii.invoke(self, "putDestinationConfig", [value]))

    @jsii.member(jsii_name="putFilterCriteria")
    def put_filter_criteria(
        self,
        *,
        filter: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LambdaEventSourceMappingFilterCriteriaFilter", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param filter: filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#filter LambdaEventSourceMapping#filter}
        '''
        value = LambdaEventSourceMappingFilterCriteria(filter=filter)

        return typing.cast(None, jsii.invoke(self, "putFilterCriteria", [value]))

    @jsii.member(jsii_name="putSelfManagedEventSource")
    def put_self_managed_event_source(
        self,
        *,
        endpoints: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        '''
        :param endpoints: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#endpoints LambdaEventSourceMapping#endpoints}.
        '''
        value = LambdaEventSourceMappingSelfManagedEventSource(endpoints=endpoints)

        return typing.cast(None, jsii.invoke(self, "putSelfManagedEventSource", [value]))

    @jsii.member(jsii_name="putSelfManagedKafkaEventSourceConfig")
    def put_self_managed_kafka_event_source_config(
        self,
        *,
        consumer_group_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param consumer_group_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#consumer_group_id LambdaEventSourceMapping#consumer_group_id}.
        '''
        value = LambdaEventSourceMappingSelfManagedKafkaEventSourceConfig(
            consumer_group_id=consumer_group_id
        )

        return typing.cast(None, jsii.invoke(self, "putSelfManagedKafkaEventSourceConfig", [value]))

    @jsii.member(jsii_name="putSourceAccessConfiguration")
    def put_source_access_configuration(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LambdaEventSourceMappingSourceAccessConfiguration", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17c8f73187df18c61107666016d9659f710f905cad98f1b5ee1210db29d31a72)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSourceAccessConfiguration", [value]))

    @jsii.member(jsii_name="resetAmazonManagedKafkaEventSourceConfig")
    def reset_amazon_managed_kafka_event_source_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAmazonManagedKafkaEventSourceConfig", []))

    @jsii.member(jsii_name="resetBatchSize")
    def reset_batch_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBatchSize", []))

    @jsii.member(jsii_name="resetBisectBatchOnFunctionError")
    def reset_bisect_batch_on_function_error(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBisectBatchOnFunctionError", []))

    @jsii.member(jsii_name="resetDestinationConfig")
    def reset_destination_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDestinationConfig", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetEventSourceArn")
    def reset_event_source_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEventSourceArn", []))

    @jsii.member(jsii_name="resetFilterCriteria")
    def reset_filter_criteria(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFilterCriteria", []))

    @jsii.member(jsii_name="resetFunctionResponseTypes")
    def reset_function_response_types(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFunctionResponseTypes", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMaximumBatchingWindowInSeconds")
    def reset_maximum_batching_window_in_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaximumBatchingWindowInSeconds", []))

    @jsii.member(jsii_name="resetMaximumRecordAgeInSeconds")
    def reset_maximum_record_age_in_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaximumRecordAgeInSeconds", []))

    @jsii.member(jsii_name="resetMaximumRetryAttempts")
    def reset_maximum_retry_attempts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaximumRetryAttempts", []))

    @jsii.member(jsii_name="resetParallelizationFactor")
    def reset_parallelization_factor(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParallelizationFactor", []))

    @jsii.member(jsii_name="resetQueues")
    def reset_queues(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueues", []))

    @jsii.member(jsii_name="resetSelfManagedEventSource")
    def reset_self_managed_event_source(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSelfManagedEventSource", []))

    @jsii.member(jsii_name="resetSelfManagedKafkaEventSourceConfig")
    def reset_self_managed_kafka_event_source_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSelfManagedKafkaEventSourceConfig", []))

    @jsii.member(jsii_name="resetSourceAccessConfiguration")
    def reset_source_access_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceAccessConfiguration", []))

    @jsii.member(jsii_name="resetStartingPosition")
    def reset_starting_position(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStartingPosition", []))

    @jsii.member(jsii_name="resetStartingPositionTimestamp")
    def reset_starting_position_timestamp(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStartingPositionTimestamp", []))

    @jsii.member(jsii_name="resetTopics")
    def reset_topics(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTopics", []))

    @jsii.member(jsii_name="resetTumblingWindowInSeconds")
    def reset_tumbling_window_in_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTumblingWindowInSeconds", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="amazonManagedKafkaEventSourceConfig")
    def amazon_managed_kafka_event_source_config(
        self,
    ) -> "LambdaEventSourceMappingAmazonManagedKafkaEventSourceConfigOutputReference":
        return typing.cast("LambdaEventSourceMappingAmazonManagedKafkaEventSourceConfigOutputReference", jsii.get(self, "amazonManagedKafkaEventSourceConfig"))

    @builtins.property
    @jsii.member(jsii_name="destinationConfig")
    def destination_config(
        self,
    ) -> "LambdaEventSourceMappingDestinationConfigOutputReference":
        return typing.cast("LambdaEventSourceMappingDestinationConfigOutputReference", jsii.get(self, "destinationConfig"))

    @builtins.property
    @jsii.member(jsii_name="filterCriteria")
    def filter_criteria(
        self,
    ) -> "LambdaEventSourceMappingFilterCriteriaOutputReference":
        return typing.cast("LambdaEventSourceMappingFilterCriteriaOutputReference", jsii.get(self, "filterCriteria"))

    @builtins.property
    @jsii.member(jsii_name="functionArn")
    def function_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "functionArn"))

    @builtins.property
    @jsii.member(jsii_name="lastModified")
    def last_modified(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastModified"))

    @builtins.property
    @jsii.member(jsii_name="lastProcessingResult")
    def last_processing_result(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastProcessingResult"))

    @builtins.property
    @jsii.member(jsii_name="selfManagedEventSource")
    def self_managed_event_source(
        self,
    ) -> "LambdaEventSourceMappingSelfManagedEventSourceOutputReference":
        return typing.cast("LambdaEventSourceMappingSelfManagedEventSourceOutputReference", jsii.get(self, "selfManagedEventSource"))

    @builtins.property
    @jsii.member(jsii_name="selfManagedKafkaEventSourceConfig")
    def self_managed_kafka_event_source_config(
        self,
    ) -> "LambdaEventSourceMappingSelfManagedKafkaEventSourceConfigOutputReference":
        return typing.cast("LambdaEventSourceMappingSelfManagedKafkaEventSourceConfigOutputReference", jsii.get(self, "selfManagedKafkaEventSourceConfig"))

    @builtins.property
    @jsii.member(jsii_name="sourceAccessConfiguration")
    def source_access_configuration(
        self,
    ) -> "LambdaEventSourceMappingSourceAccessConfigurationList":
        return typing.cast("LambdaEventSourceMappingSourceAccessConfigurationList", jsii.get(self, "sourceAccessConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @builtins.property
    @jsii.member(jsii_name="stateTransitionReason")
    def state_transition_reason(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "stateTransitionReason"))

    @builtins.property
    @jsii.member(jsii_name="uuid")
    def uuid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uuid"))

    @builtins.property
    @jsii.member(jsii_name="amazonManagedKafkaEventSourceConfigInput")
    def amazon_managed_kafka_event_source_config_input(
        self,
    ) -> typing.Optional["LambdaEventSourceMappingAmazonManagedKafkaEventSourceConfig"]:
        return typing.cast(typing.Optional["LambdaEventSourceMappingAmazonManagedKafkaEventSourceConfig"], jsii.get(self, "amazonManagedKafkaEventSourceConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="batchSizeInput")
    def batch_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "batchSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="bisectBatchOnFunctionErrorInput")
    def bisect_batch_on_function_error_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "bisectBatchOnFunctionErrorInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationConfigInput")
    def destination_config_input(
        self,
    ) -> typing.Optional["LambdaEventSourceMappingDestinationConfig"]:
        return typing.cast(typing.Optional["LambdaEventSourceMappingDestinationConfig"], jsii.get(self, "destinationConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="eventSourceArnInput")
    def event_source_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "eventSourceArnInput"))

    @builtins.property
    @jsii.member(jsii_name="filterCriteriaInput")
    def filter_criteria_input(
        self,
    ) -> typing.Optional["LambdaEventSourceMappingFilterCriteria"]:
        return typing.cast(typing.Optional["LambdaEventSourceMappingFilterCriteria"], jsii.get(self, "filterCriteriaInput"))

    @builtins.property
    @jsii.member(jsii_name="functionNameInput")
    def function_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "functionNameInput"))

    @builtins.property
    @jsii.member(jsii_name="functionResponseTypesInput")
    def function_response_types_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "functionResponseTypesInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="maximumBatchingWindowInSecondsInput")
    def maximum_batching_window_in_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maximumBatchingWindowInSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="maximumRecordAgeInSecondsInput")
    def maximum_record_age_in_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maximumRecordAgeInSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="maximumRetryAttemptsInput")
    def maximum_retry_attempts_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maximumRetryAttemptsInput"))

    @builtins.property
    @jsii.member(jsii_name="parallelizationFactorInput")
    def parallelization_factor_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "parallelizationFactorInput"))

    @builtins.property
    @jsii.member(jsii_name="queuesInput")
    def queues_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "queuesInput"))

    @builtins.property
    @jsii.member(jsii_name="selfManagedEventSourceInput")
    def self_managed_event_source_input(
        self,
    ) -> typing.Optional["LambdaEventSourceMappingSelfManagedEventSource"]:
        return typing.cast(typing.Optional["LambdaEventSourceMappingSelfManagedEventSource"], jsii.get(self, "selfManagedEventSourceInput"))

    @builtins.property
    @jsii.member(jsii_name="selfManagedKafkaEventSourceConfigInput")
    def self_managed_kafka_event_source_config_input(
        self,
    ) -> typing.Optional["LambdaEventSourceMappingSelfManagedKafkaEventSourceConfig"]:
        return typing.cast(typing.Optional["LambdaEventSourceMappingSelfManagedKafkaEventSourceConfig"], jsii.get(self, "selfManagedKafkaEventSourceConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceAccessConfigurationInput")
    def source_access_configuration_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LambdaEventSourceMappingSourceAccessConfiguration"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LambdaEventSourceMappingSourceAccessConfiguration"]]], jsii.get(self, "sourceAccessConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="startingPositionInput")
    def starting_position_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "startingPositionInput"))

    @builtins.property
    @jsii.member(jsii_name="startingPositionTimestampInput")
    def starting_position_timestamp_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "startingPositionTimestampInput"))

    @builtins.property
    @jsii.member(jsii_name="topicsInput")
    def topics_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "topicsInput"))

    @builtins.property
    @jsii.member(jsii_name="tumblingWindowInSecondsInput")
    def tumbling_window_in_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "tumblingWindowInSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="batchSize")
    def batch_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "batchSize"))

    @batch_size.setter
    def batch_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8520944f0bf5d6e18e5b4566b1f9a5b666d00bb167cc43d3ee57c7c2aa39cb1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "batchSize", value)

    @builtins.property
    @jsii.member(jsii_name="bisectBatchOnFunctionError")
    def bisect_batch_on_function_error(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "bisectBatchOnFunctionError"))

    @bisect_batch_on_function_error.setter
    def bisect_batch_on_function_error(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__34d9d1ddcca1c7e8ef3af903886f6c4a09bf1258feea577aba1f9c6fe26f21ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bisectBatchOnFunctionError", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__550f64f8e86c762a03ee244ddcba44b25706e6df013825d2a47f9999052a52ef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="eventSourceArn")
    def event_source_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "eventSourceArn"))

    @event_source_arn.setter
    def event_source_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5afb31ea0875d01ca338596859f936c4cce5a50e79b5f9347edc289d3e9e3753)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventSourceArn", value)

    @builtins.property
    @jsii.member(jsii_name="functionName")
    def function_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "functionName"))

    @function_name.setter
    def function_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91beb63822fbf57ee9880dfb3f0a3eed84eea81d76fbf786bf2e04609c8ab505)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "functionName", value)

    @builtins.property
    @jsii.member(jsii_name="functionResponseTypes")
    def function_response_types(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "functionResponseTypes"))

    @function_response_types.setter
    def function_response_types(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__195b395dcf05e5f9fe519bd52be8520bfd7f8b0774b0739a671a125c6bc8bc01)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "functionResponseTypes", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3587eb25bd82b25459b134bf5d20aaa69d7d5091d37be36d4d7988cf9bf8a1d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="maximumBatchingWindowInSeconds")
    def maximum_batching_window_in_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maximumBatchingWindowInSeconds"))

    @maximum_batching_window_in_seconds.setter
    def maximum_batching_window_in_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc3c5ba81566732e36c97a6bf20729a951f8364fe40108592d05024912deb4b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maximumBatchingWindowInSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="maximumRecordAgeInSeconds")
    def maximum_record_age_in_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maximumRecordAgeInSeconds"))

    @maximum_record_age_in_seconds.setter
    def maximum_record_age_in_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__34eed8bedc85805551addacc6fbdec630a5cc9cb838bf4aed54d14113b9750ff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maximumRecordAgeInSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="maximumRetryAttempts")
    def maximum_retry_attempts(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maximumRetryAttempts"))

    @maximum_retry_attempts.setter
    def maximum_retry_attempts(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1a76e83ebabc6c8bc958a08b7600bb80b6b4d5ef210705a1e6da9ca82598615)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maximumRetryAttempts", value)

    @builtins.property
    @jsii.member(jsii_name="parallelizationFactor")
    def parallelization_factor(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "parallelizationFactor"))

    @parallelization_factor.setter
    def parallelization_factor(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c58096ce3a9c00470502271cf2bcb4abebc0da6c78b5dca5b94c2d74abc8e625)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parallelizationFactor", value)

    @builtins.property
    @jsii.member(jsii_name="queues")
    def queues(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "queues"))

    @queues.setter
    def queues(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7496e9672cd50a12f9a69abd3556b053de3b3aa9f4e2ae18d70c6de0194058ed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queues", value)

    @builtins.property
    @jsii.member(jsii_name="startingPosition")
    def starting_position(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "startingPosition"))

    @starting_position.setter
    def starting_position(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8cec97eaa120b9f0456e524d79d328b22e50e5b0f408720ac2c8c6a34d8c87ff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startingPosition", value)

    @builtins.property
    @jsii.member(jsii_name="startingPositionTimestamp")
    def starting_position_timestamp(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "startingPositionTimestamp"))

    @starting_position_timestamp.setter
    def starting_position_timestamp(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__493a0b806be9bc521e85e9520abcc695263ca309412b0eccdeadd58bd4750618)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startingPositionTimestamp", value)

    @builtins.property
    @jsii.member(jsii_name="topics")
    def topics(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "topics"))

    @topics.setter
    def topics(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ddef2a317ff13a8725be2cfd3aacb87b85662abff6f63f48493da7a382121e2b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "topics", value)

    @builtins.property
    @jsii.member(jsii_name="tumblingWindowInSeconds")
    def tumbling_window_in_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "tumblingWindowInSeconds"))

    @tumbling_window_in_seconds.setter
    def tumbling_window_in_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2feae161b08bb6867debd52ebeb495389fc7742c8ea95e6e54b78fc406eba625)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tumblingWindowInSeconds", value)


@jsii.data_type(
    jsii_type="aws.lambdaEventSourceMapping.LambdaEventSourceMappingAmazonManagedKafkaEventSourceConfig",
    jsii_struct_bases=[],
    name_mapping={"consumer_group_id": "consumerGroupId"},
)
class LambdaEventSourceMappingAmazonManagedKafkaEventSourceConfig:
    def __init__(
        self,
        *,
        consumer_group_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param consumer_group_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#consumer_group_id LambdaEventSourceMapping#consumer_group_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5fb52f35a99b0d88279780edbe242530191c24c0c93c639076b58aa82b31478b)
            check_type(argname="argument consumer_group_id", value=consumer_group_id, expected_type=type_hints["consumer_group_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if consumer_group_id is not None:
            self._values["consumer_group_id"] = consumer_group_id

    @builtins.property
    def consumer_group_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#consumer_group_id LambdaEventSourceMapping#consumer_group_id}.'''
        result = self._values.get("consumer_group_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LambdaEventSourceMappingAmazonManagedKafkaEventSourceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LambdaEventSourceMappingAmazonManagedKafkaEventSourceConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lambdaEventSourceMapping.LambdaEventSourceMappingAmazonManagedKafkaEventSourceConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e7a61dc3bf12cfd509aed52660eb7ba4ecd0b471a1e2eaefb236cc7260f581e1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetConsumerGroupId")
    def reset_consumer_group_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConsumerGroupId", []))

    @builtins.property
    @jsii.member(jsii_name="consumerGroupIdInput")
    def consumer_group_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "consumerGroupIdInput"))

    @builtins.property
    @jsii.member(jsii_name="consumerGroupId")
    def consumer_group_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "consumerGroupId"))

    @consumer_group_id.setter
    def consumer_group_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5fdbcd5f18d386fb6e9761f897239294b3409c5f9c451a728dff25cc2cfb9a16)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "consumerGroupId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LambdaEventSourceMappingAmazonManagedKafkaEventSourceConfig]:
        return typing.cast(typing.Optional[LambdaEventSourceMappingAmazonManagedKafkaEventSourceConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LambdaEventSourceMappingAmazonManagedKafkaEventSourceConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3004ad524f0999131eac6a5e837034a4d70a57660ccb3b7d7737ba0a4027724)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.lambdaEventSourceMapping.LambdaEventSourceMappingConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "function_name": "functionName",
        "amazon_managed_kafka_event_source_config": "amazonManagedKafkaEventSourceConfig",
        "batch_size": "batchSize",
        "bisect_batch_on_function_error": "bisectBatchOnFunctionError",
        "destination_config": "destinationConfig",
        "enabled": "enabled",
        "event_source_arn": "eventSourceArn",
        "filter_criteria": "filterCriteria",
        "function_response_types": "functionResponseTypes",
        "id": "id",
        "maximum_batching_window_in_seconds": "maximumBatchingWindowInSeconds",
        "maximum_record_age_in_seconds": "maximumRecordAgeInSeconds",
        "maximum_retry_attempts": "maximumRetryAttempts",
        "parallelization_factor": "parallelizationFactor",
        "queues": "queues",
        "self_managed_event_source": "selfManagedEventSource",
        "self_managed_kafka_event_source_config": "selfManagedKafkaEventSourceConfig",
        "source_access_configuration": "sourceAccessConfiguration",
        "starting_position": "startingPosition",
        "starting_position_timestamp": "startingPositionTimestamp",
        "topics": "topics",
        "tumbling_window_in_seconds": "tumblingWindowInSeconds",
    },
)
class LambdaEventSourceMappingConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        function_name: builtins.str,
        amazon_managed_kafka_event_source_config: typing.Optional[typing.Union[LambdaEventSourceMappingAmazonManagedKafkaEventSourceConfig, typing.Dict[builtins.str, typing.Any]]] = None,
        batch_size: typing.Optional[jsii.Number] = None,
        bisect_batch_on_function_error: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        destination_config: typing.Optional[typing.Union["LambdaEventSourceMappingDestinationConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        event_source_arn: typing.Optional[builtins.str] = None,
        filter_criteria: typing.Optional[typing.Union["LambdaEventSourceMappingFilterCriteria", typing.Dict[builtins.str, typing.Any]]] = None,
        function_response_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        maximum_batching_window_in_seconds: typing.Optional[jsii.Number] = None,
        maximum_record_age_in_seconds: typing.Optional[jsii.Number] = None,
        maximum_retry_attempts: typing.Optional[jsii.Number] = None,
        parallelization_factor: typing.Optional[jsii.Number] = None,
        queues: typing.Optional[typing.Sequence[builtins.str]] = None,
        self_managed_event_source: typing.Optional[typing.Union["LambdaEventSourceMappingSelfManagedEventSource", typing.Dict[builtins.str, typing.Any]]] = None,
        self_managed_kafka_event_source_config: typing.Optional[typing.Union["LambdaEventSourceMappingSelfManagedKafkaEventSourceConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        source_access_configuration: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LambdaEventSourceMappingSourceAccessConfiguration", typing.Dict[builtins.str, typing.Any]]]]] = None,
        starting_position: typing.Optional[builtins.str] = None,
        starting_position_timestamp: typing.Optional[builtins.str] = None,
        topics: typing.Optional[typing.Sequence[builtins.str]] = None,
        tumbling_window_in_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param function_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#function_name LambdaEventSourceMapping#function_name}.
        :param amazon_managed_kafka_event_source_config: amazon_managed_kafka_event_source_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#amazon_managed_kafka_event_source_config LambdaEventSourceMapping#amazon_managed_kafka_event_source_config}
        :param batch_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#batch_size LambdaEventSourceMapping#batch_size}.
        :param bisect_batch_on_function_error: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#bisect_batch_on_function_error LambdaEventSourceMapping#bisect_batch_on_function_error}.
        :param destination_config: destination_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#destination_config LambdaEventSourceMapping#destination_config}
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#enabled LambdaEventSourceMapping#enabled}.
        :param event_source_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#event_source_arn LambdaEventSourceMapping#event_source_arn}.
        :param filter_criteria: filter_criteria block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#filter_criteria LambdaEventSourceMapping#filter_criteria}
        :param function_response_types: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#function_response_types LambdaEventSourceMapping#function_response_types}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#id LambdaEventSourceMapping#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param maximum_batching_window_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#maximum_batching_window_in_seconds LambdaEventSourceMapping#maximum_batching_window_in_seconds}.
        :param maximum_record_age_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#maximum_record_age_in_seconds LambdaEventSourceMapping#maximum_record_age_in_seconds}.
        :param maximum_retry_attempts: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#maximum_retry_attempts LambdaEventSourceMapping#maximum_retry_attempts}.
        :param parallelization_factor: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#parallelization_factor LambdaEventSourceMapping#parallelization_factor}.
        :param queues: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#queues LambdaEventSourceMapping#queues}.
        :param self_managed_event_source: self_managed_event_source block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#self_managed_event_source LambdaEventSourceMapping#self_managed_event_source}
        :param self_managed_kafka_event_source_config: self_managed_kafka_event_source_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#self_managed_kafka_event_source_config LambdaEventSourceMapping#self_managed_kafka_event_source_config}
        :param source_access_configuration: source_access_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#source_access_configuration LambdaEventSourceMapping#source_access_configuration}
        :param starting_position: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#starting_position LambdaEventSourceMapping#starting_position}.
        :param starting_position_timestamp: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#starting_position_timestamp LambdaEventSourceMapping#starting_position_timestamp}.
        :param topics: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#topics LambdaEventSourceMapping#topics}.
        :param tumbling_window_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#tumbling_window_in_seconds LambdaEventSourceMapping#tumbling_window_in_seconds}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(amazon_managed_kafka_event_source_config, dict):
            amazon_managed_kafka_event_source_config = LambdaEventSourceMappingAmazonManagedKafkaEventSourceConfig(**amazon_managed_kafka_event_source_config)
        if isinstance(destination_config, dict):
            destination_config = LambdaEventSourceMappingDestinationConfig(**destination_config)
        if isinstance(filter_criteria, dict):
            filter_criteria = LambdaEventSourceMappingFilterCriteria(**filter_criteria)
        if isinstance(self_managed_event_source, dict):
            self_managed_event_source = LambdaEventSourceMappingSelfManagedEventSource(**self_managed_event_source)
        if isinstance(self_managed_kafka_event_source_config, dict):
            self_managed_kafka_event_source_config = LambdaEventSourceMappingSelfManagedKafkaEventSourceConfig(**self_managed_kafka_event_source_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35bc74599b1dfb4ad7fb3e074996f03fad6314252ee4bddb42f9e4ac5e464a44)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument function_name", value=function_name, expected_type=type_hints["function_name"])
            check_type(argname="argument amazon_managed_kafka_event_source_config", value=amazon_managed_kafka_event_source_config, expected_type=type_hints["amazon_managed_kafka_event_source_config"])
            check_type(argname="argument batch_size", value=batch_size, expected_type=type_hints["batch_size"])
            check_type(argname="argument bisect_batch_on_function_error", value=bisect_batch_on_function_error, expected_type=type_hints["bisect_batch_on_function_error"])
            check_type(argname="argument destination_config", value=destination_config, expected_type=type_hints["destination_config"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument event_source_arn", value=event_source_arn, expected_type=type_hints["event_source_arn"])
            check_type(argname="argument filter_criteria", value=filter_criteria, expected_type=type_hints["filter_criteria"])
            check_type(argname="argument function_response_types", value=function_response_types, expected_type=type_hints["function_response_types"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument maximum_batching_window_in_seconds", value=maximum_batching_window_in_seconds, expected_type=type_hints["maximum_batching_window_in_seconds"])
            check_type(argname="argument maximum_record_age_in_seconds", value=maximum_record_age_in_seconds, expected_type=type_hints["maximum_record_age_in_seconds"])
            check_type(argname="argument maximum_retry_attempts", value=maximum_retry_attempts, expected_type=type_hints["maximum_retry_attempts"])
            check_type(argname="argument parallelization_factor", value=parallelization_factor, expected_type=type_hints["parallelization_factor"])
            check_type(argname="argument queues", value=queues, expected_type=type_hints["queues"])
            check_type(argname="argument self_managed_event_source", value=self_managed_event_source, expected_type=type_hints["self_managed_event_source"])
            check_type(argname="argument self_managed_kafka_event_source_config", value=self_managed_kafka_event_source_config, expected_type=type_hints["self_managed_kafka_event_source_config"])
            check_type(argname="argument source_access_configuration", value=source_access_configuration, expected_type=type_hints["source_access_configuration"])
            check_type(argname="argument starting_position", value=starting_position, expected_type=type_hints["starting_position"])
            check_type(argname="argument starting_position_timestamp", value=starting_position_timestamp, expected_type=type_hints["starting_position_timestamp"])
            check_type(argname="argument topics", value=topics, expected_type=type_hints["topics"])
            check_type(argname="argument tumbling_window_in_seconds", value=tumbling_window_in_seconds, expected_type=type_hints["tumbling_window_in_seconds"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "function_name": function_name,
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
        if amazon_managed_kafka_event_source_config is not None:
            self._values["amazon_managed_kafka_event_source_config"] = amazon_managed_kafka_event_source_config
        if batch_size is not None:
            self._values["batch_size"] = batch_size
        if bisect_batch_on_function_error is not None:
            self._values["bisect_batch_on_function_error"] = bisect_batch_on_function_error
        if destination_config is not None:
            self._values["destination_config"] = destination_config
        if enabled is not None:
            self._values["enabled"] = enabled
        if event_source_arn is not None:
            self._values["event_source_arn"] = event_source_arn
        if filter_criteria is not None:
            self._values["filter_criteria"] = filter_criteria
        if function_response_types is not None:
            self._values["function_response_types"] = function_response_types
        if id is not None:
            self._values["id"] = id
        if maximum_batching_window_in_seconds is not None:
            self._values["maximum_batching_window_in_seconds"] = maximum_batching_window_in_seconds
        if maximum_record_age_in_seconds is not None:
            self._values["maximum_record_age_in_seconds"] = maximum_record_age_in_seconds
        if maximum_retry_attempts is not None:
            self._values["maximum_retry_attempts"] = maximum_retry_attempts
        if parallelization_factor is not None:
            self._values["parallelization_factor"] = parallelization_factor
        if queues is not None:
            self._values["queues"] = queues
        if self_managed_event_source is not None:
            self._values["self_managed_event_source"] = self_managed_event_source
        if self_managed_kafka_event_source_config is not None:
            self._values["self_managed_kafka_event_source_config"] = self_managed_kafka_event_source_config
        if source_access_configuration is not None:
            self._values["source_access_configuration"] = source_access_configuration
        if starting_position is not None:
            self._values["starting_position"] = starting_position
        if starting_position_timestamp is not None:
            self._values["starting_position_timestamp"] = starting_position_timestamp
        if topics is not None:
            self._values["topics"] = topics
        if tumbling_window_in_seconds is not None:
            self._values["tumbling_window_in_seconds"] = tumbling_window_in_seconds

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
    def function_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#function_name LambdaEventSourceMapping#function_name}.'''
        result = self._values.get("function_name")
        assert result is not None, "Required property 'function_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def amazon_managed_kafka_event_source_config(
        self,
    ) -> typing.Optional[LambdaEventSourceMappingAmazonManagedKafkaEventSourceConfig]:
        '''amazon_managed_kafka_event_source_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#amazon_managed_kafka_event_source_config LambdaEventSourceMapping#amazon_managed_kafka_event_source_config}
        '''
        result = self._values.get("amazon_managed_kafka_event_source_config")
        return typing.cast(typing.Optional[LambdaEventSourceMappingAmazonManagedKafkaEventSourceConfig], result)

    @builtins.property
    def batch_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#batch_size LambdaEventSourceMapping#batch_size}.'''
        result = self._values.get("batch_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def bisect_batch_on_function_error(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#bisect_batch_on_function_error LambdaEventSourceMapping#bisect_batch_on_function_error}.'''
        result = self._values.get("bisect_batch_on_function_error")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def destination_config(
        self,
    ) -> typing.Optional["LambdaEventSourceMappingDestinationConfig"]:
        '''destination_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#destination_config LambdaEventSourceMapping#destination_config}
        '''
        result = self._values.get("destination_config")
        return typing.cast(typing.Optional["LambdaEventSourceMappingDestinationConfig"], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#enabled LambdaEventSourceMapping#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def event_source_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#event_source_arn LambdaEventSourceMapping#event_source_arn}.'''
        result = self._values.get("event_source_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def filter_criteria(
        self,
    ) -> typing.Optional["LambdaEventSourceMappingFilterCriteria"]:
        '''filter_criteria block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#filter_criteria LambdaEventSourceMapping#filter_criteria}
        '''
        result = self._values.get("filter_criteria")
        return typing.cast(typing.Optional["LambdaEventSourceMappingFilterCriteria"], result)

    @builtins.property
    def function_response_types(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#function_response_types LambdaEventSourceMapping#function_response_types}.'''
        result = self._values.get("function_response_types")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#id LambdaEventSourceMapping#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def maximum_batching_window_in_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#maximum_batching_window_in_seconds LambdaEventSourceMapping#maximum_batching_window_in_seconds}.'''
        result = self._values.get("maximum_batching_window_in_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def maximum_record_age_in_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#maximum_record_age_in_seconds LambdaEventSourceMapping#maximum_record_age_in_seconds}.'''
        result = self._values.get("maximum_record_age_in_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def maximum_retry_attempts(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#maximum_retry_attempts LambdaEventSourceMapping#maximum_retry_attempts}.'''
        result = self._values.get("maximum_retry_attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def parallelization_factor(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#parallelization_factor LambdaEventSourceMapping#parallelization_factor}.'''
        result = self._values.get("parallelization_factor")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def queues(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#queues LambdaEventSourceMapping#queues}.'''
        result = self._values.get("queues")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def self_managed_event_source(
        self,
    ) -> typing.Optional["LambdaEventSourceMappingSelfManagedEventSource"]:
        '''self_managed_event_source block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#self_managed_event_source LambdaEventSourceMapping#self_managed_event_source}
        '''
        result = self._values.get("self_managed_event_source")
        return typing.cast(typing.Optional["LambdaEventSourceMappingSelfManagedEventSource"], result)

    @builtins.property
    def self_managed_kafka_event_source_config(
        self,
    ) -> typing.Optional["LambdaEventSourceMappingSelfManagedKafkaEventSourceConfig"]:
        '''self_managed_kafka_event_source_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#self_managed_kafka_event_source_config LambdaEventSourceMapping#self_managed_kafka_event_source_config}
        '''
        result = self._values.get("self_managed_kafka_event_source_config")
        return typing.cast(typing.Optional["LambdaEventSourceMappingSelfManagedKafkaEventSourceConfig"], result)

    @builtins.property
    def source_access_configuration(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LambdaEventSourceMappingSourceAccessConfiguration"]]]:
        '''source_access_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#source_access_configuration LambdaEventSourceMapping#source_access_configuration}
        '''
        result = self._values.get("source_access_configuration")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LambdaEventSourceMappingSourceAccessConfiguration"]]], result)

    @builtins.property
    def starting_position(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#starting_position LambdaEventSourceMapping#starting_position}.'''
        result = self._values.get("starting_position")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def starting_position_timestamp(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#starting_position_timestamp LambdaEventSourceMapping#starting_position_timestamp}.'''
        result = self._values.get("starting_position_timestamp")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def topics(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#topics LambdaEventSourceMapping#topics}.'''
        result = self._values.get("topics")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tumbling_window_in_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#tumbling_window_in_seconds LambdaEventSourceMapping#tumbling_window_in_seconds}.'''
        result = self._values.get("tumbling_window_in_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LambdaEventSourceMappingConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.lambdaEventSourceMapping.LambdaEventSourceMappingDestinationConfig",
    jsii_struct_bases=[],
    name_mapping={"on_failure": "onFailure"},
)
class LambdaEventSourceMappingDestinationConfig:
    def __init__(
        self,
        *,
        on_failure: typing.Optional[typing.Union["LambdaEventSourceMappingDestinationConfigOnFailure", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param on_failure: on_failure block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#on_failure LambdaEventSourceMapping#on_failure}
        '''
        if isinstance(on_failure, dict):
            on_failure = LambdaEventSourceMappingDestinationConfigOnFailure(**on_failure)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__351557df9005a60dbc4b9b0844b31f80e4666e6dc81cd7637b98c359ef37afac)
            check_type(argname="argument on_failure", value=on_failure, expected_type=type_hints["on_failure"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if on_failure is not None:
            self._values["on_failure"] = on_failure

    @builtins.property
    def on_failure(
        self,
    ) -> typing.Optional["LambdaEventSourceMappingDestinationConfigOnFailure"]:
        '''on_failure block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#on_failure LambdaEventSourceMapping#on_failure}
        '''
        result = self._values.get("on_failure")
        return typing.cast(typing.Optional["LambdaEventSourceMappingDestinationConfigOnFailure"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LambdaEventSourceMappingDestinationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.lambdaEventSourceMapping.LambdaEventSourceMappingDestinationConfigOnFailure",
    jsii_struct_bases=[],
    name_mapping={"destination_arn": "destinationArn"},
)
class LambdaEventSourceMappingDestinationConfigOnFailure:
    def __init__(self, *, destination_arn: builtins.str) -> None:
        '''
        :param destination_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#destination_arn LambdaEventSourceMapping#destination_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e50c0629fe98d7df8b70c0b62d5e4814393b01b1f9fb0a7b7c33820029ae95af)
            check_type(argname="argument destination_arn", value=destination_arn, expected_type=type_hints["destination_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "destination_arn": destination_arn,
        }

    @builtins.property
    def destination_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#destination_arn LambdaEventSourceMapping#destination_arn}.'''
        result = self._values.get("destination_arn")
        assert result is not None, "Required property 'destination_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LambdaEventSourceMappingDestinationConfigOnFailure(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LambdaEventSourceMappingDestinationConfigOnFailureOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lambdaEventSourceMapping.LambdaEventSourceMappingDestinationConfigOnFailureOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__66400dc8954782bbfbcce739277d7b1bf9c4ad1d5bf596024914c969e7a98b5b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="destinationArnInput")
    def destination_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationArnInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationArn")
    def destination_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destinationArn"))

    @destination_arn.setter
    def destination_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4bdbcf1971d8b4c2de25de04928f6b3572fdad930c63fb50fea88b7e7e6c0c78)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LambdaEventSourceMappingDestinationConfigOnFailure]:
        return typing.cast(typing.Optional[LambdaEventSourceMappingDestinationConfigOnFailure], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LambdaEventSourceMappingDestinationConfigOnFailure],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1077694f7bf7e5840102e82235260f9ffdf30cbc1bec0c2877166d36b400257e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LambdaEventSourceMappingDestinationConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lambdaEventSourceMapping.LambdaEventSourceMappingDestinationConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__863adec7399ae46f58d06ca7ca8bb0b89413ae10e101cea15999d5f1ad811843)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putOnFailure")
    def put_on_failure(self, *, destination_arn: builtins.str) -> None:
        '''
        :param destination_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#destination_arn LambdaEventSourceMapping#destination_arn}.
        '''
        value = LambdaEventSourceMappingDestinationConfigOnFailure(
            destination_arn=destination_arn
        )

        return typing.cast(None, jsii.invoke(self, "putOnFailure", [value]))

    @jsii.member(jsii_name="resetOnFailure")
    def reset_on_failure(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOnFailure", []))

    @builtins.property
    @jsii.member(jsii_name="onFailure")
    def on_failure(
        self,
    ) -> LambdaEventSourceMappingDestinationConfigOnFailureOutputReference:
        return typing.cast(LambdaEventSourceMappingDestinationConfigOnFailureOutputReference, jsii.get(self, "onFailure"))

    @builtins.property
    @jsii.member(jsii_name="onFailureInput")
    def on_failure_input(
        self,
    ) -> typing.Optional[LambdaEventSourceMappingDestinationConfigOnFailure]:
        return typing.cast(typing.Optional[LambdaEventSourceMappingDestinationConfigOnFailure], jsii.get(self, "onFailureInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LambdaEventSourceMappingDestinationConfig]:
        return typing.cast(typing.Optional[LambdaEventSourceMappingDestinationConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LambdaEventSourceMappingDestinationConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23713dc6accdb9f94d1d5c72581895bee581a933e313dae1aa06a8952636ed83)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.lambdaEventSourceMapping.LambdaEventSourceMappingFilterCriteria",
    jsii_struct_bases=[],
    name_mapping={"filter": "filter"},
)
class LambdaEventSourceMappingFilterCriteria:
    def __init__(
        self,
        *,
        filter: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LambdaEventSourceMappingFilterCriteriaFilter", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param filter: filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#filter LambdaEventSourceMapping#filter}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f665599571598a38b04c86a24ab3a38d979359cee4ea692e3afa91b5b02bee47)
            check_type(argname="argument filter", value=filter, expected_type=type_hints["filter"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if filter is not None:
            self._values["filter"] = filter

    @builtins.property
    def filter(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LambdaEventSourceMappingFilterCriteriaFilter"]]]:
        '''filter block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#filter LambdaEventSourceMapping#filter}
        '''
        result = self._values.get("filter")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LambdaEventSourceMappingFilterCriteriaFilter"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LambdaEventSourceMappingFilterCriteria(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.lambdaEventSourceMapping.LambdaEventSourceMappingFilterCriteriaFilter",
    jsii_struct_bases=[],
    name_mapping={"pattern": "pattern"},
)
class LambdaEventSourceMappingFilterCriteriaFilter:
    def __init__(self, *, pattern: typing.Optional[builtins.str] = None) -> None:
        '''
        :param pattern: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#pattern LambdaEventSourceMapping#pattern}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5df98b4c69bd95f431c20f0a8e5cdd807e32dde56cf2e8b42b971b324314f0a)
            check_type(argname="argument pattern", value=pattern, expected_type=type_hints["pattern"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if pattern is not None:
            self._values["pattern"] = pattern

    @builtins.property
    def pattern(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#pattern LambdaEventSourceMapping#pattern}.'''
        result = self._values.get("pattern")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LambdaEventSourceMappingFilterCriteriaFilter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LambdaEventSourceMappingFilterCriteriaFilterList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lambdaEventSourceMapping.LambdaEventSourceMappingFilterCriteriaFilterList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ca2407b2b6c60e5061e18e946a5751a975bb921ec22240271dac644b44c1c636)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LambdaEventSourceMappingFilterCriteriaFilterOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42dc6971b5c85999b54de9cce5fcad65dbcc20aa91d9840b2e9c59f2da6b3b3d)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LambdaEventSourceMappingFilterCriteriaFilterOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__242020642b007fc5e5c6e3ef6e51aa2a86deffb3e67fcf4ce6d99732695e1774)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9f72a08b00d0fc5a74d2d5c781a004e562583b3f5a60dd1f00b7bf3ddacad209)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7646fae3222e66f4184ea9a1a54258cfead2d5bbc5e7f28ee180060ee10eff46)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LambdaEventSourceMappingFilterCriteriaFilter]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LambdaEventSourceMappingFilterCriteriaFilter]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LambdaEventSourceMappingFilterCriteriaFilter]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f4d7915effcaf4c78906f6b03f49430e09a145b37867bf9b17989411987bb55)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LambdaEventSourceMappingFilterCriteriaFilterOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lambdaEventSourceMapping.LambdaEventSourceMappingFilterCriteriaFilterOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__98b71223d9c08cfe59a4dda8c35c323fc7014d64443c5e3ff520e1a9a95f5d5c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetPattern")
    def reset_pattern(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPattern", []))

    @builtins.property
    @jsii.member(jsii_name="patternInput")
    def pattern_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "patternInput"))

    @builtins.property
    @jsii.member(jsii_name="pattern")
    def pattern(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pattern"))

    @pattern.setter
    def pattern(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3440b6ea48c604bc9767c9c9e4e7318519cd980611f7f5a535fd122a9bd0070)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pattern", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LambdaEventSourceMappingFilterCriteriaFilter, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LambdaEventSourceMappingFilterCriteriaFilter, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LambdaEventSourceMappingFilterCriteriaFilter, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__211fdd285ab10aaf1c8e3f0aa09c9e329e4ec2a61c1141b34a95737563958dce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LambdaEventSourceMappingFilterCriteriaOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lambdaEventSourceMapping.LambdaEventSourceMappingFilterCriteriaOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__669d3d61b4856d241c03c94f03f4b26e156f48f26d8d22b7ec0225724012f383)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putFilter")
    def put_filter(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LambdaEventSourceMappingFilterCriteriaFilter, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8fa11a25516a08a4686fe48472234974d05f5a90c151f64ef2b632818091449)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putFilter", [value]))

    @jsii.member(jsii_name="resetFilter")
    def reset_filter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFilter", []))

    @builtins.property
    @jsii.member(jsii_name="filter")
    def filter(self) -> LambdaEventSourceMappingFilterCriteriaFilterList:
        return typing.cast(LambdaEventSourceMappingFilterCriteriaFilterList, jsii.get(self, "filter"))

    @builtins.property
    @jsii.member(jsii_name="filterInput")
    def filter_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LambdaEventSourceMappingFilterCriteriaFilter]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LambdaEventSourceMappingFilterCriteriaFilter]]], jsii.get(self, "filterInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LambdaEventSourceMappingFilterCriteria]:
        return typing.cast(typing.Optional[LambdaEventSourceMappingFilterCriteria], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LambdaEventSourceMappingFilterCriteria],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0fc3cfaee6fbc9f0f11b5045b4dd6dc53e9fbc1ec91f2b7e96201e57bdc3a39b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.lambdaEventSourceMapping.LambdaEventSourceMappingSelfManagedEventSource",
    jsii_struct_bases=[],
    name_mapping={"endpoints": "endpoints"},
)
class LambdaEventSourceMappingSelfManagedEventSource:
    def __init__(
        self,
        *,
        endpoints: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        '''
        :param endpoints: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#endpoints LambdaEventSourceMapping#endpoints}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bfb8e77b47ed8b8141654b07fea3e44faec686de15c86fee133fd280a3dc4fc1)
            check_type(argname="argument endpoints", value=endpoints, expected_type=type_hints["endpoints"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "endpoints": endpoints,
        }

    @builtins.property
    def endpoints(self) -> typing.Mapping[builtins.str, builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#endpoints LambdaEventSourceMapping#endpoints}.'''
        result = self._values.get("endpoints")
        assert result is not None, "Required property 'endpoints' is missing"
        return typing.cast(typing.Mapping[builtins.str, builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LambdaEventSourceMappingSelfManagedEventSource(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LambdaEventSourceMappingSelfManagedEventSourceOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lambdaEventSourceMapping.LambdaEventSourceMappingSelfManagedEventSourceOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__51b06c31a47e3773fc3ca009ed996a2cabeaf61040f872fe61c31e8eb924b16c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="endpointsInput")
    def endpoints_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "endpointsInput"))

    @builtins.property
    @jsii.member(jsii_name="endpoints")
    def endpoints(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "endpoints"))

    @endpoints.setter
    def endpoints(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0187b7c3ae02dc9785c6d4b9b67a1a79077f1c762aad0896d3c7ff5b09664d82)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpoints", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LambdaEventSourceMappingSelfManagedEventSource]:
        return typing.cast(typing.Optional[LambdaEventSourceMappingSelfManagedEventSource], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LambdaEventSourceMappingSelfManagedEventSource],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0ee9f4d9fe8b607a9f3270a8c57eb27a5d7fe742b48f23989175158351c201f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.lambdaEventSourceMapping.LambdaEventSourceMappingSelfManagedKafkaEventSourceConfig",
    jsii_struct_bases=[],
    name_mapping={"consumer_group_id": "consumerGroupId"},
)
class LambdaEventSourceMappingSelfManagedKafkaEventSourceConfig:
    def __init__(
        self,
        *,
        consumer_group_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param consumer_group_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#consumer_group_id LambdaEventSourceMapping#consumer_group_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa505b390fb0e037324eab38812f93027e92654c4d57d26adc8549f957da989b)
            check_type(argname="argument consumer_group_id", value=consumer_group_id, expected_type=type_hints["consumer_group_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if consumer_group_id is not None:
            self._values["consumer_group_id"] = consumer_group_id

    @builtins.property
    def consumer_group_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#consumer_group_id LambdaEventSourceMapping#consumer_group_id}.'''
        result = self._values.get("consumer_group_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LambdaEventSourceMappingSelfManagedKafkaEventSourceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LambdaEventSourceMappingSelfManagedKafkaEventSourceConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lambdaEventSourceMapping.LambdaEventSourceMappingSelfManagedKafkaEventSourceConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5ccba314f9bd149e19fe353262c5f70b7be198b0db9b59e4ed6c52c01830cefc)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetConsumerGroupId")
    def reset_consumer_group_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConsumerGroupId", []))

    @builtins.property
    @jsii.member(jsii_name="consumerGroupIdInput")
    def consumer_group_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "consumerGroupIdInput"))

    @builtins.property
    @jsii.member(jsii_name="consumerGroupId")
    def consumer_group_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "consumerGroupId"))

    @consumer_group_id.setter
    def consumer_group_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a06cd570e90c63651d3ab294350704dbcbe66725ddc75dca68044c92f4c18a78)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "consumerGroupId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LambdaEventSourceMappingSelfManagedKafkaEventSourceConfig]:
        return typing.cast(typing.Optional[LambdaEventSourceMappingSelfManagedKafkaEventSourceConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LambdaEventSourceMappingSelfManagedKafkaEventSourceConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a3589954d27c428aeb76206b760daeda181dcd8f0bcbe5a0e635f4fd1487107)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.lambdaEventSourceMapping.LambdaEventSourceMappingSourceAccessConfiguration",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "uri": "uri"},
)
class LambdaEventSourceMappingSourceAccessConfiguration:
    def __init__(self, *, type: builtins.str, uri: builtins.str) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#type LambdaEventSourceMapping#type}.
        :param uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#uri LambdaEventSourceMapping#uri}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__881325acfdcd0bc15127f624f7ecf3aebc5ea812dc0272ba11f45471cd1291f0)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument uri", value=uri, expected_type=type_hints["uri"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
            "uri": uri,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#type LambdaEventSourceMapping#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def uri(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping#uri LambdaEventSourceMapping#uri}.'''
        result = self._values.get("uri")
        assert result is not None, "Required property 'uri' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LambdaEventSourceMappingSourceAccessConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LambdaEventSourceMappingSourceAccessConfigurationList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lambdaEventSourceMapping.LambdaEventSourceMappingSourceAccessConfigurationList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6a46bd058e0b7441f41c78a7d7089db054079dab3e029ae1716b770f88e14739)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LambdaEventSourceMappingSourceAccessConfigurationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20c41148477c28773d9704f297d8a6f11df93b5d54b04c21fae0b65d790eca85)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LambdaEventSourceMappingSourceAccessConfigurationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79ab7c46d3a1c542d197775e4afcdd0ee328c21925c3872715bad70c8b000b1f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__754a82d20035b7c7acda25242321b520574a91d474f290b3b88688478478cdbc)
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
            type_hints = typing.get_type_hints(_typecheckingstub__efca5d475481db7ebc91bf86d1b656c1716fcc871135da3fd2a0989d3d15a629)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LambdaEventSourceMappingSourceAccessConfiguration]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LambdaEventSourceMappingSourceAccessConfiguration]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LambdaEventSourceMappingSourceAccessConfiguration]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a71167b39f86eec6d083d482625a9cf6482ef156cb4d55d4860bd32d36d7de09)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LambdaEventSourceMappingSourceAccessConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lambdaEventSourceMapping.LambdaEventSourceMappingSourceAccessConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4386ac72adf48bc701f7893f16ff4cce6e78f13ebb1ac051fddfa77ba8e2561c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="uriInput")
    def uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "uriInput"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4dcbb0d28188d1efee117fcac0b7e18ffd86ec20fa47769ab047958217f25500)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="uri")
    def uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uri"))

    @uri.setter
    def uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__594e7752d16b8f76a3ffd42e064a48263097902d66ee253617d897be93360e41)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "uri", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LambdaEventSourceMappingSourceAccessConfiguration, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LambdaEventSourceMappingSourceAccessConfiguration, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LambdaEventSourceMappingSourceAccessConfiguration, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7ad8c66d2988ea836d4ad9cff202346dd8572011909979bbc516b1e3a4a8968)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "LambdaEventSourceMapping",
    "LambdaEventSourceMappingAmazonManagedKafkaEventSourceConfig",
    "LambdaEventSourceMappingAmazonManagedKafkaEventSourceConfigOutputReference",
    "LambdaEventSourceMappingConfig",
    "LambdaEventSourceMappingDestinationConfig",
    "LambdaEventSourceMappingDestinationConfigOnFailure",
    "LambdaEventSourceMappingDestinationConfigOnFailureOutputReference",
    "LambdaEventSourceMappingDestinationConfigOutputReference",
    "LambdaEventSourceMappingFilterCriteria",
    "LambdaEventSourceMappingFilterCriteriaFilter",
    "LambdaEventSourceMappingFilterCriteriaFilterList",
    "LambdaEventSourceMappingFilterCriteriaFilterOutputReference",
    "LambdaEventSourceMappingFilterCriteriaOutputReference",
    "LambdaEventSourceMappingSelfManagedEventSource",
    "LambdaEventSourceMappingSelfManagedEventSourceOutputReference",
    "LambdaEventSourceMappingSelfManagedKafkaEventSourceConfig",
    "LambdaEventSourceMappingSelfManagedKafkaEventSourceConfigOutputReference",
    "LambdaEventSourceMappingSourceAccessConfiguration",
    "LambdaEventSourceMappingSourceAccessConfigurationList",
    "LambdaEventSourceMappingSourceAccessConfigurationOutputReference",
]

publication.publish()

def _typecheckingstub__203b8d75a05a96a2c4242d28dbea347c739933bb98ad80e2101ea3ff8b7039c4(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    function_name: builtins.str,
    amazon_managed_kafka_event_source_config: typing.Optional[typing.Union[LambdaEventSourceMappingAmazonManagedKafkaEventSourceConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    batch_size: typing.Optional[jsii.Number] = None,
    bisect_batch_on_function_error: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    destination_config: typing.Optional[typing.Union[LambdaEventSourceMappingDestinationConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    event_source_arn: typing.Optional[builtins.str] = None,
    filter_criteria: typing.Optional[typing.Union[LambdaEventSourceMappingFilterCriteria, typing.Dict[builtins.str, typing.Any]]] = None,
    function_response_types: typing.Optional[typing.Sequence[builtins.str]] = None,
    id: typing.Optional[builtins.str] = None,
    maximum_batching_window_in_seconds: typing.Optional[jsii.Number] = None,
    maximum_record_age_in_seconds: typing.Optional[jsii.Number] = None,
    maximum_retry_attempts: typing.Optional[jsii.Number] = None,
    parallelization_factor: typing.Optional[jsii.Number] = None,
    queues: typing.Optional[typing.Sequence[builtins.str]] = None,
    self_managed_event_source: typing.Optional[typing.Union[LambdaEventSourceMappingSelfManagedEventSource, typing.Dict[builtins.str, typing.Any]]] = None,
    self_managed_kafka_event_source_config: typing.Optional[typing.Union[LambdaEventSourceMappingSelfManagedKafkaEventSourceConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    source_access_configuration: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LambdaEventSourceMappingSourceAccessConfiguration, typing.Dict[builtins.str, typing.Any]]]]] = None,
    starting_position: typing.Optional[builtins.str] = None,
    starting_position_timestamp: typing.Optional[builtins.str] = None,
    topics: typing.Optional[typing.Sequence[builtins.str]] = None,
    tumbling_window_in_seconds: typing.Optional[jsii.Number] = None,
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

def _typecheckingstub__17c8f73187df18c61107666016d9659f710f905cad98f1b5ee1210db29d31a72(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LambdaEventSourceMappingSourceAccessConfiguration, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8520944f0bf5d6e18e5b4566b1f9a5b666d00bb167cc43d3ee57c7c2aa39cb1(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34d9d1ddcca1c7e8ef3af903886f6c4a09bf1258feea577aba1f9c6fe26f21ab(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__550f64f8e86c762a03ee244ddcba44b25706e6df013825d2a47f9999052a52ef(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5afb31ea0875d01ca338596859f936c4cce5a50e79b5f9347edc289d3e9e3753(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91beb63822fbf57ee9880dfb3f0a3eed84eea81d76fbf786bf2e04609c8ab505(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__195b395dcf05e5f9fe519bd52be8520bfd7f8b0774b0739a671a125c6bc8bc01(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3587eb25bd82b25459b134bf5d20aaa69d7d5091d37be36d4d7988cf9bf8a1d0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc3c5ba81566732e36c97a6bf20729a951f8364fe40108592d05024912deb4b4(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34eed8bedc85805551addacc6fbdec630a5cc9cb838bf4aed54d14113b9750ff(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1a76e83ebabc6c8bc958a08b7600bb80b6b4d5ef210705a1e6da9ca82598615(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c58096ce3a9c00470502271cf2bcb4abebc0da6c78b5dca5b94c2d74abc8e625(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7496e9672cd50a12f9a69abd3556b053de3b3aa9f4e2ae18d70c6de0194058ed(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8cec97eaa120b9f0456e524d79d328b22e50e5b0f408720ac2c8c6a34d8c87ff(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__493a0b806be9bc521e85e9520abcc695263ca309412b0eccdeadd58bd4750618(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ddef2a317ff13a8725be2cfd3aacb87b85662abff6f63f48493da7a382121e2b(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2feae161b08bb6867debd52ebeb495389fc7742c8ea95e6e54b78fc406eba625(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5fb52f35a99b0d88279780edbe242530191c24c0c93c639076b58aa82b31478b(
    *,
    consumer_group_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7a61dc3bf12cfd509aed52660eb7ba4ecd0b471a1e2eaefb236cc7260f581e1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5fdbcd5f18d386fb6e9761f897239294b3409c5f9c451a728dff25cc2cfb9a16(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3004ad524f0999131eac6a5e837034a4d70a57660ccb3b7d7737ba0a4027724(
    value: typing.Optional[LambdaEventSourceMappingAmazonManagedKafkaEventSourceConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35bc74599b1dfb4ad7fb3e074996f03fad6314252ee4bddb42f9e4ac5e464a44(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    function_name: builtins.str,
    amazon_managed_kafka_event_source_config: typing.Optional[typing.Union[LambdaEventSourceMappingAmazonManagedKafkaEventSourceConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    batch_size: typing.Optional[jsii.Number] = None,
    bisect_batch_on_function_error: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    destination_config: typing.Optional[typing.Union[LambdaEventSourceMappingDestinationConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    event_source_arn: typing.Optional[builtins.str] = None,
    filter_criteria: typing.Optional[typing.Union[LambdaEventSourceMappingFilterCriteria, typing.Dict[builtins.str, typing.Any]]] = None,
    function_response_types: typing.Optional[typing.Sequence[builtins.str]] = None,
    id: typing.Optional[builtins.str] = None,
    maximum_batching_window_in_seconds: typing.Optional[jsii.Number] = None,
    maximum_record_age_in_seconds: typing.Optional[jsii.Number] = None,
    maximum_retry_attempts: typing.Optional[jsii.Number] = None,
    parallelization_factor: typing.Optional[jsii.Number] = None,
    queues: typing.Optional[typing.Sequence[builtins.str]] = None,
    self_managed_event_source: typing.Optional[typing.Union[LambdaEventSourceMappingSelfManagedEventSource, typing.Dict[builtins.str, typing.Any]]] = None,
    self_managed_kafka_event_source_config: typing.Optional[typing.Union[LambdaEventSourceMappingSelfManagedKafkaEventSourceConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    source_access_configuration: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LambdaEventSourceMappingSourceAccessConfiguration, typing.Dict[builtins.str, typing.Any]]]]] = None,
    starting_position: typing.Optional[builtins.str] = None,
    starting_position_timestamp: typing.Optional[builtins.str] = None,
    topics: typing.Optional[typing.Sequence[builtins.str]] = None,
    tumbling_window_in_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__351557df9005a60dbc4b9b0844b31f80e4666e6dc81cd7637b98c359ef37afac(
    *,
    on_failure: typing.Optional[typing.Union[LambdaEventSourceMappingDestinationConfigOnFailure, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e50c0629fe98d7df8b70c0b62d5e4814393b01b1f9fb0a7b7c33820029ae95af(
    *,
    destination_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66400dc8954782bbfbcce739277d7b1bf9c4ad1d5bf596024914c969e7a98b5b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4bdbcf1971d8b4c2de25de04928f6b3572fdad930c63fb50fea88b7e7e6c0c78(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1077694f7bf7e5840102e82235260f9ffdf30cbc1bec0c2877166d36b400257e(
    value: typing.Optional[LambdaEventSourceMappingDestinationConfigOnFailure],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__863adec7399ae46f58d06ca7ca8bb0b89413ae10e101cea15999d5f1ad811843(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23713dc6accdb9f94d1d5c72581895bee581a933e313dae1aa06a8952636ed83(
    value: typing.Optional[LambdaEventSourceMappingDestinationConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f665599571598a38b04c86a24ab3a38d979359cee4ea692e3afa91b5b02bee47(
    *,
    filter: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LambdaEventSourceMappingFilterCriteriaFilter, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5df98b4c69bd95f431c20f0a8e5cdd807e32dde56cf2e8b42b971b324314f0a(
    *,
    pattern: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca2407b2b6c60e5061e18e946a5751a975bb921ec22240271dac644b44c1c636(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42dc6971b5c85999b54de9cce5fcad65dbcc20aa91d9840b2e9c59f2da6b3b3d(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__242020642b007fc5e5c6e3ef6e51aa2a86deffb3e67fcf4ce6d99732695e1774(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f72a08b00d0fc5a74d2d5c781a004e562583b3f5a60dd1f00b7bf3ddacad209(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7646fae3222e66f4184ea9a1a54258cfead2d5bbc5e7f28ee180060ee10eff46(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f4d7915effcaf4c78906f6b03f49430e09a145b37867bf9b17989411987bb55(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LambdaEventSourceMappingFilterCriteriaFilter]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98b71223d9c08cfe59a4dda8c35c323fc7014d64443c5e3ff520e1a9a95f5d5c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3440b6ea48c604bc9767c9c9e4e7318519cd980611f7f5a535fd122a9bd0070(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__211fdd285ab10aaf1c8e3f0aa09c9e329e4ec2a61c1141b34a95737563958dce(
    value: typing.Optional[typing.Union[LambdaEventSourceMappingFilterCriteriaFilter, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__669d3d61b4856d241c03c94f03f4b26e156f48f26d8d22b7ec0225724012f383(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8fa11a25516a08a4686fe48472234974d05f5a90c151f64ef2b632818091449(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LambdaEventSourceMappingFilterCriteriaFilter, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0fc3cfaee6fbc9f0f11b5045b4dd6dc53e9fbc1ec91f2b7e96201e57bdc3a39b(
    value: typing.Optional[LambdaEventSourceMappingFilterCriteria],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bfb8e77b47ed8b8141654b07fea3e44faec686de15c86fee133fd280a3dc4fc1(
    *,
    endpoints: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51b06c31a47e3773fc3ca009ed996a2cabeaf61040f872fe61c31e8eb924b16c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0187b7c3ae02dc9785c6d4b9b67a1a79077f1c762aad0896d3c7ff5b09664d82(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0ee9f4d9fe8b607a9f3270a8c57eb27a5d7fe742b48f23989175158351c201f(
    value: typing.Optional[LambdaEventSourceMappingSelfManagedEventSource],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa505b390fb0e037324eab38812f93027e92654c4d57d26adc8549f957da989b(
    *,
    consumer_group_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ccba314f9bd149e19fe353262c5f70b7be198b0db9b59e4ed6c52c01830cefc(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a06cd570e90c63651d3ab294350704dbcbe66725ddc75dca68044c92f4c18a78(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a3589954d27c428aeb76206b760daeda181dcd8f0bcbe5a0e635f4fd1487107(
    value: typing.Optional[LambdaEventSourceMappingSelfManagedKafkaEventSourceConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__881325acfdcd0bc15127f624f7ecf3aebc5ea812dc0272ba11f45471cd1291f0(
    *,
    type: builtins.str,
    uri: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a46bd058e0b7441f41c78a7d7089db054079dab3e029ae1716b770f88e14739(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20c41148477c28773d9704f297d8a6f11df93b5d54b04c21fae0b65d790eca85(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79ab7c46d3a1c542d197775e4afcdd0ee328c21925c3872715bad70c8b000b1f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__754a82d20035b7c7acda25242321b520574a91d474f290b3b88688478478cdbc(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__efca5d475481db7ebc91bf86d1b656c1716fcc871135da3fd2a0989d3d15a629(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a71167b39f86eec6d083d482625a9cf6482ef156cb4d55d4860bd32d36d7de09(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LambdaEventSourceMappingSourceAccessConfiguration]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4386ac72adf48bc701f7893f16ff4cce6e78f13ebb1ac051fddfa77ba8e2561c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4dcbb0d28188d1efee117fcac0b7e18ffd86ec20fa47769ab047958217f25500(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__594e7752d16b8f76a3ffd42e064a48263097902d66ee253617d897be93360e41(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7ad8c66d2988ea836d4ad9cff202346dd8572011909979bbc516b1e3a4a8968(
    value: typing.Optional[typing.Union[LambdaEventSourceMappingSourceAccessConfiguration, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
