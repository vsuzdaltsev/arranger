'''
# `aws_glue_catalog_table`

Refer to the Terraform Registory for docs: [`aws_glue_catalog_table`](https://www.terraform.io/docs/providers/aws/r/glue_catalog_table).
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


class GlueCatalogTable(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.glueCatalogTable.GlueCatalogTable",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table aws_glue_catalog_table}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        database_name: builtins.str,
        name: builtins.str,
        catalog_id: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        owner: typing.Optional[builtins.str] = None,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        partition_index: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GlueCatalogTablePartitionIndex", typing.Dict[builtins.str, typing.Any]]]]] = None,
        partition_keys: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GlueCatalogTablePartitionKeys", typing.Dict[builtins.str, typing.Any]]]]] = None,
        retention: typing.Optional[jsii.Number] = None,
        storage_descriptor: typing.Optional[typing.Union["GlueCatalogTableStorageDescriptor", typing.Dict[builtins.str, typing.Any]]] = None,
        table_type: typing.Optional[builtins.str] = None,
        target_table: typing.Optional[typing.Union["GlueCatalogTableTargetTable", typing.Dict[builtins.str, typing.Any]]] = None,
        view_expanded_text: typing.Optional[builtins.str] = None,
        view_original_text: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table aws_glue_catalog_table} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param database_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#database_name GlueCatalogTable#database_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#name GlueCatalogTable#name}.
        :param catalog_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#catalog_id GlueCatalogTable#catalog_id}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#description GlueCatalogTable#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#id GlueCatalogTable#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param owner: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#owner GlueCatalogTable#owner}.
        :param parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#parameters GlueCatalogTable#parameters}.
        :param partition_index: partition_index block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#partition_index GlueCatalogTable#partition_index}
        :param partition_keys: partition_keys block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#partition_keys GlueCatalogTable#partition_keys}
        :param retention: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#retention GlueCatalogTable#retention}.
        :param storage_descriptor: storage_descriptor block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#storage_descriptor GlueCatalogTable#storage_descriptor}
        :param table_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#table_type GlueCatalogTable#table_type}.
        :param target_table: target_table block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#target_table GlueCatalogTable#target_table}
        :param view_expanded_text: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#view_expanded_text GlueCatalogTable#view_expanded_text}.
        :param view_original_text: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#view_original_text GlueCatalogTable#view_original_text}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a709fbfbc0ae96913d4062b940330f68ef6768a0e485d3e62a062a6bac0b17eb)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GlueCatalogTableConfig(
            database_name=database_name,
            name=name,
            catalog_id=catalog_id,
            description=description,
            id=id,
            owner=owner,
            parameters=parameters,
            partition_index=partition_index,
            partition_keys=partition_keys,
            retention=retention,
            storage_descriptor=storage_descriptor,
            table_type=table_type,
            target_table=target_table,
            view_expanded_text=view_expanded_text,
            view_original_text=view_original_text,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putPartitionIndex")
    def put_partition_index(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GlueCatalogTablePartitionIndex", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38faaa10398c4e2beda4679112f01927101d130f8a91afe13a5cc83715ea987c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPartitionIndex", [value]))

    @jsii.member(jsii_name="putPartitionKeys")
    def put_partition_keys(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GlueCatalogTablePartitionKeys", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc9beac348162d722ef8c98f14779ba41e183fd12d94625dc08c4dd53fd5204a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPartitionKeys", [value]))

    @jsii.member(jsii_name="putStorageDescriptor")
    def put_storage_descriptor(
        self,
        *,
        bucket_columns: typing.Optional[typing.Sequence[builtins.str]] = None,
        columns: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GlueCatalogTableStorageDescriptorColumns", typing.Dict[builtins.str, typing.Any]]]]] = None,
        compressed: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        input_format: typing.Optional[builtins.str] = None,
        location: typing.Optional[builtins.str] = None,
        number_of_buckets: typing.Optional[jsii.Number] = None,
        output_format: typing.Optional[builtins.str] = None,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        schema_reference: typing.Optional[typing.Union["GlueCatalogTableStorageDescriptorSchemaReference", typing.Dict[builtins.str, typing.Any]]] = None,
        ser_de_info: typing.Optional[typing.Union["GlueCatalogTableStorageDescriptorSerDeInfo", typing.Dict[builtins.str, typing.Any]]] = None,
        skewed_info: typing.Optional[typing.Union["GlueCatalogTableStorageDescriptorSkewedInfo", typing.Dict[builtins.str, typing.Any]]] = None,
        sort_columns: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GlueCatalogTableStorageDescriptorSortColumns", typing.Dict[builtins.str, typing.Any]]]]] = None,
        stored_as_sub_directories: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param bucket_columns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#bucket_columns GlueCatalogTable#bucket_columns}.
        :param columns: columns block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#columns GlueCatalogTable#columns}
        :param compressed: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#compressed GlueCatalogTable#compressed}.
        :param input_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#input_format GlueCatalogTable#input_format}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#location GlueCatalogTable#location}.
        :param number_of_buckets: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#number_of_buckets GlueCatalogTable#number_of_buckets}.
        :param output_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#output_format GlueCatalogTable#output_format}.
        :param parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#parameters GlueCatalogTable#parameters}.
        :param schema_reference: schema_reference block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#schema_reference GlueCatalogTable#schema_reference}
        :param ser_de_info: ser_de_info block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#ser_de_info GlueCatalogTable#ser_de_info}
        :param skewed_info: skewed_info block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#skewed_info GlueCatalogTable#skewed_info}
        :param sort_columns: sort_columns block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#sort_columns GlueCatalogTable#sort_columns}
        :param stored_as_sub_directories: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#stored_as_sub_directories GlueCatalogTable#stored_as_sub_directories}.
        '''
        value = GlueCatalogTableStorageDescriptor(
            bucket_columns=bucket_columns,
            columns=columns,
            compressed=compressed,
            input_format=input_format,
            location=location,
            number_of_buckets=number_of_buckets,
            output_format=output_format,
            parameters=parameters,
            schema_reference=schema_reference,
            ser_de_info=ser_de_info,
            skewed_info=skewed_info,
            sort_columns=sort_columns,
            stored_as_sub_directories=stored_as_sub_directories,
        )

        return typing.cast(None, jsii.invoke(self, "putStorageDescriptor", [value]))

    @jsii.member(jsii_name="putTargetTable")
    def put_target_table(
        self,
        *,
        catalog_id: builtins.str,
        database_name: builtins.str,
        name: builtins.str,
    ) -> None:
        '''
        :param catalog_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#catalog_id GlueCatalogTable#catalog_id}.
        :param database_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#database_name GlueCatalogTable#database_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#name GlueCatalogTable#name}.
        '''
        value = GlueCatalogTableTargetTable(
            catalog_id=catalog_id, database_name=database_name, name=name
        )

        return typing.cast(None, jsii.invoke(self, "putTargetTable", [value]))

    @jsii.member(jsii_name="resetCatalogId")
    def reset_catalog_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCatalogId", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetOwner")
    def reset_owner(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOwner", []))

    @jsii.member(jsii_name="resetParameters")
    def reset_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParameters", []))

    @jsii.member(jsii_name="resetPartitionIndex")
    def reset_partition_index(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPartitionIndex", []))

    @jsii.member(jsii_name="resetPartitionKeys")
    def reset_partition_keys(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPartitionKeys", []))

    @jsii.member(jsii_name="resetRetention")
    def reset_retention(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetention", []))

    @jsii.member(jsii_name="resetStorageDescriptor")
    def reset_storage_descriptor(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageDescriptor", []))

    @jsii.member(jsii_name="resetTableType")
    def reset_table_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTableType", []))

    @jsii.member(jsii_name="resetTargetTable")
    def reset_target_table(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetTable", []))

    @jsii.member(jsii_name="resetViewExpandedText")
    def reset_view_expanded_text(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetViewExpandedText", []))

    @jsii.member(jsii_name="resetViewOriginalText")
    def reset_view_original_text(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetViewOriginalText", []))

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
    @jsii.member(jsii_name="partitionIndex")
    def partition_index(self) -> "GlueCatalogTablePartitionIndexList":
        return typing.cast("GlueCatalogTablePartitionIndexList", jsii.get(self, "partitionIndex"))

    @builtins.property
    @jsii.member(jsii_name="partitionKeys")
    def partition_keys(self) -> "GlueCatalogTablePartitionKeysList":
        return typing.cast("GlueCatalogTablePartitionKeysList", jsii.get(self, "partitionKeys"))

    @builtins.property
    @jsii.member(jsii_name="storageDescriptor")
    def storage_descriptor(self) -> "GlueCatalogTableStorageDescriptorOutputReference":
        return typing.cast("GlueCatalogTableStorageDescriptorOutputReference", jsii.get(self, "storageDescriptor"))

    @builtins.property
    @jsii.member(jsii_name="targetTable")
    def target_table(self) -> "GlueCatalogTableTargetTableOutputReference":
        return typing.cast("GlueCatalogTableTargetTableOutputReference", jsii.get(self, "targetTable"))

    @builtins.property
    @jsii.member(jsii_name="catalogIdInput")
    def catalog_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "catalogIdInput"))

    @builtins.property
    @jsii.member(jsii_name="databaseNameInput")
    def database_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseNameInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="ownerInput")
    def owner_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ownerInput"))

    @builtins.property
    @jsii.member(jsii_name="parametersInput")
    def parameters_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "parametersInput"))

    @builtins.property
    @jsii.member(jsii_name="partitionIndexInput")
    def partition_index_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GlueCatalogTablePartitionIndex"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GlueCatalogTablePartitionIndex"]]], jsii.get(self, "partitionIndexInput"))

    @builtins.property
    @jsii.member(jsii_name="partitionKeysInput")
    def partition_keys_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GlueCatalogTablePartitionKeys"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GlueCatalogTablePartitionKeys"]]], jsii.get(self, "partitionKeysInput"))

    @builtins.property
    @jsii.member(jsii_name="retentionInput")
    def retention_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retentionInput"))

    @builtins.property
    @jsii.member(jsii_name="storageDescriptorInput")
    def storage_descriptor_input(
        self,
    ) -> typing.Optional["GlueCatalogTableStorageDescriptor"]:
        return typing.cast(typing.Optional["GlueCatalogTableStorageDescriptor"], jsii.get(self, "storageDescriptorInput"))

    @builtins.property
    @jsii.member(jsii_name="tableTypeInput")
    def table_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tableTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="targetTableInput")
    def target_table_input(self) -> typing.Optional["GlueCatalogTableTargetTable"]:
        return typing.cast(typing.Optional["GlueCatalogTableTargetTable"], jsii.get(self, "targetTableInput"))

    @builtins.property
    @jsii.member(jsii_name="viewExpandedTextInput")
    def view_expanded_text_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "viewExpandedTextInput"))

    @builtins.property
    @jsii.member(jsii_name="viewOriginalTextInput")
    def view_original_text_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "viewOriginalTextInput"))

    @builtins.property
    @jsii.member(jsii_name="catalogId")
    def catalog_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "catalogId"))

    @catalog_id.setter
    def catalog_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb37e2d527352ef4a2bc478cbf17cce96cd1159f134efab5459e34e465b89d3d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "catalogId", value)

    @builtins.property
    @jsii.member(jsii_name="databaseName")
    def database_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "databaseName"))

    @database_name.setter
    def database_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d76a606b8b2ff41fcc5f689dac5806ca11ef656f98afedf89ef2940fc8d1757f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "databaseName", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8dff6b848f4ee015dcbd7e1428fdd3f6040177115e52e068723340621e78682e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1e1c4f4b9c106b352f97ea6c17279fc295efe0c65fb10c056277f05c0b2f140)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ad5c6e3fa85feb6695acf77c7cfcd856731da64fd6fcc075c6b08f67d3e4eef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="owner")
    def owner(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "owner"))

    @owner.setter
    def owner(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a3efd212f3482317c04f134b27a07eee5f4d7ffa8227d81c0efdc3fdd147d59)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "owner", value)

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0298b83f0feae14a7c462aa753ab8d27ce817615f07f652ed0fbcaecb34a771f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameters", value)

    @builtins.property
    @jsii.member(jsii_name="retention")
    def retention(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "retention"))

    @retention.setter
    def retention(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56180aeee073853ab358595fe4dfc8788edd4a76e190e5947e69ecb8649ca417)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retention", value)

    @builtins.property
    @jsii.member(jsii_name="tableType")
    def table_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tableType"))

    @table_type.setter
    def table_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c27d4ab86a4eeac0e86ae0289d6a11ce9c0134d2f02b3aada6f10b6f7d67664d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tableType", value)

    @builtins.property
    @jsii.member(jsii_name="viewExpandedText")
    def view_expanded_text(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "viewExpandedText"))

    @view_expanded_text.setter
    def view_expanded_text(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cec4b2110e00d7d0b3874ab64c16719fb2ffdb9bfd6e5a725063ff109a771cc5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "viewExpandedText", value)

    @builtins.property
    @jsii.member(jsii_name="viewOriginalText")
    def view_original_text(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "viewOriginalText"))

    @view_original_text.setter
    def view_original_text(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca9076b26dd1cbcab3daea6a6d668aa9621ce0c6714ea9fb7f884c998acd9cda)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "viewOriginalText", value)


