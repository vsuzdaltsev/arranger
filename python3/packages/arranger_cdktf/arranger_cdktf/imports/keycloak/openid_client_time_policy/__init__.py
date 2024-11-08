"""
# `keycloak_openid_client_time_policy`

Refer to the Terraform Registory for docs: [`keycloak_openid_client_time_policy`](https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_time_policy).
"""
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


class OpenidClientTimePolicy(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.openidClientTimePolicy.OpenidClientTimePolicy",
):
    """Represents a {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_time_policy keycloak_openid_client_time_policy}."""

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        decision_strategy: builtins.str,
        name: builtins.str,
        realm_id: builtins.str,
        resource_server_id: builtins.str,
        day_month: typing.Optional[builtins.str] = None,
        day_month_end: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        hour: typing.Optional[builtins.str] = None,
        hour_end: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        logic: typing.Optional[builtins.str] = None,
        minute: typing.Optional[builtins.str] = None,
        minute_end: typing.Optional[builtins.str] = None,
        month: typing.Optional[builtins.str] = None,
        month_end: typing.Optional[builtins.str] = None,
        not_before: typing.Optional[builtins.str] = None,
        not_on_or_after: typing.Optional[builtins.str] = None,
        year: typing.Optional[builtins.str] = None,
        year_end: typing.Optional[builtins.str] = None,
        connection: typing.Optional[
            typing.Union[
                typing.Union[
                    _cdktf_9a9027ec.SSHProvisionerConnection,
                    typing.Dict[builtins.str, typing.Any],
                ],
                typing.Union[
                    _cdktf_9a9027ec.WinrmProvisionerConnection,
                    typing.Dict[builtins.str, typing.Any],
                ],
            ]
        ] = None,
        count: typing.Optional[
            typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]
        ] = None,
        depends_on: typing.Optional[
            typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]
        ] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[
            typing.Union[
                _cdktf_9a9027ec.TerraformResourceLifecycle,
                typing.Dict[builtins.str, typing.Any],
            ]
        ] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[
            typing.Sequence[
                typing.Union[
                    typing.Union[
                        _cdktf_9a9027ec.FileProvisioner,
                        typing.Dict[builtins.str, typing.Any],
                    ],
                    typing.Union[
                        _cdktf_9a9027ec.LocalExecProvisioner,
                        typing.Dict[builtins.str, typing.Any],
                    ],
                    typing.Union[
                        _cdktf_9a9027ec.RemoteExecProvisioner,
                        typing.Dict[builtins.str, typing.Any],
                    ],
                ]
            ]
        ] = None,
    ) -> None:
        """Create a new {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_time_policy keycloak_openid_client_time_policy} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param decision_strategy: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_time_policy#decision_strategy OpenidClientTimePolicy#decision_strategy}.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_time_policy#name OpenidClientTimePolicy#name}.
        :param realm_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_time_policy#realm_id OpenidClientTimePolicy#realm_id}.
        :param resource_server_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_time_policy#resource_server_id OpenidClientTimePolicy#resource_server_id}.
        :param day_month: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_time_policy#day_month OpenidClientTimePolicy#day_month}.
        :param day_month_end: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_time_policy#day_month_end OpenidClientTimePolicy#day_month_end}.
        :param description: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_time_policy#description OpenidClientTimePolicy#description}.
        :param hour: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_time_policy#hour OpenidClientTimePolicy#hour}.
        :param hour_end: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_time_policy#hour_end OpenidClientTimePolicy#hour_end}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_time_policy#id OpenidClientTimePolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param logic: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_time_policy#logic OpenidClientTimePolicy#logic}.
        :param minute: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_time_policy#minute OpenidClientTimePolicy#minute}.
        :param minute_end: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_time_policy#minute_end OpenidClientTimePolicy#minute_end}.
        :param month: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_time_policy#month OpenidClientTimePolicy#month}.
        :param month_end: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_time_policy#month_end OpenidClientTimePolicy#month_end}.
        :param not_before: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_time_policy#not_before OpenidClientTimePolicy#not_before}.
        :param not_on_or_after: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_time_policy#not_on_or_after OpenidClientTimePolicy#not_on_or_after}.
        :param year: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_time_policy#year OpenidClientTimePolicy#year}.
        :param year_end: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_time_policy#year_end OpenidClientTimePolicy#year_end}.
        :param connection:
        :param count:
        :param depends_on:
        :param for_each:
        :param lifecycle:
        :param provider:
        :param provisioners:
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__67d80ed87f7d1929e658d14105600342251359732fa8ad0ce3905338c94c8824
            )
            check_type(
                argname="argument scope", value=scope, expected_type=type_hints["scope"]
            )
            check_type(
                argname="argument id_", value=id_, expected_type=type_hints["id_"]
            )
        config = OpenidClientTimePolicyConfig(
            decision_strategy=decision_strategy,
            name=name,
            realm_id=realm_id,
            resource_server_id=resource_server_id,
            day_month=day_month,
            day_month_end=day_month_end,
            description=description,
            hour=hour,
            hour_end=hour_end,
            id=id,
            logic=logic,
            minute=minute,
            minute_end=minute_end,
            month=month,
            month_end=month_end,
            not_before=not_before,
            not_on_or_after=not_on_or_after,
            year=year,
            year_end=year_end,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetDayMonth")
    def reset_day_month(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDayMonth", []))

    @jsii.member(jsii_name="resetDayMonthEnd")
    def reset_day_month_end(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDayMonthEnd", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetHour")
    def reset_hour(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHour", []))

    @jsii.member(jsii_name="resetHourEnd")
    def reset_hour_end(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHourEnd", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLogic")
    def reset_logic(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogic", []))

    @jsii.member(jsii_name="resetMinute")
    def reset_minute(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinute", []))

    @jsii.member(jsii_name="resetMinuteEnd")
    def reset_minute_end(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinuteEnd", []))

    @jsii.member(jsii_name="resetMonth")
    def reset_month(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMonth", []))

    @jsii.member(jsii_name="resetMonthEnd")
    def reset_month_end(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMonthEnd", []))

    @jsii.member(jsii_name="resetNotBefore")
    def reset_not_before(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotBefore", []))

    @jsii.member(jsii_name="resetNotOnOrAfter")
    def reset_not_on_or_after(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotOnOrAfter", []))

    @jsii.member(jsii_name="resetYear")
    def reset_year(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetYear", []))

    @jsii.member(jsii_name="resetYearEnd")
    def reset_year_end(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetYearEnd", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(
            typing.Mapping[builtins.str, typing.Any],
            jsii.invoke(self, "synthesizeAttributes", []),
        )

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="dayMonthEndInput")
    def day_month_end_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "dayMonthEndInput")
        )

    @builtins.property
    @jsii.member(jsii_name="dayMonthInput")
    def day_month_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "dayMonthInput")
        )

    @builtins.property
    @jsii.member(jsii_name="decisionStrategyInput")
    def decision_strategy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "decisionStrategyInput")
        )

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "descriptionInput")
        )

    @builtins.property
    @jsii.member(jsii_name="hourEndInput")
    def hour_end_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "hourEndInput")
        )

    @builtins.property
    @jsii.member(jsii_name="hourInput")
    def hour_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hourInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="logicInput")
    def logic_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logicInput"))

    @builtins.property
    @jsii.member(jsii_name="minuteEndInput")
    def minute_end_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "minuteEndInput")
        )

    @builtins.property
    @jsii.member(jsii_name="minuteInput")
    def minute_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "minuteInput"))

    @builtins.property
    @jsii.member(jsii_name="monthEndInput")
    def month_end_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "monthEndInput")
        )

    @builtins.property
    @jsii.member(jsii_name="monthInput")
    def month_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "monthInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="notBeforeInput")
    def not_before_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "notBeforeInput")
        )

    @builtins.property
    @jsii.member(jsii_name="notOnOrAfterInput")
    def not_on_or_after_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "notOnOrAfterInput")
        )

    @builtins.property
    @jsii.member(jsii_name="realmIdInput")
    def realm_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "realmIdInput")
        )

    @builtins.property
    @jsii.member(jsii_name="resourceServerIdInput")
    def resource_server_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "resourceServerIdInput")
        )

    @builtins.property
    @jsii.member(jsii_name="yearEndInput")
    def year_end_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "yearEndInput")
        )

    @builtins.property
    @jsii.member(jsii_name="yearInput")
    def year_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "yearInput"))

    @builtins.property
    @jsii.member(jsii_name="dayMonth")
    def day_month(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dayMonth"))

    @day_month.setter
    def day_month(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__ede6f2c1c887f7c3c74556c3651d865d01cfaeafe8298637642a333670983dd3
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "dayMonth", value)

    @builtins.property
    @jsii.member(jsii_name="dayMonthEnd")
    def day_month_end(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dayMonthEnd"))

    @day_month_end.setter
    def day_month_end(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__d0f40ddd6f4aca34bd24c85968d9bdd1a5c2c593ff44d56f9511b123ec20af9c
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "dayMonthEnd", value)

    @builtins.property
    @jsii.member(jsii_name="decisionStrategy")
    def decision_strategy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "decisionStrategy"))

    @decision_strategy.setter
    def decision_strategy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__b6b428f60bba90ae845327757c9162ec5a5b4a3355a47fbf5d52beba94564f35
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "decisionStrategy", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__20be8d658b50805cd0bbd09b67116f283ab0b7e613256a3d94f9af42321c9228
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="hour")
    def hour(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hour"))

    @hour.setter
    def hour(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__d80c3f41e557e2923dfe8d5c46759b03335b7dbe615e13c0e9a15cd624dfba7d
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "hour", value)

    @builtins.property
    @jsii.member(jsii_name="hourEnd")
    def hour_end(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hourEnd"))

    @hour_end.setter
    def hour_end(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__6ceba4abd221d8019d2415789b33a9315044bd352a8a2b1e51820d17a9460395
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "hourEnd", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__f98a930c76722d7867ba07ec363761bb0776d4eb62b1328160334ad0726bfaf6
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="logic")
    def logic(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logic"))

    @logic.setter
    def logic(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__ad3c6131ebd8c40d38667a53f961087185ab4c01a9de9ba2de182d973a66d7a7
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "logic", value)

    @builtins.property
    @jsii.member(jsii_name="minute")
    def minute(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "minute"))

    @minute.setter
    def minute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__87f93659f0846c3c5db6d2230777fa0d74d90daade0d4a45a172a125df06c2d1
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "minute", value)

    @builtins.property
    @jsii.member(jsii_name="minuteEnd")
    def minute_end(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "minuteEnd"))

    @minute_end.setter
    def minute_end(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__0851500835aeddc3e7a05f5ec2a56ca118640f960863ad5be5a02eab5ab8272d
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "minuteEnd", value)

    @builtins.property
    @jsii.member(jsii_name="month")
    def month(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "month"))

    @month.setter
    def month(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__8ef41a583e323fbfc9e89c509bebcb6071b95eafa44dabb1121141d8cf7fd38b
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "month", value)

    @builtins.property
    @jsii.member(jsii_name="monthEnd")
    def month_end(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "monthEnd"))

    @month_end.setter
    def month_end(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__1a34840a138981e06435ce6d584f3bd365875821d506f68774f156cbb3848bb4
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "monthEnd", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__a1d816aa20e91b578e159d601427223f67a8dbe9ad78132f000c7dd6f010d590
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="notBefore")
    def not_before(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "notBefore"))

    @not_before.setter
    def not_before(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__f61ca6f8bb5282d967a5141afa4d6f723f6103192b5c15fe65ea08ec90721020
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "notBefore", value)

    @builtins.property
    @jsii.member(jsii_name="notOnOrAfter")
    def not_on_or_after(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "notOnOrAfter"))

    @not_on_or_after.setter
    def not_on_or_after(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__68423b8c42021650da1a8705d7183433ff75fcc8e801d1fbff7774e11187ec4d
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "notOnOrAfter", value)

    @builtins.property
    @jsii.member(jsii_name="realmId")
    def realm_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "realmId"))

    @realm_id.setter
    def realm_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__1981343e88546026c7a87c766623c4de2f152d3da9376731fdf26cfd70ed9438
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "realmId", value)

    @builtins.property
    @jsii.member(jsii_name="resourceServerId")
    def resource_server_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceServerId"))

    @resource_server_id.setter
    def resource_server_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__55f06fbea73a43987fc5440c5209044eec62990987dc03881b743b933be0a319
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "resourceServerId", value)

    @builtins.property
    @jsii.member(jsii_name="year")
    def year(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "year"))

    @year.setter
    def year(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__16013e4a6cb02c1aa937eccedf73b59a87d0e5036eb824977450465edd7e3c37
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "year", value)

    @builtins.property
    @jsii.member(jsii_name="yearEnd")
    def year_end(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "yearEnd"))

    @year_end.setter
    def year_end(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__2b9d8951fce766bda05341c7ef0db399b4a2ae454878c7da9bc0588397208032
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "yearEnd", value)


@jsii.data_type(
    jsii_type="keycloak.openidClientTimePolicy.OpenidClientTimePolicyConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "decision_strategy": "decisionStrategy",
        "name": "name",
        "realm_id": "realmId",
        "resource_server_id": "resourceServerId",
        "day_month": "dayMonth",
        "day_month_end": "dayMonthEnd",
        "description": "description",
        "hour": "hour",
        "hour_end": "hourEnd",
        "id": "id",
        "logic": "logic",
        "minute": "minute",
        "minute_end": "minuteEnd",
        "month": "month",
        "month_end": "monthEnd",
        "not_before": "notBefore",
        "not_on_or_after": "notOnOrAfter",
        "year": "year",
        "year_end": "yearEnd",
    },
)
class OpenidClientTimePolicyConfig(_cdktf_9a9027ec.TerraformMetaArguments):
    def __init__(
        self,
        *,
        connection: typing.Optional[
            typing.Union[
                typing.Union[
                    _cdktf_9a9027ec.SSHProvisionerConnection,
                    typing.Dict[builtins.str, typing.Any],
                ],
                typing.Union[
                    _cdktf_9a9027ec.WinrmProvisionerConnection,
                    typing.Dict[builtins.str, typing.Any],
                ],
            ]
        ] = None,
        count: typing.Optional[
            typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]
        ] = None,
        depends_on: typing.Optional[
            typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]
        ] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[
            typing.Union[
                _cdktf_9a9027ec.TerraformResourceLifecycle,
                typing.Dict[builtins.str, typing.Any],
            ]
        ] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[
            typing.Sequence[
                typing.Union[
                    typing.Union[
                        _cdktf_9a9027ec.FileProvisioner,
                        typing.Dict[builtins.str, typing.Any],
                    ],
                    typing.Union[
                        _cdktf_9a9027ec.LocalExecProvisioner,
                        typing.Dict[builtins.str, typing.Any],
                    ],
                    typing.Union[
                        _cdktf_9a9027ec.RemoteExecProvisioner,
                        typing.Dict[builtins.str, typing.Any],
                    ],
                ]
            ]
        ] = None,
        decision_strategy: builtins.str,
        name: builtins.str,
        realm_id: builtins.str,
        resource_server_id: builtins.str,
        day_month: typing.Optional[builtins.str] = None,
        day_month_end: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        hour: typing.Optional[builtins.str] = None,
        hour_end: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        logic: typing.Optional[builtins.str] = None,
        minute: typing.Optional[builtins.str] = None,
        minute_end: typing.Optional[builtins.str] = None,
        month: typing.Optional[builtins.str] = None,
        month_end: typing.Optional[builtins.str] = None,
        not_before: typing.Optional[builtins.str] = None,
        not_on_or_after: typing.Optional[builtins.str] = None,
        year: typing.Optional[builtins.str] = None,
        year_end: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param connection:
        :param count:
        :param depends_on:
        :param for_each:
        :param lifecycle:
        :param provider:
        :param provisioners:
        :param decision_strategy: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_time_policy#decision_strategy OpenidClientTimePolicy#decision_strategy}.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_time_policy#name OpenidClientTimePolicy#name}.
        :param realm_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_time_policy#realm_id OpenidClientTimePolicy#realm_id}.
        :param resource_server_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_time_policy#resource_server_id OpenidClientTimePolicy#resource_server_id}.
        :param day_month: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_time_policy#day_month OpenidClientTimePolicy#day_month}.
        :param day_month_end: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_time_policy#day_month_end OpenidClientTimePolicy#day_month_end}.
        :param description: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_time_policy#description OpenidClientTimePolicy#description}.
        :param hour: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_time_policy#hour OpenidClientTimePolicy#hour}.
        :param hour_end: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_time_policy#hour_end OpenidClientTimePolicy#hour_end}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_time_policy#id OpenidClientTimePolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param logic: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_time_policy#logic OpenidClientTimePolicy#logic}.
        :param minute: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_time_policy#minute OpenidClientTimePolicy#minute}.
        :param minute_end: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_time_policy#minute_end OpenidClientTimePolicy#minute_end}.
        :param month: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_time_policy#month OpenidClientTimePolicy#month}.
        :param month_end: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_time_policy#month_end OpenidClientTimePolicy#month_end}.
        :param not_before: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_time_policy#not_before OpenidClientTimePolicy#not_before}.
        :param not_on_or_after: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_time_policy#not_on_or_after OpenidClientTimePolicy#not_on_or_after}.
        :param year: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_time_policy#year OpenidClientTimePolicy#year}.
        :param year_end: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_time_policy#year_end OpenidClientTimePolicy#year_end}.
        """
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__1f4b16b5efeb7c9f17fb7eed46062c80ef6576f7b0f0e4328d8c91bc87cdef53
            )
            check_type(
                argname="argument connection",
                value=connection,
                expected_type=type_hints["connection"],
            )
            check_type(
                argname="argument count", value=count, expected_type=type_hints["count"]
            )
            check_type(
                argname="argument depends_on",
                value=depends_on,
                expected_type=type_hints["depends_on"],
            )
            check_type(
                argname="argument for_each",
                value=for_each,
                expected_type=type_hints["for_each"],
            )
            check_type(
                argname="argument lifecycle",
                value=lifecycle,
                expected_type=type_hints["lifecycle"],
            )
            check_type(
                argname="argument provider",
                value=provider,
                expected_type=type_hints["provider"],
            )
            check_type(
                argname="argument provisioners",
                value=provisioners,
                expected_type=type_hints["provisioners"],
            )
            check_type(
                argname="argument decision_strategy",
                value=decision_strategy,
                expected_type=type_hints["decision_strategy"],
            )
            check_type(
                argname="argument name", value=name, expected_type=type_hints["name"]
            )
            check_type(
                argname="argument realm_id",
                value=realm_id,
                expected_type=type_hints["realm_id"],
            )
            check_type(
                argname="argument resource_server_id",
                value=resource_server_id,
                expected_type=type_hints["resource_server_id"],
            )
            check_type(
                argname="argument day_month",
                value=day_month,
                expected_type=type_hints["day_month"],
            )
            check_type(
                argname="argument day_month_end",
                value=day_month_end,
                expected_type=type_hints["day_month_end"],
            )
            check_type(
                argname="argument description",
                value=description,
                expected_type=type_hints["description"],
            )
            check_type(
                argname="argument hour", value=hour, expected_type=type_hints["hour"]
            )
            check_type(
                argname="argument hour_end",
                value=hour_end,
                expected_type=type_hints["hour_end"],
            )
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(
                argname="argument logic", value=logic, expected_type=type_hints["logic"]
            )
            check_type(
                argname="argument minute",
                value=minute,
                expected_type=type_hints["minute"],
            )
            check_type(
                argname="argument minute_end",
                value=minute_end,
                expected_type=type_hints["minute_end"],
            )
            check_type(
                argname="argument month", value=month, expected_type=type_hints["month"]
            )
            check_type(
                argname="argument month_end",
                value=month_end,
                expected_type=type_hints["month_end"],
            )
            check_type(
                argname="argument not_before",
                value=not_before,
                expected_type=type_hints["not_before"],
            )
            check_type(
                argname="argument not_on_or_after",
                value=not_on_or_after,
                expected_type=type_hints["not_on_or_after"],
            )
            check_type(
                argname="argument year", value=year, expected_type=type_hints["year"]
            )
            check_type(
                argname="argument year_end",
                value=year_end,
                expected_type=type_hints["year_end"],
            )
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "decision_strategy": decision_strategy,
            "name": name,
            "realm_id": realm_id,
            "resource_server_id": resource_server_id,
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
        if day_month is not None:
            self._values["day_month"] = day_month
        if day_month_end is not None:
            self._values["day_month_end"] = day_month_end
        if description is not None:
            self._values["description"] = description
        if hour is not None:
            self._values["hour"] = hour
        if hour_end is not None:
            self._values["hour_end"] = hour_end
        if id is not None:
            self._values["id"] = id
        if logic is not None:
            self._values["logic"] = logic
        if minute is not None:
            self._values["minute"] = minute
        if minute_end is not None:
            self._values["minute_end"] = minute_end
        if month is not None:
            self._values["month"] = month
        if month_end is not None:
            self._values["month_end"] = month_end
        if not_before is not None:
            self._values["not_before"] = not_before
        if not_on_or_after is not None:
            self._values["not_on_or_after"] = not_on_or_after
        if year is not None:
            self._values["year"] = year
        if year_end is not None:
            self._values["year_end"] = year_end

    @builtins.property
    def connection(
        self,
    ) -> typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.SSHProvisionerConnection,
            _cdktf_9a9027ec.WinrmProvisionerConnection,
        ]
    ]:
        """
        :stability: experimental
        """
        result = self._values.get("connection")
        return typing.cast(
            typing.Optional[
                typing.Union[
                    _cdktf_9a9027ec.SSHProvisionerConnection,
                    _cdktf_9a9027ec.WinrmProvisionerConnection,
                ]
            ],
            result,
        )

    @builtins.property
    def count(
        self,
    ) -> typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]]:
        """
        :stability: experimental
        """
        result = self._values.get("count")
        return typing.cast(
            typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]],
            result,
        )

    @builtins.property
    def depends_on(
        self,
    ) -> typing.Optional[typing.List[_cdktf_9a9027ec.ITerraformDependable]]:
        """
        :stability: experimental
        """
        result = self._values.get("depends_on")
        return typing.cast(
            typing.Optional[typing.List[_cdktf_9a9027ec.ITerraformDependable]], result
        )

    @builtins.property
    def for_each(self) -> typing.Optional[_cdktf_9a9027ec.ITerraformIterator]:
        """
        :stability: experimental
        """
        result = self._values.get("for_each")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.ITerraformIterator], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[_cdktf_9a9027ec.TerraformResourceLifecycle]:
        """
        :stability: experimental
        """
        result = self._values.get("lifecycle")
        return typing.cast(
            typing.Optional[_cdktf_9a9027ec.TerraformResourceLifecycle], result
        )

    @builtins.property
    def provider(self) -> typing.Optional[_cdktf_9a9027ec.TerraformProvider]:
        """
        :stability: experimental
        """
        result = self._values.get("provider")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.TerraformProvider], result)

    @builtins.property
    def provisioners(
        self,
    ) -> typing.Optional[
        typing.List[
            typing.Union[
                _cdktf_9a9027ec.FileProvisioner,
                _cdktf_9a9027ec.LocalExecProvisioner,
                _cdktf_9a9027ec.RemoteExecProvisioner,
            ]
        ]
    ]:
        """
        :stability: experimental
        """
        result = self._values.get("provisioners")
        return typing.cast(
            typing.Optional[
                typing.List[
                    typing.Union[
                        _cdktf_9a9027ec.FileProvisioner,
                        _cdktf_9a9027ec.LocalExecProvisioner,
                        _cdktf_9a9027ec.RemoteExecProvisioner,
                    ]
                ]
            ],
            result,
        )

    @builtins.property
    def decision_strategy(self) -> builtins.str:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_time_policy#decision_strategy OpenidClientTimePolicy#decision_strategy}."""
        result = self._values.get("decision_strategy")
        assert result is not None, "Required property 'decision_strategy' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_time_policy#name OpenidClientTimePolicy#name}."""
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def realm_id(self) -> builtins.str:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_time_policy#realm_id OpenidClientTimePolicy#realm_id}."""
        result = self._values.get("realm_id")
        assert result is not None, "Required property 'realm_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_server_id(self) -> builtins.str:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_time_policy#resource_server_id OpenidClientTimePolicy#resource_server_id}."""
        result = self._values.get("resource_server_id")
        assert result is not None, "Required property 'resource_server_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def day_month(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_time_policy#day_month OpenidClientTimePolicy#day_month}."""
        result = self._values.get("day_month")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def day_month_end(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_time_policy#day_month_end OpenidClientTimePolicy#day_month_end}."""
        result = self._values.get("day_month_end")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_time_policy#description OpenidClientTimePolicy#description}."""
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def hour(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_time_policy#hour OpenidClientTimePolicy#hour}."""
        result = self._values.get("hour")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def hour_end(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_time_policy#hour_end OpenidClientTimePolicy#hour_end}."""
        result = self._values.get("hour_end")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_time_policy#id OpenidClientTimePolicy#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        """
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def logic(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_time_policy#logic OpenidClientTimePolicy#logic}."""
        result = self._values.get("logic")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def minute(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_time_policy#minute OpenidClientTimePolicy#minute}."""
        result = self._values.get("minute")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def minute_end(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_time_policy#minute_end OpenidClientTimePolicy#minute_end}."""
        result = self._values.get("minute_end")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def month(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_time_policy#month OpenidClientTimePolicy#month}."""
        result = self._values.get("month")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def month_end(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_time_policy#month_end OpenidClientTimePolicy#month_end}."""
        result = self._values.get("month_end")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def not_before(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_time_policy#not_before OpenidClientTimePolicy#not_before}."""
        result = self._values.get("not_before")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def not_on_or_after(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_time_policy#not_on_or_after OpenidClientTimePolicy#not_on_or_after}."""
        result = self._values.get("not_on_or_after")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def year(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_time_policy#year OpenidClientTimePolicy#year}."""
        result = self._values.get("year")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def year_end(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_time_policy#year_end OpenidClientTimePolicy#year_end}."""
        result = self._values.get("year_end")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OpenidClientTimePolicyConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "OpenidClientTimePolicy",
    "OpenidClientTimePolicyConfig",
]

publication.publish()


def _typecheckingstub__67d80ed87f7d1929e658d14105600342251359732fa8ad0ce3905338c94c8824(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    decision_strategy: builtins.str,
    name: builtins.str,
    realm_id: builtins.str,
    resource_server_id: builtins.str,
    day_month: typing.Optional[builtins.str] = None,
    day_month_end: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    hour: typing.Optional[builtins.str] = None,
    hour_end: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    logic: typing.Optional[builtins.str] = None,
    minute: typing.Optional[builtins.str] = None,
    minute_end: typing.Optional[builtins.str] = None,
    month: typing.Optional[builtins.str] = None,
    month_end: typing.Optional[builtins.str] = None,
    not_before: typing.Optional[builtins.str] = None,
    not_on_or_after: typing.Optional[builtins.str] = None,
    year: typing.Optional[builtins.str] = None,
    year_end: typing.Optional[builtins.str] = None,
    connection: typing.Optional[
        typing.Union[
            typing.Union[
                _cdktf_9a9027ec.SSHProvisionerConnection,
                typing.Dict[builtins.str, typing.Any],
            ],
            typing.Union[
                _cdktf_9a9027ec.WinrmProvisionerConnection,
                typing.Dict[builtins.str, typing.Any],
            ],
        ]
    ] = None,
    count: typing.Optional[
        typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]
    ] = None,
    depends_on: typing.Optional[
        typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]
    ] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.TerraformResourceLifecycle,
            typing.Dict[builtins.str, typing.Any],
        ]
    ] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[
        typing.Sequence[
            typing.Union[
                typing.Union[
                    _cdktf_9a9027ec.FileProvisioner,
                    typing.Dict[builtins.str, typing.Any],
                ],
                typing.Union[
                    _cdktf_9a9027ec.LocalExecProvisioner,
                    typing.Dict[builtins.str, typing.Any],
                ],
                typing.Union[
                    _cdktf_9a9027ec.RemoteExecProvisioner,
                    typing.Dict[builtins.str, typing.Any],
                ],
            ]
        ]
    ] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__ede6f2c1c887f7c3c74556c3651d865d01cfaeafe8298637642a333670983dd3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__d0f40ddd6f4aca34bd24c85968d9bdd1a5c2c593ff44d56f9511b123ec20af9c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__b6b428f60bba90ae845327757c9162ec5a5b4a3355a47fbf5d52beba94564f35(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__20be8d658b50805cd0bbd09b67116f283ab0b7e613256a3d94f9af42321c9228(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__d80c3f41e557e2923dfe8d5c46759b03335b7dbe615e13c0e9a15cd624dfba7d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__6ceba4abd221d8019d2415789b33a9315044bd352a8a2b1e51820d17a9460395(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__f98a930c76722d7867ba07ec363761bb0776d4eb62b1328160334ad0726bfaf6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__ad3c6131ebd8c40d38667a53f961087185ab4c01a9de9ba2de182d973a66d7a7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__87f93659f0846c3c5db6d2230777fa0d74d90daade0d4a45a172a125df06c2d1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__0851500835aeddc3e7a05f5ec2a56ca118640f960863ad5be5a02eab5ab8272d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__8ef41a583e323fbfc9e89c509bebcb6071b95eafa44dabb1121141d8cf7fd38b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__1a34840a138981e06435ce6d584f3bd365875821d506f68774f156cbb3848bb4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__a1d816aa20e91b578e159d601427223f67a8dbe9ad78132f000c7dd6f010d590(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__f61ca6f8bb5282d967a5141afa4d6f723f6103192b5c15fe65ea08ec90721020(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__68423b8c42021650da1a8705d7183433ff75fcc8e801d1fbff7774e11187ec4d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__1981343e88546026c7a87c766623c4de2f152d3da9376731fdf26cfd70ed9438(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__55f06fbea73a43987fc5440c5209044eec62990987dc03881b743b933be0a319(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__16013e4a6cb02c1aa937eccedf73b59a87d0e5036eb824977450465edd7e3c37(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__2b9d8951fce766bda05341c7ef0db399b4a2ae454878c7da9bc0588397208032(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__1f4b16b5efeb7c9f17fb7eed46062c80ef6576f7b0f0e4328d8c91bc87cdef53(
    *,
    connection: typing.Optional[
        typing.Union[
            typing.Union[
                _cdktf_9a9027ec.SSHProvisionerConnection,
                typing.Dict[builtins.str, typing.Any],
            ],
            typing.Union[
                _cdktf_9a9027ec.WinrmProvisionerConnection,
                typing.Dict[builtins.str, typing.Any],
            ],
        ]
    ] = None,
    count: typing.Optional[
        typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]
    ] = None,
    depends_on: typing.Optional[
        typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]
    ] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.TerraformResourceLifecycle,
            typing.Dict[builtins.str, typing.Any],
        ]
    ] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[
        typing.Sequence[
            typing.Union[
                typing.Union[
                    _cdktf_9a9027ec.FileProvisioner,
                    typing.Dict[builtins.str, typing.Any],
                ],
                typing.Union[
                    _cdktf_9a9027ec.LocalExecProvisioner,
                    typing.Dict[builtins.str, typing.Any],
                ],
                typing.Union[
                    _cdktf_9a9027ec.RemoteExecProvisioner,
                    typing.Dict[builtins.str, typing.Any],
                ],
            ]
        ]
    ] = None,
    decision_strategy: builtins.str,
    name: builtins.str,
    realm_id: builtins.str,
    resource_server_id: builtins.str,
    day_month: typing.Optional[builtins.str] = None,
    day_month_end: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    hour: typing.Optional[builtins.str] = None,
    hour_end: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    logic: typing.Optional[builtins.str] = None,
    minute: typing.Optional[builtins.str] = None,
    minute_end: typing.Optional[builtins.str] = None,
    month: typing.Optional[builtins.str] = None,
    month_end: typing.Optional[builtins.str] = None,
    not_before: typing.Optional[builtins.str] = None,
    not_on_or_after: typing.Optional[builtins.str] = None,
    year: typing.Optional[builtins.str] = None,
    year_end: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
