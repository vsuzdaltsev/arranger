'''
# `data_postgresql_schemas`

Refer to the Terraform Registory for docs: [`data_postgresql_schemas`](https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs/data-sources/schemas).
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


class DataPostgresqlSchemas(
    _cdktf_9a9027ec.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="postgresql.dataPostgresqlSchemas.DataPostgresqlSchemas",
):
    '''Represents a {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs/data-sources/schemas postgresql_schemas}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        database: builtins.str,
        id: typing.Optional[builtins.str] = None,
        include_system_schemas: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        like_all_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
        like_any_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
        not_like_all_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
        regex_pattern: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs/data-sources/schemas postgresql_schemas} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param database: The PostgreSQL database which will be queried for schema names. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs/data-sources/schemas#database DataPostgresqlSchemas#database}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs/data-sources/schemas#id DataPostgresqlSchemas#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param include_system_schemas: Determines whether to include system schemas (pg_ prefix and information_schema). 'public' will always be included. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs/data-sources/schemas#include_system_schemas DataPostgresqlSchemas#include_system_schemas}
        :param like_all_patterns: Expression(s) which will be pattern matched in the query using the PostgreSQL LIKE ALL operator. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs/data-sources/schemas#like_all_patterns DataPostgresqlSchemas#like_all_patterns}
        :param like_any_patterns: Expression(s) which will be pattern matched in the query using the PostgreSQL LIKE ANY operator. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs/data-sources/schemas#like_any_patterns DataPostgresqlSchemas#like_any_patterns}
        :param not_like_all_patterns: Expression(s) which will be pattern matched in the query using the PostgreSQL NOT LIKE ALL operator. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs/data-sources/schemas#not_like_all_patterns DataPostgresqlSchemas#not_like_all_patterns}
        :param regex_pattern: Expression which will be pattern matched in the query using the PostgreSQL ~ (regular expression match) operator. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs/data-sources/schemas#regex_pattern DataPostgresqlSchemas#regex_pattern}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__636666f588e0cd9ade159fb65b884af2db1d2b7c6bb259017054555916218c01)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataPostgresqlSchemasConfig(
            database=database,
            id=id,
            include_system_schemas=include_system_schemas,
            like_all_patterns=like_all_patterns,
            like_any_patterns=like_any_patterns,
            not_like_all_patterns=not_like_all_patterns,
            regex_pattern=regex_pattern,
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

    @jsii.member(jsii_name="resetIncludeSystemSchemas")
    def reset_include_system_schemas(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludeSystemSchemas", []))

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

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="schemas")
    def schemas(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "schemas"))

    @builtins.property
    @jsii.member(jsii_name="databaseInput")
    def database_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="includeSystemSchemasInput")
    def include_system_schemas_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "includeSystemSchemasInput"))

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
    @jsii.member(jsii_name="database")
    def database(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "database"))

    @database.setter
    def database(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d80c5e35c1457291fc57a0ee6e332594c524299ee9e18da89c916b578c9725d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "database", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26e59dc4ac1fa7f9ff7f2ff4c360e71a0dd1131ecf960c1ded2bc26782ad7fad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="includeSystemSchemas")
    def include_system_schemas(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "includeSystemSchemas"))

    @include_system_schemas.setter
    def include_system_schemas(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1328ebbe53f8d45237f506c470fba8a6bef612647fec04834666abdfa7604fa5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includeSystemSchemas", value)

    @builtins.property
    @jsii.member(jsii_name="likeAllPatterns")
    def like_all_patterns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "likeAllPatterns"))

    @like_all_patterns.setter
    def like_all_patterns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb254b342c787c9bc465a08142e77d416f3f36582a7a322b5914fa12198ff942)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "likeAllPatterns", value)

    @builtins.property
    @jsii.member(jsii_name="likeAnyPatterns")
    def like_any_patterns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "likeAnyPatterns"))

    @like_any_patterns.setter
    def like_any_patterns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15b57e0aa4bf5697ba9118955cc1e222e356d04d91923413021b6e1fb04a4a0a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "likeAnyPatterns", value)

    @builtins.property
    @jsii.member(jsii_name="notLikeAllPatterns")
    def not_like_all_patterns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "notLikeAllPatterns"))

    @not_like_all_patterns.setter
    def not_like_all_patterns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__adad589e285b3f7a07a3900028fe1fe4422ba379292dcf09f052553caaf75fa4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notLikeAllPatterns", value)

    @builtins.property
    @jsii.member(jsii_name="regexPattern")
    def regex_pattern(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "regexPattern"))

    @regex_pattern.setter
    def regex_pattern(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c6ddea7678e60a6753b532c74d468126f17a7fab1fd0fa76f21688caf4fb93f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "regexPattern", value)


