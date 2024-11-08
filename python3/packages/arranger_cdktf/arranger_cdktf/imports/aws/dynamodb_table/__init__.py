'''
# `aws_dynamodb_table`

Refer to the Terraform Registory for docs: [`aws_dynamodb_table`](https://www.terraform.io/docs/providers/aws/r/dynamodb_table).
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


class DynamodbTable(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dynamodbTable.DynamodbTable",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table aws_dynamodb_table}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        attribute: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DynamodbTableAttribute", typing.Dict[builtins.str, typing.Any]]]]] = None,
        billing_mode: typing.Optional[builtins.str] = None,
        global_secondary_index: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DynamodbTableGlobalSecondaryIndex", typing.Dict[builtins.str, typing.Any]]]]] = None,
        hash_key: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        local_secondary_index: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DynamodbTableLocalSecondaryIndex", typing.Dict[builtins.str, typing.Any]]]]] = None,
        point_in_time_recovery: typing.Optional[typing.Union["DynamodbTablePointInTimeRecovery", typing.Dict[builtins.str, typing.Any]]] = None,
        range_key: typing.Optional[builtins.str] = None,
        read_capacity: typing.Optional[jsii.Number] = None,
        replica: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DynamodbTableReplica", typing.Dict[builtins.str, typing.Any]]]]] = None,
        restore_date_time: typing.Optional[builtins.str] = None,
        restore_source_name: typing.Optional[builtins.str] = None,
        restore_to_latest_time: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        server_side_encryption: typing.Optional[typing.Union["DynamodbTableServerSideEncryption", typing.Dict[builtins.str, typing.Any]]] = None,
        stream_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        stream_view_type: typing.Optional[builtins.str] = None,
        table_class: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["DynamodbTableTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        ttl: typing.Optional[typing.Union["DynamodbTableTtl", typing.Dict[builtins.str, typing.Any]]] = None,
        write_capacity: typing.Optional[jsii.Number] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table aws_dynamodb_table} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#name DynamodbTable#name}.
        :param attribute: attribute block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#attribute DynamodbTable#attribute}
        :param billing_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#billing_mode DynamodbTable#billing_mode}.
        :param global_secondary_index: global_secondary_index block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#global_secondary_index DynamodbTable#global_secondary_index}
        :param hash_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#hash_key DynamodbTable#hash_key}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#id DynamodbTable#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param local_secondary_index: local_secondary_index block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#local_secondary_index DynamodbTable#local_secondary_index}
        :param point_in_time_recovery: point_in_time_recovery block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#point_in_time_recovery DynamodbTable#point_in_time_recovery}
        :param range_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#range_key DynamodbTable#range_key}.
        :param read_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#read_capacity DynamodbTable#read_capacity}.
        :param replica: replica block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#replica DynamodbTable#replica}
        :param restore_date_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#restore_date_time DynamodbTable#restore_date_time}.
        :param restore_source_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#restore_source_name DynamodbTable#restore_source_name}.
        :param restore_to_latest_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#restore_to_latest_time DynamodbTable#restore_to_latest_time}.
        :param server_side_encryption: server_side_encryption block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#server_side_encryption DynamodbTable#server_side_encryption}
        :param stream_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#stream_enabled DynamodbTable#stream_enabled}.
        :param stream_view_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#stream_view_type DynamodbTable#stream_view_type}.
        :param table_class: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#table_class DynamodbTable#table_class}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#tags DynamodbTable#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#tags_all DynamodbTable#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#timeouts DynamodbTable#timeouts}
        :param ttl: ttl block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#ttl DynamodbTable#ttl}
        :param write_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#write_capacity DynamodbTable#write_capacity}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__195cebc3a317b1c8a35f9a17d5a50f1ec737abd62fd14599da6268dec9f51a03)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DynamodbTableConfig(
            name=name,
            attribute=attribute,
            billing_mode=billing_mode,
            global_secondary_index=global_secondary_index,
            hash_key=hash_key,
            id=id,
            local_secondary_index=local_secondary_index,
            point_in_time_recovery=point_in_time_recovery,
            range_key=range_key,
            read_capacity=read_capacity,
            replica=replica,
            restore_date_time=restore_date_time,
            restore_source_name=restore_source_name,
            restore_to_latest_time=restore_to_latest_time,
            server_side_encryption=server_side_encryption,
            stream_enabled=stream_enabled,
            stream_view_type=stream_view_type,
            table_class=table_class,
            tags=tags,
            tags_all=tags_all,
            timeouts=timeouts,
            ttl=ttl,
            write_capacity=write_capacity,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAttribute")
    def put_attribute(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DynamodbTableAttribute", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e6f9706b27b4d89f553d2ce789cad1e288cb1266ea3824c25882eeb6857508c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAttribute", [value]))

    @jsii.member(jsii_name="putGlobalSecondaryIndex")
    def put_global_secondary_index(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DynamodbTableGlobalSecondaryIndex", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15af35b4b616a51fa0f36cfbe333a1e1af3840473f91c289a389f3ddc8eecb3b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putGlobalSecondaryIndex", [value]))

    @jsii.member(jsii_name="putLocalSecondaryIndex")
    def put_local_secondary_index(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DynamodbTableLocalSecondaryIndex", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d87705e1ac3a40bd6585db376affdcc340c305318228db563d7e79851fcb82b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLocalSecondaryIndex", [value]))

    @jsii.member(jsii_name="putPointInTimeRecovery")
    def put_point_in_time_recovery(
        self,
        *,
        enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#enabled DynamodbTable#enabled}.
        '''
        value = DynamodbTablePointInTimeRecovery(enabled=enabled)

        return typing.cast(None, jsii.invoke(self, "putPointInTimeRecovery", [value]))

    @jsii.member(jsii_name="putReplica")
    def put_replica(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DynamodbTableReplica", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b9c238f7260bb1d3c2929ca54322fdd86a17415e03c151080273e625dc2e0b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putReplica", [value]))

    @jsii.member(jsii_name="putServerSideEncryption")
    def put_server_side_encryption(
        self,
        *,
        enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        kms_key_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#enabled DynamodbTable#enabled}.
        :param kms_key_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#kms_key_arn DynamodbTable#kms_key_arn}.
        '''
        value = DynamodbTableServerSideEncryption(
            enabled=enabled, kms_key_arn=kms_key_arn
        )

        return typing.cast(None, jsii.invoke(self, "putServerSideEncryption", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#create DynamodbTable#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#delete DynamodbTable#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#update DynamodbTable#update}.
        '''
        value = DynamodbTableTimeouts(create=create, delete=delete, update=update)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putTtl")
    def put_ttl(
        self,
        *,
        attribute_name: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param attribute_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#attribute_name DynamodbTable#attribute_name}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#enabled DynamodbTable#enabled}.
        '''
        value = DynamodbTableTtl(attribute_name=attribute_name, enabled=enabled)

        return typing.cast(None, jsii.invoke(self, "putTtl", [value]))

    @jsii.member(jsii_name="resetAttribute")
    def reset_attribute(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAttribute", []))

    @jsii.member(jsii_name="resetBillingMode")
    def reset_billing_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBillingMode", []))

    @jsii.member(jsii_name="resetGlobalSecondaryIndex")
    def reset_global_secondary_index(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGlobalSecondaryIndex", []))

    @jsii.member(jsii_name="resetHashKey")
    def reset_hash_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHashKey", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLocalSecondaryIndex")
    def reset_local_secondary_index(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocalSecondaryIndex", []))

    @jsii.member(jsii_name="resetPointInTimeRecovery")
    def reset_point_in_time_recovery(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPointInTimeRecovery", []))

    @jsii.member(jsii_name="resetRangeKey")
    def reset_range_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRangeKey", []))

    @jsii.member(jsii_name="resetReadCapacity")
    def reset_read_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadCapacity", []))

    @jsii.member(jsii_name="resetReplica")
    def reset_replica(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReplica", []))

    @jsii.member(jsii_name="resetRestoreDateTime")
    def reset_restore_date_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRestoreDateTime", []))

    @jsii.member(jsii_name="resetRestoreSourceName")
    def reset_restore_source_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRestoreSourceName", []))

    @jsii.member(jsii_name="resetRestoreToLatestTime")
    def reset_restore_to_latest_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRestoreToLatestTime", []))

    @jsii.member(jsii_name="resetServerSideEncryption")
    def reset_server_side_encryption(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServerSideEncryption", []))

    @jsii.member(jsii_name="resetStreamEnabled")
    def reset_stream_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStreamEnabled", []))

    @jsii.member(jsii_name="resetStreamViewType")
    def reset_stream_view_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStreamViewType", []))

    @jsii.member(jsii_name="resetTableClass")
    def reset_table_class(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTableClass", []))

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

    @jsii.member(jsii_name="resetWriteCapacity")
    def reset_write_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWriteCapacity", []))

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
    @jsii.member(jsii_name="attribute")
    def attribute(self) -> "DynamodbTableAttributeList":
        return typing.cast("DynamodbTableAttributeList", jsii.get(self, "attribute"))

    @builtins.property
    @jsii.member(jsii_name="globalSecondaryIndex")
    def global_secondary_index(self) -> "DynamodbTableGlobalSecondaryIndexList":
        return typing.cast("DynamodbTableGlobalSecondaryIndexList", jsii.get(self, "globalSecondaryIndex"))

    @builtins.property
    @jsii.member(jsii_name="localSecondaryIndex")
    def local_secondary_index(self) -> "DynamodbTableLocalSecondaryIndexList":
        return typing.cast("DynamodbTableLocalSecondaryIndexList", jsii.get(self, "localSecondaryIndex"))

    @builtins.property
    @jsii.member(jsii_name="pointInTimeRecovery")
    def point_in_time_recovery(
        self,
    ) -> "DynamodbTablePointInTimeRecoveryOutputReference":
        return typing.cast("DynamodbTablePointInTimeRecoveryOutputReference", jsii.get(self, "pointInTimeRecovery"))

    @builtins.property
    @jsii.member(jsii_name="replica")
    def replica(self) -> "DynamodbTableReplicaList":
        return typing.cast("DynamodbTableReplicaList", jsii.get(self, "replica"))

    @builtins.property
    @jsii.member(jsii_name="serverSideEncryption")
    def server_side_encryption(
        self,
    ) -> "DynamodbTableServerSideEncryptionOutputReference":
        return typing.cast("DynamodbTableServerSideEncryptionOutputReference", jsii.get(self, "serverSideEncryption"))

    @builtins.property
    @jsii.member(jsii_name="streamArn")
    def stream_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "streamArn"))

    @builtins.property
    @jsii.member(jsii_name="streamLabel")
    def stream_label(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "streamLabel"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "DynamodbTableTimeoutsOutputReference":
        return typing.cast("DynamodbTableTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="ttl")
    def ttl(self) -> "DynamodbTableTtlOutputReference":
        return typing.cast("DynamodbTableTtlOutputReference", jsii.get(self, "ttl"))

    @builtins.property
    @jsii.member(jsii_name="attributeInput")
    def attribute_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DynamodbTableAttribute"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DynamodbTableAttribute"]]], jsii.get(self, "attributeInput"))

    @builtins.property
    @jsii.member(jsii_name="billingModeInput")
    def billing_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "billingModeInput"))

    @builtins.property
    @jsii.member(jsii_name="globalSecondaryIndexInput")
    def global_secondary_index_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DynamodbTableGlobalSecondaryIndex"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DynamodbTableGlobalSecondaryIndex"]]], jsii.get(self, "globalSecondaryIndexInput"))

    @builtins.property
    @jsii.member(jsii_name="hashKeyInput")
    def hash_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hashKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="localSecondaryIndexInput")
    def local_secondary_index_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DynamodbTableLocalSecondaryIndex"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DynamodbTableLocalSecondaryIndex"]]], jsii.get(self, "localSecondaryIndexInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="pointInTimeRecoveryInput")
    def point_in_time_recovery_input(
        self,
    ) -> typing.Optional["DynamodbTablePointInTimeRecovery"]:
        return typing.cast(typing.Optional["DynamodbTablePointInTimeRecovery"], jsii.get(self, "pointInTimeRecoveryInput"))

    @builtins.property
    @jsii.member(jsii_name="rangeKeyInput")
    def range_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rangeKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="readCapacityInput")
    def read_capacity_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "readCapacityInput"))

    @builtins.property
    @jsii.member(jsii_name="replicaInput")
    def replica_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DynamodbTableReplica"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DynamodbTableReplica"]]], jsii.get(self, "replicaInput"))

    @builtins.property
    @jsii.member(jsii_name="restoreDateTimeInput")
    def restore_date_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "restoreDateTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="restoreSourceNameInput")
    def restore_source_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "restoreSourceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="restoreToLatestTimeInput")
    def restore_to_latest_time_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "restoreToLatestTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="serverSideEncryptionInput")
    def server_side_encryption_input(
        self,
    ) -> typing.Optional["DynamodbTableServerSideEncryption"]:
        return typing.cast(typing.Optional["DynamodbTableServerSideEncryption"], jsii.get(self, "serverSideEncryptionInput"))

    @builtins.property
    @jsii.member(jsii_name="streamEnabledInput")
    def stream_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "streamEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="streamViewTypeInput")
    def stream_view_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "streamViewTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="tableClassInput")
    def table_class_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tableClassInput"))

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
    ) -> typing.Optional[typing.Union["DynamodbTableTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["DynamodbTableTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="ttlInput")
    def ttl_input(self) -> typing.Optional["DynamodbTableTtl"]:
        return typing.cast(typing.Optional["DynamodbTableTtl"], jsii.get(self, "ttlInput"))

    @builtins.property
    @jsii.member(jsii_name="writeCapacityInput")
    def write_capacity_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "writeCapacityInput"))

    @builtins.property
    @jsii.member(jsii_name="billingMode")
    def billing_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "billingMode"))

    @billing_mode.setter
    def billing_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__536518bb65083cb1c6e142b614c52eff0a5e4702b8f86972e4c3c8b97f13d400)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "billingMode", value)

    @builtins.property
    @jsii.member(jsii_name="hashKey")
    def hash_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hashKey"))

    @hash_key.setter
    def hash_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15c69111e07b835b3bc0f081277f4a7b58f748626355a943c92e618f6bc61f00)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hashKey", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd5e1af684c1b15ef054e19abd124009823c767f7b989e771304f7ae215a30de)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c158abe44aa0c29e152cd46d283691e364b1ae0a6d5d4b332a527d39b5a99cd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="rangeKey")
    def range_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rangeKey"))

    @range_key.setter
    def range_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b2a44e866c33c60f9eab3638a95b498acf56808423b93d0301df130e26c346c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rangeKey", value)

    @builtins.property
    @jsii.member(jsii_name="readCapacity")
    def read_capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "readCapacity"))

    @read_capacity.setter
    def read_capacity(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__90205c51f054bda807cdb1d473e312d44415fcbac4149ef177af47f5d77fc3b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="restoreDateTime")
    def restore_date_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "restoreDateTime"))

    @restore_date_time.setter
    def restore_date_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d4303dde9957a3a50f87dc861e632e2e0a62cd2f05ae90639be5d503f83bd85)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "restoreDateTime", value)

    @builtins.property
    @jsii.member(jsii_name="restoreSourceName")
    def restore_source_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "restoreSourceName"))

    @restore_source_name.setter
    def restore_source_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a29e548b4b3319076f7d4d2f3e316ca20b963e27a79e97a193e7a7f9d0b2a32b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "restoreSourceName", value)

    @builtins.property
    @jsii.member(jsii_name="restoreToLatestTime")
    def restore_to_latest_time(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "restoreToLatestTime"))

    @restore_to_latest_time.setter
    def restore_to_latest_time(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78196ff02db2e4ba1420035556a114260ad7ec451887148be663c90294fb37ef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "restoreToLatestTime", value)

    @builtins.property
    @jsii.member(jsii_name="streamEnabled")
    def stream_enabled(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "streamEnabled"))

    @stream_enabled.setter
    def stream_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d62033ae459affb6e7447225a46245401ddf0bbf6cca71d8b239c4182701700)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "streamEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="streamViewType")
    def stream_view_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "streamViewType"))

    @stream_view_type.setter
    def stream_view_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be57d3674070ec4631108065f28d6cbb8a11cb01e66edc00f52dceab5c8be82b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "streamViewType", value)

    @builtins.property
    @jsii.member(jsii_name="tableClass")
    def table_class(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tableClass"))

    @table_class.setter
    def table_class(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad9a2b0d2fb37f05e8400bd99478638824a46bac45c3c933fd63f87a66de17c0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tableClass", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e35fd75ca431a9dd29057bc922db58bea97404303e110c5cfb5296d6585cedc3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3663aa3932f0f5abf28d1b6a09aaa1792b486e8155f8ff6d38826d9432ae2f05)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)

    @builtins.property
    @jsii.member(jsii_name="writeCapacity")
    def write_capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "writeCapacity"))

    @write_capacity.setter
    def write_capacity(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66019203adce417e3d18126479c16792493e6df9dbe9197a1150c3c386a9e638)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "writeCapacity", value)


@jsii.data_type(
    jsii_type="aws.dynamodbTable.DynamodbTableAttribute",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "type": "type"},
)
class DynamodbTableAttribute:
    def __init__(self, *, name: builtins.str, type: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#name DynamodbTable#name}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#type DynamodbTable#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6af99b1c929e1307d7ffbd969ad9856ae0cf036431d757886d7df9941eebe208)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "type": type,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#name DynamodbTable#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#type DynamodbTable#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DynamodbTableAttribute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DynamodbTableAttributeList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dynamodbTable.DynamodbTableAttributeList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9159773d5b6f4f62d467d6296c603e0f51f057dab4e4eca1af269c71a2c11ee2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "DynamodbTableAttributeOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__101759bed407fd8a326a1ee2c700174f313e8074279539966609bba6a82269ea)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DynamodbTableAttributeOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__868bfe6b1196af921c3c0b95523a8da388b3a65bc8c1acf3721f4a99134cd863)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c245336d4cb6d78e05455959d1f19427c3779a9d7fe8749a48eb46d4f20bf06d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__50ff46daff0193ea702f3bd4fba47f4061e05329d1f2dbca8de3d4dae19a47c0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DynamodbTableAttribute]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DynamodbTableAttribute]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DynamodbTableAttribute]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f5bc26d9a77116ad1484e0c653d11cfe611334b7ba1e924c9e9db750ee59df18)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DynamodbTableAttributeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dynamodbTable.DynamodbTableAttributeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5eb27d13cb54cc35bf5fe3d0fdb4a0e44eb354b2ac23301501d0a5c213ff3df5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__523aa8084580509128c8383e0539ef80db195892202f8b33c5cebfe707030ef0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cbb50ffc145bea4a4497398bea2de25ac06328aa806cb03ce78dd23c629ea910)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DynamodbTableAttribute, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DynamodbTableAttribute, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DynamodbTableAttribute, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7815dbb1e475697f35c76c4eab7759251a5c4722b743ef293693a8b816755732)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.dynamodbTable.DynamodbTableConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "name": "name",
        "attribute": "attribute",
        "billing_mode": "billingMode",
        "global_secondary_index": "globalSecondaryIndex",
        "hash_key": "hashKey",
        "id": "id",
        "local_secondary_index": "localSecondaryIndex",
        "point_in_time_recovery": "pointInTimeRecovery",
        "range_key": "rangeKey",
        "read_capacity": "readCapacity",
        "replica": "replica",
        "restore_date_time": "restoreDateTime",
        "restore_source_name": "restoreSourceName",
        "restore_to_latest_time": "restoreToLatestTime",
        "server_side_encryption": "serverSideEncryption",
        "stream_enabled": "streamEnabled",
        "stream_view_type": "streamViewType",
        "table_class": "tableClass",
        "tags": "tags",
        "tags_all": "tagsAll",
        "timeouts": "timeouts",
        "ttl": "ttl",
        "write_capacity": "writeCapacity",
    },
)
class DynamodbTableConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        name: builtins.str,
        attribute: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DynamodbTableAttribute, typing.Dict[builtins.str, typing.Any]]]]] = None,
        billing_mode: typing.Optional[builtins.str] = None,
        global_secondary_index: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DynamodbTableGlobalSecondaryIndex", typing.Dict[builtins.str, typing.Any]]]]] = None,
        hash_key: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        local_secondary_index: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DynamodbTableLocalSecondaryIndex", typing.Dict[builtins.str, typing.Any]]]]] = None,
        point_in_time_recovery: typing.Optional[typing.Union["DynamodbTablePointInTimeRecovery", typing.Dict[builtins.str, typing.Any]]] = None,
        range_key: typing.Optional[builtins.str] = None,
        read_capacity: typing.Optional[jsii.Number] = None,
        replica: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DynamodbTableReplica", typing.Dict[builtins.str, typing.Any]]]]] = None,
        restore_date_time: typing.Optional[builtins.str] = None,
        restore_source_name: typing.Optional[builtins.str] = None,
        restore_to_latest_time: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        server_side_encryption: typing.Optional[typing.Union["DynamodbTableServerSideEncryption", typing.Dict[builtins.str, typing.Any]]] = None,
        stream_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        stream_view_type: typing.Optional[builtins.str] = None,
        table_class: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["DynamodbTableTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        ttl: typing.Optional[typing.Union["DynamodbTableTtl", typing.Dict[builtins.str, typing.Any]]] = None,
        write_capacity: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#name DynamodbTable#name}.
        :param attribute: attribute block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#attribute DynamodbTable#attribute}
        :param billing_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#billing_mode DynamodbTable#billing_mode}.
        :param global_secondary_index: global_secondary_index block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#global_secondary_index DynamodbTable#global_secondary_index}
        :param hash_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#hash_key DynamodbTable#hash_key}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#id DynamodbTable#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param local_secondary_index: local_secondary_index block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#local_secondary_index DynamodbTable#local_secondary_index}
        :param point_in_time_recovery: point_in_time_recovery block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#point_in_time_recovery DynamodbTable#point_in_time_recovery}
        :param range_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#range_key DynamodbTable#range_key}.
        :param read_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#read_capacity DynamodbTable#read_capacity}.
        :param replica: replica block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#replica DynamodbTable#replica}
        :param restore_date_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#restore_date_time DynamodbTable#restore_date_time}.
        :param restore_source_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#restore_source_name DynamodbTable#restore_source_name}.
        :param restore_to_latest_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#restore_to_latest_time DynamodbTable#restore_to_latest_time}.
        :param server_side_encryption: server_side_encryption block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#server_side_encryption DynamodbTable#server_side_encryption}
        :param stream_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#stream_enabled DynamodbTable#stream_enabled}.
        :param stream_view_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#stream_view_type DynamodbTable#stream_view_type}.
        :param table_class: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#table_class DynamodbTable#table_class}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#tags DynamodbTable#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#tags_all DynamodbTable#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#timeouts DynamodbTable#timeouts}
        :param ttl: ttl block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#ttl DynamodbTable#ttl}
        :param write_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#write_capacity DynamodbTable#write_capacity}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(point_in_time_recovery, dict):
            point_in_time_recovery = DynamodbTablePointInTimeRecovery(**point_in_time_recovery)
        if isinstance(server_side_encryption, dict):
            server_side_encryption = DynamodbTableServerSideEncryption(**server_side_encryption)
        if isinstance(timeouts, dict):
            timeouts = DynamodbTableTimeouts(**timeouts)
        if isinstance(ttl, dict):
            ttl = DynamodbTableTtl(**ttl)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__350f895c7dc5f8832f7fc64a998e67e41b6f2e2670a71dd18a81ecb55b6a9edb)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument attribute", value=attribute, expected_type=type_hints["attribute"])
            check_type(argname="argument billing_mode", value=billing_mode, expected_type=type_hints["billing_mode"])
            check_type(argname="argument global_secondary_index", value=global_secondary_index, expected_type=type_hints["global_secondary_index"])
            check_type(argname="argument hash_key", value=hash_key, expected_type=type_hints["hash_key"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument local_secondary_index", value=local_secondary_index, expected_type=type_hints["local_secondary_index"])
            check_type(argname="argument point_in_time_recovery", value=point_in_time_recovery, expected_type=type_hints["point_in_time_recovery"])
            check_type(argname="argument range_key", value=range_key, expected_type=type_hints["range_key"])
            check_type(argname="argument read_capacity", value=read_capacity, expected_type=type_hints["read_capacity"])
            check_type(argname="argument replica", value=replica, expected_type=type_hints["replica"])
            check_type(argname="argument restore_date_time", value=restore_date_time, expected_type=type_hints["restore_date_time"])
            check_type(argname="argument restore_source_name", value=restore_source_name, expected_type=type_hints["restore_source_name"])
            check_type(argname="argument restore_to_latest_time", value=restore_to_latest_time, expected_type=type_hints["restore_to_latest_time"])
            check_type(argname="argument server_side_encryption", value=server_side_encryption, expected_type=type_hints["server_side_encryption"])
            check_type(argname="argument stream_enabled", value=stream_enabled, expected_type=type_hints["stream_enabled"])
            check_type(argname="argument stream_view_type", value=stream_view_type, expected_type=type_hints["stream_view_type"])
            check_type(argname="argument table_class", value=table_class, expected_type=type_hints["table_class"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument ttl", value=ttl, expected_type=type_hints["ttl"])
            check_type(argname="argument write_capacity", value=write_capacity, expected_type=type_hints["write_capacity"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
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
        if attribute is not None:
            self._values["attribute"] = attribute
        if billing_mode is not None:
            self._values["billing_mode"] = billing_mode
        if global_secondary_index is not None:
            self._values["global_secondary_index"] = global_secondary_index
        if hash_key is not None:
            self._values["hash_key"] = hash_key
        if id is not None:
            self._values["id"] = id
        if local_secondary_index is not None:
            self._values["local_secondary_index"] = local_secondary_index
        if point_in_time_recovery is not None:
            self._values["point_in_time_recovery"] = point_in_time_recovery
        if range_key is not None:
            self._values["range_key"] = range_key
        if read_capacity is not None:
            self._values["read_capacity"] = read_capacity
        if replica is not None:
            self._values["replica"] = replica
        if restore_date_time is not None:
            self._values["restore_date_time"] = restore_date_time
        if restore_source_name is not None:
            self._values["restore_source_name"] = restore_source_name
        if restore_to_latest_time is not None:
            self._values["restore_to_latest_time"] = restore_to_latest_time
        if server_side_encryption is not None:
            self._values["server_side_encryption"] = server_side_encryption
        if stream_enabled is not None:
            self._values["stream_enabled"] = stream_enabled
        if stream_view_type is not None:
            self._values["stream_view_type"] = stream_view_type
        if table_class is not None:
            self._values["table_class"] = table_class
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if ttl is not None:
            self._values["ttl"] = ttl
        if write_capacity is not None:
            self._values["write_capacity"] = write_capacity

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
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#name DynamodbTable#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def attribute(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DynamodbTableAttribute]]]:
        '''attribute block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#attribute DynamodbTable#attribute}
        '''
        result = self._values.get("attribute")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DynamodbTableAttribute]]], result)

    @builtins.property
    def billing_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#billing_mode DynamodbTable#billing_mode}.'''
        result = self._values.get("billing_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def global_secondary_index(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DynamodbTableGlobalSecondaryIndex"]]]:
        '''global_secondary_index block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#global_secondary_index DynamodbTable#global_secondary_index}
        '''
        result = self._values.get("global_secondary_index")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DynamodbTableGlobalSecondaryIndex"]]], result)

    @builtins.property
    def hash_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#hash_key DynamodbTable#hash_key}.'''
        result = self._values.get("hash_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#id DynamodbTable#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def local_secondary_index(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DynamodbTableLocalSecondaryIndex"]]]:
        '''local_secondary_index block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#local_secondary_index DynamodbTable#local_secondary_index}
        '''
        result = self._values.get("local_secondary_index")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DynamodbTableLocalSecondaryIndex"]]], result)

    @builtins.property
    def point_in_time_recovery(
        self,
    ) -> typing.Optional["DynamodbTablePointInTimeRecovery"]:
        '''point_in_time_recovery block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#point_in_time_recovery DynamodbTable#point_in_time_recovery}
        '''
        result = self._values.get("point_in_time_recovery")
        return typing.cast(typing.Optional["DynamodbTablePointInTimeRecovery"], result)

    @builtins.property
    def range_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#range_key DynamodbTable#range_key}.'''
        result = self._values.get("range_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read_capacity(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#read_capacity DynamodbTable#read_capacity}.'''
        result = self._values.get("read_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def replica(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DynamodbTableReplica"]]]:
        '''replica block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#replica DynamodbTable#replica}
        '''
        result = self._values.get("replica")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DynamodbTableReplica"]]], result)

    @builtins.property
    def restore_date_time(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#restore_date_time DynamodbTable#restore_date_time}.'''
        result = self._values.get("restore_date_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def restore_source_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#restore_source_name DynamodbTable#restore_source_name}.'''
        result = self._values.get("restore_source_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def restore_to_latest_time(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#restore_to_latest_time DynamodbTable#restore_to_latest_time}.'''
        result = self._values.get("restore_to_latest_time")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def server_side_encryption(
        self,
    ) -> typing.Optional["DynamodbTableServerSideEncryption"]:
        '''server_side_encryption block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#server_side_encryption DynamodbTable#server_side_encryption}
        '''
        result = self._values.get("server_side_encryption")
        return typing.cast(typing.Optional["DynamodbTableServerSideEncryption"], result)

    @builtins.property
    def stream_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#stream_enabled DynamodbTable#stream_enabled}.'''
        result = self._values.get("stream_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def stream_view_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#stream_view_type DynamodbTable#stream_view_type}.'''
        result = self._values.get("stream_view_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def table_class(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#table_class DynamodbTable#table_class}.'''
        result = self._values.get("table_class")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#tags DynamodbTable#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#tags_all DynamodbTable#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["DynamodbTableTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#timeouts DynamodbTable#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["DynamodbTableTimeouts"], result)

    @builtins.property
    def ttl(self) -> typing.Optional["DynamodbTableTtl"]:
        '''ttl block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#ttl DynamodbTable#ttl}
        '''
        result = self._values.get("ttl")
        return typing.cast(typing.Optional["DynamodbTableTtl"], result)

    @builtins.property
    def write_capacity(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#write_capacity DynamodbTable#write_capacity}.'''
        result = self._values.get("write_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DynamodbTableConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.dynamodbTable.DynamodbTableGlobalSecondaryIndex",
    jsii_struct_bases=[],
    name_mapping={
        "hash_key": "hashKey",
        "name": "name",
        "projection_type": "projectionType",
        "non_key_attributes": "nonKeyAttributes",
        "range_key": "rangeKey",
        "read_capacity": "readCapacity",
        "write_capacity": "writeCapacity",
    },
)
class DynamodbTableGlobalSecondaryIndex:
    def __init__(
        self,
        *,
        hash_key: builtins.str,
        name: builtins.str,
        projection_type: builtins.str,
        non_key_attributes: typing.Optional[typing.Sequence[builtins.str]] = None,
        range_key: typing.Optional[builtins.str] = None,
        read_capacity: typing.Optional[jsii.Number] = None,
        write_capacity: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param hash_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#hash_key DynamodbTable#hash_key}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#name DynamodbTable#name}.
        :param projection_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#projection_type DynamodbTable#projection_type}.
        :param non_key_attributes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#non_key_attributes DynamodbTable#non_key_attributes}.
        :param range_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#range_key DynamodbTable#range_key}.
        :param read_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#read_capacity DynamodbTable#read_capacity}.
        :param write_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#write_capacity DynamodbTable#write_capacity}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc4afcd8896b61195f3fb2c2bfea3e75c9da1984297039fa54c6e2aafb682a12)
            check_type(argname="argument hash_key", value=hash_key, expected_type=type_hints["hash_key"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument projection_type", value=projection_type, expected_type=type_hints["projection_type"])
            check_type(argname="argument non_key_attributes", value=non_key_attributes, expected_type=type_hints["non_key_attributes"])
            check_type(argname="argument range_key", value=range_key, expected_type=type_hints["range_key"])
            check_type(argname="argument read_capacity", value=read_capacity, expected_type=type_hints["read_capacity"])
            check_type(argname="argument write_capacity", value=write_capacity, expected_type=type_hints["write_capacity"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "hash_key": hash_key,
            "name": name,
            "projection_type": projection_type,
        }
        if non_key_attributes is not None:
            self._values["non_key_attributes"] = non_key_attributes
        if range_key is not None:
            self._values["range_key"] = range_key
        if read_capacity is not None:
            self._values["read_capacity"] = read_capacity
        if write_capacity is not None:
            self._values["write_capacity"] = write_capacity

    @builtins.property
    def hash_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#hash_key DynamodbTable#hash_key}.'''
        result = self._values.get("hash_key")
        assert result is not None, "Required property 'hash_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#name DynamodbTable#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def projection_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#projection_type DynamodbTable#projection_type}.'''
        result = self._values.get("projection_type")
        assert result is not None, "Required property 'projection_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def non_key_attributes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#non_key_attributes DynamodbTable#non_key_attributes}.'''
        result = self._values.get("non_key_attributes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def range_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#range_key DynamodbTable#range_key}.'''
        result = self._values.get("range_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read_capacity(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#read_capacity DynamodbTable#read_capacity}.'''
        result = self._values.get("read_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def write_capacity(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#write_capacity DynamodbTable#write_capacity}.'''
        result = self._values.get("write_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DynamodbTableGlobalSecondaryIndex(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DynamodbTableGlobalSecondaryIndexList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dynamodbTable.DynamodbTableGlobalSecondaryIndexList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e540ae88b59c427fd03fae211a940977b30f81f4115fd9e30cf75af28c94d8f8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DynamodbTableGlobalSecondaryIndexOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d13d65e136e748269c632ba8ce98832cd4b29fd3381b11a59113ebd7624b307c)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DynamodbTableGlobalSecondaryIndexOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d81c1bd63cda832596c66ec7d11f8a72a7853f7c8ba42770d8a272b9e987b35)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e10abb210e6a94ad6bcc5c884de6e7b17db7c4785469ff5b84f97bb0e22be917)
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
            type_hints = typing.get_type_hints(_typecheckingstub__841f292bf4991b356c4e8b04ee8c429c11070bf8af1373a382703c50d5459827)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DynamodbTableGlobalSecondaryIndex]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DynamodbTableGlobalSecondaryIndex]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DynamodbTableGlobalSecondaryIndex]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5607e72a89b96c6df05a32fb715a84b6796d5190b8c11748538ec2b9ec68974)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DynamodbTableGlobalSecondaryIndexOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dynamodbTable.DynamodbTableGlobalSecondaryIndexOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__422b2af7c4fafa6cd7248a11bbad67300a54c198df6576f3a33dcc230c319304)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetNonKeyAttributes")
    def reset_non_key_attributes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNonKeyAttributes", []))

    @jsii.member(jsii_name="resetRangeKey")
    def reset_range_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRangeKey", []))

    @jsii.member(jsii_name="resetReadCapacity")
    def reset_read_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadCapacity", []))

    @jsii.member(jsii_name="resetWriteCapacity")
    def reset_write_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWriteCapacity", []))

    @builtins.property
    @jsii.member(jsii_name="hashKeyInput")
    def hash_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hashKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="nonKeyAttributesInput")
    def non_key_attributes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "nonKeyAttributesInput"))

    @builtins.property
    @jsii.member(jsii_name="projectionTypeInput")
    def projection_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectionTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="rangeKeyInput")
    def range_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rangeKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="readCapacityInput")
    def read_capacity_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "readCapacityInput"))

    @builtins.property
    @jsii.member(jsii_name="writeCapacityInput")
    def write_capacity_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "writeCapacityInput"))

    @builtins.property
    @jsii.member(jsii_name="hashKey")
    def hash_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hashKey"))

    @hash_key.setter
    def hash_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f77a4538c6f54081f2254413af67a340f15e7d78cc38dac2e4b98030d438c95)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hashKey", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__561db6da41b9d256e3fd88b8e72ce2c619eb978fba1591c0309c1253d0c5716e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="nonKeyAttributes")
    def non_key_attributes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "nonKeyAttributes"))

    @non_key_attributes.setter
    def non_key_attributes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17880382fdd20431e4e491f0a6b1f19265e057715d69dfc338050e57bb6af6d5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nonKeyAttributes", value)

    @builtins.property
    @jsii.member(jsii_name="projectionType")
    def projection_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "projectionType"))

    @projection_type.setter
    def projection_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d64674db6bc8f339d4c39cddb6a7da32ec236a41c709c707c9bf787db235cf74)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projectionType", value)

    @builtins.property
    @jsii.member(jsii_name="rangeKey")
    def range_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rangeKey"))

    @range_key.setter
    def range_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a904df9dcc0957786a3c361076bbc45e31682b39e91b08b60ef32fa46f158f8d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rangeKey", value)

    @builtins.property
    @jsii.member(jsii_name="readCapacity")
    def read_capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "readCapacity"))

    @read_capacity.setter
    def read_capacity(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8bd8f5209e18f53137ce1df2a1971fe7ad339df23485094cf7dc6ed913e3daca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="writeCapacity")
    def write_capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "writeCapacity"))

    @write_capacity.setter
    def write_capacity(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b0a6b396e35e6dee178802a58e79c05a3c23b359c806b219126f41df0c9968f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "writeCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DynamodbTableGlobalSecondaryIndex, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DynamodbTableGlobalSecondaryIndex, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DynamodbTableGlobalSecondaryIndex, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9207c04cf5dd1933cf73147614ffcf685c5328b765f970be3e71545a914b3b37)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.dynamodbTable.DynamodbTableLocalSecondaryIndex",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "projection_type": "projectionType",
        "range_key": "rangeKey",
        "non_key_attributes": "nonKeyAttributes",
    },
)
class DynamodbTableLocalSecondaryIndex:
    def __init__(
        self,
        *,
        name: builtins.str,
        projection_type: builtins.str,
        range_key: builtins.str,
        non_key_attributes: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#name DynamodbTable#name}.
        :param projection_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#projection_type DynamodbTable#projection_type}.
        :param range_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#range_key DynamodbTable#range_key}.
        :param non_key_attributes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#non_key_attributes DynamodbTable#non_key_attributes}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a49565124d4b1c0b0f080f3814409927c390a52ca43f7f400451e3737b65028)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument projection_type", value=projection_type, expected_type=type_hints["projection_type"])
            check_type(argname="argument range_key", value=range_key, expected_type=type_hints["range_key"])
            check_type(argname="argument non_key_attributes", value=non_key_attributes, expected_type=type_hints["non_key_attributes"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "projection_type": projection_type,
            "range_key": range_key,
        }
        if non_key_attributes is not None:
            self._values["non_key_attributes"] = non_key_attributes

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#name DynamodbTable#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def projection_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#projection_type DynamodbTable#projection_type}.'''
        result = self._values.get("projection_type")
        assert result is not None, "Required property 'projection_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def range_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#range_key DynamodbTable#range_key}.'''
        result = self._values.get("range_key")
        assert result is not None, "Required property 'range_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def non_key_attributes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#non_key_attributes DynamodbTable#non_key_attributes}.'''
        result = self._values.get("non_key_attributes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DynamodbTableLocalSecondaryIndex(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DynamodbTableLocalSecondaryIndexList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dynamodbTable.DynamodbTableLocalSecondaryIndexList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a30335b8d56c4e9222313b89fb200452e34f23af0e21ba3fbf7469af93f60648)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DynamodbTableLocalSecondaryIndexOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9eda57b24ba3bfffa0f737e19767bdb036a3ddd99b27087b2e7a43bc2c98704e)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DynamodbTableLocalSecondaryIndexOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d73dc375c8280ae8262165381395449aaac05b7bc8d2e3a3eb57876d88cc5c2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b1af6057a617952496f6eaf5ef0ef841c01bc176f6bc6787d9f4e9df576409b5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a5eb0de877109530b31511ffc5007ce35f30813cb666126d33a7a7de8989fc1a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DynamodbTableLocalSecondaryIndex]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DynamodbTableLocalSecondaryIndex]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DynamodbTableLocalSecondaryIndex]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa72270e1025d3ddcee5b3b7d3ddbb62cc7dbd4f74f6247fbb481ab05b561ec2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DynamodbTableLocalSecondaryIndexOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dynamodbTable.DynamodbTableLocalSecondaryIndexOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2cfe93b36e20217e630c34604ff68c51fc78061ea48320065e5e16e21938cdf3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetNonKeyAttributes")
    def reset_non_key_attributes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNonKeyAttributes", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="nonKeyAttributesInput")
    def non_key_attributes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "nonKeyAttributesInput"))

    @builtins.property
    @jsii.member(jsii_name="projectionTypeInput")
    def projection_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectionTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="rangeKeyInput")
    def range_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rangeKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f3ca8f28df3e137ab2f8258a43e6becf3ab65d926e1a68040b1db2aa0d020425)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="nonKeyAttributes")
    def non_key_attributes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "nonKeyAttributes"))

    @non_key_attributes.setter
    def non_key_attributes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9fbd763518822e7a39877d57102760b9b9bd3befe6d1724c30096c3bbd71ec5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nonKeyAttributes", value)

    @builtins.property
    @jsii.member(jsii_name="projectionType")
    def projection_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "projectionType"))

    @projection_type.setter
    def projection_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__870c3a1bd4c79f0a2303d6ffc5698f747c5a7fbdd20b944c06daa46a0767b443)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projectionType", value)

    @builtins.property
    @jsii.member(jsii_name="rangeKey")
    def range_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rangeKey"))

    @range_key.setter
    def range_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9636099c9c75ca4b61e020cda115a1dca897993aa35e551b577ebff28cb8790c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rangeKey", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DynamodbTableLocalSecondaryIndex, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DynamodbTableLocalSecondaryIndex, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DynamodbTableLocalSecondaryIndex, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c6abd6568daa9016b5ea471aadd2d4a065d6bff94006e8b441fca83dece6014)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.dynamodbTable.DynamodbTablePointInTimeRecovery",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled"},
)
class DynamodbTablePointInTimeRecovery:
    def __init__(
        self,
        *,
        enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#enabled DynamodbTable#enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__edc11212fd981d0c0cb262c01f4629594af32843981ac5fa5f440652076f00e6)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "enabled": enabled,
        }

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#enabled DynamodbTable#enabled}.'''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DynamodbTablePointInTimeRecovery(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DynamodbTablePointInTimeRecoveryOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dynamodbTable.DynamodbTablePointInTimeRecoveryOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f9d002ab179ec8994fc44e7856ae2545ee94e613801bcbbb08ef255eaeb10bff)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__30d757b5a35d1e4fc2aa07cf7b217131ccca8e269af6504fa936d9505f189fbd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DynamodbTablePointInTimeRecovery]:
        return typing.cast(typing.Optional[DynamodbTablePointInTimeRecovery], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DynamodbTablePointInTimeRecovery],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aee58edbe4165b3e4e556e27202c7f784a7827ef5024d0f7f3312c152ba59d1a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.dynamodbTable.DynamodbTableReplica",
    jsii_struct_bases=[],
    name_mapping={
        "region_name": "regionName",
        "kms_key_arn": "kmsKeyArn",
        "point_in_time_recovery": "pointInTimeRecovery",
        "propagate_tags": "propagateTags",
    },
)
class DynamodbTableReplica:
    def __init__(
        self,
        *,
        region_name: builtins.str,
        kms_key_arn: typing.Optional[builtins.str] = None,
        point_in_time_recovery: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        propagate_tags: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param region_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#region_name DynamodbTable#region_name}.
        :param kms_key_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#kms_key_arn DynamodbTable#kms_key_arn}.
        :param point_in_time_recovery: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#point_in_time_recovery DynamodbTable#point_in_time_recovery}.
        :param propagate_tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#propagate_tags DynamodbTable#propagate_tags}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f91d485547d293a9f69d2d0b4bfaa40bc9e6cff0a5caf6d136dccd111e0c9cd1)
            check_type(argname="argument region_name", value=region_name, expected_type=type_hints["region_name"])
            check_type(argname="argument kms_key_arn", value=kms_key_arn, expected_type=type_hints["kms_key_arn"])
            check_type(argname="argument point_in_time_recovery", value=point_in_time_recovery, expected_type=type_hints["point_in_time_recovery"])
            check_type(argname="argument propagate_tags", value=propagate_tags, expected_type=type_hints["propagate_tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "region_name": region_name,
        }
        if kms_key_arn is not None:
            self._values["kms_key_arn"] = kms_key_arn
        if point_in_time_recovery is not None:
            self._values["point_in_time_recovery"] = point_in_time_recovery
        if propagate_tags is not None:
            self._values["propagate_tags"] = propagate_tags

    @builtins.property
    def region_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#region_name DynamodbTable#region_name}.'''
        result = self._values.get("region_name")
        assert result is not None, "Required property 'region_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#kms_key_arn DynamodbTable#kms_key_arn}.'''
        result = self._values.get("kms_key_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def point_in_time_recovery(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#point_in_time_recovery DynamodbTable#point_in_time_recovery}.'''
        result = self._values.get("point_in_time_recovery")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def propagate_tags(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#propagate_tags DynamodbTable#propagate_tags}.'''
        result = self._values.get("propagate_tags")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DynamodbTableReplica(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DynamodbTableReplicaList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dynamodbTable.DynamodbTableReplicaList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f1a19990018a189f4043053f05602f6f6dcf565798f876cc61fafc536f62ff33)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "DynamodbTableReplicaOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__86d92614c1b2fadf39601e4df626b8ba0c7751762a09b9242d4317a3fed6d06b)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DynamodbTableReplicaOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__205232e6287383a7f9c4ec67072cb6b744d24b0ad86a52ced3668357d90cb984)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b209f9351d53e7711c2e858d4ff2d5ba1c1d17de7ada51b8527cc2e63f75b4a3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__eff5c75fb409414b71a95dbbed892065eaddb81f6d0da0dde212bc321bbc4556)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DynamodbTableReplica]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DynamodbTableReplica]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DynamodbTableReplica]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00a19b342cf3c7b69329fb1e528102e735fa6735e9827374a7a72e5dfa186a5e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DynamodbTableReplicaOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dynamodbTable.DynamodbTableReplicaOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__28505521bafc1d160218913bb91e75df96bd8e3359fdb2a599a35603896bf7c7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetKmsKeyArn")
    def reset_kms_key_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKeyArn", []))

    @jsii.member(jsii_name="resetPointInTimeRecovery")
    def reset_point_in_time_recovery(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPointInTimeRecovery", []))

    @jsii.member(jsii_name="resetPropagateTags")
    def reset_propagate_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPropagateTags", []))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyArnInput")
    def kms_key_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyArnInput"))

    @builtins.property
    @jsii.member(jsii_name="pointInTimeRecoveryInput")
    def point_in_time_recovery_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "pointInTimeRecoveryInput"))

    @builtins.property
    @jsii.member(jsii_name="propagateTagsInput")
    def propagate_tags_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "propagateTagsInput"))

    @builtins.property
    @jsii.member(jsii_name="regionNameInput")
    def region_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionNameInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyArn")
    def kms_key_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyArn"))

    @kms_key_arn.setter
    def kms_key_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__34ff4e585be313d318a4a82e9620f0cb9009f591badb1e7dbc2b56ac4d2ebe70)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyArn", value)

    @builtins.property
    @jsii.member(jsii_name="pointInTimeRecovery")
    def point_in_time_recovery(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "pointInTimeRecovery"))

    @point_in_time_recovery.setter
    def point_in_time_recovery(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca9e93624b5b435d62db258159e05827dfea9ff90f37a850aa0129f746b31119)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pointInTimeRecovery", value)

    @builtins.property
    @jsii.member(jsii_name="propagateTags")
    def propagate_tags(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "propagateTags"))

    @propagate_tags.setter
    def propagate_tags(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c7578ac569f8f6ea67dae3efa0bf9442cd3bfdb16fb98d0d8b452f0d183c52a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "propagateTags", value)

    @builtins.property
    @jsii.member(jsii_name="regionName")
    def region_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "regionName"))

    @region_name.setter
    def region_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a96597cb42cd492ef12c81d3689282e4495157ab21d03aa78d2711c44df483e7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "regionName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DynamodbTableReplica, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DynamodbTableReplica, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DynamodbTableReplica, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52434c72600138d558a975a91515ef2403a256208da1a293b193a1574ca90971)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.dynamodbTable.DynamodbTableServerSideEncryption",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "kms_key_arn": "kmsKeyArn"},
)
class DynamodbTableServerSideEncryption:
    def __init__(
        self,
        *,
        enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        kms_key_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#enabled DynamodbTable#enabled}.
        :param kms_key_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#kms_key_arn DynamodbTable#kms_key_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2bd274e8d0129dd62a315758589ce7da3438c06f8bb6055a621bb17dd8f40a65)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument kms_key_arn", value=kms_key_arn, expected_type=type_hints["kms_key_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "enabled": enabled,
        }
        if kms_key_arn is not None:
            self._values["kms_key_arn"] = kms_key_arn

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#enabled DynamodbTable#enabled}.'''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    @builtins.property
    def kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#kms_key_arn DynamodbTable#kms_key_arn}.'''
        result = self._values.get("kms_key_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DynamodbTableServerSideEncryption(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DynamodbTableServerSideEncryptionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dynamodbTable.DynamodbTableServerSideEncryptionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9bdd10495a98f240362ca9bb729e8309c223dacb64054821d826e1c9702417dc)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetKmsKeyArn")
    def reset_kms_key_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKeyArn", []))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyArnInput")
    def kms_key_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyArnInput"))

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4728a37b9ebbd51246f1ea035b550f0b70c7cac9724f5bef73a73e46cf8f902)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyArn")
    def kms_key_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyArn"))

    @kms_key_arn.setter
    def kms_key_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70f89876c65f38e6e0a86b55bcd38cd1664d3fd4fe1cba123523d3aa78e9266e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DynamodbTableServerSideEncryption]:
        return typing.cast(typing.Optional[DynamodbTableServerSideEncryption], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DynamodbTableServerSideEncryption],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9733d75db07e94f2484a5a9d55d5003059a2a668c2917eebd3398ec0e5cf372f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.dynamodbTable.DynamodbTableTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class DynamodbTableTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#create DynamodbTable#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#delete DynamodbTable#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#update DynamodbTable#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09e45ccfa54cc5885cd12d37a20a6478658d9438a6a412055d73c64739609a13)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#create DynamodbTable#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#delete DynamodbTable#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#update DynamodbTable#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DynamodbTableTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DynamodbTableTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dynamodbTable.DynamodbTableTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ec473a2cf633676225ed11257b2a9f1cec4a1044df0d98f550d2e8b4cc568a6c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b48da4918c3f85ba1649127279dcb3023a2a0810275aba2e73bca9a8d0416008)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1248e3fff62cbb991afc586f0d887aee948b41cfde48564c625591533831f78)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3dc4616e06470ddd306d738e9cdb12c80315824d5e8a5c8e4bb21f6587016442)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DynamodbTableTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DynamodbTableTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DynamodbTableTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5d0cef2f065d985f488caa443d139f53c5810f0bf6d2740b6ee48704c6e5757)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.dynamodbTable.DynamodbTableTtl",
    jsii_struct_bases=[],
    name_mapping={"attribute_name": "attributeName", "enabled": "enabled"},
)
class DynamodbTableTtl:
    def __init__(
        self,
        *,
        attribute_name: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param attribute_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#attribute_name DynamodbTable#attribute_name}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#enabled DynamodbTable#enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b104a60a24c303a83d895fa6758690d79975722fa4a72cc5c631e562ff0fc14)
            check_type(argname="argument attribute_name", value=attribute_name, expected_type=type_hints["attribute_name"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "attribute_name": attribute_name,
        }
        if enabled is not None:
            self._values["enabled"] = enabled

    @builtins.property
    def attribute_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#attribute_name DynamodbTable#attribute_name}.'''
        result = self._values.get("attribute_name")
        assert result is not None, "Required property 'attribute_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dynamodb_table#enabled DynamodbTable#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DynamodbTableTtl(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DynamodbTableTtlOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dynamodbTable.DynamodbTableTtlOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__928999bb18dbdcf5b6dde116acf4541bd4336f5a96b55a04defe041a3fe0c525)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @builtins.property
    @jsii.member(jsii_name="attributeNameInput")
    def attribute_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "attributeNameInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="attributeName")
    def attribute_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "attributeName"))

    @attribute_name.setter
    def attribute_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b84d68dbd6d7499c195302ee53b92f607b45fbf11b50730c22a525b3b9e3a114)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "attributeName", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ddf265e8c8baec28c18ac558afe859410ed91078b5a50c029422c4b7ea9bc38f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DynamodbTableTtl]:
        return typing.cast(typing.Optional[DynamodbTableTtl], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[DynamodbTableTtl]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b997db7449b8562bbff42bf40a52982b6bfa41f83b5672535c085ba0b63d550b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DynamodbTable",
    "DynamodbTableAttribute",
    "DynamodbTableAttributeList",
    "DynamodbTableAttributeOutputReference",
    "DynamodbTableConfig",
    "DynamodbTableGlobalSecondaryIndex",
    "DynamodbTableGlobalSecondaryIndexList",
    "DynamodbTableGlobalSecondaryIndexOutputReference",
    "DynamodbTableLocalSecondaryIndex",
    "DynamodbTableLocalSecondaryIndexList",
    "DynamodbTableLocalSecondaryIndexOutputReference",
    "DynamodbTablePointInTimeRecovery",
    "DynamodbTablePointInTimeRecoveryOutputReference",
    "DynamodbTableReplica",
    "DynamodbTableReplicaList",
    "DynamodbTableReplicaOutputReference",
    "DynamodbTableServerSideEncryption",
    "DynamodbTableServerSideEncryptionOutputReference",
    "DynamodbTableTimeouts",
    "DynamodbTableTimeoutsOutputReference",
    "DynamodbTableTtl",
    "DynamodbTableTtlOutputReference",
]

