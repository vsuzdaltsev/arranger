'''
# `aws_glue_partition`

Refer to the Terraform Registory for docs: [`aws_glue_partition`](https://www.terraform.io/docs/providers/aws/r/glue_partition).
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


class GluePartition(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.gluePartition.GluePartition",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/glue_partition aws_glue_partition}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        database_name: builtins.str,
        partition_values: typing.Sequence[builtins.str],
        table_name: builtins.str,
        catalog_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        storage_descriptor: typing.Optional[typing.Union["GluePartitionStorageDescriptor", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/glue_partition aws_glue_partition} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param database_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#database_name GluePartition#database_name}.
        :param partition_values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#partition_values GluePartition#partition_values}.
        :param table_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#table_name GluePartition#table_name}.
        :param catalog_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#catalog_id GluePartition#catalog_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#id GluePartition#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#parameters GluePartition#parameters}.
        :param storage_descriptor: storage_descriptor block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#storage_descriptor GluePartition#storage_descriptor}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__839bf712fe8cac9588d6ca463e3617a0d88eeecc3013b18147f1afbb3b4ec337)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GluePartitionConfig(
            database_name=database_name,
            partition_values=partition_values,
            table_name=table_name,
            catalog_id=catalog_id,
            id=id,
            parameters=parameters,
            storage_descriptor=storage_descriptor,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putStorageDescriptor")
    def put_storage_descriptor(
        self,
        *,
        bucket_columns: typing.Optional[typing.Sequence[builtins.str]] = None,
        columns: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GluePartitionStorageDescriptorColumns", typing.Dict[builtins.str, typing.Any]]]]] = None,
        compressed: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        input_format: typing.Optional[builtins.str] = None,
        location: typing.Optional[builtins.str] = None,
        number_of_buckets: typing.Optional[jsii.Number] = None,
        output_format: typing.Optional[builtins.str] = None,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        ser_de_info: typing.Optional[typing.Union["GluePartitionStorageDescriptorSerDeInfo", typing.Dict[builtins.str, typing.Any]]] = None,
        skewed_info: typing.Optional[typing.Union["GluePartitionStorageDescriptorSkewedInfo", typing.Dict[builtins.str, typing.Any]]] = None,
        sort_columns: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GluePartitionStorageDescriptorSortColumns", typing.Dict[builtins.str, typing.Any]]]]] = None,
        stored_as_sub_directories: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param bucket_columns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#bucket_columns GluePartition#bucket_columns}.
        :param columns: columns block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#columns GluePartition#columns}
        :param compressed: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#compressed GluePartition#compressed}.
        :param input_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#input_format GluePartition#input_format}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#location GluePartition#location}.
        :param number_of_buckets: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#number_of_buckets GluePartition#number_of_buckets}.
        :param output_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#output_format GluePartition#output_format}.
        :param parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#parameters GluePartition#parameters}.
        :param ser_de_info: ser_de_info block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#ser_de_info GluePartition#ser_de_info}
        :param skewed_info: skewed_info block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#skewed_info GluePartition#skewed_info}
        :param sort_columns: sort_columns block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#sort_columns GluePartition#sort_columns}
        :param stored_as_sub_directories: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#stored_as_sub_directories GluePartition#stored_as_sub_directories}.
        '''
        value = GluePartitionStorageDescriptor(
            bucket_columns=bucket_columns,
            columns=columns,
            compressed=compressed,
            input_format=input_format,
            location=location,
            number_of_buckets=number_of_buckets,
            output_format=output_format,
            parameters=parameters,
            ser_de_info=ser_de_info,
            skewed_info=skewed_info,
            sort_columns=sort_columns,
            stored_as_sub_directories=stored_as_sub_directories,
        )

        return typing.cast(None, jsii.invoke(self, "putStorageDescriptor", [value]))

    @jsii.member(jsii_name="resetCatalogId")
    def reset_catalog_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCatalogId", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetParameters")
    def reset_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParameters", []))

    @jsii.member(jsii_name="resetStorageDescriptor")
    def reset_storage_descriptor(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageDescriptor", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="creationTime")
    def creation_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "creationTime"))

    @builtins.property
    @jsii.member(jsii_name="lastAccessedTime")
    def last_accessed_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastAccessedTime"))

    @builtins.property
    @jsii.member(jsii_name="lastAnalyzedTime")
    def last_analyzed_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastAnalyzedTime"))

    @builtins.property
    @jsii.member(jsii_name="storageDescriptor")
    def storage_descriptor(self) -> "GluePartitionStorageDescriptorOutputReference":
        return typing.cast("GluePartitionStorageDescriptorOutputReference", jsii.get(self, "storageDescriptor"))

    @builtins.property
    @jsii.member(jsii_name="catalogIdInput")
    def catalog_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "catalogIdInput"))

    @builtins.property
    @jsii.member(jsii_name="databaseNameInput")
    def database_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseNameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="parametersInput")
    def parameters_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "parametersInput"))

    @builtins.property
    @jsii.member(jsii_name="partitionValuesInput")
    def partition_values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "partitionValuesInput"))

    @builtins.property
    @jsii.member(jsii_name="storageDescriptorInput")
    def storage_descriptor_input(
        self,
    ) -> typing.Optional["GluePartitionStorageDescriptor"]:
        return typing.cast(typing.Optional["GluePartitionStorageDescriptor"], jsii.get(self, "storageDescriptorInput"))

    @builtins.property
    @jsii.member(jsii_name="tableNameInput")
    def table_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tableNameInput"))

    @builtins.property
    @jsii.member(jsii_name="catalogId")
    def catalog_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "catalogId"))

    @catalog_id.setter
    def catalog_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__187c4a9a890f93aee59a3f70c37fd2924fe6946a53c5b59ecaa19f874c8a77bb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "catalogId", value)

    @builtins.property
    @jsii.member(jsii_name="databaseName")
    def database_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "databaseName"))

    @database_name.setter
    def database_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f82355eb496a325ac48aa6473684c671b401da6060fb43b297b0493891455396)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "databaseName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__51b95b2bab63a71c467e0ee60357b03916fbe41403db30d7c97c76eefdf44172)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93b12c02a79bd1df8b0fb24dbcf1c1ab969d1706c9645c8a9e1da7f19fd8a34b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameters", value)

    @builtins.property
    @jsii.member(jsii_name="partitionValues")
    def partition_values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "partitionValues"))

    @partition_values.setter
    def partition_values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af35f74711760026a9b0eea4b1d55169759448e36c548bb994757d3db28fbab5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "partitionValues", value)

    @builtins.property
    @jsii.member(jsii_name="tableName")
    def table_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tableName"))

    @table_name.setter
    def table_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2f70c2b39f1a19553be277231a2b43d58116c1a08e104ad3c4cf6a200004916)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tableName", value)


