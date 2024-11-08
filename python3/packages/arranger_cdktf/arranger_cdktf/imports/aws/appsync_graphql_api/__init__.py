'''
# `aws_appsync_graphql_api`

Refer to the Terraform Registory for docs: [`aws_appsync_graphql_api`](https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api).
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


class AppsyncGraphqlApi(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appsyncGraphqlApi.AppsyncGraphqlApi",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api aws_appsync_graphql_api}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        authentication_type: builtins.str,
        name: builtins.str,
        additional_authentication_provider: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["AppsyncGraphqlApiAdditionalAuthenticationProvider", typing.Dict[builtins.str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        lambda_authorizer_config: typing.Optional[typing.Union["AppsyncGraphqlApiLambdaAuthorizerConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        log_config: typing.Optional[typing.Union["AppsyncGraphqlApiLogConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        openid_connect_config: typing.Optional[typing.Union["AppsyncGraphqlApiOpenidConnectConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        schema: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        user_pool_config: typing.Optional[typing.Union["AppsyncGraphqlApiUserPoolConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        xray_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api aws_appsync_graphql_api} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param authentication_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#authentication_type AppsyncGraphqlApi#authentication_type}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#name AppsyncGraphqlApi#name}.
        :param additional_authentication_provider: additional_authentication_provider block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#additional_authentication_provider AppsyncGraphqlApi#additional_authentication_provider}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#id AppsyncGraphqlApi#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param lambda_authorizer_config: lambda_authorizer_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#lambda_authorizer_config AppsyncGraphqlApi#lambda_authorizer_config}
        :param log_config: log_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#log_config AppsyncGraphqlApi#log_config}
        :param openid_connect_config: openid_connect_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#openid_connect_config AppsyncGraphqlApi#openid_connect_config}
        :param schema: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#schema AppsyncGraphqlApi#schema}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#tags AppsyncGraphqlApi#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#tags_all AppsyncGraphqlApi#tags_all}.
        :param user_pool_config: user_pool_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#user_pool_config AppsyncGraphqlApi#user_pool_config}
        :param xray_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#xray_enabled AppsyncGraphqlApi#xray_enabled}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b1a34e24e4ecb77f94a4b7290523974e81ede49c5c2680b9673de754702cdf9)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = AppsyncGraphqlApiConfig(
            authentication_type=authentication_type,
            name=name,
            additional_authentication_provider=additional_authentication_provider,
            id=id,
            lambda_authorizer_config=lambda_authorizer_config,
            log_config=log_config,
            openid_connect_config=openid_connect_config,
            schema=schema,
            tags=tags,
            tags_all=tags_all,
            user_pool_config=user_pool_config,
            xray_enabled=xray_enabled,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAdditionalAuthenticationProvider")
    def put_additional_authentication_provider(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["AppsyncGraphqlApiAdditionalAuthenticationProvider", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d22f3cd5becc11aac2f69743221ed57a1d4da2a90136c7bee1f6c30becc6ca92)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAdditionalAuthenticationProvider", [value]))

    @jsii.member(jsii_name="putLambdaAuthorizerConfig")
    def put_lambda_authorizer_config(
        self,
        *,
        authorizer_uri: builtins.str,
        authorizer_result_ttl_in_seconds: typing.Optional[jsii.Number] = None,
        identity_validation_expression: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param authorizer_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#authorizer_uri AppsyncGraphqlApi#authorizer_uri}.
        :param authorizer_result_ttl_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#authorizer_result_ttl_in_seconds AppsyncGraphqlApi#authorizer_result_ttl_in_seconds}.
        :param identity_validation_expression: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#identity_validation_expression AppsyncGraphqlApi#identity_validation_expression}.
        '''
        value = AppsyncGraphqlApiLambdaAuthorizerConfig(
            authorizer_uri=authorizer_uri,
            authorizer_result_ttl_in_seconds=authorizer_result_ttl_in_seconds,
            identity_validation_expression=identity_validation_expression,
        )

        return typing.cast(None, jsii.invoke(self, "putLambdaAuthorizerConfig", [value]))

    @jsii.member(jsii_name="putLogConfig")
    def put_log_config(
        self,
        *,
        cloudwatch_logs_role_arn: builtins.str,
        field_log_level: builtins.str,
        exclude_verbose_content: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param cloudwatch_logs_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#cloudwatch_logs_role_arn AppsyncGraphqlApi#cloudwatch_logs_role_arn}.
        :param field_log_level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#field_log_level AppsyncGraphqlApi#field_log_level}.
        :param exclude_verbose_content: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#exclude_verbose_content AppsyncGraphqlApi#exclude_verbose_content}.
        '''
        value = AppsyncGraphqlApiLogConfig(
            cloudwatch_logs_role_arn=cloudwatch_logs_role_arn,
            field_log_level=field_log_level,
            exclude_verbose_content=exclude_verbose_content,
        )

        return typing.cast(None, jsii.invoke(self, "putLogConfig", [value]))

    @jsii.member(jsii_name="putOpenidConnectConfig")
    def put_openid_connect_config(
        self,
        *,
        issuer: builtins.str,
        auth_ttl: typing.Optional[jsii.Number] = None,
        client_id: typing.Optional[builtins.str] = None,
        iat_ttl: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param issuer: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#issuer AppsyncGraphqlApi#issuer}.
        :param auth_ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#auth_ttl AppsyncGraphqlApi#auth_ttl}.
        :param client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#client_id AppsyncGraphqlApi#client_id}.
        :param iat_ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#iat_ttl AppsyncGraphqlApi#iat_ttl}.
        '''
        value = AppsyncGraphqlApiOpenidConnectConfig(
            issuer=issuer, auth_ttl=auth_ttl, client_id=client_id, iat_ttl=iat_ttl
        )

        return typing.cast(None, jsii.invoke(self, "putOpenidConnectConfig", [value]))

    @jsii.member(jsii_name="putUserPoolConfig")
    def put_user_pool_config(
        self,
        *,
        default_action: builtins.str,
        user_pool_id: builtins.str,
        app_id_client_regex: typing.Optional[builtins.str] = None,
        aws_region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param default_action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#default_action AppsyncGraphqlApi#default_action}.
        :param user_pool_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#user_pool_id AppsyncGraphqlApi#user_pool_id}.
        :param app_id_client_regex: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#app_id_client_regex AppsyncGraphqlApi#app_id_client_regex}.
        :param aws_region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#aws_region AppsyncGraphqlApi#aws_region}.
        '''
        value = AppsyncGraphqlApiUserPoolConfig(
            default_action=default_action,
            user_pool_id=user_pool_id,
            app_id_client_regex=app_id_client_regex,
            aws_region=aws_region,
        )

        return typing.cast(None, jsii.invoke(self, "putUserPoolConfig", [value]))

    @jsii.member(jsii_name="resetAdditionalAuthenticationProvider")
    def reset_additional_authentication_provider(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdditionalAuthenticationProvider", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLambdaAuthorizerConfig")
    def reset_lambda_authorizer_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLambdaAuthorizerConfig", []))

    @jsii.member(jsii_name="resetLogConfig")
    def reset_log_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogConfig", []))

    @jsii.member(jsii_name="resetOpenidConnectConfig")
    def reset_openid_connect_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOpenidConnectConfig", []))

    @jsii.member(jsii_name="resetSchema")
    def reset_schema(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSchema", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetUserPoolConfig")
    def reset_user_pool_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserPoolConfig", []))

    @jsii.member(jsii_name="resetXrayEnabled")
    def reset_xray_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetXrayEnabled", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="additionalAuthenticationProvider")
    def additional_authentication_provider(
        self,
    ) -> "AppsyncGraphqlApiAdditionalAuthenticationProviderList":
        return typing.cast("AppsyncGraphqlApiAdditionalAuthenticationProviderList", jsii.get(self, "additionalAuthenticationProvider"))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="lambdaAuthorizerConfig")
    def lambda_authorizer_config(
        self,
    ) -> "AppsyncGraphqlApiLambdaAuthorizerConfigOutputReference":
        return typing.cast("AppsyncGraphqlApiLambdaAuthorizerConfigOutputReference", jsii.get(self, "lambdaAuthorizerConfig"))

    @builtins.property
    @jsii.member(jsii_name="logConfig")
    def log_config(self) -> "AppsyncGraphqlApiLogConfigOutputReference":
        return typing.cast("AppsyncGraphqlApiLogConfigOutputReference", jsii.get(self, "logConfig"))

    @builtins.property
    @jsii.member(jsii_name="openidConnectConfig")
    def openid_connect_config(
        self,
    ) -> "AppsyncGraphqlApiOpenidConnectConfigOutputReference":
        return typing.cast("AppsyncGraphqlApiOpenidConnectConfigOutputReference", jsii.get(self, "openidConnectConfig"))

    @builtins.property
    @jsii.member(jsii_name="uris")
    def uris(self) -> _cdktf_9a9027ec.StringMap:
        return typing.cast(_cdktf_9a9027ec.StringMap, jsii.get(self, "uris"))

    @builtins.property
    @jsii.member(jsii_name="userPoolConfig")
    def user_pool_config(self) -> "AppsyncGraphqlApiUserPoolConfigOutputReference":
        return typing.cast("AppsyncGraphqlApiUserPoolConfigOutputReference", jsii.get(self, "userPoolConfig"))

    @builtins.property
    @jsii.member(jsii_name="additionalAuthenticationProviderInput")
    def additional_authentication_provider_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AppsyncGraphqlApiAdditionalAuthenticationProvider"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AppsyncGraphqlApiAdditionalAuthenticationProvider"]]], jsii.get(self, "additionalAuthenticationProviderInput"))

    @builtins.property
    @jsii.member(jsii_name="authenticationTypeInput")
    def authentication_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authenticationTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="lambdaAuthorizerConfigInput")
    def lambda_authorizer_config_input(
        self,
    ) -> typing.Optional["AppsyncGraphqlApiLambdaAuthorizerConfig"]:
        return typing.cast(typing.Optional["AppsyncGraphqlApiLambdaAuthorizerConfig"], jsii.get(self, "lambdaAuthorizerConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="logConfigInput")
    def log_config_input(self) -> typing.Optional["AppsyncGraphqlApiLogConfig"]:
        return typing.cast(typing.Optional["AppsyncGraphqlApiLogConfig"], jsii.get(self, "logConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="openidConnectConfigInput")
    def openid_connect_config_input(
        self,
    ) -> typing.Optional["AppsyncGraphqlApiOpenidConnectConfig"]:
        return typing.cast(typing.Optional["AppsyncGraphqlApiOpenidConnectConfig"], jsii.get(self, "openidConnectConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="schemaInput")
    def schema_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "schemaInput"))

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
    @jsii.member(jsii_name="userPoolConfigInput")
    def user_pool_config_input(
        self,
    ) -> typing.Optional["AppsyncGraphqlApiUserPoolConfig"]:
        return typing.cast(typing.Optional["AppsyncGraphqlApiUserPoolConfig"], jsii.get(self, "userPoolConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="xrayEnabledInput")
    def xray_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "xrayEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="authenticationType")
    def authentication_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authenticationType"))

    @authentication_type.setter
    def authentication_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0434458a270cd4c322a10da94f955dd06696b4805536dc2687ec0334fcc6488f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authenticationType", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f3fce342308f1087946d8f2dc37269259162733b211ed68a306b4cddcd127599)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ecedb068407c4d8af8436e1f5de6a2e2dd1e66ec9745453b41bead429ff90fa8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="schema")
    def schema(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "schema"))

    @schema.setter
    def schema(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1bacba8a99c5793613fbeaf6a6068c36b88d32996da9367697490b0798259d73)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schema", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__202e8d4473b03aab739ab0fe3b3814ba31b16faf6aedb6e1dc151dc390df6860)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2942adcba69973f0ff64b04d5c330e68cd1d3e267ca05f3db4f1766bd2b84435)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)

    @builtins.property
    @jsii.member(jsii_name="xrayEnabled")
    def xray_enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "xrayEnabled"))

    @xray_enabled.setter
    def xray_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53041cc9b24097abc2fe0d927e5b6e0f2c91c5a2f9dde6ddb1508c6dadc7fdf0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "xrayEnabled", value)


@jsii.data_type(
    jsii_type="aws.appsyncGraphqlApi.AppsyncGraphqlApiAdditionalAuthenticationProvider",
    jsii_struct_bases=[],
    name_mapping={
        "authentication_type": "authenticationType",
        "lambda_authorizer_config": "lambdaAuthorizerConfig",
        "openid_connect_config": "openidConnectConfig",
        "user_pool_config": "userPoolConfig",
    },
)
class AppsyncGraphqlApiAdditionalAuthenticationProvider:
    def __init__(
        self,
        *,
        authentication_type: builtins.str,
        lambda_authorizer_config: typing.Optional[typing.Union["AppsyncGraphqlApiAdditionalAuthenticationProviderLambdaAuthorizerConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        openid_connect_config: typing.Optional[typing.Union["AppsyncGraphqlApiAdditionalAuthenticationProviderOpenidConnectConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        user_pool_config: typing.Optional[typing.Union["AppsyncGraphqlApiAdditionalAuthenticationProviderUserPoolConfig", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param authentication_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#authentication_type AppsyncGraphqlApi#authentication_type}.
        :param lambda_authorizer_config: lambda_authorizer_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#lambda_authorizer_config AppsyncGraphqlApi#lambda_authorizer_config}
        :param openid_connect_config: openid_connect_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#openid_connect_config AppsyncGraphqlApi#openid_connect_config}
        :param user_pool_config: user_pool_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#user_pool_config AppsyncGraphqlApi#user_pool_config}
        '''
        if isinstance(lambda_authorizer_config, dict):
            lambda_authorizer_config = AppsyncGraphqlApiAdditionalAuthenticationProviderLambdaAuthorizerConfig(**lambda_authorizer_config)
        if isinstance(openid_connect_config, dict):
            openid_connect_config = AppsyncGraphqlApiAdditionalAuthenticationProviderOpenidConnectConfig(**openid_connect_config)
        if isinstance(user_pool_config, dict):
            user_pool_config = AppsyncGraphqlApiAdditionalAuthenticationProviderUserPoolConfig(**user_pool_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1fef41dea32bc2860defc6d68a0080d08f0f1a0374642eb0fa725bad5049888e)
            check_type(argname="argument authentication_type", value=authentication_type, expected_type=type_hints["authentication_type"])
            check_type(argname="argument lambda_authorizer_config", value=lambda_authorizer_config, expected_type=type_hints["lambda_authorizer_config"])
            check_type(argname="argument openid_connect_config", value=openid_connect_config, expected_type=type_hints["openid_connect_config"])
            check_type(argname="argument user_pool_config", value=user_pool_config, expected_type=type_hints["user_pool_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "authentication_type": authentication_type,
        }
        if lambda_authorizer_config is not None:
            self._values["lambda_authorizer_config"] = lambda_authorizer_config
        if openid_connect_config is not None:
            self._values["openid_connect_config"] = openid_connect_config
        if user_pool_config is not None:
            self._values["user_pool_config"] = user_pool_config

    @builtins.property
    def authentication_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#authentication_type AppsyncGraphqlApi#authentication_type}.'''
        result = self._values.get("authentication_type")
        assert result is not None, "Required property 'authentication_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def lambda_authorizer_config(
        self,
    ) -> typing.Optional["AppsyncGraphqlApiAdditionalAuthenticationProviderLambdaAuthorizerConfig"]:
        '''lambda_authorizer_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#lambda_authorizer_config AppsyncGraphqlApi#lambda_authorizer_config}
        '''
        result = self._values.get("lambda_authorizer_config")
        return typing.cast(typing.Optional["AppsyncGraphqlApiAdditionalAuthenticationProviderLambdaAuthorizerConfig"], result)

    @builtins.property
    def openid_connect_config(
        self,
    ) -> typing.Optional["AppsyncGraphqlApiAdditionalAuthenticationProviderOpenidConnectConfig"]:
        '''openid_connect_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#openid_connect_config AppsyncGraphqlApi#openid_connect_config}
        '''
        result = self._values.get("openid_connect_config")
        return typing.cast(typing.Optional["AppsyncGraphqlApiAdditionalAuthenticationProviderOpenidConnectConfig"], result)

    @builtins.property
    def user_pool_config(
        self,
    ) -> typing.Optional["AppsyncGraphqlApiAdditionalAuthenticationProviderUserPoolConfig"]:
        '''user_pool_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#user_pool_config AppsyncGraphqlApi#user_pool_config}
        '''
        result = self._values.get("user_pool_config")
        return typing.cast(typing.Optional["AppsyncGraphqlApiAdditionalAuthenticationProviderUserPoolConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppsyncGraphqlApiAdditionalAuthenticationProvider(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appsyncGraphqlApi.AppsyncGraphqlApiAdditionalAuthenticationProviderLambdaAuthorizerConfig",
    jsii_struct_bases=[],
    name_mapping={
        "authorizer_uri": "authorizerUri",
        "authorizer_result_ttl_in_seconds": "authorizerResultTtlInSeconds",
        "identity_validation_expression": "identityValidationExpression",
    },
)
class AppsyncGraphqlApiAdditionalAuthenticationProviderLambdaAuthorizerConfig:
    def __init__(
        self,
        *,
        authorizer_uri: builtins.str,
        authorizer_result_ttl_in_seconds: typing.Optional[jsii.Number] = None,
        identity_validation_expression: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param authorizer_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#authorizer_uri AppsyncGraphqlApi#authorizer_uri}.
        :param authorizer_result_ttl_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#authorizer_result_ttl_in_seconds AppsyncGraphqlApi#authorizer_result_ttl_in_seconds}.
        :param identity_validation_expression: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#identity_validation_expression AppsyncGraphqlApi#identity_validation_expression}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__69f66dc9fca88d321d473b1b9de41d1380f1ce01d2ba816cb39f6c1892632a2d)
            check_type(argname="argument authorizer_uri", value=authorizer_uri, expected_type=type_hints["authorizer_uri"])
            check_type(argname="argument authorizer_result_ttl_in_seconds", value=authorizer_result_ttl_in_seconds, expected_type=type_hints["authorizer_result_ttl_in_seconds"])
            check_type(argname="argument identity_validation_expression", value=identity_validation_expression, expected_type=type_hints["identity_validation_expression"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "authorizer_uri": authorizer_uri,
        }
        if authorizer_result_ttl_in_seconds is not None:
            self._values["authorizer_result_ttl_in_seconds"] = authorizer_result_ttl_in_seconds
        if identity_validation_expression is not None:
            self._values["identity_validation_expression"] = identity_validation_expression

    @builtins.property
    def authorizer_uri(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#authorizer_uri AppsyncGraphqlApi#authorizer_uri}.'''
        result = self._values.get("authorizer_uri")
        assert result is not None, "Required property 'authorizer_uri' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def authorizer_result_ttl_in_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#authorizer_result_ttl_in_seconds AppsyncGraphqlApi#authorizer_result_ttl_in_seconds}.'''
        result = self._values.get("authorizer_result_ttl_in_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def identity_validation_expression(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#identity_validation_expression AppsyncGraphqlApi#identity_validation_expression}.'''
        result = self._values.get("identity_validation_expression")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppsyncGraphqlApiAdditionalAuthenticationProviderLambdaAuthorizerConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppsyncGraphqlApiAdditionalAuthenticationProviderLambdaAuthorizerConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appsyncGraphqlApi.AppsyncGraphqlApiAdditionalAuthenticationProviderLambdaAuthorizerConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__620bc731715a89ff080e52e826de078a7179156b81903550740b4f47db57dc10)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAuthorizerResultTtlInSeconds")
    def reset_authorizer_result_ttl_in_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthorizerResultTtlInSeconds", []))

    @jsii.member(jsii_name="resetIdentityValidationExpression")
    def reset_identity_validation_expression(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentityValidationExpression", []))

    @builtins.property
    @jsii.member(jsii_name="authorizerResultTtlInSecondsInput")
    def authorizer_result_ttl_in_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "authorizerResultTtlInSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="authorizerUriInput")
    def authorizer_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authorizerUriInput"))

    @builtins.property
    @jsii.member(jsii_name="identityValidationExpressionInput")
    def identity_validation_expression_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "identityValidationExpressionInput"))

    @builtins.property
    @jsii.member(jsii_name="authorizerResultTtlInSeconds")
    def authorizer_result_ttl_in_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "authorizerResultTtlInSeconds"))

    @authorizer_result_ttl_in_seconds.setter
    def authorizer_result_ttl_in_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c9299d4d4f4282ae613febbf1854546cf89da6fa74fc9cf248b56274ec42b22)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authorizerResultTtlInSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="authorizerUri")
    def authorizer_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authorizerUri"))

    @authorizer_uri.setter
    def authorizer_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e9a011855ae5d434796efc86db82fc92557712e05da8e8eebae50c82bbbeebd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authorizerUri", value)

    @builtins.property
    @jsii.member(jsii_name="identityValidationExpression")
    def identity_validation_expression(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "identityValidationExpression"))

    @identity_validation_expression.setter
    def identity_validation_expression(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e44ceccafdfab349258b2bc34ed8c64c942ed44e803b16436dbde739f10aa92d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityValidationExpression", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppsyncGraphqlApiAdditionalAuthenticationProviderLambdaAuthorizerConfig]:
        return typing.cast(typing.Optional[AppsyncGraphqlApiAdditionalAuthenticationProviderLambdaAuthorizerConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppsyncGraphqlApiAdditionalAuthenticationProviderLambdaAuthorizerConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4724fb48c019b4428723d296ba5b6c80284fb8eae918984160f3b7cc3b915dee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppsyncGraphqlApiAdditionalAuthenticationProviderList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appsyncGraphqlApi.AppsyncGraphqlApiAdditionalAuthenticationProviderList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__fc4a31a7fea2dc0e68ea3c756370f168caee26f25c5969b3469480c929f42c28)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "AppsyncGraphqlApiAdditionalAuthenticationProviderOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f7c47086be47925fd6a3b3f63c14733ac15c9c60937b723a28c4ebe0c69dadeb)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AppsyncGraphqlApiAdditionalAuthenticationProviderOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9fb7b03066ff1e4925faa739d5ac3d85a382192e94fb93718c4d284fa283a61)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3852c5a690b7a7eb501759ea7401d012782f14e859c6351dbad702c09ffd2d31)
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
            type_hints = typing.get_type_hints(_typecheckingstub__798b8bf319e6422a0af0539b43dc6359caf792a25c88c5858fefcf29d177b7d6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppsyncGraphqlApiAdditionalAuthenticationProvider]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppsyncGraphqlApiAdditionalAuthenticationProvider]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppsyncGraphqlApiAdditionalAuthenticationProvider]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e81d27ce849a8d8a686ce8a2703837e9ba88e4415d74c66585fe8a101bdcae5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appsyncGraphqlApi.AppsyncGraphqlApiAdditionalAuthenticationProviderOpenidConnectConfig",
    jsii_struct_bases=[],
    name_mapping={
        "issuer": "issuer",
        "auth_ttl": "authTtl",
        "client_id": "clientId",
        "iat_ttl": "iatTtl",
    },
)
class AppsyncGraphqlApiAdditionalAuthenticationProviderOpenidConnectConfig:
    def __init__(
        self,
        *,
        issuer: builtins.str,
        auth_ttl: typing.Optional[jsii.Number] = None,
        client_id: typing.Optional[builtins.str] = None,
        iat_ttl: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param issuer: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#issuer AppsyncGraphqlApi#issuer}.
        :param auth_ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#auth_ttl AppsyncGraphqlApi#auth_ttl}.
        :param client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#client_id AppsyncGraphqlApi#client_id}.
        :param iat_ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#iat_ttl AppsyncGraphqlApi#iat_ttl}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__898165341f00f84ca1cba6b225b6e7bfb7ba056130ccff6dbd79e405ff7f1d1b)
            check_type(argname="argument issuer", value=issuer, expected_type=type_hints["issuer"])
            check_type(argname="argument auth_ttl", value=auth_ttl, expected_type=type_hints["auth_ttl"])
            check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
            check_type(argname="argument iat_ttl", value=iat_ttl, expected_type=type_hints["iat_ttl"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "issuer": issuer,
        }
        if auth_ttl is not None:
            self._values["auth_ttl"] = auth_ttl
        if client_id is not None:
            self._values["client_id"] = client_id
        if iat_ttl is not None:
            self._values["iat_ttl"] = iat_ttl

    @builtins.property
    def issuer(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#issuer AppsyncGraphqlApi#issuer}.'''
        result = self._values.get("issuer")
        assert result is not None, "Required property 'issuer' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def auth_ttl(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#auth_ttl AppsyncGraphqlApi#auth_ttl}.'''
        result = self._values.get("auth_ttl")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def client_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#client_id AppsyncGraphqlApi#client_id}.'''
        result = self._values.get("client_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def iat_ttl(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#iat_ttl AppsyncGraphqlApi#iat_ttl}.'''
        result = self._values.get("iat_ttl")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppsyncGraphqlApiAdditionalAuthenticationProviderOpenidConnectConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppsyncGraphqlApiAdditionalAuthenticationProviderOpenidConnectConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appsyncGraphqlApi.AppsyncGraphqlApiAdditionalAuthenticationProviderOpenidConnectConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a2c754f7f2df89404d8021c25a14da516aef338a4444aa078e77272d00f3588b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAuthTtl")
    def reset_auth_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthTtl", []))

    @jsii.member(jsii_name="resetClientId")
    def reset_client_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientId", []))

    @jsii.member(jsii_name="resetIatTtl")
    def reset_iat_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIatTtl", []))

    @builtins.property
    @jsii.member(jsii_name="authTtlInput")
    def auth_ttl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "authTtlInput"))

    @builtins.property
    @jsii.member(jsii_name="clientIdInput")
    def client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="iatTtlInput")
    def iat_ttl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "iatTtlInput"))

    @builtins.property
    @jsii.member(jsii_name="issuerInput")
    def issuer_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "issuerInput"))

    @builtins.property
    @jsii.member(jsii_name="authTtl")
    def auth_ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "authTtl"))

    @auth_ttl.setter
    def auth_ttl(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7498b9e24a81d67bf46bd313a6ef8172f621304b2bb5c7c222a407bdd03342c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authTtl", value)

    @builtins.property
    @jsii.member(jsii_name="clientId")
    def client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientId"))

    @client_id.setter
    def client_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c458e67045b2e5a5e900221a10ac9fa43d682e7b32f1ce14fe88ef0a3a2a431)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientId", value)

    @builtins.property
    @jsii.member(jsii_name="iatTtl")
    def iat_ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "iatTtl"))

    @iat_ttl.setter
    def iat_ttl(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce277e8b9fb0dec3e4bac1bff5aa007cb357962e7ab9969098a0e27e413326bb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iatTtl", value)

    @builtins.property
    @jsii.member(jsii_name="issuer")
    def issuer(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "issuer"))

    @issuer.setter
    def issuer(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a193b440b1c14088bc034ef3baaac9f7cb4c36fff439580c6a6a9314f99a716)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "issuer", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppsyncGraphqlApiAdditionalAuthenticationProviderOpenidConnectConfig]:
        return typing.cast(typing.Optional[AppsyncGraphqlApiAdditionalAuthenticationProviderOpenidConnectConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppsyncGraphqlApiAdditionalAuthenticationProviderOpenidConnectConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aadd7ca1c32ef4362015261061d4e9752186456e5d942bffaeb9054efaa1e33d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppsyncGraphqlApiAdditionalAuthenticationProviderOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appsyncGraphqlApi.AppsyncGraphqlApiAdditionalAuthenticationProviderOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__683824807154119cb210b87c1ae922a943d57e9af9ba1278b0aba1dc73de92c9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putLambdaAuthorizerConfig")
    def put_lambda_authorizer_config(
        self,
        *,
        authorizer_uri: builtins.str,
        authorizer_result_ttl_in_seconds: typing.Optional[jsii.Number] = None,
        identity_validation_expression: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param authorizer_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#authorizer_uri AppsyncGraphqlApi#authorizer_uri}.
        :param authorizer_result_ttl_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#authorizer_result_ttl_in_seconds AppsyncGraphqlApi#authorizer_result_ttl_in_seconds}.
        :param identity_validation_expression: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#identity_validation_expression AppsyncGraphqlApi#identity_validation_expression}.
        '''
        value = AppsyncGraphqlApiAdditionalAuthenticationProviderLambdaAuthorizerConfig(
            authorizer_uri=authorizer_uri,
            authorizer_result_ttl_in_seconds=authorizer_result_ttl_in_seconds,
            identity_validation_expression=identity_validation_expression,
        )

        return typing.cast(None, jsii.invoke(self, "putLambdaAuthorizerConfig", [value]))

    @jsii.member(jsii_name="putOpenidConnectConfig")
    def put_openid_connect_config(
        self,
        *,
        issuer: builtins.str,
        auth_ttl: typing.Optional[jsii.Number] = None,
        client_id: typing.Optional[builtins.str] = None,
        iat_ttl: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param issuer: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#issuer AppsyncGraphqlApi#issuer}.
        :param auth_ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#auth_ttl AppsyncGraphqlApi#auth_ttl}.
        :param client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#client_id AppsyncGraphqlApi#client_id}.
        :param iat_ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#iat_ttl AppsyncGraphqlApi#iat_ttl}.
        '''
        value = AppsyncGraphqlApiAdditionalAuthenticationProviderOpenidConnectConfig(
            issuer=issuer, auth_ttl=auth_ttl, client_id=client_id, iat_ttl=iat_ttl
        )

        return typing.cast(None, jsii.invoke(self, "putOpenidConnectConfig", [value]))

    @jsii.member(jsii_name="putUserPoolConfig")
    def put_user_pool_config(
        self,
        *,
        user_pool_id: builtins.str,
        app_id_client_regex: typing.Optional[builtins.str] = None,
        aws_region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param user_pool_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#user_pool_id AppsyncGraphqlApi#user_pool_id}.
        :param app_id_client_regex: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#app_id_client_regex AppsyncGraphqlApi#app_id_client_regex}.
        :param aws_region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#aws_region AppsyncGraphqlApi#aws_region}.
        '''
        value = AppsyncGraphqlApiAdditionalAuthenticationProviderUserPoolConfig(
            user_pool_id=user_pool_id,
            app_id_client_regex=app_id_client_regex,
            aws_region=aws_region,
        )

        return typing.cast(None, jsii.invoke(self, "putUserPoolConfig", [value]))

    @jsii.member(jsii_name="resetLambdaAuthorizerConfig")
    def reset_lambda_authorizer_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLambdaAuthorizerConfig", []))

    @jsii.member(jsii_name="resetOpenidConnectConfig")
    def reset_openid_connect_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOpenidConnectConfig", []))

    @jsii.member(jsii_name="resetUserPoolConfig")
    def reset_user_pool_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserPoolConfig", []))

    @builtins.property
    @jsii.member(jsii_name="lambdaAuthorizerConfig")
    def lambda_authorizer_config(
        self,
    ) -> AppsyncGraphqlApiAdditionalAuthenticationProviderLambdaAuthorizerConfigOutputReference:
        return typing.cast(AppsyncGraphqlApiAdditionalAuthenticationProviderLambdaAuthorizerConfigOutputReference, jsii.get(self, "lambdaAuthorizerConfig"))

    @builtins.property
    @jsii.member(jsii_name="openidConnectConfig")
    def openid_connect_config(
        self,
    ) -> AppsyncGraphqlApiAdditionalAuthenticationProviderOpenidConnectConfigOutputReference:
        return typing.cast(AppsyncGraphqlApiAdditionalAuthenticationProviderOpenidConnectConfigOutputReference, jsii.get(self, "openidConnectConfig"))

    @builtins.property
    @jsii.member(jsii_name="userPoolConfig")
    def user_pool_config(
        self,
    ) -> "AppsyncGraphqlApiAdditionalAuthenticationProviderUserPoolConfigOutputReference":
        return typing.cast("AppsyncGraphqlApiAdditionalAuthenticationProviderUserPoolConfigOutputReference", jsii.get(self, "userPoolConfig"))

    @builtins.property
    @jsii.member(jsii_name="authenticationTypeInput")
    def authentication_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authenticationTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="lambdaAuthorizerConfigInput")
    def lambda_authorizer_config_input(
        self,
    ) -> typing.Optional[AppsyncGraphqlApiAdditionalAuthenticationProviderLambdaAuthorizerConfig]:
        return typing.cast(typing.Optional[AppsyncGraphqlApiAdditionalAuthenticationProviderLambdaAuthorizerConfig], jsii.get(self, "lambdaAuthorizerConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="openidConnectConfigInput")
    def openid_connect_config_input(
        self,
    ) -> typing.Optional[AppsyncGraphqlApiAdditionalAuthenticationProviderOpenidConnectConfig]:
        return typing.cast(typing.Optional[AppsyncGraphqlApiAdditionalAuthenticationProviderOpenidConnectConfig], jsii.get(self, "openidConnectConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="userPoolConfigInput")
    def user_pool_config_input(
        self,
    ) -> typing.Optional["AppsyncGraphqlApiAdditionalAuthenticationProviderUserPoolConfig"]:
        return typing.cast(typing.Optional["AppsyncGraphqlApiAdditionalAuthenticationProviderUserPoolConfig"], jsii.get(self, "userPoolConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="authenticationType")
    def authentication_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authenticationType"))

    @authentication_type.setter
    def authentication_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee325082ae6ce1d7dd0f9ccb88170cf129acb25572afaa29769cb770147f6bca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authenticationType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AppsyncGraphqlApiAdditionalAuthenticationProvider, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AppsyncGraphqlApiAdditionalAuthenticationProvider, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AppsyncGraphqlApiAdditionalAuthenticationProvider, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99d083472215d2a2ad8a9c8fd1a561f9e5b606408d0de80781a3b1b07a7da15c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appsyncGraphqlApi.AppsyncGraphqlApiAdditionalAuthenticationProviderUserPoolConfig",
    jsii_struct_bases=[],
    name_mapping={
        "user_pool_id": "userPoolId",
        "app_id_client_regex": "appIdClientRegex",
        "aws_region": "awsRegion",
    },
)
class AppsyncGraphqlApiAdditionalAuthenticationProviderUserPoolConfig:
    def __init__(
        self,
        *,
        user_pool_id: builtins.str,
        app_id_client_regex: typing.Optional[builtins.str] = None,
        aws_region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param user_pool_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#user_pool_id AppsyncGraphqlApi#user_pool_id}.
        :param app_id_client_regex: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#app_id_client_regex AppsyncGraphqlApi#app_id_client_regex}.
        :param aws_region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#aws_region AppsyncGraphqlApi#aws_region}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39254179b3c7cf72cbcb98b51fb9fe389cce3fd77e203406dfb0699853dce158)
            check_type(argname="argument user_pool_id", value=user_pool_id, expected_type=type_hints["user_pool_id"])
            check_type(argname="argument app_id_client_regex", value=app_id_client_regex, expected_type=type_hints["app_id_client_regex"])
            check_type(argname="argument aws_region", value=aws_region, expected_type=type_hints["aws_region"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "user_pool_id": user_pool_id,
        }
        if app_id_client_regex is not None:
            self._values["app_id_client_regex"] = app_id_client_regex
        if aws_region is not None:
            self._values["aws_region"] = aws_region

    @builtins.property
    def user_pool_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#user_pool_id AppsyncGraphqlApi#user_pool_id}.'''
        result = self._values.get("user_pool_id")
        assert result is not None, "Required property 'user_pool_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def app_id_client_regex(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#app_id_client_regex AppsyncGraphqlApi#app_id_client_regex}.'''
        result = self._values.get("app_id_client_regex")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def aws_region(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#aws_region AppsyncGraphqlApi#aws_region}.'''
        result = self._values.get("aws_region")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppsyncGraphqlApiAdditionalAuthenticationProviderUserPoolConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppsyncGraphqlApiAdditionalAuthenticationProviderUserPoolConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appsyncGraphqlApi.AppsyncGraphqlApiAdditionalAuthenticationProviderUserPoolConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8901445df744a3725cf4021abefc3577978b3eb872fdb15659b3f6588846a164)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAppIdClientRegex")
    def reset_app_id_client_regex(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAppIdClientRegex", []))

    @jsii.member(jsii_name="resetAwsRegion")
    def reset_aws_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsRegion", []))

    @builtins.property
    @jsii.member(jsii_name="appIdClientRegexInput")
    def app_id_client_regex_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "appIdClientRegexInput"))

    @builtins.property
    @jsii.member(jsii_name="awsRegionInput")
    def aws_region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "awsRegionInput"))

    @builtins.property
    @jsii.member(jsii_name="userPoolIdInput")
    def user_pool_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userPoolIdInput"))

    @builtins.property
    @jsii.member(jsii_name="appIdClientRegex")
    def app_id_client_regex(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "appIdClientRegex"))

    @app_id_client_regex.setter
    def app_id_client_regex(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd8386c604f4c0445981d8dd1a7b75a2f8cce53436b83ea4f504282fab4e2175)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appIdClientRegex", value)

    @builtins.property
    @jsii.member(jsii_name="awsRegion")
    def aws_region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "awsRegion"))

    @aws_region.setter
    def aws_region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d7f16d45218c635a0574c1a19bb410358194432ce4893b43a3b05fda55011a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsRegion", value)

    @builtins.property
    @jsii.member(jsii_name="userPoolId")
    def user_pool_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userPoolId"))

    @user_pool_id.setter
    def user_pool_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ce4d3e2333b17f4c2edb0e56d8ed380914a57b7fa8eae006924976b5380bbd3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userPoolId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppsyncGraphqlApiAdditionalAuthenticationProviderUserPoolConfig]:
        return typing.cast(typing.Optional[AppsyncGraphqlApiAdditionalAuthenticationProviderUserPoolConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppsyncGraphqlApiAdditionalAuthenticationProviderUserPoolConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4f3f9bd07b9957a514e97b463ab2d04c92c7a6ca4776975153a1bf551ab5028)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appsyncGraphqlApi.AppsyncGraphqlApiConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "authentication_type": "authenticationType",
        "name": "name",
        "additional_authentication_provider": "additionalAuthenticationProvider",
        "id": "id",
        "lambda_authorizer_config": "lambdaAuthorizerConfig",
        "log_config": "logConfig",
        "openid_connect_config": "openidConnectConfig",
        "schema": "schema",
        "tags": "tags",
        "tags_all": "tagsAll",
        "user_pool_config": "userPoolConfig",
        "xray_enabled": "xrayEnabled",
    },
)
class AppsyncGraphqlApiConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        authentication_type: builtins.str,
        name: builtins.str,
        additional_authentication_provider: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AppsyncGraphqlApiAdditionalAuthenticationProvider, typing.Dict[builtins.str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        lambda_authorizer_config: typing.Optional[typing.Union["AppsyncGraphqlApiLambdaAuthorizerConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        log_config: typing.Optional[typing.Union["AppsyncGraphqlApiLogConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        openid_connect_config: typing.Optional[typing.Union["AppsyncGraphqlApiOpenidConnectConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        schema: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        user_pool_config: typing.Optional[typing.Union["AppsyncGraphqlApiUserPoolConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        xray_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param authentication_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#authentication_type AppsyncGraphqlApi#authentication_type}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#name AppsyncGraphqlApi#name}.
        :param additional_authentication_provider: additional_authentication_provider block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#additional_authentication_provider AppsyncGraphqlApi#additional_authentication_provider}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#id AppsyncGraphqlApi#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param lambda_authorizer_config: lambda_authorizer_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#lambda_authorizer_config AppsyncGraphqlApi#lambda_authorizer_config}
        :param log_config: log_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#log_config AppsyncGraphqlApi#log_config}
        :param openid_connect_config: openid_connect_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#openid_connect_config AppsyncGraphqlApi#openid_connect_config}
        :param schema: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#schema AppsyncGraphqlApi#schema}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#tags AppsyncGraphqlApi#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#tags_all AppsyncGraphqlApi#tags_all}.
        :param user_pool_config: user_pool_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#user_pool_config AppsyncGraphqlApi#user_pool_config}
        :param xray_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#xray_enabled AppsyncGraphqlApi#xray_enabled}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(lambda_authorizer_config, dict):
            lambda_authorizer_config = AppsyncGraphqlApiLambdaAuthorizerConfig(**lambda_authorizer_config)
        if isinstance(log_config, dict):
            log_config = AppsyncGraphqlApiLogConfig(**log_config)
        if isinstance(openid_connect_config, dict):
            openid_connect_config = AppsyncGraphqlApiOpenidConnectConfig(**openid_connect_config)
        if isinstance(user_pool_config, dict):
            user_pool_config = AppsyncGraphqlApiUserPoolConfig(**user_pool_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5acdb08b8e9d2b0b71645eb811197e6bc72006b848839da1d9dcab7ccac938ba)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument authentication_type", value=authentication_type, expected_type=type_hints["authentication_type"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument additional_authentication_provider", value=additional_authentication_provider, expected_type=type_hints["additional_authentication_provider"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument lambda_authorizer_config", value=lambda_authorizer_config, expected_type=type_hints["lambda_authorizer_config"])
            check_type(argname="argument log_config", value=log_config, expected_type=type_hints["log_config"])
            check_type(argname="argument openid_connect_config", value=openid_connect_config, expected_type=type_hints["openid_connect_config"])
            check_type(argname="argument schema", value=schema, expected_type=type_hints["schema"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument user_pool_config", value=user_pool_config, expected_type=type_hints["user_pool_config"])
            check_type(argname="argument xray_enabled", value=xray_enabled, expected_type=type_hints["xray_enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "authentication_type": authentication_type,
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
        if additional_authentication_provider is not None:
            self._values["additional_authentication_provider"] = additional_authentication_provider
        if id is not None:
            self._values["id"] = id
        if lambda_authorizer_config is not None:
            self._values["lambda_authorizer_config"] = lambda_authorizer_config
        if log_config is not None:
            self._values["log_config"] = log_config
        if openid_connect_config is not None:
            self._values["openid_connect_config"] = openid_connect_config
        if schema is not None:
            self._values["schema"] = schema
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if user_pool_config is not None:
            self._values["user_pool_config"] = user_pool_config
        if xray_enabled is not None:
            self._values["xray_enabled"] = xray_enabled

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
    def authentication_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#authentication_type AppsyncGraphqlApi#authentication_type}.'''
        result = self._values.get("authentication_type")
        assert result is not None, "Required property 'authentication_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#name AppsyncGraphqlApi#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def additional_authentication_provider(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppsyncGraphqlApiAdditionalAuthenticationProvider]]]:
        '''additional_authentication_provider block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#additional_authentication_provider AppsyncGraphqlApi#additional_authentication_provider}
        '''
        result = self._values.get("additional_authentication_provider")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppsyncGraphqlApiAdditionalAuthenticationProvider]]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#id AppsyncGraphqlApi#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lambda_authorizer_config(
        self,
    ) -> typing.Optional["AppsyncGraphqlApiLambdaAuthorizerConfig"]:
        '''lambda_authorizer_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#lambda_authorizer_config AppsyncGraphqlApi#lambda_authorizer_config}
        '''
        result = self._values.get("lambda_authorizer_config")
        return typing.cast(typing.Optional["AppsyncGraphqlApiLambdaAuthorizerConfig"], result)

    @builtins.property
    def log_config(self) -> typing.Optional["AppsyncGraphqlApiLogConfig"]:
        '''log_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#log_config AppsyncGraphqlApi#log_config}
        '''
        result = self._values.get("log_config")
        return typing.cast(typing.Optional["AppsyncGraphqlApiLogConfig"], result)

    @builtins.property
    def openid_connect_config(
        self,
    ) -> typing.Optional["AppsyncGraphqlApiOpenidConnectConfig"]:
        '''openid_connect_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#openid_connect_config AppsyncGraphqlApi#openid_connect_config}
        '''
        result = self._values.get("openid_connect_config")
        return typing.cast(typing.Optional["AppsyncGraphqlApiOpenidConnectConfig"], result)

    @builtins.property
    def schema(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#schema AppsyncGraphqlApi#schema}.'''
        result = self._values.get("schema")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#tags AppsyncGraphqlApi#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#tags_all AppsyncGraphqlApi#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def user_pool_config(self) -> typing.Optional["AppsyncGraphqlApiUserPoolConfig"]:
        '''user_pool_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#user_pool_config AppsyncGraphqlApi#user_pool_config}
        '''
        result = self._values.get("user_pool_config")
        return typing.cast(typing.Optional["AppsyncGraphqlApiUserPoolConfig"], result)

    @builtins.property
    def xray_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#xray_enabled AppsyncGraphqlApi#xray_enabled}.'''
        result = self._values.get("xray_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppsyncGraphqlApiConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appsyncGraphqlApi.AppsyncGraphqlApiLambdaAuthorizerConfig",
    jsii_struct_bases=[],
    name_mapping={
        "authorizer_uri": "authorizerUri",
        "authorizer_result_ttl_in_seconds": "authorizerResultTtlInSeconds",
        "identity_validation_expression": "identityValidationExpression",
    },
)
class AppsyncGraphqlApiLambdaAuthorizerConfig:
    def __init__(
        self,
        *,
        authorizer_uri: builtins.str,
        authorizer_result_ttl_in_seconds: typing.Optional[jsii.Number] = None,
        identity_validation_expression: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param authorizer_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#authorizer_uri AppsyncGraphqlApi#authorizer_uri}.
        :param authorizer_result_ttl_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#authorizer_result_ttl_in_seconds AppsyncGraphqlApi#authorizer_result_ttl_in_seconds}.
        :param identity_validation_expression: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#identity_validation_expression AppsyncGraphqlApi#identity_validation_expression}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5b00640b754230c1197929ea07e535705ce34103bc1573be2b7f30e505edde1)
            check_type(argname="argument authorizer_uri", value=authorizer_uri, expected_type=type_hints["authorizer_uri"])
            check_type(argname="argument authorizer_result_ttl_in_seconds", value=authorizer_result_ttl_in_seconds, expected_type=type_hints["authorizer_result_ttl_in_seconds"])
            check_type(argname="argument identity_validation_expression", value=identity_validation_expression, expected_type=type_hints["identity_validation_expression"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "authorizer_uri": authorizer_uri,
        }
        if authorizer_result_ttl_in_seconds is not None:
            self._values["authorizer_result_ttl_in_seconds"] = authorizer_result_ttl_in_seconds
        if identity_validation_expression is not None:
            self._values["identity_validation_expression"] = identity_validation_expression

    @builtins.property
    def authorizer_uri(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#authorizer_uri AppsyncGraphqlApi#authorizer_uri}.'''
        result = self._values.get("authorizer_uri")
        assert result is not None, "Required property 'authorizer_uri' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def authorizer_result_ttl_in_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#authorizer_result_ttl_in_seconds AppsyncGraphqlApi#authorizer_result_ttl_in_seconds}.'''
        result = self._values.get("authorizer_result_ttl_in_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def identity_validation_expression(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#identity_validation_expression AppsyncGraphqlApi#identity_validation_expression}.'''
        result = self._values.get("identity_validation_expression")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppsyncGraphqlApiLambdaAuthorizerConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppsyncGraphqlApiLambdaAuthorizerConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appsyncGraphqlApi.AppsyncGraphqlApiLambdaAuthorizerConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__257662f126a92c9e40c87c5569acf309790744f37717dc87b36ce05a2d82cf12)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAuthorizerResultTtlInSeconds")
    def reset_authorizer_result_ttl_in_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthorizerResultTtlInSeconds", []))

    @jsii.member(jsii_name="resetIdentityValidationExpression")
    def reset_identity_validation_expression(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentityValidationExpression", []))

    @builtins.property
    @jsii.member(jsii_name="authorizerResultTtlInSecondsInput")
    def authorizer_result_ttl_in_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "authorizerResultTtlInSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="authorizerUriInput")
    def authorizer_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authorizerUriInput"))

    @builtins.property
    @jsii.member(jsii_name="identityValidationExpressionInput")
    def identity_validation_expression_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "identityValidationExpressionInput"))

    @builtins.property
    @jsii.member(jsii_name="authorizerResultTtlInSeconds")
    def authorizer_result_ttl_in_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "authorizerResultTtlInSeconds"))

    @authorizer_result_ttl_in_seconds.setter
    def authorizer_result_ttl_in_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0daff97f93d85fd88dfb7eee120da4d4c548bc68dca16ae4a210284ba288b0e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authorizerResultTtlInSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="authorizerUri")
    def authorizer_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authorizerUri"))

    @authorizer_uri.setter
    def authorizer_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0fa70d500b60b6b04d399a646861e82f7e67938252c9cfab88827a98f376d0c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authorizerUri", value)

    @builtins.property
    @jsii.member(jsii_name="identityValidationExpression")
    def identity_validation_expression(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "identityValidationExpression"))

    @identity_validation_expression.setter
    def identity_validation_expression(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a98600c3428d472d5ab533b7603925976cd6180251bcfb934e96dde84a945488)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityValidationExpression", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppsyncGraphqlApiLambdaAuthorizerConfig]:
        return typing.cast(typing.Optional[AppsyncGraphqlApiLambdaAuthorizerConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppsyncGraphqlApiLambdaAuthorizerConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b53846991e78b7a575d606b04a6e0271f98d9ec5d6bb4cb3e7f04499d41be67)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appsyncGraphqlApi.AppsyncGraphqlApiLogConfig",
    jsii_struct_bases=[],
    name_mapping={
        "cloudwatch_logs_role_arn": "cloudwatchLogsRoleArn",
        "field_log_level": "fieldLogLevel",
        "exclude_verbose_content": "excludeVerboseContent",
    },
)
class AppsyncGraphqlApiLogConfig:
    def __init__(
        self,
        *,
        cloudwatch_logs_role_arn: builtins.str,
        field_log_level: builtins.str,
        exclude_verbose_content: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param cloudwatch_logs_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#cloudwatch_logs_role_arn AppsyncGraphqlApi#cloudwatch_logs_role_arn}.
        :param field_log_level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#field_log_level AppsyncGraphqlApi#field_log_level}.
        :param exclude_verbose_content: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#exclude_verbose_content AppsyncGraphqlApi#exclude_verbose_content}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09793a91b3c42b5fe5479bd057dc9829728a9c21e100e426d97c670f13ca1813)
            check_type(argname="argument cloudwatch_logs_role_arn", value=cloudwatch_logs_role_arn, expected_type=type_hints["cloudwatch_logs_role_arn"])
            check_type(argname="argument field_log_level", value=field_log_level, expected_type=type_hints["field_log_level"])
            check_type(argname="argument exclude_verbose_content", value=exclude_verbose_content, expected_type=type_hints["exclude_verbose_content"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cloudwatch_logs_role_arn": cloudwatch_logs_role_arn,
            "field_log_level": field_log_level,
        }
        if exclude_verbose_content is not None:
            self._values["exclude_verbose_content"] = exclude_verbose_content

    @builtins.property
    def cloudwatch_logs_role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#cloudwatch_logs_role_arn AppsyncGraphqlApi#cloudwatch_logs_role_arn}.'''
        result = self._values.get("cloudwatch_logs_role_arn")
        assert result is not None, "Required property 'cloudwatch_logs_role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def field_log_level(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#field_log_level AppsyncGraphqlApi#field_log_level}.'''
        result = self._values.get("field_log_level")
        assert result is not None, "Required property 'field_log_level' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def exclude_verbose_content(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#exclude_verbose_content AppsyncGraphqlApi#exclude_verbose_content}.'''
        result = self._values.get("exclude_verbose_content")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppsyncGraphqlApiLogConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppsyncGraphqlApiLogConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appsyncGraphqlApi.AppsyncGraphqlApiLogConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e8bcc01fbcbd937867b5cdabd57b260edc27de543045c129d053159210e00d70)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetExcludeVerboseContent")
    def reset_exclude_verbose_content(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExcludeVerboseContent", []))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchLogsRoleArnInput")
    def cloudwatch_logs_role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cloudwatchLogsRoleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="excludeVerboseContentInput")
    def exclude_verbose_content_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "excludeVerboseContentInput"))

    @builtins.property
    @jsii.member(jsii_name="fieldLogLevelInput")
    def field_log_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fieldLogLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchLogsRoleArn")
    def cloudwatch_logs_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cloudwatchLogsRoleArn"))

    @cloudwatch_logs_role_arn.setter
    def cloudwatch_logs_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ada265987dfd3706e158ba324e2c6f04c86af3623f2f964a7ec6b367f26c920e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloudwatchLogsRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="excludeVerboseContent")
    def exclude_verbose_content(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "excludeVerboseContent"))

    @exclude_verbose_content.setter
    def exclude_verbose_content(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ef5358a24a8406636bb250180f1e4f95d98672c1e770cb72afaf44c18f67028)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "excludeVerboseContent", value)

    @builtins.property
    @jsii.member(jsii_name="fieldLogLevel")
    def field_log_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fieldLogLevel"))

    @field_log_level.setter
    def field_log_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a46d5ab183a50c3384dab27eaa9f51d70d3e4f559476f852c187384a2d6446ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fieldLogLevel", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppsyncGraphqlApiLogConfig]:
        return typing.cast(typing.Optional[AppsyncGraphqlApiLogConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppsyncGraphqlApiLogConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c8df2482e5864543312990f5a80c0a04d56e56a600624cee26b7291496749bf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appsyncGraphqlApi.AppsyncGraphqlApiOpenidConnectConfig",
    jsii_struct_bases=[],
    name_mapping={
        "issuer": "issuer",
        "auth_ttl": "authTtl",
        "client_id": "clientId",
        "iat_ttl": "iatTtl",
    },
)
class AppsyncGraphqlApiOpenidConnectConfig:
    def __init__(
        self,
        *,
        issuer: builtins.str,
        auth_ttl: typing.Optional[jsii.Number] = None,
        client_id: typing.Optional[builtins.str] = None,
        iat_ttl: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param issuer: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#issuer AppsyncGraphqlApi#issuer}.
        :param auth_ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#auth_ttl AppsyncGraphqlApi#auth_ttl}.
        :param client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#client_id AppsyncGraphqlApi#client_id}.
        :param iat_ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#iat_ttl AppsyncGraphqlApi#iat_ttl}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7f52394fe3d36e25bc8b7e7a5e39856d928284a198637a679a1a9c50c868f1d)
            check_type(argname="argument issuer", value=issuer, expected_type=type_hints["issuer"])
            check_type(argname="argument auth_ttl", value=auth_ttl, expected_type=type_hints["auth_ttl"])
            check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
            check_type(argname="argument iat_ttl", value=iat_ttl, expected_type=type_hints["iat_ttl"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "issuer": issuer,
        }
        if auth_ttl is not None:
            self._values["auth_ttl"] = auth_ttl
        if client_id is not None:
            self._values["client_id"] = client_id
        if iat_ttl is not None:
            self._values["iat_ttl"] = iat_ttl

    @builtins.property
    def issuer(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#issuer AppsyncGraphqlApi#issuer}.'''
        result = self._values.get("issuer")
        assert result is not None, "Required property 'issuer' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def auth_ttl(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#auth_ttl AppsyncGraphqlApi#auth_ttl}.'''
        result = self._values.get("auth_ttl")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def client_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#client_id AppsyncGraphqlApi#client_id}.'''
        result = self._values.get("client_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def iat_ttl(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#iat_ttl AppsyncGraphqlApi#iat_ttl}.'''
        result = self._values.get("iat_ttl")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppsyncGraphqlApiOpenidConnectConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppsyncGraphqlApiOpenidConnectConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appsyncGraphqlApi.AppsyncGraphqlApiOpenidConnectConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3821f44e0bd646401122ce5763b4e5972f62862d2b6edcde3139f498610da141)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAuthTtl")
    def reset_auth_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthTtl", []))

    @jsii.member(jsii_name="resetClientId")
    def reset_client_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientId", []))

    @jsii.member(jsii_name="resetIatTtl")
    def reset_iat_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIatTtl", []))

    @builtins.property
    @jsii.member(jsii_name="authTtlInput")
    def auth_ttl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "authTtlInput"))

    @builtins.property
    @jsii.member(jsii_name="clientIdInput")
    def client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="iatTtlInput")
    def iat_ttl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "iatTtlInput"))

    @builtins.property
    @jsii.member(jsii_name="issuerInput")
    def issuer_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "issuerInput"))

    @builtins.property
    @jsii.member(jsii_name="authTtl")
    def auth_ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "authTtl"))

    @auth_ttl.setter
    def auth_ttl(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c441fcb88dece3743252858580293cb83c1a7f61026194450473e992b947654)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authTtl", value)

    @builtins.property
    @jsii.member(jsii_name="clientId")
    def client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientId"))

    @client_id.setter
    def client_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0924ff43a1f672fb054efa920d9a76e7f3f8348a0dd4e87942e40207d267076)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientId", value)

    @builtins.property
    @jsii.member(jsii_name="iatTtl")
    def iat_ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "iatTtl"))

    @iat_ttl.setter
    def iat_ttl(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ec6c0686f1006916974a67fb6c6ab4ec16c8078ac001afe15ac4a2ae6fc8f9c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iatTtl", value)

    @builtins.property
    @jsii.member(jsii_name="issuer")
    def issuer(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "issuer"))

    @issuer.setter
    def issuer(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf48e72489bcc2416c8136fde077d8a7bf0e32bccf95ca06fc3fbd2a0486edf9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "issuer", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppsyncGraphqlApiOpenidConnectConfig]:
        return typing.cast(typing.Optional[AppsyncGraphqlApiOpenidConnectConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppsyncGraphqlApiOpenidConnectConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__218e32d28ffe92772917d53e786a56d2202bd59b76cb283edb10482d1f432e53)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appsyncGraphqlApi.AppsyncGraphqlApiUserPoolConfig",
    jsii_struct_bases=[],
    name_mapping={
        "default_action": "defaultAction",
        "user_pool_id": "userPoolId",
        "app_id_client_regex": "appIdClientRegex",
        "aws_region": "awsRegion",
    },
)
class AppsyncGraphqlApiUserPoolConfig:
    def __init__(
        self,
        *,
        default_action: builtins.str,
        user_pool_id: builtins.str,
        app_id_client_regex: typing.Optional[builtins.str] = None,
        aws_region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param default_action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#default_action AppsyncGraphqlApi#default_action}.
        :param user_pool_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#user_pool_id AppsyncGraphqlApi#user_pool_id}.
        :param app_id_client_regex: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#app_id_client_regex AppsyncGraphqlApi#app_id_client_regex}.
        :param aws_region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#aws_region AppsyncGraphqlApi#aws_region}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f96123bf43274cacf8899e5d518f76668b910930e4e31093e21734de7c7369da)
            check_type(argname="argument default_action", value=default_action, expected_type=type_hints["default_action"])
            check_type(argname="argument user_pool_id", value=user_pool_id, expected_type=type_hints["user_pool_id"])
            check_type(argname="argument app_id_client_regex", value=app_id_client_regex, expected_type=type_hints["app_id_client_regex"])
            check_type(argname="argument aws_region", value=aws_region, expected_type=type_hints["aws_region"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "default_action": default_action,
            "user_pool_id": user_pool_id,
        }
        if app_id_client_regex is not None:
            self._values["app_id_client_regex"] = app_id_client_regex
        if aws_region is not None:
            self._values["aws_region"] = aws_region

    @builtins.property
    def default_action(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#default_action AppsyncGraphqlApi#default_action}.'''
        result = self._values.get("default_action")
        assert result is not None, "Required property 'default_action' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_pool_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#user_pool_id AppsyncGraphqlApi#user_pool_id}.'''
        result = self._values.get("user_pool_id")
        assert result is not None, "Required property 'user_pool_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def app_id_client_regex(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#app_id_client_regex AppsyncGraphqlApi#app_id_client_regex}.'''
        result = self._values.get("app_id_client_regex")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def aws_region(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#aws_region AppsyncGraphqlApi#aws_region}.'''
        result = self._values.get("aws_region")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppsyncGraphqlApiUserPoolConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppsyncGraphqlApiUserPoolConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appsyncGraphqlApi.AppsyncGraphqlApiUserPoolConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__02dfd490eb8ffd1dd726a024d33f7f1cb9db7b3af2baf977108bb59804c0a7ee)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAppIdClientRegex")
    def reset_app_id_client_regex(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAppIdClientRegex", []))

    @jsii.member(jsii_name="resetAwsRegion")
    def reset_aws_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsRegion", []))

    @builtins.property
    @jsii.member(jsii_name="appIdClientRegexInput")
    def app_id_client_regex_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "appIdClientRegexInput"))

    @builtins.property
    @jsii.member(jsii_name="awsRegionInput")
    def aws_region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "awsRegionInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultActionInput")
    def default_action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultActionInput"))

    @builtins.property
    @jsii.member(jsii_name="userPoolIdInput")
    def user_pool_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userPoolIdInput"))

    @builtins.property
    @jsii.member(jsii_name="appIdClientRegex")
    def app_id_client_regex(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "appIdClientRegex"))

    @app_id_client_regex.setter
    def app_id_client_regex(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d284c88871a05035bd3e42a664971d90b7b097f8b0daa320938e7ff1bedf85d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appIdClientRegex", value)

    @builtins.property
    @jsii.member(jsii_name="awsRegion")
    def aws_region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "awsRegion"))

    @aws_region.setter
    def aws_region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ba0014fee9df28047fece03ea378f725e10305b552fec78b7278fe9d45dd15d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsRegion", value)

    @builtins.property
    @jsii.member(jsii_name="defaultAction")
    def default_action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultAction"))

    @default_action.setter
    def default_action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3cd63955607c4010cb5c14a910bfcb7fddc8d3ca4e96e6111a1a8306e7cfd41a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultAction", value)

    @builtins.property
    @jsii.member(jsii_name="userPoolId")
    def user_pool_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userPoolId"))

    @user_pool_id.setter
    def user_pool_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f66808c863e043ce62bded0681c971a5a632314dd2e2a56e867d872deccd947)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userPoolId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppsyncGraphqlApiUserPoolConfig]:
        return typing.cast(typing.Optional[AppsyncGraphqlApiUserPoolConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppsyncGraphqlApiUserPoolConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d84c913e26f417ac6eb94adee8d388fa28cfb57e77624d7a5dd4359246a5b8d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "AppsyncGraphqlApi",
    "AppsyncGraphqlApiAdditionalAuthenticationProvider",
    "AppsyncGraphqlApiAdditionalAuthenticationProviderLambdaAuthorizerConfig",
    "AppsyncGraphqlApiAdditionalAuthenticationProviderLambdaAuthorizerConfigOutputReference",
    "AppsyncGraphqlApiAdditionalAuthenticationProviderList",
    "AppsyncGraphqlApiAdditionalAuthenticationProviderOpenidConnectConfig",
    "AppsyncGraphqlApiAdditionalAuthenticationProviderOpenidConnectConfigOutputReference",
    "AppsyncGraphqlApiAdditionalAuthenticationProviderOutputReference",
    "AppsyncGraphqlApiAdditionalAuthenticationProviderUserPoolConfig",
    "AppsyncGraphqlApiAdditionalAuthenticationProviderUserPoolConfigOutputReference",
    "AppsyncGraphqlApiConfig",
    "AppsyncGraphqlApiLambdaAuthorizerConfig",
    "AppsyncGraphqlApiLambdaAuthorizerConfigOutputReference",
    "AppsyncGraphqlApiLogConfig",
    "AppsyncGraphqlApiLogConfigOutputReference",
    "AppsyncGraphqlApiOpenidConnectConfig",
    "AppsyncGraphqlApiOpenidConnectConfigOutputReference",
    "AppsyncGraphqlApiUserPoolConfig",
    "AppsyncGraphqlApiUserPoolConfigOutputReference",
]

publication.publish()

def _typecheckingstub__0b1a34e24e4ecb77f94a4b7290523974e81ede49c5c2680b9673de754702cdf9(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    authentication_type: builtins.str,
    name: builtins.str,
    additional_authentication_provider: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AppsyncGraphqlApiAdditionalAuthenticationProvider, typing.Dict[builtins.str, typing.Any]]]]] = None,
    id: typing.Optional[builtins.str] = None,
    lambda_authorizer_config: typing.Optional[typing.Union[AppsyncGraphqlApiLambdaAuthorizerConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    log_config: typing.Optional[typing.Union[AppsyncGraphqlApiLogConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    openid_connect_config: typing.Optional[typing.Union[AppsyncGraphqlApiOpenidConnectConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    schema: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    user_pool_config: typing.Optional[typing.Union[AppsyncGraphqlApiUserPoolConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    xray_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
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

def _typecheckingstub__d22f3cd5becc11aac2f69743221ed57a1d4da2a90136c7bee1f6c30becc6ca92(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AppsyncGraphqlApiAdditionalAuthenticationProvider, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0434458a270cd4c322a10da94f955dd06696b4805536dc2687ec0334fcc6488f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3fce342308f1087946d8f2dc37269259162733b211ed68a306b4cddcd127599(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ecedb068407c4d8af8436e1f5de6a2e2dd1e66ec9745453b41bead429ff90fa8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1bacba8a99c5793613fbeaf6a6068c36b88d32996da9367697490b0798259d73(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__202e8d4473b03aab739ab0fe3b3814ba31b16faf6aedb6e1dc151dc390df6860(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2942adcba69973f0ff64b04d5c330e68cd1d3e267ca05f3db4f1766bd2b84435(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53041cc9b24097abc2fe0d927e5b6e0f2c91c5a2f9dde6ddb1508c6dadc7fdf0(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1fef41dea32bc2860defc6d68a0080d08f0f1a0374642eb0fa725bad5049888e(
    *,
    authentication_type: builtins.str,
    lambda_authorizer_config: typing.Optional[typing.Union[AppsyncGraphqlApiAdditionalAuthenticationProviderLambdaAuthorizerConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    openid_connect_config: typing.Optional[typing.Union[AppsyncGraphqlApiAdditionalAuthenticationProviderOpenidConnectConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    user_pool_config: typing.Optional[typing.Union[AppsyncGraphqlApiAdditionalAuthenticationProviderUserPoolConfig, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69f66dc9fca88d321d473b1b9de41d1380f1ce01d2ba816cb39f6c1892632a2d(
    *,
    authorizer_uri: builtins.str,
    authorizer_result_ttl_in_seconds: typing.Optional[jsii.Number] = None,
    identity_validation_expression: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__620bc731715a89ff080e52e826de078a7179156b81903550740b4f47db57dc10(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c9299d4d4f4282ae613febbf1854546cf89da6fa74fc9cf248b56274ec42b22(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e9a011855ae5d434796efc86db82fc92557712e05da8e8eebae50c82bbbeebd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e44ceccafdfab349258b2bc34ed8c64c942ed44e803b16436dbde739f10aa92d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4724fb48c019b4428723d296ba5b6c80284fb8eae918984160f3b7cc3b915dee(
    value: typing.Optional[AppsyncGraphqlApiAdditionalAuthenticationProviderLambdaAuthorizerConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc4a31a7fea2dc0e68ea3c756370f168caee26f25c5969b3469480c929f42c28(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7c47086be47925fd6a3b3f63c14733ac15c9c60937b723a28c4ebe0c69dadeb(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9fb7b03066ff1e4925faa739d5ac3d85a382192e94fb93718c4d284fa283a61(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3852c5a690b7a7eb501759ea7401d012782f14e859c6351dbad702c09ffd2d31(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__798b8bf319e6422a0af0539b43dc6359caf792a25c88c5858fefcf29d177b7d6(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e81d27ce849a8d8a686ce8a2703837e9ba88e4415d74c66585fe8a101bdcae5(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppsyncGraphqlApiAdditionalAuthenticationProvider]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__898165341f00f84ca1cba6b225b6e7bfb7ba056130ccff6dbd79e405ff7f1d1b(
    *,
    issuer: builtins.str,
    auth_ttl: typing.Optional[jsii.Number] = None,
    client_id: typing.Optional[builtins.str] = None,
    iat_ttl: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2c754f7f2df89404d8021c25a14da516aef338a4444aa078e77272d00f3588b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7498b9e24a81d67bf46bd313a6ef8172f621304b2bb5c7c222a407bdd03342c(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c458e67045b2e5a5e900221a10ac9fa43d682e7b32f1ce14fe88ef0a3a2a431(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce277e8b9fb0dec3e4bac1bff5aa007cb357962e7ab9969098a0e27e413326bb(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a193b440b1c14088bc034ef3baaac9f7cb4c36fff439580c6a6a9314f99a716(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aadd7ca1c32ef4362015261061d4e9752186456e5d942bffaeb9054efaa1e33d(
    value: typing.Optional[AppsyncGraphqlApiAdditionalAuthenticationProviderOpenidConnectConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__683824807154119cb210b87c1ae922a943d57e9af9ba1278b0aba1dc73de92c9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee325082ae6ce1d7dd0f9ccb88170cf129acb25572afaa29769cb770147f6bca(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99d083472215d2a2ad8a9c8fd1a561f9e5b606408d0de80781a3b1b07a7da15c(
    value: typing.Optional[typing.Union[AppsyncGraphqlApiAdditionalAuthenticationProvider, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39254179b3c7cf72cbcb98b51fb9fe389cce3fd77e203406dfb0699853dce158(
    *,
    user_pool_id: builtins.str,
    app_id_client_regex: typing.Optional[builtins.str] = None,
    aws_region: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8901445df744a3725cf4021abefc3577978b3eb872fdb15659b3f6588846a164(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd8386c604f4c0445981d8dd1a7b75a2f8cce53436b83ea4f504282fab4e2175(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d7f16d45218c635a0574c1a19bb410358194432ce4893b43a3b05fda55011a2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ce4d3e2333b17f4c2edb0e56d8ed380914a57b7fa8eae006924976b5380bbd3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4f3f9bd07b9957a514e97b463ab2d04c92c7a6ca4776975153a1bf551ab5028(
    value: typing.Optional[AppsyncGraphqlApiAdditionalAuthenticationProviderUserPoolConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5acdb08b8e9d2b0b71645eb811197e6bc72006b848839da1d9dcab7ccac938ba(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    authentication_type: builtins.str,
    name: builtins.str,
    additional_authentication_provider: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AppsyncGraphqlApiAdditionalAuthenticationProvider, typing.Dict[builtins.str, typing.Any]]]]] = None,
    id: typing.Optional[builtins.str] = None,
    lambda_authorizer_config: typing.Optional[typing.Union[AppsyncGraphqlApiLambdaAuthorizerConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    log_config: typing.Optional[typing.Union[AppsyncGraphqlApiLogConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    openid_connect_config: typing.Optional[typing.Union[AppsyncGraphqlApiOpenidConnectConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    schema: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    user_pool_config: typing.Optional[typing.Union[AppsyncGraphqlApiUserPoolConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    xray_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5b00640b754230c1197929ea07e535705ce34103bc1573be2b7f30e505edde1(
    *,
    authorizer_uri: builtins.str,
    authorizer_result_ttl_in_seconds: typing.Optional[jsii.Number] = None,
    identity_validation_expression: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__257662f126a92c9e40c87c5569acf309790744f37717dc87b36ce05a2d82cf12(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0daff97f93d85fd88dfb7eee120da4d4c548bc68dca16ae4a210284ba288b0e0(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0fa70d500b60b6b04d399a646861e82f7e67938252c9cfab88827a98f376d0c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a98600c3428d472d5ab533b7603925976cd6180251bcfb934e96dde84a945488(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b53846991e78b7a575d606b04a6e0271f98d9ec5d6bb4cb3e7f04499d41be67(
    value: typing.Optional[AppsyncGraphqlApiLambdaAuthorizerConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09793a91b3c42b5fe5479bd057dc9829728a9c21e100e426d97c670f13ca1813(
    *,
    cloudwatch_logs_role_arn: builtins.str,
    field_log_level: builtins.str,
    exclude_verbose_content: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8bcc01fbcbd937867b5cdabd57b260edc27de543045c129d053159210e00d70(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ada265987dfd3706e158ba324e2c6f04c86af3623f2f964a7ec6b367f26c920e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ef5358a24a8406636bb250180f1e4f95d98672c1e770cb72afaf44c18f67028(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a46d5ab183a50c3384dab27eaa9f51d70d3e4f559476f852c187384a2d6446ab(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c8df2482e5864543312990f5a80c0a04d56e56a600624cee26b7291496749bf(
    value: typing.Optional[AppsyncGraphqlApiLogConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7f52394fe3d36e25bc8b7e7a5e39856d928284a198637a679a1a9c50c868f1d(
    *,
    issuer: builtins.str,
    auth_ttl: typing.Optional[jsii.Number] = None,
    client_id: typing.Optional[builtins.str] = None,
    iat_ttl: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3821f44e0bd646401122ce5763b4e5972f62862d2b6edcde3139f498610da141(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c441fcb88dece3743252858580293cb83c1a7f61026194450473e992b947654(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0924ff43a1f672fb054efa920d9a76e7f3f8348a0dd4e87942e40207d267076(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ec6c0686f1006916974a67fb6c6ab4ec16c8078ac001afe15ac4a2ae6fc8f9c(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf48e72489bcc2416c8136fde077d8a7bf0e32bccf95ca06fc3fbd2a0486edf9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__218e32d28ffe92772917d53e786a56d2202bd59b76cb283edb10482d1f432e53(
    value: typing.Optional[AppsyncGraphqlApiOpenidConnectConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f96123bf43274cacf8899e5d518f76668b910930e4e31093e21734de7c7369da(
    *,
    default_action: builtins.str,
    user_pool_id: builtins.str,
    app_id_client_regex: typing.Optional[builtins.str] = None,
    aws_region: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02dfd490eb8ffd1dd726a024d33f7f1cb9db7b3af2baf977108bb59804c0a7ee(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d284c88871a05035bd3e42a664971d90b7b097f8b0daa320938e7ff1bedf85d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ba0014fee9df28047fece03ea378f725e10305b552fec78b7278fe9d45dd15d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3cd63955607c4010cb5c14a910bfcb7fddc8d3ca4e96e6111a1a8306e7cfd41a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f66808c863e043ce62bded0681c971a5a632314dd2e2a56e867d872deccd947(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d84c913e26f417ac6eb94adee8d388fa28cfb57e77624d7a5dd4359246a5b8d(
    value: typing.Optional[AppsyncGraphqlApiUserPoolConfig],
) -> None:
    """Type checking stubs"""
    pass
