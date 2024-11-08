'''
# `aws_s3_bucket_lifecycle_configuration`

Refer to the Terraform Registory for docs: [`aws_s3_bucket_lifecycle_configuration`](https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration).
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


class S3BucketLifecycleConfiguration(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3BucketLifecycleConfiguration.S3BucketLifecycleConfiguration",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration aws_s3_bucket_lifecycle_configuration}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        bucket: builtins.str,
        rule: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["S3BucketLifecycleConfigurationRule", typing.Dict[builtins.str, typing.Any]]]],
        expected_bucket_owner: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration aws_s3_bucket_lifecycle_configuration} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#bucket S3BucketLifecycleConfiguration#bucket}.
        :param rule: rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#rule S3BucketLifecycleConfiguration#rule}
        :param expected_bucket_owner: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#expected_bucket_owner S3BucketLifecycleConfiguration#expected_bucket_owner}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#id S3BucketLifecycleConfiguration#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db24ff7d5d15a31afa7223abd24a8e67b2a6d3b6c93ee39d1723830fe9e41652)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = S3BucketLifecycleConfigurationConfig(
            bucket=bucket,
            rule=rule,
            expected_bucket_owner=expected_bucket_owner,
            id=id,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putRule")
    def put_rule(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["S3BucketLifecycleConfigurationRule", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef126be78300ce8d6548ec18ae342ea56ba640beb4939573d63eb19bc5561327)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRule", [value]))

    @jsii.member(jsii_name="resetExpectedBucketOwner")
    def reset_expected_bucket_owner(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExpectedBucketOwner", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="rule")
    def rule(self) -> "S3BucketLifecycleConfigurationRuleList":
        return typing.cast("S3BucketLifecycleConfigurationRuleList", jsii.get(self, "rule"))

    @builtins.property
    @jsii.member(jsii_name="bucketInput")
    def bucket_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketInput"))

    @builtins.property
    @jsii.member(jsii_name="expectedBucketOwnerInput")
    def expected_bucket_owner_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "expectedBucketOwnerInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleInput")
    def rule_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["S3BucketLifecycleConfigurationRule"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["S3BucketLifecycleConfigurationRule"]]], jsii.get(self, "ruleInput"))

    @builtins.property
    @jsii.member(jsii_name="bucket")
    def bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucket"))

    @bucket.setter
    def bucket(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5c574db07cf41a685c8ee528734d9b88836516a91b2b78b1c9aa212adcb6a8a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucket", value)

    @builtins.property
    @jsii.member(jsii_name="expectedBucketOwner")
    def expected_bucket_owner(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expectedBucketOwner"))

    @expected_bucket_owner.setter
    def expected_bucket_owner(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38908fbe40beebff95afe525931dc881ee84b4330299e310559139620b86051f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expectedBucketOwner", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9463016f07ddffdf3a637d60e26f07056c514f047eb57d3d78b7dcf66822384e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)


@jsii.data_type(
    jsii_type="aws.s3BucketLifecycleConfiguration.S3BucketLifecycleConfigurationConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "bucket": "bucket",
        "rule": "rule",
        "expected_bucket_owner": "expectedBucketOwner",
        "id": "id",
    },
)
class S3BucketLifecycleConfigurationConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        bucket: builtins.str,
        rule: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["S3BucketLifecycleConfigurationRule", typing.Dict[builtins.str, typing.Any]]]],
        expected_bucket_owner: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#bucket S3BucketLifecycleConfiguration#bucket}.
        :param rule: rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#rule S3BucketLifecycleConfiguration#rule}
        :param expected_bucket_owner: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#expected_bucket_owner S3BucketLifecycleConfiguration#expected_bucket_owner}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#id S3BucketLifecycleConfiguration#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a45af29c28739881fe73b7bab967228c72d4abd7f8ad70f503620bfb41de6371)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
            check_type(argname="argument expected_bucket_owner", value=expected_bucket_owner, expected_type=type_hints["expected_bucket_owner"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bucket": bucket,
            "rule": rule,
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
        if expected_bucket_owner is not None:
            self._values["expected_bucket_owner"] = expected_bucket_owner
        if id is not None:
            self._values["id"] = id

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
    def bucket(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#bucket S3BucketLifecycleConfiguration#bucket}.'''
        result = self._values.get("bucket")
        assert result is not None, "Required property 'bucket' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rule(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["S3BucketLifecycleConfigurationRule"]]:
        '''rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#rule S3BucketLifecycleConfiguration#rule}
        '''
        result = self._values.get("rule")
        assert result is not None, "Required property 'rule' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["S3BucketLifecycleConfigurationRule"]], result)

    @builtins.property
    def expected_bucket_owner(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#expected_bucket_owner S3BucketLifecycleConfiguration#expected_bucket_owner}.'''
        result = self._values.get("expected_bucket_owner")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#id S3BucketLifecycleConfiguration#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketLifecycleConfigurationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.s3BucketLifecycleConfiguration.S3BucketLifecycleConfigurationRule",
    jsii_struct_bases=[],
    name_mapping={
        "id": "id",
        "status": "status",
        "abort_incomplete_multipart_upload": "abortIncompleteMultipartUpload",
        "expiration": "expiration",
        "filter": "filter",
        "noncurrent_version_expiration": "noncurrentVersionExpiration",
        "noncurrent_version_transition": "noncurrentVersionTransition",
        "prefix": "prefix",
        "transition": "transition",
    },
)
class S3BucketLifecycleConfigurationRule:
    def __init__(
        self,
        *,
        id: builtins.str,
        status: builtins.str,
        abort_incomplete_multipart_upload: typing.Optional[typing.Union["S3BucketLifecycleConfigurationRuleAbortIncompleteMultipartUpload", typing.Dict[builtins.str, typing.Any]]] = None,
        expiration: typing.Optional[typing.Union["S3BucketLifecycleConfigurationRuleExpiration", typing.Dict[builtins.str, typing.Any]]] = None,
        filter: typing.Optional[typing.Union["S3BucketLifecycleConfigurationRuleFilter", typing.Dict[builtins.str, typing.Any]]] = None,
        noncurrent_version_expiration: typing.Optional[typing.Union["S3BucketLifecycleConfigurationRuleNoncurrentVersionExpiration", typing.Dict[builtins.str, typing.Any]]] = None,
        noncurrent_version_transition: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["S3BucketLifecycleConfigurationRuleNoncurrentVersionTransition", typing.Dict[builtins.str, typing.Any]]]]] = None,
        prefix: typing.Optional[builtins.str] = None,
        transition: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["S3BucketLifecycleConfigurationRuleTransition", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#id S3BucketLifecycleConfiguration#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#status S3BucketLifecycleConfiguration#status}.
        :param abort_incomplete_multipart_upload: abort_incomplete_multipart_upload block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#abort_incomplete_multipart_upload S3BucketLifecycleConfiguration#abort_incomplete_multipart_upload}
        :param expiration: expiration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#expiration S3BucketLifecycleConfiguration#expiration}
        :param filter: filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#filter S3BucketLifecycleConfiguration#filter}
        :param noncurrent_version_expiration: noncurrent_version_expiration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#noncurrent_version_expiration S3BucketLifecycleConfiguration#noncurrent_version_expiration}
        :param noncurrent_version_transition: noncurrent_version_transition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#noncurrent_version_transition S3BucketLifecycleConfiguration#noncurrent_version_transition}
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#prefix S3BucketLifecycleConfiguration#prefix}.
        :param transition: transition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#transition S3BucketLifecycleConfiguration#transition}
        '''
        if isinstance(abort_incomplete_multipart_upload, dict):
            abort_incomplete_multipart_upload = S3BucketLifecycleConfigurationRuleAbortIncompleteMultipartUpload(**abort_incomplete_multipart_upload)
        if isinstance(expiration, dict):
            expiration = S3BucketLifecycleConfigurationRuleExpiration(**expiration)
        if isinstance(filter, dict):
            filter = S3BucketLifecycleConfigurationRuleFilter(**filter)
        if isinstance(noncurrent_version_expiration, dict):
            noncurrent_version_expiration = S3BucketLifecycleConfigurationRuleNoncurrentVersionExpiration(**noncurrent_version_expiration)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__968920fab5956d1b562f411f3f4d2594bca2a3323bffc30d789923b217671ed8)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            check_type(argname="argument abort_incomplete_multipart_upload", value=abort_incomplete_multipart_upload, expected_type=type_hints["abort_incomplete_multipart_upload"])
            check_type(argname="argument expiration", value=expiration, expected_type=type_hints["expiration"])
            check_type(argname="argument filter", value=filter, expected_type=type_hints["filter"])
            check_type(argname="argument noncurrent_version_expiration", value=noncurrent_version_expiration, expected_type=type_hints["noncurrent_version_expiration"])
            check_type(argname="argument noncurrent_version_transition", value=noncurrent_version_transition, expected_type=type_hints["noncurrent_version_transition"])
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
            check_type(argname="argument transition", value=transition, expected_type=type_hints["transition"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "id": id,
            "status": status,
        }
        if abort_incomplete_multipart_upload is not None:
            self._values["abort_incomplete_multipart_upload"] = abort_incomplete_multipart_upload
        if expiration is not None:
            self._values["expiration"] = expiration
        if filter is not None:
            self._values["filter"] = filter
        if noncurrent_version_expiration is not None:
            self._values["noncurrent_version_expiration"] = noncurrent_version_expiration
        if noncurrent_version_transition is not None:
            self._values["noncurrent_version_transition"] = noncurrent_version_transition
        if prefix is not None:
            self._values["prefix"] = prefix
        if transition is not None:
            self._values["transition"] = transition

    @builtins.property
    def id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#id S3BucketLifecycleConfiguration#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def status(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#status S3BucketLifecycleConfiguration#status}.'''
        result = self._values.get("status")
        assert result is not None, "Required property 'status' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def abort_incomplete_multipart_upload(
        self,
    ) -> typing.Optional["S3BucketLifecycleConfigurationRuleAbortIncompleteMultipartUpload"]:
        '''abort_incomplete_multipart_upload block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#abort_incomplete_multipart_upload S3BucketLifecycleConfiguration#abort_incomplete_multipart_upload}
        '''
        result = self._values.get("abort_incomplete_multipart_upload")
        return typing.cast(typing.Optional["S3BucketLifecycleConfigurationRuleAbortIncompleteMultipartUpload"], result)

    @builtins.property
    def expiration(
        self,
    ) -> typing.Optional["S3BucketLifecycleConfigurationRuleExpiration"]:
        '''expiration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#expiration S3BucketLifecycleConfiguration#expiration}
        '''
        result = self._values.get("expiration")
        return typing.cast(typing.Optional["S3BucketLifecycleConfigurationRuleExpiration"], result)

    @builtins.property
    def filter(self) -> typing.Optional["S3BucketLifecycleConfigurationRuleFilter"]:
        '''filter block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#filter S3BucketLifecycleConfiguration#filter}
        '''
        result = self._values.get("filter")
        return typing.cast(typing.Optional["S3BucketLifecycleConfigurationRuleFilter"], result)

    @builtins.property
    def noncurrent_version_expiration(
        self,
    ) -> typing.Optional["S3BucketLifecycleConfigurationRuleNoncurrentVersionExpiration"]:
        '''noncurrent_version_expiration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#noncurrent_version_expiration S3BucketLifecycleConfiguration#noncurrent_version_expiration}
        '''
        result = self._values.get("noncurrent_version_expiration")
        return typing.cast(typing.Optional["S3BucketLifecycleConfigurationRuleNoncurrentVersionExpiration"], result)

    @builtins.property
    def noncurrent_version_transition(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["S3BucketLifecycleConfigurationRuleNoncurrentVersionTransition"]]]:
        '''noncurrent_version_transition block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#noncurrent_version_transition S3BucketLifecycleConfiguration#noncurrent_version_transition}
        '''
        result = self._values.get("noncurrent_version_transition")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["S3BucketLifecycleConfigurationRuleNoncurrentVersionTransition"]]], result)

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#prefix S3BucketLifecycleConfiguration#prefix}.'''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def transition(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["S3BucketLifecycleConfigurationRuleTransition"]]]:
        '''transition block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#transition S3BucketLifecycleConfiguration#transition}
        '''
        result = self._values.get("transition")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["S3BucketLifecycleConfigurationRuleTransition"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketLifecycleConfigurationRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.s3BucketLifecycleConfiguration.S3BucketLifecycleConfigurationRuleAbortIncompleteMultipartUpload",
    jsii_struct_bases=[],
    name_mapping={"days_after_initiation": "daysAfterInitiation"},
)
class S3BucketLifecycleConfigurationRuleAbortIncompleteMultipartUpload:
    def __init__(
        self,
        *,
        days_after_initiation: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param days_after_initiation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#days_after_initiation S3BucketLifecycleConfiguration#days_after_initiation}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f86b7c99c1f9cbc877252ffd1805af6bff7b6603c6d6f14c0734050ed87a1e41)
            check_type(argname="argument days_after_initiation", value=days_after_initiation, expected_type=type_hints["days_after_initiation"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if days_after_initiation is not None:
            self._values["days_after_initiation"] = days_after_initiation

    @builtins.property
    def days_after_initiation(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#days_after_initiation S3BucketLifecycleConfiguration#days_after_initiation}.'''
        result = self._values.get("days_after_initiation")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketLifecycleConfigurationRuleAbortIncompleteMultipartUpload(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3BucketLifecycleConfigurationRuleAbortIncompleteMultipartUploadOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3BucketLifecycleConfiguration.S3BucketLifecycleConfigurationRuleAbortIncompleteMultipartUploadOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7ce65fc9eae34c2f3db982dced008e8b7378fccfc9d88d49df89809e15fb4f32)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDaysAfterInitiation")
    def reset_days_after_initiation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDaysAfterInitiation", []))

    @builtins.property
    @jsii.member(jsii_name="daysAfterInitiationInput")
    def days_after_initiation_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "daysAfterInitiationInput"))

    @builtins.property
    @jsii.member(jsii_name="daysAfterInitiation")
    def days_after_initiation(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "daysAfterInitiation"))

    @days_after_initiation.setter
    def days_after_initiation(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b720c16b317f227dbe9835eae86243112a939b9373afca567658cd5fba61d6e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "daysAfterInitiation", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3BucketLifecycleConfigurationRuleAbortIncompleteMultipartUpload]:
        return typing.cast(typing.Optional[S3BucketLifecycleConfigurationRuleAbortIncompleteMultipartUpload], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3BucketLifecycleConfigurationRuleAbortIncompleteMultipartUpload],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a6cfa593ce3e28ea09fde9eb3842e758aaa4eb998bc422c47a1e28de85a7239)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.s3BucketLifecycleConfiguration.S3BucketLifecycleConfigurationRuleExpiration",
    jsii_struct_bases=[],
    name_mapping={
        "date": "date",
        "days": "days",
        "expired_object_delete_marker": "expiredObjectDeleteMarker",
    },
)
class S3BucketLifecycleConfigurationRuleExpiration:
    def __init__(
        self,
        *,
        date: typing.Optional[builtins.str] = None,
        days: typing.Optional[jsii.Number] = None,
        expired_object_delete_marker: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param date: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#date S3BucketLifecycleConfiguration#date}.
        :param days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#days S3BucketLifecycleConfiguration#days}.
        :param expired_object_delete_marker: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#expired_object_delete_marker S3BucketLifecycleConfiguration#expired_object_delete_marker}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aff495db03d5b067b48f71d3941a7435a6e91d45c09f927e939419d36ea6f67b)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#date S3BucketLifecycleConfiguration#date}.'''
        result = self._values.get("date")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def days(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#days S3BucketLifecycleConfiguration#days}.'''
        result = self._values.get("days")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def expired_object_delete_marker(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#expired_object_delete_marker S3BucketLifecycleConfiguration#expired_object_delete_marker}.'''
        result = self._values.get("expired_object_delete_marker")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketLifecycleConfigurationRuleExpiration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3BucketLifecycleConfigurationRuleExpirationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3BucketLifecycleConfiguration.S3BucketLifecycleConfigurationRuleExpirationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7b6e82ceaa273d3b1746534326ffb9e3ea6986e082033fdb60b8d0106c301b3e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__07cd3dd547af324ce341b80c782dfc2bfc933e96aae4e097cfb55796fcf4835f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "date", value)

    @builtins.property
    @jsii.member(jsii_name="days")
    def days(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "days"))

    @days.setter
    def days(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89ce2c52c9ff7d5f201eee3df1d800f9a9e41830298e34edd41fb7887ce1d2f9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__681c210d4f284b06de6416deffb11566729a82c160c05a96a40a57938cc68586)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expiredObjectDeleteMarker", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3BucketLifecycleConfigurationRuleExpiration]:
        return typing.cast(typing.Optional[S3BucketLifecycleConfigurationRuleExpiration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3BucketLifecycleConfigurationRuleExpiration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__413328a20de4196832e7c63767f0367d5b04b58a124e5aa82a0cb5711f2ae5ff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.s3BucketLifecycleConfiguration.S3BucketLifecycleConfigurationRuleFilter",
    jsii_struct_bases=[],
    name_mapping={
        "and_": "and",
        "object_size_greater_than": "objectSizeGreaterThan",
        "object_size_less_than": "objectSizeLessThan",
        "prefix": "prefix",
        "tag": "tag",
    },
)
class S3BucketLifecycleConfigurationRuleFilter:
    def __init__(
        self,
        *,
        and_: typing.Optional[typing.Union["S3BucketLifecycleConfigurationRuleFilterAnd", typing.Dict[builtins.str, typing.Any]]] = None,
        object_size_greater_than: typing.Optional[builtins.str] = None,
        object_size_less_than: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
        tag: typing.Optional[typing.Union["S3BucketLifecycleConfigurationRuleFilterTag", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param and_: and block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#and S3BucketLifecycleConfiguration#and}
        :param object_size_greater_than: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#object_size_greater_than S3BucketLifecycleConfiguration#object_size_greater_than}.
        :param object_size_less_than: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#object_size_less_than S3BucketLifecycleConfiguration#object_size_less_than}.
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#prefix S3BucketLifecycleConfiguration#prefix}.
        :param tag: tag block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#tag S3BucketLifecycleConfiguration#tag}
        '''
        if isinstance(and_, dict):
            and_ = S3BucketLifecycleConfigurationRuleFilterAnd(**and_)
        if isinstance(tag, dict):
            tag = S3BucketLifecycleConfigurationRuleFilterTag(**tag)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb9ebb81cff0e4929a668999c5448b4664a862cebd49ee8ebdb3276c385a1864)
            check_type(argname="argument and_", value=and_, expected_type=type_hints["and_"])
            check_type(argname="argument object_size_greater_than", value=object_size_greater_than, expected_type=type_hints["object_size_greater_than"])
            check_type(argname="argument object_size_less_than", value=object_size_less_than, expected_type=type_hints["object_size_less_than"])
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
            check_type(argname="argument tag", value=tag, expected_type=type_hints["tag"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if and_ is not None:
            self._values["and_"] = and_
        if object_size_greater_than is not None:
            self._values["object_size_greater_than"] = object_size_greater_than
        if object_size_less_than is not None:
            self._values["object_size_less_than"] = object_size_less_than
        if prefix is not None:
            self._values["prefix"] = prefix
        if tag is not None:
            self._values["tag"] = tag

    @builtins.property
    def and_(self) -> typing.Optional["S3BucketLifecycleConfigurationRuleFilterAnd"]:
        '''and block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#and S3BucketLifecycleConfiguration#and}
        '''
        result = self._values.get("and_")
        return typing.cast(typing.Optional["S3BucketLifecycleConfigurationRuleFilterAnd"], result)

    @builtins.property
    def object_size_greater_than(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#object_size_greater_than S3BucketLifecycleConfiguration#object_size_greater_than}.'''
        result = self._values.get("object_size_greater_than")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def object_size_less_than(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#object_size_less_than S3BucketLifecycleConfiguration#object_size_less_than}.'''
        result = self._values.get("object_size_less_than")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#prefix S3BucketLifecycleConfiguration#prefix}.'''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tag(self) -> typing.Optional["S3BucketLifecycleConfigurationRuleFilterTag"]:
        '''tag block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#tag S3BucketLifecycleConfiguration#tag}
        '''
        result = self._values.get("tag")
        return typing.cast(typing.Optional["S3BucketLifecycleConfigurationRuleFilterTag"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketLifecycleConfigurationRuleFilter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.s3BucketLifecycleConfiguration.S3BucketLifecycleConfigurationRuleFilterAnd",
    jsii_struct_bases=[],
    name_mapping={
        "object_size_greater_than": "objectSizeGreaterThan",
        "object_size_less_than": "objectSizeLessThan",
        "prefix": "prefix",
        "tags": "tags",
    },
)
class S3BucketLifecycleConfigurationRuleFilterAnd:
    def __init__(
        self,
        *,
        object_size_greater_than: typing.Optional[jsii.Number] = None,
        object_size_less_than: typing.Optional[jsii.Number] = None,
        prefix: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param object_size_greater_than: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#object_size_greater_than S3BucketLifecycleConfiguration#object_size_greater_than}.
        :param object_size_less_than: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#object_size_less_than S3BucketLifecycleConfiguration#object_size_less_than}.
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#prefix S3BucketLifecycleConfiguration#prefix}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#tags S3BucketLifecycleConfiguration#tags}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6aba8b1c3381ba2ee35fefb43a4347502111740b5210fd0cf5c4d1e37dbd412d)
            check_type(argname="argument object_size_greater_than", value=object_size_greater_than, expected_type=type_hints["object_size_greater_than"])
            check_type(argname="argument object_size_less_than", value=object_size_less_than, expected_type=type_hints["object_size_less_than"])
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if object_size_greater_than is not None:
            self._values["object_size_greater_than"] = object_size_greater_than
        if object_size_less_than is not None:
            self._values["object_size_less_than"] = object_size_less_than
        if prefix is not None:
            self._values["prefix"] = prefix
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def object_size_greater_than(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#object_size_greater_than S3BucketLifecycleConfiguration#object_size_greater_than}.'''
        result = self._values.get("object_size_greater_than")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def object_size_less_than(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#object_size_less_than S3BucketLifecycleConfiguration#object_size_less_than}.'''
        result = self._values.get("object_size_less_than")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#prefix S3BucketLifecycleConfiguration#prefix}.'''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#tags S3BucketLifecycleConfiguration#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketLifecycleConfigurationRuleFilterAnd(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3BucketLifecycleConfigurationRuleFilterAndOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3BucketLifecycleConfiguration.S3BucketLifecycleConfigurationRuleFilterAndOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7d53e8a10c801bbb492a0627c29fe0aaddcb5528c341c424e4c826842cc22c21)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetObjectSizeGreaterThan")
    def reset_object_size_greater_than(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetObjectSizeGreaterThan", []))

    @jsii.member(jsii_name="resetObjectSizeLessThan")
    def reset_object_size_less_than(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetObjectSizeLessThan", []))

    @jsii.member(jsii_name="resetPrefix")
    def reset_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrefix", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @builtins.property
    @jsii.member(jsii_name="objectSizeGreaterThanInput")
    def object_size_greater_than_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "objectSizeGreaterThanInput"))

    @builtins.property
    @jsii.member(jsii_name="objectSizeLessThanInput")
    def object_size_less_than_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "objectSizeLessThanInput"))

    @builtins.property
    @jsii.member(jsii_name="prefixInput")
    def prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefixInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="objectSizeGreaterThan")
    def object_size_greater_than(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "objectSizeGreaterThan"))

    @object_size_greater_than.setter
    def object_size_greater_than(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5682da2212285e1a898fc839aa466c61eff454c987099d90e068625488ef6fb5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "objectSizeGreaterThan", value)

    @builtins.property
    @jsii.member(jsii_name="objectSizeLessThan")
    def object_size_less_than(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "objectSizeLessThan"))

    @object_size_less_than.setter
    def object_size_less_than(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd618a9176ad9206da4bdb84e85c0226fa0c57ce3398d40b3f8f4dab9c64f4e5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "objectSizeLessThan", value)

    @builtins.property
    @jsii.member(jsii_name="prefix")
    def prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prefix"))

    @prefix.setter
    def prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4bad66f58bc304959b70594c91a3f36b29a663a4cf158a4389c37f7c1e536fe6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefix", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__808ca16bb51334ac6495fe54428f2c2d90f00b5e37bc9afc21ee8640dfd135a5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3BucketLifecycleConfigurationRuleFilterAnd]:
        return typing.cast(typing.Optional[S3BucketLifecycleConfigurationRuleFilterAnd], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3BucketLifecycleConfigurationRuleFilterAnd],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f1fcc3df1ee2eaf18b1002fb58fd6569b1c4ef1743b1b6985f99208d856465b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class S3BucketLifecycleConfigurationRuleFilterOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3BucketLifecycleConfiguration.S3BucketLifecycleConfigurationRuleFilterOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7a36ac283c878e276bb626c366217144f09c1f925009ed9e98e83259a65ec4a1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAnd")
    def put_and(
        self,
        *,
        object_size_greater_than: typing.Optional[jsii.Number] = None,
        object_size_less_than: typing.Optional[jsii.Number] = None,
        prefix: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param object_size_greater_than: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#object_size_greater_than S3BucketLifecycleConfiguration#object_size_greater_than}.
        :param object_size_less_than: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#object_size_less_than S3BucketLifecycleConfiguration#object_size_less_than}.
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#prefix S3BucketLifecycleConfiguration#prefix}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#tags S3BucketLifecycleConfiguration#tags}.
        '''
        value = S3BucketLifecycleConfigurationRuleFilterAnd(
            object_size_greater_than=object_size_greater_than,
            object_size_less_than=object_size_less_than,
            prefix=prefix,
            tags=tags,
        )

        return typing.cast(None, jsii.invoke(self, "putAnd", [value]))

    @jsii.member(jsii_name="putTag")
    def put_tag(self, *, key: builtins.str, value: builtins.str) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#key S3BucketLifecycleConfiguration#key}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#value S3BucketLifecycleConfiguration#value}.
        '''
        value_ = S3BucketLifecycleConfigurationRuleFilterTag(key=key, value=value)

        return typing.cast(None, jsii.invoke(self, "putTag", [value_]))

    @jsii.member(jsii_name="resetAnd")
    def reset_and(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAnd", []))

    @jsii.member(jsii_name="resetObjectSizeGreaterThan")
    def reset_object_size_greater_than(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetObjectSizeGreaterThan", []))

    @jsii.member(jsii_name="resetObjectSizeLessThan")
    def reset_object_size_less_than(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetObjectSizeLessThan", []))

    @jsii.member(jsii_name="resetPrefix")
    def reset_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrefix", []))

    @jsii.member(jsii_name="resetTag")
    def reset_tag(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTag", []))

    @builtins.property
    @jsii.member(jsii_name="and")
    def and_(self) -> S3BucketLifecycleConfigurationRuleFilterAndOutputReference:
        return typing.cast(S3BucketLifecycleConfigurationRuleFilterAndOutputReference, jsii.get(self, "and"))

    @builtins.property
    @jsii.member(jsii_name="tag")
    def tag(self) -> "S3BucketLifecycleConfigurationRuleFilterTagOutputReference":
        return typing.cast("S3BucketLifecycleConfigurationRuleFilterTagOutputReference", jsii.get(self, "tag"))

    @builtins.property
    @jsii.member(jsii_name="andInput")
    def and_input(self) -> typing.Optional[S3BucketLifecycleConfigurationRuleFilterAnd]:
        return typing.cast(typing.Optional[S3BucketLifecycleConfigurationRuleFilterAnd], jsii.get(self, "andInput"))

    @builtins.property
    @jsii.member(jsii_name="objectSizeGreaterThanInput")
    def object_size_greater_than_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectSizeGreaterThanInput"))

    @builtins.property
    @jsii.member(jsii_name="objectSizeLessThanInput")
    def object_size_less_than_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectSizeLessThanInput"))

    @builtins.property
    @jsii.member(jsii_name="prefixInput")
    def prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefixInput"))

    @builtins.property
    @jsii.member(jsii_name="tagInput")
    def tag_input(
        self,
    ) -> typing.Optional["S3BucketLifecycleConfigurationRuleFilterTag"]:
        return typing.cast(typing.Optional["S3BucketLifecycleConfigurationRuleFilterTag"], jsii.get(self, "tagInput"))

    @builtins.property
    @jsii.member(jsii_name="objectSizeGreaterThan")
    def object_size_greater_than(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "objectSizeGreaterThan"))

    @object_size_greater_than.setter
    def object_size_greater_than(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05dae23d0b115bf0c3578e89aa08586b3cd5412b1cddf9cd84ec06808cd9059e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "objectSizeGreaterThan", value)

    @builtins.property
    @jsii.member(jsii_name="objectSizeLessThan")
    def object_size_less_than(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "objectSizeLessThan"))

    @object_size_less_than.setter
    def object_size_less_than(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f196f12a09bff73d2d3531cd7e8e9fd5959bbfbfd753ba90164f1154adc785d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "objectSizeLessThan", value)

    @builtins.property
    @jsii.member(jsii_name="prefix")
    def prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prefix"))

    @prefix.setter
    def prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f2e8cd641dc2fd2b54c5bf955e986e48514429e40bc5cdeea26d6ffe193b65c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefix", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3BucketLifecycleConfigurationRuleFilter]:
        return typing.cast(typing.Optional[S3BucketLifecycleConfigurationRuleFilter], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3BucketLifecycleConfigurationRuleFilter],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8fb8cce3fd41c4956cd3c6e179eb8aa6aeb8957258482b66ceaf6646050e38d3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.s3BucketLifecycleConfiguration.S3BucketLifecycleConfigurationRuleFilterTag",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "value": "value"},
)
class S3BucketLifecycleConfigurationRuleFilterTag:
    def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#key S3BucketLifecycleConfiguration#key}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#value S3BucketLifecycleConfiguration#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b963b084acf65b7d7d26968b186b9173e6da36a2b52e7a9c4fb5afd02e0be302)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
            "value": value,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#key S3BucketLifecycleConfiguration#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#value S3BucketLifecycleConfiguration#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketLifecycleConfigurationRuleFilterTag(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3BucketLifecycleConfigurationRuleFilterTagOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3BucketLifecycleConfiguration.S3BucketLifecycleConfigurationRuleFilterTagOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__522f749ca319818429ff578ef97cb7ba98c02e943392b712cacfc8dfbddbb418)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a6bbe56cbff0f82fef64f4e8de2a379900715142177bcc4504b67529eed08e3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ecf5ade85798f2b8b71f8531616687dcccf223785eeb2da8c5f3dce8be189c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3BucketLifecycleConfigurationRuleFilterTag]:
        return typing.cast(typing.Optional[S3BucketLifecycleConfigurationRuleFilterTag], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3BucketLifecycleConfigurationRuleFilterTag],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__286df149ca9445e595e53acac1d0337b406d26e3fbed8453199cf7c129fcba69)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class S3BucketLifecycleConfigurationRuleList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3BucketLifecycleConfiguration.S3BucketLifecycleConfigurationRuleList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__fc55194c27cc074ed957a393ce7030f8dc7f412f99347093c6ec1db6e0bedc7b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "S3BucketLifecycleConfigurationRuleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c17794cff93c6926bbce6c3b4602cafdbe33a414c02d87abd50f49803925a9b)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("S3BucketLifecycleConfigurationRuleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f13e85c14d53932e9ff2f8dad70df259db69ba4864508831a1c2fda3fa85609)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1042a97ee37a9eb8001f0751b703674a3f29ee1d71d80073311f16c14e8ded37)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d2b44c20e258e73a8d0fddc634331c6459399e9278721142df9f5e670cfd5621)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[S3BucketLifecycleConfigurationRule]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[S3BucketLifecycleConfigurationRule]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[S3BucketLifecycleConfigurationRule]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b86eec3034805ef5433d2c3b8e900d33eaa56e639d43184804c88b33cb090fbc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.s3BucketLifecycleConfiguration.S3BucketLifecycleConfigurationRuleNoncurrentVersionExpiration",
    jsii_struct_bases=[],
    name_mapping={
        "newer_noncurrent_versions": "newerNoncurrentVersions",
        "noncurrent_days": "noncurrentDays",
    },
)
class S3BucketLifecycleConfigurationRuleNoncurrentVersionExpiration:
    def __init__(
        self,
        *,
        newer_noncurrent_versions: typing.Optional[builtins.str] = None,
        noncurrent_days: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param newer_noncurrent_versions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#newer_noncurrent_versions S3BucketLifecycleConfiguration#newer_noncurrent_versions}.
        :param noncurrent_days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#noncurrent_days S3BucketLifecycleConfiguration#noncurrent_days}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c85759cf56b52cf8eb852d0a75ae3fb6a1dd7049fd40760824e3cb4a672e60b1)
            check_type(argname="argument newer_noncurrent_versions", value=newer_noncurrent_versions, expected_type=type_hints["newer_noncurrent_versions"])
            check_type(argname="argument noncurrent_days", value=noncurrent_days, expected_type=type_hints["noncurrent_days"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if newer_noncurrent_versions is not None:
            self._values["newer_noncurrent_versions"] = newer_noncurrent_versions
        if noncurrent_days is not None:
            self._values["noncurrent_days"] = noncurrent_days

    @builtins.property
    def newer_noncurrent_versions(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#newer_noncurrent_versions S3BucketLifecycleConfiguration#newer_noncurrent_versions}.'''
        result = self._values.get("newer_noncurrent_versions")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def noncurrent_days(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#noncurrent_days S3BucketLifecycleConfiguration#noncurrent_days}.'''
        result = self._values.get("noncurrent_days")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketLifecycleConfigurationRuleNoncurrentVersionExpiration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3BucketLifecycleConfigurationRuleNoncurrentVersionExpirationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3BucketLifecycleConfiguration.S3BucketLifecycleConfigurationRuleNoncurrentVersionExpirationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3f8eff63df319a76b71818e92d325720a013f216bf10ae45f6ec2d96d4dd7a3a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetNewerNoncurrentVersions")
    def reset_newer_noncurrent_versions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNewerNoncurrentVersions", []))

    @jsii.member(jsii_name="resetNoncurrentDays")
    def reset_noncurrent_days(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNoncurrentDays", []))

    @builtins.property
    @jsii.member(jsii_name="newerNoncurrentVersionsInput")
    def newer_noncurrent_versions_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "newerNoncurrentVersionsInput"))

    @builtins.property
    @jsii.member(jsii_name="noncurrentDaysInput")
    def noncurrent_days_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "noncurrentDaysInput"))

    @builtins.property
    @jsii.member(jsii_name="newerNoncurrentVersions")
    def newer_noncurrent_versions(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "newerNoncurrentVersions"))

    @newer_noncurrent_versions.setter
    def newer_noncurrent_versions(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__952b665ce9dd20f7545700baf1d6f1a251e0b4ecb46adf4306f7213b42ee4770)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "newerNoncurrentVersions", value)

    @builtins.property
    @jsii.member(jsii_name="noncurrentDays")
    def noncurrent_days(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "noncurrentDays"))

    @noncurrent_days.setter
    def noncurrent_days(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__71a05078d173e297335a416d6c167646a88b21d311b7dff652257ee037ec842f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "noncurrentDays", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3BucketLifecycleConfigurationRuleNoncurrentVersionExpiration]:
        return typing.cast(typing.Optional[S3BucketLifecycleConfigurationRuleNoncurrentVersionExpiration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3BucketLifecycleConfigurationRuleNoncurrentVersionExpiration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f210318751f3bb54fa9454455f22968bb64eb1f70092d64d1398758f66eed467)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.s3BucketLifecycleConfiguration.S3BucketLifecycleConfigurationRuleNoncurrentVersionTransition",
    jsii_struct_bases=[],
    name_mapping={
        "storage_class": "storageClass",
        "newer_noncurrent_versions": "newerNoncurrentVersions",
        "noncurrent_days": "noncurrentDays",
    },
)
class S3BucketLifecycleConfigurationRuleNoncurrentVersionTransition:
    def __init__(
        self,
        *,
        storage_class: builtins.str,
        newer_noncurrent_versions: typing.Optional[builtins.str] = None,
        noncurrent_days: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param storage_class: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#storage_class S3BucketLifecycleConfiguration#storage_class}.
        :param newer_noncurrent_versions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#newer_noncurrent_versions S3BucketLifecycleConfiguration#newer_noncurrent_versions}.
        :param noncurrent_days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#noncurrent_days S3BucketLifecycleConfiguration#noncurrent_days}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54631da314a434f2f418a41d7cce646ef6c1152c6f74ef15792fc3fef50e6e17)
            check_type(argname="argument storage_class", value=storage_class, expected_type=type_hints["storage_class"])
            check_type(argname="argument newer_noncurrent_versions", value=newer_noncurrent_versions, expected_type=type_hints["newer_noncurrent_versions"])
            check_type(argname="argument noncurrent_days", value=noncurrent_days, expected_type=type_hints["noncurrent_days"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "storage_class": storage_class,
        }
        if newer_noncurrent_versions is not None:
            self._values["newer_noncurrent_versions"] = newer_noncurrent_versions
        if noncurrent_days is not None:
            self._values["noncurrent_days"] = noncurrent_days

    @builtins.property
    def storage_class(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#storage_class S3BucketLifecycleConfiguration#storage_class}.'''
        result = self._values.get("storage_class")
        assert result is not None, "Required property 'storage_class' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def newer_noncurrent_versions(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#newer_noncurrent_versions S3BucketLifecycleConfiguration#newer_noncurrent_versions}.'''
        result = self._values.get("newer_noncurrent_versions")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def noncurrent_days(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#noncurrent_days S3BucketLifecycleConfiguration#noncurrent_days}.'''
        result = self._values.get("noncurrent_days")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketLifecycleConfigurationRuleNoncurrentVersionTransition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3BucketLifecycleConfigurationRuleNoncurrentVersionTransitionList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3BucketLifecycleConfiguration.S3BucketLifecycleConfigurationRuleNoncurrentVersionTransitionList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4ad2d990331e650ae3153b0e5d54d32568d7e02cdf133fb4f79fff72a7f260cb)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "S3BucketLifecycleConfigurationRuleNoncurrentVersionTransitionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f083c828ab514baaf85219eacebbe9dc878f07616c34ea428b4be9cc0f4e6ec)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("S3BucketLifecycleConfigurationRuleNoncurrentVersionTransitionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3baf11ed23592a8d34c19cbfaa8af51da9db35b02b22df45565842098859d15)
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
            type_hints = typing.get_type_hints(_typecheckingstub__89fa0dc6193edc5645d697315682fb625e3767aaa56b2021836d7b9bf8c3b7dc)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9f6793337759444b4fc40bdedaaee2d4f3d60298f549df709f2e19f7667b917f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[S3BucketLifecycleConfigurationRuleNoncurrentVersionTransition]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[S3BucketLifecycleConfigurationRuleNoncurrentVersionTransition]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[S3BucketLifecycleConfigurationRuleNoncurrentVersionTransition]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e884b26c9feceaef30629aa5646f63223478d164ed9d69b0d1931e97343533e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class S3BucketLifecycleConfigurationRuleNoncurrentVersionTransitionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3BucketLifecycleConfiguration.S3BucketLifecycleConfigurationRuleNoncurrentVersionTransitionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ac807e27e90bd5fead366eb0f9afb8f8506a7a51e1ebbec850131df95639f9a6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetNewerNoncurrentVersions")
    def reset_newer_noncurrent_versions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNewerNoncurrentVersions", []))

    @jsii.member(jsii_name="resetNoncurrentDays")
    def reset_noncurrent_days(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNoncurrentDays", []))

    @builtins.property
    @jsii.member(jsii_name="newerNoncurrentVersionsInput")
    def newer_noncurrent_versions_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "newerNoncurrentVersionsInput"))

    @builtins.property
    @jsii.member(jsii_name="noncurrentDaysInput")
    def noncurrent_days_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "noncurrentDaysInput"))

    @builtins.property
    @jsii.member(jsii_name="storageClassInput")
    def storage_class_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageClassInput"))

    @builtins.property
    @jsii.member(jsii_name="newerNoncurrentVersions")
    def newer_noncurrent_versions(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "newerNoncurrentVersions"))

    @newer_noncurrent_versions.setter
    def newer_noncurrent_versions(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2d4297eefc197b71d09c0a206fd0af8e89a44ef4a2758b1af9c9c04828cad55)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "newerNoncurrentVersions", value)

    @builtins.property
    @jsii.member(jsii_name="noncurrentDays")
    def noncurrent_days(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "noncurrentDays"))

    @noncurrent_days.setter
    def noncurrent_days(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__28b3113d9ba4aa160b4ca1963988a8370d34fa2db8bb0f62d55ab5766adea919)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "noncurrentDays", value)

    @builtins.property
    @jsii.member(jsii_name="storageClass")
    def storage_class(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageClass"))

    @storage_class.setter
    def storage_class(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c00e5178b721d0d2bbcd476f5a42f8d1a3d05629ac401aaa0c6a814cab450f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageClass", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[S3BucketLifecycleConfigurationRuleNoncurrentVersionTransition, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[S3BucketLifecycleConfigurationRuleNoncurrentVersionTransition, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[S3BucketLifecycleConfigurationRuleNoncurrentVersionTransition, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82d50ac1545adcaac4fb60973b4fe8683280feb9ed7211d7c46c400711e351f2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class S3BucketLifecycleConfigurationRuleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3BucketLifecycleConfiguration.S3BucketLifecycleConfigurationRuleOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6fa690e87266de00a28fc701e1aceb6ff312baca19c0b108e3e775c8e9e1b99e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putAbortIncompleteMultipartUpload")
    def put_abort_incomplete_multipart_upload(
        self,
        *,
        days_after_initiation: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param days_after_initiation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#days_after_initiation S3BucketLifecycleConfiguration#days_after_initiation}.
        '''
        value = S3BucketLifecycleConfigurationRuleAbortIncompleteMultipartUpload(
            days_after_initiation=days_after_initiation
        )

        return typing.cast(None, jsii.invoke(self, "putAbortIncompleteMultipartUpload", [value]))

    @jsii.member(jsii_name="putExpiration")
    def put_expiration(
        self,
        *,
        date: typing.Optional[builtins.str] = None,
        days: typing.Optional[jsii.Number] = None,
        expired_object_delete_marker: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param date: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#date S3BucketLifecycleConfiguration#date}.
        :param days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#days S3BucketLifecycleConfiguration#days}.
        :param expired_object_delete_marker: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#expired_object_delete_marker S3BucketLifecycleConfiguration#expired_object_delete_marker}.
        '''
        value = S3BucketLifecycleConfigurationRuleExpiration(
            date=date,
            days=days,
            expired_object_delete_marker=expired_object_delete_marker,
        )

        return typing.cast(None, jsii.invoke(self, "putExpiration", [value]))

    @jsii.member(jsii_name="putFilter")
    def put_filter(
        self,
        *,
        and_: typing.Optional[typing.Union[S3BucketLifecycleConfigurationRuleFilterAnd, typing.Dict[builtins.str, typing.Any]]] = None,
        object_size_greater_than: typing.Optional[builtins.str] = None,
        object_size_less_than: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
        tag: typing.Optional[typing.Union[S3BucketLifecycleConfigurationRuleFilterTag, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param and_: and block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#and S3BucketLifecycleConfiguration#and}
        :param object_size_greater_than: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#object_size_greater_than S3BucketLifecycleConfiguration#object_size_greater_than}.
        :param object_size_less_than: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#object_size_less_than S3BucketLifecycleConfiguration#object_size_less_than}.
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#prefix S3BucketLifecycleConfiguration#prefix}.
        :param tag: tag block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#tag S3BucketLifecycleConfiguration#tag}
        '''
        value = S3BucketLifecycleConfigurationRuleFilter(
            and_=and_,
            object_size_greater_than=object_size_greater_than,
            object_size_less_than=object_size_less_than,
            prefix=prefix,
            tag=tag,
        )

        return typing.cast(None, jsii.invoke(self, "putFilter", [value]))

    @jsii.member(jsii_name="putNoncurrentVersionExpiration")
    def put_noncurrent_version_expiration(
        self,
        *,
        newer_noncurrent_versions: typing.Optional[builtins.str] = None,
        noncurrent_days: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param newer_noncurrent_versions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#newer_noncurrent_versions S3BucketLifecycleConfiguration#newer_noncurrent_versions}.
        :param noncurrent_days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#noncurrent_days S3BucketLifecycleConfiguration#noncurrent_days}.
        '''
        value = S3BucketLifecycleConfigurationRuleNoncurrentVersionExpiration(
            newer_noncurrent_versions=newer_noncurrent_versions,
            noncurrent_days=noncurrent_days,
        )

        return typing.cast(None, jsii.invoke(self, "putNoncurrentVersionExpiration", [value]))

    @jsii.member(jsii_name="putNoncurrentVersionTransition")
    def put_noncurrent_version_transition(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[S3BucketLifecycleConfigurationRuleNoncurrentVersionTransition, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21a701e62dd190a9eada6d08cbc52733a5cdbea15243f3777c7d3d8d257642f6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNoncurrentVersionTransition", [value]))

    @jsii.member(jsii_name="putTransition")
    def put_transition(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["S3BucketLifecycleConfigurationRuleTransition", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12d8bbaddd3daa0f1ce0cb9ddec47ca00367a833171bf8989c8bf749eb35021c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTransition", [value]))

    @jsii.member(jsii_name="resetAbortIncompleteMultipartUpload")
    def reset_abort_incomplete_multipart_upload(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAbortIncompleteMultipartUpload", []))

    @jsii.member(jsii_name="resetExpiration")
    def reset_expiration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExpiration", []))

    @jsii.member(jsii_name="resetFilter")
    def reset_filter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFilter", []))

    @jsii.member(jsii_name="resetNoncurrentVersionExpiration")
    def reset_noncurrent_version_expiration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNoncurrentVersionExpiration", []))

    @jsii.member(jsii_name="resetNoncurrentVersionTransition")
    def reset_noncurrent_version_transition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNoncurrentVersionTransition", []))

    @jsii.member(jsii_name="resetPrefix")
    def reset_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrefix", []))

    @jsii.member(jsii_name="resetTransition")
    def reset_transition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTransition", []))

    @builtins.property
    @jsii.member(jsii_name="abortIncompleteMultipartUpload")
    def abort_incomplete_multipart_upload(
        self,
    ) -> S3BucketLifecycleConfigurationRuleAbortIncompleteMultipartUploadOutputReference:
        return typing.cast(S3BucketLifecycleConfigurationRuleAbortIncompleteMultipartUploadOutputReference, jsii.get(self, "abortIncompleteMultipartUpload"))

    @builtins.property
    @jsii.member(jsii_name="expiration")
    def expiration(self) -> S3BucketLifecycleConfigurationRuleExpirationOutputReference:
        return typing.cast(S3BucketLifecycleConfigurationRuleExpirationOutputReference, jsii.get(self, "expiration"))

    @builtins.property
    @jsii.member(jsii_name="filter")
    def filter(self) -> S3BucketLifecycleConfigurationRuleFilterOutputReference:
        return typing.cast(S3BucketLifecycleConfigurationRuleFilterOutputReference, jsii.get(self, "filter"))

    @builtins.property
    @jsii.member(jsii_name="noncurrentVersionExpiration")
    def noncurrent_version_expiration(
        self,
    ) -> S3BucketLifecycleConfigurationRuleNoncurrentVersionExpirationOutputReference:
        return typing.cast(S3BucketLifecycleConfigurationRuleNoncurrentVersionExpirationOutputReference, jsii.get(self, "noncurrentVersionExpiration"))

    @builtins.property
    @jsii.member(jsii_name="noncurrentVersionTransition")
    def noncurrent_version_transition(
        self,
    ) -> S3BucketLifecycleConfigurationRuleNoncurrentVersionTransitionList:
        return typing.cast(S3BucketLifecycleConfigurationRuleNoncurrentVersionTransitionList, jsii.get(self, "noncurrentVersionTransition"))

    @builtins.property
    @jsii.member(jsii_name="transition")
    def transition(self) -> "S3BucketLifecycleConfigurationRuleTransitionList":
        return typing.cast("S3BucketLifecycleConfigurationRuleTransitionList", jsii.get(self, "transition"))

    @builtins.property
    @jsii.member(jsii_name="abortIncompleteMultipartUploadInput")
    def abort_incomplete_multipart_upload_input(
        self,
    ) -> typing.Optional[S3BucketLifecycleConfigurationRuleAbortIncompleteMultipartUpload]:
        return typing.cast(typing.Optional[S3BucketLifecycleConfigurationRuleAbortIncompleteMultipartUpload], jsii.get(self, "abortIncompleteMultipartUploadInput"))

    @builtins.property
    @jsii.member(jsii_name="expirationInput")
    def expiration_input(
        self,
    ) -> typing.Optional[S3BucketLifecycleConfigurationRuleExpiration]:
        return typing.cast(typing.Optional[S3BucketLifecycleConfigurationRuleExpiration], jsii.get(self, "expirationInput"))

    @builtins.property
    @jsii.member(jsii_name="filterInput")
    def filter_input(self) -> typing.Optional[S3BucketLifecycleConfigurationRuleFilter]:
        return typing.cast(typing.Optional[S3BucketLifecycleConfigurationRuleFilter], jsii.get(self, "filterInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="noncurrentVersionExpirationInput")
    def noncurrent_version_expiration_input(
        self,
    ) -> typing.Optional[S3BucketLifecycleConfigurationRuleNoncurrentVersionExpiration]:
        return typing.cast(typing.Optional[S3BucketLifecycleConfigurationRuleNoncurrentVersionExpiration], jsii.get(self, "noncurrentVersionExpirationInput"))

    @builtins.property
    @jsii.member(jsii_name="noncurrentVersionTransitionInput")
    def noncurrent_version_transition_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[S3BucketLifecycleConfigurationRuleNoncurrentVersionTransition]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[S3BucketLifecycleConfigurationRuleNoncurrentVersionTransition]]], jsii.get(self, "noncurrentVersionTransitionInput"))

    @builtins.property
    @jsii.member(jsii_name="prefixInput")
    def prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefixInput"))

    @builtins.property
    @jsii.member(jsii_name="statusInput")
    def status_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statusInput"))

    @builtins.property
    @jsii.member(jsii_name="transitionInput")
    def transition_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["S3BucketLifecycleConfigurationRuleTransition"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["S3BucketLifecycleConfigurationRuleTransition"]]], jsii.get(self, "transitionInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c16c3eecec1ce930d6ce13e619c4e413cbc1a1b518dc93d7c51d821467b48e9c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="prefix")
    def prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prefix"))

    @prefix.setter
    def prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b667e967843280514ed557969a190a8fd023370ea22378b449b0c13086da575c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefix", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @status.setter
    def status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1a438e1c8a0259109ceb5aa7189af7ee42e9cf219824944acbf354d8cac6b05)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[S3BucketLifecycleConfigurationRule, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[S3BucketLifecycleConfigurationRule, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[S3BucketLifecycleConfigurationRule, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5462d9e3a71fddf8260863aacee79fb902604d74d2feffbb0c2c945efae4023c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.s3BucketLifecycleConfiguration.S3BucketLifecycleConfigurationRuleTransition",
    jsii_struct_bases=[],
    name_mapping={"storage_class": "storageClass", "date": "date", "days": "days"},
)
class S3BucketLifecycleConfigurationRuleTransition:
    def __init__(
        self,
        *,
        storage_class: builtins.str,
        date: typing.Optional[builtins.str] = None,
        days: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param storage_class: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#storage_class S3BucketLifecycleConfiguration#storage_class}.
        :param date: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#date S3BucketLifecycleConfiguration#date}.
        :param days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#days S3BucketLifecycleConfiguration#days}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__900f5374647b97aeb0219279fbb2154de8ed6c40d06c41e43a9497ccc90d7dfc)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#storage_class S3BucketLifecycleConfiguration#storage_class}.'''
        result = self._values.get("storage_class")
        assert result is not None, "Required property 'storage_class' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def date(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#date S3BucketLifecycleConfiguration#date}.'''
        result = self._values.get("date")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def days(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_lifecycle_configuration#days S3BucketLifecycleConfiguration#days}.'''
        result = self._values.get("days")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketLifecycleConfigurationRuleTransition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3BucketLifecycleConfigurationRuleTransitionList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3BucketLifecycleConfiguration.S3BucketLifecycleConfigurationRuleTransitionList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__70b9e4470ff5f57a481cbec79b29d64e20a5b0cec74df940f3e400666af0aaba)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "S3BucketLifecycleConfigurationRuleTransitionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fbe3d26fdb99bcdb93d927f447a63a0bbdfbf6d35242b53ef1c330b20a556afc)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("S3BucketLifecycleConfigurationRuleTransitionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8438af099c65af518d414edb8d5b2661f853020be71447ee943bed73aa5c2c0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__fa89f9f53e52da598adcc7fbdd8bbaa6a498d22d6c0acbd71cb3d560dac5e380)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5c9502543eb38e003c4e22ad4899262eb9d30815301feac089a0989a809d8342)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[S3BucketLifecycleConfigurationRuleTransition]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[S3BucketLifecycleConfigurationRuleTransition]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[S3BucketLifecycleConfigurationRuleTransition]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cbbd41907ddd77add83c53bd75f6e7322e01056c0e46b157543c3d674d14a35b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class S3BucketLifecycleConfigurationRuleTransitionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3BucketLifecycleConfiguration.S3BucketLifecycleConfigurationRuleTransitionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__52a7ecf830241b08724e686ea26f6db369b18623f8c53d4315962ce40f13aab7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__16b9b97b4a7048ed677dc572b989a03a53335720349629c3102e5e926e6fd0ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "date", value)

    @builtins.property
    @jsii.member(jsii_name="days")
    def days(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "days"))

    @days.setter
    def days(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89b4cec19f17859a52c1515ac8ca7e154181cfed89285e1fb3185c7c186506e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "days", value)

    @builtins.property
    @jsii.member(jsii_name="storageClass")
    def storage_class(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageClass"))

    @storage_class.setter
    def storage_class(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__697b9c5730d4dce5cc44bfc57933928c5719a3fa6c704773c35e5fbef1ab17cb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageClass", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[S3BucketLifecycleConfigurationRuleTransition, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[S3BucketLifecycleConfigurationRuleTransition, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[S3BucketLifecycleConfigurationRuleTransition, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11eb396097d64cbdab26b7f691e534115a6decfecf984fe558d1a427020125d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "S3BucketLifecycleConfiguration",
    "S3BucketLifecycleConfigurationConfig",
    "S3BucketLifecycleConfigurationRule",
    "S3BucketLifecycleConfigurationRuleAbortIncompleteMultipartUpload",
    "S3BucketLifecycleConfigurationRuleAbortIncompleteMultipartUploadOutputReference",
    "S3BucketLifecycleConfigurationRuleExpiration",
    "S3BucketLifecycleConfigurationRuleExpirationOutputReference",
    "S3BucketLifecycleConfigurationRuleFilter",
    "S3BucketLifecycleConfigurationRuleFilterAnd",
    "S3BucketLifecycleConfigurationRuleFilterAndOutputReference",
    "S3BucketLifecycleConfigurationRuleFilterOutputReference",
    "S3BucketLifecycleConfigurationRuleFilterTag",
    "S3BucketLifecycleConfigurationRuleFilterTagOutputReference",
    "S3BucketLifecycleConfigurationRuleList",
    "S3BucketLifecycleConfigurationRuleNoncurrentVersionExpiration",
    "S3BucketLifecycleConfigurationRuleNoncurrentVersionExpirationOutputReference",
    "S3BucketLifecycleConfigurationRuleNoncurrentVersionTransition",
    "S3BucketLifecycleConfigurationRuleNoncurrentVersionTransitionList",
    "S3BucketLifecycleConfigurationRuleNoncurrentVersionTransitionOutputReference",
    "S3BucketLifecycleConfigurationRuleOutputReference",
    "S3BucketLifecycleConfigurationRuleTransition",
    "S3BucketLifecycleConfigurationRuleTransitionList",
    "S3BucketLifecycleConfigurationRuleTransitionOutputReference",
]

publication.publish()

def _typecheckingstub__db24ff7d5d15a31afa7223abd24a8e67b2a6d3b6c93ee39d1723830fe9e41652(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    bucket: builtins.str,
    rule: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[S3BucketLifecycleConfigurationRule, typing.Dict[builtins.str, typing.Any]]]],
    expected_bucket_owner: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__ef126be78300ce8d6548ec18ae342ea56ba640beb4939573d63eb19bc5561327(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[S3BucketLifecycleConfigurationRule, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5c574db07cf41a685c8ee528734d9b88836516a91b2b78b1c9aa212adcb6a8a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38908fbe40beebff95afe525931dc881ee84b4330299e310559139620b86051f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9463016f07ddffdf3a637d60e26f07056c514f047eb57d3d78b7dcf66822384e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a45af29c28739881fe73b7bab967228c72d4abd7f8ad70f503620bfb41de6371(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    bucket: builtins.str,
    rule: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[S3BucketLifecycleConfigurationRule, typing.Dict[builtins.str, typing.Any]]]],
    expected_bucket_owner: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__968920fab5956d1b562f411f3f4d2594bca2a3323bffc30d789923b217671ed8(
    *,
    id: builtins.str,
    status: builtins.str,
    abort_incomplete_multipart_upload: typing.Optional[typing.Union[S3BucketLifecycleConfigurationRuleAbortIncompleteMultipartUpload, typing.Dict[builtins.str, typing.Any]]] = None,
    expiration: typing.Optional[typing.Union[S3BucketLifecycleConfigurationRuleExpiration, typing.Dict[builtins.str, typing.Any]]] = None,
    filter: typing.Optional[typing.Union[S3BucketLifecycleConfigurationRuleFilter, typing.Dict[builtins.str, typing.Any]]] = None,
    noncurrent_version_expiration: typing.Optional[typing.Union[S3BucketLifecycleConfigurationRuleNoncurrentVersionExpiration, typing.Dict[builtins.str, typing.Any]]] = None,
    noncurrent_version_transition: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[S3BucketLifecycleConfigurationRuleNoncurrentVersionTransition, typing.Dict[builtins.str, typing.Any]]]]] = None,
    prefix: typing.Optional[builtins.str] = None,
    transition: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[S3BucketLifecycleConfigurationRuleTransition, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f86b7c99c1f9cbc877252ffd1805af6bff7b6603c6d6f14c0734050ed87a1e41(
    *,
    days_after_initiation: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ce65fc9eae34c2f3db982dced008e8b7378fccfc9d88d49df89809e15fb4f32(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b720c16b317f227dbe9835eae86243112a939b9373afca567658cd5fba61d6e0(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a6cfa593ce3e28ea09fde9eb3842e758aaa4eb998bc422c47a1e28de85a7239(
    value: typing.Optional[S3BucketLifecycleConfigurationRuleAbortIncompleteMultipartUpload],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aff495db03d5b067b48f71d3941a7435a6e91d45c09f927e939419d36ea6f67b(
    *,
    date: typing.Optional[builtins.str] = None,
    days: typing.Optional[jsii.Number] = None,
    expired_object_delete_marker: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b6e82ceaa273d3b1746534326ffb9e3ea6986e082033fdb60b8d0106c301b3e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07cd3dd547af324ce341b80c782dfc2bfc933e96aae4e097cfb55796fcf4835f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89ce2c52c9ff7d5f201eee3df1d800f9a9e41830298e34edd41fb7887ce1d2f9(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__681c210d4f284b06de6416deffb11566729a82c160c05a96a40a57938cc68586(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__413328a20de4196832e7c63767f0367d5b04b58a124e5aa82a0cb5711f2ae5ff(
    value: typing.Optional[S3BucketLifecycleConfigurationRuleExpiration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb9ebb81cff0e4929a668999c5448b4664a862cebd49ee8ebdb3276c385a1864(
    *,
    and_: typing.Optional[typing.Union[S3BucketLifecycleConfigurationRuleFilterAnd, typing.Dict[builtins.str, typing.Any]]] = None,
    object_size_greater_than: typing.Optional[builtins.str] = None,
    object_size_less_than: typing.Optional[builtins.str] = None,
    prefix: typing.Optional[builtins.str] = None,
    tag: typing.Optional[typing.Union[S3BucketLifecycleConfigurationRuleFilterTag, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6aba8b1c3381ba2ee35fefb43a4347502111740b5210fd0cf5c4d1e37dbd412d(
    *,
    object_size_greater_than: typing.Optional[jsii.Number] = None,
    object_size_less_than: typing.Optional[jsii.Number] = None,
    prefix: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d53e8a10c801bbb492a0627c29fe0aaddcb5528c341c424e4c826842cc22c21(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5682da2212285e1a898fc839aa466c61eff454c987099d90e068625488ef6fb5(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd618a9176ad9206da4bdb84e85c0226fa0c57ce3398d40b3f8f4dab9c64f4e5(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4bad66f58bc304959b70594c91a3f36b29a663a4cf158a4389c37f7c1e536fe6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__808ca16bb51334ac6495fe54428f2c2d90f00b5e37bc9afc21ee8640dfd135a5(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f1fcc3df1ee2eaf18b1002fb58fd6569b1c4ef1743b1b6985f99208d856465b(
    value: typing.Optional[S3BucketLifecycleConfigurationRuleFilterAnd],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a36ac283c878e276bb626c366217144f09c1f925009ed9e98e83259a65ec4a1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05dae23d0b115bf0c3578e89aa08586b3cd5412b1cddf9cd84ec06808cd9059e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f196f12a09bff73d2d3531cd7e8e9fd5959bbfbfd753ba90164f1154adc785d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f2e8cd641dc2fd2b54c5bf955e986e48514429e40bc5cdeea26d6ffe193b65c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8fb8cce3fd41c4956cd3c6e179eb8aa6aeb8957258482b66ceaf6646050e38d3(
    value: typing.Optional[S3BucketLifecycleConfigurationRuleFilter],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b963b084acf65b7d7d26968b186b9173e6da36a2b52e7a9c4fb5afd02e0be302(
    *,
    key: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__522f749ca319818429ff578ef97cb7ba98c02e943392b712cacfc8dfbddbb418(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a6bbe56cbff0f82fef64f4e8de2a379900715142177bcc4504b67529eed08e3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ecf5ade85798f2b8b71f8531616687dcccf223785eeb2da8c5f3dce8be189c6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__286df149ca9445e595e53acac1d0337b406d26e3fbed8453199cf7c129fcba69(
    value: typing.Optional[S3BucketLifecycleConfigurationRuleFilterTag],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc55194c27cc074ed957a393ce7030f8dc7f412f99347093c6ec1db6e0bedc7b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c17794cff93c6926bbce6c3b4602cafdbe33a414c02d87abd50f49803925a9b(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f13e85c14d53932e9ff2f8dad70df259db69ba4864508831a1c2fda3fa85609(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1042a97ee37a9eb8001f0751b703674a3f29ee1d71d80073311f16c14e8ded37(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2b44c20e258e73a8d0fddc634331c6459399e9278721142df9f5e670cfd5621(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b86eec3034805ef5433d2c3b8e900d33eaa56e639d43184804c88b33cb090fbc(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[S3BucketLifecycleConfigurationRule]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c85759cf56b52cf8eb852d0a75ae3fb6a1dd7049fd40760824e3cb4a672e60b1(
    *,
    newer_noncurrent_versions: typing.Optional[builtins.str] = None,
    noncurrent_days: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f8eff63df319a76b71818e92d325720a013f216bf10ae45f6ec2d96d4dd7a3a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__952b665ce9dd20f7545700baf1d6f1a251e0b4ecb46adf4306f7213b42ee4770(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71a05078d173e297335a416d6c167646a88b21d311b7dff652257ee037ec842f(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f210318751f3bb54fa9454455f22968bb64eb1f70092d64d1398758f66eed467(
    value: typing.Optional[S3BucketLifecycleConfigurationRuleNoncurrentVersionExpiration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54631da314a434f2f418a41d7cce646ef6c1152c6f74ef15792fc3fef50e6e17(
    *,
    storage_class: builtins.str,
    newer_noncurrent_versions: typing.Optional[builtins.str] = None,
    noncurrent_days: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ad2d990331e650ae3153b0e5d54d32568d7e02cdf133fb4f79fff72a7f260cb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f083c828ab514baaf85219eacebbe9dc878f07616c34ea428b4be9cc0f4e6ec(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3baf11ed23592a8d34c19cbfaa8af51da9db35b02b22df45565842098859d15(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89fa0dc6193edc5645d697315682fb625e3767aaa56b2021836d7b9bf8c3b7dc(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f6793337759444b4fc40bdedaaee2d4f3d60298f549df709f2e19f7667b917f(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e884b26c9feceaef30629aa5646f63223478d164ed9d69b0d1931e97343533e(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[S3BucketLifecycleConfigurationRuleNoncurrentVersionTransition]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac807e27e90bd5fead366eb0f9afb8f8506a7a51e1ebbec850131df95639f9a6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2d4297eefc197b71d09c0a206fd0af8e89a44ef4a2758b1af9c9c04828cad55(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28b3113d9ba4aa160b4ca1963988a8370d34fa2db8bb0f62d55ab5766adea919(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c00e5178b721d0d2bbcd476f5a42f8d1a3d05629ac401aaa0c6a814cab450f8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82d50ac1545adcaac4fb60973b4fe8683280feb9ed7211d7c46c400711e351f2(
    value: typing.Optional[typing.Union[S3BucketLifecycleConfigurationRuleNoncurrentVersionTransition, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6fa690e87266de00a28fc701e1aceb6ff312baca19c0b108e3e775c8e9e1b99e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21a701e62dd190a9eada6d08cbc52733a5cdbea15243f3777c7d3d8d257642f6(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[S3BucketLifecycleConfigurationRuleNoncurrentVersionTransition, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12d8bbaddd3daa0f1ce0cb9ddec47ca00367a833171bf8989c8bf749eb35021c(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[S3BucketLifecycleConfigurationRuleTransition, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c16c3eecec1ce930d6ce13e619c4e413cbc1a1b518dc93d7c51d821467b48e9c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b667e967843280514ed557969a190a8fd023370ea22378b449b0c13086da575c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1a438e1c8a0259109ceb5aa7189af7ee42e9cf219824944acbf354d8cac6b05(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5462d9e3a71fddf8260863aacee79fb902604d74d2feffbb0c2c945efae4023c(
    value: typing.Optional[typing.Union[S3BucketLifecycleConfigurationRule, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__900f5374647b97aeb0219279fbb2154de8ed6c40d06c41e43a9497ccc90d7dfc(
    *,
    storage_class: builtins.str,
    date: typing.Optional[builtins.str] = None,
    days: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70b9e4470ff5f57a481cbec79b29d64e20a5b0cec74df940f3e400666af0aaba(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fbe3d26fdb99bcdb93d927f447a63a0bbdfbf6d35242b53ef1c330b20a556afc(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8438af099c65af518d414edb8d5b2661f853020be71447ee943bed73aa5c2c0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa89f9f53e52da598adcc7fbdd8bbaa6a498d22d6c0acbd71cb3d560dac5e380(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c9502543eb38e003c4e22ad4899262eb9d30815301feac089a0989a809d8342(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cbbd41907ddd77add83c53bd75f6e7322e01056c0e46b157543c3d674d14a35b(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[S3BucketLifecycleConfigurationRuleTransition]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52a7ecf830241b08724e686ea26f6db369b18623f8c53d4315962ce40f13aab7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16b9b97b4a7048ed677dc572b989a03a53335720349629c3102e5e926e6fd0ec(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89b4cec19f17859a52c1515ac8ca7e154181cfed89285e1fb3185c7c186506e6(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__697b9c5730d4dce5cc44bfc57933928c5719a3fa6c704773c35e5fbef1ab17cb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11eb396097d64cbdab26b7f691e534115a6decfecf984fe558d1a427020125d0(
    value: typing.Optional[typing.Union[S3BucketLifecycleConfigurationRuleTransition, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