@jsii.data_type(
    jsii_type="aws.glueCatalogTable.GlueCatalogTableConfig",
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
        "name": "name",
        "catalog_id": "catalogId",
        "description": "description",
        "id": "id",
        "owner": "owner",
        "parameters": "parameters",
        "partition_index": "partitionIndex",
        "partition_keys": "partitionKeys",
        "retention": "retention",
        "storage_descriptor": "storageDescriptor",
        "table_type": "tableType",
        "target_table": "targetTable",
        "view_expanded_text": "viewExpandedText",
        "view_original_text": "viewOriginalText",
    },
)
class GlueCatalogTableConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        name: builtins.str,
        catalog_id: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        owner: typing.Optional[builtins.str] = None,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        partition_index: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GlueCatalogTablePartitionIndex", typing.Dict[builtins.str, typing.Any]]]]] = None,
        partition_keys: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GlueCatalogTablePartitionKeys", typing.Dict[builtins.str, typing.Any]]]]] = None,
        retention: typing.Optional[jsii.Number] = None,
        storage_descriptor: typing.Optional[typing.Union["GlueCatalogTableStorageDescriptor", typing.Dict[builtins.str, typing.Any]]] = None,
        table_type: typing.Optional[builtins.str] = None,
        target_table: typing.Optional[typing.Union["GlueCatalogTableTargetTable", typing.Dict[builtins.str, typing.Any]]] = None,
        view_expanded_text: typing.Optional[builtins.str] = None,
        view_original_text: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param database_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#database_name GlueCatalogTable#database_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#name GlueCatalogTable#name}.
        :param catalog_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#catalog_id GlueCatalogTable#catalog_id}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#description GlueCatalogTable#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#id GlueCatalogTable#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param owner: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#owner GlueCatalogTable#owner}.
        :param parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#parameters GlueCatalogTable#parameters}.
        :param partition_index: partition_index block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#partition_index GlueCatalogTable#partition_index}
        :param partition_keys: partition_keys block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#partition_keys GlueCatalogTable#partition_keys}
        :param retention: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#retention GlueCatalogTable#retention}.
        :param storage_descriptor: storage_descriptor block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#storage_descriptor GlueCatalogTable#storage_descriptor}
        :param table_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#table_type GlueCatalogTable#table_type}.
        :param target_table: target_table block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#target_table GlueCatalogTable#target_table}
        :param view_expanded_text: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#view_expanded_text GlueCatalogTable#view_expanded_text}.
        :param view_original_text: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#view_original_text GlueCatalogTable#view_original_text}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(storage_descriptor, dict):
            storage_descriptor = GlueCatalogTableStorageDescriptor(**storage_descriptor)
        if isinstance(target_table, dict):
            target_table = GlueCatalogTableTargetTable(**target_table)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a60b838237e9be7efc7a66a0b10f9da46d6b31ff60bd9dd37fcf59c90b1052f4)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument owner", value=owner, expected_type=type_hints["owner"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument partition_index", value=partition_index, expected_type=type_hints["partition_index"])
            check_type(argname="argument partition_keys", value=partition_keys, expected_type=type_hints["partition_keys"])
            check_type(argname="argument retention", value=retention, expected_type=type_hints["retention"])
            check_type(argname="argument storage_descriptor", value=storage_descriptor, expected_type=type_hints["storage_descriptor"])
            check_type(argname="argument table_type", value=table_type, expected_type=type_hints["table_type"])
            check_type(argname="argument target_table", value=target_table, expected_type=type_hints["target_table"])
            check_type(argname="argument view_expanded_text", value=view_expanded_text, expected_type=type_hints["view_expanded_text"])
            check_type(argname="argument view_original_text", value=view_original_text, expected_type=type_hints["view_original_text"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "database_name": database_name,
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
        if catalog_id is not None:
            self._values["catalog_id"] = catalog_id
        if description is not None:
            self._values["description"] = description
        if id is not None:
            self._values["id"] = id
        if owner is not None:
            self._values["owner"] = owner
        if parameters is not None:
            self._values["parameters"] = parameters
        if partition_index is not None:
            self._values["partition_index"] = partition_index
        if partition_keys is not None:
            self._values["partition_keys"] = partition_keys
        if retention is not None:
            self._values["retention"] = retention
        if storage_descriptor is not None:
            self._values["storage_descriptor"] = storage_descriptor
        if table_type is not None:
            self._values["table_type"] = table_type
        if target_table is not None:
            self._values["target_table"] = target_table
        if view_expanded_text is not None:
            self._values["view_expanded_text"] = view_expanded_text
        if view_original_text is not None:
            self._values["view_original_text"] = view_original_text

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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#database_name GlueCatalogTable#database_name}.'''
        result = self._values.get("database_name")
        assert result is not None, "Required property 'database_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#name GlueCatalogTable#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def catalog_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#catalog_id GlueCatalogTable#catalog_id}.'''
        result = self._values.get("catalog_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#description GlueCatalogTable#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#id GlueCatalogTable#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def owner(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#owner GlueCatalogTable#owner}.'''
        result = self._values.get("owner")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parameters(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#parameters GlueCatalogTable#parameters}.'''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def partition_index(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GlueCatalogTablePartitionIndex"]]]:
        '''partition_index block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#partition_index GlueCatalogTable#partition_index}
        '''
        result = self._values.get("partition_index")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GlueCatalogTablePartitionIndex"]]], result)

    @builtins.property
    def partition_keys(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GlueCatalogTablePartitionKeys"]]]:
        '''partition_keys block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#partition_keys GlueCatalogTable#partition_keys}
        '''
        result = self._values.get("partition_keys")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GlueCatalogTablePartitionKeys"]]], result)

    @builtins.property
    def retention(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#retention GlueCatalogTable#retention}.'''
        result = self._values.get("retention")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def storage_descriptor(
        self,
    ) -> typing.Optional["GlueCatalogTableStorageDescriptor"]:
        '''storage_descriptor block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#storage_descriptor GlueCatalogTable#storage_descriptor}
        '''
        result = self._values.get("storage_descriptor")
        return typing.cast(typing.Optional["GlueCatalogTableStorageDescriptor"], result)

    @builtins.property
    def table_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#table_type GlueCatalogTable#table_type}.'''
        result = self._values.get("table_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_table(self) -> typing.Optional["GlueCatalogTableTargetTable"]:
        '''target_table block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#target_table GlueCatalogTable#target_table}
        '''
        result = self._values.get("target_table")
        return typing.cast(typing.Optional["GlueCatalogTableTargetTable"], result)

    @builtins.property
    def view_expanded_text(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#view_expanded_text GlueCatalogTable#view_expanded_text}.'''
        result = self._values.get("view_expanded_text")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def view_original_text(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#view_original_text GlueCatalogTable#view_original_text}.'''
        result = self._values.get("view_original_text")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GlueCatalogTableConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.glueCatalogTable.GlueCatalogTablePartitionIndex",
    jsii_struct_bases=[],
    name_mapping={"index_name": "indexName", "keys": "keys"},
)
class GlueCatalogTablePartitionIndex:
    def __init__(
        self,
        *,
        index_name: builtins.str,
        keys: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param index_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#index_name GlueCatalogTable#index_name}.
        :param keys: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#keys GlueCatalogTable#keys}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03c8acf6e5e581fcce09bc2762f563ac7c925093b8de8a8cbbdbd5f7b32dbb83)
            check_type(argname="argument index_name", value=index_name, expected_type=type_hints["index_name"])
            check_type(argname="argument keys", value=keys, expected_type=type_hints["keys"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "index_name": index_name,
            "keys": keys,
        }

    @builtins.property
    def index_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#index_name GlueCatalogTable#index_name}.'''
        result = self._values.get("index_name")
        assert result is not None, "Required property 'index_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def keys(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#keys GlueCatalogTable#keys}.'''
        result = self._values.get("keys")
        assert result is not None, "Required property 'keys' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GlueCatalogTablePartitionIndex(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GlueCatalogTablePartitionIndexList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.glueCatalogTable.GlueCatalogTablePartitionIndexList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ee6593c1d3d4876b7f42514f3f7516d29b83997c2cb9cc34bb43ba4ab2d8fed0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GlueCatalogTablePartitionIndexOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6183ccfaa2083b3a15e2f17a89512498b3ccf53c61135bd04304bea12ec6b55)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GlueCatalogTablePartitionIndexOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc8494c5241a20d7adee24eea2f715f97846c7fb1952e62b17e307eef518cbaa)
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
            type_hints = typing.get_type_hints(_typecheckingstub__229af285ef442a7fabb99b7503daeab85a2be60a1ce39f0e67a13f4e2eb5d0c1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__63a55275a07efcb918e51805acf17dee7dc868bc1a3734321e14b0aaa87f49d6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GlueCatalogTablePartitionIndex]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GlueCatalogTablePartitionIndex]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GlueCatalogTablePartitionIndex]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc2df2fbda926a51c795face471c01ffd79ecfc780fee9b603b2203db1e49bd3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GlueCatalogTablePartitionIndexOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.glueCatalogTable.GlueCatalogTablePartitionIndexOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__862b6e9eeca88915aa2a398b88b8e0cd009721342e302a1c1cde8e4fa129dfb8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="indexStatus")
    def index_status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "indexStatus"))

    @builtins.property
    @jsii.member(jsii_name="indexNameInput")
    def index_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "indexNameInput"))

    @builtins.property
    @jsii.member(jsii_name="keysInput")
    def keys_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "keysInput"))

    @builtins.property
    @jsii.member(jsii_name="indexName")
    def index_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "indexName"))

    @index_name.setter
    def index_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d15a60f515e9ea3431bb0caeea2cf51f282b6e26c3ecd101f75cd45a027157c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "indexName", value)

    @builtins.property
    @jsii.member(jsii_name="keys")
    def keys(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "keys"))

    @keys.setter
    def keys(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c6924c80fe7818b37f66b805f116e97312226086e233c89b9af1e13db230e5d1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keys", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GlueCatalogTablePartitionIndex, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GlueCatalogTablePartitionIndex, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GlueCatalogTablePartitionIndex, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b066886539f8cb5ed308dd5079a42a1e7bbe7c84d67f6b6e16238f90c8afadb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.glueCatalogTable.GlueCatalogTablePartitionKeys",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "comment": "comment", "type": "type"},
)
class GlueCatalogTablePartitionKeys:
    def __init__(
        self,
        *,
        name: builtins.str,
        comment: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#name GlueCatalogTable#name}.
        :param comment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#comment GlueCatalogTable#comment}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#type GlueCatalogTable#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f0b3bcab84ae200bd4cdd98db03a4b1eb925c832a502a0ccbe4c9d38b28df6c)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if comment is not None:
            self._values["comment"] = comment
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#name GlueCatalogTable#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#comment GlueCatalogTable#comment}.'''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#type GlueCatalogTable#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GlueCatalogTablePartitionKeys(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GlueCatalogTablePartitionKeysList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.glueCatalogTable.GlueCatalogTablePartitionKeysList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4113ca280093b97dde0bfec52fe51118d5a69d8204a8eb4a0f44e558dcc0c6c3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "GlueCatalogTablePartitionKeysOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e769a4699e1554cedb6add6d869ebeb5d84d24330f26286dcf9562f93c58d0da)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GlueCatalogTablePartitionKeysOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6cf50726e97820615c001da4853ec1044284d3721f65a5df75d30e17129652b6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__63f77c106d1201f29ec8d7aeb857740a4f58c1a628aad9acba2b36cca43665c0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3d0611bf0838be91863c7a420a50584e79377f3dcd211b516e2efb85af47488a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GlueCatalogTablePartitionKeys]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GlueCatalogTablePartitionKeys]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GlueCatalogTablePartitionKeys]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7641637e74d5bfdf6e1677dfa85a329b4f356ae39b713e4ffaa24bd2434f82c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GlueCatalogTablePartitionKeysOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.glueCatalogTable.GlueCatalogTablePartitionKeysOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__35e36a2b598007e89ea6052f10ea04ce000fd95232d0b7e962938be1138ed7c3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetComment")
    def reset_comment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComment", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="commentInput")
    def comment_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "commentInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="comment")
    def comment(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "comment"))

    @comment.setter
    def comment(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be9bb0291b61b62b54ed7ab02942c1717b9f436145621c69412a8053bc532f67)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "comment", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b49f6e49c069c2104bd6855a06c233f7af4f0d63a19efe9bcc74125d5ebc68e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7f57c2e2259ace8061ffb3f79d6ef4e481627a27bec29aa975b57ddab85ff15)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GlueCatalogTablePartitionKeys, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GlueCatalogTablePartitionKeys, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GlueCatalogTablePartitionKeys, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9cc517909fb932ba4c6b11d8559e457f07a54bef3af2f5aa166629b283d82aaf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.glueCatalogTable.GlueCatalogTableStorageDescriptor",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_columns": "bucketColumns",
        "columns": "columns",
        "compressed": "compressed",
        "input_format": "inputFormat",
        "location": "location",
        "number_of_buckets": "numberOfBuckets",
        "output_format": "outputFormat",
        "parameters": "parameters",
        "schema_reference": "schemaReference",
        "ser_de_info": "serDeInfo",
        "skewed_info": "skewedInfo",
        "sort_columns": "sortColumns",
        "stored_as_sub_directories": "storedAsSubDirectories",
    },
)
class GlueCatalogTableStorageDescriptor:
    def __init__(
        self,
        *,
        bucket_columns: typing.Optional[typing.Sequence[builtins.str]] = None,
        columns: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GlueCatalogTableStorageDescriptorColumns", typing.Dict[builtins.str, typing.Any]]]]] = None,
        compressed: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        input_format: typing.Optional[builtins.str] = None,
        location: typing.Optional[builtins.str] = None,
        number_of_buckets: typing.Optional[jsii.Number] = None,
        output_format: typing.Optional[builtins.str] = None,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        schema_reference: typing.Optional[typing.Union["GlueCatalogTableStorageDescriptorSchemaReference", typing.Dict[builtins.str, typing.Any]]] = None,
        ser_de_info: typing.Optional[typing.Union["GlueCatalogTableStorageDescriptorSerDeInfo", typing.Dict[builtins.str, typing.Any]]] = None,
        skewed_info: typing.Optional[typing.Union["GlueCatalogTableStorageDescriptorSkewedInfo", typing.Dict[builtins.str, typing.Any]]] = None,
        sort_columns: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GlueCatalogTableStorageDescriptorSortColumns", typing.Dict[builtins.str, typing.Any]]]]] = None,
        stored_as_sub_directories: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param bucket_columns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#bucket_columns GlueCatalogTable#bucket_columns}.
        :param columns: columns block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#columns GlueCatalogTable#columns}
        :param compressed: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#compressed GlueCatalogTable#compressed}.
        :param input_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#input_format GlueCatalogTable#input_format}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#location GlueCatalogTable#location}.
        :param number_of_buckets: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#number_of_buckets GlueCatalogTable#number_of_buckets}.
        :param output_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#output_format GlueCatalogTable#output_format}.
        :param parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#parameters GlueCatalogTable#parameters}.
        :param schema_reference: schema_reference block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#schema_reference GlueCatalogTable#schema_reference}
        :param ser_de_info: ser_de_info block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#ser_de_info GlueCatalogTable#ser_de_info}
        :param skewed_info: skewed_info block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#skewed_info GlueCatalogTable#skewed_info}
        :param sort_columns: sort_columns block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#sort_columns GlueCatalogTable#sort_columns}
        :param stored_as_sub_directories: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#stored_as_sub_directories GlueCatalogTable#stored_as_sub_directories}.
        '''
        if isinstance(schema_reference, dict):
            schema_reference = GlueCatalogTableStorageDescriptorSchemaReference(**schema_reference)
        if isinstance(ser_de_info, dict):
            ser_de_info = GlueCatalogTableStorageDescriptorSerDeInfo(**ser_de_info)
        if isinstance(skewed_info, dict):
            skewed_info = GlueCatalogTableStorageDescriptorSkewedInfo(**skewed_info)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__afa97fed3a1a402a8e8e34167062c83e2db0eb305fb34356688f23998d5019eb)
            check_type(argname="argument bucket_columns", value=bucket_columns, expected_type=type_hints["bucket_columns"])
            check_type(argname="argument columns", value=columns, expected_type=type_hints["columns"])
            check_type(argname="argument compressed", value=compressed, expected_type=type_hints["compressed"])
            check_type(argname="argument input_format", value=input_format, expected_type=type_hints["input_format"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument number_of_buckets", value=number_of_buckets, expected_type=type_hints["number_of_buckets"])
            check_type(argname="argument output_format", value=output_format, expected_type=type_hints["output_format"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument schema_reference", value=schema_reference, expected_type=type_hints["schema_reference"])
            check_type(argname="argument ser_de_info", value=ser_de_info, expected_type=type_hints["ser_de_info"])
            check_type(argname="argument skewed_info", value=skewed_info, expected_type=type_hints["skewed_info"])
            check_type(argname="argument sort_columns", value=sort_columns, expected_type=type_hints["sort_columns"])
            check_type(argname="argument stored_as_sub_directories", value=stored_as_sub_directories, expected_type=type_hints["stored_as_sub_directories"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if bucket_columns is not None:
            self._values["bucket_columns"] = bucket_columns
        if columns is not None:
            self._values["columns"] = columns
        if compressed is not None:
            self._values["compressed"] = compressed
        if input_format is not None:
            self._values["input_format"] = input_format
        if location is not None:
            self._values["location"] = location
        if number_of_buckets is not None:
            self._values["number_of_buckets"] = number_of_buckets
        if output_format is not None:
            self._values["output_format"] = output_format
        if parameters is not None:
            self._values["parameters"] = parameters
        if schema_reference is not None:
            self._values["schema_reference"] = schema_reference
        if ser_de_info is not None:
            self._values["ser_de_info"] = ser_de_info
        if skewed_info is not None:
            self._values["skewed_info"] = skewed_info
        if sort_columns is not None:
            self._values["sort_columns"] = sort_columns
        if stored_as_sub_directories is not None:
            self._values["stored_as_sub_directories"] = stored_as_sub_directories

    @builtins.property
    def bucket_columns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#bucket_columns GlueCatalogTable#bucket_columns}.'''
        result = self._values.get("bucket_columns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def columns(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GlueCatalogTableStorageDescriptorColumns"]]]:
        '''columns block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#columns GlueCatalogTable#columns}
        '''
        result = self._values.get("columns")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GlueCatalogTableStorageDescriptorColumns"]]], result)

    @builtins.property
    def compressed(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#compressed GlueCatalogTable#compressed}.'''
        result = self._values.get("compressed")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def input_format(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#input_format GlueCatalogTable#input_format}.'''
        result = self._values.get("input_format")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def location(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#location GlueCatalogTable#location}.'''
        result = self._values.get("location")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def number_of_buckets(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#number_of_buckets GlueCatalogTable#number_of_buckets}.'''
        result = self._values.get("number_of_buckets")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def output_format(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#output_format GlueCatalogTable#output_format}.'''
        result = self._values.get("output_format")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parameters(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#parameters GlueCatalogTable#parameters}.'''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def schema_reference(
        self,
    ) -> typing.Optional["GlueCatalogTableStorageDescriptorSchemaReference"]:
        '''schema_reference block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#schema_reference GlueCatalogTable#schema_reference}
        '''
        result = self._values.get("schema_reference")
        return typing.cast(typing.Optional["GlueCatalogTableStorageDescriptorSchemaReference"], result)

    @builtins.property
    def ser_de_info(
        self,
    ) -> typing.Optional["GlueCatalogTableStorageDescriptorSerDeInfo"]:
        '''ser_de_info block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#ser_de_info GlueCatalogTable#ser_de_info}
        '''
        result = self._values.get("ser_de_info")
        return typing.cast(typing.Optional["GlueCatalogTableStorageDescriptorSerDeInfo"], result)

    @builtins.property
    def skewed_info(
        self,
    ) -> typing.Optional["GlueCatalogTableStorageDescriptorSkewedInfo"]:
        '''skewed_info block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#skewed_info GlueCatalogTable#skewed_info}
        '''
        result = self._values.get("skewed_info")
        return typing.cast(typing.Optional["GlueCatalogTableStorageDescriptorSkewedInfo"], result)

    @builtins.property
    def sort_columns(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GlueCatalogTableStorageDescriptorSortColumns"]]]:
        '''sort_columns block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#sort_columns GlueCatalogTable#sort_columns}
        '''
        result = self._values.get("sort_columns")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GlueCatalogTableStorageDescriptorSortColumns"]]], result)

    @builtins.property
    def stored_as_sub_directories(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#stored_as_sub_directories GlueCatalogTable#stored_as_sub_directories}.'''
        result = self._values.get("stored_as_sub_directories")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GlueCatalogTableStorageDescriptor(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.glueCatalogTable.GlueCatalogTableStorageDescriptorColumns",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "comment": "comment",
        "parameters": "parameters",
        "type": "type",
    },
)
class GlueCatalogTableStorageDescriptorColumns:
    def __init__(
        self,
        *,
        name: builtins.str,
        comment: typing.Optional[builtins.str] = None,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#name GlueCatalogTable#name}.
        :param comment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#comment GlueCatalogTable#comment}.
        :param parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#parameters GlueCatalogTable#parameters}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#type GlueCatalogTable#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f777b3baf40f731f04b0d54c6fc540ee3078100c5fa5a4ae97ae1ff99ce79bf)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if comment is not None:
            self._values["comment"] = comment
        if parameters is not None:
            self._values["parameters"] = parameters
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#name GlueCatalogTable#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#comment GlueCatalogTable#comment}.'''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parameters(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#parameters GlueCatalogTable#parameters}.'''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#type GlueCatalogTable#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GlueCatalogTableStorageDescriptorColumns(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GlueCatalogTableStorageDescriptorColumnsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.glueCatalogTable.GlueCatalogTableStorageDescriptorColumnsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9eb035a22afea7128a34cd9a90a2bf6d9cce432843cd34dbbd9356f759ab32d8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GlueCatalogTableStorageDescriptorColumnsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b9a1dfd64b0bb894a258d60a1192109728ecb87d58a0530fa628ff1d1112f388)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GlueCatalogTableStorageDescriptorColumnsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b83bcd059bfd8d4687c2b279deafe6c6617acae450140742c1370d0ad2cda2a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0d74a7f2a08d2a8c9edba1b549e1e845b1affd79d01f13eea8c83bae090ee0ee)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ee56fecc14e189c17219cb2962c3c89b5246d332363064eb363600b39add98f4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GlueCatalogTableStorageDescriptorColumns]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GlueCatalogTableStorageDescriptorColumns]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GlueCatalogTableStorageDescriptorColumns]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ef55cff43ac821f64006b6b6887ac1332e8dd64fd21259199e5106c54adaaf8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GlueCatalogTableStorageDescriptorColumnsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.glueCatalogTable.GlueCatalogTableStorageDescriptorColumnsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4ff1f8f275c7f1ebde504a73274d9780037cf33ecd18b4edaa4bc95cb9752624)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetComment")
    def reset_comment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComment", []))

    @jsii.member(jsii_name="resetParameters")
    def reset_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParameters", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="commentInput")
    def comment_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "commentInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="parametersInput")
    def parameters_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "parametersInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="comment")
    def comment(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "comment"))

    @comment.setter
    def comment(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d39442be907bb143c5c78ec78a02ae517f4dc4ef6400f44dd0a85718cbe8202)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "comment", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1f8b0e05b63c6dd377dbb8217e44440f5a3b51f50f7f644ddc68395e2f3119c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff601f95a434e09da10b39b0421d7760ab2885a551acf41479a8a9dd27e8b480)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameters", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b76b59b3331e084eb6c689a16f4980704cdc1d619a18a9433f24dc1ae07f7b3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GlueCatalogTableStorageDescriptorColumns, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GlueCatalogTableStorageDescriptorColumns, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GlueCatalogTableStorageDescriptorColumns, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef2c3e96396d495e4c938532b4a3b4c6bd414d2a7cffd59b3abe0cda1fce0ecd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GlueCatalogTableStorageDescriptorOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.glueCatalogTable.GlueCatalogTableStorageDescriptorOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7cb1f7c0d809cedc2251ec6894bd44235edbd6de5d520abe1666b8e156a67cac)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putColumns")
    def put_columns(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GlueCatalogTableStorageDescriptorColumns, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35d412b346bca35af81a392f2e170838fc83a68bc72017b190afd1ee4e8bfeaa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putColumns", [value]))

    @jsii.member(jsii_name="putSchemaReference")
    def put_schema_reference(
        self,
        *,
        schema_version_number: jsii.Number,
        schema_id: typing.Optional[typing.Union["GlueCatalogTableStorageDescriptorSchemaReferenceSchemaId", typing.Dict[builtins.str, typing.Any]]] = None,
        schema_version_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param schema_version_number: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#schema_version_number GlueCatalogTable#schema_version_number}.
        :param schema_id: schema_id block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#schema_id GlueCatalogTable#schema_id}
        :param schema_version_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#schema_version_id GlueCatalogTable#schema_version_id}.
        '''
        value = GlueCatalogTableStorageDescriptorSchemaReference(
            schema_version_number=schema_version_number,
            schema_id=schema_id,
            schema_version_id=schema_version_id,
        )

        return typing.cast(None, jsii.invoke(self, "putSchemaReference", [value]))

    @jsii.member(jsii_name="putSerDeInfo")
    def put_ser_de_info(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        serialization_library: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#name GlueCatalogTable#name}.
        :param parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#parameters GlueCatalogTable#parameters}.
        :param serialization_library: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#serialization_library GlueCatalogTable#serialization_library}.
        '''
        value = GlueCatalogTableStorageDescriptorSerDeInfo(
            name=name,
            parameters=parameters,
            serialization_library=serialization_library,
        )

        return typing.cast(None, jsii.invoke(self, "putSerDeInfo", [value]))

    @jsii.member(jsii_name="putSkewedInfo")
    def put_skewed_info(
        self,
        *,
        skewed_column_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        skewed_column_value_location_maps: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        skewed_column_values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param skewed_column_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#skewed_column_names GlueCatalogTable#skewed_column_names}.
        :param skewed_column_value_location_maps: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#skewed_column_value_location_maps GlueCatalogTable#skewed_column_value_location_maps}.
        :param skewed_column_values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#skewed_column_values GlueCatalogTable#skewed_column_values}.
        '''
        value = GlueCatalogTableStorageDescriptorSkewedInfo(
            skewed_column_names=skewed_column_names,
            skewed_column_value_location_maps=skewed_column_value_location_maps,
            skewed_column_values=skewed_column_values,
        )

        return typing.cast(None, jsii.invoke(self, "putSkewedInfo", [value]))

    @jsii.member(jsii_name="putSortColumns")
    def put_sort_columns(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GlueCatalogTableStorageDescriptorSortColumns", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fbad93cc4a1643d1980568aa7076ff9db8658481e16cf4e1ff02e4100c77ee3b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSortColumns", [value]))

    @jsii.member(jsii_name="resetBucketColumns")
    def reset_bucket_columns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketColumns", []))

    @jsii.member(jsii_name="resetColumns")
    def reset_columns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetColumns", []))

    @jsii.member(jsii_name="resetCompressed")
    def reset_compressed(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCompressed", []))

    @jsii.member(jsii_name="resetInputFormat")
    def reset_input_format(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInputFormat", []))

    @jsii.member(jsii_name="resetLocation")
    def reset_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocation", []))

    @jsii.member(jsii_name="resetNumberOfBuckets")
    def reset_number_of_buckets(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNumberOfBuckets", []))

    @jsii.member(jsii_name="resetOutputFormat")
    def reset_output_format(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOutputFormat", []))

    @jsii.member(jsii_name="resetParameters")
    def reset_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParameters", []))

    @jsii.member(jsii_name="resetSchemaReference")
    def reset_schema_reference(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSchemaReference", []))

    @jsii.member(jsii_name="resetSerDeInfo")
    def reset_ser_de_info(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSerDeInfo", []))

    @jsii.member(jsii_name="resetSkewedInfo")
    def reset_skewed_info(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSkewedInfo", []))

    @jsii.member(jsii_name="resetSortColumns")
    def reset_sort_columns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSortColumns", []))

    @jsii.member(jsii_name="resetStoredAsSubDirectories")
    def reset_stored_as_sub_directories(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStoredAsSubDirectories", []))

    @builtins.property
    @jsii.member(jsii_name="columns")
    def columns(self) -> GlueCatalogTableStorageDescriptorColumnsList:
        return typing.cast(GlueCatalogTableStorageDescriptorColumnsList, jsii.get(self, "columns"))

    @builtins.property
    @jsii.member(jsii_name="schemaReference")
    def schema_reference(
        self,
    ) -> "GlueCatalogTableStorageDescriptorSchemaReferenceOutputReference":
        return typing.cast("GlueCatalogTableStorageDescriptorSchemaReferenceOutputReference", jsii.get(self, "schemaReference"))

    @builtins.property
    @jsii.member(jsii_name="serDeInfo")
    def ser_de_info(
        self,
    ) -> "GlueCatalogTableStorageDescriptorSerDeInfoOutputReference":
        return typing.cast("GlueCatalogTableStorageDescriptorSerDeInfoOutputReference", jsii.get(self, "serDeInfo"))

    @builtins.property
    @jsii.member(jsii_name="skewedInfo")
    def skewed_info(
        self,
    ) -> "GlueCatalogTableStorageDescriptorSkewedInfoOutputReference":
        return typing.cast("GlueCatalogTableStorageDescriptorSkewedInfoOutputReference", jsii.get(self, "skewedInfo"))

    @builtins.property
    @jsii.member(jsii_name="sortColumns")
    def sort_columns(self) -> "GlueCatalogTableStorageDescriptorSortColumnsList":
        return typing.cast("GlueCatalogTableStorageDescriptorSortColumnsList", jsii.get(self, "sortColumns"))

    @builtins.property
    @jsii.member(jsii_name="bucketColumnsInput")
    def bucket_columns_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "bucketColumnsInput"))

    @builtins.property
    @jsii.member(jsii_name="columnsInput")
    def columns_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GlueCatalogTableStorageDescriptorColumns]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GlueCatalogTableStorageDescriptorColumns]]], jsii.get(self, "columnsInput"))

    @builtins.property
    @jsii.member(jsii_name="compressedInput")
    def compressed_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "compressedInput"))

    @builtins.property
    @jsii.member(jsii_name="inputFormatInput")
    def input_format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "inputFormatInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="numberOfBucketsInput")
    def number_of_buckets_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "numberOfBucketsInput"))

    @builtins.property
    @jsii.member(jsii_name="outputFormatInput")
    def output_format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "outputFormatInput"))

    @builtins.property
    @jsii.member(jsii_name="parametersInput")
    def parameters_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "parametersInput"))

    @builtins.property
    @jsii.member(jsii_name="schemaReferenceInput")
    def schema_reference_input(
        self,
    ) -> typing.Optional["GlueCatalogTableStorageDescriptorSchemaReference"]:
        return typing.cast(typing.Optional["GlueCatalogTableStorageDescriptorSchemaReference"], jsii.get(self, "schemaReferenceInput"))

    @builtins.property
    @jsii.member(jsii_name="serDeInfoInput")
    def ser_de_info_input(
        self,
    ) -> typing.Optional["GlueCatalogTableStorageDescriptorSerDeInfo"]:
        return typing.cast(typing.Optional["GlueCatalogTableStorageDescriptorSerDeInfo"], jsii.get(self, "serDeInfoInput"))

    @builtins.property
    @jsii.member(jsii_name="skewedInfoInput")
    def skewed_info_input(
        self,
    ) -> typing.Optional["GlueCatalogTableStorageDescriptorSkewedInfo"]:
        return typing.cast(typing.Optional["GlueCatalogTableStorageDescriptorSkewedInfo"], jsii.get(self, "skewedInfoInput"))

    @builtins.property
    @jsii.member(jsii_name="sortColumnsInput")
    def sort_columns_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GlueCatalogTableStorageDescriptorSortColumns"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GlueCatalogTableStorageDescriptorSortColumns"]]], jsii.get(self, "sortColumnsInput"))

    @builtins.property
    @jsii.member(jsii_name="storedAsSubDirectoriesInput")
    def stored_as_sub_directories_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "storedAsSubDirectoriesInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketColumns")
    def bucket_columns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "bucketColumns"))

    @bucket_columns.setter
    def bucket_columns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e93d8c619581893f8c1a41593426e2acd190ee95b4f3fd8c98e96bdc7fbb81c7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketColumns", value)

    @builtins.property
    @jsii.member(jsii_name="compressed")
    def compressed(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "compressed"))

    @compressed.setter
    def compressed(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc4db4802465cf9518002cf08d42e936416d6fce0847d23eec0ef3fb108ba1b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "compressed", value)

    @builtins.property
    @jsii.member(jsii_name="inputFormat")
    def input_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "inputFormat"))

    @input_format.setter
    def input_format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b904ca36f410ce8296cb872101d8ce8498a9140d33dbb64397e23cceec1aff9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "inputFormat", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84ea4ff96761ba4017060c5e5db50cf7d3021b45e50e9ea50098a96fd8c21f1e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="numberOfBuckets")
    def number_of_buckets(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "numberOfBuckets"))

    @number_of_buckets.setter
    def number_of_buckets(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__65b8f83414a2105efb4a04379e309b19a7931a8d7942f5a3f199b04dfaf6b3d6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "numberOfBuckets", value)

    @builtins.property
    @jsii.member(jsii_name="outputFormat")
    def output_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "outputFormat"))

    @output_format.setter
    def output_format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0fd596e5a64f40f1a887014392509831353ddbc0452a662f207b9bf65705a7b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "outputFormat", value)

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5194542811fc8242346cb167f417681407c1f0021ee56c4768cf2b2eee9624da)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameters", value)

    @builtins.property
    @jsii.member(jsii_name="storedAsSubDirectories")
    def stored_as_sub_directories(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "storedAsSubDirectories"))

    @stored_as_sub_directories.setter
    def stored_as_sub_directories(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__977e8c7b2faf9e7b2b621d40694eca54c5bf63b3b732fbd0194d958ae72e8077)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storedAsSubDirectories", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GlueCatalogTableStorageDescriptor]:
        return typing.cast(typing.Optional[GlueCatalogTableStorageDescriptor], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GlueCatalogTableStorageDescriptor],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b947ce15571cc7d4c2adb09fb0e3def9b705415c79e31d59aad1ccfd4326be4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.glueCatalogTable.GlueCatalogTableStorageDescriptorSchemaReference",
    jsii_struct_bases=[],
    name_mapping={
        "schema_version_number": "schemaVersionNumber",
        "schema_id": "schemaId",
        "schema_version_id": "schemaVersionId",
    },
)
class GlueCatalogTableStorageDescriptorSchemaReference:
    def __init__(
        self,
        *,
        schema_version_number: jsii.Number,
        schema_id: typing.Optional[typing.Union["GlueCatalogTableStorageDescriptorSchemaReferenceSchemaId", typing.Dict[builtins.str, typing.Any]]] = None,
        schema_version_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param schema_version_number: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#schema_version_number GlueCatalogTable#schema_version_number}.
        :param schema_id: schema_id block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#schema_id GlueCatalogTable#schema_id}
        :param schema_version_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#schema_version_id GlueCatalogTable#schema_version_id}.
        '''
        if isinstance(schema_id, dict):
            schema_id = GlueCatalogTableStorageDescriptorSchemaReferenceSchemaId(**schema_id)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f042da52312d9eef478a5efb94a999846228838e2f00ec49b7d674795fd03197)
            check_type(argname="argument schema_version_number", value=schema_version_number, expected_type=type_hints["schema_version_number"])
            check_type(argname="argument schema_id", value=schema_id, expected_type=type_hints["schema_id"])
            check_type(argname="argument schema_version_id", value=schema_version_id, expected_type=type_hints["schema_version_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "schema_version_number": schema_version_number,
        }
        if schema_id is not None:
            self._values["schema_id"] = schema_id
        if schema_version_id is not None:
            self._values["schema_version_id"] = schema_version_id

    @builtins.property
    def schema_version_number(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#schema_version_number GlueCatalogTable#schema_version_number}.'''
        result = self._values.get("schema_version_number")
        assert result is not None, "Required property 'schema_version_number' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def schema_id(
        self,
    ) -> typing.Optional["GlueCatalogTableStorageDescriptorSchemaReferenceSchemaId"]:
        '''schema_id block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#schema_id GlueCatalogTable#schema_id}
        '''
        result = self._values.get("schema_id")
        return typing.cast(typing.Optional["GlueCatalogTableStorageDescriptorSchemaReferenceSchemaId"], result)

    @builtins.property
    def schema_version_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#schema_version_id GlueCatalogTable#schema_version_id}.'''
        result = self._values.get("schema_version_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GlueCatalogTableStorageDescriptorSchemaReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GlueCatalogTableStorageDescriptorSchemaReferenceOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.glueCatalogTable.GlueCatalogTableStorageDescriptorSchemaReferenceOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4a01dd009b9cdfd8020e0fd5e96f91c3ba2b255fb86007be0cae61537ca1dbe6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putSchemaId")
    def put_schema_id(
        self,
        *,
        registry_name: typing.Optional[builtins.str] = None,
        schema_arn: typing.Optional[builtins.str] = None,
        schema_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param registry_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#registry_name GlueCatalogTable#registry_name}.
        :param schema_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#schema_arn GlueCatalogTable#schema_arn}.
        :param schema_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#schema_name GlueCatalogTable#schema_name}.
        '''
        value = GlueCatalogTableStorageDescriptorSchemaReferenceSchemaId(
            registry_name=registry_name, schema_arn=schema_arn, schema_name=schema_name
        )

        return typing.cast(None, jsii.invoke(self, "putSchemaId", [value]))

    @jsii.member(jsii_name="resetSchemaId")
    def reset_schema_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSchemaId", []))

    @jsii.member(jsii_name="resetSchemaVersionId")
    def reset_schema_version_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSchemaVersionId", []))

    @builtins.property
    @jsii.member(jsii_name="schemaId")
    def schema_id(
        self,
    ) -> "GlueCatalogTableStorageDescriptorSchemaReferenceSchemaIdOutputReference":
        return typing.cast("GlueCatalogTableStorageDescriptorSchemaReferenceSchemaIdOutputReference", jsii.get(self, "schemaId"))

    @builtins.property
    @jsii.member(jsii_name="schemaIdInput")
    def schema_id_input(
        self,
    ) -> typing.Optional["GlueCatalogTableStorageDescriptorSchemaReferenceSchemaId"]:
        return typing.cast(typing.Optional["GlueCatalogTableStorageDescriptorSchemaReferenceSchemaId"], jsii.get(self, "schemaIdInput"))

    @builtins.property
    @jsii.member(jsii_name="schemaVersionIdInput")
    def schema_version_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "schemaVersionIdInput"))

    @builtins.property
    @jsii.member(jsii_name="schemaVersionNumberInput")
    def schema_version_number_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "schemaVersionNumberInput"))

    @builtins.property
    @jsii.member(jsii_name="schemaVersionId")
    def schema_version_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "schemaVersionId"))

    @schema_version_id.setter
    def schema_version_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b452ff2e7c60c3b217c05cb12a4301f9ff0876d7a902212684200c5a0b19397)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schemaVersionId", value)

    @builtins.property
    @jsii.member(jsii_name="schemaVersionNumber")
    def schema_version_number(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "schemaVersionNumber"))

    @schema_version_number.setter
    def schema_version_number(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14758d5f13922773b1f71958f727573c729ec6c898cac65e2ad7e542867f10e1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schemaVersionNumber", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GlueCatalogTableStorageDescriptorSchemaReference]:
        return typing.cast(typing.Optional[GlueCatalogTableStorageDescriptorSchemaReference], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GlueCatalogTableStorageDescriptorSchemaReference],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2508e6f37e66072d5c845e882f4d72b5ce80f28df1289957039eb728774efe8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.glueCatalogTable.GlueCatalogTableStorageDescriptorSchemaReferenceSchemaId",
    jsii_struct_bases=[],
    name_mapping={
        "registry_name": "registryName",
        "schema_arn": "schemaArn",
        "schema_name": "schemaName",
    },
)
class GlueCatalogTableStorageDescriptorSchemaReferenceSchemaId:
    def __init__(
        self,
        *,
        registry_name: typing.Optional[builtins.str] = None,
        schema_arn: typing.Optional[builtins.str] = None,
        schema_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param registry_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#registry_name GlueCatalogTable#registry_name}.
        :param schema_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#schema_arn GlueCatalogTable#schema_arn}.
        :param schema_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#schema_name GlueCatalogTable#schema_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25c8d3e8f4f5f811d22156562bb4eb9617a089e4079b496b3f2db59f1b07a177)
            check_type(argname="argument registry_name", value=registry_name, expected_type=type_hints["registry_name"])
            check_type(argname="argument schema_arn", value=schema_arn, expected_type=type_hints["schema_arn"])
            check_type(argname="argument schema_name", value=schema_name, expected_type=type_hints["schema_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if registry_name is not None:
            self._values["registry_name"] = registry_name
        if schema_arn is not None:
            self._values["schema_arn"] = schema_arn
        if schema_name is not None:
            self._values["schema_name"] = schema_name

    @builtins.property
    def registry_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#registry_name GlueCatalogTable#registry_name}.'''
        result = self._values.get("registry_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def schema_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#schema_arn GlueCatalogTable#schema_arn}.'''
        result = self._values.get("schema_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def schema_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#schema_name GlueCatalogTable#schema_name}.'''
        result = self._values.get("schema_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GlueCatalogTableStorageDescriptorSchemaReferenceSchemaId(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GlueCatalogTableStorageDescriptorSchemaReferenceSchemaIdOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.glueCatalogTable.GlueCatalogTableStorageDescriptorSchemaReferenceSchemaIdOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b1794f9a68825a5a2c0907ab9c90952a4cdbde238a1a83f9f33fd5dad016a1a4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetRegistryName")
    def reset_registry_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegistryName", []))

    @jsii.member(jsii_name="resetSchemaArn")
    def reset_schema_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSchemaArn", []))

    @jsii.member(jsii_name="resetSchemaName")
    def reset_schema_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSchemaName", []))

    @builtins.property
    @jsii.member(jsii_name="registryNameInput")
    def registry_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "registryNameInput"))

    @builtins.property
    @jsii.member(jsii_name="schemaArnInput")
    def schema_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "schemaArnInput"))

    @builtins.property
    @jsii.member(jsii_name="schemaNameInput")
    def schema_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "schemaNameInput"))

    @builtins.property
    @jsii.member(jsii_name="registryName")
    def registry_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "registryName"))

    @registry_name.setter
    def registry_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f4d49cc2f204e5268ccc31f670cf7ca4d62eaec6bcedbd6d1ab0affe370ea59)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "registryName", value)

    @builtins.property
    @jsii.member(jsii_name="schemaArn")
    def schema_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "schemaArn"))

    @schema_arn.setter
    def schema_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb005a55ddbb44e1009ef6ab34ace1453f1110b001219ffcb5942f5e533ae045)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schemaArn", value)

    @builtins.property
    @jsii.member(jsii_name="schemaName")
    def schema_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "schemaName"))

    @schema_name.setter
    def schema_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8194c6f0e0158b36a9deea77a2d9ec85d4a4fee4ad7c419640631229a72cd136)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schemaName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GlueCatalogTableStorageDescriptorSchemaReferenceSchemaId]:
        return typing.cast(typing.Optional[GlueCatalogTableStorageDescriptorSchemaReferenceSchemaId], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GlueCatalogTableStorageDescriptorSchemaReferenceSchemaId],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4326748962c13452291e29ebfd7dfd005b204c43a04ff088d939f16d2a02088)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.glueCatalogTable.GlueCatalogTableStorageDescriptorSerDeInfo",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "parameters": "parameters",
        "serialization_library": "serializationLibrary",
    },
)
class GlueCatalogTableStorageDescriptorSerDeInfo:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        serialization_library: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#name GlueCatalogTable#name}.
        :param parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#parameters GlueCatalogTable#parameters}.
        :param serialization_library: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#serialization_library GlueCatalogTable#serialization_library}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e542dd898ee07399ba11f16153085a17cdf06307048b92086b387a11e3922fd)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument serialization_library", value=serialization_library, expected_type=type_hints["serialization_library"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if parameters is not None:
            self._values["parameters"] = parameters
        if serialization_library is not None:
            self._values["serialization_library"] = serialization_library

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#name GlueCatalogTable#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parameters(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#parameters GlueCatalogTable#parameters}.'''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def serialization_library(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#serialization_library GlueCatalogTable#serialization_library}.'''
        result = self._values.get("serialization_library")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GlueCatalogTableStorageDescriptorSerDeInfo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GlueCatalogTableStorageDescriptorSerDeInfoOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.glueCatalogTable.GlueCatalogTableStorageDescriptorSerDeInfoOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d0337cc3ef3515709776d47f93d42b1ef5295d8f6b68d5a96994e5c2e4fdaff7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetParameters")
    def reset_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParameters", []))

    @jsii.member(jsii_name="resetSerializationLibrary")
    def reset_serialization_library(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSerializationLibrary", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="parametersInput")
    def parameters_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "parametersInput"))

    @builtins.property
    @jsii.member(jsii_name="serializationLibraryInput")
    def serialization_library_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serializationLibraryInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6a8b361b9ae51ff32ea47252dd56b05fe937309a9ce4449cc1cacc1ead58793)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__791b77a9bf05e5fb34c3675970188b1c5c79209760648db6089979454724e254)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameters", value)

    @builtins.property
    @jsii.member(jsii_name="serializationLibrary")
    def serialization_library(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serializationLibrary"))

    @serialization_library.setter
    def serialization_library(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__acfbe580c3fff3fd9d3ed4c18d6a6d21d19303454fc516def53873585e53f037)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serializationLibrary", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GlueCatalogTableStorageDescriptorSerDeInfo]:
        return typing.cast(typing.Optional[GlueCatalogTableStorageDescriptorSerDeInfo], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GlueCatalogTableStorageDescriptorSerDeInfo],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61aae02309e6cae0cf0a3fe81a554563c25954fb3f5c0112f3978b602bbce15a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.glueCatalogTable.GlueCatalogTableStorageDescriptorSkewedInfo",
    jsii_struct_bases=[],
    name_mapping={
        "skewed_column_names": "skewedColumnNames",
        "skewed_column_value_location_maps": "skewedColumnValueLocationMaps",
        "skewed_column_values": "skewedColumnValues",
    },
)
class GlueCatalogTableStorageDescriptorSkewedInfo:
    def __init__(
        self,
        *,
        skewed_column_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        skewed_column_value_location_maps: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        skewed_column_values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param skewed_column_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#skewed_column_names GlueCatalogTable#skewed_column_names}.
        :param skewed_column_value_location_maps: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#skewed_column_value_location_maps GlueCatalogTable#skewed_column_value_location_maps}.
        :param skewed_column_values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#skewed_column_values GlueCatalogTable#skewed_column_values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dcf3e2dcc61055e4816ba1c4d46b4e02d4c5e34af5d065b200c2d04ef7b834db)
            check_type(argname="argument skewed_column_names", value=skewed_column_names, expected_type=type_hints["skewed_column_names"])
            check_type(argname="argument skewed_column_value_location_maps", value=skewed_column_value_location_maps, expected_type=type_hints["skewed_column_value_location_maps"])
            check_type(argname="argument skewed_column_values", value=skewed_column_values, expected_type=type_hints["skewed_column_values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if skewed_column_names is not None:
            self._values["skewed_column_names"] = skewed_column_names
        if skewed_column_value_location_maps is not None:
            self._values["skewed_column_value_location_maps"] = skewed_column_value_location_maps
        if skewed_column_values is not None:
            self._values["skewed_column_values"] = skewed_column_values

    @builtins.property
    def skewed_column_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#skewed_column_names GlueCatalogTable#skewed_column_names}.'''
        result = self._values.get("skewed_column_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def skewed_column_value_location_maps(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#skewed_column_value_location_maps GlueCatalogTable#skewed_column_value_location_maps}.'''
        result = self._values.get("skewed_column_value_location_maps")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def skewed_column_values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#skewed_column_values GlueCatalogTable#skewed_column_values}.'''
        result = self._values.get("skewed_column_values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GlueCatalogTableStorageDescriptorSkewedInfo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GlueCatalogTableStorageDescriptorSkewedInfoOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.glueCatalogTable.GlueCatalogTableStorageDescriptorSkewedInfoOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f7ef907402d147f83363efc3b7ee708bef1081f555d4a493c02facbf57075b92)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetSkewedColumnNames")
    def reset_skewed_column_names(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSkewedColumnNames", []))

    @jsii.member(jsii_name="resetSkewedColumnValueLocationMaps")
    def reset_skewed_column_value_location_maps(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSkewedColumnValueLocationMaps", []))

    @jsii.member(jsii_name="resetSkewedColumnValues")
    def reset_skewed_column_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSkewedColumnValues", []))

    @builtins.property
    @jsii.member(jsii_name="skewedColumnNamesInput")
    def skewed_column_names_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "skewedColumnNamesInput"))

    @builtins.property
    @jsii.member(jsii_name="skewedColumnValueLocationMapsInput")
    def skewed_column_value_location_maps_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "skewedColumnValueLocationMapsInput"))

    @builtins.property
    @jsii.member(jsii_name="skewedColumnValuesInput")
    def skewed_column_values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "skewedColumnValuesInput"))

    @builtins.property
    @jsii.member(jsii_name="skewedColumnNames")
    def skewed_column_names(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "skewedColumnNames"))

    @skewed_column_names.setter
    def skewed_column_names(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54863d1aed1939c4b9e1918d87c2281c2045b9840b60a2e86342484fb3feedd8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "skewedColumnNames", value)

    @builtins.property
    @jsii.member(jsii_name="skewedColumnValueLocationMaps")
    def skewed_column_value_location_maps(
        self,
    ) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "skewedColumnValueLocationMaps"))

    @skewed_column_value_location_maps.setter
    def skewed_column_value_location_maps(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6882bf20ed16f06a83816bfa9ba30d1ff4a3ae08c086a5f4183247d42363e097)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "skewedColumnValueLocationMaps", value)

    @builtins.property
    @jsii.member(jsii_name="skewedColumnValues")
    def skewed_column_values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "skewedColumnValues"))

    @skewed_column_values.setter
    def skewed_column_values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a8e430349cce8728149a7e171994703b24337997846486c7ab8886e0e09d2833)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "skewedColumnValues", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GlueCatalogTableStorageDescriptorSkewedInfo]:
        return typing.cast(typing.Optional[GlueCatalogTableStorageDescriptorSkewedInfo], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GlueCatalogTableStorageDescriptorSkewedInfo],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af9e580fb6d3703b2a1cac481c0bdb9d3764d30a9507a417f2d1b14fff1e4002)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.glueCatalogTable.GlueCatalogTableStorageDescriptorSortColumns",
    jsii_struct_bases=[],
    name_mapping={"column": "column", "sort_order": "sortOrder"},
)
class GlueCatalogTableStorageDescriptorSortColumns:
    def __init__(self, *, column: builtins.str, sort_order: jsii.Number) -> None:
        '''
        :param column: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#column GlueCatalogTable#column}.
        :param sort_order: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#sort_order GlueCatalogTable#sort_order}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84ae7c32b1c27a86c0c421e12ad69ae6023facc00d39a41f9a591b51349a98da)
            check_type(argname="argument column", value=column, expected_type=type_hints["column"])
            check_type(argname="argument sort_order", value=sort_order, expected_type=type_hints["sort_order"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "column": column,
            "sort_order": sort_order,
        }

    @builtins.property
    def column(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#column GlueCatalogTable#column}.'''
        result = self._values.get("column")
        assert result is not None, "Required property 'column' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sort_order(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#sort_order GlueCatalogTable#sort_order}.'''
        result = self._values.get("sort_order")
        assert result is not None, "Required property 'sort_order' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GlueCatalogTableStorageDescriptorSortColumns(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GlueCatalogTableStorageDescriptorSortColumnsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.glueCatalogTable.GlueCatalogTableStorageDescriptorSortColumnsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__216be9329f142dc7a8ab2a48300c902fe145ae184461f8bbe3621cde9872db1b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GlueCatalogTableStorageDescriptorSortColumnsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a8608c3c77d641cf1bbc42d64ff88ba1a6351e2eee481ff2f4e1adffd5f1fd3)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GlueCatalogTableStorageDescriptorSortColumnsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__abb485fcf6d67cf21ff2002d05a047e9f73adfa6a354b955c4332c865296fa0f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2ec9bad1f11a01863ec9abc639a2c62b051ecdd136008077baacc43d3e879248)
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
            type_hints = typing.get_type_hints(_typecheckingstub__18e951bd0d4abb241edf33e79d2d9a2a5483b7c6019ba16faffb6d06624998ff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GlueCatalogTableStorageDescriptorSortColumns]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GlueCatalogTableStorageDescriptorSortColumns]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GlueCatalogTableStorageDescriptorSortColumns]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__417c0abf7a41592b3c458217d43c4ac4a66fffeda272389ea9b7409e54e21f7f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GlueCatalogTableStorageDescriptorSortColumnsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.glueCatalogTable.GlueCatalogTableStorageDescriptorSortColumnsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__21befd888cebda4566228c2ce0365c6acc45aa4f0305657335f900d0a9a937ab)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="columnInput")
    def column_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "columnInput"))

    @builtins.property
    @jsii.member(jsii_name="sortOrderInput")
    def sort_order_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sortOrderInput"))

    @builtins.property
    @jsii.member(jsii_name="column")
    def column(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "column"))

    @column.setter
    def column(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7afa1b1e6f941274d8e70ae7fb71b9416feb4a2ab282abfa50812ffb9ab7726)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "column", value)

    @builtins.property
    @jsii.member(jsii_name="sortOrder")
    def sort_order(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "sortOrder"))

    @sort_order.setter
    def sort_order(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89273f8445e0a8f3a5988eef1684ea33525b2c558394f6cb9c84a1659ede9752)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sortOrder", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GlueCatalogTableStorageDescriptorSortColumns, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GlueCatalogTableStorageDescriptorSortColumns, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GlueCatalogTableStorageDescriptorSortColumns, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__551657ae3032c0c9ec1de0a7042a72e9d850dc3716ea19ad8c2dd00ba0065109)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.glueCatalogTable.GlueCatalogTableTargetTable",
    jsii_struct_bases=[],
    name_mapping={
        "catalog_id": "catalogId",
        "database_name": "databaseName",
        "name": "name",
    },
)
class GlueCatalogTableTargetTable:
    def __init__(
        self,
        *,
        catalog_id: builtins.str,
        database_name: builtins.str,
        name: builtins.str,
    ) -> None:
        '''
        :param catalog_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#catalog_id GlueCatalogTable#catalog_id}.
        :param database_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#database_name GlueCatalogTable#database_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#name GlueCatalogTable#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b30d751371dcf3384f08b6904b28c414eedae2d71f3615a1efe68bd8cc6c4c93)
            check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
            check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "catalog_id": catalog_id,
            "database_name": database_name,
            "name": name,
        }

    @builtins.property
    def catalog_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#catalog_id GlueCatalogTable#catalog_id}.'''
        result = self._values.get("catalog_id")
        assert result is not None, "Required property 'catalog_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def database_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#database_name GlueCatalogTable#database_name}.'''
        result = self._values.get("database_name")
        assert result is not None, "Required property 'database_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_table#name GlueCatalogTable#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GlueCatalogTableTargetTable(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GlueCatalogTableTargetTableOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.glueCatalogTable.GlueCatalogTableTargetTableOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ed7cd9a6e9af1b2fd85a77857bf6c0fd4f1961dc22107f322ef170d82e4873fa)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

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
    @jsii.member(jsii_name="catalogId")
    def catalog_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "catalogId"))

    @catalog_id.setter
    def catalog_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7c9dc6c82b37bc61cad69f2ba8d78c8736f8108dca0b65a8f349863913332ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "catalogId", value)

    @builtins.property
    @jsii.member(jsii_name="databaseName")
    def database_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "databaseName"))

    @database_name.setter
    def database_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19f365064e84910cdb987d05d03e71008c5e6169eb8de7d2d96bd92e5fe4240e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "databaseName", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a914a953ebfe1cc4821cd35268f976d74fad511e508880b8e284df91b8603c53)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GlueCatalogTableTargetTable]:
        return typing.cast(typing.Optional[GlueCatalogTableTargetTable], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GlueCatalogTableTargetTable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b07bb3e97ddc8134600e204b64c68fae754c37bc93578150b3ebe8812b0e0efc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GlueCatalogTable",
    "GlueCatalogTableConfig",
    "GlueCatalogTablePartitionIndex",
    "GlueCatalogTablePartitionIndexList",
    "GlueCatalogTablePartitionIndexOutputReference",
    "GlueCatalogTablePartitionKeys",
    "GlueCatalogTablePartitionKeysList",
    "GlueCatalogTablePartitionKeysOutputReference",
    "GlueCatalogTableStorageDescriptor",
    "GlueCatalogTableStorageDescriptorColumns",
    "GlueCatalogTableStorageDescriptorColumnsList",
    "GlueCatalogTableStorageDescriptorColumnsOutputReference",
    "GlueCatalogTableStorageDescriptorOutputReference",
    "GlueCatalogTableStorageDescriptorSchemaReference",
    "GlueCatalogTableStorageDescriptorSchemaReferenceOutputReference",
    "GlueCatalogTableStorageDescriptorSchemaReferenceSchemaId",
    "GlueCatalogTableStorageDescriptorSchemaReferenceSchemaIdOutputReference",
    "GlueCatalogTableStorageDescriptorSerDeInfo",
    "GlueCatalogTableStorageDescriptorSerDeInfoOutputReference",
    "GlueCatalogTableStorageDescriptorSkewedInfo",
    "GlueCatalogTableStorageDescriptorSkewedInfoOutputReference",
    "GlueCatalogTableStorageDescriptorSortColumns",
    "GlueCatalogTableStorageDescriptorSortColumnsList",
    "GlueCatalogTableStorageDescriptorSortColumnsOutputReference",
    "GlueCatalogTableTargetTable",
    "GlueCatalogTableTargetTableOutputReference",
]

