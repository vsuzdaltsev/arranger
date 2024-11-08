'''
# `aws_budgets_budget_action`

Refer to the Terraform Registory for docs: [`aws_budgets_budget_action`](https://www.terraform.io/docs/providers/aws/r/budgets_budget_action).
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


class BudgetsBudgetAction(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.budgetsBudgetAction.BudgetsBudgetAction",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget_action aws_budgets_budget_action}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        action_threshold: typing.Union["BudgetsBudgetActionActionThreshold", typing.Dict[builtins.str, typing.Any]],
        action_type: builtins.str,
        approval_model: builtins.str,
        budget_name: builtins.str,
        definition: typing.Union["BudgetsBudgetActionDefinition", typing.Dict[builtins.str, typing.Any]],
        execution_role_arn: builtins.str,
        notification_type: builtins.str,
        subscriber: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["BudgetsBudgetActionSubscriber", typing.Dict[builtins.str, typing.Any]]]],
        account_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget_action aws_budgets_budget_action} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param action_threshold: action_threshold block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget_action#action_threshold BudgetsBudgetAction#action_threshold}
        :param action_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget_action#action_type BudgetsBudgetAction#action_type}.
        :param approval_model: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget_action#approval_model BudgetsBudgetAction#approval_model}.
        :param budget_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget_action#budget_name BudgetsBudgetAction#budget_name}.
        :param definition: definition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget_action#definition BudgetsBudgetAction#definition}
        :param execution_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget_action#execution_role_arn BudgetsBudgetAction#execution_role_arn}.
        :param notification_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget_action#notification_type BudgetsBudgetAction#notification_type}.
        :param subscriber: subscriber block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget_action#subscriber BudgetsBudgetAction#subscriber}
        :param account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget_action#account_id BudgetsBudgetAction#account_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget_action#id BudgetsBudgetAction#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56d766de6cd1913653ba6bd7766e4e29af271f627d24e1eb68d5d01e5d45ec8b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = BudgetsBudgetActionConfig(
            action_threshold=action_threshold,
            action_type=action_type,
            approval_model=approval_model,
            budget_name=budget_name,
            definition=definition,
            execution_role_arn=execution_role_arn,
            notification_type=notification_type,
            subscriber=subscriber,
            account_id=account_id,
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

    @jsii.member(jsii_name="putActionThreshold")
    def put_action_threshold(
        self,
        *,
        action_threshold_type: builtins.str,
        action_threshold_value: jsii.Number,
    ) -> None:
        '''
        :param action_threshold_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget_action#action_threshold_type BudgetsBudgetAction#action_threshold_type}.
        :param action_threshold_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget_action#action_threshold_value BudgetsBudgetAction#action_threshold_value}.
        '''
        value = BudgetsBudgetActionActionThreshold(
            action_threshold_type=action_threshold_type,
            action_threshold_value=action_threshold_value,
        )

        return typing.cast(None, jsii.invoke(self, "putActionThreshold", [value]))

    @jsii.member(jsii_name="putDefinition")
    def put_definition(
        self,
        *,
        iam_action_definition: typing.Optional[typing.Union["BudgetsBudgetActionDefinitionIamActionDefinition", typing.Dict[builtins.str, typing.Any]]] = None,
        scp_action_definition: typing.Optional[typing.Union["BudgetsBudgetActionDefinitionScpActionDefinition", typing.Dict[builtins.str, typing.Any]]] = None,
        ssm_action_definition: typing.Optional[typing.Union["BudgetsBudgetActionDefinitionSsmActionDefinition", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param iam_action_definition: iam_action_definition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget_action#iam_action_definition BudgetsBudgetAction#iam_action_definition}
        :param scp_action_definition: scp_action_definition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget_action#scp_action_definition BudgetsBudgetAction#scp_action_definition}
        :param ssm_action_definition: ssm_action_definition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget_action#ssm_action_definition BudgetsBudgetAction#ssm_action_definition}
        '''
        value = BudgetsBudgetActionDefinition(
            iam_action_definition=iam_action_definition,
            scp_action_definition=scp_action_definition,
            ssm_action_definition=ssm_action_definition,
        )

        return typing.cast(None, jsii.invoke(self, "putDefinition", [value]))

    @jsii.member(jsii_name="putSubscriber")
    def put_subscriber(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["BudgetsBudgetActionSubscriber", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d39dfe4df23db6b7b1a59b4b85462328ad795c5e1798f76fc8c120930b95550)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSubscriber", [value]))

    @jsii.member(jsii_name="resetAccountId")
    def reset_account_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccountId", []))

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
    @jsii.member(jsii_name="actionId")
    def action_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "actionId"))

    @builtins.property
    @jsii.member(jsii_name="actionThreshold")
    def action_threshold(self) -> "BudgetsBudgetActionActionThresholdOutputReference":
        return typing.cast("BudgetsBudgetActionActionThresholdOutputReference", jsii.get(self, "actionThreshold"))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="definition")
    def definition(self) -> "BudgetsBudgetActionDefinitionOutputReference":
        return typing.cast("BudgetsBudgetActionDefinitionOutputReference", jsii.get(self, "definition"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="subscriber")
    def subscriber(self) -> "BudgetsBudgetActionSubscriberList":
        return typing.cast("BudgetsBudgetActionSubscriberList", jsii.get(self, "subscriber"))

    @builtins.property
    @jsii.member(jsii_name="accountIdInput")
    def account_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="actionThresholdInput")
    def action_threshold_input(
        self,
    ) -> typing.Optional["BudgetsBudgetActionActionThreshold"]:
        return typing.cast(typing.Optional["BudgetsBudgetActionActionThreshold"], jsii.get(self, "actionThresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="actionTypeInput")
    def action_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="approvalModelInput")
    def approval_model_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "approvalModelInput"))

    @builtins.property
    @jsii.member(jsii_name="budgetNameInput")
    def budget_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "budgetNameInput"))

    @builtins.property
    @jsii.member(jsii_name="definitionInput")
    def definition_input(self) -> typing.Optional["BudgetsBudgetActionDefinition"]:
        return typing.cast(typing.Optional["BudgetsBudgetActionDefinition"], jsii.get(self, "definitionInput"))

    @builtins.property
    @jsii.member(jsii_name="executionRoleArnInput")
    def execution_role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "executionRoleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="notificationTypeInput")
    def notification_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "notificationTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="subscriberInput")
    def subscriber_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["BudgetsBudgetActionSubscriber"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["BudgetsBudgetActionSubscriber"]]], jsii.get(self, "subscriberInput"))

    @builtins.property
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accountId"))

    @account_id.setter
    def account_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad6a8c0bed7e8cac32fc045d01046ec81e7f70dc4870eaf46ac3b66859da7e10)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountId", value)

    @builtins.property
    @jsii.member(jsii_name="actionType")
    def action_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "actionType"))

    @action_type.setter
    def action_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aef4f9957a8970ea759cbca37b9f8147458ccbf1e505a633f3146810934752ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "actionType", value)

    @builtins.property
    @jsii.member(jsii_name="approvalModel")
    def approval_model(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "approvalModel"))

    @approval_model.setter
    def approval_model(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7dbae82ffda7b9906ce7dbaf7785fa4c7eab966a16021fbaac603e300859d3e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "approvalModel", value)

    @builtins.property
    @jsii.member(jsii_name="budgetName")
    def budget_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "budgetName"))

    @budget_name.setter
    def budget_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8975ba4598c5758836dadbc7c1a56cebdf88ebcb1714129b45d7c7c14a854967)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "budgetName", value)

    @builtins.property
    @jsii.member(jsii_name="executionRoleArn")
    def execution_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "executionRoleArn"))

    @execution_role_arn.setter
    def execution_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fcc74ac99056bd9d4c152773e479803f4984111a948fe1cb6d9051f3d1a3b0bb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "executionRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82f5eeaa1cef4b4e62b19167c4da3941f9d7ddbcc5c18ec409496eac09cbbc8d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="notificationType")
    def notification_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "notificationType"))

    @notification_type.setter
    def notification_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80a49c731e7311a19ecb48d98a53516ce2896550d2d6ae8beea8a7d6afebace5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notificationType", value)


