'''
# `aws_lex_bot`

Refer to the Terraform Registory for docs: [`aws_lex_bot`](https://www.terraform.io/docs/providers/aws/r/lex_bot).
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


class LexBot(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lexBot.LexBot",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/lex_bot aws_lex_bot}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        abort_statement: typing.Union["LexBotAbortStatement", typing.Dict[builtins.str, typing.Any]],
        child_directed: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        intent: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LexBotIntent", typing.Dict[builtins.str, typing.Any]]]],
        name: builtins.str,
        clarification_prompt: typing.Optional[typing.Union["LexBotClarificationPrompt", typing.Dict[builtins.str, typing.Any]]] = None,
        create_version: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        description: typing.Optional[builtins.str] = None,
        detect_sentiment: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_model_improvements: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        idle_session_ttl_in_seconds: typing.Optional[jsii.Number] = None,
        locale: typing.Optional[builtins.str] = None,
        nlu_intent_confidence_threshold: typing.Optional[jsii.Number] = None,
        process_behavior: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["LexBotTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        voice_id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/lex_bot aws_lex_bot} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param abort_statement: abort_statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#abort_statement LexBot#abort_statement}
        :param child_directed: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#child_directed LexBot#child_directed}.
        :param intent: intent block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#intent LexBot#intent}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#name LexBot#name}.
        :param clarification_prompt: clarification_prompt block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#clarification_prompt LexBot#clarification_prompt}
        :param create_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#create_version LexBot#create_version}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#description LexBot#description}.
        :param detect_sentiment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#detect_sentiment LexBot#detect_sentiment}.
        :param enable_model_improvements: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#enable_model_improvements LexBot#enable_model_improvements}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#id LexBot#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param idle_session_ttl_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#idle_session_ttl_in_seconds LexBot#idle_session_ttl_in_seconds}.
        :param locale: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#locale LexBot#locale}.
        :param nlu_intent_confidence_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#nlu_intent_confidence_threshold LexBot#nlu_intent_confidence_threshold}.
        :param process_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#process_behavior LexBot#process_behavior}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#timeouts LexBot#timeouts}
        :param voice_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#voice_id LexBot#voice_id}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73aac88fe822dc8e492546e2aff1f59e83e4a51ad6748b80a83355fc320fedb6)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = LexBotConfig(
            abort_statement=abort_statement,
            child_directed=child_directed,
            intent=intent,
            name=name,
            clarification_prompt=clarification_prompt,
            create_version=create_version,
            description=description,
            detect_sentiment=detect_sentiment,
            enable_model_improvements=enable_model_improvements,
            id=id,
            idle_session_ttl_in_seconds=idle_session_ttl_in_seconds,
            locale=locale,
            nlu_intent_confidence_threshold=nlu_intent_confidence_threshold,
            process_behavior=process_behavior,
            timeouts=timeouts,
            voice_id=voice_id,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAbortStatement")
    def put_abort_statement(
        self,
        *,
        message: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LexBotAbortStatementMessage", typing.Dict[builtins.str, typing.Any]]]],
        response_card: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param message: message block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#message LexBot#message}
        :param response_card: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#response_card LexBot#response_card}.
        '''
        value = LexBotAbortStatement(message=message, response_card=response_card)

        return typing.cast(None, jsii.invoke(self, "putAbortStatement", [value]))

    @jsii.member(jsii_name="putClarificationPrompt")
    def put_clarification_prompt(
        self,
        *,
        max_attempts: jsii.Number,
        message: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LexBotClarificationPromptMessage", typing.Dict[builtins.str, typing.Any]]]],
        response_card: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param max_attempts: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#max_attempts LexBot#max_attempts}.
        :param message: message block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#message LexBot#message}
        :param response_card: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#response_card LexBot#response_card}.
        '''
        value = LexBotClarificationPrompt(
            max_attempts=max_attempts, message=message, response_card=response_card
        )

        return typing.cast(None, jsii.invoke(self, "putClarificationPrompt", [value]))

    @jsii.member(jsii_name="putIntent")
    def put_intent(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LexBotIntent", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d862f00fb7aced13817d3adf22603cf0f30b53856dd9428858c5488522455fd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putIntent", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#create LexBot#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#delete LexBot#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#update LexBot#update}.
        '''
        value = LexBotTimeouts(create=create, delete=delete, update=update)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetClarificationPrompt")
    def reset_clarification_prompt(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClarificationPrompt", []))

    @jsii.member(jsii_name="resetCreateVersion")
    def reset_create_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreateVersion", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetDetectSentiment")
    def reset_detect_sentiment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDetectSentiment", []))

    @jsii.member(jsii_name="resetEnableModelImprovements")
    def reset_enable_model_improvements(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableModelImprovements", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIdleSessionTtlInSeconds")
    def reset_idle_session_ttl_in_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdleSessionTtlInSeconds", []))

    @jsii.member(jsii_name="resetLocale")
    def reset_locale(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocale", []))

    @jsii.member(jsii_name="resetNluIntentConfidenceThreshold")
    def reset_nlu_intent_confidence_threshold(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNluIntentConfidenceThreshold", []))

    @jsii.member(jsii_name="resetProcessBehavior")
    def reset_process_behavior(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProcessBehavior", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetVoiceId")
    def reset_voice_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVoiceId", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="abortStatement")
    def abort_statement(self) -> "LexBotAbortStatementOutputReference":
        return typing.cast("LexBotAbortStatementOutputReference", jsii.get(self, "abortStatement"))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="checksum")
    def checksum(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "checksum"))

    @builtins.property
    @jsii.member(jsii_name="clarificationPrompt")
    def clarification_prompt(self) -> "LexBotClarificationPromptOutputReference":
        return typing.cast("LexBotClarificationPromptOutputReference", jsii.get(self, "clarificationPrompt"))

    @builtins.property
    @jsii.member(jsii_name="createdDate")
    def created_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdDate"))

    @builtins.property
    @jsii.member(jsii_name="failureReason")
    def failure_reason(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "failureReason"))

    @builtins.property
    @jsii.member(jsii_name="intent")
    def intent(self) -> "LexBotIntentList":
        return typing.cast("LexBotIntentList", jsii.get(self, "intent"))

    @builtins.property
    @jsii.member(jsii_name="lastUpdatedDate")
    def last_updated_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastUpdatedDate"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "LexBotTimeoutsOutputReference":
        return typing.cast("LexBotTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @builtins.property
    @jsii.member(jsii_name="abortStatementInput")
    def abort_statement_input(self) -> typing.Optional["LexBotAbortStatement"]:
        return typing.cast(typing.Optional["LexBotAbortStatement"], jsii.get(self, "abortStatementInput"))

    @builtins.property
    @jsii.member(jsii_name="childDirectedInput")
    def child_directed_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "childDirectedInput"))

    @builtins.property
    @jsii.member(jsii_name="clarificationPromptInput")
    def clarification_prompt_input(
        self,
    ) -> typing.Optional["LexBotClarificationPrompt"]:
        return typing.cast(typing.Optional["LexBotClarificationPrompt"], jsii.get(self, "clarificationPromptInput"))

    @builtins.property
    @jsii.member(jsii_name="createVersionInput")
    def create_version_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "createVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="detectSentimentInput")
    def detect_sentiment_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "detectSentimentInput"))

    @builtins.property
    @jsii.member(jsii_name="enableModelImprovementsInput")
    def enable_model_improvements_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableModelImprovementsInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="idleSessionTtlInSecondsInput")
    def idle_session_ttl_in_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "idleSessionTtlInSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="intentInput")
    def intent_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LexBotIntent"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LexBotIntent"]]], jsii.get(self, "intentInput"))

    @builtins.property
    @jsii.member(jsii_name="localeInput")
    def locale_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "localeInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="nluIntentConfidenceThresholdInput")
    def nlu_intent_confidence_threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "nluIntentConfidenceThresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="processBehaviorInput")
    def process_behavior_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "processBehaviorInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["LexBotTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["LexBotTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="voiceIdInput")
    def voice_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "voiceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="childDirected")
    def child_directed(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "childDirected"))

    @child_directed.setter
    def child_directed(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb1d374fd5d7bf02bf249ce6cef3d4d57eed0f1eda99efe630e181857345d523)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "childDirected", value)

    @builtins.property
    @jsii.member(jsii_name="createVersion")
    def create_version(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "createVersion"))

    @create_version.setter
    def create_version(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0cdc1c448f6064b77d801087794e6b4796e80eb72c5337866157ac61639980cb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "createVersion", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0b88f0d528683c151012aada4ef60ecfc7647e5be7214750b15a5903bb5af97)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="detectSentiment")
    def detect_sentiment(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "detectSentiment"))

    @detect_sentiment.setter
    def detect_sentiment(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de19c8f404a3dff10bac55543afe048c86ed6d5750fb1cc926487cbcdde974a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "detectSentiment", value)

    @builtins.property
    @jsii.member(jsii_name="enableModelImprovements")
    def enable_model_improvements(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enableModelImprovements"))

    @enable_model_improvements.setter
    def enable_model_improvements(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6da1874a077b504c479507c6dcc1fd9dd67c985dc3618ba253d2848d5c7ca1b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableModelImprovements", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b91bf29fdd767225e8b5c47d773741847bacc4707f6b27576bb6813dc431da9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="idleSessionTtlInSeconds")
    def idle_session_ttl_in_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "idleSessionTtlInSeconds"))

    @idle_session_ttl_in_seconds.setter
    def idle_session_ttl_in_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49748c59a9446e64d7d825b7e02e4e9d94f273d1feabd2bb6951debf71e94e7d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "idleSessionTtlInSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="locale")
    def locale(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "locale"))

    @locale.setter
    def locale(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fea75e627ef32074423ec954fc379418de8a256a2b4b3283a80fa891cf3794b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "locale", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc21ed8e3f93befcbeae6e6bd3ef50a8db2f2dbba40851f355a080f7673801c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="nluIntentConfidenceThreshold")
    def nlu_intent_confidence_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "nluIntentConfidenceThreshold"))

    @nlu_intent_confidence_threshold.setter
    def nlu_intent_confidence_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43fad0850e5e0ba3fa6311e1e23acf55c8b7742b408f15887fc5282ea14ba9d4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nluIntentConfidenceThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="processBehavior")
    def process_behavior(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "processBehavior"))

    @process_behavior.setter
    def process_behavior(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4ed194cb67a54d4e7df3f807dd855addc3e5425ec75d65fed18b9d281a72bc9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "processBehavior", value)

    @builtins.property
    @jsii.member(jsii_name="voiceId")
    def voice_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "voiceId"))

    @voice_id.setter
    def voice_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b1b3d0ef1de364dcb6af9abfec3410428103c682f29751a06476480cf0c3cf9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "voiceId", value)