@jsii.data_type(
    jsii_type="postgresql.dataPostgresqlSchemas.DataPostgresqlSchemasConfig",
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
        "include_system_schemas": "includeSystemSchemas",
        "like_all_patterns": "likeAllPatterns",
        "like_any_patterns": "likeAnyPatterns",
        "not_like_all_patterns": "notLikeAllPatterns",
        "regex_pattern": "regexPattern",
    },
)
class DataPostgresqlSchemasConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        include_system_schemas: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        like_all_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
        like_any_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
        not_like_all_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
        regex_pattern: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param database: The PostgreSQL database which will be queried for schema names. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs/data-sources/schemas#database DataPostgresqlSchemas#database}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs/data-sources/schemas#id DataPostgresqlSchemas#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param include_system_schemas: Determines whether to include system schemas (pg_ prefix and information_schema). 'public' will always be included. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs/data-sources/schemas#include_system_schemas DataPostgresqlSchemas#include_system_schemas}
        :param like_all_patterns: Expression(s) which will be pattern matched in the query using the PostgreSQL LIKE ALL operator. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs/data-sources/schemas#like_all_patterns DataPostgresqlSchemas#like_all_patterns}
        :param like_any_patterns: Expression(s) which will be pattern matched in the query using the PostgreSQL LIKE ANY operator. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs/data-sources/schemas#like_any_patterns DataPostgresqlSchemas#like_any_patterns}
        :param not_like_all_patterns: Expression(s) which will be pattern matched in the query using the PostgreSQL NOT LIKE ALL operator. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs/data-sources/schemas#not_like_all_patterns DataPostgresqlSchemas#not_like_all_patterns}
        :param regex_pattern: Expression which will be pattern matched in the query using the PostgreSQL ~ (regular expression match) operator. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs/data-sources/schemas#regex_pattern DataPostgresqlSchemas#regex_pattern}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92feb660e01dc013b3a41e0ee3fedf8c9ca37e07cde45bf4f0ca07bee960ac42)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument database", value=database, expected_type=type_hints["database"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument include_system_schemas", value=include_system_schemas, expected_type=type_hints["include_system_schemas"])
            check_type(argname="argument like_all_patterns", value=like_all_patterns, expected_type=type_hints["like_all_patterns"])
            check_type(argname="argument like_any_patterns", value=like_any_patterns, expected_type=type_hints["like_any_patterns"])
            check_type(argname="argument not_like_all_patterns", value=not_like_all_patterns, expected_type=type_hints["not_like_all_patterns"])
            check_type(argname="argument regex_pattern", value=regex_pattern, expected_type=type_hints["regex_pattern"])
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
        if include_system_schemas is not None:
            self._values["include_system_schemas"] = include_system_schemas
        if like_all_patterns is not None:
            self._values["like_all_patterns"] = like_all_patterns
        if like_any_patterns is not None:
            self._values["like_any_patterns"] = like_any_patterns
        if not_like_all_patterns is not None:
            self._values["not_like_all_patterns"] = not_like_all_patterns
        if regex_pattern is not None:
            self._values["regex_pattern"] = regex_pattern

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
        '''The PostgreSQL database which will be queried for schema names.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs/data-sources/schemas#database DataPostgresqlSchemas#database}
        '''
        result = self._values.get("database")
        assert result is not None, "Required property 'database' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs/data-sources/schemas#id DataPostgresqlSchemas#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def include_system_schemas(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Determines whether to include system schemas (pg_ prefix and information_schema). 'public' will always be included.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs/data-sources/schemas#include_system_schemas DataPostgresqlSchemas#include_system_schemas}
        '''
        result = self._values.get("include_system_schemas")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def like_all_patterns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Expression(s) which will be pattern matched in the query using the PostgreSQL LIKE ALL operator.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs/data-sources/schemas#like_all_patterns DataPostgresqlSchemas#like_all_patterns}
        '''
        result = self._values.get("like_all_patterns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def like_any_patterns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Expression(s) which will be pattern matched in the query using the PostgreSQL LIKE ANY operator.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs/data-sources/schemas#like_any_patterns DataPostgresqlSchemas#like_any_patterns}
        '''
        result = self._values.get("like_any_patterns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def not_like_all_patterns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Expression(s) which will be pattern matched in the query using the PostgreSQL NOT LIKE ALL operator.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs/data-sources/schemas#not_like_all_patterns DataPostgresqlSchemas#not_like_all_patterns}
        '''
        result = self._values.get("not_like_all_patterns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def regex_pattern(self) -> typing.Optional[builtins.str]:
        '''Expression which will be pattern matched in the query using the PostgreSQL ~ (regular expression match) operator.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs/data-sources/schemas#regex_pattern DataPostgresqlSchemas#regex_pattern}
        '''
        result = self._values.get("regex_pattern")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataPostgresqlSchemasConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "DataPostgresqlSchemas",
    "DataPostgresqlSchemasConfig",
]

publication.publish()

def _typecheckingstub__636666f588e0cd9ade159fb65b884af2db1d2b7c6bb259017054555916218c01(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    database: builtins.str,
    id: typing.Optional[builtins.str] = None,
    include_system_schemas: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    like_all_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
    like_any_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
    not_like_all_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
    regex_pattern: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__0d80c5e35c1457291fc57a0ee6e332594c524299ee9e18da89c916b578c9725d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26e59dc4ac1fa7f9ff7f2ff4c360e71a0dd1131ecf960c1ded2bc26782ad7fad(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1328ebbe53f8d45237f506c470fba8a6bef612647fec04834666abdfa7604fa5(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb254b342c787c9bc465a08142e77d416f3f36582a7a322b5914fa12198ff942(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15b57e0aa4bf5697ba9118955cc1e222e356d04d91923413021b6e1fb04a4a0a(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__adad589e285b3f7a07a3900028fe1fe4422ba379292dcf09f052553caaf75fa4(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6ddea7678e60a6753b532c74d468126f17a7fab1fd0fa76f21688caf4fb93f8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92feb660e01dc013b3a41e0ee3fedf8c9ca37e07cde45bf4f0ca07bee960ac42(
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
    include_system_schemas: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    like_all_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
    like_any_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
    not_like_all_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
    regex_pattern: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
