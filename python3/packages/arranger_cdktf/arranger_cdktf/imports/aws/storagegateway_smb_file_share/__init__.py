'''
# `aws_storagegateway_smb_file_share`

Refer to the Terraform Registory for docs: [`aws_storagegateway_smb_file_share`](https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share).
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


class StoragegatewaySmbFileShare(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.storagegatewaySmbFileShare.StoragegatewaySmbFileShare",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share aws_storagegateway_smb_file_share}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        gateway_arn: builtins.str,
        location_arn: builtins.str,
        role_arn: builtins.str,
        access_based_enumeration: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        admin_user_list: typing.Optional[typing.Sequence[builtins.str]] = None,
        audit_destination_arn: typing.Optional[builtins.str] = None,
        authentication: typing.Optional[builtins.str] = None,
        bucket_region: typing.Optional[builtins.str] = None,
        cache_attributes: typing.Optional[typing.Union["StoragegatewaySmbFileShareCacheAttributes", typing.Dict[builtins.str, typing.Any]]] = None,
        case_sensitivity: typing.Optional[builtins.str] = None,
        default_storage_class: typing.Optional[builtins.str] = None,
        file_share_name: typing.Optional[builtins.str] = None,
        guess_mime_type_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        invalid_user_list: typing.Optional[typing.Sequence[builtins.str]] = None,
        kms_encrypted: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
        notification_policy: typing.Optional[builtins.str] = None,
        object_acl: typing.Optional[builtins.str] = None,
        oplocks_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        requester_pays: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        smb_acl_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["StoragegatewaySmbFileShareTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        valid_user_list: typing.Optional[typing.Sequence[builtins.str]] = None,
        vpc_endpoint_dns_name: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share aws_storagegateway_smb_file_share} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param gateway_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#gateway_arn StoragegatewaySmbFileShare#gateway_arn}.
        :param location_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#location_arn StoragegatewaySmbFileShare#location_arn}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#role_arn StoragegatewaySmbFileShare#role_arn}.
        :param access_based_enumeration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#access_based_enumeration StoragegatewaySmbFileShare#access_based_enumeration}.
        :param admin_user_list: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#admin_user_list StoragegatewaySmbFileShare#admin_user_list}.
        :param audit_destination_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#audit_destination_arn StoragegatewaySmbFileShare#audit_destination_arn}.
        :param authentication: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#authentication StoragegatewaySmbFileShare#authentication}.
        :param bucket_region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#bucket_region StoragegatewaySmbFileShare#bucket_region}.
        :param cache_attributes: cache_attributes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#cache_attributes StoragegatewaySmbFileShare#cache_attributes}
        :param case_sensitivity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#case_sensitivity StoragegatewaySmbFileShare#case_sensitivity}.
        :param default_storage_class: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#default_storage_class StoragegatewaySmbFileShare#default_storage_class}.
        :param file_share_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#file_share_name StoragegatewaySmbFileShare#file_share_name}.
        :param guess_mime_type_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#guess_mime_type_enabled StoragegatewaySmbFileShare#guess_mime_type_enabled}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#id StoragegatewaySmbFileShare#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param invalid_user_list: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#invalid_user_list StoragegatewaySmbFileShare#invalid_user_list}.
        :param kms_encrypted: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#kms_encrypted StoragegatewaySmbFileShare#kms_encrypted}.
        :param kms_key_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#kms_key_arn StoragegatewaySmbFileShare#kms_key_arn}.
        :param notification_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#notification_policy StoragegatewaySmbFileShare#notification_policy}.
        :param object_acl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#object_acl StoragegatewaySmbFileShare#object_acl}.
        :param oplocks_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#oplocks_enabled StoragegatewaySmbFileShare#oplocks_enabled}.
        :param read_only: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#read_only StoragegatewaySmbFileShare#read_only}.
        :param requester_pays: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#requester_pays StoragegatewaySmbFileShare#requester_pays}.
        :param smb_acl_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#smb_acl_enabled StoragegatewaySmbFileShare#smb_acl_enabled}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#tags StoragegatewaySmbFileShare#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#tags_all StoragegatewaySmbFileShare#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#timeouts StoragegatewaySmbFileShare#timeouts}
        :param valid_user_list: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#valid_user_list StoragegatewaySmbFileShare#valid_user_list}.
        :param vpc_endpoint_dns_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#vpc_endpoint_dns_name StoragegatewaySmbFileShare#vpc_endpoint_dns_name}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b914268fdd5e94dc84507944ac32452e814470b8a7aeb6c3332dc595f12f026)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = StoragegatewaySmbFileShareConfig(
            gateway_arn=gateway_arn,
            location_arn=location_arn,
            role_arn=role_arn,
            access_based_enumeration=access_based_enumeration,
            admin_user_list=admin_user_list,
            audit_destination_arn=audit_destination_arn,
            authentication=authentication,
            bucket_region=bucket_region,
            cache_attributes=cache_attributes,
            case_sensitivity=case_sensitivity,
            default_storage_class=default_storage_class,
            file_share_name=file_share_name,
            guess_mime_type_enabled=guess_mime_type_enabled,
            id=id,
            invalid_user_list=invalid_user_list,
            kms_encrypted=kms_encrypted,
            kms_key_arn=kms_key_arn,
            notification_policy=notification_policy,
            object_acl=object_acl,
            oplocks_enabled=oplocks_enabled,
            read_only=read_only,
            requester_pays=requester_pays,
            smb_acl_enabled=smb_acl_enabled,
            tags=tags,
            tags_all=tags_all,
            timeouts=timeouts,
            valid_user_list=valid_user_list,
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
        :param cache_stale_timeout_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#cache_stale_timeout_in_seconds StoragegatewaySmbFileShare#cache_stale_timeout_in_seconds}.
        '''
        value = StoragegatewaySmbFileShareCacheAttributes(
            cache_stale_timeout_in_seconds=cache_stale_timeout_in_seconds
        )

        return typing.cast(None, jsii.invoke(self, "putCacheAttributes", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#create StoragegatewaySmbFileShare#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#delete StoragegatewaySmbFileShare#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#update StoragegatewaySmbFileShare#update}.
        '''
        value = StoragegatewaySmbFileShareTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAccessBasedEnumeration")
    def reset_access_based_enumeration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessBasedEnumeration", []))

    @jsii.member(jsii_name="resetAdminUserList")
    def reset_admin_user_list(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdminUserList", []))

    @jsii.member(jsii_name="resetAuditDestinationArn")
    def reset_audit_destination_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuditDestinationArn", []))

    @jsii.member(jsii_name="resetAuthentication")
    def reset_authentication(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthentication", []))

    @jsii.member(jsii_name="resetBucketRegion")
    def reset_bucket_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketRegion", []))

    @jsii.member(jsii_name="resetCacheAttributes")
    def reset_cache_attributes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCacheAttributes", []))

    @jsii.member(jsii_name="resetCaseSensitivity")
    def reset_case_sensitivity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCaseSensitivity", []))

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

    @jsii.member(jsii_name="resetInvalidUserList")
    def reset_invalid_user_list(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInvalidUserList", []))

    @jsii.member(jsii_name="resetKmsEncrypted")
    def reset_kms_encrypted(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsEncrypted", []))

    @jsii.member(jsii_name="resetKmsKeyArn")
    def reset_kms_key_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKeyArn", []))

    @jsii.member(jsii_name="resetNotificationPolicy")
    def reset_notification_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotificationPolicy", []))

    @jsii.member(jsii_name="resetObjectAcl")
    def reset_object_acl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetObjectAcl", []))

    @jsii.member(jsii_name="resetOplocksEnabled")
    def reset_oplocks_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOplocksEnabled", []))

    @jsii.member(jsii_name="resetReadOnly")
    def reset_read_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadOnly", []))

    @jsii.member(jsii_name="resetRequesterPays")
    def reset_requester_pays(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequesterPays", []))

    @jsii.member(jsii_name="resetSmbAclEnabled")
    def reset_smb_acl_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSmbAclEnabled", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetValidUserList")
    def reset_valid_user_list(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValidUserList", []))

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
    ) -> "StoragegatewaySmbFileShareCacheAttributesOutputReference":
        return typing.cast("StoragegatewaySmbFileShareCacheAttributesOutputReference", jsii.get(self, "cacheAttributes"))

    @builtins.property
    @jsii.member(jsii_name="fileshareId")
    def fileshare_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fileshareId"))

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "StoragegatewaySmbFileShareTimeoutsOutputReference":
        return typing.cast("StoragegatewaySmbFileShareTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="accessBasedEnumerationInput")
    def access_based_enumeration_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "accessBasedEnumerationInput"))

    @builtins.property
    @jsii.member(jsii_name="adminUserListInput")
    def admin_user_list_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "adminUserListInput"))

    @builtins.property
    @jsii.member(jsii_name="auditDestinationArnInput")
    def audit_destination_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "auditDestinationArnInput"))

    @builtins.property
    @jsii.member(jsii_name="authenticationInput")
    def authentication_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authenticationInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketRegionInput")
    def bucket_region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketRegionInput"))

    @builtins.property
    @jsii.member(jsii_name="cacheAttributesInput")
    def cache_attributes_input(
        self,
    ) -> typing.Optional["StoragegatewaySmbFileShareCacheAttributes"]:
        return typing.cast(typing.Optional["StoragegatewaySmbFileShareCacheAttributes"], jsii.get(self, "cacheAttributesInput"))

    @builtins.property
    @jsii.member(jsii_name="caseSensitivityInput")
    def case_sensitivity_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "caseSensitivityInput"))

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
    @jsii.member(jsii_name="invalidUserListInput")
    def invalid_user_list_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "invalidUserListInput"))

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
    @jsii.member(jsii_name="notificationPolicyInput")
    def notification_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "notificationPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="objectAclInput")
    def object_acl_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectAclInput"))

    @builtins.property
    @jsii.member(jsii_name="oplocksEnabledInput")
    def oplocks_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "oplocksEnabledInput"))

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
    @jsii.member(jsii_name="smbAclEnabledInput")
    def smb_acl_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "smbAclEnabledInput"))

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
    ) -> typing.Optional[typing.Union["StoragegatewaySmbFileShareTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["StoragegatewaySmbFileShareTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="validUserListInput")
    def valid_user_list_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "validUserListInput"))

    @builtins.property
    @jsii.member(jsii_name="vpcEndpointDnsNameInput")
    def vpc_endpoint_dns_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vpcEndpointDnsNameInput"))

    @builtins.property
    @jsii.member(jsii_name="accessBasedEnumeration")
    def access_based_enumeration(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "accessBasedEnumeration"))

    @access_based_enumeration.setter
    def access_based_enumeration(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99ab31efdce589d75cfc3e7815f103ffc2675ac1f8f31bc2113f008891c6a618)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessBasedEnumeration", value)

    @builtins.property
    @jsii.member(jsii_name="adminUserList")
    def admin_user_list(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "adminUserList"))

    @admin_user_list.setter
    def admin_user_list(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c9cc6f2b32fdbdb6b7a18c66d20fe55cb9a13a6bae649158fd97093b0d30b840)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adminUserList", value)

    @builtins.property
    @jsii.member(jsii_name="auditDestinationArn")
    def audit_destination_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "auditDestinationArn"))

    @audit_destination_arn.setter
    def audit_destination_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7edcbe8d937883ff3cde00503bee1063a7bb5d918d53ce46ccfee6a40e6b543d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "auditDestinationArn", value)

    @builtins.property
    @jsii.member(jsii_name="authentication")
    def authentication(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authentication"))

    @authentication.setter
    def authentication(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__508c824fb409c01e097cbd36ee5e992b076c0757aa5487c9300084d9c24cf837)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authentication", value)

    @builtins.property
    @jsii.member(jsii_name="bucketRegion")
    def bucket_region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketRegion"))

    @bucket_region.setter
    def bucket_region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6463dc05288aa59540f8e85d01b59af40f563e63fa81301bf5ddfbeac1908e63)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketRegion", value)

    @builtins.property
    @jsii.member(jsii_name="caseSensitivity")
    def case_sensitivity(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "caseSensitivity"))

    @case_sensitivity.setter
    def case_sensitivity(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c6d18ce844e5f2e1f093f684aaba559c1134265627be2c46ede5fbdf54cc3c8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "caseSensitivity", value)

    @builtins.property
    @jsii.member(jsii_name="defaultStorageClass")
    def default_storage_class(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultStorageClass"))

    @default_storage_class.setter
    def default_storage_class(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__837f01a36e660882bdb501ce6d5baceaa2f1ef0e573675d372ed9933046e1415)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultStorageClass", value)

    @builtins.property
    @jsii.member(jsii_name="fileShareName")
    def file_share_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fileShareName"))

    @file_share_name.setter
    def file_share_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56be707ecaf4e97f30feb4151466a88228677b17dd35b04f37f2cbee0a4a74d4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileShareName", value)

    @builtins.property
    @jsii.member(jsii_name="gatewayArn")
    def gateway_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gatewayArn"))

    @gateway_arn.setter
    def gateway_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8fdf64bd1de10cb3cd5906cfb61fb931cf240b7d7bd69efbed9a643896d5e253)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2ae9092b7c2b63c8dee1174abfd3bc2016202b68a839629a7f6834a39f4e8c6d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "guessMimeTypeEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32f35b5b9546a0931a09d787930b307a410001bc6a0a53be3219bf8206b00371)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="invalidUserList")
    def invalid_user_list(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "invalidUserList"))

    @invalid_user_list.setter
    def invalid_user_list(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80df646e4662adffdd9b6caec58cc744b8c9710141352da6a6c2ac52bb294528)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "invalidUserList", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__6699d3909f9b71ec7e8dd4b96942801c3fc647d0053b42a944df87a48e73a9ac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsEncrypted", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyArn")
    def kms_key_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyArn"))

    @kms_key_arn.setter
    def kms_key_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ffb24caac3ea651a74361055c1446812933f323583cacd75e504f28ef95e245)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyArn", value)

    @builtins.property
    @jsii.member(jsii_name="locationArn")
    def location_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "locationArn"))

    @location_arn.setter
    def location_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce3b1891226c1c783344b3da29040efc195a1738ec03c4cf197ed2e4df974bb5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "locationArn", value)

    @builtins.property
    @jsii.member(jsii_name="notificationPolicy")
    def notification_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "notificationPolicy"))

    @notification_policy.setter
    def notification_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94cde6984ea86c8e0edb2d74f7bb73a5689a1201e0b65493be4083f519729e9b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notificationPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="objectAcl")
    def object_acl(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "objectAcl"))

    @object_acl.setter
    def object_acl(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__785208f35955e7116fa782f817f8d6f652d303a89b8d3a777fa733a6a809ff96)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "objectAcl", value)

    @builtins.property
    @jsii.member(jsii_name="oplocksEnabled")
    def oplocks_enabled(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "oplocksEnabled"))

    @oplocks_enabled.setter
    def oplocks_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8fceebf25e2442995d4b9ccfaaad3bb331d684492b2465fb5b67db20492165c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oplocksEnabled", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__a5dae2da4be16fd0dd5e5d77780075e7c82c0f1518e54579401ffe1dd54fc2cc)
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
            type_hints = typing.get_type_hints(_typecheckingstub__68a79c5b1f02afb6db4c1de1ab985e3e03d4bae13a96332e785f4bc4be5166cc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requesterPays", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fcbd6e2606c33134b9cc92270744c3bdf6b4ab05b206001de487b5acf1e955fe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="smbAclEnabled")
    def smb_acl_enabled(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "smbAclEnabled"))

    @smb_acl_enabled.setter
    def smb_acl_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__036ed8dfe7c31ff0d2aa65d5059cd8779afba83c985bb44760be32dcf0bc780d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "smbAclEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7745f864b1a33444dbc706e05c0e43c41918cdc395e99eaa33170134e20ce586)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed37f1665578747f84f686d70a72bbe29dfe5ac840dccc12e9b1502d3a0b96ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)

    @builtins.property
    @jsii.member(jsii_name="validUserList")
    def valid_user_list(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "validUserList"))

    @valid_user_list.setter
    def valid_user_list(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec4d7b2f83960c7ea730f5249f078e277173dc70a662b109267741d20ec79f5a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "validUserList", value)

    @builtins.property
    @jsii.member(jsii_name="vpcEndpointDnsName")
    def vpc_endpoint_dns_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vpcEndpointDnsName"))

    @vpc_endpoint_dns_name.setter
    def vpc_endpoint_dns_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6863aee0cbf3621d7a798fb338a2a1248203a5d8c9c0ef1adf6df42eb46ff9ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcEndpointDnsName", value)


@jsii.data_type(
    jsii_type="aws.storagegatewaySmbFileShare.StoragegatewaySmbFileShareCacheAttributes",
    jsii_struct_bases=[],
    name_mapping={"cache_stale_timeout_in_seconds": "cacheStaleTimeoutInSeconds"},
)
class StoragegatewaySmbFileShareCacheAttributes:
    def __init__(
        self,
        *,
        cache_stale_timeout_in_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param cache_stale_timeout_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#cache_stale_timeout_in_seconds StoragegatewaySmbFileShare#cache_stale_timeout_in_seconds}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0f78321b5522bffa167bce81ebc644f8ec9d705ea5664720b8208f679a6eb1f)
            check_type(argname="argument cache_stale_timeout_in_seconds", value=cache_stale_timeout_in_seconds, expected_type=type_hints["cache_stale_timeout_in_seconds"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if cache_stale_timeout_in_seconds is not None:
            self._values["cache_stale_timeout_in_seconds"] = cache_stale_timeout_in_seconds

    @builtins.property
    def cache_stale_timeout_in_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#cache_stale_timeout_in_seconds StoragegatewaySmbFileShare#cache_stale_timeout_in_seconds}.'''
        result = self._values.get("cache_stale_timeout_in_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StoragegatewaySmbFileShareCacheAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StoragegatewaySmbFileShareCacheAttributesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.storagegatewaySmbFileShare.StoragegatewaySmbFileShareCacheAttributesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ad12b1e8a4021a9dc198b86441a0e33d3b311dd7bac5178d1a97296d141abf05)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9063be72ea781f14e0bf3280ec5f19bce701c27158293adf26415c9aa9a6ffe5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cacheStaleTimeoutInSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[StoragegatewaySmbFileShareCacheAttributes]:
        return typing.cast(typing.Optional[StoragegatewaySmbFileShareCacheAttributes], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[StoragegatewaySmbFileShareCacheAttributes],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__372cbd41f41ce2a7c79db37f41f8452b524ed2fe295cd8786ebba57eb4fefa84)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.storagegatewaySmbFileShare.StoragegatewaySmbFileShareConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "gateway_arn": "gatewayArn",
        "location_arn": "locationArn",
        "role_arn": "roleArn",
        "access_based_enumeration": "accessBasedEnumeration",
        "admin_user_list": "adminUserList",
        "audit_destination_arn": "auditDestinationArn",
        "authentication": "authentication",
        "bucket_region": "bucketRegion",
        "cache_attributes": "cacheAttributes",
        "case_sensitivity": "caseSensitivity",
        "default_storage_class": "defaultStorageClass",
        "file_share_name": "fileShareName",
        "guess_mime_type_enabled": "guessMimeTypeEnabled",
        "id": "id",
        "invalid_user_list": "invalidUserList",
        "kms_encrypted": "kmsEncrypted",
        "kms_key_arn": "kmsKeyArn",
        "notification_policy": "notificationPolicy",
        "object_acl": "objectAcl",
        "oplocks_enabled": "oplocksEnabled",
        "read_only": "readOnly",
        "requester_pays": "requesterPays",
        "smb_acl_enabled": "smbAclEnabled",
        "tags": "tags",
        "tags_all": "tagsAll",
        "timeouts": "timeouts",
        "valid_user_list": "validUserList",
        "vpc_endpoint_dns_name": "vpcEndpointDnsName",
    },
)
class StoragegatewaySmbFileShareConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        gateway_arn: builtins.str,
        location_arn: builtins.str,
        role_arn: builtins.str,
        access_based_enumeration: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        admin_user_list: typing.Optional[typing.Sequence[builtins.str]] = None,
        audit_destination_arn: typing.Optional[builtins.str] = None,
        authentication: typing.Optional[builtins.str] = None,
        bucket_region: typing.Optional[builtins.str] = None,
        cache_attributes: typing.Optional[typing.Union[StoragegatewaySmbFileShareCacheAttributes, typing.Dict[builtins.str, typing.Any]]] = None,
        case_sensitivity: typing.Optional[builtins.str] = None,
        default_storage_class: typing.Optional[builtins.str] = None,
        file_share_name: typing.Optional[builtins.str] = None,
        guess_mime_type_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        invalid_user_list: typing.Optional[typing.Sequence[builtins.str]] = None,
        kms_encrypted: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
        notification_policy: typing.Optional[builtins.str] = None,
        object_acl: typing.Optional[builtins.str] = None,
        oplocks_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        requester_pays: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        smb_acl_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["StoragegatewaySmbFileShareTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        valid_user_list: typing.Optional[typing.Sequence[builtins.str]] = None,
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
        :param gateway_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#gateway_arn StoragegatewaySmbFileShare#gateway_arn}.
        :param location_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#location_arn StoragegatewaySmbFileShare#location_arn}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#role_arn StoragegatewaySmbFileShare#role_arn}.
        :param access_based_enumeration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#access_based_enumeration StoragegatewaySmbFileShare#access_based_enumeration}.
        :param admin_user_list: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#admin_user_list StoragegatewaySmbFileShare#admin_user_list}.
        :param audit_destination_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#audit_destination_arn StoragegatewaySmbFileShare#audit_destination_arn}.
        :param authentication: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#authentication StoragegatewaySmbFileShare#authentication}.
        :param bucket_region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#bucket_region StoragegatewaySmbFileShare#bucket_region}.
        :param cache_attributes: cache_attributes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#cache_attributes StoragegatewaySmbFileShare#cache_attributes}
        :param case_sensitivity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#case_sensitivity StoragegatewaySmbFileShare#case_sensitivity}.
        :param default_storage_class: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#default_storage_class StoragegatewaySmbFileShare#default_storage_class}.
        :param file_share_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#file_share_name StoragegatewaySmbFileShare#file_share_name}.
        :param guess_mime_type_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#guess_mime_type_enabled StoragegatewaySmbFileShare#guess_mime_type_enabled}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#id StoragegatewaySmbFileShare#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param invalid_user_list: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#invalid_user_list StoragegatewaySmbFileShare#invalid_user_list}.
        :param kms_encrypted: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#kms_encrypted StoragegatewaySmbFileShare#kms_encrypted}.
        :param kms_key_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#kms_key_arn StoragegatewaySmbFileShare#kms_key_arn}.
        :param notification_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#notification_policy StoragegatewaySmbFileShare#notification_policy}.
        :param object_acl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#object_acl StoragegatewaySmbFileShare#object_acl}.
        :param oplocks_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#oplocks_enabled StoragegatewaySmbFileShare#oplocks_enabled}.
        :param read_only: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#read_only StoragegatewaySmbFileShare#read_only}.
        :param requester_pays: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#requester_pays StoragegatewaySmbFileShare#requester_pays}.
        :param smb_acl_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#smb_acl_enabled StoragegatewaySmbFileShare#smb_acl_enabled}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#tags StoragegatewaySmbFileShare#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#tags_all StoragegatewaySmbFileShare#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#timeouts StoragegatewaySmbFileShare#timeouts}
        :param valid_user_list: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#valid_user_list StoragegatewaySmbFileShare#valid_user_list}.
        :param vpc_endpoint_dns_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#vpc_endpoint_dns_name StoragegatewaySmbFileShare#vpc_endpoint_dns_name}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(cache_attributes, dict):
            cache_attributes = StoragegatewaySmbFileShareCacheAttributes(**cache_attributes)
        if isinstance(timeouts, dict):
            timeouts = StoragegatewaySmbFileShareTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b58d64316a6f25d488a17cee8e5c6f62348ab14ccecbe7fa62c8cd890e9787a)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument gateway_arn", value=gateway_arn, expected_type=type_hints["gateway_arn"])
            check_type(argname="argument location_arn", value=location_arn, expected_type=type_hints["location_arn"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument access_based_enumeration", value=access_based_enumeration, expected_type=type_hints["access_based_enumeration"])
            check_type(argname="argument admin_user_list", value=admin_user_list, expected_type=type_hints["admin_user_list"])
            check_type(argname="argument audit_destination_arn", value=audit_destination_arn, expected_type=type_hints["audit_destination_arn"])
            check_type(argname="argument authentication", value=authentication, expected_type=type_hints["authentication"])
            check_type(argname="argument bucket_region", value=bucket_region, expected_type=type_hints["bucket_region"])
            check_type(argname="argument cache_attributes", value=cache_attributes, expected_type=type_hints["cache_attributes"])
            check_type(argname="argument case_sensitivity", value=case_sensitivity, expected_type=type_hints["case_sensitivity"])
            check_type(argname="argument default_storage_class", value=default_storage_class, expected_type=type_hints["default_storage_class"])
            check_type(argname="argument file_share_name", value=file_share_name, expected_type=type_hints["file_share_name"])
            check_type(argname="argument guess_mime_type_enabled", value=guess_mime_type_enabled, expected_type=type_hints["guess_mime_type_enabled"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument invalid_user_list", value=invalid_user_list, expected_type=type_hints["invalid_user_list"])
            check_type(argname="argument kms_encrypted", value=kms_encrypted, expected_type=type_hints["kms_encrypted"])
            check_type(argname="argument kms_key_arn", value=kms_key_arn, expected_type=type_hints["kms_key_arn"])
            check_type(argname="argument notification_policy", value=notification_policy, expected_type=type_hints["notification_policy"])
            check_type(argname="argument object_acl", value=object_acl, expected_type=type_hints["object_acl"])
            check_type(argname="argument oplocks_enabled", value=oplocks_enabled, expected_type=type_hints["oplocks_enabled"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
            check_type(argname="argument requester_pays", value=requester_pays, expected_type=type_hints["requester_pays"])
            check_type(argname="argument smb_acl_enabled", value=smb_acl_enabled, expected_type=type_hints["smb_acl_enabled"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument valid_user_list", value=valid_user_list, expected_type=type_hints["valid_user_list"])
            check_type(argname="argument vpc_endpoint_dns_name", value=vpc_endpoint_dns_name, expected_type=type_hints["vpc_endpoint_dns_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
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
        if access_based_enumeration is not None:
            self._values["access_based_enumeration"] = access_based_enumeration
        if admin_user_list is not None:
            self._values["admin_user_list"] = admin_user_list
        if audit_destination_arn is not None:
            self._values["audit_destination_arn"] = audit_destination_arn
        if authentication is not None:
            self._values["authentication"] = authentication
        if bucket_region is not None:
            self._values["bucket_region"] = bucket_region
        if cache_attributes is not None:
            self._values["cache_attributes"] = cache_attributes
        if case_sensitivity is not None:
            self._values["case_sensitivity"] = case_sensitivity
        if default_storage_class is not None:
            self._values["default_storage_class"] = default_storage_class
        if file_share_name is not None:
            self._values["file_share_name"] = file_share_name
        if guess_mime_type_enabled is not None:
            self._values["guess_mime_type_enabled"] = guess_mime_type_enabled
        if id is not None:
            self._values["id"] = id
        if invalid_user_list is not None:
            self._values["invalid_user_list"] = invalid_user_list
        if kms_encrypted is not None:
            self._values["kms_encrypted"] = kms_encrypted
        if kms_key_arn is not None:
            self._values["kms_key_arn"] = kms_key_arn
        if notification_policy is not None:
            self._values["notification_policy"] = notification_policy
        if object_acl is not None:
            self._values["object_acl"] = object_acl
        if oplocks_enabled is not None:
            self._values["oplocks_enabled"] = oplocks_enabled
        if read_only is not None:
            self._values["read_only"] = read_only
        if requester_pays is not None:
            self._values["requester_pays"] = requester_pays
        if smb_acl_enabled is not None:
            self._values["smb_acl_enabled"] = smb_acl_enabled
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if valid_user_list is not None:
            self._values["valid_user_list"] = valid_user_list
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
    def gateway_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#gateway_arn StoragegatewaySmbFileShare#gateway_arn}.'''
        result = self._values.get("gateway_arn")
        assert result is not None, "Required property 'gateway_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def location_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#location_arn StoragegatewaySmbFileShare#location_arn}.'''
        result = self._values.get("location_arn")
        assert result is not None, "Required property 'location_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#role_arn StoragegatewaySmbFileShare#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_based_enumeration(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#access_based_enumeration StoragegatewaySmbFileShare#access_based_enumeration}.'''
        result = self._values.get("access_based_enumeration")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def admin_user_list(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#admin_user_list StoragegatewaySmbFileShare#admin_user_list}.'''
        result = self._values.get("admin_user_list")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def audit_destination_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#audit_destination_arn StoragegatewaySmbFileShare#audit_destination_arn}.'''
        result = self._values.get("audit_destination_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def authentication(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#authentication StoragegatewaySmbFileShare#authentication}.'''
        result = self._values.get("authentication")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bucket_region(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#bucket_region StoragegatewaySmbFileShare#bucket_region}.'''
        result = self._values.get("bucket_region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cache_attributes(
        self,
    ) -> typing.Optional[StoragegatewaySmbFileShareCacheAttributes]:
        '''cache_attributes block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#cache_attributes StoragegatewaySmbFileShare#cache_attributes}
        '''
        result = self._values.get("cache_attributes")
        return typing.cast(typing.Optional[StoragegatewaySmbFileShareCacheAttributes], result)

    @builtins.property
    def case_sensitivity(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#case_sensitivity StoragegatewaySmbFileShare#case_sensitivity}.'''
        result = self._values.get("case_sensitivity")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_storage_class(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#default_storage_class StoragegatewaySmbFileShare#default_storage_class}.'''
        result = self._values.get("default_storage_class")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def file_share_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#file_share_name StoragegatewaySmbFileShare#file_share_name}.'''
        result = self._values.get("file_share_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def guess_mime_type_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#guess_mime_type_enabled StoragegatewaySmbFileShare#guess_mime_type_enabled}.'''
        result = self._values.get("guess_mime_type_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#id StoragegatewaySmbFileShare#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def invalid_user_list(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#invalid_user_list StoragegatewaySmbFileShare#invalid_user_list}.'''
        result = self._values.get("invalid_user_list")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def kms_encrypted(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#kms_encrypted StoragegatewaySmbFileShare#kms_encrypted}.'''
        result = self._values.get("kms_encrypted")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#kms_key_arn StoragegatewaySmbFileShare#kms_key_arn}.'''
        result = self._values.get("kms_key_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def notification_policy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#notification_policy StoragegatewaySmbFileShare#notification_policy}.'''
        result = self._values.get("notification_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def object_acl(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#object_acl StoragegatewaySmbFileShare#object_acl}.'''
        result = self._values.get("object_acl")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oplocks_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#oplocks_enabled StoragegatewaySmbFileShare#oplocks_enabled}.'''
        result = self._values.get("oplocks_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def read_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#read_only StoragegatewaySmbFileShare#read_only}.'''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def requester_pays(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#requester_pays StoragegatewaySmbFileShare#requester_pays}.'''
        result = self._values.get("requester_pays")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def smb_acl_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#smb_acl_enabled StoragegatewaySmbFileShare#smb_acl_enabled}.'''
        result = self._values.get("smb_acl_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#tags StoragegatewaySmbFileShare#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#tags_all StoragegatewaySmbFileShare#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["StoragegatewaySmbFileShareTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#timeouts StoragegatewaySmbFileShare#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["StoragegatewaySmbFileShareTimeouts"], result)

    @builtins.property
    def valid_user_list(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#valid_user_list StoragegatewaySmbFileShare#valid_user_list}.'''
        result = self._values.get("valid_user_list")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def vpc_endpoint_dns_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#vpc_endpoint_dns_name StoragegatewaySmbFileShare#vpc_endpoint_dns_name}.'''
        result = self._values.get("vpc_endpoint_dns_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StoragegatewaySmbFileShareConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.storagegatewaySmbFileShare.StoragegatewaySmbFileShareTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class StoragegatewaySmbFileShareTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#create StoragegatewaySmbFileShare#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#delete StoragegatewaySmbFileShare#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#update StoragegatewaySmbFileShare#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa84738dd9fd7eed85e3ec39cd425d2f4ede5ca91abfc074e41a3b3c8db249c1)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#create StoragegatewaySmbFileShare#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#delete StoragegatewaySmbFileShare#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share#update StoragegatewaySmbFileShare#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StoragegatewaySmbFileShareTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StoragegatewaySmbFileShareTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.storagegatewaySmbFileShare.StoragegatewaySmbFileShareTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__916297d80795c0d1fa9000231e4a843396699e0ef0945ad227b59893efd3cfd5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__dac76d27914c27a8561fb0325801860dd490ab78005a1b3230669a580dfd3975)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76c94afc027daf7e3076544e9f569b75f8b2dd0f554151923ef53af30c993f7f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52f20c15f124064ab165ba42d35949f01613ce19cc9bc1c1043fe5c7c92d4447)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[StoragegatewaySmbFileShareTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[StoragegatewaySmbFileShareTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[StoragegatewaySmbFileShareTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cfa508d6b96bc39bcfbca4cc40c090a78509f740a099bcfcc6b67bfd5ca2ca7c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "StoragegatewaySmbFileShare",
    "StoragegatewaySmbFileShareCacheAttributes",
    "StoragegatewaySmbFileShareCacheAttributesOutputReference",
    "StoragegatewaySmbFileShareConfig",
    "StoragegatewaySmbFileShareTimeouts",
    "StoragegatewaySmbFileShareTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__0b914268fdd5e94dc84507944ac32452e814470b8a7aeb6c3332dc595f12f026(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    gateway_arn: builtins.str,
    location_arn: builtins.str,
    role_arn: builtins.str,
    access_based_enumeration: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    admin_user_list: typing.Optional[typing.Sequence[builtins.str]] = None,
    audit_destination_arn: typing.Optional[builtins.str] = None,
    authentication: typing.Optional[builtins.str] = None,
    bucket_region: typing.Optional[builtins.str] = None,
    cache_attributes: typing.Optional[typing.Union[StoragegatewaySmbFileShareCacheAttributes, typing.Dict[builtins.str, typing.Any]]] = None,
    case_sensitivity: typing.Optional[builtins.str] = None,
    default_storage_class: typing.Optional[builtins.str] = None,
    file_share_name: typing.Optional[builtins.str] = None,
    guess_mime_type_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    invalid_user_list: typing.Optional[typing.Sequence[builtins.str]] = None,
    kms_encrypted: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    kms_key_arn: typing.Optional[builtins.str] = None,
    notification_policy: typing.Optional[builtins.str] = None,
    object_acl: typing.Optional[builtins.str] = None,
    oplocks_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    requester_pays: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    smb_acl_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[StoragegatewaySmbFileShareTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    valid_user_list: typing.Optional[typing.Sequence[builtins.str]] = None,
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

def _typecheckingstub__99ab31efdce589d75cfc3e7815f103ffc2675ac1f8f31bc2113f008891c6a618(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9cc6f2b32fdbdb6b7a18c66d20fe55cb9a13a6bae649158fd97093b0d30b840(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7edcbe8d937883ff3cde00503bee1063a7bb5d918d53ce46ccfee6a40e6b543d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__508c824fb409c01e097cbd36ee5e992b076c0757aa5487c9300084d9c24cf837(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6463dc05288aa59540f8e85d01b59af40f563e63fa81301bf5ddfbeac1908e63(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c6d18ce844e5f2e1f093f684aaba559c1134265627be2c46ede5fbdf54cc3c8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__837f01a36e660882bdb501ce6d5baceaa2f1ef0e573675d372ed9933046e1415(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56be707ecaf4e97f30feb4151466a88228677b17dd35b04f37f2cbee0a4a74d4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8fdf64bd1de10cb3cd5906cfb61fb931cf240b7d7bd69efbed9a643896d5e253(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ae9092b7c2b63c8dee1174abfd3bc2016202b68a839629a7f6834a39f4e8c6d(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32f35b5b9546a0931a09d787930b307a410001bc6a0a53be3219bf8206b00371(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80df646e4662adffdd9b6caec58cc744b8c9710141352da6a6c2ac52bb294528(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6699d3909f9b71ec7e8dd4b96942801c3fc647d0053b42a944df87a48e73a9ac(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ffb24caac3ea651a74361055c1446812933f323583cacd75e504f28ef95e245(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce3b1891226c1c783344b3da29040efc195a1738ec03c4cf197ed2e4df974bb5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94cde6984ea86c8e0edb2d74f7bb73a5689a1201e0b65493be4083f519729e9b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__785208f35955e7116fa782f817f8d6f652d303a89b8d3a777fa733a6a809ff96(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8fceebf25e2442995d4b9ccfaaad3bb331d684492b2465fb5b67db20492165c(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5dae2da4be16fd0dd5e5d77780075e7c82c0f1518e54579401ffe1dd54fc2cc(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68a79c5b1f02afb6db4c1de1ab985e3e03d4bae13a96332e785f4bc4be5166cc(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fcbd6e2606c33134b9cc92270744c3bdf6b4ab05b206001de487b5acf1e955fe(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__036ed8dfe7c31ff0d2aa65d5059cd8779afba83c985bb44760be32dcf0bc780d(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7745f864b1a33444dbc706e05c0e43c41918cdc395e99eaa33170134e20ce586(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed37f1665578747f84f686d70a72bbe29dfe5ac840dccc12e9b1502d3a0b96ec(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec4d7b2f83960c7ea730f5249f078e277173dc70a662b109267741d20ec79f5a(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6863aee0cbf3621d7a798fb338a2a1248203a5d8c9c0ef1adf6df42eb46ff9ce(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0f78321b5522bffa167bce81ebc644f8ec9d705ea5664720b8208f679a6eb1f(
    *,
    cache_stale_timeout_in_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad12b1e8a4021a9dc198b86441a0e33d3b311dd7bac5178d1a97296d141abf05(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9063be72ea781f14e0bf3280ec5f19bce701c27158293adf26415c9aa9a6ffe5(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__372cbd41f41ce2a7c79db37f41f8452b524ed2fe295cd8786ebba57eb4fefa84(
    value: typing.Optional[StoragegatewaySmbFileShareCacheAttributes],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b58d64316a6f25d488a17cee8e5c6f62348ab14ccecbe7fa62c8cd890e9787a(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    gateway_arn: builtins.str,
    location_arn: builtins.str,
    role_arn: builtins.str,
    access_based_enumeration: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    admin_user_list: typing.Optional[typing.Sequence[builtins.str]] = None,
    audit_destination_arn: typing.Optional[builtins.str] = None,
    authentication: typing.Optional[builtins.str] = None,
    bucket_region: typing.Optional[builtins.str] = None,
    cache_attributes: typing.Optional[typing.Union[StoragegatewaySmbFileShareCacheAttributes, typing.Dict[builtins.str, typing.Any]]] = None,
    case_sensitivity: typing.Optional[builtins.str] = None,
    default_storage_class: typing.Optional[builtins.str] = None,
    file_share_name: typing.Optional[builtins.str] = None,
    guess_mime_type_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    invalid_user_list: typing.Optional[typing.Sequence[builtins.str]] = None,
    kms_encrypted: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    kms_key_arn: typing.Optional[builtins.str] = None,
    notification_policy: typing.Optional[builtins.str] = None,
    object_acl: typing.Optional[builtins.str] = None,
    oplocks_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    requester_pays: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    smb_acl_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[StoragegatewaySmbFileShareTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    valid_user_list: typing.Optional[typing.Sequence[builtins.str]] = None,
    vpc_endpoint_dns_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa84738dd9fd7eed85e3ec39cd425d2f4ede5ca91abfc074e41a3b3c8db249c1(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__916297d80795c0d1fa9000231e4a843396699e0ef0945ad227b59893efd3cfd5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dac76d27914c27a8561fb0325801860dd490ab78005a1b3230669a580dfd3975(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76c94afc027daf7e3076544e9f569b75f8b2dd0f554151923ef53af30c993f7f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52f20c15f124064ab165ba42d35949f01613ce19cc9bc1c1043fe5c7c92d4447(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfa508d6b96bc39bcfbca4cc40c090a78509f740a099bcfcc6b67bfd5ca2ca7c(
    value: typing.Optional[typing.Union[StoragegatewaySmbFileShareTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
