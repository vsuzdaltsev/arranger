'''
# `aws_timestreamwrite_table`

Refer to the Terraform Registory for docs: [`aws_timestreamwrite_table`](https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table).
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


class TimestreamwriteTable(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.timestreamwriteTable.TimestreamwriteTable",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table aws_timestreamwrite_table}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        database_name: builtins.str,
        table_name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        magnetic_store_write_properties: typing.Optional[typing.Union["TimestreamwriteTableMagneticStoreWriteProperties", typing.Dict[builtins.str, typing.Any]]] = None,
        retention_properties: typing.Optional[typing.Union["TimestreamwriteTableRetentionProperties", typing.Dict[builtins.str, typing.Any]]] = None,
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
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table aws_timestreamwrite_table} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param database_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#database_name TimestreamwriteTable#database_name}.
        :param table_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#table_name TimestreamwriteTable#table_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#id TimestreamwriteTable#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param magnetic_store_write_properties: magnetic_store_write_properties block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#magnetic_store_write_properties TimestreamwriteTable#magnetic_store_write_properties}
        :param retention_properties: retention_properties block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#retention_properties TimestreamwriteTable#retention_properties}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#tags TimestreamwriteTable#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#tags_all TimestreamwriteTable#tags_all}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7575cb61f042c4d65198d8076a30dff566b020953d6188b988af8ad9616f14c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = TimestreamwriteTableConfig(
            database_name=database_name,
            table_name=table_name,
            id=id,
            magnetic_store_write_properties=magnetic_store_write_properties,
            retention_properties=retention_properties,
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

    @jsii.member(jsii_name="putMagneticStoreWriteProperties")
    def put_magnetic_store_write_properties(
        self,
        *,
        enable_magnetic_store_writes: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        magnetic_store_rejected_data_location: typing.Optional[typing.Union["TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocation", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param enable_magnetic_store_writes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#enable_magnetic_store_writes TimestreamwriteTable#enable_magnetic_store_writes}.
        :param magnetic_store_rejected_data_location: magnetic_store_rejected_data_location block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#magnetic_store_rejected_data_location TimestreamwriteTable#magnetic_store_rejected_data_location}
        '''
        value = TimestreamwriteTableMagneticStoreWriteProperties(
            enable_magnetic_store_writes=enable_magnetic_store_writes,
            magnetic_store_rejected_data_location=magnetic_store_rejected_data_location,
        )

        return typing.cast(None, jsii.invoke(self, "putMagneticStoreWriteProperties", [value]))

    @jsii.member(jsii_name="putRetentionProperties")
    def put_retention_properties(
        self,
        *,
        magnetic_store_retention_period_in_days: jsii.Number,
        memory_store_retention_period_in_hours: jsii.Number,
    ) -> None:
        '''
        :param magnetic_store_retention_period_in_days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#magnetic_store_retention_period_in_days TimestreamwriteTable#magnetic_store_retention_period_in_days}.
        :param memory_store_retention_period_in_hours: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#memory_store_retention_period_in_hours TimestreamwriteTable#memory_store_retention_period_in_hours}.
        '''
        value = TimestreamwriteTableRetentionProperties(
            magnetic_store_retention_period_in_days=magnetic_store_retention_period_in_days,
            memory_store_retention_period_in_hours=memory_store_retention_period_in_hours,
        )

        return typing.cast(None, jsii.invoke(self, "putRetentionProperties", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMagneticStoreWriteProperties")
    def reset_magnetic_store_write_properties(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMagneticStoreWriteProperties", []))

    @jsii.member(jsii_name="resetRetentionProperties")
    def reset_retention_properties(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetentionProperties", []))

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
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="magneticStoreWriteProperties")
    def magnetic_store_write_properties(
        self,
    ) -> "TimestreamwriteTableMagneticStoreWritePropertiesOutputReference":
        return typing.cast("TimestreamwriteTableMagneticStoreWritePropertiesOutputReference", jsii.get(self, "magneticStoreWriteProperties"))

    @builtins.property
    @jsii.member(jsii_name="retentionProperties")
    def retention_properties(
        self,
    ) -> "TimestreamwriteTableRetentionPropertiesOutputReference":
        return typing.cast("TimestreamwriteTableRetentionPropertiesOutputReference", jsii.get(self, "retentionProperties"))

    @builtins.property
    @jsii.member(jsii_name="databaseNameInput")
    def database_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseNameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="magneticStoreWritePropertiesInput")
    def magnetic_store_write_properties_input(
        self,
    ) -> typing.Optional["TimestreamwriteTableMagneticStoreWriteProperties"]:
        return typing.cast(typing.Optional["TimestreamwriteTableMagneticStoreWriteProperties"], jsii.get(self, "magneticStoreWritePropertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="retentionPropertiesInput")
    def retention_properties_input(
        self,
    ) -> typing.Optional["TimestreamwriteTableRetentionProperties"]:
        return typing.cast(typing.Optional["TimestreamwriteTableRetentionProperties"], jsii.get(self, "retentionPropertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="tableNameInput")
    def table_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tableNameInput"))

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
    @jsii.member(jsii_name="databaseName")
    def database_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "databaseName"))

    @database_name.setter
    def database_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14fb13e3a0a356dec9d19b119f55a983419c44d917d1d94db70435a76c7f5fd7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "databaseName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b0ac12a02f69011e337dbaef093e874b4e57ee2bf80a10a2b875e277a07ba87)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="tableName")
    def table_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tableName"))

    @table_name.setter
    def table_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__508b57fb94e42b6f1c7b15401f1b7dc190d8027a948ec6db6d4cafbe9b33110a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tableName", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4424483bd32c6aeb34fda4e1356a79c0824261fecd48227e1779a58a5a1e69bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af0d7dc11d11778db372ba0ac467f4eb9f0479444cf6c33296866b37f9499254)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)


@jsii.data_type(
    jsii_type="aws.timestreamwriteTable.TimestreamwriteTableConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "database_name": "databaseName",
        "table_name": "tableName",
        "id": "id",
        "magnetic_store_write_properties": "magneticStoreWriteProperties",
        "retention_properties": "retentionProperties",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class TimestreamwriteTableConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        database_name: builtins.str,
        table_name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        magnetic_store_write_properties: typing.Optional[typing.Union["TimestreamwriteTableMagneticStoreWriteProperties", typing.Dict[builtins.str, typing.Any]]] = None,
        retention_properties: typing.Optional[typing.Union["TimestreamwriteTableRetentionProperties", typing.Dict[builtins.str, typing.Any]]] = None,
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
        :param database_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#database_name TimestreamwriteTable#database_name}.
        :param table_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#table_name TimestreamwriteTable#table_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#id TimestreamwriteTable#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param magnetic_store_write_properties: magnetic_store_write_properties block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#magnetic_store_write_properties TimestreamwriteTable#magnetic_store_write_properties}
        :param retention_properties: retention_properties block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#retention_properties TimestreamwriteTable#retention_properties}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#tags TimestreamwriteTable#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#tags_all TimestreamwriteTable#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(magnetic_store_write_properties, dict):
            magnetic_store_write_properties = TimestreamwriteTableMagneticStoreWriteProperties(**magnetic_store_write_properties)
        if isinstance(retention_properties, dict):
            retention_properties = TimestreamwriteTableRetentionProperties(**retention_properties)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7369d7448a744f9fecc1c91c2151bf367d4112e0c541a533c56e60a8bee9f2e7)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
            check_type(argname="argument table_name", value=table_name, expected_type=type_hints["table_name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument magnetic_store_write_properties", value=magnetic_store_write_properties, expected_type=type_hints["magnetic_store_write_properties"])
            check_type(argname="argument retention_properties", value=retention_properties, expected_type=type_hints["retention_properties"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "database_name": database_name,
            "table_name": table_name,
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
        if magnetic_store_write_properties is not None:
            self._values["magnetic_store_write_properties"] = magnetic_store_write_properties
        if retention_properties is not None:
            self._values["retention_properties"] = retention_properties
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
    def database_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#database_name TimestreamwriteTable#database_name}.'''
        result = self._values.get("database_name")
        assert result is not None, "Required property 'database_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def table_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#table_name TimestreamwriteTable#table_name}.'''
        result = self._values.get("table_name")
        assert result is not None, "Required property 'table_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#id TimestreamwriteTable#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def magnetic_store_write_properties(
        self,
    ) -> typing.Optional["TimestreamwriteTableMagneticStoreWriteProperties"]:
        '''magnetic_store_write_properties block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#magnetic_store_write_properties TimestreamwriteTable#magnetic_store_write_properties}
        '''
        result = self._values.get("magnetic_store_write_properties")
        return typing.cast(typing.Optional["TimestreamwriteTableMagneticStoreWriteProperties"], result)

    @builtins.property
    def retention_properties(
        self,
    ) -> typing.Optional["TimestreamwriteTableRetentionProperties"]:
        '''retention_properties block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#retention_properties TimestreamwriteTable#retention_properties}
        '''
        result = self._values.get("retention_properties")
        return typing.cast(typing.Optional["TimestreamwriteTableRetentionProperties"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#tags TimestreamwriteTable#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#tags_all TimestreamwriteTable#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TimestreamwriteTableConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.timestreamwriteTable.TimestreamwriteTableMagneticStoreWriteProperties",
    jsii_struct_bases=[],
    name_mapping={
        "enable_magnetic_store_writes": "enableMagneticStoreWrites",
        "magnetic_store_rejected_data_location": "magneticStoreRejectedDataLocation",
    },
)
class TimestreamwriteTableMagneticStoreWriteProperties:
    def __init__(
        self,
        *,
        enable_magnetic_store_writes: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        magnetic_store_rejected_data_location: typing.Optional[typing.Union["TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocation", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param enable_magnetic_store_writes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#enable_magnetic_store_writes TimestreamwriteTable#enable_magnetic_store_writes}.
        :param magnetic_store_rejected_data_location: magnetic_store_rejected_data_location block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#magnetic_store_rejected_data_location TimestreamwriteTable#magnetic_store_rejected_data_location}
        '''
        if isinstance(magnetic_store_rejected_data_location, dict):
            magnetic_store_rejected_data_location = TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocation(**magnetic_store_rejected_data_location)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9742d87f0fb64eef3948ae3338e07380ed75f1b71eed804d75258b881f6a8ab)
            check_type(argname="argument enable_magnetic_store_writes", value=enable_magnetic_store_writes, expected_type=type_hints["enable_magnetic_store_writes"])
            check_type(argname="argument magnetic_store_rejected_data_location", value=magnetic_store_rejected_data_location, expected_type=type_hints["magnetic_store_rejected_data_location"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if enable_magnetic_store_writes is not None:
            self._values["enable_magnetic_store_writes"] = enable_magnetic_store_writes
        if magnetic_store_rejected_data_location is not None:
            self._values["magnetic_store_rejected_data_location"] = magnetic_store_rejected_data_location

    @builtins.property
    def enable_magnetic_store_writes(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#enable_magnetic_store_writes TimestreamwriteTable#enable_magnetic_store_writes}.'''
        result = self._values.get("enable_magnetic_store_writes")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def magnetic_store_rejected_data_location(
        self,
    ) -> typing.Optional["TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocation"]:
        '''magnetic_store_rejected_data_location block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#magnetic_store_rejected_data_location TimestreamwriteTable#magnetic_store_rejected_data_location}
        '''
        result = self._values.get("magnetic_store_rejected_data_location")
        return typing.cast(typing.Optional["TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocation"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TimestreamwriteTableMagneticStoreWriteProperties(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.timestreamwriteTable.TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocation",
    jsii_struct_bases=[],
    name_mapping={"s3_configuration": "s3Configuration"},
)
class TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocation:
    def __init__(
        self,
        *,
        s3_configuration: typing.Optional[typing.Union["TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocationS3Configuration", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param s3_configuration: s3_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#s3_configuration TimestreamwriteTable#s3_configuration}
        '''
        if isinstance(s3_configuration, dict):
            s3_configuration = TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocationS3Configuration(**s3_configuration)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1182ff1941e34ae8cf6617fc2fbe484ec6d483d8cfedaa5a3306beeee299a0cd)
            check_type(argname="argument s3_configuration", value=s3_configuration, expected_type=type_hints["s3_configuration"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if s3_configuration is not None:
            self._values["s3_configuration"] = s3_configuration

    @builtins.property
    def s3_configuration(
        self,
    ) -> typing.Optional["TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocationS3Configuration"]:
        '''s3_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#s3_configuration TimestreamwriteTable#s3_configuration}
        '''
        result = self._values.get("s3_configuration")
        return typing.cast(typing.Optional["TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocationS3Configuration"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.timestreamwriteTable.TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__edac81173e6252b7234f18b57eaed7bd9a52791a51eaba581224373dc5b0f319)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putS3Configuration")
    def put_s3_configuration(
        self,
        *,
        bucket_name: typing.Optional[builtins.str] = None,
        encryption_option: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        object_key_prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#bucket_name TimestreamwriteTable#bucket_name}.
        :param encryption_option: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#encryption_option TimestreamwriteTable#encryption_option}.
        :param kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#kms_key_id TimestreamwriteTable#kms_key_id}.
        :param object_key_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#object_key_prefix TimestreamwriteTable#object_key_prefix}.
        '''
        value = TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocationS3Configuration(
            bucket_name=bucket_name,
            encryption_option=encryption_option,
            kms_key_id=kms_key_id,
            object_key_prefix=object_key_prefix,
        )

        return typing.cast(None, jsii.invoke(self, "putS3Configuration", [value]))

    @jsii.member(jsii_name="resetS3Configuration")
    def reset_s3_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3Configuration", []))

    @builtins.property
    @jsii.member(jsii_name="s3Configuration")
    def s3_configuration(
        self,
    ) -> "TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocationS3ConfigurationOutputReference":
        return typing.cast("TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocationS3ConfigurationOutputReference", jsii.get(self, "s3Configuration"))

    @builtins.property
    @jsii.member(jsii_name="s3ConfigurationInput")
    def s3_configuration_input(
        self,
    ) -> typing.Optional["TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocationS3Configuration"]:
        return typing.cast(typing.Optional["TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocationS3Configuration"], jsii.get(self, "s3ConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocation]:
        return typing.cast(typing.Optional[TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocation], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocation],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a0d568c2619f1662e094463d1f4b3c0f17e82d632cc5cc003669749f6ae2130)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.timestreamwriteTable.TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocationS3Configuration",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_name": "bucketName",
        "encryption_option": "encryptionOption",
        "kms_key_id": "kmsKeyId",
        "object_key_prefix": "objectKeyPrefix",
    },
)
class TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocationS3Configuration:
    def __init__(
        self,
        *,
        bucket_name: typing.Optional[builtins.str] = None,
        encryption_option: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        object_key_prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#bucket_name TimestreamwriteTable#bucket_name}.
        :param encryption_option: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#encryption_option TimestreamwriteTable#encryption_option}.
        :param kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#kms_key_id TimestreamwriteTable#kms_key_id}.
        :param object_key_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#object_key_prefix TimestreamwriteTable#object_key_prefix}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77a879c35c3970a6493f3943db89fa1724c59a68aba169717f4c8f742951c70b)
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            check_type(argname="argument encryption_option", value=encryption_option, expected_type=type_hints["encryption_option"])
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            check_type(argname="argument object_key_prefix", value=object_key_prefix, expected_type=type_hints["object_key_prefix"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if bucket_name is not None:
            self._values["bucket_name"] = bucket_name
        if encryption_option is not None:
            self._values["encryption_option"] = encryption_option
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if object_key_prefix is not None:
            self._values["object_key_prefix"] = object_key_prefix

    @builtins.property
    def bucket_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#bucket_name TimestreamwriteTable#bucket_name}.'''
        result = self._values.get("bucket_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encryption_option(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#encryption_option TimestreamwriteTable#encryption_option}.'''
        result = self._values.get("encryption_option")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#kms_key_id TimestreamwriteTable#kms_key_id}.'''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def object_key_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#object_key_prefix TimestreamwriteTable#object_key_prefix}.'''
        result = self._values.get("object_key_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocationS3Configuration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocationS3ConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.timestreamwriteTable.TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocationS3ConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3bd224f0018e801c14e63df73d65fdd769b2bb86ac6d7df0241a9d34a50bcc2f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBucketName")
    def reset_bucket_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketName", []))

    @jsii.member(jsii_name="resetEncryptionOption")
    def reset_encryption_option(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncryptionOption", []))

    @jsii.member(jsii_name="resetKmsKeyId")
    def reset_kms_key_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKeyId", []))

    @jsii.member(jsii_name="resetObjectKeyPrefix")
    def reset_object_key_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetObjectKeyPrefix", []))

    @builtins.property
    @jsii.member(jsii_name="bucketNameInput")
    def bucket_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketNameInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptionOptionInput")
    def encryption_option_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "encryptionOptionInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyIdInput")
    def kms_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="objectKeyPrefixInput")
    def object_key_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectKeyPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketName")
    def bucket_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketName"))

    @bucket_name.setter
    def bucket_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77f7f075b5af2422bcd6ba6faa3da13082d8f67464f33e176877f216b65504e7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketName", value)

    @builtins.property
    @jsii.member(jsii_name="encryptionOption")
    def encryption_option(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "encryptionOption"))

    @encryption_option.setter
    def encryption_option(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8be481154a81ca5d19b5301cde66d091b0f7332826f422d408093f5fd026c71)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionOption", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b4463a6a253cd6f0d23ad31a9b5f8e4f681c00afd24e8b357f908c40864440b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="objectKeyPrefix")
    def object_key_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "objectKeyPrefix"))

    @object_key_prefix.setter
    def object_key_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09f8ff4d3dd9f9a7cd0e7979d743bb78f9e0ed726396208e227503b002549dd2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "objectKeyPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocationS3Configuration]:
        return typing.cast(typing.Optional[TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocationS3Configuration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocationS3Configuration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ab9d324c94b3245e27e5ebf079cadbc46794b707ba2d509d29f2d8d50824d27)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class TimestreamwriteTableMagneticStoreWritePropertiesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.timestreamwriteTable.TimestreamwriteTableMagneticStoreWritePropertiesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c129331130c18c10fdd26348cee8e289788cd23183b8899010acd3b654c4800a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMagneticStoreRejectedDataLocation")
    def put_magnetic_store_rejected_data_location(
        self,
        *,
        s3_configuration: typing.Optional[typing.Union[TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocationS3Configuration, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param s3_configuration: s3_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#s3_configuration TimestreamwriteTable#s3_configuration}
        '''
        value = TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocation(
            s3_configuration=s3_configuration
        )

        return typing.cast(None, jsii.invoke(self, "putMagneticStoreRejectedDataLocation", [value]))

    @jsii.member(jsii_name="resetEnableMagneticStoreWrites")
    def reset_enable_magnetic_store_writes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableMagneticStoreWrites", []))

    @jsii.member(jsii_name="resetMagneticStoreRejectedDataLocation")
    def reset_magnetic_store_rejected_data_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMagneticStoreRejectedDataLocation", []))

    @builtins.property
    @jsii.member(jsii_name="magneticStoreRejectedDataLocation")
    def magnetic_store_rejected_data_location(
        self,
    ) -> TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocationOutputReference:
        return typing.cast(TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocationOutputReference, jsii.get(self, "magneticStoreRejectedDataLocation"))

    @builtins.property
    @jsii.member(jsii_name="enableMagneticStoreWritesInput")
    def enable_magnetic_store_writes_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableMagneticStoreWritesInput"))

    @builtins.property
    @jsii.member(jsii_name="magneticStoreRejectedDataLocationInput")
    def magnetic_store_rejected_data_location_input(
        self,
    ) -> typing.Optional[TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocation]:
        return typing.cast(typing.Optional[TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocation], jsii.get(self, "magneticStoreRejectedDataLocationInput"))

    @builtins.property
    @jsii.member(jsii_name="enableMagneticStoreWrites")
    def enable_magnetic_store_writes(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enableMagneticStoreWrites"))

    @enable_magnetic_store_writes.setter
    def enable_magnetic_store_writes(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__235b8deefeaaba86e81dcaf1106c40d8dfdf1865da442d09b9cca8757cba8105)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableMagneticStoreWrites", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[TimestreamwriteTableMagneticStoreWriteProperties]:
        return typing.cast(typing.Optional[TimestreamwriteTableMagneticStoreWriteProperties], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[TimestreamwriteTableMagneticStoreWriteProperties],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a120a53a076c3f5f74a5dc4b2d22c73f862c4c4f265946f1b1790edef3beae23)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.timestreamwriteTable.TimestreamwriteTableRetentionProperties",
    jsii_struct_bases=[],
    name_mapping={
        "magnetic_store_retention_period_in_days": "magneticStoreRetentionPeriodInDays",
        "memory_store_retention_period_in_hours": "memoryStoreRetentionPeriodInHours",
    },
)
class TimestreamwriteTableRetentionProperties:
    def __init__(
        self,
        *,
        magnetic_store_retention_period_in_days: jsii.Number,
        memory_store_retention_period_in_hours: jsii.Number,
    ) -> None:
        '''
        :param magnetic_store_retention_period_in_days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#magnetic_store_retention_period_in_days TimestreamwriteTable#magnetic_store_retention_period_in_days}.
        :param memory_store_retention_period_in_hours: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#memory_store_retention_period_in_hours TimestreamwriteTable#memory_store_retention_period_in_hours}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52945b01e7d357b81199e80d04c5c826bccec170567d0630abe187113822cd6e)
            check_type(argname="argument magnetic_store_retention_period_in_days", value=magnetic_store_retention_period_in_days, expected_type=type_hints["magnetic_store_retention_period_in_days"])
            check_type(argname="argument memory_store_retention_period_in_hours", value=memory_store_retention_period_in_hours, expected_type=type_hints["memory_store_retention_period_in_hours"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "magnetic_store_retention_period_in_days": magnetic_store_retention_period_in_days,
            "memory_store_retention_period_in_hours": memory_store_retention_period_in_hours,
        }

    @builtins.property
    def magnetic_store_retention_period_in_days(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#magnetic_store_retention_period_in_days TimestreamwriteTable#magnetic_store_retention_period_in_days}.'''
        result = self._values.get("magnetic_store_retention_period_in_days")
        assert result is not None, "Required property 'magnetic_store_retention_period_in_days' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def memory_store_retention_period_in_hours(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#memory_store_retention_period_in_hours TimestreamwriteTable#memory_store_retention_period_in_hours}.'''
        result = self._values.get("memory_store_retention_period_in_hours")
        assert result is not None, "Required property 'memory_store_retention_period_in_hours' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TimestreamwriteTableRetentionProperties(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TimestreamwriteTableRetentionPropertiesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.timestreamwriteTable.TimestreamwriteTableRetentionPropertiesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b264563e23b18adf8d15a5e03d90e4a1f1b8fef568b5240556f9c9bdef4c5b86)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="magneticStoreRetentionPeriodInDaysInput")
    def magnetic_store_retention_period_in_days_input(
        self,
    ) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "magneticStoreRetentionPeriodInDaysInput"))

    @builtins.property
    @jsii.member(jsii_name="memoryStoreRetentionPeriodInHoursInput")
    def memory_store_retention_period_in_hours_input(
        self,
    ) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "memoryStoreRetentionPeriodInHoursInput"))

    @builtins.property
    @jsii.member(jsii_name="magneticStoreRetentionPeriodInDays")
    def magnetic_store_retention_period_in_days(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "magneticStoreRetentionPeriodInDays"))

    @magnetic_store_retention_period_in_days.setter
    def magnetic_store_retention_period_in_days(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dde80eec66c2fffdfa560a51a85205dd017f5f6202c1e7427e02eacdbe417b01)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "magneticStoreRetentionPeriodInDays", value)

    @builtins.property
    @jsii.member(jsii_name="memoryStoreRetentionPeriodInHours")
    def memory_store_retention_period_in_hours(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "memoryStoreRetentionPeriodInHours"))

    @memory_store_retention_period_in_hours.setter
    def memory_store_retention_period_in_hours(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__712a9ffb4a53f8b6066e3381623e9b80a6423b604fc1bee79ba6afcb89f47886)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memoryStoreRetentionPeriodInHours", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[TimestreamwriteTableRetentionProperties]:
        return typing.cast(typing.Optional[TimestreamwriteTableRetentionProperties], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[TimestreamwriteTableRetentionProperties],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76e8cd8201c14c8d64d47662eed211689229229fa8b9e73b4caddfad22d5f143)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "TimestreamwriteTable",
    "TimestreamwriteTableConfig",
    "TimestreamwriteTableMagneticStoreWriteProperties",
    "TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocation",
    "TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocationOutputReference",
    "TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocationS3Configuration",
    "TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocationS3ConfigurationOutputReference",
    "TimestreamwriteTableMagneticStoreWritePropertiesOutputReference",
    "TimestreamwriteTableRetentionProperties",
    "TimestreamwriteTableRetentionPropertiesOutputReference",
]

publication.publish()

def _typecheckingstub__e7575cb61f042c4d65198d8076a30dff566b020953d6188b988af8ad9616f14c(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    database_name: builtins.str,
    table_name: builtins.str,
    id: typing.Optional[builtins.str] = None,
    magnetic_store_write_properties: typing.Optional[typing.Union[TimestreamwriteTableMagneticStoreWriteProperties, typing.Dict[builtins.str, typing.Any]]] = None,
    retention_properties: typing.Optional[typing.Union[TimestreamwriteTableRetentionProperties, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__14fb13e3a0a356dec9d19b119f55a983419c44d917d1d94db70435a76c7f5fd7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b0ac12a02f69011e337dbaef093e874b4e57ee2bf80a10a2b875e277a07ba87(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__508b57fb94e42b6f1c7b15401f1b7dc190d8027a948ec6db6d4cafbe9b33110a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4424483bd32c6aeb34fda4e1356a79c0824261fecd48227e1779a58a5a1e69bc(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af0d7dc11d11778db372ba0ac467f4eb9f0479444cf6c33296866b37f9499254(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7369d7448a744f9fecc1c91c2151bf367d4112e0c541a533c56e60a8bee9f2e7(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    database_name: builtins.str,
    table_name: builtins.str,
    id: typing.Optional[builtins.str] = None,
    magnetic_store_write_properties: typing.Optional[typing.Union[TimestreamwriteTableMagneticStoreWriteProperties, typing.Dict[builtins.str, typing.Any]]] = None,
    retention_properties: typing.Optional[typing.Union[TimestreamwriteTableRetentionProperties, typing.Dict[builtins.str, typing.Any]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9742d87f0fb64eef3948ae3338e07380ed75f1b71eed804d75258b881f6a8ab(
    *,
    enable_magnetic_store_writes: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    magnetic_store_rejected_data_location: typing.Optional[typing.Union[TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocation, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1182ff1941e34ae8cf6617fc2fbe484ec6d483d8cfedaa5a3306beeee299a0cd(
    *,
    s3_configuration: typing.Optional[typing.Union[TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocationS3Configuration, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__edac81173e6252b7234f18b57eaed7bd9a52791a51eaba581224373dc5b0f319(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a0d568c2619f1662e094463d1f4b3c0f17e82d632cc5cc003669749f6ae2130(
    value: typing.Optional[TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocation],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77a879c35c3970a6493f3943db89fa1724c59a68aba169717f4c8f742951c70b(
    *,
    bucket_name: typing.Optional[builtins.str] = None,
    encryption_option: typing.Optional[builtins.str] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    object_key_prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3bd224f0018e801c14e63df73d65fdd769b2bb86ac6d7df0241a9d34a50bcc2f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77f7f075b5af2422bcd6ba6faa3da13082d8f67464f33e176877f216b65504e7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8be481154a81ca5d19b5301cde66d091b0f7332826f422d408093f5fd026c71(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b4463a6a253cd6f0d23ad31a9b5f8e4f681c00afd24e8b357f908c40864440b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09f8ff4d3dd9f9a7cd0e7979d743bb78f9e0ed726396208e227503b002549dd2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ab9d324c94b3245e27e5ebf079cadbc46794b707ba2d509d29f2d8d50824d27(
    value: typing.Optional[TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocationS3Configuration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c129331130c18c10fdd26348cee8e289788cd23183b8899010acd3b654c4800a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__235b8deefeaaba86e81dcaf1106c40d8dfdf1865da442d09b9cca8757cba8105(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a120a53a076c3f5f74a5dc4b2d22c73f862c4c4f265946f1b1790edef3beae23(
    value: typing.Optional[TimestreamwriteTableMagneticStoreWriteProperties],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52945b01e7d357b81199e80d04c5c826bccec170567d0630abe187113822cd6e(
    *,
    magnetic_store_retention_period_in_days: jsii.Number,
    memory_store_retention_period_in_hours: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b264563e23b18adf8d15a5e03d90e4a1f1b8fef568b5240556f9c9bdef4c5b86(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dde80eec66c2fffdfa560a51a85205dd017f5f6202c1e7427e02eacdbe417b01(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__712a9ffb4a53f8b6066e3381623e9b80a6423b604fc1bee79ba6afcb89f47886(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76e8cd8201c14c8d64d47662eed211689229229fa8b9e73b4caddfad22d5f143(
    value: typing.Optional[TimestreamwriteTableRetentionProperties],
) -> None:
    """Type checking stubs"""
    pass
