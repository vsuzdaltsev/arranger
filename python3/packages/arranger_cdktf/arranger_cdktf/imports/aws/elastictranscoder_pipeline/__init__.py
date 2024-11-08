'''
# `aws_elastictranscoder_pipeline`

Refer to the Terraform Registory for docs: [`aws_elastictranscoder_pipeline`](https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline).
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


class ElastictranscoderPipeline(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.elastictranscoderPipeline.ElastictranscoderPipeline",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline aws_elastictranscoder_pipeline}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        input_bucket: builtins.str,
        role: builtins.str,
        aws_kms_key_arn: typing.Optional[builtins.str] = None,
        content_config: typing.Optional[typing.Union["ElastictranscoderPipelineContentConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        content_config_permissions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ElastictranscoderPipelineContentConfigPermissions", typing.Dict[builtins.str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        notifications: typing.Optional[typing.Union["ElastictranscoderPipelineNotifications", typing.Dict[builtins.str, typing.Any]]] = None,
        output_bucket: typing.Optional[builtins.str] = None,
        thumbnail_config: typing.Optional[typing.Union["ElastictranscoderPipelineThumbnailConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        thumbnail_config_permissions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ElastictranscoderPipelineThumbnailConfigPermissions", typing.Dict[builtins.str, typing.Any]]]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline aws_elastictranscoder_pipeline} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param input_bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#input_bucket ElastictranscoderPipeline#input_bucket}.
        :param role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#role ElastictranscoderPipeline#role}.
        :param aws_kms_key_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#aws_kms_key_arn ElastictranscoderPipeline#aws_kms_key_arn}.
        :param content_config: content_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#content_config ElastictranscoderPipeline#content_config}
        :param content_config_permissions: content_config_permissions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#content_config_permissions ElastictranscoderPipeline#content_config_permissions}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#id ElastictranscoderPipeline#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#name ElastictranscoderPipeline#name}.
        :param notifications: notifications block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#notifications ElastictranscoderPipeline#notifications}
        :param output_bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#output_bucket ElastictranscoderPipeline#output_bucket}.
        :param thumbnail_config: thumbnail_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#thumbnail_config ElastictranscoderPipeline#thumbnail_config}
        :param thumbnail_config_permissions: thumbnail_config_permissions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#thumbnail_config_permissions ElastictranscoderPipeline#thumbnail_config_permissions}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8206339e19b742dfea5df7e73062be9fc2eef2862b1ca1ce2a55e41c7daeaf2a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ElastictranscoderPipelineConfig(
            input_bucket=input_bucket,
            role=role,
            aws_kms_key_arn=aws_kms_key_arn,
            content_config=content_config,
            content_config_permissions=content_config_permissions,
            id=id,
            name=name,
            notifications=notifications,
            output_bucket=output_bucket,
            thumbnail_config=thumbnail_config,
            thumbnail_config_permissions=thumbnail_config_permissions,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putContentConfig")
    def put_content_config(
        self,
        *,
        bucket: typing.Optional[builtins.str] = None,
        storage_class: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#bucket ElastictranscoderPipeline#bucket}.
        :param storage_class: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#storage_class ElastictranscoderPipeline#storage_class}.
        '''
        value = ElastictranscoderPipelineContentConfig(
            bucket=bucket, storage_class=storage_class
        )

        return typing.cast(None, jsii.invoke(self, "putContentConfig", [value]))

    @jsii.member(jsii_name="putContentConfigPermissions")
    def put_content_config_permissions(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ElastictranscoderPipelineContentConfigPermissions", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a459fbce11d9e3006272dedef00ae8bb6efdfa834a2526db6e218ae2a68321bf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putContentConfigPermissions", [value]))

    @jsii.member(jsii_name="putNotifications")
    def put_notifications(
        self,
        *,
        completed: typing.Optional[builtins.str] = None,
        error: typing.Optional[builtins.str] = None,
        progressing: typing.Optional[builtins.str] = None,
        warning: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param completed: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#completed ElastictranscoderPipeline#completed}.
        :param error: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#error ElastictranscoderPipeline#error}.
        :param progressing: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#progressing ElastictranscoderPipeline#progressing}.
        :param warning: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#warning ElastictranscoderPipeline#warning}.
        '''
        value = ElastictranscoderPipelineNotifications(
            completed=completed, error=error, progressing=progressing, warning=warning
        )

        return typing.cast(None, jsii.invoke(self, "putNotifications", [value]))

    @jsii.member(jsii_name="putThumbnailConfig")
    def put_thumbnail_config(
        self,
        *,
        bucket: typing.Optional[builtins.str] = None,
        storage_class: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#bucket ElastictranscoderPipeline#bucket}.
        :param storage_class: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#storage_class ElastictranscoderPipeline#storage_class}.
        '''
        value = ElastictranscoderPipelineThumbnailConfig(
            bucket=bucket, storage_class=storage_class
        )

        return typing.cast(None, jsii.invoke(self, "putThumbnailConfig", [value]))

    @jsii.member(jsii_name="putThumbnailConfigPermissions")
    def put_thumbnail_config_permissions(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ElastictranscoderPipelineThumbnailConfigPermissions", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__170a48a2d288307e346875c28a9a8b4d6bb8a437b6073bfe14ade9f228d8124e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putThumbnailConfigPermissions", [value]))

    @jsii.member(jsii_name="resetAwsKmsKeyArn")
    def reset_aws_kms_key_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsKmsKeyArn", []))

    @jsii.member(jsii_name="resetContentConfig")
    def reset_content_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContentConfig", []))

    @jsii.member(jsii_name="resetContentConfigPermissions")
    def reset_content_config_permissions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContentConfigPermissions", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetNotifications")
    def reset_notifications(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotifications", []))

    @jsii.member(jsii_name="resetOutputBucket")
    def reset_output_bucket(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOutputBucket", []))

    @jsii.member(jsii_name="resetThumbnailConfig")
    def reset_thumbnail_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetThumbnailConfig", []))

    @jsii.member(jsii_name="resetThumbnailConfigPermissions")
    def reset_thumbnail_config_permissions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetThumbnailConfigPermissions", []))

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
    @jsii.member(jsii_name="contentConfig")
    def content_config(self) -> "ElastictranscoderPipelineContentConfigOutputReference":
        return typing.cast("ElastictranscoderPipelineContentConfigOutputReference", jsii.get(self, "contentConfig"))

    @builtins.property
    @jsii.member(jsii_name="contentConfigPermissions")
    def content_config_permissions(
        self,
    ) -> "ElastictranscoderPipelineContentConfigPermissionsList":
        return typing.cast("ElastictranscoderPipelineContentConfigPermissionsList", jsii.get(self, "contentConfigPermissions"))

    @builtins.property
    @jsii.member(jsii_name="notifications")
    def notifications(self) -> "ElastictranscoderPipelineNotificationsOutputReference":
        return typing.cast("ElastictranscoderPipelineNotificationsOutputReference", jsii.get(self, "notifications"))

    @builtins.property
    @jsii.member(jsii_name="thumbnailConfig")
    def thumbnail_config(
        self,
    ) -> "ElastictranscoderPipelineThumbnailConfigOutputReference":
        return typing.cast("ElastictranscoderPipelineThumbnailConfigOutputReference", jsii.get(self, "thumbnailConfig"))

    @builtins.property
    @jsii.member(jsii_name="thumbnailConfigPermissions")
    def thumbnail_config_permissions(
        self,
    ) -> "ElastictranscoderPipelineThumbnailConfigPermissionsList":
        return typing.cast("ElastictranscoderPipelineThumbnailConfigPermissionsList", jsii.get(self, "thumbnailConfigPermissions"))

    @builtins.property
    @jsii.member(jsii_name="awsKmsKeyArnInput")
    def aws_kms_key_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "awsKmsKeyArnInput"))

    @builtins.property
    @jsii.member(jsii_name="contentConfigInput")
    def content_config_input(
        self,
    ) -> typing.Optional["ElastictranscoderPipelineContentConfig"]:
        return typing.cast(typing.Optional["ElastictranscoderPipelineContentConfig"], jsii.get(self, "contentConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="contentConfigPermissionsInput")
    def content_config_permissions_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ElastictranscoderPipelineContentConfigPermissions"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ElastictranscoderPipelineContentConfigPermissions"]]], jsii.get(self, "contentConfigPermissionsInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="inputBucketInput")
    def input_bucket_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "inputBucketInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="notificationsInput")
    def notifications_input(
        self,
    ) -> typing.Optional["ElastictranscoderPipelineNotifications"]:
        return typing.cast(typing.Optional["ElastictranscoderPipelineNotifications"], jsii.get(self, "notificationsInput"))

    @builtins.property
    @jsii.member(jsii_name="outputBucketInput")
    def output_bucket_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "outputBucketInput"))

    @builtins.property
    @jsii.member(jsii_name="roleInput")
    def role_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleInput"))

    @builtins.property
    @jsii.member(jsii_name="thumbnailConfigInput")
    def thumbnail_config_input(
        self,
    ) -> typing.Optional["ElastictranscoderPipelineThumbnailConfig"]:
        return typing.cast(typing.Optional["ElastictranscoderPipelineThumbnailConfig"], jsii.get(self, "thumbnailConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="thumbnailConfigPermissionsInput")
    def thumbnail_config_permissions_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ElastictranscoderPipelineThumbnailConfigPermissions"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ElastictranscoderPipelineThumbnailConfigPermissions"]]], jsii.get(self, "thumbnailConfigPermissionsInput"))

    @builtins.property
    @jsii.member(jsii_name="awsKmsKeyArn")
    def aws_kms_key_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "awsKmsKeyArn"))

    @aws_kms_key_arn.setter
    def aws_kms_key_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00a1ef47a3f342f21b23ae663fe7160bfbaad7a1a18dd8dd79d181f91d73fe2e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsKmsKeyArn", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b6e4b6e8e58b315c3b1e4ecab6a662009332d392ed26b28c1ac22d88a16c2835)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="inputBucket")
    def input_bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "inputBucket"))

    @input_bucket.setter
    def input_bucket(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1fbf826e2b5841da7470a2d1e6c47ad11a89ca1ae0eae18c2c5d4378488d7e9b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "inputBucket", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dfa98159944be9bc9e0c2b38917ea512c73b811ea86390b8b8a313e2c3819435)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="outputBucket")
    def output_bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "outputBucket"))

    @output_bucket.setter
    def output_bucket(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26b900055461da11c52ea33b350079dd131fa5f6149c187dcf8acb2376309ef0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "outputBucket", value)

    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "role"))

    @role.setter
    def role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e18e25bf77f3f48d29c846467ef3fe82d370a02f052dc1957b96a553ec485d82)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "role", value)


