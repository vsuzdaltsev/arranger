'''
# `aws_keyspaces_table`

Refer to the Terraform Registory for docs: [`aws_keyspaces_table`](https://www.terraform.io/docs/providers/aws/r/keyspaces_table).
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


class KeyspacesTable(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.keyspacesTable.KeyspacesTable",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table aws_keyspaces_table}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        keyspace_name: builtins.str,
        schema_definition: typing.Union["KeyspacesTableSchemaDefinition", typing.Dict[builtins.str, typing.Any]],
        table_name: builtins.str,
        capacity_specification: typing.Optional[typing.Union["KeyspacesTableCapacitySpecification", typing.Dict[builtins.str, typing.Any]]] = None,
        comment: typing.Optional[typing.Union["KeyspacesTableComment", typing.Dict[builtins.str, typing.Any]]] = None,
        default_time_to_live: typing.Optional[jsii.Number] = None,
        encryption_specification: typing.Optional[typing.Union["KeyspacesTableEncryptionSpecification", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        point_in_time_recovery: typing.Optional[typing.Union["KeyspacesTablePointInTimeRecovery", typing.Dict[builtins.str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["KeyspacesTableTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        ttl: typing.Optional[typing.Union["KeyspacesTableTtl", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table aws_keyspaces_table} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param keyspace_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#keyspace_name KeyspacesTable#keyspace_name}.
        :param schema_definition: schema_definition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#schema_definition KeyspacesTable#schema_definition}
        :param table_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#table_name KeyspacesTable#table_name}.
        :param capacity_specification: capacity_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#capacity_specification KeyspacesTable#capacity_specification}
        :param comment: comment block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#comment KeyspacesTable#comment}
        :param default_time_to_live: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#default_time_to_live KeyspacesTable#default_time_to_live}.
        :param encryption_specification: encryption_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#encryption_specification KeyspacesTable#encryption_specification}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#id KeyspacesTable#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param point_in_time_recovery: point_in_time_recovery block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#point_in_time_recovery KeyspacesTable#point_in_time_recovery}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#tags KeyspacesTable#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#tags_all KeyspacesTable#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#timeouts KeyspacesTable#timeouts}
        :param ttl: ttl block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#ttl KeyspacesTable#ttl}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b990ef3bd6e359d2e2ee531697caa7d9d74dacd42de2bf32f8efe0cd771d6dc4)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = KeyspacesTableConfig(
            keyspace_name=keyspace_name,
            schema_definition=schema_definition,
            table_name=table_name,
            capacity_specification=capacity_specification,
            comment=comment,
            default_time_to_live=default_time_to_live,
            encryption_specification=encryption_specification,
            id=id,
            point_in_time_recovery=point_in_time_recovery,
            tags=tags,
            tags_all=tags_all,
            timeouts=timeouts,
            ttl=ttl,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putCapacitySpecification")
    def put_capacity_specification(
        self,
        *,
        read_capacity_units: typing.Optional[jsii.Number] = None,
        throughput_mode: typing.Optional[builtins.str] = None,
        write_capacity_units: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param read_capacity_units: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#read_capacity_units KeyspacesTable#read_capacity_units}.
        :param throughput_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#throughput_mode KeyspacesTable#throughput_mode}.
        :param write_capacity_units: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#write_capacity_units KeyspacesTable#write_capacity_units}.
        '''
        value = KeyspacesTableCapacitySpecification(
            read_capacity_units=read_capacity_units,
            throughput_mode=throughput_mode,
            write_capacity_units=write_capacity_units,
        )

        return typing.cast(None, jsii.invoke(self, "putCapacitySpecification", [value]))

    @jsii.member(jsii_name="putComment")
    def put_comment(self, *, message: typing.Optional[builtins.str] = None) -> None:
        '''
        :param message: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#message KeyspacesTable#message}.
        '''
        value = KeyspacesTableComment(message=message)

        return typing.cast(None, jsii.invoke(self, "putComment", [value]))

    @jsii.member(jsii_name="putEncryptionSpecification")
    def put_encryption_specification(
        self,
        *,
        kms_key_identifier: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param kms_key_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#kms_key_identifier KeyspacesTable#kms_key_identifier}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#type KeyspacesTable#type}.
        '''
        value = KeyspacesTableEncryptionSpecification(
            kms_key_identifier=kms_key_identifier, type=type
        )

        return typing.cast(None, jsii.invoke(self, "putEncryptionSpecification", [value]))

    @jsii.member(jsii_name="putPointInTimeRecovery")
    def put_point_in_time_recovery(
        self,
        *,
        status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#status KeyspacesTable#status}.
        '''
        value = KeyspacesTablePointInTimeRecovery(status=status)

        return typing.cast(None, jsii.invoke(self, "putPointInTimeRecovery", [value]))

    @jsii.member(jsii_name="putSchemaDefinition")
    def put_schema_definition(
        self,
        *,
        column: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KeyspacesTableSchemaDefinitionColumn", typing.Dict[builtins.str, typing.Any]]]],
        partition_key: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KeyspacesTableSchemaDefinitionPartitionKey", typing.Dict[builtins.str, typing.Any]]]],
        clustering_key: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KeyspacesTableSchemaDefinitionClusteringKey", typing.Dict[builtins.str, typing.Any]]]]] = None,
        static_column: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KeyspacesTableSchemaDefinitionStaticColumn", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param column: column block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#column KeyspacesTable#column}
        :param partition_key: partition_key block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#partition_key KeyspacesTable#partition_key}
        :param clustering_key: clustering_key block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#clustering_key KeyspacesTable#clustering_key}
        :param static_column: static_column block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#static_column KeyspacesTable#static_column}
        '''
        value = KeyspacesTableSchemaDefinition(
            column=column,
            partition_key=partition_key,
            clustering_key=clustering_key,
            static_column=static_column,
        )

        return typing.cast(None, jsii.invoke(self, "putSchemaDefinition", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#create KeyspacesTable#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#delete KeyspacesTable#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#update KeyspacesTable#update}.
        '''
        value = KeyspacesTableTimeouts(create=create, delete=delete, update=update)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putTtl")
    def put_ttl(self, *, status: builtins.str) -> None:
        '''
        :param status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#status KeyspacesTable#status}.
        '''
        value = KeyspacesTableTtl(status=status)

        return typing.cast(None, jsii.invoke(self, "putTtl", [value]))

    @jsii.member(jsii_name="resetCapacitySpecification")
    def reset_capacity_specification(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCapacitySpecification", []))

    @jsii.member(jsii_name="resetComment")
    def reset_comment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComment", []))

    @jsii.member(jsii_name="resetDefaultTimeToLive")
    def reset_default_time_to_live(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultTimeToLive", []))

    @jsii.member(jsii_name="resetEncryptionSpecification")
    def reset_encryption_specification(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncryptionSpecification", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetPointInTimeRecovery")
    def reset_point_in_time_recovery(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPointInTimeRecovery", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetTtl")
    def reset_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTtl", []))

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
    @jsii.member(jsii_name="capacitySpecification")
    def capacity_specification(
        self,
    ) -> "KeyspacesTableCapacitySpecificationOutputReference":
        return typing.cast("KeyspacesTableCapacitySpecificationOutputReference", jsii.get(self, "capacitySpecification"))

    @builtins.property
    @jsii.member(jsii_name="comment")
    def comment(self) -> "KeyspacesTableCommentOutputReference":
        return typing.cast("KeyspacesTableCommentOutputReference", jsii.get(self, "comment"))

    @builtins.property
    @jsii.member(jsii_name="encryptionSpecification")
    def encryption_specification(
        self,
    ) -> "KeyspacesTableEncryptionSpecificationOutputReference":
        return typing.cast("KeyspacesTableEncryptionSpecificationOutputReference", jsii.get(self, "encryptionSpecification"))

    @builtins.property
    @jsii.member(jsii_name="pointInTimeRecovery")
    def point_in_time_recovery(
        self,
    ) -> "KeyspacesTablePointInTimeRecoveryOutputReference":
        return typing.cast("KeyspacesTablePointInTimeRecoveryOutputReference", jsii.get(self, "pointInTimeRecovery"))

    @builtins.property
    @jsii.member(jsii_name="schemaDefinition")
    def schema_definition(self) -> "KeyspacesTableSchemaDefinitionOutputReference":
        return typing.cast("KeyspacesTableSchemaDefinitionOutputReference", jsii.get(self, "schemaDefinition"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "KeyspacesTableTimeoutsOutputReference":
        return typing.cast("KeyspacesTableTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="ttl")
    def ttl(self) -> "KeyspacesTableTtlOutputReference":
        return typing.cast("KeyspacesTableTtlOutputReference", jsii.get(self, "ttl"))

    @builtins.property
    @jsii.member(jsii_name="capacitySpecificationInput")
    def capacity_specification_input(
        self,
    ) -> typing.Optional["KeyspacesTableCapacitySpecification"]:
        return typing.cast(typing.Optional["KeyspacesTableCapacitySpecification"], jsii.get(self, "capacitySpecificationInput"))

    @builtins.property
    @jsii.member(jsii_name="commentInput")
    def comment_input(self) -> typing.Optional["KeyspacesTableComment"]:
        return typing.cast(typing.Optional["KeyspacesTableComment"], jsii.get(self, "commentInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultTimeToLiveInput")
    def default_time_to_live_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "defaultTimeToLiveInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptionSpecificationInput")
    def encryption_specification_input(
        self,
    ) -> typing.Optional["KeyspacesTableEncryptionSpecification"]:
        return typing.cast(typing.Optional["KeyspacesTableEncryptionSpecification"], jsii.get(self, "encryptionSpecificationInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="keyspaceNameInput")
    def keyspace_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyspaceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="pointInTimeRecoveryInput")
    def point_in_time_recovery_input(
        self,
    ) -> typing.Optional["KeyspacesTablePointInTimeRecovery"]:
        return typing.cast(typing.Optional["KeyspacesTablePointInTimeRecovery"], jsii.get(self, "pointInTimeRecoveryInput"))

    @builtins.property
    @jsii.member(jsii_name="schemaDefinitionInput")
    def schema_definition_input(
        self,
    ) -> typing.Optional["KeyspacesTableSchemaDefinition"]:
        return typing.cast(typing.Optional["KeyspacesTableSchemaDefinition"], jsii.get(self, "schemaDefinitionInput"))

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
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["KeyspacesTableTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["KeyspacesTableTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="ttlInput")
    def ttl_input(self) -> typing.Optional["KeyspacesTableTtl"]:
        return typing.cast(typing.Optional["KeyspacesTableTtl"], jsii.get(self, "ttlInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultTimeToLive")
    def default_time_to_live(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "defaultTimeToLive"))

    @default_time_to_live.setter
    def default_time_to_live(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7638875b13fa98fc3ba4f0a54df65fff60d5486dd89ccecec5474f3ffaeae8cb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultTimeToLive", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b08a5f4b98cf0f0342612904e19ea262e67c3bc133cf245efe3ee02f7e8fc5a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="keyspaceName")
    def keyspace_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyspaceName"))

    @keyspace_name.setter
    def keyspace_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c08f91a29a7fb4594169eaa9a1aa6459bec76da642a4399b985b9d95539e9d6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyspaceName", value)

    @builtins.property
    @jsii.member(jsii_name="tableName")
    def table_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tableName"))

    @table_name.setter
    def table_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aae9c6cc3a83c15ff274d379870e0bfafcc3cc392222fdbd48d6af3867493b73)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tableName", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a2bb0942979a7b3e7ca4327bbc7e46477ae3b1fcfff38867adfb21c2187fe26)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e606535bd97f3b3eaf479aa486055275bfbc61b4861583b819567a23ec78f195)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)


@jsii.data_type(
    jsii_type="aws.keyspacesTable.KeyspacesTableCapacitySpecification",
    jsii_struct_bases=[],
    name_mapping={
        "read_capacity_units": "readCapacityUnits",
        "throughput_mode": "throughputMode",
        "write_capacity_units": "writeCapacityUnits",
    },
)
class KeyspacesTableCapacitySpecification:
    def __init__(
        self,
        *,
        read_capacity_units: typing.Optional[jsii.Number] = None,
        throughput_mode: typing.Optional[builtins.str] = None,
        write_capacity_units: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param read_capacity_units: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#read_capacity_units KeyspacesTable#read_capacity_units}.
        :param throughput_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#throughput_mode KeyspacesTable#throughput_mode}.
        :param write_capacity_units: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#write_capacity_units KeyspacesTable#write_capacity_units}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e61c1675f1dd7cea14c7c82f05434faf403e55071d26f3f3651d782c871c39d)
            check_type(argname="argument read_capacity_units", value=read_capacity_units, expected_type=type_hints["read_capacity_units"])
            check_type(argname="argument throughput_mode", value=throughput_mode, expected_type=type_hints["throughput_mode"])
            check_type(argname="argument write_capacity_units", value=write_capacity_units, expected_type=type_hints["write_capacity_units"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if read_capacity_units is not None:
            self._values["read_capacity_units"] = read_capacity_units
        if throughput_mode is not None:
            self._values["throughput_mode"] = throughput_mode
        if write_capacity_units is not None:
            self._values["write_capacity_units"] = write_capacity_units

    @builtins.property
    def read_capacity_units(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#read_capacity_units KeyspacesTable#read_capacity_units}.'''
        result = self._values.get("read_capacity_units")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def throughput_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#throughput_mode KeyspacesTable#throughput_mode}.'''
        result = self._values.get("throughput_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def write_capacity_units(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#write_capacity_units KeyspacesTable#write_capacity_units}.'''
        result = self._values.get("write_capacity_units")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KeyspacesTableCapacitySpecification(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KeyspacesTableCapacitySpecificationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.keyspacesTable.KeyspacesTableCapacitySpecificationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__acc840395157fff65c8327d35ddd257f1a2b290dca5f33b66d77f883936d1328)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetReadCapacityUnits")
    def reset_read_capacity_units(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadCapacityUnits", []))

    @jsii.member(jsii_name="resetThroughputMode")
    def reset_throughput_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetThroughputMode", []))

    @jsii.member(jsii_name="resetWriteCapacityUnits")
    def reset_write_capacity_units(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWriteCapacityUnits", []))

    @builtins.property
    @jsii.member(jsii_name="readCapacityUnitsInput")
    def read_capacity_units_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "readCapacityUnitsInput"))

    @builtins.property
    @jsii.member(jsii_name="throughputModeInput")
    def throughput_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "throughputModeInput"))

    @builtins.property
    @jsii.member(jsii_name="writeCapacityUnitsInput")
    def write_capacity_units_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "writeCapacityUnitsInput"))

    @builtins.property
    @jsii.member(jsii_name="readCapacityUnits")
    def read_capacity_units(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "readCapacityUnits"))

    @read_capacity_units.setter
    def read_capacity_units(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1dac35bd30fe7bba23ce8031d3036b920fbad68a2729e700fdbb6997031e58f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readCapacityUnits", value)

    @builtins.property
    @jsii.member(jsii_name="throughputMode")
    def throughput_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "throughputMode"))

    @throughput_mode.setter
    def throughput_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab0c2cc06591f411041f498ec2f9dde11031a1bccd0308e6b11ee4afdab5910d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "throughputMode", value)

    @builtins.property
    @jsii.member(jsii_name="writeCapacityUnits")
    def write_capacity_units(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "writeCapacityUnits"))

    @write_capacity_units.setter
    def write_capacity_units(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5c8f417a74555ad6fd23da655950a142456eccd3e3268506586976e5e4565f2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "writeCapacityUnits", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[KeyspacesTableCapacitySpecification]:
        return typing.cast(typing.Optional[KeyspacesTableCapacitySpecification], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KeyspacesTableCapacitySpecification],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__509eb9200687c22a3cd83cc087d72bd918e98a7cf2ae35e70812cadde0373438)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.keyspacesTable.KeyspacesTableComment",
    jsii_struct_bases=[],
    name_mapping={"message": "message"},
)
class KeyspacesTableComment:
    def __init__(self, *, message: typing.Optional[builtins.str] = None) -> None:
        '''
        :param message: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#message KeyspacesTable#message}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d71742ca2f8f7af4764855ea6a4be093d4a4d941b38c18fe514e32d9e4ad0bf)
            check_type(argname="argument message", value=message, expected_type=type_hints["message"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if message is not None:
            self._values["message"] = message

    @builtins.property
    def message(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#message KeyspacesTable#message}.'''
        result = self._values.get("message")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KeyspacesTableComment(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KeyspacesTableCommentOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.keyspacesTable.KeyspacesTableCommentOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1bffb69d15e0b90d3a480086760ca652a48a5b9b48f8955c96b10bf55b562f8f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMessage")
    def reset_message(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMessage", []))

    @builtins.property
    @jsii.member(jsii_name="messageInput")
    def message_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "messageInput"))

    @builtins.property
    @jsii.member(jsii_name="message")
    def message(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "message"))

    @message.setter
    def message(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ef930777e69709c77121866b78325721ab09075eeac620e0a05ebf1eef8125a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "message", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[KeyspacesTableComment]:
        return typing.cast(typing.Optional[KeyspacesTableComment], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[KeyspacesTableComment]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e639ab4c9176c1b10a0ca2bbb0548dcedcfaa8a0f3b9c2004333d864210c515)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.keyspacesTable.KeyspacesTableConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "keyspace_name": "keyspaceName",
        "schema_definition": "schemaDefinition",
        "table_name": "tableName",
        "capacity_specification": "capacitySpecification",
        "comment": "comment",
        "default_time_to_live": "defaultTimeToLive",
        "encryption_specification": "encryptionSpecification",
        "id": "id",
        "point_in_time_recovery": "pointInTimeRecovery",
        "tags": "tags",
        "tags_all": "tagsAll",
        "timeouts": "timeouts",
        "ttl": "ttl",
    },
)
class KeyspacesTableConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        keyspace_name: builtins.str,
        schema_definition: typing.Union["KeyspacesTableSchemaDefinition", typing.Dict[builtins.str, typing.Any]],
        table_name: builtins.str,
        capacity_specification: typing.Optional[typing.Union[KeyspacesTableCapacitySpecification, typing.Dict[builtins.str, typing.Any]]] = None,
        comment: typing.Optional[typing.Union[KeyspacesTableComment, typing.Dict[builtins.str, typing.Any]]] = None,
        default_time_to_live: typing.Optional[jsii.Number] = None,
        encryption_specification: typing.Optional[typing.Union["KeyspacesTableEncryptionSpecification", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        point_in_time_recovery: typing.Optional[typing.Union["KeyspacesTablePointInTimeRecovery", typing.Dict[builtins.str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["KeyspacesTableTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        ttl: typing.Optional[typing.Union["KeyspacesTableTtl", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param keyspace_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#keyspace_name KeyspacesTable#keyspace_name}.
        :param schema_definition: schema_definition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#schema_definition KeyspacesTable#schema_definition}
        :param table_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#table_name KeyspacesTable#table_name}.
        :param capacity_specification: capacity_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#capacity_specification KeyspacesTable#capacity_specification}
        :param comment: comment block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#comment KeyspacesTable#comment}
        :param default_time_to_live: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#default_time_to_live KeyspacesTable#default_time_to_live}.
        :param encryption_specification: encryption_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#encryption_specification KeyspacesTable#encryption_specification}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#id KeyspacesTable#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param point_in_time_recovery: point_in_time_recovery block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#point_in_time_recovery KeyspacesTable#point_in_time_recovery}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#tags KeyspacesTable#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#tags_all KeyspacesTable#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#timeouts KeyspacesTable#timeouts}
        :param ttl: ttl block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#ttl KeyspacesTable#ttl}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(schema_definition, dict):
            schema_definition = KeyspacesTableSchemaDefinition(**schema_definition)
        if isinstance(capacity_specification, dict):
            capacity_specification = KeyspacesTableCapacitySpecification(**capacity_specification)
        if isinstance(comment, dict):
            comment = KeyspacesTableComment(**comment)
        if isinstance(encryption_specification, dict):
            encryption_specification = KeyspacesTableEncryptionSpecification(**encryption_specification)
        if isinstance(point_in_time_recovery, dict):
            point_in_time_recovery = KeyspacesTablePointInTimeRecovery(**point_in_time_recovery)
        if isinstance(timeouts, dict):
            timeouts = KeyspacesTableTimeouts(**timeouts)
        if isinstance(ttl, dict):
            ttl = KeyspacesTableTtl(**ttl)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a100d85574997370f4a0428f130762a098580232ccd53c289ea923585b371ec9)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument keyspace_name", value=keyspace_name, expected_type=type_hints["keyspace_name"])
            check_type(argname="argument schema_definition", value=schema_definition, expected_type=type_hints["schema_definition"])
            check_type(argname="argument table_name", value=table_name, expected_type=type_hints["table_name"])
            check_type(argname="argument capacity_specification", value=capacity_specification, expected_type=type_hints["capacity_specification"])
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument default_time_to_live", value=default_time_to_live, expected_type=type_hints["default_time_to_live"])
            check_type(argname="argument encryption_specification", value=encryption_specification, expected_type=type_hints["encryption_specification"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument point_in_time_recovery", value=point_in_time_recovery, expected_type=type_hints["point_in_time_recovery"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument ttl", value=ttl, expected_type=type_hints["ttl"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "keyspace_name": keyspace_name,
            "schema_definition": schema_definition,
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
        if capacity_specification is not None:
            self._values["capacity_specification"] = capacity_specification
        if comment is not None:
            self._values["comment"] = comment
        if default_time_to_live is not None:
            self._values["default_time_to_live"] = default_time_to_live
        if encryption_specification is not None:
            self._values["encryption_specification"] = encryption_specification
        if id is not None:
            self._values["id"] = id
        if point_in_time_recovery is not None:
            self._values["point_in_time_recovery"] = point_in_time_recovery
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if ttl is not None:
            self._values["ttl"] = ttl

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
    def keyspace_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#keyspace_name KeyspacesTable#keyspace_name}.'''
        result = self._values.get("keyspace_name")
        assert result is not None, "Required property 'keyspace_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def schema_definition(self) -> "KeyspacesTableSchemaDefinition":
        '''schema_definition block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#schema_definition KeyspacesTable#schema_definition}
        '''
        result = self._values.get("schema_definition")
        assert result is not None, "Required property 'schema_definition' is missing"
        return typing.cast("KeyspacesTableSchemaDefinition", result)

    @builtins.property
    def table_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#table_name KeyspacesTable#table_name}.'''
        result = self._values.get("table_name")
        assert result is not None, "Required property 'table_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def capacity_specification(
        self,
    ) -> typing.Optional[KeyspacesTableCapacitySpecification]:
        '''capacity_specification block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#capacity_specification KeyspacesTable#capacity_specification}
        '''
        result = self._values.get("capacity_specification")
        return typing.cast(typing.Optional[KeyspacesTableCapacitySpecification], result)

    @builtins.property
    def comment(self) -> typing.Optional[KeyspacesTableComment]:
        '''comment block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#comment KeyspacesTable#comment}
        '''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[KeyspacesTableComment], result)

    @builtins.property
    def default_time_to_live(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#default_time_to_live KeyspacesTable#default_time_to_live}.'''
        result = self._values.get("default_time_to_live")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def encryption_specification(
        self,
    ) -> typing.Optional["KeyspacesTableEncryptionSpecification"]:
        '''encryption_specification block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#encryption_specification KeyspacesTable#encryption_specification}
        '''
        result = self._values.get("encryption_specification")
        return typing.cast(typing.Optional["KeyspacesTableEncryptionSpecification"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#id KeyspacesTable#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def point_in_time_recovery(
        self,
    ) -> typing.Optional["KeyspacesTablePointInTimeRecovery"]:
        '''point_in_time_recovery block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#point_in_time_recovery KeyspacesTable#point_in_time_recovery}
        '''
        result = self._values.get("point_in_time_recovery")
        return typing.cast(typing.Optional["KeyspacesTablePointInTimeRecovery"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#tags KeyspacesTable#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#tags_all KeyspacesTable#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["KeyspacesTableTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#timeouts KeyspacesTable#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["KeyspacesTableTimeouts"], result)

    @builtins.property
    def ttl(self) -> typing.Optional["KeyspacesTableTtl"]:
        '''ttl block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#ttl KeyspacesTable#ttl}
        '''
        result = self._values.get("ttl")
        return typing.cast(typing.Optional["KeyspacesTableTtl"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KeyspacesTableConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.keyspacesTable.KeyspacesTableEncryptionSpecification",
    jsii_struct_bases=[],
    name_mapping={"kms_key_identifier": "kmsKeyIdentifier", "type": "type"},
)
class KeyspacesTableEncryptionSpecification:
    def __init__(
        self,
        *,
        kms_key_identifier: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param kms_key_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#kms_key_identifier KeyspacesTable#kms_key_identifier}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#type KeyspacesTable#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c2ba84e03669802531d08e6573ed5360b9484d56497a87ebd6a05ce51a869c6)
            check_type(argname="argument kms_key_identifier", value=kms_key_identifier, expected_type=type_hints["kms_key_identifier"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if kms_key_identifier is not None:
            self._values["kms_key_identifier"] = kms_key_identifier
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def kms_key_identifier(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#kms_key_identifier KeyspacesTable#kms_key_identifier}.'''
        result = self._values.get("kms_key_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#type KeyspacesTable#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KeyspacesTableEncryptionSpecification(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KeyspacesTableEncryptionSpecificationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.keyspacesTable.KeyspacesTableEncryptionSpecificationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3b9a90563cb6545f7d336e741b22cefd7f4e507c3f9c33ad8161b50eadb1e81b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetKmsKeyIdentifier")
    def reset_kms_key_identifier(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKeyIdentifier", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyIdentifierInput")
    def kms_key_identifier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyIdentifierInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyIdentifier")
    def kms_key_identifier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyIdentifier"))

    @kms_key_identifier.setter
    def kms_key_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7850788ed49de7fccdbf9913a1479d3153fe75325c1da5ed4c28f9f985211ac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__febc4cba8fdf1ecc1efa253fdf15e95a92c964d31658d3abbc988c1b746852a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[KeyspacesTableEncryptionSpecification]:
        return typing.cast(typing.Optional[KeyspacesTableEncryptionSpecification], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KeyspacesTableEncryptionSpecification],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20dfe5f55f114509475a5ae63fbe10aa73a7591c88bfe7e3d7bad60f55e443e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.keyspacesTable.KeyspacesTablePointInTimeRecovery",
    jsii_struct_bases=[],
    name_mapping={"status": "status"},
)
class KeyspacesTablePointInTimeRecovery:
    def __init__(self, *, status: typing.Optional[builtins.str] = None) -> None:
        '''
        :param status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#status KeyspacesTable#status}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__635182fd32823308cbdf1a49c1dbcd5d57718fcb1af8153a285d5e292396f9e9)
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#status KeyspacesTable#status}.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KeyspacesTablePointInTimeRecovery(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KeyspacesTablePointInTimeRecoveryOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.keyspacesTable.KeyspacesTablePointInTimeRecoveryOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__913e46f4b3ee499bd2f3e3231d864894d00bed93dae0c7b2464f278fd96a5314)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetStatus")
    def reset_status(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatus", []))

    @builtins.property
    @jsii.member(jsii_name="statusInput")
    def status_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statusInput"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @status.setter
    def status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3774d0127b943f6f1ecc30e7830dddc919219646e182dacad64387493c30cf27)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[KeyspacesTablePointInTimeRecovery]:
        return typing.cast(typing.Optional[KeyspacesTablePointInTimeRecovery], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KeyspacesTablePointInTimeRecovery],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e1a96d6963aaca9074b04fbb598c0e751f7e1fa3c27f7252b4b8b3b1e6f2178)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.keyspacesTable.KeyspacesTableSchemaDefinition",
    jsii_struct_bases=[],
    name_mapping={
        "column": "column",
        "partition_key": "partitionKey",
        "clustering_key": "clusteringKey",
        "static_column": "staticColumn",
    },
)
class KeyspacesTableSchemaDefinition:
    def __init__(
        self,
        *,
        column: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KeyspacesTableSchemaDefinitionColumn", typing.Dict[builtins.str, typing.Any]]]],
        partition_key: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KeyspacesTableSchemaDefinitionPartitionKey", typing.Dict[builtins.str, typing.Any]]]],
        clustering_key: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KeyspacesTableSchemaDefinitionClusteringKey", typing.Dict[builtins.str, typing.Any]]]]] = None,
        static_column: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KeyspacesTableSchemaDefinitionStaticColumn", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param column: column block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#column KeyspacesTable#column}
        :param partition_key: partition_key block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#partition_key KeyspacesTable#partition_key}
        :param clustering_key: clustering_key block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#clustering_key KeyspacesTable#clustering_key}
        :param static_column: static_column block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#static_column KeyspacesTable#static_column}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__270e276fd809a21739c4d0355775ebfda3c0411be5d12cfe98396c265824d63e)
            check_type(argname="argument column", value=column, expected_type=type_hints["column"])
            check_type(argname="argument partition_key", value=partition_key, expected_type=type_hints["partition_key"])
            check_type(argname="argument clustering_key", value=clustering_key, expected_type=type_hints["clustering_key"])
            check_type(argname="argument static_column", value=static_column, expected_type=type_hints["static_column"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "column": column,
            "partition_key": partition_key,
        }
        if clustering_key is not None:
            self._values["clustering_key"] = clustering_key
        if static_column is not None:
            self._values["static_column"] = static_column

    @builtins.property
    def column(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KeyspacesTableSchemaDefinitionColumn"]]:
        '''column block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#column KeyspacesTable#column}
        '''
        result = self._values.get("column")
        assert result is not None, "Required property 'column' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KeyspacesTableSchemaDefinitionColumn"]], result)

    @builtins.property
    def partition_key(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KeyspacesTableSchemaDefinitionPartitionKey"]]:
        '''partition_key block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#partition_key KeyspacesTable#partition_key}
        '''
        result = self._values.get("partition_key")
        assert result is not None, "Required property 'partition_key' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KeyspacesTableSchemaDefinitionPartitionKey"]], result)

    @builtins.property
    def clustering_key(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KeyspacesTableSchemaDefinitionClusteringKey"]]]:
        '''clustering_key block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#clustering_key KeyspacesTable#clustering_key}
        '''
        result = self._values.get("clustering_key")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KeyspacesTableSchemaDefinitionClusteringKey"]]], result)

    @builtins.property
    def static_column(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KeyspacesTableSchemaDefinitionStaticColumn"]]]:
        '''static_column block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#static_column KeyspacesTable#static_column}
        '''
        result = self._values.get("static_column")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KeyspacesTableSchemaDefinitionStaticColumn"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KeyspacesTableSchemaDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.keyspacesTable.KeyspacesTableSchemaDefinitionClusteringKey",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "order_by": "orderBy"},
)
class KeyspacesTableSchemaDefinitionClusteringKey:
    def __init__(self, *, name: builtins.str, order_by: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#name KeyspacesTable#name}.
        :param order_by: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#order_by KeyspacesTable#order_by}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f44673376121c01b61f192c668d4b6b5a60ccd4bf905bbbdc3b51641a416ff2)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument order_by", value=order_by, expected_type=type_hints["order_by"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "order_by": order_by,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#name KeyspacesTable#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def order_by(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#order_by KeyspacesTable#order_by}.'''
        result = self._values.get("order_by")
        assert result is not None, "Required property 'order_by' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KeyspacesTableSchemaDefinitionClusteringKey(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KeyspacesTableSchemaDefinitionClusteringKeyList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.keyspacesTable.KeyspacesTableSchemaDefinitionClusteringKeyList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3f80de0fb452ecab7cb9d2717f13a99ca9ccad3d2e69cd8c921c0d41aec5c5d9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "KeyspacesTableSchemaDefinitionClusteringKeyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a2d54ba448a1d730d0b319b29eeb2bd73f229369556b6f1804cafa6994e9ac6)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KeyspacesTableSchemaDefinitionClusteringKeyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__464d590bab66efeeb72849e5122a6281e335cfe21bc4c1732688d1884bd4c30f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__aecd9cde9fe6307892efa42ad854ddcd66b47521f20047e10259dd54b2c29b22)
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
            type_hints = typing.get_type_hints(_typecheckingstub__909d79206a5560ec228e1916b40aa0713a42c97b417eb37844b9f698e87bdbe7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KeyspacesTableSchemaDefinitionClusteringKey]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KeyspacesTableSchemaDefinitionClusteringKey]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KeyspacesTableSchemaDefinitionClusteringKey]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b091385059f714a8edd5be6a84b8a526e4f4e54fc27e0335a586121a5d97d33)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KeyspacesTableSchemaDefinitionClusteringKeyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.keyspacesTable.KeyspacesTableSchemaDefinitionClusteringKeyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__77340753be4170e665fb5e5da18e3f79fd5088aedf8e916fa77c90333541ca49)
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
    @jsii.member(jsii_name="orderByInput")
    def order_by_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "orderByInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb55f748d93bdf61e862aea322b31e4bfb709a128f1862566edf1493a567d761)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="orderBy")
    def order_by(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "orderBy"))

    @order_by.setter
    def order_by(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d9d0dc8c3ed6db09db3e5d8f56efcd24dadf53f1e4c3a93c1f6eee0d05253eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "orderBy", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[KeyspacesTableSchemaDefinitionClusteringKey, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[KeyspacesTableSchemaDefinitionClusteringKey, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[KeyspacesTableSchemaDefinitionClusteringKey, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__436be81d7f99a3d333ea1914f8e6e5eec98c6cb23bbd8f185db379d6a030cd1c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.keyspacesTable.KeyspacesTableSchemaDefinitionColumn",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "type": "type"},
)
class KeyspacesTableSchemaDefinitionColumn:
    def __init__(self, *, name: builtins.str, type: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#name KeyspacesTable#name}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#type KeyspacesTable#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02f2f37ffa67de2a54308b0ea5a9c43932566d5af2ff7afbd25cb5a602e846de)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "type": type,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#name KeyspacesTable#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#type KeyspacesTable#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KeyspacesTableSchemaDefinitionColumn(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KeyspacesTableSchemaDefinitionColumnList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.keyspacesTable.KeyspacesTableSchemaDefinitionColumnList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b9c3c0ba76f130ac0775271284937cd43d07f42e04d27f021722e84b80741e1a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "KeyspacesTableSchemaDefinitionColumnOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64a2debf9ca48bcb6b7ca6c7a624a2ddc212653b12519c23457105f7530192e6)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KeyspacesTableSchemaDefinitionColumnOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ddd8c2ff1d3ff082038ececdaa5f288d21e6c70029444c20aaed89b4e0841a2a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4cd9da13b2804ce0fe9f6236078e4a832151dde0503ebb34378d9e1f06bb020e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c8526a98789519821d65ba5ae763fb7ac41ff64aab36dc32d173cf8c1d58f795)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KeyspacesTableSchemaDefinitionColumn]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KeyspacesTableSchemaDefinitionColumn]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KeyspacesTableSchemaDefinitionColumn]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e6c78c0741cde86212e5caa38263025762a48902b97b2772f566fae120c55e3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KeyspacesTableSchemaDefinitionColumnOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.keyspacesTable.KeyspacesTableSchemaDefinitionColumnOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a201076b52fcd481968629fbc3c0619c66d3d892e721addb0b90171573e8b2d5)
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
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9924a2c71b49baedef1ccfd6fb914f41b088b161b2cce3220cacdac6ea4b9fbd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4bb45ae69d4e47d368e5020459b8b121f581b1a73d95a0f56865a42a9d9b54ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[KeyspacesTableSchemaDefinitionColumn, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[KeyspacesTableSchemaDefinitionColumn, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[KeyspacesTableSchemaDefinitionColumn, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a12f8040a52f600dd0538e5fce752e8cb1b8b436450a7dde71b8abca501428c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KeyspacesTableSchemaDefinitionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.keyspacesTable.KeyspacesTableSchemaDefinitionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__bb5fb43828bdb743e9795571ae17107c17663d7577a846a0eb8b4d6bdac90660)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putClusteringKey")
    def put_clustering_key(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KeyspacesTableSchemaDefinitionClusteringKey, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6337acb8dce8f30a4cc85b466246886b1287c735ac23da257fd7592f963fc2dc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putClusteringKey", [value]))

    @jsii.member(jsii_name="putColumn")
    def put_column(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KeyspacesTableSchemaDefinitionColumn, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4760b03e4977baef03ef218e0b135134b009c68d53d91c658134284d12b3a07)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putColumn", [value]))

    @jsii.member(jsii_name="putPartitionKey")
    def put_partition_key(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KeyspacesTableSchemaDefinitionPartitionKey", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e541a67bd266fd594f6bdd7e0a4e9c59d09e539629303f549f17d52c0f1f48ea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPartitionKey", [value]))

    @jsii.member(jsii_name="putStaticColumn")
    def put_static_column(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KeyspacesTableSchemaDefinitionStaticColumn", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a18bc376f6b9437f6d69d6dd387fda7bfb71d63f3a28ae82fbc62ae1fa602e88)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putStaticColumn", [value]))

    @jsii.member(jsii_name="resetClusteringKey")
    def reset_clustering_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClusteringKey", []))

    @jsii.member(jsii_name="resetStaticColumn")
    def reset_static_column(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStaticColumn", []))

    @builtins.property
    @jsii.member(jsii_name="clusteringKey")
    def clustering_key(self) -> KeyspacesTableSchemaDefinitionClusteringKeyList:
        return typing.cast(KeyspacesTableSchemaDefinitionClusteringKeyList, jsii.get(self, "clusteringKey"))

    @builtins.property
    @jsii.member(jsii_name="column")
    def column(self) -> KeyspacesTableSchemaDefinitionColumnList:
        return typing.cast(KeyspacesTableSchemaDefinitionColumnList, jsii.get(self, "column"))

    @builtins.property
    @jsii.member(jsii_name="partitionKey")
    def partition_key(self) -> "KeyspacesTableSchemaDefinitionPartitionKeyList":
        return typing.cast("KeyspacesTableSchemaDefinitionPartitionKeyList", jsii.get(self, "partitionKey"))

    @builtins.property
    @jsii.member(jsii_name="staticColumn")
    def static_column(self) -> "KeyspacesTableSchemaDefinitionStaticColumnList":
        return typing.cast("KeyspacesTableSchemaDefinitionStaticColumnList", jsii.get(self, "staticColumn"))

    @builtins.property
    @jsii.member(jsii_name="clusteringKeyInput")
    def clustering_key_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KeyspacesTableSchemaDefinitionClusteringKey]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KeyspacesTableSchemaDefinitionClusteringKey]]], jsii.get(self, "clusteringKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="columnInput")
    def column_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KeyspacesTableSchemaDefinitionColumn]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KeyspacesTableSchemaDefinitionColumn]]], jsii.get(self, "columnInput"))

    @builtins.property
    @jsii.member(jsii_name="partitionKeyInput")
    def partition_key_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KeyspacesTableSchemaDefinitionPartitionKey"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KeyspacesTableSchemaDefinitionPartitionKey"]]], jsii.get(self, "partitionKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="staticColumnInput")
    def static_column_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KeyspacesTableSchemaDefinitionStaticColumn"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KeyspacesTableSchemaDefinitionStaticColumn"]]], jsii.get(self, "staticColumnInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[KeyspacesTableSchemaDefinition]:
        return typing.cast(typing.Optional[KeyspacesTableSchemaDefinition], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KeyspacesTableSchemaDefinition],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14b0637e1ea9e84a7ed15b0737c670534ba5d62f57929f299ce5b2be1696bbc5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.keyspacesTable.KeyspacesTableSchemaDefinitionPartitionKey",
    jsii_struct_bases=[],
    name_mapping={"name": "name"},
)
class KeyspacesTableSchemaDefinitionPartitionKey:
    def __init__(self, *, name: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#name KeyspacesTable#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0bb7c958f7ae803c5ef9d3772976bbd629d6a4cb67a82499666ca53594f57f7f)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#name KeyspacesTable#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KeyspacesTableSchemaDefinitionPartitionKey(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KeyspacesTableSchemaDefinitionPartitionKeyList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.keyspacesTable.KeyspacesTableSchemaDefinitionPartitionKeyList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6fb20d5f8187eb3cec33129d1ca3b24ea60f32462d1a0a320da745279209a6de)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "KeyspacesTableSchemaDefinitionPartitionKeyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ee3e75b47c184aeca327aef4ae701de7881acb2c23e63582b142091d9b63e4b)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KeyspacesTableSchemaDefinitionPartitionKeyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b276a6fa173567ea60c2c32754d6611e0797ce7fdba101d94268db5e6458d4d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9890a19f16c876be50a147795f203ea6c5f8c035c2db947f883acba6ec1b3ec5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__78aa7d7495433657e718c8f59df755cc779c9d480382f280c0f8227483b50d73)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KeyspacesTableSchemaDefinitionPartitionKey]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KeyspacesTableSchemaDefinitionPartitionKey]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KeyspacesTableSchemaDefinitionPartitionKey]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f4da18d2724b8b38046300025d33a2ebcc85371405b6febc63eec29db6082ee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KeyspacesTableSchemaDefinitionPartitionKeyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.keyspacesTable.KeyspacesTableSchemaDefinitionPartitionKeyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__30ce2998c2fa17a76649719b44463eb414629ccc4d481db24549e97335a5f87a)
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
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b32aa9074228c1e9ed16796f44d741a1010dc8d33daca2ebaf350d742bcc33af)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[KeyspacesTableSchemaDefinitionPartitionKey, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[KeyspacesTableSchemaDefinitionPartitionKey, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[KeyspacesTableSchemaDefinitionPartitionKey, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cfb343b4a2eb09d34c70c5564843f97bc393216065c53c21d6e9a25d6649cd3a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.keyspacesTable.KeyspacesTableSchemaDefinitionStaticColumn",
    jsii_struct_bases=[],
    name_mapping={"name": "name"},
)
class KeyspacesTableSchemaDefinitionStaticColumn:
    def __init__(self, *, name: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#name KeyspacesTable#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2225227e40aeb7a3b9fb7260718ad082ad50731d2585c7550534f24dc9545b9)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#name KeyspacesTable#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KeyspacesTableSchemaDefinitionStaticColumn(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KeyspacesTableSchemaDefinitionStaticColumnList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.keyspacesTable.KeyspacesTableSchemaDefinitionStaticColumnList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f227bbf917640b381d51b8741152277690abd14ef27305a8c488cce3098a1731)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "KeyspacesTableSchemaDefinitionStaticColumnOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f8b0f1d7f1616f56abe80886b3c2f658a63fe42489ca8e436c897721c62573d)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KeyspacesTableSchemaDefinitionStaticColumnOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e63a78609c21a85432841c519dcf298ce108454ea92065e4cb5db5bb61e0ee3a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__be94342f5dba9184632c21065b9124827fbd22a1f7d287bbdd0cb49be561e5e5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f97ce585362fc30fc684a2015908822360bfa02d4fe41d1409583f126d23c351)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KeyspacesTableSchemaDefinitionStaticColumn]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KeyspacesTableSchemaDefinitionStaticColumn]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KeyspacesTableSchemaDefinitionStaticColumn]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58d4484f2d54661097d4d4b74ba587d7e1bfc8545c7bb21a6f88abb7bc0c47c4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KeyspacesTableSchemaDefinitionStaticColumnOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.keyspacesTable.KeyspacesTableSchemaDefinitionStaticColumnOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0cc9380442187db76a1577cdabf55dc17cddb8ce970c5220603f2eaf8f09d4eb)
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
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__992e93aec82dbc55569c6d85916e814b77110ee0c6b7ccd1d34be897e462cb94)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[KeyspacesTableSchemaDefinitionStaticColumn, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[KeyspacesTableSchemaDefinitionStaticColumn, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[KeyspacesTableSchemaDefinitionStaticColumn, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb344ca8f8bbe51993bc525b8ff77882a7776b3da120706410d1117bd75a0152)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.keyspacesTable.KeyspacesTableTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class KeyspacesTableTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#create KeyspacesTable#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#delete KeyspacesTable#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#update KeyspacesTable#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89b5433a3f405137c23f6d6682143d2e5d8cc6ea3edbdf6d7054ebe9a1389dab)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#create KeyspacesTable#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#delete KeyspacesTable#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#update KeyspacesTable#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KeyspacesTableTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KeyspacesTableTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.keyspacesTable.KeyspacesTableTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2107567a7badd7010e29bf3f4b726fa68582ce4f99dda4554fbde280671aa4ac)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @jsii.member(jsii_name="resetUpdate")
    def reset_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdate", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__348f806290d8a612b90b9888807e2cae4183e1aa06867fbb11b3d9e959453264)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb35b9822d066bfc0915b8db317d22366a253a6b8b68aee2d4166a8d9e8baca0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__afc08f36e1fbe1857d8c27272c78f37187ec950b2ef5f107dd0c3c008b872558)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[KeyspacesTableTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[KeyspacesTableTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[KeyspacesTableTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b845c32bb4ecd7d1541313a15f2f59bd4c9660fe17e6a00d049dabbf5b264fce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.keyspacesTable.KeyspacesTableTtl",
    jsii_struct_bases=[],
    name_mapping={"status": "status"},
)
class KeyspacesTableTtl:
    def __init__(self, *, status: builtins.str) -> None:
        '''
        :param status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#status KeyspacesTable#status}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__257ab20b6b01302eddd3330b14b5a3c7c9c987e2db9a82644d55ec05918a1390)
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "status": status,
        }

    @builtins.property
    def status(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#status KeyspacesTable#status}.'''
        result = self._values.get("status")
        assert result is not None, "Required property 'status' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KeyspacesTableTtl(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KeyspacesTableTtlOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.keyspacesTable.KeyspacesTableTtlOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__92c26b8e09f3fc06dd09b7934895b17a6d71b26c8115c0c087dc21af86b710fd)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="statusInput")
    def status_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statusInput"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @status.setter
    def status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8be5738b255e1a7e46630c3fa77cda50d5fecd9d27d524e5da623df67f369fd9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[KeyspacesTableTtl]:
        return typing.cast(typing.Optional[KeyspacesTableTtl], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[KeyspacesTableTtl]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1520afb75849e6683e9c1c593d5920b7a9e2a602378b559f08c0534b138902a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "KeyspacesTable",
    "KeyspacesTableCapacitySpecification",
    "KeyspacesTableCapacitySpecificationOutputReference",
    "KeyspacesTableComment",
    "KeyspacesTableCommentOutputReference",
    "KeyspacesTableConfig",
    "KeyspacesTableEncryptionSpecification",
    "KeyspacesTableEncryptionSpecificationOutputReference",
    "KeyspacesTablePointInTimeRecovery",
    "KeyspacesTablePointInTimeRecoveryOutputReference",
    "KeyspacesTableSchemaDefinition",
    "KeyspacesTableSchemaDefinitionClusteringKey",
    "KeyspacesTableSchemaDefinitionClusteringKeyList",
    "KeyspacesTableSchemaDefinitionClusteringKeyOutputReference",
    "KeyspacesTableSchemaDefinitionColumn",
    "KeyspacesTableSchemaDefinitionColumnList",
    "KeyspacesTableSchemaDefinitionColumnOutputReference",
    "KeyspacesTableSchemaDefinitionOutputReference",
    "KeyspacesTableSchemaDefinitionPartitionKey",
    "KeyspacesTableSchemaDefinitionPartitionKeyList",
    "KeyspacesTableSchemaDefinitionPartitionKeyOutputReference",
    "KeyspacesTableSchemaDefinitionStaticColumn",
    "KeyspacesTableSchemaDefinitionStaticColumnList",
    "KeyspacesTableSchemaDefinitionStaticColumnOutputReference",
    "KeyspacesTableTimeouts",
    "KeyspacesTableTimeoutsOutputReference",
    "KeyspacesTableTtl",
    "KeyspacesTableTtlOutputReference",
]

publication.publish()

def _typecheckingstub__b990ef3bd6e359d2e2ee531697caa7d9d74dacd42de2bf32f8efe0cd771d6dc4(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    keyspace_name: builtins.str,
    schema_definition: typing.Union[KeyspacesTableSchemaDefinition, typing.Dict[builtins.str, typing.Any]],
    table_name: builtins.str,
    capacity_specification: typing.Optional[typing.Union[KeyspacesTableCapacitySpecification, typing.Dict[builtins.str, typing.Any]]] = None,
    comment: typing.Optional[typing.Union[KeyspacesTableComment, typing.Dict[builtins.str, typing.Any]]] = None,
    default_time_to_live: typing.Optional[jsii.Number] = None,
    encryption_specification: typing.Optional[typing.Union[KeyspacesTableEncryptionSpecification, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    point_in_time_recovery: typing.Optional[typing.Union[KeyspacesTablePointInTimeRecovery, typing.Dict[builtins.str, typing.Any]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[KeyspacesTableTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    ttl: typing.Optional[typing.Union[KeyspacesTableTtl, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__7638875b13fa98fc3ba4f0a54df65fff60d5486dd89ccecec5474f3ffaeae8cb(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b08a5f4b98cf0f0342612904e19ea262e67c3bc133cf245efe3ee02f7e8fc5a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c08f91a29a7fb4594169eaa9a1aa6459bec76da642a4399b985b9d95539e9d6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aae9c6cc3a83c15ff274d379870e0bfafcc3cc392222fdbd48d6af3867493b73(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a2bb0942979a7b3e7ca4327bbc7e46477ae3b1fcfff38867adfb21c2187fe26(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e606535bd97f3b3eaf479aa486055275bfbc61b4861583b819567a23ec78f195(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e61c1675f1dd7cea14c7c82f05434faf403e55071d26f3f3651d782c871c39d(
    *,
    read_capacity_units: typing.Optional[jsii.Number] = None,
    throughput_mode: typing.Optional[builtins.str] = None,
    write_capacity_units: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__acc840395157fff65c8327d35ddd257f1a2b290dca5f33b66d77f883936d1328(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1dac35bd30fe7bba23ce8031d3036b920fbad68a2729e700fdbb6997031e58f(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab0c2cc06591f411041f498ec2f9dde11031a1bccd0308e6b11ee4afdab5910d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5c8f417a74555ad6fd23da655950a142456eccd3e3268506586976e5e4565f2(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__509eb9200687c22a3cd83cc087d72bd918e98a7cf2ae35e70812cadde0373438(
    value: typing.Optional[KeyspacesTableCapacitySpecification],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d71742ca2f8f7af4764855ea6a4be093d4a4d941b38c18fe514e32d9e4ad0bf(
    *,
    message: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1bffb69d15e0b90d3a480086760ca652a48a5b9b48f8955c96b10bf55b562f8f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ef930777e69709c77121866b78325721ab09075eeac620e0a05ebf1eef8125a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e639ab4c9176c1b10a0ca2bbb0548dcedcfaa8a0f3b9c2004333d864210c515(
    value: typing.Optional[KeyspacesTableComment],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a100d85574997370f4a0428f130762a098580232ccd53c289ea923585b371ec9(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    keyspace_name: builtins.str,
    schema_definition: typing.Union[KeyspacesTableSchemaDefinition, typing.Dict[builtins.str, typing.Any]],
    table_name: builtins.str,
    capacity_specification: typing.Optional[typing.Union[KeyspacesTableCapacitySpecification, typing.Dict[builtins.str, typing.Any]]] = None,
    comment: typing.Optional[typing.Union[KeyspacesTableComment, typing.Dict[builtins.str, typing.Any]]] = None,
    default_time_to_live: typing.Optional[jsii.Number] = None,
    encryption_specification: typing.Optional[typing.Union[KeyspacesTableEncryptionSpecification, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    point_in_time_recovery: typing.Optional[typing.Union[KeyspacesTablePointInTimeRecovery, typing.Dict[builtins.str, typing.Any]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[KeyspacesTableTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    ttl: typing.Optional[typing.Union[KeyspacesTableTtl, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c2ba84e03669802531d08e6573ed5360b9484d56497a87ebd6a05ce51a869c6(
    *,
    kms_key_identifier: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b9a90563cb6545f7d336e741b22cefd7f4e507c3f9c33ad8161b50eadb1e81b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7850788ed49de7fccdbf9913a1479d3153fe75325c1da5ed4c28f9f985211ac(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__febc4cba8fdf1ecc1efa253fdf15e95a92c964d31658d3abbc988c1b746852a2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20dfe5f55f114509475a5ae63fbe10aa73a7591c88bfe7e3d7bad60f55e443e6(
    value: typing.Optional[KeyspacesTableEncryptionSpecification],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__635182fd32823308cbdf1a49c1dbcd5d57718fcb1af8153a285d5e292396f9e9(
    *,
    status: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__913e46f4b3ee499bd2f3e3231d864894d00bed93dae0c7b2464f278fd96a5314(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3774d0127b943f6f1ecc30e7830dddc919219646e182dacad64387493c30cf27(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e1a96d6963aaca9074b04fbb598c0e751f7e1fa3c27f7252b4b8b3b1e6f2178(
    value: typing.Optional[KeyspacesTablePointInTimeRecovery],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__270e276fd809a21739c4d0355775ebfda3c0411be5d12cfe98396c265824d63e(
    *,
    column: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KeyspacesTableSchemaDefinitionColumn, typing.Dict[builtins.str, typing.Any]]]],
    partition_key: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KeyspacesTableSchemaDefinitionPartitionKey, typing.Dict[builtins.str, typing.Any]]]],
    clustering_key: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KeyspacesTableSchemaDefinitionClusteringKey, typing.Dict[builtins.str, typing.Any]]]]] = None,
    static_column: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KeyspacesTableSchemaDefinitionStaticColumn, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f44673376121c01b61f192c668d4b6b5a60ccd4bf905bbbdc3b51641a416ff2(
    *,
    name: builtins.str,
    order_by: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f80de0fb452ecab7cb9d2717f13a99ca9ccad3d2e69cd8c921c0d41aec5c5d9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a2d54ba448a1d730d0b319b29eeb2bd73f229369556b6f1804cafa6994e9ac6(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__464d590bab66efeeb72849e5122a6281e335cfe21bc4c1732688d1884bd4c30f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aecd9cde9fe6307892efa42ad854ddcd66b47521f20047e10259dd54b2c29b22(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__909d79206a5560ec228e1916b40aa0713a42c97b417eb37844b9f698e87bdbe7(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b091385059f714a8edd5be6a84b8a526e4f4e54fc27e0335a586121a5d97d33(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KeyspacesTableSchemaDefinitionClusteringKey]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77340753be4170e665fb5e5da18e3f79fd5088aedf8e916fa77c90333541ca49(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb55f748d93bdf61e862aea322b31e4bfb709a128f1862566edf1493a567d761(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d9d0dc8c3ed6db09db3e5d8f56efcd24dadf53f1e4c3a93c1f6eee0d05253eb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__436be81d7f99a3d333ea1914f8e6e5eec98c6cb23bbd8f185db379d6a030cd1c(
    value: typing.Optional[typing.Union[KeyspacesTableSchemaDefinitionClusteringKey, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02f2f37ffa67de2a54308b0ea5a9c43932566d5af2ff7afbd25cb5a602e846de(
    *,
    name: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9c3c0ba76f130ac0775271284937cd43d07f42e04d27f021722e84b80741e1a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64a2debf9ca48bcb6b7ca6c7a624a2ddc212653b12519c23457105f7530192e6(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ddd8c2ff1d3ff082038ececdaa5f288d21e6c70029444c20aaed89b4e0841a2a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4cd9da13b2804ce0fe9f6236078e4a832151dde0503ebb34378d9e1f06bb020e(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8526a98789519821d65ba5ae763fb7ac41ff64aab36dc32d173cf8c1d58f795(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e6c78c0741cde86212e5caa38263025762a48902b97b2772f566fae120c55e3(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KeyspacesTableSchemaDefinitionColumn]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a201076b52fcd481968629fbc3c0619c66d3d892e721addb0b90171573e8b2d5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9924a2c71b49baedef1ccfd6fb914f41b088b161b2cce3220cacdac6ea4b9fbd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4bb45ae69d4e47d368e5020459b8b121f581b1a73d95a0f56865a42a9d9b54ce(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a12f8040a52f600dd0538e5fce752e8cb1b8b436450a7dde71b8abca501428c(
    value: typing.Optional[typing.Union[KeyspacesTableSchemaDefinitionColumn, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb5fb43828bdb743e9795571ae17107c17663d7577a846a0eb8b4d6bdac90660(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6337acb8dce8f30a4cc85b466246886b1287c735ac23da257fd7592f963fc2dc(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KeyspacesTableSchemaDefinitionClusteringKey, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4760b03e4977baef03ef218e0b135134b009c68d53d91c658134284d12b3a07(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KeyspacesTableSchemaDefinitionColumn, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e541a67bd266fd594f6bdd7e0a4e9c59d09e539629303f549f17d52c0f1f48ea(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KeyspacesTableSchemaDefinitionPartitionKey, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a18bc376f6b9437f6d69d6dd387fda7bfb71d63f3a28ae82fbc62ae1fa602e88(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KeyspacesTableSchemaDefinitionStaticColumn, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14b0637e1ea9e84a7ed15b0737c670534ba5d62f57929f299ce5b2be1696bbc5(
    value: typing.Optional[KeyspacesTableSchemaDefinition],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0bb7c958f7ae803c5ef9d3772976bbd629d6a4cb67a82499666ca53594f57f7f(
    *,
    name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6fb20d5f8187eb3cec33129d1ca3b24ea60f32462d1a0a320da745279209a6de(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ee3e75b47c184aeca327aef4ae701de7881acb2c23e63582b142091d9b63e4b(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b276a6fa173567ea60c2c32754d6611e0797ce7fdba101d94268db5e6458d4d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9890a19f16c876be50a147795f203ea6c5f8c035c2db947f883acba6ec1b3ec5(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78aa7d7495433657e718c8f59df755cc779c9d480382f280c0f8227483b50d73(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f4da18d2724b8b38046300025d33a2ebcc85371405b6febc63eec29db6082ee(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KeyspacesTableSchemaDefinitionPartitionKey]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30ce2998c2fa17a76649719b44463eb414629ccc4d481db24549e97335a5f87a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b32aa9074228c1e9ed16796f44d741a1010dc8d33daca2ebaf350d742bcc33af(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfb343b4a2eb09d34c70c5564843f97bc393216065c53c21d6e9a25d6649cd3a(
    value: typing.Optional[typing.Union[KeyspacesTableSchemaDefinitionPartitionKey, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2225227e40aeb7a3b9fb7260718ad082ad50731d2585c7550534f24dc9545b9(
    *,
    name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f227bbf917640b381d51b8741152277690abd14ef27305a8c488cce3098a1731(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f8b0f1d7f1616f56abe80886b3c2f658a63fe42489ca8e436c897721c62573d(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e63a78609c21a85432841c519dcf298ce108454ea92065e4cb5db5bb61e0ee3a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be94342f5dba9184632c21065b9124827fbd22a1f7d287bbdd0cb49be561e5e5(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f97ce585362fc30fc684a2015908822360bfa02d4fe41d1409583f126d23c351(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58d4484f2d54661097d4d4b74ba587d7e1bfc8545c7bb21a6f88abb7bc0c47c4(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KeyspacesTableSchemaDefinitionStaticColumn]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0cc9380442187db76a1577cdabf55dc17cddb8ce970c5220603f2eaf8f09d4eb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__992e93aec82dbc55569c6d85916e814b77110ee0c6b7ccd1d34be897e462cb94(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb344ca8f8bbe51993bc525b8ff77882a7776b3da120706410d1117bd75a0152(
    value: typing.Optional[typing.Union[KeyspacesTableSchemaDefinitionStaticColumn, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89b5433a3f405137c23f6d6682143d2e5d8cc6ea3edbdf6d7054ebe9a1389dab(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2107567a7badd7010e29bf3f4b726fa68582ce4f99dda4554fbde280671aa4ac(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__348f806290d8a612b90b9888807e2cae4183e1aa06867fbb11b3d9e959453264(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb35b9822d066bfc0915b8db317d22366a253a6b8b68aee2d4166a8d9e8baca0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afc08f36e1fbe1857d8c27272c78f37187ec950b2ef5f107dd0c3c008b872558(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b845c32bb4ecd7d1541313a15f2f59bd4c9660fe17e6a00d049dabbf5b264fce(
    value: typing.Optional[typing.Union[KeyspacesTableTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__257ab20b6b01302eddd3330b14b5a3c7c9c987e2db9a82644d55ec05918a1390(
    *,
    status: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92c26b8e09f3fc06dd09b7934895b17a6d71b26c8115c0c087dc21af86b710fd(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8be5738b255e1a7e46630c3fa77cda50d5fecd9d27d524e5da623df67f369fd9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1520afb75849e6683e9c1c593d5920b7a9e2a602378b559f08c0534b138902a(
    value: typing.Optional[KeyspacesTableTtl],
) -> None:
    """Type checking stubs"""
    pass
