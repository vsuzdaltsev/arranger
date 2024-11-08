'''
# `aws_rum_app_monitor`

Refer to the Terraform Registory for docs: [`aws_rum_app_monitor`](https://www.terraform.io/docs/providers/aws/r/rum_app_monitor).
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


class RumAppMonitor(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.rumAppMonitor.RumAppMonitor",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/rum_app_monitor aws_rum_app_monitor}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        domain: builtins.str,
        name: builtins.str,
        app_monitor_configuration: typing.Optional[typing.Union["RumAppMonitorAppMonitorConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        cw_log_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
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
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/rum_app_monitor aws_rum_app_monitor} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param domain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rum_app_monitor#domain RumAppMonitor#domain}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rum_app_monitor#name RumAppMonitor#name}.
        :param app_monitor_configuration: app_monitor_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rum_app_monitor#app_monitor_configuration RumAppMonitor#app_monitor_configuration}
        :param cw_log_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rum_app_monitor#cw_log_enabled RumAppMonitor#cw_log_enabled}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rum_app_monitor#id RumAppMonitor#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rum_app_monitor#tags RumAppMonitor#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rum_app_monitor#tags_all RumAppMonitor#tags_all}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9bd0399301c027b6879287276f7c9df78d60dfc4c1195dd77c0f3f6be9c04c9)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = RumAppMonitorConfig(
            domain=domain,
            name=name,
            app_monitor_configuration=app_monitor_configuration,
            cw_log_enabled=cw_log_enabled,
            id=id,
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

    @jsii.member(jsii_name="putAppMonitorConfiguration")
    def put_app_monitor_configuration(
        self,
        *,
        allow_cookies: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_xray: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        excluded_pages: typing.Optional[typing.Sequence[builtins.str]] = None,
        favorite_pages: typing.Optional[typing.Sequence[builtins.str]] = None,
        guest_role_arn: typing.Optional[builtins.str] = None,
        identity_pool_id: typing.Optional[builtins.str] = None,
        included_pages: typing.Optional[typing.Sequence[builtins.str]] = None,
        session_sample_rate: typing.Optional[jsii.Number] = None,
        telemetries: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param allow_cookies: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rum_app_monitor#allow_cookies RumAppMonitor#allow_cookies}.
        :param enable_xray: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rum_app_monitor#enable_xray RumAppMonitor#enable_xray}.
        :param excluded_pages: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rum_app_monitor#excluded_pages RumAppMonitor#excluded_pages}.
        :param favorite_pages: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rum_app_monitor#favorite_pages RumAppMonitor#favorite_pages}.
        :param guest_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rum_app_monitor#guest_role_arn RumAppMonitor#guest_role_arn}.
        :param identity_pool_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rum_app_monitor#identity_pool_id RumAppMonitor#identity_pool_id}.
        :param included_pages: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rum_app_monitor#included_pages RumAppMonitor#included_pages}.
        :param session_sample_rate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rum_app_monitor#session_sample_rate RumAppMonitor#session_sample_rate}.
        :param telemetries: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rum_app_monitor#telemetries RumAppMonitor#telemetries}.
        '''
        value = RumAppMonitorAppMonitorConfiguration(
            allow_cookies=allow_cookies,
            enable_xray=enable_xray,
            excluded_pages=excluded_pages,
            favorite_pages=favorite_pages,
            guest_role_arn=guest_role_arn,
            identity_pool_id=identity_pool_id,
            included_pages=included_pages,
            session_sample_rate=session_sample_rate,
            telemetries=telemetries,
        )

        return typing.cast(None, jsii.invoke(self, "putAppMonitorConfiguration", [value]))

    @jsii.member(jsii_name="resetAppMonitorConfiguration")
    def reset_app_monitor_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAppMonitorConfiguration", []))

    @jsii.member(jsii_name="resetCwLogEnabled")
    def reset_cw_log_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCwLogEnabled", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

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
    @jsii.member(jsii_name="appMonitorConfiguration")
    def app_monitor_configuration(
        self,
    ) -> "RumAppMonitorAppMonitorConfigurationOutputReference":
        return typing.cast("RumAppMonitorAppMonitorConfigurationOutputReference", jsii.get(self, "appMonitorConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="appMonitorId")
    def app_monitor_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "appMonitorId"))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="cwLogGroup")
    def cw_log_group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cwLogGroup"))

    @builtins.property
    @jsii.member(jsii_name="appMonitorConfigurationInput")
    def app_monitor_configuration_input(
        self,
    ) -> typing.Optional["RumAppMonitorAppMonitorConfiguration"]:
        return typing.cast(typing.Optional["RumAppMonitorAppMonitorConfiguration"], jsii.get(self, "appMonitorConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="cwLogEnabledInput")
    def cw_log_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "cwLogEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="domainInput")
    def domain_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

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
    @jsii.member(jsii_name="cwLogEnabled")
    def cw_log_enabled(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "cwLogEnabled"))

    @cw_log_enabled.setter
    def cw_log_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8fd57647e2261cfa3608d445dfd141ead5c08003fb00b919812d0aa2395c8b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cwLogEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="domain")
    def domain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domain"))

    @domain.setter
    def domain(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e7b3cad1ae8896094e43e8971366a4261bbd840b319b40a2128f6774318caf5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domain", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70bbdfff8c53bf500f905685f78a026f7b21659f30db3a420826a187b599766f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4cb784c1b7f8d495fe2e1610214c0570d8f41b633fbba4cb5c61252f290d1ccf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7e978f77070a63aa86d4c30f3df723fb3cdfaa025309dbb6e1772b8983190b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7af291d33e564cc1f06bc75a14974161e722448a054f56aa4fa5aa6d96da060d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)


@jsii.data_type(
    jsii_type="aws.rumAppMonitor.RumAppMonitorAppMonitorConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "allow_cookies": "allowCookies",
        "enable_xray": "enableXray",
        "excluded_pages": "excludedPages",
        "favorite_pages": "favoritePages",
        "guest_role_arn": "guestRoleArn",
        "identity_pool_id": "identityPoolId",
        "included_pages": "includedPages",
        "session_sample_rate": "sessionSampleRate",
        "telemetries": "telemetries",
    },
)
class RumAppMonitorAppMonitorConfiguration:
    def __init__(
        self,
        *,
        allow_cookies: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_xray: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        excluded_pages: typing.Optional[typing.Sequence[builtins.str]] = None,
        favorite_pages: typing.Optional[typing.Sequence[builtins.str]] = None,
        guest_role_arn: typing.Optional[builtins.str] = None,
        identity_pool_id: typing.Optional[builtins.str] = None,
        included_pages: typing.Optional[typing.Sequence[builtins.str]] = None,
        session_sample_rate: typing.Optional[jsii.Number] = None,
        telemetries: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param allow_cookies: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rum_app_monitor#allow_cookies RumAppMonitor#allow_cookies}.
        :param enable_xray: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rum_app_monitor#enable_xray RumAppMonitor#enable_xray}.
        :param excluded_pages: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rum_app_monitor#excluded_pages RumAppMonitor#excluded_pages}.
        :param favorite_pages: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rum_app_monitor#favorite_pages RumAppMonitor#favorite_pages}.
        :param guest_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rum_app_monitor#guest_role_arn RumAppMonitor#guest_role_arn}.
        :param identity_pool_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rum_app_monitor#identity_pool_id RumAppMonitor#identity_pool_id}.
        :param included_pages: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rum_app_monitor#included_pages RumAppMonitor#included_pages}.
        :param session_sample_rate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rum_app_monitor#session_sample_rate RumAppMonitor#session_sample_rate}.
        :param telemetries: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rum_app_monitor#telemetries RumAppMonitor#telemetries}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d52d9d28616613d0772b94993ad246f1983ac8424baec28f66a099aaf1bf195e)
            check_type(argname="argument allow_cookies", value=allow_cookies, expected_type=type_hints["allow_cookies"])
            check_type(argname="argument enable_xray", value=enable_xray, expected_type=type_hints["enable_xray"])
            check_type(argname="argument excluded_pages", value=excluded_pages, expected_type=type_hints["excluded_pages"])
            check_type(argname="argument favorite_pages", value=favorite_pages, expected_type=type_hints["favorite_pages"])
            check_type(argname="argument guest_role_arn", value=guest_role_arn, expected_type=type_hints["guest_role_arn"])
            check_type(argname="argument identity_pool_id", value=identity_pool_id, expected_type=type_hints["identity_pool_id"])
            check_type(argname="argument included_pages", value=included_pages, expected_type=type_hints["included_pages"])
            check_type(argname="argument session_sample_rate", value=session_sample_rate, expected_type=type_hints["session_sample_rate"])
            check_type(argname="argument telemetries", value=telemetries, expected_type=type_hints["telemetries"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if allow_cookies is not None:
            self._values["allow_cookies"] = allow_cookies
        if enable_xray is not None:
            self._values["enable_xray"] = enable_xray
        if excluded_pages is not None:
            self._values["excluded_pages"] = excluded_pages
        if favorite_pages is not None:
            self._values["favorite_pages"] = favorite_pages
        if guest_role_arn is not None:
            self._values["guest_role_arn"] = guest_role_arn
        if identity_pool_id is not None:
            self._values["identity_pool_id"] = identity_pool_id
        if included_pages is not None:
            self._values["included_pages"] = included_pages
        if session_sample_rate is not None:
            self._values["session_sample_rate"] = session_sample_rate
        if telemetries is not None:
            self._values["telemetries"] = telemetries

    @builtins.property
    def allow_cookies(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rum_app_monitor#allow_cookies RumAppMonitor#allow_cookies}.'''
        result = self._values.get("allow_cookies")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def enable_xray(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rum_app_monitor#enable_xray RumAppMonitor#enable_xray}.'''
        result = self._values.get("enable_xray")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def excluded_pages(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rum_app_monitor#excluded_pages RumAppMonitor#excluded_pages}.'''
        result = self._values.get("excluded_pages")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def favorite_pages(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rum_app_monitor#favorite_pages RumAppMonitor#favorite_pages}.'''
        result = self._values.get("favorite_pages")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def guest_role_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rum_app_monitor#guest_role_arn RumAppMonitor#guest_role_arn}.'''
        result = self._values.get("guest_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def identity_pool_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rum_app_monitor#identity_pool_id RumAppMonitor#identity_pool_id}.'''
        result = self._values.get("identity_pool_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def included_pages(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rum_app_monitor#included_pages RumAppMonitor#included_pages}.'''
        result = self._values.get("included_pages")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def session_sample_rate(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rum_app_monitor#session_sample_rate RumAppMonitor#session_sample_rate}.'''
        result = self._values.get("session_sample_rate")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def telemetries(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rum_app_monitor#telemetries RumAppMonitor#telemetries}.'''
        result = self._values.get("telemetries")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RumAppMonitorAppMonitorConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RumAppMonitorAppMonitorConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.rumAppMonitor.RumAppMonitorAppMonitorConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cfe2eea81c2bd6ee78141b0f98f5cafd27f32701d24998f957b806b9f2597039)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAllowCookies")
    def reset_allow_cookies(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowCookies", []))

    @jsii.member(jsii_name="resetEnableXray")
    def reset_enable_xray(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableXray", []))

    @jsii.member(jsii_name="resetExcludedPages")
    def reset_excluded_pages(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExcludedPages", []))

    @jsii.member(jsii_name="resetFavoritePages")
    def reset_favorite_pages(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFavoritePages", []))

    @jsii.member(jsii_name="resetGuestRoleArn")
    def reset_guest_role_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGuestRoleArn", []))

    @jsii.member(jsii_name="resetIdentityPoolId")
    def reset_identity_pool_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentityPoolId", []))

    @jsii.member(jsii_name="resetIncludedPages")
    def reset_included_pages(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludedPages", []))

    @jsii.member(jsii_name="resetSessionSampleRate")
    def reset_session_sample_rate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSessionSampleRate", []))

    @jsii.member(jsii_name="resetTelemetries")
    def reset_telemetries(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTelemetries", []))

    @builtins.property
    @jsii.member(jsii_name="allowCookiesInput")
    def allow_cookies_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "allowCookiesInput"))

    @builtins.property
    @jsii.member(jsii_name="enableXrayInput")
    def enable_xray_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableXrayInput"))

    @builtins.property
    @jsii.member(jsii_name="excludedPagesInput")
    def excluded_pages_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "excludedPagesInput"))

    @builtins.property
    @jsii.member(jsii_name="favoritePagesInput")
    def favorite_pages_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "favoritePagesInput"))

    @builtins.property
    @jsii.member(jsii_name="guestRoleArnInput")
    def guest_role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "guestRoleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="identityPoolIdInput")
    def identity_pool_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "identityPoolIdInput"))

    @builtins.property
    @jsii.member(jsii_name="includedPagesInput")
    def included_pages_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "includedPagesInput"))

    @builtins.property
    @jsii.member(jsii_name="sessionSampleRateInput")
    def session_sample_rate_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sessionSampleRateInput"))

    @builtins.property
    @jsii.member(jsii_name="telemetriesInput")
    def telemetries_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "telemetriesInput"))

    @builtins.property
    @jsii.member(jsii_name="allowCookies")
    def allow_cookies(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "allowCookies"))

    @allow_cookies.setter
    def allow_cookies(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f030094fd6db1bbf6ee0813a198858e3778a9217909c737d17adc545c82bd94)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowCookies", value)

    @builtins.property
    @jsii.member(jsii_name="enableXray")
    def enable_xray(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enableXray"))

    @enable_xray.setter
    def enable_xray(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62f717bfb98a3ea110f4ed7a7c4de7a20ab7d918ed8dde3a72aec7ccba743556)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableXray", value)

    @builtins.property
    @jsii.member(jsii_name="excludedPages")
    def excluded_pages(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "excludedPages"))

    @excluded_pages.setter
    def excluded_pages(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7c29e3c6bfce098e8825959b3b33513afff6b3472f98e882116d758cf8b989c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "excludedPages", value)

    @builtins.property
    @jsii.member(jsii_name="favoritePages")
    def favorite_pages(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "favoritePages"))

    @favorite_pages.setter
    def favorite_pages(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b687f5868c4e0b0301b2a21d25ec6f23f48d3bc56335127330d8a98bc640332b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "favoritePages", value)

    @builtins.property
    @jsii.member(jsii_name="guestRoleArn")
    def guest_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "guestRoleArn"))

    @guest_role_arn.setter
    def guest_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e2a09af52fb4638e16f03d801759014b17e38b145d04d807053598bdbf4232a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "guestRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="identityPoolId")
    def identity_pool_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "identityPoolId"))

    @identity_pool_id.setter
    def identity_pool_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ca00578b5cb9bc9036d21c969ac3f625dc139462eb3bf0d22e92707b34b3195)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityPoolId", value)

    @builtins.property
    @jsii.member(jsii_name="includedPages")
    def included_pages(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "includedPages"))

    @included_pages.setter
    def included_pages(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aafc3d692cc05d80c52b2b19020c8e60d771e0ece7f78f376ae8bc99d839ff25)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includedPages", value)

    @builtins.property
    @jsii.member(jsii_name="sessionSampleRate")
    def session_sample_rate(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "sessionSampleRate"))

    @session_sample_rate.setter
    def session_sample_rate(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d2ad719d7447a24cf640743ffcd41a3952bad0102bfe4149fe3fabdd0be4d62)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sessionSampleRate", value)

    @builtins.property
    @jsii.member(jsii_name="telemetries")
    def telemetries(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "telemetries"))

    @telemetries.setter
    def telemetries(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2cc99054c2a4f296ba6a6d69de1fa6eda7cc69ecf8fdd78e272232b3ce268414)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "telemetries", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[RumAppMonitorAppMonitorConfiguration]:
        return typing.cast(typing.Optional[RumAppMonitorAppMonitorConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[RumAppMonitorAppMonitorConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4922362c498f23c57e6237a7a50fc268674ff61712a46f530ee646277d9a0dff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.rumAppMonitor.RumAppMonitorConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "domain": "domain",
        "name": "name",
        "app_monitor_configuration": "appMonitorConfiguration",
        "cw_log_enabled": "cwLogEnabled",
        "id": "id",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class RumAppMonitorConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        domain: builtins.str,
        name: builtins.str,
        app_monitor_configuration: typing.Optional[typing.Union[RumAppMonitorAppMonitorConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
        cw_log_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
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
        :param domain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rum_app_monitor#domain RumAppMonitor#domain}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rum_app_monitor#name RumAppMonitor#name}.
        :param app_monitor_configuration: app_monitor_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rum_app_monitor#app_monitor_configuration RumAppMonitor#app_monitor_configuration}
        :param cw_log_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rum_app_monitor#cw_log_enabled RumAppMonitor#cw_log_enabled}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rum_app_monitor#id RumAppMonitor#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rum_app_monitor#tags RumAppMonitor#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rum_app_monitor#tags_all RumAppMonitor#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(app_monitor_configuration, dict):
            app_monitor_configuration = RumAppMonitorAppMonitorConfiguration(**app_monitor_configuration)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b6a217bfa5e42ee4760a5cc60eba6170dfa576a2e5d9b225e08c5d6cfedd893e)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument domain", value=domain, expected_type=type_hints["domain"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument app_monitor_configuration", value=app_monitor_configuration, expected_type=type_hints["app_monitor_configuration"])
            check_type(argname="argument cw_log_enabled", value=cw_log_enabled, expected_type=type_hints["cw_log_enabled"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain": domain,
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
        if app_monitor_configuration is not None:
            self._values["app_monitor_configuration"] = app_monitor_configuration
        if cw_log_enabled is not None:
            self._values["cw_log_enabled"] = cw_log_enabled
        if id is not None:
            self._values["id"] = id
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
    def domain(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rum_app_monitor#domain RumAppMonitor#domain}.'''
        result = self._values.get("domain")
        assert result is not None, "Required property 'domain' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rum_app_monitor#name RumAppMonitor#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def app_monitor_configuration(
        self,
    ) -> typing.Optional[RumAppMonitorAppMonitorConfiguration]:
        '''app_monitor_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rum_app_monitor#app_monitor_configuration RumAppMonitor#app_monitor_configuration}
        '''
        result = self._values.get("app_monitor_configuration")
        return typing.cast(typing.Optional[RumAppMonitorAppMonitorConfiguration], result)

    @builtins.property
    def cw_log_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rum_app_monitor#cw_log_enabled RumAppMonitor#cw_log_enabled}.'''
        result = self._values.get("cw_log_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rum_app_monitor#id RumAppMonitor#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rum_app_monitor#tags RumAppMonitor#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rum_app_monitor#tags_all RumAppMonitor#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RumAppMonitorConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "RumAppMonitor",
    "RumAppMonitorAppMonitorConfiguration",
    "RumAppMonitorAppMonitorConfigurationOutputReference",
    "RumAppMonitorConfig",
]

publication.publish()

def _typecheckingstub__a9bd0399301c027b6879287276f7c9df78d60dfc4c1195dd77c0f3f6be9c04c9(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    domain: builtins.str,
    name: builtins.str,
    app_monitor_configuration: typing.Optional[typing.Union[RumAppMonitorAppMonitorConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    cw_log_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__f8fd57647e2261cfa3608d445dfd141ead5c08003fb00b919812d0aa2395c8b6(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e7b3cad1ae8896094e43e8971366a4261bbd840b319b40a2128f6774318caf5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70bbdfff8c53bf500f905685f78a026f7b21659f30db3a420826a187b599766f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4cb784c1b7f8d495fe2e1610214c0570d8f41b633fbba4cb5c61252f290d1ccf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7e978f77070a63aa86d4c30f3df723fb3cdfaa025309dbb6e1772b8983190b6(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7af291d33e564cc1f06bc75a14974161e722448a054f56aa4fa5aa6d96da060d(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d52d9d28616613d0772b94993ad246f1983ac8424baec28f66a099aaf1bf195e(
    *,
    allow_cookies: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    enable_xray: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    excluded_pages: typing.Optional[typing.Sequence[builtins.str]] = None,
    favorite_pages: typing.Optional[typing.Sequence[builtins.str]] = None,
    guest_role_arn: typing.Optional[builtins.str] = None,
    identity_pool_id: typing.Optional[builtins.str] = None,
    included_pages: typing.Optional[typing.Sequence[builtins.str]] = None,
    session_sample_rate: typing.Optional[jsii.Number] = None,
    telemetries: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfe2eea81c2bd6ee78141b0f98f5cafd27f32701d24998f957b806b9f2597039(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f030094fd6db1bbf6ee0813a198858e3778a9217909c737d17adc545c82bd94(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62f717bfb98a3ea110f4ed7a7c4de7a20ab7d918ed8dde3a72aec7ccba743556(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7c29e3c6bfce098e8825959b3b33513afff6b3472f98e882116d758cf8b989c(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b687f5868c4e0b0301b2a21d25ec6f23f48d3bc56335127330d8a98bc640332b(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e2a09af52fb4638e16f03d801759014b17e38b145d04d807053598bdbf4232a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ca00578b5cb9bc9036d21c969ac3f625dc139462eb3bf0d22e92707b34b3195(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aafc3d692cc05d80c52b2b19020c8e60d771e0ece7f78f376ae8bc99d839ff25(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d2ad719d7447a24cf640743ffcd41a3952bad0102bfe4149fe3fabdd0be4d62(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2cc99054c2a4f296ba6a6d69de1fa6eda7cc69ecf8fdd78e272232b3ce268414(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4922362c498f23c57e6237a7a50fc268674ff61712a46f530ee646277d9a0dff(
    value: typing.Optional[RumAppMonitorAppMonitorConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6a217bfa5e42ee4760a5cc60eba6170dfa576a2e5d9b225e08c5d6cfedd893e(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    domain: builtins.str,
    name: builtins.str,
    app_monitor_configuration: typing.Optional[typing.Union[RumAppMonitorAppMonitorConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    cw_log_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass
