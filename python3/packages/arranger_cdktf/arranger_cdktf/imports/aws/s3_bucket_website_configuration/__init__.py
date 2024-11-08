'''
# `aws_s3_bucket_website_configuration`

Refer to the Terraform Registory for docs: [`aws_s3_bucket_website_configuration`](https://www.terraform.io/docs/providers/aws/r/s3_bucket_website_configuration).
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


class S3BucketWebsiteConfiguration(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3BucketWebsiteConfiguration.S3BucketWebsiteConfiguration",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_website_configuration aws_s3_bucket_website_configuration}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        bucket: builtins.str,
        error_document: typing.Optional[typing.Union["S3BucketWebsiteConfigurationErrorDocument", typing.Dict[builtins.str, typing.Any]]] = None,
        expected_bucket_owner: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        index_document: typing.Optional[typing.Union["S3BucketWebsiteConfigurationIndexDocument", typing.Dict[builtins.str, typing.Any]]] = None,
        redirect_all_requests_to: typing.Optional[typing.Union["S3BucketWebsiteConfigurationRedirectAllRequestsTo", typing.Dict[builtins.str, typing.Any]]] = None,
        routing_rule: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["S3BucketWebsiteConfigurationRoutingRule", typing.Dict[builtins.str, typing.Any]]]]] = None,
        routing_rules: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_website_configuration aws_s3_bucket_website_configuration} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_website_configuration#bucket S3BucketWebsiteConfiguration#bucket}.
        :param error_document: error_document block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_website_configuration#error_document S3BucketWebsiteConfiguration#error_document}
        :param expected_bucket_owner: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_website_configuration#expected_bucket_owner S3BucketWebsiteConfiguration#expected_bucket_owner}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_website_configuration#id S3BucketWebsiteConfiguration#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param index_document: index_document block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_website_configuration#index_document S3BucketWebsiteConfiguration#index_document}
        :param redirect_all_requests_to: redirect_all_requests_to block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_website_configuration#redirect_all_requests_to S3BucketWebsiteConfiguration#redirect_all_requests_to}
        :param routing_rule: routing_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_website_configuration#routing_rule S3BucketWebsiteConfiguration#routing_rule}
        :param routing_rules: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_website_configuration#routing_rules S3BucketWebsiteConfiguration#routing_rules}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f125c8c5ceb6ac5fb10447b6ef2c452d2f7bcb0714e5aef3edaef14fcb5462e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = S3BucketWebsiteConfigurationConfig(
            bucket=bucket,
            error_document=error_document,
            expected_bucket_owner=expected_bucket_owner,
            id=id,
            index_document=index_document,
            redirect_all_requests_to=redirect_all_requests_to,
            routing_rule=routing_rule,
            routing_rules=routing_rules,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putErrorDocument")
    def put_error_document(self, *, key: builtins.str) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_website_configuration#key S3BucketWebsiteConfiguration#key}.
        '''
        value = S3BucketWebsiteConfigurationErrorDocument(key=key)

        return typing.cast(None, jsii.invoke(self, "putErrorDocument", [value]))

    @jsii.member(jsii_name="putIndexDocument")
    def put_index_document(self, *, suffix: builtins.str) -> None:
        '''
        :param suffix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_website_configuration#suffix S3BucketWebsiteConfiguration#suffix}.
        '''
        value = S3BucketWebsiteConfigurationIndexDocument(suffix=suffix)

        return typing.cast(None, jsii.invoke(self, "putIndexDocument", [value]))

    @jsii.member(jsii_name="putRedirectAllRequestsTo")
    def put_redirect_all_requests_to(
        self,
        *,
        host_name: builtins.str,
        protocol: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param host_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_website_configuration#host_name S3BucketWebsiteConfiguration#host_name}.
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_website_configuration#protocol S3BucketWebsiteConfiguration#protocol}.
        '''
        value = S3BucketWebsiteConfigurationRedirectAllRequestsTo(
            host_name=host_name, protocol=protocol
        )

        return typing.cast(None, jsii.invoke(self, "putRedirectAllRequestsTo", [value]))

    @jsii.member(jsii_name="putRoutingRule")
    def put_routing_rule(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["S3BucketWebsiteConfigurationRoutingRule", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a94d408966f92f2a3e36a707050c58675ce1e8c7842da94eb5c75d3b9aff047)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRoutingRule", [value]))

    @jsii.member(jsii_name="resetErrorDocument")
    def reset_error_document(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetErrorDocument", []))

    @jsii.member(jsii_name="resetExpectedBucketOwner")
    def reset_expected_bucket_owner(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExpectedBucketOwner", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIndexDocument")
    def reset_index_document(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIndexDocument", []))

    @jsii.member(jsii_name="resetRedirectAllRequestsTo")
    def reset_redirect_all_requests_to(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedirectAllRequestsTo", []))

    @jsii.member(jsii_name="resetRoutingRule")
    def reset_routing_rule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRoutingRule", []))

    @jsii.member(jsii_name="resetRoutingRules")
    def reset_routing_rules(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRoutingRules", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="errorDocument")
    def error_document(
        self,
    ) -> "S3BucketWebsiteConfigurationErrorDocumentOutputReference":
        return typing.cast("S3BucketWebsiteConfigurationErrorDocumentOutputReference", jsii.get(self, "errorDocument"))

    @builtins.property
    @jsii.member(jsii_name="indexDocument")
    def index_document(
        self,
    ) -> "S3BucketWebsiteConfigurationIndexDocumentOutputReference":
        return typing.cast("S3BucketWebsiteConfigurationIndexDocumentOutputReference", jsii.get(self, "indexDocument"))

    @builtins.property
    @jsii.member(jsii_name="redirectAllRequestsTo")
    def redirect_all_requests_to(
        self,
    ) -> "S3BucketWebsiteConfigurationRedirectAllRequestsToOutputReference":
        return typing.cast("S3BucketWebsiteConfigurationRedirectAllRequestsToOutputReference", jsii.get(self, "redirectAllRequestsTo"))

    @builtins.property
    @jsii.member(jsii_name="routingRule")
    def routing_rule(self) -> "S3BucketWebsiteConfigurationRoutingRuleList":
        return typing.cast("S3BucketWebsiteConfigurationRoutingRuleList", jsii.get(self, "routingRule"))

    @builtins.property
    @jsii.member(jsii_name="websiteDomain")
    def website_domain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "websiteDomain"))

    @builtins.property
    @jsii.member(jsii_name="websiteEndpoint")
    def website_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "websiteEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="bucketInput")
    def bucket_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketInput"))

    @builtins.property
    @jsii.member(jsii_name="errorDocumentInput")
    def error_document_input(
        self,
    ) -> typing.Optional["S3BucketWebsiteConfigurationErrorDocument"]:
        return typing.cast(typing.Optional["S3BucketWebsiteConfigurationErrorDocument"], jsii.get(self, "errorDocumentInput"))

    @builtins.property
    @jsii.member(jsii_name="expectedBucketOwnerInput")
    def expected_bucket_owner_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "expectedBucketOwnerInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="indexDocumentInput")
    def index_document_input(
        self,
    ) -> typing.Optional["S3BucketWebsiteConfigurationIndexDocument"]:
        return typing.cast(typing.Optional["S3BucketWebsiteConfigurationIndexDocument"], jsii.get(self, "indexDocumentInput"))

    @builtins.property
    @jsii.member(jsii_name="redirectAllRequestsToInput")
    def redirect_all_requests_to_input(
        self,
    ) -> typing.Optional["S3BucketWebsiteConfigurationRedirectAllRequestsTo"]:
        return typing.cast(typing.Optional["S3BucketWebsiteConfigurationRedirectAllRequestsTo"], jsii.get(self, "redirectAllRequestsToInput"))

    @builtins.property
    @jsii.member(jsii_name="routingRuleInput")
    def routing_rule_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["S3BucketWebsiteConfigurationRoutingRule"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["S3BucketWebsiteConfigurationRoutingRule"]]], jsii.get(self, "routingRuleInput"))

    @builtins.property
    @jsii.member(jsii_name="routingRulesInput")
    def routing_rules_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "routingRulesInput"))

    @builtins.property
    @jsii.member(jsii_name="bucket")
    def bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucket"))

    @bucket.setter
    def bucket(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d519b0ab2e7bb5129c9ccae53ab84cd4c5d2418183d5d1b82b7caefba5322be9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucket", value)

    @builtins.property
    @jsii.member(jsii_name="expectedBucketOwner")
    def expected_bucket_owner(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expectedBucketOwner"))

    @expected_bucket_owner.setter
    def expected_bucket_owner(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__363ef195560b57a60723933d0db42aa062d3a15b0d55ce7cc40f4c4ff9a9532f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expectedBucketOwner", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__71c13e0383d5dbeaed2cdf3671a681a0d1d1e70ab1de93a923995312c2aaf1a8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="routingRules")
    def routing_rules(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "routingRules"))

    @routing_rules.setter
    def routing_rules(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1d17f5525a526cd48fc6f7b724811c16fb47d88b20c6c3956094e3ad82449ef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "routingRules", value)


@jsii.data_type(
    jsii_type="aws.s3BucketWebsiteConfiguration.S3BucketWebsiteConfigurationConfig",
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
        "error_document": "errorDocument",
        "expected_bucket_owner": "expectedBucketOwner",
        "id": "id",
        "index_document": "indexDocument",
        "redirect_all_requests_to": "redirectAllRequestsTo",
        "routing_rule": "routingRule",
        "routing_rules": "routingRules",
    },
)
class S3BucketWebsiteConfigurationConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        error_document: typing.Optional[typing.Union["S3BucketWebsiteConfigurationErrorDocument", typing.Dict[builtins.str, typing.Any]]] = None,
        expected_bucket_owner: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        index_document: typing.Optional[typing.Union["S3BucketWebsiteConfigurationIndexDocument", typing.Dict[builtins.str, typing.Any]]] = None,
        redirect_all_requests_to: typing.Optional[typing.Union["S3BucketWebsiteConfigurationRedirectAllRequestsTo", typing.Dict[builtins.str, typing.Any]]] = None,
        routing_rule: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["S3BucketWebsiteConfigurationRoutingRule", typing.Dict[builtins.str, typing.Any]]]]] = None,
        routing_rules: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_website_configuration#bucket S3BucketWebsiteConfiguration#bucket}.
        :param error_document: error_document block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_website_configuration#error_document S3BucketWebsiteConfiguration#error_document}
        :param expected_bucket_owner: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_website_configuration#expected_bucket_owner S3BucketWebsiteConfiguration#expected_bucket_owner}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_website_configuration#id S3BucketWebsiteConfiguration#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param index_document: index_document block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_website_configuration#index_document S3BucketWebsiteConfiguration#index_document}
        :param redirect_all_requests_to: redirect_all_requests_to block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_website_configuration#redirect_all_requests_to S3BucketWebsiteConfiguration#redirect_all_requests_to}
        :param routing_rule: routing_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_website_configuration#routing_rule S3BucketWebsiteConfiguration#routing_rule}
        :param routing_rules: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_website_configuration#routing_rules S3BucketWebsiteConfiguration#routing_rules}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(error_document, dict):
            error_document = S3BucketWebsiteConfigurationErrorDocument(**error_document)
        if isinstance(index_document, dict):
            index_document = S3BucketWebsiteConfigurationIndexDocument(**index_document)
        if isinstance(redirect_all_requests_to, dict):
            redirect_all_requests_to = S3BucketWebsiteConfigurationRedirectAllRequestsTo(**redirect_all_requests_to)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0e436e27cd4193084edafee6474635fab0d90a34d77042e325847daf329c43d)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument error_document", value=error_document, expected_type=type_hints["error_document"])
            check_type(argname="argument expected_bucket_owner", value=expected_bucket_owner, expected_type=type_hints["expected_bucket_owner"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument index_document", value=index_document, expected_type=type_hints["index_document"])
            check_type(argname="argument redirect_all_requests_to", value=redirect_all_requests_to, expected_type=type_hints["redirect_all_requests_to"])
            check_type(argname="argument routing_rule", value=routing_rule, expected_type=type_hints["routing_rule"])
            check_type(argname="argument routing_rules", value=routing_rules, expected_type=type_hints["routing_rules"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bucket": bucket,
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
        if error_document is not None:
            self._values["error_document"] = error_document
        if expected_bucket_owner is not None:
            self._values["expected_bucket_owner"] = expected_bucket_owner
        if id is not None:
            self._values["id"] = id
        if index_document is not None:
            self._values["index_document"] = index_document
        if redirect_all_requests_to is not None:
            self._values["redirect_all_requests_to"] = redirect_all_requests_to
        if routing_rule is not None:
            self._values["routing_rule"] = routing_rule
        if routing_rules is not None:
            self._values["routing_rules"] = routing_rules

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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_website_configuration#bucket S3BucketWebsiteConfiguration#bucket}.'''
        result = self._values.get("bucket")
        assert result is not None, "Required property 'bucket' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def error_document(
        self,
    ) -> typing.Optional["S3BucketWebsiteConfigurationErrorDocument"]:
        '''error_document block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_website_configuration#error_document S3BucketWebsiteConfiguration#error_document}
        '''
        result = self._values.get("error_document")
        return typing.cast(typing.Optional["S3BucketWebsiteConfigurationErrorDocument"], result)

    @builtins.property
    def expected_bucket_owner(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_website_configuration#expected_bucket_owner S3BucketWebsiteConfiguration#expected_bucket_owner}.'''
        result = self._values.get("expected_bucket_owner")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_website_configuration#id S3BucketWebsiteConfiguration#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def index_document(
        self,
    ) -> typing.Optional["S3BucketWebsiteConfigurationIndexDocument"]:
        '''index_document block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_website_configuration#index_document S3BucketWebsiteConfiguration#index_document}
        '''
        result = self._values.get("index_document")
        return typing.cast(typing.Optional["S3BucketWebsiteConfigurationIndexDocument"], result)

    @builtins.property
    def redirect_all_requests_to(
        self,
    ) -> typing.Optional["S3BucketWebsiteConfigurationRedirectAllRequestsTo"]:
        '''redirect_all_requests_to block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_website_configuration#redirect_all_requests_to S3BucketWebsiteConfiguration#redirect_all_requests_to}
        '''
        result = self._values.get("redirect_all_requests_to")
        return typing.cast(typing.Optional["S3BucketWebsiteConfigurationRedirectAllRequestsTo"], result)

    @builtins.property
    def routing_rule(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["S3BucketWebsiteConfigurationRoutingRule"]]]:
        '''routing_rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_website_configuration#routing_rule S3BucketWebsiteConfiguration#routing_rule}
        '''
        result = self._values.get("routing_rule")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["S3BucketWebsiteConfigurationRoutingRule"]]], result)

    @builtins.property
    def routing_rules(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_website_configuration#routing_rules S3BucketWebsiteConfiguration#routing_rules}.'''
        result = self._values.get("routing_rules")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketWebsiteConfigurationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.s3BucketWebsiteConfiguration.S3BucketWebsiteConfigurationErrorDocument",
    jsii_struct_bases=[],
    name_mapping={"key": "key"},
)
class S3BucketWebsiteConfigurationErrorDocument:
    def __init__(self, *, key: builtins.str) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_website_configuration#key S3BucketWebsiteConfiguration#key}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c81a7b1145fa5b6a63a48a669a8945d9548a5495d0d7d77b2fc13c2a10de62f5)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_website_configuration#key S3BucketWebsiteConfiguration#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketWebsiteConfigurationErrorDocument(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3BucketWebsiteConfigurationErrorDocumentOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3BucketWebsiteConfiguration.S3BucketWebsiteConfigurationErrorDocumentOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0eaa9fcfe998ee3b31a319d332c94beb69fe3afb96bc35c4a7204219750a90bb)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__753c6ff3e56dc44cd5c7880a6409b6a31fc3948fc1fef0f9649519315cdd68d6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3BucketWebsiteConfigurationErrorDocument]:
        return typing.cast(typing.Optional[S3BucketWebsiteConfigurationErrorDocument], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3BucketWebsiteConfigurationErrorDocument],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c4b60072b15c8c32dfb5cd389aa3eb1c96b615067faaa8e9b3af2841cb8c6fc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.s3BucketWebsiteConfiguration.S3BucketWebsiteConfigurationIndexDocument",
    jsii_struct_bases=[],
    name_mapping={"suffix": "suffix"},
)
class S3BucketWebsiteConfigurationIndexDocument:
    def __init__(self, *, suffix: builtins.str) -> None:
        '''
        :param suffix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_website_configuration#suffix S3BucketWebsiteConfiguration#suffix}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8899c29bb12381b327b226ae248e463e713cdde7a611ac85b306bace1d5fe298)
            check_type(argname="argument suffix", value=suffix, expected_type=type_hints["suffix"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "suffix": suffix,
        }

    @builtins.property
    def suffix(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_website_configuration#suffix S3BucketWebsiteConfiguration#suffix}.'''
        result = self._values.get("suffix")
        assert result is not None, "Required property 'suffix' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketWebsiteConfigurationIndexDocument(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3BucketWebsiteConfigurationIndexDocumentOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3BucketWebsiteConfiguration.S3BucketWebsiteConfigurationIndexDocumentOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__de56fbcd730c63c4056f09af5ca9a0bc56d8bd1ac3467021634325120a8c3a7a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="suffixInput")
    def suffix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "suffixInput"))

    @builtins.property
    @jsii.member(jsii_name="suffix")
    def suffix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "suffix"))

    @suffix.setter
    def suffix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e2a61c2b8377d6a7121ea149a4ec6e46e773ab7cd4ed4ba5416017e7261e7ea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "suffix", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3BucketWebsiteConfigurationIndexDocument]:
        return typing.cast(typing.Optional[S3BucketWebsiteConfigurationIndexDocument], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3BucketWebsiteConfigurationIndexDocument],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be1d97bdc86156dcca2fb32ba7a8f21412fba58d4f068eeb4bd4bb922cd45c4a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.s3BucketWebsiteConfiguration.S3BucketWebsiteConfigurationRedirectAllRequestsTo",
    jsii_struct_bases=[],
    name_mapping={"host_name": "hostName", "protocol": "protocol"},
)
class S3BucketWebsiteConfigurationRedirectAllRequestsTo:
    def __init__(
        self,
        *,
        host_name: builtins.str,
        protocol: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param host_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_website_configuration#host_name S3BucketWebsiteConfiguration#host_name}.
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_website_configuration#protocol S3BucketWebsiteConfiguration#protocol}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23da42d36f3a973b48e23f135e3cb0ddeb979b85ab90bb218eda2e286b0c61ae)
            check_type(argname="argument host_name", value=host_name, expected_type=type_hints["host_name"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "host_name": host_name,
        }
        if protocol is not None:
            self._values["protocol"] = protocol

    @builtins.property
    def host_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_website_configuration#host_name S3BucketWebsiteConfiguration#host_name}.'''
        result = self._values.get("host_name")
        assert result is not None, "Required property 'host_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def protocol(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_website_configuration#protocol S3BucketWebsiteConfiguration#protocol}.'''
        result = self._values.get("protocol")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketWebsiteConfigurationRedirectAllRequestsTo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3BucketWebsiteConfigurationRedirectAllRequestsToOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3BucketWebsiteConfiguration.S3BucketWebsiteConfigurationRedirectAllRequestsToOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__65b4cd0ece39c3dc07d4fae584b50be9ede40c2afec4b1c70b54228110ae2933)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetProtocol")
    def reset_protocol(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProtocol", []))

    @builtins.property
    @jsii.member(jsii_name="hostNameInput")
    def host_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostNameInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolInput")
    def protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocolInput"))

    @builtins.property
    @jsii.member(jsii_name="hostName")
    def host_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostName"))

    @host_name.setter
    def host_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__436103fcf5540eb95af1655709b74bddd7abbc5905c2aac601136cc04fb0e74f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostName", value)

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae8af6670925aa847b7fdc94435e99e02045037330045aac666e2a6920c53c73)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3BucketWebsiteConfigurationRedirectAllRequestsTo]:
        return typing.cast(typing.Optional[S3BucketWebsiteConfigurationRedirectAllRequestsTo], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3BucketWebsiteConfigurationRedirectAllRequestsTo],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f85eb97bc9f08907928f4ae5f61d6d3c055991bb7a206c924d63ca31f0cdafb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.s3BucketWebsiteConfiguration.S3BucketWebsiteConfigurationRoutingRule",
    jsii_struct_bases=[],
    name_mapping={"redirect": "redirect", "condition": "condition"},
)
class S3BucketWebsiteConfigurationRoutingRule:
    def __init__(
        self,
        *,
        redirect: typing.Union["S3BucketWebsiteConfigurationRoutingRuleRedirect", typing.Dict[builtins.str, typing.Any]],
        condition: typing.Optional[typing.Union["S3BucketWebsiteConfigurationRoutingRuleCondition", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param redirect: redirect block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_website_configuration#redirect S3BucketWebsiteConfiguration#redirect}
        :param condition: condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_website_configuration#condition S3BucketWebsiteConfiguration#condition}
        '''
        if isinstance(redirect, dict):
            redirect = S3BucketWebsiteConfigurationRoutingRuleRedirect(**redirect)
        if isinstance(condition, dict):
            condition = S3BucketWebsiteConfigurationRoutingRuleCondition(**condition)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5abbf01f6095c665382ca81ea49b3cc3f8357a6e24797c7ce1ef0599831e4ad1)
            check_type(argname="argument redirect", value=redirect, expected_type=type_hints["redirect"])
            check_type(argname="argument condition", value=condition, expected_type=type_hints["condition"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "redirect": redirect,
        }
        if condition is not None:
            self._values["condition"] = condition

    @builtins.property
    def redirect(self) -> "S3BucketWebsiteConfigurationRoutingRuleRedirect":
        '''redirect block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_website_configuration#redirect S3BucketWebsiteConfiguration#redirect}
        '''
        result = self._values.get("redirect")
        assert result is not None, "Required property 'redirect' is missing"
        return typing.cast("S3BucketWebsiteConfigurationRoutingRuleRedirect", result)

    @builtins.property
    def condition(
        self,
    ) -> typing.Optional["S3BucketWebsiteConfigurationRoutingRuleCondition"]:
        '''condition block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_website_configuration#condition S3BucketWebsiteConfiguration#condition}
        '''
        result = self._values.get("condition")
        return typing.cast(typing.Optional["S3BucketWebsiteConfigurationRoutingRuleCondition"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketWebsiteConfigurationRoutingRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.s3BucketWebsiteConfiguration.S3BucketWebsiteConfigurationRoutingRuleCondition",
    jsii_struct_bases=[],
    name_mapping={
        "http_error_code_returned_equals": "httpErrorCodeReturnedEquals",
        "key_prefix_equals": "keyPrefixEquals",
    },
)
class S3BucketWebsiteConfigurationRoutingRuleCondition:
    def __init__(
        self,
        *,
        http_error_code_returned_equals: typing.Optional[builtins.str] = None,
        key_prefix_equals: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param http_error_code_returned_equals: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_website_configuration#http_error_code_returned_equals S3BucketWebsiteConfiguration#http_error_code_returned_equals}.
        :param key_prefix_equals: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_website_configuration#key_prefix_equals S3BucketWebsiteConfiguration#key_prefix_equals}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d2b20bf9ca1aa247ff3e8457ba3fdb0bc432d9413680efcde2fd3287031ccc6)
            check_type(argname="argument http_error_code_returned_equals", value=http_error_code_returned_equals, expected_type=type_hints["http_error_code_returned_equals"])
            check_type(argname="argument key_prefix_equals", value=key_prefix_equals, expected_type=type_hints["key_prefix_equals"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if http_error_code_returned_equals is not None:
            self._values["http_error_code_returned_equals"] = http_error_code_returned_equals
        if key_prefix_equals is not None:
            self._values["key_prefix_equals"] = key_prefix_equals

    @builtins.property
    def http_error_code_returned_equals(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_website_configuration#http_error_code_returned_equals S3BucketWebsiteConfiguration#http_error_code_returned_equals}.'''
        result = self._values.get("http_error_code_returned_equals")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key_prefix_equals(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_website_configuration#key_prefix_equals S3BucketWebsiteConfiguration#key_prefix_equals}.'''
        result = self._values.get("key_prefix_equals")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketWebsiteConfigurationRoutingRuleCondition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3BucketWebsiteConfigurationRoutingRuleConditionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3BucketWebsiteConfiguration.S3BucketWebsiteConfigurationRoutingRuleConditionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2c33d711838e373827fa8c6f8c9b40dc551d43b7b81884d622c030ca7c80e5f8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetHttpErrorCodeReturnedEquals")
    def reset_http_error_code_returned_equals(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpErrorCodeReturnedEquals", []))

    @jsii.member(jsii_name="resetKeyPrefixEquals")
    def reset_key_prefix_equals(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyPrefixEquals", []))

    @builtins.property
    @jsii.member(jsii_name="httpErrorCodeReturnedEqualsInput")
    def http_error_code_returned_equals_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "httpErrorCodeReturnedEqualsInput"))

    @builtins.property
    @jsii.member(jsii_name="keyPrefixEqualsInput")
    def key_prefix_equals_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyPrefixEqualsInput"))

    @builtins.property
    @jsii.member(jsii_name="httpErrorCodeReturnedEquals")
    def http_error_code_returned_equals(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "httpErrorCodeReturnedEquals"))

    @http_error_code_returned_equals.setter
    def http_error_code_returned_equals(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f38f441f3b6c7965bd20437462c7684ccd694c4a050bcbd68179360b9893c1b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpErrorCodeReturnedEquals", value)

    @builtins.property
    @jsii.member(jsii_name="keyPrefixEquals")
    def key_prefix_equals(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyPrefixEquals"))

    @key_prefix_equals.setter
    def key_prefix_equals(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb74dd87cc4b0276b257372bd6e3f16c175d5d9cf78232e967dcf1aea5b45bed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyPrefixEquals", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3BucketWebsiteConfigurationRoutingRuleCondition]:
        return typing.cast(typing.Optional[S3BucketWebsiteConfigurationRoutingRuleCondition], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3BucketWebsiteConfigurationRoutingRuleCondition],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97da822e1f535bd08630435d1a95091ecb44e6a583e9113333cff78d510b59cd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class S3BucketWebsiteConfigurationRoutingRuleList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3BucketWebsiteConfiguration.S3BucketWebsiteConfigurationRoutingRuleList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5c3c246be4662a87252f0e39a46ab0e82b30d9735080a07cced07a72f0dc361b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "S3BucketWebsiteConfigurationRoutingRuleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01a7c05d113fcbcc816e57c4595a00b48c68983a6b13c004046ed37491eb2986)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("S3BucketWebsiteConfigurationRoutingRuleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__253775abbcb4eb8c597f29c41a059e64043ae86267495b63dc1594707e0c92dc)
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
            type_hints = typing.get_type_hints(_typecheckingstub__be5f7e89d6644360fc5469d4d8527f3dcb62448e3484088de92b87fb6ea0987a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ba9cf2fbfac4775949b0c6d2ba8713654474dba4d6b68e65dba9f023b6a4a7bf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[S3BucketWebsiteConfigurationRoutingRule]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[S3BucketWebsiteConfigurationRoutingRule]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[S3BucketWebsiteConfigurationRoutingRule]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a6059c0dcd2cdde1fb873c49f1f1bb8a37ac79b3f9786ba32fa32e632084cd8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class S3BucketWebsiteConfigurationRoutingRuleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3BucketWebsiteConfiguration.S3BucketWebsiteConfigurationRoutingRuleOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__867e80e4007c7f6504501c41e3d6cb56edb8d583644c975201a81cde93bd3cf0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putCondition")
    def put_condition(
        self,
        *,
        http_error_code_returned_equals: typing.Optional[builtins.str] = None,
        key_prefix_equals: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param http_error_code_returned_equals: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_website_configuration#http_error_code_returned_equals S3BucketWebsiteConfiguration#http_error_code_returned_equals}.
        :param key_prefix_equals: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_website_configuration#key_prefix_equals S3BucketWebsiteConfiguration#key_prefix_equals}.
        '''
        value = S3BucketWebsiteConfigurationRoutingRuleCondition(
            http_error_code_returned_equals=http_error_code_returned_equals,
            key_prefix_equals=key_prefix_equals,
        )

        return typing.cast(None, jsii.invoke(self, "putCondition", [value]))

    @jsii.member(jsii_name="putRedirect")
    def put_redirect(
        self,
        *,
        host_name: typing.Optional[builtins.str] = None,
        http_redirect_code: typing.Optional[builtins.str] = None,
        protocol: typing.Optional[builtins.str] = None,
        replace_key_prefix_with: typing.Optional[builtins.str] = None,
        replace_key_with: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param host_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_website_configuration#host_name S3BucketWebsiteConfiguration#host_name}.
        :param http_redirect_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_website_configuration#http_redirect_code S3BucketWebsiteConfiguration#http_redirect_code}.
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_website_configuration#protocol S3BucketWebsiteConfiguration#protocol}.
        :param replace_key_prefix_with: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_website_configuration#replace_key_prefix_with S3BucketWebsiteConfiguration#replace_key_prefix_with}.
        :param replace_key_with: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_website_configuration#replace_key_with S3BucketWebsiteConfiguration#replace_key_with}.
        '''
        value = S3BucketWebsiteConfigurationRoutingRuleRedirect(
            host_name=host_name,
            http_redirect_code=http_redirect_code,
            protocol=protocol,
            replace_key_prefix_with=replace_key_prefix_with,
            replace_key_with=replace_key_with,
        )

        return typing.cast(None, jsii.invoke(self, "putRedirect", [value]))

    @jsii.member(jsii_name="resetCondition")
    def reset_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCondition", []))

    @builtins.property
    @jsii.member(jsii_name="condition")
    def condition(
        self,
    ) -> S3BucketWebsiteConfigurationRoutingRuleConditionOutputReference:
        return typing.cast(S3BucketWebsiteConfigurationRoutingRuleConditionOutputReference, jsii.get(self, "condition"))

    @builtins.property
    @jsii.member(jsii_name="redirect")
    def redirect(
        self,
    ) -> "S3BucketWebsiteConfigurationRoutingRuleRedirectOutputReference":
        return typing.cast("S3BucketWebsiteConfigurationRoutingRuleRedirectOutputReference", jsii.get(self, "redirect"))

    @builtins.property
    @jsii.member(jsii_name="conditionInput")
    def condition_input(
        self,
    ) -> typing.Optional[S3BucketWebsiteConfigurationRoutingRuleCondition]:
        return typing.cast(typing.Optional[S3BucketWebsiteConfigurationRoutingRuleCondition], jsii.get(self, "conditionInput"))

    @builtins.property
    @jsii.member(jsii_name="redirectInput")
    def redirect_input(
        self,
    ) -> typing.Optional["S3BucketWebsiteConfigurationRoutingRuleRedirect"]:
        return typing.cast(typing.Optional["S3BucketWebsiteConfigurationRoutingRuleRedirect"], jsii.get(self, "redirectInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[S3BucketWebsiteConfigurationRoutingRule, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[S3BucketWebsiteConfigurationRoutingRule, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[S3BucketWebsiteConfigurationRoutingRule, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a42081e51920558aad2de7e49cdd2af49ab1d169e58e9ba966844914881e5a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.s3BucketWebsiteConfiguration.S3BucketWebsiteConfigurationRoutingRuleRedirect",
    jsii_struct_bases=[],
    name_mapping={
        "host_name": "hostName",
        "http_redirect_code": "httpRedirectCode",
        "protocol": "protocol",
        "replace_key_prefix_with": "replaceKeyPrefixWith",
        "replace_key_with": "replaceKeyWith",
    },
)
class S3BucketWebsiteConfigurationRoutingRuleRedirect:
    def __init__(
        self,
        *,
        host_name: typing.Optional[builtins.str] = None,
        http_redirect_code: typing.Optional[builtins.str] = None,
        protocol: typing.Optional[builtins.str] = None,
        replace_key_prefix_with: typing.Optional[builtins.str] = None,
        replace_key_with: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param host_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_website_configuration#host_name S3BucketWebsiteConfiguration#host_name}.
        :param http_redirect_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_website_configuration#http_redirect_code S3BucketWebsiteConfiguration#http_redirect_code}.
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_website_configuration#protocol S3BucketWebsiteConfiguration#protocol}.
        :param replace_key_prefix_with: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_website_configuration#replace_key_prefix_with S3BucketWebsiteConfiguration#replace_key_prefix_with}.
        :param replace_key_with: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_website_configuration#replace_key_with S3BucketWebsiteConfiguration#replace_key_with}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc1cb9c9811adf77d554f110c60b1bcb7e8cc2b231ba573bbd4748236c1bd555)
            check_type(argname="argument host_name", value=host_name, expected_type=type_hints["host_name"])
            check_type(argname="argument http_redirect_code", value=http_redirect_code, expected_type=type_hints["http_redirect_code"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument replace_key_prefix_with", value=replace_key_prefix_with, expected_type=type_hints["replace_key_prefix_with"])
            check_type(argname="argument replace_key_with", value=replace_key_with, expected_type=type_hints["replace_key_with"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if host_name is not None:
            self._values["host_name"] = host_name
        if http_redirect_code is not None:
            self._values["http_redirect_code"] = http_redirect_code
        if protocol is not None:
            self._values["protocol"] = protocol
        if replace_key_prefix_with is not None:
            self._values["replace_key_prefix_with"] = replace_key_prefix_with
        if replace_key_with is not None:
            self._values["replace_key_with"] = replace_key_with

    @builtins.property
    def host_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_website_configuration#host_name S3BucketWebsiteConfiguration#host_name}.'''
        result = self._values.get("host_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def http_redirect_code(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_website_configuration#http_redirect_code S3BucketWebsiteConfiguration#http_redirect_code}.'''
        result = self._values.get("http_redirect_code")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def protocol(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_website_configuration#protocol S3BucketWebsiteConfiguration#protocol}.'''
        result = self._values.get("protocol")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def replace_key_prefix_with(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_website_configuration#replace_key_prefix_with S3BucketWebsiteConfiguration#replace_key_prefix_with}.'''
        result = self._values.get("replace_key_prefix_with")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def replace_key_with(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_website_configuration#replace_key_with S3BucketWebsiteConfiguration#replace_key_with}.'''
        result = self._values.get("replace_key_with")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketWebsiteConfigurationRoutingRuleRedirect(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3BucketWebsiteConfigurationRoutingRuleRedirectOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3BucketWebsiteConfiguration.S3BucketWebsiteConfigurationRoutingRuleRedirectOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__98dd91e59aa71a03144de08f50388c5c31cd4b9b450153d6817e92c144b0685a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetHostName")
    def reset_host_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostName", []))

    @jsii.member(jsii_name="resetHttpRedirectCode")
    def reset_http_redirect_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpRedirectCode", []))

    @jsii.member(jsii_name="resetProtocol")
    def reset_protocol(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProtocol", []))

    @jsii.member(jsii_name="resetReplaceKeyPrefixWith")
    def reset_replace_key_prefix_with(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReplaceKeyPrefixWith", []))

    @jsii.member(jsii_name="resetReplaceKeyWith")
    def reset_replace_key_with(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReplaceKeyWith", []))

    @builtins.property
    @jsii.member(jsii_name="hostNameInput")
    def host_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostNameInput"))

    @builtins.property
    @jsii.member(jsii_name="httpRedirectCodeInput")
    def http_redirect_code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "httpRedirectCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolInput")
    def protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocolInput"))

    @builtins.property
    @jsii.member(jsii_name="replaceKeyPrefixWithInput")
    def replace_key_prefix_with_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "replaceKeyPrefixWithInput"))

    @builtins.property
    @jsii.member(jsii_name="replaceKeyWithInput")
    def replace_key_with_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "replaceKeyWithInput"))

    @builtins.property
    @jsii.member(jsii_name="hostName")
    def host_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostName"))

    @host_name.setter
    def host_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e18eed4daae31d3e003153b934fdbce0cfe9256e242329f52964a1321a00f04)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostName", value)

    @builtins.property
    @jsii.member(jsii_name="httpRedirectCode")
    def http_redirect_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "httpRedirectCode"))

    @http_redirect_code.setter
    def http_redirect_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8bd8723a7e2400b84dcc0ec6442c4e78d218d218680ccaaf63e933a1681deed9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpRedirectCode", value)

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac111fe51fedc00be1fe0c13caa50ac24b24a11e66c6b372a9b913dcadd7ea06)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="replaceKeyPrefixWith")
    def replace_key_prefix_with(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "replaceKeyPrefixWith"))

    @replace_key_prefix_with.setter
    def replace_key_prefix_with(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b108e2a1a7ff1271f091fe72895941649653afeb645ca6009d2cd95a74bd1a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replaceKeyPrefixWith", value)

    @builtins.property
    @jsii.member(jsii_name="replaceKeyWith")
    def replace_key_with(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "replaceKeyWith"))

    @replace_key_with.setter
    def replace_key_with(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a539af46b9dd53a490031dce8d476f622c8ccd9fdf2ab4337f7aaaab410cea42)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replaceKeyWith", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3BucketWebsiteConfigurationRoutingRuleRedirect]:
        return typing.cast(typing.Optional[S3BucketWebsiteConfigurationRoutingRuleRedirect], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3BucketWebsiteConfigurationRoutingRuleRedirect],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d031a6e8fc5c93e9646cd079c3b280ae57e75a2fc7001058fcb1a5a5fc44288)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "S3BucketWebsiteConfiguration",
    "S3BucketWebsiteConfigurationConfig",
    "S3BucketWebsiteConfigurationErrorDocument",
    "S3BucketWebsiteConfigurationErrorDocumentOutputReference",
    "S3BucketWebsiteConfigurationIndexDocument",
    "S3BucketWebsiteConfigurationIndexDocumentOutputReference",
    "S3BucketWebsiteConfigurationRedirectAllRequestsTo",
    "S3BucketWebsiteConfigurationRedirectAllRequestsToOutputReference",
    "S3BucketWebsiteConfigurationRoutingRule",
    "S3BucketWebsiteConfigurationRoutingRuleCondition",
    "S3BucketWebsiteConfigurationRoutingRuleConditionOutputReference",
    "S3BucketWebsiteConfigurationRoutingRuleList",
    "S3BucketWebsiteConfigurationRoutingRuleOutputReference",
    "S3BucketWebsiteConfigurationRoutingRuleRedirect",
    "S3BucketWebsiteConfigurationRoutingRuleRedirectOutputReference",
]

publication.publish()

def _typecheckingstub__5f125c8c5ceb6ac5fb10447b6ef2c452d2f7bcb0714e5aef3edaef14fcb5462e(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    bucket: builtins.str,
    error_document: typing.Optional[typing.Union[S3BucketWebsiteConfigurationErrorDocument, typing.Dict[builtins.str, typing.Any]]] = None,
    expected_bucket_owner: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    index_document: typing.Optional[typing.Union[S3BucketWebsiteConfigurationIndexDocument, typing.Dict[builtins.str, typing.Any]]] = None,
    redirect_all_requests_to: typing.Optional[typing.Union[S3BucketWebsiteConfigurationRedirectAllRequestsTo, typing.Dict[builtins.str, typing.Any]]] = None,
    routing_rule: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[S3BucketWebsiteConfigurationRoutingRule, typing.Dict[builtins.str, typing.Any]]]]] = None,
    routing_rules: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__0a94d408966f92f2a3e36a707050c58675ce1e8c7842da94eb5c75d3b9aff047(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[S3BucketWebsiteConfigurationRoutingRule, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d519b0ab2e7bb5129c9ccae53ab84cd4c5d2418183d5d1b82b7caefba5322be9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__363ef195560b57a60723933d0db42aa062d3a15b0d55ce7cc40f4c4ff9a9532f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71c13e0383d5dbeaed2cdf3671a681a0d1d1e70ab1de93a923995312c2aaf1a8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1d17f5525a526cd48fc6f7b724811c16fb47d88b20c6c3956094e3ad82449ef(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0e436e27cd4193084edafee6474635fab0d90a34d77042e325847daf329c43d(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    bucket: builtins.str,
    error_document: typing.Optional[typing.Union[S3BucketWebsiteConfigurationErrorDocument, typing.Dict[builtins.str, typing.Any]]] = None,
    expected_bucket_owner: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    index_document: typing.Optional[typing.Union[S3BucketWebsiteConfigurationIndexDocument, typing.Dict[builtins.str, typing.Any]]] = None,
    redirect_all_requests_to: typing.Optional[typing.Union[S3BucketWebsiteConfigurationRedirectAllRequestsTo, typing.Dict[builtins.str, typing.Any]]] = None,
    routing_rule: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[S3BucketWebsiteConfigurationRoutingRule, typing.Dict[builtins.str, typing.Any]]]]] = None,
    routing_rules: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c81a7b1145fa5b6a63a48a669a8945d9548a5495d0d7d77b2fc13c2a10de62f5(
    *,
    key: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0eaa9fcfe998ee3b31a319d332c94beb69fe3afb96bc35c4a7204219750a90bb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__753c6ff3e56dc44cd5c7880a6409b6a31fc3948fc1fef0f9649519315cdd68d6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c4b60072b15c8c32dfb5cd389aa3eb1c96b615067faaa8e9b3af2841cb8c6fc(
    value: typing.Optional[S3BucketWebsiteConfigurationErrorDocument],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8899c29bb12381b327b226ae248e463e713cdde7a611ac85b306bace1d5fe298(
    *,
    suffix: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de56fbcd730c63c4056f09af5ca9a0bc56d8bd1ac3467021634325120a8c3a7a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e2a61c2b8377d6a7121ea149a4ec6e46e773ab7cd4ed4ba5416017e7261e7ea(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be1d97bdc86156dcca2fb32ba7a8f21412fba58d4f068eeb4bd4bb922cd45c4a(
    value: typing.Optional[S3BucketWebsiteConfigurationIndexDocument],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23da42d36f3a973b48e23f135e3cb0ddeb979b85ab90bb218eda2e286b0c61ae(
    *,
    host_name: builtins.str,
    protocol: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65b4cd0ece39c3dc07d4fae584b50be9ede40c2afec4b1c70b54228110ae2933(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__436103fcf5540eb95af1655709b74bddd7abbc5905c2aac601136cc04fb0e74f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae8af6670925aa847b7fdc94435e99e02045037330045aac666e2a6920c53c73(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f85eb97bc9f08907928f4ae5f61d6d3c055991bb7a206c924d63ca31f0cdafb(
    value: typing.Optional[S3BucketWebsiteConfigurationRedirectAllRequestsTo],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5abbf01f6095c665382ca81ea49b3cc3f8357a6e24797c7ce1ef0599831e4ad1(
    *,
    redirect: typing.Union[S3BucketWebsiteConfigurationRoutingRuleRedirect, typing.Dict[builtins.str, typing.Any]],
    condition: typing.Optional[typing.Union[S3BucketWebsiteConfigurationRoutingRuleCondition, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d2b20bf9ca1aa247ff3e8457ba3fdb0bc432d9413680efcde2fd3287031ccc6(
    *,
    http_error_code_returned_equals: typing.Optional[builtins.str] = None,
    key_prefix_equals: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c33d711838e373827fa8c6f8c9b40dc551d43b7b81884d622c030ca7c80e5f8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f38f441f3b6c7965bd20437462c7684ccd694c4a050bcbd68179360b9893c1b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb74dd87cc4b0276b257372bd6e3f16c175d5d9cf78232e967dcf1aea5b45bed(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97da822e1f535bd08630435d1a95091ecb44e6a583e9113333cff78d510b59cd(
    value: typing.Optional[S3BucketWebsiteConfigurationRoutingRuleCondition],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c3c246be4662a87252f0e39a46ab0e82b30d9735080a07cced07a72f0dc361b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01a7c05d113fcbcc816e57c4595a00b48c68983a6b13c004046ed37491eb2986(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__253775abbcb4eb8c597f29c41a059e64043ae86267495b63dc1594707e0c92dc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be5f7e89d6644360fc5469d4d8527f3dcb62448e3484088de92b87fb6ea0987a(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba9cf2fbfac4775949b0c6d2ba8713654474dba4d6b68e65dba9f023b6a4a7bf(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a6059c0dcd2cdde1fb873c49f1f1bb8a37ac79b3f9786ba32fa32e632084cd8(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[S3BucketWebsiteConfigurationRoutingRule]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__867e80e4007c7f6504501c41e3d6cb56edb8d583644c975201a81cde93bd3cf0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a42081e51920558aad2de7e49cdd2af49ab1d169e58e9ba966844914881e5a2(
    value: typing.Optional[typing.Union[S3BucketWebsiteConfigurationRoutingRule, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc1cb9c9811adf77d554f110c60b1bcb7e8cc2b231ba573bbd4748236c1bd555(
    *,
    host_name: typing.Optional[builtins.str] = None,
    http_redirect_code: typing.Optional[builtins.str] = None,
    protocol: typing.Optional[builtins.str] = None,
    replace_key_prefix_with: typing.Optional[builtins.str] = None,
    replace_key_with: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98dd91e59aa71a03144de08f50388c5c31cd4b9b450153d6817e92c144b0685a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e18eed4daae31d3e003153b934fdbce0cfe9256e242329f52964a1321a00f04(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8bd8723a7e2400b84dcc0ec6442c4e78d218d218680ccaaf63e933a1681deed9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac111fe51fedc00be1fe0c13caa50ac24b24a11e66c6b372a9b913dcadd7ea06(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b108e2a1a7ff1271f091fe72895941649653afeb645ca6009d2cd95a74bd1a2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a539af46b9dd53a490031dce8d476f622c8ccd9fdf2ab4337f7aaaab410cea42(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d031a6e8fc5c93e9646cd079c3b280ae57e75a2fc7001058fcb1a5a5fc44288(
    value: typing.Optional[S3BucketWebsiteConfigurationRoutingRuleRedirect],
) -> None:
    """Type checking stubs"""
    pass
