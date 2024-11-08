'''
# `aws_s3_bucket`

Refer to the Terraform Registory for docs: [`aws_s3_bucket`](https://www.terraform.io/docs/providers/aws/r/s3_bucket).
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


class S3Bucket(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3Bucket.S3Bucket",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket aws_s3_bucket}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        acceleration_status: typing.Optional[builtins.str] = None,
        acl: typing.Optional[builtins.str] = None,
        bucket: typing.Optional[builtins.str] = None,
        bucket_prefix: typing.Optional[builtins.str] = None,
        cors_rule: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["S3BucketCorsRule", typing.Dict[builtins.str, typing.Any]]]]] = None,
        force_destroy: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        grant: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["S3BucketGrant", typing.Dict[builtins.str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        lifecycle_rule: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["S3BucketLifecycleRule", typing.Dict[builtins.str, typing.Any]]]]] = None,
        logging: typing.Optional[typing.Union["S3BucketLogging", typing.Dict[builtins.str, typing.Any]]] = None,
        object_lock_configuration: typing.Optional[typing.Union["S3BucketObjectLockConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        object_lock_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        policy: typing.Optional[builtins.str] = None,
        replication_configuration: typing.Optional[typing.Union["S3BucketReplicationConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        request_payer: typing.Optional[builtins.str] = None,
        server_side_encryption_configuration: typing.Optional[typing.Union["S3BucketServerSideEncryptionConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["S3BucketTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        versioning: typing.Optional[typing.Union["S3BucketVersioning", typing.Dict[builtins.str, typing.Any]]] = None,
        website: typing.Optional[typing.Union["S3BucketWebsite", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket aws_s3_bucket} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param acceleration_status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#acceleration_status S3Bucket#acceleration_status}.
        :param acl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#acl S3Bucket#acl}.
        :param bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#bucket S3Bucket#bucket}.
        :param bucket_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#bucket_prefix S3Bucket#bucket_prefix}.
        :param cors_rule: cors_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#cors_rule S3Bucket#cors_rule}
        :param force_destroy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#force_destroy S3Bucket#force_destroy}.
        :param grant: grant block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#grant S3Bucket#grant}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#id S3Bucket#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param lifecycle_rule: lifecycle_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#lifecycle_rule S3Bucket#lifecycle_rule}
        :param logging: logging block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#logging S3Bucket#logging}
        :param object_lock_configuration: object_lock_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#object_lock_configuration S3Bucket#object_lock_configuration}
        :param object_lock_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#object_lock_enabled S3Bucket#object_lock_enabled}.
        :param policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#policy S3Bucket#policy}.
        :param replication_configuration: replication_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#replication_configuration S3Bucket#replication_configuration}
        :param request_payer: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#request_payer S3Bucket#request_payer}.
        :param server_side_encryption_configuration: server_side_encryption_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#server_side_encryption_configuration S3Bucket#server_side_encryption_configuration}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#tags S3Bucket#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#tags_all S3Bucket#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#timeouts S3Bucket#timeouts}
        :param versioning: versioning block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#versioning S3Bucket#versioning}
        :param website: website block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#website S3Bucket#website}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc0af23835865888eaefeebdd062e1335ba688f838efccfdd34a608659a14ec9)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = S3BucketConfig(
            acceleration_status=acceleration_status,
            acl=acl,
            bucket=bucket,
            bucket_prefix=bucket_prefix,
            cors_rule=cors_rule,
            force_destroy=force_destroy,
            grant=grant,
            id=id,
            lifecycle_rule=lifecycle_rule,
            logging=logging,
            object_lock_configuration=object_lock_configuration,
            object_lock_enabled=object_lock_enabled,
            policy=policy,
            replication_configuration=replication_configuration,
            request_payer=request_payer,
            server_side_encryption_configuration=server_side_encryption_configuration,
            tags=tags,
            tags_all=tags_all,
            timeouts=timeouts,
            versioning=versioning,
            website=website,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putCorsRule")
    def put_cors_rule(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["S3BucketCorsRule", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59443412b46cddd9bd999cb306f49c70c9d537e146e77fc542a4688198d32c81)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCorsRule", [value]))

    @jsii.member(jsii_name="putGrant")
    def put_grant(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["S3BucketGrant", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03b333ee3a4a814a21d385853c0daf4f286c73256fe5b38f1fb30fdae05102fd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putGrant", [value]))

    @jsii.member(jsii_name="putLifecycleRule")
    def put_lifecycle_rule(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["S3BucketLifecycleRule", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__138933bc9001d3dbffb393f7c2347e6a6f318eb448906738d9074b977a63b5fc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLifecycleRule", [value]))

    @jsii.member(jsii_name="putLogging")
    def put_logging(
        self,
        *,
        target_bucket: builtins.str,
        target_prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param target_bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#target_bucket S3Bucket#target_bucket}.
        :param target_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#target_prefix S3Bucket#target_prefix}.
        '''
        value = S3BucketLogging(
            target_bucket=target_bucket, target_prefix=target_prefix
        )

        return typing.cast(None, jsii.invoke(self, "putLogging", [value]))

    @jsii.member(jsii_name="putObjectLockConfiguration")
    def put_object_lock_configuration(
        self,
        *,
        object_lock_enabled: typing.Optional[builtins.str] = None,
        rule: typing.Optional[typing.Union["S3BucketObjectLockConfigurationRule", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param object_lock_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#object_lock_enabled S3Bucket#object_lock_enabled}.
        :param rule: rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#rule S3Bucket#rule}
        '''
        value = S3BucketObjectLockConfiguration(
            object_lock_enabled=object_lock_enabled, rule=rule
        )

        return typing.cast(None, jsii.invoke(self, "putObjectLockConfiguration", [value]))

    @jsii.member(jsii_name="putReplicationConfiguration")
    def put_replication_configuration(
        self,
        *,
        role: builtins.str,
        rules: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["S3BucketReplicationConfigurationRules", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#role S3Bucket#role}.
        :param rules: rules block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#rules S3Bucket#rules}
        '''
        value = S3BucketReplicationConfiguration(role=role, rules=rules)

        return typing.cast(None, jsii.invoke(self, "putReplicationConfiguration", [value]))

    @jsii.member(jsii_name="putServerSideEncryptionConfiguration")
    def put_server_side_encryption_configuration(
        self,
        *,
        rule: typing.Union["S3BucketServerSideEncryptionConfigurationRule", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param rule: rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#rule S3Bucket#rule}
        '''
        value = S3BucketServerSideEncryptionConfiguration(rule=rule)

        return typing.cast(None, jsii.invoke(self, "putServerSideEncryptionConfiguration", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#create S3Bucket#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#delete S3Bucket#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#read S3Bucket#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#update S3Bucket#update}.
        '''
        value = S3BucketTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putVersioning")
    def put_versioning(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        mfa_delete: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#enabled S3Bucket#enabled}.
        :param mfa_delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#mfa_delete S3Bucket#mfa_delete}.
        '''
        value = S3BucketVersioning(enabled=enabled, mfa_delete=mfa_delete)

        return typing.cast(None, jsii.invoke(self, "putVersioning", [value]))

    @jsii.member(jsii_name="putWebsite")
    def put_website(
        self,
        *,
        error_document: typing.Optional[builtins.str] = None,
        index_document: typing.Optional[builtins.str] = None,
        redirect_all_requests_to: typing.Optional[builtins.str] = None,
        routing_rules: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param error_document: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#error_document S3Bucket#error_document}.
        :param index_document: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#index_document S3Bucket#index_document}.
        :param redirect_all_requests_to: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#redirect_all_requests_to S3Bucket#redirect_all_requests_to}.
        :param routing_rules: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#routing_rules S3Bucket#routing_rules}.
        '''
        value = S3BucketWebsite(
            error_document=error_document,
            index_document=index_document,
            redirect_all_requests_to=redirect_all_requests_to,
            routing_rules=routing_rules,
        )

        return typing.cast(None, jsii.invoke(self, "putWebsite", [value]))

    @jsii.member(jsii_name="resetAccelerationStatus")
    def reset_acceleration_status(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccelerationStatus", []))

    @jsii.member(jsii_name="resetAcl")
    def reset_acl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAcl", []))

    @jsii.member(jsii_name="resetBucket")
    def reset_bucket(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucket", []))

    @jsii.member(jsii_name="resetBucketPrefix")
    def reset_bucket_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketPrefix", []))

    @jsii.member(jsii_name="resetCorsRule")
    def reset_cors_rule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCorsRule", []))

    @jsii.member(jsii_name="resetForceDestroy")
    def reset_force_destroy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForceDestroy", []))

    @jsii.member(jsii_name="resetGrant")
    def reset_grant(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGrant", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLifecycleRule")
    def reset_lifecycle_rule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLifecycleRule", []))

    @jsii.member(jsii_name="resetLogging")
    def reset_logging(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogging", []))

    @jsii.member(jsii_name="resetObjectLockConfiguration")
    def reset_object_lock_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetObjectLockConfiguration", []))

    @jsii.member(jsii_name="resetObjectLockEnabled")
    def reset_object_lock_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetObjectLockEnabled", []))

    @jsii.member(jsii_name="resetPolicy")
    def reset_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPolicy", []))

    @jsii.member(jsii_name="resetReplicationConfiguration")
    def reset_replication_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReplicationConfiguration", []))

    @jsii.member(jsii_name="resetRequestPayer")
    def reset_request_payer(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestPayer", []))

    @jsii.member(jsii_name="resetServerSideEncryptionConfiguration")
    def reset_server_side_encryption_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServerSideEncryptionConfiguration", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetVersioning")
    def reset_versioning(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVersioning", []))

    @jsii.member(jsii_name="resetWebsite")
    def reset_website(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWebsite", []))

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
    @jsii.member(jsii_name="bucketDomainName")
    def bucket_domain_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketDomainName"))

    @builtins.property
    @jsii.member(jsii_name="bucketRegionalDomainName")
    def bucket_regional_domain_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketRegionalDomainName"))

    @builtins.property
    @jsii.member(jsii_name="corsRule")
    def cors_rule(self) -> "S3BucketCorsRuleList":
        return typing.cast("S3BucketCorsRuleList", jsii.get(self, "corsRule"))

    @builtins.property
    @jsii.member(jsii_name="grant")
    def grant(self) -> "S3BucketGrantList":
        return typing.cast("S3BucketGrantList", jsii.get(self, "grant"))

    @builtins.property
    @jsii.member(jsii_name="hostedZoneId")
    def hosted_zone_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostedZoneId"))

    @builtins.property
    @jsii.member(jsii_name="lifecycleRule")
    def lifecycle_rule(self) -> "S3BucketLifecycleRuleList":
        return typing.cast("S3BucketLifecycleRuleList", jsii.get(self, "lifecycleRule"))

    @builtins.property
    @jsii.member(jsii_name="logging")
    def logging(self) -> "S3BucketLoggingOutputReference":
        return typing.cast("S3BucketLoggingOutputReference", jsii.get(self, "logging"))

    @builtins.property
    @jsii.member(jsii_name="objectLockConfiguration")
    def object_lock_configuration(
        self,
    ) -> "S3BucketObjectLockConfigurationOutputReference":
        return typing.cast("S3BucketObjectLockConfigurationOutputReference", jsii.get(self, "objectLockConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @builtins.property
    @jsii.member(jsii_name="replicationConfiguration")
    def replication_configuration(
        self,
    ) -> "S3BucketReplicationConfigurationOutputReference":
        return typing.cast("S3BucketReplicationConfigurationOutputReference", jsii.get(self, "replicationConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="serverSideEncryptionConfiguration")
    def server_side_encryption_configuration(
        self,
    ) -> "S3BucketServerSideEncryptionConfigurationOutputReference":
        return typing.cast("S3BucketServerSideEncryptionConfigurationOutputReference", jsii.get(self, "serverSideEncryptionConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "S3BucketTimeoutsOutputReference":
        return typing.cast("S3BucketTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="versioning")
    def versioning(self) -> "S3BucketVersioningOutputReference":
        return typing.cast("S3BucketVersioningOutputReference", jsii.get(self, "versioning"))

    @builtins.property
    @jsii.member(jsii_name="website")
    def website(self) -> "S3BucketWebsiteOutputReference":
        return typing.cast("S3BucketWebsiteOutputReference", jsii.get(self, "website"))

    @builtins.property
    @jsii.member(jsii_name="websiteDomain")
    def website_domain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "websiteDomain"))

    @builtins.property
    @jsii.member(jsii_name="websiteEndpoint")
    def website_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "websiteEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="accelerationStatusInput")
    def acceleration_status_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accelerationStatusInput"))

    @builtins.property
    @jsii.member(jsii_name="aclInput")
    def acl_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aclInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketInput")
    def bucket_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketPrefixInput")
    def bucket_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="corsRuleInput")
    def cors_rule_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["S3BucketCorsRule"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["S3BucketCorsRule"]]], jsii.get(self, "corsRuleInput"))

    @builtins.property
    @jsii.member(jsii_name="forceDestroyInput")
    def force_destroy_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "forceDestroyInput"))

    @builtins.property
    @jsii.member(jsii_name="grantInput")
    def grant_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["S3BucketGrant"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["S3BucketGrant"]]], jsii.get(self, "grantInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="lifecycleRuleInput")
    def lifecycle_rule_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["S3BucketLifecycleRule"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["S3BucketLifecycleRule"]]], jsii.get(self, "lifecycleRuleInput"))

    @builtins.property
    @jsii.member(jsii_name="loggingInput")
    def logging_input(self) -> typing.Optional["S3BucketLogging"]:
        return typing.cast(typing.Optional["S3BucketLogging"], jsii.get(self, "loggingInput"))

    @builtins.property
    @jsii.member(jsii_name="objectLockConfigurationInput")
    def object_lock_configuration_input(
        self,
    ) -> typing.Optional["S3BucketObjectLockConfiguration"]:
        return typing.cast(typing.Optional["S3BucketObjectLockConfiguration"], jsii.get(self, "objectLockConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="objectLockEnabledInput")
    def object_lock_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "objectLockEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="policyInput")
    def policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "policyInput"))

    @builtins.property
    @jsii.member(jsii_name="replicationConfigurationInput")
    def replication_configuration_input(
        self,
    ) -> typing.Optional["S3BucketReplicationConfiguration"]:
        return typing.cast(typing.Optional["S3BucketReplicationConfiguration"], jsii.get(self, "replicationConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="requestPayerInput")
    def request_payer_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "requestPayerInput"))

    @builtins.property
    @jsii.member(jsii_name="serverSideEncryptionConfigurationInput")
    def server_side_encryption_configuration_input(
        self,
    ) -> typing.Optional["S3BucketServerSideEncryptionConfiguration"]:
        return typing.cast(typing.Optional["S3BucketServerSideEncryptionConfiguration"], jsii.get(self, "serverSideEncryptionConfigurationInput"))

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
    ) -> typing.Optional[typing.Union["S3BucketTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["S3BucketTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="versioningInput")
    def versioning_input(self) -> typing.Optional["S3BucketVersioning"]:
        return typing.cast(typing.Optional["S3BucketVersioning"], jsii.get(self, "versioningInput"))

    @builtins.property
    @jsii.member(jsii_name="websiteInput")
    def website_input(self) -> typing.Optional["S3BucketWebsite"]:
        return typing.cast(typing.Optional["S3BucketWebsite"], jsii.get(self, "websiteInput"))

    @builtins.property
    @jsii.member(jsii_name="accelerationStatus")
    def acceleration_status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accelerationStatus"))

    @acceleration_status.setter
    def acceleration_status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f86a908b5f61fe5301087c112b13197c61196eb277daa05f08e36f71d59302cd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accelerationStatus", value)

    @builtins.property
    @jsii.member(jsii_name="acl")
    def acl(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "acl"))

    @acl.setter
    def acl(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b691ae88fc3a0bb0a428a626b4db60a42dae0659012eb63437c56a5cda4a068)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "acl", value)

    @builtins.property
    @jsii.member(jsii_name="bucket")
    def bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucket"))

    @bucket.setter
    def bucket(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b0d11b5164a927bb74ba02d20713ac625d52ed68c45cd952fda2ef685d447df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucket", value)

    @builtins.property
    @jsii.member(jsii_name="bucketPrefix")
    def bucket_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketPrefix"))

    @bucket_prefix.setter
    def bucket_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25578cbcb50906c03d22724e79c3b3186414afcacd67b466712b43f31219c669)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="forceDestroy")
    def force_destroy(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "forceDestroy"))

    @force_destroy.setter
    def force_destroy(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aab6eaa55e34658d41fe358da5a5a08dcd824d710cc070026db4eee1fcfb031c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forceDestroy", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e7c0822a5575ff0ac4663d817d5ba38c6d393db9319903934cdc7e20fe3a543)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="objectLockEnabled")
    def object_lock_enabled(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "objectLockEnabled"))

    @object_lock_enabled.setter
    def object_lock_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__775edd63cae681a2a9676704cf8232486f5b8138a66dab3489d2b362bb4e049d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "objectLockEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="policy")
    def policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "policy"))

    @policy.setter
    def policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f1366cee0f6ed05e02969a3c0e9f65bd8912a903b50796e3b35647335605e5d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policy", value)

    @builtins.property
    @jsii.member(jsii_name="requestPayer")
    def request_payer(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "requestPayer"))

    @request_payer.setter
    def request_payer(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b29097cff1db62f8df0881ac9606872f9a58a722f11c426b05c7a053b6fba80e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requestPayer", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6e153b999a7955b6088f7ca7ed267d7ba0c564871eb3abdc281a377da339c25)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d172309882755cf123d3483b899c4753e852bd277e2707cad93efc335d9c69c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)


@jsii.data_type(
    jsii_type="aws.s3Bucket.S3BucketConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "acceleration_status": "accelerationStatus",
        "acl": "acl",
        "bucket": "bucket",
        "bucket_prefix": "bucketPrefix",
        "cors_rule": "corsRule",
        "force_destroy": "forceDestroy",
        "grant": "grant",
        "id": "id",
        "lifecycle_rule": "lifecycleRule",
        "logging": "logging",
        "object_lock_configuration": "objectLockConfiguration",
        "object_lock_enabled": "objectLockEnabled",
        "policy": "policy",
        "replication_configuration": "replicationConfiguration",
        "request_payer": "requestPayer",
        "server_side_encryption_configuration": "serverSideEncryptionConfiguration",
        "tags": "tags",
        "tags_all": "tagsAll",
        "timeouts": "timeouts",
        "versioning": "versioning",
        "website": "website",
    },
)
class S3BucketConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        acceleration_status: typing.Optional[builtins.str] = None,
        acl: typing.Optional[builtins.str] = None,
        bucket: typing.Optional[builtins.str] = None,
        bucket_prefix: typing.Optional[builtins.str] = None,
        cors_rule: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["S3BucketCorsRule", typing.Dict[builtins.str, typing.Any]]]]] = None,
        force_destroy: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        grant: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["S3BucketGrant", typing.Dict[builtins.str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        lifecycle_rule: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["S3BucketLifecycleRule", typing.Dict[builtins.str, typing.Any]]]]] = None,
        logging: typing.Optional[typing.Union["S3BucketLogging", typing.Dict[builtins.str, typing.Any]]] = None,
        object_lock_configuration: typing.Optional[typing.Union["S3BucketObjectLockConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        object_lock_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        policy: typing.Optional[builtins.str] = None,
        replication_configuration: typing.Optional[typing.Union["S3BucketReplicationConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        request_payer: typing.Optional[builtins.str] = None,
        server_side_encryption_configuration: typing.Optional[typing.Union["S3BucketServerSideEncryptionConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["S3BucketTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        versioning: typing.Optional[typing.Union["S3BucketVersioning", typing.Dict[builtins.str, typing.Any]]] = None,
        website: typing.Optional[typing.Union["S3BucketWebsite", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param acceleration_status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#acceleration_status S3Bucket#acceleration_status}.
        :param acl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#acl S3Bucket#acl}.
        :param bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#bucket S3Bucket#bucket}.
        :param bucket_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#bucket_prefix S3Bucket#bucket_prefix}.
        :param cors_rule: cors_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#cors_rule S3Bucket#cors_rule}
        :param force_destroy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#force_destroy S3Bucket#force_destroy}.
        :param grant: grant block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#grant S3Bucket#grant}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#id S3Bucket#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param lifecycle_rule: lifecycle_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#lifecycle_rule S3Bucket#lifecycle_rule}
        :param logging: logging block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#logging S3Bucket#logging}
        :param object_lock_configuration: object_lock_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#object_lock_configuration S3Bucket#object_lock_configuration}
        :param object_lock_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#object_lock_enabled S3Bucket#object_lock_enabled}.
        :param policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#policy S3Bucket#policy}.
        :param replication_configuration: replication_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#replication_configuration S3Bucket#replication_configuration}
        :param request_payer: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#request_payer S3Bucket#request_payer}.
        :param server_side_encryption_configuration: server_side_encryption_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#server_side_encryption_configuration S3Bucket#server_side_encryption_configuration}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#tags S3Bucket#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#tags_all S3Bucket#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#timeouts S3Bucket#timeouts}
        :param versioning: versioning block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#versioning S3Bucket#versioning}
        :param website: website block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#website S3Bucket#website}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(logging, dict):
            logging = S3BucketLogging(**logging)
        if isinstance(object_lock_configuration, dict):
            object_lock_configuration = S3BucketObjectLockConfiguration(**object_lock_configuration)
        if isinstance(replication_configuration, dict):
            replication_configuration = S3BucketReplicationConfiguration(**replication_configuration)
        if isinstance(server_side_encryption_configuration, dict):
            server_side_encryption_configuration = S3BucketServerSideEncryptionConfiguration(**server_side_encryption_configuration)
        if isinstance(timeouts, dict):
            timeouts = S3BucketTimeouts(**timeouts)
        if isinstance(versioning, dict):
            versioning = S3BucketVersioning(**versioning)
        if isinstance(website, dict):
            website = S3BucketWebsite(**website)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__777baa4fbb89830b9838d20921e83f4e931ff672e541c19eb83e636a56c39844)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument acceleration_status", value=acceleration_status, expected_type=type_hints["acceleration_status"])
            check_type(argname="argument acl", value=acl, expected_type=type_hints["acl"])
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument bucket_prefix", value=bucket_prefix, expected_type=type_hints["bucket_prefix"])
            check_type(argname="argument cors_rule", value=cors_rule, expected_type=type_hints["cors_rule"])
            check_type(argname="argument force_destroy", value=force_destroy, expected_type=type_hints["force_destroy"])
            check_type(argname="argument grant", value=grant, expected_type=type_hints["grant"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument lifecycle_rule", value=lifecycle_rule, expected_type=type_hints["lifecycle_rule"])
            check_type(argname="argument logging", value=logging, expected_type=type_hints["logging"])
            check_type(argname="argument object_lock_configuration", value=object_lock_configuration, expected_type=type_hints["object_lock_configuration"])
            check_type(argname="argument object_lock_enabled", value=object_lock_enabled, expected_type=type_hints["object_lock_enabled"])
            check_type(argname="argument policy", value=policy, expected_type=type_hints["policy"])
            check_type(argname="argument replication_configuration", value=replication_configuration, expected_type=type_hints["replication_configuration"])
            check_type(argname="argument request_payer", value=request_payer, expected_type=type_hints["request_payer"])
            check_type(argname="argument server_side_encryption_configuration", value=server_side_encryption_configuration, expected_type=type_hints["server_side_encryption_configuration"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument versioning", value=versioning, expected_type=type_hints["versioning"])
            check_type(argname="argument website", value=website, expected_type=type_hints["website"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
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
        if acceleration_status is not None:
            self._values["acceleration_status"] = acceleration_status
        if acl is not None:
            self._values["acl"] = acl
        if bucket is not None:
            self._values["bucket"] = bucket
        if bucket_prefix is not None:
            self._values["bucket_prefix"] = bucket_prefix
        if cors_rule is not None:
            self._values["cors_rule"] = cors_rule
        if force_destroy is not None:
            self._values["force_destroy"] = force_destroy
        if grant is not None:
            self._values["grant"] = grant
        if id is not None:
            self._values["id"] = id
        if lifecycle_rule is not None:
            self._values["lifecycle_rule"] = lifecycle_rule
        if logging is not None:
            self._values["logging"] = logging
        if object_lock_configuration is not None:
            self._values["object_lock_configuration"] = object_lock_configuration
        if object_lock_enabled is not None:
            self._values["object_lock_enabled"] = object_lock_enabled
        if policy is not None:
            self._values["policy"] = policy
        if replication_configuration is not None:
            self._values["replication_configuration"] = replication_configuration
        if request_payer is not None:
            self._values["request_payer"] = request_payer
        if server_side_encryption_configuration is not None:
            self._values["server_side_encryption_configuration"] = server_side_encryption_configuration
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if versioning is not None:
            self._values["versioning"] = versioning
        if website is not None:
            self._values["website"] = website

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
    def acceleration_status(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#acceleration_status S3Bucket#acceleration_status}.'''
        result = self._values.get("acceleration_status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def acl(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#acl S3Bucket#acl}.'''
        result = self._values.get("acl")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bucket(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#bucket S3Bucket#bucket}.'''
        result = self._values.get("bucket")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bucket_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#bucket_prefix S3Bucket#bucket_prefix}.'''
        result = self._values.get("bucket_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cors_rule(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["S3BucketCorsRule"]]]:
        '''cors_rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#cors_rule S3Bucket#cors_rule}
        '''
        result = self._values.get("cors_rule")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["S3BucketCorsRule"]]], result)

    @builtins.property
    def force_destroy(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#force_destroy S3Bucket#force_destroy}.'''
        result = self._values.get("force_destroy")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def grant(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["S3BucketGrant"]]]:
        '''grant block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#grant S3Bucket#grant}
        '''
        result = self._values.get("grant")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["S3BucketGrant"]]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#id S3Bucket#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lifecycle_rule(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["S3BucketLifecycleRule"]]]:
        '''lifecycle_rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#lifecycle_rule S3Bucket#lifecycle_rule}
        '''
        result = self._values.get("lifecycle_rule")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["S3BucketLifecycleRule"]]], result)

    @builtins.property
    def logging(self) -> typing.Optional["S3BucketLogging"]:
        '''logging block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#logging S3Bucket#logging}
        '''
        result = self._values.get("logging")
        return typing.cast(typing.Optional["S3BucketLogging"], result)

    @builtins.property
    def object_lock_configuration(
        self,
    ) -> typing.Optional["S3BucketObjectLockConfiguration"]:
        '''object_lock_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#object_lock_configuration S3Bucket#object_lock_configuration}
        '''
        result = self._values.get("object_lock_configuration")
        return typing.cast(typing.Optional["S3BucketObjectLockConfiguration"], result)

    @builtins.property
    def object_lock_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#object_lock_enabled S3Bucket#object_lock_enabled}.'''
        result = self._values.get("object_lock_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def policy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#policy S3Bucket#policy}.'''
        result = self._values.get("policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def replication_configuration(
        self,
    ) -> typing.Optional["S3BucketReplicationConfiguration"]:
        '''replication_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#replication_configuration S3Bucket#replication_configuration}
        '''
        result = self._values.get("replication_configuration")
        return typing.cast(typing.Optional["S3BucketReplicationConfiguration"], result)

    @builtins.property
    def request_payer(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#request_payer S3Bucket#request_payer}.'''
        result = self._values.get("request_payer")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def server_side_encryption_configuration(
        self,
    ) -> typing.Optional["S3BucketServerSideEncryptionConfiguration"]:
        '''server_side_encryption_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#server_side_encryption_configuration S3Bucket#server_side_encryption_configuration}
        '''
        result = self._values.get("server_side_encryption_configuration")
        return typing.cast(typing.Optional["S3BucketServerSideEncryptionConfiguration"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#tags S3Bucket#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#tags_all S3Bucket#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["S3BucketTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#timeouts S3Bucket#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["S3BucketTimeouts"], result)

    @builtins.property
    def versioning(self) -> typing.Optional["S3BucketVersioning"]:
        '''versioning block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#versioning S3Bucket#versioning}
        '''
        result = self._values.get("versioning")
        return typing.cast(typing.Optional["S3BucketVersioning"], result)

    @builtins.property
    def website(self) -> typing.Optional["S3BucketWebsite"]:
        '''website block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#website S3Bucket#website}
        '''
        result = self._values.get("website")
        return typing.cast(typing.Optional["S3BucketWebsite"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.s3Bucket.S3BucketCorsRule",
    jsii_struct_bases=[],
    name_mapping={
        "allowed_methods": "allowedMethods",
        "allowed_origins": "allowedOrigins",
        "allowed_headers": "allowedHeaders",
        "expose_headers": "exposeHeaders",
        "max_age_seconds": "maxAgeSeconds",
    },
)
class S3BucketCorsRule:
    def __init__(
        self,
        *,
        allowed_methods: typing.Sequence[builtins.str],
        allowed_origins: typing.Sequence[builtins.str],
        allowed_headers: typing.Optional[typing.Sequence[builtins.str]] = None,
        expose_headers: typing.Optional[typing.Sequence[builtins.str]] = None,
        max_age_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param allowed_methods: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#allowed_methods S3Bucket#allowed_methods}.
        :param allowed_origins: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#allowed_origins S3Bucket#allowed_origins}.
        :param allowed_headers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#allowed_headers S3Bucket#allowed_headers}.
        :param expose_headers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#expose_headers S3Bucket#expose_headers}.
        :param max_age_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#max_age_seconds S3Bucket#max_age_seconds}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d82c291e063cbf62727aa6a7b283bb6811e149559594b1a705f784a5736189e1)
            check_type(argname="argument allowed_methods", value=allowed_methods, expected_type=type_hints["allowed_methods"])
            check_type(argname="argument allowed_origins", value=allowed_origins, expected_type=type_hints["allowed_origins"])
            check_type(argname="argument allowed_headers", value=allowed_headers, expected_type=type_hints["allowed_headers"])
            check_type(argname="argument expose_headers", value=expose_headers, expected_type=type_hints["expose_headers"])
            check_type(argname="argument max_age_seconds", value=max_age_seconds, expected_type=type_hints["max_age_seconds"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "allowed_methods": allowed_methods,
            "allowed_origins": allowed_origins,
        }
        if allowed_headers is not None:
            self._values["allowed_headers"] = allowed_headers
        if expose_headers is not None:
            self._values["expose_headers"] = expose_headers
        if max_age_seconds is not None:
            self._values["max_age_seconds"] = max_age_seconds

    @builtins.property
    def allowed_methods(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#allowed_methods S3Bucket#allowed_methods}.'''
        result = self._values.get("allowed_methods")
        assert result is not None, "Required property 'allowed_methods' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def allowed_origins(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#allowed_origins S3Bucket#allowed_origins}.'''
        result = self._values.get("allowed_origins")
        assert result is not None, "Required property 'allowed_origins' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def allowed_headers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#allowed_headers S3Bucket#allowed_headers}.'''
        result = self._values.get("allowed_headers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def expose_headers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#expose_headers S3Bucket#expose_headers}.'''
        result = self._values.get("expose_headers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def max_age_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#max_age_seconds S3Bucket#max_age_seconds}.'''
        result = self._values.get("max_age_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketCorsRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3BucketCorsRuleList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3Bucket.S3BucketCorsRuleList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a206e3e3ca6b5dd73b3170530501c538382a60e7cfb52982511f6c3fc16968ca)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "S3BucketCorsRuleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd82e1e6cb2e09b63680a9bcecae239e308f42543e7afceefab994572d2f8475)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("S3BucketCorsRuleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9dcb9ba3711889ed8e6c395d0b0feca8079aea7d91809fd3720182d9453b1ac9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__234559482a15427c82f0f2646b9847e8bd3bbc7e10813600cde0dabe21246cc4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9ed4abd7680f598a86f6a3ce83d39a5145190bbe755d6cbf1fb61153ca0614a6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[S3BucketCorsRule]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[S3BucketCorsRule]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[S3BucketCorsRule]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5af0657b9022fbd2ac06d532c2b2c73ea48c499a2c55db9f79b9817a85f3f3ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class S3BucketCorsRuleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3Bucket.S3BucketCorsRuleOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0c8415b7dd36ab18e2f0ac039d72561a64d0eeb75ad99a48275038ae8a4d059d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAllowedHeaders")
    def reset_allowed_headers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedHeaders", []))

    @jsii.member(jsii_name="resetExposeHeaders")
    def reset_expose_headers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExposeHeaders", []))

    @jsii.member(jsii_name="resetMaxAgeSeconds")
    def reset_max_age_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxAgeSeconds", []))

    @builtins.property
    @jsii.member(jsii_name="allowedHeadersInput")
    def allowed_headers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedHeadersInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedMethodsInput")
    def allowed_methods_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedMethodsInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedOriginsInput")
    def allowed_origins_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedOriginsInput"))

    @builtins.property
    @jsii.member(jsii_name="exposeHeadersInput")
    def expose_headers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "exposeHeadersInput"))

    @builtins.property
    @jsii.member(jsii_name="maxAgeSecondsInput")
    def max_age_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxAgeSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedHeaders")
    def allowed_headers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedHeaders"))

    @allowed_headers.setter
    def allowed_headers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29baa73cc30a148e24705fc274762c557e170e8f29654e3433c6916e1d02d8fb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedHeaders", value)

    @builtins.property
    @jsii.member(jsii_name="allowedMethods")
    def allowed_methods(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedMethods"))

    @allowed_methods.setter
    def allowed_methods(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79da6f462f3447f0724a89761e02478f84d10c949cc763cac8fa4a2e4addcea9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedMethods", value)

    @builtins.property
    @jsii.member(jsii_name="allowedOrigins")
    def allowed_origins(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedOrigins"))

    @allowed_origins.setter
    def allowed_origins(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5978601fb006d93cf8372978c03a89a27453a23efc8f88073f04f1d435e01018)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedOrigins", value)

    @builtins.property
    @jsii.member(jsii_name="exposeHeaders")
    def expose_headers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "exposeHeaders"))

    @expose_headers.setter
    def expose_headers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67604d72454c9c629847eddaa50c71a120f2a3162cc578d4774ce20931f15ccd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exposeHeaders", value)

    @builtins.property
    @jsii.member(jsii_name="maxAgeSeconds")
    def max_age_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxAgeSeconds"))

    @max_age_seconds.setter
    def max_age_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__107214a50019ba8892f8a0665e0d8ccc5fa8637f08beb852c1827522bf4021f6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxAgeSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[S3BucketCorsRule, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[S3BucketCorsRule, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[S3BucketCorsRule, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ab4cf6d7306befe88716f5ae060dabf118f73e1ee6105ab239bb46f79c54ed6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.s3Bucket.S3BucketGrant",
    jsii_struct_bases=[],
    name_mapping={
        "permissions": "permissions",
        "type": "type",
        "id": "id",
        "uri": "uri",
    },
)
class S3BucketGrant:
    def __init__(
        self,
        *,
        permissions: typing.Sequence[builtins.str],
        type: builtins.str,
        id: typing.Optional[builtins.str] = None,
        uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param permissions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#permissions S3Bucket#permissions}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#type S3Bucket#type}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#id S3Bucket#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#uri S3Bucket#uri}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__604190d5601bce01465b47d4fbf34d343f948c0f1fb9da3c4fea27fcf377d8f6)
            check_type(argname="argument permissions", value=permissions, expected_type=type_hints["permissions"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument uri", value=uri, expected_type=type_hints["uri"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "permissions": permissions,
            "type": type,
        }
        if id is not None:
            self._values["id"] = id
        if uri is not None:
            self._values["uri"] = uri

    @builtins.property
    def permissions(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#permissions S3Bucket#permissions}.'''
        result = self._values.get("permissions")
        assert result is not None, "Required property 'permissions' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#type S3Bucket#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#id S3Bucket#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def uri(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#uri S3Bucket#uri}.'''
        result = self._values.get("uri")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketGrant(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3BucketGrantList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3Bucket.S3BucketGrantList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__932a7d884e9bc8b89ecb8b9132e58c3ab8d31d0b65c8373de1ad64508e3b6f36)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "S3BucketGrantOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72cdd30de58acfa685a8feb618a1861d420cb2d10776a390cf82a5af9061c706)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("S3BucketGrantOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c53b6bcf6c062e8823eef3f03637693d9c9920e1aee1e54068169dccfb66fe94)
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
            type_hints = typing.get_type_hints(_typecheckingstub__caa7cdece3fb0380926c6880ce59c9efa82eb77baf2165a065326876f84f1194)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1b781244e3eea82b72372f1405356d94e1adc3d7c94194ad2c7a935a002ce477)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[S3BucketGrant]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[S3BucketGrant]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[S3BucketGrant]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd34c5d1bbb4115e1418a8361409f78954c45d12ae5ed9b4b942bde647aaa9e5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class S3BucketGrantOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3Bucket.S3BucketGrantOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__187d0ebc2ecb26a564a49d189065d81657dad8b7b70d3e427933bf61e47dac86)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetUri")
    def reset_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUri", []))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="permissionsInput")
    def permissions_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "permissionsInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="uriInput")
    def uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "uriInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7cbb3078b03dd5604ec3e44e93651660a2efe8d837ada4ee9d3c1e1bd5d045c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="permissions")
    def permissions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "permissions"))

    @permissions.setter
    def permissions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5896db6d43b7141014d9444d7dbe1e990ce95bdc6a683dbac5659e3d2c6543a0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "permissions", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c3b89b43110292cdeaf6223c841f53c922fa34239cc625728e48476710dc46a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="uri")
    def uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uri"))

    @uri.setter
    def uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__828085b85382d2361f65706a99a85431246cdb8aacd8945988fa4bf1dce46baf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "uri", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[S3BucketGrant, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[S3BucketGrant, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[S3BucketGrant, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a1333d67f7fb8cddbaeb35f0c8fafc01f20eb871d1ed3c6ab9da25fb74de8d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.s3Bucket.S3BucketLifecycleRule",
    jsii_struct_bases=[],
    name_mapping={
        "enabled": "enabled",
        "abort_incomplete_multipart_upload_days": "abortIncompleteMultipartUploadDays",
        "expiration": "expiration",
        "id": "id",
        "noncurrent_version_expiration": "noncurrentVersionExpiration",
        "noncurrent_version_transition": "noncurrentVersionTransition",
        "prefix": "prefix",
        "tags": "tags",
        "transition": "transition",
    },
)
class S3BucketLifecycleRule:
    def __init__(
        self,
        *,
        enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        abort_incomplete_multipart_upload_days: typing.Optional[jsii.Number] = None,
        expiration: typing.Optional[typing.Union["S3BucketLifecycleRuleExpiration", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        noncurrent_version_expiration: typing.Optional[typing.Union["S3BucketLifecycleRuleNoncurrentVersionExpiration", typing.Dict[builtins.str, typing.Any]]] = None,
        noncurrent_version_transition: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["S3BucketLifecycleRuleNoncurrentVersionTransition", typing.Dict[builtins.str, typing.Any]]]]] = None,
        prefix: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        transition: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["S3BucketLifecycleRuleTransition", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#enabled S3Bucket#enabled}.
        :param abort_incomplete_multipart_upload_days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#abort_incomplete_multipart_upload_days S3Bucket#abort_incomplete_multipart_upload_days}.
        :param expiration: expiration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#expiration S3Bucket#expiration}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#id S3Bucket#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param noncurrent_version_expiration: noncurrent_version_expiration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#noncurrent_version_expiration S3Bucket#noncurrent_version_expiration}
        :param noncurrent_version_transition: noncurrent_version_transition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#noncurrent_version_transition S3Bucket#noncurrent_version_transition}
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#prefix S3Bucket#prefix}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#tags S3Bucket#tags}.
        :param transition: transition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#transition S3Bucket#transition}
        '''
        if isinstance(expiration, dict):
            expiration = S3BucketLifecycleRuleExpiration(**expiration)
        if isinstance(noncurrent_version_expiration, dict):
            noncurrent_version_expiration = S3BucketLifecycleRuleNoncurrentVersionExpiration(**noncurrent_version_expiration)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80ca1c12fa30c0c5685cf18f87f72b6c279b7e84b5cd4aa550c0116342f3ec29)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument abort_incomplete_multipart_upload_days", value=abort_incomplete_multipart_upload_days, expected_type=type_hints["abort_incomplete_multipart_upload_days"])
            check_type(argname="argument expiration", value=expiration, expected_type=type_hints["expiration"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument noncurrent_version_expiration", value=noncurrent_version_expiration, expected_type=type_hints["noncurrent_version_expiration"])
            check_type(argname="argument noncurrent_version_transition", value=noncurrent_version_transition, expected_type=type_hints["noncurrent_version_transition"])
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument transition", value=transition, expected_type=type_hints["transition"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "enabled": enabled,
        }
        if abort_incomplete_multipart_upload_days is not None:
            self._values["abort_incomplete_multipart_upload_days"] = abort_incomplete_multipart_upload_days
        if expiration is not None:
            self._values["expiration"] = expiration
        if id is not None:
            self._values["id"] = id
        if noncurrent_version_expiration is not None:
            self._values["noncurrent_version_expiration"] = noncurrent_version_expiration
        if noncurrent_version_transition is not None:
            self._values["noncurrent_version_transition"] = noncurrent_version_transition
        if prefix is not None:
            self._values["prefix"] = prefix
        if tags is not None:
            self._values["tags"] = tags
        if transition is not None:
            self._values["transition"] = transition

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#enabled S3Bucket#enabled}.'''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    @builtins.property
    def abort_incomplete_multipart_upload_days(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#abort_incomplete_multipart_upload_days S3Bucket#abort_incomplete_multipart_upload_days}.'''
        result = self._values.get("abort_incomplete_multipart_upload_days")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def expiration(self) -> typing.Optional["S3BucketLifecycleRuleExpiration"]:
        '''expiration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#expiration S3Bucket#expiration}
        '''
        result = self._values.get("expiration")
        return typing.cast(typing.Optional["S3BucketLifecycleRuleExpiration"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#id S3Bucket#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def noncurrent_version_expiration(
        self,
    ) -> typing.Optional["S3BucketLifecycleRuleNoncurrentVersionExpiration"]:
        '''noncurrent_version_expiration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#noncurrent_version_expiration S3Bucket#noncurrent_version_expiration}
        '''
        result = self._values.get("noncurrent_version_expiration")
        return typing.cast(typing.Optional["S3BucketLifecycleRuleNoncurrentVersionExpiration"], result)

    @builtins.property
    def noncurrent_version_transition(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["S3BucketLifecycleRuleNoncurrentVersionTransition"]]]:
        '''noncurrent_version_transition block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#noncurrent_version_transition S3Bucket#noncurrent_version_transition}
        '''
        result = self._values.get("noncurrent_version_transition")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["S3BucketLifecycleRuleNoncurrentVersionTransition"]]], result)

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#prefix S3Bucket#prefix}.'''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#tags S3Bucket#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def transition(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["S3BucketLifecycleRuleTransition"]]]:
        '''transition block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#transition S3Bucket#transition}
        '''
        result = self._values.get("transition")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["S3BucketLifecycleRuleTransition"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketLifecycleRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.s3Bucket.S3BucketLifecycleRuleExpiration",
    jsii_struct_bases=[],
    name_mapping={
        "date": "date",
        "days": "days",
        "expired_object_delete_marker": "expiredObjectDeleteMarker",
    },
)
class S3BucketLifecycleRuleExpiration:
    def __init__(
        self,
        *,
        date: typing.Optional[builtins.str] = None,
        days: typing.Optional[jsii.Number] = None,
        expired_object_delete_marker: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param date: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#date S3Bucket#date}.
        :param days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#days S3Bucket#days}.
        :param expired_object_delete_marker: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#expired_object_delete_marker S3Bucket#expired_object_delete_marker}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__739b7abc821fb43a2bec3af53b209773c21c718fa2eb186aaf6098c139bbf4b5)
            check_type(argname="argument date", value=date, expected_type=type_hints["date"])
            check_type(argname="argument days", value=days, expected_type=type_hints["days"])
            check_type(argname="argument expired_object_delete_marker", value=expired_object_delete_marker, expected_type=type_hints["expired_object_delete_marker"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if date is not None:
            self._values["date"] = date
        if days is not None:
            self._values["days"] = days
        if expired_object_delete_marker is not None:
            self._values["expired_object_delete_marker"] = expired_object_delete_marker

    @builtins.property
    def date(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#date S3Bucket#date}.'''
        result = self._values.get("date")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def days(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#days S3Bucket#days}.'''
        result = self._values.get("days")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def expired_object_delete_marker(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#expired_object_delete_marker S3Bucket#expired_object_delete_marker}.'''
        result = self._values.get("expired_object_delete_marker")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketLifecycleRuleExpiration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3BucketLifecycleRuleExpirationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3Bucket.S3BucketLifecycleRuleExpirationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b97ad0bd9009373c3934881985aab2be04f86ed9bf64049413c0259eb724721d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDate")
    def reset_date(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDate", []))

    @jsii.member(jsii_name="resetDays")
    def reset_days(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDays", []))

    @jsii.member(jsii_name="resetExpiredObjectDeleteMarker")
    def reset_expired_object_delete_marker(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExpiredObjectDeleteMarker", []))

    @builtins.property
    @jsii.member(jsii_name="dateInput")
    def date_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dateInput"))

    @builtins.property
    @jsii.member(jsii_name="daysInput")
    def days_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "daysInput"))

    @builtins.property
    @jsii.member(jsii_name="expiredObjectDeleteMarkerInput")
    def expired_object_delete_marker_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "expiredObjectDeleteMarkerInput"))

    @builtins.property
    @jsii.member(jsii_name="date")
    def date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "date"))

    @date.setter
    def date(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82e14d83b39e33cc6563032cf9658a1cfc01118238e93b752d794c8d2e6534b5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "date", value)

    @builtins.property
    @jsii.member(jsii_name="days")
    def days(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "days"))

    @days.setter
    def days(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e4f51ed492c71b5e71308e010208a62b12de941b6b5160226c9e33da60888df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "days", value)

    @builtins.property
    @jsii.member(jsii_name="expiredObjectDeleteMarker")
    def expired_object_delete_marker(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "expiredObjectDeleteMarker"))

    @expired_object_delete_marker.setter
    def expired_object_delete_marker(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c0013fcc7f0c4398f25c6dd310e331e7d44e4b3a24ec7091d9b39679bc0885d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expiredObjectDeleteMarker", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[S3BucketLifecycleRuleExpiration]:
        return typing.cast(typing.Optional[S3BucketLifecycleRuleExpiration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3BucketLifecycleRuleExpiration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0696861c7b7a9b59f3d881eca9d0339234d98044de8a4dcac151c5b5ff86c12)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class S3BucketLifecycleRuleList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3Bucket.S3BucketLifecycleRuleList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__bcf331a02d550f6108bc1c40000cd33c9c1b4e5a59605376a35d38da6aa5c881)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "S3BucketLifecycleRuleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0be3aa9de1b3e1af6840c023ea533def8019a6c4fa9a42ac322f3a5a2b708aed)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("S3BucketLifecycleRuleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da0efed52c97ea2725b2170a49214425e9a8491f86ee4764e35c792b4e6a0cfc)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8248c68a789b2343ccf56d4db7b6ac59a51ea78e74654ceebd0c5fe278f14977)
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
            type_hints = typing.get_type_hints(_typecheckingstub__96d2c354b906e94afe733ff5cabff5cb64845c2948a772c42c75fdecc28ff03c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[S3BucketLifecycleRule]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[S3BucketLifecycleRule]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[S3BucketLifecycleRule]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d77207183a354af8fe8dedbb44902e9982891f037ad345c2d84604a771c0218)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.s3Bucket.S3BucketLifecycleRuleNoncurrentVersionExpiration",
    jsii_struct_bases=[],
    name_mapping={"days": "days"},
)
class S3BucketLifecycleRuleNoncurrentVersionExpiration:
    def __init__(self, *, days: typing.Optional[jsii.Number] = None) -> None:
        '''
        :param days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#days S3Bucket#days}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__903034d7896a3c427948dc17fb4613c20be0192d06d2c8957c116a97ba9e5063)
            check_type(argname="argument days", value=days, expected_type=type_hints["days"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if days is not None:
            self._values["days"] = days

    @builtins.property
    def days(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#days S3Bucket#days}.'''
        result = self._values.get("days")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketLifecycleRuleNoncurrentVersionExpiration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3BucketLifecycleRuleNoncurrentVersionExpirationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3Bucket.S3BucketLifecycleRuleNoncurrentVersionExpirationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a1c6366f6224013a7c097ad0dfe21f3efe51f285ca507cf66e053aa61add458a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDays")
    def reset_days(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDays", []))

    @builtins.property
    @jsii.member(jsii_name="daysInput")
    def days_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "daysInput"))

    @builtins.property
    @jsii.member(jsii_name="days")
    def days(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "days"))

    @days.setter
    def days(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c157e5dab5b03ec6eee4b5d95043418a4145cad7bda8509945e60d93db12067)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "days", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3BucketLifecycleRuleNoncurrentVersionExpiration]:
        return typing.cast(typing.Optional[S3BucketLifecycleRuleNoncurrentVersionExpiration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3BucketLifecycleRuleNoncurrentVersionExpiration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54d62c1029fad84a2d63462887acf94555e0c527919e591127cac2fe812215ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.s3Bucket.S3BucketLifecycleRuleNoncurrentVersionTransition",
    jsii_struct_bases=[],
    name_mapping={"storage_class": "storageClass", "days": "days"},
)
class S3BucketLifecycleRuleNoncurrentVersionTransition:
    def __init__(
        self,
        *,
        storage_class: builtins.str,
        days: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param storage_class: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#storage_class S3Bucket#storage_class}.
        :param days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#days S3Bucket#days}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a5e87ab248f6a841c2ce169c9b16930e7a6b7934be48671f19c82361896bf22)
            check_type(argname="argument storage_class", value=storage_class, expected_type=type_hints["storage_class"])
            check_type(argname="argument days", value=days, expected_type=type_hints["days"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "storage_class": storage_class,
        }
        if days is not None:
            self._values["days"] = days

    @builtins.property
    def storage_class(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#storage_class S3Bucket#storage_class}.'''
        result = self._values.get("storage_class")
        assert result is not None, "Required property 'storage_class' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def days(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#days S3Bucket#days}.'''
        result = self._values.get("days")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketLifecycleRuleNoncurrentVersionTransition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3BucketLifecycleRuleNoncurrentVersionTransitionList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3Bucket.S3BucketLifecycleRuleNoncurrentVersionTransitionList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a90178b81d679b9562c8a3961a2ae6e62567854e13fb4484965d592b199fa653)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "S3BucketLifecycleRuleNoncurrentVersionTransitionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2685a7e0af91d6f6b6ab2bca41205b992e2de838fb747d0a70b20a1c25233c9)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("S3BucketLifecycleRuleNoncurrentVersionTransitionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2054e755c6316bb7d493e5784d603d0f176f734478774ee1877466dc5ad0bd6b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__44b512a9cb73872f82633e8eeb5ac5bb3d2e595547971ffdc858c26924642dd4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0ea5e413f26d49b1a5f66d2b390cb7e6d7733fba213d9cf3e3f102ff0314951a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[S3BucketLifecycleRuleNoncurrentVersionTransition]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[S3BucketLifecycleRuleNoncurrentVersionTransition]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[S3BucketLifecycleRuleNoncurrentVersionTransition]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49a293e2faad2c9a177e15d2b4693dfbc884666a449c0cfd1b1133eb22beb4b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class S3BucketLifecycleRuleNoncurrentVersionTransitionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3Bucket.S3BucketLifecycleRuleNoncurrentVersionTransitionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__95b5fad17d58df6973f64eaa12bdb8aff6834057ae20a793b8a79d2284becf11)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDays")
    def reset_days(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDays", []))

    @builtins.property
    @jsii.member(jsii_name="daysInput")
    def days_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "daysInput"))

    @builtins.property
    @jsii.member(jsii_name="storageClassInput")
    def storage_class_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageClassInput"))

    @builtins.property
    @jsii.member(jsii_name="days")
    def days(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "days"))

    @days.setter
    def days(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c231974e9e9b0f710ed14a625385a67ff58e900175de3b8182291190a03e7224)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "days", value)

    @builtins.property
    @jsii.member(jsii_name="storageClass")
    def storage_class(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageClass"))

    @storage_class.setter
    def storage_class(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__716545e6476bcdcb54a13699104cb065dadd03ee0ea8bb70fd022094da686430)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageClass", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[S3BucketLifecycleRuleNoncurrentVersionTransition, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[S3BucketLifecycleRuleNoncurrentVersionTransition, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[S3BucketLifecycleRuleNoncurrentVersionTransition, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__823a9528bee817ad4607a72a954a3fc95f65dabb02e19fc01d2952d10d747b48)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class S3BucketLifecycleRuleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3Bucket.S3BucketLifecycleRuleOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7c589d6ad4c8bd36c49ef549557b8df4f0d255fdba5258e56d343c27ce9644b1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putExpiration")
    def put_expiration(
        self,
        *,
        date: typing.Optional[builtins.str] = None,
        days: typing.Optional[jsii.Number] = None,
        expired_object_delete_marker: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param date: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#date S3Bucket#date}.
        :param days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#days S3Bucket#days}.
        :param expired_object_delete_marker: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#expired_object_delete_marker S3Bucket#expired_object_delete_marker}.
        '''
        value = S3BucketLifecycleRuleExpiration(
            date=date,
            days=days,
            expired_object_delete_marker=expired_object_delete_marker,
        )

        return typing.cast(None, jsii.invoke(self, "putExpiration", [value]))

    @jsii.member(jsii_name="putNoncurrentVersionExpiration")
    def put_noncurrent_version_expiration(
        self,
        *,
        days: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#days S3Bucket#days}.
        '''
        value = S3BucketLifecycleRuleNoncurrentVersionExpiration(days=days)

        return typing.cast(None, jsii.invoke(self, "putNoncurrentVersionExpiration", [value]))

    @jsii.member(jsii_name="putNoncurrentVersionTransition")
    def put_noncurrent_version_transition(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[S3BucketLifecycleRuleNoncurrentVersionTransition, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5026cb91f7a324975796adb7d0e7dd11b82da4b76ed91867d4ccadf5b5190462)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNoncurrentVersionTransition", [value]))

    @jsii.member(jsii_name="putTransition")
    def put_transition(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["S3BucketLifecycleRuleTransition", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__34e1cfdea381841ffde4e198c430a3704c47f2ba409cb129b04b689fb6f8aece)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTransition", [value]))

    @jsii.member(jsii_name="resetAbortIncompleteMultipartUploadDays")
    def reset_abort_incomplete_multipart_upload_days(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAbortIncompleteMultipartUploadDays", []))

    @jsii.member(jsii_name="resetExpiration")
    def reset_expiration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExpiration", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetNoncurrentVersionExpiration")
    def reset_noncurrent_version_expiration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNoncurrentVersionExpiration", []))

    @jsii.member(jsii_name="resetNoncurrentVersionTransition")
    def reset_noncurrent_version_transition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNoncurrentVersionTransition", []))

    @jsii.member(jsii_name="resetPrefix")
    def reset_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrefix", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTransition")
    def reset_transition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTransition", []))

    @builtins.property
    @jsii.member(jsii_name="expiration")
    def expiration(self) -> S3BucketLifecycleRuleExpirationOutputReference:
        return typing.cast(S3BucketLifecycleRuleExpirationOutputReference, jsii.get(self, "expiration"))

    @builtins.property
    @jsii.member(jsii_name="noncurrentVersionExpiration")
    def noncurrent_version_expiration(
        self,
    ) -> S3BucketLifecycleRuleNoncurrentVersionExpirationOutputReference:
        return typing.cast(S3BucketLifecycleRuleNoncurrentVersionExpirationOutputReference, jsii.get(self, "noncurrentVersionExpiration"))

    @builtins.property
    @jsii.member(jsii_name="noncurrentVersionTransition")
    def noncurrent_version_transition(
        self,
    ) -> S3BucketLifecycleRuleNoncurrentVersionTransitionList:
        return typing.cast(S3BucketLifecycleRuleNoncurrentVersionTransitionList, jsii.get(self, "noncurrentVersionTransition"))

    @builtins.property
    @jsii.member(jsii_name="transition")
    def transition(self) -> "S3BucketLifecycleRuleTransitionList":
        return typing.cast("S3BucketLifecycleRuleTransitionList", jsii.get(self, "transition"))

    @builtins.property
    @jsii.member(jsii_name="abortIncompleteMultipartUploadDaysInput")
    def abort_incomplete_multipart_upload_days_input(
        self,
    ) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "abortIncompleteMultipartUploadDaysInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="expirationInput")
    def expiration_input(self) -> typing.Optional[S3BucketLifecycleRuleExpiration]:
        return typing.cast(typing.Optional[S3BucketLifecycleRuleExpiration], jsii.get(self, "expirationInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="noncurrentVersionExpirationInput")
    def noncurrent_version_expiration_input(
        self,
    ) -> typing.Optional[S3BucketLifecycleRuleNoncurrentVersionExpiration]:
        return typing.cast(typing.Optional[S3BucketLifecycleRuleNoncurrentVersionExpiration], jsii.get(self, "noncurrentVersionExpirationInput"))

    @builtins.property
    @jsii.member(jsii_name="noncurrentVersionTransitionInput")
    def noncurrent_version_transition_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[S3BucketLifecycleRuleNoncurrentVersionTransition]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[S3BucketLifecycleRuleNoncurrentVersionTransition]]], jsii.get(self, "noncurrentVersionTransitionInput"))

    @builtins.property
    @jsii.member(jsii_name="prefixInput")
    def prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefixInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="transitionInput")
    def transition_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["S3BucketLifecycleRuleTransition"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["S3BucketLifecycleRuleTransition"]]], jsii.get(self, "transitionInput"))

    @builtins.property
    @jsii.member(jsii_name="abortIncompleteMultipartUploadDays")
    def abort_incomplete_multipart_upload_days(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "abortIncompleteMultipartUploadDays"))

    @abort_incomplete_multipart_upload_days.setter
    def abort_incomplete_multipart_upload_days(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd4f9e4fabbc7bfd07e5bbadbe2b1f1cf960a4d32c28eb98aaff019a7cf65596)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "abortIncompleteMultipartUploadDays", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__dc8228e48a97cf79bb818e30d4497c3a04d6f41270813a6ff4b76dc18207f13b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f8dcdb064b9b8311e711a2dd5d02a0541f2936ce340cbb93c25c2c63ae3732c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="prefix")
    def prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prefix"))

    @prefix.setter
    def prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f675443676653389d89388f47f38ac3c2d6483d3c4b11145e342cdb1e3d8f41a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefix", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd789dcd5f275877282bae90821bd7669b583d946734aa33099ecd869eb10bcf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[S3BucketLifecycleRule, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[S3BucketLifecycleRule, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[S3BucketLifecycleRule, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad9a49f2b6bd9bcab1ab2b72c8a2f2f965a2a8fcb5956cc28cc4e0cc77d837fc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.s3Bucket.S3BucketLifecycleRuleTransition",
    jsii_struct_bases=[],
    name_mapping={"storage_class": "storageClass", "date": "date", "days": "days"},
)
class S3BucketLifecycleRuleTransition:
    def __init__(
        self,
        *,
        storage_class: builtins.str,
        date: typing.Optional[builtins.str] = None,
        days: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param storage_class: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#storage_class S3Bucket#storage_class}.
        :param date: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#date S3Bucket#date}.
        :param days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#days S3Bucket#days}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c6590efbab9aab57e9492a9e9b6fb43e9a71cae76db80011ec50f261e17bc95)
            check_type(argname="argument storage_class", value=storage_class, expected_type=type_hints["storage_class"])
            check_type(argname="argument date", value=date, expected_type=type_hints["date"])
            check_type(argname="argument days", value=days, expected_type=type_hints["days"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "storage_class": storage_class,
        }
        if date is not None:
            self._values["date"] = date
        if days is not None:
            self._values["days"] = days

    @builtins.property
    def storage_class(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#storage_class S3Bucket#storage_class}.'''
        result = self._values.get("storage_class")
        assert result is not None, "Required property 'storage_class' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def date(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#date S3Bucket#date}.'''
        result = self._values.get("date")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def days(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#days S3Bucket#days}.'''
        result = self._values.get("days")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketLifecycleRuleTransition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3BucketLifecycleRuleTransitionList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3Bucket.S3BucketLifecycleRuleTransitionList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__639d3afa6d2466e93bb451ba1739b0fbe8afa0ebcd80fea31f07a37430a7edac)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "S3BucketLifecycleRuleTransitionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a96ab2722432c9e1afedc524ef016cb93513aafd52bfc1d32097d83f8f164ee7)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("S3BucketLifecycleRuleTransitionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c4f2ebafd22e1179b610b52e2c4f11b8e26b7afbae91625bd5d6a8a5a394152)
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
            type_hints = typing.get_type_hints(_typecheckingstub__99a6f2d2340a8e978f09967b6747fb86ddcbbc5a38433f8c0af8a96184b7cff2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9772c3d900667aaeae51df774a2f1aa2003989183f7670f1283206f86512da32)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[S3BucketLifecycleRuleTransition]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[S3BucketLifecycleRuleTransition]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[S3BucketLifecycleRuleTransition]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35142a2641f17fff8c1aef3225411e57430513aa0048764b71f2dd64eccabea0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class S3BucketLifecycleRuleTransitionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3Bucket.S3BucketLifecycleRuleTransitionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1c5d86b2b1a322b21f5ef7d70d45f9f6c09b36d382865e33354d1ec824c72b95)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDate")
    def reset_date(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDate", []))

    @jsii.member(jsii_name="resetDays")
    def reset_days(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDays", []))

    @builtins.property
    @jsii.member(jsii_name="dateInput")
    def date_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dateInput"))

    @builtins.property
    @jsii.member(jsii_name="daysInput")
    def days_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "daysInput"))

    @builtins.property
    @jsii.member(jsii_name="storageClassInput")
    def storage_class_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageClassInput"))

    @builtins.property
    @jsii.member(jsii_name="date")
    def date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "date"))

    @date.setter
    def date(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__751cc72fb7f8edc25e062d8156738e00f9bf894b0e027aeaa09e00e81e74adc7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "date", value)

    @builtins.property
    @jsii.member(jsii_name="days")
    def days(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "days"))

    @days.setter
    def days(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4be540f17ee9ee3d6d977a129f505a94ac0e6fbfb939fec3e1164029898b1dfa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "days", value)

    @builtins.property
    @jsii.member(jsii_name="storageClass")
    def storage_class(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageClass"))

    @storage_class.setter
    def storage_class(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44b96ae23d406be0a46043331c9a01cc831cfd321d6c6bfae8f1b1a3257a3768)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageClass", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[S3BucketLifecycleRuleTransition, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[S3BucketLifecycleRuleTransition, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[S3BucketLifecycleRuleTransition, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b8e5b7021db03e7b22a0d5779d2d99596acc7fc860e66b3b6443282b2175b1f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.s3Bucket.S3BucketLogging",
    jsii_struct_bases=[],
    name_mapping={"target_bucket": "targetBucket", "target_prefix": "targetPrefix"},
)
class S3BucketLogging:
    def __init__(
        self,
        *,
        target_bucket: builtins.str,
        target_prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param target_bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#target_bucket S3Bucket#target_bucket}.
        :param target_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#target_prefix S3Bucket#target_prefix}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4cf88ff8d9e909681bce96a4b5f7b8eccc1e1321204810d2d5de60de4ef5009)
            check_type(argname="argument target_bucket", value=target_bucket, expected_type=type_hints["target_bucket"])
            check_type(argname="argument target_prefix", value=target_prefix, expected_type=type_hints["target_prefix"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "target_bucket": target_bucket,
        }
        if target_prefix is not None:
            self._values["target_prefix"] = target_prefix

    @builtins.property
    def target_bucket(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#target_bucket S3Bucket#target_bucket}.'''
        result = self._values.get("target_bucket")
        assert result is not None, "Required property 'target_bucket' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#target_prefix S3Bucket#target_prefix}.'''
        result = self._values.get("target_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketLogging(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3BucketLoggingOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3Bucket.S3BucketLoggingOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f3b3970f3c7bb1ee477520122968eeff00ae66e05e797d55b1fc7ce020e907b9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetTargetPrefix")
    def reset_target_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetPrefix", []))

    @builtins.property
    @jsii.member(jsii_name="targetBucketInput")
    def target_bucket_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetBucketInput"))

    @builtins.property
    @jsii.member(jsii_name="targetPrefixInput")
    def target_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="targetBucket")
    def target_bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetBucket"))

    @target_bucket.setter
    def target_bucket(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c173b9fb5a00be883d975d21bdf6256ea281a7f66fe6a599d0d728abc00271a6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetBucket", value)

    @builtins.property
    @jsii.member(jsii_name="targetPrefix")
    def target_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetPrefix"))

    @target_prefix.setter
    def target_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6eef86d19833592ef6a07d9b85acad4c2a79ef9bac6926c9e448fd92767de3b2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[S3BucketLogging]:
        return typing.cast(typing.Optional[S3BucketLogging], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[S3BucketLogging]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6cfc62ac8f17908119c81489b6c4d3167d9bd7b07fb2dde07ce00f17360abcad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.s3Bucket.S3BucketObjectLockConfiguration",
    jsii_struct_bases=[],
    name_mapping={"object_lock_enabled": "objectLockEnabled", "rule": "rule"},
)
class S3BucketObjectLockConfiguration:
    def __init__(
        self,
        *,
        object_lock_enabled: typing.Optional[builtins.str] = None,
        rule: typing.Optional[typing.Union["S3BucketObjectLockConfigurationRule", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param object_lock_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#object_lock_enabled S3Bucket#object_lock_enabled}.
        :param rule: rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#rule S3Bucket#rule}
        '''
        if isinstance(rule, dict):
            rule = S3BucketObjectLockConfigurationRule(**rule)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f76932c8f33bcf0fe3bf3c9dbf7893f66d5451d61b6f0ce156e8b4acbfa63021)
            check_type(argname="argument object_lock_enabled", value=object_lock_enabled, expected_type=type_hints["object_lock_enabled"])
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if object_lock_enabled is not None:
            self._values["object_lock_enabled"] = object_lock_enabled
        if rule is not None:
            self._values["rule"] = rule

    @builtins.property
    def object_lock_enabled(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#object_lock_enabled S3Bucket#object_lock_enabled}.'''
        result = self._values.get("object_lock_enabled")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rule(self) -> typing.Optional["S3BucketObjectLockConfigurationRule"]:
        '''rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#rule S3Bucket#rule}
        '''
        result = self._values.get("rule")
        return typing.cast(typing.Optional["S3BucketObjectLockConfigurationRule"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketObjectLockConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3BucketObjectLockConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3Bucket.S3BucketObjectLockConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__31a3293cde95a486dc3109980fdcace0d1e05594aee84f60de96d4d5be7910df)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putRule")
    def put_rule(
        self,
        *,
        default_retention: typing.Union["S3BucketObjectLockConfigurationRuleDefaultRetention", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param default_retention: default_retention block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#default_retention S3Bucket#default_retention}
        '''
        value = S3BucketObjectLockConfigurationRule(
            default_retention=default_retention
        )

        return typing.cast(None, jsii.invoke(self, "putRule", [value]))

    @jsii.member(jsii_name="resetObjectLockEnabled")
    def reset_object_lock_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetObjectLockEnabled", []))

    @jsii.member(jsii_name="resetRule")
    def reset_rule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRule", []))

    @builtins.property
    @jsii.member(jsii_name="rule")
    def rule(self) -> "S3BucketObjectLockConfigurationRuleOutputReference":
        return typing.cast("S3BucketObjectLockConfigurationRuleOutputReference", jsii.get(self, "rule"))

    @builtins.property
    @jsii.member(jsii_name="objectLockEnabledInput")
    def object_lock_enabled_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectLockEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleInput")
    def rule_input(self) -> typing.Optional["S3BucketObjectLockConfigurationRule"]:
        return typing.cast(typing.Optional["S3BucketObjectLockConfigurationRule"], jsii.get(self, "ruleInput"))

    @builtins.property
    @jsii.member(jsii_name="objectLockEnabled")
    def object_lock_enabled(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "objectLockEnabled"))

    @object_lock_enabled.setter
    def object_lock_enabled(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e817890ad0bab6a4f654edd084c7d52281709819f9c2649707022ae4af848a5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "objectLockEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[S3BucketObjectLockConfiguration]:
        return typing.cast(typing.Optional[S3BucketObjectLockConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3BucketObjectLockConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__198007cedf585d7fdb5331e52fc6e7a941e6a4830d796c22d1c3ab179a66445e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.s3Bucket.S3BucketObjectLockConfigurationRule",
    jsii_struct_bases=[],
    name_mapping={"default_retention": "defaultRetention"},
)
class S3BucketObjectLockConfigurationRule:
    def __init__(
        self,
        *,
        default_retention: typing.Union["S3BucketObjectLockConfigurationRuleDefaultRetention", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param default_retention: default_retention block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#default_retention S3Bucket#default_retention}
        '''
        if isinstance(default_retention, dict):
            default_retention = S3BucketObjectLockConfigurationRuleDefaultRetention(**default_retention)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d6cdb3f620734bb921a459901c63632a1e5fff8bd963ee2807d611929615a75)
            check_type(argname="argument default_retention", value=default_retention, expected_type=type_hints["default_retention"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "default_retention": default_retention,
        }

    @builtins.property
    def default_retention(
        self,
    ) -> "S3BucketObjectLockConfigurationRuleDefaultRetention":
        '''default_retention block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#default_retention S3Bucket#default_retention}
        '''
        result = self._values.get("default_retention")
        assert result is not None, "Required property 'default_retention' is missing"
        return typing.cast("S3BucketObjectLockConfigurationRuleDefaultRetention", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketObjectLockConfigurationRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.s3Bucket.S3BucketObjectLockConfigurationRuleDefaultRetention",
    jsii_struct_bases=[],
    name_mapping={"mode": "mode", "days": "days", "years": "years"},
)
class S3BucketObjectLockConfigurationRuleDefaultRetention:
    def __init__(
        self,
        *,
        mode: builtins.str,
        days: typing.Optional[jsii.Number] = None,
        years: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#mode S3Bucket#mode}.
        :param days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#days S3Bucket#days}.
        :param years: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#years S3Bucket#years}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b25aa6e3acfe819ae30fcc0fe79af67a1f2910c9f89aca73f62395f49c437ff4)
            check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
            check_type(argname="argument days", value=days, expected_type=type_hints["days"])
            check_type(argname="argument years", value=years, expected_type=type_hints["years"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "mode": mode,
        }
        if days is not None:
            self._values["days"] = days
        if years is not None:
            self._values["years"] = years

    @builtins.property
    def mode(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#mode S3Bucket#mode}.'''
        result = self._values.get("mode")
        assert result is not None, "Required property 'mode' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def days(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#days S3Bucket#days}.'''
        result = self._values.get("days")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def years(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#years S3Bucket#years}.'''
        result = self._values.get("years")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketObjectLockConfigurationRuleDefaultRetention(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3BucketObjectLockConfigurationRuleDefaultRetentionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3Bucket.S3BucketObjectLockConfigurationRuleDefaultRetentionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__be412b219f1410dc5db2405b6c66ad4404df20eea564f35219bb954b30dcd29a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDays")
    def reset_days(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDays", []))

    @jsii.member(jsii_name="resetYears")
    def reset_years(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetYears", []))

    @builtins.property
    @jsii.member(jsii_name="daysInput")
    def days_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "daysInput"))

    @builtins.property
    @jsii.member(jsii_name="modeInput")
    def mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modeInput"))

    @builtins.property
    @jsii.member(jsii_name="yearsInput")
    def years_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "yearsInput"))

    @builtins.property
    @jsii.member(jsii_name="days")
    def days(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "days"))

    @days.setter
    def days(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07b0432cbefb2fdb254e47ece7a90b1e94265833df8c6ba6a58549958e7be61c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "days", value)

    @builtins.property
    @jsii.member(jsii_name="mode")
    def mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mode"))

    @mode.setter
    def mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d36dd31459d42c724b2dfd4133cc619239bdfcf0d5fff98233689ee5502afd15)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mode", value)

    @builtins.property
    @jsii.member(jsii_name="years")
    def years(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "years"))

    @years.setter
    def years(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3fc23c4e91a1ba564673863b5f2a7c37aef33830133a67407c0cfb541e67b461)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "years", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3BucketObjectLockConfigurationRuleDefaultRetention]:
        return typing.cast(typing.Optional[S3BucketObjectLockConfigurationRuleDefaultRetention], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3BucketObjectLockConfigurationRuleDefaultRetention],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3100a4daa6cb1d9184aed19cb886768192627cf76eb3966f4f00785b0cc523db)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class S3BucketObjectLockConfigurationRuleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3Bucket.S3BucketObjectLockConfigurationRuleOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__fcd8528593ef15ed52b302299f1e5feac69a18f21979ef9d3e6d14192d3283a0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDefaultRetention")
    def put_default_retention(
        self,
        *,
        mode: builtins.str,
        days: typing.Optional[jsii.Number] = None,
        years: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#mode S3Bucket#mode}.
        :param days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#days S3Bucket#days}.
        :param years: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#years S3Bucket#years}.
        '''
        value = S3BucketObjectLockConfigurationRuleDefaultRetention(
            mode=mode, days=days, years=years
        )

        return typing.cast(None, jsii.invoke(self, "putDefaultRetention", [value]))

    @builtins.property
    @jsii.member(jsii_name="defaultRetention")
    def default_retention(
        self,
    ) -> S3BucketObjectLockConfigurationRuleDefaultRetentionOutputReference:
        return typing.cast(S3BucketObjectLockConfigurationRuleDefaultRetentionOutputReference, jsii.get(self, "defaultRetention"))

    @builtins.property
    @jsii.member(jsii_name="defaultRetentionInput")
    def default_retention_input(
        self,
    ) -> typing.Optional[S3BucketObjectLockConfigurationRuleDefaultRetention]:
        return typing.cast(typing.Optional[S3BucketObjectLockConfigurationRuleDefaultRetention], jsii.get(self, "defaultRetentionInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[S3BucketObjectLockConfigurationRule]:
        return typing.cast(typing.Optional[S3BucketObjectLockConfigurationRule], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3BucketObjectLockConfigurationRule],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11d96d322441aa0ce991943b566bed667bdf1afac285e84d1f2e4d0b0ac6f2b7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.s3Bucket.S3BucketReplicationConfiguration",
    jsii_struct_bases=[],
    name_mapping={"role": "role", "rules": "rules"},
)
class S3BucketReplicationConfiguration:
    def __init__(
        self,
        *,
        role: builtins.str,
        rules: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["S3BucketReplicationConfigurationRules", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#role S3Bucket#role}.
        :param rules: rules block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#rules S3Bucket#rules}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9942c61c03b74f4b8d2619252b40b0a0252c5f473f7b6bb8b022f1c13f9b0d60)
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument rules", value=rules, expected_type=type_hints["rules"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "role": role,
            "rules": rules,
        }

    @builtins.property
    def role(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#role S3Bucket#role}.'''
        result = self._values.get("role")
        assert result is not None, "Required property 'role' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rules(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["S3BucketReplicationConfigurationRules"]]:
        '''rules block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#rules S3Bucket#rules}
        '''
        result = self._values.get("rules")
        assert result is not None, "Required property 'rules' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["S3BucketReplicationConfigurationRules"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketReplicationConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3BucketReplicationConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3Bucket.S3BucketReplicationConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__798ad556d9676da9ab8e95de512ddce8f22f6c09c8dd4b07286ce7bdb3655562)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putRules")
    def put_rules(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["S3BucketReplicationConfigurationRules", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6863e602734556d192a4c880f166660bd35d2eaadcf0509c3e11cf354294fee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRules", [value]))

    @builtins.property
    @jsii.member(jsii_name="rules")
    def rules(self) -> "S3BucketReplicationConfigurationRulesList":
        return typing.cast("S3BucketReplicationConfigurationRulesList", jsii.get(self, "rules"))

    @builtins.property
    @jsii.member(jsii_name="roleInput")
    def role_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleInput"))

    @builtins.property
    @jsii.member(jsii_name="rulesInput")
    def rules_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["S3BucketReplicationConfigurationRules"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["S3BucketReplicationConfigurationRules"]]], jsii.get(self, "rulesInput"))

    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "role"))

    @role.setter
    def role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f56587c20b4a16b8734bd3c114fd6e9a40ca07baa0ad54d942ad572c921c01ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "role", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[S3BucketReplicationConfiguration]:
        return typing.cast(typing.Optional[S3BucketReplicationConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3BucketReplicationConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed4c002119ee85c3f79b78c191b6ad413d1e329e9eea74cd9d7ca1b405b58abb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.s3Bucket.S3BucketReplicationConfigurationRules",
    jsii_struct_bases=[],
    name_mapping={
        "destination": "destination",
        "status": "status",
        "delete_marker_replication_status": "deleteMarkerReplicationStatus",
        "filter": "filter",
        "id": "id",
        "prefix": "prefix",
        "priority": "priority",
        "source_selection_criteria": "sourceSelectionCriteria",
    },
)
class S3BucketReplicationConfigurationRules:
    def __init__(
        self,
        *,
        destination: typing.Union["S3BucketReplicationConfigurationRulesDestination", typing.Dict[builtins.str, typing.Any]],
        status: builtins.str,
        delete_marker_replication_status: typing.Optional[builtins.str] = None,
        filter: typing.Optional[typing.Union["S3BucketReplicationConfigurationRulesFilter", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
        priority: typing.Optional[jsii.Number] = None,
        source_selection_criteria: typing.Optional[typing.Union["S3BucketReplicationConfigurationRulesSourceSelectionCriteria", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param destination: destination block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#destination S3Bucket#destination}
        :param status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#status S3Bucket#status}.
        :param delete_marker_replication_status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#delete_marker_replication_status S3Bucket#delete_marker_replication_status}.
        :param filter: filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#filter S3Bucket#filter}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#id S3Bucket#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#prefix S3Bucket#prefix}.
        :param priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#priority S3Bucket#priority}.
        :param source_selection_criteria: source_selection_criteria block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#source_selection_criteria S3Bucket#source_selection_criteria}
        '''
        if isinstance(destination, dict):
            destination = S3BucketReplicationConfigurationRulesDestination(**destination)
        if isinstance(filter, dict):
            filter = S3BucketReplicationConfigurationRulesFilter(**filter)
        if isinstance(source_selection_criteria, dict):
            source_selection_criteria = S3BucketReplicationConfigurationRulesSourceSelectionCriteria(**source_selection_criteria)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__142a394731b60110d1f0e43731ceff4058b8f26bbaf1536b100eb85c49787002)
            check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            check_type(argname="argument delete_marker_replication_status", value=delete_marker_replication_status, expected_type=type_hints["delete_marker_replication_status"])
            check_type(argname="argument filter", value=filter, expected_type=type_hints["filter"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument source_selection_criteria", value=source_selection_criteria, expected_type=type_hints["source_selection_criteria"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "destination": destination,
            "status": status,
        }
        if delete_marker_replication_status is not None:
            self._values["delete_marker_replication_status"] = delete_marker_replication_status
        if filter is not None:
            self._values["filter"] = filter
        if id is not None:
            self._values["id"] = id
        if prefix is not None:
            self._values["prefix"] = prefix
        if priority is not None:
            self._values["priority"] = priority
        if source_selection_criteria is not None:
            self._values["source_selection_criteria"] = source_selection_criteria

    @builtins.property
    def destination(self) -> "S3BucketReplicationConfigurationRulesDestination":
        '''destination block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#destination S3Bucket#destination}
        '''
        result = self._values.get("destination")
        assert result is not None, "Required property 'destination' is missing"
        return typing.cast("S3BucketReplicationConfigurationRulesDestination", result)

    @builtins.property
    def status(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#status S3Bucket#status}.'''
        result = self._values.get("status")
        assert result is not None, "Required property 'status' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def delete_marker_replication_status(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#delete_marker_replication_status S3Bucket#delete_marker_replication_status}.'''
        result = self._values.get("delete_marker_replication_status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def filter(self) -> typing.Optional["S3BucketReplicationConfigurationRulesFilter"]:
        '''filter block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#filter S3Bucket#filter}
        '''
        result = self._values.get("filter")
        return typing.cast(typing.Optional["S3BucketReplicationConfigurationRulesFilter"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#id S3Bucket#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#prefix S3Bucket#prefix}.'''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def priority(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#priority S3Bucket#priority}.'''
        result = self._values.get("priority")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def source_selection_criteria(
        self,
    ) -> typing.Optional["S3BucketReplicationConfigurationRulesSourceSelectionCriteria"]:
        '''source_selection_criteria block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#source_selection_criteria S3Bucket#source_selection_criteria}
        '''
        result = self._values.get("source_selection_criteria")
        return typing.cast(typing.Optional["S3BucketReplicationConfigurationRulesSourceSelectionCriteria"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketReplicationConfigurationRules(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.s3Bucket.S3BucketReplicationConfigurationRulesDestination",
    jsii_struct_bases=[],
    name_mapping={
        "bucket": "bucket",
        "access_control_translation": "accessControlTranslation",
        "account_id": "accountId",
        "metrics": "metrics",
        "replica_kms_key_id": "replicaKmsKeyId",
        "replication_time": "replicationTime",
        "storage_class": "storageClass",
    },
)
class S3BucketReplicationConfigurationRulesDestination:
    def __init__(
        self,
        *,
        bucket: builtins.str,
        access_control_translation: typing.Optional[typing.Union["S3BucketReplicationConfigurationRulesDestinationAccessControlTranslation", typing.Dict[builtins.str, typing.Any]]] = None,
        account_id: typing.Optional[builtins.str] = None,
        metrics: typing.Optional[typing.Union["S3BucketReplicationConfigurationRulesDestinationMetrics", typing.Dict[builtins.str, typing.Any]]] = None,
        replica_kms_key_id: typing.Optional[builtins.str] = None,
        replication_time: typing.Optional[typing.Union["S3BucketReplicationConfigurationRulesDestinationReplicationTime", typing.Dict[builtins.str, typing.Any]]] = None,
        storage_class: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#bucket S3Bucket#bucket}.
        :param access_control_translation: access_control_translation block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#access_control_translation S3Bucket#access_control_translation}
        :param account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#account_id S3Bucket#account_id}.
        :param metrics: metrics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#metrics S3Bucket#metrics}
        :param replica_kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#replica_kms_key_id S3Bucket#replica_kms_key_id}.
        :param replication_time: replication_time block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#replication_time S3Bucket#replication_time}
        :param storage_class: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#storage_class S3Bucket#storage_class}.
        '''
        if isinstance(access_control_translation, dict):
            access_control_translation = S3BucketReplicationConfigurationRulesDestinationAccessControlTranslation(**access_control_translation)
        if isinstance(metrics, dict):
            metrics = S3BucketReplicationConfigurationRulesDestinationMetrics(**metrics)
        if isinstance(replication_time, dict):
            replication_time = S3BucketReplicationConfigurationRulesDestinationReplicationTime(**replication_time)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0604e4923062b1932bcc4754a919a6a1caf856811d27a68011de17799aff4dee)
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument access_control_translation", value=access_control_translation, expected_type=type_hints["access_control_translation"])
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
            check_type(argname="argument metrics", value=metrics, expected_type=type_hints["metrics"])
            check_type(argname="argument replica_kms_key_id", value=replica_kms_key_id, expected_type=type_hints["replica_kms_key_id"])
            check_type(argname="argument replication_time", value=replication_time, expected_type=type_hints["replication_time"])
            check_type(argname="argument storage_class", value=storage_class, expected_type=type_hints["storage_class"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bucket": bucket,
        }
        if access_control_translation is not None:
            self._values["access_control_translation"] = access_control_translation
        if account_id is not None:
            self._values["account_id"] = account_id
        if metrics is not None:
            self._values["metrics"] = metrics
        if replica_kms_key_id is not None:
            self._values["replica_kms_key_id"] = replica_kms_key_id
        if replication_time is not None:
            self._values["replication_time"] = replication_time
        if storage_class is not None:
            self._values["storage_class"] = storage_class

    @builtins.property
    def bucket(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#bucket S3Bucket#bucket}.'''
        result = self._values.get("bucket")
        assert result is not None, "Required property 'bucket' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_control_translation(
        self,
    ) -> typing.Optional["S3BucketReplicationConfigurationRulesDestinationAccessControlTranslation"]:
        '''access_control_translation block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#access_control_translation S3Bucket#access_control_translation}
        '''
        result = self._values.get("access_control_translation")
        return typing.cast(typing.Optional["S3BucketReplicationConfigurationRulesDestinationAccessControlTranslation"], result)

    @builtins.property
    def account_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#account_id S3Bucket#account_id}.'''
        result = self._values.get("account_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def metrics(
        self,
    ) -> typing.Optional["S3BucketReplicationConfigurationRulesDestinationMetrics"]:
        '''metrics block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#metrics S3Bucket#metrics}
        '''
        result = self._values.get("metrics")
        return typing.cast(typing.Optional["S3BucketReplicationConfigurationRulesDestinationMetrics"], result)

    @builtins.property
    def replica_kms_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#replica_kms_key_id S3Bucket#replica_kms_key_id}.'''
        result = self._values.get("replica_kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def replication_time(
        self,
    ) -> typing.Optional["S3BucketReplicationConfigurationRulesDestinationReplicationTime"]:
        '''replication_time block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#replication_time S3Bucket#replication_time}
        '''
        result = self._values.get("replication_time")
        return typing.cast(typing.Optional["S3BucketReplicationConfigurationRulesDestinationReplicationTime"], result)

    @builtins.property
    def storage_class(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#storage_class S3Bucket#storage_class}.'''
        result = self._values.get("storage_class")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketReplicationConfigurationRulesDestination(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.s3Bucket.S3BucketReplicationConfigurationRulesDestinationAccessControlTranslation",
    jsii_struct_bases=[],
    name_mapping={"owner": "owner"},
)
class S3BucketReplicationConfigurationRulesDestinationAccessControlTranslation:
    def __init__(self, *, owner: builtins.str) -> None:
        '''
        :param owner: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#owner S3Bucket#owner}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c72f8b37d06ec45eafff55931878f5c1b33db77dbc1ab5a433550a104b7ae553)
            check_type(argname="argument owner", value=owner, expected_type=type_hints["owner"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "owner": owner,
        }

    @builtins.property
    def owner(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#owner S3Bucket#owner}.'''
        result = self._values.get("owner")
        assert result is not None, "Required property 'owner' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketReplicationConfigurationRulesDestinationAccessControlTranslation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3BucketReplicationConfigurationRulesDestinationAccessControlTranslationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3Bucket.S3BucketReplicationConfigurationRulesDestinationAccessControlTranslationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3631a6e5973e38ac199cf5e39f5ac094988361bbad8dde46d6214714fd92d917)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="ownerInput")
    def owner_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ownerInput"))

    @builtins.property
    @jsii.member(jsii_name="owner")
    def owner(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "owner"))

    @owner.setter
    def owner(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a95a00452090773f0f4be0aa60d45965ab6b9a8b9bc19f7c8b9c7ae6b34640a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "owner", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3BucketReplicationConfigurationRulesDestinationAccessControlTranslation]:
        return typing.cast(typing.Optional[S3BucketReplicationConfigurationRulesDestinationAccessControlTranslation], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3BucketReplicationConfigurationRulesDestinationAccessControlTranslation],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f06d8971cfc48698e67f56adbe9550abf2b9c948a5247bd9187b4ff97588f6bb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.s3Bucket.S3BucketReplicationConfigurationRulesDestinationMetrics",
    jsii_struct_bases=[],
    name_mapping={"minutes": "minutes", "status": "status"},
)
class S3BucketReplicationConfigurationRulesDestinationMetrics:
    def __init__(
        self,
        *,
        minutes: typing.Optional[jsii.Number] = None,
        status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#minutes S3Bucket#minutes}.
        :param status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#status S3Bucket#status}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cdd9ffa63eb759697513e95bae66d7e2b5c1c7725f9250a201ea0f1d5ba9732c)
            check_type(argname="argument minutes", value=minutes, expected_type=type_hints["minutes"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if minutes is not None:
            self._values["minutes"] = minutes
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def minutes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#minutes S3Bucket#minutes}.'''
        result = self._values.get("minutes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#status S3Bucket#status}.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketReplicationConfigurationRulesDestinationMetrics(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3BucketReplicationConfigurationRulesDestinationMetricsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3Bucket.S3BucketReplicationConfigurationRulesDestinationMetricsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9549ab84da8a9df1b9f6ed9bdbe69ef4f8214aeb1a9aca9f52ae020f7d57d3f1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMinutes")
    def reset_minutes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinutes", []))

    @jsii.member(jsii_name="resetStatus")
    def reset_status(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatus", []))

    @builtins.property
    @jsii.member(jsii_name="minutesInput")
    def minutes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minutesInput"))

    @builtins.property
    @jsii.member(jsii_name="statusInput")
    def status_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statusInput"))

    @builtins.property
    @jsii.member(jsii_name="minutes")
    def minutes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minutes"))

    @minutes.setter
    def minutes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53779ed79b4a4607cb826e0bd7efd7933b291fb921ffc2ea1d0dd3d0cce3652c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minutes", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @status.setter
    def status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d19ca935975a72bbaf0df37f7ab904328ccc5d001d37a9c20d33b9a51fb5526b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3BucketReplicationConfigurationRulesDestinationMetrics]:
        return typing.cast(typing.Optional[S3BucketReplicationConfigurationRulesDestinationMetrics], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3BucketReplicationConfigurationRulesDestinationMetrics],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca805597d40bfde2d615d102cffaf546f972d6e5c0ddf1ad0e970ab11e86072e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class S3BucketReplicationConfigurationRulesDestinationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3Bucket.S3BucketReplicationConfigurationRulesDestinationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7416447563ecf10627f5219425f2e4117bccfd4e297522fc4858a920c2c723de)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAccessControlTranslation")
    def put_access_control_translation(self, *, owner: builtins.str) -> None:
        '''
        :param owner: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#owner S3Bucket#owner}.
        '''
        value = S3BucketReplicationConfigurationRulesDestinationAccessControlTranslation(
            owner=owner
        )

        return typing.cast(None, jsii.invoke(self, "putAccessControlTranslation", [value]))

    @jsii.member(jsii_name="putMetrics")
    def put_metrics(
        self,
        *,
        minutes: typing.Optional[jsii.Number] = None,
        status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#minutes S3Bucket#minutes}.
        :param status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#status S3Bucket#status}.
        '''
        value = S3BucketReplicationConfigurationRulesDestinationMetrics(
            minutes=minutes, status=status
        )

        return typing.cast(None, jsii.invoke(self, "putMetrics", [value]))

    @jsii.member(jsii_name="putReplicationTime")
    def put_replication_time(
        self,
        *,
        minutes: typing.Optional[jsii.Number] = None,
        status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#minutes S3Bucket#minutes}.
        :param status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#status S3Bucket#status}.
        '''
        value = S3BucketReplicationConfigurationRulesDestinationReplicationTime(
            minutes=minutes, status=status
        )

        return typing.cast(None, jsii.invoke(self, "putReplicationTime", [value]))

    @jsii.member(jsii_name="resetAccessControlTranslation")
    def reset_access_control_translation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessControlTranslation", []))

    @jsii.member(jsii_name="resetAccountId")
    def reset_account_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccountId", []))

    @jsii.member(jsii_name="resetMetrics")
    def reset_metrics(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetrics", []))

    @jsii.member(jsii_name="resetReplicaKmsKeyId")
    def reset_replica_kms_key_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReplicaKmsKeyId", []))

    @jsii.member(jsii_name="resetReplicationTime")
    def reset_replication_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReplicationTime", []))

    @jsii.member(jsii_name="resetStorageClass")
    def reset_storage_class(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageClass", []))

    @builtins.property
    @jsii.member(jsii_name="accessControlTranslation")
    def access_control_translation(
        self,
    ) -> S3BucketReplicationConfigurationRulesDestinationAccessControlTranslationOutputReference:
        return typing.cast(S3BucketReplicationConfigurationRulesDestinationAccessControlTranslationOutputReference, jsii.get(self, "accessControlTranslation"))

    @builtins.property
    @jsii.member(jsii_name="metrics")
    def metrics(
        self,
    ) -> S3BucketReplicationConfigurationRulesDestinationMetricsOutputReference:
        return typing.cast(S3BucketReplicationConfigurationRulesDestinationMetricsOutputReference, jsii.get(self, "metrics"))

    @builtins.property
    @jsii.member(jsii_name="replicationTime")
    def replication_time(
        self,
    ) -> "S3BucketReplicationConfigurationRulesDestinationReplicationTimeOutputReference":
        return typing.cast("S3BucketReplicationConfigurationRulesDestinationReplicationTimeOutputReference", jsii.get(self, "replicationTime"))

    @builtins.property
    @jsii.member(jsii_name="accessControlTranslationInput")
    def access_control_translation_input(
        self,
    ) -> typing.Optional[S3BucketReplicationConfigurationRulesDestinationAccessControlTranslation]:
        return typing.cast(typing.Optional[S3BucketReplicationConfigurationRulesDestinationAccessControlTranslation], jsii.get(self, "accessControlTranslationInput"))

    @builtins.property
    @jsii.member(jsii_name="accountIdInput")
    def account_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketInput")
    def bucket_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsInput")
    def metrics_input(
        self,
    ) -> typing.Optional[S3BucketReplicationConfigurationRulesDestinationMetrics]:
        return typing.cast(typing.Optional[S3BucketReplicationConfigurationRulesDestinationMetrics], jsii.get(self, "metricsInput"))

    @builtins.property
    @jsii.member(jsii_name="replicaKmsKeyIdInput")
    def replica_kms_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "replicaKmsKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="replicationTimeInput")
    def replication_time_input(
        self,
    ) -> typing.Optional["S3BucketReplicationConfigurationRulesDestinationReplicationTime"]:
        return typing.cast(typing.Optional["S3BucketReplicationConfigurationRulesDestinationReplicationTime"], jsii.get(self, "replicationTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="storageClassInput")
    def storage_class_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageClassInput"))

    @builtins.property
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accountId"))

    @account_id.setter
    def account_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__922fd1635a0059d62c1a02fa10eefe904559ac58630fb52cc27a7b5c15bb53ac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountId", value)

    @builtins.property
    @jsii.member(jsii_name="bucket")
    def bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucket"))

    @bucket.setter
    def bucket(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7999ff358f71e1ad1fe8b21c064ae7583ea1f1e30770a31f01a608bd8b43e390)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucket", value)

    @builtins.property
    @jsii.member(jsii_name="replicaKmsKeyId")
    def replica_kms_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "replicaKmsKeyId"))

    @replica_kms_key_id.setter
    def replica_kms_key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3daa0614577da81d17c902b9239318d5af3bb4b14ba9beab8018aeb65a3583bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replicaKmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="storageClass")
    def storage_class(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageClass"))

    @storage_class.setter
    def storage_class(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c27237eb18c84db2dc341691634cd7f0ac178777d7f988d9d035ed624768ace)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageClass", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3BucketReplicationConfigurationRulesDestination]:
        return typing.cast(typing.Optional[S3BucketReplicationConfigurationRulesDestination], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3BucketReplicationConfigurationRulesDestination],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc30a8bdd6c2de79b03b8f0c62b918b4cd4f2313de2a341300e634d9db643686)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.s3Bucket.S3BucketReplicationConfigurationRulesDestinationReplicationTime",
    jsii_struct_bases=[],
    name_mapping={"minutes": "minutes", "status": "status"},
)
class S3BucketReplicationConfigurationRulesDestinationReplicationTime:
    def __init__(
        self,
        *,
        minutes: typing.Optional[jsii.Number] = None,
        status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#minutes S3Bucket#minutes}.
        :param status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#status S3Bucket#status}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ce0eb686017296725a6d5b6f03020faae07b36a6e61824cd57e6370770ecfce)
            check_type(argname="argument minutes", value=minutes, expected_type=type_hints["minutes"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if minutes is not None:
            self._values["minutes"] = minutes
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def minutes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#minutes S3Bucket#minutes}.'''
        result = self._values.get("minutes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#status S3Bucket#status}.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketReplicationConfigurationRulesDestinationReplicationTime(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3BucketReplicationConfigurationRulesDestinationReplicationTimeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3Bucket.S3BucketReplicationConfigurationRulesDestinationReplicationTimeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__dc3fb0b1de8d86f78aa94c0fb645f88a60f1ebc8f4965b37caf6b1957091ccd0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMinutes")
    def reset_minutes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinutes", []))

    @jsii.member(jsii_name="resetStatus")
    def reset_status(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatus", []))

    @builtins.property
    @jsii.member(jsii_name="minutesInput")
    def minutes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minutesInput"))

    @builtins.property
    @jsii.member(jsii_name="statusInput")
    def status_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statusInput"))

    @builtins.property
    @jsii.member(jsii_name="minutes")
    def minutes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minutes"))

    @minutes.setter
    def minutes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a617ca7021b18c05c4dafcc1e78c4268c13723bcf4a95ae7a21f460acb9021d6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minutes", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @status.setter
    def status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8361fbd3b7e9c2fae43cc7c58436e24d7f0cb4b4449cf4addc851c037c1411d3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3BucketReplicationConfigurationRulesDestinationReplicationTime]:
        return typing.cast(typing.Optional[S3BucketReplicationConfigurationRulesDestinationReplicationTime], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3BucketReplicationConfigurationRulesDestinationReplicationTime],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39ad51207f89c323424be31963f6f27e67dda9a9367c75557d38b983a86b7a6c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.s3Bucket.S3BucketReplicationConfigurationRulesFilter",
    jsii_struct_bases=[],
    name_mapping={"prefix": "prefix", "tags": "tags"},
)
class S3BucketReplicationConfigurationRulesFilter:
    def __init__(
        self,
        *,
        prefix: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#prefix S3Bucket#prefix}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#tags S3Bucket#tags}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1807a92adcf82027065ffaac6b3ad957f71c4a86e8a478b7e49642c5bd756b43)
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if prefix is not None:
            self._values["prefix"] = prefix
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#prefix S3Bucket#prefix}.'''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#tags S3Bucket#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketReplicationConfigurationRulesFilter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3BucketReplicationConfigurationRulesFilterOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3Bucket.S3BucketReplicationConfigurationRulesFilterOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__dec4dca82937648ac242e4a16894a03cf7b6155b1aa4ee1b22d667f2053f7bd3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetPrefix")
    def reset_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrefix", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @builtins.property
    @jsii.member(jsii_name="prefixInput")
    def prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefixInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="prefix")
    def prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prefix"))

    @prefix.setter
    def prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b19fbeddeafb9cd11b68cd48411aaa01174256741fdb1ca8c39c588b2fe738eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefix", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2df72c7f3e4bd43f43ed8bd067e19814acf44a12741178d0d2ada606594cfd35)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3BucketReplicationConfigurationRulesFilter]:
        return typing.cast(typing.Optional[S3BucketReplicationConfigurationRulesFilter], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3BucketReplicationConfigurationRulesFilter],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d76c80f186df167c7769f877777f3ed4031100ff745f5b10980020d6477154f4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class S3BucketReplicationConfigurationRulesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3Bucket.S3BucketReplicationConfigurationRulesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e9a20cc3df642cddea702de54dc0ed8eb2fb48c7244dcd7a5e4eef62d43606be)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "S3BucketReplicationConfigurationRulesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__739d6487d618e2fed1440f3baa0e4ca70992705efce5c57f68589f5e12478deb)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("S3BucketReplicationConfigurationRulesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__acbc81a7ecfd33cd692255d959241ccdfceacf0da456d55a508f48bf13cfc7d2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__df3880a40ab9ef96d6108aba1020b531a9e3fc6135919d7ee5580c7febb1ffe3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e5287e3060f918b89d5a527b3e2ea15be93c07df7b3482c7909f720b690e7f75)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[S3BucketReplicationConfigurationRules]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[S3BucketReplicationConfigurationRules]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[S3BucketReplicationConfigurationRules]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c9f04f614c64de3aaf23cb2789e4bf38db08c2564fac2edf037e79e52ab97b56)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class S3BucketReplicationConfigurationRulesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3Bucket.S3BucketReplicationConfigurationRulesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b19b20f98177d468c3588eb183c9f27962cb3d9f758bb4f7320999a8424e9b68)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putDestination")
    def put_destination(
        self,
        *,
        bucket: builtins.str,
        access_control_translation: typing.Optional[typing.Union[S3BucketReplicationConfigurationRulesDestinationAccessControlTranslation, typing.Dict[builtins.str, typing.Any]]] = None,
        account_id: typing.Optional[builtins.str] = None,
        metrics: typing.Optional[typing.Union[S3BucketReplicationConfigurationRulesDestinationMetrics, typing.Dict[builtins.str, typing.Any]]] = None,
        replica_kms_key_id: typing.Optional[builtins.str] = None,
        replication_time: typing.Optional[typing.Union[S3BucketReplicationConfigurationRulesDestinationReplicationTime, typing.Dict[builtins.str, typing.Any]]] = None,
        storage_class: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#bucket S3Bucket#bucket}.
        :param access_control_translation: access_control_translation block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#access_control_translation S3Bucket#access_control_translation}
        :param account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#account_id S3Bucket#account_id}.
        :param metrics: metrics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#metrics S3Bucket#metrics}
        :param replica_kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#replica_kms_key_id S3Bucket#replica_kms_key_id}.
        :param replication_time: replication_time block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#replication_time S3Bucket#replication_time}
        :param storage_class: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#storage_class S3Bucket#storage_class}.
        '''
        value = S3BucketReplicationConfigurationRulesDestination(
            bucket=bucket,
            access_control_translation=access_control_translation,
            account_id=account_id,
            metrics=metrics,
            replica_kms_key_id=replica_kms_key_id,
            replication_time=replication_time,
            storage_class=storage_class,
        )

        return typing.cast(None, jsii.invoke(self, "putDestination", [value]))

    @jsii.member(jsii_name="putFilter")
    def put_filter(
        self,
        *,
        prefix: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#prefix S3Bucket#prefix}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#tags S3Bucket#tags}.
        '''
        value = S3BucketReplicationConfigurationRulesFilter(prefix=prefix, tags=tags)

        return typing.cast(None, jsii.invoke(self, "putFilter", [value]))

    @jsii.member(jsii_name="putSourceSelectionCriteria")
    def put_source_selection_criteria(
        self,
        *,
        sse_kms_encrypted_objects: typing.Optional[typing.Union["S3BucketReplicationConfigurationRulesSourceSelectionCriteriaSseKmsEncryptedObjects", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param sse_kms_encrypted_objects: sse_kms_encrypted_objects block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#sse_kms_encrypted_objects S3Bucket#sse_kms_encrypted_objects}
        '''
        value = S3BucketReplicationConfigurationRulesSourceSelectionCriteria(
            sse_kms_encrypted_objects=sse_kms_encrypted_objects
        )

        return typing.cast(None, jsii.invoke(self, "putSourceSelectionCriteria", [value]))

    @jsii.member(jsii_name="resetDeleteMarkerReplicationStatus")
    def reset_delete_marker_replication_status(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeleteMarkerReplicationStatus", []))

    @jsii.member(jsii_name="resetFilter")
    def reset_filter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFilter", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetPrefix")
    def reset_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrefix", []))

    @jsii.member(jsii_name="resetPriority")
    def reset_priority(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPriority", []))

    @jsii.member(jsii_name="resetSourceSelectionCriteria")
    def reset_source_selection_criteria(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceSelectionCriteria", []))

    @builtins.property
    @jsii.member(jsii_name="destination")
    def destination(
        self,
    ) -> S3BucketReplicationConfigurationRulesDestinationOutputReference:
        return typing.cast(S3BucketReplicationConfigurationRulesDestinationOutputReference, jsii.get(self, "destination"))

    @builtins.property
    @jsii.member(jsii_name="filter")
    def filter(self) -> S3BucketReplicationConfigurationRulesFilterOutputReference:
        return typing.cast(S3BucketReplicationConfigurationRulesFilterOutputReference, jsii.get(self, "filter"))

    @builtins.property
    @jsii.member(jsii_name="sourceSelectionCriteria")
    def source_selection_criteria(
        self,
    ) -> "S3BucketReplicationConfigurationRulesSourceSelectionCriteriaOutputReference":
        return typing.cast("S3BucketReplicationConfigurationRulesSourceSelectionCriteriaOutputReference", jsii.get(self, "sourceSelectionCriteria"))

    @builtins.property
    @jsii.member(jsii_name="deleteMarkerReplicationStatusInput")
    def delete_marker_replication_status_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteMarkerReplicationStatusInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationInput")
    def destination_input(
        self,
    ) -> typing.Optional[S3BucketReplicationConfigurationRulesDestination]:
        return typing.cast(typing.Optional[S3BucketReplicationConfigurationRulesDestination], jsii.get(self, "destinationInput"))

    @builtins.property
    @jsii.member(jsii_name="filterInput")
    def filter_input(
        self,
    ) -> typing.Optional[S3BucketReplicationConfigurationRulesFilter]:
        return typing.cast(typing.Optional[S3BucketReplicationConfigurationRulesFilter], jsii.get(self, "filterInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="prefixInput")
    def prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefixInput"))

    @builtins.property
    @jsii.member(jsii_name="priorityInput")
    def priority_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "priorityInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceSelectionCriteriaInput")
    def source_selection_criteria_input(
        self,
    ) -> typing.Optional["S3BucketReplicationConfigurationRulesSourceSelectionCriteria"]:
        return typing.cast(typing.Optional["S3BucketReplicationConfigurationRulesSourceSelectionCriteria"], jsii.get(self, "sourceSelectionCriteriaInput"))

    @builtins.property
    @jsii.member(jsii_name="statusInput")
    def status_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statusInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteMarkerReplicationStatus")
    def delete_marker_replication_status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deleteMarkerReplicationStatus"))

    @delete_marker_replication_status.setter
    def delete_marker_replication_status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__767a9a376eba0effa3acf738196aade8086a0fc1ab703b97d175698670ce6fb1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deleteMarkerReplicationStatus", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3df3bdad95fe1c63208188caaac8870a82df680d1fbfbf28d1c3bd2eb272578)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="prefix")
    def prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prefix"))

    @prefix.setter
    def prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f22c094e0d83c1b9d091edda9dff6e1d69630d489efa15fca91c9f6041a9b47d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefix", value)

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b98d2a97dc16d290f47307a2324b1f6309def1bf3ad167661b652736c56efad7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @status.setter
    def status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b7943b6b8a59a60f6e2013842880f7469d2d5de97d452c037d181936d2b5e9e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[S3BucketReplicationConfigurationRules, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[S3BucketReplicationConfigurationRules, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[S3BucketReplicationConfigurationRules, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6afe5c6932e02888d906aeb5f20bf4e54d39c862746fe06cbc945990db3270d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.s3Bucket.S3BucketReplicationConfigurationRulesSourceSelectionCriteria",
    jsii_struct_bases=[],
    name_mapping={"sse_kms_encrypted_objects": "sseKmsEncryptedObjects"},
)
class S3BucketReplicationConfigurationRulesSourceSelectionCriteria:
    def __init__(
        self,
        *,
        sse_kms_encrypted_objects: typing.Optional[typing.Union["S3BucketReplicationConfigurationRulesSourceSelectionCriteriaSseKmsEncryptedObjects", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param sse_kms_encrypted_objects: sse_kms_encrypted_objects block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#sse_kms_encrypted_objects S3Bucket#sse_kms_encrypted_objects}
        '''
        if isinstance(sse_kms_encrypted_objects, dict):
            sse_kms_encrypted_objects = S3BucketReplicationConfigurationRulesSourceSelectionCriteriaSseKmsEncryptedObjects(**sse_kms_encrypted_objects)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0e14fa81e549a39a3ef152b10d22f7c4155bc8886aefb12e2065dea3b39a648)
            check_type(argname="argument sse_kms_encrypted_objects", value=sse_kms_encrypted_objects, expected_type=type_hints["sse_kms_encrypted_objects"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if sse_kms_encrypted_objects is not None:
            self._values["sse_kms_encrypted_objects"] = sse_kms_encrypted_objects

    @builtins.property
    def sse_kms_encrypted_objects(
        self,
    ) -> typing.Optional["S3BucketReplicationConfigurationRulesSourceSelectionCriteriaSseKmsEncryptedObjects"]:
        '''sse_kms_encrypted_objects block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#sse_kms_encrypted_objects S3Bucket#sse_kms_encrypted_objects}
        '''
        result = self._values.get("sse_kms_encrypted_objects")
        return typing.cast(typing.Optional["S3BucketReplicationConfigurationRulesSourceSelectionCriteriaSseKmsEncryptedObjects"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketReplicationConfigurationRulesSourceSelectionCriteria(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3BucketReplicationConfigurationRulesSourceSelectionCriteriaOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3Bucket.S3BucketReplicationConfigurationRulesSourceSelectionCriteriaOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f9047b1e067afd5c7198e567df4809c35522ba1cf56d3eea7534a1fc6d91e988)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putSseKmsEncryptedObjects")
    def put_sse_kms_encrypted_objects(
        self,
        *,
        enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#enabled S3Bucket#enabled}.
        '''
        value = S3BucketReplicationConfigurationRulesSourceSelectionCriteriaSseKmsEncryptedObjects(
            enabled=enabled
        )

        return typing.cast(None, jsii.invoke(self, "putSseKmsEncryptedObjects", [value]))

    @jsii.member(jsii_name="resetSseKmsEncryptedObjects")
    def reset_sse_kms_encrypted_objects(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSseKmsEncryptedObjects", []))

    @builtins.property
    @jsii.member(jsii_name="sseKmsEncryptedObjects")
    def sse_kms_encrypted_objects(
        self,
    ) -> "S3BucketReplicationConfigurationRulesSourceSelectionCriteriaSseKmsEncryptedObjectsOutputReference":
        return typing.cast("S3BucketReplicationConfigurationRulesSourceSelectionCriteriaSseKmsEncryptedObjectsOutputReference", jsii.get(self, "sseKmsEncryptedObjects"))

    @builtins.property
    @jsii.member(jsii_name="sseKmsEncryptedObjectsInput")
    def sse_kms_encrypted_objects_input(
        self,
    ) -> typing.Optional["S3BucketReplicationConfigurationRulesSourceSelectionCriteriaSseKmsEncryptedObjects"]:
        return typing.cast(typing.Optional["S3BucketReplicationConfigurationRulesSourceSelectionCriteriaSseKmsEncryptedObjects"], jsii.get(self, "sseKmsEncryptedObjectsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3BucketReplicationConfigurationRulesSourceSelectionCriteria]:
        return typing.cast(typing.Optional[S3BucketReplicationConfigurationRulesSourceSelectionCriteria], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3BucketReplicationConfigurationRulesSourceSelectionCriteria],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f30c100e06f1e8e9f78c1160c43c8d051e1731e63f4ace75cb42bbb3704d7e82)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.s3Bucket.S3BucketReplicationConfigurationRulesSourceSelectionCriteriaSseKmsEncryptedObjects",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled"},
)
class S3BucketReplicationConfigurationRulesSourceSelectionCriteriaSseKmsEncryptedObjects:
    def __init__(
        self,
        *,
        enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#enabled S3Bucket#enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a24ebfa79bc9f280d43fdd2e611bc29225dd4c10399edd08a5f555974689f3ef)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "enabled": enabled,
        }

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#enabled S3Bucket#enabled}.'''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketReplicationConfigurationRulesSourceSelectionCriteriaSseKmsEncryptedObjects(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3BucketReplicationConfigurationRulesSourceSelectionCriteriaSseKmsEncryptedObjectsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3Bucket.S3BucketReplicationConfigurationRulesSourceSelectionCriteriaSseKmsEncryptedObjectsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__bfcc5a8946fb0687b109fc27d0b20760085787d87f3bf5d15bf3327e5900ab71)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0214ffc7cfe71a0d91b58e1ff18147bdd5581e750c02fcaac48ed18be09c7a4c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3BucketReplicationConfigurationRulesSourceSelectionCriteriaSseKmsEncryptedObjects]:
        return typing.cast(typing.Optional[S3BucketReplicationConfigurationRulesSourceSelectionCriteriaSseKmsEncryptedObjects], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3BucketReplicationConfigurationRulesSourceSelectionCriteriaSseKmsEncryptedObjects],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a9fde38a79549cf69017ab70f085110e84303d92cc964ca08c726990ec77315)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.s3Bucket.S3BucketServerSideEncryptionConfiguration",
    jsii_struct_bases=[],
    name_mapping={"rule": "rule"},
)
class S3BucketServerSideEncryptionConfiguration:
    def __init__(
        self,
        *,
        rule: typing.Union["S3BucketServerSideEncryptionConfigurationRule", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param rule: rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#rule S3Bucket#rule}
        '''
        if isinstance(rule, dict):
            rule = S3BucketServerSideEncryptionConfigurationRule(**rule)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5bdf50ae47bff19317735c3cc30881d0cfa8fc0c825547a7f87468409f3f8256)
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "rule": rule,
        }

    @builtins.property
    def rule(self) -> "S3BucketServerSideEncryptionConfigurationRule":
        '''rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#rule S3Bucket#rule}
        '''
        result = self._values.get("rule")
        assert result is not None, "Required property 'rule' is missing"
        return typing.cast("S3BucketServerSideEncryptionConfigurationRule", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketServerSideEncryptionConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3BucketServerSideEncryptionConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3Bucket.S3BucketServerSideEncryptionConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4e054b213412766682edd074e9404a23f260898ceeb4566a025e7eeece3c5e97)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putRule")
    def put_rule(
        self,
        *,
        apply_server_side_encryption_by_default: typing.Union["S3BucketServerSideEncryptionConfigurationRuleApplyServerSideEncryptionByDefault", typing.Dict[builtins.str, typing.Any]],
        bucket_key_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param apply_server_side_encryption_by_default: apply_server_side_encryption_by_default block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#apply_server_side_encryption_by_default S3Bucket#apply_server_side_encryption_by_default}
        :param bucket_key_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#bucket_key_enabled S3Bucket#bucket_key_enabled}.
        '''
        value = S3BucketServerSideEncryptionConfigurationRule(
            apply_server_side_encryption_by_default=apply_server_side_encryption_by_default,
            bucket_key_enabled=bucket_key_enabled,
        )

        return typing.cast(None, jsii.invoke(self, "putRule", [value]))

    @builtins.property
    @jsii.member(jsii_name="rule")
    def rule(self) -> "S3BucketServerSideEncryptionConfigurationRuleOutputReference":
        return typing.cast("S3BucketServerSideEncryptionConfigurationRuleOutputReference", jsii.get(self, "rule"))

    @builtins.property
    @jsii.member(jsii_name="ruleInput")
    def rule_input(
        self,
    ) -> typing.Optional["S3BucketServerSideEncryptionConfigurationRule"]:
        return typing.cast(typing.Optional["S3BucketServerSideEncryptionConfigurationRule"], jsii.get(self, "ruleInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3BucketServerSideEncryptionConfiguration]:
        return typing.cast(typing.Optional[S3BucketServerSideEncryptionConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3BucketServerSideEncryptionConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__beadce034aa87cfaf1de57de368d609b6c46d655047b2349fc44d1398ea1e40f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.s3Bucket.S3BucketServerSideEncryptionConfigurationRule",
    jsii_struct_bases=[],
    name_mapping={
        "apply_server_side_encryption_by_default": "applyServerSideEncryptionByDefault",
        "bucket_key_enabled": "bucketKeyEnabled",
    },
)
class S3BucketServerSideEncryptionConfigurationRule:
    def __init__(
        self,
        *,
        apply_server_side_encryption_by_default: typing.Union["S3BucketServerSideEncryptionConfigurationRuleApplyServerSideEncryptionByDefault", typing.Dict[builtins.str, typing.Any]],
        bucket_key_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param apply_server_side_encryption_by_default: apply_server_side_encryption_by_default block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#apply_server_side_encryption_by_default S3Bucket#apply_server_side_encryption_by_default}
        :param bucket_key_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#bucket_key_enabled S3Bucket#bucket_key_enabled}.
        '''
        if isinstance(apply_server_side_encryption_by_default, dict):
            apply_server_side_encryption_by_default = S3BucketServerSideEncryptionConfigurationRuleApplyServerSideEncryptionByDefault(**apply_server_side_encryption_by_default)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9d09131272dc42dd40298ba5a585821c7c4c20bbcac0042800daa5c08a414af)
            check_type(argname="argument apply_server_side_encryption_by_default", value=apply_server_side_encryption_by_default, expected_type=type_hints["apply_server_side_encryption_by_default"])
            check_type(argname="argument bucket_key_enabled", value=bucket_key_enabled, expected_type=type_hints["bucket_key_enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "apply_server_side_encryption_by_default": apply_server_side_encryption_by_default,
        }
        if bucket_key_enabled is not None:
            self._values["bucket_key_enabled"] = bucket_key_enabled

    @builtins.property
    def apply_server_side_encryption_by_default(
        self,
    ) -> "S3BucketServerSideEncryptionConfigurationRuleApplyServerSideEncryptionByDefault":
        '''apply_server_side_encryption_by_default block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#apply_server_side_encryption_by_default S3Bucket#apply_server_side_encryption_by_default}
        '''
        result = self._values.get("apply_server_side_encryption_by_default")
        assert result is not None, "Required property 'apply_server_side_encryption_by_default' is missing"
        return typing.cast("S3BucketServerSideEncryptionConfigurationRuleApplyServerSideEncryptionByDefault", result)

    @builtins.property
    def bucket_key_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#bucket_key_enabled S3Bucket#bucket_key_enabled}.'''
        result = self._values.get("bucket_key_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketServerSideEncryptionConfigurationRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.s3Bucket.S3BucketServerSideEncryptionConfigurationRuleApplyServerSideEncryptionByDefault",
    jsii_struct_bases=[],
    name_mapping={
        "sse_algorithm": "sseAlgorithm",
        "kms_master_key_id": "kmsMasterKeyId",
    },
)
class S3BucketServerSideEncryptionConfigurationRuleApplyServerSideEncryptionByDefault:
    def __init__(
        self,
        *,
        sse_algorithm: builtins.str,
        kms_master_key_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param sse_algorithm: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#sse_algorithm S3Bucket#sse_algorithm}.
        :param kms_master_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#kms_master_key_id S3Bucket#kms_master_key_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b543f0775903c35c2e8a07b3860531665754e57fef685c89ff2524b37405dea5)
            check_type(argname="argument sse_algorithm", value=sse_algorithm, expected_type=type_hints["sse_algorithm"])
            check_type(argname="argument kms_master_key_id", value=kms_master_key_id, expected_type=type_hints["kms_master_key_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "sse_algorithm": sse_algorithm,
        }
        if kms_master_key_id is not None:
            self._values["kms_master_key_id"] = kms_master_key_id

    @builtins.property
    def sse_algorithm(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#sse_algorithm S3Bucket#sse_algorithm}.'''
        result = self._values.get("sse_algorithm")
        assert result is not None, "Required property 'sse_algorithm' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def kms_master_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#kms_master_key_id S3Bucket#kms_master_key_id}.'''
        result = self._values.get("kms_master_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketServerSideEncryptionConfigurationRuleApplyServerSideEncryptionByDefault(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3BucketServerSideEncryptionConfigurationRuleApplyServerSideEncryptionByDefaultOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3Bucket.S3BucketServerSideEncryptionConfigurationRuleApplyServerSideEncryptionByDefaultOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2b4b2f628afcf9c9c8027f878bbe2a295648a32056cc2e0b1c9e8ff3b2fd6a98)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetKmsMasterKeyId")
    def reset_kms_master_key_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsMasterKeyId", []))

    @builtins.property
    @jsii.member(jsii_name="kmsMasterKeyIdInput")
    def kms_master_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsMasterKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="sseAlgorithmInput")
    def sse_algorithm_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sseAlgorithmInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsMasterKeyId")
    def kms_master_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsMasterKeyId"))

    @kms_master_key_id.setter
    def kms_master_key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af9d078332726f44438fa45cad23e4db0f054f7a7bcddefbbb3a08a1f61e6adb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsMasterKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="sseAlgorithm")
    def sse_algorithm(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sseAlgorithm"))

    @sse_algorithm.setter
    def sse_algorithm(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce7689fe14b5dab723ab473e388b8bbec9b2158676942710ad73fef45581afaf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sseAlgorithm", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3BucketServerSideEncryptionConfigurationRuleApplyServerSideEncryptionByDefault]:
        return typing.cast(typing.Optional[S3BucketServerSideEncryptionConfigurationRuleApplyServerSideEncryptionByDefault], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3BucketServerSideEncryptionConfigurationRuleApplyServerSideEncryptionByDefault],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8216331060c4ec4e4314f451ec1bd12baa9392439a7f5c80a5ef0fabe9ac4339)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class S3BucketServerSideEncryptionConfigurationRuleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3Bucket.S3BucketServerSideEncryptionConfigurationRuleOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__35a682e36c4b7ceb7ef853bc826f5c3442fa9c90516145a3ab51003053d268a1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putApplyServerSideEncryptionByDefault")
    def put_apply_server_side_encryption_by_default(
        self,
        *,
        sse_algorithm: builtins.str,
        kms_master_key_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param sse_algorithm: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#sse_algorithm S3Bucket#sse_algorithm}.
        :param kms_master_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#kms_master_key_id S3Bucket#kms_master_key_id}.
        '''
        value = S3BucketServerSideEncryptionConfigurationRuleApplyServerSideEncryptionByDefault(
            sse_algorithm=sse_algorithm, kms_master_key_id=kms_master_key_id
        )

        return typing.cast(None, jsii.invoke(self, "putApplyServerSideEncryptionByDefault", [value]))

    @jsii.member(jsii_name="resetBucketKeyEnabled")
    def reset_bucket_key_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketKeyEnabled", []))

    @builtins.property
    @jsii.member(jsii_name="applyServerSideEncryptionByDefault")
    def apply_server_side_encryption_by_default(
        self,
    ) -> S3BucketServerSideEncryptionConfigurationRuleApplyServerSideEncryptionByDefaultOutputReference:
        return typing.cast(S3BucketServerSideEncryptionConfigurationRuleApplyServerSideEncryptionByDefaultOutputReference, jsii.get(self, "applyServerSideEncryptionByDefault"))

    @builtins.property
    @jsii.member(jsii_name="applyServerSideEncryptionByDefaultInput")
    def apply_server_side_encryption_by_default_input(
        self,
    ) -> typing.Optional[S3BucketServerSideEncryptionConfigurationRuleApplyServerSideEncryptionByDefault]:
        return typing.cast(typing.Optional[S3BucketServerSideEncryptionConfigurationRuleApplyServerSideEncryptionByDefault], jsii.get(self, "applyServerSideEncryptionByDefaultInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketKeyEnabledInput")
    def bucket_key_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "bucketKeyEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketKeyEnabled")
    def bucket_key_enabled(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "bucketKeyEnabled"))

    @bucket_key_enabled.setter
    def bucket_key_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8be9a8e236f74967494dcd4232c6246b6db73c4e1231f95c1e5b1d9ced06c6c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketKeyEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3BucketServerSideEncryptionConfigurationRule]:
        return typing.cast(typing.Optional[S3BucketServerSideEncryptionConfigurationRule], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3BucketServerSideEncryptionConfigurationRule],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6b37620c8432d089100580bd326740144cddb2b1a79d7cedc24ff2358b838b9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.s3Bucket.S3BucketTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class S3BucketTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#create S3Bucket#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#delete S3Bucket#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#read S3Bucket#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#update S3Bucket#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ef2b61b399f0a7eae1c724ef8f53d49ce1e0c89265e29dc357133cd3b947ea9)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument read", value=read, expected_type=type_hints["read"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if read is not None:
            self._values["read"] = read
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#create S3Bucket#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#delete S3Bucket#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#read S3Bucket#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#update S3Bucket#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3BucketTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3Bucket.S3BucketTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e18cf0adc4f280107e06a694001823ca17b0fde086b19b07e5d0ab8de46ad0bc)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @jsii.member(jsii_name="resetRead")
    def reset_read(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRead", []))

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
    @jsii.member(jsii_name="readInput")
    def read_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "readInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__747aa465726ad68ab4b78df43966707a04f38546c44822418292ec528cd9cf20)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79edcd8e9aa319f5646fc9bb47c27b8363e7ed0bfd27b1abcc9722d00ea03dbd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__611899cad83e4bc295fcb336af846114deda93391600278f766b5c28edff745e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__22b2a424cb2e73416b34769ce344efd456644691ae048adeb93ea4749758bca2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[S3BucketTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[S3BucketTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[S3BucketTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__373bd13115554647b378f57a7b53da0c3a842c824ff358d1a4993482f24d8fd4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.s3Bucket.S3BucketVersioning",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "mfa_delete": "mfaDelete"},
)
class S3BucketVersioning:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        mfa_delete: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#enabled S3Bucket#enabled}.
        :param mfa_delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#mfa_delete S3Bucket#mfa_delete}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__deed5fb6619c87e559fd02faf471ddb1941c0d921b7ee52c7703f4beb5d2a0c4)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument mfa_delete", value=mfa_delete, expected_type=type_hints["mfa_delete"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled
        if mfa_delete is not None:
            self._values["mfa_delete"] = mfa_delete

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#enabled S3Bucket#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def mfa_delete(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#mfa_delete S3Bucket#mfa_delete}.'''
        result = self._values.get("mfa_delete")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketVersioning(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3BucketVersioningOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3Bucket.S3BucketVersioningOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f0a8f036a4745d0c98345b8dc98cb7dcfc7f313920b61dce33595609301afaa9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetMfaDelete")
    def reset_mfa_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMfaDelete", []))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="mfaDeleteInput")
    def mfa_delete_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "mfaDeleteInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__73641170eadfde24aa55b13bbb07782532ff0093db2841972926774539b4774c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="mfaDelete")
    def mfa_delete(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "mfaDelete"))

    @mfa_delete.setter
    def mfa_delete(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bfea9f490b89708f8654554e6b521a784a088c20beeaa6bb7af98e671cf0e577)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mfaDelete", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[S3BucketVersioning]:
        return typing.cast(typing.Optional[S3BucketVersioning], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[S3BucketVersioning]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e496bfeb4d2f20a3dfc8df002e4f254b7d479205b86b7c6c071e89de5c51749)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.s3Bucket.S3BucketWebsite",
    jsii_struct_bases=[],
    name_mapping={
        "error_document": "errorDocument",
        "index_document": "indexDocument",
        "redirect_all_requests_to": "redirectAllRequestsTo",
        "routing_rules": "routingRules",
    },
)
class S3BucketWebsite:
    def __init__(
        self,
        *,
        error_document: typing.Optional[builtins.str] = None,
        index_document: typing.Optional[builtins.str] = None,
        redirect_all_requests_to: typing.Optional[builtins.str] = None,
        routing_rules: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param error_document: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#error_document S3Bucket#error_document}.
        :param index_document: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#index_document S3Bucket#index_document}.
        :param redirect_all_requests_to: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#redirect_all_requests_to S3Bucket#redirect_all_requests_to}.
        :param routing_rules: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#routing_rules S3Bucket#routing_rules}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__baab272a902534e3fbaca09c0ff3a305b46761a941d26941ee4cf329f48facaf)
            check_type(argname="argument error_document", value=error_document, expected_type=type_hints["error_document"])
            check_type(argname="argument index_document", value=index_document, expected_type=type_hints["index_document"])
            check_type(argname="argument redirect_all_requests_to", value=redirect_all_requests_to, expected_type=type_hints["redirect_all_requests_to"])
            check_type(argname="argument routing_rules", value=routing_rules, expected_type=type_hints["routing_rules"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if error_document is not None:
            self._values["error_document"] = error_document
        if index_document is not None:
            self._values["index_document"] = index_document
        if redirect_all_requests_to is not None:
            self._values["redirect_all_requests_to"] = redirect_all_requests_to
        if routing_rules is not None:
            self._values["routing_rules"] = routing_rules

    @builtins.property
    def error_document(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#error_document S3Bucket#error_document}.'''
        result = self._values.get("error_document")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def index_document(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#index_document S3Bucket#index_document}.'''
        result = self._values.get("index_document")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def redirect_all_requests_to(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#redirect_all_requests_to S3Bucket#redirect_all_requests_to}.'''
        result = self._values.get("redirect_all_requests_to")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def routing_rules(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket#routing_rules S3Bucket#routing_rules}.'''
        result = self._values.get("routing_rules")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketWebsite(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3BucketWebsiteOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3Bucket.S3BucketWebsiteOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8ddef3c1ae3f99c59e178833c751f1762ed832dce9ae036c19e5beda00a7f011)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetErrorDocument")
    def reset_error_document(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetErrorDocument", []))

    @jsii.member(jsii_name="resetIndexDocument")
    def reset_index_document(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIndexDocument", []))

    @jsii.member(jsii_name="resetRedirectAllRequestsTo")
    def reset_redirect_all_requests_to(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedirectAllRequestsTo", []))

    @jsii.member(jsii_name="resetRoutingRules")
    def reset_routing_rules(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRoutingRules", []))

    @builtins.property
    @jsii.member(jsii_name="errorDocumentInput")
    def error_document_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "errorDocumentInput"))

    @builtins.property
    @jsii.member(jsii_name="indexDocumentInput")
    def index_document_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "indexDocumentInput"))

    @builtins.property
    @jsii.member(jsii_name="redirectAllRequestsToInput")
    def redirect_all_requests_to_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "redirectAllRequestsToInput"))

    @builtins.property
    @jsii.member(jsii_name="routingRulesInput")
    def routing_rules_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "routingRulesInput"))

    @builtins.property
    @jsii.member(jsii_name="errorDocument")
    def error_document(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "errorDocument"))

    @error_document.setter
    def error_document(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__635cf0d562b32d83d55dbe0a3686aaba3f1e9b3378e349a572b6656b1fda425b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "errorDocument", value)

    @builtins.property
    @jsii.member(jsii_name="indexDocument")
    def index_document(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "indexDocument"))

    @index_document.setter
    def index_document(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91e3f15be42665ae13fddc3044ddbb3c239e0de66ca0cc86b01e9e627562a536)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "indexDocument", value)

    @builtins.property
    @jsii.member(jsii_name="redirectAllRequestsTo")
    def redirect_all_requests_to(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "redirectAllRequestsTo"))

    @redirect_all_requests_to.setter
    def redirect_all_requests_to(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3268cb6be684c20fc86371db785b78c613db73a5d718b1ba1d4bbdf153eec270)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redirectAllRequestsTo", value)

    @builtins.property
    @jsii.member(jsii_name="routingRules")
    def routing_rules(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "routingRules"))

    @routing_rules.setter
    def routing_rules(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__879a37cc57b33c619adaffe80b9470702a994ae8e6410dc2bcfd66b4dabffe47)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "routingRules", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[S3BucketWebsite]:
        return typing.cast(typing.Optional[S3BucketWebsite], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[S3BucketWebsite]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59f30a146f04d229e6198adfe2c6ede8aa09cc122d2f521b52f5f18a3bc55869)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "S3Bucket",
    "S3BucketConfig",
    "S3BucketCorsRule",
    "S3BucketCorsRuleList",
    "S3BucketCorsRuleOutputReference",
    "S3BucketGrant",
    "S3BucketGrantList",
    "S3BucketGrantOutputReference",
    "S3BucketLifecycleRule",
    "S3BucketLifecycleRuleExpiration",
    "S3BucketLifecycleRuleExpirationOutputReference",
    "S3BucketLifecycleRuleList",
    "S3BucketLifecycleRuleNoncurrentVersionExpiration",
    "S3BucketLifecycleRuleNoncurrentVersionExpirationOutputReference",
    "S3BucketLifecycleRuleNoncurrentVersionTransition",
    "S3BucketLifecycleRuleNoncurrentVersionTransitionList",
    "S3BucketLifecycleRuleNoncurrentVersionTransitionOutputReference",
    "S3BucketLifecycleRuleOutputReference",
    "S3BucketLifecycleRuleTransition",
    "S3BucketLifecycleRuleTransitionList",
    "S3BucketLifecycleRuleTransitionOutputReference",
    "S3BucketLogging",
    "S3BucketLoggingOutputReference",
    "S3BucketObjectLockConfiguration",
    "S3BucketObjectLockConfigurationOutputReference",
    "S3BucketObjectLockConfigurationRule",
    "S3BucketObjectLockConfigurationRuleDefaultRetention",
    "S3BucketObjectLockConfigurationRuleDefaultRetentionOutputReference",
    "S3BucketObjectLockConfigurationRuleOutputReference",
    "S3BucketReplicationConfiguration",
    "S3BucketReplicationConfigurationOutputReference",
    "S3BucketReplicationConfigurationRules",
    "S3BucketReplicationConfigurationRulesDestination",
    "S3BucketReplicationConfigurationRulesDestinationAccessControlTranslation",
    "S3BucketReplicationConfigurationRulesDestinationAccessControlTranslationOutputReference",
    "S3BucketReplicationConfigurationRulesDestinationMetrics",
    "S3BucketReplicationConfigurationRulesDestinationMetricsOutputReference",
    "S3BucketReplicationConfigurationRulesDestinationOutputReference",
    "S3BucketReplicationConfigurationRulesDestinationReplicationTime",
    "S3BucketReplicationConfigurationRulesDestinationReplicationTimeOutputReference",
    "S3BucketReplicationConfigurationRulesFilter",
    "S3BucketReplicationConfigurationRulesFilterOutputReference",
    "S3BucketReplicationConfigurationRulesList",
    "S3BucketReplicationConfigurationRulesOutputReference",
    "S3BucketReplicationConfigurationRulesSourceSelectionCriteria",
    "S3BucketReplicationConfigurationRulesSourceSelectionCriteriaOutputReference",
    "S3BucketReplicationConfigurationRulesSourceSelectionCriteriaSseKmsEncryptedObjects",
    "S3BucketReplicationConfigurationRulesSourceSelectionCriteriaSseKmsEncryptedObjectsOutputReference",
    "S3BucketServerSideEncryptionConfiguration",
    "S3BucketServerSideEncryptionConfigurationOutputReference",
    "S3BucketServerSideEncryptionConfigurationRule",
    "S3BucketServerSideEncryptionConfigurationRuleApplyServerSideEncryptionByDefault",
    "S3BucketServerSideEncryptionConfigurationRuleApplyServerSideEncryptionByDefaultOutputReference",
    "S3BucketServerSideEncryptionConfigurationRuleOutputReference",
    "S3BucketTimeouts",
    "S3BucketTimeoutsOutputReference",
    "S3BucketVersioning",
    "S3BucketVersioningOutputReference",
    "S3BucketWebsite",
    "S3BucketWebsiteOutputReference",
]

publication.publish()

def _typecheckingstub__bc0af23835865888eaefeebdd062e1335ba688f838efccfdd34a608659a14ec9(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    acceleration_status: typing.Optional[builtins.str] = None,
    acl: typing.Optional[builtins.str] = None,
    bucket: typing.Optional[builtins.str] = None,
    bucket_prefix: typing.Optional[builtins.str] = None,
    cors_rule: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[S3BucketCorsRule, typing.Dict[builtins.str, typing.Any]]]]] = None,
    force_destroy: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    grant: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[S3BucketGrant, typing.Dict[builtins.str, typing.Any]]]]] = None,
    id: typing.Optional[builtins.str] = None,
    lifecycle_rule: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[S3BucketLifecycleRule, typing.Dict[builtins.str, typing.Any]]]]] = None,
    logging: typing.Optional[typing.Union[S3BucketLogging, typing.Dict[builtins.str, typing.Any]]] = None,
    object_lock_configuration: typing.Optional[typing.Union[S3BucketObjectLockConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    object_lock_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    policy: typing.Optional[builtins.str] = None,
    replication_configuration: typing.Optional[typing.Union[S3BucketReplicationConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    request_payer: typing.Optional[builtins.str] = None,
    server_side_encryption_configuration: typing.Optional[typing.Union[S3BucketServerSideEncryptionConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[S3BucketTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    versioning: typing.Optional[typing.Union[S3BucketVersioning, typing.Dict[builtins.str, typing.Any]]] = None,
    website: typing.Optional[typing.Union[S3BucketWebsite, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__59443412b46cddd9bd999cb306f49c70c9d537e146e77fc542a4688198d32c81(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[S3BucketCorsRule, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03b333ee3a4a814a21d385853c0daf4f286c73256fe5b38f1fb30fdae05102fd(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[S3BucketGrant, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__138933bc9001d3dbffb393f7c2347e6a6f318eb448906738d9074b977a63b5fc(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[S3BucketLifecycleRule, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f86a908b5f61fe5301087c112b13197c61196eb277daa05f08e36f71d59302cd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b691ae88fc3a0bb0a428a626b4db60a42dae0659012eb63437c56a5cda4a068(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b0d11b5164a927bb74ba02d20713ac625d52ed68c45cd952fda2ef685d447df(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25578cbcb50906c03d22724e79c3b3186414afcacd67b466712b43f31219c669(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aab6eaa55e34658d41fe358da5a5a08dcd824d710cc070026db4eee1fcfb031c(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e7c0822a5575ff0ac4663d817d5ba38c6d393db9319903934cdc7e20fe3a543(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__775edd63cae681a2a9676704cf8232486f5b8138a66dab3489d2b362bb4e049d(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f1366cee0f6ed05e02969a3c0e9f65bd8912a903b50796e3b35647335605e5d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b29097cff1db62f8df0881ac9606872f9a58a722f11c426b05c7a053b6fba80e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6e153b999a7955b6088f7ca7ed267d7ba0c564871eb3abdc281a377da339c25(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d172309882755cf123d3483b899c4753e852bd277e2707cad93efc335d9c69c2(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__777baa4fbb89830b9838d20921e83f4e931ff672e541c19eb83e636a56c39844(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    acceleration_status: typing.Optional[builtins.str] = None,
    acl: typing.Optional[builtins.str] = None,
    bucket: typing.Optional[builtins.str] = None,
    bucket_prefix: typing.Optional[builtins.str] = None,
    cors_rule: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[S3BucketCorsRule, typing.Dict[builtins.str, typing.Any]]]]] = None,
    force_destroy: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    grant: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[S3BucketGrant, typing.Dict[builtins.str, typing.Any]]]]] = None,
    id: typing.Optional[builtins.str] = None,
    lifecycle_rule: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[S3BucketLifecycleRule, typing.Dict[builtins.str, typing.Any]]]]] = None,
    logging: typing.Optional[typing.Union[S3BucketLogging, typing.Dict[builtins.str, typing.Any]]] = None,
    object_lock_configuration: typing.Optional[typing.Union[S3BucketObjectLockConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    object_lock_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    policy: typing.Optional[builtins.str] = None,
    replication_configuration: typing.Optional[typing.Union[S3BucketReplicationConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    request_payer: typing.Optional[builtins.str] = None,
    server_side_encryption_configuration: typing.Optional[typing.Union[S3BucketServerSideEncryptionConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[S3BucketTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    versioning: typing.Optional[typing.Union[S3BucketVersioning, typing.Dict[builtins.str, typing.Any]]] = None,
    website: typing.Optional[typing.Union[S3BucketWebsite, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d82c291e063cbf62727aa6a7b283bb6811e149559594b1a705f784a5736189e1(
    *,
    allowed_methods: typing.Sequence[builtins.str],
    allowed_origins: typing.Sequence[builtins.str],
    allowed_headers: typing.Optional[typing.Sequence[builtins.str]] = None,
    expose_headers: typing.Optional[typing.Sequence[builtins.str]] = None,
    max_age_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a206e3e3ca6b5dd73b3170530501c538382a60e7cfb52982511f6c3fc16968ca(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd82e1e6cb2e09b63680a9bcecae239e308f42543e7afceefab994572d2f8475(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9dcb9ba3711889ed8e6c395d0b0feca8079aea7d91809fd3720182d9453b1ac9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__234559482a15427c82f0f2646b9847e8bd3bbc7e10813600cde0dabe21246cc4(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ed4abd7680f598a86f6a3ce83d39a5145190bbe755d6cbf1fb61153ca0614a6(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5af0657b9022fbd2ac06d532c2b2c73ea48c499a2c55db9f79b9817a85f3f3ae(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[S3BucketCorsRule]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c8415b7dd36ab18e2f0ac039d72561a64d0eeb75ad99a48275038ae8a4d059d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29baa73cc30a148e24705fc274762c557e170e8f29654e3433c6916e1d02d8fb(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79da6f462f3447f0724a89761e02478f84d10c949cc763cac8fa4a2e4addcea9(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5978601fb006d93cf8372978c03a89a27453a23efc8f88073f04f1d435e01018(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67604d72454c9c629847eddaa50c71a120f2a3162cc578d4774ce20931f15ccd(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__107214a50019ba8892f8a0665e0d8ccc5fa8637f08beb852c1827522bf4021f6(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ab4cf6d7306befe88716f5ae060dabf118f73e1ee6105ab239bb46f79c54ed6(
    value: typing.Optional[typing.Union[S3BucketCorsRule, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__604190d5601bce01465b47d4fbf34d343f948c0f1fb9da3c4fea27fcf377d8f6(
    *,
    permissions: typing.Sequence[builtins.str],
    type: builtins.str,
    id: typing.Optional[builtins.str] = None,
    uri: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__932a7d884e9bc8b89ecb8b9132e58c3ab8d31d0b65c8373de1ad64508e3b6f36(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72cdd30de58acfa685a8feb618a1861d420cb2d10776a390cf82a5af9061c706(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c53b6bcf6c062e8823eef3f03637693d9c9920e1aee1e54068169dccfb66fe94(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__caa7cdece3fb0380926c6880ce59c9efa82eb77baf2165a065326876f84f1194(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b781244e3eea82b72372f1405356d94e1adc3d7c94194ad2c7a935a002ce477(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd34c5d1bbb4115e1418a8361409f78954c45d12ae5ed9b4b942bde647aaa9e5(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[S3BucketGrant]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__187d0ebc2ecb26a564a49d189065d81657dad8b7b70d3e427933bf61e47dac86(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7cbb3078b03dd5604ec3e44e93651660a2efe8d837ada4ee9d3c1e1bd5d045c5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5896db6d43b7141014d9444d7dbe1e990ce95bdc6a683dbac5659e3d2c6543a0(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c3b89b43110292cdeaf6223c841f53c922fa34239cc625728e48476710dc46a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__828085b85382d2361f65706a99a85431246cdb8aacd8945988fa4bf1dce46baf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a1333d67f7fb8cddbaeb35f0c8fafc01f20eb871d1ed3c6ab9da25fb74de8d2(
    value: typing.Optional[typing.Union[S3BucketGrant, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80ca1c12fa30c0c5685cf18f87f72b6c279b7e84b5cd4aa550c0116342f3ec29(
    *,
    enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    abort_incomplete_multipart_upload_days: typing.Optional[jsii.Number] = None,
    expiration: typing.Optional[typing.Union[S3BucketLifecycleRuleExpiration, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    noncurrent_version_expiration: typing.Optional[typing.Union[S3BucketLifecycleRuleNoncurrentVersionExpiration, typing.Dict[builtins.str, typing.Any]]] = None,
    noncurrent_version_transition: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[S3BucketLifecycleRuleNoncurrentVersionTransition, typing.Dict[builtins.str, typing.Any]]]]] = None,
    prefix: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    transition: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[S3BucketLifecycleRuleTransition, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__739b7abc821fb43a2bec3af53b209773c21c718fa2eb186aaf6098c139bbf4b5(
    *,
    date: typing.Optional[builtins.str] = None,
    days: typing.Optional[jsii.Number] = None,
    expired_object_delete_marker: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b97ad0bd9009373c3934881985aab2be04f86ed9bf64049413c0259eb724721d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82e14d83b39e33cc6563032cf9658a1cfc01118238e93b752d794c8d2e6534b5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e4f51ed492c71b5e71308e010208a62b12de941b6b5160226c9e33da60888df(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c0013fcc7f0c4398f25c6dd310e331e7d44e4b3a24ec7091d9b39679bc0885d(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0696861c7b7a9b59f3d881eca9d0339234d98044de8a4dcac151c5b5ff86c12(
    value: typing.Optional[S3BucketLifecycleRuleExpiration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bcf331a02d550f6108bc1c40000cd33c9c1b4e5a59605376a35d38da6aa5c881(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0be3aa9de1b3e1af6840c023ea533def8019a6c4fa9a42ac322f3a5a2b708aed(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da0efed52c97ea2725b2170a49214425e9a8491f86ee4764e35c792b4e6a0cfc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8248c68a789b2343ccf56d4db7b6ac59a51ea78e74654ceebd0c5fe278f14977(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96d2c354b906e94afe733ff5cabff5cb64845c2948a772c42c75fdecc28ff03c(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d77207183a354af8fe8dedbb44902e9982891f037ad345c2d84604a771c0218(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[S3BucketLifecycleRule]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__903034d7896a3c427948dc17fb4613c20be0192d06d2c8957c116a97ba9e5063(
    *,
    days: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1c6366f6224013a7c097ad0dfe21f3efe51f285ca507cf66e053aa61add458a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c157e5dab5b03ec6eee4b5d95043418a4145cad7bda8509945e60d93db12067(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54d62c1029fad84a2d63462887acf94555e0c527919e591127cac2fe812215ec(
    value: typing.Optional[S3BucketLifecycleRuleNoncurrentVersionExpiration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a5e87ab248f6a841c2ce169c9b16930e7a6b7934be48671f19c82361896bf22(
    *,
    storage_class: builtins.str,
    days: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a90178b81d679b9562c8a3961a2ae6e62567854e13fb4484965d592b199fa653(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2685a7e0af91d6f6b6ab2bca41205b992e2de838fb747d0a70b20a1c25233c9(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2054e755c6316bb7d493e5784d603d0f176f734478774ee1877466dc5ad0bd6b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44b512a9cb73872f82633e8eeb5ac5bb3d2e595547971ffdc858c26924642dd4(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ea5e413f26d49b1a5f66d2b390cb7e6d7733fba213d9cf3e3f102ff0314951a(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49a293e2faad2c9a177e15d2b4693dfbc884666a449c0cfd1b1133eb22beb4b4(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[S3BucketLifecycleRuleNoncurrentVersionTransition]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95b5fad17d58df6973f64eaa12bdb8aff6834057ae20a793b8a79d2284becf11(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c231974e9e9b0f710ed14a625385a67ff58e900175de3b8182291190a03e7224(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__716545e6476bcdcb54a13699104cb065dadd03ee0ea8bb70fd022094da686430(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__823a9528bee817ad4607a72a954a3fc95f65dabb02e19fc01d2952d10d747b48(
    value: typing.Optional[typing.Union[S3BucketLifecycleRuleNoncurrentVersionTransition, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c589d6ad4c8bd36c49ef549557b8df4f0d255fdba5258e56d343c27ce9644b1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5026cb91f7a324975796adb7d0e7dd11b82da4b76ed91867d4ccadf5b5190462(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[S3BucketLifecycleRuleNoncurrentVersionTransition, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34e1cfdea381841ffde4e198c430a3704c47f2ba409cb129b04b689fb6f8aece(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[S3BucketLifecycleRuleTransition, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd4f9e4fabbc7bfd07e5bbadbe2b1f1cf960a4d32c28eb98aaff019a7cf65596(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc8228e48a97cf79bb818e30d4497c3a04d6f41270813a6ff4b76dc18207f13b(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f8dcdb064b9b8311e711a2dd5d02a0541f2936ce340cbb93c25c2c63ae3732c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f675443676653389d89388f47f38ac3c2d6483d3c4b11145e342cdb1e3d8f41a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd789dcd5f275877282bae90821bd7669b583d946734aa33099ecd869eb10bcf(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad9a49f2b6bd9bcab1ab2b72c8a2f2f965a2a8fcb5956cc28cc4e0cc77d837fc(
    value: typing.Optional[typing.Union[S3BucketLifecycleRule, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c6590efbab9aab57e9492a9e9b6fb43e9a71cae76db80011ec50f261e17bc95(
    *,
    storage_class: builtins.str,
    date: typing.Optional[builtins.str] = None,
    days: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__639d3afa6d2466e93bb451ba1739b0fbe8afa0ebcd80fea31f07a37430a7edac(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a96ab2722432c9e1afedc524ef016cb93513aafd52bfc1d32097d83f8f164ee7(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c4f2ebafd22e1179b610b52e2c4f11b8e26b7afbae91625bd5d6a8a5a394152(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99a6f2d2340a8e978f09967b6747fb86ddcbbc5a38433f8c0af8a96184b7cff2(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9772c3d900667aaeae51df774a2f1aa2003989183f7670f1283206f86512da32(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35142a2641f17fff8c1aef3225411e57430513aa0048764b71f2dd64eccabea0(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[S3BucketLifecycleRuleTransition]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c5d86b2b1a322b21f5ef7d70d45f9f6c09b36d382865e33354d1ec824c72b95(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__751cc72fb7f8edc25e062d8156738e00f9bf894b0e027aeaa09e00e81e74adc7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4be540f17ee9ee3d6d977a129f505a94ac0e6fbfb939fec3e1164029898b1dfa(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44b96ae23d406be0a46043331c9a01cc831cfd321d6c6bfae8f1b1a3257a3768(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b8e5b7021db03e7b22a0d5779d2d99596acc7fc860e66b3b6443282b2175b1f(
    value: typing.Optional[typing.Union[S3BucketLifecycleRuleTransition, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4cf88ff8d9e909681bce96a4b5f7b8eccc1e1321204810d2d5de60de4ef5009(
    *,
    target_bucket: builtins.str,
    target_prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3b3970f3c7bb1ee477520122968eeff00ae66e05e797d55b1fc7ce020e907b9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c173b9fb5a00be883d975d21bdf6256ea281a7f66fe6a599d0d728abc00271a6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6eef86d19833592ef6a07d9b85acad4c2a79ef9bac6926c9e448fd92767de3b2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6cfc62ac8f17908119c81489b6c4d3167d9bd7b07fb2dde07ce00f17360abcad(
    value: typing.Optional[S3BucketLogging],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f76932c8f33bcf0fe3bf3c9dbf7893f66d5451d61b6f0ce156e8b4acbfa63021(
    *,
    object_lock_enabled: typing.Optional[builtins.str] = None,
    rule: typing.Optional[typing.Union[S3BucketObjectLockConfigurationRule, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31a3293cde95a486dc3109980fdcace0d1e05594aee84f60de96d4d5be7910df(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e817890ad0bab6a4f654edd084c7d52281709819f9c2649707022ae4af848a5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__198007cedf585d7fdb5331e52fc6e7a941e6a4830d796c22d1c3ab179a66445e(
    value: typing.Optional[S3BucketObjectLockConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d6cdb3f620734bb921a459901c63632a1e5fff8bd963ee2807d611929615a75(
    *,
    default_retention: typing.Union[S3BucketObjectLockConfigurationRuleDefaultRetention, typing.Dict[builtins.str, typing.Any]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b25aa6e3acfe819ae30fcc0fe79af67a1f2910c9f89aca73f62395f49c437ff4(
    *,
    mode: builtins.str,
    days: typing.Optional[jsii.Number] = None,
    years: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be412b219f1410dc5db2405b6c66ad4404df20eea564f35219bb954b30dcd29a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07b0432cbefb2fdb254e47ece7a90b1e94265833df8c6ba6a58549958e7be61c(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d36dd31459d42c724b2dfd4133cc619239bdfcf0d5fff98233689ee5502afd15(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3fc23c4e91a1ba564673863b5f2a7c37aef33830133a67407c0cfb541e67b461(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3100a4daa6cb1d9184aed19cb886768192627cf76eb3966f4f00785b0cc523db(
    value: typing.Optional[S3BucketObjectLockConfigurationRuleDefaultRetention],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fcd8528593ef15ed52b302299f1e5feac69a18f21979ef9d3e6d14192d3283a0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11d96d322441aa0ce991943b566bed667bdf1afac285e84d1f2e4d0b0ac6f2b7(
    value: typing.Optional[S3BucketObjectLockConfigurationRule],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9942c61c03b74f4b8d2619252b40b0a0252c5f473f7b6bb8b022f1c13f9b0d60(
    *,
    role: builtins.str,
    rules: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[S3BucketReplicationConfigurationRules, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__798ad556d9676da9ab8e95de512ddce8f22f6c09c8dd4b07286ce7bdb3655562(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6863e602734556d192a4c880f166660bd35d2eaadcf0509c3e11cf354294fee(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[S3BucketReplicationConfigurationRules, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f56587c20b4a16b8734bd3c114fd6e9a40ca07baa0ad54d942ad572c921c01ae(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed4c002119ee85c3f79b78c191b6ad413d1e329e9eea74cd9d7ca1b405b58abb(
    value: typing.Optional[S3BucketReplicationConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__142a394731b60110d1f0e43731ceff4058b8f26bbaf1536b100eb85c49787002(
    *,
    destination: typing.Union[S3BucketReplicationConfigurationRulesDestination, typing.Dict[builtins.str, typing.Any]],
    status: builtins.str,
    delete_marker_replication_status: typing.Optional[builtins.str] = None,
    filter: typing.Optional[typing.Union[S3BucketReplicationConfigurationRulesFilter, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    prefix: typing.Optional[builtins.str] = None,
    priority: typing.Optional[jsii.Number] = None,
    source_selection_criteria: typing.Optional[typing.Union[S3BucketReplicationConfigurationRulesSourceSelectionCriteria, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0604e4923062b1932bcc4754a919a6a1caf856811d27a68011de17799aff4dee(
    *,
    bucket: builtins.str,
    access_control_translation: typing.Optional[typing.Union[S3BucketReplicationConfigurationRulesDestinationAccessControlTranslation, typing.Dict[builtins.str, typing.Any]]] = None,
    account_id: typing.Optional[builtins.str] = None,
    metrics: typing.Optional[typing.Union[S3BucketReplicationConfigurationRulesDestinationMetrics, typing.Dict[builtins.str, typing.Any]]] = None,
    replica_kms_key_id: typing.Optional[builtins.str] = None,
    replication_time: typing.Optional[typing.Union[S3BucketReplicationConfigurationRulesDestinationReplicationTime, typing.Dict[builtins.str, typing.Any]]] = None,
    storage_class: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c72f8b37d06ec45eafff55931878f5c1b33db77dbc1ab5a433550a104b7ae553(
    *,
    owner: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3631a6e5973e38ac199cf5e39f5ac094988361bbad8dde46d6214714fd92d917(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a95a00452090773f0f4be0aa60d45965ab6b9a8b9bc19f7c8b9c7ae6b34640a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f06d8971cfc48698e67f56adbe9550abf2b9c948a5247bd9187b4ff97588f6bb(
    value: typing.Optional[S3BucketReplicationConfigurationRulesDestinationAccessControlTranslation],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cdd9ffa63eb759697513e95bae66d7e2b5c1c7725f9250a201ea0f1d5ba9732c(
    *,
    minutes: typing.Optional[jsii.Number] = None,
    status: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9549ab84da8a9df1b9f6ed9bdbe69ef4f8214aeb1a9aca9f52ae020f7d57d3f1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53779ed79b4a4607cb826e0bd7efd7933b291fb921ffc2ea1d0dd3d0cce3652c(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d19ca935975a72bbaf0df37f7ab904328ccc5d001d37a9c20d33b9a51fb5526b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca805597d40bfde2d615d102cffaf546f972d6e5c0ddf1ad0e970ab11e86072e(
    value: typing.Optional[S3BucketReplicationConfigurationRulesDestinationMetrics],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7416447563ecf10627f5219425f2e4117bccfd4e297522fc4858a920c2c723de(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__922fd1635a0059d62c1a02fa10eefe904559ac58630fb52cc27a7b5c15bb53ac(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7999ff358f71e1ad1fe8b21c064ae7583ea1f1e30770a31f01a608bd8b43e390(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3daa0614577da81d17c902b9239318d5af3bb4b14ba9beab8018aeb65a3583bc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c27237eb18c84db2dc341691634cd7f0ac178777d7f988d9d035ed624768ace(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc30a8bdd6c2de79b03b8f0c62b918b4cd4f2313de2a341300e634d9db643686(
    value: typing.Optional[S3BucketReplicationConfigurationRulesDestination],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ce0eb686017296725a6d5b6f03020faae07b36a6e61824cd57e6370770ecfce(
    *,
    minutes: typing.Optional[jsii.Number] = None,
    status: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc3fb0b1de8d86f78aa94c0fb645f88a60f1ebc8f4965b37caf6b1957091ccd0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a617ca7021b18c05c4dafcc1e78c4268c13723bcf4a95ae7a21f460acb9021d6(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8361fbd3b7e9c2fae43cc7c58436e24d7f0cb4b4449cf4addc851c037c1411d3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39ad51207f89c323424be31963f6f27e67dda9a9367c75557d38b983a86b7a6c(
    value: typing.Optional[S3BucketReplicationConfigurationRulesDestinationReplicationTime],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1807a92adcf82027065ffaac6b3ad957f71c4a86e8a478b7e49642c5bd756b43(
    *,
    prefix: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dec4dca82937648ac242e4a16894a03cf7b6155b1aa4ee1b22d667f2053f7bd3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b19fbeddeafb9cd11b68cd48411aaa01174256741fdb1ca8c39c588b2fe738eb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2df72c7f3e4bd43f43ed8bd067e19814acf44a12741178d0d2ada606594cfd35(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d76c80f186df167c7769f877777f3ed4031100ff745f5b10980020d6477154f4(
    value: typing.Optional[S3BucketReplicationConfigurationRulesFilter],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9a20cc3df642cddea702de54dc0ed8eb2fb48c7244dcd7a5e4eef62d43606be(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__739d6487d618e2fed1440f3baa0e4ca70992705efce5c57f68589f5e12478deb(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__acbc81a7ecfd33cd692255d959241ccdfceacf0da456d55a508f48bf13cfc7d2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df3880a40ab9ef96d6108aba1020b531a9e3fc6135919d7ee5580c7febb1ffe3(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5287e3060f918b89d5a527b3e2ea15be93c07df7b3482c7909f720b690e7f75(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9f04f614c64de3aaf23cb2789e4bf38db08c2564fac2edf037e79e52ab97b56(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[S3BucketReplicationConfigurationRules]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b19b20f98177d468c3588eb183c9f27962cb3d9f758bb4f7320999a8424e9b68(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__767a9a376eba0effa3acf738196aade8086a0fc1ab703b97d175698670ce6fb1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3df3bdad95fe1c63208188caaac8870a82df680d1fbfbf28d1c3bd2eb272578(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f22c094e0d83c1b9d091edda9dff6e1d69630d489efa15fca91c9f6041a9b47d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b98d2a97dc16d290f47307a2324b1f6309def1bf3ad167661b652736c56efad7(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b7943b6b8a59a60f6e2013842880f7469d2d5de97d452c037d181936d2b5e9e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6afe5c6932e02888d906aeb5f20bf4e54d39c862746fe06cbc945990db3270d(
    value: typing.Optional[typing.Union[S3BucketReplicationConfigurationRules, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0e14fa81e549a39a3ef152b10d22f7c4155bc8886aefb12e2065dea3b39a648(
    *,
    sse_kms_encrypted_objects: typing.Optional[typing.Union[S3BucketReplicationConfigurationRulesSourceSelectionCriteriaSseKmsEncryptedObjects, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9047b1e067afd5c7198e567df4809c35522ba1cf56d3eea7534a1fc6d91e988(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f30c100e06f1e8e9f78c1160c43c8d051e1731e63f4ace75cb42bbb3704d7e82(
    value: typing.Optional[S3BucketReplicationConfigurationRulesSourceSelectionCriteria],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a24ebfa79bc9f280d43fdd2e611bc29225dd4c10399edd08a5f555974689f3ef(
    *,
    enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bfcc5a8946fb0687b109fc27d0b20760085787d87f3bf5d15bf3327e5900ab71(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0214ffc7cfe71a0d91b58e1ff18147bdd5581e750c02fcaac48ed18be09c7a4c(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a9fde38a79549cf69017ab70f085110e84303d92cc964ca08c726990ec77315(
    value: typing.Optional[S3BucketReplicationConfigurationRulesSourceSelectionCriteriaSseKmsEncryptedObjects],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5bdf50ae47bff19317735c3cc30881d0cfa8fc0c825547a7f87468409f3f8256(
    *,
    rule: typing.Union[S3BucketServerSideEncryptionConfigurationRule, typing.Dict[builtins.str, typing.Any]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e054b213412766682edd074e9404a23f260898ceeb4566a025e7eeece3c5e97(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__beadce034aa87cfaf1de57de368d609b6c46d655047b2349fc44d1398ea1e40f(
    value: typing.Optional[S3BucketServerSideEncryptionConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9d09131272dc42dd40298ba5a585821c7c4c20bbcac0042800daa5c08a414af(
    *,
    apply_server_side_encryption_by_default: typing.Union[S3BucketServerSideEncryptionConfigurationRuleApplyServerSideEncryptionByDefault, typing.Dict[builtins.str, typing.Any]],
    bucket_key_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b543f0775903c35c2e8a07b3860531665754e57fef685c89ff2524b37405dea5(
    *,
    sse_algorithm: builtins.str,
    kms_master_key_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b4b2f628afcf9c9c8027f878bbe2a295648a32056cc2e0b1c9e8ff3b2fd6a98(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af9d078332726f44438fa45cad23e4db0f054f7a7bcddefbbb3a08a1f61e6adb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce7689fe14b5dab723ab473e388b8bbec9b2158676942710ad73fef45581afaf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8216331060c4ec4e4314f451ec1bd12baa9392439a7f5c80a5ef0fabe9ac4339(
    value: typing.Optional[S3BucketServerSideEncryptionConfigurationRuleApplyServerSideEncryptionByDefault],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35a682e36c4b7ceb7ef853bc826f5c3442fa9c90516145a3ab51003053d268a1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8be9a8e236f74967494dcd4232c6246b6db73c4e1231f95c1e5b1d9ced06c6c6(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6b37620c8432d089100580bd326740144cddb2b1a79d7cedc24ff2358b838b9(
    value: typing.Optional[S3BucketServerSideEncryptionConfigurationRule],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ef2b61b399f0a7eae1c724ef8f53d49ce1e0c89265e29dc357133cd3b947ea9(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    read: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e18cf0adc4f280107e06a694001823ca17b0fde086b19b07e5d0ab8de46ad0bc(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__747aa465726ad68ab4b78df43966707a04f38546c44822418292ec528cd9cf20(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79edcd8e9aa319f5646fc9bb47c27b8363e7ed0bfd27b1abcc9722d00ea03dbd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__611899cad83e4bc295fcb336af846114deda93391600278f766b5c28edff745e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22b2a424cb2e73416b34769ce344efd456644691ae048adeb93ea4749758bca2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__373bd13115554647b378f57a7b53da0c3a842c824ff358d1a4993482f24d8fd4(
    value: typing.Optional[typing.Union[S3BucketTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__deed5fb6619c87e559fd02faf471ddb1941c0d921b7ee52c7703f4beb5d2a0c4(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    mfa_delete: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0a8f036a4745d0c98345b8dc98cb7dcfc7f313920b61dce33595609301afaa9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73641170eadfde24aa55b13bbb07782532ff0093db2841972926774539b4774c(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bfea9f490b89708f8654554e6b521a784a088c20beeaa6bb7af98e671cf0e577(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e496bfeb4d2f20a3dfc8df002e4f254b7d479205b86b7c6c071e89de5c51749(
    value: typing.Optional[S3BucketVersioning],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__baab272a902534e3fbaca09c0ff3a305b46761a941d26941ee4cf329f48facaf(
    *,
    error_document: typing.Optional[builtins.str] = None,
    index_document: typing.Optional[builtins.str] = None,
    redirect_all_requests_to: typing.Optional[builtins.str] = None,
    routing_rules: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ddef3c1ae3f99c59e178833c751f1762ed832dce9ae036c19e5beda00a7f011(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__635cf0d562b32d83d55dbe0a3686aaba3f1e9b3378e349a572b6656b1fda425b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91e3f15be42665ae13fddc3044ddbb3c239e0de66ca0cc86b01e9e627562a536(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3268cb6be684c20fc86371db785b78c613db73a5d718b1ba1d4bbdf153eec270(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__879a37cc57b33c619adaffe80b9470702a994ae8e6410dc2bcfd66b4dabffe47(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59f30a146f04d229e6198adfe2c6ede8aa09cc122d2f521b52f5f18a3bc55869(
    value: typing.Optional[S3BucketWebsite],
) -> None:
    """Type checking stubs"""
    pass
