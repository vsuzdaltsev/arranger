'''
# `aws_db_proxy_default_target_group`

Refer to the Terraform Registory for docs: [`aws_db_proxy_default_target_group`](https://www.terraform.io/docs/providers/aws/r/db_proxy_default_target_group).
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


class DbProxyDefaultTargetGroup(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dbProxyDefaultTargetGroup.DbProxyDefaultTargetGroup",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/db_proxy_default_target_group aws_db_proxy_default_target_group}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        db_proxy_name: builtins.str,
        connection_pool_config: typing.Optional[typing.Union["DbProxyDefaultTargetGroupConnectionPoolConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["DbProxyDefaultTargetGroupTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/db_proxy_default_target_group aws_db_proxy_default_target_group} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param db_proxy_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_proxy_default_target_group#db_proxy_name DbProxyDefaultTargetGroup#db_proxy_name}.
        :param connection_pool_config: connection_pool_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_proxy_default_target_group#connection_pool_config DbProxyDefaultTargetGroup#connection_pool_config}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_proxy_default_target_group#id DbProxyDefaultTargetGroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_proxy_default_target_group#timeouts DbProxyDefaultTargetGroup#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18ede948b8c16d27a8f8a7a2ab44a59dbecd34f51b90fdfedc230ce57fc22728)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DbProxyDefaultTargetGroupConfig(
            db_proxy_name=db_proxy_name,
            connection_pool_config=connection_pool_config,
            id=id,
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

    @jsii.member(jsii_name="putConnectionPoolConfig")
    def put_connection_pool_config(
        self,
        *,
        connection_borrow_timeout: typing.Optional[jsii.Number] = None,
        init_query: typing.Optional[builtins.str] = None,
        max_connections_percent: typing.Optional[jsii.Number] = None,
        max_idle_connections_percent: typing.Optional[jsii.Number] = None,
        session_pinning_filters: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param connection_borrow_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_proxy_default_target_group#connection_borrow_timeout DbProxyDefaultTargetGroup#connection_borrow_timeout}.
        :param init_query: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_proxy_default_target_group#init_query DbProxyDefaultTargetGroup#init_query}.
        :param max_connections_percent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_proxy_default_target_group#max_connections_percent DbProxyDefaultTargetGroup#max_connections_percent}.
        :param max_idle_connections_percent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_proxy_default_target_group#max_idle_connections_percent DbProxyDefaultTargetGroup#max_idle_connections_percent}.
        :param session_pinning_filters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_proxy_default_target_group#session_pinning_filters DbProxyDefaultTargetGroup#session_pinning_filters}.
        '''
        value = DbProxyDefaultTargetGroupConnectionPoolConfig(
            connection_borrow_timeout=connection_borrow_timeout,
            init_query=init_query,
            max_connections_percent=max_connections_percent,
            max_idle_connections_percent=max_idle_connections_percent,
            session_pinning_filters=session_pinning_filters,
        )

        return typing.cast(None, jsii.invoke(self, "putConnectionPoolConfig", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_proxy_default_target_group#create DbProxyDefaultTargetGroup#create}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_proxy_default_target_group#update DbProxyDefaultTargetGroup#update}.
        '''
        value = DbProxyDefaultTargetGroupTimeouts(create=create, update=update)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetConnectionPoolConfig")
    def reset_connection_pool_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectionPoolConfig", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

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
    @jsii.member(jsii_name="connectionPoolConfig")
    def connection_pool_config(
        self,
    ) -> "DbProxyDefaultTargetGroupConnectionPoolConfigOutputReference":
        return typing.cast("DbProxyDefaultTargetGroupConnectionPoolConfigOutputReference", jsii.get(self, "connectionPoolConfig"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "DbProxyDefaultTargetGroupTimeoutsOutputReference":
        return typing.cast("DbProxyDefaultTargetGroupTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="connectionPoolConfigInput")
    def connection_pool_config_input(
        self,
    ) -> typing.Optional["DbProxyDefaultTargetGroupConnectionPoolConfig"]:
        return typing.cast(typing.Optional["DbProxyDefaultTargetGroupConnectionPoolConfig"], jsii.get(self, "connectionPoolConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="dbProxyNameInput")
    def db_proxy_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dbProxyNameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["DbProxyDefaultTargetGroupTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["DbProxyDefaultTargetGroupTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="dbProxyName")
    def db_proxy_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dbProxyName"))

    @db_proxy_name.setter
    def db_proxy_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef7a320eb570922f4aa39ef684b297f1012454e53761536275eb8abdd25293dc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dbProxyName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78dcc817393643532676d2030b61177b06bf3adaf362508d16f4d0f0f8c71a21)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)


@jsii.data_type(
    jsii_type="aws.dbProxyDefaultTargetGroup.DbProxyDefaultTargetGroupConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "db_proxy_name": "dbProxyName",
        "connection_pool_config": "connectionPoolConfig",
        "id": "id",
        "timeouts": "timeouts",
    },
)
class DbProxyDefaultTargetGroupConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        db_proxy_name: builtins.str,
        connection_pool_config: typing.Optional[typing.Union["DbProxyDefaultTargetGroupConnectionPoolConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["DbProxyDefaultTargetGroupTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param db_proxy_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_proxy_default_target_group#db_proxy_name DbProxyDefaultTargetGroup#db_proxy_name}.
        :param connection_pool_config: connection_pool_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_proxy_default_target_group#connection_pool_config DbProxyDefaultTargetGroup#connection_pool_config}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_proxy_default_target_group#id DbProxyDefaultTargetGroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_proxy_default_target_group#timeouts DbProxyDefaultTargetGroup#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(connection_pool_config, dict):
            connection_pool_config = DbProxyDefaultTargetGroupConnectionPoolConfig(**connection_pool_config)
        if isinstance(timeouts, dict):
            timeouts = DbProxyDefaultTargetGroupTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a149fe9ad8901184203f5548b79132bbb64f7b3f40560c7c0fac683a808b0a0b)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument db_proxy_name", value=db_proxy_name, expected_type=type_hints["db_proxy_name"])
            check_type(argname="argument connection_pool_config", value=connection_pool_config, expected_type=type_hints["connection_pool_config"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "db_proxy_name": db_proxy_name,
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
        if connection_pool_config is not None:
            self._values["connection_pool_config"] = connection_pool_config
        if id is not None:
            self._values["id"] = id
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
    def db_proxy_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_proxy_default_target_group#db_proxy_name DbProxyDefaultTargetGroup#db_proxy_name}.'''
        result = self._values.get("db_proxy_name")
        assert result is not None, "Required property 'db_proxy_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def connection_pool_config(
        self,
    ) -> typing.Optional["DbProxyDefaultTargetGroupConnectionPoolConfig"]:
        '''connection_pool_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_proxy_default_target_group#connection_pool_config DbProxyDefaultTargetGroup#connection_pool_config}
        '''
        result = self._values.get("connection_pool_config")
        return typing.cast(typing.Optional["DbProxyDefaultTargetGroupConnectionPoolConfig"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_proxy_default_target_group#id DbProxyDefaultTargetGroup#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["DbProxyDefaultTargetGroupTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_proxy_default_target_group#timeouts DbProxyDefaultTargetGroup#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["DbProxyDefaultTargetGroupTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DbProxyDefaultTargetGroupConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.dbProxyDefaultTargetGroup.DbProxyDefaultTargetGroupConnectionPoolConfig",
    jsii_struct_bases=[],
    name_mapping={
        "connection_borrow_timeout": "connectionBorrowTimeout",
        "init_query": "initQuery",
        "max_connections_percent": "maxConnectionsPercent",
        "max_idle_connections_percent": "maxIdleConnectionsPercent",
        "session_pinning_filters": "sessionPinningFilters",
    },
)
class DbProxyDefaultTargetGroupConnectionPoolConfig:
    def __init__(
        self,
        *,
        connection_borrow_timeout: typing.Optional[jsii.Number] = None,
        init_query: typing.Optional[builtins.str] = None,
        max_connections_percent: typing.Optional[jsii.Number] = None,
        max_idle_connections_percent: typing.Optional[jsii.Number] = None,
        session_pinning_filters: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param connection_borrow_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_proxy_default_target_group#connection_borrow_timeout DbProxyDefaultTargetGroup#connection_borrow_timeout}.
        :param init_query: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_proxy_default_target_group#init_query DbProxyDefaultTargetGroup#init_query}.
        :param max_connections_percent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_proxy_default_target_group#max_connections_percent DbProxyDefaultTargetGroup#max_connections_percent}.
        :param max_idle_connections_percent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_proxy_default_target_group#max_idle_connections_percent DbProxyDefaultTargetGroup#max_idle_connections_percent}.
        :param session_pinning_filters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_proxy_default_target_group#session_pinning_filters DbProxyDefaultTargetGroup#session_pinning_filters}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db03f2d1dc8aca5bdd73d0f7fc1c07a068110e08633fa8fddd9686582eec6066)
            check_type(argname="argument connection_borrow_timeout", value=connection_borrow_timeout, expected_type=type_hints["connection_borrow_timeout"])
            check_type(argname="argument init_query", value=init_query, expected_type=type_hints["init_query"])
            check_type(argname="argument max_connections_percent", value=max_connections_percent, expected_type=type_hints["max_connections_percent"])
            check_type(argname="argument max_idle_connections_percent", value=max_idle_connections_percent, expected_type=type_hints["max_idle_connections_percent"])
            check_type(argname="argument session_pinning_filters", value=session_pinning_filters, expected_type=type_hints["session_pinning_filters"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if connection_borrow_timeout is not None:
            self._values["connection_borrow_timeout"] = connection_borrow_timeout
        if init_query is not None:
            self._values["init_query"] = init_query
        if max_connections_percent is not None:
            self._values["max_connections_percent"] = max_connections_percent
        if max_idle_connections_percent is not None:
            self._values["max_idle_connections_percent"] = max_idle_connections_percent
        if session_pinning_filters is not None:
            self._values["session_pinning_filters"] = session_pinning_filters

    @builtins.property
    def connection_borrow_timeout(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_proxy_default_target_group#connection_borrow_timeout DbProxyDefaultTargetGroup#connection_borrow_timeout}.'''
        result = self._values.get("connection_borrow_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def init_query(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_proxy_default_target_group#init_query DbProxyDefaultTargetGroup#init_query}.'''
        result = self._values.get("init_query")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_connections_percent(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_proxy_default_target_group#max_connections_percent DbProxyDefaultTargetGroup#max_connections_percent}.'''
        result = self._values.get("max_connections_percent")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_idle_connections_percent(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_proxy_default_target_group#max_idle_connections_percent DbProxyDefaultTargetGroup#max_idle_connections_percent}.'''
        result = self._values.get("max_idle_connections_percent")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def session_pinning_filters(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_proxy_default_target_group#session_pinning_filters DbProxyDefaultTargetGroup#session_pinning_filters}.'''
        result = self._values.get("session_pinning_filters")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DbProxyDefaultTargetGroupConnectionPoolConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DbProxyDefaultTargetGroupConnectionPoolConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dbProxyDefaultTargetGroup.DbProxyDefaultTargetGroupConnectionPoolConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__aa7aa0dfaa73e5766ef5e4b929edcca8205b840fddc8c1c73a683eb68772e4bd)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetConnectionBorrowTimeout")
    def reset_connection_borrow_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectionBorrowTimeout", []))

    @jsii.member(jsii_name="resetInitQuery")
    def reset_init_query(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInitQuery", []))

    @jsii.member(jsii_name="resetMaxConnectionsPercent")
    def reset_max_connections_percent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxConnectionsPercent", []))

    @jsii.member(jsii_name="resetMaxIdleConnectionsPercent")
    def reset_max_idle_connections_percent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxIdleConnectionsPercent", []))

    @jsii.member(jsii_name="resetSessionPinningFilters")
    def reset_session_pinning_filters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSessionPinningFilters", []))

    @builtins.property
    @jsii.member(jsii_name="connectionBorrowTimeoutInput")
    def connection_borrow_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "connectionBorrowTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="initQueryInput")
    def init_query_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "initQueryInput"))

    @builtins.property
    @jsii.member(jsii_name="maxConnectionsPercentInput")
    def max_connections_percent_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxConnectionsPercentInput"))

    @builtins.property
    @jsii.member(jsii_name="maxIdleConnectionsPercentInput")
    def max_idle_connections_percent_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxIdleConnectionsPercentInput"))

    @builtins.property
    @jsii.member(jsii_name="sessionPinningFiltersInput")
    def session_pinning_filters_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sessionPinningFiltersInput"))

    @builtins.property
    @jsii.member(jsii_name="connectionBorrowTimeout")
    def connection_borrow_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "connectionBorrowTimeout"))

    @connection_borrow_timeout.setter
    def connection_borrow_timeout(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80d743d0801bfbe6be12dcb254b426f80829d4c825879d598fafcb72f49cffd4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionBorrowTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="initQuery")
    def init_query(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "initQuery"))

    @init_query.setter
    def init_query(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__16d0821cbab62e7ee675b7ce28d456ee86f449db5e8433b17eb983e8c77d0489)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "initQuery", value)

    @builtins.property
    @jsii.member(jsii_name="maxConnectionsPercent")
    def max_connections_percent(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxConnectionsPercent"))

    @max_connections_percent.setter
    def max_connections_percent(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e0077c03f08484e24a101c6454a5b5027d6b2eee170f24f9fb22e2f53aee4819)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxConnectionsPercent", value)

    @builtins.property
    @jsii.member(jsii_name="maxIdleConnectionsPercent")
    def max_idle_connections_percent(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxIdleConnectionsPercent"))

    @max_idle_connections_percent.setter
    def max_idle_connections_percent(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74fa0bd0067c4ccf07531543e95b6115369480d279048fc27bf7df26aa8dfd7b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxIdleConnectionsPercent", value)

    @builtins.property
    @jsii.member(jsii_name="sessionPinningFilters")
    def session_pinning_filters(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sessionPinningFilters"))

    @session_pinning_filters.setter
    def session_pinning_filters(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bbe9d0ab7839e598c5e6e75f13819204440e391350e2a1490bb5f6a085e7270b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sessionPinningFilters", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DbProxyDefaultTargetGroupConnectionPoolConfig]:
        return typing.cast(typing.Optional[DbProxyDefaultTargetGroupConnectionPoolConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DbProxyDefaultTargetGroupConnectionPoolConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1589ae4567ae7a5f004e16df8b9ce04427844ba40d6cc4fb17e6cf461f9a4327)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.dbProxyDefaultTargetGroup.DbProxyDefaultTargetGroupTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "update": "update"},
)
class DbProxyDefaultTargetGroupTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_proxy_default_target_group#create DbProxyDefaultTargetGroup#create}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_proxy_default_target_group#update DbProxyDefaultTargetGroup#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d5f8ead336e7c5a23cea5e5a51f9a3f5102dea55b300befb89ac4670f9d75e3)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_proxy_default_target_group#create DbProxyDefaultTargetGroup#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_proxy_default_target_group#update DbProxyDefaultTargetGroup#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DbProxyDefaultTargetGroupTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DbProxyDefaultTargetGroupTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dbProxyDefaultTargetGroup.DbProxyDefaultTargetGroupTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__31d0612bd5f2902157ab266d310b3275b259f6db04ba97dd41d95356122c4f6a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetUpdate")
    def reset_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdate", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__b2dd6affeff4c5568da710887e338351709487342afbf6b918f6b97b9b538aed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd1dbd03c36936b76c232017407b0fbba173228ee8ed158434c10530e3523b99)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DbProxyDefaultTargetGroupTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DbProxyDefaultTargetGroupTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DbProxyDefaultTargetGroupTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4149533c4e479deac83c01a9a9f408310e5112041567e638ca13d39a6a8a6a82)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DbProxyDefaultTargetGroup",
    "DbProxyDefaultTargetGroupConfig",
    "DbProxyDefaultTargetGroupConnectionPoolConfig",
    "DbProxyDefaultTargetGroupConnectionPoolConfigOutputReference",
    "DbProxyDefaultTargetGroupTimeouts",
    "DbProxyDefaultTargetGroupTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__18ede948b8c16d27a8f8a7a2ab44a59dbecd34f51b90fdfedc230ce57fc22728(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    db_proxy_name: builtins.str,
    connection_pool_config: typing.Optional[typing.Union[DbProxyDefaultTargetGroupConnectionPoolConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[DbProxyDefaultTargetGroupTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__ef7a320eb570922f4aa39ef684b297f1012454e53761536275eb8abdd25293dc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78dcc817393643532676d2030b61177b06bf3adaf362508d16f4d0f0f8c71a21(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a149fe9ad8901184203f5548b79132bbb64f7b3f40560c7c0fac683a808b0a0b(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    db_proxy_name: builtins.str,
    connection_pool_config: typing.Optional[typing.Union[DbProxyDefaultTargetGroupConnectionPoolConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[DbProxyDefaultTargetGroupTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db03f2d1dc8aca5bdd73d0f7fc1c07a068110e08633fa8fddd9686582eec6066(
    *,
    connection_borrow_timeout: typing.Optional[jsii.Number] = None,
    init_query: typing.Optional[builtins.str] = None,
    max_connections_percent: typing.Optional[jsii.Number] = None,
    max_idle_connections_percent: typing.Optional[jsii.Number] = None,
    session_pinning_filters: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa7aa0dfaa73e5766ef5e4b929edcca8205b840fddc8c1c73a683eb68772e4bd(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80d743d0801bfbe6be12dcb254b426f80829d4c825879d598fafcb72f49cffd4(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16d0821cbab62e7ee675b7ce28d456ee86f449db5e8433b17eb983e8c77d0489(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0077c03f08484e24a101c6454a5b5027d6b2eee170f24f9fb22e2f53aee4819(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74fa0bd0067c4ccf07531543e95b6115369480d279048fc27bf7df26aa8dfd7b(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bbe9d0ab7839e598c5e6e75f13819204440e391350e2a1490bb5f6a085e7270b(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1589ae4567ae7a5f004e16df8b9ce04427844ba40d6cc4fb17e6cf461f9a4327(
    value: typing.Optional[DbProxyDefaultTargetGroupConnectionPoolConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d5f8ead336e7c5a23cea5e5a51f9a3f5102dea55b300befb89ac4670f9d75e3(
    *,
    create: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31d0612bd5f2902157ab266d310b3275b259f6db04ba97dd41d95356122c4f6a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2dd6affeff4c5568da710887e338351709487342afbf6b918f6b97b9b538aed(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd1dbd03c36936b76c232017407b0fbba173228ee8ed158434c10530e3523b99(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4149533c4e479deac83c01a9a9f408310e5112041567e638ca13d39a6a8a6a82(
    value: typing.Optional[typing.Union[DbProxyDefaultTargetGroupTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
