'''
# `aws_db_snapshot_copy`

Refer to the Terraform Registory for docs: [`aws_db_snapshot_copy`](https://www.terraform.io/docs/providers/aws/r/db_snapshot_copy).
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


class DbSnapshotCopy(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dbSnapshotCopy.DbSnapshotCopy",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/db_snapshot_copy aws_db_snapshot_copy}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        source_db_snapshot_identifier: builtins.str,
        target_db_snapshot_identifier: builtins.str,
        copy_tags: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        destination_region: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        option_group_name: typing.Optional[builtins.str] = None,
        presigned_url: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        target_custom_availability_zone: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["DbSnapshotCopyTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/db_snapshot_copy aws_db_snapshot_copy} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param source_db_snapshot_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_snapshot_copy#source_db_snapshot_identifier DbSnapshotCopy#source_db_snapshot_identifier}.
        :param target_db_snapshot_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_snapshot_copy#target_db_snapshot_identifier DbSnapshotCopy#target_db_snapshot_identifier}.
        :param copy_tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_snapshot_copy#copy_tags DbSnapshotCopy#copy_tags}.
        :param destination_region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_snapshot_copy#destination_region DbSnapshotCopy#destination_region}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_snapshot_copy#id DbSnapshotCopy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_snapshot_copy#kms_key_id DbSnapshotCopy#kms_key_id}.
        :param option_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_snapshot_copy#option_group_name DbSnapshotCopy#option_group_name}.
        :param presigned_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_snapshot_copy#presigned_url DbSnapshotCopy#presigned_url}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_snapshot_copy#tags DbSnapshotCopy#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_snapshot_copy#tags_all DbSnapshotCopy#tags_all}.
        :param target_custom_availability_zone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_snapshot_copy#target_custom_availability_zone DbSnapshotCopy#target_custom_availability_zone}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_snapshot_copy#timeouts DbSnapshotCopy#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6934dcaf2d3b27be5e2ae8953602bcc51fcb771bd7759cf06a87b9d72ff12c7)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DbSnapshotCopyConfig(
            source_db_snapshot_identifier=source_db_snapshot_identifier,
            target_db_snapshot_identifier=target_db_snapshot_identifier,
            copy_tags=copy_tags,
            destination_region=destination_region,
            id=id,
            kms_key_id=kms_key_id,
            option_group_name=option_group_name,
            presigned_url=presigned_url,
            tags=tags,
            tags_all=tags_all,
            target_custom_availability_zone=target_custom_availability_zone,
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

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(self, *, create: typing.Optional[builtins.str] = None) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_snapshot_copy#create DbSnapshotCopy#create}.
        '''
        value = DbSnapshotCopyTimeouts(create=create)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetCopyTags")
    def reset_copy_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCopyTags", []))

    @jsii.member(jsii_name="resetDestinationRegion")
    def reset_destination_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDestinationRegion", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetKmsKeyId")
    def reset_kms_key_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKeyId", []))

    @jsii.member(jsii_name="resetOptionGroupName")
    def reset_option_group_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOptionGroupName", []))

    @jsii.member(jsii_name="resetPresignedUrl")
    def reset_presigned_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPresignedUrl", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetTargetCustomAvailabilityZone")
    def reset_target_custom_availability_zone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetCustomAvailabilityZone", []))

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
    @jsii.member(jsii_name="allocatedStorage")
    def allocated_storage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "allocatedStorage"))

    @builtins.property
    @jsii.member(jsii_name="availabilityZone")
    def availability_zone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "availabilityZone"))

    @builtins.property
    @jsii.member(jsii_name="dbSnapshotArn")
    def db_snapshot_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dbSnapshotArn"))

    @builtins.property
    @jsii.member(jsii_name="encrypted")
    def encrypted(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "encrypted"))

    @builtins.property
    @jsii.member(jsii_name="engine")
    def engine(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "engine"))

    @builtins.property
    @jsii.member(jsii_name="engineVersion")
    def engine_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "engineVersion"))

    @builtins.property
    @jsii.member(jsii_name="iops")
    def iops(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "iops"))

    @builtins.property
    @jsii.member(jsii_name="licenseModel")
    def license_model(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "licenseModel"))

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @builtins.property
    @jsii.member(jsii_name="snapshotType")
    def snapshot_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "snapshotType"))

    @builtins.property
    @jsii.member(jsii_name="sourceRegion")
    def source_region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceRegion"))

    @builtins.property
    @jsii.member(jsii_name="storageType")
    def storage_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageType"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "DbSnapshotCopyTimeoutsOutputReference":
        return typing.cast("DbSnapshotCopyTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="vpcId")
    def vpc_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vpcId"))

    @builtins.property
    @jsii.member(jsii_name="copyTagsInput")
    def copy_tags_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "copyTagsInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationRegionInput")
    def destination_region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationRegionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyIdInput")
    def kms_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="optionGroupNameInput")
    def option_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "optionGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="presignedUrlInput")
    def presigned_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "presignedUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceDbSnapshotIdentifierInput")
    def source_db_snapshot_identifier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceDbSnapshotIdentifierInput"))

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
    @jsii.member(jsii_name="targetCustomAvailabilityZoneInput")
    def target_custom_availability_zone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetCustomAvailabilityZoneInput"))

    @builtins.property
    @jsii.member(jsii_name="targetDbSnapshotIdentifierInput")
    def target_db_snapshot_identifier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetDbSnapshotIdentifierInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["DbSnapshotCopyTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["DbSnapshotCopyTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="copyTags")
    def copy_tags(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "copyTags"))

    @copy_tags.setter
    def copy_tags(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f0568a5d8e255c2b65c0a5f51ce43abc1e17aef461afdea46ab01128761716a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "copyTags", value)

    @builtins.property
    @jsii.member(jsii_name="destinationRegion")
    def destination_region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destinationRegion"))

    @destination_region.setter
    def destination_region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d4228922a47d7a37d02ee28430ff62b39bff9294c87368cd7af9927f971dd40)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationRegion", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78583e68a6612b38d6e7f90735dcd6a05e0fb4dbd11bdbf0883a9ea5081d0253)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4ff58e894e8d45a84710095570f8cdaefc4f5675529e4bcba8db1c724d72162)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="optionGroupName")
    def option_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "optionGroupName"))

    @option_group_name.setter
    def option_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92d831902f75d35e83afdf0ec66182a032a1bb1d5067f2375710a1e892ac0848)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "optionGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="presignedUrl")
    def presigned_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "presignedUrl"))

    @presigned_url.setter
    def presigned_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e93ba6c4aa919324dc3ece78bc857e7d944a342cd87f5c12e0765e370f2a004)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "presignedUrl", value)

    @builtins.property
    @jsii.member(jsii_name="sourceDbSnapshotIdentifier")
    def source_db_snapshot_identifier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceDbSnapshotIdentifier"))

    @source_db_snapshot_identifier.setter
    def source_db_snapshot_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0f668ff2760796928d677c951e05d45aedbb2ef76be46b43c300dc0396795fd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceDbSnapshotIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7c6e057c4ddcb700566e2a93596ca31dd3fe1e8960eddea6e2ca4dccd34349b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed28df467e813d895608fef4a962278cd93dc7d7fb9942d3c3fb3aac96109131)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)

    @builtins.property
    @jsii.member(jsii_name="targetCustomAvailabilityZone")
    def target_custom_availability_zone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetCustomAvailabilityZone"))

    @target_custom_availability_zone.setter
    def target_custom_availability_zone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__65853343daa37077c018ba4acd8d9d08bb45911e29466f8494bc237117923336)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetCustomAvailabilityZone", value)

    @builtins.property
    @jsii.member(jsii_name="targetDbSnapshotIdentifier")
    def target_db_snapshot_identifier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetDbSnapshotIdentifier"))

    @target_db_snapshot_identifier.setter
    def target_db_snapshot_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__65706e599360ac151f888da7993842b2673ca57e07c71b91f12dd3564db5d23a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetDbSnapshotIdentifier", value)


@jsii.data_type(
    jsii_type="aws.dbSnapshotCopy.DbSnapshotCopyConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "source_db_snapshot_identifier": "sourceDbSnapshotIdentifier",
        "target_db_snapshot_identifier": "targetDbSnapshotIdentifier",
        "copy_tags": "copyTags",
        "destination_region": "destinationRegion",
        "id": "id",
        "kms_key_id": "kmsKeyId",
        "option_group_name": "optionGroupName",
        "presigned_url": "presignedUrl",
        "tags": "tags",
        "tags_all": "tagsAll",
        "target_custom_availability_zone": "targetCustomAvailabilityZone",
        "timeouts": "timeouts",
    },
)
class DbSnapshotCopyConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        source_db_snapshot_identifier: builtins.str,
        target_db_snapshot_identifier: builtins.str,
        copy_tags: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        destination_region: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        option_group_name: typing.Optional[builtins.str] = None,
        presigned_url: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        target_custom_availability_zone: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["DbSnapshotCopyTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param source_db_snapshot_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_snapshot_copy#source_db_snapshot_identifier DbSnapshotCopy#source_db_snapshot_identifier}.
        :param target_db_snapshot_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_snapshot_copy#target_db_snapshot_identifier DbSnapshotCopy#target_db_snapshot_identifier}.
        :param copy_tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_snapshot_copy#copy_tags DbSnapshotCopy#copy_tags}.
        :param destination_region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_snapshot_copy#destination_region DbSnapshotCopy#destination_region}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_snapshot_copy#id DbSnapshotCopy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_snapshot_copy#kms_key_id DbSnapshotCopy#kms_key_id}.
        :param option_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_snapshot_copy#option_group_name DbSnapshotCopy#option_group_name}.
        :param presigned_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_snapshot_copy#presigned_url DbSnapshotCopy#presigned_url}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_snapshot_copy#tags DbSnapshotCopy#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_snapshot_copy#tags_all DbSnapshotCopy#tags_all}.
        :param target_custom_availability_zone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_snapshot_copy#target_custom_availability_zone DbSnapshotCopy#target_custom_availability_zone}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_snapshot_copy#timeouts DbSnapshotCopy#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = DbSnapshotCopyTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__663fb65e23e890e988e54cf9dfa004535cdc31cd060c9bbb1c5a209c614a886a)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument source_db_snapshot_identifier", value=source_db_snapshot_identifier, expected_type=type_hints["source_db_snapshot_identifier"])
            check_type(argname="argument target_db_snapshot_identifier", value=target_db_snapshot_identifier, expected_type=type_hints["target_db_snapshot_identifier"])
            check_type(argname="argument copy_tags", value=copy_tags, expected_type=type_hints["copy_tags"])
            check_type(argname="argument destination_region", value=destination_region, expected_type=type_hints["destination_region"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            check_type(argname="argument option_group_name", value=option_group_name, expected_type=type_hints["option_group_name"])
            check_type(argname="argument presigned_url", value=presigned_url, expected_type=type_hints["presigned_url"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument target_custom_availability_zone", value=target_custom_availability_zone, expected_type=type_hints["target_custom_availability_zone"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "source_db_snapshot_identifier": source_db_snapshot_identifier,
            "target_db_snapshot_identifier": target_db_snapshot_identifier,
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
        if copy_tags is not None:
            self._values["copy_tags"] = copy_tags
        if destination_region is not None:
            self._values["destination_region"] = destination_region
        if id is not None:
            self._values["id"] = id
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if option_group_name is not None:
            self._values["option_group_name"] = option_group_name
        if presigned_url is not None:
            self._values["presigned_url"] = presigned_url
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if target_custom_availability_zone is not None:
            self._values["target_custom_availability_zone"] = target_custom_availability_zone
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
    def source_db_snapshot_identifier(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_snapshot_copy#source_db_snapshot_identifier DbSnapshotCopy#source_db_snapshot_identifier}.'''
        result = self._values.get("source_db_snapshot_identifier")
        assert result is not None, "Required property 'source_db_snapshot_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_db_snapshot_identifier(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_snapshot_copy#target_db_snapshot_identifier DbSnapshotCopy#target_db_snapshot_identifier}.'''
        result = self._values.get("target_db_snapshot_identifier")
        assert result is not None, "Required property 'target_db_snapshot_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def copy_tags(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_snapshot_copy#copy_tags DbSnapshotCopy#copy_tags}.'''
        result = self._values.get("copy_tags")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def destination_region(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_snapshot_copy#destination_region DbSnapshotCopy#destination_region}.'''
        result = self._values.get("destination_region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_snapshot_copy#id DbSnapshotCopy#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_snapshot_copy#kms_key_id DbSnapshotCopy#kms_key_id}.'''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def option_group_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_snapshot_copy#option_group_name DbSnapshotCopy#option_group_name}.'''
        result = self._values.get("option_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def presigned_url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_snapshot_copy#presigned_url DbSnapshotCopy#presigned_url}.'''
        result = self._values.get("presigned_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_snapshot_copy#tags DbSnapshotCopy#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_snapshot_copy#tags_all DbSnapshotCopy#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def target_custom_availability_zone(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_snapshot_copy#target_custom_availability_zone DbSnapshotCopy#target_custom_availability_zone}.'''
        result = self._values.get("target_custom_availability_zone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["DbSnapshotCopyTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_snapshot_copy#timeouts DbSnapshotCopy#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["DbSnapshotCopyTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DbSnapshotCopyConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.dbSnapshotCopy.DbSnapshotCopyTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create"},
)
class DbSnapshotCopyTimeouts:
    def __init__(self, *, create: typing.Optional[builtins.str] = None) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_snapshot_copy#create DbSnapshotCopy#create}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__465b03f7de6ff9951b042705dc8a5fc8e5d62056a3c59f1854ebe1174f3ac466)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_snapshot_copy#create DbSnapshotCopy#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DbSnapshotCopyTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DbSnapshotCopyTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dbSnapshotCopy.DbSnapshotCopyTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__bc97d6bda75d2a201737b20d4df5c868d6148bb7f017425bef362dfabc880db7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e09ac928cf250da045cbb98e5b6ee2934ceb57e59a0d8632117d9ad5964f6e9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DbSnapshotCopyTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DbSnapshotCopyTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DbSnapshotCopyTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4dbe831a56476f202d1299fd18db3e8966da983ae43b388602150c7128eac76d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DbSnapshotCopy",
    "DbSnapshotCopyConfig",
    "DbSnapshotCopyTimeouts",
    "DbSnapshotCopyTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__e6934dcaf2d3b27be5e2ae8953602bcc51fcb771bd7759cf06a87b9d72ff12c7(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    source_db_snapshot_identifier: builtins.str,
    target_db_snapshot_identifier: builtins.str,
    copy_tags: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    destination_region: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    option_group_name: typing.Optional[builtins.str] = None,
    presigned_url: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    target_custom_availability_zone: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[DbSnapshotCopyTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__f0568a5d8e255c2b65c0a5f51ce43abc1e17aef461afdea46ab01128761716a7(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d4228922a47d7a37d02ee28430ff62b39bff9294c87368cd7af9927f971dd40(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78583e68a6612b38d6e7f90735dcd6a05e0fb4dbd11bdbf0883a9ea5081d0253(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4ff58e894e8d45a84710095570f8cdaefc4f5675529e4bcba8db1c724d72162(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92d831902f75d35e83afdf0ec66182a032a1bb1d5067f2375710a1e892ac0848(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e93ba6c4aa919324dc3ece78bc857e7d944a342cd87f5c12e0765e370f2a004(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0f668ff2760796928d677c951e05d45aedbb2ef76be46b43c300dc0396795fd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7c6e057c4ddcb700566e2a93596ca31dd3fe1e8960eddea6e2ca4dccd34349b(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed28df467e813d895608fef4a962278cd93dc7d7fb9942d3c3fb3aac96109131(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65853343daa37077c018ba4acd8d9d08bb45911e29466f8494bc237117923336(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65706e599360ac151f888da7993842b2673ca57e07c71b91f12dd3564db5d23a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__663fb65e23e890e988e54cf9dfa004535cdc31cd060c9bbb1c5a209c614a886a(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    source_db_snapshot_identifier: builtins.str,
    target_db_snapshot_identifier: builtins.str,
    copy_tags: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    destination_region: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    option_group_name: typing.Optional[builtins.str] = None,
    presigned_url: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    target_custom_availability_zone: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[DbSnapshotCopyTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__465b03f7de6ff9951b042705dc8a5fc8e5d62056a3c59f1854ebe1174f3ac466(
    *,
    create: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc97d6bda75d2a201737b20d4df5c868d6148bb7f017425bef362dfabc880db7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e09ac928cf250da045cbb98e5b6ee2934ceb57e59a0d8632117d9ad5964f6e9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4dbe831a56476f202d1299fd18db3e8966da983ae43b388602150c7128eac76d(
    value: typing.Optional[typing.Union[DbSnapshotCopyTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
