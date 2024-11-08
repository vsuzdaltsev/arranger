'''
# `aws_lakeformation_resource_lf_tags`

Refer to the Terraform Registory for docs: [`aws_lakeformation_resource_lf_tags`](https://www.terraform.io/docs/providers/aws/r/lakeformation_resource_lf_tags).
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


class LakeformationResourceLfTags(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lakeformationResourceLfTags.LakeformationResourceLfTags",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_resource_lf_tags aws_lakeformation_resource_lf_tags}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        lf_tag: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LakeformationResourceLfTagsLfTag", typing.Dict[builtins.str, typing.Any]]]],
        catalog_id: typing.Optional[builtins.str] = None,
        database: typing.Optional[typing.Union["LakeformationResourceLfTagsDatabase", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        table: typing.Optional[typing.Union["LakeformationResourceLfTagsTable", typing.Dict[builtins.str, typing.Any]]] = None,
        table_with_columns: typing.Optional[typing.Union["LakeformationResourceLfTagsTableWithColumns", typing.Dict[builtins.str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["LakeformationResourceLfTagsTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_resource_lf_tags aws_lakeformation_resource_lf_tags} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param lf_tag: lf_tag block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_resource_lf_tags#lf_tag LakeformationResourceLfTags#lf_tag}
        :param catalog_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_resource_lf_tags#catalog_id LakeformationResourceLfTags#catalog_id}.
        :param database: database block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_resource_lf_tags#database LakeformationResourceLfTags#database}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_resource_lf_tags#id LakeformationResourceLfTags#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param table: table block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_resource_lf_tags#table LakeformationResourceLfTags#table}
        :param table_with_columns: table_with_columns block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_resource_lf_tags#table_with_columns LakeformationResourceLfTags#table_with_columns}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_resource_lf_tags#timeouts LakeformationResourceLfTags#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39f076c554285c456060b76dd557323bea60ab580cd7241b9b9665af34f060a0)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = LakeformationResourceLfTagsConfig(
            lf_tag=lf_tag,
            catalog_id=catalog_id,
            database=database,
            id=id,
            table=table,
            table_with_columns=table_with_columns,
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

    @jsii.member(jsii_name="putDatabase")
    def put_database(
        self,
        *,
        name: builtins.str,
        catalog_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_resource_lf_tags#name LakeformationResourceLfTags#name}.
        :param catalog_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_resource_lf_tags#catalog_id LakeformationResourceLfTags#catalog_id}.
        '''
        value = LakeformationResourceLfTagsDatabase(name=name, catalog_id=catalog_id)

        return typing.cast(None, jsii.invoke(self, "putDatabase", [value]))

    @jsii.member(jsii_name="putLfTag")
    def put_lf_tag(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LakeformationResourceLfTagsLfTag", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2be5e2fba25d124e503305bf5de36c302bb57488013fde277e56f995b3ec4545)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLfTag", [value]))

    @jsii.member(jsii_name="putTable")
    def put_table(
        self,
        *,
        database_name: builtins.str,
        catalog_id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        wildcard: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param database_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_resource_lf_tags#database_name LakeformationResourceLfTags#database_name}.
        :param catalog_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_resource_lf_tags#catalog_id LakeformationResourceLfTags#catalog_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_resource_lf_tags#name LakeformationResourceLfTags#name}.
        :param wildcard: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_resource_lf_tags#wildcard LakeformationResourceLfTags#wildcard}.
        '''
        value = LakeformationResourceLfTagsTable(
            database_name=database_name,
            catalog_id=catalog_id,
            name=name,
            wildcard=wildcard,
        )

        return typing.cast(None, jsii.invoke(self, "putTable", [value]))

    @jsii.member(jsii_name="putTableWithColumns")
    def put_table_with_columns(
        self,
        *,
        database_name: builtins.str,
        name: builtins.str,
        catalog_id: typing.Optional[builtins.str] = None,
        column_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        excluded_column_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        wildcard: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param database_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_resource_lf_tags#database_name LakeformationResourceLfTags#database_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_resource_lf_tags#name LakeformationResourceLfTags#name}.
        :param catalog_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_resource_lf_tags#catalog_id LakeformationResourceLfTags#catalog_id}.
        :param column_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_resource_lf_tags#column_names LakeformationResourceLfTags#column_names}.
        :param excluded_column_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_resource_lf_tags#excluded_column_names LakeformationResourceLfTags#excluded_column_names}.
        :param wildcard: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_resource_lf_tags#wildcard LakeformationResourceLfTags#wildcard}.
        '''
        value = LakeformationResourceLfTagsTableWithColumns(
            database_name=database_name,
            name=name,
            catalog_id=catalog_id,
            column_names=column_names,
            excluded_column_names=excluded_column_names,
            wildcard=wildcard,
        )

        return typing.cast(None, jsii.invoke(self, "putTableWithColumns", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_resource_lf_tags#create LakeformationResourceLfTags#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_resource_lf_tags#delete LakeformationResourceLfTags#delete}.
        '''
        value = LakeformationResourceLfTagsTimeouts(create=create, delete=delete)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetCatalogId")
    def reset_catalog_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCatalogId", []))

    @jsii.member(jsii_name="resetDatabase")
    def reset_database(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatabase", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetTable")
    def reset_table(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTable", []))

    @jsii.member(jsii_name="resetTableWithColumns")
    def reset_table_with_columns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTableWithColumns", []))

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
    @jsii.member(jsii_name="database")
    def database(self) -> "LakeformationResourceLfTagsDatabaseOutputReference":
        return typing.cast("LakeformationResourceLfTagsDatabaseOutputReference", jsii.get(self, "database"))

    @builtins.property
    @jsii.member(jsii_name="lfTag")
    def lf_tag(self) -> "LakeformationResourceLfTagsLfTagList":
        return typing.cast("LakeformationResourceLfTagsLfTagList", jsii.get(self, "lfTag"))

    @builtins.property
    @jsii.member(jsii_name="table")
    def table(self) -> "LakeformationResourceLfTagsTableOutputReference":
        return typing.cast("LakeformationResourceLfTagsTableOutputReference", jsii.get(self, "table"))

    @builtins.property
    @jsii.member(jsii_name="tableWithColumns")
    def table_with_columns(
        self,
    ) -> "LakeformationResourceLfTagsTableWithColumnsOutputReference":
        return typing.cast("LakeformationResourceLfTagsTableWithColumnsOutputReference", jsii.get(self, "tableWithColumns"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "LakeformationResourceLfTagsTimeoutsOutputReference":
        return typing.cast("LakeformationResourceLfTagsTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="catalogIdInput")
    def catalog_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "catalogIdInput"))

    @builtins.property
    @jsii.member(jsii_name="databaseInput")
    def database_input(self) -> typing.Optional["LakeformationResourceLfTagsDatabase"]:
        return typing.cast(typing.Optional["LakeformationResourceLfTagsDatabase"], jsii.get(self, "databaseInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="lfTagInput")
    def lf_tag_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LakeformationResourceLfTagsLfTag"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LakeformationResourceLfTagsLfTag"]]], jsii.get(self, "lfTagInput"))

    @builtins.property
    @jsii.member(jsii_name="tableInput")
    def table_input(self) -> typing.Optional["LakeformationResourceLfTagsTable"]:
        return typing.cast(typing.Optional["LakeformationResourceLfTagsTable"], jsii.get(self, "tableInput"))

    @builtins.property
    @jsii.member(jsii_name="tableWithColumnsInput")
    def table_with_columns_input(
        self,
    ) -> typing.Optional["LakeformationResourceLfTagsTableWithColumns"]:
        return typing.cast(typing.Optional["LakeformationResourceLfTagsTableWithColumns"], jsii.get(self, "tableWithColumnsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["LakeformationResourceLfTagsTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["LakeformationResourceLfTagsTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="catalogId")
    def catalog_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "catalogId"))

    @catalog_id.setter
    def catalog_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f66e19706284df9d74d2b1bca1ef462ce8576617d9f5cbcbc4424eb45c4e8b79)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "catalogId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df5fe67c8862289680e8ac43a515ae03845179ca4d69249e005af23901080f60)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)


@jsii.data_type(
    jsii_type="aws.lakeformationResourceLfTags.LakeformationResourceLfTagsConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "lf_tag": "lfTag",
        "catalog_id": "catalogId",
        "database": "database",
        "id": "id",
        "table": "table",
        "table_with_columns": "tableWithColumns",
        "timeouts": "timeouts",
    },
)
class LakeformationResourceLfTagsConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        lf_tag: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LakeformationResourceLfTagsLfTag", typing.Dict[builtins.str, typing.Any]]]],
        catalog_id: typing.Optional[builtins.str] = None,
        database: typing.Optional[typing.Union["LakeformationResourceLfTagsDatabase", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        table: typing.Optional[typing.Union["LakeformationResourceLfTagsTable", typing.Dict[builtins.str, typing.Any]]] = None,
        table_with_columns: typing.Optional[typing.Union["LakeformationResourceLfTagsTableWithColumns", typing.Dict[builtins.str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["LakeformationResourceLfTagsTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param lf_tag: lf_tag block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_resource_lf_tags#lf_tag LakeformationResourceLfTags#lf_tag}
        :param catalog_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_resource_lf_tags#catalog_id LakeformationResourceLfTags#catalog_id}.
        :param database: database block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_resource_lf_tags#database LakeformationResourceLfTags#database}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_resource_lf_tags#id LakeformationResourceLfTags#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param table: table block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_resource_lf_tags#table LakeformationResourceLfTags#table}
        :param table_with_columns: table_with_columns block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_resource_lf_tags#table_with_columns LakeformationResourceLfTags#table_with_columns}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_resource_lf_tags#timeouts LakeformationResourceLfTags#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(database, dict):
            database = LakeformationResourceLfTagsDatabase(**database)
        if isinstance(table, dict):
            table = LakeformationResourceLfTagsTable(**table)
        if isinstance(table_with_columns, dict):
            table_with_columns = LakeformationResourceLfTagsTableWithColumns(**table_with_columns)
        if isinstance(timeouts, dict):
            timeouts = LakeformationResourceLfTagsTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1943d6e3e15f4a76299df2cc26873b0bd9e5bb73954e6905682578fd5f5f63fb)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument lf_tag", value=lf_tag, expected_type=type_hints["lf_tag"])
            check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
            check_type(argname="argument database", value=database, expected_type=type_hints["database"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument table", value=table, expected_type=type_hints["table"])
            check_type(argname="argument table_with_columns", value=table_with_columns, expected_type=type_hints["table_with_columns"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "lf_tag": lf_tag,
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
        if catalog_id is not None:
            self._values["catalog_id"] = catalog_id
        if database is not None:
            self._values["database"] = database
        if id is not None:
            self._values["id"] = id
        if table is not None:
            self._values["table"] = table
        if table_with_columns is not None:
            self._values["table_with_columns"] = table_with_columns
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
    def lf_tag(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LakeformationResourceLfTagsLfTag"]]:
        '''lf_tag block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_resource_lf_tags#lf_tag LakeformationResourceLfTags#lf_tag}
        '''
        result = self._values.get("lf_tag")
        assert result is not None, "Required property 'lf_tag' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LakeformationResourceLfTagsLfTag"]], result)

    @builtins.property
    def catalog_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_resource_lf_tags#catalog_id LakeformationResourceLfTags#catalog_id}.'''
        result = self._values.get("catalog_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def database(self) -> typing.Optional["LakeformationResourceLfTagsDatabase"]:
        '''database block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_resource_lf_tags#database LakeformationResourceLfTags#database}
        '''
        result = self._values.get("database")
        return typing.cast(typing.Optional["LakeformationResourceLfTagsDatabase"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_resource_lf_tags#id LakeformationResourceLfTags#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def table(self) -> typing.Optional["LakeformationResourceLfTagsTable"]:
        '''table block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_resource_lf_tags#table LakeformationResourceLfTags#table}
        '''
        result = self._values.get("table")
        return typing.cast(typing.Optional["LakeformationResourceLfTagsTable"], result)

    @builtins.property
    def table_with_columns(
        self,
    ) -> typing.Optional["LakeformationResourceLfTagsTableWithColumns"]:
        '''table_with_columns block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_resource_lf_tags#table_with_columns LakeformationResourceLfTags#table_with_columns}
        '''
        result = self._values.get("table_with_columns")
        return typing.cast(typing.Optional["LakeformationResourceLfTagsTableWithColumns"], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["LakeformationResourceLfTagsTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_resource_lf_tags#timeouts LakeformationResourceLfTags#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["LakeformationResourceLfTagsTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LakeformationResourceLfTagsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.lakeformationResourceLfTags.LakeformationResourceLfTagsDatabase",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "catalog_id": "catalogId"},
)
class LakeformationResourceLfTagsDatabase:
    def __init__(
        self,
        *,
        name: builtins.str,
        catalog_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_resource_lf_tags#name LakeformationResourceLfTags#name}.
        :param catalog_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_resource_lf_tags#catalog_id LakeformationResourceLfTags#catalog_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ab85b52ced0c0ce59899dad5209a527b7038a3a8fc2b6bbd6c273416643dee0)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if catalog_id is not None:
            self._values["catalog_id"] = catalog_id

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_resource_lf_tags#name LakeformationResourceLfTags#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def catalog_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_resource_lf_tags#catalog_id LakeformationResourceLfTags#catalog_id}.'''
        result = self._values.get("catalog_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LakeformationResourceLfTagsDatabase(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LakeformationResourceLfTagsDatabaseOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lakeformationResourceLfTags.LakeformationResourceLfTagsDatabaseOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4333aa32d6b056ce5ab8661e8c20fa9ca52fe0d213749e059892c9eaabceb272)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCatalogId")
    def reset_catalog_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCatalogId", []))

    @builtins.property
    @jsii.member(jsii_name="catalogIdInput")
    def catalog_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "catalogIdInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="catalogId")
    def catalog_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "catalogId"))

    @catalog_id.setter
    def catalog_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1623938c39d55ecc184a2759a9c63e34d47bd07a417374ce90a5a1cac600079)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "catalogId", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5a40bb63c5c3d38f70b87a35b38f6ab13ab0ac1df57533e4252f89db180e120)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LakeformationResourceLfTagsDatabase]:
        return typing.cast(typing.Optional[LakeformationResourceLfTagsDatabase], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LakeformationResourceLfTagsDatabase],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b8f841dfeeb377c17c89853b06f5f7e0d753097d71b9b6b2e031bc0986c7373)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.lakeformationResourceLfTags.LakeformationResourceLfTagsLfTag",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "value": "value", "catalog_id": "catalogId"},
)
class LakeformationResourceLfTagsLfTag:
    def __init__(
        self,
        *,
        key: builtins.str,
        value: builtins.str,
        catalog_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_resource_lf_tags#key LakeformationResourceLfTags#key}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_resource_lf_tags#value LakeformationResourceLfTags#value}.
        :param catalog_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_resource_lf_tags#catalog_id LakeformationResourceLfTags#catalog_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af3574eca405e9d8dd23d21f9a73fe4fe9ed46d609254f59bf0b9afadcba6403)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
            "value": value,
        }
        if catalog_id is not None:
            self._values["catalog_id"] = catalog_id

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_resource_lf_tags#key LakeformationResourceLfTags#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_resource_lf_tags#value LakeformationResourceLfTags#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def catalog_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_resource_lf_tags#catalog_id LakeformationResourceLfTags#catalog_id}.'''
        result = self._values.get("catalog_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LakeformationResourceLfTagsLfTag(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LakeformationResourceLfTagsLfTagList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lakeformationResourceLfTags.LakeformationResourceLfTagsLfTagList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6ef6696d9dcbfcd851c7bee4803abf912b5151e61e56a6a4b12d9849c4363621)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LakeformationResourceLfTagsLfTagOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2454a92e1251bf3d0fff73f3a921a5d0251223e2336f1e2e90f4e78662c91c91)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LakeformationResourceLfTagsLfTagOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b45da11c77eb9093b59acc927b9cd1f2e0c2ef2fdb8e04d6ae0b9a869c25c7f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0bb13bee8e94b0dc525afd217c1eaaa856f0a4091fc9a738409612a1d2195fe9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e044175dde581ad0655784342edc61e96a7f86cc6869bbf8b7cc638579278bf8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LakeformationResourceLfTagsLfTag]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LakeformationResourceLfTagsLfTag]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LakeformationResourceLfTagsLfTag]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e315b990352a768ac7fb173385dadded8fd341234389947dcde41958d13c2c88)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LakeformationResourceLfTagsLfTagOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lakeformationResourceLfTags.LakeformationResourceLfTagsLfTagOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__60dd8903771032b8c891cd83c6df3c03ccfdcb3d4d3097a2b408578132184309)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCatalogId")
    def reset_catalog_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCatalogId", []))

    @builtins.property
    @jsii.member(jsii_name="catalogIdInput")
    def catalog_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "catalogIdInput"))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="catalogId")
    def catalog_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "catalogId"))

    @catalog_id.setter
    def catalog_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76ea43ca64356110a8747a4dcbcfd5e9e7b4dd7b2cf47e915d55ee40b01358b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "catalogId", value)

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8b1a83e9bd65b05e2e2429eccee5bc191051ed990be66ddef582ff0b6efcbb6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__873bc00687ae07dab3fe06ca90b2fd36c28a586101cb8aed882e7f827c57922a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LakeformationResourceLfTagsLfTag, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LakeformationResourceLfTagsLfTag, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LakeformationResourceLfTagsLfTag, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__429ae855ee542f72e5c11cabdefd519e6de7b62750b20cd9f43aac1ce5332060)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.lakeformationResourceLfTags.LakeformationResourceLfTagsTable",
    jsii_struct_bases=[],
    name_mapping={
        "database_name": "databaseName",
        "catalog_id": "catalogId",
        "name": "name",
        "wildcard": "wildcard",
    },
)
class LakeformationResourceLfTagsTable:
    def __init__(
        self,
        *,
        database_name: builtins.str,
        catalog_id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        wildcard: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param database_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_resource_lf_tags#database_name LakeformationResourceLfTags#database_name}.
        :param catalog_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_resource_lf_tags#catalog_id LakeformationResourceLfTags#catalog_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_resource_lf_tags#name LakeformationResourceLfTags#name}.
        :param wildcard: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_resource_lf_tags#wildcard LakeformationResourceLfTags#wildcard}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3a9992e210c195c64a5a86413664d23471c2d01b28c15f7b01dae044c579bca)
            check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
            check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument wildcard", value=wildcard, expected_type=type_hints["wildcard"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "database_name": database_name,
        }
        if catalog_id is not None:
            self._values["catalog_id"] = catalog_id
        if name is not None:
            self._values["name"] = name
        if wildcard is not None:
            self._values["wildcard"] = wildcard

    @builtins.property
    def database_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_resource_lf_tags#database_name LakeformationResourceLfTags#database_name}.'''
        result = self._values.get("database_name")
        assert result is not None, "Required property 'database_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def catalog_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_resource_lf_tags#catalog_id LakeformationResourceLfTags#catalog_id}.'''
        result = self._values.get("catalog_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_resource_lf_tags#name LakeformationResourceLfTags#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def wildcard(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_resource_lf_tags#wildcard LakeformationResourceLfTags#wildcard}.'''
        result = self._values.get("wildcard")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LakeformationResourceLfTagsTable(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LakeformationResourceLfTagsTableOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lakeformationResourceLfTags.LakeformationResourceLfTagsTableOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2882acadd42194b6aa301f18d5780516e8238766dfc174ed9c1cdb56220abe35)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCatalogId")
    def reset_catalog_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCatalogId", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetWildcard")
    def reset_wildcard(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWildcard", []))

    @builtins.property
    @jsii.member(jsii_name="catalogIdInput")
    def catalog_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "catalogIdInput"))

    @builtins.property
    @jsii.member(jsii_name="databaseNameInput")
    def database_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseNameInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="wildcardInput")
    def wildcard_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "wildcardInput"))

    @builtins.property
    @jsii.member(jsii_name="catalogId")
    def catalog_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "catalogId"))

    @catalog_id.setter
    def catalog_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bdc7a847c85dd4c718339610a6c1cf7f624d79613f30b30c6846369a9f3555f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "catalogId", value)

    @builtins.property
    @jsii.member(jsii_name="databaseName")
    def database_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "databaseName"))

    @database_name.setter
    def database_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f593fa8537570ccd9f5c37d9d309c94b4f0863af4e3e3f234fe8c8caea5040bd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "databaseName", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d158b5c22a3e4e597d73724554f9aa5fc22b047d9e556917134a89021ca62c96)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="wildcard")
    def wildcard(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "wildcard"))

    @wildcard.setter
    def wildcard(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__453874710aaae1847c4e89f4eb37752dac47d749fdee060d80cdd3b56e4ed953)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wildcard", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LakeformationResourceLfTagsTable]:
        return typing.cast(typing.Optional[LakeformationResourceLfTagsTable], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LakeformationResourceLfTagsTable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__624a902ef5c5a8f3e9110eddacb4db740807b0bfa7e6a5e7c5a7efd12ca11474)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.lakeformationResourceLfTags.LakeformationResourceLfTagsTableWithColumns",
    jsii_struct_bases=[],
    name_mapping={
        "database_name": "databaseName",
        "name": "name",
        "catalog_id": "catalogId",
        "column_names": "columnNames",
        "excluded_column_names": "excludedColumnNames",
        "wildcard": "wildcard",
    },
)
class LakeformationResourceLfTagsTableWithColumns:
    def __init__(
        self,
        *,
        database_name: builtins.str,
        name: builtins.str,
        catalog_id: typing.Optional[builtins.str] = None,
        column_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        excluded_column_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        wildcard: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param database_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_resource_lf_tags#database_name LakeformationResourceLfTags#database_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_resource_lf_tags#name LakeformationResourceLfTags#name}.
        :param catalog_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_resource_lf_tags#catalog_id LakeformationResourceLfTags#catalog_id}.
        :param column_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_resource_lf_tags#column_names LakeformationResourceLfTags#column_names}.
        :param excluded_column_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_resource_lf_tags#excluded_column_names LakeformationResourceLfTags#excluded_column_names}.
        :param wildcard: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_resource_lf_tags#wildcard LakeformationResourceLfTags#wildcard}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c7ee56df27503aede123055ad1b1dc8d9f5f1153c818956852215eb1df82c1e)
            check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
            check_type(argname="argument column_names", value=column_names, expected_type=type_hints["column_names"])
            check_type(argname="argument excluded_column_names", value=excluded_column_names, expected_type=type_hints["excluded_column_names"])
            check_type(argname="argument wildcard", value=wildcard, expected_type=type_hints["wildcard"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "database_name": database_name,
            "name": name,
        }
        if catalog_id is not None:
            self._values["catalog_id"] = catalog_id
        if column_names is not None:
            self._values["column_names"] = column_names
        if excluded_column_names is not None:
            self._values["excluded_column_names"] = excluded_column_names
        if wildcard is not None:
            self._values["wildcard"] = wildcard

    @builtins.property
    def database_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_resource_lf_tags#database_name LakeformationResourceLfTags#database_name}.'''
        result = self._values.get("database_name")
        assert result is not None, "Required property 'database_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_resource_lf_tags#name LakeformationResourceLfTags#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def catalog_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_resource_lf_tags#catalog_id LakeformationResourceLfTags#catalog_id}.'''
        result = self._values.get("catalog_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def column_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_resource_lf_tags#column_names LakeformationResourceLfTags#column_names}.'''
        result = self._values.get("column_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def excluded_column_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_resource_lf_tags#excluded_column_names LakeformationResourceLfTags#excluded_column_names}.'''
        result = self._values.get("excluded_column_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def wildcard(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_resource_lf_tags#wildcard LakeformationResourceLfTags#wildcard}.'''
        result = self._values.get("wildcard")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LakeformationResourceLfTagsTableWithColumns(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LakeformationResourceLfTagsTableWithColumnsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lakeformationResourceLfTags.LakeformationResourceLfTagsTableWithColumnsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__37c4252786e0d571dfec5fbc91c91146622b37712a5f7f36b0079f3df4712c5d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCatalogId")
    def reset_catalog_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCatalogId", []))

    @jsii.member(jsii_name="resetColumnNames")
    def reset_column_names(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetColumnNames", []))

    @jsii.member(jsii_name="resetExcludedColumnNames")
    def reset_excluded_column_names(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExcludedColumnNames", []))

    @jsii.member(jsii_name="resetWildcard")
    def reset_wildcard(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWildcard", []))

    @builtins.property
    @jsii.member(jsii_name="catalogIdInput")
    def catalog_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "catalogIdInput"))

    @builtins.property
    @jsii.member(jsii_name="columnNamesInput")
    def column_names_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "columnNamesInput"))

    @builtins.property
    @jsii.member(jsii_name="databaseNameInput")
    def database_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseNameInput"))

    @builtins.property
    @jsii.member(jsii_name="excludedColumnNamesInput")
    def excluded_column_names_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "excludedColumnNamesInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="wildcardInput")
    def wildcard_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "wildcardInput"))

    @builtins.property
    @jsii.member(jsii_name="catalogId")
    def catalog_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "catalogId"))

    @catalog_id.setter
    def catalog_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f657fb99327c642d6497e8ed2440cdf9305f083e45718af74ba0f1c91ffd21a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "catalogId", value)

    @builtins.property
    @jsii.member(jsii_name="columnNames")
    def column_names(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "columnNames"))

    @column_names.setter
    def column_names(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f640920cb554cf64a61da662c3fcca974d75232309b530d7f59a8519fbfbfb0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "columnNames", value)

    @builtins.property
    @jsii.member(jsii_name="databaseName")
    def database_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "databaseName"))

    @database_name.setter
    def database_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__446bc37870aafacecc0e35753be895d5762de18aa5dde3088c3fa6ea9c5f07e8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "databaseName", value)

    @builtins.property
    @jsii.member(jsii_name="excludedColumnNames")
    def excluded_column_names(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "excludedColumnNames"))

    @excluded_column_names.setter
    def excluded_column_names(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e043026a7b03fc22aa4b761dec2755ff1bd830a55b99ae7d598d91047a2d17f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "excludedColumnNames", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b35764fc2d259b34ee093d70646287c77aa974582ad1a45036d61be8f0c6a84)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="wildcard")
    def wildcard(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "wildcard"))

    @wildcard.setter
    def wildcard(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e14977ee97495245e8d1b63b400f2a22dccc3af5bc486da7d05a994f7377681)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wildcard", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LakeformationResourceLfTagsTableWithColumns]:
        return typing.cast(typing.Optional[LakeformationResourceLfTagsTableWithColumns], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LakeformationResourceLfTagsTableWithColumns],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c825d213dd32b76eae840d626689dea555798ca5cc424754693e1ea71750b533)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.lakeformationResourceLfTags.LakeformationResourceLfTagsTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete"},
)
class LakeformationResourceLfTagsTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_resource_lf_tags#create LakeformationResourceLfTags#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_resource_lf_tags#delete LakeformationResourceLfTags#delete}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0f656f1918d6432fcd66038c5423c1e51b076a3e2ca88096d238b6090875604)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_resource_lf_tags#create LakeformationResourceLfTags#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_resource_lf_tags#delete LakeformationResourceLfTags#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LakeformationResourceLfTagsTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LakeformationResourceLfTagsTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lakeformationResourceLfTags.LakeformationResourceLfTagsTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cb1a1951fd80dd5d0a16b7e7b1b752fdedbcf2f531d8dd4ee96e4d09718d9ae5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b9b140879bd3931d460c48bc8da621d57ba8ef997add78286135434744bccdf7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e8a1d8bd832a441a65759a2ca34d441f906036fe1aba320b130b2238b24f0ed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LakeformationResourceLfTagsTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LakeformationResourceLfTagsTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LakeformationResourceLfTagsTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15a1c797ed97dbaa8e955424c2ea205fdfede69814a9b1fddf36444e1d1dc7b9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "LakeformationResourceLfTags",
    "LakeformationResourceLfTagsConfig",
    "LakeformationResourceLfTagsDatabase",
    "LakeformationResourceLfTagsDatabaseOutputReference",
    "LakeformationResourceLfTagsLfTag",
    "LakeformationResourceLfTagsLfTagList",
    "LakeformationResourceLfTagsLfTagOutputReference",
    "LakeformationResourceLfTagsTable",
    "LakeformationResourceLfTagsTableOutputReference",
    "LakeformationResourceLfTagsTableWithColumns",
    "LakeformationResourceLfTagsTableWithColumnsOutputReference",
    "LakeformationResourceLfTagsTimeouts",
    "LakeformationResourceLfTagsTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__39f076c554285c456060b76dd557323bea60ab580cd7241b9b9665af34f060a0(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    lf_tag: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LakeformationResourceLfTagsLfTag, typing.Dict[builtins.str, typing.Any]]]],
    catalog_id: typing.Optional[builtins.str] = None,
    database: typing.Optional[typing.Union[LakeformationResourceLfTagsDatabase, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    table: typing.Optional[typing.Union[LakeformationResourceLfTagsTable, typing.Dict[builtins.str, typing.Any]]] = None,
    table_with_columns: typing.Optional[typing.Union[LakeformationResourceLfTagsTableWithColumns, typing.Dict[builtins.str, typing.Any]]] = None,
    timeouts: typing.Optional[typing.Union[LakeformationResourceLfTagsTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__2be5e2fba25d124e503305bf5de36c302bb57488013fde277e56f995b3ec4545(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LakeformationResourceLfTagsLfTag, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f66e19706284df9d74d2b1bca1ef462ce8576617d9f5cbcbc4424eb45c4e8b79(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df5fe67c8862289680e8ac43a515ae03845179ca4d69249e005af23901080f60(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1943d6e3e15f4a76299df2cc26873b0bd9e5bb73954e6905682578fd5f5f63fb(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    lf_tag: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LakeformationResourceLfTagsLfTag, typing.Dict[builtins.str, typing.Any]]]],
    catalog_id: typing.Optional[builtins.str] = None,
    database: typing.Optional[typing.Union[LakeformationResourceLfTagsDatabase, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    table: typing.Optional[typing.Union[LakeformationResourceLfTagsTable, typing.Dict[builtins.str, typing.Any]]] = None,
    table_with_columns: typing.Optional[typing.Union[LakeformationResourceLfTagsTableWithColumns, typing.Dict[builtins.str, typing.Any]]] = None,
    timeouts: typing.Optional[typing.Union[LakeformationResourceLfTagsTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ab85b52ced0c0ce59899dad5209a527b7038a3a8fc2b6bbd6c273416643dee0(
    *,
    name: builtins.str,
    catalog_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4333aa32d6b056ce5ab8661e8c20fa9ca52fe0d213749e059892c9eaabceb272(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1623938c39d55ecc184a2759a9c63e34d47bd07a417374ce90a5a1cac600079(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5a40bb63c5c3d38f70b87a35b38f6ab13ab0ac1df57533e4252f89db180e120(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b8f841dfeeb377c17c89853b06f5f7e0d753097d71b9b6b2e031bc0986c7373(
    value: typing.Optional[LakeformationResourceLfTagsDatabase],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af3574eca405e9d8dd23d21f9a73fe4fe9ed46d609254f59bf0b9afadcba6403(
    *,
    key: builtins.str,
    value: builtins.str,
    catalog_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ef6696d9dcbfcd851c7bee4803abf912b5151e61e56a6a4b12d9849c4363621(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2454a92e1251bf3d0fff73f3a921a5d0251223e2336f1e2e90f4e78662c91c91(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b45da11c77eb9093b59acc927b9cd1f2e0c2ef2fdb8e04d6ae0b9a869c25c7f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0bb13bee8e94b0dc525afd217c1eaaa856f0a4091fc9a738409612a1d2195fe9(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e044175dde581ad0655784342edc61e96a7f86cc6869bbf8b7cc638579278bf8(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e315b990352a768ac7fb173385dadded8fd341234389947dcde41958d13c2c88(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LakeformationResourceLfTagsLfTag]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60dd8903771032b8c891cd83c6df3c03ccfdcb3d4d3097a2b408578132184309(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76ea43ca64356110a8747a4dcbcfd5e9e7b4dd7b2cf47e915d55ee40b01358b4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8b1a83e9bd65b05e2e2429eccee5bc191051ed990be66ddef582ff0b6efcbb6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__873bc00687ae07dab3fe06ca90b2fd36c28a586101cb8aed882e7f827c57922a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__429ae855ee542f72e5c11cabdefd519e6de7b62750b20cd9f43aac1ce5332060(
    value: typing.Optional[typing.Union[LakeformationResourceLfTagsLfTag, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3a9992e210c195c64a5a86413664d23471c2d01b28c15f7b01dae044c579bca(
    *,
    database_name: builtins.str,
    catalog_id: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    wildcard: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2882acadd42194b6aa301f18d5780516e8238766dfc174ed9c1cdb56220abe35(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bdc7a847c85dd4c718339610a6c1cf7f624d79613f30b30c6846369a9f3555f8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f593fa8537570ccd9f5c37d9d309c94b4f0863af4e3e3f234fe8c8caea5040bd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d158b5c22a3e4e597d73724554f9aa5fc22b047d9e556917134a89021ca62c96(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__453874710aaae1847c4e89f4eb37752dac47d749fdee060d80cdd3b56e4ed953(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__624a902ef5c5a8f3e9110eddacb4db740807b0bfa7e6a5e7c5a7efd12ca11474(
    value: typing.Optional[LakeformationResourceLfTagsTable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c7ee56df27503aede123055ad1b1dc8d9f5f1153c818956852215eb1df82c1e(
    *,
    database_name: builtins.str,
    name: builtins.str,
    catalog_id: typing.Optional[builtins.str] = None,
    column_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    excluded_column_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    wildcard: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37c4252786e0d571dfec5fbc91c91146622b37712a5f7f36b0079f3df4712c5d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f657fb99327c642d6497e8ed2440cdf9305f083e45718af74ba0f1c91ffd21a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f640920cb554cf64a61da662c3fcca974d75232309b530d7f59a8519fbfbfb0(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__446bc37870aafacecc0e35753be895d5762de18aa5dde3088c3fa6ea9c5f07e8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e043026a7b03fc22aa4b761dec2755ff1bd830a55b99ae7d598d91047a2d17f8(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b35764fc2d259b34ee093d70646287c77aa974582ad1a45036d61be8f0c6a84(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e14977ee97495245e8d1b63b400f2a22dccc3af5bc486da7d05a994f7377681(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c825d213dd32b76eae840d626689dea555798ca5cc424754693e1ea71750b533(
    value: typing.Optional[LakeformationResourceLfTagsTableWithColumns],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0f656f1918d6432fcd66038c5423c1e51b076a3e2ca88096d238b6090875604(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb1a1951fd80dd5d0a16b7e7b1b752fdedbcf2f531d8dd4ee96e4d09718d9ae5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9b140879bd3931d460c48bc8da621d57ba8ef997add78286135434744bccdf7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e8a1d8bd832a441a65759a2ca34d441f906036fe1aba320b130b2238b24f0ed(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15a1c797ed97dbaa8e955424c2ea205fdfede69814a9b1fddf36444e1d1dc7b9(
    value: typing.Optional[typing.Union[LakeformationResourceLfTagsTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
