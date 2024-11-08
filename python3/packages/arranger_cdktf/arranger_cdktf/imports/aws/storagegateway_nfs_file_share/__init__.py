'''
# `aws_storagegateway_nfs_file_share`

Refer to the Terraform Registory for docs: [`aws_storagegateway_nfs_file_share`](https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share).
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


class StoragegatewayNfsFileShare(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.storagegatewayNfsFileShare.StoragegatewayNfsFileShare",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share aws_storagegateway_nfs_file_share}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        client_list: typing.Sequence[builtins.str],
        gateway_arn: builtins.str,
        location_arn: builtins.str,
        role_arn: builtins.str,
        audit_destination_arn: typing.Optional[builtins.str] = None,
        bucket_region: typing.Optional[builtins.str] = None,
        cache_attributes: typing.Optional[typing.Union["StoragegatewayNfsFileShareCacheAttributes", typing.Dict[builtins.str, typing.Any]]] = None,
        default_storage_class: typing.Optional[builtins.str] = None,
        file_share_name: typing.Optional[builtins.str] = None,
        guess_mime_type_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        kms_encrypted: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
        nfs_file_share_defaults: typing.Optional[typing.Union["StoragegatewayNfsFileShareNfsFileShareDefaults", typing.Dict[builtins.str, typing.Any]]] = None,
        notification_policy: typing.Optional[builtins.str] = None,
        object_acl: typing.Optional[builtins.str] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        requester_pays: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        squash: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["StoragegatewayNfsFileShareTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        vpc_endpoint_dns_name: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share aws_storagegateway_nfs_file_share} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param client_list: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#client_list StoragegatewayNfsFileShare#client_list}.
        :param gateway_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#gateway_arn StoragegatewayNfsFileShare#gateway_arn}.
        :param location_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#location_arn StoragegatewayNfsFileShare#location_arn}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#role_arn StoragegatewayNfsFileShare#role_arn}.
        :param audit_destination_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#audit_destination_arn StoragegatewayNfsFileShare#audit_destination_arn}.
        :param bucket_region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#bucket_region StoragegatewayNfsFileShare#bucket_region}.
        :param cache_attributes: cache_attributes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#cache_attributes StoragegatewayNfsFileShare#cache_attributes}
        :param default_storage_class: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#default_storage_class StoragegatewayNfsFileShare#default_storage_class}.
        :param file_share_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#file_share_name StoragegatewayNfsFileShare#file_share_name}.
        :param guess_mime_type_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#guess_mime_type_enabled StoragegatewayNfsFileShare#guess_mime_type_enabled}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#id StoragegatewayNfsFileShare#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param kms_encrypted: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#kms_encrypted StoragegatewayNfsFileShare#kms_encrypted}.
        :param kms_key_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#kms_key_arn StoragegatewayNfsFileShare#kms_key_arn}.
        :param nfs_file_share_defaults: nfs_file_share_defaults block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#nfs_file_share_defaults StoragegatewayNfsFileShare#nfs_file_share_defaults}
        :param notification_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#notification_policy StoragegatewayNfsFileShare#notification_policy}.
        :param object_acl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#object_acl StoragegatewayNfsFileShare#object_acl}.
        :param read_only: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#read_only StoragegatewayNfsFileShare#read_only}.
        :param requester_pays: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#requester_pays StoragegatewayNfsFileShare#requester_pays}.
        :param squash: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#squash StoragegatewayNfsFileShare#squash}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#tags StoragegatewayNfsFileShare#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#tags_all StoragegatewayNfsFileShare#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#timeouts StoragegatewayNfsFileShare#timeouts}
        :param vpc_endpoint_dns_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#vpc_endpoint_dns_name StoragegatewayNfsFileShare#vpc_endpoint_dns_name}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__feb8b2dfd5d52bf141bc01fe258b20f3781f4f3b812fd17bfc23b035b73449f6)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = StoragegatewayNfsFileShareConfig(
            client_list=client_list,
            gateway_arn=gateway_arn,
            location_arn=location_arn,
            role_arn=role_arn,
            audit_destination_arn=audit_destination_arn,
            bucket_region=bucket_region,
            cache_attributes=cache_attributes,
            default_storage_class=default_storage_class,
            file_share_name=file_share_name,
            guess_mime_type_enabled=guess_mime_type_enabled,
            id=id,
            kms_encrypted=kms_encrypted,
            kms_key_arn=kms_key_arn,
            nfs_file_share_defaults=nfs_file_share_defaults,
            notification_policy=notification_policy,
            object_acl=object_acl,
            read_only=read_only,
            requester_pays=requester_pays,
            squash=squash,
            tags=tags,
            tags_all=tags_all,
            timeouts=timeouts,
            vpc_endpoint_dns_name=vpc_endpoint_dns_name,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putCacheAttributes")
    def put_cache_attributes(
        self,
        *,
        cache_stale_timeout_in_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param cache_stale_timeout_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#cache_stale_timeout_in_seconds StoragegatewayNfsFileShare#cache_stale_timeout_in_seconds}.
        '''
        value = StoragegatewayNfsFileShareCacheAttributes(
            cache_stale_timeout_in_seconds=cache_stale_timeout_in_seconds
        )

        return typing.cast(None, jsii.invoke(self, "putCacheAttributes", [value]))

    @jsii.member(jsii_name="putNfsFileShareDefaults")
    def put_nfs_file_share_defaults(
        self,
        *,
        directory_mode: typing.Optional[builtins.str] = None,
        file_mode: typing.Optional[builtins.str] = None,
        group_id: typing.Optional[builtins.str] = None,
        owner_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param directory_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#directory_mode StoragegatewayNfsFileShare#directory_mode}.
        :param file_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#file_mode StoragegatewayNfsFileShare#file_mode}.
        :param group_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#group_id StoragegatewayNfsFileShare#group_id}.
        :param owner_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#owner_id StoragegatewayNfsFileShare#owner_id}.
        '''
        value = StoragegatewayNfsFileShareNfsFileShareDefaults(
            directory_mode=directory_mode,
            file_mode=file_mode,
            group_id=group_id,
            owner_id=owner_id,
        )

        return typing.cast(None, jsii.invoke(self, "putNfsFileShareDefaults", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#create StoragegatewayNfsFileShare#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#delete StoragegatewayNfsFileShare#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#update StoragegatewayNfsFileShare#update}.
        '''
        value = StoragegatewayNfsFileShareTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAuditDestinationArn")
    def reset_audit_destination_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuditDestinationArn", []))

    @jsii.member(jsii_name="resetBucketRegion")
    def reset_bucket_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketRegion", []))

    @jsii.member(jsii_name="resetCacheAttributes")
    def reset_cache_attributes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCacheAttributes", []))

    @jsii.member(jsii_name="resetDefaultStorageClass")
    def reset_default_storage_class(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultStorageClass", []))

    @jsii.member(jsii_name="resetFileShareName")
    def reset_file_share_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFileShareName", []))

    @jsii.member(jsii_name="resetGuessMimeTypeEnabled")
    def reset_guess_mime_type_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGuessMimeTypeEnabled", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetKmsEncrypted")
    def reset_kms_encrypted(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsEncrypted", []))

    @jsii.member(jsii_name="resetKmsKeyArn")
    def reset_kms_key_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKeyArn", []))

    @jsii.member(jsii_name="resetNfsFileShareDefaults")
    def reset_nfs_file_share_defaults(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNfsFileShareDefaults", []))

    @jsii.member(jsii_name="resetNotificationPolicy")
    def reset_notification_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotificationPolicy", []))

    @jsii.member(jsii_name="resetObjectAcl")
    def reset_object_acl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetObjectAcl", []))

    @jsii.member(jsii_name="resetReadOnly")
    def reset_read_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadOnly", []))

    @jsii.member(jsii_name="resetRequesterPays")
    def reset_requester_pays(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequesterPays", []))

    @jsii.member(jsii_name="resetSquash")
    def reset_squash(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSquash", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetVpcEndpointDnsName")
    def reset_vpc_endpoint_dns_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVpcEndpointDnsName", []))

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
    @jsii.member(jsii_name="cacheAttributes")
    def cache_attributes(
        self,
    ) -> "StoragegatewayNfsFileShareCacheAttributesOutputReference":
        return typing.cast("StoragegatewayNfsFileShareCacheAttributesOutputReference", jsii.get(self, "cacheAttributes"))

    @builtins.property
    @jsii.member(jsii_name="fileshareId")
    def fileshare_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fileshareId"))

    @builtins.property
    @jsii.member(jsii_name="nfsFileShareDefaults")
    def nfs_file_share_defaults(
        self,
    ) -> "StoragegatewayNfsFileShareNfsFileShareDefaultsOutputReference":
        return typing.cast("StoragegatewayNfsFileShareNfsFileShareDefaultsOutputReference", jsii.get(self, "nfsFileShareDefaults"))

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "StoragegatewayNfsFileShareTimeoutsOutputReference":
        return typing.cast("StoragegatewayNfsFileShareTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="auditDestinationArnInput")
    def audit_destination_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "auditDestinationArnInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketRegionInput")
    def bucket_region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketRegionInput"))

    @builtins.property
    @jsii.member(jsii_name="cacheAttributesInput")
    def cache_attributes_input(
        self,
    ) -> typing.Optional["StoragegatewayNfsFileShareCacheAttributes"]:
        return typing.cast(typing.Optional["StoragegatewayNfsFileShareCacheAttributes"], jsii.get(self, "cacheAttributesInput"))

    @builtins.property
    @jsii.member(jsii_name="clientListInput")
    def client_list_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "clientListInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultStorageClassInput")
    def default_storage_class_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultStorageClassInput"))

    @builtins.property
    @jsii.member(jsii_name="fileShareNameInput")
    def file_share_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fileShareNameInput"))

    @builtins.property
    @jsii.member(jsii_name="gatewayArnInput")
    def gateway_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "gatewayArnInput"))

    @builtins.property
    @jsii.member(jsii_name="guessMimeTypeEnabledInput")
    def guess_mime_type_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "guessMimeTypeEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsEncryptedInput")
    def kms_encrypted_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "kmsEncryptedInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyArnInput")
    def kms_key_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyArnInput"))

    @builtins.property
    @jsii.member(jsii_name="locationArnInput")
    def location_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationArnInput"))

    @builtins.property
    @jsii.member(jsii_name="nfsFileShareDefaultsInput")
    def nfs_file_share_defaults_input(
        self,
    ) -> typing.Optional["StoragegatewayNfsFileShareNfsFileShareDefaults"]:
        return typing.cast(typing.Optional["StoragegatewayNfsFileShareNfsFileShareDefaults"], jsii.get(self, "nfsFileShareDefaultsInput"))

    @builtins.property
    @jsii.member(jsii_name="notificationPolicyInput")
    def notification_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "notificationPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="objectAclInput")
    def object_acl_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectAclInput"))

    @builtins.property
    @jsii.member(jsii_name="readOnlyInput")
    def read_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "readOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="requesterPaysInput")
    def requester_pays_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "requesterPaysInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="squashInput")
    def squash_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "squashInput"))

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
    ) -> typing.Optional[typing.Union["StoragegatewayNfsFileShareTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["StoragegatewayNfsFileShareTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="vpcEndpointDnsNameInput")
    def vpc_endpoint_dns_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vpcEndpointDnsNameInput"))

    @builtins.property
    @jsii.member(jsii_name="auditDestinationArn")
    def audit_destination_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "auditDestinationArn"))

    @audit_destination_arn.setter
    def audit_destination_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62a0456fd97e7af82792ccbc81ee28a24d42afa965ad49f32db89e99eb0e6d85)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "auditDestinationArn", value)

    @builtins.property
    @jsii.member(jsii_name="bucketRegion")
    def bucket_region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketRegion"))

    @bucket_region.setter
    def bucket_region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca43ac9b7b8a74364d644568131bdaa155b5d7890195a8787c476d982111766a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketRegion", value)

    @builtins.property
    @jsii.member(jsii_name="clientList")
    def client_list(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "clientList"))

    @client_list.setter
    def client_list(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a5ddd725fc035beff5bbe7615812875a9bb62ae41497e43b12745920ff674b2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientList", value)

    @builtins.property
    @jsii.member(jsii_name="defaultStorageClass")
    def default_storage_class(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultStorageClass"))

    @default_storage_class.setter
    def default_storage_class(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__afd4f15a0e5fff67ef6e057e811939a8815715bccd750136c3f9771f22e1f553)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultStorageClass", value)

    @builtins.property
    @jsii.member(jsii_name="fileShareName")
    def file_share_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fileShareName"))

    @file_share_name.setter
    def file_share_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6b0424a8ebb8be51028b1eba1ff2391c06513228049f9752f8e06d84657e947)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileShareName", value)

    @builtins.property
    @jsii.member(jsii_name="gatewayArn")
    def gateway_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gatewayArn"))

    @gateway_arn.setter
    def gateway_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a4d5a5bebb9b53a11c011f1abe34900dcd17eb32693e63ac2bc7e6d6336ae07)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gatewayArn", value)

    @builtins.property
    @jsii.member(jsii_name="guessMimeTypeEnabled")
    def guess_mime_type_enabled(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "guessMimeTypeEnabled"))

    @guess_mime_type_enabled.setter
    def guess_mime_type_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98cc08828f889e2bf2f1bc5f6788a16fba308013556d09a1eaa6f333a90a9152)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "guessMimeTypeEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67fbb7905de49385cbe3912d572be8bb1e6ac7ad3fc8cc8fc7e2d715f1c05c1f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="kmsEncrypted")
    def kms_encrypted(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "kmsEncrypted"))

    @kms_encrypted.setter
    def kms_encrypted(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8a53ea7e806c7e8a5c06b2185be12389ddf936dbae8952cd6f396a26e35c874)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsEncrypted", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyArn")
    def kms_key_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyArn"))

    @kms_key_arn.setter
    def kms_key_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a418a4dc5a10847e75a2b815a159399aea729d6c6f03b627e292d03d5f62e19c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyArn", value)

    @builtins.property
    @jsii.member(jsii_name="locationArn")
    def location_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "locationArn"))

    @location_arn.setter
    def location_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf6948246634a9cdbe68846f72ad657083653e3460ff8a25e37432f2fbe86600)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "locationArn", value)

    @builtins.property
    @jsii.member(jsii_name="notificationPolicy")
    def notification_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "notificationPolicy"))

    @notification_policy.setter
    def notification_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5e1a02054dbbff86885f4a9a3863428108bba417f88e7ce6931c84f234d6243)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notificationPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="objectAcl")
    def object_acl(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "objectAcl"))

    @object_acl.setter
    def object_acl(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b80afeb160bc31b90579ddd620da625870e39cafe364c3cf5d95ca2815379b5b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "objectAcl", value)

    @builtins.property
    @jsii.member(jsii_name="readOnly")
    def read_only(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "readOnly"))

    @read_only.setter
    def read_only(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bec32883c6938faa60b443344ad7dea8ea04f0d6bb5a1bd954b04cff666cff05)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readOnly", value)

    @builtins.property
    @jsii.member(jsii_name="requesterPays")
    def requester_pays(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "requesterPays"))

    @requester_pays.setter
    def requester_pays(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4be417807066bb593895d964d720a4542da791e959216338b70a2d83214150d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requesterPays", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c6f0a233dfbbb902f8b2f2898962448116c358cd0dff2ac2ef6bb27709f8218d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="squash")
    def squash(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "squash"))

    @squash.setter
    def squash(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3f5b532aa8ed585ed4a590109593f0af9d3ae26b6dedf46b50c0f91477953ac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "squash", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e117da4bf7b5d146a9ba66da1a006d28c51d359518d85d31ff81dd0caff3efc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5aa5f8f95e4e169b6ed4b5fc61ce23b719b257a04d8f75529b15e1bdc3a6684d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)

    @builtins.property
    @jsii.member(jsii_name="vpcEndpointDnsName")
    def vpc_endpoint_dns_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vpcEndpointDnsName"))

    @vpc_endpoint_dns_name.setter
    def vpc_endpoint_dns_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f833235144f3c52bea46ac2e1bda03c03003b784d2e74f8bc6540122725806d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcEndpointDnsName", value)