@jsii.data_type(
    jsii_type="aws.budgetsBudgetAction.BudgetsBudgetActionActionThreshold",
    jsii_struct_bases=[],
    name_mapping={
        "action_threshold_type": "actionThresholdType",
        "action_threshold_value": "actionThresholdValue",
    },
)
class BudgetsBudgetActionActionThreshold:
    def __init__(
        self,
        *,
        action_threshold_type: builtins.str,
        action_threshold_value: jsii.Number,
    ) -> None:
        '''
        :param action_threshold_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget_action#action_threshold_type BudgetsBudgetAction#action_threshold_type}.
        :param action_threshold_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget_action#action_threshold_value BudgetsBudgetAction#action_threshold_value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0cc90299efa60e6b7cc98865021d71916f208198da45f21d3d2d9d48fd718e86)
            check_type(argname="argument action_threshold_type", value=action_threshold_type, expected_type=type_hints["action_threshold_type"])
            check_type(argname="argument action_threshold_value", value=action_threshold_value, expected_type=type_hints["action_threshold_value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "action_threshold_type": action_threshold_type,
            "action_threshold_value": action_threshold_value,
        }

    @builtins.property
    def action_threshold_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget_action#action_threshold_type BudgetsBudgetAction#action_threshold_type}.'''
        result = self._values.get("action_threshold_type")
        assert result is not None, "Required property 'action_threshold_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def action_threshold_value(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget_action#action_threshold_value BudgetsBudgetAction#action_threshold_value}.'''
        result = self._values.get("action_threshold_value")
        assert result is not None, "Required property 'action_threshold_value' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BudgetsBudgetActionActionThreshold(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BudgetsBudgetActionActionThresholdOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.budgetsBudgetAction.BudgetsBudgetActionActionThresholdOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__26556e2f0296880fc63dfbb8a57ad3fef208c0b7b7cfb1bc1fd528b06fd5b144)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="actionThresholdTypeInput")
    def action_threshold_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionThresholdTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="actionThresholdValueInput")
    def action_threshold_value_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "actionThresholdValueInput"))

    @builtins.property
    @jsii.member(jsii_name="actionThresholdType")
    def action_threshold_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "actionThresholdType"))

    @action_threshold_type.setter
    def action_threshold_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b081be40eca795fb26dac7f138267e04f4e4c33814213925c8e93739570d7bdc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "actionThresholdType", value)

    @builtins.property
    @jsii.member(jsii_name="actionThresholdValue")
    def action_threshold_value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "actionThresholdValue"))

    @action_threshold_value.setter
    def action_threshold_value(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62ec594750e3d99ed1bf9a70775868cd8a600e5fc8a972fc3d174ca54ad1fd9c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "actionThresholdValue", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[BudgetsBudgetActionActionThreshold]:
        return typing.cast(typing.Optional[BudgetsBudgetActionActionThreshold], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[BudgetsBudgetActionActionThreshold],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a7b229a84b30e79a11277123805a8ee7ea27151fc5de0cd6a47686e92f47c1a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.budgetsBudgetAction.BudgetsBudgetActionConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "action_threshold": "actionThreshold",
        "action_type": "actionType",
        "approval_model": "approvalModel",
        "budget_name": "budgetName",
        "definition": "definition",
        "execution_role_arn": "executionRoleArn",
        "notification_type": "notificationType",
        "subscriber": "subscriber",
        "account_id": "accountId",
        "id": "id",
    },
)
class BudgetsBudgetActionConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        action_threshold: typing.Union[BudgetsBudgetActionActionThreshold, typing.Dict[builtins.str, typing.Any]],
        action_type: builtins.str,
        approval_model: builtins.str,
        budget_name: builtins.str,
        definition: typing.Union["BudgetsBudgetActionDefinition", typing.Dict[builtins.str, typing.Any]],
        execution_role_arn: builtins.str,
        notification_type: builtins.str,
        subscriber: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["BudgetsBudgetActionSubscriber", typing.Dict[builtins.str, typing.Any]]]],
        account_id: typing.Optional[builtins.str] = None,
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
        :param action_threshold: action_threshold block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget_action#action_threshold BudgetsBudgetAction#action_threshold}
        :param action_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget_action#action_type BudgetsBudgetAction#action_type}.
        :param approval_model: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget_action#approval_model BudgetsBudgetAction#approval_model}.
        :param budget_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget_action#budget_name BudgetsBudgetAction#budget_name}.
        :param definition: definition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget_action#definition BudgetsBudgetAction#definition}
        :param execution_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget_action#execution_role_arn BudgetsBudgetAction#execution_role_arn}.
        :param notification_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget_action#notification_type BudgetsBudgetAction#notification_type}.
        :param subscriber: subscriber block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget_action#subscriber BudgetsBudgetAction#subscriber}
        :param account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget_action#account_id BudgetsBudgetAction#account_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget_action#id BudgetsBudgetAction#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(action_threshold, dict):
            action_threshold = BudgetsBudgetActionActionThreshold(**action_threshold)
        if isinstance(definition, dict):
            definition = BudgetsBudgetActionDefinition(**definition)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7178d9bdffd23113039c37e0c3f7c4ea7ac5ea749b6062b1cdc34b8a83678d29)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument action_threshold", value=action_threshold, expected_type=type_hints["action_threshold"])
            check_type(argname="argument action_type", value=action_type, expected_type=type_hints["action_type"])
            check_type(argname="argument approval_model", value=approval_model, expected_type=type_hints["approval_model"])
            check_type(argname="argument budget_name", value=budget_name, expected_type=type_hints["budget_name"])
            check_type(argname="argument definition", value=definition, expected_type=type_hints["definition"])
            check_type(argname="argument execution_role_arn", value=execution_role_arn, expected_type=type_hints["execution_role_arn"])
            check_type(argname="argument notification_type", value=notification_type, expected_type=type_hints["notification_type"])
            check_type(argname="argument subscriber", value=subscriber, expected_type=type_hints["subscriber"])
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "action_threshold": action_threshold,
            "action_type": action_type,
            "approval_model": approval_model,
            "budget_name": budget_name,
            "definition": definition,
            "execution_role_arn": execution_role_arn,
            "notification_type": notification_type,
            "subscriber": subscriber,
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
        if account_id is not None:
            self._values["account_id"] = account_id
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
    def action_threshold(self) -> BudgetsBudgetActionActionThreshold:
        '''action_threshold block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget_action#action_threshold BudgetsBudgetAction#action_threshold}
        '''
        result = self._values.get("action_threshold")
        assert result is not None, "Required property 'action_threshold' is missing"
        return typing.cast(BudgetsBudgetActionActionThreshold, result)

    @builtins.property
    def action_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget_action#action_type BudgetsBudgetAction#action_type}.'''
        result = self._values.get("action_type")
        assert result is not None, "Required property 'action_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def approval_model(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget_action#approval_model BudgetsBudgetAction#approval_model}.'''
        result = self._values.get("approval_model")
        assert result is not None, "Required property 'approval_model' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def budget_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget_action#budget_name BudgetsBudgetAction#budget_name}.'''
        result = self._values.get("budget_name")
        assert result is not None, "Required property 'budget_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def definition(self) -> "BudgetsBudgetActionDefinition":
        '''definition block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget_action#definition BudgetsBudgetAction#definition}
        '''
        result = self._values.get("definition")
        assert result is not None, "Required property 'definition' is missing"
        return typing.cast("BudgetsBudgetActionDefinition", result)

    @builtins.property
    def execution_role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget_action#execution_role_arn BudgetsBudgetAction#execution_role_arn}.'''
        result = self._values.get("execution_role_arn")
        assert result is not None, "Required property 'execution_role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def notification_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget_action#notification_type BudgetsBudgetAction#notification_type}.'''
        result = self._values.get("notification_type")
        assert result is not None, "Required property 'notification_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subscriber(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["BudgetsBudgetActionSubscriber"]]:
        '''subscriber block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget_action#subscriber BudgetsBudgetAction#subscriber}
        '''
        result = self._values.get("subscriber")
        assert result is not None, "Required property 'subscriber' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["BudgetsBudgetActionSubscriber"]], result)

    @builtins.property
    def account_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget_action#account_id BudgetsBudgetAction#account_id}.'''
        result = self._values.get("account_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget_action#id BudgetsBudgetAction#id}.

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
        return "BudgetsBudgetActionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.budgetsBudgetAction.BudgetsBudgetActionDefinition",
    jsii_struct_bases=[],
    name_mapping={
        "iam_action_definition": "iamActionDefinition",
        "scp_action_definition": "scpActionDefinition",
        "ssm_action_definition": "ssmActionDefinition",
    },
)
class BudgetsBudgetActionDefinition:
    def __init__(
        self,
        *,
        iam_action_definition: typing.Optional[typing.Union["BudgetsBudgetActionDefinitionIamActionDefinition", typing.Dict[builtins.str, typing.Any]]] = None,
        scp_action_definition: typing.Optional[typing.Union["BudgetsBudgetActionDefinitionScpActionDefinition", typing.Dict[builtins.str, typing.Any]]] = None,
        ssm_action_definition: typing.Optional[typing.Union["BudgetsBudgetActionDefinitionSsmActionDefinition", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param iam_action_definition: iam_action_definition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget_action#iam_action_definition BudgetsBudgetAction#iam_action_definition}
        :param scp_action_definition: scp_action_definition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget_action#scp_action_definition BudgetsBudgetAction#scp_action_definition}
        :param ssm_action_definition: ssm_action_definition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget_action#ssm_action_definition BudgetsBudgetAction#ssm_action_definition}
        '''
        if isinstance(iam_action_definition, dict):
            iam_action_definition = BudgetsBudgetActionDefinitionIamActionDefinition(**iam_action_definition)
        if isinstance(scp_action_definition, dict):
            scp_action_definition = BudgetsBudgetActionDefinitionScpActionDefinition(**scp_action_definition)
        if isinstance(ssm_action_definition, dict):
            ssm_action_definition = BudgetsBudgetActionDefinitionSsmActionDefinition(**ssm_action_definition)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c2398b5d3b756c12ce7de1efdeaa8a7b15cd5180ef6941822852be114e76c902)
            check_type(argname="argument iam_action_definition", value=iam_action_definition, expected_type=type_hints["iam_action_definition"])
            check_type(argname="argument scp_action_definition", value=scp_action_definition, expected_type=type_hints["scp_action_definition"])
            check_type(argname="argument ssm_action_definition", value=ssm_action_definition, expected_type=type_hints["ssm_action_definition"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if iam_action_definition is not None:
            self._values["iam_action_definition"] = iam_action_definition
        if scp_action_definition is not None:
            self._values["scp_action_definition"] = scp_action_definition
        if ssm_action_definition is not None:
            self._values["ssm_action_definition"] = ssm_action_definition

    @builtins.property
    def iam_action_definition(
        self,
    ) -> typing.Optional["BudgetsBudgetActionDefinitionIamActionDefinition"]:
        '''iam_action_definition block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget_action#iam_action_definition BudgetsBudgetAction#iam_action_definition}
        '''
        result = self._values.get("iam_action_definition")
        return typing.cast(typing.Optional["BudgetsBudgetActionDefinitionIamActionDefinition"], result)

    @builtins.property
    def scp_action_definition(
        self,
    ) -> typing.Optional["BudgetsBudgetActionDefinitionScpActionDefinition"]:
        '''scp_action_definition block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget_action#scp_action_definition BudgetsBudgetAction#scp_action_definition}
        '''
        result = self._values.get("scp_action_definition")
        return typing.cast(typing.Optional["BudgetsBudgetActionDefinitionScpActionDefinition"], result)

    @builtins.property
    def ssm_action_definition(
        self,
    ) -> typing.Optional["BudgetsBudgetActionDefinitionSsmActionDefinition"]:
        '''ssm_action_definition block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget_action#ssm_action_definition BudgetsBudgetAction#ssm_action_definition}
        '''
        result = self._values.get("ssm_action_definition")
        return typing.cast(typing.Optional["BudgetsBudgetActionDefinitionSsmActionDefinition"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BudgetsBudgetActionDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.budgetsBudgetAction.BudgetsBudgetActionDefinitionIamActionDefinition",
    jsii_struct_bases=[],
    name_mapping={
        "policy_arn": "policyArn",
        "groups": "groups",
        "roles": "roles",
        "users": "users",
    },
)
class BudgetsBudgetActionDefinitionIamActionDefinition:
    def __init__(
        self,
        *,
        policy_arn: builtins.str,
        groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        roles: typing.Optional[typing.Sequence[builtins.str]] = None,
        users: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param policy_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget_action#policy_arn BudgetsBudgetAction#policy_arn}.
        :param groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget_action#groups BudgetsBudgetAction#groups}.
        :param roles: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget_action#roles BudgetsBudgetAction#roles}.
        :param users: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget_action#users BudgetsBudgetAction#users}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8836455a099ba82fdc728daa6caf18c57e1bb7873cefef782a7c1897428f830d)
            check_type(argname="argument policy_arn", value=policy_arn, expected_type=type_hints["policy_arn"])
            check_type(argname="argument groups", value=groups, expected_type=type_hints["groups"])
            check_type(argname="argument roles", value=roles, expected_type=type_hints["roles"])
            check_type(argname="argument users", value=users, expected_type=type_hints["users"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "policy_arn": policy_arn,
        }
        if groups is not None:
            self._values["groups"] = groups
        if roles is not None:
            self._values["roles"] = roles
        if users is not None:
            self._values["users"] = users

    @builtins.property
    def policy_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget_action#policy_arn BudgetsBudgetAction#policy_arn}.'''
        result = self._values.get("policy_arn")
        assert result is not None, "Required property 'policy_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget_action#groups BudgetsBudgetAction#groups}.'''
        result = self._values.get("groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def roles(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget_action#roles BudgetsBudgetAction#roles}.'''
        result = self._values.get("roles")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def users(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget_action#users BudgetsBudgetAction#users}.'''
        result = self._values.get("users")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BudgetsBudgetActionDefinitionIamActionDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BudgetsBudgetActionDefinitionIamActionDefinitionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.budgetsBudgetAction.BudgetsBudgetActionDefinitionIamActionDefinitionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9b602493d3527d2c36229b83d8655560a20b6d0289a58d0884b511649752da3e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetGroups")
    def reset_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroups", []))

    @jsii.member(jsii_name="resetRoles")
    def reset_roles(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRoles", []))

    @jsii.member(jsii_name="resetUsers")
    def reset_users(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsers", []))

    @builtins.property
    @jsii.member(jsii_name="groupsInput")
    def groups_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "groupsInput"))

    @builtins.property
    @jsii.member(jsii_name="policyArnInput")
    def policy_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "policyArnInput"))

    @builtins.property
    @jsii.member(jsii_name="rolesInput")
    def roles_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "rolesInput"))

    @builtins.property
    @jsii.member(jsii_name="usersInput")
    def users_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "usersInput"))

    @builtins.property
    @jsii.member(jsii_name="groups")
    def groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "groups"))

    @groups.setter
    def groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d364b657ed6000782fc32a9dff9c75f4ebd607d49d1309f4d300b865ae0a8c52)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groups", value)

    @builtins.property
    @jsii.member(jsii_name="policyArn")
    def policy_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "policyArn"))

    @policy_arn.setter
    def policy_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c6d1b6e0b6a6b1b8fb95360c8c8327edd918a5af652d7a91e735c914c9ece22)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyArn", value)

    @builtins.property
    @jsii.member(jsii_name="roles")
    def roles(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "roles"))

    @roles.setter
    def roles(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f17d715d5c8ffd264dfe56ac6023fac9441bd9f2c84398017b2a62cc61cb42c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roles", value)

    @builtins.property
    @jsii.member(jsii_name="users")
    def users(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "users"))

    @users.setter
    def users(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5797c812e83ebb0fdf298149ea7e51055b1e96178afee9dc7574ceb22758bc3e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "users", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[BudgetsBudgetActionDefinitionIamActionDefinition]:
        return typing.cast(typing.Optional[BudgetsBudgetActionDefinitionIamActionDefinition], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[BudgetsBudgetActionDefinitionIamActionDefinition],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ca55f0461962a09a0f70df161e444d1da2d016d5af790fbe9b55064c6d7b4f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class BudgetsBudgetActionDefinitionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.budgetsBudgetAction.BudgetsBudgetActionDefinitionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0254e6577d90f7dde0d72dd41328501e1ac49a1a5f3190a8a4feaee747f7c032)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putIamActionDefinition")
    def put_iam_action_definition(
        self,
        *,
        policy_arn: builtins.str,
        groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        roles: typing.Optional[typing.Sequence[builtins.str]] = None,
        users: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param policy_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget_action#policy_arn BudgetsBudgetAction#policy_arn}.
        :param groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget_action#groups BudgetsBudgetAction#groups}.
        :param roles: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget_action#roles BudgetsBudgetAction#roles}.
        :param users: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget_action#users BudgetsBudgetAction#users}.
        '''
        value = BudgetsBudgetActionDefinitionIamActionDefinition(
            policy_arn=policy_arn, groups=groups, roles=roles, users=users
        )

        return typing.cast(None, jsii.invoke(self, "putIamActionDefinition", [value]))

    @jsii.member(jsii_name="putScpActionDefinition")
    def put_scp_action_definition(
        self,
        *,
        policy_id: builtins.str,
        target_ids: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param policy_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget_action#policy_id BudgetsBudgetAction#policy_id}.
        :param target_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget_action#target_ids BudgetsBudgetAction#target_ids}.
        '''
        value = BudgetsBudgetActionDefinitionScpActionDefinition(
            policy_id=policy_id, target_ids=target_ids
        )

        return typing.cast(None, jsii.invoke(self, "putScpActionDefinition", [value]))

    @jsii.member(jsii_name="putSsmActionDefinition")
    def put_ssm_action_definition(
        self,
        *,
        action_sub_type: builtins.str,
        instance_ids: typing.Sequence[builtins.str],
        region: builtins.str,
    ) -> None:
        '''
        :param action_sub_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget_action#action_sub_type BudgetsBudgetAction#action_sub_type}.
        :param instance_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget_action#instance_ids BudgetsBudgetAction#instance_ids}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget_action#region BudgetsBudgetAction#region}.
        '''
        value = BudgetsBudgetActionDefinitionSsmActionDefinition(
            action_sub_type=action_sub_type, instance_ids=instance_ids, region=region
        )

        return typing.cast(None, jsii.invoke(self, "putSsmActionDefinition", [value]))

    @jsii.member(jsii_name="resetIamActionDefinition")
    def reset_iam_action_definition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIamActionDefinition", []))

    @jsii.member(jsii_name="resetScpActionDefinition")
    def reset_scp_action_definition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScpActionDefinition", []))

    @jsii.member(jsii_name="resetSsmActionDefinition")
    def reset_ssm_action_definition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSsmActionDefinition", []))

    @builtins.property
    @jsii.member(jsii_name="iamActionDefinition")
    def iam_action_definition(
        self,
    ) -> BudgetsBudgetActionDefinitionIamActionDefinitionOutputReference:
        return typing.cast(BudgetsBudgetActionDefinitionIamActionDefinitionOutputReference, jsii.get(self, "iamActionDefinition"))

    @builtins.property
    @jsii.member(jsii_name="scpActionDefinition")
    def scp_action_definition(
        self,
    ) -> "BudgetsBudgetActionDefinitionScpActionDefinitionOutputReference":
        return typing.cast("BudgetsBudgetActionDefinitionScpActionDefinitionOutputReference", jsii.get(self, "scpActionDefinition"))

    @builtins.property
    @jsii.member(jsii_name="ssmActionDefinition")
    def ssm_action_definition(
        self,
    ) -> "BudgetsBudgetActionDefinitionSsmActionDefinitionOutputReference":
        return typing.cast("BudgetsBudgetActionDefinitionSsmActionDefinitionOutputReference", jsii.get(self, "ssmActionDefinition"))

    @builtins.property
    @jsii.member(jsii_name="iamActionDefinitionInput")
    def iam_action_definition_input(
        self,
    ) -> typing.Optional[BudgetsBudgetActionDefinitionIamActionDefinition]:
        return typing.cast(typing.Optional[BudgetsBudgetActionDefinitionIamActionDefinition], jsii.get(self, "iamActionDefinitionInput"))

    @builtins.property
    @jsii.member(jsii_name="scpActionDefinitionInput")
    def scp_action_definition_input(
        self,
    ) -> typing.Optional["BudgetsBudgetActionDefinitionScpActionDefinition"]:
        return typing.cast(typing.Optional["BudgetsBudgetActionDefinitionScpActionDefinition"], jsii.get(self, "scpActionDefinitionInput"))

    @builtins.property
    @jsii.member(jsii_name="ssmActionDefinitionInput")
    def ssm_action_definition_input(
        self,
    ) -> typing.Optional["BudgetsBudgetActionDefinitionSsmActionDefinition"]:
        return typing.cast(typing.Optional["BudgetsBudgetActionDefinitionSsmActionDefinition"], jsii.get(self, "ssmActionDefinitionInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[BudgetsBudgetActionDefinition]:
        return typing.cast(typing.Optional[BudgetsBudgetActionDefinition], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[BudgetsBudgetActionDefinition],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ab3104abfe4504394efee9e98df9e4adf95e38f476f71216342173ebce5fd7f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.budgetsBudgetAction.BudgetsBudgetActionDefinitionScpActionDefinition",
    jsii_struct_bases=[],
    name_mapping={"policy_id": "policyId", "target_ids": "targetIds"},
)
class BudgetsBudgetActionDefinitionScpActionDefinition:
    def __init__(
        self,
        *,
        policy_id: builtins.str,
        target_ids: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param policy_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget_action#policy_id BudgetsBudgetAction#policy_id}.
        :param target_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget_action#target_ids BudgetsBudgetAction#target_ids}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a937365a3d0fbf7d69cbc4fdac4ef340b2e691be8d8ec476a8be94cf7fb12e5)
            check_type(argname="argument policy_id", value=policy_id, expected_type=type_hints["policy_id"])
            check_type(argname="argument target_ids", value=target_ids, expected_type=type_hints["target_ids"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "policy_id": policy_id,
            "target_ids": target_ids,
        }

    @builtins.property
    def policy_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget_action#policy_id BudgetsBudgetAction#policy_id}.'''
        result = self._values.get("policy_id")
        assert result is not None, "Required property 'policy_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_ids(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget_action#target_ids BudgetsBudgetAction#target_ids}.'''
        result = self._values.get("target_ids")
        assert result is not None, "Required property 'target_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BudgetsBudgetActionDefinitionScpActionDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BudgetsBudgetActionDefinitionScpActionDefinitionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.budgetsBudgetAction.BudgetsBudgetActionDefinitionScpActionDefinitionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__abb12b9213843b0debcb8a4bea927ce5fda122f3a975eafe9f5abfb5b81e281a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="policyIdInput")
    def policy_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "policyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="targetIdsInput")
    def target_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "targetIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="policyId")
    def policy_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "policyId"))

    @policy_id.setter
    def policy_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0879e24819b22fef5bb214d0fd7e63743a1931009699fe1a1a5cdb02efdf02f4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyId", value)

    @builtins.property
    @jsii.member(jsii_name="targetIds")
    def target_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "targetIds"))

    @target_ids.setter
    def target_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c73c68b66a222fee4d3bf8d4327bec2873bf676b9ee4fb9745df55a3b1f02c4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetIds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[BudgetsBudgetActionDefinitionScpActionDefinition]:
        return typing.cast(typing.Optional[BudgetsBudgetActionDefinitionScpActionDefinition], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[BudgetsBudgetActionDefinitionScpActionDefinition],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2391882194f21991c561335f62bb44215d2835d6e3c3cf7e418046f14b09466d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.budgetsBudgetAction.BudgetsBudgetActionDefinitionSsmActionDefinition",
    jsii_struct_bases=[],
    name_mapping={
        "action_sub_type": "actionSubType",
        "instance_ids": "instanceIds",
        "region": "region",
    },
)
class BudgetsBudgetActionDefinitionSsmActionDefinition:
    def __init__(
        self,
        *,
        action_sub_type: builtins.str,
        instance_ids: typing.Sequence[builtins.str],
        region: builtins.str,
    ) -> None:
        '''
        :param action_sub_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget_action#action_sub_type BudgetsBudgetAction#action_sub_type}.
        :param instance_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget_action#instance_ids BudgetsBudgetAction#instance_ids}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget_action#region BudgetsBudgetAction#region}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa5c060d3a22f9e95461ca9aa192f58dcca74476be05d2bd1aec3bcc3d7d6bce)
            check_type(argname="argument action_sub_type", value=action_sub_type, expected_type=type_hints["action_sub_type"])
            check_type(argname="argument instance_ids", value=instance_ids, expected_type=type_hints["instance_ids"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "action_sub_type": action_sub_type,
            "instance_ids": instance_ids,
            "region": region,
        }

    @builtins.property
    def action_sub_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget_action#action_sub_type BudgetsBudgetAction#action_sub_type}.'''
        result = self._values.get("action_sub_type")
        assert result is not None, "Required property 'action_sub_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def instance_ids(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget_action#instance_ids BudgetsBudgetAction#instance_ids}.'''
        result = self._values.get("instance_ids")
        assert result is not None, "Required property 'instance_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def region(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget_action#region BudgetsBudgetAction#region}.'''
        result = self._values.get("region")
        assert result is not None, "Required property 'region' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BudgetsBudgetActionDefinitionSsmActionDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BudgetsBudgetActionDefinitionSsmActionDefinitionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.budgetsBudgetAction.BudgetsBudgetActionDefinitionSsmActionDefinitionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__98082189a5e4050c1200b1c7289404c29ba4daea0af9246171f8eebcb6d8b270)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="actionSubTypeInput")
    def action_sub_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionSubTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceIdsInput")
    def instance_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "instanceIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="actionSubType")
    def action_sub_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "actionSubType"))

    @action_sub_type.setter
    def action_sub_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0fc6e9001364b727bea477f4c194ba0dc2650501645b7f61a291bc0c7e15ce72)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "actionSubType", value)

    @builtins.property
    @jsii.member(jsii_name="instanceIds")
    def instance_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "instanceIds"))

    @instance_ids.setter
    def instance_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__475efd3fa9a8ccb8551667632b2a950c38ef696cc5cfb3216f62b9ff8e7cfb9b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceIds", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f0980f48a7aae2c256f0a8b254bf6a67dd67eb9f263a4b549c2693ccbaa5177)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[BudgetsBudgetActionDefinitionSsmActionDefinition]:
        return typing.cast(typing.Optional[BudgetsBudgetActionDefinitionSsmActionDefinition], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[BudgetsBudgetActionDefinitionSsmActionDefinition],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00c7097c320640e4670232e9bca81dcfdd9e9ba346593c5356b1212eafd1b693)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.budgetsBudgetAction.BudgetsBudgetActionSubscriber",
    jsii_struct_bases=[],
    name_mapping={"address": "address", "subscription_type": "subscriptionType"},
)
class BudgetsBudgetActionSubscriber:
    def __init__(
        self,
        *,
        address: builtins.str,
        subscription_type: builtins.str,
    ) -> None:
        '''
        :param address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget_action#address BudgetsBudgetAction#address}.
        :param subscription_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget_action#subscription_type BudgetsBudgetAction#subscription_type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3125dba5ff96b22f94ec3ef974182b5ef594b424805f9ff8f385b27c74a8246d)
            check_type(argname="argument address", value=address, expected_type=type_hints["address"])
            check_type(argname="argument subscription_type", value=subscription_type, expected_type=type_hints["subscription_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "address": address,
            "subscription_type": subscription_type,
        }

    @builtins.property
    def address(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget_action#address BudgetsBudgetAction#address}.'''
        result = self._values.get("address")
        assert result is not None, "Required property 'address' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subscription_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget_action#subscription_type BudgetsBudgetAction#subscription_type}.'''
        result = self._values.get("subscription_type")
        assert result is not None, "Required property 'subscription_type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BudgetsBudgetActionSubscriber(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BudgetsBudgetActionSubscriberList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.budgetsBudgetAction.BudgetsBudgetActionSubscriberList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9e2d9ee06d707ba8e0229fe81da073fe86954ff3fb07f8b7ae9b9c4b841e37bf)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "BudgetsBudgetActionSubscriberOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__100fde12733fa798e7c7d92b16fce3ec733ff4a573d0f3244a75affcf1abfac4)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("BudgetsBudgetActionSubscriberOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f0f63c3ec41f257effd1697e48860303d7b04416d385d206305172ff660c6d9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ce00fc90791fa4ef8810ce1d8b8b2e9010e79f897c1a9768fda79981043be9a5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9c8ec56c9194d5bb97c75d8645c45d7e4e3710a8f2c4bdcb0330fb291538c67d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[BudgetsBudgetActionSubscriber]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[BudgetsBudgetActionSubscriber]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[BudgetsBudgetActionSubscriber]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96c08af0e7f7747ab38d470ea11b25c121ae26999d13e922efdbf785e3f58f43)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class BudgetsBudgetActionSubscriberOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.budgetsBudgetAction.BudgetsBudgetActionSubscriberOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e1e95ae5d0af1cb1057a35848496e01f972c65c5efc85cd5f76bf55bc1685557)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="addressInput")
    def address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "addressInput"))

    @builtins.property
    @jsii.member(jsii_name="subscriptionTypeInput")
    def subscription_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subscriptionTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="address")
    def address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "address"))

    @address.setter
    def address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20995c10b6f678b5b049faa80a8f035f385f6deb2411d4fc6bbcea826a4721d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "address", value)

    @builtins.property
    @jsii.member(jsii_name="subscriptionType")
    def subscription_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subscriptionType"))

    @subscription_type.setter
    def subscription_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23845cac1677e3df8b364272906344befc2e08558d93978e008a0e879e701895)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subscriptionType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[BudgetsBudgetActionSubscriber, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[BudgetsBudgetActionSubscriber, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[BudgetsBudgetActionSubscriber, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5dcd9d4f3ff413267841fd233db694ec3008aef50024daac6e83e0e1b3c44710)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "BudgetsBudgetAction",
    "BudgetsBudgetActionActionThreshold",
    "BudgetsBudgetActionActionThresholdOutputReference",
    "BudgetsBudgetActionConfig",
    "BudgetsBudgetActionDefinition",
    "BudgetsBudgetActionDefinitionIamActionDefinition",
    "BudgetsBudgetActionDefinitionIamActionDefinitionOutputReference",
    "BudgetsBudgetActionDefinitionOutputReference",
    "BudgetsBudgetActionDefinitionScpActionDefinition",
    "BudgetsBudgetActionDefinitionScpActionDefinitionOutputReference",
    "BudgetsBudgetActionDefinitionSsmActionDefinition",
    "BudgetsBudgetActionDefinitionSsmActionDefinitionOutputReference",
    "BudgetsBudgetActionSubscriber",
    "BudgetsBudgetActionSubscriberList",
    "BudgetsBudgetActionSubscriberOutputReference",
]

publication.publish()

def _typecheckingstub__56d766de6cd1913653ba6bd7766e4e29af271f627d24e1eb68d5d01e5d45ec8b(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    action_threshold: typing.Union[BudgetsBudgetActionActionThreshold, typing.Dict[builtins.str, typing.Any]],
    action_type: builtins.str,
    approval_model: builtins.str,
    budget_name: builtins.str,
    definition: typing.Union[BudgetsBudgetActionDefinition, typing.Dict[builtins.str, typing.Any]],
    execution_role_arn: builtins.str,
    notification_type: builtins.str,
    subscriber: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[BudgetsBudgetActionSubscriber, typing.Dict[builtins.str, typing.Any]]]],
    account_id: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__5d39dfe4df23db6b7b1a59b4b85462328ad795c5e1798f76fc8c120930b95550(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[BudgetsBudgetActionSubscriber, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad6a8c0bed7e8cac32fc045d01046ec81e7f70dc4870eaf46ac3b66859da7e10(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aef4f9957a8970ea759cbca37b9f8147458ccbf1e505a633f3146810934752ec(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7dbae82ffda7b9906ce7dbaf7785fa4c7eab966a16021fbaac603e300859d3e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8975ba4598c5758836dadbc7c1a56cebdf88ebcb1714129b45d7c7c14a854967(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fcc74ac99056bd9d4c152773e479803f4984111a948fe1cb6d9051f3d1a3b0bb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82f5eeaa1cef4b4e62b19167c4da3941f9d7ddbcc5c18ec409496eac09cbbc8d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80a49c731e7311a19ecb48d98a53516ce2896550d2d6ae8beea8a7d6afebace5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0cc90299efa60e6b7cc98865021d71916f208198da45f21d3d2d9d48fd718e86(
    *,
    action_threshold_type: builtins.str,
    action_threshold_value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26556e2f0296880fc63dfbb8a57ad3fef208c0b7b7cfb1bc1fd528b06fd5b144(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b081be40eca795fb26dac7f138267e04f4e4c33814213925c8e93739570d7bdc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62ec594750e3d99ed1bf9a70775868cd8a600e5fc8a972fc3d174ca54ad1fd9c(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a7b229a84b30e79a11277123805a8ee7ea27151fc5de0cd6a47686e92f47c1a(
    value: typing.Optional[BudgetsBudgetActionActionThreshold],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7178d9bdffd23113039c37e0c3f7c4ea7ac5ea749b6062b1cdc34b8a83678d29(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    action_threshold: typing.Union[BudgetsBudgetActionActionThreshold, typing.Dict[builtins.str, typing.Any]],
    action_type: builtins.str,
    approval_model: builtins.str,
    budget_name: builtins.str,
    definition: typing.Union[BudgetsBudgetActionDefinition, typing.Dict[builtins.str, typing.Any]],
    execution_role_arn: builtins.str,
    notification_type: builtins.str,
    subscriber: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[BudgetsBudgetActionSubscriber, typing.Dict[builtins.str, typing.Any]]]],
    account_id: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2398b5d3b756c12ce7de1efdeaa8a7b15cd5180ef6941822852be114e76c902(
    *,
    iam_action_definition: typing.Optional[typing.Union[BudgetsBudgetActionDefinitionIamActionDefinition, typing.Dict[builtins.str, typing.Any]]] = None,
    scp_action_definition: typing.Optional[typing.Union[BudgetsBudgetActionDefinitionScpActionDefinition, typing.Dict[builtins.str, typing.Any]]] = None,
    ssm_action_definition: typing.Optional[typing.Union[BudgetsBudgetActionDefinitionSsmActionDefinition, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8836455a099ba82fdc728daa6caf18c57e1bb7873cefef782a7c1897428f830d(
    *,
    policy_arn: builtins.str,
    groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    roles: typing.Optional[typing.Sequence[builtins.str]] = None,
    users: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b602493d3527d2c36229b83d8655560a20b6d0289a58d0884b511649752da3e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d364b657ed6000782fc32a9dff9c75f4ebd607d49d1309f4d300b865ae0a8c52(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c6d1b6e0b6a6b1b8fb95360c8c8327edd918a5af652d7a91e735c914c9ece22(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f17d715d5c8ffd264dfe56ac6023fac9441bd9f2c84398017b2a62cc61cb42c5(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5797c812e83ebb0fdf298149ea7e51055b1e96178afee9dc7574ceb22758bc3e(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ca55f0461962a09a0f70df161e444d1da2d016d5af790fbe9b55064c6d7b4f8(
    value: typing.Optional[BudgetsBudgetActionDefinitionIamActionDefinition],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0254e6577d90f7dde0d72dd41328501e1ac49a1a5f3190a8a4feaee747f7c032(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ab3104abfe4504394efee9e98df9e4adf95e38f476f71216342173ebce5fd7f(
    value: typing.Optional[BudgetsBudgetActionDefinition],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a937365a3d0fbf7d69cbc4fdac4ef340b2e691be8d8ec476a8be94cf7fb12e5(
    *,
    policy_id: builtins.str,
    target_ids: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__abb12b9213843b0debcb8a4bea927ce5fda122f3a975eafe9f5abfb5b81e281a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0879e24819b22fef5bb214d0fd7e63743a1931009699fe1a1a5cdb02efdf02f4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c73c68b66a222fee4d3bf8d4327bec2873bf676b9ee4fb9745df55a3b1f02c4(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2391882194f21991c561335f62bb44215d2835d6e3c3cf7e418046f14b09466d(
    value: typing.Optional[BudgetsBudgetActionDefinitionScpActionDefinition],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa5c060d3a22f9e95461ca9aa192f58dcca74476be05d2bd1aec3bcc3d7d6bce(
    *,
    action_sub_type: builtins.str,
    instance_ids: typing.Sequence[builtins.str],
    region: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98082189a5e4050c1200b1c7289404c29ba4daea0af9246171f8eebcb6d8b270(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0fc6e9001364b727bea477f4c194ba0dc2650501645b7f61a291bc0c7e15ce72(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__475efd3fa9a8ccb8551667632b2a950c38ef696cc5cfb3216f62b9ff8e7cfb9b(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f0980f48a7aae2c256f0a8b254bf6a67dd67eb9f263a4b549c2693ccbaa5177(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00c7097c320640e4670232e9bca81dcfdd9e9ba346593c5356b1212eafd1b693(
    value: typing.Optional[BudgetsBudgetActionDefinitionSsmActionDefinition],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3125dba5ff96b22f94ec3ef974182b5ef594b424805f9ff8f385b27c74a8246d(
    *,
    address: builtins.str,
    subscription_type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e2d9ee06d707ba8e0229fe81da073fe86954ff3fb07f8b7ae9b9c4b841e37bf(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__100fde12733fa798e7c7d92b16fce3ec733ff4a573d0f3244a75affcf1abfac4(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f0f63c3ec41f257effd1697e48860303d7b04416d385d206305172ff660c6d9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce00fc90791fa4ef8810ce1d8b8b2e9010e79f897c1a9768fda79981043be9a5(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c8ec56c9194d5bb97c75d8645c45d7e4e3710a8f2c4bdcb0330fb291538c67d(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96c08af0e7f7747ab38d470ea11b25c121ae26999d13e922efdbf785e3f58f43(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[BudgetsBudgetActionSubscriber]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1e95ae5d0af1cb1057a35848496e01f972c65c5efc85cd5f76bf55bc1685557(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20995c10b6f678b5b049faa80a8f035f385f6deb2411d4fc6bbcea826a4721d0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23845cac1677e3df8b364272906344befc2e08558d93978e008a0e879e701895(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5dcd9d4f3ff413267841fd233db694ec3008aef50024daac6e83e0e1b3c44710(
    value: typing.Optional[typing.Union[BudgetsBudgetActionSubscriber, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