@jsii.data_type(
    jsii_type="aws.elastictranscoderPipeline.ElastictranscoderPipelineConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "input_bucket": "inputBucket",
        "role": "role",
        "aws_kms_key_arn": "awsKmsKeyArn",
        "content_config": "contentConfig",
        "content_config_permissions": "contentConfigPermissions",
        "id": "id",
        "name": "name",
        "notifications": "notifications",
        "output_bucket": "outputBucket",
        "thumbnail_config": "thumbnailConfig",
        "thumbnail_config_permissions": "thumbnailConfigPermissions",
    },
)
class ElastictranscoderPipelineConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        input_bucket: builtins.str,
        role: builtins.str,
        aws_kms_key_arn: typing.Optional[builtins.str] = None,
        content_config: typing.Optional[typing.Union["ElastictranscoderPipelineContentConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        content_config_permissions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ElastictranscoderPipelineContentConfigPermissions", typing.Dict[builtins.str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        notifications: typing.Optional[typing.Union["ElastictranscoderPipelineNotifications", typing.Dict[builtins.str, typing.Any]]] = None,
        output_bucket: typing.Optional[builtins.str] = None,
        thumbnail_config: typing.Optional[typing.Union["ElastictranscoderPipelineThumbnailConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        thumbnail_config_permissions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ElastictranscoderPipelineThumbnailConfigPermissions", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param input_bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#input_bucket ElastictranscoderPipeline#input_bucket}.
        :param role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#role ElastictranscoderPipeline#role}.
        :param aws_kms_key_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#aws_kms_key_arn ElastictranscoderPipeline#aws_kms_key_arn}.
        :param content_config: content_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#content_config ElastictranscoderPipeline#content_config}
        :param content_config_permissions: content_config_permissions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#content_config_permissions ElastictranscoderPipeline#content_config_permissions}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#id ElastictranscoderPipeline#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#name ElastictranscoderPipeline#name}.
        :param notifications: notifications block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#notifications ElastictranscoderPipeline#notifications}
        :param output_bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#output_bucket ElastictranscoderPipeline#output_bucket}.
        :param thumbnail_config: thumbnail_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#thumbnail_config ElastictranscoderPipeline#thumbnail_config}
        :param thumbnail_config_permissions: thumbnail_config_permissions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#thumbnail_config_permissions ElastictranscoderPipeline#thumbnail_config_permissions}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(content_config, dict):
            content_config = ElastictranscoderPipelineContentConfig(**content_config)
        if isinstance(notifications, dict):
            notifications = ElastictranscoderPipelineNotifications(**notifications)
        if isinstance(thumbnail_config, dict):
            thumbnail_config = ElastictranscoderPipelineThumbnailConfig(**thumbnail_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__062fb0ef70372c6a55dfb458237e0506ffb435158cfaf763c8d91363afcc80b0)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument input_bucket", value=input_bucket, expected_type=type_hints["input_bucket"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument aws_kms_key_arn", value=aws_kms_key_arn, expected_type=type_hints["aws_kms_key_arn"])
            check_type(argname="argument content_config", value=content_config, expected_type=type_hints["content_config"])
            check_type(argname="argument content_config_permissions", value=content_config_permissions, expected_type=type_hints["content_config_permissions"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument notifications", value=notifications, expected_type=type_hints["notifications"])
            check_type(argname="argument output_bucket", value=output_bucket, expected_type=type_hints["output_bucket"])
            check_type(argname="argument thumbnail_config", value=thumbnail_config, expected_type=type_hints["thumbnail_config"])
            check_type(argname="argument thumbnail_config_permissions", value=thumbnail_config_permissions, expected_type=type_hints["thumbnail_config_permissions"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "input_bucket": input_bucket,
            "role": role,
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
        if aws_kms_key_arn is not None:
            self._values["aws_kms_key_arn"] = aws_kms_key_arn
        if content_config is not None:
            self._values["content_config"] = content_config
        if content_config_permissions is not None:
            self._values["content_config_permissions"] = content_config_permissions
        if id is not None:
            self._values["id"] = id
        if name is not None:
            self._values["name"] = name
        if notifications is not None:
            self._values["notifications"] = notifications
        if output_bucket is not None:
            self._values["output_bucket"] = output_bucket
        if thumbnail_config is not None:
            self._values["thumbnail_config"] = thumbnail_config
        if thumbnail_config_permissions is not None:
            self._values["thumbnail_config_permissions"] = thumbnail_config_permissions

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
    def input_bucket(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#input_bucket ElastictranscoderPipeline#input_bucket}.'''
        result = self._values.get("input_bucket")
        assert result is not None, "Required property 'input_bucket' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#role ElastictranscoderPipeline#role}.'''
        result = self._values.get("role")
        assert result is not None, "Required property 'role' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def aws_kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#aws_kms_key_arn ElastictranscoderPipeline#aws_kms_key_arn}.'''
        result = self._values.get("aws_kms_key_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def content_config(
        self,
    ) -> typing.Optional["ElastictranscoderPipelineContentConfig"]:
        '''content_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#content_config ElastictranscoderPipeline#content_config}
        '''
        result = self._values.get("content_config")
        return typing.cast(typing.Optional["ElastictranscoderPipelineContentConfig"], result)

    @builtins.property
    def content_config_permissions(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ElastictranscoderPipelineContentConfigPermissions"]]]:
        '''content_config_permissions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#content_config_permissions ElastictranscoderPipeline#content_config_permissions}
        '''
        result = self._values.get("content_config_permissions")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ElastictranscoderPipelineContentConfigPermissions"]]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#id ElastictranscoderPipeline#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#name ElastictranscoderPipeline#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def notifications(
        self,
    ) -> typing.Optional["ElastictranscoderPipelineNotifications"]:
        '''notifications block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#notifications ElastictranscoderPipeline#notifications}
        '''
        result = self._values.get("notifications")
        return typing.cast(typing.Optional["ElastictranscoderPipelineNotifications"], result)

    @builtins.property
    def output_bucket(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#output_bucket ElastictranscoderPipeline#output_bucket}.'''
        result = self._values.get("output_bucket")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def thumbnail_config(
        self,
    ) -> typing.Optional["ElastictranscoderPipelineThumbnailConfig"]:
        '''thumbnail_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#thumbnail_config ElastictranscoderPipeline#thumbnail_config}
        '''
        result = self._values.get("thumbnail_config")
        return typing.cast(typing.Optional["ElastictranscoderPipelineThumbnailConfig"], result)

    @builtins.property
    def thumbnail_config_permissions(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ElastictranscoderPipelineThumbnailConfigPermissions"]]]:
        '''thumbnail_config_permissions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#thumbnail_config_permissions ElastictranscoderPipeline#thumbnail_config_permissions}
        '''
        result = self._values.get("thumbnail_config_permissions")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ElastictranscoderPipelineThumbnailConfigPermissions"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastictranscoderPipelineConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.elastictranscoderPipeline.ElastictranscoderPipelineContentConfig",
    jsii_struct_bases=[],
    name_mapping={"bucket": "bucket", "storage_class": "storageClass"},
)
class ElastictranscoderPipelineContentConfig:
    def __init__(
        self,
        *,
        bucket: typing.Optional[builtins.str] = None,
        storage_class: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#bucket ElastictranscoderPipeline#bucket}.
        :param storage_class: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#storage_class ElastictranscoderPipeline#storage_class}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d518954c57f589e4d6a69071b6db818bb0b232e1f8b60b9514817f98556f1cb0)
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument storage_class", value=storage_class, expected_type=type_hints["storage_class"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if bucket is not None:
            self._values["bucket"] = bucket
        if storage_class is not None:
            self._values["storage_class"] = storage_class

    @builtins.property
    def bucket(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#bucket ElastictranscoderPipeline#bucket}.'''
        result = self._values.get("bucket")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def storage_class(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#storage_class ElastictranscoderPipeline#storage_class}.'''
        result = self._values.get("storage_class")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastictranscoderPipelineContentConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElastictranscoderPipelineContentConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.elastictranscoderPipeline.ElastictranscoderPipelineContentConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b055083f07406b78f481388cbaf40dd1e4cb0a2d5cd9b0d7cf343a312bff6457)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBucket")
    def reset_bucket(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucket", []))

    @jsii.member(jsii_name="resetStorageClass")
    def reset_storage_class(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageClass", []))

    @builtins.property
    @jsii.member(jsii_name="bucketInput")
    def bucket_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketInput"))

    @builtins.property
    @jsii.member(jsii_name="storageClassInput")
    def storage_class_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageClassInput"))

    @builtins.property
    @jsii.member(jsii_name="bucket")
    def bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucket"))

    @bucket.setter
    def bucket(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a070ff84e1e7a575bc7fc0aa62137a95c6df58a55edaac098bebc293463351d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucket", value)

    @builtins.property
    @jsii.member(jsii_name="storageClass")
    def storage_class(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageClass"))

    @storage_class.setter
    def storage_class(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b05e5a55a4e5c102874d975c5bc3e8b3882c947386e9a4bf39788ff204bb7331)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageClass", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ElastictranscoderPipelineContentConfig]:
        return typing.cast(typing.Optional[ElastictranscoderPipelineContentConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ElastictranscoderPipelineContentConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__90c31fbf72369605cd6902c6f2c0dd25ec2bcc54f6ba7562171e8fe77c53dc83)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.elastictranscoderPipeline.ElastictranscoderPipelineContentConfigPermissions",
    jsii_struct_bases=[],
    name_mapping={
        "access": "access",
        "grantee": "grantee",
        "grantee_type": "granteeType",
    },
)
class ElastictranscoderPipelineContentConfigPermissions:
    def __init__(
        self,
        *,
        access: typing.Optional[typing.Sequence[builtins.str]] = None,
        grantee: typing.Optional[builtins.str] = None,
        grantee_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param access: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#access ElastictranscoderPipeline#access}.
        :param grantee: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#grantee ElastictranscoderPipeline#grantee}.
        :param grantee_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#grantee_type ElastictranscoderPipeline#grantee_type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9f55fb139f7d9ccf3a8504ff8e8343d826d3c10fd365b1fe12c48a26f35dd8f)
            check_type(argname="argument access", value=access, expected_type=type_hints["access"])
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
            check_type(argname="argument grantee_type", value=grantee_type, expected_type=type_hints["grantee_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if access is not None:
            self._values["access"] = access
        if grantee is not None:
            self._values["grantee"] = grantee
        if grantee_type is not None:
            self._values["grantee_type"] = grantee_type

    @builtins.property
    def access(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#access ElastictranscoderPipeline#access}.'''
        result = self._values.get("access")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def grantee(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#grantee ElastictranscoderPipeline#grantee}.'''
        result = self._values.get("grantee")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def grantee_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#grantee_type ElastictranscoderPipeline#grantee_type}.'''
        result = self._values.get("grantee_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastictranscoderPipelineContentConfigPermissions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElastictranscoderPipelineContentConfigPermissionsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.elastictranscoderPipeline.ElastictranscoderPipelineContentConfigPermissionsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7265e148ab5af83f3e27b1b3f64c989e5a455d77cc444807f90f473ad7223e01)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ElastictranscoderPipelineContentConfigPermissionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27d68e131cfac0b41395eb5f10edb2750ed6460dae5130808c44ca937fda72a4)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ElastictranscoderPipelineContentConfigPermissionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1493cf72426bb309905e46669cd67c56f0847aff20a781aefe110a44b5910c85)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1db5737158f077a0d0b52d09f2bbf6ff41372549e72bd379a5ae8fe7f5ce8601)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0362dd3ab7a430211a71937e8bcbeda8cd515c72c12a60b2a9fb4f858dc5a7df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ElastictranscoderPipelineContentConfigPermissions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ElastictranscoderPipelineContentConfigPermissions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ElastictranscoderPipelineContentConfigPermissions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__775e89651a348985900e606c88f1e5caf43b5b7d8894f3261cd8b401d61d019f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElastictranscoderPipelineContentConfigPermissionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.elastictranscoderPipeline.ElastictranscoderPipelineContentConfigPermissionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__dbbea9c58aca270591c2ad853a4bfab81b23a893d96b21f98804a4faa5e1d741)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAccess")
    def reset_access(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccess", []))

    @jsii.member(jsii_name="resetGrantee")
    def reset_grantee(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGrantee", []))

    @jsii.member(jsii_name="resetGranteeType")
    def reset_grantee_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGranteeType", []))

    @builtins.property
    @jsii.member(jsii_name="accessInput")
    def access_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "accessInput"))

    @builtins.property
    @jsii.member(jsii_name="granteeInput")
    def grantee_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "granteeInput"))

    @builtins.property
    @jsii.member(jsii_name="granteeTypeInput")
    def grantee_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "granteeTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="access")
    def access(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "access"))

    @access.setter
    def access(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99717930e0906f8689d7236e0c1d73da4146b703da5408d2deebfb1618f67416)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "access", value)

    @builtins.property
    @jsii.member(jsii_name="grantee")
    def grantee(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "grantee"))

    @grantee.setter
    def grantee(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb0521637753ce0575a86482ea11f56ae118ae87da596c6ab5a5a18ea27439e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "grantee", value)

    @builtins.property
    @jsii.member(jsii_name="granteeType")
    def grantee_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "granteeType"))

    @grantee_type.setter
    def grantee_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c718b241b37ecdad80ffe46d0d073e0fa70942f06dee8f62732078a2afed2559)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "granteeType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ElastictranscoderPipelineContentConfigPermissions, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ElastictranscoderPipelineContentConfigPermissions, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ElastictranscoderPipelineContentConfigPermissions, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e94400b4064d5910913dab28e1360d5cc95fd980fda286e793525c3fbd971e4c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.elastictranscoderPipeline.ElastictranscoderPipelineNotifications",
    jsii_struct_bases=[],
    name_mapping={
        "completed": "completed",
        "error": "error",
        "progressing": "progressing",
        "warning": "warning",
    },
)
class ElastictranscoderPipelineNotifications:
    def __init__(
        self,
        *,
        completed: typing.Optional[builtins.str] = None,
        error: typing.Optional[builtins.str] = None,
        progressing: typing.Optional[builtins.str] = None,
        warning: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param completed: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#completed ElastictranscoderPipeline#completed}.
        :param error: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#error ElastictranscoderPipeline#error}.
        :param progressing: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#progressing ElastictranscoderPipeline#progressing}.
        :param warning: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#warning ElastictranscoderPipeline#warning}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7f0f582f2b215e1e6600f6da17fd1d351400017e4717cf262fae7135d1de471)
            check_type(argname="argument completed", value=completed, expected_type=type_hints["completed"])
            check_type(argname="argument error", value=error, expected_type=type_hints["error"])
            check_type(argname="argument progressing", value=progressing, expected_type=type_hints["progressing"])
            check_type(argname="argument warning", value=warning, expected_type=type_hints["warning"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if completed is not None:
            self._values["completed"] = completed
        if error is not None:
            self._values["error"] = error
        if progressing is not None:
            self._values["progressing"] = progressing
        if warning is not None:
            self._values["warning"] = warning

    @builtins.property
    def completed(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#completed ElastictranscoderPipeline#completed}.'''
        result = self._values.get("completed")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def error(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#error ElastictranscoderPipeline#error}.'''
        result = self._values.get("error")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def progressing(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#progressing ElastictranscoderPipeline#progressing}.'''
        result = self._values.get("progressing")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def warning(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#warning ElastictranscoderPipeline#warning}.'''
        result = self._values.get("warning")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastictranscoderPipelineNotifications(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElastictranscoderPipelineNotificationsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.elastictranscoderPipeline.ElastictranscoderPipelineNotificationsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__fac37e46b2f4fdafe9448673d871e551b900e7596b4727a839977a5f1a246a7f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCompleted")
    def reset_completed(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCompleted", []))

    @jsii.member(jsii_name="resetError")
    def reset_error(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetError", []))

    @jsii.member(jsii_name="resetProgressing")
    def reset_progressing(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProgressing", []))

    @jsii.member(jsii_name="resetWarning")
    def reset_warning(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWarning", []))

    @builtins.property
    @jsii.member(jsii_name="completedInput")
    def completed_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "completedInput"))

    @builtins.property
    @jsii.member(jsii_name="errorInput")
    def error_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "errorInput"))

    @builtins.property
    @jsii.member(jsii_name="progressingInput")
    def progressing_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "progressingInput"))

    @builtins.property
    @jsii.member(jsii_name="warningInput")
    def warning_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "warningInput"))

    @builtins.property
    @jsii.member(jsii_name="completed")
    def completed(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "completed"))

    @completed.setter
    def completed(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__453ffb7672176770b178499a1c0735bf111440417a6ae89b682d6d19d08a6881)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "completed", value)

    @builtins.property
    @jsii.member(jsii_name="error")
    def error(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "error"))

    @error.setter
    def error(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e38b2c5ca6d8d04d5dee96636999ada53c685ac4e7ed64b9b255994d1e14d8f3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "error", value)

    @builtins.property
    @jsii.member(jsii_name="progressing")
    def progressing(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "progressing"))

    @progressing.setter
    def progressing(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d37356f9fac972e15b1e4dd1a361fce84f3d365fdb2a5e3cb0c00c5cec7c68e3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "progressing", value)

    @builtins.property
    @jsii.member(jsii_name="warning")
    def warning(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "warning"))

    @warning.setter
    def warning(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4dfc621f2f6ca5216360d780a9e262c2776c715c38720a72912fc6a67d323d20)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "warning", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ElastictranscoderPipelineNotifications]:
        return typing.cast(typing.Optional[ElastictranscoderPipelineNotifications], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ElastictranscoderPipelineNotifications],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a54de92a406b54e1cb69609934e8b9d2a3390cbaf8472b054f4a89710973e487)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.elastictranscoderPipeline.ElastictranscoderPipelineThumbnailConfig",
    jsii_struct_bases=[],
    name_mapping={"bucket": "bucket", "storage_class": "storageClass"},
)
class ElastictranscoderPipelineThumbnailConfig:
    def __init__(
        self,
        *,
        bucket: typing.Optional[builtins.str] = None,
        storage_class: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#bucket ElastictranscoderPipeline#bucket}.
        :param storage_class: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#storage_class ElastictranscoderPipeline#storage_class}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb3de2429b4171d261dc3cda197991530f621d35c3f2b947fc5b1116c961add8)
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument storage_class", value=storage_class, expected_type=type_hints["storage_class"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if bucket is not None:
            self._values["bucket"] = bucket
        if storage_class is not None:
            self._values["storage_class"] = storage_class

    @builtins.property
    def bucket(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#bucket ElastictranscoderPipeline#bucket}.'''
        result = self._values.get("bucket")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def storage_class(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#storage_class ElastictranscoderPipeline#storage_class}.'''
        result = self._values.get("storage_class")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastictranscoderPipelineThumbnailConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElastictranscoderPipelineThumbnailConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.elastictranscoderPipeline.ElastictranscoderPipelineThumbnailConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__06052fb5be095c497b4dfbe1928c3e0ec96aeec1b3273642edb435a3eb349ade)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBucket")
    def reset_bucket(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucket", []))

    @jsii.member(jsii_name="resetStorageClass")
    def reset_storage_class(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageClass", []))

    @builtins.property
    @jsii.member(jsii_name="bucketInput")
    def bucket_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketInput"))

    @builtins.property
    @jsii.member(jsii_name="storageClassInput")
    def storage_class_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageClassInput"))

    @builtins.property
    @jsii.member(jsii_name="bucket")
    def bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucket"))

    @bucket.setter
    def bucket(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bfa7aaad9ca1b2b46a76bf7e809540e42a2aeb59160547cf3fd5c150ed9fda7f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucket", value)

    @builtins.property
    @jsii.member(jsii_name="storageClass")
    def storage_class(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageClass"))

    @storage_class.setter
    def storage_class(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4517dbda6bafa78f6238bc8234c8eadf7fe16b55ecac2bccafcc67319015008b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageClass", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ElastictranscoderPipelineThumbnailConfig]:
        return typing.cast(typing.Optional[ElastictranscoderPipelineThumbnailConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ElastictranscoderPipelineThumbnailConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29f67e30dd57f1feb03a4846f0ae7d26c31d90e2c2a6ac38eafb162dba1a80df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.elastictranscoderPipeline.ElastictranscoderPipelineThumbnailConfigPermissions",
    jsii_struct_bases=[],
    name_mapping={
        "access": "access",
        "grantee": "grantee",
        "grantee_type": "granteeType",
    },
)
class ElastictranscoderPipelineThumbnailConfigPermissions:
    def __init__(
        self,
        *,
        access: typing.Optional[typing.Sequence[builtins.str]] = None,
        grantee: typing.Optional[builtins.str] = None,
        grantee_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param access: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#access ElastictranscoderPipeline#access}.
        :param grantee: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#grantee ElastictranscoderPipeline#grantee}.
        :param grantee_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#grantee_type ElastictranscoderPipeline#grantee_type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8e2917abb3e264328ff3d1cb6254aa3bbf3a5ee4490fd258b8a9244ed690fc5)
            check_type(argname="argument access", value=access, expected_type=type_hints["access"])
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
            check_type(argname="argument grantee_type", value=grantee_type, expected_type=type_hints["grantee_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if access is not None:
            self._values["access"] = access
        if grantee is not None:
            self._values["grantee"] = grantee
        if grantee_type is not None:
            self._values["grantee_type"] = grantee_type

    @builtins.property
    def access(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#access ElastictranscoderPipeline#access}.'''
        result = self._values.get("access")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def grantee(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#grantee ElastictranscoderPipeline#grantee}.'''
        result = self._values.get("grantee")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def grantee_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#grantee_type ElastictranscoderPipeline#grantee_type}.'''
        result = self._values.get("grantee_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastictranscoderPipelineThumbnailConfigPermissions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElastictranscoderPipelineThumbnailConfigPermissionsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.elastictranscoderPipeline.ElastictranscoderPipelineThumbnailConfigPermissionsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__fd93cbd43525cbba1ab34cb2ae409d7cf197a792634031ebd390aaf1cf0d7cd1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ElastictranscoderPipelineThumbnailConfigPermissionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61e8834ded3cdb8f9947255a042fc175aa27b2cf27a260345298da57d6af2c0d)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ElastictranscoderPipelineThumbnailConfigPermissionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82680583dbdf7b408b5b0f09284a14725c03d5a4086486dc7ef52d5c4624f8a2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__45d12d734933769366af484b4c692b51558693214a4262f9e00064d87710b4a2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__dabb39974dfd3f8fe4c4be35f7e583828717ca7b6ae9849e22ffba8cf27be6f3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ElastictranscoderPipelineThumbnailConfigPermissions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ElastictranscoderPipelineThumbnailConfigPermissions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ElastictranscoderPipelineThumbnailConfigPermissions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d497f78997d4d42647ec24ef0089ea4c2058897975a4ccfbd56a21f45a8b27bf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElastictranscoderPipelineThumbnailConfigPermissionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.elastictranscoderPipeline.ElastictranscoderPipelineThumbnailConfigPermissionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__71a96b659e9684c77f4748bb0e0155a897fdc261c1d15a9b29d55cfe16c49f70)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAccess")
    def reset_access(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccess", []))

    @jsii.member(jsii_name="resetGrantee")
    def reset_grantee(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGrantee", []))

    @jsii.member(jsii_name="resetGranteeType")
    def reset_grantee_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGranteeType", []))

    @builtins.property
    @jsii.member(jsii_name="accessInput")
    def access_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "accessInput"))

    @builtins.property
    @jsii.member(jsii_name="granteeInput")
    def grantee_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "granteeInput"))

    @builtins.property
    @jsii.member(jsii_name="granteeTypeInput")
    def grantee_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "granteeTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="access")
    def access(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "access"))

    @access.setter
    def access(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62da38aab5ddfd139bd8cf3d9ce76856f673eeb597f6744df476070329fe6dac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "access", value)

    @builtins.property
    @jsii.member(jsii_name="grantee")
    def grantee(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "grantee"))

    @grantee.setter
    def grantee(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b5cc3b553ee48c83cd4b51df79657ec2d315f9930c2876dd0bab19ec98724e9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "grantee", value)

    @builtins.property
    @jsii.member(jsii_name="granteeType")
    def grantee_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "granteeType"))

    @grantee_type.setter
    def grantee_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e27aa298955b80d842bc2332a6329ae1176956e05734c61d64d69f81e7480b96)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "granteeType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ElastictranscoderPipelineThumbnailConfigPermissions, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ElastictranscoderPipelineThumbnailConfigPermissions, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ElastictranscoderPipelineThumbnailConfigPermissions, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7980f8c3783ccd1f217a0533d9e0007f33e5dd233e30c9f0b99555da3405c475)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ElastictranscoderPipeline",
    "ElastictranscoderPipelineConfig",
    "ElastictranscoderPipelineContentConfig",
    "ElastictranscoderPipelineContentConfigOutputReference",
    "ElastictranscoderPipelineContentConfigPermissions",
    "ElastictranscoderPipelineContentConfigPermissionsList",
    "ElastictranscoderPipelineContentConfigPermissionsOutputReference",
    "ElastictranscoderPipelineNotifications",
    "ElastictranscoderPipelineNotificationsOutputReference",
    "ElastictranscoderPipelineThumbnailConfig",
    "ElastictranscoderPipelineThumbnailConfigOutputReference",
    "ElastictranscoderPipelineThumbnailConfigPermissions",
    "ElastictranscoderPipelineThumbnailConfigPermissionsList",
    "ElastictranscoderPipelineThumbnailConfigPermissionsOutputReference",
]

publication.publish()

def _typecheckingstub__8206339e19b742dfea5df7e73062be9fc2eef2862b1ca1ce2a55e41c7daeaf2a(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    input_bucket: builtins.str,
    role: builtins.str,
    aws_kms_key_arn: typing.Optional[builtins.str] = None,
    content_config: typing.Optional[typing.Union[ElastictranscoderPipelineContentConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    content_config_permissions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ElastictranscoderPipelineContentConfigPermissions, typing.Dict[builtins.str, typing.Any]]]]] = None,
    id: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    notifications: typing.Optional[typing.Union[ElastictranscoderPipelineNotifications, typing.Dict[builtins.str, typing.Any]]] = None,
    output_bucket: typing.Optional[builtins.str] = None,
    thumbnail_config: typing.Optional[typing.Union[ElastictranscoderPipelineThumbnailConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    thumbnail_config_permissions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ElastictranscoderPipelineThumbnailConfigPermissions, typing.Dict[builtins.str, typing.Any]]]]] = None,
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

def _typecheckingstub__a459fbce11d9e3006272dedef00ae8bb6efdfa834a2526db6e218ae2a68321bf(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ElastictranscoderPipelineContentConfigPermissions, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__170a48a2d288307e346875c28a9a8b4d6bb8a437b6073bfe14ade9f228d8124e(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ElastictranscoderPipelineThumbnailConfigPermissions, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00a1ef47a3f342f21b23ae663fe7160bfbaad7a1a18dd8dd79d181f91d73fe2e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6e4b6e8e58b315c3b1e4ecab6a662009332d392ed26b28c1ac22d88a16c2835(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1fbf826e2b5841da7470a2d1e6c47ad11a89ca1ae0eae18c2c5d4378488d7e9b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dfa98159944be9bc9e0c2b38917ea512c73b811ea86390b8b8a313e2c3819435(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26b900055461da11c52ea33b350079dd131fa5f6149c187dcf8acb2376309ef0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e18e25bf77f3f48d29c846467ef3fe82d370a02f052dc1957b96a553ec485d82(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__062fb0ef70372c6a55dfb458237e0506ffb435158cfaf763c8d91363afcc80b0(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    input_bucket: builtins.str,
    role: builtins.str,
    aws_kms_key_arn: typing.Optional[builtins.str] = None,
    content_config: typing.Optional[typing.Union[ElastictranscoderPipelineContentConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    content_config_permissions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ElastictranscoderPipelineContentConfigPermissions, typing.Dict[builtins.str, typing.Any]]]]] = None,
    id: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    notifications: typing.Optional[typing.Union[ElastictranscoderPipelineNotifications, typing.Dict[builtins.str, typing.Any]]] = None,
    output_bucket: typing.Optional[builtins.str] = None,
    thumbnail_config: typing.Optional[typing.Union[ElastictranscoderPipelineThumbnailConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    thumbnail_config_permissions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ElastictranscoderPipelineThumbnailConfigPermissions, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d518954c57f589e4d6a69071b6db818bb0b232e1f8b60b9514817f98556f1cb0(
    *,
    bucket: typing.Optional[builtins.str] = None,
    storage_class: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b055083f07406b78f481388cbaf40dd1e4cb0a2d5cd9b0d7cf343a312bff6457(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a070ff84e1e7a575bc7fc0aa62137a95c6df58a55edaac098bebc293463351d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b05e5a55a4e5c102874d975c5bc3e8b3882c947386e9a4bf39788ff204bb7331(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90c31fbf72369605cd6902c6f2c0dd25ec2bcc54f6ba7562171e8fe77c53dc83(
    value: typing.Optional[ElastictranscoderPipelineContentConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9f55fb139f7d9ccf3a8504ff8e8343d826d3c10fd365b1fe12c48a26f35dd8f(
    *,
    access: typing.Optional[typing.Sequence[builtins.str]] = None,
    grantee: typing.Optional[builtins.str] = None,
    grantee_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7265e148ab5af83f3e27b1b3f64c989e5a455d77cc444807f90f473ad7223e01(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27d68e131cfac0b41395eb5f10edb2750ed6460dae5130808c44ca937fda72a4(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1493cf72426bb309905e46669cd67c56f0847aff20a781aefe110a44b5910c85(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1db5737158f077a0d0b52d09f2bbf6ff41372549e72bd379a5ae8fe7f5ce8601(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0362dd3ab7a430211a71937e8bcbeda8cd515c72c12a60b2a9fb4f858dc5a7df(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__775e89651a348985900e606c88f1e5caf43b5b7d8894f3261cd8b401d61d019f(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ElastictranscoderPipelineContentConfigPermissions]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dbbea9c58aca270591c2ad853a4bfab81b23a893d96b21f98804a4faa5e1d741(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99717930e0906f8689d7236e0c1d73da4146b703da5408d2deebfb1618f67416(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb0521637753ce0575a86482ea11f56ae118ae87da596c6ab5a5a18ea27439e0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c718b241b37ecdad80ffe46d0d073e0fa70942f06dee8f62732078a2afed2559(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e94400b4064d5910913dab28e1360d5cc95fd980fda286e793525c3fbd971e4c(
    value: typing.Optional[typing.Union[ElastictranscoderPipelineContentConfigPermissions, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7f0f582f2b215e1e6600f6da17fd1d351400017e4717cf262fae7135d1de471(
    *,
    completed: typing.Optional[builtins.str] = None,
    error: typing.Optional[builtins.str] = None,
    progressing: typing.Optional[builtins.str] = None,
    warning: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fac37e46b2f4fdafe9448673d871e551b900e7596b4727a839977a5f1a246a7f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__453ffb7672176770b178499a1c0735bf111440417a6ae89b682d6d19d08a6881(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e38b2c5ca6d8d04d5dee96636999ada53c685ac4e7ed64b9b255994d1e14d8f3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d37356f9fac972e15b1e4dd1a361fce84f3d365fdb2a5e3cb0c00c5cec7c68e3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4dfc621f2f6ca5216360d780a9e262c2776c715c38720a72912fc6a67d323d20(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a54de92a406b54e1cb69609934e8b9d2a3390cbaf8472b054f4a89710973e487(
    value: typing.Optional[ElastictranscoderPipelineNotifications],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb3de2429b4171d261dc3cda197991530f621d35c3f2b947fc5b1116c961add8(
    *,
    bucket: typing.Optional[builtins.str] = None,
    storage_class: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06052fb5be095c497b4dfbe1928c3e0ec96aeec1b3273642edb435a3eb349ade(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bfa7aaad9ca1b2b46a76bf7e809540e42a2aeb59160547cf3fd5c150ed9fda7f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4517dbda6bafa78f6238bc8234c8eadf7fe16b55ecac2bccafcc67319015008b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29f67e30dd57f1feb03a4846f0ae7d26c31d90e2c2a6ac38eafb162dba1a80df(
    value: typing.Optional[ElastictranscoderPipelineThumbnailConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8e2917abb3e264328ff3d1cb6254aa3bbf3a5ee4490fd258b8a9244ed690fc5(
    *,
    access: typing.Optional[typing.Sequence[builtins.str]] = None,
    grantee: typing.Optional[builtins.str] = None,
    grantee_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd93cbd43525cbba1ab34cb2ae409d7cf197a792634031ebd390aaf1cf0d7cd1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61e8834ded3cdb8f9947255a042fc175aa27b2cf27a260345298da57d6af2c0d(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82680583dbdf7b408b5b0f09284a14725c03d5a4086486dc7ef52d5c4624f8a2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45d12d734933769366af484b4c692b51558693214a4262f9e00064d87710b4a2(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dabb39974dfd3f8fe4c4be35f7e583828717ca7b6ae9849e22ffba8cf27be6f3(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d497f78997d4d42647ec24ef0089ea4c2058897975a4ccfbd56a21f45a8b27bf(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ElastictranscoderPipelineThumbnailConfigPermissions]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71a96b659e9684c77f4748bb0e0155a897fdc261c1d15a9b29d55cfe16c49f70(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62da38aab5ddfd139bd8cf3d9ce76856f673eeb597f6744df476070329fe6dac(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b5cc3b553ee48c83cd4b51df79657ec2d315f9930c2876dd0bab19ec98724e9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e27aa298955b80d842bc2332a6329ae1176956e05734c61d64d69f81e7480b96(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7980f8c3783ccd1f217a0533d9e0007f33e5dd233e30c9f0b99555da3405c475(
    value: typing.Optional[typing.Union[ElastictranscoderPipelineThumbnailConfigPermissions, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
