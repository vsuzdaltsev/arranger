'''
# `aws_lex_intent`

Refer to the Terraform Registory for docs: [`aws_lex_intent`](https://www.terraform.io/docs/providers/aws/r/lex_intent).
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


class LexIntent(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lexIntent.LexIntent",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/lex_intent aws_lex_intent}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        fulfillment_activity: typing.Union["LexIntentFulfillmentActivity", typing.Dict[builtins.str, typing.Any]],
        name: builtins.str,
        conclusion_statement: typing.Optional[typing.Union["LexIntentConclusionStatement", typing.Dict[builtins.str, typing.Any]]] = None,
        confirmation_prompt: typing.Optional[typing.Union["LexIntentConfirmationPrompt", typing.Dict[builtins.str, typing.Any]]] = None,
        create_version: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        description: typing.Optional[builtins.str] = None,
        dialog_code_hook: typing.Optional[typing.Union["LexIntentDialogCodeHook", typing.Dict[builtins.str, typing.Any]]] = None,
        follow_up_prompt: typing.Optional[typing.Union["LexIntentFollowUpPrompt", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        parent_intent_signature: typing.Optional[builtins.str] = None,
        rejection_statement: typing.Optional[typing.Union["LexIntentRejectionStatement", typing.Dict[builtins.str, typing.Any]]] = None,
        sample_utterances: typing.Optional[typing.Sequence[builtins.str]] = None,
        slot: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LexIntentSlot", typing.Dict[builtins.str, typing.Any]]]]] = None,
        timeouts: typing.Optional[typing.Union["LexIntentTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/lex_intent aws_lex_intent} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param fulfillment_activity: fulfillment_activity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#fulfillment_activity LexIntent#fulfillment_activity}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#name LexIntent#name}.
        :param conclusion_statement: conclusion_statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#conclusion_statement LexIntent#conclusion_statement}
        :param confirmation_prompt: confirmation_prompt block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#confirmation_prompt LexIntent#confirmation_prompt}
        :param create_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#create_version LexIntent#create_version}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#description LexIntent#description}.
        :param dialog_code_hook: dialog_code_hook block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#dialog_code_hook LexIntent#dialog_code_hook}
        :param follow_up_prompt: follow_up_prompt block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#follow_up_prompt LexIntent#follow_up_prompt}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#id LexIntent#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param parent_intent_signature: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#parent_intent_signature LexIntent#parent_intent_signature}.
        :param rejection_statement: rejection_statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#rejection_statement LexIntent#rejection_statement}
        :param sample_utterances: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#sample_utterances LexIntent#sample_utterances}.
        :param slot: slot block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#slot LexIntent#slot}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#timeouts LexIntent#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__458c41ddde8c77dc6c4abcef2d5661cc959c45ca10aace91513063884c6db991)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = LexIntentConfig(
            fulfillment_activity=fulfillment_activity,
            name=name,
            conclusion_statement=conclusion_statement,
            confirmation_prompt=confirmation_prompt,
            create_version=create_version,
            description=description,
            dialog_code_hook=dialog_code_hook,
            follow_up_prompt=follow_up_prompt,
            id=id,
            parent_intent_signature=parent_intent_signature,
            rejection_statement=rejection_statement,
            sample_utterances=sample_utterances,
            slot=slot,
            timeouts=timeouts,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putConclusionStatement")
    def put_conclusion_statement(
        self,
        *,
        message: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LexIntentConclusionStatementMessage", typing.Dict[builtins.str, typing.Any]]]],
        response_card: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param message: message block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#message LexIntent#message}
        :param response_card: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#response_card LexIntent#response_card}.
        '''
        value = LexIntentConclusionStatement(
            message=message, response_card=response_card
        )

        return typing.cast(None, jsii.invoke(self, "putConclusionStatement", [value]))

    @jsii.member(jsii_name="putConfirmationPrompt")
    def put_confirmation_prompt(
        self,
        *,
        max_attempts: jsii.Number,
        message: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LexIntentConfirmationPromptMessage", typing.Dict[builtins.str, typing.Any]]]],
        response_card: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param max_attempts: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#max_attempts LexIntent#max_attempts}.
        :param message: message block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#message LexIntent#message}
        :param response_card: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#response_card LexIntent#response_card}.
        '''
        value = LexIntentConfirmationPrompt(
            max_attempts=max_attempts, message=message, response_card=response_card
        )

        return typing.cast(None, jsii.invoke(self, "putConfirmationPrompt", [value]))

    @jsii.member(jsii_name="putDialogCodeHook")
    def put_dialog_code_hook(
        self,
        *,
        message_version: builtins.str,
        uri: builtins.str,
    ) -> None:
        '''
        :param message_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#message_version LexIntent#message_version}.
        :param uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#uri LexIntent#uri}.
        '''
        value = LexIntentDialogCodeHook(message_version=message_version, uri=uri)

        return typing.cast(None, jsii.invoke(self, "putDialogCodeHook", [value]))

    @jsii.member(jsii_name="putFollowUpPrompt")
    def put_follow_up_prompt(
        self,
        *,
        prompt: typing.Union["LexIntentFollowUpPromptPrompt", typing.Dict[builtins.str, typing.Any]],
        rejection_statement: typing.Union["LexIntentFollowUpPromptRejectionStatement", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param prompt: prompt block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#prompt LexIntent#prompt}
        :param rejection_statement: rejection_statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#rejection_statement LexIntent#rejection_statement}
        '''
        value = LexIntentFollowUpPrompt(
            prompt=prompt, rejection_statement=rejection_statement
        )

        return typing.cast(None, jsii.invoke(self, "putFollowUpPrompt", [value]))

    @jsii.member(jsii_name="putFulfillmentActivity")
    def put_fulfillment_activity(
        self,
        *,
        type: builtins.str,
        code_hook: typing.Optional[typing.Union["LexIntentFulfillmentActivityCodeHook", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#type LexIntent#type}.
        :param code_hook: code_hook block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#code_hook LexIntent#code_hook}
        '''
        value = LexIntentFulfillmentActivity(type=type, code_hook=code_hook)

        return typing.cast(None, jsii.invoke(self, "putFulfillmentActivity", [value]))

    @jsii.member(jsii_name="putRejectionStatement")
    def put_rejection_statement(
        self,
        *,
        message: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LexIntentRejectionStatementMessage", typing.Dict[builtins.str, typing.Any]]]],
        response_card: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param message: message block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#message LexIntent#message}
        :param response_card: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#response_card LexIntent#response_card}.
        '''
        value = LexIntentRejectionStatement(
            message=message, response_card=response_card
        )

        return typing.cast(None, jsii.invoke(self, "putRejectionStatement", [value]))

    @jsii.member(jsii_name="putSlot")
    def put_slot(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LexIntentSlot", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9ef4cbc175508744fba9e80bc657cccdedb1feac99daa065a06158ca353abd4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSlot", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#create LexIntent#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#delete LexIntent#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#update LexIntent#update}.
        '''
        value = LexIntentTimeouts(create=create, delete=delete, update=update)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetConclusionStatement")
    def reset_conclusion_statement(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConclusionStatement", []))

    @jsii.member(jsii_name="resetConfirmationPrompt")
    def reset_confirmation_prompt(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfirmationPrompt", []))

    @jsii.member(jsii_name="resetCreateVersion")
    def reset_create_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreateVersion", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetDialogCodeHook")
    def reset_dialog_code_hook(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDialogCodeHook", []))

    @jsii.member(jsii_name="resetFollowUpPrompt")
    def reset_follow_up_prompt(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFollowUpPrompt", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetParentIntentSignature")
    def reset_parent_intent_signature(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParentIntentSignature", []))

    @jsii.member(jsii_name="resetRejectionStatement")
    def reset_rejection_statement(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRejectionStatement", []))

    @jsii.member(jsii_name="resetSampleUtterances")
    def reset_sample_utterances(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSampleUtterances", []))

    @jsii.member(jsii_name="resetSlot")
    def reset_slot(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSlot", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

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
    @jsii.member(jsii_name="checksum")
    def checksum(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "checksum"))

    @builtins.property
    @jsii.member(jsii_name="conclusionStatement")
    def conclusion_statement(self) -> "LexIntentConclusionStatementOutputReference":
        return typing.cast("LexIntentConclusionStatementOutputReference", jsii.get(self, "conclusionStatement"))

    @builtins.property
    @jsii.member(jsii_name="confirmationPrompt")
    def confirmation_prompt(self) -> "LexIntentConfirmationPromptOutputReference":
        return typing.cast("LexIntentConfirmationPromptOutputReference", jsii.get(self, "confirmationPrompt"))

    @builtins.property
    @jsii.member(jsii_name="createdDate")
    def created_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdDate"))

    @builtins.property
    @jsii.member(jsii_name="dialogCodeHook")
    def dialog_code_hook(self) -> "LexIntentDialogCodeHookOutputReference":
        return typing.cast("LexIntentDialogCodeHookOutputReference", jsii.get(self, "dialogCodeHook"))

    @builtins.property
    @jsii.member(jsii_name="followUpPrompt")
    def follow_up_prompt(self) -> "LexIntentFollowUpPromptOutputReference":
        return typing.cast("LexIntentFollowUpPromptOutputReference", jsii.get(self, "followUpPrompt"))

    @builtins.property
    @jsii.member(jsii_name="fulfillmentActivity")
    def fulfillment_activity(self) -> "LexIntentFulfillmentActivityOutputReference":
        return typing.cast("LexIntentFulfillmentActivityOutputReference", jsii.get(self, "fulfillmentActivity"))

    @builtins.property
    @jsii.member(jsii_name="lastUpdatedDate")
    def last_updated_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastUpdatedDate"))

    @builtins.property
    @jsii.member(jsii_name="rejectionStatement")
    def rejection_statement(self) -> "LexIntentRejectionStatementOutputReference":
        return typing.cast("LexIntentRejectionStatementOutputReference", jsii.get(self, "rejectionStatement"))

    @builtins.property
    @jsii.member(jsii_name="slot")
    def slot(self) -> "LexIntentSlotList":
        return typing.cast("LexIntentSlotList", jsii.get(self, "slot"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "LexIntentTimeoutsOutputReference":
        return typing.cast("LexIntentTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @builtins.property
    @jsii.member(jsii_name="conclusionStatementInput")
    def conclusion_statement_input(
        self,
    ) -> typing.Optional["LexIntentConclusionStatement"]:
        return typing.cast(typing.Optional["LexIntentConclusionStatement"], jsii.get(self, "conclusionStatementInput"))

    @builtins.property
    @jsii.member(jsii_name="confirmationPromptInput")
    def confirmation_prompt_input(
        self,
    ) -> typing.Optional["LexIntentConfirmationPrompt"]:
        return typing.cast(typing.Optional["LexIntentConfirmationPrompt"], jsii.get(self, "confirmationPromptInput"))

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
    @jsii.member(jsii_name="dialogCodeHookInput")
    def dialog_code_hook_input(self) -> typing.Optional["LexIntentDialogCodeHook"]:
        return typing.cast(typing.Optional["LexIntentDialogCodeHook"], jsii.get(self, "dialogCodeHookInput"))

    @builtins.property
    @jsii.member(jsii_name="followUpPromptInput")
    def follow_up_prompt_input(self) -> typing.Optional["LexIntentFollowUpPrompt"]:
        return typing.cast(typing.Optional["LexIntentFollowUpPrompt"], jsii.get(self, "followUpPromptInput"))

    @builtins.property
    @jsii.member(jsii_name="fulfillmentActivityInput")
    def fulfillment_activity_input(
        self,
    ) -> typing.Optional["LexIntentFulfillmentActivity"]:
        return typing.cast(typing.Optional["LexIntentFulfillmentActivity"], jsii.get(self, "fulfillmentActivityInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="parentIntentSignatureInput")
    def parent_intent_signature_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "parentIntentSignatureInput"))

    @builtins.property
    @jsii.member(jsii_name="rejectionStatementInput")
    def rejection_statement_input(
        self,
    ) -> typing.Optional["LexIntentRejectionStatement"]:
        return typing.cast(typing.Optional["LexIntentRejectionStatement"], jsii.get(self, "rejectionStatementInput"))

    @builtins.property
    @jsii.member(jsii_name="sampleUtterancesInput")
    def sample_utterances_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sampleUtterancesInput"))

    @builtins.property
    @jsii.member(jsii_name="slotInput")
    def slot_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LexIntentSlot"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LexIntentSlot"]]], jsii.get(self, "slotInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["LexIntentTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["LexIntentTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__50810038e4562fc1af83f112e804d74f6265f7b7ee3989f70a6b9f61c62351c1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "createVersion", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0803ab4467448749dab96d6f66150f9a07ffa43c221a724cf8d18191869468f2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c2cedf06c6ae94f908e6160553e8acb613bcf5020e697a31d01ed5ed28d29f4a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__959a2ab8071d0e1d7283f02eeddd65eab763b2e0f453441dd0b65c587b157b59)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="parentIntentSignature")
    def parent_intent_signature(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "parentIntentSignature"))

    @parent_intent_signature.setter
    def parent_intent_signature(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5fd4eb393d5f115ab5e6081d799ef7e484184e151a1e3c50261623da293b8f54)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parentIntentSignature", value)

    @builtins.property
    @jsii.member(jsii_name="sampleUtterances")
    def sample_utterances(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sampleUtterances"))

    @sample_utterances.setter
    def sample_utterances(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75ead4851b65fca8834f4ff2f94f10bc23b725d2d2524a8d26e458859f5c2938)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sampleUtterances", value)


@jsii.data_type(
    jsii_type="aws.lexIntent.LexIntentConclusionStatement",
    jsii_struct_bases=[],
    name_mapping={"message": "message", "response_card": "responseCard"},
)
class LexIntentConclusionStatement:
    def __init__(
        self,
        *,
        message: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LexIntentConclusionStatementMessage", typing.Dict[builtins.str, typing.Any]]]],
        response_card: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param message: message block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#message LexIntent#message}
        :param response_card: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#response_card LexIntent#response_card}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__800968169f251595b94e71a1e3c9c80c5fd4188ca995ed0881c0bbd03246a40b)
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
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LexIntentConclusionStatementMessage"]]:
        '''message block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#message LexIntent#message}
        '''
        result = self._values.get("message")
        assert result is not None, "Required property 'message' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LexIntentConclusionStatementMessage"]], result)

    @builtins.property
    def response_card(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#response_card LexIntent#response_card}.'''
        result = self._values.get("response_card")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LexIntentConclusionStatement(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.lexIntent.LexIntentConclusionStatementMessage",
    jsii_struct_bases=[],
    name_mapping={
        "content": "content",
        "content_type": "contentType",
        "group_number": "groupNumber",
    },
)
class LexIntentConclusionStatementMessage:
    def __init__(
        self,
        *,
        content: builtins.str,
        content_type: builtins.str,
        group_number: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param content: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#content LexIntent#content}.
        :param content_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#content_type LexIntent#content_type}.
        :param group_number: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#group_number LexIntent#group_number}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__796562d6d8205c0d1556c371e43e0723ea821faac30924eb8c6035fce5f18f54)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#content LexIntent#content}.'''
        result = self._values.get("content")
        assert result is not None, "Required property 'content' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def content_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#content_type LexIntent#content_type}.'''
        result = self._values.get("content_type")
        assert result is not None, "Required property 'content_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def group_number(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#group_number LexIntent#group_number}.'''
        result = self._values.get("group_number")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LexIntentConclusionStatementMessage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LexIntentConclusionStatementMessageList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lexIntent.LexIntentConclusionStatementMessageList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f5fcb41b4fc1c34ea23dba80076cc2541a2bc22611f85defa27464708e19b8b3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LexIntentConclusionStatementMessageOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ebc802768bf124771c5652d77c68c1fca975632e40aaa9eb6d8e6d4dfc866c8)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LexIntentConclusionStatementMessageOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d722c45ec80e8d2cc918bb0d378d397abd5533982869748f3bd82d37a0259b02)
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
            type_hints = typing.get_type_hints(_typecheckingstub__531a92faf91aaa323e4644c370e6b2fcc768e507019299eb85022e738ec8828f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__df8e71aafea55057c254ee65aff9a8cb646159be6a85f7db0dbb2f25b849816a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LexIntentConclusionStatementMessage]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LexIntentConclusionStatementMessage]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LexIntentConclusionStatementMessage]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__176bd720cdee5b455c4ab003f4f17250e42e55de3e3c7eb2f510a503055b1396)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LexIntentConclusionStatementMessageOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lexIntent.LexIntentConclusionStatementMessageOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__14ae71101de048f8e9c69afd2687b821aa3c31abe9eb736fcda3fe82c10eb66a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__56f678f4825b6b98c6fa1b8067373916ace97674bd87ae7f5c135a7bb45c85ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "content", value)

    @builtins.property
    @jsii.member(jsii_name="contentType")
    def content_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentType"))

    @content_type.setter
    def content_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a05bc80d8e05e3c8889751800068aba2ea66c485cd835b2dfb6454aedeeb904)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentType", value)

    @builtins.property
    @jsii.member(jsii_name="groupNumber")
    def group_number(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "groupNumber"))

    @group_number.setter
    def group_number(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__738a6e3d4881b8ad5e37ab130bf7d3a3e78a1249a92c514347f061f156a6b9f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupNumber", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LexIntentConclusionStatementMessage, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LexIntentConclusionStatementMessage, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LexIntentConclusionStatementMessage, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1643de291b8287f62f720f91b42ef439d4899f423529fcb4d32ef50d1c9ccbb7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LexIntentConclusionStatementOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lexIntent.LexIntentConclusionStatementOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__158929892aa423dd63d273c2f2776e21a8f48cdca529fd377bb719e54ac7d92e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMessage")
    def put_message(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LexIntentConclusionStatementMessage, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__482807e68b0c6d8ea38859bcb9a6dabbb7f9ee0b2b26eff492cdd89968e08101)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMessage", [value]))

    @jsii.member(jsii_name="resetResponseCard")
    def reset_response_card(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResponseCard", []))

    @builtins.property
    @jsii.member(jsii_name="message")
    def message(self) -> LexIntentConclusionStatementMessageList:
        return typing.cast(LexIntentConclusionStatementMessageList, jsii.get(self, "message"))

    @builtins.property
    @jsii.member(jsii_name="messageInput")
    def message_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LexIntentConclusionStatementMessage]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LexIntentConclusionStatementMessage]]], jsii.get(self, "messageInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__10d0f44131052c0bcad3ee933147c026a73e3b4818330057efadcfca6ed060f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "responseCard", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LexIntentConclusionStatement]:
        return typing.cast(typing.Optional[LexIntentConclusionStatement], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LexIntentConclusionStatement],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__abb37937b2c96a1f563ff443de2ca0d7ba179e1b66a049de2fa4897cca55ba61)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.lexIntent.LexIntentConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "fulfillment_activity": "fulfillmentActivity",
        "name": "name",
        "conclusion_statement": "conclusionStatement",
        "confirmation_prompt": "confirmationPrompt",
        "create_version": "createVersion",
        "description": "description",
        "dialog_code_hook": "dialogCodeHook",
        "follow_up_prompt": "followUpPrompt",
        "id": "id",
        "parent_intent_signature": "parentIntentSignature",
        "rejection_statement": "rejectionStatement",
        "sample_utterances": "sampleUtterances",
        "slot": "slot",
        "timeouts": "timeouts",
    },
)
class LexIntentConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        fulfillment_activity: typing.Union["LexIntentFulfillmentActivity", typing.Dict[builtins.str, typing.Any]],
        name: builtins.str,
        conclusion_statement: typing.Optional[typing.Union[LexIntentConclusionStatement, typing.Dict[builtins.str, typing.Any]]] = None,
        confirmation_prompt: typing.Optional[typing.Union["LexIntentConfirmationPrompt", typing.Dict[builtins.str, typing.Any]]] = None,
        create_version: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        description: typing.Optional[builtins.str] = None,
        dialog_code_hook: typing.Optional[typing.Union["LexIntentDialogCodeHook", typing.Dict[builtins.str, typing.Any]]] = None,
        follow_up_prompt: typing.Optional[typing.Union["LexIntentFollowUpPrompt", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        parent_intent_signature: typing.Optional[builtins.str] = None,
        rejection_statement: typing.Optional[typing.Union["LexIntentRejectionStatement", typing.Dict[builtins.str, typing.Any]]] = None,
        sample_utterances: typing.Optional[typing.Sequence[builtins.str]] = None,
        slot: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LexIntentSlot", typing.Dict[builtins.str, typing.Any]]]]] = None,
        timeouts: typing.Optional[typing.Union["LexIntentTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param fulfillment_activity: fulfillment_activity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#fulfillment_activity LexIntent#fulfillment_activity}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#name LexIntent#name}.
        :param conclusion_statement: conclusion_statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#conclusion_statement LexIntent#conclusion_statement}
        :param confirmation_prompt: confirmation_prompt block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#confirmation_prompt LexIntent#confirmation_prompt}
        :param create_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#create_version LexIntent#create_version}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#description LexIntent#description}.
        :param dialog_code_hook: dialog_code_hook block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#dialog_code_hook LexIntent#dialog_code_hook}
        :param follow_up_prompt: follow_up_prompt block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#follow_up_prompt LexIntent#follow_up_prompt}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#id LexIntent#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param parent_intent_signature: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#parent_intent_signature LexIntent#parent_intent_signature}.
        :param rejection_statement: rejection_statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#rejection_statement LexIntent#rejection_statement}
        :param sample_utterances: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#sample_utterances LexIntent#sample_utterances}.
        :param slot: slot block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#slot LexIntent#slot}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#timeouts LexIntent#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(fulfillment_activity, dict):
            fulfillment_activity = LexIntentFulfillmentActivity(**fulfillment_activity)
        if isinstance(conclusion_statement, dict):
            conclusion_statement = LexIntentConclusionStatement(**conclusion_statement)
        if isinstance(confirmation_prompt, dict):
            confirmation_prompt = LexIntentConfirmationPrompt(**confirmation_prompt)
        if isinstance(dialog_code_hook, dict):
            dialog_code_hook = LexIntentDialogCodeHook(**dialog_code_hook)
        if isinstance(follow_up_prompt, dict):
            follow_up_prompt = LexIntentFollowUpPrompt(**follow_up_prompt)
        if isinstance(rejection_statement, dict):
            rejection_statement = LexIntentRejectionStatement(**rejection_statement)
        if isinstance(timeouts, dict):
            timeouts = LexIntentTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d360e7cc0c58e5e94d55fcff91db3c02d27a06bbc82f6855204e2af0a2c48454)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument fulfillment_activity", value=fulfillment_activity, expected_type=type_hints["fulfillment_activity"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument conclusion_statement", value=conclusion_statement, expected_type=type_hints["conclusion_statement"])
            check_type(argname="argument confirmation_prompt", value=confirmation_prompt, expected_type=type_hints["confirmation_prompt"])
            check_type(argname="argument create_version", value=create_version, expected_type=type_hints["create_version"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument dialog_code_hook", value=dialog_code_hook, expected_type=type_hints["dialog_code_hook"])
            check_type(argname="argument follow_up_prompt", value=follow_up_prompt, expected_type=type_hints["follow_up_prompt"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument parent_intent_signature", value=parent_intent_signature, expected_type=type_hints["parent_intent_signature"])
            check_type(argname="argument rejection_statement", value=rejection_statement, expected_type=type_hints["rejection_statement"])
            check_type(argname="argument sample_utterances", value=sample_utterances, expected_type=type_hints["sample_utterances"])
            check_type(argname="argument slot", value=slot, expected_type=type_hints["slot"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "fulfillment_activity": fulfillment_activity,
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
        if conclusion_statement is not None:
            self._values["conclusion_statement"] = conclusion_statement
        if confirmation_prompt is not None:
            self._values["confirmation_prompt"] = confirmation_prompt
        if create_version is not None:
            self._values["create_version"] = create_version
        if description is not None:
            self._values["description"] = description
        if dialog_code_hook is not None:
            self._values["dialog_code_hook"] = dialog_code_hook
        if follow_up_prompt is not None:
            self._values["follow_up_prompt"] = follow_up_prompt
        if id is not None:
            self._values["id"] = id
        if parent_intent_signature is not None:
            self._values["parent_intent_signature"] = parent_intent_signature
        if rejection_statement is not None:
            self._values["rejection_statement"] = rejection_statement
        if sample_utterances is not None:
            self._values["sample_utterances"] = sample_utterances
        if slot is not None:
            self._values["slot"] = slot
        if timeouts is not None:
            self._values["timeouts"] = timeouts

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
    def fulfillment_activity(self) -> "LexIntentFulfillmentActivity":
        '''fulfillment_activity block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#fulfillment_activity LexIntent#fulfillment_activity}
        '''
        result = self._values.get("fulfillment_activity")
        assert result is not None, "Required property 'fulfillment_activity' is missing"
        return typing.cast("LexIntentFulfillmentActivity", result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#name LexIntent#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def conclusion_statement(self) -> typing.Optional[LexIntentConclusionStatement]:
        '''conclusion_statement block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#conclusion_statement LexIntent#conclusion_statement}
        '''
        result = self._values.get("conclusion_statement")
        return typing.cast(typing.Optional[LexIntentConclusionStatement], result)

    @builtins.property
    def confirmation_prompt(self) -> typing.Optional["LexIntentConfirmationPrompt"]:
        '''confirmation_prompt block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#confirmation_prompt LexIntent#confirmation_prompt}
        '''
        result = self._values.get("confirmation_prompt")
        return typing.cast(typing.Optional["LexIntentConfirmationPrompt"], result)

    @builtins.property
    def create_version(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#create_version LexIntent#create_version}.'''
        result = self._values.get("create_version")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#description LexIntent#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dialog_code_hook(self) -> typing.Optional["LexIntentDialogCodeHook"]:
        '''dialog_code_hook block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#dialog_code_hook LexIntent#dialog_code_hook}
        '''
        result = self._values.get("dialog_code_hook")
        return typing.cast(typing.Optional["LexIntentDialogCodeHook"], result)

    @builtins.property
    def follow_up_prompt(self) -> typing.Optional["LexIntentFollowUpPrompt"]:
        '''follow_up_prompt block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#follow_up_prompt LexIntent#follow_up_prompt}
        '''
        result = self._values.get("follow_up_prompt")
        return typing.cast(typing.Optional["LexIntentFollowUpPrompt"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#id LexIntent#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parent_intent_signature(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#parent_intent_signature LexIntent#parent_intent_signature}.'''
        result = self._values.get("parent_intent_signature")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rejection_statement(self) -> typing.Optional["LexIntentRejectionStatement"]:
        '''rejection_statement block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#rejection_statement LexIntent#rejection_statement}
        '''
        result = self._values.get("rejection_statement")
        return typing.cast(typing.Optional["LexIntentRejectionStatement"], result)

    @builtins.property
    def sample_utterances(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#sample_utterances LexIntent#sample_utterances}.'''
        result = self._values.get("sample_utterances")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def slot(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LexIntentSlot"]]]:
        '''slot block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#slot LexIntent#slot}
        '''
        result = self._values.get("slot")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LexIntentSlot"]]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["LexIntentTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#timeouts LexIntent#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["LexIntentTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LexIntentConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.lexIntent.LexIntentConfirmationPrompt",
    jsii_struct_bases=[],
    name_mapping={
        "max_attempts": "maxAttempts",
        "message": "message",
        "response_card": "responseCard",
    },
)
class LexIntentConfirmationPrompt:
    def __init__(
        self,
        *,
        max_attempts: jsii.Number,
        message: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LexIntentConfirmationPromptMessage", typing.Dict[builtins.str, typing.Any]]]],
        response_card: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param max_attempts: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#max_attempts LexIntent#max_attempts}.
        :param message: message block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#message LexIntent#message}
        :param response_card: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#response_card LexIntent#response_card}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62f1ca124c5eb7e9e3bd9f2730e40ec9546136ddd47a29d3d3f82d0798442096)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#max_attempts LexIntent#max_attempts}.'''
        result = self._values.get("max_attempts")
        assert result is not None, "Required property 'max_attempts' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def message(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LexIntentConfirmationPromptMessage"]]:
        '''message block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#message LexIntent#message}
        '''
        result = self._values.get("message")
        assert result is not None, "Required property 'message' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LexIntentConfirmationPromptMessage"]], result)

    @builtins.property
    def response_card(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#response_card LexIntent#response_card}.'''
        result = self._values.get("response_card")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LexIntentConfirmationPrompt(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.lexIntent.LexIntentConfirmationPromptMessage",
    jsii_struct_bases=[],
    name_mapping={
        "content": "content",
        "content_type": "contentType",
        "group_number": "groupNumber",
    },
)
class LexIntentConfirmationPromptMessage:
    def __init__(
        self,
        *,
        content: builtins.str,
        content_type: builtins.str,
        group_number: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param content: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#content LexIntent#content}.
        :param content_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#content_type LexIntent#content_type}.
        :param group_number: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#group_number LexIntent#group_number}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae361b23db81673fcb255ca8e4431393a9c98da2c0b615775ce562f077227840)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#content LexIntent#content}.'''
        result = self._values.get("content")
        assert result is not None, "Required property 'content' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def content_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#content_type LexIntent#content_type}.'''
        result = self._values.get("content_type")
        assert result is not None, "Required property 'content_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def group_number(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#group_number LexIntent#group_number}.'''
        result = self._values.get("group_number")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LexIntentConfirmationPromptMessage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LexIntentConfirmationPromptMessageList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lexIntent.LexIntentConfirmationPromptMessageList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c0b4aec7bc133e5de7d10f8e70ad1c4a0c7c9760cc6902b852c1b501fa97bfc8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LexIntentConfirmationPromptMessageOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__931b8de38f5cfd29df95b27f6fb926d222e7d7b9d3c82b4547d0a55137c602fb)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LexIntentConfirmationPromptMessageOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f39168812351059b9d52ecbe4b218645937d2438296fa8863ab2de1129db778d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__512fba6e7139965199eac243f5114cd5dfbbda1a600a054a1c2db443c1b4b122)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1aa9c258e8244d8464ebdee2bce071f5980884d86886d0fc208bdb37e440f447)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LexIntentConfirmationPromptMessage]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LexIntentConfirmationPromptMessage]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LexIntentConfirmationPromptMessage]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c7ca1500ef4fe78ef1ab8978e59c384338650c5c7fa48a0663ac326c5ff99a8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LexIntentConfirmationPromptMessageOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lexIntent.LexIntentConfirmationPromptMessageOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2082e2676c0ba1a7e00bab4fbcf591f23d48d555e86144add08a02f71422579f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__fdb08e87463be3b601c735fa12e2030223d10dd695032b903bf15788cb9ff6eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "content", value)

    @builtins.property
    @jsii.member(jsii_name="contentType")
    def content_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentType"))

    @content_type.setter
    def content_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82d29d3c02bb722d78a5cf3134819b651f91d4827496648d62e698f9f55a5afe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentType", value)

    @builtins.property
    @jsii.member(jsii_name="groupNumber")
    def group_number(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "groupNumber"))

    @group_number.setter
    def group_number(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67a962f73d10d79bd94b7a1b1a1d06ea863486267f3e49ef6fdbaf1789603746)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupNumber", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LexIntentConfirmationPromptMessage, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LexIntentConfirmationPromptMessage, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LexIntentConfirmationPromptMessage, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0665780a1d23dafc59f2dd8ee0522e9251b582142469f2987f7f8aed42e084b0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LexIntentConfirmationPromptOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lexIntent.LexIntentConfirmationPromptOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ddc355321737bca555d66419c74499150ff44c5aa1bed71c89f3c311a4b9fde2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMessage")
    def put_message(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LexIntentConfirmationPromptMessage, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11cad9ff898646ed68215950c7e937a73e3f114ba0cd3a1d78424ca09a7a8498)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMessage", [value]))

    @jsii.member(jsii_name="resetResponseCard")
    def reset_response_card(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResponseCard", []))

    @builtins.property
    @jsii.member(jsii_name="message")
    def message(self) -> LexIntentConfirmationPromptMessageList:
        return typing.cast(LexIntentConfirmationPromptMessageList, jsii.get(self, "message"))

    @builtins.property
    @jsii.member(jsii_name="maxAttemptsInput")
    def max_attempts_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxAttemptsInput"))

    @builtins.property
    @jsii.member(jsii_name="messageInput")
    def message_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LexIntentConfirmationPromptMessage]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LexIntentConfirmationPromptMessage]]], jsii.get(self, "messageInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__2ad52d0336e5bbd126cfff70a0ea1c2e85113845a22c67fce0eb2c7714bcbf54)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxAttempts", value)

    @builtins.property
    @jsii.member(jsii_name="responseCard")
    def response_card(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "responseCard"))

    @response_card.setter
    def response_card(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9999e4228ebdecbbf3b00aa9792ab5e956d055082ee1b4fb8cb48f4b7abea63)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "responseCard", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LexIntentConfirmationPrompt]:
        return typing.cast(typing.Optional[LexIntentConfirmationPrompt], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LexIntentConfirmationPrompt],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f95df29aea107cd3d9dd9079c5dfefdebc766ee7d6d0e68402e7b9e83d51b9a0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.lexIntent.LexIntentDialogCodeHook",
    jsii_struct_bases=[],
    name_mapping={"message_version": "messageVersion", "uri": "uri"},
)
class LexIntentDialogCodeHook:
    def __init__(self, *, message_version: builtins.str, uri: builtins.str) -> None:
        '''
        :param message_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#message_version LexIntent#message_version}.
        :param uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#uri LexIntent#uri}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33f02e165e6c1344f4603ee9fde66d731763d1c1c7d0a8fb100a67a0df150d9b)
            check_type(argname="argument message_version", value=message_version, expected_type=type_hints["message_version"])
            check_type(argname="argument uri", value=uri, expected_type=type_hints["uri"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "message_version": message_version,
            "uri": uri,
        }

    @builtins.property
    def message_version(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#message_version LexIntent#message_version}.'''
        result = self._values.get("message_version")
        assert result is not None, "Required property 'message_version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def uri(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#uri LexIntent#uri}.'''
        result = self._values.get("uri")
        assert result is not None, "Required property 'uri' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LexIntentDialogCodeHook(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LexIntentDialogCodeHookOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lexIntent.LexIntentDialogCodeHookOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d2f73ba37efea683fc98937c5b421315bd4dd62d1c3e8e7ab85394fb8232a5c4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="messageVersionInput")
    def message_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "messageVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="uriInput")
    def uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "uriInput"))

    @builtins.property
    @jsii.member(jsii_name="messageVersion")
    def message_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "messageVersion"))

    @message_version.setter
    def message_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4e0ea681406a290ccb1e293885f272cbb85fce5606fff16deec3ddd34d24daa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "messageVersion", value)

    @builtins.property
    @jsii.member(jsii_name="uri")
    def uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uri"))

    @uri.setter
    def uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e29e3202ee374ae961d1825c5ec973934a4c0500a0d038aa3f2a6221fc32374)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "uri", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LexIntentDialogCodeHook]:
        return typing.cast(typing.Optional[LexIntentDialogCodeHook], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[LexIntentDialogCodeHook]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__378229deb67a8d0fa17563d1aba57d76e3dcae0f56fb5b09449ecc3742b7464c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.lexIntent.LexIntentFollowUpPrompt",
    jsii_struct_bases=[],
    name_mapping={"prompt": "prompt", "rejection_statement": "rejectionStatement"},
)
class LexIntentFollowUpPrompt:
    def __init__(
        self,
        *,
        prompt: typing.Union["LexIntentFollowUpPromptPrompt", typing.Dict[builtins.str, typing.Any]],
        rejection_statement: typing.Union["LexIntentFollowUpPromptRejectionStatement", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param prompt: prompt block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#prompt LexIntent#prompt}
        :param rejection_statement: rejection_statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#rejection_statement LexIntent#rejection_statement}
        '''
        if isinstance(prompt, dict):
            prompt = LexIntentFollowUpPromptPrompt(**prompt)
        if isinstance(rejection_statement, dict):
            rejection_statement = LexIntentFollowUpPromptRejectionStatement(**rejection_statement)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c324b3526ca8823429c257a63ff6db6fde04341c7b7914c157d42f7d8699dee)
            check_type(argname="argument prompt", value=prompt, expected_type=type_hints["prompt"])
            check_type(argname="argument rejection_statement", value=rejection_statement, expected_type=type_hints["rejection_statement"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "prompt": prompt,
            "rejection_statement": rejection_statement,
        }

    @builtins.property
    def prompt(self) -> "LexIntentFollowUpPromptPrompt":
        '''prompt block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#prompt LexIntent#prompt}
        '''
        result = self._values.get("prompt")
        assert result is not None, "Required property 'prompt' is missing"
        return typing.cast("LexIntentFollowUpPromptPrompt", result)

    @builtins.property
    def rejection_statement(self) -> "LexIntentFollowUpPromptRejectionStatement":
        '''rejection_statement block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#rejection_statement LexIntent#rejection_statement}
        '''
        result = self._values.get("rejection_statement")
        assert result is not None, "Required property 'rejection_statement' is missing"
        return typing.cast("LexIntentFollowUpPromptRejectionStatement", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LexIntentFollowUpPrompt(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LexIntentFollowUpPromptOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lexIntent.LexIntentFollowUpPromptOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c662ae0b60b2c5bc731deabe153fd269637213b8645dc524fc94a3f9681f86b7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putPrompt")
    def put_prompt(
        self,
        *,
        max_attempts: jsii.Number,
        message: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LexIntentFollowUpPromptPromptMessage", typing.Dict[builtins.str, typing.Any]]]],
        response_card: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param max_attempts: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#max_attempts LexIntent#max_attempts}.
        :param message: message block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#message LexIntent#message}
        :param response_card: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#response_card LexIntent#response_card}.
        '''
        value = LexIntentFollowUpPromptPrompt(
            max_attempts=max_attempts, message=message, response_card=response_card
        )

        return typing.cast(None, jsii.invoke(self, "putPrompt", [value]))

    @jsii.member(jsii_name="putRejectionStatement")
    def put_rejection_statement(
        self,
        *,
        message: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LexIntentFollowUpPromptRejectionStatementMessage", typing.Dict[builtins.str, typing.Any]]]],
        response_card: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param message: message block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#message LexIntent#message}
        :param response_card: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#response_card LexIntent#response_card}.
        '''
        value = LexIntentFollowUpPromptRejectionStatement(
            message=message, response_card=response_card
        )

        return typing.cast(None, jsii.invoke(self, "putRejectionStatement", [value]))

    @builtins.property
    @jsii.member(jsii_name="prompt")
    def prompt(self) -> "LexIntentFollowUpPromptPromptOutputReference":
        return typing.cast("LexIntentFollowUpPromptPromptOutputReference", jsii.get(self, "prompt"))

    @builtins.property
    @jsii.member(jsii_name="rejectionStatement")
    def rejection_statement(
        self,
    ) -> "LexIntentFollowUpPromptRejectionStatementOutputReference":
        return typing.cast("LexIntentFollowUpPromptRejectionStatementOutputReference", jsii.get(self, "rejectionStatement"))

    @builtins.property
    @jsii.member(jsii_name="promptInput")
    def prompt_input(self) -> typing.Optional["LexIntentFollowUpPromptPrompt"]:
        return typing.cast(typing.Optional["LexIntentFollowUpPromptPrompt"], jsii.get(self, "promptInput"))

    @builtins.property
    @jsii.member(jsii_name="rejectionStatementInput")
    def rejection_statement_input(
        self,
    ) -> typing.Optional["LexIntentFollowUpPromptRejectionStatement"]:
        return typing.cast(typing.Optional["LexIntentFollowUpPromptRejectionStatement"], jsii.get(self, "rejectionStatementInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LexIntentFollowUpPrompt]:
        return typing.cast(typing.Optional[LexIntentFollowUpPrompt], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[LexIntentFollowUpPrompt]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d5a3a7fd54d7a4e046432a2e2118c77bba5d703640632fb555e221bde4a6d00)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.lexIntent.LexIntentFollowUpPromptPrompt",
    jsii_struct_bases=[],
    name_mapping={
        "max_attempts": "maxAttempts",
        "message": "message",
        "response_card": "responseCard",
    },
)
class LexIntentFollowUpPromptPrompt:
    def __init__(
        self,
        *,
        max_attempts: jsii.Number,
        message: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LexIntentFollowUpPromptPromptMessage", typing.Dict[builtins.str, typing.Any]]]],
        response_card: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param max_attempts: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#max_attempts LexIntent#max_attempts}.
        :param message: message block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#message LexIntent#message}
        :param response_card: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#response_card LexIntent#response_card}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__325fa2feb6770b38b30ea96ee992df28e086bb38c0cfcc0fe72a84483180e03b)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#max_attempts LexIntent#max_attempts}.'''
        result = self._values.get("max_attempts")
        assert result is not None, "Required property 'max_attempts' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def message(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LexIntentFollowUpPromptPromptMessage"]]:
        '''message block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#message LexIntent#message}
        '''
        result = self._values.get("message")
        assert result is not None, "Required property 'message' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LexIntentFollowUpPromptPromptMessage"]], result)

    @builtins.property
    def response_card(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#response_card LexIntent#response_card}.'''
        result = self._values.get("response_card")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LexIntentFollowUpPromptPrompt(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.lexIntent.LexIntentFollowUpPromptPromptMessage",
    jsii_struct_bases=[],
    name_mapping={
        "content": "content",
        "content_type": "contentType",
        "group_number": "groupNumber",
    },
)
class LexIntentFollowUpPromptPromptMessage:
    def __init__(
        self,
        *,
        content: builtins.str,
        content_type: builtins.str,
        group_number: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param content: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#content LexIntent#content}.
        :param content_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#content_type LexIntent#content_type}.
        :param group_number: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#group_number LexIntent#group_number}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f8ccee2d2aba1ed3fb8c7fe3c40f08ac3c303ea25b7c63de4bd7667d28a1f0c)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#content LexIntent#content}.'''
        result = self._values.get("content")
        assert result is not None, "Required property 'content' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def content_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#content_type LexIntent#content_type}.'''
        result = self._values.get("content_type")
        assert result is not None, "Required property 'content_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def group_number(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#group_number LexIntent#group_number}.'''
        result = self._values.get("group_number")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LexIntentFollowUpPromptPromptMessage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LexIntentFollowUpPromptPromptMessageList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lexIntent.LexIntentFollowUpPromptPromptMessageList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f78aa1272fe1c0cb88e86656e457b1ed502a52ddfd608940cc3bec07760394d7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LexIntentFollowUpPromptPromptMessageOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__268320abeed4354fba950e0b14828fcca921222897a0930a4007bd24baf3ce39)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LexIntentFollowUpPromptPromptMessageOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc53bf91b26d42ac6757af9df8ccc7b7447faa27e359ce759f46c8c22caca80d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3d2588556c5148c2ce4f12dc818e260a6c6031925de48151befd6ee8c36d7977)
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
            type_hints = typing.get_type_hints(_typecheckingstub__beac6c0d077581739be1bb2227a65269e882adea25864dd6b910cefc9e9713a9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LexIntentFollowUpPromptPromptMessage]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LexIntentFollowUpPromptPromptMessage]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LexIntentFollowUpPromptPromptMessage]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57db5224062b0a1662a11863d7f10da08d0685071f2eb452d1e17b772bd9cff8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LexIntentFollowUpPromptPromptMessageOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lexIntent.LexIntentFollowUpPromptPromptMessageOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__69d9e47cc7234a5a9174d51e4ee6e8d5f51ef76746a76c6e023ec5629b2da1d8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__05ff384368cbafcaafce53d15b2a9c5f58474458da8ff77a7e9f6e3ed16bd346)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "content", value)

    @builtins.property
    @jsii.member(jsii_name="contentType")
    def content_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentType"))

    @content_type.setter
    def content_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c2012d45c8136f591e9e5ce5d3811d5e871533307193362387b0781d07d97e0a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentType", value)

    @builtins.property
    @jsii.member(jsii_name="groupNumber")
    def group_number(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "groupNumber"))

    @group_number.setter
    def group_number(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe0ad3d1f1858223c3b3d59022d6dd212364a339b32c381e08d1e4c8160c4afb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupNumber", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LexIntentFollowUpPromptPromptMessage, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LexIntentFollowUpPromptPromptMessage, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LexIntentFollowUpPromptPromptMessage, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad45ff7b45f5b1d1d9aef1d4ce17c4be0770fe3a6130a56133ac8d884b88a8db)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LexIntentFollowUpPromptPromptOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lexIntent.LexIntentFollowUpPromptPromptOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__32347601e7befb2c88470045a4a1ba90d14112f2066cc8fc0f3dea0d9ffd2d8e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMessage")
    def put_message(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LexIntentFollowUpPromptPromptMessage, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b5f6a9c38dd218b1d7977359e7c37ae93fcaac4f786378a00d1ca6f283ba4e31)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMessage", [value]))

    @jsii.member(jsii_name="resetResponseCard")
    def reset_response_card(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResponseCard", []))

    @builtins.property
    @jsii.member(jsii_name="message")
    def message(self) -> LexIntentFollowUpPromptPromptMessageList:
        return typing.cast(LexIntentFollowUpPromptPromptMessageList, jsii.get(self, "message"))

    @builtins.property
    @jsii.member(jsii_name="maxAttemptsInput")
    def max_attempts_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxAttemptsInput"))

    @builtins.property
    @jsii.member(jsii_name="messageInput")
    def message_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LexIntentFollowUpPromptPromptMessage]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LexIntentFollowUpPromptPromptMessage]]], jsii.get(self, "messageInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__913a1643dcd6d7e0156906259d7b9e1a4d386f628f33495d24213d1602f4ce5d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxAttempts", value)

    @builtins.property
    @jsii.member(jsii_name="responseCard")
    def response_card(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "responseCard"))

    @response_card.setter
    def response_card(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b5a5be256fe2b85409e04be33bb16ae120e81fd44106e517eb50c34061be0051)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "responseCard", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LexIntentFollowUpPromptPrompt]:
        return typing.cast(typing.Optional[LexIntentFollowUpPromptPrompt], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LexIntentFollowUpPromptPrompt],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af5fd3358263a0b40b7c4be7a936ee487293664b40bb66c707af13cadda3953d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.lexIntent.LexIntentFollowUpPromptRejectionStatement",
    jsii_struct_bases=[],
    name_mapping={"message": "message", "response_card": "responseCard"},
)
class LexIntentFollowUpPromptRejectionStatement:
    def __init__(
        self,
        *,
        message: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LexIntentFollowUpPromptRejectionStatementMessage", typing.Dict[builtins.str, typing.Any]]]],
        response_card: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param message: message block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#message LexIntent#message}
        :param response_card: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#response_card LexIntent#response_card}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3961e87b9d75f3640e50c77e1fbc8eff9b27054e5258eeef3c2445f668c7956f)
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
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LexIntentFollowUpPromptRejectionStatementMessage"]]:
        '''message block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#message LexIntent#message}
        '''
        result = self._values.get("message")
        assert result is not None, "Required property 'message' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LexIntentFollowUpPromptRejectionStatementMessage"]], result)

    @builtins.property
    def response_card(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#response_card LexIntent#response_card}.'''
        result = self._values.get("response_card")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LexIntentFollowUpPromptRejectionStatement(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.lexIntent.LexIntentFollowUpPromptRejectionStatementMessage",
    jsii_struct_bases=[],
    name_mapping={
        "content": "content",
        "content_type": "contentType",
        "group_number": "groupNumber",
    },
)
class LexIntentFollowUpPromptRejectionStatementMessage:
    def __init__(
        self,
        *,
        content: builtins.str,
        content_type: builtins.str,
        group_number: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param content: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#content LexIntent#content}.
        :param content_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#content_type LexIntent#content_type}.
        :param group_number: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#group_number LexIntent#group_number}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8de0738f0d7cfa3b0a57d9c8a468cea1a43ab90eb9b068d06bf9cdf228f13ce3)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#content LexIntent#content}.'''
        result = self._values.get("content")
        assert result is not None, "Required property 'content' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def content_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#content_type LexIntent#content_type}.'''
        result = self._values.get("content_type")
        assert result is not None, "Required property 'content_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def group_number(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#group_number LexIntent#group_number}.'''
        result = self._values.get("group_number")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LexIntentFollowUpPromptRejectionStatementMessage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LexIntentFollowUpPromptRejectionStatementMessageList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lexIntent.LexIntentFollowUpPromptRejectionStatementMessageList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__537acac637f01a7be06d5fe38faed53efb6291007dd49aecaaa053989f344156)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LexIntentFollowUpPromptRejectionStatementMessageOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__784d19475a60e6a7f7756cecec1bb394ae0d7bff3f71505ffa7a27630dd1a7d8)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LexIntentFollowUpPromptRejectionStatementMessageOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce2b2982bb0ac0b50ae181e7c194b465d15599d7b831e4cea1c6a749bb861bad)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8ec8c7429bd668aaf02baffda0d3cdc7526d95802ce756dce815d2d740a81cdf)
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
            type_hints = typing.get_type_hints(_typecheckingstub__72da39d91c824f0f66aae3420359da54b5963f8f9b8d2067f3aa3bd24a0b96d5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LexIntentFollowUpPromptRejectionStatementMessage]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LexIntentFollowUpPromptRejectionStatementMessage]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LexIntentFollowUpPromptRejectionStatementMessage]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__091004606ddb11b5e763d55e31788db243f96c38ce305465d7b550c0956e545b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LexIntentFollowUpPromptRejectionStatementMessageOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lexIntent.LexIntentFollowUpPromptRejectionStatementMessageOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e462dd14a0a46240f818b983189ba3ca70529af4b97ee7d390118fc8510ce6d6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__79ed9f27045324838c631c944e80b5d90cf86bc8cfbda6c5b77972c98c25054e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "content", value)

    @builtins.property
    @jsii.member(jsii_name="contentType")
    def content_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentType"))

    @content_type.setter
    def content_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25d7956476a3cc5d47f96e8ea2f35cd90fe78b04cfd7cfa0935aa7911ba0fe8a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentType", value)

    @builtins.property
    @jsii.member(jsii_name="groupNumber")
    def group_number(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "groupNumber"))

    @group_number.setter
    def group_number(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__854aeaa83f9f7f6f54557e4719ea2bde20ac2c24da753c675828ac343f511054)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupNumber", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LexIntentFollowUpPromptRejectionStatementMessage, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LexIntentFollowUpPromptRejectionStatementMessage, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LexIntentFollowUpPromptRejectionStatementMessage, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4365004aa62a7f7361897398dc98fd106566954bf5dbee08b9e3d99cfcdce8a8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LexIntentFollowUpPromptRejectionStatementOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lexIntent.LexIntentFollowUpPromptRejectionStatementOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5a4a33ab9512423b58d3af6c167b0a2cc8d45c111b64fa461565e36c8a789aa3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMessage")
    def put_message(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LexIntentFollowUpPromptRejectionStatementMessage, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c32e21b9fc1b0347f529f133ce654e35259cf572a16ab1b3fafc8f6f2b5f11c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMessage", [value]))

    @jsii.member(jsii_name="resetResponseCard")
    def reset_response_card(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResponseCard", []))

    @builtins.property
    @jsii.member(jsii_name="message")
    def message(self) -> LexIntentFollowUpPromptRejectionStatementMessageList:
        return typing.cast(LexIntentFollowUpPromptRejectionStatementMessageList, jsii.get(self, "message"))

    @builtins.property
    @jsii.member(jsii_name="messageInput")
    def message_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LexIntentFollowUpPromptRejectionStatementMessage]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LexIntentFollowUpPromptRejectionStatementMessage]]], jsii.get(self, "messageInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__d8bcb8df1fb272d25c103d53d90043af497fb2d383d6f0f5dca6358e047c0aa9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "responseCard", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LexIntentFollowUpPromptRejectionStatement]:
        return typing.cast(typing.Optional[LexIntentFollowUpPromptRejectionStatement], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LexIntentFollowUpPromptRejectionStatement],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb9300a1ab360db5f11aa799295bdac0b5f35dc344e581b046ef27b416ce317e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.lexIntent.LexIntentFulfillmentActivity",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "code_hook": "codeHook"},
)
class LexIntentFulfillmentActivity:
    def __init__(
        self,
        *,
        type: builtins.str,
        code_hook: typing.Optional[typing.Union["LexIntentFulfillmentActivityCodeHook", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#type LexIntent#type}.
        :param code_hook: code_hook block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#code_hook LexIntent#code_hook}
        '''
        if isinstance(code_hook, dict):
            code_hook = LexIntentFulfillmentActivityCodeHook(**code_hook)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c618f21579ace3a3133db57b762d7566844a0966d78227f04fb920ec450010e)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument code_hook", value=code_hook, expected_type=type_hints["code_hook"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }
        if code_hook is not None:
            self._values["code_hook"] = code_hook

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#type LexIntent#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def code_hook(self) -> typing.Optional["LexIntentFulfillmentActivityCodeHook"]:
        '''code_hook block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#code_hook LexIntent#code_hook}
        '''
        result = self._values.get("code_hook")
        return typing.cast(typing.Optional["LexIntentFulfillmentActivityCodeHook"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LexIntentFulfillmentActivity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.lexIntent.LexIntentFulfillmentActivityCodeHook",
    jsii_struct_bases=[],
    name_mapping={"message_version": "messageVersion", "uri": "uri"},
)
class LexIntentFulfillmentActivityCodeHook:
    def __init__(self, *, message_version: builtins.str, uri: builtins.str) -> None:
        '''
        :param message_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#message_version LexIntent#message_version}.
        :param uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#uri LexIntent#uri}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19712b5a64ec15018c95a2dfa398afa348edd77c010ccd503c7c77538bf2e4aa)
            check_type(argname="argument message_version", value=message_version, expected_type=type_hints["message_version"])
            check_type(argname="argument uri", value=uri, expected_type=type_hints["uri"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "message_version": message_version,
            "uri": uri,
        }

    @builtins.property
    def message_version(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#message_version LexIntent#message_version}.'''
        result = self._values.get("message_version")
        assert result is not None, "Required property 'message_version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def uri(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#uri LexIntent#uri}.'''
        result = self._values.get("uri")
        assert result is not None, "Required property 'uri' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LexIntentFulfillmentActivityCodeHook(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LexIntentFulfillmentActivityCodeHookOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lexIntent.LexIntentFulfillmentActivityCodeHookOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__74f9154ccdd39610498d33fe088fc8321c91b2a52e0121c8a0712561e9fe44f9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="messageVersionInput")
    def message_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "messageVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="uriInput")
    def uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "uriInput"))

    @builtins.property
    @jsii.member(jsii_name="messageVersion")
    def message_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "messageVersion"))

    @message_version.setter
    def message_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d8b7b68a74cf4e049c4c30e03aac00eeee23e8abcdbb304c512fa9be79e5b4d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "messageVersion", value)

    @builtins.property
    @jsii.member(jsii_name="uri")
    def uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uri"))

    @uri.setter
    def uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4addb2a5000b574dbd5bcf14c652555da50f653823ed07bb934d0fb7136ffcc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "uri", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LexIntentFulfillmentActivityCodeHook]:
        return typing.cast(typing.Optional[LexIntentFulfillmentActivityCodeHook], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LexIntentFulfillmentActivityCodeHook],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ce5b462a7dc4e304ed364de0f0a413aaa80314f8817bc2943ab2150a8744051)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LexIntentFulfillmentActivityOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lexIntent.LexIntentFulfillmentActivityOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__531434810bcc663dee3a258c4cfd9c100c90e6310cd6f3e0917de73aa20c5826)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCodeHook")
    def put_code_hook(
        self,
        *,
        message_version: builtins.str,
        uri: builtins.str,
    ) -> None:
        '''
        :param message_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#message_version LexIntent#message_version}.
        :param uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#uri LexIntent#uri}.
        '''
        value = LexIntentFulfillmentActivityCodeHook(
            message_version=message_version, uri=uri
        )

        return typing.cast(None, jsii.invoke(self, "putCodeHook", [value]))

    @jsii.member(jsii_name="resetCodeHook")
    def reset_code_hook(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCodeHook", []))

    @builtins.property
    @jsii.member(jsii_name="codeHook")
    def code_hook(self) -> LexIntentFulfillmentActivityCodeHookOutputReference:
        return typing.cast(LexIntentFulfillmentActivityCodeHookOutputReference, jsii.get(self, "codeHook"))

    @builtins.property
    @jsii.member(jsii_name="codeHookInput")
    def code_hook_input(self) -> typing.Optional[LexIntentFulfillmentActivityCodeHook]:
        return typing.cast(typing.Optional[LexIntentFulfillmentActivityCodeHook], jsii.get(self, "codeHookInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd88a7310c40228fd8c884a27e772ad4cd3954a49ce451f393939d272266641e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LexIntentFulfillmentActivity]:
        return typing.cast(typing.Optional[LexIntentFulfillmentActivity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LexIntentFulfillmentActivity],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5db1f1870f55088873c93ca9c715d92dcd90118c08beb35e508a877aac78d778)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.lexIntent.LexIntentRejectionStatement",
    jsii_struct_bases=[],
    name_mapping={"message": "message", "response_card": "responseCard"},
)
class LexIntentRejectionStatement:
    def __init__(
        self,
        *,
        message: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LexIntentRejectionStatementMessage", typing.Dict[builtins.str, typing.Any]]]],
        response_card: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param message: message block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#message LexIntent#message}
        :param response_card: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#response_card LexIntent#response_card}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae220a56545ee9ca0b58bc7da8b8063bf44f5e5d2f22175c8266c32fe8de4729)
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
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LexIntentRejectionStatementMessage"]]:
        '''message block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#message LexIntent#message}
        '''
        result = self._values.get("message")
        assert result is not None, "Required property 'message' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LexIntentRejectionStatementMessage"]], result)

    @builtins.property
    def response_card(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#response_card LexIntent#response_card}.'''
        result = self._values.get("response_card")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LexIntentRejectionStatement(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.lexIntent.LexIntentRejectionStatementMessage",
    jsii_struct_bases=[],
    name_mapping={
        "content": "content",
        "content_type": "contentType",
        "group_number": "groupNumber",
    },
)
class LexIntentRejectionStatementMessage:
    def __init__(
        self,
        *,
        content: builtins.str,
        content_type: builtins.str,
        group_number: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param content: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#content LexIntent#content}.
        :param content_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#content_type LexIntent#content_type}.
        :param group_number: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#group_number LexIntent#group_number}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__caaf6deb6172b05e07bb87fdccc152ce4d27d337d04f29b1f71414896df69608)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#content LexIntent#content}.'''
        result = self._values.get("content")
        assert result is not None, "Required property 'content' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def content_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#content_type LexIntent#content_type}.'''
        result = self._values.get("content_type")
        assert result is not None, "Required property 'content_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def group_number(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#group_number LexIntent#group_number}.'''
        result = self._values.get("group_number")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LexIntentRejectionStatementMessage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LexIntentRejectionStatementMessageList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lexIntent.LexIntentRejectionStatementMessageList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__27efd5ea43515bcd7c57254ab181575157a5b9dd3a016b0ad49a256770aabdb2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LexIntentRejectionStatementMessageOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__83823d805293be720a079328e79876c32ef83b72e79e44965c4b94058842b8e2)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LexIntentRejectionStatementMessageOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12d874dd0beace32a305fd2b039fe4428d7e90311e46d041b7cbf67000717643)
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
            type_hints = typing.get_type_hints(_typecheckingstub__42ed16be5fe6c3d939963cd25e67ec6290184c5f4135f6ffe085991fc1d19823)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a92c5f8a92ea1b83cfa73db2c1358c86b42d914a9c2c1942eb3fc2e5e5aeae29)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LexIntentRejectionStatementMessage]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LexIntentRejectionStatementMessage]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LexIntentRejectionStatementMessage]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f7bcaae90dfa230f916a488ecd14127328f6e03c75b9d2e984da8e7b8d453d9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LexIntentRejectionStatementMessageOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lexIntent.LexIntentRejectionStatementMessageOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cbea702a2d790bca1ca3a74e384b4b124256fee042eaf089e400c6455f9838d3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0dd4eec12a18d560e5881ecaa1b4e231996fcf60601606cb6e9f6906103ec83d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "content", value)

    @builtins.property
    @jsii.member(jsii_name="contentType")
    def content_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentType"))

    @content_type.setter
    def content_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d38c1a219679ca2c6271c2ef267bee79692a8dcd92afbe80c349459ca3263bcb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentType", value)

    @builtins.property
    @jsii.member(jsii_name="groupNumber")
    def group_number(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "groupNumber"))

    @group_number.setter
    def group_number(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2051833dbb28744503e554ea7c7c70015bcaf234aa550e3c5fcaa67087b9cbf0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupNumber", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LexIntentRejectionStatementMessage, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LexIntentRejectionStatementMessage, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LexIntentRejectionStatementMessage, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc0271355564af0e7cc1a2b7344fc5367dd9cb8bcfcd6201e11cde2c9730387e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LexIntentRejectionStatementOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lexIntent.LexIntentRejectionStatementOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8897fbff959bf2dca72fa1bd3fbadfda9d3a6d9a390e40260a03c88d0667fd7b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMessage")
    def put_message(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LexIntentRejectionStatementMessage, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5422808565aeabfb1980c56c7cac379aa97a6a863405f17d4a08adc2b4a83e61)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMessage", [value]))

    @jsii.member(jsii_name="resetResponseCard")
    def reset_response_card(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResponseCard", []))

    @builtins.property
    @jsii.member(jsii_name="message")
    def message(self) -> LexIntentRejectionStatementMessageList:
        return typing.cast(LexIntentRejectionStatementMessageList, jsii.get(self, "message"))

    @builtins.property
    @jsii.member(jsii_name="messageInput")
    def message_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LexIntentRejectionStatementMessage]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LexIntentRejectionStatementMessage]]], jsii.get(self, "messageInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__f87178c240c973933ee319ab6a25cffd1627b6ba871593cc344d5104a82fb5a8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "responseCard", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LexIntentRejectionStatement]:
        return typing.cast(typing.Optional[LexIntentRejectionStatement], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LexIntentRejectionStatement],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf219f28d07de58271534e8e689fe022ab97f893dd7eada7426689ae30685a46)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.lexIntent.LexIntentSlot",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "slot_constraint": "slotConstraint",
        "slot_type": "slotType",
        "description": "description",
        "priority": "priority",
        "response_card": "responseCard",
        "sample_utterances": "sampleUtterances",
        "slot_type_version": "slotTypeVersion",
        "value_elicitation_prompt": "valueElicitationPrompt",
    },
)
class LexIntentSlot:
    def __init__(
        self,
        *,
        name: builtins.str,
        slot_constraint: builtins.str,
        slot_type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        priority: typing.Optional[jsii.Number] = None,
        response_card: typing.Optional[builtins.str] = None,
        sample_utterances: typing.Optional[typing.Sequence[builtins.str]] = None,
        slot_type_version: typing.Optional[builtins.str] = None,
        value_elicitation_prompt: typing.Optional[typing.Union["LexIntentSlotValueElicitationPrompt", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#name LexIntent#name}.
        :param slot_constraint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#slot_constraint LexIntent#slot_constraint}.
        :param slot_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#slot_type LexIntent#slot_type}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#description LexIntent#description}.
        :param priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#priority LexIntent#priority}.
        :param response_card: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#response_card LexIntent#response_card}.
        :param sample_utterances: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#sample_utterances LexIntent#sample_utterances}.
        :param slot_type_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#slot_type_version LexIntent#slot_type_version}.
        :param value_elicitation_prompt: value_elicitation_prompt block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#value_elicitation_prompt LexIntent#value_elicitation_prompt}
        '''
        if isinstance(value_elicitation_prompt, dict):
            value_elicitation_prompt = LexIntentSlotValueElicitationPrompt(**value_elicitation_prompt)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__958b216637df1dea0b6ff9a21fc1e335ae0a3477b09ab9a93de5eecfce69764e)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument slot_constraint", value=slot_constraint, expected_type=type_hints["slot_constraint"])
            check_type(argname="argument slot_type", value=slot_type, expected_type=type_hints["slot_type"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument response_card", value=response_card, expected_type=type_hints["response_card"])
            check_type(argname="argument sample_utterances", value=sample_utterances, expected_type=type_hints["sample_utterances"])
            check_type(argname="argument slot_type_version", value=slot_type_version, expected_type=type_hints["slot_type_version"])
            check_type(argname="argument value_elicitation_prompt", value=value_elicitation_prompt, expected_type=type_hints["value_elicitation_prompt"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "slot_constraint": slot_constraint,
            "slot_type": slot_type,
        }
        if description is not None:
            self._values["description"] = description
        if priority is not None:
            self._values["priority"] = priority
        if response_card is not None:
            self._values["response_card"] = response_card
        if sample_utterances is not None:
            self._values["sample_utterances"] = sample_utterances
        if slot_type_version is not None:
            self._values["slot_type_version"] = slot_type_version
        if value_elicitation_prompt is not None:
            self._values["value_elicitation_prompt"] = value_elicitation_prompt

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#name LexIntent#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def slot_constraint(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#slot_constraint LexIntent#slot_constraint}.'''
        result = self._values.get("slot_constraint")
        assert result is not None, "Required property 'slot_constraint' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def slot_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#slot_type LexIntent#slot_type}.'''
        result = self._values.get("slot_type")
        assert result is not None, "Required property 'slot_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#description LexIntent#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def priority(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#priority LexIntent#priority}.'''
        result = self._values.get("priority")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def response_card(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#response_card LexIntent#response_card}.'''
        result = self._values.get("response_card")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sample_utterances(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#sample_utterances LexIntent#sample_utterances}.'''
        result = self._values.get("sample_utterances")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def slot_type_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#slot_type_version LexIntent#slot_type_version}.'''
        result = self._values.get("slot_type_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value_elicitation_prompt(
        self,
    ) -> typing.Optional["LexIntentSlotValueElicitationPrompt"]:
        '''value_elicitation_prompt block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#value_elicitation_prompt LexIntent#value_elicitation_prompt}
        '''
        result = self._values.get("value_elicitation_prompt")
        return typing.cast(typing.Optional["LexIntentSlotValueElicitationPrompt"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LexIntentSlot(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LexIntentSlotList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lexIntent.LexIntentSlotList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7d5335984a36f99df9433083ba90edd4167b6064e19a23e30b3533c92a3641f5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "LexIntentSlotOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84bee784f90c170ce6e78568c6624464b98f0437b06ca9d42cf01f5a498d602c)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LexIntentSlotOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__518f59a5758f193f84d512b5ef5dc99836a2348fec38072ffb6ba224e032c12e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9ca9498ae0bade31a9ac9514dd3493dfc76fafc809ad2b84f31a5e3b6a671acb)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f6dd93a656c83cea22373c78c96c88faa145d3c303bcd64504d38b76af30f7a9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LexIntentSlot]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LexIntentSlot]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LexIntentSlot]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60e6f6c2a4dad416d98c6a1eb6730b1a0a0ad80025938d8d6cfc9477ec9a080a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LexIntentSlotOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lexIntent.LexIntentSlotOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3aea23306911a7d763116eb9514fc68b68b3c421c521e69fc646de0a5f572c47)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putValueElicitationPrompt")
    def put_value_elicitation_prompt(
        self,
        *,
        max_attempts: jsii.Number,
        message: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LexIntentSlotValueElicitationPromptMessage", typing.Dict[builtins.str, typing.Any]]]],
        response_card: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param max_attempts: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#max_attempts LexIntent#max_attempts}.
        :param message: message block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#message LexIntent#message}
        :param response_card: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#response_card LexIntent#response_card}.
        '''
        value = LexIntentSlotValueElicitationPrompt(
            max_attempts=max_attempts, message=message, response_card=response_card
        )

        return typing.cast(None, jsii.invoke(self, "putValueElicitationPrompt", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetPriority")
    def reset_priority(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPriority", []))

    @jsii.member(jsii_name="resetResponseCard")
    def reset_response_card(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResponseCard", []))

    @jsii.member(jsii_name="resetSampleUtterances")
    def reset_sample_utterances(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSampleUtterances", []))

    @jsii.member(jsii_name="resetSlotTypeVersion")
    def reset_slot_type_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSlotTypeVersion", []))

    @jsii.member(jsii_name="resetValueElicitationPrompt")
    def reset_value_elicitation_prompt(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValueElicitationPrompt", []))

    @builtins.property
    @jsii.member(jsii_name="valueElicitationPrompt")
    def value_elicitation_prompt(
        self,
    ) -> "LexIntentSlotValueElicitationPromptOutputReference":
        return typing.cast("LexIntentSlotValueElicitationPromptOutputReference", jsii.get(self, "valueElicitationPrompt"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="priorityInput")
    def priority_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "priorityInput"))

    @builtins.property
    @jsii.member(jsii_name="responseCardInput")
    def response_card_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "responseCardInput"))

    @builtins.property
    @jsii.member(jsii_name="sampleUtterancesInput")
    def sample_utterances_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sampleUtterancesInput"))

    @builtins.property
    @jsii.member(jsii_name="slotConstraintInput")
    def slot_constraint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "slotConstraintInput"))

    @builtins.property
    @jsii.member(jsii_name="slotTypeInput")
    def slot_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "slotTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="slotTypeVersionInput")
    def slot_type_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "slotTypeVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="valueElicitationPromptInput")
    def value_elicitation_prompt_input(
        self,
    ) -> typing.Optional["LexIntentSlotValueElicitationPrompt"]:
        return typing.cast(typing.Optional["LexIntentSlotValueElicitationPrompt"], jsii.get(self, "valueElicitationPromptInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35238168c3c5986d3ab495a94d01a6ff4cd5f5f3df7eb9b0bb9a07bd377cf2ca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1c33141d72bb2feaa122aa81ff9af264a6efabd975860e2d72cbf3ed354f2c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2759db4514cc67f2094f605cb624d6e1ed685b24e7290dcd5c0d51c0aaa68c77)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)

    @builtins.property
    @jsii.member(jsii_name="responseCard")
    def response_card(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "responseCard"))

    @response_card.setter
    def response_card(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d03bf54d0dd109d02d1975a6c953e39c8c2c78f65f594377f541a2cddaba02b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "responseCard", value)

    @builtins.property
    @jsii.member(jsii_name="sampleUtterances")
    def sample_utterances(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sampleUtterances"))

    @sample_utterances.setter
    def sample_utterances(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__decb460091619cff47ba39563d0a842e83dcc3637cf064759019524dd207a7a0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sampleUtterances", value)

    @builtins.property
    @jsii.member(jsii_name="slotConstraint")
    def slot_constraint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "slotConstraint"))

    @slot_constraint.setter
    def slot_constraint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c57b8d24f1c04efaa33af50f4973191fa906d9cd287a0e2d381febc811433dd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "slotConstraint", value)

    @builtins.property
    @jsii.member(jsii_name="slotType")
    def slot_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "slotType"))

    @slot_type.setter
    def slot_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4550669574140bb2bc134ee5347494f6960eb47517945045a3aa6b2ca0a5e4ff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "slotType", value)

    @builtins.property
    @jsii.member(jsii_name="slotTypeVersion")
    def slot_type_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "slotTypeVersion"))

    @slot_type_version.setter
    def slot_type_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ca67738549052390282b6572532adb30de4b68ee48c7a33cc4332a03045da7d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "slotTypeVersion", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LexIntentSlot, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LexIntentSlot, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LexIntentSlot, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db26fd34645dbde61b3d8c91702ca16f2ac0a4f56fcd896c36e8b3d38f5f8930)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.lexIntent.LexIntentSlotValueElicitationPrompt",
    jsii_struct_bases=[],
    name_mapping={
        "max_attempts": "maxAttempts",
        "message": "message",
        "response_card": "responseCard",
    },
)
class LexIntentSlotValueElicitationPrompt:
    def __init__(
        self,
        *,
        max_attempts: jsii.Number,
        message: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LexIntentSlotValueElicitationPromptMessage", typing.Dict[builtins.str, typing.Any]]]],
        response_card: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param max_attempts: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#max_attempts LexIntent#max_attempts}.
        :param message: message block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#message LexIntent#message}
        :param response_card: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#response_card LexIntent#response_card}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__71f9133c30bcbe325d38fbf9e7fbd62aff7d2fe735788a3b42e8a539658f2de9)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#max_attempts LexIntent#max_attempts}.'''
        result = self._values.get("max_attempts")
        assert result is not None, "Required property 'max_attempts' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def message(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LexIntentSlotValueElicitationPromptMessage"]]:
        '''message block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#message LexIntent#message}
        '''
        result = self._values.get("message")
        assert result is not None, "Required property 'message' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LexIntentSlotValueElicitationPromptMessage"]], result)

    @builtins.property
    def response_card(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#response_card LexIntent#response_card}.'''
        result = self._values.get("response_card")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LexIntentSlotValueElicitationPrompt(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.lexIntent.LexIntentSlotValueElicitationPromptMessage",
    jsii_struct_bases=[],
    name_mapping={
        "content": "content",
        "content_type": "contentType",
        "group_number": "groupNumber",
    },
)
class LexIntentSlotValueElicitationPromptMessage:
    def __init__(
        self,
        *,
        content: builtins.str,
        content_type: builtins.str,
        group_number: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param content: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#content LexIntent#content}.
        :param content_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#content_type LexIntent#content_type}.
        :param group_number: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#group_number LexIntent#group_number}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__51d30ab4d2879e1f1c5e6836a9898cf8fa12a055f76fafb7e18058249ef5ab7c)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#content LexIntent#content}.'''
        result = self._values.get("content")
        assert result is not None, "Required property 'content' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def content_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#content_type LexIntent#content_type}.'''
        result = self._values.get("content_type")
        assert result is not None, "Required property 'content_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def group_number(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#group_number LexIntent#group_number}.'''
        result = self._values.get("group_number")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LexIntentSlotValueElicitationPromptMessage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LexIntentSlotValueElicitationPromptMessageList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lexIntent.LexIntentSlotValueElicitationPromptMessageList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__571de6a790c245e850e55307770aa88df977f4ff7311b49fb300550c1e812462)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LexIntentSlotValueElicitationPromptMessageOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd3b049cefb830ae26589d96b80fce590c32080fd417ccdf56a6b4781855c764)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LexIntentSlotValueElicitationPromptMessageOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__317cc1a78ca6b97b8961ee1f3a5637d862e2225987a7611b864ab7db7874c097)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9e1a2243732d22d83cf433c13e352d03042906406f3a0b12a31fedc516688ed2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3f35a24be1693054c31309c7d1448eac783063888c5b90e92bd4aeaf25daee01)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LexIntentSlotValueElicitationPromptMessage]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LexIntentSlotValueElicitationPromptMessage]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LexIntentSlotValueElicitationPromptMessage]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7feb4479805d7d9c08cfc3a64f22956ad0e954d58f808bd0eb4597634d661aca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LexIntentSlotValueElicitationPromptMessageOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lexIntent.LexIntentSlotValueElicitationPromptMessageOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f68ec455e30f18901d74dc5bc677818191133a2ba1b03ee8cd61ab48b5cf0535)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7c24cdb8818ce7a5c550f83f622a6a1d20986994c5f0046ffed9927997f368ad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "content", value)

    @builtins.property
    @jsii.member(jsii_name="contentType")
    def content_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentType"))

    @content_type.setter
    def content_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc3d98697cb6a41d8e9ef51b97ae9b30e5a68b0f5f60aebee79a8f088d90f05d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentType", value)

    @builtins.property
    @jsii.member(jsii_name="groupNumber")
    def group_number(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "groupNumber"))

    @group_number.setter
    def group_number(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77a92ec416700378078fdabb47f2afaeb34c8eeeecd70b4dff0645f2a2048f41)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupNumber", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LexIntentSlotValueElicitationPromptMessage, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LexIntentSlotValueElicitationPromptMessage, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LexIntentSlotValueElicitationPromptMessage, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf1b21332f3173bbfd4e6e5c5924e5e4a6c5b7f2e733cd9b7b6dd53cd0996935)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LexIntentSlotValueElicitationPromptOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lexIntent.LexIntentSlotValueElicitationPromptOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b15a10c732023ba94298604ace6c45ab85a5898a549263a6024cc4c12dbbc53f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMessage")
    def put_message(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LexIntentSlotValueElicitationPromptMessage, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d64602dd68d63d03d87fc86d27e40f3a682eff06eba80f896754d43d0be311de)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMessage", [value]))

    @jsii.member(jsii_name="resetResponseCard")
    def reset_response_card(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResponseCard", []))

    @builtins.property
    @jsii.member(jsii_name="message")
    def message(self) -> LexIntentSlotValueElicitationPromptMessageList:
        return typing.cast(LexIntentSlotValueElicitationPromptMessageList, jsii.get(self, "message"))

    @builtins.property
    @jsii.member(jsii_name="maxAttemptsInput")
    def max_attempts_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxAttemptsInput"))

    @builtins.property
    @jsii.member(jsii_name="messageInput")
    def message_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LexIntentSlotValueElicitationPromptMessage]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LexIntentSlotValueElicitationPromptMessage]]], jsii.get(self, "messageInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__309a36d9b0215b0e16e1a2c068918af408ba9ddd4873f8f333ace6abd3d280cb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxAttempts", value)

    @builtins.property
    @jsii.member(jsii_name="responseCard")
    def response_card(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "responseCard"))

    @response_card.setter
    def response_card(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f2c517ee39eea7a74d951a8810230fca8757b9ac174abc8c69db648bee41522)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "responseCard", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LexIntentSlotValueElicitationPrompt]:
        return typing.cast(typing.Optional[LexIntentSlotValueElicitationPrompt], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LexIntentSlotValueElicitationPrompt],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__272e296cc7307bf5c1894d9b52e016e61de3fca19f509281f07eb713a7929dfe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.lexIntent.LexIntentTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class LexIntentTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#create LexIntent#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#delete LexIntent#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#update LexIntent#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__edf25b572cfee91cb2fb4b741d23e73072ee392d98dfa9babac49e1ac8abddb0)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#create LexIntent#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#delete LexIntent#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#update LexIntent#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LexIntentTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LexIntentTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lexIntent.LexIntentTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a61a479e1f3fe4534689b297c63ca7212b878bceb2a542e6787f7ba85cf7993f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d3c685c55bbf670481d0a19e4feeeb4eeb67bf9671016bcdab6d3a63edbc25a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9908b2430db7f1e85ffaac3c3a71c00d6b062c98d760d1cc21bada07d8df93cd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03b4af735bbbffef1e43ef7610860af5905f1c41793210fb0465777709ea6bce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LexIntentTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LexIntentTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LexIntentTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__55ff714c6dea69bb15e596c77d425b5eaf14fc071f10b0ce1d6a7dd3c2dfef30)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "LexIntent",
    "LexIntentConclusionStatement",
    "LexIntentConclusionStatementMessage",
    "LexIntentConclusionStatementMessageList",
    "LexIntentConclusionStatementMessageOutputReference",
    "LexIntentConclusionStatementOutputReference",
    "LexIntentConfig",
    "LexIntentConfirmationPrompt",
    "LexIntentConfirmationPromptMessage",
    "LexIntentConfirmationPromptMessageList",
    "LexIntentConfirmationPromptMessageOutputReference",
    "LexIntentConfirmationPromptOutputReference",
    "LexIntentDialogCodeHook",
    "LexIntentDialogCodeHookOutputReference",
    "LexIntentFollowUpPrompt",
    "LexIntentFollowUpPromptOutputReference",
    "LexIntentFollowUpPromptPrompt",
    "LexIntentFollowUpPromptPromptMessage",
    "LexIntentFollowUpPromptPromptMessageList",
    "LexIntentFollowUpPromptPromptMessageOutputReference",
    "LexIntentFollowUpPromptPromptOutputReference",
    "LexIntentFollowUpPromptRejectionStatement",
    "LexIntentFollowUpPromptRejectionStatementMessage",
    "LexIntentFollowUpPromptRejectionStatementMessageList",
    "LexIntentFollowUpPromptRejectionStatementMessageOutputReference",
    "LexIntentFollowUpPromptRejectionStatementOutputReference",
    "LexIntentFulfillmentActivity",
    "LexIntentFulfillmentActivityCodeHook",
    "LexIntentFulfillmentActivityCodeHookOutputReference",
    "LexIntentFulfillmentActivityOutputReference",
    "LexIntentRejectionStatement",
    "LexIntentRejectionStatementMessage",
    "LexIntentRejectionStatementMessageList",
    "LexIntentRejectionStatementMessageOutputReference",
    "LexIntentRejectionStatementOutputReference",
    "LexIntentSlot",
    "LexIntentSlotList",
    "LexIntentSlotOutputReference",
    "LexIntentSlotValueElicitationPrompt",
    "LexIntentSlotValueElicitationPromptMessage",
    "LexIntentSlotValueElicitationPromptMessageList",
    "LexIntentSlotValueElicitationPromptMessageOutputReference",
    "LexIntentSlotValueElicitationPromptOutputReference",
    "LexIntentTimeouts",
    "LexIntentTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__458c41ddde8c77dc6c4abcef2d5661cc959c45ca10aace91513063884c6db991(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    fulfillment_activity: typing.Union[LexIntentFulfillmentActivity, typing.Dict[builtins.str, typing.Any]],
    name: builtins.str,
    conclusion_statement: typing.Optional[typing.Union[LexIntentConclusionStatement, typing.Dict[builtins.str, typing.Any]]] = None,
    confirmation_prompt: typing.Optional[typing.Union[LexIntentConfirmationPrompt, typing.Dict[builtins.str, typing.Any]]] = None,
    create_version: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    description: typing.Optional[builtins.str] = None,
    dialog_code_hook: typing.Optional[typing.Union[LexIntentDialogCodeHook, typing.Dict[builtins.str, typing.Any]]] = None,
    follow_up_prompt: typing.Optional[typing.Union[LexIntentFollowUpPrompt, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    parent_intent_signature: typing.Optional[builtins.str] = None,
    rejection_statement: typing.Optional[typing.Union[LexIntentRejectionStatement, typing.Dict[builtins.str, typing.Any]]] = None,
    sample_utterances: typing.Optional[typing.Sequence[builtins.str]] = None,
    slot: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LexIntentSlot, typing.Dict[builtins.str, typing.Any]]]]] = None,
    timeouts: typing.Optional[typing.Union[LexIntentTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__d9ef4cbc175508744fba9e80bc657cccdedb1feac99daa065a06158ca353abd4(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LexIntentSlot, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50810038e4562fc1af83f112e804d74f6265f7b7ee3989f70a6b9f61c62351c1(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0803ab4467448749dab96d6f66150f9a07ffa43c221a724cf8d18191869468f2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2cedf06c6ae94f908e6160553e8acb613bcf5020e697a31d01ed5ed28d29f4a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__959a2ab8071d0e1d7283f02eeddd65eab763b2e0f453441dd0b65c587b157b59(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5fd4eb393d5f115ab5e6081d799ef7e484184e151a1e3c50261623da293b8f54(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75ead4851b65fca8834f4ff2f94f10bc23b725d2d2524a8d26e458859f5c2938(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__800968169f251595b94e71a1e3c9c80c5fd4188ca995ed0881c0bbd03246a40b(
    *,
    message: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LexIntentConclusionStatementMessage, typing.Dict[builtins.str, typing.Any]]]],
    response_card: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__796562d6d8205c0d1556c371e43e0723ea821faac30924eb8c6035fce5f18f54(
    *,
    content: builtins.str,
    content_type: builtins.str,
    group_number: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5fcb41b4fc1c34ea23dba80076cc2541a2bc22611f85defa27464708e19b8b3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ebc802768bf124771c5652d77c68c1fca975632e40aaa9eb6d8e6d4dfc866c8(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d722c45ec80e8d2cc918bb0d378d397abd5533982869748f3bd82d37a0259b02(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__531a92faf91aaa323e4644c370e6b2fcc768e507019299eb85022e738ec8828f(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df8e71aafea55057c254ee65aff9a8cb646159be6a85f7db0dbb2f25b849816a(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__176bd720cdee5b455c4ab003f4f17250e42e55de3e3c7eb2f510a503055b1396(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LexIntentConclusionStatementMessage]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14ae71101de048f8e9c69afd2687b821aa3c31abe9eb736fcda3fe82c10eb66a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56f678f4825b6b98c6fa1b8067373916ace97674bd87ae7f5c135a7bb45c85ae(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a05bc80d8e05e3c8889751800068aba2ea66c485cd835b2dfb6454aedeeb904(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__738a6e3d4881b8ad5e37ab130bf7d3a3e78a1249a92c514347f061f156a6b9f7(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1643de291b8287f62f720f91b42ef439d4899f423529fcb4d32ef50d1c9ccbb7(
    value: typing.Optional[typing.Union[LexIntentConclusionStatementMessage, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__158929892aa423dd63d273c2f2776e21a8f48cdca529fd377bb719e54ac7d92e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__482807e68b0c6d8ea38859bcb9a6dabbb7f9ee0b2b26eff492cdd89968e08101(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LexIntentConclusionStatementMessage, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10d0f44131052c0bcad3ee933147c026a73e3b4818330057efadcfca6ed060f7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__abb37937b2c96a1f563ff443de2ca0d7ba179e1b66a049de2fa4897cca55ba61(
    value: typing.Optional[LexIntentConclusionStatement],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d360e7cc0c58e5e94d55fcff91db3c02d27a06bbc82f6855204e2af0a2c48454(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    fulfillment_activity: typing.Union[LexIntentFulfillmentActivity, typing.Dict[builtins.str, typing.Any]],
    name: builtins.str,
    conclusion_statement: typing.Optional[typing.Union[LexIntentConclusionStatement, typing.Dict[builtins.str, typing.Any]]] = None,
    confirmation_prompt: typing.Optional[typing.Union[LexIntentConfirmationPrompt, typing.Dict[builtins.str, typing.Any]]] = None,
    create_version: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    description: typing.Optional[builtins.str] = None,
    dialog_code_hook: typing.Optional[typing.Union[LexIntentDialogCodeHook, typing.Dict[builtins.str, typing.Any]]] = None,
    follow_up_prompt: typing.Optional[typing.Union[LexIntentFollowUpPrompt, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    parent_intent_signature: typing.Optional[builtins.str] = None,
    rejection_statement: typing.Optional[typing.Union[LexIntentRejectionStatement, typing.Dict[builtins.str, typing.Any]]] = None,
    sample_utterances: typing.Optional[typing.Sequence[builtins.str]] = None,
    slot: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LexIntentSlot, typing.Dict[builtins.str, typing.Any]]]]] = None,
    timeouts: typing.Optional[typing.Union[LexIntentTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62f1ca124c5eb7e9e3bd9f2730e40ec9546136ddd47a29d3d3f82d0798442096(
    *,
    max_attempts: jsii.Number,
    message: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LexIntentConfirmationPromptMessage, typing.Dict[builtins.str, typing.Any]]]],
    response_card: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae361b23db81673fcb255ca8e4431393a9c98da2c0b615775ce562f077227840(
    *,
    content: builtins.str,
    content_type: builtins.str,
    group_number: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0b4aec7bc133e5de7d10f8e70ad1c4a0c7c9760cc6902b852c1b501fa97bfc8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__931b8de38f5cfd29df95b27f6fb926d222e7d7b9d3c82b4547d0a55137c602fb(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f39168812351059b9d52ecbe4b218645937d2438296fa8863ab2de1129db778d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__512fba6e7139965199eac243f5114cd5dfbbda1a600a054a1c2db443c1b4b122(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1aa9c258e8244d8464ebdee2bce071f5980884d86886d0fc208bdb37e440f447(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c7ca1500ef4fe78ef1ab8978e59c384338650c5c7fa48a0663ac326c5ff99a8(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LexIntentConfirmationPromptMessage]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2082e2676c0ba1a7e00bab4fbcf591f23d48d555e86144add08a02f71422579f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fdb08e87463be3b601c735fa12e2030223d10dd695032b903bf15788cb9ff6eb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82d29d3c02bb722d78a5cf3134819b651f91d4827496648d62e698f9f55a5afe(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67a962f73d10d79bd94b7a1b1a1d06ea863486267f3e49ef6fdbaf1789603746(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0665780a1d23dafc59f2dd8ee0522e9251b582142469f2987f7f8aed42e084b0(
    value: typing.Optional[typing.Union[LexIntentConfirmationPromptMessage, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ddc355321737bca555d66419c74499150ff44c5aa1bed71c89f3c311a4b9fde2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11cad9ff898646ed68215950c7e937a73e3f114ba0cd3a1d78424ca09a7a8498(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LexIntentConfirmationPromptMessage, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ad52d0336e5bbd126cfff70a0ea1c2e85113845a22c67fce0eb2c7714bcbf54(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9999e4228ebdecbbf3b00aa9792ab5e956d055082ee1b4fb8cb48f4b7abea63(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f95df29aea107cd3d9dd9079c5dfefdebc766ee7d6d0e68402e7b9e83d51b9a0(
    value: typing.Optional[LexIntentConfirmationPrompt],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33f02e165e6c1344f4603ee9fde66d731763d1c1c7d0a8fb100a67a0df150d9b(
    *,
    message_version: builtins.str,
    uri: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2f73ba37efea683fc98937c5b421315bd4dd62d1c3e8e7ab85394fb8232a5c4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4e0ea681406a290ccb1e293885f272cbb85fce5606fff16deec3ddd34d24daa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e29e3202ee374ae961d1825c5ec973934a4c0500a0d038aa3f2a6221fc32374(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__378229deb67a8d0fa17563d1aba57d76e3dcae0f56fb5b09449ecc3742b7464c(
    value: typing.Optional[LexIntentDialogCodeHook],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c324b3526ca8823429c257a63ff6db6fde04341c7b7914c157d42f7d8699dee(
    *,
    prompt: typing.Union[LexIntentFollowUpPromptPrompt, typing.Dict[builtins.str, typing.Any]],
    rejection_statement: typing.Union[LexIntentFollowUpPromptRejectionStatement, typing.Dict[builtins.str, typing.Any]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c662ae0b60b2c5bc731deabe153fd269637213b8645dc524fc94a3f9681f86b7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d5a3a7fd54d7a4e046432a2e2118c77bba5d703640632fb555e221bde4a6d00(
    value: typing.Optional[LexIntentFollowUpPrompt],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__325fa2feb6770b38b30ea96ee992df28e086bb38c0cfcc0fe72a84483180e03b(
    *,
    max_attempts: jsii.Number,
    message: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LexIntentFollowUpPromptPromptMessage, typing.Dict[builtins.str, typing.Any]]]],
    response_card: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f8ccee2d2aba1ed3fb8c7fe3c40f08ac3c303ea25b7c63de4bd7667d28a1f0c(
    *,
    content: builtins.str,
    content_type: builtins.str,
    group_number: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f78aa1272fe1c0cb88e86656e457b1ed502a52ddfd608940cc3bec07760394d7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__268320abeed4354fba950e0b14828fcca921222897a0930a4007bd24baf3ce39(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc53bf91b26d42ac6757af9df8ccc7b7447faa27e359ce759f46c8c22caca80d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d2588556c5148c2ce4f12dc818e260a6c6031925de48151befd6ee8c36d7977(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__beac6c0d077581739be1bb2227a65269e882adea25864dd6b910cefc9e9713a9(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57db5224062b0a1662a11863d7f10da08d0685071f2eb452d1e17b772bd9cff8(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LexIntentFollowUpPromptPromptMessage]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69d9e47cc7234a5a9174d51e4ee6e8d5f51ef76746a76c6e023ec5629b2da1d8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05ff384368cbafcaafce53d15b2a9c5f58474458da8ff77a7e9f6e3ed16bd346(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2012d45c8136f591e9e5ce5d3811d5e871533307193362387b0781d07d97e0a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe0ad3d1f1858223c3b3d59022d6dd212364a339b32c381e08d1e4c8160c4afb(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad45ff7b45f5b1d1d9aef1d4ce17c4be0770fe3a6130a56133ac8d884b88a8db(
    value: typing.Optional[typing.Union[LexIntentFollowUpPromptPromptMessage, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32347601e7befb2c88470045a4a1ba90d14112f2066cc8fc0f3dea0d9ffd2d8e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5f6a9c38dd218b1d7977359e7c37ae93fcaac4f786378a00d1ca6f283ba4e31(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LexIntentFollowUpPromptPromptMessage, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__913a1643dcd6d7e0156906259d7b9e1a4d386f628f33495d24213d1602f4ce5d(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5a5be256fe2b85409e04be33bb16ae120e81fd44106e517eb50c34061be0051(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af5fd3358263a0b40b7c4be7a936ee487293664b40bb66c707af13cadda3953d(
    value: typing.Optional[LexIntentFollowUpPromptPrompt],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3961e87b9d75f3640e50c77e1fbc8eff9b27054e5258eeef3c2445f668c7956f(
    *,
    message: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LexIntentFollowUpPromptRejectionStatementMessage, typing.Dict[builtins.str, typing.Any]]]],
    response_card: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8de0738f0d7cfa3b0a57d9c8a468cea1a43ab90eb9b068d06bf9cdf228f13ce3(
    *,
    content: builtins.str,
    content_type: builtins.str,
    group_number: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__537acac637f01a7be06d5fe38faed53efb6291007dd49aecaaa053989f344156(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__784d19475a60e6a7f7756cecec1bb394ae0d7bff3f71505ffa7a27630dd1a7d8(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce2b2982bb0ac0b50ae181e7c194b465d15599d7b831e4cea1c6a749bb861bad(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ec8c7429bd668aaf02baffda0d3cdc7526d95802ce756dce815d2d740a81cdf(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72da39d91c824f0f66aae3420359da54b5963f8f9b8d2067f3aa3bd24a0b96d5(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__091004606ddb11b5e763d55e31788db243f96c38ce305465d7b550c0956e545b(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LexIntentFollowUpPromptRejectionStatementMessage]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e462dd14a0a46240f818b983189ba3ca70529af4b97ee7d390118fc8510ce6d6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79ed9f27045324838c631c944e80b5d90cf86bc8cfbda6c5b77972c98c25054e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25d7956476a3cc5d47f96e8ea2f35cd90fe78b04cfd7cfa0935aa7911ba0fe8a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__854aeaa83f9f7f6f54557e4719ea2bde20ac2c24da753c675828ac343f511054(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4365004aa62a7f7361897398dc98fd106566954bf5dbee08b9e3d99cfcdce8a8(
    value: typing.Optional[typing.Union[LexIntentFollowUpPromptRejectionStatementMessage, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a4a33ab9512423b58d3af6c167b0a2cc8d45c111b64fa461565e36c8a789aa3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c32e21b9fc1b0347f529f133ce654e35259cf572a16ab1b3fafc8f6f2b5f11c(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LexIntentFollowUpPromptRejectionStatementMessage, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8bcb8df1fb272d25c103d53d90043af497fb2d383d6f0f5dca6358e047c0aa9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb9300a1ab360db5f11aa799295bdac0b5f35dc344e581b046ef27b416ce317e(
    value: typing.Optional[LexIntentFollowUpPromptRejectionStatement],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c618f21579ace3a3133db57b762d7566844a0966d78227f04fb920ec450010e(
    *,
    type: builtins.str,
    code_hook: typing.Optional[typing.Union[LexIntentFulfillmentActivityCodeHook, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19712b5a64ec15018c95a2dfa398afa348edd77c010ccd503c7c77538bf2e4aa(
    *,
    message_version: builtins.str,
    uri: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74f9154ccdd39610498d33fe088fc8321c91b2a52e0121c8a0712561e9fe44f9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d8b7b68a74cf4e049c4c30e03aac00eeee23e8abcdbb304c512fa9be79e5b4d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4addb2a5000b574dbd5bcf14c652555da50f653823ed07bb934d0fb7136ffcc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ce5b462a7dc4e304ed364de0f0a413aaa80314f8817bc2943ab2150a8744051(
    value: typing.Optional[LexIntentFulfillmentActivityCodeHook],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__531434810bcc663dee3a258c4cfd9c100c90e6310cd6f3e0917de73aa20c5826(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd88a7310c40228fd8c884a27e772ad4cd3954a49ce451f393939d272266641e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5db1f1870f55088873c93ca9c715d92dcd90118c08beb35e508a877aac78d778(
    value: typing.Optional[LexIntentFulfillmentActivity],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae220a56545ee9ca0b58bc7da8b8063bf44f5e5d2f22175c8266c32fe8de4729(
    *,
    message: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LexIntentRejectionStatementMessage, typing.Dict[builtins.str, typing.Any]]]],
    response_card: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__caaf6deb6172b05e07bb87fdccc152ce4d27d337d04f29b1f71414896df69608(
    *,
    content: builtins.str,
    content_type: builtins.str,
    group_number: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27efd5ea43515bcd7c57254ab181575157a5b9dd3a016b0ad49a256770aabdb2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83823d805293be720a079328e79876c32ef83b72e79e44965c4b94058842b8e2(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12d874dd0beace32a305fd2b039fe4428d7e90311e46d041b7cbf67000717643(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42ed16be5fe6c3d939963cd25e67ec6290184c5f4135f6ffe085991fc1d19823(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a92c5f8a92ea1b83cfa73db2c1358c86b42d914a9c2c1942eb3fc2e5e5aeae29(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f7bcaae90dfa230f916a488ecd14127328f6e03c75b9d2e984da8e7b8d453d9(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LexIntentRejectionStatementMessage]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cbea702a2d790bca1ca3a74e384b4b124256fee042eaf089e400c6455f9838d3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0dd4eec12a18d560e5881ecaa1b4e231996fcf60601606cb6e9f6906103ec83d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d38c1a219679ca2c6271c2ef267bee79692a8dcd92afbe80c349459ca3263bcb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2051833dbb28744503e554ea7c7c70015bcaf234aa550e3c5fcaa67087b9cbf0(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc0271355564af0e7cc1a2b7344fc5367dd9cb8bcfcd6201e11cde2c9730387e(
    value: typing.Optional[typing.Union[LexIntentRejectionStatementMessage, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8897fbff959bf2dca72fa1bd3fbadfda9d3a6d9a390e40260a03c88d0667fd7b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5422808565aeabfb1980c56c7cac379aa97a6a863405f17d4a08adc2b4a83e61(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LexIntentRejectionStatementMessage, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f87178c240c973933ee319ab6a25cffd1627b6ba871593cc344d5104a82fb5a8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf219f28d07de58271534e8e689fe022ab97f893dd7eada7426689ae30685a46(
    value: typing.Optional[LexIntentRejectionStatement],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__958b216637df1dea0b6ff9a21fc1e335ae0a3477b09ab9a93de5eecfce69764e(
    *,
    name: builtins.str,
    slot_constraint: builtins.str,
    slot_type: builtins.str,
    description: typing.Optional[builtins.str] = None,
    priority: typing.Optional[jsii.Number] = None,
    response_card: typing.Optional[builtins.str] = None,
    sample_utterances: typing.Optional[typing.Sequence[builtins.str]] = None,
    slot_type_version: typing.Optional[builtins.str] = None,
    value_elicitation_prompt: typing.Optional[typing.Union[LexIntentSlotValueElicitationPrompt, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d5335984a36f99df9433083ba90edd4167b6064e19a23e30b3533c92a3641f5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84bee784f90c170ce6e78568c6624464b98f0437b06ca9d42cf01f5a498d602c(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__518f59a5758f193f84d512b5ef5dc99836a2348fec38072ffb6ba224e032c12e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ca9498ae0bade31a9ac9514dd3493dfc76fafc809ad2b84f31a5e3b6a671acb(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6dd93a656c83cea22373c78c96c88faa145d3c303bcd64504d38b76af30f7a9(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60e6f6c2a4dad416d98c6a1eb6730b1a0a0ad80025938d8d6cfc9477ec9a080a(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LexIntentSlot]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3aea23306911a7d763116eb9514fc68b68b3c421c521e69fc646de0a5f572c47(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35238168c3c5986d3ab495a94d01a6ff4cd5f5f3df7eb9b0bb9a07bd377cf2ca(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1c33141d72bb2feaa122aa81ff9af264a6efabd975860e2d72cbf3ed354f2c5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2759db4514cc67f2094f605cb624d6e1ed685b24e7290dcd5c0d51c0aaa68c77(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d03bf54d0dd109d02d1975a6c953e39c8c2c78f65f594377f541a2cddaba02b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__decb460091619cff47ba39563d0a842e83dcc3637cf064759019524dd207a7a0(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c57b8d24f1c04efaa33af50f4973191fa906d9cd287a0e2d381febc811433dd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4550669574140bb2bc134ee5347494f6960eb47517945045a3aa6b2ca0a5e4ff(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ca67738549052390282b6572532adb30de4b68ee48c7a33cc4332a03045da7d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db26fd34645dbde61b3d8c91702ca16f2ac0a4f56fcd896c36e8b3d38f5f8930(
    value: typing.Optional[typing.Union[LexIntentSlot, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71f9133c30bcbe325d38fbf9e7fbd62aff7d2fe735788a3b42e8a539658f2de9(
    *,
    max_attempts: jsii.Number,
    message: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LexIntentSlotValueElicitationPromptMessage, typing.Dict[builtins.str, typing.Any]]]],
    response_card: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51d30ab4d2879e1f1c5e6836a9898cf8fa12a055f76fafb7e18058249ef5ab7c(
    *,
    content: builtins.str,
    content_type: builtins.str,
    group_number: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__571de6a790c245e850e55307770aa88df977f4ff7311b49fb300550c1e812462(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd3b049cefb830ae26589d96b80fce590c32080fd417ccdf56a6b4781855c764(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__317cc1a78ca6b97b8961ee1f3a5637d862e2225987a7611b864ab7db7874c097(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e1a2243732d22d83cf433c13e352d03042906406f3a0b12a31fedc516688ed2(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f35a24be1693054c31309c7d1448eac783063888c5b90e92bd4aeaf25daee01(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7feb4479805d7d9c08cfc3a64f22956ad0e954d58f808bd0eb4597634d661aca(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LexIntentSlotValueElicitationPromptMessage]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f68ec455e30f18901d74dc5bc677818191133a2ba1b03ee8cd61ab48b5cf0535(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c24cdb8818ce7a5c550f83f622a6a1d20986994c5f0046ffed9927997f368ad(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc3d98697cb6a41d8e9ef51b97ae9b30e5a68b0f5f60aebee79a8f088d90f05d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77a92ec416700378078fdabb47f2afaeb34c8eeeecd70b4dff0645f2a2048f41(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf1b21332f3173bbfd4e6e5c5924e5e4a6c5b7f2e733cd9b7b6dd53cd0996935(
    value: typing.Optional[typing.Union[LexIntentSlotValueElicitationPromptMessage, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b15a10c732023ba94298604ace6c45ab85a5898a549263a6024cc4c12dbbc53f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d64602dd68d63d03d87fc86d27e40f3a682eff06eba80f896754d43d0be311de(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LexIntentSlotValueElicitationPromptMessage, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__309a36d9b0215b0e16e1a2c068918af408ba9ddd4873f8f333ace6abd3d280cb(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f2c517ee39eea7a74d951a8810230fca8757b9ac174abc8c69db648bee41522(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__272e296cc7307bf5c1894d9b52e016e61de3fca19f509281f07eb713a7929dfe(
    value: typing.Optional[LexIntentSlotValueElicitationPrompt],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__edf25b572cfee91cb2fb4b741d23e73072ee392d98dfa9babac49e1ac8abddb0(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a61a479e1f3fe4534689b297c63ca7212b878bceb2a542e6787f7ba85cf7993f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3c685c55bbf670481d0a19e4feeeb4eeb67bf9671016bcdab6d3a63edbc25a7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9908b2430db7f1e85ffaac3c3a71c00d6b062c98d760d1cc21bada07d8df93cd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03b4af735bbbffef1e43ef7610860af5905f1c41793210fb0465777709ea6bce(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55ff714c6dea69bb15e596c77d425b5eaf14fc071f10b0ce1d6a7dd3c2dfef30(
    value: typing.Optional[typing.Union[LexIntentTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