@jsii.data_type(
    jsii_type="aws.lexBot.LexBotAbortStatement",
    jsii_struct_bases=[],
    name_mapping={"message": "message", "response_card": "responseCard"},
)
class LexBotAbortStatement:
    def __init__(
        self,
        *,
        message: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LexBotAbortStatementMessage", typing.Dict[builtins.str, typing.Any]]]],
        response_card: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param message: message block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#message LexBot#message}
        :param response_card: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#response_card LexBot#response_card}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a8fcf461203f127b03073019221ddb3c4112423e65aa64376aaea7d9d255b467)
            check_type(argname="argument message", value=message, expected_type=type_hints["message"])
            check_type(argname="argument response_card", value=response_card, expected_type=type_hints["response_card"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "message": message,
        }
        if response_card is not None:
            self._values["response_card"] = response_card

    @builtins.property
    def message(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LexBotAbortStatementMessage"]]:
        '''message block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#message LexBot#message}
        '''
        result = self._values.get("message")
        assert result is not None, "Required property 'message' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LexBotAbortStatementMessage"]], result)

    @builtins.property
    def response_card(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#response_card LexBot#response_card}.'''
        result = self._values.get("response_card")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LexBotAbortStatement(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.lexBot.LexBotAbortStatementMessage",
    jsii_struct_bases=[],
    name_mapping={
        "content": "content",
        "content_type": "contentType",
        "group_number": "groupNumber",
    },
)
class LexBotAbortStatementMessage:
    def __init__(
        self,
        *,
        content: builtins.str,
        content_type: builtins.str,
        group_number: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param content: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#content LexBot#content}.
        :param content_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#content_type LexBot#content_type}.
        :param group_number: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#group_number LexBot#group_number}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__362ae37c94eb560d401bfaf3c56156f5c7759a33e52d2a11c3330709f5b7b50a)
            check_type(argname="argument content", value=content, expected_type=type_hints["content"])
            check_type(argname="argument content_type", value=content_type, expected_type=type_hints["content_type"])
            check_type(argname="argument group_number", value=group_number, expected_type=type_hints["group_number"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "content": content,
            "content_type": content_type,
        }
        if group_number is not None:
            self._values["group_number"] = group_number

    @builtins.property
    def content(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#content LexBot#content}.'''
        result = self._values.get("content")
        assert result is not None, "Required property 'content' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def content_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#content_type LexBot#content_type}.'''
        result = self._values.get("content_type")
        assert result is not None, "Required property 'content_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def group_number(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#group_number LexBot#group_number}.'''
        result = self._values.get("group_number")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LexBotAbortStatementMessage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LexBotAbortStatementMessageList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lexBot.LexBotAbortStatementMessageList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__dd04452b1d91db2f94833895845c5ba90f22fe00840f56509ac0cfde004f92fe)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "LexBotAbortStatementMessageOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e78c1d8b62b0bf5524d556fbe26cec6ca2d4277a8c0a8e314b50ec90c5fd5851)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LexBotAbortStatementMessageOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__86c21338b15ae150900971c7753cded94d59cac86bdc05595af51d28f407d8d1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__15ca8b9288cb13bb3635a1ffc429aa5754f00f57cfbc373ad5d337c332d4f5f2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__73ce648616f63b54ccf49fcd62afe28415aa1bb9eb3e7720c0345b8f734273a4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LexBotAbortStatementMessage]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LexBotAbortStatementMessage]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LexBotAbortStatementMessage]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cebc90ec4aab739ca634b631fa78e57ed5a294cda28caea2e70559319282ffe8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LexBotAbortStatementMessageOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lexBot.LexBotAbortStatementMessageOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2dbeee8e6f1f5c13a073884040702c709147221b3587cbbdacf3a5e49bc54402)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetGroupNumber")
    def reset_group_number(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroupNumber", []))

    @builtins.property
    @jsii.member(jsii_name="contentInput")
    def content_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentInput"))

    @builtins.property
    @jsii.member(jsii_name="contentTypeInput")
    def content_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="groupNumberInput")
    def group_number_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "groupNumberInput"))

    @builtins.property
    @jsii.member(jsii_name="content")
    def content(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "content"))

    @content.setter
    def content(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dcd8efa365a40b6b56c4b1435001e81930d47085402a3121c7251c5b27a7634b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "content", value)

    @builtins.property
    @jsii.member(jsii_name="contentType")
    def content_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentType"))

    @content_type.setter
    def content_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3696ca2e2bc28d82527617a88f984ad621f178311a3677e1b78baf44099722fb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentType", value)

    @builtins.property
    @jsii.member(jsii_name="groupNumber")
    def group_number(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "groupNumber"))

    @group_number.setter
    def group_number(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b26a817f7bee67dcdf85738c5c6e24ccfd569a92055f6f2939ad5167dbd346d9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupNumber", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LexBotAbortStatementMessage, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LexBotAbortStatementMessage, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LexBotAbortStatementMessage, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41d4ba4d5023900b784fd2ae3507c758e6dd4d436b964224af5d9783f64f047e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LexBotAbortStatementOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lexBot.LexBotAbortStatementOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__abf6709f61e21c2d695c246ac5682d6b92fafda9480f256d817bb2d69a0e6e09)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMessage")
    def put_message(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LexBotAbortStatementMessage, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__10c0675e32d0646397d57686fba1057ad3166bbfc0103bd67faf6c20dc62e45d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMessage", [value]))

    @jsii.member(jsii_name="resetResponseCard")
    def reset_response_card(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResponseCard", []))

    @builtins.property
    @jsii.member(jsii_name="message")
    def message(self) -> LexBotAbortStatementMessageList:
        return typing.cast(LexBotAbortStatementMessageList, jsii.get(self, "message"))

    @builtins.property
    @jsii.member(jsii_name="messageInput")
    def message_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LexBotAbortStatementMessage]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LexBotAbortStatementMessage]]], jsii.get(self, "messageInput"))

    @builtins.property
    @jsii.member(jsii_name="responseCardInput")
    def response_card_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "responseCardInput"))

    @builtins.property
    @jsii.member(jsii_name="responseCard")
    def response_card(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "responseCard"))

    @response_card.setter
    def response_card(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41afa1c9982934fa0554062767bae925e14ca7a0aaa04a6d82d00514cc0a386b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "responseCard", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LexBotAbortStatement]:
        return typing.cast(typing.Optional[LexBotAbortStatement], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[LexBotAbortStatement]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb8620121bae580e81b6d770c5923dfb18521767c5d4130cd7ff7f1e31675fee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.lexBot.LexBotClarificationPrompt",
    jsii_struct_bases=[],
    name_mapping={
        "max_attempts": "maxAttempts",
        "message": "message",
        "response_card": "responseCard",
    },
)
class LexBotClarificationPrompt:
    def __init__(
        self,
        *,
        max_attempts: jsii.Number,
        message: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LexBotClarificationPromptMessage", typing.Dict[builtins.str, typing.Any]]]],
        response_card: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param max_attempts: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#max_attempts LexBot#max_attempts}.
        :param message: message block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#message LexBot#message}
        :param response_card: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#response_card LexBot#response_card}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dbcbc2ddbf713ff62ef67f2ed689aa159056160e110256d5500c2fceb8e378ae)
            check_type(argname="argument max_attempts", value=max_attempts, expected_type=type_hints["max_attempts"])
            check_type(argname="argument message", value=message, expected_type=type_hints["message"])
            check_type(argname="argument response_card", value=response_card, expected_type=type_hints["response_card"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "max_attempts": max_attempts,
            "message": message,
        }
        if response_card is not None:
            self._values["response_card"] = response_card

    @builtins.property
    def max_attempts(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#max_attempts LexBot#max_attempts}.'''
        result = self._values.get("max_attempts")
        assert result is not None, "Required property 'max_attempts' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def message(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LexBotClarificationPromptMessage"]]:
        '''message block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#message LexBot#message}
        '''
        result = self._values.get("message")
        assert result is not None, "Required property 'message' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LexBotClarificationPromptMessage"]], result)

    @builtins.property
    def response_card(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#response_card LexBot#response_card}.'''
        result = self._values.get("response_card")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LexBotClarificationPrompt(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.lexBot.LexBotClarificationPromptMessage",
    jsii_struct_bases=[],
    name_mapping={
        "content": "content",
        "content_type": "contentType",
        "group_number": "groupNumber",
    },
)
class LexBotClarificationPromptMessage:
    def __init__(
        self,
        *,
        content: builtins.str,
        content_type: builtins.str,
        group_number: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param content: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#content LexBot#content}.
        :param content_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#content_type LexBot#content_type}.
        :param group_number: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#group_number LexBot#group_number}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a3b4d110efa41458fd97c42c9f60e3d0c4c01f532574935bb935e1978319acac)
            check_type(argname="argument content", value=content, expected_type=type_hints["content"])
            check_type(argname="argument content_type", value=content_type, expected_type=type_hints["content_type"])
            check_type(argname="argument group_number", value=group_number, expected_type=type_hints["group_number"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "content": content,
            "content_type": content_type,
        }
        if group_number is not None:
            self._values["group_number"] = group_number

    @builtins.property
    def content(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#content LexBot#content}.'''
        result = self._values.get("content")
        assert result is not None, "Required property 'content' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def content_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#content_type LexBot#content_type}.'''
        result = self._values.get("content_type")
        assert result is not None, "Required property 'content_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def group_number(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#group_number LexBot#group_number}.'''
        result = self._values.get("group_number")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LexBotClarificationPromptMessage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LexBotClarificationPromptMessageList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lexBot.LexBotClarificationPromptMessageList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ad60363864744cd532cc56015144d91fed6c9c2708e8f668e5c4eed3fca2da0b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LexBotClarificationPromptMessageOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__807b44eae2d5cc7b16c3a32bfc589165fa17489c3ba18514b39aabb83f116322)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LexBotClarificationPromptMessageOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a112b8a33f3614c1b4672e72ebe98c534e8672166cd0db965cd8d6bc23eae96)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ac185d76d4893e5de33546fc8fa85df8559dc302598c302a0ae8bc30f2be8c9e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__04965188b6b1dc20ae3d0cf10094da1d2bb70824f9b51d27c80945657b57e970)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LexBotClarificationPromptMessage]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LexBotClarificationPromptMessage]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LexBotClarificationPromptMessage]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd5497cc3b9aa1a6d2fb904b1a026991691ccff3d92ef23a6bf957e6467eb00b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LexBotClarificationPromptMessageOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lexBot.LexBotClarificationPromptMessageOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__71447bf4b69686033d8b8d63319e3b11cd42bf6b0de988cd1fd95af1d3de3820)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetGroupNumber")
    def reset_group_number(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroupNumber", []))

    @builtins.property
    @jsii.member(jsii_name="contentInput")
    def content_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentInput"))

    @builtins.property
    @jsii.member(jsii_name="contentTypeInput")
    def content_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="groupNumberInput")
    def group_number_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "groupNumberInput"))

    @builtins.property
    @jsii.member(jsii_name="content")
    def content(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "content"))

    @content.setter
    def content(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd30ff563b547eb0d0fa489cee05901bed13d92179840c771c0035b45836c030)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "content", value)

    @builtins.property
    @jsii.member(jsii_name="contentType")
    def content_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentType"))

    @content_type.setter
    def content_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a98774859d0cfc18d2ed927e8a2b9228ed1496160e3932d4528a2bd3ea00a928)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentType", value)

    @builtins.property
    @jsii.member(jsii_name="groupNumber")
    def group_number(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "groupNumber"))

    @group_number.setter
    def group_number(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f4acbbd280e585eca887707f9a814c5d1dfab0ba96844b6c2ea45c844e0491f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupNumber", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LexBotClarificationPromptMessage, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LexBotClarificationPromptMessage, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LexBotClarificationPromptMessage, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9082c0bdc1e8b0b38f3885861d108acf5ee4c17e64b6de9ff03a417e80957a48)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LexBotClarificationPromptOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lexBot.LexBotClarificationPromptOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7b61c0f618439d8b2972d51b766e96c3f5dd077743cf4afd71fad31471445795)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMessage")
    def put_message(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LexBotClarificationPromptMessage, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eff8cd7c11ae9d9b95fc8798ae6cdba02544ba167bcc9b479b660095abc0ec26)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMessage", [value]))

    @jsii.member(jsii_name="resetResponseCard")
    def reset_response_card(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResponseCard", []))

    @builtins.property
    @jsii.member(jsii_name="message")
    def message(self) -> LexBotClarificationPromptMessageList:
        return typing.cast(LexBotClarificationPromptMessageList, jsii.get(self, "message"))

    @builtins.property
    @jsii.member(jsii_name="maxAttemptsInput")
    def max_attempts_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxAttemptsInput"))

    @builtins.property
    @jsii.member(jsii_name="messageInput")
    def message_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LexBotClarificationPromptMessage]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LexBotClarificationPromptMessage]]], jsii.get(self, "messageInput"))

    @builtins.property
    @jsii.member(jsii_name="responseCardInput")
    def response_card_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "responseCardInput"))

    @builtins.property
    @jsii.member(jsii_name="maxAttempts")
    def max_attempts(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxAttempts"))

    @max_attempts.setter
    def max_attempts(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ef9ce7e58a6449b85d136070da3ba42454d94843170385191542a9fddcfc42a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxAttempts", value)

    @builtins.property
    @jsii.member(jsii_name="responseCard")
    def response_card(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "responseCard"))

    @response_card.setter
    def response_card(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66f0eb50033b84c9e302494cc1a54496159cca3ab823fbe8f1725f935c046db5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "responseCard", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LexBotClarificationPrompt]:
        return typing.cast(typing.Optional[LexBotClarificationPrompt], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[LexBotClarificationPrompt]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b12cc9beb2ced0cd1cbfdbfdebef75edf21c215fcf1c247643ca8784a30cc70)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.lexBot.LexBotConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "abort_statement": "abortStatement",
        "child_directed": "childDirected",
        "intent": "intent",
        "name": "name",
        "clarification_prompt": "clarificationPrompt",
        "create_version": "createVersion",
        "description": "description",
        "detect_sentiment": "detectSentiment",
        "enable_model_improvements": "enableModelImprovements",
        "id": "id",
        "idle_session_ttl_in_seconds": "idleSessionTtlInSeconds",
        "locale": "locale",
        "nlu_intent_confidence_threshold": "nluIntentConfidenceThreshold",
        "process_behavior": "processBehavior",
        "timeouts": "timeouts",
        "voice_id": "voiceId",
    },
)
class LexBotConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        abort_statement: typing.Union[LexBotAbortStatement, typing.Dict[builtins.str, typing.Any]],
        child_directed: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        intent: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LexBotIntent", typing.Dict[builtins.str, typing.Any]]]],
        name: builtins.str,
        clarification_prompt: typing.Optional[typing.Union[LexBotClarificationPrompt, typing.Dict[builtins.str, typing.Any]]] = None,
        create_version: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        description: typing.Optional[builtins.str] = None,
        detect_sentiment: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_model_improvements: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        idle_session_ttl_in_seconds: typing.Optional[jsii.Number] = None,
        locale: typing.Optional[builtins.str] = None,
        nlu_intent_confidence_threshold: typing.Optional[jsii.Number] = None,
        process_behavior: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["LexBotTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        voice_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param abort_statement: abort_statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#abort_statement LexBot#abort_statement}
        :param child_directed: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#child_directed LexBot#child_directed}.
        :param intent: intent block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#intent LexBot#intent}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#name LexBot#name}.
        :param clarification_prompt: clarification_prompt block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#clarification_prompt LexBot#clarification_prompt}
        :param create_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#create_version LexBot#create_version}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#description LexBot#description}.
        :param detect_sentiment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#detect_sentiment LexBot#detect_sentiment}.
        :param enable_model_improvements: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#enable_model_improvements LexBot#enable_model_improvements}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#id LexBot#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param idle_session_ttl_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#idle_session_ttl_in_seconds LexBot#idle_session_ttl_in_seconds}.
        :param locale: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#locale LexBot#locale}.
        :param nlu_intent_confidence_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#nlu_intent_confidence_threshold LexBot#nlu_intent_confidence_threshold}.
        :param process_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#process_behavior LexBot#process_behavior}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#timeouts LexBot#timeouts}
        :param voice_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#voice_id LexBot#voice_id}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(abort_statement, dict):
            abort_statement = LexBotAbortStatement(**abort_statement)
        if isinstance(clarification_prompt, dict):
            clarification_prompt = LexBotClarificationPrompt(**clarification_prompt)
        if isinstance(timeouts, dict):
            timeouts = LexBotTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18bd35749f292177817762dd480b72c5d419a561ff32a616c1a8397eb3940cbb)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument abort_statement", value=abort_statement, expected_type=type_hints["abort_statement"])
            check_type(argname="argument child_directed", value=child_directed, expected_type=type_hints["child_directed"])
            check_type(argname="argument intent", value=intent, expected_type=type_hints["intent"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument clarification_prompt", value=clarification_prompt, expected_type=type_hints["clarification_prompt"])
            check_type(argname="argument create_version", value=create_version, expected_type=type_hints["create_version"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument detect_sentiment", value=detect_sentiment, expected_type=type_hints["detect_sentiment"])
            check_type(argname="argument enable_model_improvements", value=enable_model_improvements, expected_type=type_hints["enable_model_improvements"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument idle_session_ttl_in_seconds", value=idle_session_ttl_in_seconds, expected_type=type_hints["idle_session_ttl_in_seconds"])
            check_type(argname="argument locale", value=locale, expected_type=type_hints["locale"])
            check_type(argname="argument nlu_intent_confidence_threshold", value=nlu_intent_confidence_threshold, expected_type=type_hints["nlu_intent_confidence_threshold"])
            check_type(argname="argument process_behavior", value=process_behavior, expected_type=type_hints["process_behavior"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument voice_id", value=voice_id, expected_type=type_hints["voice_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "abort_statement": abort_statement,
            "child_directed": child_directed,
            "intent": intent,
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
        if clarification_prompt is not None:
            self._values["clarification_prompt"] = clarification_prompt
        if create_version is not None:
            self._values["create_version"] = create_version
        if description is not None:
            self._values["description"] = description
        if detect_sentiment is not None:
            self._values["detect_sentiment"] = detect_sentiment
        if enable_model_improvements is not None:
            self._values["enable_model_improvements"] = enable_model_improvements
        if id is not None:
            self._values["id"] = id
        if idle_session_ttl_in_seconds is not None:
            self._values["idle_session_ttl_in_seconds"] = idle_session_ttl_in_seconds
        if locale is not None:
            self._values["locale"] = locale
        if nlu_intent_confidence_threshold is not None:
            self._values["nlu_intent_confidence_threshold"] = nlu_intent_confidence_threshold
        if process_behavior is not None:
            self._values["process_behavior"] = process_behavior
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if voice_id is not None:
            self._values["voice_id"] = voice_id

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
    def abort_statement(self) -> LexBotAbortStatement:
        '''abort_statement block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#abort_statement LexBot#abort_statement}
        '''
        result = self._values.get("abort_statement")
        assert result is not None, "Required property 'abort_statement' is missing"
        return typing.cast(LexBotAbortStatement, result)

    @builtins.property
    def child_directed(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#child_directed LexBot#child_directed}.'''
        result = self._values.get("child_directed")
        assert result is not None, "Required property 'child_directed' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    @builtins.property
    def intent(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LexBotIntent"]]:
        '''intent block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#intent LexBot#intent}
        '''
        result = self._values.get("intent")
        assert result is not None, "Required property 'intent' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LexBotIntent"]], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#name LexBot#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def clarification_prompt(self) -> typing.Optional[LexBotClarificationPrompt]:
        '''clarification_prompt block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#clarification_prompt LexBot#clarification_prompt}
        '''
        result = self._values.get("clarification_prompt")
        return typing.cast(typing.Optional[LexBotClarificationPrompt], result)

    @builtins.property
    def create_version(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#create_version LexBot#create_version}.'''
        result = self._values.get("create_version")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#description LexBot#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def detect_sentiment(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#detect_sentiment LexBot#detect_sentiment}.'''
        result = self._values.get("detect_sentiment")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def enable_model_improvements(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#enable_model_improvements LexBot#enable_model_improvements}.'''
        result = self._values.get("enable_model_improvements")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#id LexBot#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def idle_session_ttl_in_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#idle_session_ttl_in_seconds LexBot#idle_session_ttl_in_seconds}.'''
        result = self._values.get("idle_session_ttl_in_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def locale(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#locale LexBot#locale}.'''
        result = self._values.get("locale")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def nlu_intent_confidence_threshold(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#nlu_intent_confidence_threshold LexBot#nlu_intent_confidence_threshold}.'''
        result = self._values.get("nlu_intent_confidence_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def process_behavior(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#process_behavior LexBot#process_behavior}.'''
        result = self._values.get("process_behavior")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["LexBotTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#timeouts LexBot#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["LexBotTimeouts"], result)

    @builtins.property
    def voice_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#voice_id LexBot#voice_id}.'''
        result = self._values.get("voice_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LexBotConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.lexBot.LexBotIntent",
    jsii_struct_bases=[],
    name_mapping={"intent_name": "intentName", "intent_version": "intentVersion"},
)
class LexBotIntent:
    def __init__(
        self,
        *,
        intent_name: builtins.str,
        intent_version: builtins.str,
    ) -> None:
        '''
        :param intent_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#intent_name LexBot#intent_name}.
        :param intent_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#intent_version LexBot#intent_version}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17dd3fbc2d68b0168722cccda17dddda3fd242fa9d194cbc8e4e13ba5ff5de56)
            check_type(argname="argument intent_name", value=intent_name, expected_type=type_hints["intent_name"])
            check_type(argname="argument intent_version", value=intent_version, expected_type=type_hints["intent_version"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "intent_name": intent_name,
            "intent_version": intent_version,
        }

    @builtins.property
    def intent_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#intent_name LexBot#intent_name}.'''
        result = self._values.get("intent_name")
        assert result is not None, "Required property 'intent_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def intent_version(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#intent_version LexBot#intent_version}.'''
        result = self._values.get("intent_version")
        assert result is not None, "Required property 'intent_version' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LexBotIntent(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LexBotIntentList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lexBot.LexBotIntentList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__45119193cd0fb01feb12780973afff184a8cc379e55b0baeb72940736d3ed706)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "LexBotIntentOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aaea13013303541ddf82c86a5907df5704ace1e100b60f28a70e34400bde3fa5)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LexBotIntentOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff67fdc94e580f37d76d04d2448e34180ac3d2e58c3176d750a1beea3312a54d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__23434907b7d0161e815d14af5f55fc1428afd2897cafa185156f4269ecd8565d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__cd8a4a62790b059fe6f644d7b92717b68d93ae87f758e903fc8a2fe122048534)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LexBotIntent]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LexBotIntent]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LexBotIntent]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ff4b13cdd113bc5bc41370846ba431106ffd02b70535c15fcb281c1235a631d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LexBotIntentOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lexBot.LexBotIntentOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3c32c0adab41083c86b02aa83c0ee8dc45b528f78741f29d46487a24e3818326)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="intentNameInput")
    def intent_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "intentNameInput"))

    @builtins.property
    @jsii.member(jsii_name="intentVersionInput")
    def intent_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "intentVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="intentName")
    def intent_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "intentName"))

    @intent_name.setter
    def intent_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92b7d1d2bf75f701c7f645eaf41e6482b8c3ed3196440b87001243fe576f2bbc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "intentName", value)

    @builtins.property
    @jsii.member(jsii_name="intentVersion")
    def intent_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "intentVersion"))

    @intent_version.setter
    def intent_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15cee2f741cfb8eecc18b9d254ec563d88fb8505f78a86e1398f1cf09ea162b9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "intentVersion", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LexBotIntent, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LexBotIntent, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LexBotIntent, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59e3aabb499e377bcfaec936baf00b4aff2c77ea35282fef51688b3c4df9216f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.lexBot.LexBotTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class LexBotTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#create LexBot#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#delete LexBot#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#update LexBot#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__abc2941b4fad29d95e9f9752b8fac000dd121c83d8f3cb794613834bbaeddd42)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#create LexBot#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#delete LexBot#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#update LexBot#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LexBotTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LexBotTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lexBot.LexBotTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8fb68315a548d58caf26e3faac8b4a30f2ace323d19b3ebb79ec4a16715d8cfe)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @jsii.member(jsii_name="resetUpdate")
    def reset_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdate", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

    @builtins.property
    @jsii.member(jsii_name="updateInput")
    def update_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "updateInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99a94ad6df756906ff502546e1b4c67c0059b79f0a9df347832895ff00525836)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57f3e191851cb1ff957712e5fd70d364bfa35aa4fcb8b357f23e97be1fe5929f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17b6cebaa328c43328b7b764fd21a2bbab6e806facc391f0b413cd5112da545d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LexBotTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LexBotTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LexBotTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d598c0f16c63406b8de77146bce8c6a53e79fd51479571a58cf1ac00ff5c813b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "LexBot",
    "LexBotAbortStatement",
    "LexBotAbortStatementMessage",
    "LexBotAbortStatementMessageList",
    "LexBotAbortStatementMessageOutputReference",
    "LexBotAbortStatementOutputReference",
    "LexBotClarificationPrompt",
    "LexBotClarificationPromptMessage",
    "LexBotClarificationPromptMessageList",
    "LexBotClarificationPromptMessageOutputReference",
    "LexBotClarificationPromptOutputReference",
    "LexBotConfig",
    "LexBotIntent",
    "LexBotIntentList",
    "LexBotIntentOutputReference",
    "LexBotTimeouts",
    "LexBotTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__73aac88fe822dc8e492546e2aff1f59e83e4a51ad6748b80a83355fc320fedb6(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    abort_statement: typing.Union[LexBotAbortStatement, typing.Dict[builtins.str, typing.Any]],
    child_directed: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    intent: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LexBotIntent, typing.Dict[builtins.str, typing.Any]]]],
    name: builtins.str,
    clarification_prompt: typing.Optional[typing.Union[LexBotClarificationPrompt, typing.Dict[builtins.str, typing.Any]]] = None,
    create_version: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    description: typing.Optional[builtins.str] = None,
    detect_sentiment: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    enable_model_improvements: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    idle_session_ttl_in_seconds: typing.Optional[jsii.Number] = None,
    locale: typing.Optional[builtins.str] = None,
    nlu_intent_confidence_threshold: typing.Optional[jsii.Number] = None,
    process_behavior: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[LexBotTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    voice_id: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__4d862f00fb7aced13817d3adf22603cf0f30b53856dd9428858c5488522455fd(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LexBotIntent, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb1d374fd5d7bf02bf249ce6cef3d4d57eed0f1eda99efe630e181857345d523(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0cdc1c448f6064b77d801087794e6b4796e80eb72c5337866157ac61639980cb(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0b88f0d528683c151012aada4ef60ecfc7647e5be7214750b15a5903bb5af97(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de19c8f404a3dff10bac55543afe048c86ed6d5750fb1cc926487cbcdde974a2(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6da1874a077b504c479507c6dcc1fd9dd67c985dc3618ba253d2848d5c7ca1b(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b91bf29fdd767225e8b5c47d773741847bacc4707f6b27576bb6813dc431da9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49748c59a9446e64d7d825b7e02e4e9d94f273d1feabd2bb6951debf71e94e7d(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fea75e627ef32074423ec954fc379418de8a256a2b4b3283a80fa891cf3794b6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc21ed8e3f93befcbeae6e6bd3ef50a8db2f2dbba40851f355a080f7673801c9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43fad0850e5e0ba3fa6311e1e23acf55c8b7742b408f15887fc5282ea14ba9d4(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4ed194cb67a54d4e7df3f807dd855addc3e5425ec75d65fed18b9d281a72bc9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b1b3d0ef1de364dcb6af9abfec3410428103c682f29751a06476480cf0c3cf9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8fcf461203f127b03073019221ddb3c4112423e65aa64376aaea7d9d255b467(
    *,
    message: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LexBotAbortStatementMessage, typing.Dict[builtins.str, typing.Any]]]],
    response_card: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__362ae37c94eb560d401bfaf3c56156f5c7759a33e52d2a11c3330709f5b7b50a(
    *,
    content: builtins.str,
    content_type: builtins.str,
    group_number: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd04452b1d91db2f94833895845c5ba90f22fe00840f56509ac0cfde004f92fe(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e78c1d8b62b0bf5524d556fbe26cec6ca2d4277a8c0a8e314b50ec90c5fd5851(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86c21338b15ae150900971c7753cded94d59cac86bdc05595af51d28f407d8d1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15ca8b9288cb13bb3635a1ffc429aa5754f00f57cfbc373ad5d337c332d4f5f2(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73ce648616f63b54ccf49fcd62afe28415aa1bb9eb3e7720c0345b8f734273a4(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cebc90ec4aab739ca634b631fa78e57ed5a294cda28caea2e70559319282ffe8(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LexBotAbortStatementMessage]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2dbeee8e6f1f5c13a073884040702c709147221b3587cbbdacf3a5e49bc54402(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dcd8efa365a40b6b56c4b1435001e81930d47085402a3121c7251c5b27a7634b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3696ca2e2bc28d82527617a88f984ad621f178311a3677e1b78baf44099722fb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b26a817f7bee67dcdf85738c5c6e24ccfd569a92055f6f2939ad5167dbd346d9(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41d4ba4d5023900b784fd2ae3507c758e6dd4d436b964224af5d9783f64f047e(
    value: typing.Optional[typing.Union[LexBotAbortStatementMessage, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__abf6709f61e21c2d695c246ac5682d6b92fafda9480f256d817bb2d69a0e6e09(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10c0675e32d0646397d57686fba1057ad3166bbfc0103bd67faf6c20dc62e45d(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LexBotAbortStatementMessage, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41afa1c9982934fa0554062767bae925e14ca7a0aaa04a6d82d00514cc0a386b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb8620121bae580e81b6d770c5923dfb18521767c5d4130cd7ff7f1e31675fee(
    value: typing.Optional[LexBotAbortStatement],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dbcbc2ddbf713ff62ef67f2ed689aa159056160e110256d5500c2fceb8e378ae(
    *,
    max_attempts: jsii.Number,
    message: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LexBotClarificationPromptMessage, typing.Dict[builtins.str, typing.Any]]]],
    response_card: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3b4d110efa41458fd97c42c9f60e3d0c4c01f532574935bb935e1978319acac(
    *,
    content: builtins.str,
    content_type: builtins.str,
    group_number: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad60363864744cd532cc56015144d91fed6c9c2708e8f668e5c4eed3fca2da0b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__807b44eae2d5cc7b16c3a32bfc589165fa17489c3ba18514b39aabb83f116322(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a112b8a33f3614c1b4672e72ebe98c534e8672166cd0db965cd8d6bc23eae96(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac185d76d4893e5de33546fc8fa85df8559dc302598c302a0ae8bc30f2be8c9e(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04965188b6b1dc20ae3d0cf10094da1d2bb70824f9b51d27c80945657b57e970(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd5497cc3b9aa1a6d2fb904b1a026991691ccff3d92ef23a6bf957e6467eb00b(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LexBotClarificationPromptMessage]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71447bf4b69686033d8b8d63319e3b11cd42bf6b0de988cd1fd95af1d3de3820(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd30ff563b547eb0d0fa489cee05901bed13d92179840c771c0035b45836c030(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a98774859d0cfc18d2ed927e8a2b9228ed1496160e3932d4528a2bd3ea00a928(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f4acbbd280e585eca887707f9a814c5d1dfab0ba96844b6c2ea45c844e0491f(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9082c0bdc1e8b0b38f3885861d108acf5ee4c17e64b6de9ff03a417e80957a48(
    value: typing.Optional[typing.Union[LexBotClarificationPromptMessage, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b61c0f618439d8b2972d51b766e96c3f5dd077743cf4afd71fad31471445795(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eff8cd7c11ae9d9b95fc8798ae6cdba02544ba167bcc9b479b660095abc0ec26(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LexBotClarificationPromptMessage, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ef9ce7e58a6449b85d136070da3ba42454d94843170385191542a9fddcfc42a(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66f0eb50033b84c9e302494cc1a54496159cca3ab823fbe8f1725f935c046db5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b12cc9beb2ced0cd1cbfdbfdebef75edf21c215fcf1c247643ca8784a30cc70(
    value: typing.Optional[LexBotClarificationPrompt],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18bd35749f292177817762dd480b72c5d419a561ff32a616c1a8397eb3940cbb(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    abort_statement: typing.Union[LexBotAbortStatement, typing.Dict[builtins.str, typing.Any]],
    child_directed: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    intent: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LexBotIntent, typing.Dict[builtins.str, typing.Any]]]],
    name: builtins.str,
    clarification_prompt: typing.Optional[typing.Union[LexBotClarificationPrompt, typing.Dict[builtins.str, typing.Any]]] = None,
    create_version: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    description: typing.Optional[builtins.str] = None,
    detect_sentiment: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    enable_model_improvements: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    idle_session_ttl_in_seconds: typing.Optional[jsii.Number] = None,
    locale: typing.Optional[builtins.str] = None,
    nlu_intent_confidence_threshold: typing.Optional[jsii.Number] = None,
    process_behavior: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[LexBotTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    voice_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17dd3fbc2d68b0168722cccda17dddda3fd242fa9d194cbc8e4e13ba5ff5de56(
    *,
    intent_name: builtins.str,
    intent_version: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45119193cd0fb01feb12780973afff184a8cc379e55b0baeb72940736d3ed706(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aaea13013303541ddf82c86a5907df5704ace1e100b60f28a70e34400bde3fa5(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff67fdc94e580f37d76d04d2448e34180ac3d2e58c3176d750a1beea3312a54d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23434907b7d0161e815d14af5f55fc1428afd2897cafa185156f4269ecd8565d(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd8a4a62790b059fe6f644d7b92717b68d93ae87f758e903fc8a2fe122048534(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ff4b13cdd113bc5bc41370846ba431106ffd02b70535c15fcb281c1235a631d(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LexBotIntent]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c32c0adab41083c86b02aa83c0ee8dc45b528f78741f29d46487a24e3818326(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92b7d1d2bf75f701c7f645eaf41e6482b8c3ed3196440b87001243fe576f2bbc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15cee2f741cfb8eecc18b9d254ec563d88fb8505f78a86e1398f1cf09ea162b9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59e3aabb499e377bcfaec936baf00b4aff2c77ea35282fef51688b3c4df9216f(
    value: typing.Optional[typing.Union[LexBotIntent, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__abc2941b4fad29d95e9f9752b8fac000dd121c83d8f3cb794613834bbaeddd42(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8fb68315a548d58caf26e3faac8b4a30f2ace323d19b3ebb79ec4a16715d8cfe(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99a94ad6df756906ff502546e1b4c67c0059b79f0a9df347832895ff00525836(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57f3e191851cb1ff957712e5fd70d364bfa35aa4fcb8b357f23e97be1fe5929f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17b6cebaa328c43328b7b764fd21a2bbab6e806facc391f0b413cd5112da545d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d598c0f16c63406b8de77146bce8c6a53e79fd51479571a58cf1ac00ff5c813b(
    value: typing.Optional[typing.Union[LexBotTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
