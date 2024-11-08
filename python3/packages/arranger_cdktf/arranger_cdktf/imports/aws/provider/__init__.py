'''
# `provider`

Refer to the Terraform Registory for docs: [`aws`](https://www.terraform.io/docs/providers/aws).
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


class AwsProvider(
    _cdktf_9a9027ec.TerraformProvider,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.provider.AwsProvider",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws aws}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        access_key: typing.Optional[builtins.str] = None,
        alias: typing.Optional[builtins.str] = None,
        allowed_account_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        assume_role: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["AwsProviderAssumeRole", typing.Dict[builtins.str, typing.Any]]]]] = None,
        assume_role_with_web_identity: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["AwsProviderAssumeRoleWithWebIdentity", typing.Dict[builtins.str, typing.Any]]]]] = None,
        custom_ca_bundle: typing.Optional[builtins.str] = None,
        default_tags: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["AwsProviderDefaultTags", typing.Dict[builtins.str, typing.Any]]]]] = None,
        ec2_metadata_service_endpoint: typing.Optional[builtins.str] = None,
        ec2_metadata_service_endpoint_mode: typing.Optional[builtins.str] = None,
        endpoints: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["AwsProviderEndpoints", typing.Dict[builtins.str, typing.Any]]]]] = None,
        forbidden_account_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        http_proxy: typing.Optional[builtins.str] = None,
        ignore_tags: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["AwsProviderIgnoreTags", typing.Dict[builtins.str, typing.Any]]]]] = None,
        insecure: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        max_retries: typing.Optional[jsii.Number] = None,
        profile: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        s3_force_path_style: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        s3_use_path_style: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        secret_key: typing.Optional[builtins.str] = None,
        shared_config_files: typing.Optional[typing.Sequence[builtins.str]] = None,
        shared_credentials_file: typing.Optional[builtins.str] = None,
        shared_credentials_files: typing.Optional[typing.Sequence[builtins.str]] = None,
        skip_credentials_validation: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        skip_get_ec2_platforms: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        skip_metadata_api_check: typing.Optional[builtins.str] = None,
        skip_region_validation: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        skip_requesting_account_id: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        sts_region: typing.Optional[builtins.str] = None,
        token: typing.Optional[builtins.str] = None,
        use_dualstack_endpoint: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        use_fips_endpoint: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws aws} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param access_key: The access key for API operations. You can retrieve this from the 'Security & Credentials' section of the AWS console. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#access_key AwsProvider#access_key}
        :param alias: Alias name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#alias AwsProvider#alias}
        :param allowed_account_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#allowed_account_ids AwsProvider#allowed_account_ids}.
        :param assume_role: assume_role block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#assume_role AwsProvider#assume_role}
        :param assume_role_with_web_identity: assume_role_with_web_identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#assume_role_with_web_identity AwsProvider#assume_role_with_web_identity}
        :param custom_ca_bundle: File containing custom root and intermediate certificates. Can also be configured using the ``AWS_CA_BUNDLE`` environment variable. (Setting ``ca_bundle`` in the shared config file is not supported.) Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#custom_ca_bundle AwsProvider#custom_ca_bundle}
        :param default_tags: default_tags block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#default_tags AwsProvider#default_tags}
        :param ec2_metadata_service_endpoint: Address of the EC2 metadata service endpoint to use. Can also be configured using the ``AWS_EC2_METADATA_SERVICE_ENDPOINT`` environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#ec2_metadata_service_endpoint AwsProvider#ec2_metadata_service_endpoint}
        :param ec2_metadata_service_endpoint_mode: Protocol to use with EC2 metadata service endpoint.Valid values are ``IPv4`` and ``IPv6``. Can also be configured using the ``AWS_EC2_METADATA_SERVICE_ENDPOINT_MODE`` environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#ec2_metadata_service_endpoint_mode AwsProvider#ec2_metadata_service_endpoint_mode}
        :param endpoints: endpoints block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#endpoints AwsProvider#endpoints}
        :param forbidden_account_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#forbidden_account_ids AwsProvider#forbidden_account_ids}.
        :param http_proxy: The address of an HTTP proxy to use when accessing the AWS API. Can also be configured using the ``HTTP_PROXY`` or ``HTTPS_PROXY`` environment variables. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#http_proxy AwsProvider#http_proxy}
        :param ignore_tags: ignore_tags block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#ignore_tags AwsProvider#ignore_tags}
        :param insecure: Explicitly allow the provider to perform "insecure" SSL requests. If omitted, default value is ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#insecure AwsProvider#insecure}
        :param max_retries: The maximum number of times an AWS API request is being executed. If the API request still fails, an error is thrown. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#max_retries AwsProvider#max_retries}
        :param profile: The profile for API operations. If not set, the default profile created with ``aws configure`` will be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#profile AwsProvider#profile}
        :param region: The region where AWS operations will take place. Examples are us-east-1, us-west-2, etc. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#region AwsProvider#region}
        :param s3_force_path_style: Set this to true to enable the request to use path-style addressing, i.e., https://s3.amazonaws.com/BUCKET/KEY. By default, the S3 client will use virtual hosted bucket addressing when possible (https://BUCKET.s3.amazonaws.com/KEY). Specific to the Amazon S3 service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#s3_force_path_style AwsProvider#s3_force_path_style}
        :param s3_use_path_style: Set this to true to enable the request to use path-style addressing, i.e., https://s3.amazonaws.com/BUCKET/KEY. By default, the S3 client will use virtual hosted bucket addressing when possible (https://BUCKET.s3.amazonaws.com/KEY). Specific to the Amazon S3 service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#s3_use_path_style AwsProvider#s3_use_path_style}
        :param secret_key: The secret key for API operations. You can retrieve this from the 'Security & Credentials' section of the AWS console. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#secret_key AwsProvider#secret_key}
        :param shared_config_files: List of paths to shared config files. If not set, defaults to [~/.aws/config]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#shared_config_files AwsProvider#shared_config_files}
        :param shared_credentials_file: The path to the shared credentials file. If not set, defaults to ~/.aws/credentials. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#shared_credentials_file AwsProvider#shared_credentials_file}
        :param shared_credentials_files: List of paths to shared credentials files. If not set, defaults to [~/.aws/credentials]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#shared_credentials_files AwsProvider#shared_credentials_files}
        :param skip_credentials_validation: Skip the credentials validation via STS API. Used for AWS API implementations that do not have STS available/implemented. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#skip_credentials_validation AwsProvider#skip_credentials_validation}
        :param skip_get_ec2_platforms: Skip getting the supported EC2 platforms. Used by users that don't have ec2:DescribeAccountAttributes permissions. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#skip_get_ec2_platforms AwsProvider#skip_get_ec2_platforms}
        :param skip_metadata_api_check: Skip the AWS Metadata API check. Used for AWS API implementations that do not have a metadata api endpoint. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#skip_metadata_api_check AwsProvider#skip_metadata_api_check}
        :param skip_region_validation: Skip static validation of region name. Used by users of alternative AWS-like APIs or users w/ access to regions that are not public (yet). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#skip_region_validation AwsProvider#skip_region_validation}
        :param skip_requesting_account_id: Skip requesting the account ID. Used for AWS API implementations that do not have IAM/STS API and/or metadata API. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#skip_requesting_account_id AwsProvider#skip_requesting_account_id}
        :param sts_region: The region where AWS STS operations will take place. Examples are us-east-1 and us-west-2. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#sts_region AwsProvider#sts_region}
        :param token: session token. A session token is only required if you are using temporary security credentials. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#token AwsProvider#token}
        :param use_dualstack_endpoint: Resolve an endpoint with DualStack capability. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#use_dualstack_endpoint AwsProvider#use_dualstack_endpoint}
        :param use_fips_endpoint: Resolve an endpoint with FIPS capability. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#use_fips_endpoint AwsProvider#use_fips_endpoint}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79d01e4a5ad4d4e2c4e7b0c6770bb00e0d2c0f2c9c2cad8981a6306d1abaf694)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = AwsProviderConfig(
            access_key=access_key,
            alias=alias,
            allowed_account_ids=allowed_account_ids,
            assume_role=assume_role,
            assume_role_with_web_identity=assume_role_with_web_identity,
            custom_ca_bundle=custom_ca_bundle,
            default_tags=default_tags,
            ec2_metadata_service_endpoint=ec2_metadata_service_endpoint,
            ec2_metadata_service_endpoint_mode=ec2_metadata_service_endpoint_mode,
            endpoints=endpoints,
            forbidden_account_ids=forbidden_account_ids,
            http_proxy=http_proxy,
            ignore_tags=ignore_tags,
            insecure=insecure,
            max_retries=max_retries,
            profile=profile,
            region=region,
            s3_force_path_style=s3_force_path_style,
            s3_use_path_style=s3_use_path_style,
            secret_key=secret_key,
            shared_config_files=shared_config_files,
            shared_credentials_file=shared_credentials_file,
            shared_credentials_files=shared_credentials_files,
            skip_credentials_validation=skip_credentials_validation,
            skip_get_ec2_platforms=skip_get_ec2_platforms,
            skip_metadata_api_check=skip_metadata_api_check,
            skip_region_validation=skip_region_validation,
            skip_requesting_account_id=skip_requesting_account_id,
            sts_region=sts_region,
            token=token,
            use_dualstack_endpoint=use_dualstack_endpoint,
            use_fips_endpoint=use_fips_endpoint,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="resetAccessKey")
    def reset_access_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessKey", []))

    @jsii.member(jsii_name="resetAlias")
    def reset_alias(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlias", []))

    @jsii.member(jsii_name="resetAllowedAccountIds")
    def reset_allowed_account_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedAccountIds", []))

    @jsii.member(jsii_name="resetAssumeRole")
    def reset_assume_role(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAssumeRole", []))

    @jsii.member(jsii_name="resetAssumeRoleWithWebIdentity")
    def reset_assume_role_with_web_identity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAssumeRoleWithWebIdentity", []))

    @jsii.member(jsii_name="resetCustomCaBundle")
    def reset_custom_ca_bundle(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomCaBundle", []))

    @jsii.member(jsii_name="resetDefaultTags")
    def reset_default_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultTags", []))

    @jsii.member(jsii_name="resetEc2MetadataServiceEndpoint")
    def reset_ec2_metadata_service_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEc2MetadataServiceEndpoint", []))

    @jsii.member(jsii_name="resetEc2MetadataServiceEndpointMode")
    def reset_ec2_metadata_service_endpoint_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEc2MetadataServiceEndpointMode", []))

    @jsii.member(jsii_name="resetEndpoints")
    def reset_endpoints(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEndpoints", []))

    @jsii.member(jsii_name="resetForbiddenAccountIds")
    def reset_forbidden_account_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForbiddenAccountIds", []))

    @jsii.member(jsii_name="resetHttpProxy")
    def reset_http_proxy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpProxy", []))

    @jsii.member(jsii_name="resetIgnoreTags")
    def reset_ignore_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIgnoreTags", []))

    @jsii.member(jsii_name="resetInsecure")
    def reset_insecure(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInsecure", []))

    @jsii.member(jsii_name="resetMaxRetries")
    def reset_max_retries(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxRetries", []))

    @jsii.member(jsii_name="resetProfile")
    def reset_profile(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProfile", []))

    @jsii.member(jsii_name="resetRegion")
    def reset_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegion", []))

    @jsii.member(jsii_name="resetS3ForcePathStyle")
    def reset_s3_force_path_style(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3ForcePathStyle", []))

    @jsii.member(jsii_name="resetS3UsePathStyle")
    def reset_s3_use_path_style(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3UsePathStyle", []))

    @jsii.member(jsii_name="resetSecretKey")
    def reset_secret_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecretKey", []))

    @jsii.member(jsii_name="resetSharedConfigFiles")
    def reset_shared_config_files(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSharedConfigFiles", []))

    @jsii.member(jsii_name="resetSharedCredentialsFile")
    def reset_shared_credentials_file(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSharedCredentialsFile", []))

    @jsii.member(jsii_name="resetSharedCredentialsFiles")
    def reset_shared_credentials_files(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSharedCredentialsFiles", []))

    @jsii.member(jsii_name="resetSkipCredentialsValidation")
    def reset_skip_credentials_validation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSkipCredentialsValidation", []))

    @jsii.member(jsii_name="resetSkipGetEc2Platforms")
    def reset_skip_get_ec2_platforms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSkipGetEc2Platforms", []))

    @jsii.member(jsii_name="resetSkipMetadataApiCheck")
    def reset_skip_metadata_api_check(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSkipMetadataApiCheck", []))

    @jsii.member(jsii_name="resetSkipRegionValidation")
    def reset_skip_region_validation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSkipRegionValidation", []))

    @jsii.member(jsii_name="resetSkipRequestingAccountId")
    def reset_skip_requesting_account_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSkipRequestingAccountId", []))

    @jsii.member(jsii_name="resetStsRegion")
    def reset_sts_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStsRegion", []))

    @jsii.member(jsii_name="resetToken")
    def reset_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetToken", []))

    @jsii.member(jsii_name="resetUseDualstackEndpoint")
    def reset_use_dualstack_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUseDualstackEndpoint", []))

    @jsii.member(jsii_name="resetUseFipsEndpoint")
    def reset_use_fips_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUseFipsEndpoint", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="accessKeyInput")
    def access_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="aliasInput")
    def alias_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aliasInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedAccountIdsInput")
    def allowed_account_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedAccountIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="assumeRoleInput")
    def assume_role_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AwsProviderAssumeRole"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AwsProviderAssumeRole"]]], jsii.get(self, "assumeRoleInput"))

    @builtins.property
    @jsii.member(jsii_name="assumeRoleWithWebIdentityInput")
    def assume_role_with_web_identity_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AwsProviderAssumeRoleWithWebIdentity"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AwsProviderAssumeRoleWithWebIdentity"]]], jsii.get(self, "assumeRoleWithWebIdentityInput"))

    @builtins.property
    @jsii.member(jsii_name="customCaBundleInput")
    def custom_ca_bundle_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customCaBundleInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultTagsInput")
    def default_tags_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AwsProviderDefaultTags"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AwsProviderDefaultTags"]]], jsii.get(self, "defaultTagsInput"))

    @builtins.property
    @jsii.member(jsii_name="ec2MetadataServiceEndpointInput")
    def ec2_metadata_service_endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ec2MetadataServiceEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="ec2MetadataServiceEndpointModeInput")
    def ec2_metadata_service_endpoint_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ec2MetadataServiceEndpointModeInput"))

    @builtins.property
    @jsii.member(jsii_name="endpointsInput")
    def endpoints_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AwsProviderEndpoints"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AwsProviderEndpoints"]]], jsii.get(self, "endpointsInput"))

    @builtins.property
    @jsii.member(jsii_name="forbiddenAccountIdsInput")
    def forbidden_account_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "forbiddenAccountIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="httpProxyInput")
    def http_proxy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "httpProxyInput"))

    @builtins.property
    @jsii.member(jsii_name="ignoreTagsInput")
    def ignore_tags_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AwsProviderIgnoreTags"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AwsProviderIgnoreTags"]]], jsii.get(self, "ignoreTagsInput"))

    @builtins.property
    @jsii.member(jsii_name="insecureInput")
    def insecure_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "insecureInput"))

    @builtins.property
    @jsii.member(jsii_name="maxRetriesInput")
    def max_retries_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxRetriesInput"))

    @builtins.property
    @jsii.member(jsii_name="profileInput")
    def profile_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "profileInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="s3ForcePathStyleInput")
    def s3_force_path_style_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "s3ForcePathStyleInput"))

    @builtins.property
    @jsii.member(jsii_name="s3UsePathStyleInput")
    def s3_use_path_style_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "s3UsePathStyleInput"))

    @builtins.property
    @jsii.member(jsii_name="secretKeyInput")
    def secret_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="sharedConfigFilesInput")
    def shared_config_files_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sharedConfigFilesInput"))

    @builtins.property
    @jsii.member(jsii_name="sharedCredentialsFileInput")
    def shared_credentials_file_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sharedCredentialsFileInput"))

    @builtins.property
    @jsii.member(jsii_name="sharedCredentialsFilesInput")
    def shared_credentials_files_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sharedCredentialsFilesInput"))

    @builtins.property
    @jsii.member(jsii_name="skipCredentialsValidationInput")
    def skip_credentials_validation_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "skipCredentialsValidationInput"))

    @builtins.property
    @jsii.member(jsii_name="skipGetEc2PlatformsInput")
    def skip_get_ec2_platforms_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "skipGetEc2PlatformsInput"))

    @builtins.property
    @jsii.member(jsii_name="skipMetadataApiCheckInput")
    def skip_metadata_api_check_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "skipMetadataApiCheckInput"))

    @builtins.property
    @jsii.member(jsii_name="skipRegionValidationInput")
    def skip_region_validation_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "skipRegionValidationInput"))

    @builtins.property
    @jsii.member(jsii_name="skipRequestingAccountIdInput")
    def skip_requesting_account_id_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "skipRequestingAccountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="stsRegionInput")
    def sts_region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stsRegionInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenInput")
    def token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenInput"))

    @builtins.property
    @jsii.member(jsii_name="useDualstackEndpointInput")
    def use_dualstack_endpoint_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "useDualstackEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="useFipsEndpointInput")
    def use_fips_endpoint_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "useFipsEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="accessKey")
    def access_key(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessKey"))

    @access_key.setter
    def access_key(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e6ddf7f277405d5d266ac279eeed43945038c221d186aaec2083aa727a2fd74)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessKey", value)

    @builtins.property
    @jsii.member(jsii_name="alias")
    def alias(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alias"))

    @alias.setter
    def alias(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__329c9ab4a6f5b6ec76799f3bdbaf3618175a02d88991f7201181538cf4d107e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alias", value)

    @builtins.property
    @jsii.member(jsii_name="allowedAccountIds")
    def allowed_account_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedAccountIds"))

    @allowed_account_ids.setter
    def allowed_account_ids(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e497afb24aeb860f0f55400131fc0586f41cf5b4babe13a0b66813f3ca58ff56)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedAccountIds", value)

    @builtins.property
    @jsii.member(jsii_name="assumeRole")
    def assume_role(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AwsProviderAssumeRole"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AwsProviderAssumeRole"]]], jsii.get(self, "assumeRole"))

    @assume_role.setter
    def assume_role(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AwsProviderAssumeRole"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7fac3aced6a489bc62137ca23b7e9558383a6f46e78ea2c04edb9e34f0c56200)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "assumeRole", value)

    @builtins.property
    @jsii.member(jsii_name="assumeRoleWithWebIdentity")
    def assume_role_with_web_identity(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AwsProviderAssumeRoleWithWebIdentity"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AwsProviderAssumeRoleWithWebIdentity"]]], jsii.get(self, "assumeRoleWithWebIdentity"))

    @assume_role_with_web_identity.setter
    def assume_role_with_web_identity(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AwsProviderAssumeRoleWithWebIdentity"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f044c1002b1d41fef039a037953d1d83870b30df9d8b866d08bb342e730afc8d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "assumeRoleWithWebIdentity", value)

    @builtins.property
    @jsii.member(jsii_name="customCaBundle")
    def custom_ca_bundle(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customCaBundle"))

    @custom_ca_bundle.setter
    def custom_ca_bundle(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__28c2a8167c3d2115ba3df955c955afc18730cd4b10688e4d9934283208385be2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customCaBundle", value)

    @builtins.property
    @jsii.member(jsii_name="defaultTags")
    def default_tags(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AwsProviderDefaultTags"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AwsProviderDefaultTags"]]], jsii.get(self, "defaultTags"))

    @default_tags.setter
    def default_tags(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AwsProviderDefaultTags"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45b2d53dd8713e1dd30367f0c8376dc6404c320280b908ccf4687ef5aa4b6835)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultTags", value)

    @builtins.property
    @jsii.member(jsii_name="ec2MetadataServiceEndpoint")
    def ec2_metadata_service_endpoint(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ec2MetadataServiceEndpoint"))

    @ec2_metadata_service_endpoint.setter
    def ec2_metadata_service_endpoint(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a12dac34870a5a7d31cb2d42b50dea386e855834da222b5bdb85c9b02be9c824)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ec2MetadataServiceEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="ec2MetadataServiceEndpointMode")
    def ec2_metadata_service_endpoint_mode(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ec2MetadataServiceEndpointMode"))

    @ec2_metadata_service_endpoint_mode.setter
    def ec2_metadata_service_endpoint_mode(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a0fecbb3502d66f4f7ac00b35c942b7ad269c8f3368ca481204974392387ea9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ec2MetadataServiceEndpointMode", value)

    @builtins.property
    @jsii.member(jsii_name="endpoints")
    def endpoints(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AwsProviderEndpoints"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AwsProviderEndpoints"]]], jsii.get(self, "endpoints"))

    @endpoints.setter
    def endpoints(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AwsProviderEndpoints"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44cf70c04669415b95c340040ea5ce3a2adaf476fe92ba5eebadd75435885dcf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpoints", value)

    @builtins.property
    @jsii.member(jsii_name="forbiddenAccountIds")
    def forbidden_account_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "forbiddenAccountIds"))

    @forbidden_account_ids.setter
    def forbidden_account_ids(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45514e4f66b3c0aa52ceecb9e7cf357a2541e84cdb33866a3a6da52659fc5aee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forbiddenAccountIds", value)

    @builtins.property
    @jsii.member(jsii_name="httpProxy")
    def http_proxy(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "httpProxy"))

    @http_proxy.setter
    def http_proxy(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d6ba31ab6d5a4111534cc9b5fc2d0d1b1dc350bda85c7bb6aebf3f10188ee6d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpProxy", value)

    @builtins.property
    @jsii.member(jsii_name="ignoreTags")
    def ignore_tags(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AwsProviderIgnoreTags"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AwsProviderIgnoreTags"]]], jsii.get(self, "ignoreTags"))

    @ignore_tags.setter
    def ignore_tags(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AwsProviderIgnoreTags"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__16683780d9eacaedd2cf65280152029a69a167e488b8623b61a651e0316ba5e3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ignoreTags", value)

    @builtins.property
    @jsii.member(jsii_name="insecure")
    def insecure(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "insecure"))

    @insecure.setter
    def insecure(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__094adf8bdd9b9a3ea41642f94a994cdf56f25da81d321c32c48ae66f447fc61b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "insecure", value)

    @builtins.property
    @jsii.member(jsii_name="maxRetries")
    def max_retries(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxRetries"))

    @max_retries.setter
    def max_retries(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b018725e01d4a3ade844dcc151c024b47aadf1c55e456cce61d709ed19e73f64)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxRetries", value)

    @builtins.property
    @jsii.member(jsii_name="profile")
    def profile(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "profile"))

    @profile.setter
    def profile(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b9184f99f37a3d220afd57022265d0af921611a203aa47ce115f952b53178496)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "profile", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "region"))

    @region.setter
    def region(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8c00dcfe02c07916c464a24f072f2a8e1d0390da62549baa91b191a4c4c14a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="s3ForcePathStyle")
    def s3_force_path_style(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "s3ForcePathStyle"))

    @s3_force_path_style.setter
    def s3_force_path_style(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__033897ae06184956e1dbf5dd7cf889aa87ebc0c00a086e085eaa5f6c9a5fcb40)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3ForcePathStyle", value)

    @builtins.property
    @jsii.member(jsii_name="s3UsePathStyle")
    def s3_use_path_style(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "s3UsePathStyle"))

    @s3_use_path_style.setter
    def s3_use_path_style(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__686b231465994a539b88bdf0e95707aa84c55bcc4b640ca69b81ff45ae596d42)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3UsePathStyle", value)

    @builtins.property
    @jsii.member(jsii_name="secretKey")
    def secret_key(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretKey"))

    @secret_key.setter
    def secret_key(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae41e856252e3b69e779fb6b346e6aae59c2d3fc39ea03583639b333ea9d4120)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretKey", value)

    @builtins.property
    @jsii.member(jsii_name="sharedConfigFiles")
    def shared_config_files(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sharedConfigFiles"))

    @shared_config_files.setter
    def shared_config_files(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1ba8c54427949734bd8a68812aa794c2bd4cb81504a45ed6bd55ccf84dab77b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sharedConfigFiles", value)

    @builtins.property
    @jsii.member(jsii_name="sharedCredentialsFile")
    def shared_credentials_file(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sharedCredentialsFile"))

    @shared_credentials_file.setter
    def shared_credentials_file(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b14d56a92dd2e162cde5054496ec5568fd9b23d3ef31e9a8cb8722b49e732cfe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sharedCredentialsFile", value)

    @builtins.property
    @jsii.member(jsii_name="sharedCredentialsFiles")
    def shared_credentials_files(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sharedCredentialsFiles"))

    @shared_credentials_files.setter
    def shared_credentials_files(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a40fc10d1dbf901352037de043909f55f97f4908b10e6e07028ed3177e70c373)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sharedCredentialsFiles", value)

    @builtins.property
    @jsii.member(jsii_name="skipCredentialsValidation")
    def skip_credentials_validation(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "skipCredentialsValidation"))

    @skip_credentials_validation.setter
    def skip_credentials_validation(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e443b795c5d55f61beb3fa4e4844cda29aede842a6a9023cd2442727bdb010eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "skipCredentialsValidation", value)

    @builtins.property
    @jsii.member(jsii_name="skipGetEc2Platforms")
    def skip_get_ec2_platforms(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "skipGetEc2Platforms"))

    @skip_get_ec2_platforms.setter
    def skip_get_ec2_platforms(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8932825103f712331b2dacdacaea36711d22567775b8bff2619418e45809bbda)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "skipGetEc2Platforms", value)

    @builtins.property
    @jsii.member(jsii_name="skipMetadataApiCheck")
    def skip_metadata_api_check(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "skipMetadataApiCheck"))

    @skip_metadata_api_check.setter
    def skip_metadata_api_check(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b20ba7ad50835e6972879f3fc419cc34b0d7de8aeb27e4080636d655409b14ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "skipMetadataApiCheck", value)

    @builtins.property
    @jsii.member(jsii_name="skipRegionValidation")
    def skip_region_validation(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "skipRegionValidation"))

    @skip_region_validation.setter
    def skip_region_validation(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aff73211f199187fe1e0e34b193e02104a1927899f4532f239b0321bc16f9be6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "skipRegionValidation", value)

    @builtins.property
    @jsii.member(jsii_name="skipRequestingAccountId")
    def skip_requesting_account_id(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "skipRequestingAccountId"))

    @skip_requesting_account_id.setter
    def skip_requesting_account_id(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb112861603b499c47cddbd7ddc62f0a1460f6dc6d3adfd38b847f3edf0cb2a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "skipRequestingAccountId", value)

    @builtins.property
    @jsii.member(jsii_name="stsRegion")
    def sts_region(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stsRegion"))

    @sts_region.setter
    def sts_region(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__517ccea055b266de0e5ffca9bb644a96a230832c75c334303ffc9cfc70ca167a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stsRegion", value)

    @builtins.property
    @jsii.member(jsii_name="token")
    def token(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "token"))

    @token.setter
    def token(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad511e3b75941062abca1b6ded90cac12aa0f47fa514934d3a2fd0ffbd2c46c1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "token", value)

    @builtins.property
    @jsii.member(jsii_name="useDualstackEndpoint")
    def use_dualstack_endpoint(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "useDualstackEndpoint"))

    @use_dualstack_endpoint.setter
    def use_dualstack_endpoint(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01d4cc1b5a3b984b8f43f432d6a3d5972761b9eee58d1fc2009a83b4de4b1050)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useDualstackEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="useFipsEndpoint")
    def use_fips_endpoint(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "useFipsEndpoint"))

    @use_fips_endpoint.setter
    def use_fips_endpoint(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de337857ad500f27ce46e3c2809ed7b32771c82c10b446dd4bc550dc4e4eb5ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useFipsEndpoint", value)


@jsii.data_type(
    jsii_type="aws.provider.AwsProviderAssumeRole",
    jsii_struct_bases=[],
    name_mapping={
        "duration": "duration",
        "duration_seconds": "durationSeconds",
        "external_id": "externalId",
        "policy": "policy",
        "policy_arns": "policyArns",
        "role_arn": "roleArn",
        "session_name": "sessionName",
        "source_identity": "sourceIdentity",
        "tags": "tags",
        "transitive_tag_keys": "transitiveTagKeys",
    },
)
class AwsProviderAssumeRole:
    def __init__(
        self,
        *,
        duration: typing.Optional[builtins.str] = None,
        duration_seconds: typing.Optional[jsii.Number] = None,
        external_id: typing.Optional[builtins.str] = None,
        policy: typing.Optional[builtins.str] = None,
        policy_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        role_arn: typing.Optional[builtins.str] = None,
        session_name: typing.Optional[builtins.str] = None,
        source_identity: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        transitive_tag_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param duration: The duration, between 15 minutes and 12 hours, of the role session. Valid time units are ns, us (or µs), ms, s, h, or m. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#duration AwsProvider#duration}
        :param duration_seconds: The duration, in seconds, of the role session. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#duration_seconds AwsProvider#duration_seconds}
        :param external_id: A unique identifier that might be required when you assume a role in another account. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#external_id AwsProvider#external_id}
        :param policy: IAM Policy JSON describing further restricting permissions for the IAM Role being assumed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#policy AwsProvider#policy}
        :param policy_arns: Amazon Resource Names (ARNs) of IAM Policies describing further restricting permissions for the IAM Role being assumed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#policy_arns AwsProvider#policy_arns}
        :param role_arn: Amazon Resource Name (ARN) of an IAM Role to assume prior to making API calls. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#role_arn AwsProvider#role_arn}
        :param session_name: An identifier for the assumed role session. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#session_name AwsProvider#session_name}
        :param source_identity: Source identity specified by the principal assuming the role. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#source_identity AwsProvider#source_identity}
        :param tags: Assume role session tags. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#tags AwsProvider#tags}
        :param transitive_tag_keys: Assume role session tag keys to pass to any subsequent sessions. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#transitive_tag_keys AwsProvider#transitive_tag_keys}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b0fff6151c5904dd835a46fffd2fd5f0197275551ff7e730c5617064f2f3e1b)
            check_type(argname="argument duration", value=duration, expected_type=type_hints["duration"])
            check_type(argname="argument duration_seconds", value=duration_seconds, expected_type=type_hints["duration_seconds"])
            check_type(argname="argument external_id", value=external_id, expected_type=type_hints["external_id"])
            check_type(argname="argument policy", value=policy, expected_type=type_hints["policy"])
            check_type(argname="argument policy_arns", value=policy_arns, expected_type=type_hints["policy_arns"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument session_name", value=session_name, expected_type=type_hints["session_name"])
            check_type(argname="argument source_identity", value=source_identity, expected_type=type_hints["source_identity"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument transitive_tag_keys", value=transitive_tag_keys, expected_type=type_hints["transitive_tag_keys"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if duration is not None:
            self._values["duration"] = duration
        if duration_seconds is not None:
            self._values["duration_seconds"] = duration_seconds
        if external_id is not None:
            self._values["external_id"] = external_id
        if policy is not None:
            self._values["policy"] = policy
        if policy_arns is not None:
            self._values["policy_arns"] = policy_arns
        if role_arn is not None:
            self._values["role_arn"] = role_arn
        if session_name is not None:
            self._values["session_name"] = session_name
        if source_identity is not None:
            self._values["source_identity"] = source_identity
        if tags is not None:
            self._values["tags"] = tags
        if transitive_tag_keys is not None:
            self._values["transitive_tag_keys"] = transitive_tag_keys

    @builtins.property
    def duration(self) -> typing.Optional[builtins.str]:
        '''The duration, between 15 minutes and 12 hours, of the role session.

        Valid time units are ns, us (or µs), ms, s, h, or m.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#duration AwsProvider#duration}
        '''
        result = self._values.get("duration")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def duration_seconds(self) -> typing.Optional[jsii.Number]:
        '''The duration, in seconds, of the role session.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#duration_seconds AwsProvider#duration_seconds}
        '''
        result = self._values.get("duration_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def external_id(self) -> typing.Optional[builtins.str]:
        '''A unique identifier that might be required when you assume a role in another account.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#external_id AwsProvider#external_id}
        '''
        result = self._values.get("external_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def policy(self) -> typing.Optional[builtins.str]:
        '''IAM Policy JSON describing further restricting permissions for the IAM Role being assumed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#policy AwsProvider#policy}
        '''
        result = self._values.get("policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def policy_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Amazon Resource Names (ARNs) of IAM Policies describing further restricting permissions for the IAM Role being assumed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#policy_arns AwsProvider#policy_arns}
        '''
        result = self._values.get("policy_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''Amazon Resource Name (ARN) of an IAM Role to assume prior to making API calls.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#role_arn AwsProvider#role_arn}
        '''
        result = self._values.get("role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def session_name(self) -> typing.Optional[builtins.str]:
        '''An identifier for the assumed role session.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#session_name AwsProvider#session_name}
        '''
        result = self._values.get("session_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_identity(self) -> typing.Optional[builtins.str]:
        '''Source identity specified by the principal assuming the role.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#source_identity AwsProvider#source_identity}
        '''
        result = self._values.get("source_identity")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Assume role session tags.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#tags AwsProvider#tags}
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def transitive_tag_keys(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Assume role session tag keys to pass to any subsequent sessions.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#transitive_tag_keys AwsProvider#transitive_tag_keys}
        '''
        result = self._values.get("transitive_tag_keys")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AwsProviderAssumeRole(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.provider.AwsProviderAssumeRoleWithWebIdentity",
    jsii_struct_bases=[],
    name_mapping={
        "duration": "duration",
        "policy": "policy",
        "policy_arns": "policyArns",
        "role_arn": "roleArn",
        "session_name": "sessionName",
        "web_identity_token": "webIdentityToken",
        "web_identity_token_file": "webIdentityTokenFile",
    },
)
class AwsProviderAssumeRoleWithWebIdentity:
    def __init__(
        self,
        *,
        duration: typing.Optional[builtins.str] = None,
        policy: typing.Optional[builtins.str] = None,
        policy_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        role_arn: typing.Optional[builtins.str] = None,
        session_name: typing.Optional[builtins.str] = None,
        web_identity_token: typing.Optional[builtins.str] = None,
        web_identity_token_file: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param duration: The duration, between 15 minutes and 12 hours, of the role session. Valid time units are ns, us (or µs), ms, s, h, or m. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#duration AwsProvider#duration}
        :param policy: IAM Policy JSON describing further restricting permissions for the IAM Role being assumed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#policy AwsProvider#policy}
        :param policy_arns: Amazon Resource Names (ARNs) of IAM Policies describing further restricting permissions for the IAM Role being assumed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#policy_arns AwsProvider#policy_arns}
        :param role_arn: Amazon Resource Name (ARN) of an IAM Role to assume prior to making API calls. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#role_arn AwsProvider#role_arn}
        :param session_name: An identifier for the assumed role session. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#session_name AwsProvider#session_name}
        :param web_identity_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#web_identity_token AwsProvider#web_identity_token}.
        :param web_identity_token_file: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#web_identity_token_file AwsProvider#web_identity_token_file}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a265297a0d9fa8e6ce4af0874bbe7cece183921599025e79896c84c87070063a)
            check_type(argname="argument duration", value=duration, expected_type=type_hints["duration"])
            check_type(argname="argument policy", value=policy, expected_type=type_hints["policy"])
            check_type(argname="argument policy_arns", value=policy_arns, expected_type=type_hints["policy_arns"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument session_name", value=session_name, expected_type=type_hints["session_name"])
            check_type(argname="argument web_identity_token", value=web_identity_token, expected_type=type_hints["web_identity_token"])
            check_type(argname="argument web_identity_token_file", value=web_identity_token_file, expected_type=type_hints["web_identity_token_file"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if duration is not None:
            self._values["duration"] = duration
        if policy is not None:
            self._values["policy"] = policy
        if policy_arns is not None:
            self._values["policy_arns"] = policy_arns
        if role_arn is not None:
            self._values["role_arn"] = role_arn
        if session_name is not None:
            self._values["session_name"] = session_name
        if web_identity_token is not None:
            self._values["web_identity_token"] = web_identity_token
        if web_identity_token_file is not None:
            self._values["web_identity_token_file"] = web_identity_token_file

    @builtins.property
    def duration(self) -> typing.Optional[builtins.str]:
        '''The duration, between 15 minutes and 12 hours, of the role session.

        Valid time units are ns, us (or µs), ms, s, h, or m.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#duration AwsProvider#duration}
        '''
        result = self._values.get("duration")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def policy(self) -> typing.Optional[builtins.str]:
        '''IAM Policy JSON describing further restricting permissions for the IAM Role being assumed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#policy AwsProvider#policy}
        '''
        result = self._values.get("policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def policy_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Amazon Resource Names (ARNs) of IAM Policies describing further restricting permissions for the IAM Role being assumed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#policy_arns AwsProvider#policy_arns}
        '''
        result = self._values.get("policy_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''Amazon Resource Name (ARN) of an IAM Role to assume prior to making API calls.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#role_arn AwsProvider#role_arn}
        '''
        result = self._values.get("role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def session_name(self) -> typing.Optional[builtins.str]:
        '''An identifier for the assumed role session.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#session_name AwsProvider#session_name}
        '''
        result = self._values.get("session_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def web_identity_token(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#web_identity_token AwsProvider#web_identity_token}.'''
        result = self._values.get("web_identity_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def web_identity_token_file(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#web_identity_token_file AwsProvider#web_identity_token_file}.'''
        result = self._values.get("web_identity_token_file")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AwsProviderAssumeRoleWithWebIdentity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.provider.AwsProviderConfig",
    jsii_struct_bases=[],
    name_mapping={
        "access_key": "accessKey",
        "alias": "alias",
        "allowed_account_ids": "allowedAccountIds",
        "assume_role": "assumeRole",
        "assume_role_with_web_identity": "assumeRoleWithWebIdentity",
        "custom_ca_bundle": "customCaBundle",
        "default_tags": "defaultTags",
        "ec2_metadata_service_endpoint": "ec2MetadataServiceEndpoint",
        "ec2_metadata_service_endpoint_mode": "ec2MetadataServiceEndpointMode",
        "endpoints": "endpoints",
        "forbidden_account_ids": "forbiddenAccountIds",
        "http_proxy": "httpProxy",
        "ignore_tags": "ignoreTags",
        "insecure": "insecure",
        "max_retries": "maxRetries",
        "profile": "profile",
        "region": "region",
        "s3_force_path_style": "s3ForcePathStyle",
        "s3_use_path_style": "s3UsePathStyle",
        "secret_key": "secretKey",
        "shared_config_files": "sharedConfigFiles",
        "shared_credentials_file": "sharedCredentialsFile",
        "shared_credentials_files": "sharedCredentialsFiles",
        "skip_credentials_validation": "skipCredentialsValidation",
        "skip_get_ec2_platforms": "skipGetEc2Platforms",
        "skip_metadata_api_check": "skipMetadataApiCheck",
        "skip_region_validation": "skipRegionValidation",
        "skip_requesting_account_id": "skipRequestingAccountId",
        "sts_region": "stsRegion",
        "token": "token",
        "use_dualstack_endpoint": "useDualstackEndpoint",
        "use_fips_endpoint": "useFipsEndpoint",
    },
)
class AwsProviderConfig:
    def __init__(
        self,
        *,
        access_key: typing.Optional[builtins.str] = None,
        alias: typing.Optional[builtins.str] = None,
        allowed_account_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        assume_role: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AwsProviderAssumeRole, typing.Dict[builtins.str, typing.Any]]]]] = None,
        assume_role_with_web_identity: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AwsProviderAssumeRoleWithWebIdentity, typing.Dict[builtins.str, typing.Any]]]]] = None,
        custom_ca_bundle: typing.Optional[builtins.str] = None,
        default_tags: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["AwsProviderDefaultTags", typing.Dict[builtins.str, typing.Any]]]]] = None,
        ec2_metadata_service_endpoint: typing.Optional[builtins.str] = None,
        ec2_metadata_service_endpoint_mode: typing.Optional[builtins.str] = None,
        endpoints: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["AwsProviderEndpoints", typing.Dict[builtins.str, typing.Any]]]]] = None,
        forbidden_account_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        http_proxy: typing.Optional[builtins.str] = None,
        ignore_tags: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["AwsProviderIgnoreTags", typing.Dict[builtins.str, typing.Any]]]]] = None,
        insecure: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        max_retries: typing.Optional[jsii.Number] = None,
        profile: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        s3_force_path_style: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        s3_use_path_style: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        secret_key: typing.Optional[builtins.str] = None,
        shared_config_files: typing.Optional[typing.Sequence[builtins.str]] = None,
        shared_credentials_file: typing.Optional[builtins.str] = None,
        shared_credentials_files: typing.Optional[typing.Sequence[builtins.str]] = None,
        skip_credentials_validation: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        skip_get_ec2_platforms: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        skip_metadata_api_check: typing.Optional[builtins.str] = None,
        skip_region_validation: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        skip_requesting_account_id: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        sts_region: typing.Optional[builtins.str] = None,
        token: typing.Optional[builtins.str] = None,
        use_dualstack_endpoint: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        use_fips_endpoint: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param access_key: The access key for API operations. You can retrieve this from the 'Security & Credentials' section of the AWS console. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#access_key AwsProvider#access_key}
        :param alias: Alias name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#alias AwsProvider#alias}
        :param allowed_account_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#allowed_account_ids AwsProvider#allowed_account_ids}.
        :param assume_role: assume_role block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#assume_role AwsProvider#assume_role}
        :param assume_role_with_web_identity: assume_role_with_web_identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#assume_role_with_web_identity AwsProvider#assume_role_with_web_identity}
        :param custom_ca_bundle: File containing custom root and intermediate certificates. Can also be configured using the ``AWS_CA_BUNDLE`` environment variable. (Setting ``ca_bundle`` in the shared config file is not supported.) Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#custom_ca_bundle AwsProvider#custom_ca_bundle}
        :param default_tags: default_tags block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#default_tags AwsProvider#default_tags}
        :param ec2_metadata_service_endpoint: Address of the EC2 metadata service endpoint to use. Can also be configured using the ``AWS_EC2_METADATA_SERVICE_ENDPOINT`` environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#ec2_metadata_service_endpoint AwsProvider#ec2_metadata_service_endpoint}
        :param ec2_metadata_service_endpoint_mode: Protocol to use with EC2 metadata service endpoint.Valid values are ``IPv4`` and ``IPv6``. Can also be configured using the ``AWS_EC2_METADATA_SERVICE_ENDPOINT_MODE`` environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#ec2_metadata_service_endpoint_mode AwsProvider#ec2_metadata_service_endpoint_mode}
        :param endpoints: endpoints block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#endpoints AwsProvider#endpoints}
        :param forbidden_account_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#forbidden_account_ids AwsProvider#forbidden_account_ids}.
        :param http_proxy: The address of an HTTP proxy to use when accessing the AWS API. Can also be configured using the ``HTTP_PROXY`` or ``HTTPS_PROXY`` environment variables. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#http_proxy AwsProvider#http_proxy}
        :param ignore_tags: ignore_tags block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#ignore_tags AwsProvider#ignore_tags}
        :param insecure: Explicitly allow the provider to perform "insecure" SSL requests. If omitted, default value is ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#insecure AwsProvider#insecure}
        :param max_retries: The maximum number of times an AWS API request is being executed. If the API request still fails, an error is thrown. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#max_retries AwsProvider#max_retries}
        :param profile: The profile for API operations. If not set, the default profile created with ``aws configure`` will be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#profile AwsProvider#profile}
        :param region: The region where AWS operations will take place. Examples are us-east-1, us-west-2, etc. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#region AwsProvider#region}
        :param s3_force_path_style: Set this to true to enable the request to use path-style addressing, i.e., https://s3.amazonaws.com/BUCKET/KEY. By default, the S3 client will use virtual hosted bucket addressing when possible (https://BUCKET.s3.amazonaws.com/KEY). Specific to the Amazon S3 service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#s3_force_path_style AwsProvider#s3_force_path_style}
        :param s3_use_path_style: Set this to true to enable the request to use path-style addressing, i.e., https://s3.amazonaws.com/BUCKET/KEY. By default, the S3 client will use virtual hosted bucket addressing when possible (https://BUCKET.s3.amazonaws.com/KEY). Specific to the Amazon S3 service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#s3_use_path_style AwsProvider#s3_use_path_style}
        :param secret_key: The secret key for API operations. You can retrieve this from the 'Security & Credentials' section of the AWS console. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#secret_key AwsProvider#secret_key}
        :param shared_config_files: List of paths to shared config files. If not set, defaults to [~/.aws/config]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#shared_config_files AwsProvider#shared_config_files}
        :param shared_credentials_file: The path to the shared credentials file. If not set, defaults to ~/.aws/credentials. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#shared_credentials_file AwsProvider#shared_credentials_file}
        :param shared_credentials_files: List of paths to shared credentials files. If not set, defaults to [~/.aws/credentials]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#shared_credentials_files AwsProvider#shared_credentials_files}
        :param skip_credentials_validation: Skip the credentials validation via STS API. Used for AWS API implementations that do not have STS available/implemented. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#skip_credentials_validation AwsProvider#skip_credentials_validation}
        :param skip_get_ec2_platforms: Skip getting the supported EC2 platforms. Used by users that don't have ec2:DescribeAccountAttributes permissions. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#skip_get_ec2_platforms AwsProvider#skip_get_ec2_platforms}
        :param skip_metadata_api_check: Skip the AWS Metadata API check. Used for AWS API implementations that do not have a metadata api endpoint. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#skip_metadata_api_check AwsProvider#skip_metadata_api_check}
        :param skip_region_validation: Skip static validation of region name. Used by users of alternative AWS-like APIs or users w/ access to regions that are not public (yet). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#skip_region_validation AwsProvider#skip_region_validation}
        :param skip_requesting_account_id: Skip requesting the account ID. Used for AWS API implementations that do not have IAM/STS API and/or metadata API. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#skip_requesting_account_id AwsProvider#skip_requesting_account_id}
        :param sts_region: The region where AWS STS operations will take place. Examples are us-east-1 and us-west-2. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#sts_region AwsProvider#sts_region}
        :param token: session token. A session token is only required if you are using temporary security credentials. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#token AwsProvider#token}
        :param use_dualstack_endpoint: Resolve an endpoint with DualStack capability. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#use_dualstack_endpoint AwsProvider#use_dualstack_endpoint}
        :param use_fips_endpoint: Resolve an endpoint with FIPS capability. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#use_fips_endpoint AwsProvider#use_fips_endpoint}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e9ecfe711aa56fab8e9a3d50b7f17efb93eb1eb278f40da236a53dd50521d10)
            check_type(argname="argument access_key", value=access_key, expected_type=type_hints["access_key"])
            check_type(argname="argument alias", value=alias, expected_type=type_hints["alias"])
            check_type(argname="argument allowed_account_ids", value=allowed_account_ids, expected_type=type_hints["allowed_account_ids"])
            check_type(argname="argument assume_role", value=assume_role, expected_type=type_hints["assume_role"])
            check_type(argname="argument assume_role_with_web_identity", value=assume_role_with_web_identity, expected_type=type_hints["assume_role_with_web_identity"])
            check_type(argname="argument custom_ca_bundle", value=custom_ca_bundle, expected_type=type_hints["custom_ca_bundle"])
            check_type(argname="argument default_tags", value=default_tags, expected_type=type_hints["default_tags"])
            check_type(argname="argument ec2_metadata_service_endpoint", value=ec2_metadata_service_endpoint, expected_type=type_hints["ec2_metadata_service_endpoint"])
            check_type(argname="argument ec2_metadata_service_endpoint_mode", value=ec2_metadata_service_endpoint_mode, expected_type=type_hints["ec2_metadata_service_endpoint_mode"])
            check_type(argname="argument endpoints", value=endpoints, expected_type=type_hints["endpoints"])
            check_type(argname="argument forbidden_account_ids", value=forbidden_account_ids, expected_type=type_hints["forbidden_account_ids"])
            check_type(argname="argument http_proxy", value=http_proxy, expected_type=type_hints["http_proxy"])
            check_type(argname="argument ignore_tags", value=ignore_tags, expected_type=type_hints["ignore_tags"])
            check_type(argname="argument insecure", value=insecure, expected_type=type_hints["insecure"])
            check_type(argname="argument max_retries", value=max_retries, expected_type=type_hints["max_retries"])
            check_type(argname="argument profile", value=profile, expected_type=type_hints["profile"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument s3_force_path_style", value=s3_force_path_style, expected_type=type_hints["s3_force_path_style"])
            check_type(argname="argument s3_use_path_style", value=s3_use_path_style, expected_type=type_hints["s3_use_path_style"])
            check_type(argname="argument secret_key", value=secret_key, expected_type=type_hints["secret_key"])
            check_type(argname="argument shared_config_files", value=shared_config_files, expected_type=type_hints["shared_config_files"])
            check_type(argname="argument shared_credentials_file", value=shared_credentials_file, expected_type=type_hints["shared_credentials_file"])
            check_type(argname="argument shared_credentials_files", value=shared_credentials_files, expected_type=type_hints["shared_credentials_files"])
            check_type(argname="argument skip_credentials_validation", value=skip_credentials_validation, expected_type=type_hints["skip_credentials_validation"])
            check_type(argname="argument skip_get_ec2_platforms", value=skip_get_ec2_platforms, expected_type=type_hints["skip_get_ec2_platforms"])
            check_type(argname="argument skip_metadata_api_check", value=skip_metadata_api_check, expected_type=type_hints["skip_metadata_api_check"])
            check_type(argname="argument skip_region_validation", value=skip_region_validation, expected_type=type_hints["skip_region_validation"])
            check_type(argname="argument skip_requesting_account_id", value=skip_requesting_account_id, expected_type=type_hints["skip_requesting_account_id"])
            check_type(argname="argument sts_region", value=sts_region, expected_type=type_hints["sts_region"])
            check_type(argname="argument token", value=token, expected_type=type_hints["token"])
            check_type(argname="argument use_dualstack_endpoint", value=use_dualstack_endpoint, expected_type=type_hints["use_dualstack_endpoint"])
            check_type(argname="argument use_fips_endpoint", value=use_fips_endpoint, expected_type=type_hints["use_fips_endpoint"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if access_key is not None:
            self._values["access_key"] = access_key
        if alias is not None:
            self._values["alias"] = alias
        if allowed_account_ids is not None:
            self._values["allowed_account_ids"] = allowed_account_ids
        if assume_role is not None:
            self._values["assume_role"] = assume_role
        if assume_role_with_web_identity is not None:
            self._values["assume_role_with_web_identity"] = assume_role_with_web_identity
        if custom_ca_bundle is not None:
            self._values["custom_ca_bundle"] = custom_ca_bundle
        if default_tags is not None:
            self._values["default_tags"] = default_tags
        if ec2_metadata_service_endpoint is not None:
            self._values["ec2_metadata_service_endpoint"] = ec2_metadata_service_endpoint
        if ec2_metadata_service_endpoint_mode is not None:
            self._values["ec2_metadata_service_endpoint_mode"] = ec2_metadata_service_endpoint_mode
        if endpoints is not None:
            self._values["endpoints"] = endpoints
        if forbidden_account_ids is not None:
            self._values["forbidden_account_ids"] = forbidden_account_ids
        if http_proxy is not None:
            self._values["http_proxy"] = http_proxy
        if ignore_tags is not None:
            self._values["ignore_tags"] = ignore_tags
        if insecure is not None:
            self._values["insecure"] = insecure
        if max_retries is not None:
            self._values["max_retries"] = max_retries
        if profile is not None:
            self._values["profile"] = profile
        if region is not None:
            self._values["region"] = region
        if s3_force_path_style is not None:
            self._values["s3_force_path_style"] = s3_force_path_style
        if s3_use_path_style is not None:
            self._values["s3_use_path_style"] = s3_use_path_style
        if secret_key is not None:
            self._values["secret_key"] = secret_key
        if shared_config_files is not None:
            self._values["shared_config_files"] = shared_config_files
        if shared_credentials_file is not None:
            self._values["shared_credentials_file"] = shared_credentials_file
        if shared_credentials_files is not None:
            self._values["shared_credentials_files"] = shared_credentials_files
        if skip_credentials_validation is not None:
            self._values["skip_credentials_validation"] = skip_credentials_validation
        if skip_get_ec2_platforms is not None:
            self._values["skip_get_ec2_platforms"] = skip_get_ec2_platforms
        if skip_metadata_api_check is not None:
            self._values["skip_metadata_api_check"] = skip_metadata_api_check
        if skip_region_validation is not None:
            self._values["skip_region_validation"] = skip_region_validation
        if skip_requesting_account_id is not None:
            self._values["skip_requesting_account_id"] = skip_requesting_account_id
        if sts_region is not None:
            self._values["sts_region"] = sts_region
        if token is not None:
            self._values["token"] = token
        if use_dualstack_endpoint is not None:
            self._values["use_dualstack_endpoint"] = use_dualstack_endpoint
        if use_fips_endpoint is not None:
            self._values["use_fips_endpoint"] = use_fips_endpoint

    @builtins.property
    def access_key(self) -> typing.Optional[builtins.str]:
        '''The access key for API operations. You can retrieve this from the 'Security & Credentials' section of the AWS console.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#access_key AwsProvider#access_key}
        '''
        result = self._values.get("access_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def alias(self) -> typing.Optional[builtins.str]:
        '''Alias name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#alias AwsProvider#alias}
        '''
        result = self._values.get("alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def allowed_account_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#allowed_account_ids AwsProvider#allowed_account_ids}.'''
        result = self._values.get("allowed_account_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def assume_role(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AwsProviderAssumeRole]]]:
        '''assume_role block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#assume_role AwsProvider#assume_role}
        '''
        result = self._values.get("assume_role")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AwsProviderAssumeRole]]], result)

    @builtins.property
    def assume_role_with_web_identity(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AwsProviderAssumeRoleWithWebIdentity]]]:
        '''assume_role_with_web_identity block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#assume_role_with_web_identity AwsProvider#assume_role_with_web_identity}
        '''
        result = self._values.get("assume_role_with_web_identity")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AwsProviderAssumeRoleWithWebIdentity]]], result)

    @builtins.property
    def custom_ca_bundle(self) -> typing.Optional[builtins.str]:
        '''File containing custom root and intermediate certificates.

        Can also be configured using the ``AWS_CA_BUNDLE`` environment variable. (Setting ``ca_bundle`` in the shared config file is not supported.)

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#custom_ca_bundle AwsProvider#custom_ca_bundle}
        '''
        result = self._values.get("custom_ca_bundle")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_tags(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AwsProviderDefaultTags"]]]:
        '''default_tags block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#default_tags AwsProvider#default_tags}
        '''
        result = self._values.get("default_tags")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AwsProviderDefaultTags"]]], result)

    @builtins.property
    def ec2_metadata_service_endpoint(self) -> typing.Optional[builtins.str]:
        '''Address of the EC2 metadata service endpoint to use. Can also be configured using the ``AWS_EC2_METADATA_SERVICE_ENDPOINT`` environment variable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#ec2_metadata_service_endpoint AwsProvider#ec2_metadata_service_endpoint}
        '''
        result = self._values.get("ec2_metadata_service_endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ec2_metadata_service_endpoint_mode(self) -> typing.Optional[builtins.str]:
        '''Protocol to use with EC2 metadata service endpoint.Valid values are ``IPv4`` and ``IPv6``. Can also be configured using the ``AWS_EC2_METADATA_SERVICE_ENDPOINT_MODE`` environment variable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#ec2_metadata_service_endpoint_mode AwsProvider#ec2_metadata_service_endpoint_mode}
        '''
        result = self._values.get("ec2_metadata_service_endpoint_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def endpoints(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AwsProviderEndpoints"]]]:
        '''endpoints block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#endpoints AwsProvider#endpoints}
        '''
        result = self._values.get("endpoints")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AwsProviderEndpoints"]]], result)

    @builtins.property
    def forbidden_account_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#forbidden_account_ids AwsProvider#forbidden_account_ids}.'''
        result = self._values.get("forbidden_account_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def http_proxy(self) -> typing.Optional[builtins.str]:
        '''The address of an HTTP proxy to use when accessing the AWS API.

        Can also be configured using the ``HTTP_PROXY`` or ``HTTPS_PROXY`` environment variables.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#http_proxy AwsProvider#http_proxy}
        '''
        result = self._values.get("http_proxy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ignore_tags(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AwsProviderIgnoreTags"]]]:
        '''ignore_tags block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#ignore_tags AwsProvider#ignore_tags}
        '''
        result = self._values.get("ignore_tags")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AwsProviderIgnoreTags"]]], result)

    @builtins.property
    def insecure(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Explicitly allow the provider to perform "insecure" SSL requests. If omitted, default value is ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#insecure AwsProvider#insecure}
        '''
        result = self._values.get("insecure")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def max_retries(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of times an AWS API request is being executed.

        If the API request still fails, an error is
        thrown.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#max_retries AwsProvider#max_retries}
        '''
        result = self._values.get("max_retries")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def profile(self) -> typing.Optional[builtins.str]:
        '''The profile for API operations. If not set, the default profile created with ``aws configure`` will be used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#profile AwsProvider#profile}
        '''
        result = self._values.get("profile")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''The region where AWS operations will take place. Examples are us-east-1, us-west-2, etc.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#region AwsProvider#region}
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def s3_force_path_style(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Set this to true to enable the request to use path-style addressing, i.e., https://s3.amazonaws.com/BUCKET/KEY. By default, the S3 client will use virtual hosted bucket addressing when possible (https://BUCKET.s3.amazonaws.com/KEY). Specific to the Amazon S3 service.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#s3_force_path_style AwsProvider#s3_force_path_style}
        '''
        result = self._values.get("s3_force_path_style")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def s3_use_path_style(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Set this to true to enable the request to use path-style addressing, i.e., https://s3.amazonaws.com/BUCKET/KEY. By default, the S3 client will use virtual hosted bucket addressing when possible (https://BUCKET.s3.amazonaws.com/KEY). Specific to the Amazon S3 service.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#s3_use_path_style AwsProvider#s3_use_path_style}
        '''
        result = self._values.get("s3_use_path_style")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def secret_key(self) -> typing.Optional[builtins.str]:
        '''The secret key for API operations. You can retrieve this from the 'Security & Credentials' section of the AWS console.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#secret_key AwsProvider#secret_key}
        '''
        result = self._values.get("secret_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def shared_config_files(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of paths to shared config files. If not set, defaults to [~/.aws/config].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#shared_config_files AwsProvider#shared_config_files}
        '''
        result = self._values.get("shared_config_files")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def shared_credentials_file(self) -> typing.Optional[builtins.str]:
        '''The path to the shared credentials file. If not set, defaults to ~/.aws/credentials.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#shared_credentials_file AwsProvider#shared_credentials_file}
        '''
        result = self._values.get("shared_credentials_file")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def shared_credentials_files(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of paths to shared credentials files. If not set, defaults to [~/.aws/credentials].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#shared_credentials_files AwsProvider#shared_credentials_files}
        '''
        result = self._values.get("shared_credentials_files")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def skip_credentials_validation(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Skip the credentials validation via STS API. Used for AWS API implementations that do not have STS available/implemented.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#skip_credentials_validation AwsProvider#skip_credentials_validation}
        '''
        result = self._values.get("skip_credentials_validation")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def skip_get_ec2_platforms(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Skip getting the supported EC2 platforms. Used by users that don't have ec2:DescribeAccountAttributes permissions.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#skip_get_ec2_platforms AwsProvider#skip_get_ec2_platforms}
        '''
        result = self._values.get("skip_get_ec2_platforms")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def skip_metadata_api_check(self) -> typing.Optional[builtins.str]:
        '''Skip the AWS Metadata API check. Used for AWS API implementations that do not have a metadata api endpoint.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#skip_metadata_api_check AwsProvider#skip_metadata_api_check}
        '''
        result = self._values.get("skip_metadata_api_check")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def skip_region_validation(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Skip static validation of region name.

        Used by users of alternative AWS-like APIs or users w/ access to regions that are not public (yet).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#skip_region_validation AwsProvider#skip_region_validation}
        '''
        result = self._values.get("skip_region_validation")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def skip_requesting_account_id(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Skip requesting the account ID. Used for AWS API implementations that do not have IAM/STS API and/or metadata API.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#skip_requesting_account_id AwsProvider#skip_requesting_account_id}
        '''
        result = self._values.get("skip_requesting_account_id")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def sts_region(self) -> typing.Optional[builtins.str]:
        '''The region where AWS STS operations will take place. Examples are us-east-1 and us-west-2.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#sts_region AwsProvider#sts_region}
        '''
        result = self._values.get("sts_region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def token(self) -> typing.Optional[builtins.str]:
        '''session token. A session token is only required if you are using temporary security credentials.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#token AwsProvider#token}
        '''
        result = self._values.get("token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def use_dualstack_endpoint(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Resolve an endpoint with DualStack capability.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#use_dualstack_endpoint AwsProvider#use_dualstack_endpoint}
        '''
        result = self._values.get("use_dualstack_endpoint")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def use_fips_endpoint(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Resolve an endpoint with FIPS capability.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#use_fips_endpoint AwsProvider#use_fips_endpoint}
        '''
        result = self._values.get("use_fips_endpoint")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AwsProviderConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.provider.AwsProviderDefaultTags",
    jsii_struct_bases=[],
    name_mapping={"tags": "tags"},
)
class AwsProviderDefaultTags:
    def __init__(
        self,
        *,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param tags: Resource tags to default across all resources. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#tags AwsProvider#tags}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb76121620bbaaac7f362352ab85bc4488f7ca86ee9a1c8bf07a2ded9499c487)
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Resource tags to default across all resources.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#tags AwsProvider#tags}
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AwsProviderDefaultTags(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.provider.AwsProviderEndpoints",
    jsii_struct_bases=[],
    name_mapping={
        "accessanalyzer": "accessanalyzer",
        "account": "account",
        "acm": "acm",
        "acmpca": "acmpca",
        "alexaforbusiness": "alexaforbusiness",
        "amg": "amg",
        "amp": "amp",
        "amplify": "amplify",
        "amplifybackend": "amplifybackend",
        "amplifyuibuilder": "amplifyuibuilder",
        "apigateway": "apigateway",
        "apigatewaymanagementapi": "apigatewaymanagementapi",
        "apigatewayv2": "apigatewayv2",
        "appautoscaling": "appautoscaling",
        "appconfig": "appconfig",
        "appconfigdata": "appconfigdata",
        "appflow": "appflow",
        "appintegrations": "appintegrations",
        "appintegrationsservice": "appintegrationsservice",
        "applicationautoscaling": "applicationautoscaling",
        "applicationcostprofiler": "applicationcostprofiler",
        "applicationdiscovery": "applicationdiscovery",
        "applicationdiscoveryservice": "applicationdiscoveryservice",
        "applicationinsights": "applicationinsights",
        "appmesh": "appmesh",
        "appregistry": "appregistry",
        "apprunner": "apprunner",
        "appstream": "appstream",
        "appsync": "appsync",
        "athena": "athena",
        "auditmanager": "auditmanager",
        "augmentedairuntime": "augmentedairuntime",
        "autoscaling": "autoscaling",
        "autoscalingplans": "autoscalingplans",
        "backup": "backup",
        "backupgateway": "backupgateway",
        "batch": "batch",
        "beanstalk": "beanstalk",
        "billingconductor": "billingconductor",
        "braket": "braket",
        "budgets": "budgets",
        "ce": "ce",
        "chime": "chime",
        "chimesdkidentity": "chimesdkidentity",
        "chimesdkmeetings": "chimesdkmeetings",
        "chimesdkmessaging": "chimesdkmessaging",
        "cloud9": "cloud9",
        "cloudcontrol": "cloudcontrol",
        "cloudcontrolapi": "cloudcontrolapi",
        "clouddirectory": "clouddirectory",
        "cloudformation": "cloudformation",
        "cloudfront": "cloudfront",
        "cloudhsm": "cloudhsm",
        "cloudhsmv2": "cloudhsmv2",
        "cloudsearch": "cloudsearch",
        "cloudsearchdomain": "cloudsearchdomain",
        "cloudtrail": "cloudtrail",
        "cloudwatch": "cloudwatch",
        "cloudwatchevents": "cloudwatchevents",
        "cloudwatchevidently": "cloudwatchevidently",
        "cloudwatchlog": "cloudwatchlog",
        "cloudwatchlogs": "cloudwatchlogs",
        "cloudwatchrum": "cloudwatchrum",
        "codeartifact": "codeartifact",
        "codebuild": "codebuild",
        "codecommit": "codecommit",
        "codedeploy": "codedeploy",
        "codeguruprofiler": "codeguruprofiler",
        "codegurureviewer": "codegurureviewer",
        "codepipeline": "codepipeline",
        "codestar": "codestar",
        "codestarconnections": "codestarconnections",
        "codestarnotifications": "codestarnotifications",
        "cognitoidentity": "cognitoidentity",
        "cognitoidentityprovider": "cognitoidentityprovider",
        "cognitoidp": "cognitoidp",
        "cognitosync": "cognitosync",
        "comprehend": "comprehend",
        "comprehendmedical": "comprehendmedical",
        "computeoptimizer": "computeoptimizer",
        "config": "config",
        "configservice": "configservice",
        "connect": "connect",
        "connectcontactlens": "connectcontactlens",
        "connectparticipant": "connectparticipant",
        "connectwisdomservice": "connectwisdomservice",
        "controltower": "controltower",
        "costandusagereportservice": "costandusagereportservice",
        "costexplorer": "costexplorer",
        "cur": "cur",
        "customerprofiles": "customerprofiles",
        "databasemigration": "databasemigration",
        "databasemigrationservice": "databasemigrationservice",
        "databrew": "databrew",
        "dataexchange": "dataexchange",
        "datapipeline": "datapipeline",
        "datasync": "datasync",
        "dax": "dax",
        "deploy": "deploy",
        "detective": "detective",
        "devicefarm": "devicefarm",
        "devopsguru": "devopsguru",
        "directconnect": "directconnect",
        "directoryservice": "directoryservice",
        "discovery": "discovery",
        "dlm": "dlm",
        "dms": "dms",
        "docdb": "docdb",
        "drs": "drs",
        "ds": "ds",
        "dynamodb": "dynamodb",
        "dynamodbstreams": "dynamodbstreams",
        "ebs": "ebs",
        "ec2": "ec2",
        "ec2_instanceconnect": "ec2Instanceconnect",
        "ecr": "ecr",
        "ecrpublic": "ecrpublic",
        "ecs": "ecs",
        "efs": "efs",
        "eks": "eks",
        "elasticache": "elasticache",
        "elasticbeanstalk": "elasticbeanstalk",
        "elasticinference": "elasticinference",
        "elasticloadbalancing": "elasticloadbalancing",
        "elasticloadbalancingv2": "elasticloadbalancingv2",
        "elasticsearch": "elasticsearch",
        "elasticsearchservice": "elasticsearchservice",
        "elastictranscoder": "elastictranscoder",
        "elb": "elb",
        "elbv2": "elbv2",
        "emr": "emr",
        "emrcontainers": "emrcontainers",
        "emrserverless": "emrserverless",
        "es": "es",
        "eventbridge": "eventbridge",
        "events": "events",
        "evidently": "evidently",
        "finspace": "finspace",
        "finspacedata": "finspacedata",
        "firehose": "firehose",
        "fis": "fis",
        "fms": "fms",
        "forecast": "forecast",
        "forecastquery": "forecastquery",
        "forecastqueryservice": "forecastqueryservice",
        "forecastservice": "forecastservice",
        "frauddetector": "frauddetector",
        "fsx": "fsx",
        "gamelift": "gamelift",
        "glacier": "glacier",
        "globalaccelerator": "globalaccelerator",
        "glue": "glue",
        "gluedatabrew": "gluedatabrew",
        "grafana": "grafana",
        "greengrass": "greengrass",
        "greengrassv2": "greengrassv2",
        "groundstation": "groundstation",
        "guardduty": "guardduty",
        "health": "health",
        "healthlake": "healthlake",
        "honeycode": "honeycode",
        "iam": "iam",
        "identitystore": "identitystore",
        "imagebuilder": "imagebuilder",
        "inspector": "inspector",
        "inspector2": "inspector2",
        "inspectorv2": "inspectorv2",
        "iot": "iot",
        "iot1_clickdevices": "iot1Clickdevices",
        "iot1_clickdevicesservice": "iot1Clickdevicesservice",
        "iot1_clickprojects": "iot1Clickprojects",
        "iotanalytics": "iotanalytics",
        "iotdata": "iotdata",
        "iotdataplane": "iotdataplane",
        "iotdeviceadvisor": "iotdeviceadvisor",
        "iotevents": "iotevents",
        "ioteventsdata": "ioteventsdata",
        "iotfleethub": "iotfleethub",
        "iotjobsdata": "iotjobsdata",
        "iotjobsdataplane": "iotjobsdataplane",
        "iotsecuretunneling": "iotsecuretunneling",
        "iotsitewise": "iotsitewise",
        "iotthingsgraph": "iotthingsgraph",
        "iottwinmaker": "iottwinmaker",
        "iotwireless": "iotwireless",
        "ivs": "ivs",
        "ivschat": "ivschat",
        "kafka": "kafka",
        "kafkaconnect": "kafkaconnect",
        "kendra": "kendra",
        "keyspaces": "keyspaces",
        "kinesis": "kinesis",
        "kinesisanalytics": "kinesisanalytics",
        "kinesisanalyticsv2": "kinesisanalyticsv2",
        "kinesisvideo": "kinesisvideo",
        "kinesisvideoarchivedmedia": "kinesisvideoarchivedmedia",
        "kinesisvideomedia": "kinesisvideomedia",
        "kinesisvideosignaling": "kinesisvideosignaling",
        "kinesisvideosignalingchannels": "kinesisvideosignalingchannels",
        "kms": "kms",
        "lakeformation": "lakeformation",
        "lambda_": "lambda",
        "lex": "lex",
        "lexmodelbuilding": "lexmodelbuilding",
        "lexmodelbuildingservice": "lexmodelbuildingservice",
        "lexmodels": "lexmodels",
        "lexmodelsv2": "lexmodelsv2",
        "lexruntime": "lexruntime",
        "lexruntimeservice": "lexruntimeservice",
        "lexruntimev2": "lexruntimev2",
        "lexv2_models": "lexv2Models",
        "lexv2_runtime": "lexv2Runtime",
        "licensemanager": "licensemanager",
        "lightsail": "lightsail",
        "location": "location",
        "locationservice": "locationservice",
        "logs": "logs",
        "lookoutequipment": "lookoutequipment",
        "lookoutforvision": "lookoutforvision",
        "lookoutmetrics": "lookoutmetrics",
        "lookoutvision": "lookoutvision",
        "machinelearning": "machinelearning",
        "macie": "macie",
        "macie2": "macie2",
        "managedblockchain": "managedblockchain",
        "managedgrafana": "managedgrafana",
        "marketplacecatalog": "marketplacecatalog",
        "marketplacecommerceanalytics": "marketplacecommerceanalytics",
        "marketplaceentitlement": "marketplaceentitlement",
        "marketplaceentitlementservice": "marketplaceentitlementservice",
        "marketplacemetering": "marketplacemetering",
        "mediaconnect": "mediaconnect",
        "mediaconvert": "mediaconvert",
        "medialive": "medialive",
        "mediapackage": "mediapackage",
        "mediapackagevod": "mediapackagevod",
        "mediastore": "mediastore",
        "mediastoredata": "mediastoredata",
        "mediatailor": "mediatailor",
        "memorydb": "memorydb",
        "meteringmarketplace": "meteringmarketplace",
        "mgh": "mgh",
        "mgn": "mgn",
        "migrationhub": "migrationhub",
        "migrationhubconfig": "migrationhubconfig",
        "migrationhubrefactorspaces": "migrationhubrefactorspaces",
        "migrationhubstrategy": "migrationhubstrategy",
        "migrationhubstrategyrecommendations": "migrationhubstrategyrecommendations",
        "mobile": "mobile",
        "mq": "mq",
        "msk": "msk",
        "mturk": "mturk",
        "mwaa": "mwaa",
        "neptune": "neptune",
        "networkfirewall": "networkfirewall",
        "networkmanager": "networkmanager",
        "nimble": "nimble",
        "nimblestudio": "nimblestudio",
        "opensearch": "opensearch",
        "opensearchserverless": "opensearchserverless",
        "opensearchservice": "opensearchservice",
        "opsworks": "opsworks",
        "opsworkscm": "opsworkscm",
        "organizations": "organizations",
        "outposts": "outposts",
        "panorama": "panorama",
        "personalize": "personalize",
        "personalizeevents": "personalizeevents",
        "personalizeruntime": "personalizeruntime",
        "pi": "pi",
        "pinpoint": "pinpoint",
        "pinpointemail": "pinpointemail",
        "pinpointsmsvoice": "pinpointsmsvoice",
        "pipes": "pipes",
        "polly": "polly",
        "pricing": "pricing",
        "prometheus": "prometheus",
        "prometheusservice": "prometheusservice",
        "proton": "proton",
        "qldb": "qldb",
        "qldbsession": "qldbsession",
        "quicksight": "quicksight",
        "ram": "ram",
        "rbin": "rbin",
        "rds": "rds",
        "rdsdata": "rdsdata",
        "rdsdataservice": "rdsdataservice",
        "recyclebin": "recyclebin",
        "redshift": "redshift",
        "redshiftdata": "redshiftdata",
        "redshiftdataapiservice": "redshiftdataapiservice",
        "redshiftserverless": "redshiftserverless",
        "rekognition": "rekognition",
        "resiliencehub": "resiliencehub",
        "resourceexplorer2": "resourceexplorer2",
        "resourcegroups": "resourcegroups",
        "resourcegroupstagging": "resourcegroupstagging",
        "resourcegroupstaggingapi": "resourcegroupstaggingapi",
        "robomaker": "robomaker",
        "rolesanywhere": "rolesanywhere",
        "route53": "route53",
        "route53_domains": "route53Domains",
        "route53_recoverycluster": "route53Recoverycluster",
        "route53_recoverycontrolconfig": "route53Recoverycontrolconfig",
        "route53_recoveryreadiness": "route53Recoveryreadiness",
        "route53_resolver": "route53Resolver",
        "rum": "rum",
        "s3": "s3",
        "s3_api": "s3Api",
        "s3_control": "s3Control",
        "s3_outposts": "s3Outposts",
        "sagemaker": "sagemaker",
        "sagemakera2_iruntime": "sagemakera2Iruntime",
        "sagemakeredge": "sagemakeredge",
        "sagemakeredgemanager": "sagemakeredgemanager",
        "sagemakerfeaturestoreruntime": "sagemakerfeaturestoreruntime",
        "sagemakerruntime": "sagemakerruntime",
        "savingsplans": "savingsplans",
        "scheduler": "scheduler",
        "schemas": "schemas",
        "sdb": "sdb",
        "secretsmanager": "secretsmanager",
        "securityhub": "securityhub",
        "serverlessapplicationrepository": "serverlessapplicationrepository",
        "serverlessapprepo": "serverlessapprepo",
        "serverlessrepo": "serverlessrepo",
        "servicecatalog": "servicecatalog",
        "servicecatalogappregistry": "servicecatalogappregistry",
        "servicediscovery": "servicediscovery",
        "servicequotas": "servicequotas",
        "ses": "ses",
        "sesv2": "sesv2",
        "sfn": "sfn",
        "shield": "shield",
        "signer": "signer",
        "simpledb": "simpledb",
        "sms": "sms",
        "snowball": "snowball",
        "snowdevicemanagement": "snowdevicemanagement",
        "sns": "sns",
        "sqs": "sqs",
        "ssm": "ssm",
        "ssmcontacts": "ssmcontacts",
        "ssmincidents": "ssmincidents",
        "sso": "sso",
        "ssoadmin": "ssoadmin",
        "ssooidc": "ssooidc",
        "stepfunctions": "stepfunctions",
        "storagegateway": "storagegateway",
        "sts": "sts",
        "support": "support",
        "swf": "swf",
        "synthetics": "synthetics",
        "textract": "textract",
        "timestreamquery": "timestreamquery",
        "timestreamwrite": "timestreamwrite",
        "transcribe": "transcribe",
        "transcribeservice": "transcribeservice",
        "transcribestreaming": "transcribestreaming",
        "transcribestreamingservice": "transcribestreamingservice",
        "transfer": "transfer",
        "translate": "translate",
        "voiceid": "voiceid",
        "waf": "waf",
        "wafregional": "wafregional",
        "wafv2": "wafv2",
        "wellarchitected": "wellarchitected",
        "wisdom": "wisdom",
        "workdocs": "workdocs",
        "worklink": "worklink",
        "workmail": "workmail",
        "workmailmessageflow": "workmailmessageflow",
        "workspaces": "workspaces",
        "workspacesweb": "workspacesweb",
        "xray": "xray",
    },
)
class AwsProviderEndpoints:
    def __init__(
        self,
        *,
        accessanalyzer: typing.Optional[builtins.str] = None,
        account: typing.Optional[builtins.str] = None,
        acm: typing.Optional[builtins.str] = None,
        acmpca: typing.Optional[builtins.str] = None,
        alexaforbusiness: typing.Optional[builtins.str] = None,
        amg: typing.Optional[builtins.str] = None,
        amp: typing.Optional[builtins.str] = None,
        amplify: typing.Optional[builtins.str] = None,
        amplifybackend: typing.Optional[builtins.str] = None,
        amplifyuibuilder: typing.Optional[builtins.str] = None,
        apigateway: typing.Optional[builtins.str] = None,
        apigatewaymanagementapi: typing.Optional[builtins.str] = None,
        apigatewayv2: typing.Optional[builtins.str] = None,
        appautoscaling: typing.Optional[builtins.str] = None,
        appconfig: typing.Optional[builtins.str] = None,
        appconfigdata: typing.Optional[builtins.str] = None,
        appflow: typing.Optional[builtins.str] = None,
        appintegrations: typing.Optional[builtins.str] = None,
        appintegrationsservice: typing.Optional[builtins.str] = None,
        applicationautoscaling: typing.Optional[builtins.str] = None,
        applicationcostprofiler: typing.Optional[builtins.str] = None,
        applicationdiscovery: typing.Optional[builtins.str] = None,
        applicationdiscoveryservice: typing.Optional[builtins.str] = None,
        applicationinsights: typing.Optional[builtins.str] = None,
        appmesh: typing.Optional[builtins.str] = None,
        appregistry: typing.Optional[builtins.str] = None,
        apprunner: typing.Optional[builtins.str] = None,
        appstream: typing.Optional[builtins.str] = None,
        appsync: typing.Optional[builtins.str] = None,
        athena: typing.Optional[builtins.str] = None,
        auditmanager: typing.Optional[builtins.str] = None,
        augmentedairuntime: typing.Optional[builtins.str] = None,
        autoscaling: typing.Optional[builtins.str] = None,
        autoscalingplans: typing.Optional[builtins.str] = None,
        backup: typing.Optional[builtins.str] = None,
        backupgateway: typing.Optional[builtins.str] = None,
        batch: typing.Optional[builtins.str] = None,
        beanstalk: typing.Optional[builtins.str] = None,
        billingconductor: typing.Optional[builtins.str] = None,
        braket: typing.Optional[builtins.str] = None,
        budgets: typing.Optional[builtins.str] = None,
        ce: typing.Optional[builtins.str] = None,
        chime: typing.Optional[builtins.str] = None,
        chimesdkidentity: typing.Optional[builtins.str] = None,
        chimesdkmeetings: typing.Optional[builtins.str] = None,
        chimesdkmessaging: typing.Optional[builtins.str] = None,
        cloud9: typing.Optional[builtins.str] = None,
        cloudcontrol: typing.Optional[builtins.str] = None,
        cloudcontrolapi: typing.Optional[builtins.str] = None,
        clouddirectory: typing.Optional[builtins.str] = None,
        cloudformation: typing.Optional[builtins.str] = None,
        cloudfront: typing.Optional[builtins.str] = None,
        cloudhsm: typing.Optional[builtins.str] = None,
        cloudhsmv2: typing.Optional[builtins.str] = None,
        cloudsearch: typing.Optional[builtins.str] = None,
        cloudsearchdomain: typing.Optional[builtins.str] = None,
        cloudtrail: typing.Optional[builtins.str] = None,
        cloudwatch: typing.Optional[builtins.str] = None,
        cloudwatchevents: typing.Optional[builtins.str] = None,
        cloudwatchevidently: typing.Optional[builtins.str] = None,
        cloudwatchlog: typing.Optional[builtins.str] = None,
        cloudwatchlogs: typing.Optional[builtins.str] = None,
        cloudwatchrum: typing.Optional[builtins.str] = None,
        codeartifact: typing.Optional[builtins.str] = None,
        codebuild: typing.Optional[builtins.str] = None,
        codecommit: typing.Optional[builtins.str] = None,
        codedeploy: typing.Optional[builtins.str] = None,
        codeguruprofiler: typing.Optional[builtins.str] = None,
        codegurureviewer: typing.Optional[builtins.str] = None,
        codepipeline: typing.Optional[builtins.str] = None,
        codestar: typing.Optional[builtins.str] = None,
        codestarconnections: typing.Optional[builtins.str] = None,
        codestarnotifications: typing.Optional[builtins.str] = None,
        cognitoidentity: typing.Optional[builtins.str] = None,
        cognitoidentityprovider: typing.Optional[builtins.str] = None,
        cognitoidp: typing.Optional[builtins.str] = None,
        cognitosync: typing.Optional[builtins.str] = None,
        comprehend: typing.Optional[builtins.str] = None,
        comprehendmedical: typing.Optional[builtins.str] = None,
        computeoptimizer: typing.Optional[builtins.str] = None,
        config: typing.Optional[builtins.str] = None,
        configservice: typing.Optional[builtins.str] = None,
        connect: typing.Optional[builtins.str] = None,
        connectcontactlens: typing.Optional[builtins.str] = None,
        connectparticipant: typing.Optional[builtins.str] = None,
        connectwisdomservice: typing.Optional[builtins.str] = None,
        controltower: typing.Optional[builtins.str] = None,
        costandusagereportservice: typing.Optional[builtins.str] = None,
        costexplorer: typing.Optional[builtins.str] = None,
        cur: typing.Optional[builtins.str] = None,
        customerprofiles: typing.Optional[builtins.str] = None,
        databasemigration: typing.Optional[builtins.str] = None,
        databasemigrationservice: typing.Optional[builtins.str] = None,
        databrew: typing.Optional[builtins.str] = None,
        dataexchange: typing.Optional[builtins.str] = None,
        datapipeline: typing.Optional[builtins.str] = None,
        datasync: typing.Optional[builtins.str] = None,
        dax: typing.Optional[builtins.str] = None,
        deploy: typing.Optional[builtins.str] = None,
        detective: typing.Optional[builtins.str] = None,
        devicefarm: typing.Optional[builtins.str] = None,
        devopsguru: typing.Optional[builtins.str] = None,
        directconnect: typing.Optional[builtins.str] = None,
        directoryservice: typing.Optional[builtins.str] = None,
        discovery: typing.Optional[builtins.str] = None,
        dlm: typing.Optional[builtins.str] = None,
        dms: typing.Optional[builtins.str] = None,
        docdb: typing.Optional[builtins.str] = None,
        drs: typing.Optional[builtins.str] = None,
        ds: typing.Optional[builtins.str] = None,
        dynamodb: typing.Optional[builtins.str] = None,
        dynamodbstreams: typing.Optional[builtins.str] = None,
        ebs: typing.Optional[builtins.str] = None,
        ec2: typing.Optional[builtins.str] = None,
        ec2_instanceconnect: typing.Optional[builtins.str] = None,
        ecr: typing.Optional[builtins.str] = None,
        ecrpublic: typing.Optional[builtins.str] = None,
        ecs: typing.Optional[builtins.str] = None,
        efs: typing.Optional[builtins.str] = None,
        eks: typing.Optional[builtins.str] = None,
        elasticache: typing.Optional[builtins.str] = None,
        elasticbeanstalk: typing.Optional[builtins.str] = None,
        elasticinference: typing.Optional[builtins.str] = None,
        elasticloadbalancing: typing.Optional[builtins.str] = None,
        elasticloadbalancingv2: typing.Optional[builtins.str] = None,
        elasticsearch: typing.Optional[builtins.str] = None,
        elasticsearchservice: typing.Optional[builtins.str] = None,
        elastictranscoder: typing.Optional[builtins.str] = None,
        elb: typing.Optional[builtins.str] = None,
        elbv2: typing.Optional[builtins.str] = None,
        emr: typing.Optional[builtins.str] = None,
        emrcontainers: typing.Optional[builtins.str] = None,
        emrserverless: typing.Optional[builtins.str] = None,
        es: typing.Optional[builtins.str] = None,
        eventbridge: typing.Optional[builtins.str] = None,
        events: typing.Optional[builtins.str] = None,
        evidently: typing.Optional[builtins.str] = None,
        finspace: typing.Optional[builtins.str] = None,
        finspacedata: typing.Optional[builtins.str] = None,
        firehose: typing.Optional[builtins.str] = None,
        fis: typing.Optional[builtins.str] = None,
        fms: typing.Optional[builtins.str] = None,
        forecast: typing.Optional[builtins.str] = None,
        forecastquery: typing.Optional[builtins.str] = None,
        forecastqueryservice: typing.Optional[builtins.str] = None,
        forecastservice: typing.Optional[builtins.str] = None,
        frauddetector: typing.Optional[builtins.str] = None,
        fsx: typing.Optional[builtins.str] = None,
        gamelift: typing.Optional[builtins.str] = None,
        glacier: typing.Optional[builtins.str] = None,
        globalaccelerator: typing.Optional[builtins.str] = None,
        glue: typing.Optional[builtins.str] = None,
        gluedatabrew: typing.Optional[builtins.str] = None,
        grafana: typing.Optional[builtins.str] = None,
        greengrass: typing.Optional[builtins.str] = None,
        greengrassv2: typing.Optional[builtins.str] = None,
        groundstation: typing.Optional[builtins.str] = None,
        guardduty: typing.Optional[builtins.str] = None,
        health: typing.Optional[builtins.str] = None,
        healthlake: typing.Optional[builtins.str] = None,
        honeycode: typing.Optional[builtins.str] = None,
        iam: typing.Optional[builtins.str] = None,
        identitystore: typing.Optional[builtins.str] = None,
        imagebuilder: typing.Optional[builtins.str] = None,
        inspector: typing.Optional[builtins.str] = None,
        inspector2: typing.Optional[builtins.str] = None,
        inspectorv2: typing.Optional[builtins.str] = None,
        iot: typing.Optional[builtins.str] = None,
        iot1_clickdevices: typing.Optional[builtins.str] = None,
        iot1_clickdevicesservice: typing.Optional[builtins.str] = None,
        iot1_clickprojects: typing.Optional[builtins.str] = None,
        iotanalytics: typing.Optional[builtins.str] = None,
        iotdata: typing.Optional[builtins.str] = None,
        iotdataplane: typing.Optional[builtins.str] = None,
        iotdeviceadvisor: typing.Optional[builtins.str] = None,
        iotevents: typing.Optional[builtins.str] = None,
        ioteventsdata: typing.Optional[builtins.str] = None,
        iotfleethub: typing.Optional[builtins.str] = None,
        iotjobsdata: typing.Optional[builtins.str] = None,
        iotjobsdataplane: typing.Optional[builtins.str] = None,
        iotsecuretunneling: typing.Optional[builtins.str] = None,
        iotsitewise: typing.Optional[builtins.str] = None,
        iotthingsgraph: typing.Optional[builtins.str] = None,
        iottwinmaker: typing.Optional[builtins.str] = None,
        iotwireless: typing.Optional[builtins.str] = None,
        ivs: typing.Optional[builtins.str] = None,
        ivschat: typing.Optional[builtins.str] = None,
        kafka: typing.Optional[builtins.str] = None,
        kafkaconnect: typing.Optional[builtins.str] = None,
        kendra: typing.Optional[builtins.str] = None,
        keyspaces: typing.Optional[builtins.str] = None,
        kinesis: typing.Optional[builtins.str] = None,
        kinesisanalytics: typing.Optional[builtins.str] = None,
        kinesisanalyticsv2: typing.Optional[builtins.str] = None,
        kinesisvideo: typing.Optional[builtins.str] = None,
        kinesisvideoarchivedmedia: typing.Optional[builtins.str] = None,
        kinesisvideomedia: typing.Optional[builtins.str] = None,
        kinesisvideosignaling: typing.Optional[builtins.str] = None,
        kinesisvideosignalingchannels: typing.Optional[builtins.str] = None,
        kms: typing.Optional[builtins.str] = None,
        lakeformation: typing.Optional[builtins.str] = None,
        lambda_: typing.Optional[builtins.str] = None,
        lex: typing.Optional[builtins.str] = None,
        lexmodelbuilding: typing.Optional[builtins.str] = None,
        lexmodelbuildingservice: typing.Optional[builtins.str] = None,
        lexmodels: typing.Optional[builtins.str] = None,
        lexmodelsv2: typing.Optional[builtins.str] = None,
        lexruntime: typing.Optional[builtins.str] = None,
        lexruntimeservice: typing.Optional[builtins.str] = None,
        lexruntimev2: typing.Optional[builtins.str] = None,
        lexv2_models: typing.Optional[builtins.str] = None,
        lexv2_runtime: typing.Optional[builtins.str] = None,
        licensemanager: typing.Optional[builtins.str] = None,
        lightsail: typing.Optional[builtins.str] = None,
        location: typing.Optional[builtins.str] = None,
        locationservice: typing.Optional[builtins.str] = None,
        logs: typing.Optional[builtins.str] = None,
        lookoutequipment: typing.Optional[builtins.str] = None,
        lookoutforvision: typing.Optional[builtins.str] = None,
        lookoutmetrics: typing.Optional[builtins.str] = None,
        lookoutvision: typing.Optional[builtins.str] = None,
        machinelearning: typing.Optional[builtins.str] = None,
        macie: typing.Optional[builtins.str] = None,
        macie2: typing.Optional[builtins.str] = None,
        managedblockchain: typing.Optional[builtins.str] = None,
        managedgrafana: typing.Optional[builtins.str] = None,
        marketplacecatalog: typing.Optional[builtins.str] = None,
        marketplacecommerceanalytics: typing.Optional[builtins.str] = None,
        marketplaceentitlement: typing.Optional[builtins.str] = None,
        marketplaceentitlementservice: typing.Optional[builtins.str] = None,
        marketplacemetering: typing.Optional[builtins.str] = None,
        mediaconnect: typing.Optional[builtins.str] = None,
        mediaconvert: typing.Optional[builtins.str] = None,
        medialive: typing.Optional[builtins.str] = None,
        mediapackage: typing.Optional[builtins.str] = None,
        mediapackagevod: typing.Optional[builtins.str] = None,
        mediastore: typing.Optional[builtins.str] = None,
        mediastoredata: typing.Optional[builtins.str] = None,
        mediatailor: typing.Optional[builtins.str] = None,
        memorydb: typing.Optional[builtins.str] = None,
        meteringmarketplace: typing.Optional[builtins.str] = None,
        mgh: typing.Optional[builtins.str] = None,
        mgn: typing.Optional[builtins.str] = None,
        migrationhub: typing.Optional[builtins.str] = None,
        migrationhubconfig: typing.Optional[builtins.str] = None,
        migrationhubrefactorspaces: typing.Optional[builtins.str] = None,
        migrationhubstrategy: typing.Optional[builtins.str] = None,
        migrationhubstrategyrecommendations: typing.Optional[builtins.str] = None,
        mobile: typing.Optional[builtins.str] = None,
        mq: typing.Optional[builtins.str] = None,
        msk: typing.Optional[builtins.str] = None,
        mturk: typing.Optional[builtins.str] = None,
        mwaa: typing.Optional[builtins.str] = None,
        neptune: typing.Optional[builtins.str] = None,
        networkfirewall: typing.Optional[builtins.str] = None,
        networkmanager: typing.Optional[builtins.str] = None,
        nimble: typing.Optional[builtins.str] = None,
        nimblestudio: typing.Optional[builtins.str] = None,
        opensearch: typing.Optional[builtins.str] = None,
        opensearchserverless: typing.Optional[builtins.str] = None,
        opensearchservice: typing.Optional[builtins.str] = None,
        opsworks: typing.Optional[builtins.str] = None,
        opsworkscm: typing.Optional[builtins.str] = None,
        organizations: typing.Optional[builtins.str] = None,
        outposts: typing.Optional[builtins.str] = None,
        panorama: typing.Optional[builtins.str] = None,
        personalize: typing.Optional[builtins.str] = None,
        personalizeevents: typing.Optional[builtins.str] = None,
        personalizeruntime: typing.Optional[builtins.str] = None,
        pi: typing.Optional[builtins.str] = None,
        pinpoint: typing.Optional[builtins.str] = None,
        pinpointemail: typing.Optional[builtins.str] = None,
        pinpointsmsvoice: typing.Optional[builtins.str] = None,
        pipes: typing.Optional[builtins.str] = None,
        polly: typing.Optional[builtins.str] = None,
        pricing: typing.Optional[builtins.str] = None,
        prometheus: typing.Optional[builtins.str] = None,
        prometheusservice: typing.Optional[builtins.str] = None,
        proton: typing.Optional[builtins.str] = None,
        qldb: typing.Optional[builtins.str] = None,
        qldbsession: typing.Optional[builtins.str] = None,
        quicksight: typing.Optional[builtins.str] = None,
        ram: typing.Optional[builtins.str] = None,
        rbin: typing.Optional[builtins.str] = None,
        rds: typing.Optional[builtins.str] = None,
        rdsdata: typing.Optional[builtins.str] = None,
        rdsdataservice: typing.Optional[builtins.str] = None,
        recyclebin: typing.Optional[builtins.str] = None,
        redshift: typing.Optional[builtins.str] = None,
        redshiftdata: typing.Optional[builtins.str] = None,
        redshiftdataapiservice: typing.Optional[builtins.str] = None,
        redshiftserverless: typing.Optional[builtins.str] = None,
        rekognition: typing.Optional[builtins.str] = None,
        resiliencehub: typing.Optional[builtins.str] = None,
        resourceexplorer2: typing.Optional[builtins.str] = None,
        resourcegroups: typing.Optional[builtins.str] = None,
        resourcegroupstagging: typing.Optional[builtins.str] = None,
        resourcegroupstaggingapi: typing.Optional[builtins.str] = None,
        robomaker: typing.Optional[builtins.str] = None,
        rolesanywhere: typing.Optional[builtins.str] = None,
        route53: typing.Optional[builtins.str] = None,
        route53_domains: typing.Optional[builtins.str] = None,
        route53_recoverycluster: typing.Optional[builtins.str] = None,
        route53_recoverycontrolconfig: typing.Optional[builtins.str] = None,
        route53_recoveryreadiness: typing.Optional[builtins.str] = None,
        route53_resolver: typing.Optional[builtins.str] = None,
        rum: typing.Optional[builtins.str] = None,
        s3: typing.Optional[builtins.str] = None,
        s3_api: typing.Optional[builtins.str] = None,
        s3_control: typing.Optional[builtins.str] = None,
        s3_outposts: typing.Optional[builtins.str] = None,
        sagemaker: typing.Optional[builtins.str] = None,
        sagemakera2_iruntime: typing.Optional[builtins.str] = None,
        sagemakeredge: typing.Optional[builtins.str] = None,
        sagemakeredgemanager: typing.Optional[builtins.str] = None,
        sagemakerfeaturestoreruntime: typing.Optional[builtins.str] = None,
        sagemakerruntime: typing.Optional[builtins.str] = None,
        savingsplans: typing.Optional[builtins.str] = None,
        scheduler: typing.Optional[builtins.str] = None,
        schemas: typing.Optional[builtins.str] = None,
        sdb: typing.Optional[builtins.str] = None,
        secretsmanager: typing.Optional[builtins.str] = None,
        securityhub: typing.Optional[builtins.str] = None,
        serverlessapplicationrepository: typing.Optional[builtins.str] = None,
        serverlessapprepo: typing.Optional[builtins.str] = None,
        serverlessrepo: typing.Optional[builtins.str] = None,
        servicecatalog: typing.Optional[builtins.str] = None,
        servicecatalogappregistry: typing.Optional[builtins.str] = None,
        servicediscovery: typing.Optional[builtins.str] = None,
        servicequotas: typing.Optional[builtins.str] = None,
        ses: typing.Optional[builtins.str] = None,
        sesv2: typing.Optional[builtins.str] = None,
        sfn: typing.Optional[builtins.str] = None,
        shield: typing.Optional[builtins.str] = None,
        signer: typing.Optional[builtins.str] = None,
        simpledb: typing.Optional[builtins.str] = None,
        sms: typing.Optional[builtins.str] = None,
        snowball: typing.Optional[builtins.str] = None,
        snowdevicemanagement: typing.Optional[builtins.str] = None,
        sns: typing.Optional[builtins.str] = None,
        sqs: typing.Optional[builtins.str] = None,
        ssm: typing.Optional[builtins.str] = None,
        ssmcontacts: typing.Optional[builtins.str] = None,
        ssmincidents: typing.Optional[builtins.str] = None,
        sso: typing.Optional[builtins.str] = None,
        ssoadmin: typing.Optional[builtins.str] = None,
        ssooidc: typing.Optional[builtins.str] = None,
        stepfunctions: typing.Optional[builtins.str] = None,
        storagegateway: typing.Optional[builtins.str] = None,
        sts: typing.Optional[builtins.str] = None,
        support: typing.Optional[builtins.str] = None,
        swf: typing.Optional[builtins.str] = None,
        synthetics: typing.Optional[builtins.str] = None,
        textract: typing.Optional[builtins.str] = None,
        timestreamquery: typing.Optional[builtins.str] = None,
        timestreamwrite: typing.Optional[builtins.str] = None,
        transcribe: typing.Optional[builtins.str] = None,
        transcribeservice: typing.Optional[builtins.str] = None,
        transcribestreaming: typing.Optional[builtins.str] = None,
        transcribestreamingservice: typing.Optional[builtins.str] = None,
        transfer: typing.Optional[builtins.str] = None,
        translate: typing.Optional[builtins.str] = None,
        voiceid: typing.Optional[builtins.str] = None,
        waf: typing.Optional[builtins.str] = None,
        wafregional: typing.Optional[builtins.str] = None,
        wafv2: typing.Optional[builtins.str] = None,
        wellarchitected: typing.Optional[builtins.str] = None,
        wisdom: typing.Optional[builtins.str] = None,
        workdocs: typing.Optional[builtins.str] = None,
        worklink: typing.Optional[builtins.str] = None,
        workmail: typing.Optional[builtins.str] = None,
        workmailmessageflow: typing.Optional[builtins.str] = None,
        workspaces: typing.Optional[builtins.str] = None,
        workspacesweb: typing.Optional[builtins.str] = None,
        xray: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param accessanalyzer: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#accessanalyzer AwsProvider#accessanalyzer}
        :param account: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#account AwsProvider#account}
        :param acm: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#acm AwsProvider#acm}
        :param acmpca: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#acmpca AwsProvider#acmpca}
        :param alexaforbusiness: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#alexaforbusiness AwsProvider#alexaforbusiness}
        :param amg: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#amg AwsProvider#amg}
        :param amp: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#amp AwsProvider#amp}
        :param amplify: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#amplify AwsProvider#amplify}
        :param amplifybackend: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#amplifybackend AwsProvider#amplifybackend}
        :param amplifyuibuilder: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#amplifyuibuilder AwsProvider#amplifyuibuilder}
        :param apigateway: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#apigateway AwsProvider#apigateway}
        :param apigatewaymanagementapi: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#apigatewaymanagementapi AwsProvider#apigatewaymanagementapi}
        :param apigatewayv2: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#apigatewayv2 AwsProvider#apigatewayv2}
        :param appautoscaling: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#appautoscaling AwsProvider#appautoscaling}
        :param appconfig: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#appconfig AwsProvider#appconfig}
        :param appconfigdata: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#appconfigdata AwsProvider#appconfigdata}
        :param appflow: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#appflow AwsProvider#appflow}
        :param appintegrations: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#appintegrations AwsProvider#appintegrations}
        :param appintegrationsservice: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#appintegrationsservice AwsProvider#appintegrationsservice}
        :param applicationautoscaling: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#applicationautoscaling AwsProvider#applicationautoscaling}
        :param applicationcostprofiler: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#applicationcostprofiler AwsProvider#applicationcostprofiler}
        :param applicationdiscovery: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#applicationdiscovery AwsProvider#applicationdiscovery}
        :param applicationdiscoveryservice: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#applicationdiscoveryservice AwsProvider#applicationdiscoveryservice}
        :param applicationinsights: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#applicationinsights AwsProvider#applicationinsights}
        :param appmesh: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#appmesh AwsProvider#appmesh}
        :param appregistry: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#appregistry AwsProvider#appregistry}
        :param apprunner: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#apprunner AwsProvider#apprunner}
        :param appstream: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#appstream AwsProvider#appstream}
        :param appsync: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#appsync AwsProvider#appsync}
        :param athena: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#athena AwsProvider#athena}
        :param auditmanager: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#auditmanager AwsProvider#auditmanager}
        :param augmentedairuntime: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#augmentedairuntime AwsProvider#augmentedairuntime}
        :param autoscaling: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#autoscaling AwsProvider#autoscaling}
        :param autoscalingplans: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#autoscalingplans AwsProvider#autoscalingplans}
        :param backup: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#backup AwsProvider#backup}
        :param backupgateway: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#backupgateway AwsProvider#backupgateway}
        :param batch: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#batch AwsProvider#batch}
        :param beanstalk: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#beanstalk AwsProvider#beanstalk}
        :param billingconductor: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#billingconductor AwsProvider#billingconductor}
        :param braket: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#braket AwsProvider#braket}
        :param budgets: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#budgets AwsProvider#budgets}
        :param ce: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#ce AwsProvider#ce}
        :param chime: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#chime AwsProvider#chime}
        :param chimesdkidentity: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#chimesdkidentity AwsProvider#chimesdkidentity}
        :param chimesdkmeetings: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#chimesdkmeetings AwsProvider#chimesdkmeetings}
        :param chimesdkmessaging: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#chimesdkmessaging AwsProvider#chimesdkmessaging}
        :param cloud9: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#cloud9 AwsProvider#cloud9}
        :param cloudcontrol: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#cloudcontrol AwsProvider#cloudcontrol}
        :param cloudcontrolapi: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#cloudcontrolapi AwsProvider#cloudcontrolapi}
        :param clouddirectory: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#clouddirectory AwsProvider#clouddirectory}
        :param cloudformation: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#cloudformation AwsProvider#cloudformation}
        :param cloudfront: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#cloudfront AwsProvider#cloudfront}
        :param cloudhsm: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#cloudhsm AwsProvider#cloudhsm}
        :param cloudhsmv2: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#cloudhsmv2 AwsProvider#cloudhsmv2}
        :param cloudsearch: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#cloudsearch AwsProvider#cloudsearch}
        :param cloudsearchdomain: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#cloudsearchdomain AwsProvider#cloudsearchdomain}
        :param cloudtrail: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#cloudtrail AwsProvider#cloudtrail}
        :param cloudwatch: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#cloudwatch AwsProvider#cloudwatch}
        :param cloudwatchevents: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#cloudwatchevents AwsProvider#cloudwatchevents}
        :param cloudwatchevidently: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#cloudwatchevidently AwsProvider#cloudwatchevidently}
        :param cloudwatchlog: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#cloudwatchlog AwsProvider#cloudwatchlog}
        :param cloudwatchlogs: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#cloudwatchlogs AwsProvider#cloudwatchlogs}
        :param cloudwatchrum: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#cloudwatchrum AwsProvider#cloudwatchrum}
        :param codeartifact: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#codeartifact AwsProvider#codeartifact}
        :param codebuild: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#codebuild AwsProvider#codebuild}
        :param codecommit: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#codecommit AwsProvider#codecommit}
        :param codedeploy: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#codedeploy AwsProvider#codedeploy}
        :param codeguruprofiler: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#codeguruprofiler AwsProvider#codeguruprofiler}
        :param codegurureviewer: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#codegurureviewer AwsProvider#codegurureviewer}
        :param codepipeline: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#codepipeline AwsProvider#codepipeline}
        :param codestar: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#codestar AwsProvider#codestar}
        :param codestarconnections: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#codestarconnections AwsProvider#codestarconnections}
        :param codestarnotifications: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#codestarnotifications AwsProvider#codestarnotifications}
        :param cognitoidentity: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#cognitoidentity AwsProvider#cognitoidentity}
        :param cognitoidentityprovider: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#cognitoidentityprovider AwsProvider#cognitoidentityprovider}
        :param cognitoidp: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#cognitoidp AwsProvider#cognitoidp}
        :param cognitosync: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#cognitosync AwsProvider#cognitosync}
        :param comprehend: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#comprehend AwsProvider#comprehend}
        :param comprehendmedical: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#comprehendmedical AwsProvider#comprehendmedical}
        :param computeoptimizer: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#computeoptimizer AwsProvider#computeoptimizer}
        :param config: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#config AwsProvider#config}
        :param configservice: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#configservice AwsProvider#configservice}
        :param connect: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#connect AwsProvider#connect}
        :param connectcontactlens: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#connectcontactlens AwsProvider#connectcontactlens}
        :param connectparticipant: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#connectparticipant AwsProvider#connectparticipant}
        :param connectwisdomservice: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#connectwisdomservice AwsProvider#connectwisdomservice}
        :param controltower: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#controltower AwsProvider#controltower}
        :param costandusagereportservice: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#costandusagereportservice AwsProvider#costandusagereportservice}
        :param costexplorer: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#costexplorer AwsProvider#costexplorer}
        :param cur: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#cur AwsProvider#cur}
        :param customerprofiles: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#customerprofiles AwsProvider#customerprofiles}
        :param databasemigration: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#databasemigration AwsProvider#databasemigration}
        :param databasemigrationservice: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#databasemigrationservice AwsProvider#databasemigrationservice}
        :param databrew: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#databrew AwsProvider#databrew}
        :param dataexchange: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#dataexchange AwsProvider#dataexchange}
        :param datapipeline: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#datapipeline AwsProvider#datapipeline}
        :param datasync: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#datasync AwsProvider#datasync}
        :param dax: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#dax AwsProvider#dax}
        :param deploy: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#deploy AwsProvider#deploy}
        :param detective: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#detective AwsProvider#detective}
        :param devicefarm: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#devicefarm AwsProvider#devicefarm}
        :param devopsguru: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#devopsguru AwsProvider#devopsguru}
        :param directconnect: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#directconnect AwsProvider#directconnect}
        :param directoryservice: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#directoryservice AwsProvider#directoryservice}
        :param discovery: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#discovery AwsProvider#discovery}
        :param dlm: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#dlm AwsProvider#dlm}
        :param dms: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#dms AwsProvider#dms}
        :param docdb: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#docdb AwsProvider#docdb}
        :param drs: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#drs AwsProvider#drs}
        :param ds: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#ds AwsProvider#ds}
        :param dynamodb: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#dynamodb AwsProvider#dynamodb}
        :param dynamodbstreams: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#dynamodbstreams AwsProvider#dynamodbstreams}
        :param ebs: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#ebs AwsProvider#ebs}
        :param ec2: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#ec2 AwsProvider#ec2}
        :param ec2_instanceconnect: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#ec2instanceconnect AwsProvider#ec2instanceconnect}
        :param ecr: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#ecr AwsProvider#ecr}
        :param ecrpublic: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#ecrpublic AwsProvider#ecrpublic}
        :param ecs: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#ecs AwsProvider#ecs}
        :param efs: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#efs AwsProvider#efs}
        :param eks: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#eks AwsProvider#eks}
        :param elasticache: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#elasticache AwsProvider#elasticache}
        :param elasticbeanstalk: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#elasticbeanstalk AwsProvider#elasticbeanstalk}
        :param elasticinference: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#elasticinference AwsProvider#elasticinference}
        :param elasticloadbalancing: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#elasticloadbalancing AwsProvider#elasticloadbalancing}
        :param elasticloadbalancingv2: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#elasticloadbalancingv2 AwsProvider#elasticloadbalancingv2}
        :param elasticsearch: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#elasticsearch AwsProvider#elasticsearch}
        :param elasticsearchservice: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#elasticsearchservice AwsProvider#elasticsearchservice}
        :param elastictranscoder: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#elastictranscoder AwsProvider#elastictranscoder}
        :param elb: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#elb AwsProvider#elb}
        :param elbv2: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#elbv2 AwsProvider#elbv2}
        :param emr: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#emr AwsProvider#emr}
        :param emrcontainers: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#emrcontainers AwsProvider#emrcontainers}
        :param emrserverless: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#emrserverless AwsProvider#emrserverless}
        :param es: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#es AwsProvider#es}
        :param eventbridge: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#eventbridge AwsProvider#eventbridge}
        :param events: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#events AwsProvider#events}
        :param evidently: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#evidently AwsProvider#evidently}
        :param finspace: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#finspace AwsProvider#finspace}
        :param finspacedata: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#finspacedata AwsProvider#finspacedata}
        :param firehose: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#firehose AwsProvider#firehose}
        :param fis: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#fis AwsProvider#fis}
        :param fms: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#fms AwsProvider#fms}
        :param forecast: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#forecast AwsProvider#forecast}
        :param forecastquery: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#forecastquery AwsProvider#forecastquery}
        :param forecastqueryservice: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#forecastqueryservice AwsProvider#forecastqueryservice}
        :param forecastservice: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#forecastservice AwsProvider#forecastservice}
        :param frauddetector: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#frauddetector AwsProvider#frauddetector}
        :param fsx: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#fsx AwsProvider#fsx}
        :param gamelift: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#gamelift AwsProvider#gamelift}
        :param glacier: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#glacier AwsProvider#glacier}
        :param globalaccelerator: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#globalaccelerator AwsProvider#globalaccelerator}
        :param glue: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#glue AwsProvider#glue}
        :param gluedatabrew: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#gluedatabrew AwsProvider#gluedatabrew}
        :param grafana: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#grafana AwsProvider#grafana}
        :param greengrass: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#greengrass AwsProvider#greengrass}
        :param greengrassv2: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#greengrassv2 AwsProvider#greengrassv2}
        :param groundstation: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#groundstation AwsProvider#groundstation}
        :param guardduty: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#guardduty AwsProvider#guardduty}
        :param health: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#health AwsProvider#health}
        :param healthlake: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#healthlake AwsProvider#healthlake}
        :param honeycode: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#honeycode AwsProvider#honeycode}
        :param iam: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#iam AwsProvider#iam}
        :param identitystore: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#identitystore AwsProvider#identitystore}
        :param imagebuilder: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#imagebuilder AwsProvider#imagebuilder}
        :param inspector: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#inspector AwsProvider#inspector}
        :param inspector2: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#inspector2 AwsProvider#inspector2}
        :param inspectorv2: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#inspectorv2 AwsProvider#inspectorv2}
        :param iot: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#iot AwsProvider#iot}
        :param iot1_clickdevices: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#iot1clickdevices AwsProvider#iot1clickdevices}
        :param iot1_clickdevicesservice: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#iot1clickdevicesservice AwsProvider#iot1clickdevicesservice}
        :param iot1_clickprojects: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#iot1clickprojects AwsProvider#iot1clickprojects}
        :param iotanalytics: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#iotanalytics AwsProvider#iotanalytics}
        :param iotdata: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#iotdata AwsProvider#iotdata}
        :param iotdataplane: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#iotdataplane AwsProvider#iotdataplane}
        :param iotdeviceadvisor: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#iotdeviceadvisor AwsProvider#iotdeviceadvisor}
        :param iotevents: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#iotevents AwsProvider#iotevents}
        :param ioteventsdata: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#ioteventsdata AwsProvider#ioteventsdata}
        :param iotfleethub: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#iotfleethub AwsProvider#iotfleethub}
        :param iotjobsdata: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#iotjobsdata AwsProvider#iotjobsdata}
        :param iotjobsdataplane: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#iotjobsdataplane AwsProvider#iotjobsdataplane}
        :param iotsecuretunneling: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#iotsecuretunneling AwsProvider#iotsecuretunneling}
        :param iotsitewise: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#iotsitewise AwsProvider#iotsitewise}
        :param iotthingsgraph: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#iotthingsgraph AwsProvider#iotthingsgraph}
        :param iottwinmaker: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#iottwinmaker AwsProvider#iottwinmaker}
        :param iotwireless: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#iotwireless AwsProvider#iotwireless}
        :param ivs: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#ivs AwsProvider#ivs}
        :param ivschat: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#ivschat AwsProvider#ivschat}
        :param kafka: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#kafka AwsProvider#kafka}
        :param kafkaconnect: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#kafkaconnect AwsProvider#kafkaconnect}
        :param kendra: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#kendra AwsProvider#kendra}
        :param keyspaces: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#keyspaces AwsProvider#keyspaces}
        :param kinesis: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#kinesis AwsProvider#kinesis}
        :param kinesisanalytics: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#kinesisanalytics AwsProvider#kinesisanalytics}
        :param kinesisanalyticsv2: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#kinesisanalyticsv2 AwsProvider#kinesisanalyticsv2}
        :param kinesisvideo: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#kinesisvideo AwsProvider#kinesisvideo}
        :param kinesisvideoarchivedmedia: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#kinesisvideoarchivedmedia AwsProvider#kinesisvideoarchivedmedia}
        :param kinesisvideomedia: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#kinesisvideomedia AwsProvider#kinesisvideomedia}
        :param kinesisvideosignaling: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#kinesisvideosignaling AwsProvider#kinesisvideosignaling}
        :param kinesisvideosignalingchannels: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#kinesisvideosignalingchannels AwsProvider#kinesisvideosignalingchannels}
        :param kms: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#kms AwsProvider#kms}
        :param lakeformation: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#lakeformation AwsProvider#lakeformation}
        :param lambda_: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#lambda AwsProvider#lambda}
        :param lex: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#lex AwsProvider#lex}
        :param lexmodelbuilding: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#lexmodelbuilding AwsProvider#lexmodelbuilding}
        :param lexmodelbuildingservice: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#lexmodelbuildingservice AwsProvider#lexmodelbuildingservice}
        :param lexmodels: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#lexmodels AwsProvider#lexmodels}
        :param lexmodelsv2: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#lexmodelsv2 AwsProvider#lexmodelsv2}
        :param lexruntime: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#lexruntime AwsProvider#lexruntime}
        :param lexruntimeservice: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#lexruntimeservice AwsProvider#lexruntimeservice}
        :param lexruntimev2: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#lexruntimev2 AwsProvider#lexruntimev2}
        :param lexv2_models: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#lexv2models AwsProvider#lexv2models}
        :param lexv2_runtime: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#lexv2runtime AwsProvider#lexv2runtime}
        :param licensemanager: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#licensemanager AwsProvider#licensemanager}
        :param lightsail: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#lightsail AwsProvider#lightsail}
        :param location: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#location AwsProvider#location}
        :param locationservice: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#locationservice AwsProvider#locationservice}
        :param logs: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#logs AwsProvider#logs}
        :param lookoutequipment: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#lookoutequipment AwsProvider#lookoutequipment}
        :param lookoutforvision: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#lookoutforvision AwsProvider#lookoutforvision}
        :param lookoutmetrics: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#lookoutmetrics AwsProvider#lookoutmetrics}
        :param lookoutvision: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#lookoutvision AwsProvider#lookoutvision}
        :param machinelearning: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#machinelearning AwsProvider#machinelearning}
        :param macie: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#macie AwsProvider#macie}
        :param macie2: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#macie2 AwsProvider#macie2}
        :param managedblockchain: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#managedblockchain AwsProvider#managedblockchain}
        :param managedgrafana: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#managedgrafana AwsProvider#managedgrafana}
        :param marketplacecatalog: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#marketplacecatalog AwsProvider#marketplacecatalog}
        :param marketplacecommerceanalytics: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#marketplacecommerceanalytics AwsProvider#marketplacecommerceanalytics}
        :param marketplaceentitlement: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#marketplaceentitlement AwsProvider#marketplaceentitlement}
        :param marketplaceentitlementservice: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#marketplaceentitlementservice AwsProvider#marketplaceentitlementservice}
        :param marketplacemetering: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#marketplacemetering AwsProvider#marketplacemetering}
        :param mediaconnect: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#mediaconnect AwsProvider#mediaconnect}
        :param mediaconvert: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#mediaconvert AwsProvider#mediaconvert}
        :param medialive: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#medialive AwsProvider#medialive}
        :param mediapackage: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#mediapackage AwsProvider#mediapackage}
        :param mediapackagevod: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#mediapackagevod AwsProvider#mediapackagevod}
        :param mediastore: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#mediastore AwsProvider#mediastore}
        :param mediastoredata: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#mediastoredata AwsProvider#mediastoredata}
        :param mediatailor: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#mediatailor AwsProvider#mediatailor}
        :param memorydb: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#memorydb AwsProvider#memorydb}
        :param meteringmarketplace: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#meteringmarketplace AwsProvider#meteringmarketplace}
        :param mgh: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#mgh AwsProvider#mgh}
        :param mgn: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#mgn AwsProvider#mgn}
        :param migrationhub: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#migrationhub AwsProvider#migrationhub}
        :param migrationhubconfig: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#migrationhubconfig AwsProvider#migrationhubconfig}
        :param migrationhubrefactorspaces: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#migrationhubrefactorspaces AwsProvider#migrationhubrefactorspaces}
        :param migrationhubstrategy: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#migrationhubstrategy AwsProvider#migrationhubstrategy}
        :param migrationhubstrategyrecommendations: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#migrationhubstrategyrecommendations AwsProvider#migrationhubstrategyrecommendations}
        :param mobile: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#mobile AwsProvider#mobile}
        :param mq: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#mq AwsProvider#mq}
        :param msk: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#msk AwsProvider#msk}
        :param mturk: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#mturk AwsProvider#mturk}
        :param mwaa: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#mwaa AwsProvider#mwaa}
        :param neptune: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#neptune AwsProvider#neptune}
        :param networkfirewall: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#networkfirewall AwsProvider#networkfirewall}
        :param networkmanager: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#networkmanager AwsProvider#networkmanager}
        :param nimble: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#nimble AwsProvider#nimble}
        :param nimblestudio: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#nimblestudio AwsProvider#nimblestudio}
        :param opensearch: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#opensearch AwsProvider#opensearch}
        :param opensearchserverless: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#opensearchserverless AwsProvider#opensearchserverless}
        :param opensearchservice: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#opensearchservice AwsProvider#opensearchservice}
        :param opsworks: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#opsworks AwsProvider#opsworks}
        :param opsworkscm: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#opsworkscm AwsProvider#opsworkscm}
        :param organizations: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#organizations AwsProvider#organizations}
        :param outposts: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#outposts AwsProvider#outposts}
        :param panorama: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#panorama AwsProvider#panorama}
        :param personalize: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#personalize AwsProvider#personalize}
        :param personalizeevents: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#personalizeevents AwsProvider#personalizeevents}
        :param personalizeruntime: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#personalizeruntime AwsProvider#personalizeruntime}
        :param pi: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#pi AwsProvider#pi}
        :param pinpoint: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#pinpoint AwsProvider#pinpoint}
        :param pinpointemail: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#pinpointemail AwsProvider#pinpointemail}
        :param pinpointsmsvoice: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#pinpointsmsvoice AwsProvider#pinpointsmsvoice}
        :param pipes: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#pipes AwsProvider#pipes}
        :param polly: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#polly AwsProvider#polly}
        :param pricing: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#pricing AwsProvider#pricing}
        :param prometheus: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#prometheus AwsProvider#prometheus}
        :param prometheusservice: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#prometheusservice AwsProvider#prometheusservice}
        :param proton: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#proton AwsProvider#proton}
        :param qldb: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#qldb AwsProvider#qldb}
        :param qldbsession: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#qldbsession AwsProvider#qldbsession}
        :param quicksight: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#quicksight AwsProvider#quicksight}
        :param ram: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#ram AwsProvider#ram}
        :param rbin: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#rbin AwsProvider#rbin}
        :param rds: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#rds AwsProvider#rds}
        :param rdsdata: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#rdsdata AwsProvider#rdsdata}
        :param rdsdataservice: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#rdsdataservice AwsProvider#rdsdataservice}
        :param recyclebin: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#recyclebin AwsProvider#recyclebin}
        :param redshift: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#redshift AwsProvider#redshift}
        :param redshiftdata: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#redshiftdata AwsProvider#redshiftdata}
        :param redshiftdataapiservice: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#redshiftdataapiservice AwsProvider#redshiftdataapiservice}
        :param redshiftserverless: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#redshiftserverless AwsProvider#redshiftserverless}
        :param rekognition: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#rekognition AwsProvider#rekognition}
        :param resiliencehub: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#resiliencehub AwsProvider#resiliencehub}
        :param resourceexplorer2: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#resourceexplorer2 AwsProvider#resourceexplorer2}
        :param resourcegroups: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#resourcegroups AwsProvider#resourcegroups}
        :param resourcegroupstagging: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#resourcegroupstagging AwsProvider#resourcegroupstagging}
        :param resourcegroupstaggingapi: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#resourcegroupstaggingapi AwsProvider#resourcegroupstaggingapi}
        :param robomaker: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#robomaker AwsProvider#robomaker}
        :param rolesanywhere: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#rolesanywhere AwsProvider#rolesanywhere}
        :param route53: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#route53 AwsProvider#route53}
        :param route53_domains: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#route53domains AwsProvider#route53domains}
        :param route53_recoverycluster: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#route53recoverycluster AwsProvider#route53recoverycluster}
        :param route53_recoverycontrolconfig: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#route53recoverycontrolconfig AwsProvider#route53recoverycontrolconfig}
        :param route53_recoveryreadiness: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#route53recoveryreadiness AwsProvider#route53recoveryreadiness}
        :param route53_resolver: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#route53resolver AwsProvider#route53resolver}
        :param rum: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#rum AwsProvider#rum}
        :param s3: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#s3 AwsProvider#s3}
        :param s3_api: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#s3api AwsProvider#s3api}
        :param s3_control: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#s3control AwsProvider#s3control}
        :param s3_outposts: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#s3outposts AwsProvider#s3outposts}
        :param sagemaker: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#sagemaker AwsProvider#sagemaker}
        :param sagemakera2_iruntime: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#sagemakera2iruntime AwsProvider#sagemakera2iruntime}
        :param sagemakeredge: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#sagemakeredge AwsProvider#sagemakeredge}
        :param sagemakeredgemanager: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#sagemakeredgemanager AwsProvider#sagemakeredgemanager}
        :param sagemakerfeaturestoreruntime: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#sagemakerfeaturestoreruntime AwsProvider#sagemakerfeaturestoreruntime}
        :param sagemakerruntime: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#sagemakerruntime AwsProvider#sagemakerruntime}
        :param savingsplans: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#savingsplans AwsProvider#savingsplans}
        :param scheduler: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#scheduler AwsProvider#scheduler}
        :param schemas: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#schemas AwsProvider#schemas}
        :param sdb: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#sdb AwsProvider#sdb}
        :param secretsmanager: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#secretsmanager AwsProvider#secretsmanager}
        :param securityhub: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#securityhub AwsProvider#securityhub}
        :param serverlessapplicationrepository: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#serverlessapplicationrepository AwsProvider#serverlessapplicationrepository}
        :param serverlessapprepo: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#serverlessapprepo AwsProvider#serverlessapprepo}
        :param serverlessrepo: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#serverlessrepo AwsProvider#serverlessrepo}
        :param servicecatalog: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#servicecatalog AwsProvider#servicecatalog}
        :param servicecatalogappregistry: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#servicecatalogappregistry AwsProvider#servicecatalogappregistry}
        :param servicediscovery: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#servicediscovery AwsProvider#servicediscovery}
        :param servicequotas: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#servicequotas AwsProvider#servicequotas}
        :param ses: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#ses AwsProvider#ses}
        :param sesv2: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#sesv2 AwsProvider#sesv2}
        :param sfn: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#sfn AwsProvider#sfn}
        :param shield: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#shield AwsProvider#shield}
        :param signer: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#signer AwsProvider#signer}
        :param simpledb: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#simpledb AwsProvider#simpledb}
        :param sms: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#sms AwsProvider#sms}
        :param snowball: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#snowball AwsProvider#snowball}
        :param snowdevicemanagement: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#snowdevicemanagement AwsProvider#snowdevicemanagement}
        :param sns: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#sns AwsProvider#sns}
        :param sqs: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#sqs AwsProvider#sqs}
        :param ssm: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#ssm AwsProvider#ssm}
        :param ssmcontacts: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#ssmcontacts AwsProvider#ssmcontacts}
        :param ssmincidents: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#ssmincidents AwsProvider#ssmincidents}
        :param sso: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#sso AwsProvider#sso}
        :param ssoadmin: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#ssoadmin AwsProvider#ssoadmin}
        :param ssooidc: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#ssooidc AwsProvider#ssooidc}
        :param stepfunctions: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#stepfunctions AwsProvider#stepfunctions}
        :param storagegateway: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#storagegateway AwsProvider#storagegateway}
        :param sts: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#sts AwsProvider#sts}
        :param support: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#support AwsProvider#support}
        :param swf: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#swf AwsProvider#swf}
        :param synthetics: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#synthetics AwsProvider#synthetics}
        :param textract: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#textract AwsProvider#textract}
        :param timestreamquery: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#timestreamquery AwsProvider#timestreamquery}
        :param timestreamwrite: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#timestreamwrite AwsProvider#timestreamwrite}
        :param transcribe: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#transcribe AwsProvider#transcribe}
        :param transcribeservice: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#transcribeservice AwsProvider#transcribeservice}
        :param transcribestreaming: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#transcribestreaming AwsProvider#transcribestreaming}
        :param transcribestreamingservice: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#transcribestreamingservice AwsProvider#transcribestreamingservice}
        :param transfer: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#transfer AwsProvider#transfer}
        :param translate: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#translate AwsProvider#translate}
        :param voiceid: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#voiceid AwsProvider#voiceid}
        :param waf: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#waf AwsProvider#waf}
        :param wafregional: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#wafregional AwsProvider#wafregional}
        :param wafv2: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#wafv2 AwsProvider#wafv2}
        :param wellarchitected: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#wellarchitected AwsProvider#wellarchitected}
        :param wisdom: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#wisdom AwsProvider#wisdom}
        :param workdocs: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#workdocs AwsProvider#workdocs}
        :param worklink: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#worklink AwsProvider#worklink}
        :param workmail: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#workmail AwsProvider#workmail}
        :param workmailmessageflow: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#workmailmessageflow AwsProvider#workmailmessageflow}
        :param workspaces: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#workspaces AwsProvider#workspaces}
        :param workspacesweb: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#workspacesweb AwsProvider#workspacesweb}
        :param xray: Use this to override the default service endpoint URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#xray AwsProvider#xray}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94629cb2539035d8ffea4741e9daf3cf532679568af0e67223cdf5133dc96742)
            check_type(argname="argument accessanalyzer", value=accessanalyzer, expected_type=type_hints["accessanalyzer"])
            check_type(argname="argument account", value=account, expected_type=type_hints["account"])
            check_type(argname="argument acm", value=acm, expected_type=type_hints["acm"])
            check_type(argname="argument acmpca", value=acmpca, expected_type=type_hints["acmpca"])
            check_type(argname="argument alexaforbusiness", value=alexaforbusiness, expected_type=type_hints["alexaforbusiness"])
            check_type(argname="argument amg", value=amg, expected_type=type_hints["amg"])
            check_type(argname="argument amp", value=amp, expected_type=type_hints["amp"])
            check_type(argname="argument amplify", value=amplify, expected_type=type_hints["amplify"])
            check_type(argname="argument amplifybackend", value=amplifybackend, expected_type=type_hints["amplifybackend"])
            check_type(argname="argument amplifyuibuilder", value=amplifyuibuilder, expected_type=type_hints["amplifyuibuilder"])
            check_type(argname="argument apigateway", value=apigateway, expected_type=type_hints["apigateway"])
            check_type(argname="argument apigatewaymanagementapi", value=apigatewaymanagementapi, expected_type=type_hints["apigatewaymanagementapi"])
            check_type(argname="argument apigatewayv2", value=apigatewayv2, expected_type=type_hints["apigatewayv2"])
            check_type(argname="argument appautoscaling", value=appautoscaling, expected_type=type_hints["appautoscaling"])
            check_type(argname="argument appconfig", value=appconfig, expected_type=type_hints["appconfig"])
            check_type(argname="argument appconfigdata", value=appconfigdata, expected_type=type_hints["appconfigdata"])
            check_type(argname="argument appflow", value=appflow, expected_type=type_hints["appflow"])
            check_type(argname="argument appintegrations", value=appintegrations, expected_type=type_hints["appintegrations"])
            check_type(argname="argument appintegrationsservice", value=appintegrationsservice, expected_type=type_hints["appintegrationsservice"])
            check_type(argname="argument applicationautoscaling", value=applicationautoscaling, expected_type=type_hints["applicationautoscaling"])
            check_type(argname="argument applicationcostprofiler", value=applicationcostprofiler, expected_type=type_hints["applicationcostprofiler"])
            check_type(argname="argument applicationdiscovery", value=applicationdiscovery, expected_type=type_hints["applicationdiscovery"])
            check_type(argname="argument applicationdiscoveryservice", value=applicationdiscoveryservice, expected_type=type_hints["applicationdiscoveryservice"])
            check_type(argname="argument applicationinsights", value=applicationinsights, expected_type=type_hints["applicationinsights"])
            check_type(argname="argument appmesh", value=appmesh, expected_type=type_hints["appmesh"])
            check_type(argname="argument appregistry", value=appregistry, expected_type=type_hints["appregistry"])
            check_type(argname="argument apprunner", value=apprunner, expected_type=type_hints["apprunner"])
            check_type(argname="argument appstream", value=appstream, expected_type=type_hints["appstream"])
            check_type(argname="argument appsync", value=appsync, expected_type=type_hints["appsync"])
            check_type(argname="argument athena", value=athena, expected_type=type_hints["athena"])
            check_type(argname="argument auditmanager", value=auditmanager, expected_type=type_hints["auditmanager"])
            check_type(argname="argument augmentedairuntime", value=augmentedairuntime, expected_type=type_hints["augmentedairuntime"])
            check_type(argname="argument autoscaling", value=autoscaling, expected_type=type_hints["autoscaling"])
            check_type(argname="argument autoscalingplans", value=autoscalingplans, expected_type=type_hints["autoscalingplans"])
            check_type(argname="argument backup", value=backup, expected_type=type_hints["backup"])
            check_type(argname="argument backupgateway", value=backupgateway, expected_type=type_hints["backupgateway"])
            check_type(argname="argument batch", value=batch, expected_type=type_hints["batch"])
            check_type(argname="argument beanstalk", value=beanstalk, expected_type=type_hints["beanstalk"])
            check_type(argname="argument billingconductor", value=billingconductor, expected_type=type_hints["billingconductor"])
            check_type(argname="argument braket", value=braket, expected_type=type_hints["braket"])
            check_type(argname="argument budgets", value=budgets, expected_type=type_hints["budgets"])
            check_type(argname="argument ce", value=ce, expected_type=type_hints["ce"])
            check_type(argname="argument chime", value=chime, expected_type=type_hints["chime"])
            check_type(argname="argument chimesdkidentity", value=chimesdkidentity, expected_type=type_hints["chimesdkidentity"])
            check_type(argname="argument chimesdkmeetings", value=chimesdkmeetings, expected_type=type_hints["chimesdkmeetings"])
            check_type(argname="argument chimesdkmessaging", value=chimesdkmessaging, expected_type=type_hints["chimesdkmessaging"])
            check_type(argname="argument cloud9", value=cloud9, expected_type=type_hints["cloud9"])
            check_type(argname="argument cloudcontrol", value=cloudcontrol, expected_type=type_hints["cloudcontrol"])
            check_type(argname="argument cloudcontrolapi", value=cloudcontrolapi, expected_type=type_hints["cloudcontrolapi"])
            check_type(argname="argument clouddirectory", value=clouddirectory, expected_type=type_hints["clouddirectory"])
            check_type(argname="argument cloudformation", value=cloudformation, expected_type=type_hints["cloudformation"])
            check_type(argname="argument cloudfront", value=cloudfront, expected_type=type_hints["cloudfront"])
            check_type(argname="argument cloudhsm", value=cloudhsm, expected_type=type_hints["cloudhsm"])
            check_type(argname="argument cloudhsmv2", value=cloudhsmv2, expected_type=type_hints["cloudhsmv2"])
            check_type(argname="argument cloudsearch", value=cloudsearch, expected_type=type_hints["cloudsearch"])
            check_type(argname="argument cloudsearchdomain", value=cloudsearchdomain, expected_type=type_hints["cloudsearchdomain"])
            check_type(argname="argument cloudtrail", value=cloudtrail, expected_type=type_hints["cloudtrail"])
            check_type(argname="argument cloudwatch", value=cloudwatch, expected_type=type_hints["cloudwatch"])
            check_type(argname="argument cloudwatchevents", value=cloudwatchevents, expected_type=type_hints["cloudwatchevents"])
            check_type(argname="argument cloudwatchevidently", value=cloudwatchevidently, expected_type=type_hints["cloudwatchevidently"])
            check_type(argname="argument cloudwatchlog", value=cloudwatchlog, expected_type=type_hints["cloudwatchlog"])
            check_type(argname="argument cloudwatchlogs", value=cloudwatchlogs, expected_type=type_hints["cloudwatchlogs"])
            check_type(argname="argument cloudwatchrum", value=cloudwatchrum, expected_type=type_hints["cloudwatchrum"])
            check_type(argname="argument codeartifact", value=codeartifact, expected_type=type_hints["codeartifact"])
            check_type(argname="argument codebuild", value=codebuild, expected_type=type_hints["codebuild"])
            check_type(argname="argument codecommit", value=codecommit, expected_type=type_hints["codecommit"])
            check_type(argname="argument codedeploy", value=codedeploy, expected_type=type_hints["codedeploy"])
            check_type(argname="argument codeguruprofiler", value=codeguruprofiler, expected_type=type_hints["codeguruprofiler"])
            check_type(argname="argument codegurureviewer", value=codegurureviewer, expected_type=type_hints["codegurureviewer"])
            check_type(argname="argument codepipeline", value=codepipeline, expected_type=type_hints["codepipeline"])
            check_type(argname="argument codestar", value=codestar, expected_type=type_hints["codestar"])
            check_type(argname="argument codestarconnections", value=codestarconnections, expected_type=type_hints["codestarconnections"])
            check_type(argname="argument codestarnotifications", value=codestarnotifications, expected_type=type_hints["codestarnotifications"])
            check_type(argname="argument cognitoidentity", value=cognitoidentity, expected_type=type_hints["cognitoidentity"])
            check_type(argname="argument cognitoidentityprovider", value=cognitoidentityprovider, expected_type=type_hints["cognitoidentityprovider"])
            check_type(argname="argument cognitoidp", value=cognitoidp, expected_type=type_hints["cognitoidp"])
            check_type(argname="argument cognitosync", value=cognitosync, expected_type=type_hints["cognitosync"])
            check_type(argname="argument comprehend", value=comprehend, expected_type=type_hints["comprehend"])
            check_type(argname="argument comprehendmedical", value=comprehendmedical, expected_type=type_hints["comprehendmedical"])
            check_type(argname="argument computeoptimizer", value=computeoptimizer, expected_type=type_hints["computeoptimizer"])
            check_type(argname="argument config", value=config, expected_type=type_hints["config"])
            check_type(argname="argument configservice", value=configservice, expected_type=type_hints["configservice"])
            check_type(argname="argument connect", value=connect, expected_type=type_hints["connect"])
            check_type(argname="argument connectcontactlens", value=connectcontactlens, expected_type=type_hints["connectcontactlens"])
            check_type(argname="argument connectparticipant", value=connectparticipant, expected_type=type_hints["connectparticipant"])
            check_type(argname="argument connectwisdomservice", value=connectwisdomservice, expected_type=type_hints["connectwisdomservice"])
            check_type(argname="argument controltower", value=controltower, expected_type=type_hints["controltower"])
            check_type(argname="argument costandusagereportservice", value=costandusagereportservice, expected_type=type_hints["costandusagereportservice"])
            check_type(argname="argument costexplorer", value=costexplorer, expected_type=type_hints["costexplorer"])
            check_type(argname="argument cur", value=cur, expected_type=type_hints["cur"])
            check_type(argname="argument customerprofiles", value=customerprofiles, expected_type=type_hints["customerprofiles"])
            check_type(argname="argument databasemigration", value=databasemigration, expected_type=type_hints["databasemigration"])
            check_type(argname="argument databasemigrationservice", value=databasemigrationservice, expected_type=type_hints["databasemigrationservice"])
            check_type(argname="argument databrew", value=databrew, expected_type=type_hints["databrew"])
            check_type(argname="argument dataexchange", value=dataexchange, expected_type=type_hints["dataexchange"])
            check_type(argname="argument datapipeline", value=datapipeline, expected_type=type_hints["datapipeline"])
            check_type(argname="argument datasync", value=datasync, expected_type=type_hints["datasync"])
            check_type(argname="argument dax", value=dax, expected_type=type_hints["dax"])
            check_type(argname="argument deploy", value=deploy, expected_type=type_hints["deploy"])
            check_type(argname="argument detective", value=detective, expected_type=type_hints["detective"])
            check_type(argname="argument devicefarm", value=devicefarm, expected_type=type_hints["devicefarm"])
            check_type(argname="argument devopsguru", value=devopsguru, expected_type=type_hints["devopsguru"])
            check_type(argname="argument directconnect", value=directconnect, expected_type=type_hints["directconnect"])
            check_type(argname="argument directoryservice", value=directoryservice, expected_type=type_hints["directoryservice"])
            check_type(argname="argument discovery", value=discovery, expected_type=type_hints["discovery"])
            check_type(argname="argument dlm", value=dlm, expected_type=type_hints["dlm"])
            check_type(argname="argument dms", value=dms, expected_type=type_hints["dms"])
            check_type(argname="argument docdb", value=docdb, expected_type=type_hints["docdb"])
            check_type(argname="argument drs", value=drs, expected_type=type_hints["drs"])
            check_type(argname="argument ds", value=ds, expected_type=type_hints["ds"])
            check_type(argname="argument dynamodb", value=dynamodb, expected_type=type_hints["dynamodb"])
            check_type(argname="argument dynamodbstreams", value=dynamodbstreams, expected_type=type_hints["dynamodbstreams"])
            check_type(argname="argument ebs", value=ebs, expected_type=type_hints["ebs"])
            check_type(argname="argument ec2", value=ec2, expected_type=type_hints["ec2"])
            check_type(argname="argument ec2_instanceconnect", value=ec2_instanceconnect, expected_type=type_hints["ec2_instanceconnect"])
            check_type(argname="argument ecr", value=ecr, expected_type=type_hints["ecr"])
            check_type(argname="argument ecrpublic", value=ecrpublic, expected_type=type_hints["ecrpublic"])
            check_type(argname="argument ecs", value=ecs, expected_type=type_hints["ecs"])
            check_type(argname="argument efs", value=efs, expected_type=type_hints["efs"])
            check_type(argname="argument eks", value=eks, expected_type=type_hints["eks"])
            check_type(argname="argument elasticache", value=elasticache, expected_type=type_hints["elasticache"])
            check_type(argname="argument elasticbeanstalk", value=elasticbeanstalk, expected_type=type_hints["elasticbeanstalk"])
            check_type(argname="argument elasticinference", value=elasticinference, expected_type=type_hints["elasticinference"])
            check_type(argname="argument elasticloadbalancing", value=elasticloadbalancing, expected_type=type_hints["elasticloadbalancing"])
            check_type(argname="argument elasticloadbalancingv2", value=elasticloadbalancingv2, expected_type=type_hints["elasticloadbalancingv2"])
            check_type(argname="argument elasticsearch", value=elasticsearch, expected_type=type_hints["elasticsearch"])
            check_type(argname="argument elasticsearchservice", value=elasticsearchservice, expected_type=type_hints["elasticsearchservice"])
            check_type(argname="argument elastictranscoder", value=elastictranscoder, expected_type=type_hints["elastictranscoder"])
            check_type(argname="argument elb", value=elb, expected_type=type_hints["elb"])
            check_type(argname="argument elbv2", value=elbv2, expected_type=type_hints["elbv2"])
            check_type(argname="argument emr", value=emr, expected_type=type_hints["emr"])
            check_type(argname="argument emrcontainers", value=emrcontainers, expected_type=type_hints["emrcontainers"])
            check_type(argname="argument emrserverless", value=emrserverless, expected_type=type_hints["emrserverless"])
            check_type(argname="argument es", value=es, expected_type=type_hints["es"])
            check_type(argname="argument eventbridge", value=eventbridge, expected_type=type_hints["eventbridge"])
            check_type(argname="argument events", value=events, expected_type=type_hints["events"])
            check_type(argname="argument evidently", value=evidently, expected_type=type_hints["evidently"])
            check_type(argname="argument finspace", value=finspace, expected_type=type_hints["finspace"])
            check_type(argname="argument finspacedata", value=finspacedata, expected_type=type_hints["finspacedata"])
            check_type(argname="argument firehose", value=firehose, expected_type=type_hints["firehose"])
            check_type(argname="argument fis", value=fis, expected_type=type_hints["fis"])
            check_type(argname="argument fms", value=fms, expected_type=type_hints["fms"])
            check_type(argname="argument forecast", value=forecast, expected_type=type_hints["forecast"])
            check_type(argname="argument forecastquery", value=forecastquery, expected_type=type_hints["forecastquery"])
            check_type(argname="argument forecastqueryservice", value=forecastqueryservice, expected_type=type_hints["forecastqueryservice"])
            check_type(argname="argument forecastservice", value=forecastservice, expected_type=type_hints["forecastservice"])
            check_type(argname="argument frauddetector", value=frauddetector, expected_type=type_hints["frauddetector"])
            check_type(argname="argument fsx", value=fsx, expected_type=type_hints["fsx"])
            check_type(argname="argument gamelift", value=gamelift, expected_type=type_hints["gamelift"])
            check_type(argname="argument glacier", value=glacier, expected_type=type_hints["glacier"])
            check_type(argname="argument globalaccelerator", value=globalaccelerator, expected_type=type_hints["globalaccelerator"])
            check_type(argname="argument glue", value=glue, expected_type=type_hints["glue"])
            check_type(argname="argument gluedatabrew", value=gluedatabrew, expected_type=type_hints["gluedatabrew"])
            check_type(argname="argument grafana", value=grafana, expected_type=type_hints["grafana"])
            check_type(argname="argument greengrass", value=greengrass, expected_type=type_hints["greengrass"])
            check_type(argname="argument greengrassv2", value=greengrassv2, expected_type=type_hints["greengrassv2"])
            check_type(argname="argument groundstation", value=groundstation, expected_type=type_hints["groundstation"])
            check_type(argname="argument guardduty", value=guardduty, expected_type=type_hints["guardduty"])
            check_type(argname="argument health", value=health, expected_type=type_hints["health"])
            check_type(argname="argument healthlake", value=healthlake, expected_type=type_hints["healthlake"])
            check_type(argname="argument honeycode", value=honeycode, expected_type=type_hints["honeycode"])
            check_type(argname="argument iam", value=iam, expected_type=type_hints["iam"])
            check_type(argname="argument identitystore", value=identitystore, expected_type=type_hints["identitystore"])
            check_type(argname="argument imagebuilder", value=imagebuilder, expected_type=type_hints["imagebuilder"])
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
            check_type(argname="argument inspector2", value=inspector2, expected_type=type_hints["inspector2"])
            check_type(argname="argument inspectorv2", value=inspectorv2, expected_type=type_hints["inspectorv2"])
            check_type(argname="argument iot", value=iot, expected_type=type_hints["iot"])
            check_type(argname="argument iot1_clickdevices", value=iot1_clickdevices, expected_type=type_hints["iot1_clickdevices"])
            check_type(argname="argument iot1_clickdevicesservice", value=iot1_clickdevicesservice, expected_type=type_hints["iot1_clickdevicesservice"])
            check_type(argname="argument iot1_clickprojects", value=iot1_clickprojects, expected_type=type_hints["iot1_clickprojects"])
            check_type(argname="argument iotanalytics", value=iotanalytics, expected_type=type_hints["iotanalytics"])
            check_type(argname="argument iotdata", value=iotdata, expected_type=type_hints["iotdata"])
            check_type(argname="argument iotdataplane", value=iotdataplane, expected_type=type_hints["iotdataplane"])
            check_type(argname="argument iotdeviceadvisor", value=iotdeviceadvisor, expected_type=type_hints["iotdeviceadvisor"])
            check_type(argname="argument iotevents", value=iotevents, expected_type=type_hints["iotevents"])
            check_type(argname="argument ioteventsdata", value=ioteventsdata, expected_type=type_hints["ioteventsdata"])
            check_type(argname="argument iotfleethub", value=iotfleethub, expected_type=type_hints["iotfleethub"])
            check_type(argname="argument iotjobsdata", value=iotjobsdata, expected_type=type_hints["iotjobsdata"])
            check_type(argname="argument iotjobsdataplane", value=iotjobsdataplane, expected_type=type_hints["iotjobsdataplane"])
            check_type(argname="argument iotsecuretunneling", value=iotsecuretunneling, expected_type=type_hints["iotsecuretunneling"])
            check_type(argname="argument iotsitewise", value=iotsitewise, expected_type=type_hints["iotsitewise"])
            check_type(argname="argument iotthingsgraph", value=iotthingsgraph, expected_type=type_hints["iotthingsgraph"])
            check_type(argname="argument iottwinmaker", value=iottwinmaker, expected_type=type_hints["iottwinmaker"])
            check_type(argname="argument iotwireless", value=iotwireless, expected_type=type_hints["iotwireless"])
            check_type(argname="argument ivs", value=ivs, expected_type=type_hints["ivs"])
            check_type(argname="argument ivschat", value=ivschat, expected_type=type_hints["ivschat"])
            check_type(argname="argument kafka", value=kafka, expected_type=type_hints["kafka"])
            check_type(argname="argument kafkaconnect", value=kafkaconnect, expected_type=type_hints["kafkaconnect"])
            check_type(argname="argument kendra", value=kendra, expected_type=type_hints["kendra"])
            check_type(argname="argument keyspaces", value=keyspaces, expected_type=type_hints["keyspaces"])
            check_type(argname="argument kinesis", value=kinesis, expected_type=type_hints["kinesis"])
            check_type(argname="argument kinesisanalytics", value=kinesisanalytics, expected_type=type_hints["kinesisanalytics"])
            check_type(argname="argument kinesisanalyticsv2", value=kinesisanalyticsv2, expected_type=type_hints["kinesisanalyticsv2"])
            check_type(argname="argument kinesisvideo", value=kinesisvideo, expected_type=type_hints["kinesisvideo"])
            check_type(argname="argument kinesisvideoarchivedmedia", value=kinesisvideoarchivedmedia, expected_type=type_hints["kinesisvideoarchivedmedia"])
            check_type(argname="argument kinesisvideomedia", value=kinesisvideomedia, expected_type=type_hints["kinesisvideomedia"])
            check_type(argname="argument kinesisvideosignaling", value=kinesisvideosignaling, expected_type=type_hints["kinesisvideosignaling"])
            check_type(argname="argument kinesisvideosignalingchannels", value=kinesisvideosignalingchannels, expected_type=type_hints["kinesisvideosignalingchannels"])
            check_type(argname="argument kms", value=kms, expected_type=type_hints["kms"])
            check_type(argname="argument lakeformation", value=lakeformation, expected_type=type_hints["lakeformation"])
            check_type(argname="argument lambda_", value=lambda_, expected_type=type_hints["lambda_"])
            check_type(argname="argument lex", value=lex, expected_type=type_hints["lex"])
            check_type(argname="argument lexmodelbuilding", value=lexmodelbuilding, expected_type=type_hints["lexmodelbuilding"])
            check_type(argname="argument lexmodelbuildingservice", value=lexmodelbuildingservice, expected_type=type_hints["lexmodelbuildingservice"])
            check_type(argname="argument lexmodels", value=lexmodels, expected_type=type_hints["lexmodels"])
            check_type(argname="argument lexmodelsv2", value=lexmodelsv2, expected_type=type_hints["lexmodelsv2"])
            check_type(argname="argument lexruntime", value=lexruntime, expected_type=type_hints["lexruntime"])
            check_type(argname="argument lexruntimeservice", value=lexruntimeservice, expected_type=type_hints["lexruntimeservice"])
            check_type(argname="argument lexruntimev2", value=lexruntimev2, expected_type=type_hints["lexruntimev2"])
            check_type(argname="argument lexv2_models", value=lexv2_models, expected_type=type_hints["lexv2_models"])
            check_type(argname="argument lexv2_runtime", value=lexv2_runtime, expected_type=type_hints["lexv2_runtime"])
            check_type(argname="argument licensemanager", value=licensemanager, expected_type=type_hints["licensemanager"])
            check_type(argname="argument lightsail", value=lightsail, expected_type=type_hints["lightsail"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument locationservice", value=locationservice, expected_type=type_hints["locationservice"])
            check_type(argname="argument logs", value=logs, expected_type=type_hints["logs"])
            check_type(argname="argument lookoutequipment", value=lookoutequipment, expected_type=type_hints["lookoutequipment"])
            check_type(argname="argument lookoutforvision", value=lookoutforvision, expected_type=type_hints["lookoutforvision"])
            check_type(argname="argument lookoutmetrics", value=lookoutmetrics, expected_type=type_hints["lookoutmetrics"])
            check_type(argname="argument lookoutvision", value=lookoutvision, expected_type=type_hints["lookoutvision"])
            check_type(argname="argument machinelearning", value=machinelearning, expected_type=type_hints["machinelearning"])
            check_type(argname="argument macie", value=macie, expected_type=type_hints["macie"])
            check_type(argname="argument macie2", value=macie2, expected_type=type_hints["macie2"])
            check_type(argname="argument managedblockchain", value=managedblockchain, expected_type=type_hints["managedblockchain"])
            check_type(argname="argument managedgrafana", value=managedgrafana, expected_type=type_hints["managedgrafana"])
            check_type(argname="argument marketplacecatalog", value=marketplacecatalog, expected_type=type_hints["marketplacecatalog"])
            check_type(argname="argument marketplacecommerceanalytics", value=marketplacecommerceanalytics, expected_type=type_hints["marketplacecommerceanalytics"])
            check_type(argname="argument marketplaceentitlement", value=marketplaceentitlement, expected_type=type_hints["marketplaceentitlement"])
            check_type(argname="argument marketplaceentitlementservice", value=marketplaceentitlementservice, expected_type=type_hints["marketplaceentitlementservice"])
            check_type(argname="argument marketplacemetering", value=marketplacemetering, expected_type=type_hints["marketplacemetering"])
            check_type(argname="argument mediaconnect", value=mediaconnect, expected_type=type_hints["mediaconnect"])
            check_type(argname="argument mediaconvert", value=mediaconvert, expected_type=type_hints["mediaconvert"])
            check_type(argname="argument medialive", value=medialive, expected_type=type_hints["medialive"])
            check_type(argname="argument mediapackage", value=mediapackage, expected_type=type_hints["mediapackage"])
            check_type(argname="argument mediapackagevod", value=mediapackagevod, expected_type=type_hints["mediapackagevod"])
            check_type(argname="argument mediastore", value=mediastore, expected_type=type_hints["mediastore"])
            check_type(argname="argument mediastoredata", value=mediastoredata, expected_type=type_hints["mediastoredata"])
            check_type(argname="argument mediatailor", value=mediatailor, expected_type=type_hints["mediatailor"])
            check_type(argname="argument memorydb", value=memorydb, expected_type=type_hints["memorydb"])
            check_type(argname="argument meteringmarketplace", value=meteringmarketplace, expected_type=type_hints["meteringmarketplace"])
            check_type(argname="argument mgh", value=mgh, expected_type=type_hints["mgh"])
            check_type(argname="argument mgn", value=mgn, expected_type=type_hints["mgn"])
            check_type(argname="argument migrationhub", value=migrationhub, expected_type=type_hints["migrationhub"])
            check_type(argname="argument migrationhubconfig", value=migrationhubconfig, expected_type=type_hints["migrationhubconfig"])
            check_type(argname="argument migrationhubrefactorspaces", value=migrationhubrefactorspaces, expected_type=type_hints["migrationhubrefactorspaces"])
            check_type(argname="argument migrationhubstrategy", value=migrationhubstrategy, expected_type=type_hints["migrationhubstrategy"])
            check_type(argname="argument migrationhubstrategyrecommendations", value=migrationhubstrategyrecommendations, expected_type=type_hints["migrationhubstrategyrecommendations"])
            check_type(argname="argument mobile", value=mobile, expected_type=type_hints["mobile"])
            check_type(argname="argument mq", value=mq, expected_type=type_hints["mq"])
            check_type(argname="argument msk", value=msk, expected_type=type_hints["msk"])
            check_type(argname="argument mturk", value=mturk, expected_type=type_hints["mturk"])
            check_type(argname="argument mwaa", value=mwaa, expected_type=type_hints["mwaa"])
            check_type(argname="argument neptune", value=neptune, expected_type=type_hints["neptune"])
            check_type(argname="argument networkfirewall", value=networkfirewall, expected_type=type_hints["networkfirewall"])
            check_type(argname="argument networkmanager", value=networkmanager, expected_type=type_hints["networkmanager"])
            check_type(argname="argument nimble", value=nimble, expected_type=type_hints["nimble"])
            check_type(argname="argument nimblestudio", value=nimblestudio, expected_type=type_hints["nimblestudio"])
            check_type(argname="argument opensearch", value=opensearch, expected_type=type_hints["opensearch"])
            check_type(argname="argument opensearchserverless", value=opensearchserverless, expected_type=type_hints["opensearchserverless"])
            check_type(argname="argument opensearchservice", value=opensearchservice, expected_type=type_hints["opensearchservice"])
            check_type(argname="argument opsworks", value=opsworks, expected_type=type_hints["opsworks"])
            check_type(argname="argument opsworkscm", value=opsworkscm, expected_type=type_hints["opsworkscm"])
            check_type(argname="argument organizations", value=organizations, expected_type=type_hints["organizations"])
            check_type(argname="argument outposts", value=outposts, expected_type=type_hints["outposts"])
            check_type(argname="argument panorama", value=panorama, expected_type=type_hints["panorama"])
            check_type(argname="argument personalize", value=personalize, expected_type=type_hints["personalize"])
            check_type(argname="argument personalizeevents", value=personalizeevents, expected_type=type_hints["personalizeevents"])
            check_type(argname="argument personalizeruntime", value=personalizeruntime, expected_type=type_hints["personalizeruntime"])
            check_type(argname="argument pi", value=pi, expected_type=type_hints["pi"])
            check_type(argname="argument pinpoint", value=pinpoint, expected_type=type_hints["pinpoint"])
            check_type(argname="argument pinpointemail", value=pinpointemail, expected_type=type_hints["pinpointemail"])
            check_type(argname="argument pinpointsmsvoice", value=pinpointsmsvoice, expected_type=type_hints["pinpointsmsvoice"])
            check_type(argname="argument pipes", value=pipes, expected_type=type_hints["pipes"])
            check_type(argname="argument polly", value=polly, expected_type=type_hints["polly"])
            check_type(argname="argument pricing", value=pricing, expected_type=type_hints["pricing"])
            check_type(argname="argument prometheus", value=prometheus, expected_type=type_hints["prometheus"])
            check_type(argname="argument prometheusservice", value=prometheusservice, expected_type=type_hints["prometheusservice"])
            check_type(argname="argument proton", value=proton, expected_type=type_hints["proton"])
            check_type(argname="argument qldb", value=qldb, expected_type=type_hints["qldb"])
            check_type(argname="argument qldbsession", value=qldbsession, expected_type=type_hints["qldbsession"])
            check_type(argname="argument quicksight", value=quicksight, expected_type=type_hints["quicksight"])
            check_type(argname="argument ram", value=ram, expected_type=type_hints["ram"])
            check_type(argname="argument rbin", value=rbin, expected_type=type_hints["rbin"])
            check_type(argname="argument rds", value=rds, expected_type=type_hints["rds"])
            check_type(argname="argument rdsdata", value=rdsdata, expected_type=type_hints["rdsdata"])
            check_type(argname="argument rdsdataservice", value=rdsdataservice, expected_type=type_hints["rdsdataservice"])
            check_type(argname="argument recyclebin", value=recyclebin, expected_type=type_hints["recyclebin"])
            check_type(argname="argument redshift", value=redshift, expected_type=type_hints["redshift"])
            check_type(argname="argument redshiftdata", value=redshiftdata, expected_type=type_hints["redshiftdata"])
            check_type(argname="argument redshiftdataapiservice", value=redshiftdataapiservice, expected_type=type_hints["redshiftdataapiservice"])
            check_type(argname="argument redshiftserverless", value=redshiftserverless, expected_type=type_hints["redshiftserverless"])
            check_type(argname="argument rekognition", value=rekognition, expected_type=type_hints["rekognition"])
            check_type(argname="argument resiliencehub", value=resiliencehub, expected_type=type_hints["resiliencehub"])
            check_type(argname="argument resourceexplorer2", value=resourceexplorer2, expected_type=type_hints["resourceexplorer2"])
            check_type(argname="argument resourcegroups", value=resourcegroups, expected_type=type_hints["resourcegroups"])
            check_type(argname="argument resourcegroupstagging", value=resourcegroupstagging, expected_type=type_hints["resourcegroupstagging"])
            check_type(argname="argument resourcegroupstaggingapi", value=resourcegroupstaggingapi, expected_type=type_hints["resourcegroupstaggingapi"])
            check_type(argname="argument robomaker", value=robomaker, expected_type=type_hints["robomaker"])
            check_type(argname="argument rolesanywhere", value=rolesanywhere, expected_type=type_hints["rolesanywhere"])
            check_type(argname="argument route53", value=route53, expected_type=type_hints["route53"])
            check_type(argname="argument route53_domains", value=route53_domains, expected_type=type_hints["route53_domains"])
            check_type(argname="argument route53_recoverycluster", value=route53_recoverycluster, expected_type=type_hints["route53_recoverycluster"])
            check_type(argname="argument route53_recoverycontrolconfig", value=route53_recoverycontrolconfig, expected_type=type_hints["route53_recoverycontrolconfig"])
            check_type(argname="argument route53_recoveryreadiness", value=route53_recoveryreadiness, expected_type=type_hints["route53_recoveryreadiness"])
            check_type(argname="argument route53_resolver", value=route53_resolver, expected_type=type_hints["route53_resolver"])
            check_type(argname="argument rum", value=rum, expected_type=type_hints["rum"])
            check_type(argname="argument s3", value=s3, expected_type=type_hints["s3"])
            check_type(argname="argument s3_api", value=s3_api, expected_type=type_hints["s3_api"])
            check_type(argname="argument s3_control", value=s3_control, expected_type=type_hints["s3_control"])
            check_type(argname="argument s3_outposts", value=s3_outposts, expected_type=type_hints["s3_outposts"])
            check_type(argname="argument sagemaker", value=sagemaker, expected_type=type_hints["sagemaker"])
            check_type(argname="argument sagemakera2_iruntime", value=sagemakera2_iruntime, expected_type=type_hints["sagemakera2_iruntime"])
            check_type(argname="argument sagemakeredge", value=sagemakeredge, expected_type=type_hints["sagemakeredge"])
            check_type(argname="argument sagemakeredgemanager", value=sagemakeredgemanager, expected_type=type_hints["sagemakeredgemanager"])
            check_type(argname="argument sagemakerfeaturestoreruntime", value=sagemakerfeaturestoreruntime, expected_type=type_hints["sagemakerfeaturestoreruntime"])
            check_type(argname="argument sagemakerruntime", value=sagemakerruntime, expected_type=type_hints["sagemakerruntime"])
            check_type(argname="argument savingsplans", value=savingsplans, expected_type=type_hints["savingsplans"])
            check_type(argname="argument scheduler", value=scheduler, expected_type=type_hints["scheduler"])
            check_type(argname="argument schemas", value=schemas, expected_type=type_hints["schemas"])
            check_type(argname="argument sdb", value=sdb, expected_type=type_hints["sdb"])
            check_type(argname="argument secretsmanager", value=secretsmanager, expected_type=type_hints["secretsmanager"])
            check_type(argname="argument securityhub", value=securityhub, expected_type=type_hints["securityhub"])
            check_type(argname="argument serverlessapplicationrepository", value=serverlessapplicationrepository, expected_type=type_hints["serverlessapplicationrepository"])
            check_type(argname="argument serverlessapprepo", value=serverlessapprepo, expected_type=type_hints["serverlessapprepo"])
            check_type(argname="argument serverlessrepo", value=serverlessrepo, expected_type=type_hints["serverlessrepo"])
            check_type(argname="argument servicecatalog", value=servicecatalog, expected_type=type_hints["servicecatalog"])
            check_type(argname="argument servicecatalogappregistry", value=servicecatalogappregistry, expected_type=type_hints["servicecatalogappregistry"])
            check_type(argname="argument servicediscovery", value=servicediscovery, expected_type=type_hints["servicediscovery"])
            check_type(argname="argument servicequotas", value=servicequotas, expected_type=type_hints["servicequotas"])
            check_type(argname="argument ses", value=ses, expected_type=type_hints["ses"])
            check_type(argname="argument sesv2", value=sesv2, expected_type=type_hints["sesv2"])
            check_type(argname="argument sfn", value=sfn, expected_type=type_hints["sfn"])
            check_type(argname="argument shield", value=shield, expected_type=type_hints["shield"])
            check_type(argname="argument signer", value=signer, expected_type=type_hints["signer"])
            check_type(argname="argument simpledb", value=simpledb, expected_type=type_hints["simpledb"])
            check_type(argname="argument sms", value=sms, expected_type=type_hints["sms"])
            check_type(argname="argument snowball", value=snowball, expected_type=type_hints["snowball"])
            check_type(argname="argument snowdevicemanagement", value=snowdevicemanagement, expected_type=type_hints["snowdevicemanagement"])
            check_type(argname="argument sns", value=sns, expected_type=type_hints["sns"])
            check_type(argname="argument sqs", value=sqs, expected_type=type_hints["sqs"])
            check_type(argname="argument ssm", value=ssm, expected_type=type_hints["ssm"])
            check_type(argname="argument ssmcontacts", value=ssmcontacts, expected_type=type_hints["ssmcontacts"])
            check_type(argname="argument ssmincidents", value=ssmincidents, expected_type=type_hints["ssmincidents"])
            check_type(argname="argument sso", value=sso, expected_type=type_hints["sso"])
            check_type(argname="argument ssoadmin", value=ssoadmin, expected_type=type_hints["ssoadmin"])
            check_type(argname="argument ssooidc", value=ssooidc, expected_type=type_hints["ssooidc"])
            check_type(argname="argument stepfunctions", value=stepfunctions, expected_type=type_hints["stepfunctions"])
            check_type(argname="argument storagegateway", value=storagegateway, expected_type=type_hints["storagegateway"])
            check_type(argname="argument sts", value=sts, expected_type=type_hints["sts"])
            check_type(argname="argument support", value=support, expected_type=type_hints["support"])
            check_type(argname="argument swf", value=swf, expected_type=type_hints["swf"])
            check_type(argname="argument synthetics", value=synthetics, expected_type=type_hints["synthetics"])
            check_type(argname="argument textract", value=textract, expected_type=type_hints["textract"])
            check_type(argname="argument timestreamquery", value=timestreamquery, expected_type=type_hints["timestreamquery"])
            check_type(argname="argument timestreamwrite", value=timestreamwrite, expected_type=type_hints["timestreamwrite"])
            check_type(argname="argument transcribe", value=transcribe, expected_type=type_hints["transcribe"])
            check_type(argname="argument transcribeservice", value=transcribeservice, expected_type=type_hints["transcribeservice"])
            check_type(argname="argument transcribestreaming", value=transcribestreaming, expected_type=type_hints["transcribestreaming"])
            check_type(argname="argument transcribestreamingservice", value=transcribestreamingservice, expected_type=type_hints["transcribestreamingservice"])
            check_type(argname="argument transfer", value=transfer, expected_type=type_hints["transfer"])
            check_type(argname="argument translate", value=translate, expected_type=type_hints["translate"])
            check_type(argname="argument voiceid", value=voiceid, expected_type=type_hints["voiceid"])
            check_type(argname="argument waf", value=waf, expected_type=type_hints["waf"])
            check_type(argname="argument wafregional", value=wafregional, expected_type=type_hints["wafregional"])
            check_type(argname="argument wafv2", value=wafv2, expected_type=type_hints["wafv2"])
            check_type(argname="argument wellarchitected", value=wellarchitected, expected_type=type_hints["wellarchitected"])
            check_type(argname="argument wisdom", value=wisdom, expected_type=type_hints["wisdom"])
            check_type(argname="argument workdocs", value=workdocs, expected_type=type_hints["workdocs"])
            check_type(argname="argument worklink", value=worklink, expected_type=type_hints["worklink"])
            check_type(argname="argument workmail", value=workmail, expected_type=type_hints["workmail"])
            check_type(argname="argument workmailmessageflow", value=workmailmessageflow, expected_type=type_hints["workmailmessageflow"])
            check_type(argname="argument workspaces", value=workspaces, expected_type=type_hints["workspaces"])
            check_type(argname="argument workspacesweb", value=workspacesweb, expected_type=type_hints["workspacesweb"])
            check_type(argname="argument xray", value=xray, expected_type=type_hints["xray"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if accessanalyzer is not None:
            self._values["accessanalyzer"] = accessanalyzer
        if account is not None:
            self._values["account"] = account
        if acm is not None:
            self._values["acm"] = acm
        if acmpca is not None:
            self._values["acmpca"] = acmpca
        if alexaforbusiness is not None:
            self._values["alexaforbusiness"] = alexaforbusiness
        if amg is not None:
            self._values["amg"] = amg
        if amp is not None:
            self._values["amp"] = amp
        if amplify is not None:
            self._values["amplify"] = amplify
        if amplifybackend is not None:
            self._values["amplifybackend"] = amplifybackend
        if amplifyuibuilder is not None:
            self._values["amplifyuibuilder"] = amplifyuibuilder
        if apigateway is not None:
            self._values["apigateway"] = apigateway
        if apigatewaymanagementapi is not None:
            self._values["apigatewaymanagementapi"] = apigatewaymanagementapi
        if apigatewayv2 is not None:
            self._values["apigatewayv2"] = apigatewayv2
        if appautoscaling is not None:
            self._values["appautoscaling"] = appautoscaling
        if appconfig is not None:
            self._values["appconfig"] = appconfig
        if appconfigdata is not None:
            self._values["appconfigdata"] = appconfigdata
        if appflow is not None:
            self._values["appflow"] = appflow
        if appintegrations is not None:
            self._values["appintegrations"] = appintegrations
        if appintegrationsservice is not None:
            self._values["appintegrationsservice"] = appintegrationsservice
        if applicationautoscaling is not None:
            self._values["applicationautoscaling"] = applicationautoscaling
        if applicationcostprofiler is not None:
            self._values["applicationcostprofiler"] = applicationcostprofiler
        if applicationdiscovery is not None:
            self._values["applicationdiscovery"] = applicationdiscovery
        if applicationdiscoveryservice is not None:
            self._values["applicationdiscoveryservice"] = applicationdiscoveryservice
        if applicationinsights is not None:
            self._values["applicationinsights"] = applicationinsights
        if appmesh is not None:
            self._values["appmesh"] = appmesh
        if appregistry is not None:
            self._values["appregistry"] = appregistry
        if apprunner is not None:
            self._values["apprunner"] = apprunner
        if appstream is not None:
            self._values["appstream"] = appstream
        if appsync is not None:
            self._values["appsync"] = appsync
        if athena is not None:
            self._values["athena"] = athena
        if auditmanager is not None:
            self._values["auditmanager"] = auditmanager
        if augmentedairuntime is not None:
            self._values["augmentedairuntime"] = augmentedairuntime
        if autoscaling is not None:
            self._values["autoscaling"] = autoscaling
        if autoscalingplans is not None:
            self._values["autoscalingplans"] = autoscalingplans
        if backup is not None:
            self._values["backup"] = backup
        if backupgateway is not None:
            self._values["backupgateway"] = backupgateway
        if batch is not None:
            self._values["batch"] = batch
        if beanstalk is not None:
            self._values["beanstalk"] = beanstalk
        if billingconductor is not None:
            self._values["billingconductor"] = billingconductor
        if braket is not None:
            self._values["braket"] = braket
        if budgets is not None:
            self._values["budgets"] = budgets
        if ce is not None:
            self._values["ce"] = ce
        if chime is not None:
            self._values["chime"] = chime
        if chimesdkidentity is not None:
            self._values["chimesdkidentity"] = chimesdkidentity
        if chimesdkmeetings is not None:
            self._values["chimesdkmeetings"] = chimesdkmeetings
        if chimesdkmessaging is not None:
            self._values["chimesdkmessaging"] = chimesdkmessaging
        if cloud9 is not None:
            self._values["cloud9"] = cloud9
        if cloudcontrol is not None:
            self._values["cloudcontrol"] = cloudcontrol
        if cloudcontrolapi is not None:
            self._values["cloudcontrolapi"] = cloudcontrolapi
        if clouddirectory is not None:
            self._values["clouddirectory"] = clouddirectory
        if cloudformation is not None:
            self._values["cloudformation"] = cloudformation
        if cloudfront is not None:
            self._values["cloudfront"] = cloudfront
        if cloudhsm is not None:
            self._values["cloudhsm"] = cloudhsm
        if cloudhsmv2 is not None:
            self._values["cloudhsmv2"] = cloudhsmv2
        if cloudsearch is not None:
            self._values["cloudsearch"] = cloudsearch
        if cloudsearchdomain is not None:
            self._values["cloudsearchdomain"] = cloudsearchdomain
        if cloudtrail is not None:
            self._values["cloudtrail"] = cloudtrail
        if cloudwatch is not None:
            self._values["cloudwatch"] = cloudwatch
        if cloudwatchevents is not None:
            self._values["cloudwatchevents"] = cloudwatchevents
        if cloudwatchevidently is not None:
            self._values["cloudwatchevidently"] = cloudwatchevidently
        if cloudwatchlog is not None:
            self._values["cloudwatchlog"] = cloudwatchlog
        if cloudwatchlogs is not None:
            self._values["cloudwatchlogs"] = cloudwatchlogs
        if cloudwatchrum is not None:
            self._values["cloudwatchrum"] = cloudwatchrum
        if codeartifact is not None:
            self._values["codeartifact"] = codeartifact
        if codebuild is not None:
            self._values["codebuild"] = codebuild
        if codecommit is not None:
            self._values["codecommit"] = codecommit
        if codedeploy is not None:
            self._values["codedeploy"] = codedeploy
        if codeguruprofiler is not None:
            self._values["codeguruprofiler"] = codeguruprofiler
        if codegurureviewer is not None:
            self._values["codegurureviewer"] = codegurureviewer
        if codepipeline is not None:
            self._values["codepipeline"] = codepipeline
        if codestar is not None:
            self._values["codestar"] = codestar
        if codestarconnections is not None:
            self._values["codestarconnections"] = codestarconnections
        if codestarnotifications is not None:
            self._values["codestarnotifications"] = codestarnotifications
        if cognitoidentity is not None:
            self._values["cognitoidentity"] = cognitoidentity
        if cognitoidentityprovider is not None:
            self._values["cognitoidentityprovider"] = cognitoidentityprovider
        if cognitoidp is not None:
            self._values["cognitoidp"] = cognitoidp
        if cognitosync is not None:
            self._values["cognitosync"] = cognitosync
        if comprehend is not None:
            self._values["comprehend"] = comprehend
        if comprehendmedical is not None:
            self._values["comprehendmedical"] = comprehendmedical
        if computeoptimizer is not None:
            self._values["computeoptimizer"] = computeoptimizer
        if config is not None:
            self._values["config"] = config
        if configservice is not None:
            self._values["configservice"] = configservice
        if connect is not None:
            self._values["connect"] = connect
        if connectcontactlens is not None:
            self._values["connectcontactlens"] = connectcontactlens
        if connectparticipant is not None:
            self._values["connectparticipant"] = connectparticipant
        if connectwisdomservice is not None:
            self._values["connectwisdomservice"] = connectwisdomservice
        if controltower is not None:
            self._values["controltower"] = controltower
        if costandusagereportservice is not None:
            self._values["costandusagereportservice"] = costandusagereportservice
        if costexplorer is not None:
            self._values["costexplorer"] = costexplorer
        if cur is not None:
            self._values["cur"] = cur
        if customerprofiles is not None:
            self._values["customerprofiles"] = customerprofiles
        if databasemigration is not None:
            self._values["databasemigration"] = databasemigration
        if databasemigrationservice is not None:
            self._values["databasemigrationservice"] = databasemigrationservice
        if databrew is not None:
            self._values["databrew"] = databrew
        if dataexchange is not None:
            self._values["dataexchange"] = dataexchange
        if datapipeline is not None:
            self._values["datapipeline"] = datapipeline
        if datasync is not None:
            self._values["datasync"] = datasync
        if dax is not None:
            self._values["dax"] = dax
        if deploy is not None:
            self._values["deploy"] = deploy
        if detective is not None:
            self._values["detective"] = detective
        if devicefarm is not None:
            self._values["devicefarm"] = devicefarm
        if devopsguru is not None:
            self._values["devopsguru"] = devopsguru
        if directconnect is not None:
            self._values["directconnect"] = directconnect
        if directoryservice is not None:
            self._values["directoryservice"] = directoryservice
        if discovery is not None:
            self._values["discovery"] = discovery
        if dlm is not None:
            self._values["dlm"] = dlm
        if dms is not None:
            self._values["dms"] = dms
        if docdb is not None:
            self._values["docdb"] = docdb
        if drs is not None:
            self._values["drs"] = drs
        if ds is not None:
            self._values["ds"] = ds
        if dynamodb is not None:
            self._values["dynamodb"] = dynamodb
        if dynamodbstreams is not None:
            self._values["dynamodbstreams"] = dynamodbstreams
        if ebs is not None:
            self._values["ebs"] = ebs
        if ec2 is not None:
            self._values["ec2"] = ec2
        if ec2_instanceconnect is not None:
            self._values["ec2_instanceconnect"] = ec2_instanceconnect
        if ecr is not None:
            self._values["ecr"] = ecr
        if ecrpublic is not None:
            self._values["ecrpublic"] = ecrpublic
        if ecs is not None:
            self._values["ecs"] = ecs
        if efs is not None:
            self._values["efs"] = efs
        if eks is not None:
            self._values["eks"] = eks
        if elasticache is not None:
            self._values["elasticache"] = elasticache
        if elasticbeanstalk is not None:
            self._values["elasticbeanstalk"] = elasticbeanstalk
        if elasticinference is not None:
            self._values["elasticinference"] = elasticinference
        if elasticloadbalancing is not None:
            self._values["elasticloadbalancing"] = elasticloadbalancing
        if elasticloadbalancingv2 is not None:
            self._values["elasticloadbalancingv2"] = elasticloadbalancingv2
        if elasticsearch is not None:
            self._values["elasticsearch"] = elasticsearch
        if elasticsearchservice is not None:
            self._values["elasticsearchservice"] = elasticsearchservice
        if elastictranscoder is not None:
            self._values["elastictranscoder"] = elastictranscoder
        if elb is not None:
            self._values["elb"] = elb
        if elbv2 is not None:
            self._values["elbv2"] = elbv2
        if emr is not None:
            self._values["emr"] = emr
        if emrcontainers is not None:
            self._values["emrcontainers"] = emrcontainers
        if emrserverless is not None:
            self._values["emrserverless"] = emrserverless
        if es is not None:
            self._values["es"] = es
        if eventbridge is not None:
            self._values["eventbridge"] = eventbridge
        if events is not None:
            self._values["events"] = events
        if evidently is not None:
            self._values["evidently"] = evidently
        if finspace is not None:
            self._values["finspace"] = finspace
        if finspacedata is not None:
            self._values["finspacedata"] = finspacedata
        if firehose is not None:
            self._values["firehose"] = firehose
        if fis is not None:
            self._values["fis"] = fis
        if fms is not None:
            self._values["fms"] = fms
        if forecast is not None:
            self._values["forecast"] = forecast
        if forecastquery is not None:
            self._values["forecastquery"] = forecastquery
        if forecastqueryservice is not None:
            self._values["forecastqueryservice"] = forecastqueryservice
        if forecastservice is not None:
            self._values["forecastservice"] = forecastservice
        if frauddetector is not None:
            self._values["frauddetector"] = frauddetector
        if fsx is not None:
            self._values["fsx"] = fsx
        if gamelift is not None:
            self._values["gamelift"] = gamelift
        if glacier is not None:
            self._values["glacier"] = glacier
        if globalaccelerator is not None:
            self._values["globalaccelerator"] = globalaccelerator
        if glue is not None:
            self._values["glue"] = glue
        if gluedatabrew is not None:
            self._values["gluedatabrew"] = gluedatabrew
        if grafana is not None:
            self._values["grafana"] = grafana
        if greengrass is not None:
            self._values["greengrass"] = greengrass
        if greengrassv2 is not None:
            self._values["greengrassv2"] = greengrassv2
        if groundstation is not None:
            self._values["groundstation"] = groundstation
        if guardduty is not None:
            self._values["guardduty"] = guardduty
        if health is not None:
            self._values["health"] = health
        if healthlake is not None:
            self._values["healthlake"] = healthlake
        if honeycode is not None:
            self._values["honeycode"] = honeycode
        if iam is not None:
            self._values["iam"] = iam
        if identitystore is not None:
            self._values["identitystore"] = identitystore
        if imagebuilder is not None:
            self._values["imagebuilder"] = imagebuilder
        if inspector is not None:
            self._values["inspector"] = inspector
        if inspector2 is not None:
            self._values["inspector2"] = inspector2
        if inspectorv2 is not None:
            self._values["inspectorv2"] = inspectorv2
        if iot is not None:
            self._values["iot"] = iot
        if iot1_clickdevices is not None:
            self._values["iot1_clickdevices"] = iot1_clickdevices
        if iot1_clickdevicesservice is not None:
            self._values["iot1_clickdevicesservice"] = iot1_clickdevicesservice
        if iot1_clickprojects is not None:
            self._values["iot1_clickprojects"] = iot1_clickprojects
        if iotanalytics is not None:
            self._values["iotanalytics"] = iotanalytics
        if iotdata is not None:
            self._values["iotdata"] = iotdata
        if iotdataplane is not None:
            self._values["iotdataplane"] = iotdataplane
        if iotdeviceadvisor is not None:
            self._values["iotdeviceadvisor"] = iotdeviceadvisor
        if iotevents is not None:
            self._values["iotevents"] = iotevents
        if ioteventsdata is not None:
            self._values["ioteventsdata"] = ioteventsdata
        if iotfleethub is not None:
            self._values["iotfleethub"] = iotfleethub
        if iotjobsdata is not None:
            self._values["iotjobsdata"] = iotjobsdata
        if iotjobsdataplane is not None:
            self._values["iotjobsdataplane"] = iotjobsdataplane
        if iotsecuretunneling is not None:
            self._values["iotsecuretunneling"] = iotsecuretunneling
        if iotsitewise is not None:
            self._values["iotsitewise"] = iotsitewise
        if iotthingsgraph is not None:
            self._values["iotthingsgraph"] = iotthingsgraph
        if iottwinmaker is not None:
            self._values["iottwinmaker"] = iottwinmaker
        if iotwireless is not None:
            self._values["iotwireless"] = iotwireless
        if ivs is not None:
            self._values["ivs"] = ivs
        if ivschat is not None:
            self._values["ivschat"] = ivschat
        if kafka is not None:
            self._values["kafka"] = kafka
        if kafkaconnect is not None:
            self._values["kafkaconnect"] = kafkaconnect
        if kendra is not None:
            self._values["kendra"] = kendra
        if keyspaces is not None:
            self._values["keyspaces"] = keyspaces
        if kinesis is not None:
            self._values["kinesis"] = kinesis
        if kinesisanalytics is not None:
            self._values["kinesisanalytics"] = kinesisanalytics
        if kinesisanalyticsv2 is not None:
            self._values["kinesisanalyticsv2"] = kinesisanalyticsv2
        if kinesisvideo is not None:
            self._values["kinesisvideo"] = kinesisvideo
        if kinesisvideoarchivedmedia is not None:
            self._values["kinesisvideoarchivedmedia"] = kinesisvideoarchivedmedia
        if kinesisvideomedia is not None:
            self._values["kinesisvideomedia"] = kinesisvideomedia
        if kinesisvideosignaling is not None:
            self._values["kinesisvideosignaling"] = kinesisvideosignaling
        if kinesisvideosignalingchannels is not None:
            self._values["kinesisvideosignalingchannels"] = kinesisvideosignalingchannels
        if kms is not None:
            self._values["kms"] = kms
        if lakeformation is not None:
            self._values["lakeformation"] = lakeformation
        if lambda_ is not None:
            self._values["lambda_"] = lambda_
        if lex is not None:
            self._values["lex"] = lex
        if lexmodelbuilding is not None:
            self._values["lexmodelbuilding"] = lexmodelbuilding
        if lexmodelbuildingservice is not None:
            self._values["lexmodelbuildingservice"] = lexmodelbuildingservice
        if lexmodels is not None:
            self._values["lexmodels"] = lexmodels
        if lexmodelsv2 is not None:
            self._values["lexmodelsv2"] = lexmodelsv2
        if lexruntime is not None:
            self._values["lexruntime"] = lexruntime
        if lexruntimeservice is not None:
            self._values["lexruntimeservice"] = lexruntimeservice
        if lexruntimev2 is not None:
            self._values["lexruntimev2"] = lexruntimev2
        if lexv2_models is not None:
            self._values["lexv2_models"] = lexv2_models
        if lexv2_runtime is not None:
            self._values["lexv2_runtime"] = lexv2_runtime
        if licensemanager is not None:
            self._values["licensemanager"] = licensemanager
        if lightsail is not None:
            self._values["lightsail"] = lightsail
        if location is not None:
            self._values["location"] = location
        if locationservice is not None:
            self._values["locationservice"] = locationservice
        if logs is not None:
            self._values["logs"] = logs
        if lookoutequipment is not None:
            self._values["lookoutequipment"] = lookoutequipment
        if lookoutforvision is not None:
            self._values["lookoutforvision"] = lookoutforvision
        if lookoutmetrics is not None:
            self._values["lookoutmetrics"] = lookoutmetrics
        if lookoutvision is not None:
            self._values["lookoutvision"] = lookoutvision
        if machinelearning is not None:
            self._values["machinelearning"] = machinelearning
        if macie is not None:
            self._values["macie"] = macie
        if macie2 is not None:
            self._values["macie2"] = macie2
        if managedblockchain is not None:
            self._values["managedblockchain"] = managedblockchain
        if managedgrafana is not None:
            self._values["managedgrafana"] = managedgrafana
        if marketplacecatalog is not None:
            self._values["marketplacecatalog"] = marketplacecatalog
        if marketplacecommerceanalytics is not None:
            self._values["marketplacecommerceanalytics"] = marketplacecommerceanalytics
        if marketplaceentitlement is not None:
            self._values["marketplaceentitlement"] = marketplaceentitlement
        if marketplaceentitlementservice is not None:
            self._values["marketplaceentitlementservice"] = marketplaceentitlementservice
        if marketplacemetering is not None:
            self._values["marketplacemetering"] = marketplacemetering
        if mediaconnect is not None:
            self._values["mediaconnect"] = mediaconnect
        if mediaconvert is not None:
            self._values["mediaconvert"] = mediaconvert
        if medialive is not None:
            self._values["medialive"] = medialive
        if mediapackage is not None:
            self._values["mediapackage"] = mediapackage
        if mediapackagevod is not None:
            self._values["mediapackagevod"] = mediapackagevod
        if mediastore is not None:
            self._values["mediastore"] = mediastore
        if mediastoredata is not None:
            self._values["mediastoredata"] = mediastoredata
        if mediatailor is not None:
            self._values["mediatailor"] = mediatailor
        if memorydb is not None:
            self._values["memorydb"] = memorydb
        if meteringmarketplace is not None:
            self._values["meteringmarketplace"] = meteringmarketplace
        if mgh is not None:
            self._values["mgh"] = mgh
        if mgn is not None:
            self._values["mgn"] = mgn
        if migrationhub is not None:
            self._values["migrationhub"] = migrationhub
        if migrationhubconfig is not None:
            self._values["migrationhubconfig"] = migrationhubconfig
        if migrationhubrefactorspaces is not None:
            self._values["migrationhubrefactorspaces"] = migrationhubrefactorspaces
        if migrationhubstrategy is not None:
            self._values["migrationhubstrategy"] = migrationhubstrategy
        if migrationhubstrategyrecommendations is not None:
            self._values["migrationhubstrategyrecommendations"] = migrationhubstrategyrecommendations
        if mobile is not None:
            self._values["mobile"] = mobile
        if mq is not None:
            self._values["mq"] = mq
        if msk is not None:
            self._values["msk"] = msk
        if mturk is not None:
            self._values["mturk"] = mturk
        if mwaa is not None:
            self._values["mwaa"] = mwaa
        if neptune is not None:
            self._values["neptune"] = neptune
        if networkfirewall is not None:
            self._values["networkfirewall"] = networkfirewall
        if networkmanager is not None:
            self._values["networkmanager"] = networkmanager
        if nimble is not None:
            self._values["nimble"] = nimble
        if nimblestudio is not None:
            self._values["nimblestudio"] = nimblestudio
        if opensearch is not None:
            self._values["opensearch"] = opensearch
        if opensearchserverless is not None:
            self._values["opensearchserverless"] = opensearchserverless
        if opensearchservice is not None:
            self._values["opensearchservice"] = opensearchservice
        if opsworks is not None:
            self._values["opsworks"] = opsworks
        if opsworkscm is not None:
            self._values["opsworkscm"] = opsworkscm
        if organizations is not None:
            self._values["organizations"] = organizations
        if outposts is not None:
            self._values["outposts"] = outposts
        if panorama is not None:
            self._values["panorama"] = panorama
        if personalize is not None:
            self._values["personalize"] = personalize
        if personalizeevents is not None:
            self._values["personalizeevents"] = personalizeevents
        if personalizeruntime is not None:
            self._values["personalizeruntime"] = personalizeruntime
        if pi is not None:
            self._values["pi"] = pi
        if pinpoint is not None:
            self._values["pinpoint"] = pinpoint
        if pinpointemail is not None:
            self._values["pinpointemail"] = pinpointemail
        if pinpointsmsvoice is not None:
            self._values["pinpointsmsvoice"] = pinpointsmsvoice
        if pipes is not None:
            self._values["pipes"] = pipes
        if polly is not None:
            self._values["polly"] = polly
        if pricing is not None:
            self._values["pricing"] = pricing
        if prometheus is not None:
            self._values["prometheus"] = prometheus
        if prometheusservice is not None:
            self._values["prometheusservice"] = prometheusservice
        if proton is not None:
            self._values["proton"] = proton
        if qldb is not None:
            self._values["qldb"] = qldb
        if qldbsession is not None:
            self._values["qldbsession"] = qldbsession
        if quicksight is not None:
            self._values["quicksight"] = quicksight
        if ram is not None:
            self._values["ram"] = ram
        if rbin is not None:
            self._values["rbin"] = rbin
        if rds is not None:
            self._values["rds"] = rds
        if rdsdata is not None:
            self._values["rdsdata"] = rdsdata
        if rdsdataservice is not None:
            self._values["rdsdataservice"] = rdsdataservice
        if recyclebin is not None:
            self._values["recyclebin"] = recyclebin
        if redshift is not None:
            self._values["redshift"] = redshift
        if redshiftdata is not None:
            self._values["redshiftdata"] = redshiftdata
        if redshiftdataapiservice is not None:
            self._values["redshiftdataapiservice"] = redshiftdataapiservice
        if redshiftserverless is not None:
            self._values["redshiftserverless"] = redshiftserverless
        if rekognition is not None:
            self._values["rekognition"] = rekognition
        if resiliencehub is not None:
            self._values["resiliencehub"] = resiliencehub
        if resourceexplorer2 is not None:
            self._values["resourceexplorer2"] = resourceexplorer2
        if resourcegroups is not None:
            self._values["resourcegroups"] = resourcegroups
        if resourcegroupstagging is not None:
            self._values["resourcegroupstagging"] = resourcegroupstagging
        if resourcegroupstaggingapi is not None:
            self._values["resourcegroupstaggingapi"] = resourcegroupstaggingapi
        if robomaker is not None:
            self._values["robomaker"] = robomaker
        if rolesanywhere is not None:
            self._values["rolesanywhere"] = rolesanywhere
        if route53 is not None:
            self._values["route53"] = route53
        if route53_domains is not None:
            self._values["route53_domains"] = route53_domains
        if route53_recoverycluster is not None:
            self._values["route53_recoverycluster"] = route53_recoverycluster
        if route53_recoverycontrolconfig is not None:
            self._values["route53_recoverycontrolconfig"] = route53_recoverycontrolconfig
        if route53_recoveryreadiness is not None:
            self._values["route53_recoveryreadiness"] = route53_recoveryreadiness
        if route53_resolver is not None:
            self._values["route53_resolver"] = route53_resolver
        if rum is not None:
            self._values["rum"] = rum
        if s3 is not None:
            self._values["s3"] = s3
        if s3_api is not None:
            self._values["s3_api"] = s3_api
        if s3_control is not None:
            self._values["s3_control"] = s3_control
        if s3_outposts is not None:
            self._values["s3_outposts"] = s3_outposts
        if sagemaker is not None:
            self._values["sagemaker"] = sagemaker
        if sagemakera2_iruntime is not None:
            self._values["sagemakera2_iruntime"] = sagemakera2_iruntime
        if sagemakeredge is not None:
            self._values["sagemakeredge"] = sagemakeredge
        if sagemakeredgemanager is not None:
            self._values["sagemakeredgemanager"] = sagemakeredgemanager
        if sagemakerfeaturestoreruntime is not None:
            self._values["sagemakerfeaturestoreruntime"] = sagemakerfeaturestoreruntime
        if sagemakerruntime is not None:
            self._values["sagemakerruntime"] = sagemakerruntime
        if savingsplans is not None:
            self._values["savingsplans"] = savingsplans
        if scheduler is not None:
            self._values["scheduler"] = scheduler
        if schemas is not None:
            self._values["schemas"] = schemas
        if sdb is not None:
            self._values["sdb"] = sdb
        if secretsmanager is not None:
            self._values["secretsmanager"] = secretsmanager
        if securityhub is not None:
            self._values["securityhub"] = securityhub
        if serverlessapplicationrepository is not None:
            self._values["serverlessapplicationrepository"] = serverlessapplicationrepository
        if serverlessapprepo is not None:
            self._values["serverlessapprepo"] = serverlessapprepo
        if serverlessrepo is not None:
            self._values["serverlessrepo"] = serverlessrepo
        if servicecatalog is not None:
            self._values["servicecatalog"] = servicecatalog
        if servicecatalogappregistry is not None:
            self._values["servicecatalogappregistry"] = servicecatalogappregistry
        if servicediscovery is not None:
            self._values["servicediscovery"] = servicediscovery
        if servicequotas is not None:
            self._values["servicequotas"] = servicequotas
        if ses is not None:
            self._values["ses"] = ses
        if sesv2 is not None:
            self._values["sesv2"] = sesv2
        if sfn is not None:
            self._values["sfn"] = sfn
        if shield is not None:
            self._values["shield"] = shield
        if signer is not None:
            self._values["signer"] = signer
        if simpledb is not None:
            self._values["simpledb"] = simpledb
        if sms is not None:
            self._values["sms"] = sms
        if snowball is not None:
            self._values["snowball"] = snowball
        if snowdevicemanagement is not None:
            self._values["snowdevicemanagement"] = snowdevicemanagement
        if sns is not None:
            self._values["sns"] = sns
        if sqs is not None:
            self._values["sqs"] = sqs
        if ssm is not None:
            self._values["ssm"] = ssm
        if ssmcontacts is not None:
            self._values["ssmcontacts"] = ssmcontacts
        if ssmincidents is not None:
            self._values["ssmincidents"] = ssmincidents
        if sso is not None:
            self._values["sso"] = sso
        if ssoadmin is not None:
            self._values["ssoadmin"] = ssoadmin
        if ssooidc is not None:
            self._values["ssooidc"] = ssooidc
        if stepfunctions is not None:
            self._values["stepfunctions"] = stepfunctions
        if storagegateway is not None:
            self._values["storagegateway"] = storagegateway
        if sts is not None:
            self._values["sts"] = sts
        if support is not None:
            self._values["support"] = support
        if swf is not None:
            self._values["swf"] = swf
        if synthetics is not None:
            self._values["synthetics"] = synthetics
        if textract is not None:
            self._values["textract"] = textract
        if timestreamquery is not None:
            self._values["timestreamquery"] = timestreamquery
        if timestreamwrite is not None:
            self._values["timestreamwrite"] = timestreamwrite
        if transcribe is not None:
            self._values["transcribe"] = transcribe
        if transcribeservice is not None:
            self._values["transcribeservice"] = transcribeservice
        if transcribestreaming is not None:
            self._values["transcribestreaming"] = transcribestreaming
        if transcribestreamingservice is not None:
            self._values["transcribestreamingservice"] = transcribestreamingservice
        if transfer is not None:
            self._values["transfer"] = transfer
        if translate is not None:
            self._values["translate"] = translate
        if voiceid is not None:
            self._values["voiceid"] = voiceid
        if waf is not None:
            self._values["waf"] = waf
        if wafregional is not None:
            self._values["wafregional"] = wafregional
        if wafv2 is not None:
            self._values["wafv2"] = wafv2
        if wellarchitected is not None:
            self._values["wellarchitected"] = wellarchitected
        if wisdom is not None:
            self._values["wisdom"] = wisdom
        if workdocs is not None:
            self._values["workdocs"] = workdocs
        if worklink is not None:
            self._values["worklink"] = worklink
        if workmail is not None:
            self._values["workmail"] = workmail
        if workmailmessageflow is not None:
            self._values["workmailmessageflow"] = workmailmessageflow
        if workspaces is not None:
            self._values["workspaces"] = workspaces
        if workspacesweb is not None:
            self._values["workspacesweb"] = workspacesweb
        if xray is not None:
            self._values["xray"] = xray

    @builtins.property
    def accessanalyzer(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#accessanalyzer AwsProvider#accessanalyzer}
        '''
        result = self._values.get("accessanalyzer")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def account(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#account AwsProvider#account}
        '''
        result = self._values.get("account")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def acm(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#acm AwsProvider#acm}
        '''
        result = self._values.get("acm")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def acmpca(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#acmpca AwsProvider#acmpca}
        '''
        result = self._values.get("acmpca")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def alexaforbusiness(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#alexaforbusiness AwsProvider#alexaforbusiness}
        '''
        result = self._values.get("alexaforbusiness")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def amg(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#amg AwsProvider#amg}
        '''
        result = self._values.get("amg")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def amp(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#amp AwsProvider#amp}
        '''
        result = self._values.get("amp")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def amplify(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#amplify AwsProvider#amplify}
        '''
        result = self._values.get("amplify")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def amplifybackend(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#amplifybackend AwsProvider#amplifybackend}
        '''
        result = self._values.get("amplifybackend")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def amplifyuibuilder(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#amplifyuibuilder AwsProvider#amplifyuibuilder}
        '''
        result = self._values.get("amplifyuibuilder")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def apigateway(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#apigateway AwsProvider#apigateway}
        '''
        result = self._values.get("apigateway")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def apigatewaymanagementapi(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#apigatewaymanagementapi AwsProvider#apigatewaymanagementapi}
        '''
        result = self._values.get("apigatewaymanagementapi")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def apigatewayv2(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#apigatewayv2 AwsProvider#apigatewayv2}
        '''
        result = self._values.get("apigatewayv2")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def appautoscaling(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#appautoscaling AwsProvider#appautoscaling}
        '''
        result = self._values.get("appautoscaling")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def appconfig(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#appconfig AwsProvider#appconfig}
        '''
        result = self._values.get("appconfig")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def appconfigdata(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#appconfigdata AwsProvider#appconfigdata}
        '''
        result = self._values.get("appconfigdata")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def appflow(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#appflow AwsProvider#appflow}
        '''
        result = self._values.get("appflow")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def appintegrations(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#appintegrations AwsProvider#appintegrations}
        '''
        result = self._values.get("appintegrations")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def appintegrationsservice(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#appintegrationsservice AwsProvider#appintegrationsservice}
        '''
        result = self._values.get("appintegrationsservice")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def applicationautoscaling(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#applicationautoscaling AwsProvider#applicationautoscaling}
        '''
        result = self._values.get("applicationautoscaling")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def applicationcostprofiler(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#applicationcostprofiler AwsProvider#applicationcostprofiler}
        '''
        result = self._values.get("applicationcostprofiler")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def applicationdiscovery(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#applicationdiscovery AwsProvider#applicationdiscovery}
        '''
        result = self._values.get("applicationdiscovery")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def applicationdiscoveryservice(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#applicationdiscoveryservice AwsProvider#applicationdiscoveryservice}
        '''
        result = self._values.get("applicationdiscoveryservice")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def applicationinsights(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#applicationinsights AwsProvider#applicationinsights}
        '''
        result = self._values.get("applicationinsights")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def appmesh(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#appmesh AwsProvider#appmesh}
        '''
        result = self._values.get("appmesh")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def appregistry(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#appregistry AwsProvider#appregistry}
        '''
        result = self._values.get("appregistry")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def apprunner(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#apprunner AwsProvider#apprunner}
        '''
        result = self._values.get("apprunner")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def appstream(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#appstream AwsProvider#appstream}
        '''
        result = self._values.get("appstream")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def appsync(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#appsync AwsProvider#appsync}
        '''
        result = self._values.get("appsync")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def athena(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#athena AwsProvider#athena}
        '''
        result = self._values.get("athena")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def auditmanager(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#auditmanager AwsProvider#auditmanager}
        '''
        result = self._values.get("auditmanager")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def augmentedairuntime(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#augmentedairuntime AwsProvider#augmentedairuntime}
        '''
        result = self._values.get("augmentedairuntime")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def autoscaling(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#autoscaling AwsProvider#autoscaling}
        '''
        result = self._values.get("autoscaling")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def autoscalingplans(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#autoscalingplans AwsProvider#autoscalingplans}
        '''
        result = self._values.get("autoscalingplans")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def backup(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#backup AwsProvider#backup}
        '''
        result = self._values.get("backup")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def backupgateway(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#backupgateway AwsProvider#backupgateway}
        '''
        result = self._values.get("backupgateway")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def batch(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#batch AwsProvider#batch}
        '''
        result = self._values.get("batch")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def beanstalk(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#beanstalk AwsProvider#beanstalk}
        '''
        result = self._values.get("beanstalk")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def billingconductor(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#billingconductor AwsProvider#billingconductor}
        '''
        result = self._values.get("billingconductor")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def braket(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#braket AwsProvider#braket}
        '''
        result = self._values.get("braket")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def budgets(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#budgets AwsProvider#budgets}
        '''
        result = self._values.get("budgets")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ce(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#ce AwsProvider#ce}
        '''
        result = self._values.get("ce")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def chime(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#chime AwsProvider#chime}
        '''
        result = self._values.get("chime")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def chimesdkidentity(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#chimesdkidentity AwsProvider#chimesdkidentity}
        '''
        result = self._values.get("chimesdkidentity")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def chimesdkmeetings(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#chimesdkmeetings AwsProvider#chimesdkmeetings}
        '''
        result = self._values.get("chimesdkmeetings")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def chimesdkmessaging(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#chimesdkmessaging AwsProvider#chimesdkmessaging}
        '''
        result = self._values.get("chimesdkmessaging")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cloud9(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#cloud9 AwsProvider#cloud9}
        '''
        result = self._values.get("cloud9")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cloudcontrol(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#cloudcontrol AwsProvider#cloudcontrol}
        '''
        result = self._values.get("cloudcontrol")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cloudcontrolapi(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#cloudcontrolapi AwsProvider#cloudcontrolapi}
        '''
        result = self._values.get("cloudcontrolapi")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def clouddirectory(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#clouddirectory AwsProvider#clouddirectory}
        '''
        result = self._values.get("clouddirectory")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cloudformation(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#cloudformation AwsProvider#cloudformation}
        '''
        result = self._values.get("cloudformation")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cloudfront(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#cloudfront AwsProvider#cloudfront}
        '''
        result = self._values.get("cloudfront")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cloudhsm(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#cloudhsm AwsProvider#cloudhsm}
        '''
        result = self._values.get("cloudhsm")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cloudhsmv2(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#cloudhsmv2 AwsProvider#cloudhsmv2}
        '''
        result = self._values.get("cloudhsmv2")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cloudsearch(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#cloudsearch AwsProvider#cloudsearch}
        '''
        result = self._values.get("cloudsearch")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cloudsearchdomain(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#cloudsearchdomain AwsProvider#cloudsearchdomain}
        '''
        result = self._values.get("cloudsearchdomain")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cloudtrail(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#cloudtrail AwsProvider#cloudtrail}
        '''
        result = self._values.get("cloudtrail")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cloudwatch(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#cloudwatch AwsProvider#cloudwatch}
        '''
        result = self._values.get("cloudwatch")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cloudwatchevents(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#cloudwatchevents AwsProvider#cloudwatchevents}
        '''
        result = self._values.get("cloudwatchevents")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cloudwatchevidently(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#cloudwatchevidently AwsProvider#cloudwatchevidently}
        '''
        result = self._values.get("cloudwatchevidently")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cloudwatchlog(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#cloudwatchlog AwsProvider#cloudwatchlog}
        '''
        result = self._values.get("cloudwatchlog")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cloudwatchlogs(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#cloudwatchlogs AwsProvider#cloudwatchlogs}
        '''
        result = self._values.get("cloudwatchlogs")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cloudwatchrum(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#cloudwatchrum AwsProvider#cloudwatchrum}
        '''
        result = self._values.get("cloudwatchrum")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def codeartifact(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#codeartifact AwsProvider#codeartifact}
        '''
        result = self._values.get("codeartifact")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def codebuild(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#codebuild AwsProvider#codebuild}
        '''
        result = self._values.get("codebuild")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def codecommit(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#codecommit AwsProvider#codecommit}
        '''
        result = self._values.get("codecommit")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def codedeploy(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#codedeploy AwsProvider#codedeploy}
        '''
        result = self._values.get("codedeploy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def codeguruprofiler(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#codeguruprofiler AwsProvider#codeguruprofiler}
        '''
        result = self._values.get("codeguruprofiler")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def codegurureviewer(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#codegurureviewer AwsProvider#codegurureviewer}
        '''
        result = self._values.get("codegurureviewer")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def codepipeline(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#codepipeline AwsProvider#codepipeline}
        '''
        result = self._values.get("codepipeline")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def codestar(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#codestar AwsProvider#codestar}
        '''
        result = self._values.get("codestar")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def codestarconnections(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#codestarconnections AwsProvider#codestarconnections}
        '''
        result = self._values.get("codestarconnections")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def codestarnotifications(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#codestarnotifications AwsProvider#codestarnotifications}
        '''
        result = self._values.get("codestarnotifications")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cognitoidentity(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#cognitoidentity AwsProvider#cognitoidentity}
        '''
        result = self._values.get("cognitoidentity")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cognitoidentityprovider(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#cognitoidentityprovider AwsProvider#cognitoidentityprovider}
        '''
        result = self._values.get("cognitoidentityprovider")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cognitoidp(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#cognitoidp AwsProvider#cognitoidp}
        '''
        result = self._values.get("cognitoidp")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cognitosync(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#cognitosync AwsProvider#cognitosync}
        '''
        result = self._values.get("cognitosync")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def comprehend(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#comprehend AwsProvider#comprehend}
        '''
        result = self._values.get("comprehend")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def comprehendmedical(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#comprehendmedical AwsProvider#comprehendmedical}
        '''
        result = self._values.get("comprehendmedical")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def computeoptimizer(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#computeoptimizer AwsProvider#computeoptimizer}
        '''
        result = self._values.get("computeoptimizer")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def config(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#config AwsProvider#config}
        '''
        result = self._values.get("config")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def configservice(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#configservice AwsProvider#configservice}
        '''
        result = self._values.get("configservice")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def connect(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#connect AwsProvider#connect}
        '''
        result = self._values.get("connect")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def connectcontactlens(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#connectcontactlens AwsProvider#connectcontactlens}
        '''
        result = self._values.get("connectcontactlens")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def connectparticipant(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#connectparticipant AwsProvider#connectparticipant}
        '''
        result = self._values.get("connectparticipant")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def connectwisdomservice(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#connectwisdomservice AwsProvider#connectwisdomservice}
        '''
        result = self._values.get("connectwisdomservice")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def controltower(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#controltower AwsProvider#controltower}
        '''
        result = self._values.get("controltower")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def costandusagereportservice(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#costandusagereportservice AwsProvider#costandusagereportservice}
        '''
        result = self._values.get("costandusagereportservice")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def costexplorer(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#costexplorer AwsProvider#costexplorer}
        '''
        result = self._values.get("costexplorer")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cur(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#cur AwsProvider#cur}
        '''
        result = self._values.get("cur")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def customerprofiles(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#customerprofiles AwsProvider#customerprofiles}
        '''
        result = self._values.get("customerprofiles")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def databasemigration(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#databasemigration AwsProvider#databasemigration}
        '''
        result = self._values.get("databasemigration")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def databasemigrationservice(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#databasemigrationservice AwsProvider#databasemigrationservice}
        '''
        result = self._values.get("databasemigrationservice")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def databrew(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#databrew AwsProvider#databrew}
        '''
        result = self._values.get("databrew")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dataexchange(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#dataexchange AwsProvider#dataexchange}
        '''
        result = self._values.get("dataexchange")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def datapipeline(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#datapipeline AwsProvider#datapipeline}
        '''
        result = self._values.get("datapipeline")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def datasync(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#datasync AwsProvider#datasync}
        '''
        result = self._values.get("datasync")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dax(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#dax AwsProvider#dax}
        '''
        result = self._values.get("dax")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def deploy(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#deploy AwsProvider#deploy}
        '''
        result = self._values.get("deploy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def detective(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#detective AwsProvider#detective}
        '''
        result = self._values.get("detective")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def devicefarm(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#devicefarm AwsProvider#devicefarm}
        '''
        result = self._values.get("devicefarm")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def devopsguru(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#devopsguru AwsProvider#devopsguru}
        '''
        result = self._values.get("devopsguru")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def directconnect(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#directconnect AwsProvider#directconnect}
        '''
        result = self._values.get("directconnect")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def directoryservice(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#directoryservice AwsProvider#directoryservice}
        '''
        result = self._values.get("directoryservice")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def discovery(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#discovery AwsProvider#discovery}
        '''
        result = self._values.get("discovery")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dlm(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#dlm AwsProvider#dlm}
        '''
        result = self._values.get("dlm")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dms(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#dms AwsProvider#dms}
        '''
        result = self._values.get("dms")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def docdb(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#docdb AwsProvider#docdb}
        '''
        result = self._values.get("docdb")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def drs(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#drs AwsProvider#drs}
        '''
        result = self._values.get("drs")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ds(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#ds AwsProvider#ds}
        '''
        result = self._values.get("ds")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dynamodb(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#dynamodb AwsProvider#dynamodb}
        '''
        result = self._values.get("dynamodb")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dynamodbstreams(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#dynamodbstreams AwsProvider#dynamodbstreams}
        '''
        result = self._values.get("dynamodbstreams")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ebs(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#ebs AwsProvider#ebs}
        '''
        result = self._values.get("ebs")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ec2(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#ec2 AwsProvider#ec2}
        '''
        result = self._values.get("ec2")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ec2_instanceconnect(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#ec2instanceconnect AwsProvider#ec2instanceconnect}
        '''
        result = self._values.get("ec2_instanceconnect")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ecr(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#ecr AwsProvider#ecr}
        '''
        result = self._values.get("ecr")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ecrpublic(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#ecrpublic AwsProvider#ecrpublic}
        '''
        result = self._values.get("ecrpublic")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ecs(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#ecs AwsProvider#ecs}
        '''
        result = self._values.get("ecs")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def efs(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#efs AwsProvider#efs}
        '''
        result = self._values.get("efs")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def eks(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#eks AwsProvider#eks}
        '''
        result = self._values.get("eks")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def elasticache(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#elasticache AwsProvider#elasticache}
        '''
        result = self._values.get("elasticache")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def elasticbeanstalk(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#elasticbeanstalk AwsProvider#elasticbeanstalk}
        '''
        result = self._values.get("elasticbeanstalk")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def elasticinference(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#elasticinference AwsProvider#elasticinference}
        '''
        result = self._values.get("elasticinference")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def elasticloadbalancing(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#elasticloadbalancing AwsProvider#elasticloadbalancing}
        '''
        result = self._values.get("elasticloadbalancing")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def elasticloadbalancingv2(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#elasticloadbalancingv2 AwsProvider#elasticloadbalancingv2}
        '''
        result = self._values.get("elasticloadbalancingv2")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def elasticsearch(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#elasticsearch AwsProvider#elasticsearch}
        '''
        result = self._values.get("elasticsearch")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def elasticsearchservice(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#elasticsearchservice AwsProvider#elasticsearchservice}
        '''
        result = self._values.get("elasticsearchservice")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def elastictranscoder(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#elastictranscoder AwsProvider#elastictranscoder}
        '''
        result = self._values.get("elastictranscoder")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def elb(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#elb AwsProvider#elb}
        '''
        result = self._values.get("elb")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def elbv2(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#elbv2 AwsProvider#elbv2}
        '''
        result = self._values.get("elbv2")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def emr(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#emr AwsProvider#emr}
        '''
        result = self._values.get("emr")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def emrcontainers(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#emrcontainers AwsProvider#emrcontainers}
        '''
        result = self._values.get("emrcontainers")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def emrserverless(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#emrserverless AwsProvider#emrserverless}
        '''
        result = self._values.get("emrserverless")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def es(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#es AwsProvider#es}
        '''
        result = self._values.get("es")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def eventbridge(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#eventbridge AwsProvider#eventbridge}
        '''
        result = self._values.get("eventbridge")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def events(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#events AwsProvider#events}
        '''
        result = self._values.get("events")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def evidently(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#evidently AwsProvider#evidently}
        '''
        result = self._values.get("evidently")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def finspace(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#finspace AwsProvider#finspace}
        '''
        result = self._values.get("finspace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def finspacedata(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#finspacedata AwsProvider#finspacedata}
        '''
        result = self._values.get("finspacedata")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def firehose(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#firehose AwsProvider#firehose}
        '''
        result = self._values.get("firehose")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def fis(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#fis AwsProvider#fis}
        '''
        result = self._values.get("fis")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def fms(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#fms AwsProvider#fms}
        '''
        result = self._values.get("fms")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def forecast(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#forecast AwsProvider#forecast}
        '''
        result = self._values.get("forecast")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def forecastquery(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#forecastquery AwsProvider#forecastquery}
        '''
        result = self._values.get("forecastquery")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def forecastqueryservice(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#forecastqueryservice AwsProvider#forecastqueryservice}
        '''
        result = self._values.get("forecastqueryservice")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def forecastservice(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#forecastservice AwsProvider#forecastservice}
        '''
        result = self._values.get("forecastservice")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def frauddetector(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#frauddetector AwsProvider#frauddetector}
        '''
        result = self._values.get("frauddetector")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def fsx(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#fsx AwsProvider#fsx}
        '''
        result = self._values.get("fsx")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def gamelift(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#gamelift AwsProvider#gamelift}
        '''
        result = self._values.get("gamelift")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def glacier(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#glacier AwsProvider#glacier}
        '''
        result = self._values.get("glacier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def globalaccelerator(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#globalaccelerator AwsProvider#globalaccelerator}
        '''
        result = self._values.get("globalaccelerator")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def glue(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#glue AwsProvider#glue}
        '''
        result = self._values.get("glue")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def gluedatabrew(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#gluedatabrew AwsProvider#gluedatabrew}
        '''
        result = self._values.get("gluedatabrew")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def grafana(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#grafana AwsProvider#grafana}
        '''
        result = self._values.get("grafana")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def greengrass(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#greengrass AwsProvider#greengrass}
        '''
        result = self._values.get("greengrass")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def greengrassv2(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#greengrassv2 AwsProvider#greengrassv2}
        '''
        result = self._values.get("greengrassv2")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def groundstation(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#groundstation AwsProvider#groundstation}
        '''
        result = self._values.get("groundstation")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def guardduty(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#guardduty AwsProvider#guardduty}
        '''
        result = self._values.get("guardduty")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def health(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#health AwsProvider#health}
        '''
        result = self._values.get("health")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def healthlake(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#healthlake AwsProvider#healthlake}
        '''
        result = self._values.get("healthlake")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def honeycode(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#honeycode AwsProvider#honeycode}
        '''
        result = self._values.get("honeycode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def iam(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#iam AwsProvider#iam}
        '''
        result = self._values.get("iam")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def identitystore(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#identitystore AwsProvider#identitystore}
        '''
        result = self._values.get("identitystore")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def imagebuilder(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#imagebuilder AwsProvider#imagebuilder}
        '''
        result = self._values.get("imagebuilder")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def inspector(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#inspector AwsProvider#inspector}
        '''
        result = self._values.get("inspector")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def inspector2(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#inspector2 AwsProvider#inspector2}
        '''
        result = self._values.get("inspector2")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def inspectorv2(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#inspectorv2 AwsProvider#inspectorv2}
        '''
        result = self._values.get("inspectorv2")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def iot(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#iot AwsProvider#iot}
        '''
        result = self._values.get("iot")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def iot1_clickdevices(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#iot1clickdevices AwsProvider#iot1clickdevices}
        '''
        result = self._values.get("iot1_clickdevices")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def iot1_clickdevicesservice(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#iot1clickdevicesservice AwsProvider#iot1clickdevicesservice}
        '''
        result = self._values.get("iot1_clickdevicesservice")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def iot1_clickprojects(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#iot1clickprojects AwsProvider#iot1clickprojects}
        '''
        result = self._values.get("iot1_clickprojects")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def iotanalytics(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#iotanalytics AwsProvider#iotanalytics}
        '''
        result = self._values.get("iotanalytics")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def iotdata(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#iotdata AwsProvider#iotdata}
        '''
        result = self._values.get("iotdata")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def iotdataplane(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#iotdataplane AwsProvider#iotdataplane}
        '''
        result = self._values.get("iotdataplane")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def iotdeviceadvisor(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#iotdeviceadvisor AwsProvider#iotdeviceadvisor}
        '''
        result = self._values.get("iotdeviceadvisor")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def iotevents(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#iotevents AwsProvider#iotevents}
        '''
        result = self._values.get("iotevents")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ioteventsdata(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#ioteventsdata AwsProvider#ioteventsdata}
        '''
        result = self._values.get("ioteventsdata")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def iotfleethub(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#iotfleethub AwsProvider#iotfleethub}
        '''
        result = self._values.get("iotfleethub")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def iotjobsdata(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#iotjobsdata AwsProvider#iotjobsdata}
        '''
        result = self._values.get("iotjobsdata")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def iotjobsdataplane(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#iotjobsdataplane AwsProvider#iotjobsdataplane}
        '''
        result = self._values.get("iotjobsdataplane")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def iotsecuretunneling(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#iotsecuretunneling AwsProvider#iotsecuretunneling}
        '''
        result = self._values.get("iotsecuretunneling")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def iotsitewise(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#iotsitewise AwsProvider#iotsitewise}
        '''
        result = self._values.get("iotsitewise")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def iotthingsgraph(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#iotthingsgraph AwsProvider#iotthingsgraph}
        '''
        result = self._values.get("iotthingsgraph")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def iottwinmaker(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#iottwinmaker AwsProvider#iottwinmaker}
        '''
        result = self._values.get("iottwinmaker")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def iotwireless(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#iotwireless AwsProvider#iotwireless}
        '''
        result = self._values.get("iotwireless")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ivs(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#ivs AwsProvider#ivs}
        '''
        result = self._values.get("ivs")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ivschat(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#ivschat AwsProvider#ivschat}
        '''
        result = self._values.get("ivschat")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kafka(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#kafka AwsProvider#kafka}
        '''
        result = self._values.get("kafka")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kafkaconnect(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#kafkaconnect AwsProvider#kafkaconnect}
        '''
        result = self._values.get("kafkaconnect")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kendra(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#kendra AwsProvider#kendra}
        '''
        result = self._values.get("kendra")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def keyspaces(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#keyspaces AwsProvider#keyspaces}
        '''
        result = self._values.get("keyspaces")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kinesis(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#kinesis AwsProvider#kinesis}
        '''
        result = self._values.get("kinesis")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kinesisanalytics(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#kinesisanalytics AwsProvider#kinesisanalytics}
        '''
        result = self._values.get("kinesisanalytics")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kinesisanalyticsv2(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#kinesisanalyticsv2 AwsProvider#kinesisanalyticsv2}
        '''
        result = self._values.get("kinesisanalyticsv2")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kinesisvideo(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#kinesisvideo AwsProvider#kinesisvideo}
        '''
        result = self._values.get("kinesisvideo")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kinesisvideoarchivedmedia(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#kinesisvideoarchivedmedia AwsProvider#kinesisvideoarchivedmedia}
        '''
        result = self._values.get("kinesisvideoarchivedmedia")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kinesisvideomedia(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#kinesisvideomedia AwsProvider#kinesisvideomedia}
        '''
        result = self._values.get("kinesisvideomedia")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kinesisvideosignaling(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#kinesisvideosignaling AwsProvider#kinesisvideosignaling}
        '''
        result = self._values.get("kinesisvideosignaling")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kinesisvideosignalingchannels(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#kinesisvideosignalingchannels AwsProvider#kinesisvideosignalingchannels}
        '''
        result = self._values.get("kinesisvideosignalingchannels")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#kms AwsProvider#kms}
        '''
        result = self._values.get("kms")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lakeformation(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#lakeformation AwsProvider#lakeformation}
        '''
        result = self._values.get("lakeformation")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lambda_(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#lambda AwsProvider#lambda}
        '''
        result = self._values.get("lambda_")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lex(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#lex AwsProvider#lex}
        '''
        result = self._values.get("lex")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lexmodelbuilding(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#lexmodelbuilding AwsProvider#lexmodelbuilding}
        '''
        result = self._values.get("lexmodelbuilding")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lexmodelbuildingservice(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#lexmodelbuildingservice AwsProvider#lexmodelbuildingservice}
        '''
        result = self._values.get("lexmodelbuildingservice")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lexmodels(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#lexmodels AwsProvider#lexmodels}
        '''
        result = self._values.get("lexmodels")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lexmodelsv2(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#lexmodelsv2 AwsProvider#lexmodelsv2}
        '''
        result = self._values.get("lexmodelsv2")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lexruntime(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#lexruntime AwsProvider#lexruntime}
        '''
        result = self._values.get("lexruntime")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lexruntimeservice(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#lexruntimeservice AwsProvider#lexruntimeservice}
        '''
        result = self._values.get("lexruntimeservice")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lexruntimev2(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#lexruntimev2 AwsProvider#lexruntimev2}
        '''
        result = self._values.get("lexruntimev2")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lexv2_models(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#lexv2models AwsProvider#lexv2models}
        '''
        result = self._values.get("lexv2_models")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lexv2_runtime(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#lexv2runtime AwsProvider#lexv2runtime}
        '''
        result = self._values.get("lexv2_runtime")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def licensemanager(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#licensemanager AwsProvider#licensemanager}
        '''
        result = self._values.get("licensemanager")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lightsail(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#lightsail AwsProvider#lightsail}
        '''
        result = self._values.get("lightsail")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def location(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#location AwsProvider#location}
        '''
        result = self._values.get("location")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def locationservice(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#locationservice AwsProvider#locationservice}
        '''
        result = self._values.get("locationservice")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def logs(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#logs AwsProvider#logs}
        '''
        result = self._values.get("logs")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lookoutequipment(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#lookoutequipment AwsProvider#lookoutequipment}
        '''
        result = self._values.get("lookoutequipment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lookoutforvision(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#lookoutforvision AwsProvider#lookoutforvision}
        '''
        result = self._values.get("lookoutforvision")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lookoutmetrics(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#lookoutmetrics AwsProvider#lookoutmetrics}
        '''
        result = self._values.get("lookoutmetrics")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lookoutvision(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#lookoutvision AwsProvider#lookoutvision}
        '''
        result = self._values.get("lookoutvision")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def machinelearning(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#machinelearning AwsProvider#machinelearning}
        '''
        result = self._values.get("machinelearning")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def macie(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#macie AwsProvider#macie}
        '''
        result = self._values.get("macie")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def macie2(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#macie2 AwsProvider#macie2}
        '''
        result = self._values.get("macie2")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def managedblockchain(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#managedblockchain AwsProvider#managedblockchain}
        '''
        result = self._values.get("managedblockchain")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def managedgrafana(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#managedgrafana AwsProvider#managedgrafana}
        '''
        result = self._values.get("managedgrafana")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def marketplacecatalog(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#marketplacecatalog AwsProvider#marketplacecatalog}
        '''
        result = self._values.get("marketplacecatalog")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def marketplacecommerceanalytics(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#marketplacecommerceanalytics AwsProvider#marketplacecommerceanalytics}
        '''
        result = self._values.get("marketplacecommerceanalytics")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def marketplaceentitlement(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#marketplaceentitlement AwsProvider#marketplaceentitlement}
        '''
        result = self._values.get("marketplaceentitlement")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def marketplaceentitlementservice(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#marketplaceentitlementservice AwsProvider#marketplaceentitlementservice}
        '''
        result = self._values.get("marketplaceentitlementservice")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def marketplacemetering(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#marketplacemetering AwsProvider#marketplacemetering}
        '''
        result = self._values.get("marketplacemetering")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mediaconnect(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#mediaconnect AwsProvider#mediaconnect}
        '''
        result = self._values.get("mediaconnect")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mediaconvert(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#mediaconvert AwsProvider#mediaconvert}
        '''
        result = self._values.get("mediaconvert")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def medialive(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#medialive AwsProvider#medialive}
        '''
        result = self._values.get("medialive")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mediapackage(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#mediapackage AwsProvider#mediapackage}
        '''
        result = self._values.get("mediapackage")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mediapackagevod(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#mediapackagevod AwsProvider#mediapackagevod}
        '''
        result = self._values.get("mediapackagevod")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mediastore(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#mediastore AwsProvider#mediastore}
        '''
        result = self._values.get("mediastore")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mediastoredata(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#mediastoredata AwsProvider#mediastoredata}
        '''
        result = self._values.get("mediastoredata")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mediatailor(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#mediatailor AwsProvider#mediatailor}
        '''
        result = self._values.get("mediatailor")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def memorydb(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#memorydb AwsProvider#memorydb}
        '''
        result = self._values.get("memorydb")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def meteringmarketplace(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#meteringmarketplace AwsProvider#meteringmarketplace}
        '''
        result = self._values.get("meteringmarketplace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mgh(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#mgh AwsProvider#mgh}
        '''
        result = self._values.get("mgh")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mgn(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#mgn AwsProvider#mgn}
        '''
        result = self._values.get("mgn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def migrationhub(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#migrationhub AwsProvider#migrationhub}
        '''
        result = self._values.get("migrationhub")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def migrationhubconfig(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#migrationhubconfig AwsProvider#migrationhubconfig}
        '''
        result = self._values.get("migrationhubconfig")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def migrationhubrefactorspaces(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#migrationhubrefactorspaces AwsProvider#migrationhubrefactorspaces}
        '''
        result = self._values.get("migrationhubrefactorspaces")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def migrationhubstrategy(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#migrationhubstrategy AwsProvider#migrationhubstrategy}
        '''
        result = self._values.get("migrationhubstrategy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def migrationhubstrategyrecommendations(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#migrationhubstrategyrecommendations AwsProvider#migrationhubstrategyrecommendations}
        '''
        result = self._values.get("migrationhubstrategyrecommendations")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mobile(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#mobile AwsProvider#mobile}
        '''
        result = self._values.get("mobile")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mq(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#mq AwsProvider#mq}
        '''
        result = self._values.get("mq")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def msk(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#msk AwsProvider#msk}
        '''
        result = self._values.get("msk")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mturk(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#mturk AwsProvider#mturk}
        '''
        result = self._values.get("mturk")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mwaa(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#mwaa AwsProvider#mwaa}
        '''
        result = self._values.get("mwaa")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def neptune(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#neptune AwsProvider#neptune}
        '''
        result = self._values.get("neptune")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def networkfirewall(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#networkfirewall AwsProvider#networkfirewall}
        '''
        result = self._values.get("networkfirewall")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def networkmanager(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#networkmanager AwsProvider#networkmanager}
        '''
        result = self._values.get("networkmanager")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def nimble(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#nimble AwsProvider#nimble}
        '''
        result = self._values.get("nimble")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def nimblestudio(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#nimblestudio AwsProvider#nimblestudio}
        '''
        result = self._values.get("nimblestudio")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def opensearch(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#opensearch AwsProvider#opensearch}
        '''
        result = self._values.get("opensearch")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def opensearchserverless(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#opensearchserverless AwsProvider#opensearchserverless}
        '''
        result = self._values.get("opensearchserverless")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def opensearchservice(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#opensearchservice AwsProvider#opensearchservice}
        '''
        result = self._values.get("opensearchservice")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def opsworks(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#opsworks AwsProvider#opsworks}
        '''
        result = self._values.get("opsworks")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def opsworkscm(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#opsworkscm AwsProvider#opsworkscm}
        '''
        result = self._values.get("opsworkscm")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def organizations(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#organizations AwsProvider#organizations}
        '''
        result = self._values.get("organizations")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def outposts(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#outposts AwsProvider#outposts}
        '''
        result = self._values.get("outposts")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def panorama(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#panorama AwsProvider#panorama}
        '''
        result = self._values.get("panorama")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def personalize(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#personalize AwsProvider#personalize}
        '''
        result = self._values.get("personalize")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def personalizeevents(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#personalizeevents AwsProvider#personalizeevents}
        '''
        result = self._values.get("personalizeevents")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def personalizeruntime(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#personalizeruntime AwsProvider#personalizeruntime}
        '''
        result = self._values.get("personalizeruntime")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pi(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#pi AwsProvider#pi}
        '''
        result = self._values.get("pi")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pinpoint(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#pinpoint AwsProvider#pinpoint}
        '''
        result = self._values.get("pinpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pinpointemail(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#pinpointemail AwsProvider#pinpointemail}
        '''
        result = self._values.get("pinpointemail")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pinpointsmsvoice(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#pinpointsmsvoice AwsProvider#pinpointsmsvoice}
        '''
        result = self._values.get("pinpointsmsvoice")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pipes(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#pipes AwsProvider#pipes}
        '''
        result = self._values.get("pipes")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def polly(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#polly AwsProvider#polly}
        '''
        result = self._values.get("polly")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pricing(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#pricing AwsProvider#pricing}
        '''
        result = self._values.get("pricing")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def prometheus(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#prometheus AwsProvider#prometheus}
        '''
        result = self._values.get("prometheus")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def prometheusservice(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#prometheusservice AwsProvider#prometheusservice}
        '''
        result = self._values.get("prometheusservice")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def proton(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#proton AwsProvider#proton}
        '''
        result = self._values.get("proton")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def qldb(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#qldb AwsProvider#qldb}
        '''
        result = self._values.get("qldb")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def qldbsession(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#qldbsession AwsProvider#qldbsession}
        '''
        result = self._values.get("qldbsession")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def quicksight(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#quicksight AwsProvider#quicksight}
        '''
        result = self._values.get("quicksight")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ram(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#ram AwsProvider#ram}
        '''
        result = self._values.get("ram")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rbin(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#rbin AwsProvider#rbin}
        '''
        result = self._values.get("rbin")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rds(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#rds AwsProvider#rds}
        '''
        result = self._values.get("rds")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rdsdata(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#rdsdata AwsProvider#rdsdata}
        '''
        result = self._values.get("rdsdata")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rdsdataservice(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#rdsdataservice AwsProvider#rdsdataservice}
        '''
        result = self._values.get("rdsdataservice")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def recyclebin(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#recyclebin AwsProvider#recyclebin}
        '''
        result = self._values.get("recyclebin")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def redshift(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#redshift AwsProvider#redshift}
        '''
        result = self._values.get("redshift")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def redshiftdata(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#redshiftdata AwsProvider#redshiftdata}
        '''
        result = self._values.get("redshiftdata")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def redshiftdataapiservice(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#redshiftdataapiservice AwsProvider#redshiftdataapiservice}
        '''
        result = self._values.get("redshiftdataapiservice")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def redshiftserverless(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#redshiftserverless AwsProvider#redshiftserverless}
        '''
        result = self._values.get("redshiftserverless")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rekognition(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#rekognition AwsProvider#rekognition}
        '''
        result = self._values.get("rekognition")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resiliencehub(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#resiliencehub AwsProvider#resiliencehub}
        '''
        result = self._values.get("resiliencehub")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resourceexplorer2(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#resourceexplorer2 AwsProvider#resourceexplorer2}
        '''
        result = self._values.get("resourceexplorer2")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resourcegroups(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#resourcegroups AwsProvider#resourcegroups}
        '''
        result = self._values.get("resourcegroups")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resourcegroupstagging(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#resourcegroupstagging AwsProvider#resourcegroupstagging}
        '''
        result = self._values.get("resourcegroupstagging")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resourcegroupstaggingapi(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#resourcegroupstaggingapi AwsProvider#resourcegroupstaggingapi}
        '''
        result = self._values.get("resourcegroupstaggingapi")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def robomaker(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#robomaker AwsProvider#robomaker}
        '''
        result = self._values.get("robomaker")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rolesanywhere(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#rolesanywhere AwsProvider#rolesanywhere}
        '''
        result = self._values.get("rolesanywhere")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def route53(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#route53 AwsProvider#route53}
        '''
        result = self._values.get("route53")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def route53_domains(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#route53domains AwsProvider#route53domains}
        '''
        result = self._values.get("route53_domains")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def route53_recoverycluster(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#route53recoverycluster AwsProvider#route53recoverycluster}
        '''
        result = self._values.get("route53_recoverycluster")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def route53_recoverycontrolconfig(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#route53recoverycontrolconfig AwsProvider#route53recoverycontrolconfig}
        '''
        result = self._values.get("route53_recoverycontrolconfig")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def route53_recoveryreadiness(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#route53recoveryreadiness AwsProvider#route53recoveryreadiness}
        '''
        result = self._values.get("route53_recoveryreadiness")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def route53_resolver(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#route53resolver AwsProvider#route53resolver}
        '''
        result = self._values.get("route53_resolver")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rum(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#rum AwsProvider#rum}
        '''
        result = self._values.get("rum")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def s3(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#s3 AwsProvider#s3}
        '''
        result = self._values.get("s3")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def s3_api(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#s3api AwsProvider#s3api}
        '''
        result = self._values.get("s3_api")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def s3_control(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#s3control AwsProvider#s3control}
        '''
        result = self._values.get("s3_control")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def s3_outposts(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#s3outposts AwsProvider#s3outposts}
        '''
        result = self._values.get("s3_outposts")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sagemaker(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#sagemaker AwsProvider#sagemaker}
        '''
        result = self._values.get("sagemaker")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sagemakera2_iruntime(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#sagemakera2iruntime AwsProvider#sagemakera2iruntime}
        '''
        result = self._values.get("sagemakera2_iruntime")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sagemakeredge(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#sagemakeredge AwsProvider#sagemakeredge}
        '''
        result = self._values.get("sagemakeredge")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sagemakeredgemanager(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#sagemakeredgemanager AwsProvider#sagemakeredgemanager}
        '''
        result = self._values.get("sagemakeredgemanager")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sagemakerfeaturestoreruntime(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#sagemakerfeaturestoreruntime AwsProvider#sagemakerfeaturestoreruntime}
        '''
        result = self._values.get("sagemakerfeaturestoreruntime")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sagemakerruntime(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#sagemakerruntime AwsProvider#sagemakerruntime}
        '''
        result = self._values.get("sagemakerruntime")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def savingsplans(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#savingsplans AwsProvider#savingsplans}
        '''
        result = self._values.get("savingsplans")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scheduler(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#scheduler AwsProvider#scheduler}
        '''
        result = self._values.get("scheduler")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def schemas(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#schemas AwsProvider#schemas}
        '''
        result = self._values.get("schemas")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sdb(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#sdb AwsProvider#sdb}
        '''
        result = self._values.get("sdb")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def secretsmanager(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#secretsmanager AwsProvider#secretsmanager}
        '''
        result = self._values.get("secretsmanager")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def securityhub(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#securityhub AwsProvider#securityhub}
        '''
        result = self._values.get("securityhub")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def serverlessapplicationrepository(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#serverlessapplicationrepository AwsProvider#serverlessapplicationrepository}
        '''
        result = self._values.get("serverlessapplicationrepository")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def serverlessapprepo(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#serverlessapprepo AwsProvider#serverlessapprepo}
        '''
        result = self._values.get("serverlessapprepo")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def serverlessrepo(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#serverlessrepo AwsProvider#serverlessrepo}
        '''
        result = self._values.get("serverlessrepo")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def servicecatalog(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#servicecatalog AwsProvider#servicecatalog}
        '''
        result = self._values.get("servicecatalog")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def servicecatalogappregistry(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#servicecatalogappregistry AwsProvider#servicecatalogappregistry}
        '''
        result = self._values.get("servicecatalogappregistry")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def servicediscovery(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#servicediscovery AwsProvider#servicediscovery}
        '''
        result = self._values.get("servicediscovery")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def servicequotas(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#servicequotas AwsProvider#servicequotas}
        '''
        result = self._values.get("servicequotas")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ses(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#ses AwsProvider#ses}
        '''
        result = self._values.get("ses")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sesv2(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#sesv2 AwsProvider#sesv2}
        '''
        result = self._values.get("sesv2")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sfn(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#sfn AwsProvider#sfn}
        '''
        result = self._values.get("sfn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def shield(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#shield AwsProvider#shield}
        '''
        result = self._values.get("shield")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def signer(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#signer AwsProvider#signer}
        '''
        result = self._values.get("signer")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def simpledb(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#simpledb AwsProvider#simpledb}
        '''
        result = self._values.get("simpledb")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sms(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#sms AwsProvider#sms}
        '''
        result = self._values.get("sms")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def snowball(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#snowball AwsProvider#snowball}
        '''
        result = self._values.get("snowball")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def snowdevicemanagement(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#snowdevicemanagement AwsProvider#snowdevicemanagement}
        '''
        result = self._values.get("snowdevicemanagement")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sns(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#sns AwsProvider#sns}
        '''
        result = self._values.get("sns")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sqs(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#sqs AwsProvider#sqs}
        '''
        result = self._values.get("sqs")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ssm(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#ssm AwsProvider#ssm}
        '''
        result = self._values.get("ssm")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ssmcontacts(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#ssmcontacts AwsProvider#ssmcontacts}
        '''
        result = self._values.get("ssmcontacts")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ssmincidents(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#ssmincidents AwsProvider#ssmincidents}
        '''
        result = self._values.get("ssmincidents")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sso(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#sso AwsProvider#sso}
        '''
        result = self._values.get("sso")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ssoadmin(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#ssoadmin AwsProvider#ssoadmin}
        '''
        result = self._values.get("ssoadmin")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ssooidc(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#ssooidc AwsProvider#ssooidc}
        '''
        result = self._values.get("ssooidc")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def stepfunctions(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#stepfunctions AwsProvider#stepfunctions}
        '''
        result = self._values.get("stepfunctions")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def storagegateway(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#storagegateway AwsProvider#storagegateway}
        '''
        result = self._values.get("storagegateway")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sts(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#sts AwsProvider#sts}
        '''
        result = self._values.get("sts")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def support(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#support AwsProvider#support}
        '''
        result = self._values.get("support")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def swf(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#swf AwsProvider#swf}
        '''
        result = self._values.get("swf")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def synthetics(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#synthetics AwsProvider#synthetics}
        '''
        result = self._values.get("synthetics")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def textract(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#textract AwsProvider#textract}
        '''
        result = self._values.get("textract")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timestreamquery(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#timestreamquery AwsProvider#timestreamquery}
        '''
        result = self._values.get("timestreamquery")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timestreamwrite(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#timestreamwrite AwsProvider#timestreamwrite}
        '''
        result = self._values.get("timestreamwrite")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def transcribe(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#transcribe AwsProvider#transcribe}
        '''
        result = self._values.get("transcribe")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def transcribeservice(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#transcribeservice AwsProvider#transcribeservice}
        '''
        result = self._values.get("transcribeservice")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def transcribestreaming(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#transcribestreaming AwsProvider#transcribestreaming}
        '''
        result = self._values.get("transcribestreaming")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def transcribestreamingservice(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#transcribestreamingservice AwsProvider#transcribestreamingservice}
        '''
        result = self._values.get("transcribestreamingservice")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def transfer(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#transfer AwsProvider#transfer}
        '''
        result = self._values.get("transfer")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def translate(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#translate AwsProvider#translate}
        '''
        result = self._values.get("translate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def voiceid(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#voiceid AwsProvider#voiceid}
        '''
        result = self._values.get("voiceid")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def waf(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#waf AwsProvider#waf}
        '''
        result = self._values.get("waf")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def wafregional(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#wafregional AwsProvider#wafregional}
        '''
        result = self._values.get("wafregional")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def wafv2(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#wafv2 AwsProvider#wafv2}
        '''
        result = self._values.get("wafv2")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def wellarchitected(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#wellarchitected AwsProvider#wellarchitected}
        '''
        result = self._values.get("wellarchitected")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def wisdom(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#wisdom AwsProvider#wisdom}
        '''
        result = self._values.get("wisdom")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def workdocs(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#workdocs AwsProvider#workdocs}
        '''
        result = self._values.get("workdocs")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def worklink(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#worklink AwsProvider#worklink}
        '''
        result = self._values.get("worklink")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def workmail(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#workmail AwsProvider#workmail}
        '''
        result = self._values.get("workmail")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def workmailmessageflow(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#workmailmessageflow AwsProvider#workmailmessageflow}
        '''
        result = self._values.get("workmailmessageflow")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def workspaces(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#workspaces AwsProvider#workspaces}
        '''
        result = self._values.get("workspaces")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def workspacesweb(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#workspacesweb AwsProvider#workspacesweb}
        '''
        result = self._values.get("workspacesweb")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def xray(self) -> typing.Optional[builtins.str]:
        '''Use this to override the default service endpoint URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#xray AwsProvider#xray}
        '''
        result = self._values.get("xray")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AwsProviderEndpoints(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.provider.AwsProviderIgnoreTags",
    jsii_struct_bases=[],
    name_mapping={"key_prefixes": "keyPrefixes", "keys": "keys"},
)
class AwsProviderIgnoreTags:
    def __init__(
        self,
        *,
        key_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
        keys: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key_prefixes: Resource tag key prefixes to ignore across all resources. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#key_prefixes AwsProvider#key_prefixes}
        :param keys: Resource tag keys to ignore across all resources. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#keys AwsProvider#keys}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39ac3b64a995e2099f8d83cb9c4225e6c1f41923f4b962f43b6263c1041e9c65)
            check_type(argname="argument key_prefixes", value=key_prefixes, expected_type=type_hints["key_prefixes"])
            check_type(argname="argument keys", value=keys, expected_type=type_hints["keys"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if key_prefixes is not None:
            self._values["key_prefixes"] = key_prefixes
        if keys is not None:
            self._values["keys"] = keys

    @builtins.property
    def key_prefixes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Resource tag key prefixes to ignore across all resources.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#key_prefixes AwsProvider#key_prefixes}
        '''
        result = self._values.get("key_prefixes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def keys(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Resource tag keys to ignore across all resources.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws#keys AwsProvider#keys}
        '''
        result = self._values.get("keys")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AwsProviderIgnoreTags(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AwsProvider",
    "AwsProviderAssumeRole",
    "AwsProviderAssumeRoleWithWebIdentity",
    "AwsProviderConfig",
    "AwsProviderDefaultTags",
    "AwsProviderEndpoints",
    "AwsProviderIgnoreTags",
]

publication.publish()

def _typecheckingstub__79d01e4a5ad4d4e2c4e7b0c6770bb00e0d2c0f2c9c2cad8981a6306d1abaf694(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    access_key: typing.Optional[builtins.str] = None,
    alias: typing.Optional[builtins.str] = None,
    allowed_account_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    assume_role: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AwsProviderAssumeRole, typing.Dict[builtins.str, typing.Any]]]]] = None,
    assume_role_with_web_identity: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AwsProviderAssumeRoleWithWebIdentity, typing.Dict[builtins.str, typing.Any]]]]] = None,
    custom_ca_bundle: typing.Optional[builtins.str] = None,
    default_tags: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AwsProviderDefaultTags, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ec2_metadata_service_endpoint: typing.Optional[builtins.str] = None,
    ec2_metadata_service_endpoint_mode: typing.Optional[builtins.str] = None,
    endpoints: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AwsProviderEndpoints, typing.Dict[builtins.str, typing.Any]]]]] = None,
    forbidden_account_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    http_proxy: typing.Optional[builtins.str] = None,
    ignore_tags: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AwsProviderIgnoreTags, typing.Dict[builtins.str, typing.Any]]]]] = None,
    insecure: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    max_retries: typing.Optional[jsii.Number] = None,
    profile: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
    s3_force_path_style: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    s3_use_path_style: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    secret_key: typing.Optional[builtins.str] = None,
    shared_config_files: typing.Optional[typing.Sequence[builtins.str]] = None,
    shared_credentials_file: typing.Optional[builtins.str] = None,
    shared_credentials_files: typing.Optional[typing.Sequence[builtins.str]] = None,
    skip_credentials_validation: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    skip_get_ec2_platforms: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    skip_metadata_api_check: typing.Optional[builtins.str] = None,
    skip_region_validation: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    skip_requesting_account_id: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    sts_region: typing.Optional[builtins.str] = None,
    token: typing.Optional[builtins.str] = None,
    use_dualstack_endpoint: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    use_fips_endpoint: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e6ddf7f277405d5d266ac279eeed43945038c221d186aaec2083aa727a2fd74(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__329c9ab4a6f5b6ec76799f3bdbaf3618175a02d88991f7201181538cf4d107e6(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e497afb24aeb860f0f55400131fc0586f41cf5b4babe13a0b66813f3ca58ff56(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7fac3aced6a489bc62137ca23b7e9558383a6f46e78ea2c04edb9e34f0c56200(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AwsProviderAssumeRole]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f044c1002b1d41fef039a037953d1d83870b30df9d8b866d08bb342e730afc8d(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AwsProviderAssumeRoleWithWebIdentity]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28c2a8167c3d2115ba3df955c955afc18730cd4b10688e4d9934283208385be2(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45b2d53dd8713e1dd30367f0c8376dc6404c320280b908ccf4687ef5aa4b6835(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AwsProviderDefaultTags]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a12dac34870a5a7d31cb2d42b50dea386e855834da222b5bdb85c9b02be9c824(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a0fecbb3502d66f4f7ac00b35c942b7ad269c8f3368ca481204974392387ea9(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44cf70c04669415b95c340040ea5ce3a2adaf476fe92ba5eebadd75435885dcf(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AwsProviderEndpoints]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45514e4f66b3c0aa52ceecb9e7cf357a2541e84cdb33866a3a6da52659fc5aee(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d6ba31ab6d5a4111534cc9b5fc2d0d1b1dc350bda85c7bb6aebf3f10188ee6d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16683780d9eacaedd2cf65280152029a69a167e488b8623b61a651e0316ba5e3(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AwsProviderIgnoreTags]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__094adf8bdd9b9a3ea41642f94a994cdf56f25da81d321c32c48ae66f447fc61b(
    value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b018725e01d4a3ade844dcc151c024b47aadf1c55e456cce61d709ed19e73f64(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9184f99f37a3d220afd57022265d0af921611a203aa47ce115f952b53178496(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8c00dcfe02c07916c464a24f072f2a8e1d0390da62549baa91b191a4c4c14a7(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__033897ae06184956e1dbf5dd7cf889aa87ebc0c00a086e085eaa5f6c9a5fcb40(
    value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__686b231465994a539b88bdf0e95707aa84c55bcc4b640ca69b81ff45ae596d42(
    value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae41e856252e3b69e779fb6b346e6aae59c2d3fc39ea03583639b333ea9d4120(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1ba8c54427949734bd8a68812aa794c2bd4cb81504a45ed6bd55ccf84dab77b(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b14d56a92dd2e162cde5054496ec5568fd9b23d3ef31e9a8cb8722b49e732cfe(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a40fc10d1dbf901352037de043909f55f97f4908b10e6e07028ed3177e70c373(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e443b795c5d55f61beb3fa4e4844cda29aede842a6a9023cd2442727bdb010eb(
    value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8932825103f712331b2dacdacaea36711d22567775b8bff2619418e45809bbda(
    value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b20ba7ad50835e6972879f3fc419cc34b0d7de8aeb27e4080636d655409b14ab(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aff73211f199187fe1e0e34b193e02104a1927899f4532f239b0321bc16f9be6(
    value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb112861603b499c47cddbd7ddc62f0a1460f6dc6d3adfd38b847f3edf0cb2a2(
    value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__517ccea055b266de0e5ffca9bb644a96a230832c75c334303ffc9cfc70ca167a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad511e3b75941062abca1b6ded90cac12aa0f47fa514934d3a2fd0ffbd2c46c1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01d4cc1b5a3b984b8f43f432d6a3d5972761b9eee58d1fc2009a83b4de4b1050(
    value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de337857ad500f27ce46e3c2809ed7b32771c82c10b446dd4bc550dc4e4eb5ab(
    value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b0fff6151c5904dd835a46fffd2fd5f0197275551ff7e730c5617064f2f3e1b(
    *,
    duration: typing.Optional[builtins.str] = None,
    duration_seconds: typing.Optional[jsii.Number] = None,
    external_id: typing.Optional[builtins.str] = None,
    policy: typing.Optional[builtins.str] = None,
    policy_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    role_arn: typing.Optional[builtins.str] = None,
    session_name: typing.Optional[builtins.str] = None,
    source_identity: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    transitive_tag_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a265297a0d9fa8e6ce4af0874bbe7cece183921599025e79896c84c87070063a(
    *,
    duration: typing.Optional[builtins.str] = None,
    policy: typing.Optional[builtins.str] = None,
    policy_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    role_arn: typing.Optional[builtins.str] = None,
    session_name: typing.Optional[builtins.str] = None,
    web_identity_token: typing.Optional[builtins.str] = None,
    web_identity_token_file: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e9ecfe711aa56fab8e9a3d50b7f17efb93eb1eb278f40da236a53dd50521d10(
    *,
    access_key: typing.Optional[builtins.str] = None,
    alias: typing.Optional[builtins.str] = None,
    allowed_account_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    assume_role: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AwsProviderAssumeRole, typing.Dict[builtins.str, typing.Any]]]]] = None,
    assume_role_with_web_identity: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AwsProviderAssumeRoleWithWebIdentity, typing.Dict[builtins.str, typing.Any]]]]] = None,
    custom_ca_bundle: typing.Optional[builtins.str] = None,
    default_tags: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AwsProviderDefaultTags, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ec2_metadata_service_endpoint: typing.Optional[builtins.str] = None,
    ec2_metadata_service_endpoint_mode: typing.Optional[builtins.str] = None,
    endpoints: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AwsProviderEndpoints, typing.Dict[builtins.str, typing.Any]]]]] = None,
    forbidden_account_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    http_proxy: typing.Optional[builtins.str] = None,
    ignore_tags: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AwsProviderIgnoreTags, typing.Dict[builtins.str, typing.Any]]]]] = None,
    insecure: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    max_retries: typing.Optional[jsii.Number] = None,
    profile: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
    s3_force_path_style: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    s3_use_path_style: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    secret_key: typing.Optional[builtins.str] = None,
    shared_config_files: typing.Optional[typing.Sequence[builtins.str]] = None,
    shared_credentials_file: typing.Optional[builtins.str] = None,
    shared_credentials_files: typing.Optional[typing.Sequence[builtins.str]] = None,
    skip_credentials_validation: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    skip_get_ec2_platforms: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    skip_metadata_api_check: typing.Optional[builtins.str] = None,
    skip_region_validation: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    skip_requesting_account_id: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    sts_region: typing.Optional[builtins.str] = None,
    token: typing.Optional[builtins.str] = None,
    use_dualstack_endpoint: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    use_fips_endpoint: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb76121620bbaaac7f362352ab85bc4488f7ca86ee9a1c8bf07a2ded9499c487(
    *,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94629cb2539035d8ffea4741e9daf3cf532679568af0e67223cdf5133dc96742(
    *,
    accessanalyzer: typing.Optional[builtins.str] = None,
    account: typing.Optional[builtins.str] = None,
    acm: typing.Optional[builtins.str] = None,
    acmpca: typing.Optional[builtins.str] = None,
    alexaforbusiness: typing.Optional[builtins.str] = None,
    amg: typing.Optional[builtins.str] = None,
    amp: typing.Optional[builtins.str] = None,
    amplify: typing.Optional[builtins.str] = None,
    amplifybackend: typing.Optional[builtins.str] = None,
    amplifyuibuilder: typing.Optional[builtins.str] = None,
    apigateway: typing.Optional[builtins.str] = None,
    apigatewaymanagementapi: typing.Optional[builtins.str] = None,
    apigatewayv2: typing.Optional[builtins.str] = None,
    appautoscaling: typing.Optional[builtins.str] = None,
    appconfig: typing.Optional[builtins.str] = None,
    appconfigdata: typing.Optional[builtins.str] = None,
    appflow: typing.Optional[builtins.str] = None,
    appintegrations: typing.Optional[builtins.str] = None,
    appintegrationsservice: typing.Optional[builtins.str] = None,
    applicationautoscaling: typing.Optional[builtins.str] = None,
    applicationcostprofiler: typing.Optional[builtins.str] = None,
    applicationdiscovery: typing.Optional[builtins.str] = None,
    applicationdiscoveryservice: typing.Optional[builtins.str] = None,
    applicationinsights: typing.Optional[builtins.str] = None,
    appmesh: typing.Optional[builtins.str] = None,
    appregistry: typing.Optional[builtins.str] = None,
    apprunner: typing.Optional[builtins.str] = None,
    appstream: typing.Optional[builtins.str] = None,
    appsync: typing.Optional[builtins.str] = None,
    athena: typing.Optional[builtins.str] = None,
    auditmanager: typing.Optional[builtins.str] = None,
    augmentedairuntime: typing.Optional[builtins.str] = None,
    autoscaling: typing.Optional[builtins.str] = None,
    autoscalingplans: typing.Optional[builtins.str] = None,
    backup: typing.Optional[builtins.str] = None,
    backupgateway: typing.Optional[builtins.str] = None,
    batch: typing.Optional[builtins.str] = None,
    beanstalk: typing.Optional[builtins.str] = None,
    billingconductor: typing.Optional[builtins.str] = None,
    braket: typing.Optional[builtins.str] = None,
    budgets: typing.Optional[builtins.str] = None,
    ce: typing.Optional[builtins.str] = None,
    chime: typing.Optional[builtins.str] = None,
    chimesdkidentity: typing.Optional[builtins.str] = None,
    chimesdkmeetings: typing.Optional[builtins.str] = None,
    chimesdkmessaging: typing.Optional[builtins.str] = None,
    cloud9: typing.Optional[builtins.str] = None,
    cloudcontrol: typing.Optional[builtins.str] = None,
    cloudcontrolapi: typing.Optional[builtins.str] = None,
    clouddirectory: typing.Optional[builtins.str] = None,
    cloudformation: typing.Optional[builtins.str] = None,
    cloudfront: typing.Optional[builtins.str] = None,
    cloudhsm: typing.Optional[builtins.str] = None,
    cloudhsmv2: typing.Optional[builtins.str] = None,
    cloudsearch: typing.Optional[builtins.str] = None,
    cloudsearchdomain: typing.Optional[builtins.str] = None,
    cloudtrail: typing.Optional[builtins.str] = None,
    cloudwatch: typing.Optional[builtins.str] = None,
    cloudwatchevents: typing.Optional[builtins.str] = None,
    cloudwatchevidently: typing.Optional[builtins.str] = None,
    cloudwatchlog: typing.Optional[builtins.str] = None,
    cloudwatchlogs: typing.Optional[builtins.str] = None,
    cloudwatchrum: typing.Optional[builtins.str] = None,
    codeartifact: typing.Optional[builtins.str] = None,
    codebuild: typing.Optional[builtins.str] = None,
    codecommit: typing.Optional[builtins.str] = None,
    codedeploy: typing.Optional[builtins.str] = None,
    codeguruprofiler: typing.Optional[builtins.str] = None,
    codegurureviewer: typing.Optional[builtins.str] = None,
    codepipeline: typing.Optional[builtins.str] = None,
    codestar: typing.Optional[builtins.str] = None,
    codestarconnections: typing.Optional[builtins.str] = None,
    codestarnotifications: typing.Optional[builtins.str] = None,
    cognitoidentity: typing.Optional[builtins.str] = None,
    cognitoidentityprovider: typing.Optional[builtins.str] = None,
    cognitoidp: typing.Optional[builtins.str] = None,
    cognitosync: typing.Optional[builtins.str] = None,
    comprehend: typing.Optional[builtins.str] = None,
    comprehendmedical: typing.Optional[builtins.str] = None,
    computeoptimizer: typing.Optional[builtins.str] = None,
    config: typing.Optional[builtins.str] = None,
    configservice: typing.Optional[builtins.str] = None,
    connect: typing.Optional[builtins.str] = None,
    connectcontactlens: typing.Optional[builtins.str] = None,
    connectparticipant: typing.Optional[builtins.str] = None,
    connectwisdomservice: typing.Optional[builtins.str] = None,
    controltower: typing.Optional[builtins.str] = None,
    costandusagereportservice: typing.Optional[builtins.str] = None,
    costexplorer: typing.Optional[builtins.str] = None,
    cur: typing.Optional[builtins.str] = None,
    customerprofiles: typing.Optional[builtins.str] = None,
    databasemigration: typing.Optional[builtins.str] = None,
    databasemigrationservice: typing.Optional[builtins.str] = None,
    databrew: typing.Optional[builtins.str] = None,
    dataexchange: typing.Optional[builtins.str] = None,
    datapipeline: typing.Optional[builtins.str] = None,
    datasync: typing.Optional[builtins.str] = None,
    dax: typing.Optional[builtins.str] = None,
    deploy: typing.Optional[builtins.str] = None,
    detective: typing.Optional[builtins.str] = None,
    devicefarm: typing.Optional[builtins.str] = None,
    devopsguru: typing.Optional[builtins.str] = None,
    directconnect: typing.Optional[builtins.str] = None,
    directoryservice: typing.Optional[builtins.str] = None,
    discovery: typing.Optional[builtins.str] = None,
    dlm: typing.Optional[builtins.str] = None,
    dms: typing.Optional[builtins.str] = None,
    docdb: typing.Optional[builtins.str] = None,
    drs: typing.Optional[builtins.str] = None,
    ds: typing.Optional[builtins.str] = None,
    dynamodb: typing.Optional[builtins.str] = None,
    dynamodbstreams: typing.Optional[builtins.str] = None,
    ebs: typing.Optional[builtins.str] = None,
    ec2: typing.Optional[builtins.str] = None,
    ec2_instanceconnect: typing.Optional[builtins.str] = None,
    ecr: typing.Optional[builtins.str] = None,
    ecrpublic: typing.Optional[builtins.str] = None,
    ecs: typing.Optional[builtins.str] = None,
    efs: typing.Optional[builtins.str] = None,
    eks: typing.Optional[builtins.str] = None,
    elasticache: typing.Optional[builtins.str] = None,
    elasticbeanstalk: typing.Optional[builtins.str] = None,
    elasticinference: typing.Optional[builtins.str] = None,
    elasticloadbalancing: typing.Optional[builtins.str] = None,
    elasticloadbalancingv2: typing.Optional[builtins.str] = None,
    elasticsearch: typing.Optional[builtins.str] = None,
    elasticsearchservice: typing.Optional[builtins.str] = None,
    elastictranscoder: typing.Optional[builtins.str] = None,
    elb: typing.Optional[builtins.str] = None,
    elbv2: typing.Optional[builtins.str] = None,
    emr: typing.Optional[builtins.str] = None,
    emrcontainers: typing.Optional[builtins.str] = None,
    emrserverless: typing.Optional[builtins.str] = None,
    es: typing.Optional[builtins.str] = None,
    eventbridge: typing.Optional[builtins.str] = None,
    events: typing.Optional[builtins.str] = None,
    evidently: typing.Optional[builtins.str] = None,
    finspace: typing.Optional[builtins.str] = None,
    finspacedata: typing.Optional[builtins.str] = None,
    firehose: typing.Optional[builtins.str] = None,
    fis: typing.Optional[builtins.str] = None,
    fms: typing.Optional[builtins.str] = None,
    forecast: typing.Optional[builtins.str] = None,
    forecastquery: typing.Optional[builtins.str] = None,
    forecastqueryservice: typing.Optional[builtins.str] = None,
    forecastservice: typing.Optional[builtins.str] = None,
    frauddetector: typing.Optional[builtins.str] = None,
    fsx: typing.Optional[builtins.str] = None,
    gamelift: typing.Optional[builtins.str] = None,
    glacier: typing.Optional[builtins.str] = None,
    globalaccelerator: typing.Optional[builtins.str] = None,
    glue: typing.Optional[builtins.str] = None,
    gluedatabrew: typing.Optional[builtins.str] = None,
    grafana: typing.Optional[builtins.str] = None,
    greengrass: typing.Optional[builtins.str] = None,
    greengrassv2: typing.Optional[builtins.str] = None,
    groundstation: typing.Optional[builtins.str] = None,
    guardduty: typing.Optional[builtins.str] = None,
    health: typing.Optional[builtins.str] = None,
    healthlake: typing.Optional[builtins.str] = None,
    honeycode: typing.Optional[builtins.str] = None,
    iam: typing.Optional[builtins.str] = None,
    identitystore: typing.Optional[builtins.str] = None,
    imagebuilder: typing.Optional[builtins.str] = None,
    inspector: typing.Optional[builtins.str] = None,
    inspector2: typing.Optional[builtins.str] = None,
    inspectorv2: typing.Optional[builtins.str] = None,
    iot: typing.Optional[builtins.str] = None,
    iot1_clickdevices: typing.Optional[builtins.str] = None,
    iot1_clickdevicesservice: typing.Optional[builtins.str] = None,
    iot1_clickprojects: typing.Optional[builtins.str] = None,
    iotanalytics: typing.Optional[builtins.str] = None,
    iotdata: typing.Optional[builtins.str] = None,
    iotdataplane: typing.Optional[builtins.str] = None,
    iotdeviceadvisor: typing.Optional[builtins.str] = None,
    iotevents: typing.Optional[builtins.str] = None,
    ioteventsdata: typing.Optional[builtins.str] = None,
    iotfleethub: typing.Optional[builtins.str] = None,
    iotjobsdata: typing.Optional[builtins.str] = None,
    iotjobsdataplane: typing.Optional[builtins.str] = None,
    iotsecuretunneling: typing.Optional[builtins.str] = None,
    iotsitewise: typing.Optional[builtins.str] = None,
    iotthingsgraph: typing.Optional[builtins.str] = None,
    iottwinmaker: typing.Optional[builtins.str] = None,
    iotwireless: typing.Optional[builtins.str] = None,
    ivs: typing.Optional[builtins.str] = None,
    ivschat: typing.Optional[builtins.str] = None,
    kafka: typing.Optional[builtins.str] = None,
    kafkaconnect: typing.Optional[builtins.str] = None,
    kendra: typing.Optional[builtins.str] = None,
    keyspaces: typing.Optional[builtins.str] = None,
    kinesis: typing.Optional[builtins.str] = None,
    kinesisanalytics: typing.Optional[builtins.str] = None,
    kinesisanalyticsv2: typing.Optional[builtins.str] = None,
    kinesisvideo: typing.Optional[builtins.str] = None,
    kinesisvideoarchivedmedia: typing.Optional[builtins.str] = None,
    kinesisvideomedia: typing.Optional[builtins.str] = None,
    kinesisvideosignaling: typing.Optional[builtins.str] = None,
    kinesisvideosignalingchannels: typing.Optional[builtins.str] = None,
    kms: typing.Optional[builtins.str] = None,
    lakeformation: typing.Optional[builtins.str] = None,
    lambda_: typing.Optional[builtins.str] = None,
    lex: typing.Optional[builtins.str] = None,
    lexmodelbuilding: typing.Optional[builtins.str] = None,
    lexmodelbuildingservice: typing.Optional[builtins.str] = None,
    lexmodels: typing.Optional[builtins.str] = None,
    lexmodelsv2: typing.Optional[builtins.str] = None,
    lexruntime: typing.Optional[builtins.str] = None,
    lexruntimeservice: typing.Optional[builtins.str] = None,
    lexruntimev2: typing.Optional[builtins.str] = None,
    lexv2_models: typing.Optional[builtins.str] = None,
    lexv2_runtime: typing.Optional[builtins.str] = None,
    licensemanager: typing.Optional[builtins.str] = None,
    lightsail: typing.Optional[builtins.str] = None,
    location: typing.Optional[builtins.str] = None,
    locationservice: typing.Optional[builtins.str] = None,
    logs: typing.Optional[builtins.str] = None,
    lookoutequipment: typing.Optional[builtins.str] = None,
    lookoutforvision: typing.Optional[builtins.str] = None,
    lookoutmetrics: typing.Optional[builtins.str] = None,
    lookoutvision: typing.Optional[builtins.str] = None,
    machinelearning: typing.Optional[builtins.str] = None,
    macie: typing.Optional[builtins.str] = None,
    macie2: typing.Optional[builtins.str] = None,
    managedblockchain: typing.Optional[builtins.str] = None,
    managedgrafana: typing.Optional[builtins.str] = None,
    marketplacecatalog: typing.Optional[builtins.str] = None,
    marketplacecommerceanalytics: typing.Optional[builtins.str] = None,
    marketplaceentitlement: typing.Optional[builtins.str] = None,
    marketplaceentitlementservice: typing.Optional[builtins.str] = None,
    marketplacemetering: typing.Optional[builtins.str] = None,
    mediaconnect: typing.Optional[builtins.str] = None,
    mediaconvert: typing.Optional[builtins.str] = None,
    medialive: typing.Optional[builtins.str] = None,
    mediapackage: typing.Optional[builtins.str] = None,
    mediapackagevod: typing.Optional[builtins.str] = None,
    mediastore: typing.Optional[builtins.str] = None,
    mediastoredata: typing.Optional[builtins.str] = None,
    mediatailor: typing.Optional[builtins.str] = None,
    memorydb: typing.Optional[builtins.str] = None,
    meteringmarketplace: typing.Optional[builtins.str] = None,
    mgh: typing.Optional[builtins.str] = None,
    mgn: typing.Optional[builtins.str] = None,
    migrationhub: typing.Optional[builtins.str] = None,
    migrationhubconfig: typing.Optional[builtins.str] = None,
    migrationhubrefactorspaces: typing.Optional[builtins.str] = None,
    migrationhubstrategy: typing.Optional[builtins.str] = None,
    migrationhubstrategyrecommendations: typing.Optional[builtins.str] = None,
    mobile: typing.Optional[builtins.str] = None,
    mq: typing.Optional[builtins.str] = None,
    msk: typing.Optional[builtins.str] = None,
    mturk: typing.Optional[builtins.str] = None,
    mwaa: typing.Optional[builtins.str] = None,
    neptune: typing.Optional[builtins.str] = None,
    networkfirewall: typing.Optional[builtins.str] = None,
    networkmanager: typing.Optional[builtins.str] = None,
    nimble: typing.Optional[builtins.str] = None,
    nimblestudio: typing.Optional[builtins.str] = None,
    opensearch: typing.Optional[builtins.str] = None,
    opensearchserverless: typing.Optional[builtins.str] = None,
    opensearchservice: typing.Optional[builtins.str] = None,
    opsworks: typing.Optional[builtins.str] = None,
    opsworkscm: typing.Optional[builtins.str] = None,
    organizations: typing.Optional[builtins.str] = None,
    outposts: typing.Optional[builtins.str] = None,
    panorama: typing.Optional[builtins.str] = None,
    personalize: typing.Optional[builtins.str] = None,
    personalizeevents: typing.Optional[builtins.str] = None,
    personalizeruntime: typing.Optional[builtins.str] = None,
    pi: typing.Optional[builtins.str] = None,
    pinpoint: typing.Optional[builtins.str] = None,
    pinpointemail: typing.Optional[builtins.str] = None,
    pinpointsmsvoice: typing.Optional[builtins.str] = None,
    pipes: typing.Optional[builtins.str] = None,
    polly: typing.Optional[builtins.str] = None,
    pricing: typing.Optional[builtins.str] = None,
    prometheus: typing.Optional[builtins.str] = None,
    prometheusservice: typing.Optional[builtins.str] = None,
    proton: typing.Optional[builtins.str] = None,
    qldb: typing.Optional[builtins.str] = None,
    qldbsession: typing.Optional[builtins.str] = None,
    quicksight: typing.Optional[builtins.str] = None,
    ram: typing.Optional[builtins.str] = None,
    rbin: typing.Optional[builtins.str] = None,
    rds: typing.Optional[builtins.str] = None,
    rdsdata: typing.Optional[builtins.str] = None,
    rdsdataservice: typing.Optional[builtins.str] = None,
    recyclebin: typing.Optional[builtins.str] = None,
    redshift: typing.Optional[builtins.str] = None,
    redshiftdata: typing.Optional[builtins.str] = None,
    redshiftdataapiservice: typing.Optional[builtins.str] = None,
    redshiftserverless: typing.Optional[builtins.str] = None,
    rekognition: typing.Optional[builtins.str] = None,
    resiliencehub: typing.Optional[builtins.str] = None,
    resourceexplorer2: typing.Optional[builtins.str] = None,
    resourcegroups: typing.Optional[builtins.str] = None,
    resourcegroupstagging: typing.Optional[builtins.str] = None,
    resourcegroupstaggingapi: typing.Optional[builtins.str] = None,
    robomaker: typing.Optional[builtins.str] = None,
    rolesanywhere: typing.Optional[builtins.str] = None,
    route53: typing.Optional[builtins.str] = None,
    route53_domains: typing.Optional[builtins.str] = None,
    route53_recoverycluster: typing.Optional[builtins.str] = None,
    route53_recoverycontrolconfig: typing.Optional[builtins.str] = None,
    route53_recoveryreadiness: typing.Optional[builtins.str] = None,
    route53_resolver: typing.Optional[builtins.str] = None,
    rum: typing.Optional[builtins.str] = None,
    s3: typing.Optional[builtins.str] = None,
    s3_api: typing.Optional[builtins.str] = None,
    s3_control: typing.Optional[builtins.str] = None,
    s3_outposts: typing.Optional[builtins.str] = None,
    sagemaker: typing.Optional[builtins.str] = None,
    sagemakera2_iruntime: typing.Optional[builtins.str] = None,
    sagemakeredge: typing.Optional[builtins.str] = None,
    sagemakeredgemanager: typing.Optional[builtins.str] = None,
    sagemakerfeaturestoreruntime: typing.Optional[builtins.str] = None,
    sagemakerruntime: typing.Optional[builtins.str] = None,
    savingsplans: typing.Optional[builtins.str] = None,
    scheduler: typing.Optional[builtins.str] = None,
    schemas: typing.Optional[builtins.str] = None,
    sdb: typing.Optional[builtins.str] = None,
    secretsmanager: typing.Optional[builtins.str] = None,
    securityhub: typing.Optional[builtins.str] = None,
    serverlessapplicationrepository: typing.Optional[builtins.str] = None,
    serverlessapprepo: typing.Optional[builtins.str] = None,
    serverlessrepo: typing.Optional[builtins.str] = None,
    servicecatalog: typing.Optional[builtins.str] = None,
    servicecatalogappregistry: typing.Optional[builtins.str] = None,
    servicediscovery: typing.Optional[builtins.str] = None,
    servicequotas: typing.Optional[builtins.str] = None,
    ses: typing.Optional[builtins.str] = None,
    sesv2: typing.Optional[builtins.str] = None,
    sfn: typing.Optional[builtins.str] = None,
    shield: typing.Optional[builtins.str] = None,
    signer: typing.Optional[builtins.str] = None,
    simpledb: typing.Optional[builtins.str] = None,
    sms: typing.Optional[builtins.str] = None,
    snowball: typing.Optional[builtins.str] = None,
    snowdevicemanagement: typing.Optional[builtins.str] = None,
    sns: typing.Optional[builtins.str] = None,
    sqs: typing.Optional[builtins.str] = None,
    ssm: typing.Optional[builtins.str] = None,
    ssmcontacts: typing.Optional[builtins.str] = None,
    ssmincidents: typing.Optional[builtins.str] = None,
    sso: typing.Optional[builtins.str] = None,
    ssoadmin: typing.Optional[builtins.str] = None,
    ssooidc: typing.Optional[builtins.str] = None,
    stepfunctions: typing.Optional[builtins.str] = None,
    storagegateway: typing.Optional[builtins.str] = None,
    sts: typing.Optional[builtins.str] = None,
    support: typing.Optional[builtins.str] = None,
    swf: typing.Optional[builtins.str] = None,
    synthetics: typing.Optional[builtins.str] = None,
    textract: typing.Optional[builtins.str] = None,
    timestreamquery: typing.Optional[builtins.str] = None,
    timestreamwrite: typing.Optional[builtins.str] = None,
    transcribe: typing.Optional[builtins.str] = None,
    transcribeservice: typing.Optional[builtins.str] = None,
    transcribestreaming: typing.Optional[builtins.str] = None,
    transcribestreamingservice: typing.Optional[builtins.str] = None,
    transfer: typing.Optional[builtins.str] = None,
    translate: typing.Optional[builtins.str] = None,
    voiceid: typing.Optional[builtins.str] = None,
    waf: typing.Optional[builtins.str] = None,
    wafregional: typing.Optional[builtins.str] = None,
    wafv2: typing.Optional[builtins.str] = None,
    wellarchitected: typing.Optional[builtins.str] = None,
    wisdom: typing.Optional[builtins.str] = None,
    workdocs: typing.Optional[builtins.str] = None,
    worklink: typing.Optional[builtins.str] = None,
    workmail: typing.Optional[builtins.str] = None,
    workmailmessageflow: typing.Optional[builtins.str] = None,
    workspaces: typing.Optional[builtins.str] = None,
    workspacesweb: typing.Optional[builtins.str] = None,
    xray: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39ac3b64a995e2099f8d83cb9c4225e6c1f41923f4b962f43b6263c1041e9c65(
    *,
    key_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
    keys: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass
