'''
# `aws_budgets_budget`

Refer to the Terraform Registory for docs: [`aws_budgets_budget`](https://www.terraform.io/docs/providers/aws/r/budgets_budget).
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


class BudgetsBudget(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.budgetsBudget.BudgetsBudget",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget aws_budgets_budget}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        budget_type: builtins.str,
        time_unit: builtins.str,
        account_id: typing.Optional[builtins.str] = None,
        auto_adjust_data: typing.Optional[typing.Union["BudgetsBudgetAutoAdjustData", typing.Dict[builtins.str, typing.Any]]] = None,
        cost_filter: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["BudgetsBudgetCostFilter", typing.Dict[builtins.str, typing.Any]]]]] = None,
        cost_filters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        cost_types: typing.Optional[typing.Union["BudgetsBudgetCostTypes", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        limit_amount: typing.Optional[builtins.str] = None,
        limit_unit: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        name_prefix: typing.Optional[builtins.str] = None,
        notification: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["BudgetsBudgetNotification", typing.Dict[builtins.str, typing.Any]]]]] = None,
        planned_limit: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["BudgetsBudgetPlannedLimit", typing.Dict[builtins.str, typing.Any]]]]] = None,
        time_period_end: typing.Optional[builtins.str] = None,
        time_period_start: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget aws_budgets_budget} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param budget_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#budget_type BudgetsBudget#budget_type}.
        :param time_unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#time_unit BudgetsBudget#time_unit}.
        :param account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#account_id BudgetsBudget#account_id}.
        :param auto_adjust_data: auto_adjust_data block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#auto_adjust_data BudgetsBudget#auto_adjust_data}
        :param cost_filter: cost_filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#cost_filter BudgetsBudget#cost_filter}
        :param cost_filters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#cost_filters BudgetsBudget#cost_filters}.
        :param cost_types: cost_types block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#cost_types BudgetsBudget#cost_types}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#id BudgetsBudget#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param limit_amount: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#limit_amount BudgetsBudget#limit_amount}.
        :param limit_unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#limit_unit BudgetsBudget#limit_unit}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#name BudgetsBudget#name}.
        :param name_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#name_prefix BudgetsBudget#name_prefix}.
        :param notification: notification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#notification BudgetsBudget#notification}
        :param planned_limit: planned_limit block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#planned_limit BudgetsBudget#planned_limit}
        :param time_period_end: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#time_period_end BudgetsBudget#time_period_end}.
        :param time_period_start: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#time_period_start BudgetsBudget#time_period_start}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__356b584a7cb0712c03baaddc0592dc0d71b263b5fa9bac5efb334dce9f5c4a57)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = BudgetsBudgetConfig(
            budget_type=budget_type,
            time_unit=time_unit,
            account_id=account_id,
            auto_adjust_data=auto_adjust_data,
            cost_filter=cost_filter,
            cost_filters=cost_filters,
            cost_types=cost_types,
            id=id,
            limit_amount=limit_amount,
            limit_unit=limit_unit,
            name=name,
            name_prefix=name_prefix,
            notification=notification,
            planned_limit=planned_limit,
            time_period_end=time_period_end,
            time_period_start=time_period_start,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAutoAdjustData")
    def put_auto_adjust_data(
        self,
        *,
        auto_adjust_type: builtins.str,
        historical_options: typing.Optional[typing.Union["BudgetsBudgetAutoAdjustDataHistoricalOptions", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param auto_adjust_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#auto_adjust_type BudgetsBudget#auto_adjust_type}.
        :param historical_options: historical_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#historical_options BudgetsBudget#historical_options}
        '''
        value = BudgetsBudgetAutoAdjustData(
            auto_adjust_type=auto_adjust_type, historical_options=historical_options
        )

        return typing.cast(None, jsii.invoke(self, "putAutoAdjustData", [value]))

    @jsii.member(jsii_name="putCostFilter")
    def put_cost_filter(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["BudgetsBudgetCostFilter", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8db66af9aa933ace25e2ddfd9875aa33ed46fc46b403cde56b7d38943a6fadfd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCostFilter", [value]))

    @jsii.member(jsii_name="putCostTypes")
    def put_cost_types(
        self,
        *,
        include_credit: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        include_discount: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        include_other_subscription: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        include_recurring: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        include_refund: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        include_subscription: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        include_support: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        include_tax: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        include_upfront: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        use_amortized: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        use_blended: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param include_credit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#include_credit BudgetsBudget#include_credit}.
        :param include_discount: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#include_discount BudgetsBudget#include_discount}.
        :param include_other_subscription: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#include_other_subscription BudgetsBudget#include_other_subscription}.
        :param include_recurring: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#include_recurring BudgetsBudget#include_recurring}.
        :param include_refund: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#include_refund BudgetsBudget#include_refund}.
        :param include_subscription: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#include_subscription BudgetsBudget#include_subscription}.
        :param include_support: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#include_support BudgetsBudget#include_support}.
        :param include_tax: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#include_tax BudgetsBudget#include_tax}.
        :param include_upfront: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#include_upfront BudgetsBudget#include_upfront}.
        :param use_amortized: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#use_amortized BudgetsBudget#use_amortized}.
        :param use_blended: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#use_blended BudgetsBudget#use_blended}.
        '''
        value = BudgetsBudgetCostTypes(
            include_credit=include_credit,
            include_discount=include_discount,
            include_other_subscription=include_other_subscription,
            include_recurring=include_recurring,
            include_refund=include_refund,
            include_subscription=include_subscription,
            include_support=include_support,
            include_tax=include_tax,
            include_upfront=include_upfront,
            use_amortized=use_amortized,
            use_blended=use_blended,
        )

        return typing.cast(None, jsii.invoke(self, "putCostTypes", [value]))

    @jsii.member(jsii_name="putNotification")
    def put_notification(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["BudgetsBudgetNotification", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9da005e8dcca95795770d3a740e7e05fbf7ab032534b7365a3f4467c0aca8e5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNotification", [value]))

    @jsii.member(jsii_name="putPlannedLimit")
    def put_planned_limit(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["BudgetsBudgetPlannedLimit", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f924c48667cf8ba03181993ff23654d3433bea3fbf97e66d6a3dc6a33ca9596)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPlannedLimit", [value]))

    @jsii.member(jsii_name="resetAccountId")
    def reset_account_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccountId", []))

    @jsii.member(jsii_name="resetAutoAdjustData")
    def reset_auto_adjust_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoAdjustData", []))

    @jsii.member(jsii_name="resetCostFilter")
    def reset_cost_filter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCostFilter", []))

    @jsii.member(jsii_name="resetCostFilters")
    def reset_cost_filters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCostFilters", []))

    @jsii.member(jsii_name="resetCostTypes")
    def reset_cost_types(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCostTypes", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLimitAmount")
    def reset_limit_amount(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLimitAmount", []))

    @jsii.member(jsii_name="resetLimitUnit")
    def reset_limit_unit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLimitUnit", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetNamePrefix")
    def reset_name_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamePrefix", []))

    @jsii.member(jsii_name="resetNotification")
    def reset_notification(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotification", []))

    @jsii.member(jsii_name="resetPlannedLimit")
    def reset_planned_limit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPlannedLimit", []))

    @jsii.member(jsii_name="resetTimePeriodEnd")
    def reset_time_period_end(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimePeriodEnd", []))

    @jsii.member(jsii_name="resetTimePeriodStart")
    def reset_time_period_start(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimePeriodStart", []))

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
    @jsii.member(jsii_name="autoAdjustData")
    def auto_adjust_data(self) -> "BudgetsBudgetAutoAdjustDataOutputReference":
        return typing.cast("BudgetsBudgetAutoAdjustDataOutputReference", jsii.get(self, "autoAdjustData"))

    @builtins.property
    @jsii.member(jsii_name="costFilter")
    def cost_filter(self) -> "BudgetsBudgetCostFilterList":
        return typing.cast("BudgetsBudgetCostFilterList", jsii.get(self, "costFilter"))

    @builtins.property
    @jsii.member(jsii_name="costTypes")
    def cost_types(self) -> "BudgetsBudgetCostTypesOutputReference":
        return typing.cast("BudgetsBudgetCostTypesOutputReference", jsii.get(self, "costTypes"))

    @builtins.property
    @jsii.member(jsii_name="notification")
    def notification(self) -> "BudgetsBudgetNotificationList":
        return typing.cast("BudgetsBudgetNotificationList", jsii.get(self, "notification"))

    @builtins.property
    @jsii.member(jsii_name="plannedLimit")
    def planned_limit(self) -> "BudgetsBudgetPlannedLimitList":
        return typing.cast("BudgetsBudgetPlannedLimitList", jsii.get(self, "plannedLimit"))

    @builtins.property
    @jsii.member(jsii_name="accountIdInput")
    def account_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="autoAdjustDataInput")
    def auto_adjust_data_input(self) -> typing.Optional["BudgetsBudgetAutoAdjustData"]:
        return typing.cast(typing.Optional["BudgetsBudgetAutoAdjustData"], jsii.get(self, "autoAdjustDataInput"))

    @builtins.property
    @jsii.member(jsii_name="budgetTypeInput")
    def budget_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "budgetTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="costFilterInput")
    def cost_filter_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["BudgetsBudgetCostFilter"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["BudgetsBudgetCostFilter"]]], jsii.get(self, "costFilterInput"))

    @builtins.property
    @jsii.member(jsii_name="costFiltersInput")
    def cost_filters_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "costFiltersInput"))

    @builtins.property
    @jsii.member(jsii_name="costTypesInput")
    def cost_types_input(self) -> typing.Optional["BudgetsBudgetCostTypes"]:
        return typing.cast(typing.Optional["BudgetsBudgetCostTypes"], jsii.get(self, "costTypesInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="limitAmountInput")
    def limit_amount_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "limitAmountInput"))

    @builtins.property
    @jsii.member(jsii_name="limitUnitInput")
    def limit_unit_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "limitUnitInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="namePrefixInput")
    def name_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namePrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="notificationInput")
    def notification_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["BudgetsBudgetNotification"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["BudgetsBudgetNotification"]]], jsii.get(self, "notificationInput"))

    @builtins.property
    @jsii.member(jsii_name="plannedLimitInput")
    def planned_limit_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["BudgetsBudgetPlannedLimit"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["BudgetsBudgetPlannedLimit"]]], jsii.get(self, "plannedLimitInput"))

    @builtins.property
    @jsii.member(jsii_name="timePeriodEndInput")
    def time_period_end_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timePeriodEndInput"))

    @builtins.property
    @jsii.member(jsii_name="timePeriodStartInput")
    def time_period_start_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timePeriodStartInput"))

    @builtins.property
    @jsii.member(jsii_name="timeUnitInput")
    def time_unit_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timeUnitInput"))

    @builtins.property
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accountId"))

    @account_id.setter
    def account_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bcaa4c0fd65d487a7b900998f2d8e187d574b52f961e53821195b4f9da40ca71)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountId", value)

    @builtins.property
    @jsii.member(jsii_name="budgetType")
    def budget_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "budgetType"))

    @budget_type.setter
    def budget_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__508435880c6f7bbf0a77123a48406de10bb9937063a83e23eac3405b1fe8e9f2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "budgetType", value)

    @builtins.property
    @jsii.member(jsii_name="costFilters")
    def cost_filters(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "costFilters"))

    @cost_filters.setter
    def cost_filters(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8109f77e478ab539e59451fa5963568855a37a3a7ce9a623b4691b0f12bbd8cf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "costFilters", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__115d0c7908223f8f3403b0117c216cd313ff356c3da27a775b6b8b5ca0b5a9ac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="limitAmount")
    def limit_amount(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "limitAmount"))

    @limit_amount.setter
    def limit_amount(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1007b7573eaae3601280ccf50ae3b0dcc6e0e274830986dd7a371931b5451e9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "limitAmount", value)

    @builtins.property
    @jsii.member(jsii_name="limitUnit")
    def limit_unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "limitUnit"))

    @limit_unit.setter
    def limit_unit(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__28926a00fbdc5bdaf74b51154c49744df1721e231feb53b376ff19bda4c7fd54)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "limitUnit", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42fd8774fbaae4d74f29106ed6176725cf1bfe5677c6037d7b4457cf4a3d1df2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namePrefix")
    def name_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namePrefix"))

    @name_prefix.setter
    def name_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d9197caae863b07651316149341924af52d2584db68f49ae1bf8fb7f775f614)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namePrefix", value)

    @builtins.property
    @jsii.member(jsii_name="timePeriodEnd")
    def time_period_end(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timePeriodEnd"))

    @time_period_end.setter
    def time_period_end(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__864a581f3219bc31637bc3e4c3712323c15afb9fc271717a22295a5c9fc786ed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timePeriodEnd", value)

    @builtins.property
    @jsii.member(jsii_name="timePeriodStart")
    def time_period_start(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timePeriodStart"))

    @time_period_start.setter
    def time_period_start(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a4485d56d914ce8e1a8369c98beabd26ab74717bd9d2f24b8b9b75c55044728)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timePeriodStart", value)

    @builtins.property
    @jsii.member(jsii_name="timeUnit")
    def time_unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timeUnit"))

    @time_unit.setter
    def time_unit(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4285fd98afb64132deb35a54e4f71db4afe00149ae34ebf460c29db0cfb42110)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeUnit", value)


@jsii.data_type(
    jsii_type="aws.budgetsBudget.BudgetsBudgetAutoAdjustData",
    jsii_struct_bases=[],
    name_mapping={
        "auto_adjust_type": "autoAdjustType",
        "historical_options": "historicalOptions",
    },
)
class BudgetsBudgetAutoAdjustData:
    def __init__(
        self,
        *,
        auto_adjust_type: builtins.str,
        historical_options: typing.Optional[typing.Union["BudgetsBudgetAutoAdjustDataHistoricalOptions", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param auto_adjust_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#auto_adjust_type BudgetsBudget#auto_adjust_type}.
        :param historical_options: historical_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#historical_options BudgetsBudget#historical_options}
        '''
        if isinstance(historical_options, dict):
            historical_options = BudgetsBudgetAutoAdjustDataHistoricalOptions(**historical_options)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1d1529d0cd1b8f17e844e48ef202401589b16b7e6c41bbb14fc6fd0df44ba07)
            check_type(argname="argument auto_adjust_type", value=auto_adjust_type, expected_type=type_hints["auto_adjust_type"])
            check_type(argname="argument historical_options", value=historical_options, expected_type=type_hints["historical_options"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "auto_adjust_type": auto_adjust_type,
        }
        if historical_options is not None:
            self._values["historical_options"] = historical_options

    @builtins.property
    def auto_adjust_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#auto_adjust_type BudgetsBudget#auto_adjust_type}.'''
        result = self._values.get("auto_adjust_type")
        assert result is not None, "Required property 'auto_adjust_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def historical_options(
        self,
    ) -> typing.Optional["BudgetsBudgetAutoAdjustDataHistoricalOptions"]:
        '''historical_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#historical_options BudgetsBudget#historical_options}
        '''
        result = self._values.get("historical_options")
        return typing.cast(typing.Optional["BudgetsBudgetAutoAdjustDataHistoricalOptions"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BudgetsBudgetAutoAdjustData(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.budgetsBudget.BudgetsBudgetAutoAdjustDataHistoricalOptions",
    jsii_struct_bases=[],
    name_mapping={"budget_adjustment_period": "budgetAdjustmentPeriod"},
)
class BudgetsBudgetAutoAdjustDataHistoricalOptions:
    def __init__(self, *, budget_adjustment_period: jsii.Number) -> None:
        '''
        :param budget_adjustment_period: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#budget_adjustment_period BudgetsBudget#budget_adjustment_period}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__596f0f5271bb13dd686b848042478ac80d76dc1105233265f63f42d05c16854e)
            check_type(argname="argument budget_adjustment_period", value=budget_adjustment_period, expected_type=type_hints["budget_adjustment_period"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "budget_adjustment_period": budget_adjustment_period,
        }

    @builtins.property
    def budget_adjustment_period(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#budget_adjustment_period BudgetsBudget#budget_adjustment_period}.'''
        result = self._values.get("budget_adjustment_period")
        assert result is not None, "Required property 'budget_adjustment_period' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BudgetsBudgetAutoAdjustDataHistoricalOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BudgetsBudgetAutoAdjustDataHistoricalOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.budgetsBudget.BudgetsBudgetAutoAdjustDataHistoricalOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__db629e4def2198b67282eebf51b3cab5a39808f95d05e473ed035841daf901d9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="lookbackAvailablePeriods")
    def lookback_available_periods(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "lookbackAvailablePeriods"))

    @builtins.property
    @jsii.member(jsii_name="budgetAdjustmentPeriodInput")
    def budget_adjustment_period_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "budgetAdjustmentPeriodInput"))

    @builtins.property
    @jsii.member(jsii_name="budgetAdjustmentPeriod")
    def budget_adjustment_period(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "budgetAdjustmentPeriod"))

    @budget_adjustment_period.setter
    def budget_adjustment_period(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4587436cb17291e6944869948eccff50dc6a54e8f043ceea7fe34c728a1b3310)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "budgetAdjustmentPeriod", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[BudgetsBudgetAutoAdjustDataHistoricalOptions]:
        return typing.cast(typing.Optional[BudgetsBudgetAutoAdjustDataHistoricalOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[BudgetsBudgetAutoAdjustDataHistoricalOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d94257eef8d822dda756ddc2f3f380e947a97d7755778e042acf6714c949dbad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class BudgetsBudgetAutoAdjustDataOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.budgetsBudget.BudgetsBudgetAutoAdjustDataOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b76471cc00c34bff0c5a68d7ce75269f6b23b70870f4cb2bdfe82dead5ec3cb3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putHistoricalOptions")
    def put_historical_options(self, *, budget_adjustment_period: jsii.Number) -> None:
        '''
        :param budget_adjustment_period: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#budget_adjustment_period BudgetsBudget#budget_adjustment_period}.
        '''
        value = BudgetsBudgetAutoAdjustDataHistoricalOptions(
            budget_adjustment_period=budget_adjustment_period
        )

        return typing.cast(None, jsii.invoke(self, "putHistoricalOptions", [value]))

    @jsii.member(jsii_name="resetHistoricalOptions")
    def reset_historical_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHistoricalOptions", []))

    @builtins.property
    @jsii.member(jsii_name="historicalOptions")
    def historical_options(
        self,
    ) -> BudgetsBudgetAutoAdjustDataHistoricalOptionsOutputReference:
        return typing.cast(BudgetsBudgetAutoAdjustDataHistoricalOptionsOutputReference, jsii.get(self, "historicalOptions"))

    @builtins.property
    @jsii.member(jsii_name="lastAutoAdjustTime")
    def last_auto_adjust_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastAutoAdjustTime"))

    @builtins.property
    @jsii.member(jsii_name="autoAdjustTypeInput")
    def auto_adjust_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "autoAdjustTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="historicalOptionsInput")
    def historical_options_input(
        self,
    ) -> typing.Optional[BudgetsBudgetAutoAdjustDataHistoricalOptions]:
        return typing.cast(typing.Optional[BudgetsBudgetAutoAdjustDataHistoricalOptions], jsii.get(self, "historicalOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="autoAdjustType")
    def auto_adjust_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "autoAdjustType"))

    @auto_adjust_type.setter
    def auto_adjust_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72cad06da56d19dc447cccc463ec00b3a96f59a9332e3daf9db1355578294b5e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoAdjustType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[BudgetsBudgetAutoAdjustData]:
        return typing.cast(typing.Optional[BudgetsBudgetAutoAdjustData], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[BudgetsBudgetAutoAdjustData],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a9557ec55ba7ca71743f4c0db936652e625577ae29f3abb0c2da4318d08188e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.budgetsBudget.BudgetsBudgetConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "budget_type": "budgetType",
        "time_unit": "timeUnit",
        "account_id": "accountId",
        "auto_adjust_data": "autoAdjustData",
        "cost_filter": "costFilter",
        "cost_filters": "costFilters",
        "cost_types": "costTypes",
        "id": "id",
        "limit_amount": "limitAmount",
        "limit_unit": "limitUnit",
        "name": "name",
        "name_prefix": "namePrefix",
        "notification": "notification",
        "planned_limit": "plannedLimit",
        "time_period_end": "timePeriodEnd",
        "time_period_start": "timePeriodStart",
    },
)
class BudgetsBudgetConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        budget_type: builtins.str,
        time_unit: builtins.str,
        account_id: typing.Optional[builtins.str] = None,
        auto_adjust_data: typing.Optional[typing.Union[BudgetsBudgetAutoAdjustData, typing.Dict[builtins.str, typing.Any]]] = None,
        cost_filter: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["BudgetsBudgetCostFilter", typing.Dict[builtins.str, typing.Any]]]]] = None,
        cost_filters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        cost_types: typing.Optional[typing.Union["BudgetsBudgetCostTypes", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        limit_amount: typing.Optional[builtins.str] = None,
        limit_unit: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        name_prefix: typing.Optional[builtins.str] = None,
        notification: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["BudgetsBudgetNotification", typing.Dict[builtins.str, typing.Any]]]]] = None,
        planned_limit: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["BudgetsBudgetPlannedLimit", typing.Dict[builtins.str, typing.Any]]]]] = None,
        time_period_end: typing.Optional[builtins.str] = None,
        time_period_start: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param budget_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#budget_type BudgetsBudget#budget_type}.
        :param time_unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#time_unit BudgetsBudget#time_unit}.
        :param account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#account_id BudgetsBudget#account_id}.
        :param auto_adjust_data: auto_adjust_data block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#auto_adjust_data BudgetsBudget#auto_adjust_data}
        :param cost_filter: cost_filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#cost_filter BudgetsBudget#cost_filter}
        :param cost_filters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#cost_filters BudgetsBudget#cost_filters}.
        :param cost_types: cost_types block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#cost_types BudgetsBudget#cost_types}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#id BudgetsBudget#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param limit_amount: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#limit_amount BudgetsBudget#limit_amount}.
        :param limit_unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#limit_unit BudgetsBudget#limit_unit}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#name BudgetsBudget#name}.
        :param name_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#name_prefix BudgetsBudget#name_prefix}.
        :param notification: notification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#notification BudgetsBudget#notification}
        :param planned_limit: planned_limit block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#planned_limit BudgetsBudget#planned_limit}
        :param time_period_end: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#time_period_end BudgetsBudget#time_period_end}.
        :param time_period_start: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#time_period_start BudgetsBudget#time_period_start}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(auto_adjust_data, dict):
            auto_adjust_data = BudgetsBudgetAutoAdjustData(**auto_adjust_data)
        if isinstance(cost_types, dict):
            cost_types = BudgetsBudgetCostTypes(**cost_types)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a57d66f1694981333f2e43fd0bfe47281eea40cb6633d475795fa4b520c1bf1)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument budget_type", value=budget_type, expected_type=type_hints["budget_type"])
            check_type(argname="argument time_unit", value=time_unit, expected_type=type_hints["time_unit"])
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
            check_type(argname="argument auto_adjust_data", value=auto_adjust_data, expected_type=type_hints["auto_adjust_data"])
            check_type(argname="argument cost_filter", value=cost_filter, expected_type=type_hints["cost_filter"])
            check_type(argname="argument cost_filters", value=cost_filters, expected_type=type_hints["cost_filters"])
            check_type(argname="argument cost_types", value=cost_types, expected_type=type_hints["cost_types"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument limit_amount", value=limit_amount, expected_type=type_hints["limit_amount"])
            check_type(argname="argument limit_unit", value=limit_unit, expected_type=type_hints["limit_unit"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument name_prefix", value=name_prefix, expected_type=type_hints["name_prefix"])
            check_type(argname="argument notification", value=notification, expected_type=type_hints["notification"])
            check_type(argname="argument planned_limit", value=planned_limit, expected_type=type_hints["planned_limit"])
            check_type(argname="argument time_period_end", value=time_period_end, expected_type=type_hints["time_period_end"])
            check_type(argname="argument time_period_start", value=time_period_start, expected_type=type_hints["time_period_start"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "budget_type": budget_type,
            "time_unit": time_unit,
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
        if auto_adjust_data is not None:
            self._values["auto_adjust_data"] = auto_adjust_data
        if cost_filter is not None:
            self._values["cost_filter"] = cost_filter
        if cost_filters is not None:
            self._values["cost_filters"] = cost_filters
        if cost_types is not None:
            self._values["cost_types"] = cost_types
        if id is not None:
            self._values["id"] = id
        if limit_amount is not None:
            self._values["limit_amount"] = limit_amount
        if limit_unit is not None:
            self._values["limit_unit"] = limit_unit
        if name is not None:
            self._values["name"] = name
        if name_prefix is not None:
            self._values["name_prefix"] = name_prefix
        if notification is not None:
            self._values["notification"] = notification
        if planned_limit is not None:
            self._values["planned_limit"] = planned_limit
        if time_period_end is not None:
            self._values["time_period_end"] = time_period_end
        if time_period_start is not None:
            self._values["time_period_start"] = time_period_start

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
    def budget_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#budget_type BudgetsBudget#budget_type}.'''
        result = self._values.get("budget_type")
        assert result is not None, "Required property 'budget_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def time_unit(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#time_unit BudgetsBudget#time_unit}.'''
        result = self._values.get("time_unit")
        assert result is not None, "Required property 'time_unit' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def account_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#account_id BudgetsBudget#account_id}.'''
        result = self._values.get("account_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def auto_adjust_data(self) -> typing.Optional[BudgetsBudgetAutoAdjustData]:
        '''auto_adjust_data block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#auto_adjust_data BudgetsBudget#auto_adjust_data}
        '''
        result = self._values.get("auto_adjust_data")
        return typing.cast(typing.Optional[BudgetsBudgetAutoAdjustData], result)

    @builtins.property
    def cost_filter(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["BudgetsBudgetCostFilter"]]]:
        '''cost_filter block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#cost_filter BudgetsBudget#cost_filter}
        '''
        result = self._values.get("cost_filter")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["BudgetsBudgetCostFilter"]]], result)

    @builtins.property
    def cost_filters(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#cost_filters BudgetsBudget#cost_filters}.'''
        result = self._values.get("cost_filters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def cost_types(self) -> typing.Optional["BudgetsBudgetCostTypes"]:
        '''cost_types block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#cost_types BudgetsBudget#cost_types}
        '''
        result = self._values.get("cost_types")
        return typing.cast(typing.Optional["BudgetsBudgetCostTypes"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#id BudgetsBudget#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def limit_amount(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#limit_amount BudgetsBudget#limit_amount}.'''
        result = self._values.get("limit_amount")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def limit_unit(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#limit_unit BudgetsBudget#limit_unit}.'''
        result = self._values.get("limit_unit")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#name BudgetsBudget#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#name_prefix BudgetsBudget#name_prefix}.'''
        result = self._values.get("name_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def notification(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["BudgetsBudgetNotification"]]]:
        '''notification block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#notification BudgetsBudget#notification}
        '''
        result = self._values.get("notification")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["BudgetsBudgetNotification"]]], result)

    @builtins.property
    def planned_limit(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["BudgetsBudgetPlannedLimit"]]]:
        '''planned_limit block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#planned_limit BudgetsBudget#planned_limit}
        '''
        result = self._values.get("planned_limit")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["BudgetsBudgetPlannedLimit"]]], result)

    @builtins.property
    def time_period_end(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#time_period_end BudgetsBudget#time_period_end}.'''
        result = self._values.get("time_period_end")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def time_period_start(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#time_period_start BudgetsBudget#time_period_start}.'''
        result = self._values.get("time_period_start")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BudgetsBudgetConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.budgetsBudget.BudgetsBudgetCostFilter",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "values": "values"},
)
class BudgetsBudgetCostFilter:
    def __init__(
        self,
        *,
        name: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#name BudgetsBudget#name}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#values BudgetsBudget#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ccc5ca6a65328ca23d543a35b9d60c654eff42ee34e14a729814e481174f1105)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "values": values,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#name BudgetsBudget#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#values BudgetsBudget#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BudgetsBudgetCostFilter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BudgetsBudgetCostFilterList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.budgetsBudget.BudgetsBudgetCostFilterList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__bd35c9f41e7d3af33af08feaad71866ba1881736fd4983a01b88d58330f71492)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "BudgetsBudgetCostFilterOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a27c5cde2009d466f61aebb8298d809432e477d3a577982e6f2d0e29b613ef5)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("BudgetsBudgetCostFilterOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a979b6d522d27a10c12af5fb7f65be5024b4bab8744e4dd12c9319406c71071)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4f75cdf826663436926a0dc30dcb5de85868340b0e16ded358fe41afe833caec)
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
            type_hints = typing.get_type_hints(_typecheckingstub__30bc42c75aaf78062fd8e7c62c5fb0678b9b27e68fcd5db7e3ff346c6ece5303)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[BudgetsBudgetCostFilter]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[BudgetsBudgetCostFilter]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[BudgetsBudgetCostFilter]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__807f3f3ad2ae9922431babe2c4d5562f9e324ab81b0775d548ef76f811c47518)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class BudgetsBudgetCostFilterOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.budgetsBudget.BudgetsBudgetCostFilterOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__12ead4c4510ff22a7c2f841f2fc8affe5c9bb74a536063a6fa86929120c727c0)
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
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d7fe8eb9d628de4f0cda8ab865190fa88621bf40812ba8910ba39b2ecdbe079)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0cb373716a0c617923cd4c3cb569195bc19bf08bfcfd0a5e89324866ac2387d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[BudgetsBudgetCostFilter, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[BudgetsBudgetCostFilter, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[BudgetsBudgetCostFilter, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b6ae1eeda5e711f21961761a3080cec802938f2591b7d14eb9283f699b4fa81)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.budgetsBudget.BudgetsBudgetCostTypes",
    jsii_struct_bases=[],
    name_mapping={
        "include_credit": "includeCredit",
        "include_discount": "includeDiscount",
        "include_other_subscription": "includeOtherSubscription",
        "include_recurring": "includeRecurring",
        "include_refund": "includeRefund",
        "include_subscription": "includeSubscription",
        "include_support": "includeSupport",
        "include_tax": "includeTax",
        "include_upfront": "includeUpfront",
        "use_amortized": "useAmortized",
        "use_blended": "useBlended",
    },
)
class BudgetsBudgetCostTypes:
    def __init__(
        self,
        *,
        include_credit: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        include_discount: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        include_other_subscription: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        include_recurring: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        include_refund: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        include_subscription: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        include_support: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        include_tax: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        include_upfront: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        use_amortized: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        use_blended: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param include_credit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#include_credit BudgetsBudget#include_credit}.
        :param include_discount: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#include_discount BudgetsBudget#include_discount}.
        :param include_other_subscription: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#include_other_subscription BudgetsBudget#include_other_subscription}.
        :param include_recurring: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#include_recurring BudgetsBudget#include_recurring}.
        :param include_refund: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#include_refund BudgetsBudget#include_refund}.
        :param include_subscription: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#include_subscription BudgetsBudget#include_subscription}.
        :param include_support: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#include_support BudgetsBudget#include_support}.
        :param include_tax: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#include_tax BudgetsBudget#include_tax}.
        :param include_upfront: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#include_upfront BudgetsBudget#include_upfront}.
        :param use_amortized: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#use_amortized BudgetsBudget#use_amortized}.
        :param use_blended: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#use_blended BudgetsBudget#use_blended}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e792876d5cbdcd87090370c53e06c9bc1db61e76ba6c71e0952ef0016d2b6dc7)
            check_type(argname="argument include_credit", value=include_credit, expected_type=type_hints["include_credit"])
            check_type(argname="argument include_discount", value=include_discount, expected_type=type_hints["include_discount"])
            check_type(argname="argument include_other_subscription", value=include_other_subscription, expected_type=type_hints["include_other_subscription"])
            check_type(argname="argument include_recurring", value=include_recurring, expected_type=type_hints["include_recurring"])
            check_type(argname="argument include_refund", value=include_refund, expected_type=type_hints["include_refund"])
            check_type(argname="argument include_subscription", value=include_subscription, expected_type=type_hints["include_subscription"])
            check_type(argname="argument include_support", value=include_support, expected_type=type_hints["include_support"])
            check_type(argname="argument include_tax", value=include_tax, expected_type=type_hints["include_tax"])
            check_type(argname="argument include_upfront", value=include_upfront, expected_type=type_hints["include_upfront"])
            check_type(argname="argument use_amortized", value=use_amortized, expected_type=type_hints["use_amortized"])
            check_type(argname="argument use_blended", value=use_blended, expected_type=type_hints["use_blended"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if include_credit is not None:
            self._values["include_credit"] = include_credit
        if include_discount is not None:
            self._values["include_discount"] = include_discount
        if include_other_subscription is not None:
            self._values["include_other_subscription"] = include_other_subscription
        if include_recurring is not None:
            self._values["include_recurring"] = include_recurring
        if include_refund is not None:
            self._values["include_refund"] = include_refund
        if include_subscription is not None:
            self._values["include_subscription"] = include_subscription
        if include_support is not None:
            self._values["include_support"] = include_support
        if include_tax is not None:
            self._values["include_tax"] = include_tax
        if include_upfront is not None:
            self._values["include_upfront"] = include_upfront
        if use_amortized is not None:
            self._values["use_amortized"] = use_amortized
        if use_blended is not None:
            self._values["use_blended"] = use_blended

    @builtins.property
    def include_credit(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#include_credit BudgetsBudget#include_credit}.'''
        result = self._values.get("include_credit")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def include_discount(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#include_discount BudgetsBudget#include_discount}.'''
        result = self._values.get("include_discount")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def include_other_subscription(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#include_other_subscription BudgetsBudget#include_other_subscription}.'''
        result = self._values.get("include_other_subscription")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def include_recurring(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#include_recurring BudgetsBudget#include_recurring}.'''
        result = self._values.get("include_recurring")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def include_refund(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#include_refund BudgetsBudget#include_refund}.'''
        result = self._values.get("include_refund")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def include_subscription(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#include_subscription BudgetsBudget#include_subscription}.'''
        result = self._values.get("include_subscription")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def include_support(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#include_support BudgetsBudget#include_support}.'''
        result = self._values.get("include_support")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def include_tax(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#include_tax BudgetsBudget#include_tax}.'''
        result = self._values.get("include_tax")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def include_upfront(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#include_upfront BudgetsBudget#include_upfront}.'''
        result = self._values.get("include_upfront")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def use_amortized(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#use_amortized BudgetsBudget#use_amortized}.'''
        result = self._values.get("use_amortized")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def use_blended(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#use_blended BudgetsBudget#use_blended}.'''
        result = self._values.get("use_blended")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BudgetsBudgetCostTypes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BudgetsBudgetCostTypesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.budgetsBudget.BudgetsBudgetCostTypesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__949ab37769299079ad00e28f371156a975eb11686e50a16c03082a698aa1a9c5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetIncludeCredit")
    def reset_include_credit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludeCredit", []))

    @jsii.member(jsii_name="resetIncludeDiscount")
    def reset_include_discount(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludeDiscount", []))

    @jsii.member(jsii_name="resetIncludeOtherSubscription")
    def reset_include_other_subscription(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludeOtherSubscription", []))

    @jsii.member(jsii_name="resetIncludeRecurring")
    def reset_include_recurring(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludeRecurring", []))

    @jsii.member(jsii_name="resetIncludeRefund")
    def reset_include_refund(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludeRefund", []))

    @jsii.member(jsii_name="resetIncludeSubscription")
    def reset_include_subscription(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludeSubscription", []))

    @jsii.member(jsii_name="resetIncludeSupport")
    def reset_include_support(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludeSupport", []))

    @jsii.member(jsii_name="resetIncludeTax")
    def reset_include_tax(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludeTax", []))

    @jsii.member(jsii_name="resetIncludeUpfront")
    def reset_include_upfront(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludeUpfront", []))

    @jsii.member(jsii_name="resetUseAmortized")
    def reset_use_amortized(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUseAmortized", []))

    @jsii.member(jsii_name="resetUseBlended")
    def reset_use_blended(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUseBlended", []))

    @builtins.property
    @jsii.member(jsii_name="includeCreditInput")
    def include_credit_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "includeCreditInput"))

    @builtins.property
    @jsii.member(jsii_name="includeDiscountInput")
    def include_discount_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "includeDiscountInput"))

    @builtins.property
    @jsii.member(jsii_name="includeOtherSubscriptionInput")
    def include_other_subscription_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "includeOtherSubscriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="includeRecurringInput")
    def include_recurring_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "includeRecurringInput"))

    @builtins.property
    @jsii.member(jsii_name="includeRefundInput")
    def include_refund_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "includeRefundInput"))

    @builtins.property
    @jsii.member(jsii_name="includeSubscriptionInput")
    def include_subscription_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "includeSubscriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="includeSupportInput")
    def include_support_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "includeSupportInput"))

    @builtins.property
    @jsii.member(jsii_name="includeTaxInput")
    def include_tax_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "includeTaxInput"))

    @builtins.property
    @jsii.member(jsii_name="includeUpfrontInput")
    def include_upfront_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "includeUpfrontInput"))

    @builtins.property
    @jsii.member(jsii_name="useAmortizedInput")
    def use_amortized_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "useAmortizedInput"))

    @builtins.property
    @jsii.member(jsii_name="useBlendedInput")
    def use_blended_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "useBlendedInput"))

    @builtins.property
    @jsii.member(jsii_name="includeCredit")
    def include_credit(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "includeCredit"))

    @include_credit.setter
    def include_credit(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf1ba00bee3b22ec9f26797097ddf52c3ec1c4764a296eb4a0e4233b256e600d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includeCredit", value)

    @builtins.property
    @jsii.member(jsii_name="includeDiscount")
    def include_discount(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "includeDiscount"))

    @include_discount.setter
    def include_discount(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1257fc963ee084bcc24f5505437f25c43a8ede2a4cb2e15936d4f10d3c37d842)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includeDiscount", value)

    @builtins.property
    @jsii.member(jsii_name="includeOtherSubscription")
    def include_other_subscription(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "includeOtherSubscription"))

    @include_other_subscription.setter
    def include_other_subscription(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49d183727c2e15d15b881759d3b0533125efc64a5b4fd8a948d7dd0f23ecc559)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includeOtherSubscription", value)

    @builtins.property
    @jsii.member(jsii_name="includeRecurring")
    def include_recurring(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "includeRecurring"))

    @include_recurring.setter
    def include_recurring(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ead02199cbc8ae4591253659a6839bb01c50f4824292f38f51759a8ef080224)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includeRecurring", value)

    @builtins.property
    @jsii.member(jsii_name="includeRefund")
    def include_refund(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "includeRefund"))

    @include_refund.setter
    def include_refund(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de91b59cf3c3655a730aa094d4e502ce4eec0feb83b8f185f89ab77e44229b68)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includeRefund", value)

    @builtins.property
    @jsii.member(jsii_name="includeSubscription")
    def include_subscription(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "includeSubscription"))

    @include_subscription.setter
    def include_subscription(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c19d7383af006654770494dca7c073c0c5956035fc693fdaac46636399bfc134)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includeSubscription", value)

    @builtins.property
    @jsii.member(jsii_name="includeSupport")
    def include_support(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "includeSupport"))

    @include_support.setter
    def include_support(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa4ec13efb39ad365c7c0e5d50c7c030b9401e3ebeeb880ecce3ade7a37ccac8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includeSupport", value)

    @builtins.property
    @jsii.member(jsii_name="includeTax")
    def include_tax(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "includeTax"))

    @include_tax.setter
    def include_tax(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e099c35bacdf5291ce9afc9e7b274d6141e40e468dd163543dd8244be46b772)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includeTax", value)

    @builtins.property
    @jsii.member(jsii_name="includeUpfront")
    def include_upfront(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "includeUpfront"))

    @include_upfront.setter
    def include_upfront(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__317b8628e55f34a1138653bb436b93e462453e80ac26a0741515b5dd6e607aee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includeUpfront", value)

    @builtins.property
    @jsii.member(jsii_name="useAmortized")
    def use_amortized(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "useAmortized"))

    @use_amortized.setter
    def use_amortized(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__449dde6636cf6955c58eafecb66c18ed3dc9456dc9ed88fdcc4e14df127f76a1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useAmortized", value)

    @builtins.property
    @jsii.member(jsii_name="useBlended")
    def use_blended(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "useBlended"))

    @use_blended.setter
    def use_blended(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__120dc981302fe921a3926a5d2aaa1903a9c3f2166f3d695f750883a84522cbd3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useBlended", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[BudgetsBudgetCostTypes]:
        return typing.cast(typing.Optional[BudgetsBudgetCostTypes], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[BudgetsBudgetCostTypes]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be854f967161b7efd19975d2ea3d9d7cd5e5261ec5636de9ffafb9d2475727eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.budgetsBudget.BudgetsBudgetNotification",
    jsii_struct_bases=[],
    name_mapping={
        "comparison_operator": "comparisonOperator",
        "notification_type": "notificationType",
        "threshold": "threshold",
        "threshold_type": "thresholdType",
        "subscriber_email_addresses": "subscriberEmailAddresses",
        "subscriber_sns_topic_arns": "subscriberSnsTopicArns",
    },
)
class BudgetsBudgetNotification:
    def __init__(
        self,
        *,
        comparison_operator: builtins.str,
        notification_type: builtins.str,
        threshold: jsii.Number,
        threshold_type: builtins.str,
        subscriber_email_addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
        subscriber_sns_topic_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param comparison_operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#comparison_operator BudgetsBudget#comparison_operator}.
        :param notification_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#notification_type BudgetsBudget#notification_type}.
        :param threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#threshold BudgetsBudget#threshold}.
        :param threshold_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#threshold_type BudgetsBudget#threshold_type}.
        :param subscriber_email_addresses: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#subscriber_email_addresses BudgetsBudget#subscriber_email_addresses}.
        :param subscriber_sns_topic_arns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#subscriber_sns_topic_arns BudgetsBudget#subscriber_sns_topic_arns}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab948bc31149515277f33684f873967d20e2fd146c011063a82918e71c196c5a)
            check_type(argname="argument comparison_operator", value=comparison_operator, expected_type=type_hints["comparison_operator"])
            check_type(argname="argument notification_type", value=notification_type, expected_type=type_hints["notification_type"])
            check_type(argname="argument threshold", value=threshold, expected_type=type_hints["threshold"])
            check_type(argname="argument threshold_type", value=threshold_type, expected_type=type_hints["threshold_type"])
            check_type(argname="argument subscriber_email_addresses", value=subscriber_email_addresses, expected_type=type_hints["subscriber_email_addresses"])
            check_type(argname="argument subscriber_sns_topic_arns", value=subscriber_sns_topic_arns, expected_type=type_hints["subscriber_sns_topic_arns"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "comparison_operator": comparison_operator,
            "notification_type": notification_type,
            "threshold": threshold,
            "threshold_type": threshold_type,
        }
        if subscriber_email_addresses is not None:
            self._values["subscriber_email_addresses"] = subscriber_email_addresses
        if subscriber_sns_topic_arns is not None:
            self._values["subscriber_sns_topic_arns"] = subscriber_sns_topic_arns

    @builtins.property
    def comparison_operator(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#comparison_operator BudgetsBudget#comparison_operator}.'''
        result = self._values.get("comparison_operator")
        assert result is not None, "Required property 'comparison_operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def notification_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#notification_type BudgetsBudget#notification_type}.'''
        result = self._values.get("notification_type")
        assert result is not None, "Required property 'notification_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def threshold(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#threshold BudgetsBudget#threshold}.'''
        result = self._values.get("threshold")
        assert result is not None, "Required property 'threshold' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def threshold_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#threshold_type BudgetsBudget#threshold_type}.'''
        result = self._values.get("threshold_type")
        assert result is not None, "Required property 'threshold_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subscriber_email_addresses(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#subscriber_email_addresses BudgetsBudget#subscriber_email_addresses}.'''
        result = self._values.get("subscriber_email_addresses")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def subscriber_sns_topic_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#subscriber_sns_topic_arns BudgetsBudget#subscriber_sns_topic_arns}.'''
        result = self._values.get("subscriber_sns_topic_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BudgetsBudgetNotification(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BudgetsBudgetNotificationList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.budgetsBudget.BudgetsBudgetNotificationList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__369e0d2d5e7b0a6e62deb7d494e969a5b02a5ab89ff6dfd438e8b8118a1ad86d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "BudgetsBudgetNotificationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77d0cb2bc0ee121753b3d950adebffa58a04de22df28f0fe488e4c905c5ee87d)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("BudgetsBudgetNotificationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c02427d2ba81eb16167ee7f9ed4cd75b27acebbad5f595a64e6d266c190d4066)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0da3f8cfd3096ce4b4f72b3721d000abde2b8cc44bac586a3e5c51c737c7506b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d17ff07c7735df9f37439052d8bf93b4218dad631fdd3288e6fd77275a3f0ee5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[BudgetsBudgetNotification]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[BudgetsBudgetNotification]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[BudgetsBudgetNotification]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__279cb5c8a162affd071992a19464f1b02fe7683e5dc1a2d17640980895fbea86)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class BudgetsBudgetNotificationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.budgetsBudget.BudgetsBudgetNotificationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__41499064d75d7cf466165961e74ca9d9dd29914bca254afb0d467fad17e53684)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetSubscriberEmailAddresses")
    def reset_subscriber_email_addresses(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubscriberEmailAddresses", []))

    @jsii.member(jsii_name="resetSubscriberSnsTopicArns")
    def reset_subscriber_sns_topic_arns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubscriberSnsTopicArns", []))

    @builtins.property
    @jsii.member(jsii_name="comparisonOperatorInput")
    def comparison_operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "comparisonOperatorInput"))

    @builtins.property
    @jsii.member(jsii_name="notificationTypeInput")
    def notification_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "notificationTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="subscriberEmailAddressesInput")
    def subscriber_email_addresses_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "subscriberEmailAddressesInput"))

    @builtins.property
    @jsii.member(jsii_name="subscriberSnsTopicArnsInput")
    def subscriber_sns_topic_arns_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "subscriberSnsTopicArnsInput"))

    @builtins.property
    @jsii.member(jsii_name="thresholdInput")
    def threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "thresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="thresholdTypeInput")
    def threshold_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "thresholdTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="comparisonOperator")
    def comparison_operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "comparisonOperator"))

    @comparison_operator.setter
    def comparison_operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f7bd20698e996e941e0c80688aa15ae1ef9b5e73157db3b98e4d665e206baee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "comparisonOperator", value)

    @builtins.property
    @jsii.member(jsii_name="notificationType")
    def notification_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "notificationType"))

    @notification_type.setter
    def notification_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__768abdcf890e0ee60d7536aebad77141c0e26d3a5dc9e447928992fcd8f30705)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notificationType", value)

    @builtins.property
    @jsii.member(jsii_name="subscriberEmailAddresses")
    def subscriber_email_addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subscriberEmailAddresses"))

    @subscriber_email_addresses.setter
    def subscriber_email_addresses(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3db9896ff4aa0be4c4d0819ba83c1525e3ac82b2c8413b7d21fe6e7e30174e71)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subscriberEmailAddresses", value)

    @builtins.property
    @jsii.member(jsii_name="subscriberSnsTopicArns")
    def subscriber_sns_topic_arns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subscriberSnsTopicArns"))

    @subscriber_sns_topic_arns.setter
    def subscriber_sns_topic_arns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a2d58a90142d61f2e00e99348d7200cb08b9e6df0fbf9006fee1a9cd0f0174b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subscriberSnsTopicArns", value)

    @builtins.property
    @jsii.member(jsii_name="threshold")
    def threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "threshold"))

    @threshold.setter
    def threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ed940785b0ae0ac44d97696f617c6a02ce7cfcbcc9aedcc08792d110df6ad52)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "threshold", value)

    @builtins.property
    @jsii.member(jsii_name="thresholdType")
    def threshold_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "thresholdType"))

    @threshold_type.setter
    def threshold_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__186d14966e724ce43db1ed98d52dbe149546e729f2e7b6fabe9aacebcbd3ccaf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "thresholdType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[BudgetsBudgetNotification, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[BudgetsBudgetNotification, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[BudgetsBudgetNotification, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__599fa45232f42b616dc7a66317a3112dfb35a9f49e2da565cc9d1ca94a5b8ca8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.budgetsBudget.BudgetsBudgetPlannedLimit",
    jsii_struct_bases=[],
    name_mapping={"amount": "amount", "start_time": "startTime", "unit": "unit"},
)
class BudgetsBudgetPlannedLimit:
    def __init__(
        self,
        *,
        amount: builtins.str,
        start_time: builtins.str,
        unit: builtins.str,
    ) -> None:
        '''
        :param amount: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#amount BudgetsBudget#amount}.
        :param start_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#start_time BudgetsBudget#start_time}.
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#unit BudgetsBudget#unit}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c84a8109ef7039a1eecfc958a971494b0bcd029a1f4adc6ae24eb5991a22c7b5)
            check_type(argname="argument amount", value=amount, expected_type=type_hints["amount"])
            check_type(argname="argument start_time", value=start_time, expected_type=type_hints["start_time"])
            check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "amount": amount,
            "start_time": start_time,
            "unit": unit,
        }

    @builtins.property
    def amount(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#amount BudgetsBudget#amount}.'''
        result = self._values.get("amount")
        assert result is not None, "Required property 'amount' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def start_time(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#start_time BudgetsBudget#start_time}.'''
        result = self._values.get("start_time")
        assert result is not None, "Required property 'start_time' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def unit(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/budgets_budget#unit BudgetsBudget#unit}.'''
        result = self._values.get("unit")
        assert result is not None, "Required property 'unit' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BudgetsBudgetPlannedLimit(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BudgetsBudgetPlannedLimitList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.budgetsBudget.BudgetsBudgetPlannedLimitList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__202444ab3007cacd4823295414780c7ee7777977c9972414c4180d54ad4aafce)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "BudgetsBudgetPlannedLimitOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d77508e83e6b0ba59816d6ea06c3c0473f26c6b865442a6eb9031bce7c334ad7)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("BudgetsBudgetPlannedLimitOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__34c4d4cfc75f4c89b24ac98bafb8fe520e3289cf3bca0e2c12b8d6125fbfb1cb)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9602a1d2155442db1ca51f977df87f3d4f3454d2387e09d283189bb5fb9f7cff)
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
            type_hints = typing.get_type_hints(_typecheckingstub__98e620a5a52c14ce29bd73ab1c7cfc7e186cce8fce8db07366d24fbdac65c55a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[BudgetsBudgetPlannedLimit]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[BudgetsBudgetPlannedLimit]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[BudgetsBudgetPlannedLimit]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d2d0bcd13d351451b31a9ed159bee648e1b5ac107ba436edba725e7445125f4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class BudgetsBudgetPlannedLimitOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.budgetsBudget.BudgetsBudgetPlannedLimitOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__44a67f51a1a8d9a2f68b1af12437986733d1a2a0bf13b4344ccaa2672a9ec5f0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="amountInput")
    def amount_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "amountInput"))

    @builtins.property
    @jsii.member(jsii_name="startTimeInput")
    def start_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "startTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="unitInput")
    def unit_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "unitInput"))

    @builtins.property
    @jsii.member(jsii_name="amount")
    def amount(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "amount"))

    @amount.setter
    def amount(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d5bdd9bd893fc482cb5f6f3daf3a4ba8c35166dccc059ce185515e7529ca546)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "amount", value)

    @builtins.property
    @jsii.member(jsii_name="startTime")
    def start_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "startTime"))

    @start_time.setter
    def start_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9816f7ed729251535194b9e77c7a1fbbdb2a8c7b87c1d1fefa4b0b1459827468)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startTime", value)

    @builtins.property
    @jsii.member(jsii_name="unit")
    def unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "unit"))

    @unit.setter
    def unit(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f811c879496a5789ded9410dbbb8b80cc03c4a1ca966c7c4e2135955f9314702)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unit", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[BudgetsBudgetPlannedLimit, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[BudgetsBudgetPlannedLimit, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[BudgetsBudgetPlannedLimit, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__317da42d3cedf6b60842a0e0e46206444fb5a2b28c3e530bc21a3b51aee2014c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "BudgetsBudget",
    "BudgetsBudgetAutoAdjustData",
    "BudgetsBudgetAutoAdjustDataHistoricalOptions",
    "BudgetsBudgetAutoAdjustDataHistoricalOptionsOutputReference",
    "BudgetsBudgetAutoAdjustDataOutputReference",
    "BudgetsBudgetConfig",
    "BudgetsBudgetCostFilter",
    "BudgetsBudgetCostFilterList",
    "BudgetsBudgetCostFilterOutputReference",
    "BudgetsBudgetCostTypes",
    "BudgetsBudgetCostTypesOutputReference",
    "BudgetsBudgetNotification",
    "BudgetsBudgetNotificationList",
    "BudgetsBudgetNotificationOutputReference",
    "BudgetsBudgetPlannedLimit",
    "BudgetsBudgetPlannedLimitList",
    "BudgetsBudgetPlannedLimitOutputReference",
]

publication.publish()

def _typecheckingstub__356b584a7cb0712c03baaddc0592dc0d71b263b5fa9bac5efb334dce9f5c4a57(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    budget_type: builtins.str,
    time_unit: builtins.str,
    account_id: typing.Optional[builtins.str] = None,
    auto_adjust_data: typing.Optional[typing.Union[BudgetsBudgetAutoAdjustData, typing.Dict[builtins.str, typing.Any]]] = None,
    cost_filter: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[BudgetsBudgetCostFilter, typing.Dict[builtins.str, typing.Any]]]]] = None,
    cost_filters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    cost_types: typing.Optional[typing.Union[BudgetsBudgetCostTypes, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    limit_amount: typing.Optional[builtins.str] = None,
    limit_unit: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    name_prefix: typing.Optional[builtins.str] = None,
    notification: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[BudgetsBudgetNotification, typing.Dict[builtins.str, typing.Any]]]]] = None,
    planned_limit: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[BudgetsBudgetPlannedLimit, typing.Dict[builtins.str, typing.Any]]]]] = None,
    time_period_end: typing.Optional[builtins.str] = None,
    time_period_start: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__8db66af9aa933ace25e2ddfd9875aa33ed46fc46b403cde56b7d38943a6fadfd(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[BudgetsBudgetCostFilter, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9da005e8dcca95795770d3a740e7e05fbf7ab032534b7365a3f4467c0aca8e5(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[BudgetsBudgetNotification, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f924c48667cf8ba03181993ff23654d3433bea3fbf97e66d6a3dc6a33ca9596(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[BudgetsBudgetPlannedLimit, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bcaa4c0fd65d487a7b900998f2d8e187d574b52f961e53821195b4f9da40ca71(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__508435880c6f7bbf0a77123a48406de10bb9937063a83e23eac3405b1fe8e9f2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8109f77e478ab539e59451fa5963568855a37a3a7ce9a623b4691b0f12bbd8cf(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__115d0c7908223f8f3403b0117c216cd313ff356c3da27a775b6b8b5ca0b5a9ac(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1007b7573eaae3601280ccf50ae3b0dcc6e0e274830986dd7a371931b5451e9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28926a00fbdc5bdaf74b51154c49744df1721e231feb53b376ff19bda4c7fd54(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42fd8774fbaae4d74f29106ed6176725cf1bfe5677c6037d7b4457cf4a3d1df2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d9197caae863b07651316149341924af52d2584db68f49ae1bf8fb7f775f614(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__864a581f3219bc31637bc3e4c3712323c15afb9fc271717a22295a5c9fc786ed(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a4485d56d914ce8e1a8369c98beabd26ab74717bd9d2f24b8b9b75c55044728(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4285fd98afb64132deb35a54e4f71db4afe00149ae34ebf460c29db0cfb42110(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1d1529d0cd1b8f17e844e48ef202401589b16b7e6c41bbb14fc6fd0df44ba07(
    *,
    auto_adjust_type: builtins.str,
    historical_options: typing.Optional[typing.Union[BudgetsBudgetAutoAdjustDataHistoricalOptions, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__596f0f5271bb13dd686b848042478ac80d76dc1105233265f63f42d05c16854e(
    *,
    budget_adjustment_period: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db629e4def2198b67282eebf51b3cab5a39808f95d05e473ed035841daf901d9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4587436cb17291e6944869948eccff50dc6a54e8f043ceea7fe34c728a1b3310(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d94257eef8d822dda756ddc2f3f380e947a97d7755778e042acf6714c949dbad(
    value: typing.Optional[BudgetsBudgetAutoAdjustDataHistoricalOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b76471cc00c34bff0c5a68d7ce75269f6b23b70870f4cb2bdfe82dead5ec3cb3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72cad06da56d19dc447cccc463ec00b3a96f59a9332e3daf9db1355578294b5e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a9557ec55ba7ca71743f4c0db936652e625577ae29f3abb0c2da4318d08188e(
    value: typing.Optional[BudgetsBudgetAutoAdjustData],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a57d66f1694981333f2e43fd0bfe47281eea40cb6633d475795fa4b520c1bf1(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    budget_type: builtins.str,
    time_unit: builtins.str,
    account_id: typing.Optional[builtins.str] = None,
    auto_adjust_data: typing.Optional[typing.Union[BudgetsBudgetAutoAdjustData, typing.Dict[builtins.str, typing.Any]]] = None,
    cost_filter: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[BudgetsBudgetCostFilter, typing.Dict[builtins.str, typing.Any]]]]] = None,
    cost_filters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    cost_types: typing.Optional[typing.Union[BudgetsBudgetCostTypes, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    limit_amount: typing.Optional[builtins.str] = None,
    limit_unit: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    name_prefix: typing.Optional[builtins.str] = None,
    notification: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[BudgetsBudgetNotification, typing.Dict[builtins.str, typing.Any]]]]] = None,
    planned_limit: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[BudgetsBudgetPlannedLimit, typing.Dict[builtins.str, typing.Any]]]]] = None,
    time_period_end: typing.Optional[builtins.str] = None,
    time_period_start: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ccc5ca6a65328ca23d543a35b9d60c654eff42ee34e14a729814e481174f1105(
    *,
    name: builtins.str,
    values: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd35c9f41e7d3af33af08feaad71866ba1881736fd4983a01b88d58330f71492(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a27c5cde2009d466f61aebb8298d809432e477d3a577982e6f2d0e29b613ef5(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a979b6d522d27a10c12af5fb7f65be5024b4bab8744e4dd12c9319406c71071(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f75cdf826663436926a0dc30dcb5de85868340b0e16ded358fe41afe833caec(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30bc42c75aaf78062fd8e7c62c5fb0678b9b27e68fcd5db7e3ff346c6ece5303(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__807f3f3ad2ae9922431babe2c4d5562f9e324ab81b0775d548ef76f811c47518(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[BudgetsBudgetCostFilter]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12ead4c4510ff22a7c2f841f2fc8affe5c9bb74a536063a6fa86929120c727c0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d7fe8eb9d628de4f0cda8ab865190fa88621bf40812ba8910ba39b2ecdbe079(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0cb373716a0c617923cd4c3cb569195bc19bf08bfcfd0a5e89324866ac2387d(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b6ae1eeda5e711f21961761a3080cec802938f2591b7d14eb9283f699b4fa81(
    value: typing.Optional[typing.Union[BudgetsBudgetCostFilter, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e792876d5cbdcd87090370c53e06c9bc1db61e76ba6c71e0952ef0016d2b6dc7(
    *,
    include_credit: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    include_discount: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    include_other_subscription: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    include_recurring: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    include_refund: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    include_subscription: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    include_support: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    include_tax: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    include_upfront: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    use_amortized: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    use_blended: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__949ab37769299079ad00e28f371156a975eb11686e50a16c03082a698aa1a9c5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf1ba00bee3b22ec9f26797097ddf52c3ec1c4764a296eb4a0e4233b256e600d(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1257fc963ee084bcc24f5505437f25c43a8ede2a4cb2e15936d4f10d3c37d842(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49d183727c2e15d15b881759d3b0533125efc64a5b4fd8a948d7dd0f23ecc559(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ead02199cbc8ae4591253659a6839bb01c50f4824292f38f51759a8ef080224(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de91b59cf3c3655a730aa094d4e502ce4eec0feb83b8f185f89ab77e44229b68(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c19d7383af006654770494dca7c073c0c5956035fc693fdaac46636399bfc134(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa4ec13efb39ad365c7c0e5d50c7c030b9401e3ebeeb880ecce3ade7a37ccac8(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e099c35bacdf5291ce9afc9e7b274d6141e40e468dd163543dd8244be46b772(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__317b8628e55f34a1138653bb436b93e462453e80ac26a0741515b5dd6e607aee(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__449dde6636cf6955c58eafecb66c18ed3dc9456dc9ed88fdcc4e14df127f76a1(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__120dc981302fe921a3926a5d2aaa1903a9c3f2166f3d695f750883a84522cbd3(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be854f967161b7efd19975d2ea3d9d7cd5e5261ec5636de9ffafb9d2475727eb(
    value: typing.Optional[BudgetsBudgetCostTypes],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab948bc31149515277f33684f873967d20e2fd146c011063a82918e71c196c5a(
    *,
    comparison_operator: builtins.str,
    notification_type: builtins.str,
    threshold: jsii.Number,
    threshold_type: builtins.str,
    subscriber_email_addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
    subscriber_sns_topic_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__369e0d2d5e7b0a6e62deb7d494e969a5b02a5ab89ff6dfd438e8b8118a1ad86d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77d0cb2bc0ee121753b3d950adebffa58a04de22df28f0fe488e4c905c5ee87d(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c02427d2ba81eb16167ee7f9ed4cd75b27acebbad5f595a64e6d266c190d4066(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0da3f8cfd3096ce4b4f72b3721d000abde2b8cc44bac586a3e5c51c737c7506b(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d17ff07c7735df9f37439052d8bf93b4218dad631fdd3288e6fd77275a3f0ee5(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__279cb5c8a162affd071992a19464f1b02fe7683e5dc1a2d17640980895fbea86(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[BudgetsBudgetNotification]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41499064d75d7cf466165961e74ca9d9dd29914bca254afb0d467fad17e53684(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f7bd20698e996e941e0c80688aa15ae1ef9b5e73157db3b98e4d665e206baee(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__768abdcf890e0ee60d7536aebad77141c0e26d3a5dc9e447928992fcd8f30705(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3db9896ff4aa0be4c4d0819ba83c1525e3ac82b2c8413b7d21fe6e7e30174e71(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a2d58a90142d61f2e00e99348d7200cb08b9e6df0fbf9006fee1a9cd0f0174b(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ed940785b0ae0ac44d97696f617c6a02ce7cfcbcc9aedcc08792d110df6ad52(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__186d14966e724ce43db1ed98d52dbe149546e729f2e7b6fabe9aacebcbd3ccaf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__599fa45232f42b616dc7a66317a3112dfb35a9f49e2da565cc9d1ca94a5b8ca8(
    value: typing.Optional[typing.Union[BudgetsBudgetNotification, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c84a8109ef7039a1eecfc958a971494b0bcd029a1f4adc6ae24eb5991a22c7b5(
    *,
    amount: builtins.str,
    start_time: builtins.str,
    unit: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__202444ab3007cacd4823295414780c7ee7777977c9972414c4180d54ad4aafce(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d77508e83e6b0ba59816d6ea06c3c0473f26c6b865442a6eb9031bce7c334ad7(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34c4d4cfc75f4c89b24ac98bafb8fe520e3289cf3bca0e2c12b8d6125fbfb1cb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9602a1d2155442db1ca51f977df87f3d4f3454d2387e09d283189bb5fb9f7cff(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98e620a5a52c14ce29bd73ab1c7cfc7e186cce8fce8db07366d24fbdac65c55a(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d2d0bcd13d351451b31a9ed159bee648e1b5ac107ba436edba725e7445125f4(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[BudgetsBudgetPlannedLimit]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44a67f51a1a8d9a2f68b1af12437986733d1a2a0bf13b4344ccaa2672a9ec5f0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d5bdd9bd893fc482cb5f6f3daf3a4ba8c35166dccc059ce185515e7529ca546(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9816f7ed729251535194b9e77c7a1fbbdb2a8c7b87c1d1fefa4b0b1459827468(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f811c879496a5789ded9410dbbb8b80cc03c4a1ca966c7c4e2135955f9314702(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__317da42d3cedf6b60842a0e0e46206444fb5a2b28c3e530bc21a3b51aee2014c(
    value: typing.Optional[typing.Union[BudgetsBudgetPlannedLimit, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
