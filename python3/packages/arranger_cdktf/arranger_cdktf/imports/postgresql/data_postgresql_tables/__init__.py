'''
# `data_postgresql_tables`

Refer to the Terraform Registory for docs: [`data_postgresql_tables`](https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs/data-sources/tables).
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


class DataPostgresqlTables(
    _cdktf_9a9027ec.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="postgresql.dataPostgresqlTables.DataPostgresqlTables",
):
    '''Represents a {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs/data-sources/tables postgresql_tables}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        database: builtins.str,
        id: typing.Optional[builtins.str] = None,
        like_all_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
        like_any_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
        not_like_all_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
        regex_pattern: typing.Optional[builtins.str] = None,
        schemas: typing.Optional[typing.Sequence[builtins.str]] = None,
        table_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs/data-sources/tables postgresql_tables} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param database: The PostgreSQL database which will be queried for table names. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs/data-sources/tables#database DataPostgresqlTables#database}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs/data-sources/tables#id DataPostgresqlTables#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param like_all_patterns: Expression(s) which will be pattern matched against table names in the query using the PostgreSQL LIKE ALL operator. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs/data-sources/tables#like_all_patterns DataPostgresqlTables#like_all_patterns}
        :param like_any_patterns: Expression(s) which will be pattern matched against table names in the query using the PostgreSQL LIKE ANY operator. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs/data-sources/tables#like_any_patterns DataPostgresqlTables#like_any_patterns}
        :param not_like_all_patterns: Expression(s) which will be pattern matched against table names in the query using the PostgreSQL NOT LIKE ALL operator. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs/data-sources/tables#not_like_all_patterns DataPostgresqlTables#not_like_all_patterns}
        :param regex_pattern: Expression which will be pattern matched against table names in the query using the PostgreSQL ~ (regular expression match) operator. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs/data-sources/tables#regex_pattern DataPostgresqlTables#regex_pattern}
        :param schemas: The PostgreSQL schema(s) which will be queried for table names. Queries all schemas in the database by default. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs/data-sources/tables#schemas DataPostgresqlTables#schemas}
        :param table_types: The PostgreSQL table types which will be queried for table names. Includes all table types by default. Use 'BASE TABLE' for normal tables only Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs/data-sources/tables#table_types DataPostgresqlTables#table_types}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58ce0f8e908c8f431400532ef1db229c8731ee606ea42317bbb83818d18b4c08)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataPostgresqlTablesConfig(
            database=database,
            id=id,
            like_all_patterns=like_all_patterns,
            like_any_patterns=like_any_patterns,
            not_like_all_patterns=not_like_all_patterns,
            regex_pattern=regex_pattern,
            schemas=schemas,
            table_types=table_types,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLikeAllPatterns")
    def reset_like_all_patterns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLikeAllPatterns", []))

    @jsii.member(jsii_name="resetLikeAnyPatterns")
    def reset_like_any_patterns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLikeAnyPatterns", []))

    @jsii.member(jsii_name="resetNotLikeAllPatterns")
    def reset_not_like_all_patterns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotLikeAllPatterns", []))

    @jsii.member(jsii_name="resetRegexPattern")
    def reset_regex_pattern(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegexPattern", []))

    @jsii.member(jsii_name="resetSchemas")
    def reset_schemas(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSchemas", []))

    @jsii.member(jsii_name="resetTableTypes")
    def reset_table_types(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTableTypes", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="tables")
    def tables(self) -> "DataPostgresqlTablesTablesList":
        return typing.cast("DataPostgresqlTablesTablesList", jsii.get(self, "tables"))

    @builtins.property
    @jsii.member(jsii_name="databaseInput")
    def database_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="likeAllPatternsInput")
    def like_all_patterns_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "likeAllPatternsInput"))

    @builtins.property
    @jsii.member(jsii_name="likeAnyPatternsInput")
    def like_any_patterns_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "likeAnyPatternsInput"))

    @builtins.property
    @jsii.member(jsii_name="notLikeAllPatternsInput")
    def not_like_all_patterns_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "notLikeAllPatternsInput"))

    @builtins.property
    @jsii.member(jsii_name="regexPatternInput")
    def regex_pattern_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regexPatternInput"))

    @builtins.property
    @jsii.member(jsii_name="schemasInput")
    def schemas_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "schemasInput"))

    @builtins.property
    @jsii.member(jsii_name="tableTypesInput")
    def table_types_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tableTypesInput"))

    @builtins.property
    @jsii.member(jsii_name="database")
    def database(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "database"))

    @database.setter
    def database(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be762dc102c4d881d4e919e027e8f0c6163b8920843edeab44ce103aa0d3d9e1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "database", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43e77da7fc18e3a4a6a71ffd70874e74b8b3d1790bb4abdc7215d0ccc41b5f6e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="likeAllPatterns")
    def like_all_patterns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "likeAllPatterns"))

    @like_all_patterns.setter
    def like_all_patterns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5bbd1b0121bf970ef1aa698671699060780c72f121036d685506fc4b12c86334)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "likeAllPatterns", value)

    @builtins.property
    @jsii.member(jsii_name="likeAnyPatterns")
    def like_any_patterns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "likeAnyPatterns"))

    @like_any_patterns.setter
    def like_any_patterns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1516a90558703ff58c653a4d2e27d7e13296fe1118df00f4d462a59108ac8e8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "likeAnyPatterns", value)

    @builtins.property
    @jsii.member(jsii_name="notLikeAllPatterns")
    def not_like_all_patterns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "notLikeAllPatterns"))

    @not_like_all_patterns.setter
    def not_like_all_patterns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7f9883bd1e5b46ca3faff274792aecd3254ec03befbb00b219cdc9e92a4e3b9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notLikeAllPatterns", value)

    @builtins.property
    @jsii.member(jsii_name="regexPattern")
    def regex_pattern(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "regexPattern"))

    @regex_pattern.setter
    def regex_pattern(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc5242c8457f17a45ae97c921f084d39efd5a9779e830f3dad2ba9f3f0a482e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "regexPattern", value)

    @builtins.property
    @jsii.member(jsii_name="schemas")
    def schemas(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "schemas"))

    @schemas.setter
    def schemas(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14a01155ad34167f0e43820324dca3d3b3f07d70ab0c1d465e84c72fd40c08ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schemas", value)

    @builtins.property
    @jsii.member(jsii_name="tableTypes")
    def table_types(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tableTypes"))

    @table_types.setter
    def table_types(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91220b407319c58b3d17c88d57dcc2d432c96d1b4833e854a5947376cf924afc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tableTypes", value)


@jsii.data_type(
    jsii_type="postgresql.dataPostgresqlTables.DataPostgresqlTablesConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "database": "database",
        "id": "id",
        "like_all_patterns": "likeAllPatterns",
        "like_any_patterns": "likeAnyPatterns",
        "not_like_all_patterns": "notLikeAllPatterns",
        "regex_pattern": "regexPattern",
        "schemas": "schemas",
        "table_types": "tableTypes",
    },
)
class DataPostgresqlTablesConfig(_cdktf_9a9027ec.TerraformMetaArguments):
    def __init__(
        self,
        *,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
        database: builtins.str,
        id: typing.Optional[builtins.str] = None,
        like_all_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
        like_any_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
        not_like_all_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
        regex_pattern: typing.Optional[builtins.str] = None,
        schemas: typing.Optional[typing.Sequence[builtins.str]] = None,
        table_types: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param database: The PostgreSQL database which will be queried for table names. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs/data-sources/tables#database DataPostgresqlTables#database}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs/data-sources/tables#id DataPostgresqlTables#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param like_all_patterns: Expression(s) which will be pattern matched against table names in the query using the PostgreSQL LIKE ALL operator. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs/data-sources/tables#like_all_patterns DataPostgresqlTables#like_all_patterns}
        :param like_any_patterns: Expression(s) which will be pattern matched against table names in the query using the PostgreSQL LIKE ANY operator. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs/data-sources/tables#like_any_patterns DataPostgresqlTables#like_any_patterns}
        :param not_like_all_patterns: Expression(s) which will be pattern matched against table names in the query using the PostgreSQL NOT LIKE ALL operator. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs/data-sources/tables#not_like_all_patterns DataPostgresqlTables#not_like_all_patterns}
        :param regex_pattern: Expression which will be pattern matched against table names in the query using the PostgreSQL ~ (regular expression match) operator. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs/data-sources/tables#regex_pattern DataPostgresqlTables#regex_pattern}
        :param schemas: The PostgreSQL schema(s) which will be queried for table names. Queries all schemas in the database by default. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs/data-sources/tables#schemas DataPostgresqlTables#schemas}
        :param table_types: The PostgreSQL table types which will be queried for table names. Includes all table types by default. Use 'BASE TABLE' for normal tables only Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs/data-sources/tables#table_types DataPostgresqlTables#table_types}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1cfe2c1cdad12284f4582c465b0321408300cf540b3bd83aed068c094aa277c4)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument database", value=database, expected_type=type_hints["database"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument like_all_patterns", value=like_all_patterns, expected_type=type_hints["like_all_patterns"])
            check_type(argname="argument like_any_patterns", value=like_any_patterns, expected_type=type_hints["like_any_patterns"])
            check_type(argname="argument not_like_all_patterns", value=not_like_all_patterns, expected_type=type_hints["not_like_all_patterns"])
            check_type(argname="argument regex_pattern", value=regex_pattern, expected_type=type_hints["regex_pattern"])
            check_type(argname="argument schemas", value=schemas, expected_type=type_hints["schemas"])
            check_type(argname="argument table_types", value=table_types, expected_type=type_hints["table_types"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "database": database,
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
        if id is not None:
            self._values["id"] = id
        if like_all_patterns is not None:
            self._values["like_all_patterns"] = like_all_patterns
        if like_any_patterns is not None:
            self._values["like_any_patterns"] = like_any_patterns
        if not_like_all_patterns is not None:
            self._values["not_like_all_patterns"] = not_like_all_patterns
        if regex_pattern is not None:
            self._values["regex_pattern"] = regex_pattern
        if schemas is not None:
            self._values["schemas"] = schemas
        if table_types is not None:
            self._values["table_types"] = table_types

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
    def count(
        self,
    ) -> typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]], result)

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
    def database(self) -> builtins.str:
        '''The PostgreSQL database which will be queried for table names.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs/data-sources/tables#database DataPostgresqlTables#database}
        '''
        result = self._values.get("database")
        assert result is not None, "Required property 'database' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs/data-sources/tables#id DataPostgresqlTables#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def like_all_patterns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Expression(s) which will be pattern matched against table names in the query using the PostgreSQL LIKE ALL operator.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs/data-sources/tables#like_all_patterns DataPostgresqlTables#like_all_patterns}
        '''
        result = self._values.get("like_all_patterns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def like_any_patterns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Expression(s) which will be pattern matched against table names in the query using the PostgreSQL LIKE ANY operator.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs/data-sources/tables#like_any_patterns DataPostgresqlTables#like_any_patterns}
        '''
        result = self._values.get("like_any_patterns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def not_like_all_patterns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Expression(s) which will be pattern matched against table names in the query using the PostgreSQL NOT LIKE ALL operator.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs/data-sources/tables#not_like_all_patterns DataPostgresqlTables#not_like_all_patterns}
        '''
        result = self._values.get("not_like_all_patterns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def regex_pattern(self) -> typing.Optional[builtins.str]:
        '''Expression which will be pattern matched against table names in the query using the PostgreSQL ~ (regular expression match) operator.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs/data-sources/tables#regex_pattern DataPostgresqlTables#regex_pattern}
        '''
        result = self._values.get("regex_pattern")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def schemas(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The PostgreSQL schema(s) which will be queried for table names. Queries all schemas in the database by default.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs/data-sources/tables#schemas DataPostgresqlTables#schemas}
        '''
        result = self._values.get("schemas")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def table_types(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The PostgreSQL table types which will be queried for table names.

        Includes all table types by default. Use 'BASE TABLE' for normal tables only

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs/data-sources/tables#table_types DataPostgresqlTables#table_types}
        '''
        result = self._values.get("table_types")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataPostgresqlTablesConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="postgresql.dataPostgresqlTables.DataPostgresqlTablesTables",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataPostgresqlTablesTables:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataPostgresqlTablesTables(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataPostgresqlTablesTablesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="postgresql.dataPostgresqlTables.DataPostgresqlTablesTablesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e44000f6c3de68e7b41ca5d241375e41564d0465ea58a25ca2009a948376b8ac)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "DataPostgresqlTablesTablesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__30208ba1ad4da87e0a663292c54a80ef5666d34e638294784f3615ee76de9905)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataPostgresqlTablesTablesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7e877c1cbf9cc397ab4e7d190ad14937e4a5da3dd9ab5b4eaa2ee7afa43048f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7d24bdd935fb9a3911c1f849e395ce748b8e31414d5fa3f2bcdcd6ad0502b4c7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__208337539cfc5732f5e86aa3779819eabfcb4615650ca2ef663f4a219f1928c7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataPostgresqlTablesTablesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="postgresql.dataPostgresqlTables.DataPostgresqlTablesTablesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b43ec1ccaef75c6ee3adf6c71d806693e78ce04cbd49e5c2bc79eefef822ce93)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="objectName")
    def object_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "objectName"))

    @builtins.property
    @jsii.member(jsii_name="schemaName")
    def schema_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "schemaName"))

    @builtins.property
    @jsii.member(jsii_name="tableType")
    def table_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tableType"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataPostgresqlTablesTables]:
        return typing.cast(typing.Optional[DataPostgresqlTablesTables], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataPostgresqlTablesTables],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__193b273fef00b7a7f63673b7ae2968342f19dd4d6c87d7b4bed1b74d8922e30f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DataPostgresqlTables",
    "DataPostgresqlTablesConfig",
    "DataPostgresqlTablesTables",
    "DataPostgresqlTablesTablesList",
    "DataPostgresqlTablesTablesOutputReference",
]

publication.publish()

def _typecheckingstub__58ce0f8e908c8f431400532ef1db229c8731ee606ea42317bbb83818d18b4c08(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    database: builtins.str,
    id: typing.Optional[builtins.str] = None,
    like_all_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
    like_any_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
    not_like_all_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
    regex_pattern: typing.Optional[builtins.str] = None,
    schemas: typing.Optional[typing.Sequence[builtins.str]] = None,
    table_types: typing.Optional[typing.Sequence[builtins.str]] = None,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be762dc102c4d881d4e919e027e8f0c6163b8920843edeab44ce103aa0d3d9e1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43e77da7fc18e3a4a6a71ffd70874e74b8b3d1790bb4abdc7215d0ccc41b5f6e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5bbd1b0121bf970ef1aa698671699060780c72f121036d685506fc4b12c86334(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1516a90558703ff58c653a4d2e27d7e13296fe1118df00f4d462a59108ac8e8(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7f9883bd1e5b46ca3faff274792aecd3254ec03befbb00b219cdc9e92a4e3b9(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc5242c8457f17a45ae97c921f084d39efd5a9779e830f3dad2ba9f3f0a482e0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14a01155ad34167f0e43820324dca3d3b3f07d70ab0c1d465e84c72fd40c08ce(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91220b407319c58b3d17c88d57dcc2d432c96d1b4833e854a5947376cf924afc(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1cfe2c1cdad12284f4582c465b0321408300cf540b3bd83aed068c094aa277c4(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    database: builtins.str,
    id: typing.Optional[builtins.str] = None,
    like_all_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
    like_any_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
    not_like_all_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
    regex_pattern: typing.Optional[builtins.str] = None,
    schemas: typing.Optional[typing.Sequence[builtins.str]] = None,
    table_types: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e44000f6c3de68e7b41ca5d241375e41564d0465ea58a25ca2009a948376b8ac(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30208ba1ad4da87e0a663292c54a80ef5666d34e638294784f3615ee76de9905(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7e877c1cbf9cc397ab4e7d190ad14937e4a5da3dd9ab5b4eaa2ee7afa43048f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d24bdd935fb9a3911c1f849e395ce748b8e31414d5fa3f2bcdcd6ad0502b4c7(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__208337539cfc5732f5e86aa3779819eabfcb4615650ca2ef663f4a219f1928c7(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b43ec1ccaef75c6ee3adf6c71d806693e78ce04cbd49e5c2bc79eefef822ce93(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__193b273fef00b7a7f63673b7ae2968342f19dd4d6c87d7b4bed1b74d8922e30f(
    value: typing.Optional[DataPostgresqlTablesTables],
) -> None:
    """Type checking stubs"""
    pass
