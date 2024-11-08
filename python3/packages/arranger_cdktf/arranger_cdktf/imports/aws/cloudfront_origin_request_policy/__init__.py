'''
# `aws_cloudfront_origin_request_policy`

Refer to the Terraform Registory for docs: [`aws_cloudfront_origin_request_policy`](https://www.terraform.io/docs/providers/aws/r/cloudfront_origin_request_policy).
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


class CloudfrontOriginRequestPolicy(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudfrontOriginRequestPolicy.CloudfrontOriginRequestPolicy",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_origin_request_policy aws_cloudfront_origin_request_policy}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        cookies_config: typing.Union["CloudfrontOriginRequestPolicyCookiesConfig", typing.Dict[builtins.str, typing.Any]],
        headers_config: typing.Union["CloudfrontOriginRequestPolicyHeadersConfig", typing.Dict[builtins.str, typing.Any]],
        name: builtins.str,
        query_strings_config: typing.Union["CloudfrontOriginRequestPolicyQueryStringsConfig", typing.Dict[builtins.str, typing.Any]],
        comment: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_origin_request_policy aws_cloudfront_origin_request_policy} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param cookies_config: cookies_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_origin_request_policy#cookies_config CloudfrontOriginRequestPolicy#cookies_config}
        :param headers_config: headers_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_origin_request_policy#headers_config CloudfrontOriginRequestPolicy#headers_config}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_origin_request_policy#name CloudfrontOriginRequestPolicy#name}.
        :param query_strings_config: query_strings_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_origin_request_policy#query_strings_config CloudfrontOriginRequestPolicy#query_strings_config}
        :param comment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_origin_request_policy#comment CloudfrontOriginRequestPolicy#comment}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_origin_request_policy#id CloudfrontOriginRequestPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b9de80ecf0eed42fc40032f6ba468d2cea871b2b31fd09db4c04ef957df627c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = CloudfrontOriginRequestPolicyConfig(
            cookies_config=cookies_config,
            headers_config=headers_config,
            name=name,
            query_strings_config=query_strings_config,
            comment=comment,
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

    @jsii.member(jsii_name="putCookiesConfig")
    def put_cookies_config(
        self,
        *,
        cookie_behavior: builtins.str,
        cookies: typing.Optional[typing.Union["CloudfrontOriginRequestPolicyCookiesConfigCookies", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param cookie_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_origin_request_policy#cookie_behavior CloudfrontOriginRequestPolicy#cookie_behavior}.
        :param cookies: cookies block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_origin_request_policy#cookies CloudfrontOriginRequestPolicy#cookies}
        '''
        value = CloudfrontOriginRequestPolicyCookiesConfig(
            cookie_behavior=cookie_behavior, cookies=cookies
        )

        return typing.cast(None, jsii.invoke(self, "putCookiesConfig", [value]))

    @jsii.member(jsii_name="putHeadersConfig")
    def put_headers_config(
        self,
        *,
        header_behavior: typing.Optional[builtins.str] = None,
        headers: typing.Optional[typing.Union["CloudfrontOriginRequestPolicyHeadersConfigHeaders", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param header_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_origin_request_policy#header_behavior CloudfrontOriginRequestPolicy#header_behavior}.
        :param headers: headers block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_origin_request_policy#headers CloudfrontOriginRequestPolicy#headers}
        '''
        value = CloudfrontOriginRequestPolicyHeadersConfig(
            header_behavior=header_behavior, headers=headers
        )

        return typing.cast(None, jsii.invoke(self, "putHeadersConfig", [value]))

    @jsii.member(jsii_name="putQueryStringsConfig")
    def put_query_strings_config(
        self,
        *,
        query_string_behavior: builtins.str,
        query_strings: typing.Optional[typing.Union["CloudfrontOriginRequestPolicyQueryStringsConfigQueryStrings", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param query_string_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_origin_request_policy#query_string_behavior CloudfrontOriginRequestPolicy#query_string_behavior}.
        :param query_strings: query_strings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_origin_request_policy#query_strings CloudfrontOriginRequestPolicy#query_strings}
        '''
        value = CloudfrontOriginRequestPolicyQueryStringsConfig(
            query_string_behavior=query_string_behavior, query_strings=query_strings
        )

        return typing.cast(None, jsii.invoke(self, "putQueryStringsConfig", [value]))

    @jsii.member(jsii_name="resetComment")
    def reset_comment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComment", []))

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
    @jsii.member(jsii_name="cookiesConfig")
    def cookies_config(
        self,
    ) -> "CloudfrontOriginRequestPolicyCookiesConfigOutputReference":
        return typing.cast("CloudfrontOriginRequestPolicyCookiesConfigOutputReference", jsii.get(self, "cookiesConfig"))

    @builtins.property
    @jsii.member(jsii_name="etag")
    def etag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "etag"))

    @builtins.property
    @jsii.member(jsii_name="headersConfig")
    def headers_config(
        self,
    ) -> "CloudfrontOriginRequestPolicyHeadersConfigOutputReference":
        return typing.cast("CloudfrontOriginRequestPolicyHeadersConfigOutputReference", jsii.get(self, "headersConfig"))

    @builtins.property
    @jsii.member(jsii_name="queryStringsConfig")
    def query_strings_config(
        self,
    ) -> "CloudfrontOriginRequestPolicyQueryStringsConfigOutputReference":
        return typing.cast("CloudfrontOriginRequestPolicyQueryStringsConfigOutputReference", jsii.get(self, "queryStringsConfig"))

    @builtins.property
    @jsii.member(jsii_name="commentInput")
    def comment_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "commentInput"))

    @builtins.property
    @jsii.member(jsii_name="cookiesConfigInput")
    def cookies_config_input(
        self,
    ) -> typing.Optional["CloudfrontOriginRequestPolicyCookiesConfig"]:
        return typing.cast(typing.Optional["CloudfrontOriginRequestPolicyCookiesConfig"], jsii.get(self, "cookiesConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="headersConfigInput")
    def headers_config_input(
        self,
    ) -> typing.Optional["CloudfrontOriginRequestPolicyHeadersConfig"]:
        return typing.cast(typing.Optional["CloudfrontOriginRequestPolicyHeadersConfig"], jsii.get(self, "headersConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="queryStringsConfigInput")
    def query_strings_config_input(
        self,
    ) -> typing.Optional["CloudfrontOriginRequestPolicyQueryStringsConfig"]:
        return typing.cast(typing.Optional["CloudfrontOriginRequestPolicyQueryStringsConfig"], jsii.get(self, "queryStringsConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="comment")
    def comment(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "comment"))

    @comment.setter
    def comment(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2a38c161de7a85b48ff9cbfa5d41e206b8a45e3e4c581bbac44bb9d1e408fa3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "comment", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dccc5183c07f5c6e66f0deb2affbc11a83a11b71d889a9363d3c2e4e97d46c8a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f087a1f6d50408c15993d484925ca2b0fc09113b9b319c99f97d6652a23eb2d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="aws.cloudfrontOriginRequestPolicy.CloudfrontOriginRequestPolicyConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "cookies_config": "cookiesConfig",
        "headers_config": "headersConfig",
        "name": "name",
        "query_strings_config": "queryStringsConfig",
        "comment": "comment",
        "id": "id",
    },
)
class CloudfrontOriginRequestPolicyConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        cookies_config: typing.Union["CloudfrontOriginRequestPolicyCookiesConfig", typing.Dict[builtins.str, typing.Any]],
        headers_config: typing.Union["CloudfrontOriginRequestPolicyHeadersConfig", typing.Dict[builtins.str, typing.Any]],
        name: builtins.str,
        query_strings_config: typing.Union["CloudfrontOriginRequestPolicyQueryStringsConfig", typing.Dict[builtins.str, typing.Any]],
        comment: typing.Optional[builtins.str] = None,
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
        :param cookies_config: cookies_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_origin_request_policy#cookies_config CloudfrontOriginRequestPolicy#cookies_config}
        :param headers_config: headers_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_origin_request_policy#headers_config CloudfrontOriginRequestPolicy#headers_config}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_origin_request_policy#name CloudfrontOriginRequestPolicy#name}.
        :param query_strings_config: query_strings_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_origin_request_policy#query_strings_config CloudfrontOriginRequestPolicy#query_strings_config}
        :param comment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_origin_request_policy#comment CloudfrontOriginRequestPolicy#comment}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_origin_request_policy#id CloudfrontOriginRequestPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(cookies_config, dict):
            cookies_config = CloudfrontOriginRequestPolicyCookiesConfig(**cookies_config)
        if isinstance(headers_config, dict):
            headers_config = CloudfrontOriginRequestPolicyHeadersConfig(**headers_config)
        if isinstance(query_strings_config, dict):
            query_strings_config = CloudfrontOriginRequestPolicyQueryStringsConfig(**query_strings_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa8fe381a05de48d46240cad45f71eacc33c6d1c80483385528a063d6a76bcb0)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument cookies_config", value=cookies_config, expected_type=type_hints["cookies_config"])
            check_type(argname="argument headers_config", value=headers_config, expected_type=type_hints["headers_config"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument query_strings_config", value=query_strings_config, expected_type=type_hints["query_strings_config"])
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cookies_config": cookies_config,
            "headers_config": headers_config,
            "name": name,
            "query_strings_config": query_strings_config,
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
        if comment is not None:
            self._values["comment"] = comment
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
    def cookies_config(self) -> "CloudfrontOriginRequestPolicyCookiesConfig":
        '''cookies_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_origin_request_policy#cookies_config CloudfrontOriginRequestPolicy#cookies_config}
        '''
        result = self._values.get("cookies_config")
        assert result is not None, "Required property 'cookies_config' is missing"
        return typing.cast("CloudfrontOriginRequestPolicyCookiesConfig", result)

    @builtins.property
    def headers_config(self) -> "CloudfrontOriginRequestPolicyHeadersConfig":
        '''headers_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_origin_request_policy#headers_config CloudfrontOriginRequestPolicy#headers_config}
        '''
        result = self._values.get("headers_config")
        assert result is not None, "Required property 'headers_config' is missing"
        return typing.cast("CloudfrontOriginRequestPolicyHeadersConfig", result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_origin_request_policy#name CloudfrontOriginRequestPolicy#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def query_strings_config(self) -> "CloudfrontOriginRequestPolicyQueryStringsConfig":
        '''query_strings_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_origin_request_policy#query_strings_config CloudfrontOriginRequestPolicy#query_strings_config}
        '''
        result = self._values.get("query_strings_config")
        assert result is not None, "Required property 'query_strings_config' is missing"
        return typing.cast("CloudfrontOriginRequestPolicyQueryStringsConfig", result)

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_origin_request_policy#comment CloudfrontOriginRequestPolicy#comment}.'''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_origin_request_policy#id CloudfrontOriginRequestPolicy#id}.

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
        return "CloudfrontOriginRequestPolicyConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.cloudfrontOriginRequestPolicy.CloudfrontOriginRequestPolicyCookiesConfig",
    jsii_struct_bases=[],
    name_mapping={"cookie_behavior": "cookieBehavior", "cookies": "cookies"},
)
class CloudfrontOriginRequestPolicyCookiesConfig:
    def __init__(
        self,
        *,
        cookie_behavior: builtins.str,
        cookies: typing.Optional[typing.Union["CloudfrontOriginRequestPolicyCookiesConfigCookies", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param cookie_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_origin_request_policy#cookie_behavior CloudfrontOriginRequestPolicy#cookie_behavior}.
        :param cookies: cookies block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_origin_request_policy#cookies CloudfrontOriginRequestPolicy#cookies}
        '''
        if isinstance(cookies, dict):
            cookies = CloudfrontOriginRequestPolicyCookiesConfigCookies(**cookies)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d882065aaa68264b62b157468bac2090580e8307611eafe45cc60a8990a0bac)
            check_type(argname="argument cookie_behavior", value=cookie_behavior, expected_type=type_hints["cookie_behavior"])
            check_type(argname="argument cookies", value=cookies, expected_type=type_hints["cookies"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cookie_behavior": cookie_behavior,
        }
        if cookies is not None:
            self._values["cookies"] = cookies

    @builtins.property
    def cookie_behavior(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_origin_request_policy#cookie_behavior CloudfrontOriginRequestPolicy#cookie_behavior}.'''
        result = self._values.get("cookie_behavior")
        assert result is not None, "Required property 'cookie_behavior' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cookies(
        self,
    ) -> typing.Optional["CloudfrontOriginRequestPolicyCookiesConfigCookies"]:
        '''cookies block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_origin_request_policy#cookies CloudfrontOriginRequestPolicy#cookies}
        '''
        result = self._values.get("cookies")
        return typing.cast(typing.Optional["CloudfrontOriginRequestPolicyCookiesConfigCookies"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudfrontOriginRequestPolicyCookiesConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.cloudfrontOriginRequestPolicy.CloudfrontOriginRequestPolicyCookiesConfigCookies",
    jsii_struct_bases=[],
    name_mapping={"items": "items"},
)
class CloudfrontOriginRequestPolicyCookiesConfigCookies:
    def __init__(
        self,
        *,
        items: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param items: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_origin_request_policy#items CloudfrontOriginRequestPolicy#items}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59a7d647f2391f89d5758eafcd6d2c0399f12b5098ef7060b31e49b44545dec3)
            check_type(argname="argument items", value=items, expected_type=type_hints["items"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if items is not None:
            self._values["items"] = items

    @builtins.property
    def items(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_origin_request_policy#items CloudfrontOriginRequestPolicy#items}.'''
        result = self._values.get("items")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudfrontOriginRequestPolicyCookiesConfigCookies(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudfrontOriginRequestPolicyCookiesConfigCookiesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudfrontOriginRequestPolicy.CloudfrontOriginRequestPolicyCookiesConfigCookiesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3a7b10ef7b1845b0c5dd27e088412ea1254abeee50d09e151532359758ccb17f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetItems")
    def reset_items(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetItems", []))

    @builtins.property
    @jsii.member(jsii_name="itemsInput")
    def items_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "itemsInput"))

    @builtins.property
    @jsii.member(jsii_name="items")
    def items(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "items"))

    @items.setter
    def items(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1df00e5897155e8afb9b1241bc5c0952ec1c52f51b1b9337d434083c4de9171)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "items", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CloudfrontOriginRequestPolicyCookiesConfigCookies]:
        return typing.cast(typing.Optional[CloudfrontOriginRequestPolicyCookiesConfigCookies], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudfrontOriginRequestPolicyCookiesConfigCookies],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8769c17784ba807d4b348cb65594a9814b2c961b33b90279c77408f41eb88738)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CloudfrontOriginRequestPolicyCookiesConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudfrontOriginRequestPolicy.CloudfrontOriginRequestPolicyCookiesConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b164e4d515469a1cf719ae006b76a9f7c7aba1142b3fb0d1e252cc715dc2c08b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCookies")
    def put_cookies(
        self,
        *,
        items: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param items: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_origin_request_policy#items CloudfrontOriginRequestPolicy#items}.
        '''
        value = CloudfrontOriginRequestPolicyCookiesConfigCookies(items=items)

        return typing.cast(None, jsii.invoke(self, "putCookies", [value]))

    @jsii.member(jsii_name="resetCookies")
    def reset_cookies(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCookies", []))

    @builtins.property
    @jsii.member(jsii_name="cookies")
    def cookies(
        self,
    ) -> CloudfrontOriginRequestPolicyCookiesConfigCookiesOutputReference:
        return typing.cast(CloudfrontOriginRequestPolicyCookiesConfigCookiesOutputReference, jsii.get(self, "cookies"))

    @builtins.property
    @jsii.member(jsii_name="cookieBehaviorInput")
    def cookie_behavior_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cookieBehaviorInput"))

    @builtins.property
    @jsii.member(jsii_name="cookiesInput")
    def cookies_input(
        self,
    ) -> typing.Optional[CloudfrontOriginRequestPolicyCookiesConfigCookies]:
        return typing.cast(typing.Optional[CloudfrontOriginRequestPolicyCookiesConfigCookies], jsii.get(self, "cookiesInput"))

    @builtins.property
    @jsii.member(jsii_name="cookieBehavior")
    def cookie_behavior(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cookieBehavior"))

    @cookie_behavior.setter
    def cookie_behavior(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f83576219240e38bd039d5f6c955a9524ac15a67e7b046792502ca6f1fd5261)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cookieBehavior", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CloudfrontOriginRequestPolicyCookiesConfig]:
        return typing.cast(typing.Optional[CloudfrontOriginRequestPolicyCookiesConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudfrontOriginRequestPolicyCookiesConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__844b110d745854a278d171444c921f561101f4f5e08f5057a7f947d074d10b22)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.cloudfrontOriginRequestPolicy.CloudfrontOriginRequestPolicyHeadersConfig",
    jsii_struct_bases=[],
    name_mapping={"header_behavior": "headerBehavior", "headers": "headers"},
)
class CloudfrontOriginRequestPolicyHeadersConfig:
    def __init__(
        self,
        *,
        header_behavior: typing.Optional[builtins.str] = None,
        headers: typing.Optional[typing.Union["CloudfrontOriginRequestPolicyHeadersConfigHeaders", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param header_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_origin_request_policy#header_behavior CloudfrontOriginRequestPolicy#header_behavior}.
        :param headers: headers block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_origin_request_policy#headers CloudfrontOriginRequestPolicy#headers}
        '''
        if isinstance(headers, dict):
            headers = CloudfrontOriginRequestPolicyHeadersConfigHeaders(**headers)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68bbfd175ecdd6cbf24072562229b83ac95108c95c88ce18ed06e74230570a59)
            check_type(argname="argument header_behavior", value=header_behavior, expected_type=type_hints["header_behavior"])
            check_type(argname="argument headers", value=headers, expected_type=type_hints["headers"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if header_behavior is not None:
            self._values["header_behavior"] = header_behavior
        if headers is not None:
            self._values["headers"] = headers

    @builtins.property
    def header_behavior(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_origin_request_policy#header_behavior CloudfrontOriginRequestPolicy#header_behavior}.'''
        result = self._values.get("header_behavior")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def headers(
        self,
    ) -> typing.Optional["CloudfrontOriginRequestPolicyHeadersConfigHeaders"]:
        '''headers block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_origin_request_policy#headers CloudfrontOriginRequestPolicy#headers}
        '''
        result = self._values.get("headers")
        return typing.cast(typing.Optional["CloudfrontOriginRequestPolicyHeadersConfigHeaders"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudfrontOriginRequestPolicyHeadersConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.cloudfrontOriginRequestPolicy.CloudfrontOriginRequestPolicyHeadersConfigHeaders",
    jsii_struct_bases=[],
    name_mapping={"items": "items"},
)
class CloudfrontOriginRequestPolicyHeadersConfigHeaders:
    def __init__(
        self,
        *,
        items: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param items: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_origin_request_policy#items CloudfrontOriginRequestPolicy#items}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7dfb4b3c064f525c8300e00bb72fa421864e2288fb812cedd05e0c4ce3853a49)
            check_type(argname="argument items", value=items, expected_type=type_hints["items"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if items is not None:
            self._values["items"] = items

    @builtins.property
    def items(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_origin_request_policy#items CloudfrontOriginRequestPolicy#items}.'''
        result = self._values.get("items")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudfrontOriginRequestPolicyHeadersConfigHeaders(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudfrontOriginRequestPolicyHeadersConfigHeadersOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudfrontOriginRequestPolicy.CloudfrontOriginRequestPolicyHeadersConfigHeadersOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__89da5b50c8c7224f121fdba1a0dd8aacab361f56e9805f84685191af209ea91b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetItems")
    def reset_items(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetItems", []))

    @builtins.property
    @jsii.member(jsii_name="itemsInput")
    def items_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "itemsInput"))

    @builtins.property
    @jsii.member(jsii_name="items")
    def items(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "items"))

    @items.setter
    def items(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1fd1d4fc7b0784f82d9fbe740f4f5f100506715d938897ec10c3687b6a38e202)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "items", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CloudfrontOriginRequestPolicyHeadersConfigHeaders]:
        return typing.cast(typing.Optional[CloudfrontOriginRequestPolicyHeadersConfigHeaders], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudfrontOriginRequestPolicyHeadersConfigHeaders],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74d650a1fd2dd2fb02f4ea64edfe549fe69cb8023fb5e32c407c971f45a8f6a6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CloudfrontOriginRequestPolicyHeadersConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudfrontOriginRequestPolicy.CloudfrontOriginRequestPolicyHeadersConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8dbd09bc0d6b2f77c51f5546d0e75d318c8dbfc0c752470661a6d67c8c9dd045)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putHeaders")
    def put_headers(
        self,
        *,
        items: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param items: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_origin_request_policy#items CloudfrontOriginRequestPolicy#items}.
        '''
        value = CloudfrontOriginRequestPolicyHeadersConfigHeaders(items=items)

        return typing.cast(None, jsii.invoke(self, "putHeaders", [value]))

    @jsii.member(jsii_name="resetHeaderBehavior")
    def reset_header_behavior(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeaderBehavior", []))

    @jsii.member(jsii_name="resetHeaders")
    def reset_headers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeaders", []))

    @builtins.property
    @jsii.member(jsii_name="headers")
    def headers(
        self,
    ) -> CloudfrontOriginRequestPolicyHeadersConfigHeadersOutputReference:
        return typing.cast(CloudfrontOriginRequestPolicyHeadersConfigHeadersOutputReference, jsii.get(self, "headers"))

    @builtins.property
    @jsii.member(jsii_name="headerBehaviorInput")
    def header_behavior_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "headerBehaviorInput"))

    @builtins.property
    @jsii.member(jsii_name="headersInput")
    def headers_input(
        self,
    ) -> typing.Optional[CloudfrontOriginRequestPolicyHeadersConfigHeaders]:
        return typing.cast(typing.Optional[CloudfrontOriginRequestPolicyHeadersConfigHeaders], jsii.get(self, "headersInput"))

    @builtins.property
    @jsii.member(jsii_name="headerBehavior")
    def header_behavior(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "headerBehavior"))

    @header_behavior.setter
    def header_behavior(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4cc8337f312cfbed2ba6995c8522978dd4f017e208942b383580c8deb525c5c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "headerBehavior", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CloudfrontOriginRequestPolicyHeadersConfig]:
        return typing.cast(typing.Optional[CloudfrontOriginRequestPolicyHeadersConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudfrontOriginRequestPolicyHeadersConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4fd090aa10384d55d9d9102ea7160917b2fd6bc1f774cfbb09100ea70f8eb601)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.cloudfrontOriginRequestPolicy.CloudfrontOriginRequestPolicyQueryStringsConfig",
    jsii_struct_bases=[],
    name_mapping={
        "query_string_behavior": "queryStringBehavior",
        "query_strings": "queryStrings",
    },
)
class CloudfrontOriginRequestPolicyQueryStringsConfig:
    def __init__(
        self,
        *,
        query_string_behavior: builtins.str,
        query_strings: typing.Optional[typing.Union["CloudfrontOriginRequestPolicyQueryStringsConfigQueryStrings", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param query_string_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_origin_request_policy#query_string_behavior CloudfrontOriginRequestPolicy#query_string_behavior}.
        :param query_strings: query_strings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_origin_request_policy#query_strings CloudfrontOriginRequestPolicy#query_strings}
        '''
        if isinstance(query_strings, dict):
            query_strings = CloudfrontOriginRequestPolicyQueryStringsConfigQueryStrings(**query_strings)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c64da6d5aa5070741ff6651e5a4198a4cfbbb411bcc85f88b4cfe78cf5aa9915)
            check_type(argname="argument query_string_behavior", value=query_string_behavior, expected_type=type_hints["query_string_behavior"])
            check_type(argname="argument query_strings", value=query_strings, expected_type=type_hints["query_strings"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "query_string_behavior": query_string_behavior,
        }
        if query_strings is not None:
            self._values["query_strings"] = query_strings

    @builtins.property
    def query_string_behavior(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_origin_request_policy#query_string_behavior CloudfrontOriginRequestPolicy#query_string_behavior}.'''
        result = self._values.get("query_string_behavior")
        assert result is not None, "Required property 'query_string_behavior' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def query_strings(
        self,
    ) -> typing.Optional["CloudfrontOriginRequestPolicyQueryStringsConfigQueryStrings"]:
        '''query_strings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_origin_request_policy#query_strings CloudfrontOriginRequestPolicy#query_strings}
        '''
        result = self._values.get("query_strings")
        return typing.cast(typing.Optional["CloudfrontOriginRequestPolicyQueryStringsConfigQueryStrings"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudfrontOriginRequestPolicyQueryStringsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudfrontOriginRequestPolicyQueryStringsConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudfrontOriginRequestPolicy.CloudfrontOriginRequestPolicyQueryStringsConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__be88cba83dfdd4a3e731817ec7419a4fad5699c69067ec6f1ee33df2d4cbf771)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putQueryStrings")
    def put_query_strings(
        self,
        *,
        items: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param items: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_origin_request_policy#items CloudfrontOriginRequestPolicy#items}.
        '''
        value = CloudfrontOriginRequestPolicyQueryStringsConfigQueryStrings(
            items=items
        )

        return typing.cast(None, jsii.invoke(self, "putQueryStrings", [value]))

    @jsii.member(jsii_name="resetQueryStrings")
    def reset_query_strings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueryStrings", []))

    @builtins.property
    @jsii.member(jsii_name="queryStrings")
    def query_strings(
        self,
    ) -> "CloudfrontOriginRequestPolicyQueryStringsConfigQueryStringsOutputReference":
        return typing.cast("CloudfrontOriginRequestPolicyQueryStringsConfigQueryStringsOutputReference", jsii.get(self, "queryStrings"))

    @builtins.property
    @jsii.member(jsii_name="queryStringBehaviorInput")
    def query_string_behavior_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryStringBehaviorInput"))

    @builtins.property
    @jsii.member(jsii_name="queryStringsInput")
    def query_strings_input(
        self,
    ) -> typing.Optional["CloudfrontOriginRequestPolicyQueryStringsConfigQueryStrings"]:
        return typing.cast(typing.Optional["CloudfrontOriginRequestPolicyQueryStringsConfigQueryStrings"], jsii.get(self, "queryStringsInput"))

    @builtins.property
    @jsii.member(jsii_name="queryStringBehavior")
    def query_string_behavior(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "queryStringBehavior"))

    @query_string_behavior.setter
    def query_string_behavior(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0ef1b1341e643205579783bd334254af4120249023ebf7a85fd3ee123bb23ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queryStringBehavior", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CloudfrontOriginRequestPolicyQueryStringsConfig]:
        return typing.cast(typing.Optional[CloudfrontOriginRequestPolicyQueryStringsConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudfrontOriginRequestPolicyQueryStringsConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ec33eba0b9594ab203e016238d77d43c2a067e5a89826dbf1dac753ec74b2be)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.cloudfrontOriginRequestPolicy.CloudfrontOriginRequestPolicyQueryStringsConfigQueryStrings",
    jsii_struct_bases=[],
    name_mapping={"items": "items"},
)
class CloudfrontOriginRequestPolicyQueryStringsConfigQueryStrings:
    def __init__(
        self,
        *,
        items: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param items: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_origin_request_policy#items CloudfrontOriginRequestPolicy#items}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ede8a13e4440cc979684a5190f0bcad97958b390497c40ecbfca4d6f8da97ecd)
            check_type(argname="argument items", value=items, expected_type=type_hints["items"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if items is not None:
            self._values["items"] = items

    @builtins.property
    def items(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_origin_request_policy#items CloudfrontOriginRequestPolicy#items}.'''
        result = self._values.get("items")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudfrontOriginRequestPolicyQueryStringsConfigQueryStrings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudfrontOriginRequestPolicyQueryStringsConfigQueryStringsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudfrontOriginRequestPolicy.CloudfrontOriginRequestPolicyQueryStringsConfigQueryStringsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5fea3a25a89d4dc88cd48859f8ce44ee3f8211c29233bfa4bd3c2e4d57666f0f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetItems")
    def reset_items(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetItems", []))

    @builtins.property
    @jsii.member(jsii_name="itemsInput")
    def items_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "itemsInput"))

    @builtins.property
    @jsii.member(jsii_name="items")
    def items(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "items"))

    @items.setter
    def items(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b905f29c7cbd0971f3539635f3f0f93278c07a170b9286f3fac473f63c049863)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "items", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CloudfrontOriginRequestPolicyQueryStringsConfigQueryStrings]:
        return typing.cast(typing.Optional[CloudfrontOriginRequestPolicyQueryStringsConfigQueryStrings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudfrontOriginRequestPolicyQueryStringsConfigQueryStrings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0be639844caa46ee8a3f25a09ea71bac15ad1c918d4174627ffe66731e0c506f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "CloudfrontOriginRequestPolicy",
    "CloudfrontOriginRequestPolicyConfig",
    "CloudfrontOriginRequestPolicyCookiesConfig",
    "CloudfrontOriginRequestPolicyCookiesConfigCookies",
    "CloudfrontOriginRequestPolicyCookiesConfigCookiesOutputReference",
    "CloudfrontOriginRequestPolicyCookiesConfigOutputReference",
    "CloudfrontOriginRequestPolicyHeadersConfig",
    "CloudfrontOriginRequestPolicyHeadersConfigHeaders",
    "CloudfrontOriginRequestPolicyHeadersConfigHeadersOutputReference",
    "CloudfrontOriginRequestPolicyHeadersConfigOutputReference",
    "CloudfrontOriginRequestPolicyQueryStringsConfig",
    "CloudfrontOriginRequestPolicyQueryStringsConfigOutputReference",
    "CloudfrontOriginRequestPolicyQueryStringsConfigQueryStrings",
    "CloudfrontOriginRequestPolicyQueryStringsConfigQueryStringsOutputReference",
]

publication.publish()

def _typecheckingstub__0b9de80ecf0eed42fc40032f6ba468d2cea871b2b31fd09db4c04ef957df627c(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    cookies_config: typing.Union[CloudfrontOriginRequestPolicyCookiesConfig, typing.Dict[builtins.str, typing.Any]],
    headers_config: typing.Union[CloudfrontOriginRequestPolicyHeadersConfig, typing.Dict[builtins.str, typing.Any]],
    name: builtins.str,
    query_strings_config: typing.Union[CloudfrontOriginRequestPolicyQueryStringsConfig, typing.Dict[builtins.str, typing.Any]],
    comment: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__a2a38c161de7a85b48ff9cbfa5d41e206b8a45e3e4c581bbac44bb9d1e408fa3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dccc5183c07f5c6e66f0deb2affbc11a83a11b71d889a9363d3c2e4e97d46c8a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f087a1f6d50408c15993d484925ca2b0fc09113b9b319c99f97d6652a23eb2d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa8fe381a05de48d46240cad45f71eacc33c6d1c80483385528a063d6a76bcb0(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    cookies_config: typing.Union[CloudfrontOriginRequestPolicyCookiesConfig, typing.Dict[builtins.str, typing.Any]],
    headers_config: typing.Union[CloudfrontOriginRequestPolicyHeadersConfig, typing.Dict[builtins.str, typing.Any]],
    name: builtins.str,
    query_strings_config: typing.Union[CloudfrontOriginRequestPolicyQueryStringsConfig, typing.Dict[builtins.str, typing.Any]],
    comment: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d882065aaa68264b62b157468bac2090580e8307611eafe45cc60a8990a0bac(
    *,
    cookie_behavior: builtins.str,
    cookies: typing.Optional[typing.Union[CloudfrontOriginRequestPolicyCookiesConfigCookies, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59a7d647f2391f89d5758eafcd6d2c0399f12b5098ef7060b31e49b44545dec3(
    *,
    items: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a7b10ef7b1845b0c5dd27e088412ea1254abeee50d09e151532359758ccb17f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1df00e5897155e8afb9b1241bc5c0952ec1c52f51b1b9337d434083c4de9171(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8769c17784ba807d4b348cb65594a9814b2c961b33b90279c77408f41eb88738(
    value: typing.Optional[CloudfrontOriginRequestPolicyCookiesConfigCookies],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b164e4d515469a1cf719ae006b76a9f7c7aba1142b3fb0d1e252cc715dc2c08b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f83576219240e38bd039d5f6c955a9524ac15a67e7b046792502ca6f1fd5261(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__844b110d745854a278d171444c921f561101f4f5e08f5057a7f947d074d10b22(
    value: typing.Optional[CloudfrontOriginRequestPolicyCookiesConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68bbfd175ecdd6cbf24072562229b83ac95108c95c88ce18ed06e74230570a59(
    *,
    header_behavior: typing.Optional[builtins.str] = None,
    headers: typing.Optional[typing.Union[CloudfrontOriginRequestPolicyHeadersConfigHeaders, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7dfb4b3c064f525c8300e00bb72fa421864e2288fb812cedd05e0c4ce3853a49(
    *,
    items: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89da5b50c8c7224f121fdba1a0dd8aacab361f56e9805f84685191af209ea91b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1fd1d4fc7b0784f82d9fbe740f4f5f100506715d938897ec10c3687b6a38e202(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74d650a1fd2dd2fb02f4ea64edfe549fe69cb8023fb5e32c407c971f45a8f6a6(
    value: typing.Optional[CloudfrontOriginRequestPolicyHeadersConfigHeaders],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8dbd09bc0d6b2f77c51f5546d0e75d318c8dbfc0c752470661a6d67c8c9dd045(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4cc8337f312cfbed2ba6995c8522978dd4f017e208942b383580c8deb525c5c2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4fd090aa10384d55d9d9102ea7160917b2fd6bc1f774cfbb09100ea70f8eb601(
    value: typing.Optional[CloudfrontOriginRequestPolicyHeadersConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c64da6d5aa5070741ff6651e5a4198a4cfbbb411bcc85f88b4cfe78cf5aa9915(
    *,
    query_string_behavior: builtins.str,
    query_strings: typing.Optional[typing.Union[CloudfrontOriginRequestPolicyQueryStringsConfigQueryStrings, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be88cba83dfdd4a3e731817ec7419a4fad5699c69067ec6f1ee33df2d4cbf771(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0ef1b1341e643205579783bd334254af4120249023ebf7a85fd3ee123bb23ab(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ec33eba0b9594ab203e016238d77d43c2a067e5a89826dbf1dac753ec74b2be(
    value: typing.Optional[CloudfrontOriginRequestPolicyQueryStringsConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ede8a13e4440cc979684a5190f0bcad97958b390497c40ecbfca4d6f8da97ecd(
    *,
    items: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5fea3a25a89d4dc88cd48859f8ce44ee3f8211c29233bfa4bd3c2e4d57666f0f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b905f29c7cbd0971f3539635f3f0f93278c07a170b9286f3fac473f63c049863(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0be639844caa46ee8a3f25a09ea71bac15ad1c918d4174627ffe66731e0c506f(
    value: typing.Optional[CloudfrontOriginRequestPolicyQueryStringsConfigQueryStrings],
) -> None:
    """Type checking stubs"""
    pass