publication.publish()

def _typecheckingstub__a709fbfbc0ae96913d4062b940330f68ef6768a0e485d3e62a062a6bac0b17eb(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    database_name: builtins.str,
    name: builtins.str,
    catalog_id: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    owner: typing.Optional[builtins.str] = None,
    parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    partition_index: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GlueCatalogTablePartitionIndex, typing.Dict[builtins.str, typing.Any]]]]] = None,
    partition_keys: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GlueCatalogTablePartitionKeys, typing.Dict[builtins.str, typing.Any]]]]] = None,
    retention: typing.Optional[jsii.Number] = None,
    storage_descriptor: typing.Optional[typing.Union[GlueCatalogTableStorageDescriptor, typing.Dict[builtins.str, typing.Any]]] = None,
    table_type: typing.Optional[builtins.str] = None,
    target_table: typing.Optional[typing.Union[GlueCatalogTableTargetTable, typing.Dict[builtins.str, typing.Any]]] = None,
    view_expanded_text: typing.Optional[builtins.str] = None,
    view_original_text: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__38faaa10398c4e2beda4679112f01927101d130f8a91afe13a5cc83715ea987c(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GlueCatalogTablePartitionIndex, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc9beac348162d722ef8c98f14779ba41e183fd12d94625dc08c4dd53fd5204a(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GlueCatalogTablePartitionKeys, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb37e2d527352ef4a2bc478cbf17cce96cd1159f134efab5459e34e465b89d3d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d76a606b8b2ff41fcc5f689dac5806ca11ef656f98afedf89ef2940fc8d1757f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8dff6b848f4ee015dcbd7e1428fdd3f6040177115e52e068723340621e78682e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1e1c4f4b9c106b352f97ea6c17279fc295efe0c65fb10c056277f05c0b2f140(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ad5c6e3fa85feb6695acf77c7cfcd856731da64fd6fcc075c6b08f67d3e4eef(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a3efd212f3482317c04f134b27a07eee5f4d7ffa8227d81c0efdc3fdd147d59(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0298b83f0feae14a7c462aa753ab8d27ce817615f07f652ed0fbcaecb34a771f(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56180aeee073853ab358595fe4dfc8788edd4a76e190e5947e69ecb8649ca417(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c27d4ab86a4eeac0e86ae0289d6a11ce9c0134d2f02b3aada6f10b6f7d67664d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cec4b2110e00d7d0b3874ab64c16719fb2ffdb9bfd6e5a725063ff109a771cc5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca9076b26dd1cbcab3daea6a6d668aa9621ce0c6714ea9fb7f884c998acd9cda(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a60b838237e9be7efc7a66a0b10f9da46d6b31ff60bd9dd37fcf59c90b1052f4(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    database_name: builtins.str,
    name: builtins.str,
    catalog_id: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    owner: typing.Optional[builtins.str] = None,
    parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    partition_index: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GlueCatalogTablePartitionIndex, typing.Dict[builtins.str, typing.Any]]]]] = None,
    partition_keys: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GlueCatalogTablePartitionKeys, typing.Dict[builtins.str, typing.Any]]]]] = None,
    retention: typing.Optional[jsii.Number] = None,
    storage_descriptor: typing.Optional[typing.Union[GlueCatalogTableStorageDescriptor, typing.Dict[builtins.str, typing.Any]]] = None,
    table_type: typing.Optional[builtins.str] = None,
    target_table: typing.Optional[typing.Union[GlueCatalogTableTargetTable, typing.Dict[builtins.str, typing.Any]]] = None,
    view_expanded_text: typing.Optional[builtins.str] = None,
    view_original_text: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03c8acf6e5e581fcce09bc2762f563ac7c925093b8de8a8cbbdbd5f7b32dbb83(
    *,
    index_name: builtins.str,
    keys: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee6593c1d3d4876b7f42514f3f7516d29b83997c2cb9cc34bb43ba4ab2d8fed0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6183ccfaa2083b3a15e2f17a89512498b3ccf53c61135bd04304bea12ec6b55(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc8494c5241a20d7adee24eea2f715f97846c7fb1952e62b17e307eef518cbaa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__229af285ef442a7fabb99b7503daeab85a2be60a1ce39f0e67a13f4e2eb5d0c1(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63a55275a07efcb918e51805acf17dee7dc868bc1a3734321e14b0aaa87f49d6(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc2df2fbda926a51c795face471c01ffd79ecfc780fee9b603b2203db1e49bd3(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GlueCatalogTablePartitionIndex]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__862b6e9eeca88915aa2a398b88b8e0cd009721342e302a1c1cde8e4fa129dfb8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d15a60f515e9ea3431bb0caeea2cf51f282b6e26c3ecd101f75cd45a027157c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6924c80fe7818b37f66b805f116e97312226086e233c89b9af1e13db230e5d1(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b066886539f8cb5ed308dd5079a42a1e7bbe7c84d67f6b6e16238f90c8afadb(
    value: typing.Optional[typing.Union[GlueCatalogTablePartitionIndex, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f0b3bcab84ae200bd4cdd98db03a4b1eb925c832a502a0ccbe4c9d38b28df6c(
    *,
    name: builtins.str,
    comment: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4113ca280093b97dde0bfec52fe51118d5a69d8204a8eb4a0f44e558dcc0c6c3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e769a4699e1554cedb6add6d869ebeb5d84d24330f26286dcf9562f93c58d0da(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6cf50726e97820615c001da4853ec1044284d3721f65a5df75d30e17129652b6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63f77c106d1201f29ec8d7aeb857740a4f58c1a628aad9acba2b36cca43665c0(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d0611bf0838be91863c7a420a50584e79377f3dcd211b516e2efb85af47488a(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7641637e74d5bfdf6e1677dfa85a329b4f356ae39b713e4ffaa24bd2434f82c9(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GlueCatalogTablePartitionKeys]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35e36a2b598007e89ea6052f10ea04ce000fd95232d0b7e962938be1138ed7c3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be9bb0291b61b62b54ed7ab02942c1717b9f436145621c69412a8053bc532f67(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b49f6e49c069c2104bd6855a06c233f7af4f0d63a19efe9bcc74125d5ebc68e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7f57c2e2259ace8061ffb3f79d6ef4e481627a27bec29aa975b57ddab85ff15(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9cc517909fb932ba4c6b11d8559e457f07a54bef3af2f5aa166629b283d82aaf(
    value: typing.Optional[typing.Union[GlueCatalogTablePartitionKeys, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afa97fed3a1a402a8e8e34167062c83e2db0eb305fb34356688f23998d5019eb(
    *,
    bucket_columns: typing.Optional[typing.Sequence[builtins.str]] = None,
    columns: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GlueCatalogTableStorageDescriptorColumns, typing.Dict[builtins.str, typing.Any]]]]] = None,
    compressed: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    input_format: typing.Optional[builtins.str] = None,
    location: typing.Optional[builtins.str] = None,
    number_of_buckets: typing.Optional[jsii.Number] = None,
    output_format: typing.Optional[builtins.str] = None,
    parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    schema_reference: typing.Optional[typing.Union[GlueCatalogTableStorageDescriptorSchemaReference, typing.Dict[builtins.str, typing.Any]]] = None,
    ser_de_info: typing.Optional[typing.Union[GlueCatalogTableStorageDescriptorSerDeInfo, typing.Dict[builtins.str, typing.Any]]] = None,
    skewed_info: typing.Optional[typing.Union[GlueCatalogTableStorageDescriptorSkewedInfo, typing.Dict[builtins.str, typing.Any]]] = None,
    sort_columns: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GlueCatalogTableStorageDescriptorSortColumns, typing.Dict[builtins.str, typing.Any]]]]] = None,
    stored_as_sub_directories: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f777b3baf40f731f04b0d54c6fc540ee3078100c5fa5a4ae97ae1ff99ce79bf(
    *,
    name: builtins.str,
    comment: typing.Optional[builtins.str] = None,
    parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9eb035a22afea7128a34cd9a90a2bf6d9cce432843cd34dbbd9356f759ab32d8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9a1dfd64b0bb894a258d60a1192109728ecb87d58a0530fa628ff1d1112f388(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b83bcd059bfd8d4687c2b279deafe6c6617acae450140742c1370d0ad2cda2a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d74a7f2a08d2a8c9edba1b549e1e845b1affd79d01f13eea8c83bae090ee0ee(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee56fecc14e189c17219cb2962c3c89b5246d332363064eb363600b39add98f4(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ef55cff43ac821f64006b6b6887ac1332e8dd64fd21259199e5106c54adaaf8(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GlueCatalogTableStorageDescriptorColumns]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ff1f8f275c7f1ebde504a73274d9780037cf33ecd18b4edaa4bc95cb9752624(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d39442be907bb143c5c78ec78a02ae517f4dc4ef6400f44dd0a85718cbe8202(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1f8b0e05b63c6dd377dbb8217e44440f5a3b51f50f7f644ddc68395e2f3119c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff601f95a434e09da10b39b0421d7760ab2885a551acf41479a8a9dd27e8b480(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b76b59b3331e084eb6c689a16f4980704cdc1d619a18a9433f24dc1ae07f7b3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef2c3e96396d495e4c938532b4a3b4c6bd414d2a7cffd59b3abe0cda1fce0ecd(
    value: typing.Optional[typing.Union[GlueCatalogTableStorageDescriptorColumns, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7cb1f7c0d809cedc2251ec6894bd44235edbd6de5d520abe1666b8e156a67cac(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35d412b346bca35af81a392f2e170838fc83a68bc72017b190afd1ee4e8bfeaa(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GlueCatalogTableStorageDescriptorColumns, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fbad93cc4a1643d1980568aa7076ff9db8658481e16cf4e1ff02e4100c77ee3b(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GlueCatalogTableStorageDescriptorSortColumns, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e93d8c619581893f8c1a41593426e2acd190ee95b4f3fd8c98e96bdc7fbb81c7(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc4db4802465cf9518002cf08d42e936416d6fce0847d23eec0ef3fb108ba1b4(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b904ca36f410ce8296cb872101d8ce8498a9140d33dbb64397e23cceec1aff9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84ea4ff96761ba4017060c5e5db50cf7d3021b45e50e9ea50098a96fd8c21f1e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65b8f83414a2105efb4a04379e309b19a7931a8d7942f5a3f199b04dfaf6b3d6(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0fd596e5a64f40f1a887014392509831353ddbc0452a662f207b9bf65705a7b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5194542811fc8242346cb167f417681407c1f0021ee56c4768cf2b2eee9624da(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__977e8c7b2faf9e7b2b621d40694eca54c5bf63b3b732fbd0194d958ae72e8077(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b947ce15571cc7d4c2adb09fb0e3def9b705415c79e31d59aad1ccfd4326be4(
    value: typing.Optional[GlueCatalogTableStorageDescriptor],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f042da52312d9eef478a5efb94a999846228838e2f00ec49b7d674795fd03197(
    *,
    schema_version_number: jsii.Number,
    schema_id: typing.Optional[typing.Union[GlueCatalogTableStorageDescriptorSchemaReferenceSchemaId, typing.Dict[builtins.str, typing.Any]]] = None,
    schema_version_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a01dd009b9cdfd8020e0fd5e96f91c3ba2b255fb86007be0cae61537ca1dbe6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b452ff2e7c60c3b217c05cb12a4301f9ff0876d7a902212684200c5a0b19397(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14758d5f13922773b1f71958f727573c729ec6c898cac65e2ad7e542867f10e1(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2508e6f37e66072d5c845e882f4d72b5ce80f28df1289957039eb728774efe8(
    value: typing.Optional[GlueCatalogTableStorageDescriptorSchemaReference],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25c8d3e8f4f5f811d22156562bb4eb9617a089e4079b496b3f2db59f1b07a177(
    *,
    registry_name: typing.Optional[builtins.str] = None,
    schema_arn: typing.Optional[builtins.str] = None,
    schema_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1794f9a68825a5a2c0907ab9c90952a4cdbde238a1a83f9f33fd5dad016a1a4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f4d49cc2f204e5268ccc31f670cf7ca4d62eaec6bcedbd6d1ab0affe370ea59(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb005a55ddbb44e1009ef6ab34ace1453f1110b001219ffcb5942f5e533ae045(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8194c6f0e0158b36a9deea77a2d9ec85d4a4fee4ad7c419640631229a72cd136(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4326748962c13452291e29ebfd7dfd005b204c43a04ff088d939f16d2a02088(
    value: typing.Optional[GlueCatalogTableStorageDescriptorSchemaReferenceSchemaId],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e542dd898ee07399ba11f16153085a17cdf06307048b92086b387a11e3922fd(
    *,
    name: typing.Optional[builtins.str] = None,
    parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    serialization_library: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0337cc3ef3515709776d47f93d42b1ef5295d8f6b68d5a96994e5c2e4fdaff7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6a8b361b9ae51ff32ea47252dd56b05fe937309a9ce4449cc1cacc1ead58793(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__791b77a9bf05e5fb34c3675970188b1c5c79209760648db6089979454724e254(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__acfbe580c3fff3fd9d3ed4c18d6a6d21d19303454fc516def53873585e53f037(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61aae02309e6cae0cf0a3fe81a554563c25954fb3f5c0112f3978b602bbce15a(
    value: typing.Optional[GlueCatalogTableStorageDescriptorSerDeInfo],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dcf3e2dcc61055e4816ba1c4d46b4e02d4c5e34af5d065b200c2d04ef7b834db(
    *,
    skewed_column_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    skewed_column_value_location_maps: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    skewed_column_values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7ef907402d147f83363efc3b7ee708bef1081f555d4a493c02facbf57075b92(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54863d1aed1939c4b9e1918d87c2281c2045b9840b60a2e86342484fb3feedd8(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6882bf20ed16f06a83816bfa9ba30d1ff4a3ae08c086a5f4183247d42363e097(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8e430349cce8728149a7e171994703b24337997846486c7ab8886e0e09d2833(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af9e580fb6d3703b2a1cac481c0bdb9d3764d30a9507a417f2d1b14fff1e4002(
    value: typing.Optional[GlueCatalogTableStorageDescriptorSkewedInfo],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84ae7c32b1c27a86c0c421e12ad69ae6023facc00d39a41f9a591b51349a98da(
    *,
    column: builtins.str,
    sort_order: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__216be9329f142dc7a8ab2a48300c902fe145ae184461f8bbe3621cde9872db1b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a8608c3c77d641cf1bbc42d64ff88ba1a6351e2eee481ff2f4e1adffd5f1fd3(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__abb485fcf6d67cf21ff2002d05a047e9f73adfa6a354b955c4332c865296fa0f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ec9bad1f11a01863ec9abc639a2c62b051ecdd136008077baacc43d3e879248(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18e951bd0d4abb241edf33e79d2d9a2a5483b7c6019ba16faffb6d06624998ff(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__417c0abf7a41592b3c458217d43c4ac4a66fffeda272389ea9b7409e54e21f7f(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GlueCatalogTableStorageDescriptorSortColumns]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21befd888cebda4566228c2ce0365c6acc45aa4f0305657335f900d0a9a937ab(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7afa1b1e6f941274d8e70ae7fb71b9416feb4a2ab282abfa50812ffb9ab7726(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89273f8445e0a8f3a5988eef1684ea33525b2c558394f6cb9c84a1659ede9752(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__551657ae3032c0c9ec1de0a7042a72e9d850dc3716ea19ad8c2dd00ba0065109(
    value: typing.Optional[typing.Union[GlueCatalogTableStorageDescriptorSortColumns, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b30d751371dcf3384f08b6904b28c414eedae2d71f3615a1efe68bd8cc6c4c93(
    *,
    catalog_id: builtins.str,
    database_name: builtins.str,
    name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed7cd9a6e9af1b2fd85a77857bf6c0fd4f1961dc22107f322ef170d82e4873fa(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7c9dc6c82b37bc61cad69f2ba8d78c8736f8108dca0b65a8f349863913332ec(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19f365064e84910cdb987d05d03e71008c5e6169eb8de7d2d96bd92e5fe4240e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a914a953ebfe1cc4821cd35268f976d74fad511e508880b8e284df91b8603c53(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b07bb3e97ddc8134600e204b64c68fae754c37bc93578150b3ebe8812b0e0efc(
    value: typing.Optional[GlueCatalogTableTargetTable],
) -> None:
    """Type checking stubs"""
    pass
