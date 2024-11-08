'''
# `aws_cloudfront_distribution`

Refer to the Terraform Registory for docs: [`aws_cloudfront_distribution`](https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution).
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


class CloudfrontDistribution(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudfrontDistribution.CloudfrontDistribution",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution aws_cloudfront_distribution}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        default_cache_behavior: typing.Union["CloudfrontDistributionDefaultCacheBehavior", typing.Dict[builtins.str, typing.Any]],
        enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        origin: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CloudfrontDistributionOrigin", typing.Dict[builtins.str, typing.Any]]]],
        restrictions: typing.Union["CloudfrontDistributionRestrictions", typing.Dict[builtins.str, typing.Any]],
        viewer_certificate: typing.Union["CloudfrontDistributionViewerCertificate", typing.Dict[builtins.str, typing.Any]],
        aliases: typing.Optional[typing.Sequence[builtins.str]] = None,
        comment: typing.Optional[builtins.str] = None,
        custom_error_response: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CloudfrontDistributionCustomErrorResponse", typing.Dict[builtins.str, typing.Any]]]]] = None,
        default_root_object: typing.Optional[builtins.str] = None,
        http_version: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        is_ipv6_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        logging_config: typing.Optional[typing.Union["CloudfrontDistributionLoggingConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        ordered_cache_behavior: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CloudfrontDistributionOrderedCacheBehavior", typing.Dict[builtins.str, typing.Any]]]]] = None,
        origin_group: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CloudfrontDistributionOriginGroup", typing.Dict[builtins.str, typing.Any]]]]] = None,
        price_class: typing.Optional[builtins.str] = None,
        retain_on_delete: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        wait_for_deployment: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        web_acl_id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution aws_cloudfront_distribution} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param default_cache_behavior: default_cache_behavior block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#default_cache_behavior CloudfrontDistribution#default_cache_behavior}
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#enabled CloudfrontDistribution#enabled}.
        :param origin: origin block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#origin CloudfrontDistribution#origin}
        :param restrictions: restrictions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#restrictions CloudfrontDistribution#restrictions}
        :param viewer_certificate: viewer_certificate block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#viewer_certificate CloudfrontDistribution#viewer_certificate}
        :param aliases: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#aliases CloudfrontDistribution#aliases}.
        :param comment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#comment CloudfrontDistribution#comment}.
        :param custom_error_response: custom_error_response block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#custom_error_response CloudfrontDistribution#custom_error_response}
        :param default_root_object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#default_root_object CloudfrontDistribution#default_root_object}.
        :param http_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#http_version CloudfrontDistribution#http_version}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#id CloudfrontDistribution#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param is_ipv6_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#is_ipv6_enabled CloudfrontDistribution#is_ipv6_enabled}.
        :param logging_config: logging_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#logging_config CloudfrontDistribution#logging_config}
        :param ordered_cache_behavior: ordered_cache_behavior block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#ordered_cache_behavior CloudfrontDistribution#ordered_cache_behavior}
        :param origin_group: origin_group block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#origin_group CloudfrontDistribution#origin_group}
        :param price_class: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#price_class CloudfrontDistribution#price_class}.
        :param retain_on_delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#retain_on_delete CloudfrontDistribution#retain_on_delete}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#tags CloudfrontDistribution#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#tags_all CloudfrontDistribution#tags_all}.
        :param wait_for_deployment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#wait_for_deployment CloudfrontDistribution#wait_for_deployment}.
        :param web_acl_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#web_acl_id CloudfrontDistribution#web_acl_id}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__537c13993acd6e2b6c73b4161f7ac82b232baca0cf078fcc6e7ed3b5423fb000)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = CloudfrontDistributionConfig(
            default_cache_behavior=default_cache_behavior,
            enabled=enabled,
            origin=origin,
            restrictions=restrictions,
            viewer_certificate=viewer_certificate,
            aliases=aliases,
            comment=comment,
            custom_error_response=custom_error_response,
            default_root_object=default_root_object,
            http_version=http_version,
            id=id,
            is_ipv6_enabled=is_ipv6_enabled,
            logging_config=logging_config,
            ordered_cache_behavior=ordered_cache_behavior,
            origin_group=origin_group,
            price_class=price_class,
            retain_on_delete=retain_on_delete,
            tags=tags,
            tags_all=tags_all,
            wait_for_deployment=wait_for_deployment,
            web_acl_id=web_acl_id,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putCustomErrorResponse")
    def put_custom_error_response(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CloudfrontDistributionCustomErrorResponse", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__693fa4e944d0c071082304dfbddc46ac8859d49f45a0179496be98b02699d2b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCustomErrorResponse", [value]))

    @jsii.member(jsii_name="putDefaultCacheBehavior")
    def put_default_cache_behavior(
        self,
        *,
        allowed_methods: typing.Sequence[builtins.str],
        cached_methods: typing.Sequence[builtins.str],
        target_origin_id: builtins.str,
        viewer_protocol_policy: builtins.str,
        cache_policy_id: typing.Optional[builtins.str] = None,
        compress: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        default_ttl: typing.Optional[jsii.Number] = None,
        field_level_encryption_id: typing.Optional[builtins.str] = None,
        forwarded_values: typing.Optional[typing.Union["CloudfrontDistributionDefaultCacheBehaviorForwardedValues", typing.Dict[builtins.str, typing.Any]]] = None,
        function_association: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CloudfrontDistributionDefaultCacheBehaviorFunctionAssociation", typing.Dict[builtins.str, typing.Any]]]]] = None,
        lambda_function_association: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CloudfrontDistributionDefaultCacheBehaviorLambdaFunctionAssociation", typing.Dict[builtins.str, typing.Any]]]]] = None,
        max_ttl: typing.Optional[jsii.Number] = None,
        min_ttl: typing.Optional[jsii.Number] = None,
        origin_request_policy_id: typing.Optional[builtins.str] = None,
        realtime_log_config_arn: typing.Optional[builtins.str] = None,
        response_headers_policy_id: typing.Optional[builtins.str] = None,
        smooth_streaming: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        trusted_key_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        trusted_signers: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param allowed_methods: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#allowed_methods CloudfrontDistribution#allowed_methods}.
        :param cached_methods: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#cached_methods CloudfrontDistribution#cached_methods}.
        :param target_origin_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#target_origin_id CloudfrontDistribution#target_origin_id}.
        :param viewer_protocol_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#viewer_protocol_policy CloudfrontDistribution#viewer_protocol_policy}.
        :param cache_policy_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#cache_policy_id CloudfrontDistribution#cache_policy_id}.
        :param compress: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#compress CloudfrontDistribution#compress}.
        :param default_ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#default_ttl CloudfrontDistribution#default_ttl}.
        :param field_level_encryption_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#field_level_encryption_id CloudfrontDistribution#field_level_encryption_id}.
        :param forwarded_values: forwarded_values block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#forwarded_values CloudfrontDistribution#forwarded_values}
        :param function_association: function_association block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#function_association CloudfrontDistribution#function_association}
        :param lambda_function_association: lambda_function_association block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#lambda_function_association CloudfrontDistribution#lambda_function_association}
        :param max_ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#max_ttl CloudfrontDistribution#max_ttl}.
        :param min_ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#min_ttl CloudfrontDistribution#min_ttl}.
        :param origin_request_policy_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#origin_request_policy_id CloudfrontDistribution#origin_request_policy_id}.
        :param realtime_log_config_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#realtime_log_config_arn CloudfrontDistribution#realtime_log_config_arn}.
        :param response_headers_policy_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#response_headers_policy_id CloudfrontDistribution#response_headers_policy_id}.
        :param smooth_streaming: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#smooth_streaming CloudfrontDistribution#smooth_streaming}.
        :param trusted_key_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#trusted_key_groups CloudfrontDistribution#trusted_key_groups}.
        :param trusted_signers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#trusted_signers CloudfrontDistribution#trusted_signers}.
        '''
        value = CloudfrontDistributionDefaultCacheBehavior(
            allowed_methods=allowed_methods,
            cached_methods=cached_methods,
            target_origin_id=target_origin_id,
            viewer_protocol_policy=viewer_protocol_policy,
            cache_policy_id=cache_policy_id,
            compress=compress,
            default_ttl=default_ttl,
            field_level_encryption_id=field_level_encryption_id,
            forwarded_values=forwarded_values,
            function_association=function_association,
            lambda_function_association=lambda_function_association,
            max_ttl=max_ttl,
            min_ttl=min_ttl,
            origin_request_policy_id=origin_request_policy_id,
            realtime_log_config_arn=realtime_log_config_arn,
            response_headers_policy_id=response_headers_policy_id,
            smooth_streaming=smooth_streaming,
            trusted_key_groups=trusted_key_groups,
            trusted_signers=trusted_signers,
        )

        return typing.cast(None, jsii.invoke(self, "putDefaultCacheBehavior", [value]))

    @jsii.member(jsii_name="putLoggingConfig")
    def put_logging_config(
        self,
        *,
        bucket: builtins.str,
        include_cookies: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#bucket CloudfrontDistribution#bucket}.
        :param include_cookies: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#include_cookies CloudfrontDistribution#include_cookies}.
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#prefix CloudfrontDistribution#prefix}.
        '''
        value = CloudfrontDistributionLoggingConfig(
            bucket=bucket, include_cookies=include_cookies, prefix=prefix
        )

        return typing.cast(None, jsii.invoke(self, "putLoggingConfig", [value]))

    @jsii.member(jsii_name="putOrderedCacheBehavior")
    def put_ordered_cache_behavior(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CloudfrontDistributionOrderedCacheBehavior", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4da4967ed056af60178e962bbf55590811d5a4d38162b07225809bb4ada36a3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putOrderedCacheBehavior", [value]))

    @jsii.member(jsii_name="putOrigin")
    def put_origin(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CloudfrontDistributionOrigin", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cbe4bfff05b454ee4d99df93a74777a058f1b0b9bb6f1cc766232e272c6c5333)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putOrigin", [value]))

    @jsii.member(jsii_name="putOriginGroup")
    def put_origin_group(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CloudfrontDistributionOriginGroup", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d2fa0f4a41e4ed0c0c5d2eade544bfb3566349ca184732b735e541b1556111f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putOriginGroup", [value]))

    @jsii.member(jsii_name="putRestrictions")
    def put_restrictions(
        self,
        *,
        geo_restriction: typing.Union["CloudfrontDistributionRestrictionsGeoRestriction", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param geo_restriction: geo_restriction block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#geo_restriction CloudfrontDistribution#geo_restriction}
        '''
        value = CloudfrontDistributionRestrictions(geo_restriction=geo_restriction)

        return typing.cast(None, jsii.invoke(self, "putRestrictions", [value]))

    @jsii.member(jsii_name="putViewerCertificate")
    def put_viewer_certificate(
        self,
        *,
        acm_certificate_arn: typing.Optional[builtins.str] = None,
        cloudfront_default_certificate: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        iam_certificate_id: typing.Optional[builtins.str] = None,
        minimum_protocol_version: typing.Optional[builtins.str] = None,
        ssl_support_method: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param acm_certificate_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#acm_certificate_arn CloudfrontDistribution#acm_certificate_arn}.
        :param cloudfront_default_certificate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#cloudfront_default_certificate CloudfrontDistribution#cloudfront_default_certificate}.
        :param iam_certificate_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#iam_certificate_id CloudfrontDistribution#iam_certificate_id}.
        :param minimum_protocol_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#minimum_protocol_version CloudfrontDistribution#minimum_protocol_version}.
        :param ssl_support_method: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#ssl_support_method CloudfrontDistribution#ssl_support_method}.
        '''
        value = CloudfrontDistributionViewerCertificate(
            acm_certificate_arn=acm_certificate_arn,
            cloudfront_default_certificate=cloudfront_default_certificate,
            iam_certificate_id=iam_certificate_id,
            minimum_protocol_version=minimum_protocol_version,
            ssl_support_method=ssl_support_method,
        )

        return typing.cast(None, jsii.invoke(self, "putViewerCertificate", [value]))

    @jsii.member(jsii_name="resetAliases")
    def reset_aliases(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAliases", []))

    @jsii.member(jsii_name="resetComment")
    def reset_comment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComment", []))

    @jsii.member(jsii_name="resetCustomErrorResponse")
    def reset_custom_error_response(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomErrorResponse", []))

    @jsii.member(jsii_name="resetDefaultRootObject")
    def reset_default_root_object(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultRootObject", []))

    @jsii.member(jsii_name="resetHttpVersion")
    def reset_http_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpVersion", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIsIpv6Enabled")
    def reset_is_ipv6_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsIpv6Enabled", []))

    @jsii.member(jsii_name="resetLoggingConfig")
    def reset_logging_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoggingConfig", []))

    @jsii.member(jsii_name="resetOrderedCacheBehavior")
    def reset_ordered_cache_behavior(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOrderedCacheBehavior", []))

    @jsii.member(jsii_name="resetOriginGroup")
    def reset_origin_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOriginGroup", []))

    @jsii.member(jsii_name="resetPriceClass")
    def reset_price_class(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPriceClass", []))

    @jsii.member(jsii_name="resetRetainOnDelete")
    def reset_retain_on_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetainOnDelete", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetWaitForDeployment")
    def reset_wait_for_deployment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWaitForDeployment", []))

    @jsii.member(jsii_name="resetWebAclId")
    def reset_web_acl_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWebAclId", []))

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
    @jsii.member(jsii_name="callerReference")
    def caller_reference(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "callerReference"))

    @builtins.property
    @jsii.member(jsii_name="customErrorResponse")
    def custom_error_response(self) -> "CloudfrontDistributionCustomErrorResponseList":
        return typing.cast("CloudfrontDistributionCustomErrorResponseList", jsii.get(self, "customErrorResponse"))

    @builtins.property
    @jsii.member(jsii_name="defaultCacheBehavior")
    def default_cache_behavior(
        self,
    ) -> "CloudfrontDistributionDefaultCacheBehaviorOutputReference":
        return typing.cast("CloudfrontDistributionDefaultCacheBehaviorOutputReference", jsii.get(self, "defaultCacheBehavior"))

    @builtins.property
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domainName"))

    @builtins.property
    @jsii.member(jsii_name="etag")
    def etag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "etag"))

    @builtins.property
    @jsii.member(jsii_name="hostedZoneId")
    def hosted_zone_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostedZoneId"))

    @builtins.property
    @jsii.member(jsii_name="inProgressValidationBatches")
    def in_progress_validation_batches(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "inProgressValidationBatches"))

    @builtins.property
    @jsii.member(jsii_name="lastModifiedTime")
    def last_modified_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastModifiedTime"))

    @builtins.property
    @jsii.member(jsii_name="loggingConfig")
    def logging_config(self) -> "CloudfrontDistributionLoggingConfigOutputReference":
        return typing.cast("CloudfrontDistributionLoggingConfigOutputReference", jsii.get(self, "loggingConfig"))

    @builtins.property
    @jsii.member(jsii_name="orderedCacheBehavior")
    def ordered_cache_behavior(
        self,
    ) -> "CloudfrontDistributionOrderedCacheBehaviorList":
        return typing.cast("CloudfrontDistributionOrderedCacheBehaviorList", jsii.get(self, "orderedCacheBehavior"))

    @builtins.property
    @jsii.member(jsii_name="origin")
    def origin(self) -> "CloudfrontDistributionOriginList":
        return typing.cast("CloudfrontDistributionOriginList", jsii.get(self, "origin"))

    @builtins.property
    @jsii.member(jsii_name="originGroup")
    def origin_group(self) -> "CloudfrontDistributionOriginGroupList":
        return typing.cast("CloudfrontDistributionOriginGroupList", jsii.get(self, "originGroup"))

    @builtins.property
    @jsii.member(jsii_name="restrictions")
    def restrictions(self) -> "CloudfrontDistributionRestrictionsOutputReference":
        return typing.cast("CloudfrontDistributionRestrictionsOutputReference", jsii.get(self, "restrictions"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="trustedKeyGroups")
    def trusted_key_groups(self) -> "CloudfrontDistributionTrustedKeyGroupsList":
        return typing.cast("CloudfrontDistributionTrustedKeyGroupsList", jsii.get(self, "trustedKeyGroups"))

    @builtins.property
    @jsii.member(jsii_name="trustedSigners")
    def trusted_signers(self) -> "CloudfrontDistributionTrustedSignersList":
        return typing.cast("CloudfrontDistributionTrustedSignersList", jsii.get(self, "trustedSigners"))

    @builtins.property
    @jsii.member(jsii_name="viewerCertificate")
    def viewer_certificate(
        self,
    ) -> "CloudfrontDistributionViewerCertificateOutputReference":
        return typing.cast("CloudfrontDistributionViewerCertificateOutputReference", jsii.get(self, "viewerCertificate"))

    @builtins.property
    @jsii.member(jsii_name="aliasesInput")
    def aliases_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "aliasesInput"))

    @builtins.property
    @jsii.member(jsii_name="commentInput")
    def comment_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "commentInput"))

    @builtins.property
    @jsii.member(jsii_name="customErrorResponseInput")
    def custom_error_response_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CloudfrontDistributionCustomErrorResponse"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CloudfrontDistributionCustomErrorResponse"]]], jsii.get(self, "customErrorResponseInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultCacheBehaviorInput")
    def default_cache_behavior_input(
        self,
    ) -> typing.Optional["CloudfrontDistributionDefaultCacheBehavior"]:
        return typing.cast(typing.Optional["CloudfrontDistributionDefaultCacheBehavior"], jsii.get(self, "defaultCacheBehaviorInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultRootObjectInput")
    def default_root_object_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultRootObjectInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="httpVersionInput")
    def http_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "httpVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="isIpv6EnabledInput")
    def is_ipv6_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "isIpv6EnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="loggingConfigInput")
    def logging_config_input(
        self,
    ) -> typing.Optional["CloudfrontDistributionLoggingConfig"]:
        return typing.cast(typing.Optional["CloudfrontDistributionLoggingConfig"], jsii.get(self, "loggingConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="orderedCacheBehaviorInput")
    def ordered_cache_behavior_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CloudfrontDistributionOrderedCacheBehavior"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CloudfrontDistributionOrderedCacheBehavior"]]], jsii.get(self, "orderedCacheBehaviorInput"))

    @builtins.property
    @jsii.member(jsii_name="originGroupInput")
    def origin_group_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CloudfrontDistributionOriginGroup"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CloudfrontDistributionOriginGroup"]]], jsii.get(self, "originGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="originInput")
    def origin_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CloudfrontDistributionOrigin"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CloudfrontDistributionOrigin"]]], jsii.get(self, "originInput"))

    @builtins.property
    @jsii.member(jsii_name="priceClassInput")
    def price_class_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "priceClassInput"))

    @builtins.property
    @jsii.member(jsii_name="restrictionsInput")
    def restrictions_input(
        self,
    ) -> typing.Optional["CloudfrontDistributionRestrictions"]:
        return typing.cast(typing.Optional["CloudfrontDistributionRestrictions"], jsii.get(self, "restrictionsInput"))

    @builtins.property
    @jsii.member(jsii_name="retainOnDeleteInput")
    def retain_on_delete_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "retainOnDeleteInput"))

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
    @jsii.member(jsii_name="viewerCertificateInput")
    def viewer_certificate_input(
        self,
    ) -> typing.Optional["CloudfrontDistributionViewerCertificate"]:
        return typing.cast(typing.Optional["CloudfrontDistributionViewerCertificate"], jsii.get(self, "viewerCertificateInput"))

    @builtins.property
    @jsii.member(jsii_name="waitForDeploymentInput")
    def wait_for_deployment_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "waitForDeploymentInput"))

    @builtins.property
    @jsii.member(jsii_name="webAclIdInput")
    def web_acl_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "webAclIdInput"))

    @builtins.property
    @jsii.member(jsii_name="aliases")
    def aliases(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "aliases"))

    @aliases.setter
    def aliases(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__880903284b6361d655958cf340fca71bfbf2d12834fd1f3295487b2ba57a6110)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "aliases", value)

    @builtins.property
    @jsii.member(jsii_name="comment")
    def comment(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "comment"))

    @comment.setter
    def comment(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a31205617d67931520bbe80122e2101b53b6013a30ef03733610878bf1b4efb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "comment", value)

    @builtins.property
    @jsii.member(jsii_name="defaultRootObject")
    def default_root_object(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultRootObject"))

    @default_root_object.setter
    def default_root_object(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de53c6814589d594cc2261ef3600f9d3f83728dcac81719151f918ea38b84a82)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultRootObject", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__02a7ed2f90deaf58736e10a43b6939e6cf1919d5553df6722930d2f3ad52241a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="httpVersion")
    def http_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "httpVersion"))

    @http_version.setter
    def http_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8431d65cf5912b4c51b1420923429f1608527c667f8ce54223d74d361a86baa8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpVersion", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__419ab06763abeca7768f8984a880fb3c25944a916aeeb695be40803d318ee420)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="isIpv6Enabled")
    def is_ipv6_enabled(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "isIpv6Enabled"))

    @is_ipv6_enabled.setter
    def is_ipv6_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a00378c42f69ae7ed5c0c9ff0f10c027a2b0f0cc82273727dabfc0fb296d327)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isIpv6Enabled", value)

    @builtins.property
    @jsii.member(jsii_name="priceClass")
    def price_class(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "priceClass"))

    @price_class.setter
    def price_class(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cbd1fc8803d5fc465c175f89b742add0c745b0f11ceef7f837d088a95b4c33f4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priceClass", value)

    @builtins.property
    @jsii.member(jsii_name="retainOnDelete")
    def retain_on_delete(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "retainOnDelete"))

    @retain_on_delete.setter
    def retain_on_delete(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c62290c7cff376845d83f4bc9713a5180f49f8a007b63841d6cd89f61a30520)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retainOnDelete", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4785c3d897cc882173c87a2ca3255389fa01cd6b5da7e9d815096a210d057b7f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d85f06a631beac96be0ccf53edff4bc69a098e97d828b1fbc861d925f26157f3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)

    @builtins.property
    @jsii.member(jsii_name="waitForDeployment")
    def wait_for_deployment(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "waitForDeployment"))

    @wait_for_deployment.setter
    def wait_for_deployment(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__597d7c165716fa2b78bff43446959882e34ad910d58716b3e062d0bbd5e6151c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "waitForDeployment", value)

    @builtins.property
    @jsii.member(jsii_name="webAclId")
    def web_acl_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "webAclId"))

    @web_acl_id.setter
    def web_acl_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45405caef5ded3a9f651185abec0c8ab174266ebeef752d10705431039715551)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "webAclId", value)


@jsii.data_type(
    jsii_type="aws.cloudfrontDistribution.CloudfrontDistributionConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "default_cache_behavior": "defaultCacheBehavior",
        "enabled": "enabled",
        "origin": "origin",
        "restrictions": "restrictions",
        "viewer_certificate": "viewerCertificate",
        "aliases": "aliases",
        "comment": "comment",
        "custom_error_response": "customErrorResponse",
        "default_root_object": "defaultRootObject",
        "http_version": "httpVersion",
        "id": "id",
        "is_ipv6_enabled": "isIpv6Enabled",
        "logging_config": "loggingConfig",
        "ordered_cache_behavior": "orderedCacheBehavior",
        "origin_group": "originGroup",
        "price_class": "priceClass",
        "retain_on_delete": "retainOnDelete",
        "tags": "tags",
        "tags_all": "tagsAll",
        "wait_for_deployment": "waitForDeployment",
        "web_acl_id": "webAclId",
    },
)
class CloudfrontDistributionConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        default_cache_behavior: typing.Union["CloudfrontDistributionDefaultCacheBehavior", typing.Dict[builtins.str, typing.Any]],
        enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        origin: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CloudfrontDistributionOrigin", typing.Dict[builtins.str, typing.Any]]]],
        restrictions: typing.Union["CloudfrontDistributionRestrictions", typing.Dict[builtins.str, typing.Any]],
        viewer_certificate: typing.Union["CloudfrontDistributionViewerCertificate", typing.Dict[builtins.str, typing.Any]],
        aliases: typing.Optional[typing.Sequence[builtins.str]] = None,
        comment: typing.Optional[builtins.str] = None,
        custom_error_response: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CloudfrontDistributionCustomErrorResponse", typing.Dict[builtins.str, typing.Any]]]]] = None,
        default_root_object: typing.Optional[builtins.str] = None,
        http_version: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        is_ipv6_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        logging_config: typing.Optional[typing.Union["CloudfrontDistributionLoggingConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        ordered_cache_behavior: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CloudfrontDistributionOrderedCacheBehavior", typing.Dict[builtins.str, typing.Any]]]]] = None,
        origin_group: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CloudfrontDistributionOriginGroup", typing.Dict[builtins.str, typing.Any]]]]] = None,
        price_class: typing.Optional[builtins.str] = None,
        retain_on_delete: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        wait_for_deployment: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        web_acl_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param default_cache_behavior: default_cache_behavior block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#default_cache_behavior CloudfrontDistribution#default_cache_behavior}
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#enabled CloudfrontDistribution#enabled}.
        :param origin: origin block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#origin CloudfrontDistribution#origin}
        :param restrictions: restrictions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#restrictions CloudfrontDistribution#restrictions}
        :param viewer_certificate: viewer_certificate block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#viewer_certificate CloudfrontDistribution#viewer_certificate}
        :param aliases: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#aliases CloudfrontDistribution#aliases}.
        :param comment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#comment CloudfrontDistribution#comment}.
        :param custom_error_response: custom_error_response block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#custom_error_response CloudfrontDistribution#custom_error_response}
        :param default_root_object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#default_root_object CloudfrontDistribution#default_root_object}.
        :param http_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#http_version CloudfrontDistribution#http_version}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#id CloudfrontDistribution#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param is_ipv6_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#is_ipv6_enabled CloudfrontDistribution#is_ipv6_enabled}.
        :param logging_config: logging_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#logging_config CloudfrontDistribution#logging_config}
        :param ordered_cache_behavior: ordered_cache_behavior block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#ordered_cache_behavior CloudfrontDistribution#ordered_cache_behavior}
        :param origin_group: origin_group block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#origin_group CloudfrontDistribution#origin_group}
        :param price_class: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#price_class CloudfrontDistribution#price_class}.
        :param retain_on_delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#retain_on_delete CloudfrontDistribution#retain_on_delete}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#tags CloudfrontDistribution#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#tags_all CloudfrontDistribution#tags_all}.
        :param wait_for_deployment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#wait_for_deployment CloudfrontDistribution#wait_for_deployment}.
        :param web_acl_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#web_acl_id CloudfrontDistribution#web_acl_id}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(default_cache_behavior, dict):
            default_cache_behavior = CloudfrontDistributionDefaultCacheBehavior(**default_cache_behavior)
        if isinstance(restrictions, dict):
            restrictions = CloudfrontDistributionRestrictions(**restrictions)
        if isinstance(viewer_certificate, dict):
            viewer_certificate = CloudfrontDistributionViewerCertificate(**viewer_certificate)
        if isinstance(logging_config, dict):
            logging_config = CloudfrontDistributionLoggingConfig(**logging_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__22bf645392d91cb4c77981819d1bebb3d1ebaf238096601338826e0f4dfe96d4)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument default_cache_behavior", value=default_cache_behavior, expected_type=type_hints["default_cache_behavior"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument origin", value=origin, expected_type=type_hints["origin"])
            check_type(argname="argument restrictions", value=restrictions, expected_type=type_hints["restrictions"])
            check_type(argname="argument viewer_certificate", value=viewer_certificate, expected_type=type_hints["viewer_certificate"])
            check_type(argname="argument aliases", value=aliases, expected_type=type_hints["aliases"])
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument custom_error_response", value=custom_error_response, expected_type=type_hints["custom_error_response"])
            check_type(argname="argument default_root_object", value=default_root_object, expected_type=type_hints["default_root_object"])
            check_type(argname="argument http_version", value=http_version, expected_type=type_hints["http_version"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument is_ipv6_enabled", value=is_ipv6_enabled, expected_type=type_hints["is_ipv6_enabled"])
            check_type(argname="argument logging_config", value=logging_config, expected_type=type_hints["logging_config"])
            check_type(argname="argument ordered_cache_behavior", value=ordered_cache_behavior, expected_type=type_hints["ordered_cache_behavior"])
            check_type(argname="argument origin_group", value=origin_group, expected_type=type_hints["origin_group"])
            check_type(argname="argument price_class", value=price_class, expected_type=type_hints["price_class"])
            check_type(argname="argument retain_on_delete", value=retain_on_delete, expected_type=type_hints["retain_on_delete"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument wait_for_deployment", value=wait_for_deployment, expected_type=type_hints["wait_for_deployment"])
            check_type(argname="argument web_acl_id", value=web_acl_id, expected_type=type_hints["web_acl_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "default_cache_behavior": default_cache_behavior,
            "enabled": enabled,
            "origin": origin,
            "restrictions": restrictions,
            "viewer_certificate": viewer_certificate,
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
        if aliases is not None:
            self._values["aliases"] = aliases
        if comment is not None:
            self._values["comment"] = comment
        if custom_error_response is not None:
            self._values["custom_error_response"] = custom_error_response
        if default_root_object is not None:
            self._values["default_root_object"] = default_root_object
        if http_version is not None:
            self._values["http_version"] = http_version
        if id is not None:
            self._values["id"] = id
        if is_ipv6_enabled is not None:
            self._values["is_ipv6_enabled"] = is_ipv6_enabled
        if logging_config is not None:
            self._values["logging_config"] = logging_config
        if ordered_cache_behavior is not None:
            self._values["ordered_cache_behavior"] = ordered_cache_behavior
        if origin_group is not None:
            self._values["origin_group"] = origin_group
        if price_class is not None:
            self._values["price_class"] = price_class
        if retain_on_delete is not None:
            self._values["retain_on_delete"] = retain_on_delete
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if wait_for_deployment is not None:
            self._values["wait_for_deployment"] = wait_for_deployment
        if web_acl_id is not None:
            self._values["web_acl_id"] = web_acl_id

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
    def default_cache_behavior(self) -> "CloudfrontDistributionDefaultCacheBehavior":
        '''default_cache_behavior block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#default_cache_behavior CloudfrontDistribution#default_cache_behavior}
        '''
        result = self._values.get("default_cache_behavior")
        assert result is not None, "Required property 'default_cache_behavior' is missing"
        return typing.cast("CloudfrontDistributionDefaultCacheBehavior", result)

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#enabled CloudfrontDistribution#enabled}.'''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    @builtins.property
    def origin(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CloudfrontDistributionOrigin"]]:
        '''origin block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#origin CloudfrontDistribution#origin}
        '''
        result = self._values.get("origin")
        assert result is not None, "Required property 'origin' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CloudfrontDistributionOrigin"]], result)

    @builtins.property
    def restrictions(self) -> "CloudfrontDistributionRestrictions":
        '''restrictions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#restrictions CloudfrontDistribution#restrictions}
        '''
        result = self._values.get("restrictions")
        assert result is not None, "Required property 'restrictions' is missing"
        return typing.cast("CloudfrontDistributionRestrictions", result)

    @builtins.property
    def viewer_certificate(self) -> "CloudfrontDistributionViewerCertificate":
        '''viewer_certificate block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#viewer_certificate CloudfrontDistribution#viewer_certificate}
        '''
        result = self._values.get("viewer_certificate")
        assert result is not None, "Required property 'viewer_certificate' is missing"
        return typing.cast("CloudfrontDistributionViewerCertificate", result)

    @builtins.property
    def aliases(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#aliases CloudfrontDistribution#aliases}.'''
        result = self._values.get("aliases")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#comment CloudfrontDistribution#comment}.'''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_error_response(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CloudfrontDistributionCustomErrorResponse"]]]:
        '''custom_error_response block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#custom_error_response CloudfrontDistribution#custom_error_response}
        '''
        result = self._values.get("custom_error_response")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CloudfrontDistributionCustomErrorResponse"]]], result)

    @builtins.property
    def default_root_object(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#default_root_object CloudfrontDistribution#default_root_object}.'''
        result = self._values.get("default_root_object")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def http_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#http_version CloudfrontDistribution#http_version}.'''
        result = self._values.get("http_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#id CloudfrontDistribution#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def is_ipv6_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#is_ipv6_enabled CloudfrontDistribution#is_ipv6_enabled}.'''
        result = self._values.get("is_ipv6_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def logging_config(self) -> typing.Optional["CloudfrontDistributionLoggingConfig"]:
        '''logging_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#logging_config CloudfrontDistribution#logging_config}
        '''
        result = self._values.get("logging_config")
        return typing.cast(typing.Optional["CloudfrontDistributionLoggingConfig"], result)

    @builtins.property
    def ordered_cache_behavior(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CloudfrontDistributionOrderedCacheBehavior"]]]:
        '''ordered_cache_behavior block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#ordered_cache_behavior CloudfrontDistribution#ordered_cache_behavior}
        '''
        result = self._values.get("ordered_cache_behavior")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CloudfrontDistributionOrderedCacheBehavior"]]], result)

    @builtins.property
    def origin_group(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CloudfrontDistributionOriginGroup"]]]:
        '''origin_group block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#origin_group CloudfrontDistribution#origin_group}
        '''
        result = self._values.get("origin_group")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CloudfrontDistributionOriginGroup"]]], result)

    @builtins.property
    def price_class(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#price_class CloudfrontDistribution#price_class}.'''
        result = self._values.get("price_class")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def retain_on_delete(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#retain_on_delete CloudfrontDistribution#retain_on_delete}.'''
        result = self._values.get("retain_on_delete")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#tags CloudfrontDistribution#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#tags_all CloudfrontDistribution#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def wait_for_deployment(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#wait_for_deployment CloudfrontDistribution#wait_for_deployment}.'''
        result = self._values.get("wait_for_deployment")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def web_acl_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#web_acl_id CloudfrontDistribution#web_acl_id}.'''
        result = self._values.get("web_acl_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudfrontDistributionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.cloudfrontDistribution.CloudfrontDistributionCustomErrorResponse",
    jsii_struct_bases=[],
    name_mapping={
        "error_code": "errorCode",
        "error_caching_min_ttl": "errorCachingMinTtl",
        "response_code": "responseCode",
        "response_page_path": "responsePagePath",
    },
)
class CloudfrontDistributionCustomErrorResponse:
    def __init__(
        self,
        *,
        error_code: jsii.Number,
        error_caching_min_ttl: typing.Optional[jsii.Number] = None,
        response_code: typing.Optional[jsii.Number] = None,
        response_page_path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param error_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#error_code CloudfrontDistribution#error_code}.
        :param error_caching_min_ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#error_caching_min_ttl CloudfrontDistribution#error_caching_min_ttl}.
        :param response_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#response_code CloudfrontDistribution#response_code}.
        :param response_page_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#response_page_path CloudfrontDistribution#response_page_path}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__daa368baa7d9046da2a0318670f62d735ea039b65bfbe1a2ae53bc84abc27956)
            check_type(argname="argument error_code", value=error_code, expected_type=type_hints["error_code"])
            check_type(argname="argument error_caching_min_ttl", value=error_caching_min_ttl, expected_type=type_hints["error_caching_min_ttl"])
            check_type(argname="argument response_code", value=response_code, expected_type=type_hints["response_code"])
            check_type(argname="argument response_page_path", value=response_page_path, expected_type=type_hints["response_page_path"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "error_code": error_code,
        }
        if error_caching_min_ttl is not None:
            self._values["error_caching_min_ttl"] = error_caching_min_ttl
        if response_code is not None:
            self._values["response_code"] = response_code
        if response_page_path is not None:
            self._values["response_page_path"] = response_page_path

    @builtins.property
    def error_code(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#error_code CloudfrontDistribution#error_code}.'''
        result = self._values.get("error_code")
        assert result is not None, "Required property 'error_code' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def error_caching_min_ttl(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#error_caching_min_ttl CloudfrontDistribution#error_caching_min_ttl}.'''
        result = self._values.get("error_caching_min_ttl")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def response_code(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#response_code CloudfrontDistribution#response_code}.'''
        result = self._values.get("response_code")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def response_page_path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#response_page_path CloudfrontDistribution#response_page_path}.'''
        result = self._values.get("response_page_path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudfrontDistributionCustomErrorResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudfrontDistributionCustomErrorResponseList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudfrontDistribution.CloudfrontDistributionCustomErrorResponseList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__633e263ac6985420932ddfd32bdd08a7087ee1794f804ab6db6677b28cde94f6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CloudfrontDistributionCustomErrorResponseOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80a8e9eb951084dacc5b0dfb269185f2d4a3f37db978cd586a1e62c770d83652)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CloudfrontDistributionCustomErrorResponseOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__adbe2a5fdeba767dd0290e74dd25b7655f597e934753a51ea210992a96176664)
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
            type_hints = typing.get_type_hints(_typecheckingstub__22c90344449458364212d5cc4e9d03a7ea020fc9ffa1dfcb2bfe82403955bcaa)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b35cc896b128e9b25b90a803bb1fc4a12fc1949d858f89aaeefbc2b0d09a919d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudfrontDistributionCustomErrorResponse]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudfrontDistributionCustomErrorResponse]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudfrontDistributionCustomErrorResponse]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a016707f9007118c8bda4ac7847108657f3ec01219ec97293a771ac56906f344)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CloudfrontDistributionCustomErrorResponseOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudfrontDistribution.CloudfrontDistributionCustomErrorResponseOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3606cb1226e879de02f613da9b68bb21e3467d459bc8909b0cf2cae9a89832bb)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetErrorCachingMinTtl")
    def reset_error_caching_min_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetErrorCachingMinTtl", []))

    @jsii.member(jsii_name="resetResponseCode")
    def reset_response_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResponseCode", []))

    @jsii.member(jsii_name="resetResponsePagePath")
    def reset_response_page_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResponsePagePath", []))

    @builtins.property
    @jsii.member(jsii_name="errorCachingMinTtlInput")
    def error_caching_min_ttl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "errorCachingMinTtlInput"))

    @builtins.property
    @jsii.member(jsii_name="errorCodeInput")
    def error_code_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "errorCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="responseCodeInput")
    def response_code_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "responseCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="responsePagePathInput")
    def response_page_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "responsePagePathInput"))

    @builtins.property
    @jsii.member(jsii_name="errorCachingMinTtl")
    def error_caching_min_ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "errorCachingMinTtl"))

    @error_caching_min_ttl.setter
    def error_caching_min_ttl(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bcfc25ebd380547c66edcbd48d677d01ae2404f5c3dd55089740e6de39dbf5c1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "errorCachingMinTtl", value)

    @builtins.property
    @jsii.member(jsii_name="errorCode")
    def error_code(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "errorCode"))

    @error_code.setter
    def error_code(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cad4122c69ea74c47c40234835ec0208af9072c04226fc043b490b6a2a139f85)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "errorCode", value)

    @builtins.property
    @jsii.member(jsii_name="responseCode")
    def response_code(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "responseCode"))

    @response_code.setter
    def response_code(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c84a9ed6d65aa0c5f503e9bf6e2b08f46a2128fd8c3020273e4be168655c87e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "responseCode", value)

    @builtins.property
    @jsii.member(jsii_name="responsePagePath")
    def response_page_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "responsePagePath"))

    @response_page_path.setter
    def response_page_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f2cb8e3054e49adb5871e1c95ad82e10f38ed1c3657f801cd54ad2ec805fe95)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "responsePagePath", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CloudfrontDistributionCustomErrorResponse, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CloudfrontDistributionCustomErrorResponse, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CloudfrontDistributionCustomErrorResponse, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82c48b1462e82b4ef78339473501af98133dbdde909f696164e9410121f1ff2f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.cloudfrontDistribution.CloudfrontDistributionDefaultCacheBehavior",
    jsii_struct_bases=[],
    name_mapping={
        "allowed_methods": "allowedMethods",
        "cached_methods": "cachedMethods",
        "target_origin_id": "targetOriginId",
        "viewer_protocol_policy": "viewerProtocolPolicy",
        "cache_policy_id": "cachePolicyId",
        "compress": "compress",
        "default_ttl": "defaultTtl",
        "field_level_encryption_id": "fieldLevelEncryptionId",
        "forwarded_values": "forwardedValues",
        "function_association": "functionAssociation",
        "lambda_function_association": "lambdaFunctionAssociation",
        "max_ttl": "maxTtl",
        "min_ttl": "minTtl",
        "origin_request_policy_id": "originRequestPolicyId",
        "realtime_log_config_arn": "realtimeLogConfigArn",
        "response_headers_policy_id": "responseHeadersPolicyId",
        "smooth_streaming": "smoothStreaming",
        "trusted_key_groups": "trustedKeyGroups",
        "trusted_signers": "trustedSigners",
    },
)
class CloudfrontDistributionDefaultCacheBehavior:
    def __init__(
        self,
        *,
        allowed_methods: typing.Sequence[builtins.str],
        cached_methods: typing.Sequence[builtins.str],
        target_origin_id: builtins.str,
        viewer_protocol_policy: builtins.str,
        cache_policy_id: typing.Optional[builtins.str] = None,
        compress: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        default_ttl: typing.Optional[jsii.Number] = None,
        field_level_encryption_id: typing.Optional[builtins.str] = None,
        forwarded_values: typing.Optional[typing.Union["CloudfrontDistributionDefaultCacheBehaviorForwardedValues", typing.Dict[builtins.str, typing.Any]]] = None,
        function_association: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CloudfrontDistributionDefaultCacheBehaviorFunctionAssociation", typing.Dict[builtins.str, typing.Any]]]]] = None,
        lambda_function_association: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CloudfrontDistributionDefaultCacheBehaviorLambdaFunctionAssociation", typing.Dict[builtins.str, typing.Any]]]]] = None,
        max_ttl: typing.Optional[jsii.Number] = None,
        min_ttl: typing.Optional[jsii.Number] = None,
        origin_request_policy_id: typing.Optional[builtins.str] = None,
        realtime_log_config_arn: typing.Optional[builtins.str] = None,
        response_headers_policy_id: typing.Optional[builtins.str] = None,
        smooth_streaming: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        trusted_key_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        trusted_signers: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param allowed_methods: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#allowed_methods CloudfrontDistribution#allowed_methods}.
        :param cached_methods: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#cached_methods CloudfrontDistribution#cached_methods}.
        :param target_origin_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#target_origin_id CloudfrontDistribution#target_origin_id}.
        :param viewer_protocol_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#viewer_protocol_policy CloudfrontDistribution#viewer_protocol_policy}.
        :param cache_policy_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#cache_policy_id CloudfrontDistribution#cache_policy_id}.
        :param compress: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#compress CloudfrontDistribution#compress}.
        :param default_ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#default_ttl CloudfrontDistribution#default_ttl}.
        :param field_level_encryption_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#field_level_encryption_id CloudfrontDistribution#field_level_encryption_id}.
        :param forwarded_values: forwarded_values block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#forwarded_values CloudfrontDistribution#forwarded_values}
        :param function_association: function_association block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#function_association CloudfrontDistribution#function_association}
        :param lambda_function_association: lambda_function_association block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#lambda_function_association CloudfrontDistribution#lambda_function_association}
        :param max_ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#max_ttl CloudfrontDistribution#max_ttl}.
        :param min_ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#min_ttl CloudfrontDistribution#min_ttl}.
        :param origin_request_policy_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#origin_request_policy_id CloudfrontDistribution#origin_request_policy_id}.
        :param realtime_log_config_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#realtime_log_config_arn CloudfrontDistribution#realtime_log_config_arn}.
        :param response_headers_policy_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#response_headers_policy_id CloudfrontDistribution#response_headers_policy_id}.
        :param smooth_streaming: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#smooth_streaming CloudfrontDistribution#smooth_streaming}.
        :param trusted_key_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#trusted_key_groups CloudfrontDistribution#trusted_key_groups}.
        :param trusted_signers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#trusted_signers CloudfrontDistribution#trusted_signers}.
        '''
        if isinstance(forwarded_values, dict):
            forwarded_values = CloudfrontDistributionDefaultCacheBehaviorForwardedValues(**forwarded_values)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f7ce19f434f14df24b5610bb2a84ca6e6b1e4b5d7c563fc1bd58897fff4a7c18)
            check_type(argname="argument allowed_methods", value=allowed_methods, expected_type=type_hints["allowed_methods"])
            check_type(argname="argument cached_methods", value=cached_methods, expected_type=type_hints["cached_methods"])
            check_type(argname="argument target_origin_id", value=target_origin_id, expected_type=type_hints["target_origin_id"])
            check_type(argname="argument viewer_protocol_policy", value=viewer_protocol_policy, expected_type=type_hints["viewer_protocol_policy"])
            check_type(argname="argument cache_policy_id", value=cache_policy_id, expected_type=type_hints["cache_policy_id"])
            check_type(argname="argument compress", value=compress, expected_type=type_hints["compress"])
            check_type(argname="argument default_ttl", value=default_ttl, expected_type=type_hints["default_ttl"])
            check_type(argname="argument field_level_encryption_id", value=field_level_encryption_id, expected_type=type_hints["field_level_encryption_id"])
            check_type(argname="argument forwarded_values", value=forwarded_values, expected_type=type_hints["forwarded_values"])
            check_type(argname="argument function_association", value=function_association, expected_type=type_hints["function_association"])
            check_type(argname="argument lambda_function_association", value=lambda_function_association, expected_type=type_hints["lambda_function_association"])
            check_type(argname="argument max_ttl", value=max_ttl, expected_type=type_hints["max_ttl"])
            check_type(argname="argument min_ttl", value=min_ttl, expected_type=type_hints["min_ttl"])
            check_type(argname="argument origin_request_policy_id", value=origin_request_policy_id, expected_type=type_hints["origin_request_policy_id"])
            check_type(argname="argument realtime_log_config_arn", value=realtime_log_config_arn, expected_type=type_hints["realtime_log_config_arn"])
            check_type(argname="argument response_headers_policy_id", value=response_headers_policy_id, expected_type=type_hints["response_headers_policy_id"])
            check_type(argname="argument smooth_streaming", value=smooth_streaming, expected_type=type_hints["smooth_streaming"])
            check_type(argname="argument trusted_key_groups", value=trusted_key_groups, expected_type=type_hints["trusted_key_groups"])
            check_type(argname="argument trusted_signers", value=trusted_signers, expected_type=type_hints["trusted_signers"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "allowed_methods": allowed_methods,
            "cached_methods": cached_methods,
            "target_origin_id": target_origin_id,
            "viewer_protocol_policy": viewer_protocol_policy,
        }
        if cache_policy_id is not None:
            self._values["cache_policy_id"] = cache_policy_id
        if compress is not None:
            self._values["compress"] = compress
        if default_ttl is not None:
            self._values["default_ttl"] = default_ttl
        if field_level_encryption_id is not None:
            self._values["field_level_encryption_id"] = field_level_encryption_id
        if forwarded_values is not None:
            self._values["forwarded_values"] = forwarded_values
        if function_association is not None:
            self._values["function_association"] = function_association
        if lambda_function_association is not None:
            self._values["lambda_function_association"] = lambda_function_association
        if max_ttl is not None:
            self._values["max_ttl"] = max_ttl
        if min_ttl is not None:
            self._values["min_ttl"] = min_ttl
        if origin_request_policy_id is not None:
            self._values["origin_request_policy_id"] = origin_request_policy_id
        if realtime_log_config_arn is not None:
            self._values["realtime_log_config_arn"] = realtime_log_config_arn
        if response_headers_policy_id is not None:
            self._values["response_headers_policy_id"] = response_headers_policy_id
        if smooth_streaming is not None:
            self._values["smooth_streaming"] = smooth_streaming
        if trusted_key_groups is not None:
            self._values["trusted_key_groups"] = trusted_key_groups
        if trusted_signers is not None:
            self._values["trusted_signers"] = trusted_signers

    @builtins.property
    def allowed_methods(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#allowed_methods CloudfrontDistribution#allowed_methods}.'''
        result = self._values.get("allowed_methods")
        assert result is not None, "Required property 'allowed_methods' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def cached_methods(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#cached_methods CloudfrontDistribution#cached_methods}.'''
        result = self._values.get("cached_methods")
        assert result is not None, "Required property 'cached_methods' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def target_origin_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#target_origin_id CloudfrontDistribution#target_origin_id}.'''
        result = self._values.get("target_origin_id")
        assert result is not None, "Required property 'target_origin_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def viewer_protocol_policy(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#viewer_protocol_policy CloudfrontDistribution#viewer_protocol_policy}.'''
        result = self._values.get("viewer_protocol_policy")
        assert result is not None, "Required property 'viewer_protocol_policy' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cache_policy_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#cache_policy_id CloudfrontDistribution#cache_policy_id}.'''
        result = self._values.get("cache_policy_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def compress(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#compress CloudfrontDistribution#compress}.'''
        result = self._values.get("compress")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def default_ttl(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#default_ttl CloudfrontDistribution#default_ttl}.'''
        result = self._values.get("default_ttl")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def field_level_encryption_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#field_level_encryption_id CloudfrontDistribution#field_level_encryption_id}.'''
        result = self._values.get("field_level_encryption_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def forwarded_values(
        self,
    ) -> typing.Optional["CloudfrontDistributionDefaultCacheBehaviorForwardedValues"]:
        '''forwarded_values block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#forwarded_values CloudfrontDistribution#forwarded_values}
        '''
        result = self._values.get("forwarded_values")
        return typing.cast(typing.Optional["CloudfrontDistributionDefaultCacheBehaviorForwardedValues"], result)

    @builtins.property
    def function_association(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CloudfrontDistributionDefaultCacheBehaviorFunctionAssociation"]]]:
        '''function_association block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#function_association CloudfrontDistribution#function_association}
        '''
        result = self._values.get("function_association")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CloudfrontDistributionDefaultCacheBehaviorFunctionAssociation"]]], result)

    @builtins.property
    def lambda_function_association(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CloudfrontDistributionDefaultCacheBehaviorLambdaFunctionAssociation"]]]:
        '''lambda_function_association block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#lambda_function_association CloudfrontDistribution#lambda_function_association}
        '''
        result = self._values.get("lambda_function_association")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CloudfrontDistributionDefaultCacheBehaviorLambdaFunctionAssociation"]]], result)

    @builtins.property
    def max_ttl(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#max_ttl CloudfrontDistribution#max_ttl}.'''
        result = self._values.get("max_ttl")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_ttl(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#min_ttl CloudfrontDistribution#min_ttl}.'''
        result = self._values.get("min_ttl")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def origin_request_policy_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#origin_request_policy_id CloudfrontDistribution#origin_request_policy_id}.'''
        result = self._values.get("origin_request_policy_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def realtime_log_config_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#realtime_log_config_arn CloudfrontDistribution#realtime_log_config_arn}.'''
        result = self._values.get("realtime_log_config_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def response_headers_policy_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#response_headers_policy_id CloudfrontDistribution#response_headers_policy_id}.'''
        result = self._values.get("response_headers_policy_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def smooth_streaming(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#smooth_streaming CloudfrontDistribution#smooth_streaming}.'''
        result = self._values.get("smooth_streaming")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def trusted_key_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#trusted_key_groups CloudfrontDistribution#trusted_key_groups}.'''
        result = self._values.get("trusted_key_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def trusted_signers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#trusted_signers CloudfrontDistribution#trusted_signers}.'''
        result = self._values.get("trusted_signers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudfrontDistributionDefaultCacheBehavior(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.cloudfrontDistribution.CloudfrontDistributionDefaultCacheBehaviorForwardedValues",
    jsii_struct_bases=[],
    name_mapping={
        "cookies": "cookies",
        "query_string": "queryString",
        "headers": "headers",
        "query_string_cache_keys": "queryStringCacheKeys",
    },
)
class CloudfrontDistributionDefaultCacheBehaviorForwardedValues:
    def __init__(
        self,
        *,
        cookies: typing.Union["CloudfrontDistributionDefaultCacheBehaviorForwardedValuesCookies", typing.Dict[builtins.str, typing.Any]],
        query_string: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        headers: typing.Optional[typing.Sequence[builtins.str]] = None,
        query_string_cache_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param cookies: cookies block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#cookies CloudfrontDistribution#cookies}
        :param query_string: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#query_string CloudfrontDistribution#query_string}.
        :param headers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#headers CloudfrontDistribution#headers}.
        :param query_string_cache_keys: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#query_string_cache_keys CloudfrontDistribution#query_string_cache_keys}.
        '''
        if isinstance(cookies, dict):
            cookies = CloudfrontDistributionDefaultCacheBehaviorForwardedValuesCookies(**cookies)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32c0244c6329ab1f5bd1778295ea5772539953da641f2c3bfdfa424e8380a63d)
            check_type(argname="argument cookies", value=cookies, expected_type=type_hints["cookies"])
            check_type(argname="argument query_string", value=query_string, expected_type=type_hints["query_string"])
            check_type(argname="argument headers", value=headers, expected_type=type_hints["headers"])
            check_type(argname="argument query_string_cache_keys", value=query_string_cache_keys, expected_type=type_hints["query_string_cache_keys"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cookies": cookies,
            "query_string": query_string,
        }
        if headers is not None:
            self._values["headers"] = headers
        if query_string_cache_keys is not None:
            self._values["query_string_cache_keys"] = query_string_cache_keys

    @builtins.property
    def cookies(
        self,
    ) -> "CloudfrontDistributionDefaultCacheBehaviorForwardedValuesCookies":
        '''cookies block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#cookies CloudfrontDistribution#cookies}
        '''
        result = self._values.get("cookies")
        assert result is not None, "Required property 'cookies' is missing"
        return typing.cast("CloudfrontDistributionDefaultCacheBehaviorForwardedValuesCookies", result)

    @builtins.property
    def query_string(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#query_string CloudfrontDistribution#query_string}.'''
        result = self._values.get("query_string")
        assert result is not None, "Required property 'query_string' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    @builtins.property
    def headers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#headers CloudfrontDistribution#headers}.'''
        result = self._values.get("headers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def query_string_cache_keys(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#query_string_cache_keys CloudfrontDistribution#query_string_cache_keys}.'''
        result = self._values.get("query_string_cache_keys")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudfrontDistributionDefaultCacheBehaviorForwardedValues(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.cloudfrontDistribution.CloudfrontDistributionDefaultCacheBehaviorForwardedValuesCookies",
    jsii_struct_bases=[],
    name_mapping={"forward": "forward", "whitelisted_names": "whitelistedNames"},
)
class CloudfrontDistributionDefaultCacheBehaviorForwardedValuesCookies:
    def __init__(
        self,
        *,
        forward: builtins.str,
        whitelisted_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param forward: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#forward CloudfrontDistribution#forward}.
        :param whitelisted_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#whitelisted_names CloudfrontDistribution#whitelisted_names}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b9b5ee965da4e227472844199d0141043eeb43482ab93cbadfbb104429af0727)
            check_type(argname="argument forward", value=forward, expected_type=type_hints["forward"])
            check_type(argname="argument whitelisted_names", value=whitelisted_names, expected_type=type_hints["whitelisted_names"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "forward": forward,
        }
        if whitelisted_names is not None:
            self._values["whitelisted_names"] = whitelisted_names

    @builtins.property
    def forward(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#forward CloudfrontDistribution#forward}.'''
        result = self._values.get("forward")
        assert result is not None, "Required property 'forward' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def whitelisted_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#whitelisted_names CloudfrontDistribution#whitelisted_names}.'''
        result = self._values.get("whitelisted_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudfrontDistributionDefaultCacheBehaviorForwardedValuesCookies(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudfrontDistributionDefaultCacheBehaviorForwardedValuesCookiesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudfrontDistribution.CloudfrontDistributionDefaultCacheBehaviorForwardedValuesCookiesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8705ba1d7060c4304029e79ee5629d4c29844fc055923f83de2687ff83c12d27)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetWhitelistedNames")
    def reset_whitelisted_names(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWhitelistedNames", []))

    @builtins.property
    @jsii.member(jsii_name="forwardInput")
    def forward_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "forwardInput"))

    @builtins.property
    @jsii.member(jsii_name="whitelistedNamesInput")
    def whitelisted_names_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "whitelistedNamesInput"))

    @builtins.property
    @jsii.member(jsii_name="forward")
    def forward(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "forward"))

    @forward.setter
    def forward(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c40ad7ba30ed69132a8f85ae9c0a9ac178e4e06d9d9ad6fc78140ba72d142f52)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forward", value)

    @builtins.property
    @jsii.member(jsii_name="whitelistedNames")
    def whitelisted_names(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "whitelistedNames"))

    @whitelisted_names.setter
    def whitelisted_names(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba777e24aa27c1f34e6f04e8aeece19b53f7120b4a9267fdc8f8fce906f19926)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "whitelistedNames", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CloudfrontDistributionDefaultCacheBehaviorForwardedValuesCookies]:
        return typing.cast(typing.Optional[CloudfrontDistributionDefaultCacheBehaviorForwardedValuesCookies], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudfrontDistributionDefaultCacheBehaviorForwardedValuesCookies],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38ace5aea34273e6f8a19d7981ad49ca437ce8d2673ab5485468bc9c7cce30d5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CloudfrontDistributionDefaultCacheBehaviorForwardedValuesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudfrontDistribution.CloudfrontDistributionDefaultCacheBehaviorForwardedValuesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c2d80065eac04f24401c049629dbd5cd15498a04f1f808227a75e75f3150406f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCookies")
    def put_cookies(
        self,
        *,
        forward: builtins.str,
        whitelisted_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param forward: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#forward CloudfrontDistribution#forward}.
        :param whitelisted_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#whitelisted_names CloudfrontDistribution#whitelisted_names}.
        '''
        value = CloudfrontDistributionDefaultCacheBehaviorForwardedValuesCookies(
            forward=forward, whitelisted_names=whitelisted_names
        )

        return typing.cast(None, jsii.invoke(self, "putCookies", [value]))

    @jsii.member(jsii_name="resetHeaders")
    def reset_headers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeaders", []))

    @jsii.member(jsii_name="resetQueryStringCacheKeys")
    def reset_query_string_cache_keys(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueryStringCacheKeys", []))

    @builtins.property
    @jsii.member(jsii_name="cookies")
    def cookies(
        self,
    ) -> CloudfrontDistributionDefaultCacheBehaviorForwardedValuesCookiesOutputReference:
        return typing.cast(CloudfrontDistributionDefaultCacheBehaviorForwardedValuesCookiesOutputReference, jsii.get(self, "cookies"))

    @builtins.property
    @jsii.member(jsii_name="cookiesInput")
    def cookies_input(
        self,
    ) -> typing.Optional[CloudfrontDistributionDefaultCacheBehaviorForwardedValuesCookies]:
        return typing.cast(typing.Optional[CloudfrontDistributionDefaultCacheBehaviorForwardedValuesCookies], jsii.get(self, "cookiesInput"))

    @builtins.property
    @jsii.member(jsii_name="headersInput")
    def headers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "headersInput"))

    @builtins.property
    @jsii.member(jsii_name="queryStringCacheKeysInput")
    def query_string_cache_keys_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "queryStringCacheKeysInput"))

    @builtins.property
    @jsii.member(jsii_name="queryStringInput")
    def query_string_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "queryStringInput"))

    @builtins.property
    @jsii.member(jsii_name="headers")
    def headers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "headers"))

    @headers.setter
    def headers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__683c2cb22fef7d4e7fa7fdff30de52c8e0fcaad62678dad44ea0ce525991e660)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "headers", value)

    @builtins.property
    @jsii.member(jsii_name="queryString")
    def query_string(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "queryString"))

    @query_string.setter
    def query_string(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c93b43ac5303a4a811af6e2e2dd6d9e6c79abc601a537fe75115990c915d01d1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queryString", value)

    @builtins.property
    @jsii.member(jsii_name="queryStringCacheKeys")
    def query_string_cache_keys(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "queryStringCacheKeys"))

    @query_string_cache_keys.setter
    def query_string_cache_keys(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa6f87aee5ac0b42c0be6e87795bc9a5e93110cf28c217ab880a0c7c4fbc540d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queryStringCacheKeys", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CloudfrontDistributionDefaultCacheBehaviorForwardedValues]:
        return typing.cast(typing.Optional[CloudfrontDistributionDefaultCacheBehaviorForwardedValues], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudfrontDistributionDefaultCacheBehaviorForwardedValues],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__800fbd874547e66952cdf76101fbf23320360bf12bed45c73aea6c2b66701072)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.cloudfrontDistribution.CloudfrontDistributionDefaultCacheBehaviorFunctionAssociation",
    jsii_struct_bases=[],
    name_mapping={"event_type": "eventType", "function_arn": "functionArn"},
)
class CloudfrontDistributionDefaultCacheBehaviorFunctionAssociation:
    def __init__(self, *, event_type: builtins.str, function_arn: builtins.str) -> None:
        '''
        :param event_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#event_type CloudfrontDistribution#event_type}.
        :param function_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#function_arn CloudfrontDistribution#function_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fee9f2389b6cf80b8418d8dc60c8e04eeb057d4f34433f7e8e0f709481749f6e)
            check_type(argname="argument event_type", value=event_type, expected_type=type_hints["event_type"])
            check_type(argname="argument function_arn", value=function_arn, expected_type=type_hints["function_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "event_type": event_type,
            "function_arn": function_arn,
        }

    @builtins.property
    def event_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#event_type CloudfrontDistribution#event_type}.'''
        result = self._values.get("event_type")
        assert result is not None, "Required property 'event_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def function_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#function_arn CloudfrontDistribution#function_arn}.'''
        result = self._values.get("function_arn")
        assert result is not None, "Required property 'function_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudfrontDistributionDefaultCacheBehaviorFunctionAssociation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudfrontDistributionDefaultCacheBehaviorFunctionAssociationList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudfrontDistribution.CloudfrontDistributionDefaultCacheBehaviorFunctionAssociationList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9948262e42a36b73d14176c6f2c87df0163f57ddb4cb980e2aabada0bf295ffb)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CloudfrontDistributionDefaultCacheBehaviorFunctionAssociationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c883336c1dc2288f780e842b2f3705d642338b428f36ce9d45a66293c1cab63)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CloudfrontDistributionDefaultCacheBehaviorFunctionAssociationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e47a8408991769a1ab26a9adc0bdd50248fb139f4277cb12d581e3284df6bc72)
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
            type_hints = typing.get_type_hints(_typecheckingstub__23e71d29162584f4492089dd3d0b0dcc472cf93bcbf8cf378c217bf7c5d90241)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e05ad474fc839ecdf8c629f2e662ec1f727e2a5f544f6f78f3cae27f3f1a76f3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudfrontDistributionDefaultCacheBehaviorFunctionAssociation]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudfrontDistributionDefaultCacheBehaviorFunctionAssociation]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudfrontDistributionDefaultCacheBehaviorFunctionAssociation]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f065a66935b2d0edc4ee8fea733751fb8a1d1ad62e37d7dff1a2ce694b805c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CloudfrontDistributionDefaultCacheBehaviorFunctionAssociationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudfrontDistribution.CloudfrontDistributionDefaultCacheBehaviorFunctionAssociationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__99f4bfba5c044b8ee7010e7bb3ade131300a7c65032294cf012fafb3f28ccd63)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="eventTypeInput")
    def event_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "eventTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="functionArnInput")
    def function_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "functionArnInput"))

    @builtins.property
    @jsii.member(jsii_name="eventType")
    def event_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "eventType"))

    @event_type.setter
    def event_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7786aae39efd09cabf832eef0a97d397e35a58cfd7fed28f11e6e0112619108)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventType", value)

    @builtins.property
    @jsii.member(jsii_name="functionArn")
    def function_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "functionArn"))

    @function_arn.setter
    def function_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97bc4343d8812353cfce955215af54f5cf017c238fcf69dca5a5776a8773bfa3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "functionArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CloudfrontDistributionDefaultCacheBehaviorFunctionAssociation, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CloudfrontDistributionDefaultCacheBehaviorFunctionAssociation, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CloudfrontDistributionDefaultCacheBehaviorFunctionAssociation, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf906a49e43493df0484f58e3c77fb9d5f270137989e60b966ae21d0f7e903ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.cloudfrontDistribution.CloudfrontDistributionDefaultCacheBehaviorLambdaFunctionAssociation",
    jsii_struct_bases=[],
    name_mapping={
        "event_type": "eventType",
        "lambda_arn": "lambdaArn",
        "include_body": "includeBody",
    },
)
class CloudfrontDistributionDefaultCacheBehaviorLambdaFunctionAssociation:
    def __init__(
        self,
        *,
        event_type: builtins.str,
        lambda_arn: builtins.str,
        include_body: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param event_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#event_type CloudfrontDistribution#event_type}.
        :param lambda_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#lambda_arn CloudfrontDistribution#lambda_arn}.
        :param include_body: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#include_body CloudfrontDistribution#include_body}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f3472d6b8fe9ba0216ebbfdd868fbbbc07a33032238a98fd96ffd360b01c7fb7)
            check_type(argname="argument event_type", value=event_type, expected_type=type_hints["event_type"])
            check_type(argname="argument lambda_arn", value=lambda_arn, expected_type=type_hints["lambda_arn"])
            check_type(argname="argument include_body", value=include_body, expected_type=type_hints["include_body"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "event_type": event_type,
            "lambda_arn": lambda_arn,
        }
        if include_body is not None:
            self._values["include_body"] = include_body

    @builtins.property
    def event_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#event_type CloudfrontDistribution#event_type}.'''
        result = self._values.get("event_type")
        assert result is not None, "Required property 'event_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def lambda_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#lambda_arn CloudfrontDistribution#lambda_arn}.'''
        result = self._values.get("lambda_arn")
        assert result is not None, "Required property 'lambda_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def include_body(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#include_body CloudfrontDistribution#include_body}.'''
        result = self._values.get("include_body")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudfrontDistributionDefaultCacheBehaviorLambdaFunctionAssociation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudfrontDistributionDefaultCacheBehaviorLambdaFunctionAssociationList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudfrontDistribution.CloudfrontDistributionDefaultCacheBehaviorLambdaFunctionAssociationList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__bca0f1e0ec94d3a9ae48da3b8fab014eff80c84fe60d868bd02d42509e7178de)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CloudfrontDistributionDefaultCacheBehaviorLambdaFunctionAssociationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3876c9b5019a0d0d3eb0f24674bf0704fd35efec4545f3774e0aca7104d96fa6)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CloudfrontDistributionDefaultCacheBehaviorLambdaFunctionAssociationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b8e54f4abba733e387303b819a2f1c61e130d923b26c26b3b40508bfe9b7bc8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b9446a31b9454daa70b3a6f05491652cda2286d9c55ebeb7295bb33cf3638a6d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__98627b8809b90911ba9a2a274a5d274b928d42d8a3d2afd15d141b9f6482505a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudfrontDistributionDefaultCacheBehaviorLambdaFunctionAssociation]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudfrontDistributionDefaultCacheBehaviorLambdaFunctionAssociation]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudfrontDistributionDefaultCacheBehaviorLambdaFunctionAssociation]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__497b47d03e90006f00eeb2d7a1e68fa04177cea7f7cd6b81dd6228fad9231721)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CloudfrontDistributionDefaultCacheBehaviorLambdaFunctionAssociationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudfrontDistribution.CloudfrontDistributionDefaultCacheBehaviorLambdaFunctionAssociationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__fd37c7c646a342d806a8706e639b4f4440d6708c9b35564f56be1368a74c1226)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetIncludeBody")
    def reset_include_body(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludeBody", []))

    @builtins.property
    @jsii.member(jsii_name="eventTypeInput")
    def event_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "eventTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="includeBodyInput")
    def include_body_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "includeBodyInput"))

    @builtins.property
    @jsii.member(jsii_name="lambdaArnInput")
    def lambda_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lambdaArnInput"))

    @builtins.property
    @jsii.member(jsii_name="eventType")
    def event_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "eventType"))

    @event_type.setter
    def event_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5c2061a6228c62c5731d5298fbb0e76c52be091ee9ce92f0231f2d291a065c0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventType", value)

    @builtins.property
    @jsii.member(jsii_name="includeBody")
    def include_body(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "includeBody"))

    @include_body.setter
    def include_body(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d48c16f2981054966ad7cd99e5aa32c0cbcc638f6e09d44ffa33ab6e418fcb72)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includeBody", value)

    @builtins.property
    @jsii.member(jsii_name="lambdaArn")
    def lambda_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lambdaArn"))

    @lambda_arn.setter
    def lambda_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cabd54e303c6aaec377d106c71529e715a540bfe5d380ebc41c14635f422f733)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lambdaArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CloudfrontDistributionDefaultCacheBehaviorLambdaFunctionAssociation, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CloudfrontDistributionDefaultCacheBehaviorLambdaFunctionAssociation, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CloudfrontDistributionDefaultCacheBehaviorLambdaFunctionAssociation, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bfc00ee98b5222a310511df2428a280e3891053052850db39e11cadf8d8567dd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CloudfrontDistributionDefaultCacheBehaviorOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudfrontDistribution.CloudfrontDistributionDefaultCacheBehaviorOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__59b1bfb95cd89c4c42f0499aeb704e5126d23f3239ecdee8cebf41b73177ee40)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putForwardedValues")
    def put_forwarded_values(
        self,
        *,
        cookies: typing.Union[CloudfrontDistributionDefaultCacheBehaviorForwardedValuesCookies, typing.Dict[builtins.str, typing.Any]],
        query_string: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        headers: typing.Optional[typing.Sequence[builtins.str]] = None,
        query_string_cache_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param cookies: cookies block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#cookies CloudfrontDistribution#cookies}
        :param query_string: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#query_string CloudfrontDistribution#query_string}.
        :param headers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#headers CloudfrontDistribution#headers}.
        :param query_string_cache_keys: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#query_string_cache_keys CloudfrontDistribution#query_string_cache_keys}.
        '''
        value = CloudfrontDistributionDefaultCacheBehaviorForwardedValues(
            cookies=cookies,
            query_string=query_string,
            headers=headers,
            query_string_cache_keys=query_string_cache_keys,
        )

        return typing.cast(None, jsii.invoke(self, "putForwardedValues", [value]))

    @jsii.member(jsii_name="putFunctionAssociation")
    def put_function_association(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CloudfrontDistributionDefaultCacheBehaviorFunctionAssociation, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9229ffea0d2ddc99c8363ccf81572e056bd996192fd848e1bf2e4fc38cb0368f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putFunctionAssociation", [value]))

    @jsii.member(jsii_name="putLambdaFunctionAssociation")
    def put_lambda_function_association(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CloudfrontDistributionDefaultCacheBehaviorLambdaFunctionAssociation, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b9011554a08df3f7d6e8d0714e2bfbd8adeca2c6a861f5dfc2c203ae9f71dfd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLambdaFunctionAssociation", [value]))

    @jsii.member(jsii_name="resetCachePolicyId")
    def reset_cache_policy_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCachePolicyId", []))

    @jsii.member(jsii_name="resetCompress")
    def reset_compress(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCompress", []))

    @jsii.member(jsii_name="resetDefaultTtl")
    def reset_default_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultTtl", []))

    @jsii.member(jsii_name="resetFieldLevelEncryptionId")
    def reset_field_level_encryption_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFieldLevelEncryptionId", []))

    @jsii.member(jsii_name="resetForwardedValues")
    def reset_forwarded_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForwardedValues", []))

    @jsii.member(jsii_name="resetFunctionAssociation")
    def reset_function_association(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFunctionAssociation", []))

    @jsii.member(jsii_name="resetLambdaFunctionAssociation")
    def reset_lambda_function_association(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLambdaFunctionAssociation", []))

    @jsii.member(jsii_name="resetMaxTtl")
    def reset_max_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxTtl", []))

    @jsii.member(jsii_name="resetMinTtl")
    def reset_min_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinTtl", []))

    @jsii.member(jsii_name="resetOriginRequestPolicyId")
    def reset_origin_request_policy_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOriginRequestPolicyId", []))

    @jsii.member(jsii_name="resetRealtimeLogConfigArn")
    def reset_realtime_log_config_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRealtimeLogConfigArn", []))

    @jsii.member(jsii_name="resetResponseHeadersPolicyId")
    def reset_response_headers_policy_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResponseHeadersPolicyId", []))

    @jsii.member(jsii_name="resetSmoothStreaming")
    def reset_smooth_streaming(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSmoothStreaming", []))

    @jsii.member(jsii_name="resetTrustedKeyGroups")
    def reset_trusted_key_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTrustedKeyGroups", []))

    @jsii.member(jsii_name="resetTrustedSigners")
    def reset_trusted_signers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTrustedSigners", []))

    @builtins.property
    @jsii.member(jsii_name="forwardedValues")
    def forwarded_values(
        self,
    ) -> CloudfrontDistributionDefaultCacheBehaviorForwardedValuesOutputReference:
        return typing.cast(CloudfrontDistributionDefaultCacheBehaviorForwardedValuesOutputReference, jsii.get(self, "forwardedValues"))

    @builtins.property
    @jsii.member(jsii_name="functionAssociation")
    def function_association(
        self,
    ) -> CloudfrontDistributionDefaultCacheBehaviorFunctionAssociationList:
        return typing.cast(CloudfrontDistributionDefaultCacheBehaviorFunctionAssociationList, jsii.get(self, "functionAssociation"))

    @builtins.property
    @jsii.member(jsii_name="lambdaFunctionAssociation")
    def lambda_function_association(
        self,
    ) -> CloudfrontDistributionDefaultCacheBehaviorLambdaFunctionAssociationList:
        return typing.cast(CloudfrontDistributionDefaultCacheBehaviorLambdaFunctionAssociationList, jsii.get(self, "lambdaFunctionAssociation"))

    @builtins.property
    @jsii.member(jsii_name="allowedMethodsInput")
    def allowed_methods_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedMethodsInput"))

    @builtins.property
    @jsii.member(jsii_name="cachedMethodsInput")
    def cached_methods_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "cachedMethodsInput"))

    @builtins.property
    @jsii.member(jsii_name="cachePolicyIdInput")
    def cache_policy_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cachePolicyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="compressInput")
    def compress_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "compressInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultTtlInput")
    def default_ttl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "defaultTtlInput"))

    @builtins.property
    @jsii.member(jsii_name="fieldLevelEncryptionIdInput")
    def field_level_encryption_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fieldLevelEncryptionIdInput"))

    @builtins.property
    @jsii.member(jsii_name="forwardedValuesInput")
    def forwarded_values_input(
        self,
    ) -> typing.Optional[CloudfrontDistributionDefaultCacheBehaviorForwardedValues]:
        return typing.cast(typing.Optional[CloudfrontDistributionDefaultCacheBehaviorForwardedValues], jsii.get(self, "forwardedValuesInput"))

    @builtins.property
    @jsii.member(jsii_name="functionAssociationInput")
    def function_association_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudfrontDistributionDefaultCacheBehaviorFunctionAssociation]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudfrontDistributionDefaultCacheBehaviorFunctionAssociation]]], jsii.get(self, "functionAssociationInput"))

    @builtins.property
    @jsii.member(jsii_name="lambdaFunctionAssociationInput")
    def lambda_function_association_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudfrontDistributionDefaultCacheBehaviorLambdaFunctionAssociation]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudfrontDistributionDefaultCacheBehaviorLambdaFunctionAssociation]]], jsii.get(self, "lambdaFunctionAssociationInput"))

    @builtins.property
    @jsii.member(jsii_name="maxTtlInput")
    def max_ttl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxTtlInput"))

    @builtins.property
    @jsii.member(jsii_name="minTtlInput")
    def min_ttl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minTtlInput"))

    @builtins.property
    @jsii.member(jsii_name="originRequestPolicyIdInput")
    def origin_request_policy_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "originRequestPolicyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="realtimeLogConfigArnInput")
    def realtime_log_config_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "realtimeLogConfigArnInput"))

    @builtins.property
    @jsii.member(jsii_name="responseHeadersPolicyIdInput")
    def response_headers_policy_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "responseHeadersPolicyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="smoothStreamingInput")
    def smooth_streaming_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "smoothStreamingInput"))

    @builtins.property
    @jsii.member(jsii_name="targetOriginIdInput")
    def target_origin_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetOriginIdInput"))

    @builtins.property
    @jsii.member(jsii_name="trustedKeyGroupsInput")
    def trusted_key_groups_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "trustedKeyGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="trustedSignersInput")
    def trusted_signers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "trustedSignersInput"))

    @builtins.property
    @jsii.member(jsii_name="viewerProtocolPolicyInput")
    def viewer_protocol_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "viewerProtocolPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedMethods")
    def allowed_methods(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedMethods"))

    @allowed_methods.setter
    def allowed_methods(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c972c76f72ad2b1c60863449078a064430ebe9865d003833693117246b6f1caf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedMethods", value)

    @builtins.property
    @jsii.member(jsii_name="cachedMethods")
    def cached_methods(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "cachedMethods"))

    @cached_methods.setter
    def cached_methods(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3dcfe43aa61805a48eb996e90f5e1a55655d0fab89694570d38681a1eb3cee3b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cachedMethods", value)

    @builtins.property
    @jsii.member(jsii_name="cachePolicyId")
    def cache_policy_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cachePolicyId"))

    @cache_policy_id.setter
    def cache_policy_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb16eeceb7f614e206be080d90cbc9ac1130decee370919f637850eaf877a9ca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cachePolicyId", value)

    @builtins.property
    @jsii.member(jsii_name="compress")
    def compress(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "compress"))

    @compress.setter
    def compress(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f41a048dd0752bd0b972efc840edf65f00973f95e3a906a589bce6332f332f54)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "compress", value)

    @builtins.property
    @jsii.member(jsii_name="defaultTtl")
    def default_ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "defaultTtl"))

    @default_ttl.setter
    def default_ttl(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04e628a96879405c6487ca5cfeb96ff564f2c7d3dbc9a93775220b048280f085)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultTtl", value)

    @builtins.property
    @jsii.member(jsii_name="fieldLevelEncryptionId")
    def field_level_encryption_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fieldLevelEncryptionId"))

    @field_level_encryption_id.setter
    def field_level_encryption_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68e92d6ac6a6a77b67a88ea5263c47bf66611f89a3bdddafee0a86a50a426117)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fieldLevelEncryptionId", value)

    @builtins.property
    @jsii.member(jsii_name="maxTtl")
    def max_ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxTtl"))

    @max_ttl.setter
    def max_ttl(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70272ab108bf356b355081a53010a28ebfec499acc2bb9df4d44fc8492292146)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxTtl", value)

    @builtins.property
    @jsii.member(jsii_name="minTtl")
    def min_ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minTtl"))

    @min_ttl.setter
    def min_ttl(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6f3886a15ea4e4de36f6ebd4d41b63646438e841f99ee30eb2fcb722349d815)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minTtl", value)

    @builtins.property
    @jsii.member(jsii_name="originRequestPolicyId")
    def origin_request_policy_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "originRequestPolicyId"))

    @origin_request_policy_id.setter
    def origin_request_policy_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__199c533f5182a780a9c29a44a6f1872b1dd552ca28902e38a5bbdac018664a43)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "originRequestPolicyId", value)

    @builtins.property
    @jsii.member(jsii_name="realtimeLogConfigArn")
    def realtime_log_config_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "realtimeLogConfigArn"))

    @realtime_log_config_arn.setter
    def realtime_log_config_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b6c913fa81a523bc5a73637d1d0016d7552f1de6bbf15f49ad92e4e5ab3a3ef4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "realtimeLogConfigArn", value)

    @builtins.property
    @jsii.member(jsii_name="responseHeadersPolicyId")
    def response_headers_policy_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "responseHeadersPolicyId"))

    @response_headers_policy_id.setter
    def response_headers_policy_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dca01e70bd2c85ffa4d2cd82feff88bf32384068f736e34a9e4062dad8b9b137)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "responseHeadersPolicyId", value)

    @builtins.property
    @jsii.member(jsii_name="smoothStreaming")
    def smooth_streaming(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "smoothStreaming"))

    @smooth_streaming.setter
    def smooth_streaming(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc38bc2a8b9ad56990e02427ce6302654c99514bfb230523d404369570cd69de)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "smoothStreaming", value)

    @builtins.property
    @jsii.member(jsii_name="targetOriginId")
    def target_origin_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetOriginId"))

    @target_origin_id.setter
    def target_origin_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd1240d7f89ec6ff3ae288a7ff5e5eaebf82cbccb39290c50ffe62292288867e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetOriginId", value)

    @builtins.property
    @jsii.member(jsii_name="trustedKeyGroups")
    def trusted_key_groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "trustedKeyGroups"))

    @trusted_key_groups.setter
    def trusted_key_groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b11a5b95dbb82269d872958247dca536ea4876e1ed306df90cf72b40f8d786f0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "trustedKeyGroups", value)

    @builtins.property
    @jsii.member(jsii_name="trustedSigners")
    def trusted_signers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "trustedSigners"))

    @trusted_signers.setter
    def trusted_signers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5afa0606b4cb75e58cfb7d73f787294fced8b9c74e6ec8d4efab7941359a47c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "trustedSigners", value)

    @builtins.property
    @jsii.member(jsii_name="viewerProtocolPolicy")
    def viewer_protocol_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "viewerProtocolPolicy"))

    @viewer_protocol_policy.setter
    def viewer_protocol_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68316f637f40dc4555d8746e4dd55a761af563405b58babab846cd3fdb457372)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "viewerProtocolPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CloudfrontDistributionDefaultCacheBehavior]:
        return typing.cast(typing.Optional[CloudfrontDistributionDefaultCacheBehavior], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudfrontDistributionDefaultCacheBehavior],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04828e2fa534f1bf31ef620ebeaee1fd2b1b5d3f32d446b92e65853f143b3665)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.cloudfrontDistribution.CloudfrontDistributionLoggingConfig",
    jsii_struct_bases=[],
    name_mapping={
        "bucket": "bucket",
        "include_cookies": "includeCookies",
        "prefix": "prefix",
    },
)
class CloudfrontDistributionLoggingConfig:
    def __init__(
        self,
        *,
        bucket: builtins.str,
        include_cookies: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#bucket CloudfrontDistribution#bucket}.
        :param include_cookies: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#include_cookies CloudfrontDistribution#include_cookies}.
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#prefix CloudfrontDistribution#prefix}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12d2ca1030ac013f6642613003d9f796dd82c8935f5565affcde5865574653f0)
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument include_cookies", value=include_cookies, expected_type=type_hints["include_cookies"])
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bucket": bucket,
        }
        if include_cookies is not None:
            self._values["include_cookies"] = include_cookies
        if prefix is not None:
            self._values["prefix"] = prefix

    @builtins.property
    def bucket(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#bucket CloudfrontDistribution#bucket}.'''
        result = self._values.get("bucket")
        assert result is not None, "Required property 'bucket' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def include_cookies(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#include_cookies CloudfrontDistribution#include_cookies}.'''
        result = self._values.get("include_cookies")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#prefix CloudfrontDistribution#prefix}.'''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudfrontDistributionLoggingConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudfrontDistributionLoggingConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudfrontDistribution.CloudfrontDistributionLoggingConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f860702edbfe54150a805805bf7958bd96e6ccad1e2a0343352923887b663ff9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetIncludeCookies")
    def reset_include_cookies(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludeCookies", []))

    @jsii.member(jsii_name="resetPrefix")
    def reset_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrefix", []))

    @builtins.property
    @jsii.member(jsii_name="bucketInput")
    def bucket_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketInput"))

    @builtins.property
    @jsii.member(jsii_name="includeCookiesInput")
    def include_cookies_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "includeCookiesInput"))

    @builtins.property
    @jsii.member(jsii_name="prefixInput")
    def prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefixInput"))

    @builtins.property
    @jsii.member(jsii_name="bucket")
    def bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucket"))

    @bucket.setter
    def bucket(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b76c85551bf1475d28b7442c5ac982e34052688204cd817fecacedf7d83808e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucket", value)

    @builtins.property
    @jsii.member(jsii_name="includeCookies")
    def include_cookies(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "includeCookies"))

    @include_cookies.setter
    def include_cookies(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9534feae03baecef18168a317cd83aa1e87bb3277fbf3275ef7a68873b74cd71)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includeCookies", value)

    @builtins.property
    @jsii.member(jsii_name="prefix")
    def prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prefix"))

    @prefix.setter
    def prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d63fdbb6ecf89c5d1656967a835d030547a0e7c080edd0df6b847400727e0a3a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefix", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudfrontDistributionLoggingConfig]:
        return typing.cast(typing.Optional[CloudfrontDistributionLoggingConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudfrontDistributionLoggingConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4caff979ef0377faebca058a139f1bc8fd1a184b56820772d3271c03382cf2bd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.cloudfrontDistribution.CloudfrontDistributionOrderedCacheBehavior",
    jsii_struct_bases=[],
    name_mapping={
        "allowed_methods": "allowedMethods",
        "cached_methods": "cachedMethods",
        "path_pattern": "pathPattern",
        "target_origin_id": "targetOriginId",
        "viewer_protocol_policy": "viewerProtocolPolicy",
        "cache_policy_id": "cachePolicyId",
        "compress": "compress",
        "default_ttl": "defaultTtl",
        "field_level_encryption_id": "fieldLevelEncryptionId",
        "forwarded_values": "forwardedValues",
        "function_association": "functionAssociation",
        "lambda_function_association": "lambdaFunctionAssociation",
        "max_ttl": "maxTtl",
        "min_ttl": "minTtl",
        "origin_request_policy_id": "originRequestPolicyId",
        "realtime_log_config_arn": "realtimeLogConfigArn",
        "response_headers_policy_id": "responseHeadersPolicyId",
        "smooth_streaming": "smoothStreaming",
        "trusted_key_groups": "trustedKeyGroups",
        "trusted_signers": "trustedSigners",
    },
)
class CloudfrontDistributionOrderedCacheBehavior:
    def __init__(
        self,
        *,
        allowed_methods: typing.Sequence[builtins.str],
        cached_methods: typing.Sequence[builtins.str],
        path_pattern: builtins.str,
        target_origin_id: builtins.str,
        viewer_protocol_policy: builtins.str,
        cache_policy_id: typing.Optional[builtins.str] = None,
        compress: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        default_ttl: typing.Optional[jsii.Number] = None,
        field_level_encryption_id: typing.Optional[builtins.str] = None,
        forwarded_values: typing.Optional[typing.Union["CloudfrontDistributionOrderedCacheBehaviorForwardedValues", typing.Dict[builtins.str, typing.Any]]] = None,
        function_association: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CloudfrontDistributionOrderedCacheBehaviorFunctionAssociation", typing.Dict[builtins.str, typing.Any]]]]] = None,
        lambda_function_association: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CloudfrontDistributionOrderedCacheBehaviorLambdaFunctionAssociation", typing.Dict[builtins.str, typing.Any]]]]] = None,
        max_ttl: typing.Optional[jsii.Number] = None,
        min_ttl: typing.Optional[jsii.Number] = None,
        origin_request_policy_id: typing.Optional[builtins.str] = None,
        realtime_log_config_arn: typing.Optional[builtins.str] = None,
        response_headers_policy_id: typing.Optional[builtins.str] = None,
        smooth_streaming: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        trusted_key_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        trusted_signers: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param allowed_methods: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#allowed_methods CloudfrontDistribution#allowed_methods}.
        :param cached_methods: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#cached_methods CloudfrontDistribution#cached_methods}.
        :param path_pattern: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#path_pattern CloudfrontDistribution#path_pattern}.
        :param target_origin_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#target_origin_id CloudfrontDistribution#target_origin_id}.
        :param viewer_protocol_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#viewer_protocol_policy CloudfrontDistribution#viewer_protocol_policy}.
        :param cache_policy_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#cache_policy_id CloudfrontDistribution#cache_policy_id}.
        :param compress: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#compress CloudfrontDistribution#compress}.
        :param default_ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#default_ttl CloudfrontDistribution#default_ttl}.
        :param field_level_encryption_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#field_level_encryption_id CloudfrontDistribution#field_level_encryption_id}.
        :param forwarded_values: forwarded_values block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#forwarded_values CloudfrontDistribution#forwarded_values}
        :param function_association: function_association block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#function_association CloudfrontDistribution#function_association}
        :param lambda_function_association: lambda_function_association block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#lambda_function_association CloudfrontDistribution#lambda_function_association}
        :param max_ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#max_ttl CloudfrontDistribution#max_ttl}.
        :param min_ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#min_ttl CloudfrontDistribution#min_ttl}.
        :param origin_request_policy_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#origin_request_policy_id CloudfrontDistribution#origin_request_policy_id}.
        :param realtime_log_config_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#realtime_log_config_arn CloudfrontDistribution#realtime_log_config_arn}.
        :param response_headers_policy_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#response_headers_policy_id CloudfrontDistribution#response_headers_policy_id}.
        :param smooth_streaming: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#smooth_streaming CloudfrontDistribution#smooth_streaming}.
        :param trusted_key_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#trusted_key_groups CloudfrontDistribution#trusted_key_groups}.
        :param trusted_signers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#trusted_signers CloudfrontDistribution#trusted_signers}.
        '''
        if isinstance(forwarded_values, dict):
            forwarded_values = CloudfrontDistributionOrderedCacheBehaviorForwardedValues(**forwarded_values)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e273b6f1df93b6d65a5092b6435802b9966220740c99956a848379fcfa6e45d)
            check_type(argname="argument allowed_methods", value=allowed_methods, expected_type=type_hints["allowed_methods"])
            check_type(argname="argument cached_methods", value=cached_methods, expected_type=type_hints["cached_methods"])
            check_type(argname="argument path_pattern", value=path_pattern, expected_type=type_hints["path_pattern"])
            check_type(argname="argument target_origin_id", value=target_origin_id, expected_type=type_hints["target_origin_id"])
            check_type(argname="argument viewer_protocol_policy", value=viewer_protocol_policy, expected_type=type_hints["viewer_protocol_policy"])
            check_type(argname="argument cache_policy_id", value=cache_policy_id, expected_type=type_hints["cache_policy_id"])
            check_type(argname="argument compress", value=compress, expected_type=type_hints["compress"])
            check_type(argname="argument default_ttl", value=default_ttl, expected_type=type_hints["default_ttl"])
            check_type(argname="argument field_level_encryption_id", value=field_level_encryption_id, expected_type=type_hints["field_level_encryption_id"])
            check_type(argname="argument forwarded_values", value=forwarded_values, expected_type=type_hints["forwarded_values"])
            check_type(argname="argument function_association", value=function_association, expected_type=type_hints["function_association"])
            check_type(argname="argument lambda_function_association", value=lambda_function_association, expected_type=type_hints["lambda_function_association"])
            check_type(argname="argument max_ttl", value=max_ttl, expected_type=type_hints["max_ttl"])
            check_type(argname="argument min_ttl", value=min_ttl, expected_type=type_hints["min_ttl"])
            check_type(argname="argument origin_request_policy_id", value=origin_request_policy_id, expected_type=type_hints["origin_request_policy_id"])
            check_type(argname="argument realtime_log_config_arn", value=realtime_log_config_arn, expected_type=type_hints["realtime_log_config_arn"])
            check_type(argname="argument response_headers_policy_id", value=response_headers_policy_id, expected_type=type_hints["response_headers_policy_id"])
            check_type(argname="argument smooth_streaming", value=smooth_streaming, expected_type=type_hints["smooth_streaming"])
            check_type(argname="argument trusted_key_groups", value=trusted_key_groups, expected_type=type_hints["trusted_key_groups"])
            check_type(argname="argument trusted_signers", value=trusted_signers, expected_type=type_hints["trusted_signers"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "allowed_methods": allowed_methods,
            "cached_methods": cached_methods,
            "path_pattern": path_pattern,
            "target_origin_id": target_origin_id,
            "viewer_protocol_policy": viewer_protocol_policy,
        }
        if cache_policy_id is not None:
            self._values["cache_policy_id"] = cache_policy_id
        if compress is not None:
            self._values["compress"] = compress
        if default_ttl is not None:
            self._values["default_ttl"] = default_ttl
        if field_level_encryption_id is not None:
            self._values["field_level_encryption_id"] = field_level_encryption_id
        if forwarded_values is not None:
            self._values["forwarded_values"] = forwarded_values
        if function_association is not None:
            self._values["function_association"] = function_association
        if lambda_function_association is not None:
            self._values["lambda_function_association"] = lambda_function_association
        if max_ttl is not None:
            self._values["max_ttl"] = max_ttl
        if min_ttl is not None:
            self._values["min_ttl"] = min_ttl
        if origin_request_policy_id is not None:
            self._values["origin_request_policy_id"] = origin_request_policy_id
        if realtime_log_config_arn is not None:
            self._values["realtime_log_config_arn"] = realtime_log_config_arn
        if response_headers_policy_id is not None:
            self._values["response_headers_policy_id"] = response_headers_policy_id
        if smooth_streaming is not None:
            self._values["smooth_streaming"] = smooth_streaming
        if trusted_key_groups is not None:
            self._values["trusted_key_groups"] = trusted_key_groups
        if trusted_signers is not None:
            self._values["trusted_signers"] = trusted_signers

    @builtins.property
    def allowed_methods(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#allowed_methods CloudfrontDistribution#allowed_methods}.'''
        result = self._values.get("allowed_methods")
        assert result is not None, "Required property 'allowed_methods' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def cached_methods(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#cached_methods CloudfrontDistribution#cached_methods}.'''
        result = self._values.get("cached_methods")
        assert result is not None, "Required property 'cached_methods' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def path_pattern(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#path_pattern CloudfrontDistribution#path_pattern}.'''
        result = self._values.get("path_pattern")
        assert result is not None, "Required property 'path_pattern' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_origin_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#target_origin_id CloudfrontDistribution#target_origin_id}.'''
        result = self._values.get("target_origin_id")
        assert result is not None, "Required property 'target_origin_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def viewer_protocol_policy(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#viewer_protocol_policy CloudfrontDistribution#viewer_protocol_policy}.'''
        result = self._values.get("viewer_protocol_policy")
        assert result is not None, "Required property 'viewer_protocol_policy' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cache_policy_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#cache_policy_id CloudfrontDistribution#cache_policy_id}.'''
        result = self._values.get("cache_policy_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def compress(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#compress CloudfrontDistribution#compress}.'''
        result = self._values.get("compress")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def default_ttl(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#default_ttl CloudfrontDistribution#default_ttl}.'''
        result = self._values.get("default_ttl")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def field_level_encryption_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#field_level_encryption_id CloudfrontDistribution#field_level_encryption_id}.'''
        result = self._values.get("field_level_encryption_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def forwarded_values(
        self,
    ) -> typing.Optional["CloudfrontDistributionOrderedCacheBehaviorForwardedValues"]:
        '''forwarded_values block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#forwarded_values CloudfrontDistribution#forwarded_values}
        '''
        result = self._values.get("forwarded_values")
        return typing.cast(typing.Optional["CloudfrontDistributionOrderedCacheBehaviorForwardedValues"], result)

    @builtins.property
    def function_association(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CloudfrontDistributionOrderedCacheBehaviorFunctionAssociation"]]]:
        '''function_association block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#function_association CloudfrontDistribution#function_association}
        '''
        result = self._values.get("function_association")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CloudfrontDistributionOrderedCacheBehaviorFunctionAssociation"]]], result)

    @builtins.property
    def lambda_function_association(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CloudfrontDistributionOrderedCacheBehaviorLambdaFunctionAssociation"]]]:
        '''lambda_function_association block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#lambda_function_association CloudfrontDistribution#lambda_function_association}
        '''
        result = self._values.get("lambda_function_association")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CloudfrontDistributionOrderedCacheBehaviorLambdaFunctionAssociation"]]], result)

    @builtins.property
    def max_ttl(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#max_ttl CloudfrontDistribution#max_ttl}.'''
        result = self._values.get("max_ttl")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_ttl(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#min_ttl CloudfrontDistribution#min_ttl}.'''
        result = self._values.get("min_ttl")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def origin_request_policy_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#origin_request_policy_id CloudfrontDistribution#origin_request_policy_id}.'''
        result = self._values.get("origin_request_policy_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def realtime_log_config_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#realtime_log_config_arn CloudfrontDistribution#realtime_log_config_arn}.'''
        result = self._values.get("realtime_log_config_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def response_headers_policy_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#response_headers_policy_id CloudfrontDistribution#response_headers_policy_id}.'''
        result = self._values.get("response_headers_policy_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def smooth_streaming(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#smooth_streaming CloudfrontDistribution#smooth_streaming}.'''
        result = self._values.get("smooth_streaming")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def trusted_key_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#trusted_key_groups CloudfrontDistribution#trusted_key_groups}.'''
        result = self._values.get("trusted_key_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def trusted_signers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#trusted_signers CloudfrontDistribution#trusted_signers}.'''
        result = self._values.get("trusted_signers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudfrontDistributionOrderedCacheBehavior(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.cloudfrontDistribution.CloudfrontDistributionOrderedCacheBehaviorForwardedValues",
    jsii_struct_bases=[],
    name_mapping={
        "cookies": "cookies",
        "query_string": "queryString",
        "headers": "headers",
        "query_string_cache_keys": "queryStringCacheKeys",
    },
)
class CloudfrontDistributionOrderedCacheBehaviorForwardedValues:
    def __init__(
        self,
        *,
        cookies: typing.Union["CloudfrontDistributionOrderedCacheBehaviorForwardedValuesCookies", typing.Dict[builtins.str, typing.Any]],
        query_string: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        headers: typing.Optional[typing.Sequence[builtins.str]] = None,
        query_string_cache_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param cookies: cookies block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#cookies CloudfrontDistribution#cookies}
        :param query_string: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#query_string CloudfrontDistribution#query_string}.
        :param headers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#headers CloudfrontDistribution#headers}.
        :param query_string_cache_keys: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#query_string_cache_keys CloudfrontDistribution#query_string_cache_keys}.
        '''
        if isinstance(cookies, dict):
            cookies = CloudfrontDistributionOrderedCacheBehaviorForwardedValuesCookies(**cookies)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3780e0b8953bc4223510eb375ff5715f8007e7cb2b1efa2210f425a89766db93)
            check_type(argname="argument cookies", value=cookies, expected_type=type_hints["cookies"])
            check_type(argname="argument query_string", value=query_string, expected_type=type_hints["query_string"])
            check_type(argname="argument headers", value=headers, expected_type=type_hints["headers"])
            check_type(argname="argument query_string_cache_keys", value=query_string_cache_keys, expected_type=type_hints["query_string_cache_keys"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cookies": cookies,
            "query_string": query_string,
        }
        if headers is not None:
            self._values["headers"] = headers
        if query_string_cache_keys is not None:
            self._values["query_string_cache_keys"] = query_string_cache_keys

    @builtins.property
    def cookies(
        self,
    ) -> "CloudfrontDistributionOrderedCacheBehaviorForwardedValuesCookies":
        '''cookies block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#cookies CloudfrontDistribution#cookies}
        '''
        result = self._values.get("cookies")
        assert result is not None, "Required property 'cookies' is missing"
        return typing.cast("CloudfrontDistributionOrderedCacheBehaviorForwardedValuesCookies", result)

    @builtins.property
    def query_string(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#query_string CloudfrontDistribution#query_string}.'''
        result = self._values.get("query_string")
        assert result is not None, "Required property 'query_string' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    @builtins.property
    def headers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#headers CloudfrontDistribution#headers}.'''
        result = self._values.get("headers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def query_string_cache_keys(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#query_string_cache_keys CloudfrontDistribution#query_string_cache_keys}.'''
        result = self._values.get("query_string_cache_keys")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudfrontDistributionOrderedCacheBehaviorForwardedValues(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.cloudfrontDistribution.CloudfrontDistributionOrderedCacheBehaviorForwardedValuesCookies",
    jsii_struct_bases=[],
    name_mapping={"forward": "forward", "whitelisted_names": "whitelistedNames"},
)
class CloudfrontDistributionOrderedCacheBehaviorForwardedValuesCookies:
    def __init__(
        self,
        *,
        forward: builtins.str,
        whitelisted_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param forward: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#forward CloudfrontDistribution#forward}.
        :param whitelisted_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#whitelisted_names CloudfrontDistribution#whitelisted_names}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1b2d919b8b47540a017171b76aa2e4085ea3162c9c50a51f2af2c8500b14efc)
            check_type(argname="argument forward", value=forward, expected_type=type_hints["forward"])
            check_type(argname="argument whitelisted_names", value=whitelisted_names, expected_type=type_hints["whitelisted_names"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "forward": forward,
        }
        if whitelisted_names is not None:
            self._values["whitelisted_names"] = whitelisted_names

    @builtins.property
    def forward(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#forward CloudfrontDistribution#forward}.'''
        result = self._values.get("forward")
        assert result is not None, "Required property 'forward' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def whitelisted_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#whitelisted_names CloudfrontDistribution#whitelisted_names}.'''
        result = self._values.get("whitelisted_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudfrontDistributionOrderedCacheBehaviorForwardedValuesCookies(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudfrontDistributionOrderedCacheBehaviorForwardedValuesCookiesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudfrontDistribution.CloudfrontDistributionOrderedCacheBehaviorForwardedValuesCookiesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8965c40f5a63fed98e431da08e97b2f2a9625bdc80bbf4e3f5b29dc4f5514588)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetWhitelistedNames")
    def reset_whitelisted_names(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWhitelistedNames", []))

    @builtins.property
    @jsii.member(jsii_name="forwardInput")
    def forward_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "forwardInput"))

    @builtins.property
    @jsii.member(jsii_name="whitelistedNamesInput")
    def whitelisted_names_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "whitelistedNamesInput"))

    @builtins.property
    @jsii.member(jsii_name="forward")
    def forward(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "forward"))

    @forward.setter
    def forward(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bfe033ef2c79f2c011d434ca150ccd0fde2756d165c6e32b2045c5b4928ee6b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forward", value)

    @builtins.property
    @jsii.member(jsii_name="whitelistedNames")
    def whitelisted_names(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "whitelistedNames"))

    @whitelisted_names.setter
    def whitelisted_names(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ec7eb662cfe0d81b485c032a43c046705aa67f11adf443f0a11d5de11c705fb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "whitelistedNames", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CloudfrontDistributionOrderedCacheBehaviorForwardedValuesCookies]:
        return typing.cast(typing.Optional[CloudfrontDistributionOrderedCacheBehaviorForwardedValuesCookies], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudfrontDistributionOrderedCacheBehaviorForwardedValuesCookies],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf849be92617487529b8176a2ab671b39c76db02a1080633fe899b611907e17e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CloudfrontDistributionOrderedCacheBehaviorForwardedValuesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudfrontDistribution.CloudfrontDistributionOrderedCacheBehaviorForwardedValuesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e52a0798780040a4547091af8ed48a37fdeeadd069afea3681b0bbe784c9a9d1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCookies")
    def put_cookies(
        self,
        *,
        forward: builtins.str,
        whitelisted_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param forward: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#forward CloudfrontDistribution#forward}.
        :param whitelisted_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#whitelisted_names CloudfrontDistribution#whitelisted_names}.
        '''
        value = CloudfrontDistributionOrderedCacheBehaviorForwardedValuesCookies(
            forward=forward, whitelisted_names=whitelisted_names
        )

        return typing.cast(None, jsii.invoke(self, "putCookies", [value]))

    @jsii.member(jsii_name="resetHeaders")
    def reset_headers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeaders", []))

    @jsii.member(jsii_name="resetQueryStringCacheKeys")
    def reset_query_string_cache_keys(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueryStringCacheKeys", []))

    @builtins.property
    @jsii.member(jsii_name="cookies")
    def cookies(
        self,
    ) -> CloudfrontDistributionOrderedCacheBehaviorForwardedValuesCookiesOutputReference:
        return typing.cast(CloudfrontDistributionOrderedCacheBehaviorForwardedValuesCookiesOutputReference, jsii.get(self, "cookies"))

    @builtins.property
    @jsii.member(jsii_name="cookiesInput")
    def cookies_input(
        self,
    ) -> typing.Optional[CloudfrontDistributionOrderedCacheBehaviorForwardedValuesCookies]:
        return typing.cast(typing.Optional[CloudfrontDistributionOrderedCacheBehaviorForwardedValuesCookies], jsii.get(self, "cookiesInput"))

    @builtins.property
    @jsii.member(jsii_name="headersInput")
    def headers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "headersInput"))

    @builtins.property
    @jsii.member(jsii_name="queryStringCacheKeysInput")
    def query_string_cache_keys_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "queryStringCacheKeysInput"))

    @builtins.property
    @jsii.member(jsii_name="queryStringInput")
    def query_string_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "queryStringInput"))

    @builtins.property
    @jsii.member(jsii_name="headers")
    def headers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "headers"))

    @headers.setter
    def headers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed1e642cd391edaca3656bce62cddca9d03b5f7d8b8cb8a3005ea513bb4bdd05)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "headers", value)

    @builtins.property
    @jsii.member(jsii_name="queryString")
    def query_string(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "queryString"))

    @query_string.setter
    def query_string(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb0b2d38c28dc055ac7c4f5c7cd10a73a8880f1374c2ad6dab8b5c1e496cc0d3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queryString", value)

    @builtins.property
    @jsii.member(jsii_name="queryStringCacheKeys")
    def query_string_cache_keys(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "queryStringCacheKeys"))

    @query_string_cache_keys.setter
    def query_string_cache_keys(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9befc798becce42c05e20f04f2d97633cb39edc93a1f2eaaff52e0cef7bb8961)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queryStringCacheKeys", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CloudfrontDistributionOrderedCacheBehaviorForwardedValues]:
        return typing.cast(typing.Optional[CloudfrontDistributionOrderedCacheBehaviorForwardedValues], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudfrontDistributionOrderedCacheBehaviorForwardedValues],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84136ddc41493ccf0db91caea5be01be7fab7c67ecbf8bf8976d2981d12cadf8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.cloudfrontDistribution.CloudfrontDistributionOrderedCacheBehaviorFunctionAssociation",
    jsii_struct_bases=[],
    name_mapping={"event_type": "eventType", "function_arn": "functionArn"},
)
class CloudfrontDistributionOrderedCacheBehaviorFunctionAssociation:
    def __init__(self, *, event_type: builtins.str, function_arn: builtins.str) -> None:
        '''
        :param event_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#event_type CloudfrontDistribution#event_type}.
        :param function_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#function_arn CloudfrontDistribution#function_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7fa18092e6db691f05024d5c4e04d36235901654fab7957c57b9b1d1d0ad98be)
            check_type(argname="argument event_type", value=event_type, expected_type=type_hints["event_type"])
            check_type(argname="argument function_arn", value=function_arn, expected_type=type_hints["function_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "event_type": event_type,
            "function_arn": function_arn,
        }

    @builtins.property
    def event_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#event_type CloudfrontDistribution#event_type}.'''
        result = self._values.get("event_type")
        assert result is not None, "Required property 'event_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def function_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#function_arn CloudfrontDistribution#function_arn}.'''
        result = self._values.get("function_arn")
        assert result is not None, "Required property 'function_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudfrontDistributionOrderedCacheBehaviorFunctionAssociation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudfrontDistributionOrderedCacheBehaviorFunctionAssociationList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudfrontDistribution.CloudfrontDistributionOrderedCacheBehaviorFunctionAssociationList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ce7c5e1c88326285a748aea9f35eb74db652b96d6d7ae4c074a93db33d8d2c92)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CloudfrontDistributionOrderedCacheBehaviorFunctionAssociationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8adf3dfe8530c86b08a18c17941f57b680db75e0fe5c9a4d89ad7466db4f32fe)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CloudfrontDistributionOrderedCacheBehaviorFunctionAssociationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f1be4fa81b8ab14c3d8bcbc2aa000d09304939358e09ea77995bd0af2fe1b33)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5fe267dc49a848dd27da899169a3cd66c1b0d6c1809dde812b7fcd24b0acadec)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6eb11b90a10e73b1b99f1af7052c65e5a597ef30295aed54224ecef97136a77d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudfrontDistributionOrderedCacheBehaviorFunctionAssociation]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudfrontDistributionOrderedCacheBehaviorFunctionAssociation]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudfrontDistributionOrderedCacheBehaviorFunctionAssociation]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1a2900e98fadc49c13503d515d8f5d120b4fe619a53eabd270f261554291371)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CloudfrontDistributionOrderedCacheBehaviorFunctionAssociationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudfrontDistribution.CloudfrontDistributionOrderedCacheBehaviorFunctionAssociationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f2ba9c310252074c49e24b8921630d301a0d793be2178208d5a09bb1852fd8bf)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="eventTypeInput")
    def event_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "eventTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="functionArnInput")
    def function_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "functionArnInput"))

    @builtins.property
    @jsii.member(jsii_name="eventType")
    def event_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "eventType"))

    @event_type.setter
    def event_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92f014b9dcf204e695a5704537fe2569e68a711af3ff9a1d17db72fb1fd8135a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventType", value)

    @builtins.property
    @jsii.member(jsii_name="functionArn")
    def function_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "functionArn"))

    @function_arn.setter
    def function_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3c0ea8db2a99e26430d868b9d59e37aa751a4e68d633150290de429fe3fef5b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "functionArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CloudfrontDistributionOrderedCacheBehaviorFunctionAssociation, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CloudfrontDistributionOrderedCacheBehaviorFunctionAssociation, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CloudfrontDistributionOrderedCacheBehaviorFunctionAssociation, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f09b4e700ada5bc5ceeeaecff6c3da071afb87dcd675ee091c78ecb9262a8c2f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.cloudfrontDistribution.CloudfrontDistributionOrderedCacheBehaviorLambdaFunctionAssociation",
    jsii_struct_bases=[],
    name_mapping={
        "event_type": "eventType",
        "lambda_arn": "lambdaArn",
        "include_body": "includeBody",
    },
)
class CloudfrontDistributionOrderedCacheBehaviorLambdaFunctionAssociation:
    def __init__(
        self,
        *,
        event_type: builtins.str,
        lambda_arn: builtins.str,
        include_body: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param event_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#event_type CloudfrontDistribution#event_type}.
        :param lambda_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#lambda_arn CloudfrontDistribution#lambda_arn}.
        :param include_body: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#include_body CloudfrontDistribution#include_body}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e0a47d97b9faf5cbd2f85255ae8201a22a8ba344846c1c606399e820ac451cea)
            check_type(argname="argument event_type", value=event_type, expected_type=type_hints["event_type"])
            check_type(argname="argument lambda_arn", value=lambda_arn, expected_type=type_hints["lambda_arn"])
            check_type(argname="argument include_body", value=include_body, expected_type=type_hints["include_body"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "event_type": event_type,
            "lambda_arn": lambda_arn,
        }
        if include_body is not None:
            self._values["include_body"] = include_body

    @builtins.property
    def event_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#event_type CloudfrontDistribution#event_type}.'''
        result = self._values.get("event_type")
        assert result is not None, "Required property 'event_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def lambda_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#lambda_arn CloudfrontDistribution#lambda_arn}.'''
        result = self._values.get("lambda_arn")
        assert result is not None, "Required property 'lambda_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def include_body(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#include_body CloudfrontDistribution#include_body}.'''
        result = self._values.get("include_body")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudfrontDistributionOrderedCacheBehaviorLambdaFunctionAssociation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudfrontDistributionOrderedCacheBehaviorLambdaFunctionAssociationList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudfrontDistribution.CloudfrontDistributionOrderedCacheBehaviorLambdaFunctionAssociationList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3b04e9bfe78566907c8bb01689abf6b813ab6fe32a2e35ba60937f2afffe65be)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CloudfrontDistributionOrderedCacheBehaviorLambdaFunctionAssociationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a3a344bf8e8a059eca0577263dfe265778cfef39b37fc556c2b728135f8a1256)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CloudfrontDistributionOrderedCacheBehaviorLambdaFunctionAssociationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed1b230e8acf203af42d4cf45b6fb630f644c3c0e24e74a31ce9a2cbb39559b2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6298d340ad72e30d30b103d436098c1c3f76493e9faa87ab6bd02c41657f2d3f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1f6d815a1ef89bcdf07edbb7490ff16116d5620ccf60b65d7ac74f814a08e8d5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudfrontDistributionOrderedCacheBehaviorLambdaFunctionAssociation]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudfrontDistributionOrderedCacheBehaviorLambdaFunctionAssociation]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudfrontDistributionOrderedCacheBehaviorLambdaFunctionAssociation]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b3e1762cbda2aeb5687c604572ee9f97acf1e008812d868da0d17502071882b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CloudfrontDistributionOrderedCacheBehaviorLambdaFunctionAssociationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudfrontDistribution.CloudfrontDistributionOrderedCacheBehaviorLambdaFunctionAssociationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__789db6741347b5ee6c61905254b8ba9c88d772a4f28f0707a6290406294c69e4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetIncludeBody")
    def reset_include_body(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludeBody", []))

    @builtins.property
    @jsii.member(jsii_name="eventTypeInput")
    def event_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "eventTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="includeBodyInput")
    def include_body_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "includeBodyInput"))

    @builtins.property
    @jsii.member(jsii_name="lambdaArnInput")
    def lambda_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lambdaArnInput"))

    @builtins.property
    @jsii.member(jsii_name="eventType")
    def event_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "eventType"))

    @event_type.setter
    def event_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c327bd81c482913e4bcc2f95c4b48c0334c3694ae1252ca7859ff72f3cb04da)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventType", value)

    @builtins.property
    @jsii.member(jsii_name="includeBody")
    def include_body(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "includeBody"))

    @include_body.setter
    def include_body(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__742c9d8d6ba2af3e9e88378338637e7d2f00fe55a7311a2ad4586a5f41881e97)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includeBody", value)

    @builtins.property
    @jsii.member(jsii_name="lambdaArn")
    def lambda_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lambdaArn"))

    @lambda_arn.setter
    def lambda_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5cc493571d698c073258669f75f55c8df37ba9cab3846738c45c18ef4c431dc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lambdaArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CloudfrontDistributionOrderedCacheBehaviorLambdaFunctionAssociation, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CloudfrontDistributionOrderedCacheBehaviorLambdaFunctionAssociation, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CloudfrontDistributionOrderedCacheBehaviorLambdaFunctionAssociation, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62ee907dd71aee932817acfd09286d798389d42546de5fbdc401633560a952fd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CloudfrontDistributionOrderedCacheBehaviorList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudfrontDistribution.CloudfrontDistributionOrderedCacheBehaviorList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__dcd5bdb7812ba840ce14b1c27fb5d42984a4d51089beadafe2108542ba47c8c4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CloudfrontDistributionOrderedCacheBehaviorOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96b160213a5b2874716440902daa19e0694995820dc919bef2105bff1fdea21a)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CloudfrontDistributionOrderedCacheBehaviorOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d16031b5d30cf2e83914fde6a4da3a24ef310ed71883d97a371c1fed00386d3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5548e92edf59a1cca67a7ed60848eb71ade87aa6b76540fdad55e6807f62fdc7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5eb9db426a38e1ce3c806a9cfe085f5543b3e90ae844e7225e58d66931916f64)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudfrontDistributionOrderedCacheBehavior]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudfrontDistributionOrderedCacheBehavior]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudfrontDistributionOrderedCacheBehavior]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17604b0799b625c9fa655e371d2aee3a566e0e9e133649ed2941c616f58c9f0c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CloudfrontDistributionOrderedCacheBehaviorOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudfrontDistribution.CloudfrontDistributionOrderedCacheBehaviorOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7740a74d0291fb4012f4d353f080c1e482aedfe13d463f266670b9b138f0092e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putForwardedValues")
    def put_forwarded_values(
        self,
        *,
        cookies: typing.Union[CloudfrontDistributionOrderedCacheBehaviorForwardedValuesCookies, typing.Dict[builtins.str, typing.Any]],
        query_string: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        headers: typing.Optional[typing.Sequence[builtins.str]] = None,
        query_string_cache_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param cookies: cookies block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#cookies CloudfrontDistribution#cookies}
        :param query_string: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#query_string CloudfrontDistribution#query_string}.
        :param headers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#headers CloudfrontDistribution#headers}.
        :param query_string_cache_keys: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#query_string_cache_keys CloudfrontDistribution#query_string_cache_keys}.
        '''
        value = CloudfrontDistributionOrderedCacheBehaviorForwardedValues(
            cookies=cookies,
            query_string=query_string,
            headers=headers,
            query_string_cache_keys=query_string_cache_keys,
        )

        return typing.cast(None, jsii.invoke(self, "putForwardedValues", [value]))

    @jsii.member(jsii_name="putFunctionAssociation")
    def put_function_association(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CloudfrontDistributionOrderedCacheBehaviorFunctionAssociation, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e9be6db719998525bf117a414902460902d99597247667e73ba605e62c2fa75)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putFunctionAssociation", [value]))

    @jsii.member(jsii_name="putLambdaFunctionAssociation")
    def put_lambda_function_association(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CloudfrontDistributionOrderedCacheBehaviorLambdaFunctionAssociation, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f86a2f4137386d5b0c6cda651373cac7adf64226f4a1d039cc4137e06adcbf6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLambdaFunctionAssociation", [value]))

    @jsii.member(jsii_name="resetCachePolicyId")
    def reset_cache_policy_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCachePolicyId", []))

    @jsii.member(jsii_name="resetCompress")
    def reset_compress(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCompress", []))

    @jsii.member(jsii_name="resetDefaultTtl")
    def reset_default_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultTtl", []))

    @jsii.member(jsii_name="resetFieldLevelEncryptionId")
    def reset_field_level_encryption_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFieldLevelEncryptionId", []))

    @jsii.member(jsii_name="resetForwardedValues")
    def reset_forwarded_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForwardedValues", []))

    @jsii.member(jsii_name="resetFunctionAssociation")
    def reset_function_association(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFunctionAssociation", []))

    @jsii.member(jsii_name="resetLambdaFunctionAssociation")
    def reset_lambda_function_association(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLambdaFunctionAssociation", []))

    @jsii.member(jsii_name="resetMaxTtl")
    def reset_max_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxTtl", []))

    @jsii.member(jsii_name="resetMinTtl")
    def reset_min_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinTtl", []))

    @jsii.member(jsii_name="resetOriginRequestPolicyId")
    def reset_origin_request_policy_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOriginRequestPolicyId", []))

    @jsii.member(jsii_name="resetRealtimeLogConfigArn")
    def reset_realtime_log_config_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRealtimeLogConfigArn", []))

    @jsii.member(jsii_name="resetResponseHeadersPolicyId")
    def reset_response_headers_policy_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResponseHeadersPolicyId", []))

    @jsii.member(jsii_name="resetSmoothStreaming")
    def reset_smooth_streaming(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSmoothStreaming", []))

    @jsii.member(jsii_name="resetTrustedKeyGroups")
    def reset_trusted_key_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTrustedKeyGroups", []))

    @jsii.member(jsii_name="resetTrustedSigners")
    def reset_trusted_signers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTrustedSigners", []))

    @builtins.property
    @jsii.member(jsii_name="forwardedValues")
    def forwarded_values(
        self,
    ) -> CloudfrontDistributionOrderedCacheBehaviorForwardedValuesOutputReference:
        return typing.cast(CloudfrontDistributionOrderedCacheBehaviorForwardedValuesOutputReference, jsii.get(self, "forwardedValues"))

    @builtins.property
    @jsii.member(jsii_name="functionAssociation")
    def function_association(
        self,
    ) -> CloudfrontDistributionOrderedCacheBehaviorFunctionAssociationList:
        return typing.cast(CloudfrontDistributionOrderedCacheBehaviorFunctionAssociationList, jsii.get(self, "functionAssociation"))

    @builtins.property
    @jsii.member(jsii_name="lambdaFunctionAssociation")
    def lambda_function_association(
        self,
    ) -> CloudfrontDistributionOrderedCacheBehaviorLambdaFunctionAssociationList:
        return typing.cast(CloudfrontDistributionOrderedCacheBehaviorLambdaFunctionAssociationList, jsii.get(self, "lambdaFunctionAssociation"))

    @builtins.property
    @jsii.member(jsii_name="allowedMethodsInput")
    def allowed_methods_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedMethodsInput"))

    @builtins.property
    @jsii.member(jsii_name="cachedMethodsInput")
    def cached_methods_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "cachedMethodsInput"))

    @builtins.property
    @jsii.member(jsii_name="cachePolicyIdInput")
    def cache_policy_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cachePolicyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="compressInput")
    def compress_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "compressInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultTtlInput")
    def default_ttl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "defaultTtlInput"))

    @builtins.property
    @jsii.member(jsii_name="fieldLevelEncryptionIdInput")
    def field_level_encryption_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fieldLevelEncryptionIdInput"))

    @builtins.property
    @jsii.member(jsii_name="forwardedValuesInput")
    def forwarded_values_input(
        self,
    ) -> typing.Optional[CloudfrontDistributionOrderedCacheBehaviorForwardedValues]:
        return typing.cast(typing.Optional[CloudfrontDistributionOrderedCacheBehaviorForwardedValues], jsii.get(self, "forwardedValuesInput"))

    @builtins.property
    @jsii.member(jsii_name="functionAssociationInput")
    def function_association_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudfrontDistributionOrderedCacheBehaviorFunctionAssociation]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudfrontDistributionOrderedCacheBehaviorFunctionAssociation]]], jsii.get(self, "functionAssociationInput"))

    @builtins.property
    @jsii.member(jsii_name="lambdaFunctionAssociationInput")
    def lambda_function_association_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudfrontDistributionOrderedCacheBehaviorLambdaFunctionAssociation]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudfrontDistributionOrderedCacheBehaviorLambdaFunctionAssociation]]], jsii.get(self, "lambdaFunctionAssociationInput"))

    @builtins.property
    @jsii.member(jsii_name="maxTtlInput")
    def max_ttl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxTtlInput"))

    @builtins.property
    @jsii.member(jsii_name="minTtlInput")
    def min_ttl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minTtlInput"))

    @builtins.property
    @jsii.member(jsii_name="originRequestPolicyIdInput")
    def origin_request_policy_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "originRequestPolicyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="pathPatternInput")
    def path_pattern_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathPatternInput"))

    @builtins.property
    @jsii.member(jsii_name="realtimeLogConfigArnInput")
    def realtime_log_config_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "realtimeLogConfigArnInput"))

    @builtins.property
    @jsii.member(jsii_name="responseHeadersPolicyIdInput")
    def response_headers_policy_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "responseHeadersPolicyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="smoothStreamingInput")
    def smooth_streaming_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "smoothStreamingInput"))

    @builtins.property
    @jsii.member(jsii_name="targetOriginIdInput")
    def target_origin_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetOriginIdInput"))

    @builtins.property
    @jsii.member(jsii_name="trustedKeyGroupsInput")
    def trusted_key_groups_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "trustedKeyGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="trustedSignersInput")
    def trusted_signers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "trustedSignersInput"))

    @builtins.property
    @jsii.member(jsii_name="viewerProtocolPolicyInput")
    def viewer_protocol_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "viewerProtocolPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedMethods")
    def allowed_methods(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedMethods"))

    @allowed_methods.setter
    def allowed_methods(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__efe75f58f6188697ef9161e88ff6795ed860072425fa27966b865d8a8b2defc3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedMethods", value)

    @builtins.property
    @jsii.member(jsii_name="cachedMethods")
    def cached_methods(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "cachedMethods"))

    @cached_methods.setter
    def cached_methods(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23726b41986053453dc9fd4169e63955d265cdf19840ffdd0ece4f0836383f9b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cachedMethods", value)

    @builtins.property
    @jsii.member(jsii_name="cachePolicyId")
    def cache_policy_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cachePolicyId"))

    @cache_policy_id.setter
    def cache_policy_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d666a23655f4178032a7b00ce438be1b6f2d877ad522fb2a54beb4de8d47c4f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cachePolicyId", value)

    @builtins.property
    @jsii.member(jsii_name="compress")
    def compress(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "compress"))

    @compress.setter
    def compress(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91aae853eb8249f006a00369df774623df55e667bc49c2f5340697d207df7f3b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "compress", value)

    @builtins.property
    @jsii.member(jsii_name="defaultTtl")
    def default_ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "defaultTtl"))

    @default_ttl.setter
    def default_ttl(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c474c8952fb26283944a007931e4945a67ff11986b2a869f4b3003c7df2ae53b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultTtl", value)

    @builtins.property
    @jsii.member(jsii_name="fieldLevelEncryptionId")
    def field_level_encryption_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fieldLevelEncryptionId"))

    @field_level_encryption_id.setter
    def field_level_encryption_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__124ca773a0c9ab078d2f0fa543aeadf90d3c388864e32000077bf7b581ccb12a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fieldLevelEncryptionId", value)

    @builtins.property
    @jsii.member(jsii_name="maxTtl")
    def max_ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxTtl"))

    @max_ttl.setter
    def max_ttl(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb78edcd094cbbc3b9b28612f526eb6a94ad8ceef4586f9360addc547c8f476d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxTtl", value)

    @builtins.property
    @jsii.member(jsii_name="minTtl")
    def min_ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minTtl"))

    @min_ttl.setter
    def min_ttl(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3eebf10d5aafbe047e7a42b5a4b63216cb198a557074a29b5e3753c420e2d489)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minTtl", value)

    @builtins.property
    @jsii.member(jsii_name="originRequestPolicyId")
    def origin_request_policy_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "originRequestPolicyId"))

    @origin_request_policy_id.setter
    def origin_request_policy_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7b4a650064fe13f180f0a82efc7e3865db41298163a8e7ec32d4e6963b652be)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "originRequestPolicyId", value)

    @builtins.property
    @jsii.member(jsii_name="pathPattern")
    def path_pattern(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pathPattern"))

    @path_pattern.setter
    def path_pattern(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6eca684f8adf1e0b4aef6eac6ca2ad395d55c7c4cd0b43c2666c998c7456c16a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pathPattern", value)

    @builtins.property
    @jsii.member(jsii_name="realtimeLogConfigArn")
    def realtime_log_config_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "realtimeLogConfigArn"))

    @realtime_log_config_arn.setter
    def realtime_log_config_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f996058de4327e38a824f991df6104ebc7cf916dee0129f90f09ac69d188a38)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "realtimeLogConfigArn", value)

    @builtins.property
    @jsii.member(jsii_name="responseHeadersPolicyId")
    def response_headers_policy_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "responseHeadersPolicyId"))

    @response_headers_policy_id.setter
    def response_headers_policy_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21c7c292d60f4fcf6c3ba8b2de218b2eb1d6dc5ca1d45091a2d35e23ec3cba62)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "responseHeadersPolicyId", value)

    @builtins.property
    @jsii.member(jsii_name="smoothStreaming")
    def smooth_streaming(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "smoothStreaming"))

    @smooth_streaming.setter
    def smooth_streaming(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bed2443db2d81d9b6d80c22291e41eb2bb42308ab5b7f62e464b5200321c1894)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "smoothStreaming", value)

    @builtins.property
    @jsii.member(jsii_name="targetOriginId")
    def target_origin_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetOriginId"))

    @target_origin_id.setter
    def target_origin_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68676854f27256ac96c572b3a6b1b950960918890aadc232da754dbce788be44)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetOriginId", value)

    @builtins.property
    @jsii.member(jsii_name="trustedKeyGroups")
    def trusted_key_groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "trustedKeyGroups"))

    @trusted_key_groups.setter
    def trusted_key_groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6880f4f4e781f7e0150f680f720f1b7e6553dc3f47dddfc838dd560180bd288)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "trustedKeyGroups", value)

    @builtins.property
    @jsii.member(jsii_name="trustedSigners")
    def trusted_signers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "trustedSigners"))

    @trusted_signers.setter
    def trusted_signers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0dc8e6ca9d42b4ec398010dcc6590e264992d4a05434ad554c8100bf32b5c2dc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "trustedSigners", value)

    @builtins.property
    @jsii.member(jsii_name="viewerProtocolPolicy")
    def viewer_protocol_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "viewerProtocolPolicy"))

    @viewer_protocol_policy.setter
    def viewer_protocol_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b0dad78e2ab314372558800880d4f5467b13f3e9e34816fe6c7ee1267b208dc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "viewerProtocolPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CloudfrontDistributionOrderedCacheBehavior, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CloudfrontDistributionOrderedCacheBehavior, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CloudfrontDistributionOrderedCacheBehavior, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8576cf6f90608fbf0e2a5537c4000591faf425874d7a9ae1ed00c13804352f0c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.cloudfrontDistribution.CloudfrontDistributionOrigin",
    jsii_struct_bases=[],
    name_mapping={
        "domain_name": "domainName",
        "origin_id": "originId",
        "connection_attempts": "connectionAttempts",
        "connection_timeout": "connectionTimeout",
        "custom_header": "customHeader",
        "custom_origin_config": "customOriginConfig",
        "origin_access_control_id": "originAccessControlId",
        "origin_path": "originPath",
        "origin_shield": "originShield",
        "s3_origin_config": "s3OriginConfig",
    },
)
class CloudfrontDistributionOrigin:
    def __init__(
        self,
        *,
        domain_name: builtins.str,
        origin_id: builtins.str,
        connection_attempts: typing.Optional[jsii.Number] = None,
        connection_timeout: typing.Optional[jsii.Number] = None,
        custom_header: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CloudfrontDistributionOriginCustomHeader", typing.Dict[builtins.str, typing.Any]]]]] = None,
        custom_origin_config: typing.Optional[typing.Union["CloudfrontDistributionOriginCustomOriginConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        origin_access_control_id: typing.Optional[builtins.str] = None,
        origin_path: typing.Optional[builtins.str] = None,
        origin_shield: typing.Optional[typing.Union["CloudfrontDistributionOriginOriginShield", typing.Dict[builtins.str, typing.Any]]] = None,
        s3_origin_config: typing.Optional[typing.Union["CloudfrontDistributionOriginS3OriginConfig", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param domain_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#domain_name CloudfrontDistribution#domain_name}.
        :param origin_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#origin_id CloudfrontDistribution#origin_id}.
        :param connection_attempts: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#connection_attempts CloudfrontDistribution#connection_attempts}.
        :param connection_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#connection_timeout CloudfrontDistribution#connection_timeout}.
        :param custom_header: custom_header block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#custom_header CloudfrontDistribution#custom_header}
        :param custom_origin_config: custom_origin_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#custom_origin_config CloudfrontDistribution#custom_origin_config}
        :param origin_access_control_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#origin_access_control_id CloudfrontDistribution#origin_access_control_id}.
        :param origin_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#origin_path CloudfrontDistribution#origin_path}.
        :param origin_shield: origin_shield block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#origin_shield CloudfrontDistribution#origin_shield}
        :param s3_origin_config: s3_origin_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#s3_origin_config CloudfrontDistribution#s3_origin_config}
        '''
        if isinstance(custom_origin_config, dict):
            custom_origin_config = CloudfrontDistributionOriginCustomOriginConfig(**custom_origin_config)
        if isinstance(origin_shield, dict):
            origin_shield = CloudfrontDistributionOriginOriginShield(**origin_shield)
        if isinstance(s3_origin_config, dict):
            s3_origin_config = CloudfrontDistributionOriginS3OriginConfig(**s3_origin_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b808442a6ef14fc07d0f5af787f52233c2dcf77539a594f88535b9639a92792f)
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument origin_id", value=origin_id, expected_type=type_hints["origin_id"])
            check_type(argname="argument connection_attempts", value=connection_attempts, expected_type=type_hints["connection_attempts"])
            check_type(argname="argument connection_timeout", value=connection_timeout, expected_type=type_hints["connection_timeout"])
            check_type(argname="argument custom_header", value=custom_header, expected_type=type_hints["custom_header"])
            check_type(argname="argument custom_origin_config", value=custom_origin_config, expected_type=type_hints["custom_origin_config"])
            check_type(argname="argument origin_access_control_id", value=origin_access_control_id, expected_type=type_hints["origin_access_control_id"])
            check_type(argname="argument origin_path", value=origin_path, expected_type=type_hints["origin_path"])
            check_type(argname="argument origin_shield", value=origin_shield, expected_type=type_hints["origin_shield"])
            check_type(argname="argument s3_origin_config", value=s3_origin_config, expected_type=type_hints["s3_origin_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_name": domain_name,
            "origin_id": origin_id,
        }
        if connection_attempts is not None:
            self._values["connection_attempts"] = connection_attempts
        if connection_timeout is not None:
            self._values["connection_timeout"] = connection_timeout
        if custom_header is not None:
            self._values["custom_header"] = custom_header
        if custom_origin_config is not None:
            self._values["custom_origin_config"] = custom_origin_config
        if origin_access_control_id is not None:
            self._values["origin_access_control_id"] = origin_access_control_id
        if origin_path is not None:
            self._values["origin_path"] = origin_path
        if origin_shield is not None:
            self._values["origin_shield"] = origin_shield
        if s3_origin_config is not None:
            self._values["s3_origin_config"] = s3_origin_config

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#domain_name CloudfrontDistribution#domain_name}.'''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def origin_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#origin_id CloudfrontDistribution#origin_id}.'''
        result = self._values.get("origin_id")
        assert result is not None, "Required property 'origin_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def connection_attempts(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#connection_attempts CloudfrontDistribution#connection_attempts}.'''
        result = self._values.get("connection_attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def connection_timeout(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#connection_timeout CloudfrontDistribution#connection_timeout}.'''
        result = self._values.get("connection_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def custom_header(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CloudfrontDistributionOriginCustomHeader"]]]:
        '''custom_header block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#custom_header CloudfrontDistribution#custom_header}
        '''
        result = self._values.get("custom_header")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CloudfrontDistributionOriginCustomHeader"]]], result)

    @builtins.property
    def custom_origin_config(
        self,
    ) -> typing.Optional["CloudfrontDistributionOriginCustomOriginConfig"]:
        '''custom_origin_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#custom_origin_config CloudfrontDistribution#custom_origin_config}
        '''
        result = self._values.get("custom_origin_config")
        return typing.cast(typing.Optional["CloudfrontDistributionOriginCustomOriginConfig"], result)

    @builtins.property
    def origin_access_control_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#origin_access_control_id CloudfrontDistribution#origin_access_control_id}.'''
        result = self._values.get("origin_access_control_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def origin_path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#origin_path CloudfrontDistribution#origin_path}.'''
        result = self._values.get("origin_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def origin_shield(
        self,
    ) -> typing.Optional["CloudfrontDistributionOriginOriginShield"]:
        '''origin_shield block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#origin_shield CloudfrontDistribution#origin_shield}
        '''
        result = self._values.get("origin_shield")
        return typing.cast(typing.Optional["CloudfrontDistributionOriginOriginShield"], result)

    @builtins.property
    def s3_origin_config(
        self,
    ) -> typing.Optional["CloudfrontDistributionOriginS3OriginConfig"]:
        '''s3_origin_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#s3_origin_config CloudfrontDistribution#s3_origin_config}
        '''
        result = self._values.get("s3_origin_config")
        return typing.cast(typing.Optional["CloudfrontDistributionOriginS3OriginConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudfrontDistributionOrigin(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.cloudfrontDistribution.CloudfrontDistributionOriginCustomHeader",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "value": "value"},
)
class CloudfrontDistributionOriginCustomHeader:
    def __init__(self, *, name: builtins.str, value: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#name CloudfrontDistribution#name}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#value CloudfrontDistribution#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__579181c64ec8f90df065081148caef31163070545cf601e50c2de093d31676ba)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "value": value,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#name CloudfrontDistribution#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#value CloudfrontDistribution#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudfrontDistributionOriginCustomHeader(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudfrontDistributionOriginCustomHeaderList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudfrontDistribution.CloudfrontDistributionOriginCustomHeaderList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c59407230a488bd4c755890a3accb238be78d3ac6e65440eac0aae2e72349615)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CloudfrontDistributionOriginCustomHeaderOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__979dacfc0e93be6e474dc1f93c92431e326f2d535dd585ed9f38f02a9cf0dff6)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CloudfrontDistributionOriginCustomHeaderOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0cd9a86ae1ed0c834e428ddd7ed73df432d46082e48c7ac58a5a46c63430a36a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__fd6c3986ca4e6a284acc4144424eb0345f766cdd9fee9be548e269c88d45e133)
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
            type_hints = typing.get_type_hints(_typecheckingstub__33542556960a2c4287edbcdebd503d050597e5dfb69d616a1fb30d790a612de3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudfrontDistributionOriginCustomHeader]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudfrontDistributionOriginCustomHeader]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudfrontDistributionOriginCustomHeader]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__812828a9ceff14818e51a2d8f6c17248b30f59f506cd33af14ecab63764ee40a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CloudfrontDistributionOriginCustomHeaderOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudfrontDistribution.CloudfrontDistributionOriginCustomHeaderOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6ad23ab58881099e60ac6207dd2ec336a72a03c077f2aac3cb7b5f939c3c0c40)
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
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7865cc0dea616de689141609333235284982b862f039e00ed8844a675dbc0eff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eafd7a5abe591a61771fcc7ddd17829e99e4111953c8984acbc805d3847d3d99)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CloudfrontDistributionOriginCustomHeader, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CloudfrontDistributionOriginCustomHeader, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CloudfrontDistributionOriginCustomHeader, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af8912530ff476a195efd201f560086e7f702ae6ab717121176d06e2837349b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.cloudfrontDistribution.CloudfrontDistributionOriginCustomOriginConfig",
    jsii_struct_bases=[],
    name_mapping={
        "http_port": "httpPort",
        "https_port": "httpsPort",
        "origin_protocol_policy": "originProtocolPolicy",
        "origin_ssl_protocols": "originSslProtocols",
        "origin_keepalive_timeout": "originKeepaliveTimeout",
        "origin_read_timeout": "originReadTimeout",
    },
)
class CloudfrontDistributionOriginCustomOriginConfig:
    def __init__(
        self,
        *,
        http_port: jsii.Number,
        https_port: jsii.Number,
        origin_protocol_policy: builtins.str,
        origin_ssl_protocols: typing.Sequence[builtins.str],
        origin_keepalive_timeout: typing.Optional[jsii.Number] = None,
        origin_read_timeout: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param http_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#http_port CloudfrontDistribution#http_port}.
        :param https_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#https_port CloudfrontDistribution#https_port}.
        :param origin_protocol_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#origin_protocol_policy CloudfrontDistribution#origin_protocol_policy}.
        :param origin_ssl_protocols: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#origin_ssl_protocols CloudfrontDistribution#origin_ssl_protocols}.
        :param origin_keepalive_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#origin_keepalive_timeout CloudfrontDistribution#origin_keepalive_timeout}.
        :param origin_read_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#origin_read_timeout CloudfrontDistribution#origin_read_timeout}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e1cafb27d80c969a9f71593aae3f7de481fa1c76669c8d9312d35b154bf2b91)
            check_type(argname="argument http_port", value=http_port, expected_type=type_hints["http_port"])
            check_type(argname="argument https_port", value=https_port, expected_type=type_hints["https_port"])
            check_type(argname="argument origin_protocol_policy", value=origin_protocol_policy, expected_type=type_hints["origin_protocol_policy"])
            check_type(argname="argument origin_ssl_protocols", value=origin_ssl_protocols, expected_type=type_hints["origin_ssl_protocols"])
            check_type(argname="argument origin_keepalive_timeout", value=origin_keepalive_timeout, expected_type=type_hints["origin_keepalive_timeout"])
            check_type(argname="argument origin_read_timeout", value=origin_read_timeout, expected_type=type_hints["origin_read_timeout"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "http_port": http_port,
            "https_port": https_port,
            "origin_protocol_policy": origin_protocol_policy,
            "origin_ssl_protocols": origin_ssl_protocols,
        }
        if origin_keepalive_timeout is not None:
            self._values["origin_keepalive_timeout"] = origin_keepalive_timeout
        if origin_read_timeout is not None:
            self._values["origin_read_timeout"] = origin_read_timeout

    @builtins.property
    def http_port(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#http_port CloudfrontDistribution#http_port}.'''
        result = self._values.get("http_port")
        assert result is not None, "Required property 'http_port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def https_port(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#https_port CloudfrontDistribution#https_port}.'''
        result = self._values.get("https_port")
        assert result is not None, "Required property 'https_port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def origin_protocol_policy(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#origin_protocol_policy CloudfrontDistribution#origin_protocol_policy}.'''
        result = self._values.get("origin_protocol_policy")
        assert result is not None, "Required property 'origin_protocol_policy' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def origin_ssl_protocols(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#origin_ssl_protocols CloudfrontDistribution#origin_ssl_protocols}.'''
        result = self._values.get("origin_ssl_protocols")
        assert result is not None, "Required property 'origin_ssl_protocols' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def origin_keepalive_timeout(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#origin_keepalive_timeout CloudfrontDistribution#origin_keepalive_timeout}.'''
        result = self._values.get("origin_keepalive_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def origin_read_timeout(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#origin_read_timeout CloudfrontDistribution#origin_read_timeout}.'''
        result = self._values.get("origin_read_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudfrontDistributionOriginCustomOriginConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudfrontDistributionOriginCustomOriginConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudfrontDistribution.CloudfrontDistributionOriginCustomOriginConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a7add305d98c92836576bb1d390703206e9880992db0de2543bf9bdf45107432)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetOriginKeepaliveTimeout")
    def reset_origin_keepalive_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOriginKeepaliveTimeout", []))

    @jsii.member(jsii_name="resetOriginReadTimeout")
    def reset_origin_read_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOriginReadTimeout", []))

    @builtins.property
    @jsii.member(jsii_name="httpPortInput")
    def http_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "httpPortInput"))

    @builtins.property
    @jsii.member(jsii_name="httpsPortInput")
    def https_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "httpsPortInput"))

    @builtins.property
    @jsii.member(jsii_name="originKeepaliveTimeoutInput")
    def origin_keepalive_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "originKeepaliveTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="originProtocolPolicyInput")
    def origin_protocol_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "originProtocolPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="originReadTimeoutInput")
    def origin_read_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "originReadTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="originSslProtocolsInput")
    def origin_ssl_protocols_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "originSslProtocolsInput"))

    @builtins.property
    @jsii.member(jsii_name="httpPort")
    def http_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "httpPort"))

    @http_port.setter
    def http_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__10d829c8ad4c733655bfe30cfd93ddde26bfcabb8846b7b5b32685087d5e7f5d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpPort", value)

    @builtins.property
    @jsii.member(jsii_name="httpsPort")
    def https_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "httpsPort"))

    @https_port.setter
    def https_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__991f75bf433e60657e3adb68416d4647f282da8479069516635cfd8190afac2c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpsPort", value)

    @builtins.property
    @jsii.member(jsii_name="originKeepaliveTimeout")
    def origin_keepalive_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "originKeepaliveTimeout"))

    @origin_keepalive_timeout.setter
    def origin_keepalive_timeout(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b5793bc43b613703676dbbe986b1641fdf5b0ee622c20cc4e64813162e5bceb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "originKeepaliveTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="originProtocolPolicy")
    def origin_protocol_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "originProtocolPolicy"))

    @origin_protocol_policy.setter
    def origin_protocol_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a8c5d6f39d05b539d418c8b105318f36bfc56db5ea68d8017f78d4a00b821eea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "originProtocolPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="originReadTimeout")
    def origin_read_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "originReadTimeout"))

    @origin_read_timeout.setter
    def origin_read_timeout(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bcde30b53d5d917d56a725e20094f90378b153999713c39aa6081eca356c262d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "originReadTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="originSslProtocols")
    def origin_ssl_protocols(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "originSslProtocols"))

    @origin_ssl_protocols.setter
    def origin_ssl_protocols(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__508c4e282d93fa604bb0688d16263695a5a1c0b8dd90aa93347ef220f04df8c7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "originSslProtocols", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CloudfrontDistributionOriginCustomOriginConfig]:
        return typing.cast(typing.Optional[CloudfrontDistributionOriginCustomOriginConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudfrontDistributionOriginCustomOriginConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9cadbf12563ac7cc36066eb0d14c25645617472f3ff61976e7825f6cd35cffea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.cloudfrontDistribution.CloudfrontDistributionOriginGroup",
    jsii_struct_bases=[],
    name_mapping={
        "failover_criteria": "failoverCriteria",
        "member": "member",
        "origin_id": "originId",
    },
)
class CloudfrontDistributionOriginGroup:
    def __init__(
        self,
        *,
        failover_criteria: typing.Union["CloudfrontDistributionOriginGroupFailoverCriteria", typing.Dict[builtins.str, typing.Any]],
        member: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CloudfrontDistributionOriginGroupMember", typing.Dict[builtins.str, typing.Any]]]],
        origin_id: builtins.str,
    ) -> None:
        '''
        :param failover_criteria: failover_criteria block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#failover_criteria CloudfrontDistribution#failover_criteria}
        :param member: member block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#member CloudfrontDistribution#member}
        :param origin_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#origin_id CloudfrontDistribution#origin_id}.
        '''
        if isinstance(failover_criteria, dict):
            failover_criteria = CloudfrontDistributionOriginGroupFailoverCriteria(**failover_criteria)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc04b96358869b5364bd8c269ee6b6c71053dda6dc3a1be6284ddf361cbb20e4)
            check_type(argname="argument failover_criteria", value=failover_criteria, expected_type=type_hints["failover_criteria"])
            check_type(argname="argument member", value=member, expected_type=type_hints["member"])
            check_type(argname="argument origin_id", value=origin_id, expected_type=type_hints["origin_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "failover_criteria": failover_criteria,
            "member": member,
            "origin_id": origin_id,
        }

    @builtins.property
    def failover_criteria(self) -> "CloudfrontDistributionOriginGroupFailoverCriteria":
        '''failover_criteria block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#failover_criteria CloudfrontDistribution#failover_criteria}
        '''
        result = self._values.get("failover_criteria")
        assert result is not None, "Required property 'failover_criteria' is missing"
        return typing.cast("CloudfrontDistributionOriginGroupFailoverCriteria", result)

    @builtins.property
    def member(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CloudfrontDistributionOriginGroupMember"]]:
        '''member block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#member CloudfrontDistribution#member}
        '''
        result = self._values.get("member")
        assert result is not None, "Required property 'member' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CloudfrontDistributionOriginGroupMember"]], result)

    @builtins.property
    def origin_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#origin_id CloudfrontDistribution#origin_id}.'''
        result = self._values.get("origin_id")
        assert result is not None, "Required property 'origin_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudfrontDistributionOriginGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.cloudfrontDistribution.CloudfrontDistributionOriginGroupFailoverCriteria",
    jsii_struct_bases=[],
    name_mapping={"status_codes": "statusCodes"},
)
class CloudfrontDistributionOriginGroupFailoverCriteria:
    def __init__(self, *, status_codes: typing.Sequence[jsii.Number]) -> None:
        '''
        :param status_codes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#status_codes CloudfrontDistribution#status_codes}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59023e9e148360643b46f004cc5742b8ca7ea4995bd2570fba048c0f10b4a9df)
            check_type(argname="argument status_codes", value=status_codes, expected_type=type_hints["status_codes"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "status_codes": status_codes,
        }

    @builtins.property
    def status_codes(self) -> typing.List[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#status_codes CloudfrontDistribution#status_codes}.'''
        result = self._values.get("status_codes")
        assert result is not None, "Required property 'status_codes' is missing"
        return typing.cast(typing.List[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudfrontDistributionOriginGroupFailoverCriteria(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudfrontDistributionOriginGroupFailoverCriteriaOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudfrontDistribution.CloudfrontDistributionOriginGroupFailoverCriteriaOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d62f83f8dc9b0b3984bc64e3bfac1bd6ec0c60379e35eb407046687cf2725b43)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="statusCodesInput")
    def status_codes_input(self) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "statusCodesInput"))

    @builtins.property
    @jsii.member(jsii_name="statusCodes")
    def status_codes(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "statusCodes"))

    @status_codes.setter
    def status_codes(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d1758d94456df292d1fd56325892f706e5bf0ba1a9a51416820f8c6c372b5b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "statusCodes", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CloudfrontDistributionOriginGroupFailoverCriteria]:
        return typing.cast(typing.Optional[CloudfrontDistributionOriginGroupFailoverCriteria], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudfrontDistributionOriginGroupFailoverCriteria],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e5c34efe96089d3ef457e590de2f0a310d929eabea91f7536b5ca992f949380)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CloudfrontDistributionOriginGroupList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudfrontDistribution.CloudfrontDistributionOriginGroupList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5137c6197b4b45c9b54949f88db591fe6979fbe05f59213c03a19fc118fb2a72)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CloudfrontDistributionOriginGroupOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08116efd1a7473d132f4c5d02e5b3b36aeb3ee59e64bcc07de110d9e0f724679)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CloudfrontDistributionOriginGroupOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85945881f0a9fee99750eb178703dec676d34384bf087948fadd32f7165d2600)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f8d6d6e12aab76792d64e6c79531a373a4396f46c75fe36961b0fec0efc1851b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__463d3cb2de5d43b94df86267284f9c89a891552a2208dbc47101ce08c430e5a0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudfrontDistributionOriginGroup]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudfrontDistributionOriginGroup]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudfrontDistributionOriginGroup]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be7a30cf7f8a3599afead8602c5e44661423e2d1aae44a77a08403bc834fdb76)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.cloudfrontDistribution.CloudfrontDistributionOriginGroupMember",
    jsii_struct_bases=[],
    name_mapping={"origin_id": "originId"},
)
class CloudfrontDistributionOriginGroupMember:
    def __init__(self, *, origin_id: builtins.str) -> None:
        '''
        :param origin_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#origin_id CloudfrontDistribution#origin_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7fe0f88b7d8c3bd8c44aba6125d20bb7848ac6f67144ec40b421c4f9390a2d87)
            check_type(argname="argument origin_id", value=origin_id, expected_type=type_hints["origin_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "origin_id": origin_id,
        }

    @builtins.property
    def origin_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#origin_id CloudfrontDistribution#origin_id}.'''
        result = self._values.get("origin_id")
        assert result is not None, "Required property 'origin_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudfrontDistributionOriginGroupMember(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudfrontDistributionOriginGroupMemberList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudfrontDistribution.CloudfrontDistributionOriginGroupMemberList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c62a792adc112cca90a643e415e5179f6d191a972e0e496282c18f3543fac5c9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CloudfrontDistributionOriginGroupMemberOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4803e520be380f5141472de6d7a8ffd56986b332ba57fd14fb583b1de55bb996)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CloudfrontDistributionOriginGroupMemberOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25917340dd733d361481593b20358f31845fbf024fce70303d9f0209425c3717)
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
            type_hints = typing.get_type_hints(_typecheckingstub__dc64d9c31299858928b527311f8d6a721220efa0aa75079a02d0ed932404632d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__072c53f4b705facbd90c150e8f7f634187aa4327639370f91e8f599ba5beed1a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudfrontDistributionOriginGroupMember]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudfrontDistributionOriginGroupMember]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudfrontDistributionOriginGroupMember]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8bf30fcd1d12624f437f10f913fbd2cc5231c3a27cae47954d7b0cc2cbb1935)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CloudfrontDistributionOriginGroupMemberOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudfrontDistribution.CloudfrontDistributionOriginGroupMemberOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__599d4dd353ad4bcc07553a81f49cdfa3b403c541fa2b2f12c32481f2c45ccf3b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="originIdInput")
    def origin_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "originIdInput"))

    @builtins.property
    @jsii.member(jsii_name="originId")
    def origin_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "originId"))

    @origin_id.setter
    def origin_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6267103d3ac7a2d983d0f406d52dd10c69a7275b4b8cf498a8832622cf55e6bb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "originId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CloudfrontDistributionOriginGroupMember, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CloudfrontDistributionOriginGroupMember, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CloudfrontDistributionOriginGroupMember, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__afb5405582c708c204378146416c09a7e24bc371e13205028bfe24080c17613d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CloudfrontDistributionOriginGroupOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudfrontDistribution.CloudfrontDistributionOriginGroupOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3ccb9244e9435c8aee4568669c9f99bae1fe355f9e2f394052edf0aa83c1c881)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putFailoverCriteria")
    def put_failover_criteria(
        self,
        *,
        status_codes: typing.Sequence[jsii.Number],
    ) -> None:
        '''
        :param status_codes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#status_codes CloudfrontDistribution#status_codes}.
        '''
        value = CloudfrontDistributionOriginGroupFailoverCriteria(
            status_codes=status_codes
        )

        return typing.cast(None, jsii.invoke(self, "putFailoverCriteria", [value]))

    @jsii.member(jsii_name="putMember")
    def put_member(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CloudfrontDistributionOriginGroupMember, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eff3f1ebc767b5deeada406ddf49ac4e182127f521abdcdb531541c22b7ec3c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMember", [value]))

    @builtins.property
    @jsii.member(jsii_name="failoverCriteria")
    def failover_criteria(
        self,
    ) -> CloudfrontDistributionOriginGroupFailoverCriteriaOutputReference:
        return typing.cast(CloudfrontDistributionOriginGroupFailoverCriteriaOutputReference, jsii.get(self, "failoverCriteria"))

    @builtins.property
    @jsii.member(jsii_name="member")
    def member(self) -> CloudfrontDistributionOriginGroupMemberList:
        return typing.cast(CloudfrontDistributionOriginGroupMemberList, jsii.get(self, "member"))

    @builtins.property
    @jsii.member(jsii_name="failoverCriteriaInput")
    def failover_criteria_input(
        self,
    ) -> typing.Optional[CloudfrontDistributionOriginGroupFailoverCriteria]:
        return typing.cast(typing.Optional[CloudfrontDistributionOriginGroupFailoverCriteria], jsii.get(self, "failoverCriteriaInput"))

    @builtins.property
    @jsii.member(jsii_name="memberInput")
    def member_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudfrontDistributionOriginGroupMember]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudfrontDistributionOriginGroupMember]]], jsii.get(self, "memberInput"))

    @builtins.property
    @jsii.member(jsii_name="originIdInput")
    def origin_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "originIdInput"))

    @builtins.property
    @jsii.member(jsii_name="originId")
    def origin_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "originId"))

    @origin_id.setter
    def origin_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09aeb9f9998c85b6d420489a79791b04602dbe7e5e63572466b16175e74830ed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "originId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CloudfrontDistributionOriginGroup, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CloudfrontDistributionOriginGroup, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CloudfrontDistributionOriginGroup, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1fce33bfe861a4dd7a2e50880d071565f54332cf84542e18b573872fa4107142)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CloudfrontDistributionOriginList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudfrontDistribution.CloudfrontDistributionOriginList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7af76aa4ea97f351edc98d75d933a8ca0d793766a4ff9821dbc676c528b48bd9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "CloudfrontDistributionOriginOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42fe36656f725503148a3f03663a459ad5fb81b848fc9c281cbcc2deded84cdc)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CloudfrontDistributionOriginOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9986a24fb96a32e242a8e19c9ee8f3d0a930b7dcad58bd819481b5511a3af56)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b5cc0bba837a2c9940294574e58ac0099ed2bae8f8c5f68bf06698f3632f774d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__fe4ab87419be423cc35ce4b454a988162badc33ca31e90bfaff2cfe369b057ca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudfrontDistributionOrigin]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudfrontDistributionOrigin]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudfrontDistributionOrigin]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2ab681fe6c6be72e4031f6a864b1aa1f0fa308b3d04e4b633c34dee6f4dacf6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.cloudfrontDistribution.CloudfrontDistributionOriginOriginShield",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "origin_shield_region": "originShieldRegion"},
)
class CloudfrontDistributionOriginOriginShield:
    def __init__(
        self,
        *,
        enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        origin_shield_region: builtins.str,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#enabled CloudfrontDistribution#enabled}.
        :param origin_shield_region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#origin_shield_region CloudfrontDistribution#origin_shield_region}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd06853bd7033a230725168881d5aa736a42908355746ea572e7919f48af9ecf)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument origin_shield_region", value=origin_shield_region, expected_type=type_hints["origin_shield_region"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "enabled": enabled,
            "origin_shield_region": origin_shield_region,
        }

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#enabled CloudfrontDistribution#enabled}.'''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    @builtins.property
    def origin_shield_region(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#origin_shield_region CloudfrontDistribution#origin_shield_region}.'''
        result = self._values.get("origin_shield_region")
        assert result is not None, "Required property 'origin_shield_region' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudfrontDistributionOriginOriginShield(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudfrontDistributionOriginOriginShieldOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudfrontDistribution.CloudfrontDistributionOriginOriginShieldOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__17f2a025ca3e6c8e1ba034a715f412b819e707b6352ee181f19cfa2eec91d4c4)
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
    @jsii.member(jsii_name="originShieldRegionInput")
    def origin_shield_region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "originShieldRegionInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__a9cdb6c0f846a3b4d75943ae17ba8ac186f64a35d6fe90e3f9cfc32e73a628e1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="originShieldRegion")
    def origin_shield_region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "originShieldRegion"))

    @origin_shield_region.setter
    def origin_shield_region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79cab0b73298ed4a11a8d44562f68ee567cbabe5bff761318af33add4f4c3190)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "originShieldRegion", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CloudfrontDistributionOriginOriginShield]:
        return typing.cast(typing.Optional[CloudfrontDistributionOriginOriginShield], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudfrontDistributionOriginOriginShield],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea3a7fe5311ea0c2e0f69cd80198ede4fc7f85afc0bc576c9a9aba6bc55a754b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CloudfrontDistributionOriginOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudfrontDistribution.CloudfrontDistributionOriginOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__dd8f1ac7ffd05ae0cdbbf65c42fb1e7d4ec09bf45abd0449e857c1d81d98d6b2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putCustomHeader")
    def put_custom_header(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CloudfrontDistributionOriginCustomHeader, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__572820daf473d586693b72e9f643426fc21cc1dde1798631c97047f9f521d50a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCustomHeader", [value]))

    @jsii.member(jsii_name="putCustomOriginConfig")
    def put_custom_origin_config(
        self,
        *,
        http_port: jsii.Number,
        https_port: jsii.Number,
        origin_protocol_policy: builtins.str,
        origin_ssl_protocols: typing.Sequence[builtins.str],
        origin_keepalive_timeout: typing.Optional[jsii.Number] = None,
        origin_read_timeout: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param http_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#http_port CloudfrontDistribution#http_port}.
        :param https_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#https_port CloudfrontDistribution#https_port}.
        :param origin_protocol_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#origin_protocol_policy CloudfrontDistribution#origin_protocol_policy}.
        :param origin_ssl_protocols: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#origin_ssl_protocols CloudfrontDistribution#origin_ssl_protocols}.
        :param origin_keepalive_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#origin_keepalive_timeout CloudfrontDistribution#origin_keepalive_timeout}.
        :param origin_read_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#origin_read_timeout CloudfrontDistribution#origin_read_timeout}.
        '''
        value = CloudfrontDistributionOriginCustomOriginConfig(
            http_port=http_port,
            https_port=https_port,
            origin_protocol_policy=origin_protocol_policy,
            origin_ssl_protocols=origin_ssl_protocols,
            origin_keepalive_timeout=origin_keepalive_timeout,
            origin_read_timeout=origin_read_timeout,
        )

        return typing.cast(None, jsii.invoke(self, "putCustomOriginConfig", [value]))

    @jsii.member(jsii_name="putOriginShield")
    def put_origin_shield(
        self,
        *,
        enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        origin_shield_region: builtins.str,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#enabled CloudfrontDistribution#enabled}.
        :param origin_shield_region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#origin_shield_region CloudfrontDistribution#origin_shield_region}.
        '''
        value = CloudfrontDistributionOriginOriginShield(
            enabled=enabled, origin_shield_region=origin_shield_region
        )

        return typing.cast(None, jsii.invoke(self, "putOriginShield", [value]))

    @jsii.member(jsii_name="putS3OriginConfig")
    def put_s3_origin_config(self, *, origin_access_identity: builtins.str) -> None:
        '''
        :param origin_access_identity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#origin_access_identity CloudfrontDistribution#origin_access_identity}.
        '''
        value = CloudfrontDistributionOriginS3OriginConfig(
            origin_access_identity=origin_access_identity
        )

        return typing.cast(None, jsii.invoke(self, "putS3OriginConfig", [value]))

    @jsii.member(jsii_name="resetConnectionAttempts")
    def reset_connection_attempts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectionAttempts", []))

    @jsii.member(jsii_name="resetConnectionTimeout")
    def reset_connection_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectionTimeout", []))

    @jsii.member(jsii_name="resetCustomHeader")
    def reset_custom_header(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomHeader", []))

    @jsii.member(jsii_name="resetCustomOriginConfig")
    def reset_custom_origin_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomOriginConfig", []))

    @jsii.member(jsii_name="resetOriginAccessControlId")
    def reset_origin_access_control_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOriginAccessControlId", []))

    @jsii.member(jsii_name="resetOriginPath")
    def reset_origin_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOriginPath", []))

    @jsii.member(jsii_name="resetOriginShield")
    def reset_origin_shield(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOriginShield", []))

    @jsii.member(jsii_name="resetS3OriginConfig")
    def reset_s3_origin_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3OriginConfig", []))

    @builtins.property
    @jsii.member(jsii_name="customHeader")
    def custom_header(self) -> CloudfrontDistributionOriginCustomHeaderList:
        return typing.cast(CloudfrontDistributionOriginCustomHeaderList, jsii.get(self, "customHeader"))

    @builtins.property
    @jsii.member(jsii_name="customOriginConfig")
    def custom_origin_config(
        self,
    ) -> CloudfrontDistributionOriginCustomOriginConfigOutputReference:
        return typing.cast(CloudfrontDistributionOriginCustomOriginConfigOutputReference, jsii.get(self, "customOriginConfig"))

    @builtins.property
    @jsii.member(jsii_name="originShield")
    def origin_shield(self) -> CloudfrontDistributionOriginOriginShieldOutputReference:
        return typing.cast(CloudfrontDistributionOriginOriginShieldOutputReference, jsii.get(self, "originShield"))

    @builtins.property
    @jsii.member(jsii_name="s3OriginConfig")
    def s3_origin_config(
        self,
    ) -> "CloudfrontDistributionOriginS3OriginConfigOutputReference":
        return typing.cast("CloudfrontDistributionOriginS3OriginConfigOutputReference", jsii.get(self, "s3OriginConfig"))

    @builtins.property
    @jsii.member(jsii_name="connectionAttemptsInput")
    def connection_attempts_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "connectionAttemptsInput"))

    @builtins.property
    @jsii.member(jsii_name="connectionTimeoutInput")
    def connection_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "connectionTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="customHeaderInput")
    def custom_header_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudfrontDistributionOriginCustomHeader]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudfrontDistributionOriginCustomHeader]]], jsii.get(self, "customHeaderInput"))

    @builtins.property
    @jsii.member(jsii_name="customOriginConfigInput")
    def custom_origin_config_input(
        self,
    ) -> typing.Optional[CloudfrontDistributionOriginCustomOriginConfig]:
        return typing.cast(typing.Optional[CloudfrontDistributionOriginCustomOriginConfig], jsii.get(self, "customOriginConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="domainNameInput")
    def domain_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainNameInput"))

    @builtins.property
    @jsii.member(jsii_name="originAccessControlIdInput")
    def origin_access_control_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "originAccessControlIdInput"))

    @builtins.property
    @jsii.member(jsii_name="originIdInput")
    def origin_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "originIdInput"))

    @builtins.property
    @jsii.member(jsii_name="originPathInput")
    def origin_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "originPathInput"))

    @builtins.property
    @jsii.member(jsii_name="originShieldInput")
    def origin_shield_input(
        self,
    ) -> typing.Optional[CloudfrontDistributionOriginOriginShield]:
        return typing.cast(typing.Optional[CloudfrontDistributionOriginOriginShield], jsii.get(self, "originShieldInput"))

    @builtins.property
    @jsii.member(jsii_name="s3OriginConfigInput")
    def s3_origin_config_input(
        self,
    ) -> typing.Optional["CloudfrontDistributionOriginS3OriginConfig"]:
        return typing.cast(typing.Optional["CloudfrontDistributionOriginS3OriginConfig"], jsii.get(self, "s3OriginConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="connectionAttempts")
    def connection_attempts(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "connectionAttempts"))

    @connection_attempts.setter
    def connection_attempts(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__55f1426c535904823863416136c389b1ff30ef1e8552e1a29d05a4942e65bdc0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionAttempts", value)

    @builtins.property
    @jsii.member(jsii_name="connectionTimeout")
    def connection_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "connectionTimeout"))

    @connection_timeout.setter
    def connection_timeout(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__494f8a87c0013faa4c5b18ed9b246e105094884ce18bf808402e527b0ebd14f5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domainName"))

    @domain_name.setter
    def domain_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0d6ddc4b56ebcf40d04f0b48c68f1c249e65d4366ff9f5539105812c5f4f065)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainName", value)

    @builtins.property
    @jsii.member(jsii_name="originAccessControlId")
    def origin_access_control_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "originAccessControlId"))

    @origin_access_control_id.setter
    def origin_access_control_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5115d98b1f84f5918660aea6b135eac1db8c486d3b930813c2e5ff101f140acb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "originAccessControlId", value)

    @builtins.property
    @jsii.member(jsii_name="originId")
    def origin_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "originId"))

    @origin_id.setter
    def origin_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4eef73c3a096a6eb19e167ee36179943866789de3e6305792e653a950b69e2ac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "originId", value)

    @builtins.property
    @jsii.member(jsii_name="originPath")
    def origin_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "originPath"))

    @origin_path.setter
    def origin_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b16ae66620556373b974af369f6f0dfbcb342f7fd4703ef5d30239a68074a6c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "originPath", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CloudfrontDistributionOrigin, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CloudfrontDistributionOrigin, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CloudfrontDistributionOrigin, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__daa5a7e8b36cee38ad2b97b2af9a954ff87e4464f79ec93c95a1389b83680b03)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.cloudfrontDistribution.CloudfrontDistributionOriginS3OriginConfig",
    jsii_struct_bases=[],
    name_mapping={"origin_access_identity": "originAccessIdentity"},
)
class CloudfrontDistributionOriginS3OriginConfig:
    def __init__(self, *, origin_access_identity: builtins.str) -> None:
        '''
        :param origin_access_identity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#origin_access_identity CloudfrontDistribution#origin_access_identity}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ebe800d16183e3db4ec4cf14fb934dab246867cf488c17bdd08b2e2eccab0065)
            check_type(argname="argument origin_access_identity", value=origin_access_identity, expected_type=type_hints["origin_access_identity"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "origin_access_identity": origin_access_identity,
        }

    @builtins.property
    def origin_access_identity(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#origin_access_identity CloudfrontDistribution#origin_access_identity}.'''
        result = self._values.get("origin_access_identity")
        assert result is not None, "Required property 'origin_access_identity' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudfrontDistributionOriginS3OriginConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudfrontDistributionOriginS3OriginConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudfrontDistribution.CloudfrontDistributionOriginS3OriginConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e45ca5716ef1d47c9915b444f0dcd00c92569c81ce276c95be5d96c45c0c1fe2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="originAccessIdentityInput")
    def origin_access_identity_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "originAccessIdentityInput"))

    @builtins.property
    @jsii.member(jsii_name="originAccessIdentity")
    def origin_access_identity(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "originAccessIdentity"))

    @origin_access_identity.setter
    def origin_access_identity(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0429d864931bbc21bc6c9e0a5e2c8cac591986526557406833d8d2e81e5d65d6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "originAccessIdentity", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CloudfrontDistributionOriginS3OriginConfig]:
        return typing.cast(typing.Optional[CloudfrontDistributionOriginS3OriginConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudfrontDistributionOriginS3OriginConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa52e356ea656c22aa32ba52f3711e4ad45e23edbc30b8ef3a645d4658fe0fb9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.cloudfrontDistribution.CloudfrontDistributionRestrictions",
    jsii_struct_bases=[],
    name_mapping={"geo_restriction": "geoRestriction"},
)
class CloudfrontDistributionRestrictions:
    def __init__(
        self,
        *,
        geo_restriction: typing.Union["CloudfrontDistributionRestrictionsGeoRestriction", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param geo_restriction: geo_restriction block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#geo_restriction CloudfrontDistribution#geo_restriction}
        '''
        if isinstance(geo_restriction, dict):
            geo_restriction = CloudfrontDistributionRestrictionsGeoRestriction(**geo_restriction)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad26c3ce4fe5e6ab55d24b6eb1debdeb90e1a04e4406bbf2a0aecfe6e353e7f6)
            check_type(argname="argument geo_restriction", value=geo_restriction, expected_type=type_hints["geo_restriction"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "geo_restriction": geo_restriction,
        }

    @builtins.property
    def geo_restriction(self) -> "CloudfrontDistributionRestrictionsGeoRestriction":
        '''geo_restriction block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#geo_restriction CloudfrontDistribution#geo_restriction}
        '''
        result = self._values.get("geo_restriction")
        assert result is not None, "Required property 'geo_restriction' is missing"
        return typing.cast("CloudfrontDistributionRestrictionsGeoRestriction", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudfrontDistributionRestrictions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.cloudfrontDistribution.CloudfrontDistributionRestrictionsGeoRestriction",
    jsii_struct_bases=[],
    name_mapping={"restriction_type": "restrictionType", "locations": "locations"},
)
class CloudfrontDistributionRestrictionsGeoRestriction:
    def __init__(
        self,
        *,
        restriction_type: builtins.str,
        locations: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param restriction_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#restriction_type CloudfrontDistribution#restriction_type}.
        :param locations: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#locations CloudfrontDistribution#locations}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5a642e581ef8b294cf3de7890d654cfe55897a554d5afe35fe045d1f3bf2254)
            check_type(argname="argument restriction_type", value=restriction_type, expected_type=type_hints["restriction_type"])
            check_type(argname="argument locations", value=locations, expected_type=type_hints["locations"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "restriction_type": restriction_type,
        }
        if locations is not None:
            self._values["locations"] = locations

    @builtins.property
    def restriction_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#restriction_type CloudfrontDistribution#restriction_type}.'''
        result = self._values.get("restriction_type")
        assert result is not None, "Required property 'restriction_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def locations(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#locations CloudfrontDistribution#locations}.'''
        result = self._values.get("locations")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudfrontDistributionRestrictionsGeoRestriction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudfrontDistributionRestrictionsGeoRestrictionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudfrontDistribution.CloudfrontDistributionRestrictionsGeoRestrictionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8fd45d7bcdfd6a3ded8949049a0e4820b9cdd1c647b081b9c10849543956f588)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetLocations")
    def reset_locations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocations", []))

    @builtins.property
    @jsii.member(jsii_name="locationsInput")
    def locations_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "locationsInput"))

    @builtins.property
    @jsii.member(jsii_name="restrictionTypeInput")
    def restriction_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "restrictionTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="locations")
    def locations(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "locations"))

    @locations.setter
    def locations(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5eb430631c16f8227ca02b712d8d333dc2fb7e12bdc5b48546d5052ed5ed2100)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "locations", value)

    @builtins.property
    @jsii.member(jsii_name="restrictionType")
    def restriction_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "restrictionType"))

    @restriction_type.setter
    def restriction_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dcfaabd9904b975a8fdd345e21d1c50cf718fdc0da3e30e9530672f77d4ca263)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "restrictionType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CloudfrontDistributionRestrictionsGeoRestriction]:
        return typing.cast(typing.Optional[CloudfrontDistributionRestrictionsGeoRestriction], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudfrontDistributionRestrictionsGeoRestriction],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70a20a448099ca51d77bbca68b105563b6944f40abc5500a8bb165fd86bb953a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CloudfrontDistributionRestrictionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudfrontDistribution.CloudfrontDistributionRestrictionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__24f1f3a8b859df16a9b92d755f4aaa6f7395bb1505ce33d4c66b284e3dab3a3a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putGeoRestriction")
    def put_geo_restriction(
        self,
        *,
        restriction_type: builtins.str,
        locations: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param restriction_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#restriction_type CloudfrontDistribution#restriction_type}.
        :param locations: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#locations CloudfrontDistribution#locations}.
        '''
        value = CloudfrontDistributionRestrictionsGeoRestriction(
            restriction_type=restriction_type, locations=locations
        )

        return typing.cast(None, jsii.invoke(self, "putGeoRestriction", [value]))

    @builtins.property
    @jsii.member(jsii_name="geoRestriction")
    def geo_restriction(
        self,
    ) -> CloudfrontDistributionRestrictionsGeoRestrictionOutputReference:
        return typing.cast(CloudfrontDistributionRestrictionsGeoRestrictionOutputReference, jsii.get(self, "geoRestriction"))

    @builtins.property
    @jsii.member(jsii_name="geoRestrictionInput")
    def geo_restriction_input(
        self,
    ) -> typing.Optional[CloudfrontDistributionRestrictionsGeoRestriction]:
        return typing.cast(typing.Optional[CloudfrontDistributionRestrictionsGeoRestriction], jsii.get(self, "geoRestrictionInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudfrontDistributionRestrictions]:
        return typing.cast(typing.Optional[CloudfrontDistributionRestrictions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudfrontDistributionRestrictions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8fca2ea15472eb2d3ec9b7286f9800ddb355fea4dec3c9524ccaaaf82e3a85a8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.cloudfrontDistribution.CloudfrontDistributionTrustedKeyGroups",
    jsii_struct_bases=[],
    name_mapping={},
)
class CloudfrontDistributionTrustedKeyGroups:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudfrontDistributionTrustedKeyGroups(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.cloudfrontDistribution.CloudfrontDistributionTrustedKeyGroupsItems",
    jsii_struct_bases=[],
    name_mapping={},
)
class CloudfrontDistributionTrustedKeyGroupsItems:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudfrontDistributionTrustedKeyGroupsItems(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudfrontDistributionTrustedKeyGroupsItemsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudfrontDistribution.CloudfrontDistributionTrustedKeyGroupsItemsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9db41a1233f968f7f072ddcd34e462323460fdde2ab8acf7a743eccb99595961)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CloudfrontDistributionTrustedKeyGroupsItemsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60c1e2e48890cbc84e048c4a11236fec3b4ad40be55660879ac336884918ca22)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CloudfrontDistributionTrustedKeyGroupsItemsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__10a65dc84d22d88c7b18cb05ff90d6d87b3d58856fc6ea4718ff8a1599b293f4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c19b8ec0e8aef6627444e6ca3c325ca09cb43e145be9bd95abeee54a6386b4fc)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6761b3ec8d13230a95abb50c47a2e3bcd570bb8da5955a87829fc6a803d0fdba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class CloudfrontDistributionTrustedKeyGroupsItemsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudfrontDistribution.CloudfrontDistributionTrustedKeyGroupsItemsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8c0568fdb802091697a264db653d5a169de31c1b193553dd0ab3ffd58bbc6535)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="keyGroupId")
    def key_group_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyGroupId"))

    @builtins.property
    @jsii.member(jsii_name="keyPairIds")
    def key_pair_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "keyPairIds"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CloudfrontDistributionTrustedKeyGroupsItems]:
        return typing.cast(typing.Optional[CloudfrontDistributionTrustedKeyGroupsItems], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudfrontDistributionTrustedKeyGroupsItems],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__832c1e347fba83399a803dedb59ebccdabc73c5d2e01137f2ac5c117d6203de2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CloudfrontDistributionTrustedKeyGroupsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudfrontDistribution.CloudfrontDistributionTrustedKeyGroupsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0775d65f85c07b062effd665ef1b0ef44c70b3f78c493d549302df016d062870)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CloudfrontDistributionTrustedKeyGroupsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fba33ea2adc5ad45ab6aa65ba954ffeed3a3954fb9370c0bb94f3739510a5dc7)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CloudfrontDistributionTrustedKeyGroupsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1150ba55ec75b45553838aca691c23f0d6681398b09fc7a327eab3fab9bd1daa)
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
            type_hints = typing.get_type_hints(_typecheckingstub__cc4cbfd6c2fe0ad9c5ce753089e9189138eddab2fc24dbe38e797dcf30f181ce)
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
            type_hints = typing.get_type_hints(_typecheckingstub__116070995b57419bff80c657c13ff00891ae57255bce9bf11c471207b3d10ab2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class CloudfrontDistributionTrustedKeyGroupsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudfrontDistribution.CloudfrontDistributionTrustedKeyGroupsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2ae69849a3af9359e6b1e88e7f86055edab02a3d281e5e786b167210de6f9402)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "enabled"))

    @builtins.property
    @jsii.member(jsii_name="items")
    def items(self) -> CloudfrontDistributionTrustedKeyGroupsItemsList:
        return typing.cast(CloudfrontDistributionTrustedKeyGroupsItemsList, jsii.get(self, "items"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudfrontDistributionTrustedKeyGroups]:
        return typing.cast(typing.Optional[CloudfrontDistributionTrustedKeyGroups], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudfrontDistributionTrustedKeyGroups],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b8c7bc72ae8c3efc3a1a4e7f373aec6c5efc7663a9105a326e1edbeda44880e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.cloudfrontDistribution.CloudfrontDistributionTrustedSigners",
    jsii_struct_bases=[],
    name_mapping={},
)
class CloudfrontDistributionTrustedSigners:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudfrontDistributionTrustedSigners(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.cloudfrontDistribution.CloudfrontDistributionTrustedSignersItems",
    jsii_struct_bases=[],
    name_mapping={},
)
class CloudfrontDistributionTrustedSignersItems:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudfrontDistributionTrustedSignersItems(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudfrontDistributionTrustedSignersItemsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudfrontDistribution.CloudfrontDistributionTrustedSignersItemsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__54c0596e83763857b6c36892bc786a70a40ae550c0fcd5b2284b6694ddc6307e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CloudfrontDistributionTrustedSignersItemsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__88491e1b0b84e9212336026105e64600967410857d9a59843320a4f8f8d904ef)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CloudfrontDistributionTrustedSignersItemsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b75e1f23b9a2eba57156529c9d850a54f0437889c5b07026c7b8db3371b1fa41)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f53261bac1494563f560520643881ea0410da1f8860aa363e307e13315fcd9a0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0d4f888d3df1ab52ece2c795a1fd4278aefd2348b1a7cc1df3e2ed10219d3086)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class CloudfrontDistributionTrustedSignersItemsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudfrontDistribution.CloudfrontDistributionTrustedSignersItemsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b9319fc32824455a6e71abb0d9617509f24e9c3ca44edf542e067b679efe2363)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="awsAccountNumber")
    def aws_account_number(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "awsAccountNumber"))

    @builtins.property
    @jsii.member(jsii_name="keyPairIds")
    def key_pair_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "keyPairIds"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CloudfrontDistributionTrustedSignersItems]:
        return typing.cast(typing.Optional[CloudfrontDistributionTrustedSignersItems], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudfrontDistributionTrustedSignersItems],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b80e68c4ccf8466d60fa4fb0dff51f846cb8f9546161093a98db6937e854af1f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CloudfrontDistributionTrustedSignersList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudfrontDistribution.CloudfrontDistributionTrustedSignersList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__52d9dd7599f527bcb377b524b009166a4d51a7d9daddef752e8c85be4cbc8407)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CloudfrontDistributionTrustedSignersOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4220956fb22e0edd61cf51a0a2a49056fbab19f246670cef3ff2d4ee6a5a1a95)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CloudfrontDistributionTrustedSignersOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2200c9f1f5a2ab3c04f71eca3cf495aefdef009447e420b1f346ef3c6083081f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__34b12b8e60710343c6013870b161b8ec1ed636c52c39ce7db4f85024c22c0d2d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ff986cac727bcf216289a378674afa3e47e3911ac44d240553513d1a7ba3c047)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class CloudfrontDistributionTrustedSignersOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudfrontDistribution.CloudfrontDistributionTrustedSignersOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__697bd4528cf47797fe84fb3abccac6c5f646e1afdb73d0e243ff54bf2f2ff9b9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "enabled"))

    @builtins.property
    @jsii.member(jsii_name="items")
    def items(self) -> CloudfrontDistributionTrustedSignersItemsList:
        return typing.cast(CloudfrontDistributionTrustedSignersItemsList, jsii.get(self, "items"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudfrontDistributionTrustedSigners]:
        return typing.cast(typing.Optional[CloudfrontDistributionTrustedSigners], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudfrontDistributionTrustedSigners],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a9ebde9536ed5a8b8450888c43d96a6e13e1578e5f502a88328a0cc1c77a1ba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.cloudfrontDistribution.CloudfrontDistributionViewerCertificate",
    jsii_struct_bases=[],
    name_mapping={
        "acm_certificate_arn": "acmCertificateArn",
        "cloudfront_default_certificate": "cloudfrontDefaultCertificate",
        "iam_certificate_id": "iamCertificateId",
        "minimum_protocol_version": "minimumProtocolVersion",
        "ssl_support_method": "sslSupportMethod",
    },
)
class CloudfrontDistributionViewerCertificate:
    def __init__(
        self,
        *,
        acm_certificate_arn: typing.Optional[builtins.str] = None,
        cloudfront_default_certificate: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        iam_certificate_id: typing.Optional[builtins.str] = None,
        minimum_protocol_version: typing.Optional[builtins.str] = None,
        ssl_support_method: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param acm_certificate_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#acm_certificate_arn CloudfrontDistribution#acm_certificate_arn}.
        :param cloudfront_default_certificate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#cloudfront_default_certificate CloudfrontDistribution#cloudfront_default_certificate}.
        :param iam_certificate_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#iam_certificate_id CloudfrontDistribution#iam_certificate_id}.
        :param minimum_protocol_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#minimum_protocol_version CloudfrontDistribution#minimum_protocol_version}.
        :param ssl_support_method: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#ssl_support_method CloudfrontDistribution#ssl_support_method}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a20fb77694bc650f679cf9a6a914b15dbfda3e686ce9bca0f0a2e91bc471e7fa)
            check_type(argname="argument acm_certificate_arn", value=acm_certificate_arn, expected_type=type_hints["acm_certificate_arn"])
            check_type(argname="argument cloudfront_default_certificate", value=cloudfront_default_certificate, expected_type=type_hints["cloudfront_default_certificate"])
            check_type(argname="argument iam_certificate_id", value=iam_certificate_id, expected_type=type_hints["iam_certificate_id"])
            check_type(argname="argument minimum_protocol_version", value=minimum_protocol_version, expected_type=type_hints["minimum_protocol_version"])
            check_type(argname="argument ssl_support_method", value=ssl_support_method, expected_type=type_hints["ssl_support_method"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if acm_certificate_arn is not None:
            self._values["acm_certificate_arn"] = acm_certificate_arn
        if cloudfront_default_certificate is not None:
            self._values["cloudfront_default_certificate"] = cloudfront_default_certificate
        if iam_certificate_id is not None:
            self._values["iam_certificate_id"] = iam_certificate_id
        if minimum_protocol_version is not None:
            self._values["minimum_protocol_version"] = minimum_protocol_version
        if ssl_support_method is not None:
            self._values["ssl_support_method"] = ssl_support_method

    @builtins.property
    def acm_certificate_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#acm_certificate_arn CloudfrontDistribution#acm_certificate_arn}.'''
        result = self._values.get("acm_certificate_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cloudfront_default_certificate(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#cloudfront_default_certificate CloudfrontDistribution#cloudfront_default_certificate}.'''
        result = self._values.get("cloudfront_default_certificate")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def iam_certificate_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#iam_certificate_id CloudfrontDistribution#iam_certificate_id}.'''
        result = self._values.get("iam_certificate_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def minimum_protocol_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#minimum_protocol_version CloudfrontDistribution#minimum_protocol_version}.'''
        result = self._values.get("minimum_protocol_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ssl_support_method(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution#ssl_support_method CloudfrontDistribution#ssl_support_method}.'''
        result = self._values.get("ssl_support_method")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudfrontDistributionViewerCertificate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudfrontDistributionViewerCertificateOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudfrontDistribution.CloudfrontDistributionViewerCertificateOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7bca6fdaaf12b42ee8c8bc4df125f73e8aee2d61063e4ce8fcc8d69a6dd42358)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAcmCertificateArn")
    def reset_acm_certificate_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAcmCertificateArn", []))

    @jsii.member(jsii_name="resetCloudfrontDefaultCertificate")
    def reset_cloudfront_default_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudfrontDefaultCertificate", []))

    @jsii.member(jsii_name="resetIamCertificateId")
    def reset_iam_certificate_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIamCertificateId", []))

    @jsii.member(jsii_name="resetMinimumProtocolVersion")
    def reset_minimum_protocol_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinimumProtocolVersion", []))

    @jsii.member(jsii_name="resetSslSupportMethod")
    def reset_ssl_support_method(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSslSupportMethod", []))

    @builtins.property
    @jsii.member(jsii_name="acmCertificateArnInput")
    def acm_certificate_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "acmCertificateArnInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudfrontDefaultCertificateInput")
    def cloudfront_default_certificate_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "cloudfrontDefaultCertificateInput"))

    @builtins.property
    @jsii.member(jsii_name="iamCertificateIdInput")
    def iam_certificate_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "iamCertificateIdInput"))

    @builtins.property
    @jsii.member(jsii_name="minimumProtocolVersionInput")
    def minimum_protocol_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "minimumProtocolVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="sslSupportMethodInput")
    def ssl_support_method_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sslSupportMethodInput"))

    @builtins.property
    @jsii.member(jsii_name="acmCertificateArn")
    def acm_certificate_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "acmCertificateArn"))

    @acm_certificate_arn.setter
    def acm_certificate_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ff529b519cd51d7e2331b9603afce3d19d863116be026f617a3ec0f44c2eafc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "acmCertificateArn", value)

    @builtins.property
    @jsii.member(jsii_name="cloudfrontDefaultCertificate")
    def cloudfront_default_certificate(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "cloudfrontDefaultCertificate"))

    @cloudfront_default_certificate.setter
    def cloudfront_default_certificate(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce1ef1e27cc5ccd954ca4d1240a5145ef97630d23d75044637698d11782b53b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloudfrontDefaultCertificate", value)

    @builtins.property
    @jsii.member(jsii_name="iamCertificateId")
    def iam_certificate_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "iamCertificateId"))

    @iam_certificate_id.setter
    def iam_certificate_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f6741d200db4b3e5c1cda160af39d9fde10ec07ebab93beb74c9a1323f09cfa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iamCertificateId", value)

    @builtins.property
    @jsii.member(jsii_name="minimumProtocolVersion")
    def minimum_protocol_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "minimumProtocolVersion"))

    @minimum_protocol_version.setter
    def minimum_protocol_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac554164a268244ad1086abb60d06e0beba5f3c7896cb52ba5504a91eed3260e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minimumProtocolVersion", value)

    @builtins.property
    @jsii.member(jsii_name="sslSupportMethod")
    def ssl_support_method(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sslSupportMethod"))

    @ssl_support_method.setter
    def ssl_support_method(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54357d7e6dc2e3cde65dde18a890bf7211309a26118a24b4d7dc4bd9c67083be)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sslSupportMethod", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CloudfrontDistributionViewerCertificate]:
        return typing.cast(typing.Optional[CloudfrontDistributionViewerCertificate], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudfrontDistributionViewerCertificate],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7cdc9ec5ad30d7b5e930c22a0431dc34759cf1214ae8b82338891906a54aaca6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "CloudfrontDistribution",
    "CloudfrontDistributionConfig",
    "CloudfrontDistributionCustomErrorResponse",
    "CloudfrontDistributionCustomErrorResponseList",
    "CloudfrontDistributionCustomErrorResponseOutputReference",
    "CloudfrontDistributionDefaultCacheBehavior",
    "CloudfrontDistributionDefaultCacheBehaviorForwardedValues",
    "CloudfrontDistributionDefaultCacheBehaviorForwardedValuesCookies",
    "CloudfrontDistributionDefaultCacheBehaviorForwardedValuesCookiesOutputReference",
    "CloudfrontDistributionDefaultCacheBehaviorForwardedValuesOutputReference",
    "CloudfrontDistributionDefaultCacheBehaviorFunctionAssociation",
    "CloudfrontDistributionDefaultCacheBehaviorFunctionAssociationList",
    "CloudfrontDistributionDefaultCacheBehaviorFunctionAssociationOutputReference",
    "CloudfrontDistributionDefaultCacheBehaviorLambdaFunctionAssociation",
    "CloudfrontDistributionDefaultCacheBehaviorLambdaFunctionAssociationList",
    "CloudfrontDistributionDefaultCacheBehaviorLambdaFunctionAssociationOutputReference",
    "CloudfrontDistributionDefaultCacheBehaviorOutputReference",
    "CloudfrontDistributionLoggingConfig",
    "CloudfrontDistributionLoggingConfigOutputReference",
    "CloudfrontDistributionOrderedCacheBehavior",
    "CloudfrontDistributionOrderedCacheBehaviorForwardedValues",
    "CloudfrontDistributionOrderedCacheBehaviorForwardedValuesCookies",
    "CloudfrontDistributionOrderedCacheBehaviorForwardedValuesCookiesOutputReference",
    "CloudfrontDistributionOrderedCacheBehaviorForwardedValuesOutputReference",
    "CloudfrontDistributionOrderedCacheBehaviorFunctionAssociation",
    "CloudfrontDistributionOrderedCacheBehaviorFunctionAssociationList",
    "CloudfrontDistributionOrderedCacheBehaviorFunctionAssociationOutputReference",
    "CloudfrontDistributionOrderedCacheBehaviorLambdaFunctionAssociation",
    "CloudfrontDistributionOrderedCacheBehaviorLambdaFunctionAssociationList",
    "CloudfrontDistributionOrderedCacheBehaviorLambdaFunctionAssociationOutputReference",
    "CloudfrontDistributionOrderedCacheBehaviorList",
    "CloudfrontDistributionOrderedCacheBehaviorOutputReference",
    "CloudfrontDistributionOrigin",
    "CloudfrontDistributionOriginCustomHeader",
    "CloudfrontDistributionOriginCustomHeaderList",
    "CloudfrontDistributionOriginCustomHeaderOutputReference",
    "CloudfrontDistributionOriginCustomOriginConfig",
    "CloudfrontDistributionOriginCustomOriginConfigOutputReference",
    "CloudfrontDistributionOriginGroup",
    "CloudfrontDistributionOriginGroupFailoverCriteria",
    "CloudfrontDistributionOriginGroupFailoverCriteriaOutputReference",
    "CloudfrontDistributionOriginGroupList",
    "CloudfrontDistributionOriginGroupMember",
    "CloudfrontDistributionOriginGroupMemberList",
    "CloudfrontDistributionOriginGroupMemberOutputReference",
    "CloudfrontDistributionOriginGroupOutputReference",
    "CloudfrontDistributionOriginList",
    "CloudfrontDistributionOriginOriginShield",
    "CloudfrontDistributionOriginOriginShieldOutputReference",
    "CloudfrontDistributionOriginOutputReference",
    "CloudfrontDistributionOriginS3OriginConfig",
    "CloudfrontDistributionOriginS3OriginConfigOutputReference",
    "CloudfrontDistributionRestrictions",
    "CloudfrontDistributionRestrictionsGeoRestriction",
    "CloudfrontDistributionRestrictionsGeoRestrictionOutputReference",
    "CloudfrontDistributionRestrictionsOutputReference",
    "CloudfrontDistributionTrustedKeyGroups",
    "CloudfrontDistributionTrustedKeyGroupsItems",
    "CloudfrontDistributionTrustedKeyGroupsItemsList",
    "CloudfrontDistributionTrustedKeyGroupsItemsOutputReference",
    "CloudfrontDistributionTrustedKeyGroupsList",
    "CloudfrontDistributionTrustedKeyGroupsOutputReference",
    "CloudfrontDistributionTrustedSigners",
    "CloudfrontDistributionTrustedSignersItems",
    "CloudfrontDistributionTrustedSignersItemsList",
    "CloudfrontDistributionTrustedSignersItemsOutputReference",
    "CloudfrontDistributionTrustedSignersList",
    "CloudfrontDistributionTrustedSignersOutputReference",
    "CloudfrontDistributionViewerCertificate",
    "CloudfrontDistributionViewerCertificateOutputReference",
]