@jsii.data_type(
    jsii_type="aws.storagegatewayNfsFileShare.StoragegatewayNfsFileShareCacheAttributes",
    jsii_struct_bases=[],
    name_mapping={"cache_stale_timeout_in_seconds": "cacheStaleTimeoutInSeconds"},
)
class StoragegatewayNfsFileShareCacheAttributes:
    def __init__(
        self,
        *,
        cache_stale_timeout_in_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param cache_stale_timeout_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#cache_stale_timeout_in_seconds StoragegatewayNfsFileShare#cache_stale_timeout_in_seconds}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c7e63012bcf12b93c0bd58325e3a1a12f6b8204d15bbe0f920fc0440f943bd9)
            check_type(argname="argument cache_stale_timeout_in_seconds", value=cache_stale_timeout_in_seconds, expected_type=type_hints["cache_stale_timeout_in_seconds"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if cache_stale_timeout_in_seconds is not None:
            self._values["cache_stale_timeout_in_seconds"] = cache_stale_timeout_in_seconds

    @builtins.property
    def cache_stale_timeout_in_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#cache_stale_timeout_in_seconds StoragegatewayNfsFileShare#cache_stale_timeout_in_seconds}.'''
        result = self._values.get("cache_stale_timeout_in_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StoragegatewayNfsFileShareCacheAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StoragegatewayNfsFileShareCacheAttributesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.storagegatewayNfsFileShare.StoragegatewayNfsFileShareCacheAttributesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f59eb08714d7b3569b974211576cfcba775cb8fd4395e2a2f765a89689dc6a62)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCacheStaleTimeoutInSeconds")
    def reset_cache_stale_timeout_in_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCacheStaleTimeoutInSeconds", []))

    @builtins.property
    @jsii.member(jsii_name="cacheStaleTimeoutInSecondsInput")
    def cache_stale_timeout_in_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "cacheStaleTimeoutInSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="cacheStaleTimeoutInSeconds")
    def cache_stale_timeout_in_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "cacheStaleTimeoutInSeconds"))

    @cache_stale_timeout_in_seconds.setter
    def cache_stale_timeout_in_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__31c295cfccc0c18f88cd41706f9bd6bf20f63dcd39fa2451028cbbec052096fd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cacheStaleTimeoutInSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[StoragegatewayNfsFileShareCacheAttributes]:
        return typing.cast(typing.Optional[StoragegatewayNfsFileShareCacheAttributes], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[StoragegatewayNfsFileShareCacheAttributes],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ffe8857aa0d757470a04fd1700cd66cbce2c93f2a9e33fbc1474e255dedda2fe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.storagegatewayNfsFileShare.StoragegatewayNfsFileShareConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "client_list": "clientList",
        "gateway_arn": "gatewayArn",
        "location_arn": "locationArn",
        "role_arn": "roleArn",
        "audit_destination_arn": "auditDestinationArn",
        "bucket_region": "bucketRegion",
        "cache_attributes": "cacheAttributes",
        "default_storage_class": "defaultStorageClass",
        "file_share_name": "fileShareName",
        "guess_mime_type_enabled": "guessMimeTypeEnabled",
        "id": "id",
        "kms_encrypted": "kmsEncrypted",
        "kms_key_arn": "kmsKeyArn",
        "nfs_file_share_defaults": "nfsFileShareDefaults",
        "notification_policy": "notificationPolicy",
        "object_acl": "objectAcl",
        "read_only": "readOnly",
        "requester_pays": "requesterPays",
        "squash": "squash",
        "tags": "tags",
        "tags_all": "tagsAll",
        "timeouts": "timeouts",
        "vpc_endpoint_dns_name": "vpcEndpointDnsName",
    },
)
class StoragegatewayNfsFileShareConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        client_list: typing.Sequence[builtins.str],
        gateway_arn: builtins.str,
        location_arn: builtins.str,
        role_arn: builtins.str,
        audit_destination_arn: typing.Optional[builtins.str] = None,
        bucket_region: typing.Optional[builtins.str] = None,
        cache_attributes: typing.Optional[typing.Union[StoragegatewayNfsFileShareCacheAttributes, typing.Dict[builtins.str, typing.Any]]] = None,
        default_storage_class: typing.Optional[builtins.str] = None,
        file_share_name: typing.Optional[builtins.str] = None,
        guess_mime_type_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        kms_encrypted: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
        nfs_file_share_defaults: typing.Optional[typing.Union["StoragegatewayNfsFileShareNfsFileShareDefaults", typing.Dict[builtins.str, typing.Any]]] = None,
        notification_policy: typing.Optional[builtins.str] = None,
        object_acl: typing.Optional[builtins.str] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        requester_pays: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        squash: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["StoragegatewayNfsFileShareTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        vpc_endpoint_dns_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param client_list: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#client_list StoragegatewayNfsFileShare#client_list}.
        :param gateway_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#gateway_arn StoragegatewayNfsFileShare#gateway_arn}.
        :param location_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#location_arn StoragegatewayNfsFileShare#location_arn}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#role_arn StoragegatewayNfsFileShare#role_arn}.
        :param audit_destination_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#audit_destination_arn StoragegatewayNfsFileShare#audit_destination_arn}.
        :param bucket_region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#bucket_region StoragegatewayNfsFileShare#bucket_region}.
        :param cache_attributes: cache_attributes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#cache_attributes StoragegatewayNfsFileShare#cache_attributes}
        :param default_storage_class: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#default_storage_class StoragegatewayNfsFileShare#default_storage_class}.
        :param file_share_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#file_share_name StoragegatewayNfsFileShare#file_share_name}.
        :param guess_mime_type_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#guess_mime_type_enabled StoragegatewayNfsFileShare#guess_mime_type_enabled}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#id StoragegatewayNfsFileShare#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param kms_encrypted: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#kms_encrypted StoragegatewayNfsFileShare#kms_encrypted}.
        :param kms_key_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#kms_key_arn StoragegatewayNfsFileShare#kms_key_arn}.
        :param nfs_file_share_defaults: nfs_file_share_defaults block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#nfs_file_share_defaults StoragegatewayNfsFileShare#nfs_file_share_defaults}
        :param notification_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#notification_policy StoragegatewayNfsFileShare#notification_policy}.
        :param object_acl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#object_acl StoragegatewayNfsFileShare#object_acl}.
        :param read_only: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#read_only StoragegatewayNfsFileShare#read_only}.
        :param requester_pays: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#requester_pays StoragegatewayNfsFileShare#requester_pays}.
        :param squash: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#squash StoragegatewayNfsFileShare#squash}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#tags StoragegatewayNfsFileShare#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#tags_all StoragegatewayNfsFileShare#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#timeouts StoragegatewayNfsFileShare#timeouts}
        :param vpc_endpoint_dns_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#vpc_endpoint_dns_name StoragegatewayNfsFileShare#vpc_endpoint_dns_name}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(cache_attributes, dict):
            cache_attributes = StoragegatewayNfsFileShareCacheAttributes(**cache_attributes)
        if isinstance(nfs_file_share_defaults, dict):
            nfs_file_share_defaults = StoragegatewayNfsFileShareNfsFileShareDefaults(**nfs_file_share_defaults)
        if isinstance(timeouts, dict):
            timeouts = StoragegatewayNfsFileShareTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c9bb26a364c789344cfefbad99baa9f0404631fba513164dca520466a7f86d4a)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument client_list", value=client_list, expected_type=type_hints["client_list"])
            check_type(argname="argument gateway_arn", value=gateway_arn, expected_type=type_hints["gateway_arn"])
            check_type(argname="argument location_arn", value=location_arn, expected_type=type_hints["location_arn"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument audit_destination_arn", value=audit_destination_arn, expected_type=type_hints["audit_destination_arn"])
            check_type(argname="argument bucket_region", value=bucket_region, expected_type=type_hints["bucket_region"])
            check_type(argname="argument cache_attributes", value=cache_attributes, expected_type=type_hints["cache_attributes"])
            check_type(argname="argument default_storage_class", value=default_storage_class, expected_type=type_hints["default_storage_class"])
            check_type(argname="argument file_share_name", value=file_share_name, expected_type=type_hints["file_share_name"])
            check_type(argname="argument guess_mime_type_enabled", value=guess_mime_type_enabled, expected_type=type_hints["guess_mime_type_enabled"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument kms_encrypted", value=kms_encrypted, expected_type=type_hints["kms_encrypted"])
            check_type(argname="argument kms_key_arn", value=kms_key_arn, expected_type=type_hints["kms_key_arn"])
            check_type(argname="argument nfs_file_share_defaults", value=nfs_file_share_defaults, expected_type=type_hints["nfs_file_share_defaults"])
            check_type(argname="argument notification_policy", value=notification_policy, expected_type=type_hints["notification_policy"])
            check_type(argname="argument object_acl", value=object_acl, expected_type=type_hints["object_acl"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
            check_type(argname="argument requester_pays", value=requester_pays, expected_type=type_hints["requester_pays"])
            check_type(argname="argument squash", value=squash, expected_type=type_hints["squash"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument vpc_endpoint_dns_name", value=vpc_endpoint_dns_name, expected_type=type_hints["vpc_endpoint_dns_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "client_list": client_list,
            "gateway_arn": gateway_arn,
            "location_arn": location_arn,
            "role_arn": role_arn,
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
        if audit_destination_arn is not None:
            self._values["audit_destination_arn"] = audit_destination_arn
        if bucket_region is not None:
            self._values["bucket_region"] = bucket_region
        if cache_attributes is not None:
            self._values["cache_attributes"] = cache_attributes
        if default_storage_class is not None:
            self._values["default_storage_class"] = default_storage_class
        if file_share_name is not None:
            self._values["file_share_name"] = file_share_name
        if guess_mime_type_enabled is not None:
            self._values["guess_mime_type_enabled"] = guess_mime_type_enabled
        if id is not None:
            self._values["id"] = id
        if kms_encrypted is not None:
            self._values["kms_encrypted"] = kms_encrypted
        if kms_key_arn is not None:
            self._values["kms_key_arn"] = kms_key_arn
        if nfs_file_share_defaults is not None:
            self._values["nfs_file_share_defaults"] = nfs_file_share_defaults
        if notification_policy is not None:
            self._values["notification_policy"] = notification_policy
        if object_acl is not None:
            self._values["object_acl"] = object_acl
        if read_only is not None:
            self._values["read_only"] = read_only
        if requester_pays is not None:
            self._values["requester_pays"] = requester_pays
        if squash is not None:
            self._values["squash"] = squash
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if vpc_endpoint_dns_name is not None:
            self._values["vpc_endpoint_dns_name"] = vpc_endpoint_dns_name

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
    def client_list(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#client_list StoragegatewayNfsFileShare#client_list}.'''
        result = self._values.get("client_list")
        assert result is not None, "Required property 'client_list' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def gateway_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#gateway_arn StoragegatewayNfsFileShare#gateway_arn}.'''
        result = self._values.get("gateway_arn")
        assert result is not None, "Required property 'gateway_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def location_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#location_arn StoragegatewayNfsFileShare#location_arn}.'''
        result = self._values.get("location_arn")
        assert result is not None, "Required property 'location_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#role_arn StoragegatewayNfsFileShare#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def audit_destination_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#audit_destination_arn StoragegatewayNfsFileShare#audit_destination_arn}.'''
        result = self._values.get("audit_destination_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bucket_region(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#bucket_region StoragegatewayNfsFileShare#bucket_region}.'''
        result = self._values.get("bucket_region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cache_attributes(
        self,
    ) -> typing.Optional[StoragegatewayNfsFileShareCacheAttributes]:
        '''cache_attributes block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#cache_attributes StoragegatewayNfsFileShare#cache_attributes}
        '''
        result = self._values.get("cache_attributes")
        return typing.cast(typing.Optional[StoragegatewayNfsFileShareCacheAttributes], result)

    @builtins.property
    def default_storage_class(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#default_storage_class StoragegatewayNfsFileShare#default_storage_class}.'''
        result = self._values.get("default_storage_class")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def file_share_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#file_share_name StoragegatewayNfsFileShare#file_share_name}.'''
        result = self._values.get("file_share_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def guess_mime_type_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#guess_mime_type_enabled StoragegatewayNfsFileShare#guess_mime_type_enabled}.'''
        result = self._values.get("guess_mime_type_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#id StoragegatewayNfsFileShare#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_encrypted(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#kms_encrypted StoragegatewayNfsFileShare#kms_encrypted}.'''
        result = self._values.get("kms_encrypted")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#kms_key_arn StoragegatewayNfsFileShare#kms_key_arn}.'''
        result = self._values.get("kms_key_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def nfs_file_share_defaults(
        self,
    ) -> typing.Optional["StoragegatewayNfsFileShareNfsFileShareDefaults"]:
        '''nfs_file_share_defaults block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#nfs_file_share_defaults StoragegatewayNfsFileShare#nfs_file_share_defaults}
        '''
        result = self._values.get("nfs_file_share_defaults")
        return typing.cast(typing.Optional["StoragegatewayNfsFileShareNfsFileShareDefaults"], result)

    @builtins.property
    def notification_policy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#notification_policy StoragegatewayNfsFileShare#notification_policy}.'''
        result = self._values.get("notification_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def object_acl(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#object_acl StoragegatewayNfsFileShare#object_acl}.'''
        result = self._values.get("object_acl")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#read_only StoragegatewayNfsFileShare#read_only}.'''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def requester_pays(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#requester_pays StoragegatewayNfsFileShare#requester_pays}.'''
        result = self._values.get("requester_pays")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def squash(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#squash StoragegatewayNfsFileShare#squash}.'''
        result = self._values.get("squash")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#tags StoragegatewayNfsFileShare#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#tags_all StoragegatewayNfsFileShare#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["StoragegatewayNfsFileShareTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#timeouts StoragegatewayNfsFileShare#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["StoragegatewayNfsFileShareTimeouts"], result)

    @builtins.property
    def vpc_endpoint_dns_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#vpc_endpoint_dns_name StoragegatewayNfsFileShare#vpc_endpoint_dns_name}.'''
        result = self._values.get("vpc_endpoint_dns_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StoragegatewayNfsFileShareConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.storagegatewayNfsFileShare.StoragegatewayNfsFileShareNfsFileShareDefaults",
    jsii_struct_bases=[],
    name_mapping={
        "directory_mode": "directoryMode",
        "file_mode": "fileMode",
        "group_id": "groupId",
        "owner_id": "ownerId",
    },
)
class StoragegatewayNfsFileShareNfsFileShareDefaults:
    def __init__(
        self,
        *,
        directory_mode: typing.Optional[builtins.str] = None,
        file_mode: typing.Optional[builtins.str] = None,
        group_id: typing.Optional[builtins.str] = None,
        owner_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param directory_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#directory_mode StoragegatewayNfsFileShare#directory_mode}.
        :param file_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#file_mode StoragegatewayNfsFileShare#file_mode}.
        :param group_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#group_id StoragegatewayNfsFileShare#group_id}.
        :param owner_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#owner_id StoragegatewayNfsFileShare#owner_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__622ca9454eb18ee09609d4d235903e0eda0ed2db470a362f9a2c6991748501d4)
            check_type(argname="argument directory_mode", value=directory_mode, expected_type=type_hints["directory_mode"])
            check_type(argname="argument file_mode", value=file_mode, expected_type=type_hints["file_mode"])
            check_type(argname="argument group_id", value=group_id, expected_type=type_hints["group_id"])
            check_type(argname="argument owner_id", value=owner_id, expected_type=type_hints["owner_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if directory_mode is not None:
            self._values["directory_mode"] = directory_mode
        if file_mode is not None:
            self._values["file_mode"] = file_mode
        if group_id is not None:
            self._values["group_id"] = group_id
        if owner_id is not None:
            self._values["owner_id"] = owner_id

    @builtins.property
    def directory_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#directory_mode StoragegatewayNfsFileShare#directory_mode}.'''
        result = self._values.get("directory_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def file_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#file_mode StoragegatewayNfsFileShare#file_mode}.'''
        result = self._values.get("file_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def group_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#group_id StoragegatewayNfsFileShare#group_id}.'''
        result = self._values.get("group_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def owner_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#owner_id StoragegatewayNfsFileShare#owner_id}.'''
        result = self._values.get("owner_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StoragegatewayNfsFileShareNfsFileShareDefaults(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StoragegatewayNfsFileShareNfsFileShareDefaultsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.storagegatewayNfsFileShare.StoragegatewayNfsFileShareNfsFileShareDefaultsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5b3cc5f60ed7ea2f6d8f06a13462a7e7e1bc86756316ee36d4e519f41ab3c079)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDirectoryMode")
    def reset_directory_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDirectoryMode", []))

    @jsii.member(jsii_name="resetFileMode")
    def reset_file_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFileMode", []))

    @jsii.member(jsii_name="resetGroupId")
    def reset_group_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroupId", []))

    @jsii.member(jsii_name="resetOwnerId")
    def reset_owner_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOwnerId", []))

    @builtins.property
    @jsii.member(jsii_name="directoryModeInput")
    def directory_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "directoryModeInput"))

    @builtins.property
    @jsii.member(jsii_name="fileModeInput")
    def file_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fileModeInput"))

    @builtins.property
    @jsii.member(jsii_name="groupIdInput")
    def group_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "groupIdInput"))

    @builtins.property
    @jsii.member(jsii_name="ownerIdInput")
    def owner_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ownerIdInput"))

    @builtins.property
    @jsii.member(jsii_name="directoryMode")
    def directory_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "directoryMode"))

    @directory_mode.setter
    def directory_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c14017d2d9a5390746121dd90d86618da59476210ae7336c77eff72844e9776c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "directoryMode", value)

    @builtins.property
    @jsii.member(jsii_name="fileMode")
    def file_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fileMode"))

    @file_mode.setter
    def file_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__721301c4620cc311c50a571a9ab1c38cccf4f0ccd32f1ed7f6989f2117c94594)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileMode", value)

    @builtins.property
    @jsii.member(jsii_name="groupId")
    def group_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "groupId"))

    @group_id.setter
    def group_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa6de9b7b535271226114d93fd7a0c029659b82623cc486bf4efbc2964971dc1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupId", value)

    @builtins.property
    @jsii.member(jsii_name="ownerId")
    def owner_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ownerId"))

    @owner_id.setter
    def owner_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd9a0610500f85a7edefeb0faec3adc1fba76cc41e3d2d8ab76117a7f3082304)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ownerId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[StoragegatewayNfsFileShareNfsFileShareDefaults]:
        return typing.cast(typing.Optional[StoragegatewayNfsFileShareNfsFileShareDefaults], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[StoragegatewayNfsFileShareNfsFileShareDefaults],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3fe978d4443df92620b4a38e502c9900771a47c24d735b3a67192c5368232fb3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.storagegatewayNfsFileShare.StoragegatewayNfsFileShareTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class StoragegatewayNfsFileShareTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#create StoragegatewayNfsFileShare#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#delete StoragegatewayNfsFileShare#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#update StoragegatewayNfsFileShare#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66cc1dcb804436f8b21ac01d8af8bc40e3af0611f13195e39dda3eb00454cf94)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#create StoragegatewayNfsFileShare#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#delete StoragegatewayNfsFileShare#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share#update StoragegatewayNfsFileShare#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StoragegatewayNfsFileShareTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StoragegatewayNfsFileShareTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.storagegatewayNfsFileShare.StoragegatewayNfsFileShareTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c54afb4f0f4e7ba3fdc8db9f475db7f5407aef50ee22a18d4557b391defdebd4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__505d8ac9e54b5bec4f039274c178bcb0bef2fc3602a9993f5bff7844998f0c78)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__217196e691b9920bdcd0dd2561d9ce6e66009bc4b90f5477b0ce4a50d67644ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__627eedf226b8afba0a8b899c9c9f4f4f85b7ee9a10e9c2fd03248b85033109fc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[StoragegatewayNfsFileShareTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[StoragegatewayNfsFileShareTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[StoragegatewayNfsFileShareTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f3f44d0e324b5e0b8ff0719d524ddab4346d78f2d69772d06b77d552e69dc92c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "StoragegatewayNfsFileShare",
    "StoragegatewayNfsFileShareCacheAttributes",
    "StoragegatewayNfsFileShareCacheAttributesOutputReference",
    "StoragegatewayNfsFileShareConfig",
    "StoragegatewayNfsFileShareNfsFileShareDefaults",
    "StoragegatewayNfsFileShareNfsFileShareDefaultsOutputReference",
    "StoragegatewayNfsFileShareTimeouts",
    "StoragegatewayNfsFileShareTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__feb8b2dfd5d52bf141bc01fe258b20f3781f4f3b812fd17bfc23b035b73449f6(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    client_list: typing.Sequence[builtins.str],
    gateway_arn: builtins.str,
    location_arn: builtins.str,
    role_arn: builtins.str,
    audit_destination_arn: typing.Optional[builtins.str] = None,
    bucket_region: typing.Optional[builtins.str] = None,
    cache_attributes: typing.Optional[typing.Union[StoragegatewayNfsFileShareCacheAttributes, typing.Dict[builtins.str, typing.Any]]] = None,
    default_storage_class: typing.Optional[builtins.str] = None,
    file_share_name: typing.Optional[builtins.str] = None,
    guess_mime_type_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    kms_encrypted: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    kms_key_arn: typing.Optional[builtins.str] = None,
    nfs_file_share_defaults: typing.Optional[typing.Union[StoragegatewayNfsFileShareNfsFileShareDefaults, typing.Dict[builtins.str, typing.Any]]] = None,
    notification_policy: typing.Optional[builtins.str] = None,
    object_acl: typing.Optional[builtins.str] = None,
    read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    requester_pays: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    squash: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[StoragegatewayNfsFileShareTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    vpc_endpoint_dns_name: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__62a0456fd97e7af82792ccbc81ee28a24d42afa965ad49f32db89e99eb0e6d85(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca43ac9b7b8a74364d644568131bdaa155b5d7890195a8787c476d982111766a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a5ddd725fc035beff5bbe7615812875a9bb62ae41497e43b12745920ff674b2(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afd4f15a0e5fff67ef6e057e811939a8815715bccd750136c3f9771f22e1f553(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6b0424a8ebb8be51028b1eba1ff2391c06513228049f9752f8e06d84657e947(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a4d5a5bebb9b53a11c011f1abe34900dcd17eb32693e63ac2bc7e6d6336ae07(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98cc08828f889e2bf2f1bc5f6788a16fba308013556d09a1eaa6f333a90a9152(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67fbb7905de49385cbe3912d572be8bb1e6ac7ad3fc8cc8fc7e2d715f1c05c1f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8a53ea7e806c7e8a5c06b2185be12389ddf936dbae8952cd6f396a26e35c874(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a418a4dc5a10847e75a2b815a159399aea729d6c6f03b627e292d03d5f62e19c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf6948246634a9cdbe68846f72ad657083653e3460ff8a25e37432f2fbe86600(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5e1a02054dbbff86885f4a9a3863428108bba417f88e7ce6931c84f234d6243(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b80afeb160bc31b90579ddd620da625870e39cafe364c3cf5d95ca2815379b5b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bec32883c6938faa60b443344ad7dea8ea04f0d6bb5a1bd954b04cff666cff05(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4be417807066bb593895d964d720a4542da791e959216338b70a2d83214150d(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6f0a233dfbbb902f8b2f2898962448116c358cd0dff2ac2ef6bb27709f8218d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3f5b532aa8ed585ed4a590109593f0af9d3ae26b6dedf46b50c0f91477953ac(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e117da4bf7b5d146a9ba66da1a006d28c51d359518d85d31ff81dd0caff3efc(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5aa5f8f95e4e169b6ed4b5fc61ce23b719b257a04d8f75529b15e1bdc3a6684d(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f833235144f3c52bea46ac2e1bda03c03003b784d2e74f8bc6540122725806d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c7e63012bcf12b93c0bd58325e3a1a12f6b8204d15bbe0f920fc0440f943bd9(
    *,
    cache_stale_timeout_in_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f59eb08714d7b3569b974211576cfcba775cb8fd4395e2a2f765a89689dc6a62(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31c295cfccc0c18f88cd41706f9bd6bf20f63dcd39fa2451028cbbec052096fd(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ffe8857aa0d757470a04fd1700cd66cbce2c93f2a9e33fbc1474e255dedda2fe(
    value: typing.Optional[StoragegatewayNfsFileShareCacheAttributes],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9bb26a364c789344cfefbad99baa9f0404631fba513164dca520466a7f86d4a(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    client_list: typing.Sequence[builtins.str],
    gateway_arn: builtins.str,
    location_arn: builtins.str,
    role_arn: builtins.str,
    audit_destination_arn: typing.Optional[builtins.str] = None,
    bucket_region: typing.Optional[builtins.str] = None,
    cache_attributes: typing.Optional[typing.Union[StoragegatewayNfsFileShareCacheAttributes, typing.Dict[builtins.str, typing.Any]]] = None,
    default_storage_class: typing.Optional[builtins.str] = None,
    file_share_name: typing.Optional[builtins.str] = None,
    guess_mime_type_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    kms_encrypted: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    kms_key_arn: typing.Optional[builtins.str] = None,
    nfs_file_share_defaults: typing.Optional[typing.Union[StoragegatewayNfsFileShareNfsFileShareDefaults, typing.Dict[builtins.str, typing.Any]]] = None,
    notification_policy: typing.Optional[builtins.str] = None,
    object_acl: typing.Optional[builtins.str] = None,
    read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    requester_pays: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    squash: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[StoragegatewayNfsFileShareTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    vpc_endpoint_dns_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__622ca9454eb18ee09609d4d235903e0eda0ed2db470a362f9a2c6991748501d4(
    *,
    directory_mode: typing.Optional[builtins.str] = None,
    file_mode: typing.Optional[builtins.str] = None,
    group_id: typing.Optional[builtins.str] = None,
    owner_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b3cc5f60ed7ea2f6d8f06a13462a7e7e1bc86756316ee36d4e519f41ab3c079(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c14017d2d9a5390746121dd90d86618da59476210ae7336c77eff72844e9776c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__721301c4620cc311c50a571a9ab1c38cccf4f0ccd32f1ed7f6989f2117c94594(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa6de9b7b535271226114d93fd7a0c029659b82623cc486bf4efbc2964971dc1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd9a0610500f85a7edefeb0faec3adc1fba76cc41e3d2d8ab76117a7f3082304(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3fe978d4443df92620b4a38e502c9900771a47c24d735b3a67192c5368232fb3(
    value: typing.Optional[StoragegatewayNfsFileShareNfsFileShareDefaults],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66cc1dcb804436f8b21ac01d8af8bc40e3af0611f13195e39dda3eb00454cf94(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c54afb4f0f4e7ba3fdc8db9f475db7f5407aef50ee22a18d4557b391defdebd4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__505d8ac9e54b5bec4f039274c178bcb0bef2fc3602a9993f5bff7844998f0c78(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__217196e691b9920bdcd0dd2561d9ce6e66009bc4b90f5477b0ce4a50d67644ae(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__627eedf226b8afba0a8b899c9c9f4f4f85b7ee9a10e9c2fd03248b85033109fc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3f44d0e324b5e0b8ff0719d524ddab4346d78f2d69772d06b77d552e69dc92c(
    value: typing.Optional[typing.Union[StoragegatewayNfsFileShareTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