@jsii.data_type(
    jsii_type="aws.gluePartition.GluePartitionConfig",
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
        "partition_values": "partitionValues",
        "table_name": "tableName",
        "catalog_id": "catalogId",
        "id": "id",
        "parameters": "parameters",
        "storage_descriptor": "storageDescriptor",
    },
)
class GluePartitionConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        partition_values: typing.Sequence[builtins.str],
        table_name: builtins.str,
        catalog_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        storage_descriptor: typing.Optional[typing.Union["GluePartitionStorageDescriptor", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param database_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#database_name GluePartition#database_name}.
        :param partition_values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#partition_values GluePartition#partition_values}.
        :param table_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#table_name GluePartition#table_name}.
        :param catalog_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#catalog_id GluePartition#catalog_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#id GluePartition#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#parameters GluePartition#parameters}.
        :param storage_descriptor: storage_descriptor block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#storage_descriptor GluePartition#storage_descriptor}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(storage_descriptor, dict):
            storage_descriptor = GluePartitionStorageDescriptor(**storage_descriptor)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66dd79004bea23aa67194caca8eb9a7936584e0b22c4047d88a0fea82b725e7c)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
            check_type(argname="argument partition_values", value=partition_values, expected_type=type_hints["partition_values"])
            check_type(argname="argument table_name", value=table_name, expected_type=type_hints["table_name"])
            check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument storage_descriptor", value=storage_descriptor, expected_type=type_hints["storage_descriptor"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "database_name": database_name,
            "partition_values": partition_values,
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
        if catalog_id is not None:
            self._values["catalog_id"] = catalog_id
        if id is not None:
            self._values["id"] = id
        if parameters is not None:
            self._values["parameters"] = parameters
        if storage_descriptor is not None:
            self._values["storage_descriptor"] = storage_descriptor

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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#database_name GluePartition#database_name}.'''
        result = self._values.get("database_name")
        assert result is not None, "Required property 'database_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def partition_values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#partition_values GluePartition#partition_values}.'''
        result = self._values.get("partition_values")
        assert result is not None, "Required property 'partition_values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def table_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#table_name GluePartition#table_name}.'''
        result = self._values.get("table_name")
        assert result is not None, "Required property 'table_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def catalog_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#catalog_id GluePartition#catalog_id}.'''
        result = self._values.get("catalog_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#id GluePartition#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parameters(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#parameters GluePartition#parameters}.'''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def storage_descriptor(self) -> typing.Optional["GluePartitionStorageDescriptor"]:
        '''storage_descriptor block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#storage_descriptor GluePartition#storage_descriptor}
        '''
        result = self._values.get("storage_descriptor")
        return typing.cast(typing.Optional["GluePartitionStorageDescriptor"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GluePartitionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.gluePartition.GluePartitionStorageDescriptor",
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
        "ser_de_info": "serDeInfo",
        "skewed_info": "skewedInfo",
        "sort_columns": "sortColumns",
        "stored_as_sub_directories": "storedAsSubDirectories",
    },
)
class GluePartitionStorageDescriptor:
    def __init__(
        self,
        *,
        bucket_columns: typing.Optional[typing.Sequence[builtins.str]] = None,
        columns: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GluePartitionStorageDescriptorColumns", typing.Dict[builtins.str, typing.Any]]]]] = None,
        compressed: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        input_format: typing.Optional[builtins.str] = None,
        location: typing.Optional[builtins.str] = None,
        number_of_buckets: typing.Optional[jsii.Number] = None,
        output_format: typing.Optional[builtins.str] = None,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        ser_de_info: typing.Optional[typing.Union["GluePartitionStorageDescriptorSerDeInfo", typing.Dict[builtins.str, typing.Any]]] = None,
        skewed_info: typing.Optional[typing.Union["GluePartitionStorageDescriptorSkewedInfo", typing.Dict[builtins.str, typing.Any]]] = None,
        sort_columns: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GluePartitionStorageDescriptorSortColumns", typing.Dict[builtins.str, typing.Any]]]]] = None,
        stored_as_sub_directories: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param bucket_columns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#bucket_columns GluePartition#bucket_columns}.
        :param columns: columns block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#columns GluePartition#columns}
        :param compressed: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#compressed GluePartition#compressed}.
        :param input_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#input_format GluePartition#input_format}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#location GluePartition#location}.
        :param number_of_buckets: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#number_of_buckets GluePartition#number_of_buckets}.
        :param output_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#output_format GluePartition#output_format}.
        :param parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#parameters GluePartition#parameters}.
        :param ser_de_info: ser_de_info block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#ser_de_info GluePartition#ser_de_info}
        :param skewed_info: skewed_info block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#skewed_info GluePartition#skewed_info}
        :param sort_columns: sort_columns block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#sort_columns GluePartition#sort_columns}
        :param stored_as_sub_directories: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#stored_as_sub_directories GluePartition#stored_as_sub_directories}.
        '''
        if isinstance(ser_de_info, dict):
            ser_de_info = GluePartitionStorageDescriptorSerDeInfo(**ser_de_info)
        if isinstance(skewed_info, dict):
            skewed_info = GluePartitionStorageDescriptorSkewedInfo(**skewed_info)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f99383e9500bcce9f6dc395056ecb347e9f9e845daafe8267c4054ab58b368ee)
            check_type(argname="argument bucket_columns", value=bucket_columns, expected_type=type_hints["bucket_columns"])
            check_type(argname="argument columns", value=columns, expected_type=type_hints["columns"])
            check_type(argname="argument compressed", value=compressed, expected_type=type_hints["compressed"])
            check_type(argname="argument input_format", value=input_format, expected_type=type_hints["input_format"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument number_of_buckets", value=number_of_buckets, expected_type=type_hints["number_of_buckets"])
            check_type(argname="argument output_format", value=output_format, expected_type=type_hints["output_format"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#bucket_columns GluePartition#bucket_columns}.'''
        result = self._values.get("bucket_columns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def columns(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GluePartitionStorageDescriptorColumns"]]]:
        '''columns block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#columns GluePartition#columns}
        '''
        result = self._values.get("columns")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GluePartitionStorageDescriptorColumns"]]], result)

    @builtins.property
    def compressed(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#compressed GluePartition#compressed}.'''
        result = self._values.get("compressed")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def input_format(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#input_format GluePartition#input_format}.'''
        result = self._values.get("input_format")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def location(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#location GluePartition#location}.'''
        result = self._values.get("location")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def number_of_buckets(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#number_of_buckets GluePartition#number_of_buckets}.'''
        result = self._values.get("number_of_buckets")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def output_format(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#output_format GluePartition#output_format}.'''
        result = self._values.get("output_format")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parameters(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#parameters GluePartition#parameters}.'''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def ser_de_info(self) -> typing.Optional["GluePartitionStorageDescriptorSerDeInfo"]:
        '''ser_de_info block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#ser_de_info GluePartition#ser_de_info}
        '''
        result = self._values.get("ser_de_info")
        return typing.cast(typing.Optional["GluePartitionStorageDescriptorSerDeInfo"], result)

    @builtins.property
    def skewed_info(
        self,
    ) -> typing.Optional["GluePartitionStorageDescriptorSkewedInfo"]:
        '''skewed_info block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#skewed_info GluePartition#skewed_info}
        '''
        result = self._values.get("skewed_info")
        return typing.cast(typing.Optional["GluePartitionStorageDescriptorSkewedInfo"], result)

    @builtins.property
    def sort_columns(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GluePartitionStorageDescriptorSortColumns"]]]:
        '''sort_columns block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#sort_columns GluePartition#sort_columns}
        '''
        result = self._values.get("sort_columns")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GluePartitionStorageDescriptorSortColumns"]]], result)

    @builtins.property
    def stored_as_sub_directories(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#stored_as_sub_directories GluePartition#stored_as_sub_directories}.'''
        result = self._values.get("stored_as_sub_directories")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GluePartitionStorageDescriptor(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.gluePartition.GluePartitionStorageDescriptorColumns",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "comment": "comment", "type": "type"},
)
class GluePartitionStorageDescriptorColumns:
    def __init__(
        self,
        *,
        name: builtins.str,
        comment: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#name GluePartition#name}.
        :param comment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#comment GluePartition#comment}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#type GluePartition#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d47c300888a3f86cfab0fa37299373e64960b2420860e0cb7425a5ffbdb8eba3)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#name GluePartition#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#comment GluePartition#comment}.'''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#type GluePartition#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GluePartitionStorageDescriptorColumns(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GluePartitionStorageDescriptorColumnsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.gluePartition.GluePartitionStorageDescriptorColumnsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__92c35ab585d3d91d7a03bc1f0fb2f0fd4472c36f9ec9529d147550c656b7a40c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GluePartitionStorageDescriptorColumnsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d64618e4d3b9c5c08c03e0ff623ff1a4f5ca2ec8fb6d0e1a5448028b185bfd6)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GluePartitionStorageDescriptorColumnsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8fc009d2e28a95f8d14f8b456da9530468af92f984b11438bfe10ec0199a8051)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d7824b8464b93b1f4f9ad2d350cfe6553b2aa689ea5cbb8ffb01af9fde63e84c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__bb2e07a29903b8938db3588621c131b518e4aafc5f369ede90e2f41904925e98)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GluePartitionStorageDescriptorColumns]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GluePartitionStorageDescriptorColumns]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GluePartitionStorageDescriptorColumns]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__865abb04f13cf6858571b0013587786afc05e44445e1a2078e8c725230ce00d1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GluePartitionStorageDescriptorColumnsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.gluePartition.GluePartitionStorageDescriptorColumnsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2fbda12c5cdd3677df346ec4453646ef90078cb7435f20944ef9d7ac8df6167d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a1f632604624b07a3668c14ebe15ed9621a7536a37d5407205260c2886549e68)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "comment", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff3560a83ad54f9d026f6fab7f805ed4cdc7c1a80ac463730599f17de35206b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__abd4932e51aa1765828bc50204b6ef5e925ec8c4fc2d3f7dda6e291a3e3233fb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GluePartitionStorageDescriptorColumns, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GluePartitionStorageDescriptorColumns, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GluePartitionStorageDescriptorColumns, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45ae91b5f655530ffc12f4c4cf4e4e3c0daf1c6c4058f63d12a23a719ea71985)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GluePartitionStorageDescriptorOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.gluePartition.GluePartitionStorageDescriptorOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3d395f129dcaaa8ca78547d2174683a7de826032682596eb08537ab2004390b7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putColumns")
    def put_columns(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GluePartitionStorageDescriptorColumns, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4101b26c378de50f3e2f4220402de504ed845da92298cbcfe7e2c87846c9dbc5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putColumns", [value]))

    @jsii.member(jsii_name="putSerDeInfo")
    def put_ser_de_info(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        serialization_library: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#name GluePartition#name}.
        :param parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#parameters GluePartition#parameters}.
        :param serialization_library: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#serialization_library GluePartition#serialization_library}.
        '''
        value = GluePartitionStorageDescriptorSerDeInfo(
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
        :param skewed_column_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#skewed_column_names GluePartition#skewed_column_names}.
        :param skewed_column_value_location_maps: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#skewed_column_value_location_maps GluePartition#skewed_column_value_location_maps}.
        :param skewed_column_values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#skewed_column_values GluePartition#skewed_column_values}.
        '''
        value = GluePartitionStorageDescriptorSkewedInfo(
            skewed_column_names=skewed_column_names,
            skewed_column_value_location_maps=skewed_column_value_location_maps,
            skewed_column_values=skewed_column_values,
        )

        return typing.cast(None, jsii.invoke(self, "putSkewedInfo", [value]))

    @jsii.member(jsii_name="putSortColumns")
    def put_sort_columns(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GluePartitionStorageDescriptorSortColumns", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d761d985476a6b8a62b18f5e8d5fe4d2a6252cf2c51781d53fde24306ff06c5)
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
    def columns(self) -> GluePartitionStorageDescriptorColumnsList:
        return typing.cast(GluePartitionStorageDescriptorColumnsList, jsii.get(self, "columns"))

    @builtins.property
    @jsii.member(jsii_name="serDeInfo")
    def ser_de_info(self) -> "GluePartitionStorageDescriptorSerDeInfoOutputReference":
        return typing.cast("GluePartitionStorageDescriptorSerDeInfoOutputReference", jsii.get(self, "serDeInfo"))

    @builtins.property
    @jsii.member(jsii_name="skewedInfo")
    def skewed_info(self) -> "GluePartitionStorageDescriptorSkewedInfoOutputReference":
        return typing.cast("GluePartitionStorageDescriptorSkewedInfoOutputReference", jsii.get(self, "skewedInfo"))

    @builtins.property
    @jsii.member(jsii_name="sortColumns")
    def sort_columns(self) -> "GluePartitionStorageDescriptorSortColumnsList":
        return typing.cast("GluePartitionStorageDescriptorSortColumnsList", jsii.get(self, "sortColumns"))

    @builtins.property
    @jsii.member(jsii_name="bucketColumnsInput")
    def bucket_columns_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "bucketColumnsInput"))

    @builtins.property
    @jsii.member(jsii_name="columnsInput")
    def columns_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GluePartitionStorageDescriptorColumns]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GluePartitionStorageDescriptorColumns]]], jsii.get(self, "columnsInput"))

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
    @jsii.member(jsii_name="serDeInfoInput")
    def ser_de_info_input(
        self,
    ) -> typing.Optional["GluePartitionStorageDescriptorSerDeInfo"]:
        return typing.cast(typing.Optional["GluePartitionStorageDescriptorSerDeInfo"], jsii.get(self, "serDeInfoInput"))

    @builtins.property
    @jsii.member(jsii_name="skewedInfoInput")
    def skewed_info_input(
        self,
    ) -> typing.Optional["GluePartitionStorageDescriptorSkewedInfo"]:
        return typing.cast(typing.Optional["GluePartitionStorageDescriptorSkewedInfo"], jsii.get(self, "skewedInfoInput"))

    @builtins.property
    @jsii.member(jsii_name="sortColumnsInput")
    def sort_columns_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GluePartitionStorageDescriptorSortColumns"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GluePartitionStorageDescriptorSortColumns"]]], jsii.get(self, "sortColumnsInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__8ce2177858ff149ace7047d1f5d8556f29790eb0bfd7d0bf078f77966a9ac715)
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
            type_hints = typing.get_type_hints(_typecheckingstub__21c23875596c1d82b6e26f014fb0a51f93256652590d3908b4a7dfcf919b647b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "compressed", value)

    @builtins.property
    @jsii.member(jsii_name="inputFormat")
    def input_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "inputFormat"))

    @input_format.setter
    def input_format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d81e932e85f2b1b14a20b68c1d7acc7014b5ebd6f3353263080dd8ac3f5f396)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "inputFormat", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0f92ec860ff9f39b1fd5b4b4530faa79a625abed2913d2b3d533e3dafb938fb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="numberOfBuckets")
    def number_of_buckets(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "numberOfBuckets"))

    @number_of_buckets.setter
    def number_of_buckets(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c21ee4aee8ca2edd52718c32e024edae3e0f9ae263ff6d10ca76e7b1595025d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "numberOfBuckets", value)

    @builtins.property
    @jsii.member(jsii_name="outputFormat")
    def output_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "outputFormat"))

    @output_format.setter
    def output_format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7cef86f1ae3adf5454b68ba072daff2b2227e44f28a8bbfb851500a7565b3f74)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "outputFormat", value)

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02958c70122fdd817687b9ea73d20eafb7e2d76fbbb39c8e6df2da42122eacd7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__07ae13d305ab1bd4240e248256e71aa55bbf7e3e6c741f5fb888984544a6fc8d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storedAsSubDirectories", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GluePartitionStorageDescriptor]:
        return typing.cast(typing.Optional[GluePartitionStorageDescriptor], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GluePartitionStorageDescriptor],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c59002a47ec8edbb2d3b80e4fe928914aa3624be0b903f6ed25c0cfc1dbd4974)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.gluePartition.GluePartitionStorageDescriptorSerDeInfo",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "parameters": "parameters",
        "serialization_library": "serializationLibrary",
    },
)
class GluePartitionStorageDescriptorSerDeInfo:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        serialization_library: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#name GluePartition#name}.
        :param parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#parameters GluePartition#parameters}.
        :param serialization_library: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#serialization_library GluePartition#serialization_library}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82870bccce556a7b1a44372d0b110a70e47a535d6bed4f055d7bd91a5a03cdc7)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#name GluePartition#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parameters(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#parameters GluePartition#parameters}.'''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def serialization_library(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#serialization_library GluePartition#serialization_library}.'''
        result = self._values.get("serialization_library")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GluePartitionStorageDescriptorSerDeInfo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GluePartitionStorageDescriptorSerDeInfoOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.gluePartition.GluePartitionStorageDescriptorSerDeInfoOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4105b0985b6a9a93e925b81daa20df479bd1e835114cf8b430e09569689106d2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4ad52fd547f6cd13ed2b52e8475ab56e15edebf9316ced6723f8a623da8b6cea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de411b17ef9ec9ad1ef5282c0ef1dd3e6ff0d130bd5de48cd663c2ee801fad71)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameters", value)

    @builtins.property
    @jsii.member(jsii_name="serializationLibrary")
    def serialization_library(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serializationLibrary"))

    @serialization_library.setter
    def serialization_library(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__55464981d8b4a3a44e016365339a8a4a71d901a616f6e4bfb7b6017566c736a4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serializationLibrary", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GluePartitionStorageDescriptorSerDeInfo]:
        return typing.cast(typing.Optional[GluePartitionStorageDescriptorSerDeInfo], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GluePartitionStorageDescriptorSerDeInfo],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a06aa57a8f61e6851d37499a8cc0adfd9177352b4ff44c90dade364ecbb13c1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.gluePartition.GluePartitionStorageDescriptorSkewedInfo",
    jsii_struct_bases=[],
    name_mapping={
        "skewed_column_names": "skewedColumnNames",
        "skewed_column_value_location_maps": "skewedColumnValueLocationMaps",
        "skewed_column_values": "skewedColumnValues",
    },
)
class GluePartitionStorageDescriptorSkewedInfo:
    def __init__(
        self,
        *,
        skewed_column_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        skewed_column_value_location_maps: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        skewed_column_values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param skewed_column_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#skewed_column_names GluePartition#skewed_column_names}.
        :param skewed_column_value_location_maps: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#skewed_column_value_location_maps GluePartition#skewed_column_value_location_maps}.
        :param skewed_column_values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#skewed_column_values GluePartition#skewed_column_values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__186f0b6876e3386357747d8a9cc489a46ffc268e20b2964a508d22559dffba38)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#skewed_column_names GluePartition#skewed_column_names}.'''
        result = self._values.get("skewed_column_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def skewed_column_value_location_maps(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#skewed_column_value_location_maps GluePartition#skewed_column_value_location_maps}.'''
        result = self._values.get("skewed_column_value_location_maps")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def skewed_column_values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#skewed_column_values GluePartition#skewed_column_values}.'''
        result = self._values.get("skewed_column_values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GluePartitionStorageDescriptorSkewedInfo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GluePartitionStorageDescriptorSkewedInfoOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.gluePartition.GluePartitionStorageDescriptorSkewedInfoOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2580883b34e2a84b61f44e280af0255a14db2ca8e7b30647d18ae3f3347eaf70)
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
            type_hints = typing.get_type_hints(_typecheckingstub__92a13f25897c8673ce8db0aeebb22d5b4a26de5e6165693751711755e298e5db)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0fb34f79f80a7bf9771de193ceafe2abf4243d644d3ab96ed079631a4c9ea435)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "skewedColumnValueLocationMaps", value)

    @builtins.property
    @jsii.member(jsii_name="skewedColumnValues")
    def skewed_column_values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "skewedColumnValues"))

    @skewed_column_values.setter
    def skewed_column_values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__240584ae66033fb8eff0ee65a47a4e276aabfbbd98679d0c4274cd9f3be4eecc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "skewedColumnValues", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GluePartitionStorageDescriptorSkewedInfo]:
        return typing.cast(typing.Optional[GluePartitionStorageDescriptorSkewedInfo], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GluePartitionStorageDescriptorSkewedInfo],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8f08840e4336d944bd03f820d0bec6fd89228e139449cbaac7ff1420a83c005)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.gluePartition.GluePartitionStorageDescriptorSortColumns",
    jsii_struct_bases=[],
    name_mapping={"column": "column", "sort_order": "sortOrder"},
)
class GluePartitionStorageDescriptorSortColumns:
    def __init__(self, *, column: builtins.str, sort_order: jsii.Number) -> None:
        '''
        :param column: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#column GluePartition#column}.
        :param sort_order: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#sort_order GluePartition#sort_order}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f2dd2eee2afc1286e7f09274b7c3ebd39cb0acae76af9f913624d7b16428467c)
            check_type(argname="argument column", value=column, expected_type=type_hints["column"])
            check_type(argname="argument sort_order", value=sort_order, expected_type=type_hints["sort_order"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "column": column,
            "sort_order": sort_order,
        }

    @builtins.property
    def column(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#column GluePartition#column}.'''
        result = self._values.get("column")
        assert result is not None, "Required property 'column' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sort_order(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_partition#sort_order GluePartition#sort_order}.'''
        result = self._values.get("sort_order")
        assert result is not None, "Required property 'sort_order' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GluePartitionStorageDescriptorSortColumns(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GluePartitionStorageDescriptorSortColumnsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.gluePartition.GluePartitionStorageDescriptorSortColumnsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__65935fda9966f6ba2a4daabad265d7e2276bc3d540ad7ec74ef6cbf7bd492384)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GluePartitionStorageDescriptorSortColumnsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8db95e63032c92d45a1f722e4de11f81d27ca5a8403ad628b796a6b0f4fe922)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GluePartitionStorageDescriptorSortColumnsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32994fb487954cb425be0bffc7e4698684a7a03073f703cbf068492177501c0c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__71969811467e2e879c5b2e7e6d30cfbd54753f8d666060b0e10f68dbf82b6365)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5cac831b60b40848248adc45f81d9659cdb6b6c6b457997ff35fe4faaa12f833)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GluePartitionStorageDescriptorSortColumns]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GluePartitionStorageDescriptorSortColumns]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GluePartitionStorageDescriptorSortColumns]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cdcc5448fad518f100651ca74434613822a0d87dca152060e7c576681b963e57)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GluePartitionStorageDescriptorSortColumnsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.gluePartition.GluePartitionStorageDescriptorSortColumnsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d1fef26e2dcad90ca95cbb06f4c1c2839aaa051b5a5a3e5ef0d5d140692d4630)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f88cc365088175261886401afaed4e40e24c2c1a48de8a764e22c1e113bcc455)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "column", value)

    @builtins.property
    @jsii.member(jsii_name="sortOrder")
    def sort_order(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "sortOrder"))

    @sort_order.setter
    def sort_order(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45024e3bf97b3994669e34f3a63e21b11fc66e015916255a930067bb11b65a28)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sortOrder", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GluePartitionStorageDescriptorSortColumns, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GluePartitionStorageDescriptorSortColumns, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GluePartitionStorageDescriptorSortColumns, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3abf1976f62e39999741ee0e84df47633c97f64eee659b8435ebd645e3da1788)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GluePartition",
    "GluePartitionConfig",
    "GluePartitionStorageDescriptor",
    "GluePartitionStorageDescriptorColumns",
    "GluePartitionStorageDescriptorColumnsList",
    "GluePartitionStorageDescriptorColumnsOutputReference",
    "GluePartitionStorageDescriptorOutputReference",
    "GluePartitionStorageDescriptorSerDeInfo",
    "GluePartitionStorageDescriptorSerDeInfoOutputReference",
    "GluePartitionStorageDescriptorSkewedInfo",
    "GluePartitionStorageDescriptorSkewedInfoOutputReference",
    "GluePartitionStorageDescriptorSortColumns",
    "GluePartitionStorageDescriptorSortColumnsList",
    "GluePartitionStorageDescriptorSortColumnsOutputReference",
]