publication.publish()

def _typecheckingstub__537c13993acd6e2b6c73b4161f7ac82b232baca0cf078fcc6e7ed3b5423fb000(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    default_cache_behavior: typing.Union[CloudfrontDistributionDefaultCacheBehavior, typing.Dict[builtins.str, typing.Any]],
    enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    origin: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CloudfrontDistributionOrigin, typing.Dict[builtins.str, typing.Any]]]],
    restrictions: typing.Union[CloudfrontDistributionRestrictions, typing.Dict[builtins.str, typing.Any]],
    viewer_certificate: typing.Union[CloudfrontDistributionViewerCertificate, typing.Dict[builtins.str, typing.Any]],
    aliases: typing.Optional[typing.Sequence[builtins.str]] = None,
    comment: typing.Optional[builtins.str] = None,
    custom_error_response: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CloudfrontDistributionCustomErrorResponse, typing.Dict[builtins.str, typing.Any]]]]] = None,
    default_root_object: typing.Optional[builtins.str] = None,
    http_version: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    is_ipv6_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    logging_config: typing.Optional[typing.Union[CloudfrontDistributionLoggingConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    ordered_cache_behavior: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CloudfrontDistributionOrderedCacheBehavior, typing.Dict[builtins.str, typing.Any]]]]] = None,
    origin_group: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CloudfrontDistributionOriginGroup, typing.Dict[builtins.str, typing.Any]]]]] = None,
    price_class: typing.Optional[builtins.str] = None,
    retain_on_delete: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    wait_for_deployment: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    web_acl_id: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__693fa4e944d0c071082304dfbddc46ac8859d49f45a0179496be98b02699d2b6(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CloudfrontDistributionCustomErrorResponse, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4da4967ed056af60178e962bbf55590811d5a4d38162b07225809bb4ada36a3(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CloudfrontDistributionOrderedCacheBehavior, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cbe4bfff05b454ee4d99df93a74777a058f1b0b9bb6f1cc766232e272c6c5333(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CloudfrontDistributionOrigin, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d2fa0f4a41e4ed0c0c5d2eade544bfb3566349ca184732b735e541b1556111f(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CloudfrontDistributionOriginGroup, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__880903284b6361d655958cf340fca71bfbf2d12834fd1f3295487b2ba57a6110(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a31205617d67931520bbe80122e2101b53b6013a30ef03733610878bf1b4efb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de53c6814589d594cc2261ef3600f9d3f83728dcac81719151f918ea38b84a82(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02a7ed2f90deaf58736e10a43b6939e6cf1919d5553df6722930d2f3ad52241a(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8431d65cf5912b4c51b1420923429f1608527c667f8ce54223d74d361a86baa8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__419ab06763abeca7768f8984a880fb3c25944a916aeeb695be40803d318ee420(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a00378c42f69ae7ed5c0c9ff0f10c027a2b0f0cc82273727dabfc0fb296d327(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cbd1fc8803d5fc465c175f89b742add0c745b0f11ceef7f837d088a95b4c33f4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c62290c7cff376845d83f4bc9713a5180f49f8a007b63841d6cd89f61a30520(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4785c3d897cc882173c87a2ca3255389fa01cd6b5da7e9d815096a210d057b7f(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d85f06a631beac96be0ccf53edff4bc69a098e97d828b1fbc861d925f26157f3(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__597d7c165716fa2b78bff43446959882e34ad910d58716b3e062d0bbd5e6151c(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45405caef5ded3a9f651185abec0c8ab174266ebeef752d10705431039715551(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22bf645392d91cb4c77981819d1bebb3d1ebaf238096601338826e0f4dfe96d4(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    default_cache_behavior: typing.Union[CloudfrontDistributionDefaultCacheBehavior, typing.Dict[builtins.str, typing.Any]],
    enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    origin: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CloudfrontDistributionOrigin, typing.Dict[builtins.str, typing.Any]]]],
    restrictions: typing.Union[CloudfrontDistributionRestrictions, typing.Dict[builtins.str, typing.Any]],
    viewer_certificate: typing.Union[CloudfrontDistributionViewerCertificate, typing.Dict[builtins.str, typing.Any]],
    aliases: typing.Optional[typing.Sequence[builtins.str]] = None,
    comment: typing.Optional[builtins.str] = None,
    custom_error_response: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CloudfrontDistributionCustomErrorResponse, typing.Dict[builtins.str, typing.Any]]]]] = None,
    default_root_object: typing.Optional[builtins.str] = None,
    http_version: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    is_ipv6_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    logging_config: typing.Optional[typing.Union[CloudfrontDistributionLoggingConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    ordered_cache_behavior: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CloudfrontDistributionOrderedCacheBehavior, typing.Dict[builtins.str, typing.Any]]]]] = None,
    origin_group: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CloudfrontDistributionOriginGroup, typing.Dict[builtins.str, typing.Any]]]]] = None,
    price_class: typing.Optional[builtins.str] = None,
    retain_on_delete: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    wait_for_deployment: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    web_acl_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__daa368baa7d9046da2a0318670f62d735ea039b65bfbe1a2ae53bc84abc27956(
    *,
    error_code: jsii.Number,
    error_caching_min_ttl: typing.Optional[jsii.Number] = None,
    response_code: typing.Optional[jsii.Number] = None,
    response_page_path: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__633e263ac6985420932ddfd32bdd08a7087ee1794f804ab6db6677b28cde94f6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80a8e9eb951084dacc5b0dfb269185f2d4a3f37db978cd586a1e62c770d83652(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__adbe2a5fdeba767dd0290e74dd25b7655f597e934753a51ea210992a96176664(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22c90344449458364212d5cc4e9d03a7ea020fc9ffa1dfcb2bfe82403955bcaa(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b35cc896b128e9b25b90a803bb1fc4a12fc1949d858f89aaeefbc2b0d09a919d(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a016707f9007118c8bda4ac7847108657f3ec01219ec97293a771ac56906f344(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudfrontDistributionCustomErrorResponse]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3606cb1226e879de02f613da9b68bb21e3467d459bc8909b0cf2cae9a89832bb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bcfc25ebd380547c66edcbd48d677d01ae2404f5c3dd55089740e6de39dbf5c1(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cad4122c69ea74c47c40234835ec0208af9072c04226fc043b490b6a2a139f85(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c84a9ed6d65aa0c5f503e9bf6e2b08f46a2128fd8c3020273e4be168655c87e(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f2cb8e3054e49adb5871e1c95ad82e10f38ed1c3657f801cd54ad2ec805fe95(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82c48b1462e82b4ef78339473501af98133dbdde909f696164e9410121f1ff2f(
    value: typing.Optional[typing.Union[CloudfrontDistributionCustomErrorResponse, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7ce19f434f14df24b5610bb2a84ca6e6b1e4b5d7c563fc1bd58897fff4a7c18(
    *,
    allowed_methods: typing.Sequence[builtins.str],
    cached_methods: typing.Sequence[builtins.str],
    target_origin_id: builtins.str,
    viewer_protocol_policy: builtins.str,
    cache_policy_id: typing.Optional[builtins.str] = None,
    compress: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    default_ttl: typing.Optional[jsii.Number] = None,
    field_level_encryption_id: typing.Optional[builtins.str] = None,
    forwarded_values: typing.Optional[typing.Union[CloudfrontDistributionDefaultCacheBehaviorForwardedValues, typing.Dict[builtins.str, typing.Any]]] = None,
    function_association: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CloudfrontDistributionDefaultCacheBehaviorFunctionAssociation, typing.Dict[builtins.str, typing.Any]]]]] = None,
    lambda_function_association: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CloudfrontDistributionDefaultCacheBehaviorLambdaFunctionAssociation, typing.Dict[builtins.str, typing.Any]]]]] = None,
    max_ttl: typing.Optional[jsii.Number] = None,
    min_ttl: typing.Optional[jsii.Number] = None,
    origin_request_policy_id: typing.Optional[builtins.str] = None,
    realtime_log_config_arn: typing.Optional[builtins.str] = None,
    response_headers_policy_id: typing.Optional[builtins.str] = None,
    smooth_streaming: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    trusted_key_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    trusted_signers: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32c0244c6329ab1f5bd1778295ea5772539953da641f2c3bfdfa424e8380a63d(
    *,
    cookies: typing.Union[CloudfrontDistributionDefaultCacheBehaviorForwardedValuesCookies, typing.Dict[builtins.str, typing.Any]],
    query_string: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    headers: typing.Optional[typing.Sequence[builtins.str]] = None,
    query_string_cache_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9b5ee965da4e227472844199d0141043eeb43482ab93cbadfbb104429af0727(
    *,
    forward: builtins.str,
    whitelisted_names: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8705ba1d7060c4304029e79ee5629d4c29844fc055923f83de2687ff83c12d27(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c40ad7ba30ed69132a8f85ae9c0a9ac178e4e06d9d9ad6fc78140ba72d142f52(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba777e24aa27c1f34e6f04e8aeece19b53f7120b4a9267fdc8f8fce906f19926(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38ace5aea34273e6f8a19d7981ad49ca437ce8d2673ab5485468bc9c7cce30d5(
    value: typing.Optional[CloudfrontDistributionDefaultCacheBehaviorForwardedValuesCookies],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2d80065eac04f24401c049629dbd5cd15498a04f1f808227a75e75f3150406f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__683c2cb22fef7d4e7fa7fdff30de52c8e0fcaad62678dad44ea0ce525991e660(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c93b43ac5303a4a811af6e2e2dd6d9e6c79abc601a537fe75115990c915d01d1(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa6f87aee5ac0b42c0be6e87795bc9a5e93110cf28c217ab880a0c7c4fbc540d(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__800fbd874547e66952cdf76101fbf23320360bf12bed45c73aea6c2b66701072(
    value: typing.Optional[CloudfrontDistributionDefaultCacheBehaviorForwardedValues],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fee9f2389b6cf80b8418d8dc60c8e04eeb057d4f34433f7e8e0f709481749f6e(
    *,
    event_type: builtins.str,
    function_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9948262e42a36b73d14176c6f2c87df0163f57ddb4cb980e2aabada0bf295ffb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c883336c1dc2288f780e842b2f3705d642338b428f36ce9d45a66293c1cab63(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e47a8408991769a1ab26a9adc0bdd50248fb139f4277cb12d581e3284df6bc72(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23e71d29162584f4492089dd3d0b0dcc472cf93bcbf8cf378c217bf7c5d90241(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e05ad474fc839ecdf8c629f2e662ec1f727e2a5f544f6f78f3cae27f3f1a76f3(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f065a66935b2d0edc4ee8fea733751fb8a1d1ad62e37d7dff1a2ce694b805c6(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudfrontDistributionDefaultCacheBehaviorFunctionAssociation]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99f4bfba5c044b8ee7010e7bb3ade131300a7c65032294cf012fafb3f28ccd63(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7786aae39efd09cabf832eef0a97d397e35a58cfd7fed28f11e6e0112619108(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97bc4343d8812353cfce955215af54f5cf017c238fcf69dca5a5776a8773bfa3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf906a49e43493df0484f58e3c77fb9d5f270137989e60b966ae21d0f7e903ab(
    value: typing.Optional[typing.Union[CloudfrontDistributionDefaultCacheBehaviorFunctionAssociation, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3472d6b8fe9ba0216ebbfdd868fbbbc07a33032238a98fd96ffd360b01c7fb7(
    *,
    event_type: builtins.str,
    lambda_arn: builtins.str,
    include_body: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bca0f1e0ec94d3a9ae48da3b8fab014eff80c84fe60d868bd02d42509e7178de(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3876c9b5019a0d0d3eb0f24674bf0704fd35efec4545f3774e0aca7104d96fa6(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b8e54f4abba733e387303b819a2f1c61e130d923b26c26b3b40508bfe9b7bc8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9446a31b9454daa70b3a6f05491652cda2286d9c55ebeb7295bb33cf3638a6d(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98627b8809b90911ba9a2a274a5d274b928d42d8a3d2afd15d141b9f6482505a(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__497b47d03e90006f00eeb2d7a1e68fa04177cea7f7cd6b81dd6228fad9231721(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudfrontDistributionDefaultCacheBehaviorLambdaFunctionAssociation]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd37c7c646a342d806a8706e639b4f4440d6708c9b35564f56be1368a74c1226(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5c2061a6228c62c5731d5298fbb0e76c52be091ee9ce92f0231f2d291a065c0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d48c16f2981054966ad7cd99e5aa32c0cbcc638f6e09d44ffa33ab6e418fcb72(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cabd54e303c6aaec377d106c71529e715a540bfe5d380ebc41c14635f422f733(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bfc00ee98b5222a310511df2428a280e3891053052850db39e11cadf8d8567dd(
    value: typing.Optional[typing.Union[CloudfrontDistributionDefaultCacheBehaviorLambdaFunctionAssociation, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59b1bfb95cd89c4c42f0499aeb704e5126d23f3239ecdee8cebf41b73177ee40(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9229ffea0d2ddc99c8363ccf81572e056bd996192fd848e1bf2e4fc38cb0368f(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CloudfrontDistributionDefaultCacheBehaviorFunctionAssociation, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b9011554a08df3f7d6e8d0714e2bfbd8adeca2c6a861f5dfc2c203ae9f71dfd(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CloudfrontDistributionDefaultCacheBehaviorLambdaFunctionAssociation, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c972c76f72ad2b1c60863449078a064430ebe9865d003833693117246b6f1caf(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3dcfe43aa61805a48eb996e90f5e1a55655d0fab89694570d38681a1eb3cee3b(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb16eeceb7f614e206be080d90cbc9ac1130decee370919f637850eaf877a9ca(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f41a048dd0752bd0b972efc840edf65f00973f95e3a906a589bce6332f332f54(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04e628a96879405c6487ca5cfeb96ff564f2c7d3dbc9a93775220b048280f085(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68e92d6ac6a6a77b67a88ea5263c47bf66611f89a3bdddafee0a86a50a426117(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70272ab108bf356b355081a53010a28ebfec499acc2bb9df4d44fc8492292146(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6f3886a15ea4e4de36f6ebd4d41b63646438e841f99ee30eb2fcb722349d815(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__199c533f5182a780a9c29a44a6f1872b1dd552ca28902e38a5bbdac018664a43(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6c913fa81a523bc5a73637d1d0016d7552f1de6bbf15f49ad92e4e5ab3a3ef4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dca01e70bd2c85ffa4d2cd82feff88bf32384068f736e34a9e4062dad8b9b137(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc38bc2a8b9ad56990e02427ce6302654c99514bfb230523d404369570cd69de(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd1240d7f89ec6ff3ae288a7ff5e5eaebf82cbccb39290c50ffe62292288867e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b11a5b95dbb82269d872958247dca536ea4876e1ed306df90cf72b40f8d786f0(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5afa0606b4cb75e58cfb7d73f787294fced8b9c74e6ec8d4efab7941359a47c(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68316f637f40dc4555d8746e4dd55a761af563405b58babab846cd3fdb457372(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04828e2fa534f1bf31ef620ebeaee1fd2b1b5d3f32d446b92e65853f143b3665(
    value: typing.Optional[CloudfrontDistributionDefaultCacheBehavior],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12d2ca1030ac013f6642613003d9f796dd82c8935f5565affcde5865574653f0(
    *,
    bucket: builtins.str,
    include_cookies: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f860702edbfe54150a805805bf7958bd96e6ccad1e2a0343352923887b663ff9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b76c85551bf1475d28b7442c5ac982e34052688204cd817fecacedf7d83808e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9534feae03baecef18168a317cd83aa1e87bb3277fbf3275ef7a68873b74cd71(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d63fdbb6ecf89c5d1656967a835d030547a0e7c080edd0df6b847400727e0a3a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4caff979ef0377faebca058a139f1bc8fd1a184b56820772d3271c03382cf2bd(
    value: typing.Optional[CloudfrontDistributionLoggingConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e273b6f1df93b6d65a5092b6435802b9966220740c99956a848379fcfa6e45d(
    *,
    allowed_methods: typing.Sequence[builtins.str],
    cached_methods: typing.Sequence[builtins.str],
    path_pattern: builtins.str,
    target_origin_id: builtins.str,
    viewer_protocol_policy: builtins.str,
    cache_policy_id: typing.Optional[builtins.str] = None,
    compress: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    default_ttl: typing.Optional[jsii.Number] = None,
    field_level_encryption_id: typing.Optional[builtins.str] = None,
    forwarded_values: typing.Optional[typing.Union[CloudfrontDistributionOrderedCacheBehaviorForwardedValues, typing.Dict[builtins.str, typing.Any]]] = None,
    function_association: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CloudfrontDistributionOrderedCacheBehaviorFunctionAssociation, typing.Dict[builtins.str, typing.Any]]]]] = None,
    lambda_function_association: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CloudfrontDistributionOrderedCacheBehaviorLambdaFunctionAssociation, typing.Dict[builtins.str, typing.Any]]]]] = None,
    max_ttl: typing.Optional[jsii.Number] = None,
    min_ttl: typing.Optional[jsii.Number] = None,
    origin_request_policy_id: typing.Optional[builtins.str] = None,
    realtime_log_config_arn: typing.Optional[builtins.str] = None,
    response_headers_policy_id: typing.Optional[builtins.str] = None,
    smooth_streaming: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    trusted_key_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    trusted_signers: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3780e0b8953bc4223510eb375ff5715f8007e7cb2b1efa2210f425a89766db93(
    *,
    cookies: typing.Union[CloudfrontDistributionOrderedCacheBehaviorForwardedValuesCookies, typing.Dict[builtins.str, typing.Any]],
    query_string: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    headers: typing.Optional[typing.Sequence[builtins.str]] = None,
    query_string_cache_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1b2d919b8b47540a017171b76aa2e4085ea3162c9c50a51f2af2c8500b14efc(
    *,
    forward: builtins.str,
    whitelisted_names: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8965c40f5a63fed98e431da08e97b2f2a9625bdc80bbf4e3f5b29dc4f5514588(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bfe033ef2c79f2c011d434ca150ccd0fde2756d165c6e32b2045c5b4928ee6b1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ec7eb662cfe0d81b485c032a43c046705aa67f11adf443f0a11d5de11c705fb(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf849be92617487529b8176a2ab671b39c76db02a1080633fe899b611907e17e(
    value: typing.Optional[CloudfrontDistributionOrderedCacheBehaviorForwardedValuesCookies],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e52a0798780040a4547091af8ed48a37fdeeadd069afea3681b0bbe784c9a9d1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed1e642cd391edaca3656bce62cddca9d03b5f7d8b8cb8a3005ea513bb4bdd05(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb0b2d38c28dc055ac7c4f5c7cd10a73a8880f1374c2ad6dab8b5c1e496cc0d3(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9befc798becce42c05e20f04f2d97633cb39edc93a1f2eaaff52e0cef7bb8961(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84136ddc41493ccf0db91caea5be01be7fab7c67ecbf8bf8976d2981d12cadf8(
    value: typing.Optional[CloudfrontDistributionOrderedCacheBehaviorForwardedValues],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7fa18092e6db691f05024d5c4e04d36235901654fab7957c57b9b1d1d0ad98be(
    *,
    event_type: builtins.str,
    function_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce7c5e1c88326285a748aea9f35eb74db652b96d6d7ae4c074a93db33d8d2c92(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8adf3dfe8530c86b08a18c17941f57b680db75e0fe5c9a4d89ad7466db4f32fe(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f1be4fa81b8ab14c3d8bcbc2aa000d09304939358e09ea77995bd0af2fe1b33(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5fe267dc49a848dd27da899169a3cd66c1b0d6c1809dde812b7fcd24b0acadec(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6eb11b90a10e73b1b99f1af7052c65e5a597ef30295aed54224ecef97136a77d(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1a2900e98fadc49c13503d515d8f5d120b4fe619a53eabd270f261554291371(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudfrontDistributionOrderedCacheBehaviorFunctionAssociation]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2ba9c310252074c49e24b8921630d301a0d793be2178208d5a09bb1852fd8bf(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92f014b9dcf204e695a5704537fe2569e68a711af3ff9a1d17db72fb1fd8135a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3c0ea8db2a99e26430d868b9d59e37aa751a4e68d633150290de429fe3fef5b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f09b4e700ada5bc5ceeeaecff6c3da071afb87dcd675ee091c78ecb9262a8c2f(
    value: typing.Optional[typing.Union[CloudfrontDistributionOrderedCacheBehaviorFunctionAssociation, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0a47d97b9faf5cbd2f85255ae8201a22a8ba344846c1c606399e820ac451cea(
    *,
    event_type: builtins.str,
    lambda_arn: builtins.str,
    include_body: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b04e9bfe78566907c8bb01689abf6b813ab6fe32a2e35ba60937f2afffe65be(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3a344bf8e8a059eca0577263dfe265778cfef39b37fc556c2b728135f8a1256(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed1b230e8acf203af42d4cf45b6fb630f644c3c0e24e74a31ce9a2cbb39559b2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6298d340ad72e30d30b103d436098c1c3f76493e9faa87ab6bd02c41657f2d3f(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f6d815a1ef89bcdf07edbb7490ff16116d5620ccf60b65d7ac74f814a08e8d5(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b3e1762cbda2aeb5687c604572ee9f97acf1e008812d868da0d17502071882b(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudfrontDistributionOrderedCacheBehaviorLambdaFunctionAssociation]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__789db6741347b5ee6c61905254b8ba9c88d772a4f28f0707a6290406294c69e4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c327bd81c482913e4bcc2f95c4b48c0334c3694ae1252ca7859ff72f3cb04da(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__742c9d8d6ba2af3e9e88378338637e7d2f00fe55a7311a2ad4586a5f41881e97(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5cc493571d698c073258669f75f55c8df37ba9cab3846738c45c18ef4c431dc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62ee907dd71aee932817acfd09286d798389d42546de5fbdc401633560a952fd(
    value: typing.Optional[typing.Union[CloudfrontDistributionOrderedCacheBehaviorLambdaFunctionAssociation, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dcd5bdb7812ba840ce14b1c27fb5d42984a4d51089beadafe2108542ba47c8c4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96b160213a5b2874716440902daa19e0694995820dc919bef2105bff1fdea21a(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d16031b5d30cf2e83914fde6a4da3a24ef310ed71883d97a371c1fed00386d3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5548e92edf59a1cca67a7ed60848eb71ade87aa6b76540fdad55e6807f62fdc7(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5eb9db426a38e1ce3c806a9cfe085f5543b3e90ae844e7225e58d66931916f64(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17604b0799b625c9fa655e371d2aee3a566e0e9e133649ed2941c616f58c9f0c(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudfrontDistributionOrderedCacheBehavior]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7740a74d0291fb4012f4d353f080c1e482aedfe13d463f266670b9b138f0092e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e9be6db719998525bf117a414902460902d99597247667e73ba605e62c2fa75(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CloudfrontDistributionOrderedCacheBehaviorFunctionAssociation, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f86a2f4137386d5b0c6cda651373cac7adf64226f4a1d039cc4137e06adcbf6(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CloudfrontDistributionOrderedCacheBehaviorLambdaFunctionAssociation, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__efe75f58f6188697ef9161e88ff6795ed860072425fa27966b865d8a8b2defc3(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23726b41986053453dc9fd4169e63955d265cdf19840ffdd0ece4f0836383f9b(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d666a23655f4178032a7b00ce438be1b6f2d877ad522fb2a54beb4de8d47c4f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91aae853eb8249f006a00369df774623df55e667bc49c2f5340697d207df7f3b(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c474c8952fb26283944a007931e4945a67ff11986b2a869f4b3003c7df2ae53b(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__124ca773a0c9ab078d2f0fa543aeadf90d3c388864e32000077bf7b581ccb12a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb78edcd094cbbc3b9b28612f526eb6a94ad8ceef4586f9360addc547c8f476d(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3eebf10d5aafbe047e7a42b5a4b63216cb198a557074a29b5e3753c420e2d489(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7b4a650064fe13f180f0a82efc7e3865db41298163a8e7ec32d4e6963b652be(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6eca684f8adf1e0b4aef6eac6ca2ad395d55c7c4cd0b43c2666c998c7456c16a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f996058de4327e38a824f991df6104ebc7cf916dee0129f90f09ac69d188a38(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21c7c292d60f4fcf6c3ba8b2de218b2eb1d6dc5ca1d45091a2d35e23ec3cba62(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bed2443db2d81d9b6d80c22291e41eb2bb42308ab5b7f62e464b5200321c1894(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68676854f27256ac96c572b3a6b1b950960918890aadc232da754dbce788be44(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6880f4f4e781f7e0150f680f720f1b7e6553dc3f47dddfc838dd560180bd288(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0dc8e6ca9d42b4ec398010dcc6590e264992d4a05434ad554c8100bf32b5c2dc(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b0dad78e2ab314372558800880d4f5467b13f3e9e34816fe6c7ee1267b208dc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8576cf6f90608fbf0e2a5537c4000591faf425874d7a9ae1ed00c13804352f0c(
    value: typing.Optional[typing.Union[CloudfrontDistributionOrderedCacheBehavior, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b808442a6ef14fc07d0f5af787f52233c2dcf77539a594f88535b9639a92792f(
    *,
    domain_name: builtins.str,
    origin_id: builtins.str,
    connection_attempts: typing.Optional[jsii.Number] = None,
    connection_timeout: typing.Optional[jsii.Number] = None,
    custom_header: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CloudfrontDistributionOriginCustomHeader, typing.Dict[builtins.str, typing.Any]]]]] = None,
    custom_origin_config: typing.Optional[typing.Union[CloudfrontDistributionOriginCustomOriginConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    origin_access_control_id: typing.Optional[builtins.str] = None,
    origin_path: typing.Optional[builtins.str] = None,
    origin_shield: typing.Optional[typing.Union[CloudfrontDistributionOriginOriginShield, typing.Dict[builtins.str, typing.Any]]] = None,
    s3_origin_config: typing.Optional[typing.Union[CloudfrontDistributionOriginS3OriginConfig, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__579181c64ec8f90df065081148caef31163070545cf601e50c2de093d31676ba(
    *,
    name: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c59407230a488bd4c755890a3accb238be78d3ac6e65440eac0aae2e72349615(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__979dacfc0e93be6e474dc1f93c92431e326f2d535dd585ed9f38f02a9cf0dff6(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0cd9a86ae1ed0c834e428ddd7ed73df432d46082e48c7ac58a5a46c63430a36a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd6c3986ca4e6a284acc4144424eb0345f766cdd9fee9be548e269c88d45e133(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33542556960a2c4287edbcdebd503d050597e5dfb69d616a1fb30d790a612de3(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__812828a9ceff14818e51a2d8f6c17248b30f59f506cd33af14ecab63764ee40a(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudfrontDistributionOriginCustomHeader]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ad23ab58881099e60ac6207dd2ec336a72a03c077f2aac3cb7b5f939c3c0c40(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7865cc0dea616de689141609333235284982b862f039e00ed8844a675dbc0eff(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eafd7a5abe591a61771fcc7ddd17829e99e4111953c8984acbc805d3847d3d99(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af8912530ff476a195efd201f560086e7f702ae6ab717121176d06e2837349b4(
    value: typing.Optional[typing.Union[CloudfrontDistributionOriginCustomHeader, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e1cafb27d80c969a9f71593aae3f7de481fa1c76669c8d9312d35b154bf2b91(
    *,
    http_port: jsii.Number,
    https_port: jsii.Number,
    origin_protocol_policy: builtins.str,
    origin_ssl_protocols: typing.Sequence[builtins.str],
    origin_keepalive_timeout: typing.Optional[jsii.Number] = None,
    origin_read_timeout: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7add305d98c92836576bb1d390703206e9880992db0de2543bf9bdf45107432(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10d829c8ad4c733655bfe30cfd93ddde26bfcabb8846b7b5b32685087d5e7f5d(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__991f75bf433e60657e3adb68416d4647f282da8479069516635cfd8190afac2c(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b5793bc43b613703676dbbe986b1641fdf5b0ee622c20cc4e64813162e5bceb(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8c5d6f39d05b539d418c8b105318f36bfc56db5ea68d8017f78d4a00b821eea(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bcde30b53d5d917d56a725e20094f90378b153999713c39aa6081eca356c262d(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__508c4e282d93fa604bb0688d16263695a5a1c0b8dd90aa93347ef220f04df8c7(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9cadbf12563ac7cc36066eb0d14c25645617472f3ff61976e7825f6cd35cffea(
    value: typing.Optional[CloudfrontDistributionOriginCustomOriginConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc04b96358869b5364bd8c269ee6b6c71053dda6dc3a1be6284ddf361cbb20e4(
    *,
    failover_criteria: typing.Union[CloudfrontDistributionOriginGroupFailoverCriteria, typing.Dict[builtins.str, typing.Any]],
    member: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CloudfrontDistributionOriginGroupMember, typing.Dict[builtins.str, typing.Any]]]],
    origin_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59023e9e148360643b46f004cc5742b8ca7ea4995bd2570fba048c0f10b4a9df(
    *,
    status_codes: typing.Sequence[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d62f83f8dc9b0b3984bc64e3bfac1bd6ec0c60379e35eb407046687cf2725b43(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d1758d94456df292d1fd56325892f706e5bf0ba1a9a51416820f8c6c372b5b8(
    value: typing.List[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e5c34efe96089d3ef457e590de2f0a310d929eabea91f7536b5ca992f949380(
    value: typing.Optional[CloudfrontDistributionOriginGroupFailoverCriteria],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5137c6197b4b45c9b54949f88db591fe6979fbe05f59213c03a19fc118fb2a72(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08116efd1a7473d132f4c5d02e5b3b36aeb3ee59e64bcc07de110d9e0f724679(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85945881f0a9fee99750eb178703dec676d34384bf087948fadd32f7165d2600(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8d6d6e12aab76792d64e6c79531a373a4396f46c75fe36961b0fec0efc1851b(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__463d3cb2de5d43b94df86267284f9c89a891552a2208dbc47101ce08c430e5a0(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be7a30cf7f8a3599afead8602c5e44661423e2d1aae44a77a08403bc834fdb76(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudfrontDistributionOriginGroup]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7fe0f88b7d8c3bd8c44aba6125d20bb7848ac6f67144ec40b421c4f9390a2d87(
    *,
    origin_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c62a792adc112cca90a643e415e5179f6d191a972e0e496282c18f3543fac5c9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4803e520be380f5141472de6d7a8ffd56986b332ba57fd14fb583b1de55bb996(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25917340dd733d361481593b20358f31845fbf024fce70303d9f0209425c3717(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc64d9c31299858928b527311f8d6a721220efa0aa75079a02d0ed932404632d(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__072c53f4b705facbd90c150e8f7f634187aa4327639370f91e8f599ba5beed1a(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8bf30fcd1d12624f437f10f913fbd2cc5231c3a27cae47954d7b0cc2cbb1935(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudfrontDistributionOriginGroupMember]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__599d4dd353ad4bcc07553a81f49cdfa3b403c541fa2b2f12c32481f2c45ccf3b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6267103d3ac7a2d983d0f406d52dd10c69a7275b4b8cf498a8832622cf55e6bb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afb5405582c708c204378146416c09a7e24bc371e13205028bfe24080c17613d(
    value: typing.Optional[typing.Union[CloudfrontDistributionOriginGroupMember, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ccb9244e9435c8aee4568669c9f99bae1fe355f9e2f394052edf0aa83c1c881(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eff3f1ebc767b5deeada406ddf49ac4e182127f521abdcdb531541c22b7ec3c2(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CloudfrontDistributionOriginGroupMember, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09aeb9f9998c85b6d420489a79791b04602dbe7e5e63572466b16175e74830ed(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1fce33bfe861a4dd7a2e50880d071565f54332cf84542e18b573872fa4107142(
    value: typing.Optional[typing.Union[CloudfrontDistributionOriginGroup, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7af76aa4ea97f351edc98d75d933a8ca0d793766a4ff9821dbc676c528b48bd9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42fe36656f725503148a3f03663a459ad5fb81b848fc9c281cbcc2deded84cdc(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9986a24fb96a32e242a8e19c9ee8f3d0a930b7dcad58bd819481b5511a3af56(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5cc0bba837a2c9940294574e58ac0099ed2bae8f8c5f68bf06698f3632f774d(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe4ab87419be423cc35ce4b454a988162badc33ca31e90bfaff2cfe369b057ca(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2ab681fe6c6be72e4031f6a864b1aa1f0fa308b3d04e4b633c34dee6f4dacf6(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudfrontDistributionOrigin]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd06853bd7033a230725168881d5aa736a42908355746ea572e7919f48af9ecf(
    *,
    enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    origin_shield_region: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17f2a025ca3e6c8e1ba034a715f412b819e707b6352ee181f19cfa2eec91d4c4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9cdb6c0f846a3b4d75943ae17ba8ac186f64a35d6fe90e3f9cfc32e73a628e1(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79cab0b73298ed4a11a8d44562f68ee567cbabe5bff761318af33add4f4c3190(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea3a7fe5311ea0c2e0f69cd80198ede4fc7f85afc0bc576c9a9aba6bc55a754b(
    value: typing.Optional[CloudfrontDistributionOriginOriginShield],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd8f1ac7ffd05ae0cdbbf65c42fb1e7d4ec09bf45abd0449e857c1d81d98d6b2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__572820daf473d586693b72e9f643426fc21cc1dde1798631c97047f9f521d50a(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CloudfrontDistributionOriginCustomHeader, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55f1426c535904823863416136c389b1ff30ef1e8552e1a29d05a4942e65bdc0(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__494f8a87c0013faa4c5b18ed9b246e105094884ce18bf808402e527b0ebd14f5(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0d6ddc4b56ebcf40d04f0b48c68f1c249e65d4366ff9f5539105812c5f4f065(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5115d98b1f84f5918660aea6b135eac1db8c486d3b930813c2e5ff101f140acb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4eef73c3a096a6eb19e167ee36179943866789de3e6305792e653a950b69e2ac(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b16ae66620556373b974af369f6f0dfbcb342f7fd4703ef5d30239a68074a6c2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__daa5a7e8b36cee38ad2b97b2af9a954ff87e4464f79ec93c95a1389b83680b03(
    value: typing.Optional[typing.Union[CloudfrontDistributionOrigin, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ebe800d16183e3db4ec4cf14fb934dab246867cf488c17bdd08b2e2eccab0065(
    *,
    origin_access_identity: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e45ca5716ef1d47c9915b444f0dcd00c92569c81ce276c95be5d96c45c0c1fe2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0429d864931bbc21bc6c9e0a5e2c8cac591986526557406833d8d2e81e5d65d6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa52e356ea656c22aa32ba52f3711e4ad45e23edbc30b8ef3a645d4658fe0fb9(
    value: typing.Optional[CloudfrontDistributionOriginS3OriginConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad26c3ce4fe5e6ab55d24b6eb1debdeb90e1a04e4406bbf2a0aecfe6e353e7f6(
    *,
    geo_restriction: typing.Union[CloudfrontDistributionRestrictionsGeoRestriction, typing.Dict[builtins.str, typing.Any]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5a642e581ef8b294cf3de7890d654cfe55897a554d5afe35fe045d1f3bf2254(
    *,
    restriction_type: builtins.str,
    locations: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8fd45d7bcdfd6a3ded8949049a0e4820b9cdd1c647b081b9c10849543956f588(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5eb430631c16f8227ca02b712d8d333dc2fb7e12bdc5b48546d5052ed5ed2100(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dcfaabd9904b975a8fdd345e21d1c50cf718fdc0da3e30e9530672f77d4ca263(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70a20a448099ca51d77bbca68b105563b6944f40abc5500a8bb165fd86bb953a(
    value: typing.Optional[CloudfrontDistributionRestrictionsGeoRestriction],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24f1f3a8b859df16a9b92d755f4aaa6f7395bb1505ce33d4c66b284e3dab3a3a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8fca2ea15472eb2d3ec9b7286f9800ddb355fea4dec3c9524ccaaaf82e3a85a8(
    value: typing.Optional[CloudfrontDistributionRestrictions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9db41a1233f968f7f072ddcd34e462323460fdde2ab8acf7a743eccb99595961(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60c1e2e48890cbc84e048c4a11236fec3b4ad40be55660879ac336884918ca22(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10a65dc84d22d88c7b18cb05ff90d6d87b3d58856fc6ea4718ff8a1599b293f4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c19b8ec0e8aef6627444e6ca3c325ca09cb43e145be9bd95abeee54a6386b4fc(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6761b3ec8d13230a95abb50c47a2e3bcd570bb8da5955a87829fc6a803d0fdba(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c0568fdb802091697a264db653d5a169de31c1b193553dd0ab3ffd58bbc6535(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__832c1e347fba83399a803dedb59ebccdabc73c5d2e01137f2ac5c117d6203de2(
    value: typing.Optional[CloudfrontDistributionTrustedKeyGroupsItems],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0775d65f85c07b062effd665ef1b0ef44c70b3f78c493d549302df016d062870(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fba33ea2adc5ad45ab6aa65ba954ffeed3a3954fb9370c0bb94f3739510a5dc7(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1150ba55ec75b45553838aca691c23f0d6681398b09fc7a327eab3fab9bd1daa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc4cbfd6c2fe0ad9c5ce753089e9189138eddab2fc24dbe38e797dcf30f181ce(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__116070995b57419bff80c657c13ff00891ae57255bce9bf11c471207b3d10ab2(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ae69849a3af9359e6b1e88e7f86055edab02a3d281e5e786b167210de6f9402(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b8c7bc72ae8c3efc3a1a4e7f373aec6c5efc7663a9105a326e1edbeda44880e(
    value: typing.Optional[CloudfrontDistributionTrustedKeyGroups],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54c0596e83763857b6c36892bc786a70a40ae550c0fcd5b2284b6694ddc6307e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88491e1b0b84e9212336026105e64600967410857d9a59843320a4f8f8d904ef(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b75e1f23b9a2eba57156529c9d850a54f0437889c5b07026c7b8db3371b1fa41(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f53261bac1494563f560520643881ea0410da1f8860aa363e307e13315fcd9a0(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d4f888d3df1ab52ece2c795a1fd4278aefd2348b1a7cc1df3e2ed10219d3086(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9319fc32824455a6e71abb0d9617509f24e9c3ca44edf542e067b679efe2363(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b80e68c4ccf8466d60fa4fb0dff51f846cb8f9546161093a98db6937e854af1f(
    value: typing.Optional[CloudfrontDistributionTrustedSignersItems],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52d9dd7599f527bcb377b524b009166a4d51a7d9daddef752e8c85be4cbc8407(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4220956fb22e0edd61cf51a0a2a49056fbab19f246670cef3ff2d4ee6a5a1a95(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2200c9f1f5a2ab3c04f71eca3cf495aefdef009447e420b1f346ef3c6083081f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34b12b8e60710343c6013870b161b8ec1ed636c52c39ce7db4f85024c22c0d2d(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff986cac727bcf216289a378674afa3e47e3911ac44d240553513d1a7ba3c047(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__697bd4528cf47797fe84fb3abccac6c5f646e1afdb73d0e243ff54bf2f2ff9b9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a9ebde9536ed5a8b8450888c43d96a6e13e1578e5f502a88328a0cc1c77a1ba(
    value: typing.Optional[CloudfrontDistributionTrustedSigners],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a20fb77694bc650f679cf9a6a914b15dbfda3e686ce9bca0f0a2e91bc471e7fa(
    *,
    acm_certificate_arn: typing.Optional[builtins.str] = None,
    cloudfront_default_certificate: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    iam_certificate_id: typing.Optional[builtins.str] = None,
    minimum_protocol_version: typing.Optional[builtins.str] = None,
    ssl_support_method: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7bca6fdaaf12b42ee8c8bc4df125f73e8aee2d61063e4ce8fcc8d69a6dd42358(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ff529b519cd51d7e2331b9603afce3d19d863116be026f617a3ec0f44c2eafc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce1ef1e27cc5ccd954ca4d1240a5145ef97630d23d75044637698d11782b53b4(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f6741d200db4b3e5c1cda160af39d9fde10ec07ebab93beb74c9a1323f09cfa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac554164a268244ad1086abb60d06e0beba5f3c7896cb52ba5504a91eed3260e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54357d7e6dc2e3cde65dde18a890bf7211309a26118a24b4d7dc4bd9c67083be(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7cdc9ec5ad30d7b5e930c22a0431dc34759cf1214ae8b82338891906a54aaca6(
    value: typing.Optional[CloudfrontDistributionViewerCertificate],
) -> None:
    """Type checking stubs"""
    pass