publication.publish()

def _typecheckingstub__195cebc3a317b1c8a35f9a17d5a50f1ec737abd62fd14599da6268dec9f51a03(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    attribute: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DynamodbTableAttribute, typing.Dict[builtins.str, typing.Any]]]]] = None,
    billing_mode: typing.Optional[builtins.str] = None,
    global_secondary_index: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DynamodbTableGlobalSecondaryIndex, typing.Dict[builtins.str, typing.Any]]]]] = None,
    hash_key: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    local_secondary_index: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DynamodbTableLocalSecondaryIndex, typing.Dict[builtins.str, typing.Any]]]]] = None,
    point_in_time_recovery: typing.Optional[typing.Union[DynamodbTablePointInTimeRecovery, typing.Dict[builtins.str, typing.Any]]] = None,
    range_key: typing.Optional[builtins.str] = None,
    read_capacity: typing.Optional[jsii.Number] = None,
    replica: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DynamodbTableReplica, typing.Dict[builtins.str, typing.Any]]]]] = None,
    restore_date_time: typing.Optional[builtins.str] = None,
    restore_source_name: typing.Optional[builtins.str] = None,
    restore_to_latest_time: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    server_side_encryption: typing.Optional[typing.Union[DynamodbTableServerSideEncryption, typing.Dict[builtins.str, typing.Any]]] = None,
    stream_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    stream_view_type: typing.Optional[builtins.str] = None,
    table_class: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[DynamodbTableTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    ttl: typing.Optional[typing.Union[DynamodbTableTtl, typing.Dict[builtins.str, typing.Any]]] = None,
    write_capacity: typing.Optional[jsii.Number] = None,
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

def _typecheckingstub__2e6f9706b27b4d89f553d2ce789cad1e288cb1266ea3824c25882eeb6857508c(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DynamodbTableAttribute, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15af35b4b616a51fa0f36cfbe333a1e1af3840473f91c289a389f3ddc8eecb3b(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DynamodbTableGlobalSecondaryIndex, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d87705e1ac3a40bd6585db376affdcc340c305318228db563d7e79851fcb82b(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DynamodbTableLocalSecondaryIndex, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b9c238f7260bb1d3c2929ca54322fdd86a17415e03c151080273e625dc2e0b4(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DynamodbTableReplica, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__536518bb65083cb1c6e142b614c52eff0a5e4702b8f86972e4c3c8b97f13d400(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15c69111e07b835b3bc0f081277f4a7b58f748626355a943c92e618f6bc61f00(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd5e1af684c1b15ef054e19abd124009823c767f7b989e771304f7ae215a30de(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c158abe44aa0c29e152cd46d283691e364b1ae0a6d5d4b332a527d39b5a99cd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b2a44e866c33c60f9eab3638a95b498acf56808423b93d0301df130e26c346c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90205c51f054bda807cdb1d473e312d44415fcbac4149ef177af47f5d77fc3b4(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d4303dde9957a3a50f87dc861e632e2e0a62cd2f05ae90639be5d503f83bd85(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a29e548b4b3319076f7d4d2f3e316ca20b963e27a79e97a193e7a7f9d0b2a32b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78196ff02db2e4ba1420035556a114260ad7ec451887148be663c90294fb37ef(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d62033ae459affb6e7447225a46245401ddf0bbf6cca71d8b239c4182701700(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be57d3674070ec4631108065f28d6cbb8a11cb01e66edc00f52dceab5c8be82b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad9a2b0d2fb37f05e8400bd99478638824a46bac45c3c933fd63f87a66de17c0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e35fd75ca431a9dd29057bc922db58bea97404303e110c5cfb5296d6585cedc3(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3663aa3932f0f5abf28d1b6a09aaa1792b486e8155f8ff6d38826d9432ae2f05(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66019203adce417e3d18126479c16792493e6df9dbe9197a1150c3c386a9e638(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6af99b1c929e1307d7ffbd969ad9856ae0cf036431d757886d7df9941eebe208(
    *,
    name: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9159773d5b6f4f62d467d6296c603e0f51f057dab4e4eca1af269c71a2c11ee2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__101759bed407fd8a326a1ee2c700174f313e8074279539966609bba6a82269ea(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__868bfe6b1196af921c3c0b95523a8da388b3a65bc8c1acf3721f4a99134cd863(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c245336d4cb6d78e05455959d1f19427c3779a9d7fe8749a48eb46d4f20bf06d(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50ff46daff0193ea702f3bd4fba47f4061e05329d1f2dbca8de3d4dae19a47c0(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5bc26d9a77116ad1484e0c653d11cfe611334b7ba1e924c9e9db750ee59df18(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DynamodbTableAttribute]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5eb27d13cb54cc35bf5fe3d0fdb4a0e44eb354b2ac23301501d0a5c213ff3df5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__523aa8084580509128c8383e0539ef80db195892202f8b33c5cebfe707030ef0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cbb50ffc145bea4a4497398bea2de25ac06328aa806cb03ce78dd23c629ea910(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7815dbb1e475697f35c76c4eab7759251a5c4722b743ef293693a8b816755732(
    value: typing.Optional[typing.Union[DynamodbTableAttribute, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__350f895c7dc5f8832f7fc64a998e67e41b6f2e2670a71dd18a81ecb55b6a9edb(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: builtins.str,
    attribute: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DynamodbTableAttribute, typing.Dict[builtins.str, typing.Any]]]]] = None,
    billing_mode: typing.Optional[builtins.str] = None,
    global_secondary_index: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DynamodbTableGlobalSecondaryIndex, typing.Dict[builtins.str, typing.Any]]]]] = None,
    hash_key: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    local_secondary_index: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DynamodbTableLocalSecondaryIndex, typing.Dict[builtins.str, typing.Any]]]]] = None,
    point_in_time_recovery: typing.Optional[typing.Union[DynamodbTablePointInTimeRecovery, typing.Dict[builtins.str, typing.Any]]] = None,
    range_key: typing.Optional[builtins.str] = None,
    read_capacity: typing.Optional[jsii.Number] = None,
    replica: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DynamodbTableReplica, typing.Dict[builtins.str, typing.Any]]]]] = None,
    restore_date_time: typing.Optional[builtins.str] = None,
    restore_source_name: typing.Optional[builtins.str] = None,
    restore_to_latest_time: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    server_side_encryption: typing.Optional[typing.Union[DynamodbTableServerSideEncryption, typing.Dict[builtins.str, typing.Any]]] = None,
    stream_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    stream_view_type: typing.Optional[builtins.str] = None,
    table_class: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[DynamodbTableTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    ttl: typing.Optional[typing.Union[DynamodbTableTtl, typing.Dict[builtins.str, typing.Any]]] = None,
    write_capacity: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc4afcd8896b61195f3fb2c2bfea3e75c9da1984297039fa54c6e2aafb682a12(
    *,
    hash_key: builtins.str,
    name: builtins.str,
    projection_type: builtins.str,
    non_key_attributes: typing.Optional[typing.Sequence[builtins.str]] = None,
    range_key: typing.Optional[builtins.str] = None,
    read_capacity: typing.Optional[jsii.Number] = None,
    write_capacity: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e540ae88b59c427fd03fae211a940977b30f81f4115fd9e30cf75af28c94d8f8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d13d65e136e748269c632ba8ce98832cd4b29fd3381b11a59113ebd7624b307c(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d81c1bd63cda832596c66ec7d11f8a72a7853f7c8ba42770d8a272b9e987b35(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e10abb210e6a94ad6bcc5c884de6e7b17db7c4785469ff5b84f97bb0e22be917(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__841f292bf4991b356c4e8b04ee8c429c11070bf8af1373a382703c50d5459827(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5607e72a89b96c6df05a32fb715a84b6796d5190b8c11748538ec2b9ec68974(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DynamodbTableGlobalSecondaryIndex]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__422b2af7c4fafa6cd7248a11bbad67300a54c198df6576f3a33dcc230c319304(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f77a4538c6f54081f2254413af67a340f15e7d78cc38dac2e4b98030d438c95(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__561db6da41b9d256e3fd88b8e72ce2c619eb978fba1591c0309c1253d0c5716e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17880382fdd20431e4e491f0a6b1f19265e057715d69dfc338050e57bb6af6d5(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d64674db6bc8f339d4c39cddb6a7da32ec236a41c709c707c9bf787db235cf74(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a904df9dcc0957786a3c361076bbc45e31682b39e91b08b60ef32fa46f158f8d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8bd8f5209e18f53137ce1df2a1971fe7ad339df23485094cf7dc6ed913e3daca(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b0a6b396e35e6dee178802a58e79c05a3c23b359c806b219126f41df0c9968f(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9207c04cf5dd1933cf73147614ffcf685c5328b765f970be3e71545a914b3b37(
    value: typing.Optional[typing.Union[DynamodbTableGlobalSecondaryIndex, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a49565124d4b1c0b0f080f3814409927c390a52ca43f7f400451e3737b65028(
    *,
    name: builtins.str,
    projection_type: builtins.str,
    range_key: builtins.str,
    non_key_attributes: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a30335b8d56c4e9222313b89fb200452e34f23af0e21ba3fbf7469af93f60648(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9eda57b24ba3bfffa0f737e19767bdb036a3ddd99b27087b2e7a43bc2c98704e(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d73dc375c8280ae8262165381395449aaac05b7bc8d2e3a3eb57876d88cc5c2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1af6057a617952496f6eaf5ef0ef841c01bc176f6bc6787d9f4e9df576409b5(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5eb0de877109530b31511ffc5007ce35f30813cb666126d33a7a7de8989fc1a(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa72270e1025d3ddcee5b3b7d3ddbb62cc7dbd4f74f6247fbb481ab05b561ec2(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DynamodbTableLocalSecondaryIndex]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2cfe93b36e20217e630c34604ff68c51fc78061ea48320065e5e16e21938cdf3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3ca8f28df3e137ab2f8258a43e6becf3ab65d926e1a68040b1db2aa0d020425(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9fbd763518822e7a39877d57102760b9b9bd3befe6d1724c30096c3bbd71ec5(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__870c3a1bd4c79f0a2303d6ffc5698f747c5a7fbdd20b944c06daa46a0767b443(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9636099c9c75ca4b61e020cda115a1dca897993aa35e551b577ebff28cb8790c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c6abd6568daa9016b5ea471aadd2d4a065d6bff94006e8b441fca83dece6014(
    value: typing.Optional[typing.Union[DynamodbTableLocalSecondaryIndex, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__edc11212fd981d0c0cb262c01f4629594af32843981ac5fa5f440652076f00e6(
    *,
    enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9d002ab179ec8994fc44e7856ae2545ee94e613801bcbbb08ef255eaeb10bff(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30d757b5a35d1e4fc2aa07cf7b217131ccca8e269af6504fa936d9505f189fbd(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aee58edbe4165b3e4e556e27202c7f784a7827ef5024d0f7f3312c152ba59d1a(
    value: typing.Optional[DynamodbTablePointInTimeRecovery],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f91d485547d293a9f69d2d0b4bfaa40bc9e6cff0a5caf6d136dccd111e0c9cd1(
    *,
    region_name: builtins.str,
    kms_key_arn: typing.Optional[builtins.str] = None,
    point_in_time_recovery: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    propagate_tags: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1a19990018a189f4043053f05602f6f6dcf565798f876cc61fafc536f62ff33(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86d92614c1b2fadf39601e4df626b8ba0c7751762a09b9242d4317a3fed6d06b(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__205232e6287383a7f9c4ec67072cb6b744d24b0ad86a52ced3668357d90cb984(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b209f9351d53e7711c2e858d4ff2d5ba1c1d17de7ada51b8527cc2e63f75b4a3(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eff5c75fb409414b71a95dbbed892065eaddb81f6d0da0dde212bc321bbc4556(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00a19b342cf3c7b69329fb1e528102e735fa6735e9827374a7a72e5dfa186a5e(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DynamodbTableReplica]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28505521bafc1d160218913bb91e75df96bd8e3359fdb2a599a35603896bf7c7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34ff4e585be313d318a4a82e9620f0cb9009f591badb1e7dbc2b56ac4d2ebe70(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca9e93624b5b435d62db258159e05827dfea9ff90f37a850aa0129f746b31119(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c7578ac569f8f6ea67dae3efa0bf9442cd3bfdb16fb98d0d8b452f0d183c52a(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a96597cb42cd492ef12c81d3689282e4495157ab21d03aa78d2711c44df483e7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52434c72600138d558a975a91515ef2403a256208da1a293b193a1574ca90971(
    value: typing.Optional[typing.Union[DynamodbTableReplica, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2bd274e8d0129dd62a315758589ce7da3438c06f8bb6055a621bb17dd8f40a65(
    *,
    enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    kms_key_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9bdd10495a98f240362ca9bb729e8309c223dacb64054821d826e1c9702417dc(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4728a37b9ebbd51246f1ea035b550f0b70c7cac9724f5bef73a73e46cf8f902(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70f89876c65f38e6e0a86b55bcd38cd1664d3fd4fe1cba123523d3aa78e9266e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9733d75db07e94f2484a5a9d55d5003059a2a668c2917eebd3398ec0e5cf372f(
    value: typing.Optional[DynamodbTableServerSideEncryption],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09e45ccfa54cc5885cd12d37a20a6478658d9438a6a412055d73c64739609a13(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec473a2cf633676225ed11257b2a9f1cec4a1044df0d98f550d2e8b4cc568a6c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b48da4918c3f85ba1649127279dcb3023a2a0810275aba2e73bca9a8d0416008(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1248e3fff62cbb991afc586f0d887aee948b41cfde48564c625591533831f78(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3dc4616e06470ddd306d738e9cdb12c80315824d5e8a5c8e4bb21f6587016442(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5d0cef2f065d985f488caa443d139f53c5810f0bf6d2740b6ee48704c6e5757(
    value: typing.Optional[typing.Union[DynamodbTableTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b104a60a24c303a83d895fa6758690d79975722fa4a72cc5c631e562ff0fc14(
    *,
    attribute_name: builtins.str,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__928999bb18dbdcf5b6dde116acf4541bd4336f5a96b55a04defe041a3fe0c525(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b84d68dbd6d7499c195302ee53b92f607b45fbf11b50730c22a525b3b9e3a114(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ddf265e8c8baec28c18ac558afe859410ed91078b5a50c029422c4b7ea9bc38f(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b997db7449b8562bbff42bf40a52982b6bfa41f83b5672535c085ba0b63d550b(
    value: typing.Optional[DynamodbTableTtl],
) -> None:
    """Type checking stubs"""
    pass