publication.publish()

def _typecheckingstub__839bf712fe8cac9588d6ca463e3617a0d88eeecc3013b18147f1afbb3b4ec337(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    database_name: builtins.str,
    partition_values: typing.Sequence[builtins.str],
    table_name: builtins.str,
    catalog_id: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    storage_descriptor: typing.Optional[typing.Union[GluePartitionStorageDescriptor, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__187c4a9a890f93aee59a3f70c37fd2924fe6946a53c5b59ecaa19f874c8a77bb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f82355eb496a325ac48aa6473684c671b401da6060fb43b297b0493891455396(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51b95b2bab63a71c467e0ee60357b03916fbe41403db30d7c97c76eefdf44172(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93b12c02a79bd1df8b0fb24dbcf1c1ab969d1706c9645c8a9e1da7f19fd8a34b(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af35f74711760026a9b0eea4b1d55169759448e36c548bb994757d3db28fbab5(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2f70c2b39f1a19553be277231a2b43d58116c1a08e104ad3c4cf6a200004916(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66dd79004bea23aa67194caca8eb9a7936584e0b22c4047d88a0fea82b725e7c(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    database_name: builtins.str,
    partition_values: typing.Sequence[builtins.str],
    table_name: builtins.str,
    catalog_id: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    storage_descriptor: typing.Optional[typing.Union[GluePartitionStorageDescriptor, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f99383e9500bcce9f6dc395056ecb347e9f9e845daafe8267c4054ab58b368ee(
    *,
    bucket_columns: typing.Optional[typing.Sequence[builtins.str]] = None,
    columns: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GluePartitionStorageDescriptorColumns, typing.Dict[builtins.str, typing.Any]]]]] = None,
    compressed: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    input_format: typing.Optional[builtins.str] = None,
    location: typing.Optional[builtins.str] = None,
    number_of_buckets: typing.Optional[jsii.Number] = None,
    output_format: typing.Optional[builtins.str] = None,
    parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ser_de_info: typing.Optional[typing.Union[GluePartitionStorageDescriptorSerDeInfo, typing.Dict[builtins.str, typing.Any]]] = None,
    skewed_info: typing.Optional[typing.Union[GluePartitionStorageDescriptorSkewedInfo, typing.Dict[builtins.str, typing.Any]]] = None,
    sort_columns: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GluePartitionStorageDescriptorSortColumns, typing.Dict[builtins.str, typing.Any]]]]] = None,
    stored_as_sub_directories: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d47c300888a3f86cfab0fa37299373e64960b2420860e0cb7425a5ffbdb8eba3(
    *,
    name: builtins.str,
    comment: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92c35ab585d3d91d7a03bc1f0fb2f0fd4472c36f9ec9529d147550c656b7a40c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d64618e4d3b9c5c08c03e0ff623ff1a4f5ca2ec8fb6d0e1a5448028b185bfd6(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8fc009d2e28a95f8d14f8b456da9530468af92f984b11438bfe10ec0199a8051(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7824b8464b93b1f4f9ad2d350cfe6553b2aa689ea5cbb8ffb01af9fde63e84c(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb2e07a29903b8938db3588621c131b518e4aafc5f369ede90e2f41904925e98(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__865abb04f13cf6858571b0013587786afc05e44445e1a2078e8c725230ce00d1(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GluePartitionStorageDescriptorColumns]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2fbda12c5cdd3677df346ec4453646ef90078cb7435f20944ef9d7ac8df6167d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1f632604624b07a3668c14ebe15ed9621a7536a37d5407205260c2886549e68(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff3560a83ad54f9d026f6fab7f805ed4cdc7c1a80ac463730599f17de35206b1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__abd4932e51aa1765828bc50204b6ef5e925ec8c4fc2d3f7dda6e291a3e3233fb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45ae91b5f655530ffc12f4c4cf4e4e3c0daf1c6c4058f63d12a23a719ea71985(
    value: typing.Optional[typing.Union[GluePartitionStorageDescriptorColumns, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d395f129dcaaa8ca78547d2174683a7de826032682596eb08537ab2004390b7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4101b26c378de50f3e2f4220402de504ed845da92298cbcfe7e2c87846c9dbc5(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GluePartitionStorageDescriptorColumns, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d761d985476a6b8a62b18f5e8d5fe4d2a6252cf2c51781d53fde24306ff06c5(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GluePartitionStorageDescriptorSortColumns, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ce2177858ff149ace7047d1f5d8556f29790eb0bfd7d0bf078f77966a9ac715(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21c23875596c1d82b6e26f014fb0a51f93256652590d3908b4a7dfcf919b647b(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d81e932e85f2b1b14a20b68c1d7acc7014b5ebd6f3353263080dd8ac3f5f396(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0f92ec860ff9f39b1fd5b4b4530faa79a625abed2913d2b3d533e3dafb938fb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c21ee4aee8ca2edd52718c32e024edae3e0f9ae263ff6d10ca76e7b1595025d(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7cef86f1ae3adf5454b68ba072daff2b2227e44f28a8bbfb851500a7565b3f74(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02958c70122fdd817687b9ea73d20eafb7e2d76fbbb39c8e6df2da42122eacd7(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07ae13d305ab1bd4240e248256e71aa55bbf7e3e6c741f5fb888984544a6fc8d(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c59002a47ec8edbb2d3b80e4fe928914aa3624be0b903f6ed25c0cfc1dbd4974(
    value: typing.Optional[GluePartitionStorageDescriptor],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82870bccce556a7b1a44372d0b110a70e47a535d6bed4f055d7bd91a5a03cdc7(
    *,
    name: typing.Optional[builtins.str] = None,
    parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    serialization_library: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4105b0985b6a9a93e925b81daa20df479bd1e835114cf8b430e09569689106d2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ad52fd547f6cd13ed2b52e8475ab56e15edebf9316ced6723f8a623da8b6cea(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de411b17ef9ec9ad1ef5282c0ef1dd3e6ff0d130bd5de48cd663c2ee801fad71(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55464981d8b4a3a44e016365339a8a4a71d901a616f6e4bfb7b6017566c736a4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a06aa57a8f61e6851d37499a8cc0adfd9177352b4ff44c90dade364ecbb13c1(
    value: typing.Optional[GluePartitionStorageDescriptorSerDeInfo],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__186f0b6876e3386357747d8a9cc489a46ffc268e20b2964a508d22559dffba38(
    *,
    skewed_column_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    skewed_column_value_location_maps: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    skewed_column_values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2580883b34e2a84b61f44e280af0255a14db2ca8e7b30647d18ae3f3347eaf70(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92a13f25897c8673ce8db0aeebb22d5b4a26de5e6165693751711755e298e5db(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0fb34f79f80a7bf9771de193ceafe2abf4243d644d3ab96ed079631a4c9ea435(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__240584ae66033fb8eff0ee65a47a4e276aabfbbd98679d0c4274cd9f3be4eecc(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8f08840e4336d944bd03f820d0bec6fd89228e139449cbaac7ff1420a83c005(
    value: typing.Optional[GluePartitionStorageDescriptorSkewedInfo],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2dd2eee2afc1286e7f09274b7c3ebd39cb0acae76af9f913624d7b16428467c(
    *,
    column: builtins.str,
    sort_order: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65935fda9966f6ba2a4daabad265d7e2276bc3d540ad7ec74ef6cbf7bd492384(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8db95e63032c92d45a1f722e4de11f81d27ca5a8403ad628b796a6b0f4fe922(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32994fb487954cb425be0bffc7e4698684a7a03073f703cbf068492177501c0c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71969811467e2e879c5b2e7e6d30cfbd54753f8d666060b0e10f68dbf82b6365(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5cac831b60b40848248adc45f81d9659cdb6b6c6b457997ff35fe4faaa12f833(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cdcc5448fad518f100651ca74434613822a0d87dca152060e7c576681b963e57(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GluePartitionStorageDescriptorSortColumns]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1fef26e2dcad90ca95cbb06f4c1c2839aaa051b5a5a3e5ef0d5d140692d4630(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f88cc365088175261886401afaed4e40e24c2c1a48de8a764e22c1e113bcc455(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45024e3bf97b3994669e34f3a63e21b11fc66e015916255a930067bb11b65a28(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3abf1976f62e39999741ee0e84df47633c97f64eee659b8435ebd645e3da1788(
    value: typing.Optional[typing.Union[GluePartitionStorageDescriptorSortColumns, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
