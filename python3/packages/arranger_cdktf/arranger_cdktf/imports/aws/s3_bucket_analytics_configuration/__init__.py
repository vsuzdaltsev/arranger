'''
# `aws_s3_bucket_analytics_configuration`

Refer to the Terraform Registory for docs: [`aws_s3_bucket_analytics_configuration`](https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration).
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


class S3BucketAnalyticsConfiguration(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3BucketAnalyticsConfiguration.S3BucketAnalyticsConfiguration",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration aws_s3_bucket_analytics_configuration}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        bucket: builtins.str,
        name: builtins.str,
        filter: typing.Optional[typing.Union["S3BucketAnalyticsConfigurationFilter", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        storage_class_analysis: typing.Optional[typing.Union["S3BucketAnalyticsConfigurationStorageClassAnalysis", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration aws_s3_bucket_analytics_configuration} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#bucket S3BucketAnalyticsConfiguration#bucket}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#name S3BucketAnalyticsConfiguration#name}.
        :param filter: filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#filter S3BucketAnalyticsConfiguration#filter}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#id S3BucketAnalyticsConfiguration#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param storage_class_analysis: storage_class_analysis block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#storage_class_analysis S3BucketAnalyticsConfiguration#storage_class_analysis}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58b0dd7cc1b63968229e2ada117c9ba8d3393185c708bbf14b757f35457f5235)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = S3BucketAnalyticsConfigurationConfig(
            bucket=bucket,
            name=name,
            filter=filter,
            id=id,
            storage_class_analysis=storage_class_analysis,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putFilter")
    def put_filter(
        self,
        *,
        prefix: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#prefix S3BucketAnalyticsConfiguration#prefix}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#tags S3BucketAnalyticsConfiguration#tags}.
        '''
        value = S3BucketAnalyticsConfigurationFilter(prefix=prefix, tags=tags)

        return typing.cast(None, jsii.invoke(self, "putFilter", [value]))

    @jsii.member(jsii_name="putStorageClassAnalysis")
    def put_storage_class_analysis(
        self,
        *,
        data_export: typing.Union["S3BucketAnalyticsConfigurationStorageClassAnalysisDataExport", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param data_export: data_export block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#data_export S3BucketAnalyticsConfiguration#data_export}
        '''
        value = S3BucketAnalyticsConfigurationStorageClassAnalysis(
            data_export=data_export
        )

        return typing.cast(None, jsii.invoke(self, "putStorageClassAnalysis", [value]))

    @jsii.member(jsii_name="resetFilter")
    def reset_filter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFilter", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetStorageClassAnalysis")
    def reset_storage_class_analysis(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageClassAnalysis", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="filter")
    def filter(self) -> "S3BucketAnalyticsConfigurationFilterOutputReference":
        return typing.cast("S3BucketAnalyticsConfigurationFilterOutputReference", jsii.get(self, "filter"))

    @builtins.property
    @jsii.member(jsii_name="storageClassAnalysis")
    def storage_class_analysis(
        self,
    ) -> "S3BucketAnalyticsConfigurationStorageClassAnalysisOutputReference":
        return typing.cast("S3BucketAnalyticsConfigurationStorageClassAnalysisOutputReference", jsii.get(self, "storageClassAnalysis"))

    @builtins.property
    @jsii.member(jsii_name="bucketInput")
    def bucket_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketInput"))

    @builtins.property
    @jsii.member(jsii_name="filterInput")
    def filter_input(self) -> typing.Optional["S3BucketAnalyticsConfigurationFilter"]:
        return typing.cast(typing.Optional["S3BucketAnalyticsConfigurationFilter"], jsii.get(self, "filterInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="storageClassAnalysisInput")
    def storage_class_analysis_input(
        self,
    ) -> typing.Optional["S3BucketAnalyticsConfigurationStorageClassAnalysis"]:
        return typing.cast(typing.Optional["S3BucketAnalyticsConfigurationStorageClassAnalysis"], jsii.get(self, "storageClassAnalysisInput"))

    @builtins.property
    @jsii.member(jsii_name="bucket")
    def bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucket"))

    @bucket.setter
    def bucket(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6502a68c4c2bb3a1f139879840125459abdf0199fcde54292cd6b2462d8c5a22)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucket", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25db507517e1051853696a65a76593c77629659465e7c0d22febc815cd7e9a1a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c35d1592944b8b26721be5c277a35ba8519562aee399a1ad00c2e9b634e3b5e1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="aws.s3BucketAnalyticsConfiguration.S3BucketAnalyticsConfigurationConfig",
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
        "name": "name",
        "filter": "filter",
        "id": "id",
        "storage_class_analysis": "storageClassAnalysis",
    },
)
class S3BucketAnalyticsConfigurationConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        name: builtins.str,
        filter: typing.Optional[typing.Union["S3BucketAnalyticsConfigurationFilter", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        storage_class_analysis: typing.Optional[typing.Union["S3BucketAnalyticsConfigurationStorageClassAnalysis", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#bucket S3BucketAnalyticsConfiguration#bucket}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#name S3BucketAnalyticsConfiguration#name}.
        :param filter: filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#filter S3BucketAnalyticsConfiguration#filter}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#id S3BucketAnalyticsConfiguration#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param storage_class_analysis: storage_class_analysis block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#storage_class_analysis S3BucketAnalyticsConfiguration#storage_class_analysis}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(filter, dict):
            filter = S3BucketAnalyticsConfigurationFilter(**filter)
        if isinstance(storage_class_analysis, dict):
            storage_class_analysis = S3BucketAnalyticsConfigurationStorageClassAnalysis(**storage_class_analysis)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fae19cc3c812737783c7471b3b171f7820e030b2b941f2a39bb7d0907354c37d)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument filter", value=filter, expected_type=type_hints["filter"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument storage_class_analysis", value=storage_class_analysis, expected_type=type_hints["storage_class_analysis"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bucket": bucket,
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
        if filter is not None:
            self._values["filter"] = filter
        if id is not None:
            self._values["id"] = id
        if storage_class_analysis is not None:
            self._values["storage_class_analysis"] = storage_class_analysis

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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#bucket S3BucketAnalyticsConfiguration#bucket}.'''
        result = self._values.get("bucket")
        assert result is not None, "Required property 'bucket' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#name S3BucketAnalyticsConfiguration#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def filter(self) -> typing.Optional["S3BucketAnalyticsConfigurationFilter"]:
        '''filter block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#filter S3BucketAnalyticsConfiguration#filter}
        '''
        result = self._values.get("filter")
        return typing.cast(typing.Optional["S3BucketAnalyticsConfigurationFilter"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#id S3BucketAnalyticsConfiguration#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def storage_class_analysis(
        self,
    ) -> typing.Optional["S3BucketAnalyticsConfigurationStorageClassAnalysis"]:
        '''storage_class_analysis block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#storage_class_analysis S3BucketAnalyticsConfiguration#storage_class_analysis}
        '''
        result = self._values.get("storage_class_analysis")
        return typing.cast(typing.Optional["S3BucketAnalyticsConfigurationStorageClassAnalysis"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketAnalyticsConfigurationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.s3BucketAnalyticsConfiguration.S3BucketAnalyticsConfigurationFilter",
    jsii_struct_bases=[],
    name_mapping={"prefix": "prefix", "tags": "tags"},
)
class S3BucketAnalyticsConfigurationFilter:
    def __init__(
        self,
        *,
        prefix: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#prefix S3BucketAnalyticsConfiguration#prefix}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#tags S3BucketAnalyticsConfiguration#tags}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87f8a9fc09bba0ddfe484c9523bcf0d6bf2a48097d53ebe9091950ed573a36e8)
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if prefix is not None:
            self._values["prefix"] = prefix
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#prefix S3BucketAnalyticsConfiguration#prefix}.'''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#tags S3BucketAnalyticsConfiguration#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketAnalyticsConfigurationFilter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3BucketAnalyticsConfigurationFilterOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3BucketAnalyticsConfiguration.S3BucketAnalyticsConfigurationFilterOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4b2f5a62f4fb981c4c6f555e0f3a5536112b0f582cce8a0f1eea93666ace7c2e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b9d3868d7853b51f424ec6623732855ed71976641cd7a68e2fd8050b3be8eceb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefix", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0daf13c47e29c42f658d35200c8457f2326dd9a90c3c5ef77d53458ff5d9ebec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[S3BucketAnalyticsConfigurationFilter]:
        return typing.cast(typing.Optional[S3BucketAnalyticsConfigurationFilter], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3BucketAnalyticsConfigurationFilter],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63042950273915b9c80d38a5780c39b42d5a49bb2ff71aced86916fe3e4a3a1f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.s3BucketAnalyticsConfiguration.S3BucketAnalyticsConfigurationStorageClassAnalysis",
    jsii_struct_bases=[],
    name_mapping={"data_export": "dataExport"},
)
class S3BucketAnalyticsConfigurationStorageClassAnalysis:
    def __init__(
        self,
        *,
        data_export: typing.Union["S3BucketAnalyticsConfigurationStorageClassAnalysisDataExport", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param data_export: data_export block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#data_export S3BucketAnalyticsConfiguration#data_export}
        '''
        if isinstance(data_export, dict):
            data_export = S3BucketAnalyticsConfigurationStorageClassAnalysisDataExport(**data_export)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db8c0ac66e4035ec640b70efdb720e4064821140c260f12332b48c4cde55c8ac)
            check_type(argname="argument data_export", value=data_export, expected_type=type_hints["data_export"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "data_export": data_export,
        }

    @builtins.property
    def data_export(
        self,
    ) -> "S3BucketAnalyticsConfigurationStorageClassAnalysisDataExport":
        '''data_export block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#data_export S3BucketAnalyticsConfiguration#data_export}
        '''
        result = self._values.get("data_export")
        assert result is not None, "Required property 'data_export' is missing"
        return typing.cast("S3BucketAnalyticsConfigurationStorageClassAnalysisDataExport", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketAnalyticsConfigurationStorageClassAnalysis(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.s3BucketAnalyticsConfiguration.S3BucketAnalyticsConfigurationStorageClassAnalysisDataExport",
    jsii_struct_bases=[],
    name_mapping={
        "destination": "destination",
        "output_schema_version": "outputSchemaVersion",
    },
)
class S3BucketAnalyticsConfigurationStorageClassAnalysisDataExport:
    def __init__(
        self,
        *,
        destination: typing.Union["S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestination", typing.Dict[builtins.str, typing.Any]],
        output_schema_version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param destination: destination block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#destination S3BucketAnalyticsConfiguration#destination}
        :param output_schema_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#output_schema_version S3BucketAnalyticsConfiguration#output_schema_version}.
        '''
        if isinstance(destination, dict):
            destination = S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestination(**destination)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ff10b49edcc5b220d46c777bddb781d8ac6ad83b184b96471c57c060fda5276)
            check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
            check_type(argname="argument output_schema_version", value=output_schema_version, expected_type=type_hints["output_schema_version"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "destination": destination,
        }
        if output_schema_version is not None:
            self._values["output_schema_version"] = output_schema_version

    @builtins.property
    def destination(
        self,
    ) -> "S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestination":
        '''destination block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#destination S3BucketAnalyticsConfiguration#destination}
        '''
        result = self._values.get("destination")
        assert result is not None, "Required property 'destination' is missing"
        return typing.cast("S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestination", result)

    @builtins.property
    def output_schema_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#output_schema_version S3BucketAnalyticsConfiguration#output_schema_version}.'''
        result = self._values.get("output_schema_version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketAnalyticsConfigurationStorageClassAnalysisDataExport(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.s3BucketAnalyticsConfiguration.S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestination",
    jsii_struct_bases=[],
    name_mapping={"s3_bucket_destination": "s3BucketDestination"},
)
class S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestination:
    def __init__(
        self,
        *,
        s3_bucket_destination: typing.Union["S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestination", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param s3_bucket_destination: s3_bucket_destination block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#s3_bucket_destination S3BucketAnalyticsConfiguration#s3_bucket_destination}
        '''
        if isinstance(s3_bucket_destination, dict):
            s3_bucket_destination = S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestination(**s3_bucket_destination)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0dfd54cadb7bfcd1cc33cddbab510b9e6a840c45388cac5b0620fc46e4b2d43)
            check_type(argname="argument s3_bucket_destination", value=s3_bucket_destination, expected_type=type_hints["s3_bucket_destination"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "s3_bucket_destination": s3_bucket_destination,
        }

    @builtins.property
    def s3_bucket_destination(
        self,
    ) -> "S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestination":
        '''s3_bucket_destination block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#s3_bucket_destination S3BucketAnalyticsConfiguration#s3_bucket_destination}
        '''
        result = self._values.get("s3_bucket_destination")
        assert result is not None, "Required property 's3_bucket_destination' is missing"
        return typing.cast("S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestination", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestination(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestinationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3BucketAnalyticsConfiguration.S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestinationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__502ea3574ecbc07b0b9293385bdb6628a64ec951ef333bd4f1aa667bf4fd47f5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putS3BucketDestination")
    def put_s3_bucket_destination(
        self,
        *,
        bucket_arn: builtins.str,
        bucket_account_id: typing.Optional[builtins.str] = None,
        format: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#bucket_arn S3BucketAnalyticsConfiguration#bucket_arn}.
        :param bucket_account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#bucket_account_id S3BucketAnalyticsConfiguration#bucket_account_id}.
        :param format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#format S3BucketAnalyticsConfiguration#format}.
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#prefix S3BucketAnalyticsConfiguration#prefix}.
        '''
        value = S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestination(
            bucket_arn=bucket_arn,
            bucket_account_id=bucket_account_id,
            format=format,
            prefix=prefix,
        )

        return typing.cast(None, jsii.invoke(self, "putS3BucketDestination", [value]))

    @builtins.property
    @jsii.member(jsii_name="s3BucketDestination")
    def s3_bucket_destination(
        self,
    ) -> "S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestinationOutputReference":
        return typing.cast("S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestinationOutputReference", jsii.get(self, "s3BucketDestination"))

    @builtins.property
    @jsii.member(jsii_name="s3BucketDestinationInput")
    def s3_bucket_destination_input(
        self,
    ) -> typing.Optional["S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestination"]:
        return typing.cast(typing.Optional["S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestination"], jsii.get(self, "s3BucketDestinationInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestination]:
        return typing.cast(typing.Optional[S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestination], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestination],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9cca424c960bf2c446ebffcd877d7343db8cdf0b20ac713ba720246a20868bf9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.s3BucketAnalyticsConfiguration.S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestination",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_arn": "bucketArn",
        "bucket_account_id": "bucketAccountId",
        "format": "format",
        "prefix": "prefix",
    },
)
class S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestination:
    def __init__(
        self,
        *,
        bucket_arn: builtins.str,
        bucket_account_id: typing.Optional[builtins.str] = None,
        format: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#bucket_arn S3BucketAnalyticsConfiguration#bucket_arn}.
        :param bucket_account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#bucket_account_id S3BucketAnalyticsConfiguration#bucket_account_id}.
        :param format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#format S3BucketAnalyticsConfiguration#format}.
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#prefix S3BucketAnalyticsConfiguration#prefix}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa809d2f2749ffb70fcf4643c80d8f5f1004dbda9e18b4d87571bbcaae81290a)
            check_type(argname="argument bucket_arn", value=bucket_arn, expected_type=type_hints["bucket_arn"])
            check_type(argname="argument bucket_account_id", value=bucket_account_id, expected_type=type_hints["bucket_account_id"])
            check_type(argname="argument format", value=format, expected_type=type_hints["format"])
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bucket_arn": bucket_arn,
        }
        if bucket_account_id is not None:
            self._values["bucket_account_id"] = bucket_account_id
        if format is not None:
            self._values["format"] = format
        if prefix is not None:
            self._values["prefix"] = prefix

    @builtins.property
    def bucket_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#bucket_arn S3BucketAnalyticsConfiguration#bucket_arn}.'''
        result = self._values.get("bucket_arn")
        assert result is not None, "Required property 'bucket_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bucket_account_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#bucket_account_id S3BucketAnalyticsConfiguration#bucket_account_id}.'''
        result = self._values.get("bucket_account_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def format(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#format S3BucketAnalyticsConfiguration#format}.'''
        result = self._values.get("format")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#prefix S3BucketAnalyticsConfiguration#prefix}.'''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestination(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestinationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3BucketAnalyticsConfiguration.S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestinationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2068c01e79a33dff2502eec459fda346186b5e8186b565c64d8a985b1ec3d446)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBucketAccountId")
    def reset_bucket_account_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketAccountId", []))

    @jsii.member(jsii_name="resetFormat")
    def reset_format(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFormat", []))

    @jsii.member(jsii_name="resetPrefix")
    def reset_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrefix", []))

    @builtins.property
    @jsii.member(jsii_name="bucketAccountIdInput")
    def bucket_account_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketAccountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketArnInput")
    def bucket_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketArnInput"))

    @builtins.property
    @jsii.member(jsii_name="formatInput")
    def format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "formatInput"))

    @builtins.property
    @jsii.member(jsii_name="prefixInput")
    def prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefixInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketAccountId")
    def bucket_account_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketAccountId"))

    @bucket_account_id.setter
    def bucket_account_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__045b655144425e2c2172efc33350f8b4c331bc6e44b9745ec43d3324535398b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketAccountId", value)

    @builtins.property
    @jsii.member(jsii_name="bucketArn")
    def bucket_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketArn"))

    @bucket_arn.setter
    def bucket_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a25263ea876b7564fca24e2efc998ca1062c9a85879fc9b381ed084041a37923)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketArn", value)

    @builtins.property
    @jsii.member(jsii_name="format")
    def format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "format"))

    @format.setter
    def format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7aa2912f0c91b191fc99805eefc599588e23b030b8e5ec3fa52e0460db5b830e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "format", value)

    @builtins.property
    @jsii.member(jsii_name="prefix")
    def prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prefix"))

    @prefix.setter
    def prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2717078ecf8eff17eb41d973189e5607c80b797bebf0ef99678c8d5e7bc7a2d7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefix", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestination]:
        return typing.cast(typing.Optional[S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestination], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestination],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__86ae6f07508ad03bfcd717f82f7970db2c729e95a350da5b9efce034aee6fa9f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3BucketAnalyticsConfiguration.S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7c6f9632af24c1d7ea70431e0d930155c6f281ebb6635d1d78d193758c457f54)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDestination")
    def put_destination(
        self,
        *,
        s3_bucket_destination: typing.Union[S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestination, typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param s3_bucket_destination: s3_bucket_destination block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#s3_bucket_destination S3BucketAnalyticsConfiguration#s3_bucket_destination}
        '''
        value = S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestination(
            s3_bucket_destination=s3_bucket_destination
        )

        return typing.cast(None, jsii.invoke(self, "putDestination", [value]))

    @jsii.member(jsii_name="resetOutputSchemaVersion")
    def reset_output_schema_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOutputSchemaVersion", []))

    @builtins.property
    @jsii.member(jsii_name="destination")
    def destination(
        self,
    ) -> S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestinationOutputReference:
        return typing.cast(S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestinationOutputReference, jsii.get(self, "destination"))

    @builtins.property
    @jsii.member(jsii_name="destinationInput")
    def destination_input(
        self,
    ) -> typing.Optional[S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestination]:
        return typing.cast(typing.Optional[S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestination], jsii.get(self, "destinationInput"))

    @builtins.property
    @jsii.member(jsii_name="outputSchemaVersionInput")
    def output_schema_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "outputSchemaVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="outputSchemaVersion")
    def output_schema_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "outputSchemaVersion"))

    @output_schema_version.setter
    def output_schema_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b096d1e9a15beeae536fb09a8ee8c608320f4eb5822993237db090f769e0b62)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "outputSchemaVersion", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3BucketAnalyticsConfigurationStorageClassAnalysisDataExport]:
        return typing.cast(typing.Optional[S3BucketAnalyticsConfigurationStorageClassAnalysisDataExport], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3BucketAnalyticsConfigurationStorageClassAnalysisDataExport],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__81a95dbeec9315d3ec2165dad2fb5eb4fc29d5b05ed79d2d39ee8909449412ef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class S3BucketAnalyticsConfigurationStorageClassAnalysisOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3BucketAnalyticsConfiguration.S3BucketAnalyticsConfigurationStorageClassAnalysisOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__38528699bc9adaeb6dcd2c68ce8847604b97102bc4daca3c1655f441835d9432)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDataExport")
    def put_data_export(
        self,
        *,
        destination: typing.Union[S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestination, typing.Dict[builtins.str, typing.Any]],
        output_schema_version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param destination: destination block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#destination S3BucketAnalyticsConfiguration#destination}
        :param output_schema_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#output_schema_version S3BucketAnalyticsConfiguration#output_schema_version}.
        '''
        value = S3BucketAnalyticsConfigurationStorageClassAnalysisDataExport(
            destination=destination, output_schema_version=output_schema_version
        )

        return typing.cast(None, jsii.invoke(self, "putDataExport", [value]))

    @builtins.property
    @jsii.member(jsii_name="dataExport")
    def data_export(
        self,
    ) -> S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportOutputReference:
        return typing.cast(S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportOutputReference, jsii.get(self, "dataExport"))

    @builtins.property
    @jsii.member(jsii_name="dataExportInput")
    def data_export_input(
        self,
    ) -> typing.Optional[S3BucketAnalyticsConfigurationStorageClassAnalysisDataExport]:
        return typing.cast(typing.Optional[S3BucketAnalyticsConfigurationStorageClassAnalysisDataExport], jsii.get(self, "dataExportInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3BucketAnalyticsConfigurationStorageClassAnalysis]:
        return typing.cast(typing.Optional[S3BucketAnalyticsConfigurationStorageClassAnalysis], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3BucketAnalyticsConfigurationStorageClassAnalysis],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0563371f5a96d1e09970f32f105d2b871568eb43c23d2662bc1f9f0fa6e1439a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "S3BucketAnalyticsConfiguration",
    "S3BucketAnalyticsConfigurationConfig",
    "S3BucketAnalyticsConfigurationFilter",
    "S3BucketAnalyticsConfigurationFilterOutputReference",
    "S3BucketAnalyticsConfigurationStorageClassAnalysis",
    "S3BucketAnalyticsConfigurationStorageClassAnalysisDataExport",
    "S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestination",
    "S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestinationOutputReference",
    "S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestination",
    "S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestinationOutputReference",
    "S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportOutputReference",
    "S3BucketAnalyticsConfigurationStorageClassAnalysisOutputReference",
]

publication.publish()

def _typecheckingstub__58b0dd7cc1b63968229e2ada117c9ba8d3393185c708bbf14b757f35457f5235(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    bucket: builtins.str,
    name: builtins.str,
    filter: typing.Optional[typing.Union[S3BucketAnalyticsConfigurationFilter, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    storage_class_analysis: typing.Optional[typing.Union[S3BucketAnalyticsConfigurationStorageClassAnalysis, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__6502a68c4c2bb3a1f139879840125459abdf0199fcde54292cd6b2462d8c5a22(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25db507517e1051853696a65a76593c77629659465e7c0d22febc815cd7e9a1a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c35d1592944b8b26721be5c277a35ba8519562aee399a1ad00c2e9b634e3b5e1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fae19cc3c812737783c7471b3b171f7820e030b2b941f2a39bb7d0907354c37d(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    bucket: builtins.str,
    name: builtins.str,
    filter: typing.Optional[typing.Union[S3BucketAnalyticsConfigurationFilter, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    storage_class_analysis: typing.Optional[typing.Union[S3BucketAnalyticsConfigurationStorageClassAnalysis, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87f8a9fc09bba0ddfe484c9523bcf0d6bf2a48097d53ebe9091950ed573a36e8(
    *,
    prefix: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b2f5a62f4fb981c4c6f555e0f3a5536112b0f582cce8a0f1eea93666ace7c2e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9d3868d7853b51f424ec6623732855ed71976641cd7a68e2fd8050b3be8eceb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0daf13c47e29c42f658d35200c8457f2326dd9a90c3c5ef77d53458ff5d9ebec(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63042950273915b9c80d38a5780c39b42d5a49bb2ff71aced86916fe3e4a3a1f(
    value: typing.Optional[S3BucketAnalyticsConfigurationFilter],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db8c0ac66e4035ec640b70efdb720e4064821140c260f12332b48c4cde55c8ac(
    *,
    data_export: typing.Union[S3BucketAnalyticsConfigurationStorageClassAnalysisDataExport, typing.Dict[builtins.str, typing.Any]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ff10b49edcc5b220d46c777bddb781d8ac6ad83b184b96471c57c060fda5276(
    *,
    destination: typing.Union[S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestination, typing.Dict[builtins.str, typing.Any]],
    output_schema_version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0dfd54cadb7bfcd1cc33cddbab510b9e6a840c45388cac5b0620fc46e4b2d43(
    *,
    s3_bucket_destination: typing.Union[S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestination, typing.Dict[builtins.str, typing.Any]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__502ea3574ecbc07b0b9293385bdb6628a64ec951ef333bd4f1aa667bf4fd47f5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9cca424c960bf2c446ebffcd877d7343db8cdf0b20ac713ba720246a20868bf9(
    value: typing.Optional[S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestination],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa809d2f2749ffb70fcf4643c80d8f5f1004dbda9e18b4d87571bbcaae81290a(
    *,
    bucket_arn: builtins.str,
    bucket_account_id: typing.Optional[builtins.str] = None,
    format: typing.Optional[builtins.str] = None,
    prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2068c01e79a33dff2502eec459fda346186b5e8186b565c64d8a985b1ec3d446(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__045b655144425e2c2172efc33350f8b4c331bc6e44b9745ec43d3324535398b1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a25263ea876b7564fca24e2efc998ca1062c9a85879fc9b381ed084041a37923(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7aa2912f0c91b191fc99805eefc599588e23b030b8e5ec3fa52e0460db5b830e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2717078ecf8eff17eb41d973189e5607c80b797bebf0ef99678c8d5e7bc7a2d7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86ae6f07508ad03bfcd717f82f7970db2c729e95a350da5b9efce034aee6fa9f(
    value: typing.Optional[S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestination],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c6f9632af24c1d7ea70431e0d930155c6f281ebb6635d1d78d193758c457f54(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b096d1e9a15beeae536fb09a8ee8c608320f4eb5822993237db090f769e0b62(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81a95dbeec9315d3ec2165dad2fb5eb4fc29d5b05ed79d2d39ee8909449412ef(
    value: typing.Optional[S3BucketAnalyticsConfigurationStorageClassAnalysisDataExport],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38528699bc9adaeb6dcd2c68ce8847604b97102bc4daca3c1655f441835d9432(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0563371f5a96d1e09970f32f105d2b871568eb43c23d2662bc1f9f0fa6e1439a(
    value: typing.Optional[S3BucketAnalyticsConfigurationStorageClassAnalysis],
) -> None:
    """Type checking stubs"""
    pass
