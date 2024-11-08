'''
# `aws_kendra_data_source`

Refer to the Terraform Registory for docs: [`aws_kendra_data_source`](https://www.terraform.io/docs/providers/aws/r/kendra_data_source).
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


class KendraDataSource(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kendraDataSource.KendraDataSource",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source aws_kendra_data_source}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        index_id: builtins.str,
        name: builtins.str,
        type: builtins.str,
        configuration: typing.Optional[typing.Union["KendraDataSourceConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        custom_document_enrichment_configuration: typing.Optional[typing.Union["KendraDataSourceCustomDocumentEnrichmentConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        language_code: typing.Optional[builtins.str] = None,
        role_arn: typing.Optional[builtins.str] = None,
        schedule: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["KendraDataSourceTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source aws_kendra_data_source} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param index_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#index_id KendraDataSource#index_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#name KendraDataSource#name}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#type KendraDataSource#type}.
        :param configuration: configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#configuration KendraDataSource#configuration}
        :param custom_document_enrichment_configuration: custom_document_enrichment_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#custom_document_enrichment_configuration KendraDataSource#custom_document_enrichment_configuration}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#description KendraDataSource#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#id KendraDataSource#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param language_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#language_code KendraDataSource#language_code}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#role_arn KendraDataSource#role_arn}.
        :param schedule: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#schedule KendraDataSource#schedule}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#tags KendraDataSource#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#tags_all KendraDataSource#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#timeouts KendraDataSource#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60baf8b44110c732a4cd738c259e25fc807db3752bc22ef2f2dd94682d1696ef)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = KendraDataSourceConfig(
            index_id=index_id,
            name=name,
            type=type,
            configuration=configuration,
            custom_document_enrichment_configuration=custom_document_enrichment_configuration,
            description=description,
            id=id,
            language_code=language_code,
            role_arn=role_arn,
            schedule=schedule,
            tags=tags,
            tags_all=tags_all,
            timeouts=timeouts,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putConfiguration")
    def put_configuration(
        self,
        *,
        s3_configuration: typing.Optional[typing.Union["KendraDataSourceConfigurationS3Configuration", typing.Dict[builtins.str, typing.Any]]] = None,
        web_crawler_configuration: typing.Optional[typing.Union["KendraDataSourceConfigurationWebCrawlerConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param s3_configuration: s3_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#s3_configuration KendraDataSource#s3_configuration}
        :param web_crawler_configuration: web_crawler_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#web_crawler_configuration KendraDataSource#web_crawler_configuration}
        '''
        value = KendraDataSourceConfiguration(
            s3_configuration=s3_configuration,
            web_crawler_configuration=web_crawler_configuration,
        )

        return typing.cast(None, jsii.invoke(self, "putConfiguration", [value]))

    @jsii.member(jsii_name="putCustomDocumentEnrichmentConfiguration")
    def put_custom_document_enrichment_configuration(
        self,
        *,
        inline_configurations: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurations", typing.Dict[builtins.str, typing.Any]]]]] = None,
        post_extraction_hook_configuration: typing.Optional[typing.Union["KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        pre_extraction_hook_configuration: typing.Optional[typing.Union["KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        role_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param inline_configurations: inline_configurations block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#inline_configurations KendraDataSource#inline_configurations}
        :param post_extraction_hook_configuration: post_extraction_hook_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#post_extraction_hook_configuration KendraDataSource#post_extraction_hook_configuration}
        :param pre_extraction_hook_configuration: pre_extraction_hook_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#pre_extraction_hook_configuration KendraDataSource#pre_extraction_hook_configuration}
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#role_arn KendraDataSource#role_arn}.
        '''
        value = KendraDataSourceCustomDocumentEnrichmentConfiguration(
            inline_configurations=inline_configurations,
            post_extraction_hook_configuration=post_extraction_hook_configuration,
            pre_extraction_hook_configuration=pre_extraction_hook_configuration,
            role_arn=role_arn,
        )

        return typing.cast(None, jsii.invoke(self, "putCustomDocumentEnrichmentConfiguration", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#create KendraDataSource#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#delete KendraDataSource#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#update KendraDataSource#update}.
        '''
        value = KendraDataSourceTimeouts(create=create, delete=delete, update=update)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetConfiguration")
    def reset_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfiguration", []))

    @jsii.member(jsii_name="resetCustomDocumentEnrichmentConfiguration")
    def reset_custom_document_enrichment_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomDocumentEnrichmentConfiguration", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLanguageCode")
    def reset_language_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLanguageCode", []))

    @jsii.member(jsii_name="resetRoleArn")
    def reset_role_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRoleArn", []))

    @jsii.member(jsii_name="resetSchedule")
    def reset_schedule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSchedule", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

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
    @jsii.member(jsii_name="configuration")
    def configuration(self) -> "KendraDataSourceConfigurationOutputReference":
        return typing.cast("KendraDataSourceConfigurationOutputReference", jsii.get(self, "configuration"))

    @builtins.property
    @jsii.member(jsii_name="createdAt")
    def created_at(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdAt"))

    @builtins.property
    @jsii.member(jsii_name="customDocumentEnrichmentConfiguration")
    def custom_document_enrichment_configuration(
        self,
    ) -> "KendraDataSourceCustomDocumentEnrichmentConfigurationOutputReference":
        return typing.cast("KendraDataSourceCustomDocumentEnrichmentConfigurationOutputReference", jsii.get(self, "customDocumentEnrichmentConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="dataSourceId")
    def data_source_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataSourceId"))

    @builtins.property
    @jsii.member(jsii_name="errorMessage")
    def error_message(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "errorMessage"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "KendraDataSourceTimeoutsOutputReference":
        return typing.cast("KendraDataSourceTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="updatedAt")
    def updated_at(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "updatedAt"))

    @builtins.property
    @jsii.member(jsii_name="configurationInput")
    def configuration_input(self) -> typing.Optional["KendraDataSourceConfiguration"]:
        return typing.cast(typing.Optional["KendraDataSourceConfiguration"], jsii.get(self, "configurationInput"))

    @builtins.property
    @jsii.member(jsii_name="customDocumentEnrichmentConfigurationInput")
    def custom_document_enrichment_configuration_input(
        self,
    ) -> typing.Optional["KendraDataSourceCustomDocumentEnrichmentConfiguration"]:
        return typing.cast(typing.Optional["KendraDataSourceCustomDocumentEnrichmentConfiguration"], jsii.get(self, "customDocumentEnrichmentConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="indexIdInput")
    def index_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "indexIdInput"))

    @builtins.property
    @jsii.member(jsii_name="languageCodeInput")
    def language_code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "languageCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="scheduleInput")
    def schedule_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scheduleInput"))

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
    ) -> typing.Optional[typing.Union["KendraDataSourceTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["KendraDataSourceTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__199e6169834a5c1ae52484b019d2fbe769d441dc4c8b7f68c2e9d0be328ba97b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__272b547feff976e273affe1902667da01e822b3cbb1af56498dcb7fc1d499046)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="indexId")
    def index_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "indexId"))

    @index_id.setter
    def index_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ecfc601d9470eb0a94aa6591da9bea496b0ea0c96d82525db85bc439387ed46)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "indexId", value)

    @builtins.property
    @jsii.member(jsii_name="languageCode")
    def language_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "languageCode"))

    @language_code.setter
    def language_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5900e9235bec373253c99a5ba0008e11e70a29e444dcb1394259519babce5c78)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "languageCode", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95b43b84a300a4a6cc1148a384923c551268640f2896b37019be3fe8c7d6db8a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67d3ebc470fc721eb050331e9c9e521ab682d392fdd5f07c105fa344cc5ac85b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="schedule")
    def schedule(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "schedule"))

    @schedule.setter
    def schedule(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24c6a9e0220405f7e2e46bb81175d34c326c1e0e8f19a1f96aa8d7831ed8f8b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schedule", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d8a7ee6566510bc41b8b98933ada52d13ec87f9f384d8b57cd487cbc856bf75)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bee823653548eaf77070e10804948c9a717dedbae6ff495c9e142acf44a8e41d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87f8b80d2a765a9f1f9a6730c5cc2a6cefad45c75dd462dc0e8838f61c304c4a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)


@jsii.data_type(
    jsii_type="aws.kendraDataSource.KendraDataSourceConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "index_id": "indexId",
        "name": "name",
        "type": "type",
        "configuration": "configuration",
        "custom_document_enrichment_configuration": "customDocumentEnrichmentConfiguration",
        "description": "description",
        "id": "id",
        "language_code": "languageCode",
        "role_arn": "roleArn",
        "schedule": "schedule",
        "tags": "tags",
        "tags_all": "tagsAll",
        "timeouts": "timeouts",
    },
)
class KendraDataSourceConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        index_id: builtins.str,
        name: builtins.str,
        type: builtins.str,
        configuration: typing.Optional[typing.Union["KendraDataSourceConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        custom_document_enrichment_configuration: typing.Optional[typing.Union["KendraDataSourceCustomDocumentEnrichmentConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        language_code: typing.Optional[builtins.str] = None,
        role_arn: typing.Optional[builtins.str] = None,
        schedule: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["KendraDataSourceTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param index_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#index_id KendraDataSource#index_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#name KendraDataSource#name}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#type KendraDataSource#type}.
        :param configuration: configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#configuration KendraDataSource#configuration}
        :param custom_document_enrichment_configuration: custom_document_enrichment_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#custom_document_enrichment_configuration KendraDataSource#custom_document_enrichment_configuration}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#description KendraDataSource#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#id KendraDataSource#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param language_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#language_code KendraDataSource#language_code}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#role_arn KendraDataSource#role_arn}.
        :param schedule: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#schedule KendraDataSource#schedule}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#tags KendraDataSource#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#tags_all KendraDataSource#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#timeouts KendraDataSource#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(configuration, dict):
            configuration = KendraDataSourceConfiguration(**configuration)
        if isinstance(custom_document_enrichment_configuration, dict):
            custom_document_enrichment_configuration = KendraDataSourceCustomDocumentEnrichmentConfiguration(**custom_document_enrichment_configuration)
        if isinstance(timeouts, dict):
            timeouts = KendraDataSourceTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02950fb7577167c63456bdd034f68dd907cf47880d5481fd4018b8aae9f59afb)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument index_id", value=index_id, expected_type=type_hints["index_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument configuration", value=configuration, expected_type=type_hints["configuration"])
            check_type(argname="argument custom_document_enrichment_configuration", value=custom_document_enrichment_configuration, expected_type=type_hints["custom_document_enrichment_configuration"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument language_code", value=language_code, expected_type=type_hints["language_code"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument schedule", value=schedule, expected_type=type_hints["schedule"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "index_id": index_id,
            "name": name,
            "type": type,
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
        if configuration is not None:
            self._values["configuration"] = configuration
        if custom_document_enrichment_configuration is not None:
            self._values["custom_document_enrichment_configuration"] = custom_document_enrichment_configuration
        if description is not None:
            self._values["description"] = description
        if id is not None:
            self._values["id"] = id
        if language_code is not None:
            self._values["language_code"] = language_code
        if role_arn is not None:
            self._values["role_arn"] = role_arn
        if schedule is not None:
            self._values["schedule"] = schedule
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if timeouts is not None:
            self._values["timeouts"] = timeouts

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
    def index_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#index_id KendraDataSource#index_id}.'''
        result = self._values.get("index_id")
        assert result is not None, "Required property 'index_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#name KendraDataSource#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#type KendraDataSource#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def configuration(self) -> typing.Optional["KendraDataSourceConfiguration"]:
        '''configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#configuration KendraDataSource#configuration}
        '''
        result = self._values.get("configuration")
        return typing.cast(typing.Optional["KendraDataSourceConfiguration"], result)

    @builtins.property
    def custom_document_enrichment_configuration(
        self,
    ) -> typing.Optional["KendraDataSourceCustomDocumentEnrichmentConfiguration"]:
        '''custom_document_enrichment_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#custom_document_enrichment_configuration KendraDataSource#custom_document_enrichment_configuration}
        '''
        result = self._values.get("custom_document_enrichment_configuration")
        return typing.cast(typing.Optional["KendraDataSourceCustomDocumentEnrichmentConfiguration"], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#description KendraDataSource#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#id KendraDataSource#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def language_code(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#language_code KendraDataSource#language_code}.'''
        result = self._values.get("language_code")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#role_arn KendraDataSource#role_arn}.'''
        result = self._values.get("role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def schedule(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#schedule KendraDataSource#schedule}.'''
        result = self._values.get("schedule")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#tags KendraDataSource#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#tags_all KendraDataSource#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["KendraDataSourceTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#timeouts KendraDataSource#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["KendraDataSourceTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraDataSourceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.kendraDataSource.KendraDataSourceConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "s3_configuration": "s3Configuration",
        "web_crawler_configuration": "webCrawlerConfiguration",
    },
)
class KendraDataSourceConfiguration:
    def __init__(
        self,
        *,
        s3_configuration: typing.Optional[typing.Union["KendraDataSourceConfigurationS3Configuration", typing.Dict[builtins.str, typing.Any]]] = None,
        web_crawler_configuration: typing.Optional[typing.Union["KendraDataSourceConfigurationWebCrawlerConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param s3_configuration: s3_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#s3_configuration KendraDataSource#s3_configuration}
        :param web_crawler_configuration: web_crawler_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#web_crawler_configuration KendraDataSource#web_crawler_configuration}
        '''
        if isinstance(s3_configuration, dict):
            s3_configuration = KendraDataSourceConfigurationS3Configuration(**s3_configuration)
        if isinstance(web_crawler_configuration, dict):
            web_crawler_configuration = KendraDataSourceConfigurationWebCrawlerConfiguration(**web_crawler_configuration)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41d1c880e481b0e5e9b5f3811c0316a97f7157781366b94cece21ce8745cab6c)
            check_type(argname="argument s3_configuration", value=s3_configuration, expected_type=type_hints["s3_configuration"])
            check_type(argname="argument web_crawler_configuration", value=web_crawler_configuration, expected_type=type_hints["web_crawler_configuration"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if s3_configuration is not None:
            self._values["s3_configuration"] = s3_configuration
        if web_crawler_configuration is not None:
            self._values["web_crawler_configuration"] = web_crawler_configuration

    @builtins.property
    def s3_configuration(
        self,
    ) -> typing.Optional["KendraDataSourceConfigurationS3Configuration"]:
        '''s3_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#s3_configuration KendraDataSource#s3_configuration}
        '''
        result = self._values.get("s3_configuration")
        return typing.cast(typing.Optional["KendraDataSourceConfigurationS3Configuration"], result)

    @builtins.property
    def web_crawler_configuration(
        self,
    ) -> typing.Optional["KendraDataSourceConfigurationWebCrawlerConfiguration"]:
        '''web_crawler_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#web_crawler_configuration KendraDataSource#web_crawler_configuration}
        '''
        result = self._values.get("web_crawler_configuration")
        return typing.cast(typing.Optional["KendraDataSourceConfigurationWebCrawlerConfiguration"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraDataSourceConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KendraDataSourceConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kendraDataSource.KendraDataSourceConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d5eb453fde97188d6a89c2f0759f5a2f01dc1c8b0c491670ee33908256870df8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putS3Configuration")
    def put_s3_configuration(
        self,
        *,
        bucket_name: builtins.str,
        access_control_list_configuration: typing.Optional[typing.Union["KendraDataSourceConfigurationS3ConfigurationAccessControlListConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        documents_metadata_configuration: typing.Optional[typing.Union["KendraDataSourceConfigurationS3ConfigurationDocumentsMetadataConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        exclusion_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
        inclusion_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
        inclusion_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#bucket_name KendraDataSource#bucket_name}.
        :param access_control_list_configuration: access_control_list_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#access_control_list_configuration KendraDataSource#access_control_list_configuration}
        :param documents_metadata_configuration: documents_metadata_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#documents_metadata_configuration KendraDataSource#documents_metadata_configuration}
        :param exclusion_patterns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#exclusion_patterns KendraDataSource#exclusion_patterns}.
        :param inclusion_patterns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#inclusion_patterns KendraDataSource#inclusion_patterns}.
        :param inclusion_prefixes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#inclusion_prefixes KendraDataSource#inclusion_prefixes}.
        '''
        value = KendraDataSourceConfigurationS3Configuration(
            bucket_name=bucket_name,
            access_control_list_configuration=access_control_list_configuration,
            documents_metadata_configuration=documents_metadata_configuration,
            exclusion_patterns=exclusion_patterns,
            inclusion_patterns=inclusion_patterns,
            inclusion_prefixes=inclusion_prefixes,
        )

        return typing.cast(None, jsii.invoke(self, "putS3Configuration", [value]))

    @jsii.member(jsii_name="putWebCrawlerConfiguration")
    def put_web_crawler_configuration(
        self,
        *,
        urls: typing.Union["KendraDataSourceConfigurationWebCrawlerConfigurationUrls", typing.Dict[builtins.str, typing.Any]],
        authentication_configuration: typing.Optional[typing.Union["KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        crawl_depth: typing.Optional[jsii.Number] = None,
        max_content_size_per_page_in_mega_bytes: typing.Optional[jsii.Number] = None,
        max_links_per_page: typing.Optional[jsii.Number] = None,
        max_urls_per_minute_crawl_rate: typing.Optional[jsii.Number] = None,
        proxy_configuration: typing.Optional[typing.Union["KendraDataSourceConfigurationWebCrawlerConfigurationProxyConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        url_exclusion_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
        url_inclusion_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param urls: urls block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#urls KendraDataSource#urls}
        :param authentication_configuration: authentication_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#authentication_configuration KendraDataSource#authentication_configuration}
        :param crawl_depth: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#crawl_depth KendraDataSource#crawl_depth}.
        :param max_content_size_per_page_in_mega_bytes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#max_content_size_per_page_in_mega_bytes KendraDataSource#max_content_size_per_page_in_mega_bytes}.
        :param max_links_per_page: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#max_links_per_page KendraDataSource#max_links_per_page}.
        :param max_urls_per_minute_crawl_rate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#max_urls_per_minute_crawl_rate KendraDataSource#max_urls_per_minute_crawl_rate}.
        :param proxy_configuration: proxy_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#proxy_configuration KendraDataSource#proxy_configuration}
        :param url_exclusion_patterns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#url_exclusion_patterns KendraDataSource#url_exclusion_patterns}.
        :param url_inclusion_patterns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#url_inclusion_patterns KendraDataSource#url_inclusion_patterns}.
        '''
        value = KendraDataSourceConfigurationWebCrawlerConfiguration(
            urls=urls,
            authentication_configuration=authentication_configuration,
            crawl_depth=crawl_depth,
            max_content_size_per_page_in_mega_bytes=max_content_size_per_page_in_mega_bytes,
            max_links_per_page=max_links_per_page,
            max_urls_per_minute_crawl_rate=max_urls_per_minute_crawl_rate,
            proxy_configuration=proxy_configuration,
            url_exclusion_patterns=url_exclusion_patterns,
            url_inclusion_patterns=url_inclusion_patterns,
        )

        return typing.cast(None, jsii.invoke(self, "putWebCrawlerConfiguration", [value]))

    @jsii.member(jsii_name="resetS3Configuration")
    def reset_s3_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3Configuration", []))

    @jsii.member(jsii_name="resetWebCrawlerConfiguration")
    def reset_web_crawler_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWebCrawlerConfiguration", []))

    @builtins.property
    @jsii.member(jsii_name="s3Configuration")
    def s3_configuration(
        self,
    ) -> "KendraDataSourceConfigurationS3ConfigurationOutputReference":
        return typing.cast("KendraDataSourceConfigurationS3ConfigurationOutputReference", jsii.get(self, "s3Configuration"))

    @builtins.property
    @jsii.member(jsii_name="webCrawlerConfiguration")
    def web_crawler_configuration(
        self,
    ) -> "KendraDataSourceConfigurationWebCrawlerConfigurationOutputReference":
        return typing.cast("KendraDataSourceConfigurationWebCrawlerConfigurationOutputReference", jsii.get(self, "webCrawlerConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="s3ConfigurationInput")
    def s3_configuration_input(
        self,
    ) -> typing.Optional["KendraDataSourceConfigurationS3Configuration"]:
        return typing.cast(typing.Optional["KendraDataSourceConfigurationS3Configuration"], jsii.get(self, "s3ConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="webCrawlerConfigurationInput")
    def web_crawler_configuration_input(
        self,
    ) -> typing.Optional["KendraDataSourceConfigurationWebCrawlerConfiguration"]:
        return typing.cast(typing.Optional["KendraDataSourceConfigurationWebCrawlerConfiguration"], jsii.get(self, "webCrawlerConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[KendraDataSourceConfiguration]:
        return typing.cast(typing.Optional[KendraDataSourceConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KendraDataSourceConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bbee117ed4ba080f85f63914824cb9bf66c43096d2515eaa39168124955de017)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kendraDataSource.KendraDataSourceConfigurationS3Configuration",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_name": "bucketName",
        "access_control_list_configuration": "accessControlListConfiguration",
        "documents_metadata_configuration": "documentsMetadataConfiguration",
        "exclusion_patterns": "exclusionPatterns",
        "inclusion_patterns": "inclusionPatterns",
        "inclusion_prefixes": "inclusionPrefixes",
    },
)
class KendraDataSourceConfigurationS3Configuration:
    def __init__(
        self,
        *,
        bucket_name: builtins.str,
        access_control_list_configuration: typing.Optional[typing.Union["KendraDataSourceConfigurationS3ConfigurationAccessControlListConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        documents_metadata_configuration: typing.Optional[typing.Union["KendraDataSourceConfigurationS3ConfigurationDocumentsMetadataConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        exclusion_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
        inclusion_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
        inclusion_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#bucket_name KendraDataSource#bucket_name}.
        :param access_control_list_configuration: access_control_list_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#access_control_list_configuration KendraDataSource#access_control_list_configuration}
        :param documents_metadata_configuration: documents_metadata_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#documents_metadata_configuration KendraDataSource#documents_metadata_configuration}
        :param exclusion_patterns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#exclusion_patterns KendraDataSource#exclusion_patterns}.
        :param inclusion_patterns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#inclusion_patterns KendraDataSource#inclusion_patterns}.
        :param inclusion_prefixes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#inclusion_prefixes KendraDataSource#inclusion_prefixes}.
        '''
        if isinstance(access_control_list_configuration, dict):
            access_control_list_configuration = KendraDataSourceConfigurationS3ConfigurationAccessControlListConfiguration(**access_control_list_configuration)
        if isinstance(documents_metadata_configuration, dict):
            documents_metadata_configuration = KendraDataSourceConfigurationS3ConfigurationDocumentsMetadataConfiguration(**documents_metadata_configuration)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac272edee0fc4616f2e89908126880ff7e37c22162963abe25d9949ffa3275ac)
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            check_type(argname="argument access_control_list_configuration", value=access_control_list_configuration, expected_type=type_hints["access_control_list_configuration"])
            check_type(argname="argument documents_metadata_configuration", value=documents_metadata_configuration, expected_type=type_hints["documents_metadata_configuration"])
            check_type(argname="argument exclusion_patterns", value=exclusion_patterns, expected_type=type_hints["exclusion_patterns"])
            check_type(argname="argument inclusion_patterns", value=inclusion_patterns, expected_type=type_hints["inclusion_patterns"])
            check_type(argname="argument inclusion_prefixes", value=inclusion_prefixes, expected_type=type_hints["inclusion_prefixes"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bucket_name": bucket_name,
        }
        if access_control_list_configuration is not None:
            self._values["access_control_list_configuration"] = access_control_list_configuration
        if documents_metadata_configuration is not None:
            self._values["documents_metadata_configuration"] = documents_metadata_configuration
        if exclusion_patterns is not None:
            self._values["exclusion_patterns"] = exclusion_patterns
        if inclusion_patterns is not None:
            self._values["inclusion_patterns"] = inclusion_patterns
        if inclusion_prefixes is not None:
            self._values["inclusion_prefixes"] = inclusion_prefixes

    @builtins.property
    def bucket_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#bucket_name KendraDataSource#bucket_name}.'''
        result = self._values.get("bucket_name")
        assert result is not None, "Required property 'bucket_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_control_list_configuration(
        self,
    ) -> typing.Optional["KendraDataSourceConfigurationS3ConfigurationAccessControlListConfiguration"]:
        '''access_control_list_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#access_control_list_configuration KendraDataSource#access_control_list_configuration}
        '''
        result = self._values.get("access_control_list_configuration")
        return typing.cast(typing.Optional["KendraDataSourceConfigurationS3ConfigurationAccessControlListConfiguration"], result)

    @builtins.property
    def documents_metadata_configuration(
        self,
    ) -> typing.Optional["KendraDataSourceConfigurationS3ConfigurationDocumentsMetadataConfiguration"]:
        '''documents_metadata_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#documents_metadata_configuration KendraDataSource#documents_metadata_configuration}
        '''
        result = self._values.get("documents_metadata_configuration")
        return typing.cast(typing.Optional["KendraDataSourceConfigurationS3ConfigurationDocumentsMetadataConfiguration"], result)

    @builtins.property
    def exclusion_patterns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#exclusion_patterns KendraDataSource#exclusion_patterns}.'''
        result = self._values.get("exclusion_patterns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def inclusion_patterns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#inclusion_patterns KendraDataSource#inclusion_patterns}.'''
        result = self._values.get("inclusion_patterns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def inclusion_prefixes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#inclusion_prefixes KendraDataSource#inclusion_prefixes}.'''
        result = self._values.get("inclusion_prefixes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraDataSourceConfigurationS3Configuration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.kendraDataSource.KendraDataSourceConfigurationS3ConfigurationAccessControlListConfiguration",
    jsii_struct_bases=[],
    name_mapping={"key_path": "keyPath"},
)
class KendraDataSourceConfigurationS3ConfigurationAccessControlListConfiguration:
    def __init__(self, *, key_path: typing.Optional[builtins.str] = None) -> None:
        '''
        :param key_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#key_path KendraDataSource#key_path}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25fbc7e1cbf8e319a8057c92bd8ee18bcf9506f301c85652f209f0e05b69cf1a)
            check_type(argname="argument key_path", value=key_path, expected_type=type_hints["key_path"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if key_path is not None:
            self._values["key_path"] = key_path

    @builtins.property
    def key_path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#key_path KendraDataSource#key_path}.'''
        result = self._values.get("key_path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraDataSourceConfigurationS3ConfigurationAccessControlListConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KendraDataSourceConfigurationS3ConfigurationAccessControlListConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kendraDataSource.KendraDataSourceConfigurationS3ConfigurationAccessControlListConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4af70d422045f46c5374f14a02125d13e4688503ed4ebb04b14559f2afdc65d3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetKeyPath")
    def reset_key_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyPath", []))

    @builtins.property
    @jsii.member(jsii_name="keyPathInput")
    def key_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyPathInput"))

    @builtins.property
    @jsii.member(jsii_name="keyPath")
    def key_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyPath"))

    @key_path.setter
    def key_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ffe2104ba3b93bdf4dca8b319ecda284d019f505637a58551f4b2e901cd2de66)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyPath", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KendraDataSourceConfigurationS3ConfigurationAccessControlListConfiguration]:
        return typing.cast(typing.Optional[KendraDataSourceConfigurationS3ConfigurationAccessControlListConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KendraDataSourceConfigurationS3ConfigurationAccessControlListConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7497b9c393cc5cdb7ef65192ff5cbc55a0dbed8f926b05349efba474697099ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kendraDataSource.KendraDataSourceConfigurationS3ConfigurationDocumentsMetadataConfiguration",
    jsii_struct_bases=[],
    name_mapping={"s3_prefix": "s3Prefix"},
)
class KendraDataSourceConfigurationS3ConfigurationDocumentsMetadataConfiguration:
    def __init__(self, *, s3_prefix: typing.Optional[builtins.str] = None) -> None:
        '''
        :param s3_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#s3_prefix KendraDataSource#s3_prefix}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d968657f0a5be41c470a76a28059a90e59c5cc0582dddf95789a111204a9b50d)
            check_type(argname="argument s3_prefix", value=s3_prefix, expected_type=type_hints["s3_prefix"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if s3_prefix is not None:
            self._values["s3_prefix"] = s3_prefix

    @builtins.property
    def s3_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#s3_prefix KendraDataSource#s3_prefix}.'''
        result = self._values.get("s3_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraDataSourceConfigurationS3ConfigurationDocumentsMetadataConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KendraDataSourceConfigurationS3ConfigurationDocumentsMetadataConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kendraDataSource.KendraDataSourceConfigurationS3ConfigurationDocumentsMetadataConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__fa015ac8da967280b719b7d0ee2bac79b2dc59511ee209cb3141508fa3083758)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetS3Prefix")
    def reset_s3_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3Prefix", []))

    @builtins.property
    @jsii.member(jsii_name="s3PrefixInput")
    def s3_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "s3PrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="s3Prefix")
    def s3_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "s3Prefix"))

    @s3_prefix.setter
    def s3_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1027f0d8eb3b08bb18369110475a6ce9573ccaf790b9b2293604625f0ccd06c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3Prefix", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KendraDataSourceConfigurationS3ConfigurationDocumentsMetadataConfiguration]:
        return typing.cast(typing.Optional[KendraDataSourceConfigurationS3ConfigurationDocumentsMetadataConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KendraDataSourceConfigurationS3ConfigurationDocumentsMetadataConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__921ac1502713f35dcb733dd0938aa3c48ebeb042d4822d51c67369921b955ea8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KendraDataSourceConfigurationS3ConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kendraDataSource.KendraDataSourceConfigurationS3ConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__46ed771170b831bebf8d0036ceec8b2dc13db12f81645e497403d6215b619533)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAccessControlListConfiguration")
    def put_access_control_list_configuration(
        self,
        *,
        key_path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param key_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#key_path KendraDataSource#key_path}.
        '''
        value = KendraDataSourceConfigurationS3ConfigurationAccessControlListConfiguration(
            key_path=key_path
        )

        return typing.cast(None, jsii.invoke(self, "putAccessControlListConfiguration", [value]))

    @jsii.member(jsii_name="putDocumentsMetadataConfiguration")
    def put_documents_metadata_configuration(
        self,
        *,
        s3_prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param s3_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#s3_prefix KendraDataSource#s3_prefix}.
        '''
        value = KendraDataSourceConfigurationS3ConfigurationDocumentsMetadataConfiguration(
            s3_prefix=s3_prefix
        )

        return typing.cast(None, jsii.invoke(self, "putDocumentsMetadataConfiguration", [value]))

    @jsii.member(jsii_name="resetAccessControlListConfiguration")
    def reset_access_control_list_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessControlListConfiguration", []))

    @jsii.member(jsii_name="resetDocumentsMetadataConfiguration")
    def reset_documents_metadata_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDocumentsMetadataConfiguration", []))

    @jsii.member(jsii_name="resetExclusionPatterns")
    def reset_exclusion_patterns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExclusionPatterns", []))

    @jsii.member(jsii_name="resetInclusionPatterns")
    def reset_inclusion_patterns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInclusionPatterns", []))

    @jsii.member(jsii_name="resetInclusionPrefixes")
    def reset_inclusion_prefixes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInclusionPrefixes", []))

    @builtins.property
    @jsii.member(jsii_name="accessControlListConfiguration")
    def access_control_list_configuration(
        self,
    ) -> KendraDataSourceConfigurationS3ConfigurationAccessControlListConfigurationOutputReference:
        return typing.cast(KendraDataSourceConfigurationS3ConfigurationAccessControlListConfigurationOutputReference, jsii.get(self, "accessControlListConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="documentsMetadataConfiguration")
    def documents_metadata_configuration(
        self,
    ) -> KendraDataSourceConfigurationS3ConfigurationDocumentsMetadataConfigurationOutputReference:
        return typing.cast(KendraDataSourceConfigurationS3ConfigurationDocumentsMetadataConfigurationOutputReference, jsii.get(self, "documentsMetadataConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="accessControlListConfigurationInput")
    def access_control_list_configuration_input(
        self,
    ) -> typing.Optional[KendraDataSourceConfigurationS3ConfigurationAccessControlListConfiguration]:
        return typing.cast(typing.Optional[KendraDataSourceConfigurationS3ConfigurationAccessControlListConfiguration], jsii.get(self, "accessControlListConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketNameInput")
    def bucket_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketNameInput"))

    @builtins.property
    @jsii.member(jsii_name="documentsMetadataConfigurationInput")
    def documents_metadata_configuration_input(
        self,
    ) -> typing.Optional[KendraDataSourceConfigurationS3ConfigurationDocumentsMetadataConfiguration]:
        return typing.cast(typing.Optional[KendraDataSourceConfigurationS3ConfigurationDocumentsMetadataConfiguration], jsii.get(self, "documentsMetadataConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="exclusionPatternsInput")
    def exclusion_patterns_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "exclusionPatternsInput"))

    @builtins.property
    @jsii.member(jsii_name="inclusionPatternsInput")
    def inclusion_patterns_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "inclusionPatternsInput"))

    @builtins.property
    @jsii.member(jsii_name="inclusionPrefixesInput")
    def inclusion_prefixes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "inclusionPrefixesInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketName")
    def bucket_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketName"))

    @bucket_name.setter
    def bucket_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad6c1a74d210b84183f81bc13ced7bea6ebc1b08b2bf89e3a42cff5ae3e32a2b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketName", value)

    @builtins.property
    @jsii.member(jsii_name="exclusionPatterns")
    def exclusion_patterns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "exclusionPatterns"))

    @exclusion_patterns.setter
    def exclusion_patterns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b579b54e68d4bb24fa34ac825207c386d770f2f79d561a06e75344a98cb3ed9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exclusionPatterns", value)

    @builtins.property
    @jsii.member(jsii_name="inclusionPatterns")
    def inclusion_patterns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "inclusionPatterns"))

    @inclusion_patterns.setter
    def inclusion_patterns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ac25a4b409f1a023345b9e9975a3e0d0e03e7446a10ae898e8be5d6eaa475ef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "inclusionPatterns", value)

    @builtins.property
    @jsii.member(jsii_name="inclusionPrefixes")
    def inclusion_prefixes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "inclusionPrefixes"))

    @inclusion_prefixes.setter
    def inclusion_prefixes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__651b60ee6ca573b83c8094ea457218613996447e3d5c4050f9bb7928231064eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "inclusionPrefixes", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KendraDataSourceConfigurationS3Configuration]:
        return typing.cast(typing.Optional[KendraDataSourceConfigurationS3Configuration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KendraDataSourceConfigurationS3Configuration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f07b052d201fc6ce5f489c16363379ea3e17d56191e8ef168406be03ace30074)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kendraDataSource.KendraDataSourceConfigurationWebCrawlerConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "urls": "urls",
        "authentication_configuration": "authenticationConfiguration",
        "crawl_depth": "crawlDepth",
        "max_content_size_per_page_in_mega_bytes": "maxContentSizePerPageInMegaBytes",
        "max_links_per_page": "maxLinksPerPage",
        "max_urls_per_minute_crawl_rate": "maxUrlsPerMinuteCrawlRate",
        "proxy_configuration": "proxyConfiguration",
        "url_exclusion_patterns": "urlExclusionPatterns",
        "url_inclusion_patterns": "urlInclusionPatterns",
    },
)
class KendraDataSourceConfigurationWebCrawlerConfiguration:
    def __init__(
        self,
        *,
        urls: typing.Union["KendraDataSourceConfigurationWebCrawlerConfigurationUrls", typing.Dict[builtins.str, typing.Any]],
        authentication_configuration: typing.Optional[typing.Union["KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        crawl_depth: typing.Optional[jsii.Number] = None,
        max_content_size_per_page_in_mega_bytes: typing.Optional[jsii.Number] = None,
        max_links_per_page: typing.Optional[jsii.Number] = None,
        max_urls_per_minute_crawl_rate: typing.Optional[jsii.Number] = None,
        proxy_configuration: typing.Optional[typing.Union["KendraDataSourceConfigurationWebCrawlerConfigurationProxyConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        url_exclusion_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
        url_inclusion_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param urls: urls block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#urls KendraDataSource#urls}
        :param authentication_configuration: authentication_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#authentication_configuration KendraDataSource#authentication_configuration}
        :param crawl_depth: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#crawl_depth KendraDataSource#crawl_depth}.
        :param max_content_size_per_page_in_mega_bytes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#max_content_size_per_page_in_mega_bytes KendraDataSource#max_content_size_per_page_in_mega_bytes}.
        :param max_links_per_page: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#max_links_per_page KendraDataSource#max_links_per_page}.
        :param max_urls_per_minute_crawl_rate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#max_urls_per_minute_crawl_rate KendraDataSource#max_urls_per_minute_crawl_rate}.
        :param proxy_configuration: proxy_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#proxy_configuration KendraDataSource#proxy_configuration}
        :param url_exclusion_patterns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#url_exclusion_patterns KendraDataSource#url_exclusion_patterns}.
        :param url_inclusion_patterns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#url_inclusion_patterns KendraDataSource#url_inclusion_patterns}.
        '''
        if isinstance(urls, dict):
            urls = KendraDataSourceConfigurationWebCrawlerConfigurationUrls(**urls)
        if isinstance(authentication_configuration, dict):
            authentication_configuration = KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfiguration(**authentication_configuration)
        if isinstance(proxy_configuration, dict):
            proxy_configuration = KendraDataSourceConfigurationWebCrawlerConfigurationProxyConfiguration(**proxy_configuration)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__88d9d4c6025ca3fea705401050fde4fb303518ad794ae4c3ad79712520c0b9bc)
            check_type(argname="argument urls", value=urls, expected_type=type_hints["urls"])
            check_type(argname="argument authentication_configuration", value=authentication_configuration, expected_type=type_hints["authentication_configuration"])
            check_type(argname="argument crawl_depth", value=crawl_depth, expected_type=type_hints["crawl_depth"])
            check_type(argname="argument max_content_size_per_page_in_mega_bytes", value=max_content_size_per_page_in_mega_bytes, expected_type=type_hints["max_content_size_per_page_in_mega_bytes"])
            check_type(argname="argument max_links_per_page", value=max_links_per_page, expected_type=type_hints["max_links_per_page"])
            check_type(argname="argument max_urls_per_minute_crawl_rate", value=max_urls_per_minute_crawl_rate, expected_type=type_hints["max_urls_per_minute_crawl_rate"])
            check_type(argname="argument proxy_configuration", value=proxy_configuration, expected_type=type_hints["proxy_configuration"])
            check_type(argname="argument url_exclusion_patterns", value=url_exclusion_patterns, expected_type=type_hints["url_exclusion_patterns"])
            check_type(argname="argument url_inclusion_patterns", value=url_inclusion_patterns, expected_type=type_hints["url_inclusion_patterns"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "urls": urls,
        }
        if authentication_configuration is not None:
            self._values["authentication_configuration"] = authentication_configuration
        if crawl_depth is not None:
            self._values["crawl_depth"] = crawl_depth
        if max_content_size_per_page_in_mega_bytes is not None:
            self._values["max_content_size_per_page_in_mega_bytes"] = max_content_size_per_page_in_mega_bytes
        if max_links_per_page is not None:
            self._values["max_links_per_page"] = max_links_per_page
        if max_urls_per_minute_crawl_rate is not None:
            self._values["max_urls_per_minute_crawl_rate"] = max_urls_per_minute_crawl_rate
        if proxy_configuration is not None:
            self._values["proxy_configuration"] = proxy_configuration
        if url_exclusion_patterns is not None:
            self._values["url_exclusion_patterns"] = url_exclusion_patterns
        if url_inclusion_patterns is not None:
            self._values["url_inclusion_patterns"] = url_inclusion_patterns

    @builtins.property
    def urls(self) -> "KendraDataSourceConfigurationWebCrawlerConfigurationUrls":
        '''urls block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#urls KendraDataSource#urls}
        '''
        result = self._values.get("urls")
        assert result is not None, "Required property 'urls' is missing"
        return typing.cast("KendraDataSourceConfigurationWebCrawlerConfigurationUrls", result)

    @builtins.property
    def authentication_configuration(
        self,
    ) -> typing.Optional["KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfiguration"]:
        '''authentication_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#authentication_configuration KendraDataSource#authentication_configuration}
        '''
        result = self._values.get("authentication_configuration")
        return typing.cast(typing.Optional["KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfiguration"], result)

    @builtins.property
    def crawl_depth(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#crawl_depth KendraDataSource#crawl_depth}.'''
        result = self._values.get("crawl_depth")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_content_size_per_page_in_mega_bytes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#max_content_size_per_page_in_mega_bytes KendraDataSource#max_content_size_per_page_in_mega_bytes}.'''
        result = self._values.get("max_content_size_per_page_in_mega_bytes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_links_per_page(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#max_links_per_page KendraDataSource#max_links_per_page}.'''
        result = self._values.get("max_links_per_page")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_urls_per_minute_crawl_rate(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#max_urls_per_minute_crawl_rate KendraDataSource#max_urls_per_minute_crawl_rate}.'''
        result = self._values.get("max_urls_per_minute_crawl_rate")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def proxy_configuration(
        self,
    ) -> typing.Optional["KendraDataSourceConfigurationWebCrawlerConfigurationProxyConfiguration"]:
        '''proxy_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#proxy_configuration KendraDataSource#proxy_configuration}
        '''
        result = self._values.get("proxy_configuration")
        return typing.cast(typing.Optional["KendraDataSourceConfigurationWebCrawlerConfigurationProxyConfiguration"], result)

    @builtins.property
    def url_exclusion_patterns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#url_exclusion_patterns KendraDataSource#url_exclusion_patterns}.'''
        result = self._values.get("url_exclusion_patterns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def url_inclusion_patterns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#url_inclusion_patterns KendraDataSource#url_inclusion_patterns}.'''
        result = self._values.get("url_inclusion_patterns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraDataSourceConfigurationWebCrawlerConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.kendraDataSource.KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfiguration",
    jsii_struct_bases=[],
    name_mapping={"basic_authentication": "basicAuthentication"},
)
class KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfiguration:
    def __init__(
        self,
        *,
        basic_authentication: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationBasicAuthentication", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param basic_authentication: basic_authentication block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#basic_authentication KendraDataSource#basic_authentication}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d112e3ad2e361321f376f608d168f91b16f0c5d5247dfb05bd10cbd886a363f9)
            check_type(argname="argument basic_authentication", value=basic_authentication, expected_type=type_hints["basic_authentication"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if basic_authentication is not None:
            self._values["basic_authentication"] = basic_authentication

    @builtins.property
    def basic_authentication(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationBasicAuthentication"]]]:
        '''basic_authentication block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#basic_authentication KendraDataSource#basic_authentication}
        '''
        result = self._values.get("basic_authentication")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationBasicAuthentication"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.kendraDataSource.KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationBasicAuthentication",
    jsii_struct_bases=[],
    name_mapping={"credentials": "credentials", "host": "host", "port": "port"},
)
class KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationBasicAuthentication:
    def __init__(
        self,
        *,
        credentials: builtins.str,
        host: builtins.str,
        port: jsii.Number,
    ) -> None:
        '''
        :param credentials: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#credentials KendraDataSource#credentials}.
        :param host: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#host KendraDataSource#host}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#port KendraDataSource#port}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c3e4ecc7ba273e89356c155547bff682c0315a940077dcfe89e6820f0a8288b)
            check_type(argname="argument credentials", value=credentials, expected_type=type_hints["credentials"])
            check_type(argname="argument host", value=host, expected_type=type_hints["host"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "credentials": credentials,
            "host": host,
            "port": port,
        }

    @builtins.property
    def credentials(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#credentials KendraDataSource#credentials}.'''
        result = self._values.get("credentials")
        assert result is not None, "Required property 'credentials' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def host(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#host KendraDataSource#host}.'''
        result = self._values.get("host")
        assert result is not None, "Required property 'host' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def port(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#port KendraDataSource#port}.'''
        result = self._values.get("port")
        assert result is not None, "Required property 'port' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationBasicAuthentication(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationBasicAuthenticationList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kendraDataSource.KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationBasicAuthenticationList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ead29c352f94497ea690ebc13efdce25297ca999506b375836eb44c0336d7de4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationBasicAuthenticationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb9163fcb9e7135c963f2437024ec13ed43cac3f7087421812d587e0b6187f25)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationBasicAuthenticationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61bd3c18e74cea20dc5e382600f449e4e647667f6972f6b3c6447ccbb9138783)
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
            type_hints = typing.get_type_hints(_typecheckingstub__729c11149a6d9c6d518c99a84f6d56ff177a8bf8b82fb398e9f1ef275dde520b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3da4d9b841da7ad76ae5d2ac1345c1ee337aef0f27138108ccef3a82ccadc8ff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationBasicAuthentication]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationBasicAuthentication]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationBasicAuthentication]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1e8c8d78d1ec402cfe572bb87db969873e2ddb442c49f9b69e2bfe820dbe284)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationBasicAuthenticationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kendraDataSource.KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationBasicAuthenticationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d7abc8f0d924d57833e508c59c14940f8d54dc30540bf5da7d94778be6ac4f0e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="credentialsInput")
    def credentials_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "credentialsInput"))

    @builtins.property
    @jsii.member(jsii_name="hostInput")
    def host_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="credentials")
    def credentials(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "credentials"))

    @credentials.setter
    def credentials(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92f2fd0e2b7d89087db40c55be42c4bc5efdbc3dce9ec40151106fdc7e269597)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "credentials", value)

    @builtins.property
    @jsii.member(jsii_name="host")
    def host(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "host"))

    @host.setter
    def host(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd3e1b2436a7ffc490cfcf5aca65da37cdb381ccacaa80378ceca1430f9bb151)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "host", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d8871fc58df39214e09c56322a7059200a0e1c610cf37f2411ead31d454de59)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationBasicAuthentication, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationBasicAuthentication, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationBasicAuthentication, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3604560a7ed2a53803c3f0abcb6fc6229822a67c4727c03f45b7be58706169b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kendraDataSource.KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0256de35f772eb4103dbda3b2c533c230edd0467ca8411da502e5df23e554b1a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putBasicAuthentication")
    def put_basic_authentication(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationBasicAuthentication, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c20a96b6e761237e8a773c0ef3d100c5345e8d04388b28c7837f87af6582504)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putBasicAuthentication", [value]))

    @jsii.member(jsii_name="resetBasicAuthentication")
    def reset_basic_authentication(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBasicAuthentication", []))

    @builtins.property
    @jsii.member(jsii_name="basicAuthentication")
    def basic_authentication(
        self,
    ) -> KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationBasicAuthenticationList:
        return typing.cast(KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationBasicAuthenticationList, jsii.get(self, "basicAuthentication"))

    @builtins.property
    @jsii.member(jsii_name="basicAuthenticationInput")
    def basic_authentication_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationBasicAuthentication]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationBasicAuthentication]]], jsii.get(self, "basicAuthenticationInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfiguration]:
        return typing.cast(typing.Optional[KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63e322859e79be33ae1b86c6e370fa6e05915accaf5e09a54c5d7608c35200fd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KendraDataSourceConfigurationWebCrawlerConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kendraDataSource.KendraDataSourceConfigurationWebCrawlerConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9aa2507809a2a1892273cb38e58ee107ac6b3fdf29d2c0298ceefcc3051f682a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAuthenticationConfiguration")
    def put_authentication_configuration(
        self,
        *,
        basic_authentication: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationBasicAuthentication, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param basic_authentication: basic_authentication block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#basic_authentication KendraDataSource#basic_authentication}
        '''
        value = KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfiguration(
            basic_authentication=basic_authentication
        )

        return typing.cast(None, jsii.invoke(self, "putAuthenticationConfiguration", [value]))

    @jsii.member(jsii_name="putProxyConfiguration")
    def put_proxy_configuration(
        self,
        *,
        host: builtins.str,
        port: jsii.Number,
        credentials: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param host: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#host KendraDataSource#host}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#port KendraDataSource#port}.
        :param credentials: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#credentials KendraDataSource#credentials}.
        '''
        value = KendraDataSourceConfigurationWebCrawlerConfigurationProxyConfiguration(
            host=host, port=port, credentials=credentials
        )

        return typing.cast(None, jsii.invoke(self, "putProxyConfiguration", [value]))

    @jsii.member(jsii_name="putUrls")
    def put_urls(
        self,
        *,
        seed_url_configuration: typing.Optional[typing.Union["KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSeedUrlConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        site_maps_configuration: typing.Optional[typing.Union["KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSiteMapsConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param seed_url_configuration: seed_url_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#seed_url_configuration KendraDataSource#seed_url_configuration}
        :param site_maps_configuration: site_maps_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#site_maps_configuration KendraDataSource#site_maps_configuration}
        '''
        value = KendraDataSourceConfigurationWebCrawlerConfigurationUrls(
            seed_url_configuration=seed_url_configuration,
            site_maps_configuration=site_maps_configuration,
        )

        return typing.cast(None, jsii.invoke(self, "putUrls", [value]))

    @jsii.member(jsii_name="resetAuthenticationConfiguration")
    def reset_authentication_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthenticationConfiguration", []))

    @jsii.member(jsii_name="resetCrawlDepth")
    def reset_crawl_depth(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCrawlDepth", []))

    @jsii.member(jsii_name="resetMaxContentSizePerPageInMegaBytes")
    def reset_max_content_size_per_page_in_mega_bytes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxContentSizePerPageInMegaBytes", []))

    @jsii.member(jsii_name="resetMaxLinksPerPage")
    def reset_max_links_per_page(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxLinksPerPage", []))

    @jsii.member(jsii_name="resetMaxUrlsPerMinuteCrawlRate")
    def reset_max_urls_per_minute_crawl_rate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxUrlsPerMinuteCrawlRate", []))

    @jsii.member(jsii_name="resetProxyConfiguration")
    def reset_proxy_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProxyConfiguration", []))

    @jsii.member(jsii_name="resetUrlExclusionPatterns")
    def reset_url_exclusion_patterns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUrlExclusionPatterns", []))

    @jsii.member(jsii_name="resetUrlInclusionPatterns")
    def reset_url_inclusion_patterns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUrlInclusionPatterns", []))

    @builtins.property
    @jsii.member(jsii_name="authenticationConfiguration")
    def authentication_configuration(
        self,
    ) -> KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationOutputReference:
        return typing.cast(KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationOutputReference, jsii.get(self, "authenticationConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="proxyConfiguration")
    def proxy_configuration(
        self,
    ) -> "KendraDataSourceConfigurationWebCrawlerConfigurationProxyConfigurationOutputReference":
        return typing.cast("KendraDataSourceConfigurationWebCrawlerConfigurationProxyConfigurationOutputReference", jsii.get(self, "proxyConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="urls")
    def urls(
        self,
    ) -> "KendraDataSourceConfigurationWebCrawlerConfigurationUrlsOutputReference":
        return typing.cast("KendraDataSourceConfigurationWebCrawlerConfigurationUrlsOutputReference", jsii.get(self, "urls"))

    @builtins.property
    @jsii.member(jsii_name="authenticationConfigurationInput")
    def authentication_configuration_input(
        self,
    ) -> typing.Optional[KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfiguration]:
        return typing.cast(typing.Optional[KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfiguration], jsii.get(self, "authenticationConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="crawlDepthInput")
    def crawl_depth_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "crawlDepthInput"))

    @builtins.property
    @jsii.member(jsii_name="maxContentSizePerPageInMegaBytesInput")
    def max_content_size_per_page_in_mega_bytes_input(
        self,
    ) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxContentSizePerPageInMegaBytesInput"))

    @builtins.property
    @jsii.member(jsii_name="maxLinksPerPageInput")
    def max_links_per_page_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxLinksPerPageInput"))

    @builtins.property
    @jsii.member(jsii_name="maxUrlsPerMinuteCrawlRateInput")
    def max_urls_per_minute_crawl_rate_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxUrlsPerMinuteCrawlRateInput"))

    @builtins.property
    @jsii.member(jsii_name="proxyConfigurationInput")
    def proxy_configuration_input(
        self,
    ) -> typing.Optional["KendraDataSourceConfigurationWebCrawlerConfigurationProxyConfiguration"]:
        return typing.cast(typing.Optional["KendraDataSourceConfigurationWebCrawlerConfigurationProxyConfiguration"], jsii.get(self, "proxyConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="urlExclusionPatternsInput")
    def url_exclusion_patterns_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "urlExclusionPatternsInput"))

    @builtins.property
    @jsii.member(jsii_name="urlInclusionPatternsInput")
    def url_inclusion_patterns_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "urlInclusionPatternsInput"))

    @builtins.property
    @jsii.member(jsii_name="urlsInput")
    def urls_input(
        self,
    ) -> typing.Optional["KendraDataSourceConfigurationWebCrawlerConfigurationUrls"]:
        return typing.cast(typing.Optional["KendraDataSourceConfigurationWebCrawlerConfigurationUrls"], jsii.get(self, "urlsInput"))

    @builtins.property
    @jsii.member(jsii_name="crawlDepth")
    def crawl_depth(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "crawlDepth"))

    @crawl_depth.setter
    def crawl_depth(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__061f17b8e671caca94ff0e1a36103b964514d4b25097a7f30f1ff050dda4d332)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "crawlDepth", value)

    @builtins.property
    @jsii.member(jsii_name="maxContentSizePerPageInMegaBytes")
    def max_content_size_per_page_in_mega_bytes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxContentSizePerPageInMegaBytes"))

    @max_content_size_per_page_in_mega_bytes.setter
    def max_content_size_per_page_in_mega_bytes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38288170f8e072d24f2362979b359135be48653a5c2e079137680872d92718bd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxContentSizePerPageInMegaBytes", value)

    @builtins.property
    @jsii.member(jsii_name="maxLinksPerPage")
    def max_links_per_page(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxLinksPerPage"))

    @max_links_per_page.setter
    def max_links_per_page(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a2ab3038e59aaf7ba74b72f620f801002b402ce82c98f65a4a5f89f76c1d015)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxLinksPerPage", value)

    @builtins.property
    @jsii.member(jsii_name="maxUrlsPerMinuteCrawlRate")
    def max_urls_per_minute_crawl_rate(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxUrlsPerMinuteCrawlRate"))

    @max_urls_per_minute_crawl_rate.setter
    def max_urls_per_minute_crawl_rate(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b72f71aed0387b5c23bb3c959a597b073baadeaf6f5a97345dba1db7e51b3ac1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxUrlsPerMinuteCrawlRate", value)

    @builtins.property
    @jsii.member(jsii_name="urlExclusionPatterns")
    def url_exclusion_patterns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "urlExclusionPatterns"))

    @url_exclusion_patterns.setter
    def url_exclusion_patterns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b010a8f1b96c8caef2f4f7e53fd097294f3ee793d1baea66340614de7bfe43d4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "urlExclusionPatterns", value)

    @builtins.property
    @jsii.member(jsii_name="urlInclusionPatterns")
    def url_inclusion_patterns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "urlInclusionPatterns"))

    @url_inclusion_patterns.setter
    def url_inclusion_patterns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b112a217ee69ef1946340ba1ee93932a51acc5e329de4e0db9eb52a1b3e7e3b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "urlInclusionPatterns", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KendraDataSourceConfigurationWebCrawlerConfiguration]:
        return typing.cast(typing.Optional[KendraDataSourceConfigurationWebCrawlerConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KendraDataSourceConfigurationWebCrawlerConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e82249e21ac04dc3f51d490f1b27d9e1b76281dd507079f0d039d556e695cee9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kendraDataSource.KendraDataSourceConfigurationWebCrawlerConfigurationProxyConfiguration",
    jsii_struct_bases=[],
    name_mapping={"host": "host", "port": "port", "credentials": "credentials"},
)
class KendraDataSourceConfigurationWebCrawlerConfigurationProxyConfiguration:
    def __init__(
        self,
        *,
        host: builtins.str,
        port: jsii.Number,
        credentials: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param host: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#host KendraDataSource#host}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#port KendraDataSource#port}.
        :param credentials: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#credentials KendraDataSource#credentials}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3de2a16c7e3edd16d8f7c03384f895efebf606d9e04de34825492e189ac4a98)
            check_type(argname="argument host", value=host, expected_type=type_hints["host"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument credentials", value=credentials, expected_type=type_hints["credentials"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "host": host,
            "port": port,
        }
        if credentials is not None:
            self._values["credentials"] = credentials

    @builtins.property
    def host(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#host KendraDataSource#host}.'''
        result = self._values.get("host")
        assert result is not None, "Required property 'host' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def port(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#port KendraDataSource#port}.'''
        result = self._values.get("port")
        assert result is not None, "Required property 'port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def credentials(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#credentials KendraDataSource#credentials}.'''
        result = self._values.get("credentials")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraDataSourceConfigurationWebCrawlerConfigurationProxyConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KendraDataSourceConfigurationWebCrawlerConfigurationProxyConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kendraDataSource.KendraDataSourceConfigurationWebCrawlerConfigurationProxyConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__38e9261de2852a82fff3fa371992876bd7261c37fd9a70c135e926db4dba5077)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCredentials")
    def reset_credentials(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCredentials", []))

    @builtins.property
    @jsii.member(jsii_name="credentialsInput")
    def credentials_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "credentialsInput"))

    @builtins.property
    @jsii.member(jsii_name="hostInput")
    def host_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="credentials")
    def credentials(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "credentials"))

    @credentials.setter
    def credentials(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9832e292f641a5ce97b40bb4f5b9dc55a5ae047f32ce5d76bd828e9bf21e7736)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "credentials", value)

    @builtins.property
    @jsii.member(jsii_name="host")
    def host(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "host"))

    @host.setter
    def host(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e324ddb6899df21974ac68e163c7a14e370814f35dfd6d2ee02afdab356fa605)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "host", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf3ce887ccde107584c92146150048214668cf33ab17ef28fe9a2e47b5c32b55)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KendraDataSourceConfigurationWebCrawlerConfigurationProxyConfiguration]:
        return typing.cast(typing.Optional[KendraDataSourceConfigurationWebCrawlerConfigurationProxyConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KendraDataSourceConfigurationWebCrawlerConfigurationProxyConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6335a511cb5d54b2ba1abbde3e6f101ea162d134705aaf49f5f05447407d7706)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kendraDataSource.KendraDataSourceConfigurationWebCrawlerConfigurationUrls",
    jsii_struct_bases=[],
    name_mapping={
        "seed_url_configuration": "seedUrlConfiguration",
        "site_maps_configuration": "siteMapsConfiguration",
    },
)
class KendraDataSourceConfigurationWebCrawlerConfigurationUrls:
    def __init__(
        self,
        *,
        seed_url_configuration: typing.Optional[typing.Union["KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSeedUrlConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        site_maps_configuration: typing.Optional[typing.Union["KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSiteMapsConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param seed_url_configuration: seed_url_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#seed_url_configuration KendraDataSource#seed_url_configuration}
        :param site_maps_configuration: site_maps_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#site_maps_configuration KendraDataSource#site_maps_configuration}
        '''
        if isinstance(seed_url_configuration, dict):
            seed_url_configuration = KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSeedUrlConfiguration(**seed_url_configuration)
        if isinstance(site_maps_configuration, dict):
            site_maps_configuration = KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSiteMapsConfiguration(**site_maps_configuration)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8258b03cfe10d579a5c41b92a4995ccbcf911eec78631468a47b6f72bbe3ca59)
            check_type(argname="argument seed_url_configuration", value=seed_url_configuration, expected_type=type_hints["seed_url_configuration"])
            check_type(argname="argument site_maps_configuration", value=site_maps_configuration, expected_type=type_hints["site_maps_configuration"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if seed_url_configuration is not None:
            self._values["seed_url_configuration"] = seed_url_configuration
        if site_maps_configuration is not None:
            self._values["site_maps_configuration"] = site_maps_configuration

    @builtins.property
    def seed_url_configuration(
        self,
    ) -> typing.Optional["KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSeedUrlConfiguration"]:
        '''seed_url_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#seed_url_configuration KendraDataSource#seed_url_configuration}
        '''
        result = self._values.get("seed_url_configuration")
        return typing.cast(typing.Optional["KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSeedUrlConfiguration"], result)

    @builtins.property
    def site_maps_configuration(
        self,
    ) -> typing.Optional["KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSiteMapsConfiguration"]:
        '''site_maps_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#site_maps_configuration KendraDataSource#site_maps_configuration}
        '''
        result = self._values.get("site_maps_configuration")
        return typing.cast(typing.Optional["KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSiteMapsConfiguration"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraDataSourceConfigurationWebCrawlerConfigurationUrls(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KendraDataSourceConfigurationWebCrawlerConfigurationUrlsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kendraDataSource.KendraDataSourceConfigurationWebCrawlerConfigurationUrlsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ec32ea3efdea05a022b3e6bae0e08ef0a38c76e4d0cc212ff1e95c1fa70ddc9f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putSeedUrlConfiguration")
    def put_seed_url_configuration(
        self,
        *,
        seed_urls: typing.Sequence[builtins.str],
        web_crawler_mode: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param seed_urls: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#seed_urls KendraDataSource#seed_urls}.
        :param web_crawler_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#web_crawler_mode KendraDataSource#web_crawler_mode}.
        '''
        value = KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSeedUrlConfiguration(
            seed_urls=seed_urls, web_crawler_mode=web_crawler_mode
        )

        return typing.cast(None, jsii.invoke(self, "putSeedUrlConfiguration", [value]))

    @jsii.member(jsii_name="putSiteMapsConfiguration")
    def put_site_maps_configuration(
        self,
        *,
        site_maps: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param site_maps: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#site_maps KendraDataSource#site_maps}.
        '''
        value = KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSiteMapsConfiguration(
            site_maps=site_maps
        )

        return typing.cast(None, jsii.invoke(self, "putSiteMapsConfiguration", [value]))

    @jsii.member(jsii_name="resetSeedUrlConfiguration")
    def reset_seed_url_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSeedUrlConfiguration", []))

    @jsii.member(jsii_name="resetSiteMapsConfiguration")
    def reset_site_maps_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSiteMapsConfiguration", []))

    @builtins.property
    @jsii.member(jsii_name="seedUrlConfiguration")
    def seed_url_configuration(
        self,
    ) -> "KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSeedUrlConfigurationOutputReference":
        return typing.cast("KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSeedUrlConfigurationOutputReference", jsii.get(self, "seedUrlConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="siteMapsConfiguration")
    def site_maps_configuration(
        self,
    ) -> "KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSiteMapsConfigurationOutputReference":
        return typing.cast("KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSiteMapsConfigurationOutputReference", jsii.get(self, "siteMapsConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="seedUrlConfigurationInput")
    def seed_url_configuration_input(
        self,
    ) -> typing.Optional["KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSeedUrlConfiguration"]:
        return typing.cast(typing.Optional["KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSeedUrlConfiguration"], jsii.get(self, "seedUrlConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="siteMapsConfigurationInput")
    def site_maps_configuration_input(
        self,
    ) -> typing.Optional["KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSiteMapsConfiguration"]:
        return typing.cast(typing.Optional["KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSiteMapsConfiguration"], jsii.get(self, "siteMapsConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KendraDataSourceConfigurationWebCrawlerConfigurationUrls]:
        return typing.cast(typing.Optional[KendraDataSourceConfigurationWebCrawlerConfigurationUrls], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KendraDataSourceConfigurationWebCrawlerConfigurationUrls],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3d26b96169a59ffd3973c08c1d20981d237a81a61cda9fbe4f2273dae3dcedf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kendraDataSource.KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSeedUrlConfiguration",
    jsii_struct_bases=[],
    name_mapping={"seed_urls": "seedUrls", "web_crawler_mode": "webCrawlerMode"},
)
class KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSeedUrlConfiguration:
    def __init__(
        self,
        *,
        seed_urls: typing.Sequence[builtins.str],
        web_crawler_mode: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param seed_urls: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#seed_urls KendraDataSource#seed_urls}.
        :param web_crawler_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#web_crawler_mode KendraDataSource#web_crawler_mode}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08afcde04375ec2878ca7327b46cb5555de55498abeb50ce14f94def0a97402d)
            check_type(argname="argument seed_urls", value=seed_urls, expected_type=type_hints["seed_urls"])
            check_type(argname="argument web_crawler_mode", value=web_crawler_mode, expected_type=type_hints["web_crawler_mode"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "seed_urls": seed_urls,
        }
        if web_crawler_mode is not None:
            self._values["web_crawler_mode"] = web_crawler_mode

    @builtins.property
    def seed_urls(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#seed_urls KendraDataSource#seed_urls}.'''
        result = self._values.get("seed_urls")
        assert result is not None, "Required property 'seed_urls' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def web_crawler_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#web_crawler_mode KendraDataSource#web_crawler_mode}.'''
        result = self._values.get("web_crawler_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSeedUrlConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSeedUrlConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kendraDataSource.KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSeedUrlConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b1462b655a166436e70c4ca329ef7a1d9d6ff724cb408eafd140f8d2d45c8aeb)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetWebCrawlerMode")
    def reset_web_crawler_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWebCrawlerMode", []))

    @builtins.property
    @jsii.member(jsii_name="seedUrlsInput")
    def seed_urls_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "seedUrlsInput"))

    @builtins.property
    @jsii.member(jsii_name="webCrawlerModeInput")
    def web_crawler_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "webCrawlerModeInput"))

    @builtins.property
    @jsii.member(jsii_name="seedUrls")
    def seed_urls(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "seedUrls"))

    @seed_urls.setter
    def seed_urls(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7a01e2aa6e08deb10e36323e17d8a55b629e65809c6c931e06ced3746b4b256)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "seedUrls", value)

    @builtins.property
    @jsii.member(jsii_name="webCrawlerMode")
    def web_crawler_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "webCrawlerMode"))

    @web_crawler_mode.setter
    def web_crawler_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4919fdc5c50f07fb4c51b1c5d4779d0522b00f781c83e587213e87ee6a5111e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "webCrawlerMode", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSeedUrlConfiguration]:
        return typing.cast(typing.Optional[KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSeedUrlConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSeedUrlConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__249cc540d39cfae626cce0064da2c0394752ddb13978e53a489ddb3eacc4c046)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kendraDataSource.KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSiteMapsConfiguration",
    jsii_struct_bases=[],
    name_mapping={"site_maps": "siteMaps"},
)
class KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSiteMapsConfiguration:
    def __init__(self, *, site_maps: typing.Sequence[builtins.str]) -> None:
        '''
        :param site_maps: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#site_maps KendraDataSource#site_maps}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d76a0e683633760867f4992099fff7eeb2dc9b89fa32439effd2290543e0fad)
            check_type(argname="argument site_maps", value=site_maps, expected_type=type_hints["site_maps"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "site_maps": site_maps,
        }

    @builtins.property
    def site_maps(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#site_maps KendraDataSource#site_maps}.'''
        result = self._values.get("site_maps")
        assert result is not None, "Required property 'site_maps' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSiteMapsConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSiteMapsConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kendraDataSource.KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSiteMapsConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4ad0e6e086f1860b32c319afe0b8e0ac60ec8d01c727c99c6d415d74023ffd0a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="siteMapsInput")
    def site_maps_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "siteMapsInput"))

    @builtins.property
    @jsii.member(jsii_name="siteMaps")
    def site_maps(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "siteMaps"))

    @site_maps.setter
    def site_maps(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ecdf20ce5c781957d0c057821aec5b10fe0ccd2a359d1cbf0dfa3aa90a6303ea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "siteMaps", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSiteMapsConfiguration]:
        return typing.cast(typing.Optional[KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSiteMapsConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSiteMapsConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8aac84ecd07d8f90d5c199982fff157ccde8fd7ff87caf237b13346de356e03a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kendraDataSource.KendraDataSourceCustomDocumentEnrichmentConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "inline_configurations": "inlineConfigurations",
        "post_extraction_hook_configuration": "postExtractionHookConfiguration",
        "pre_extraction_hook_configuration": "preExtractionHookConfiguration",
        "role_arn": "roleArn",
    },
)
class KendraDataSourceCustomDocumentEnrichmentConfiguration:
    def __init__(
        self,
        *,
        inline_configurations: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurations", typing.Dict[builtins.str, typing.Any]]]]] = None,
        post_extraction_hook_configuration: typing.Optional[typing.Union["KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        pre_extraction_hook_configuration: typing.Optional[typing.Union["KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        role_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param inline_configurations: inline_configurations block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#inline_configurations KendraDataSource#inline_configurations}
        :param post_extraction_hook_configuration: post_extraction_hook_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#post_extraction_hook_configuration KendraDataSource#post_extraction_hook_configuration}
        :param pre_extraction_hook_configuration: pre_extraction_hook_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#pre_extraction_hook_configuration KendraDataSource#pre_extraction_hook_configuration}
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#role_arn KendraDataSource#role_arn}.
        '''
        if isinstance(post_extraction_hook_configuration, dict):
            post_extraction_hook_configuration = KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfiguration(**post_extraction_hook_configuration)
        if isinstance(pre_extraction_hook_configuration, dict):
            pre_extraction_hook_configuration = KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfiguration(**pre_extraction_hook_configuration)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4307366fc5b9f720e9117582e2e37a3472b1121cc1331b4b6a45695a3f47ccd)
            check_type(argname="argument inline_configurations", value=inline_configurations, expected_type=type_hints["inline_configurations"])
            check_type(argname="argument post_extraction_hook_configuration", value=post_extraction_hook_configuration, expected_type=type_hints["post_extraction_hook_configuration"])
            check_type(argname="argument pre_extraction_hook_configuration", value=pre_extraction_hook_configuration, expected_type=type_hints["pre_extraction_hook_configuration"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if inline_configurations is not None:
            self._values["inline_configurations"] = inline_configurations
        if post_extraction_hook_configuration is not None:
            self._values["post_extraction_hook_configuration"] = post_extraction_hook_configuration
        if pre_extraction_hook_configuration is not None:
            self._values["pre_extraction_hook_configuration"] = pre_extraction_hook_configuration
        if role_arn is not None:
            self._values["role_arn"] = role_arn

    @builtins.property
    def inline_configurations(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurations"]]]:
        '''inline_configurations block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#inline_configurations KendraDataSource#inline_configurations}
        '''
        result = self._values.get("inline_configurations")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurations"]]], result)

    @builtins.property
    def post_extraction_hook_configuration(
        self,
    ) -> typing.Optional["KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfiguration"]:
        '''post_extraction_hook_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#post_extraction_hook_configuration KendraDataSource#post_extraction_hook_configuration}
        '''
        result = self._values.get("post_extraction_hook_configuration")
        return typing.cast(typing.Optional["KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfiguration"], result)

    @builtins.property
    def pre_extraction_hook_configuration(
        self,
    ) -> typing.Optional["KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfiguration"]:
        '''pre_extraction_hook_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#pre_extraction_hook_configuration KendraDataSource#pre_extraction_hook_configuration}
        '''
        result = self._values.get("pre_extraction_hook_configuration")
        return typing.cast(typing.Optional["KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfiguration"], result)

    @builtins.property
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#role_arn KendraDataSource#role_arn}.'''
        result = self._values.get("role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraDataSourceCustomDocumentEnrichmentConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.kendraDataSource.KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurations",
    jsii_struct_bases=[],
    name_mapping={
        "condition": "condition",
        "document_content_deletion": "documentContentDeletion",
        "target": "target",
    },
)
class KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurations:
    def __init__(
        self,
        *,
        condition: typing.Optional[typing.Union["KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsCondition", typing.Dict[builtins.str, typing.Any]]] = None,
        document_content_deletion: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        target: typing.Optional[typing.Union["KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTarget", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param condition: condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#condition KendraDataSource#condition}
        :param document_content_deletion: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#document_content_deletion KendraDataSource#document_content_deletion}.
        :param target: target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#target KendraDataSource#target}
        '''
        if isinstance(condition, dict):
            condition = KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsCondition(**condition)
        if isinstance(target, dict):
            target = KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTarget(**target)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a46c385ef0d708a5103352ba6fd83b619f0b98eab134e84f8a933c014ed2b4e9)
            check_type(argname="argument condition", value=condition, expected_type=type_hints["condition"])
            check_type(argname="argument document_content_deletion", value=document_content_deletion, expected_type=type_hints["document_content_deletion"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if condition is not None:
            self._values["condition"] = condition
        if document_content_deletion is not None:
            self._values["document_content_deletion"] = document_content_deletion
        if target is not None:
            self._values["target"] = target

    @builtins.property
    def condition(
        self,
    ) -> typing.Optional["KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsCondition"]:
        '''condition block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#condition KendraDataSource#condition}
        '''
        result = self._values.get("condition")
        return typing.cast(typing.Optional["KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsCondition"], result)

    @builtins.property
    def document_content_deletion(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#document_content_deletion KendraDataSource#document_content_deletion}.'''
        result = self._values.get("document_content_deletion")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def target(
        self,
    ) -> typing.Optional["KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTarget"]:
        '''target block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#target KendraDataSource#target}
        '''
        result = self._values.get("target")
        return typing.cast(typing.Optional["KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTarget"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurations(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.kendraDataSource.KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsCondition",
    jsii_struct_bases=[],
    name_mapping={
        "condition_document_attribute_key": "conditionDocumentAttributeKey",
        "operator": "operator",
        "condition_on_value": "conditionOnValue",
    },
)
class KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsCondition:
    def __init__(
        self,
        *,
        condition_document_attribute_key: builtins.str,
        operator: builtins.str,
        condition_on_value: typing.Optional[typing.Union["KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsConditionConditionOnValue", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param condition_document_attribute_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#condition_document_attribute_key KendraDataSource#condition_document_attribute_key}.
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#operator KendraDataSource#operator}.
        :param condition_on_value: condition_on_value block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#condition_on_value KendraDataSource#condition_on_value}
        '''
        if isinstance(condition_on_value, dict):
            condition_on_value = KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsConditionConditionOnValue(**condition_on_value)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee383b20a81fa94f80288cf156cff6c4a63c670b7a222c36ea7010452157228e)
            check_type(argname="argument condition_document_attribute_key", value=condition_document_attribute_key, expected_type=type_hints["condition_document_attribute_key"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument condition_on_value", value=condition_on_value, expected_type=type_hints["condition_on_value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "condition_document_attribute_key": condition_document_attribute_key,
            "operator": operator,
        }
        if condition_on_value is not None:
            self._values["condition_on_value"] = condition_on_value

    @builtins.property
    def condition_document_attribute_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#condition_document_attribute_key KendraDataSource#condition_document_attribute_key}.'''
        result = self._values.get("condition_document_attribute_key")
        assert result is not None, "Required property 'condition_document_attribute_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def operator(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#operator KendraDataSource#operator}.'''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def condition_on_value(
        self,
    ) -> typing.Optional["KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsConditionConditionOnValue"]:
        '''condition_on_value block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#condition_on_value KendraDataSource#condition_on_value}
        '''
        result = self._values.get("condition_on_value")
        return typing.cast(typing.Optional["KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsConditionConditionOnValue"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsCondition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.kendraDataSource.KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsConditionConditionOnValue",
    jsii_struct_bases=[],
    name_mapping={
        "date_value": "dateValue",
        "long_value": "longValue",
        "string_list_value": "stringListValue",
        "string_value": "stringValue",
    },
)
class KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsConditionConditionOnValue:
    def __init__(
        self,
        *,
        date_value: typing.Optional[builtins.str] = None,
        long_value: typing.Optional[jsii.Number] = None,
        string_list_value: typing.Optional[typing.Sequence[builtins.str]] = None,
        string_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param date_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#date_value KendraDataSource#date_value}.
        :param long_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#long_value KendraDataSource#long_value}.
        :param string_list_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#string_list_value KendraDataSource#string_list_value}.
        :param string_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#string_value KendraDataSource#string_value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8bcc5c631302e380b0ceb7172314316a5002a272dff82b14d8b7bbdeb313d53)
            check_type(argname="argument date_value", value=date_value, expected_type=type_hints["date_value"])
            check_type(argname="argument long_value", value=long_value, expected_type=type_hints["long_value"])
            check_type(argname="argument string_list_value", value=string_list_value, expected_type=type_hints["string_list_value"])
            check_type(argname="argument string_value", value=string_value, expected_type=type_hints["string_value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if date_value is not None:
            self._values["date_value"] = date_value
        if long_value is not None:
            self._values["long_value"] = long_value
        if string_list_value is not None:
            self._values["string_list_value"] = string_list_value
        if string_value is not None:
            self._values["string_value"] = string_value

    @builtins.property
    def date_value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#date_value KendraDataSource#date_value}.'''
        result = self._values.get("date_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def long_value(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#long_value KendraDataSource#long_value}.'''
        result = self._values.get("long_value")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def string_list_value(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#string_list_value KendraDataSource#string_list_value}.'''
        result = self._values.get("string_list_value")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def string_value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#string_value KendraDataSource#string_value}.'''
        result = self._values.get("string_value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsConditionConditionOnValue(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsConditionConditionOnValueOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kendraDataSource.KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsConditionConditionOnValueOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2bc74abd5191d10fa6ad5e6e4dcb25bb9893055478dd64c75afe2e0789d3029f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDateValue")
    def reset_date_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDateValue", []))

    @jsii.member(jsii_name="resetLongValue")
    def reset_long_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLongValue", []))

    @jsii.member(jsii_name="resetStringListValue")
    def reset_string_list_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStringListValue", []))

    @jsii.member(jsii_name="resetStringValue")
    def reset_string_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStringValue", []))

    @builtins.property
    @jsii.member(jsii_name="dateValueInput")
    def date_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dateValueInput"))

    @builtins.property
    @jsii.member(jsii_name="longValueInput")
    def long_value_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "longValueInput"))

    @builtins.property
    @jsii.member(jsii_name="stringListValueInput")
    def string_list_value_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "stringListValueInput"))

    @builtins.property
    @jsii.member(jsii_name="stringValueInput")
    def string_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stringValueInput"))

    @builtins.property
    @jsii.member(jsii_name="dateValue")
    def date_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dateValue"))

    @date_value.setter
    def date_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d310c4db32cf8b82de679700889d9d34de7bb0d310d2f2ba8905a2243582e81)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dateValue", value)

    @builtins.property
    @jsii.member(jsii_name="longValue")
    def long_value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "longValue"))

    @long_value.setter
    def long_value(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05e85bfdd1dc1efe6f35a8cc5a0f65bcfcb4ee2725c9998cd513e5d162d500f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "longValue", value)

    @builtins.property
    @jsii.member(jsii_name="stringListValue")
    def string_list_value(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "stringListValue"))

    @string_list_value.setter
    def string_list_value(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1dbb0e9ebd16e43de521763541d28b12579fa6bdb9f57ee477613c96354489cc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stringListValue", value)

    @builtins.property
    @jsii.member(jsii_name="stringValue")
    def string_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "stringValue"))

    @string_value.setter
    def string_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5dbf72d6400dad3142f7d545f1f633d1a7f8870dee9a83287d8d8dc905deb8c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stringValue", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsConditionConditionOnValue]:
        return typing.cast(typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsConditionConditionOnValue], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsConditionConditionOnValue],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__955f54c3e4c39fa5616560f82310b9c5b80ef2d88b705f74fd1aff640b40cd04)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsConditionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kendraDataSource.KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsConditionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5c0aa21b1e10ab5a1fe940519f0b1f1fa02517fa6e6ecd07b3a297c1caf79760)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putConditionOnValue")
    def put_condition_on_value(
        self,
        *,
        date_value: typing.Optional[builtins.str] = None,
        long_value: typing.Optional[jsii.Number] = None,
        string_list_value: typing.Optional[typing.Sequence[builtins.str]] = None,
        string_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param date_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#date_value KendraDataSource#date_value}.
        :param long_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#long_value KendraDataSource#long_value}.
        :param string_list_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#string_list_value KendraDataSource#string_list_value}.
        :param string_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#string_value KendraDataSource#string_value}.
        '''
        value = KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsConditionConditionOnValue(
            date_value=date_value,
            long_value=long_value,
            string_list_value=string_list_value,
            string_value=string_value,
        )

        return typing.cast(None, jsii.invoke(self, "putConditionOnValue", [value]))

    @jsii.member(jsii_name="resetConditionOnValue")
    def reset_condition_on_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConditionOnValue", []))

    @builtins.property
    @jsii.member(jsii_name="conditionOnValue")
    def condition_on_value(
        self,
    ) -> KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsConditionConditionOnValueOutputReference:
        return typing.cast(KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsConditionConditionOnValueOutputReference, jsii.get(self, "conditionOnValue"))

    @builtins.property
    @jsii.member(jsii_name="conditionDocumentAttributeKeyInput")
    def condition_document_attribute_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "conditionDocumentAttributeKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="conditionOnValueInput")
    def condition_on_value_input(
        self,
    ) -> typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsConditionConditionOnValue]:
        return typing.cast(typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsConditionConditionOnValue], jsii.get(self, "conditionOnValueInput"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="conditionDocumentAttributeKey")
    def condition_document_attribute_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "conditionDocumentAttributeKey"))

    @condition_document_attribute_key.setter
    def condition_document_attribute_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d9f50eaf9f5201323bee3fec48a7c383603dca6299bd44087438861881f4be1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "conditionDocumentAttributeKey", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57cdb94f3b4412ac46c8d35da3a17305cf202641e89c4b515c1ffe9b3b9569fa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsCondition]:
        return typing.cast(typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsCondition], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsCondition],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73842f950839dd64c923fce7fbe33be3dafed52631eff9f867a2b3fda85c5454)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kendraDataSource.KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__953db39616a86cac88e8d43ecf786b4999d4c8d1eb893a12f8f746b039be9934)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de658b4fbd1857272d7e28367782294b29c2ca3ec745ffd8840f346f69b78951)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85d149276a7139d587a632b003b559499d61d966ecb988a040a158dded781f03)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b6f62831534dba6c5caaa282a29b288ea43eb8f77fbbc1a6fda1418d900cc8e5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ad33accf57e856cea6bcb8ce170df9731c1d9f2d2510d0cdef658d3f577bb62d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurations]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurations]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurations]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f53ff39a3239e1eeea36f49fbd09aacea7dda81097ecd1750df3c3659112d566)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kendraDataSource.KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c55a747658710fc260894259e572107e1370d850d1c6859db9f48992b036b30b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putCondition")
    def put_condition(
        self,
        *,
        condition_document_attribute_key: builtins.str,
        operator: builtins.str,
        condition_on_value: typing.Optional[typing.Union[KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsConditionConditionOnValue, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param condition_document_attribute_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#condition_document_attribute_key KendraDataSource#condition_document_attribute_key}.
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#operator KendraDataSource#operator}.
        :param condition_on_value: condition_on_value block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#condition_on_value KendraDataSource#condition_on_value}
        '''
        value = KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsCondition(
            condition_document_attribute_key=condition_document_attribute_key,
            operator=operator,
            condition_on_value=condition_on_value,
        )

        return typing.cast(None, jsii.invoke(self, "putCondition", [value]))

    @jsii.member(jsii_name="putTarget")
    def put_target(
        self,
        *,
        target_document_attribute_key: typing.Optional[builtins.str] = None,
        target_document_attribute_value: typing.Optional[typing.Union["KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTargetTargetDocumentAttributeValue", typing.Dict[builtins.str, typing.Any]]] = None,
        target_document_attribute_value_deletion: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param target_document_attribute_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#target_document_attribute_key KendraDataSource#target_document_attribute_key}.
        :param target_document_attribute_value: target_document_attribute_value block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#target_document_attribute_value KendraDataSource#target_document_attribute_value}
        :param target_document_attribute_value_deletion: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#target_document_attribute_value_deletion KendraDataSource#target_document_attribute_value_deletion}.
        '''
        value = KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTarget(
            target_document_attribute_key=target_document_attribute_key,
            target_document_attribute_value=target_document_attribute_value,
            target_document_attribute_value_deletion=target_document_attribute_value_deletion,
        )

        return typing.cast(None, jsii.invoke(self, "putTarget", [value]))

    @jsii.member(jsii_name="resetCondition")
    def reset_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCondition", []))

    @jsii.member(jsii_name="resetDocumentContentDeletion")
    def reset_document_content_deletion(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDocumentContentDeletion", []))

    @jsii.member(jsii_name="resetTarget")
    def reset_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTarget", []))

    @builtins.property
    @jsii.member(jsii_name="condition")
    def condition(
        self,
    ) -> KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsConditionOutputReference:
        return typing.cast(KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsConditionOutputReference, jsii.get(self, "condition"))

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(
        self,
    ) -> "KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTargetOutputReference":
        return typing.cast("KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTargetOutputReference", jsii.get(self, "target"))

    @builtins.property
    @jsii.member(jsii_name="conditionInput")
    def condition_input(
        self,
    ) -> typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsCondition]:
        return typing.cast(typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsCondition], jsii.get(self, "conditionInput"))

    @builtins.property
    @jsii.member(jsii_name="documentContentDeletionInput")
    def document_content_deletion_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "documentContentDeletionInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(
        self,
    ) -> typing.Optional["KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTarget"]:
        return typing.cast(typing.Optional["KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTarget"], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="documentContentDeletion")
    def document_content_deletion(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "documentContentDeletion"))

    @document_content_deletion.setter
    def document_content_deletion(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b47f22de26d9e4a02a96d7eeab7d3786428b73462d5d5bab8a1821faabb1638)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "documentContentDeletion", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurations, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurations, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurations, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c48a9124b54739bd77169181e1c59f195e4f05361228ea98617eb64cbc5335b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kendraDataSource.KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTarget",
    jsii_struct_bases=[],
    name_mapping={
        "target_document_attribute_key": "targetDocumentAttributeKey",
        "target_document_attribute_value": "targetDocumentAttributeValue",
        "target_document_attribute_value_deletion": "targetDocumentAttributeValueDeletion",
    },
)
class KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTarget:
    def __init__(
        self,
        *,
        target_document_attribute_key: typing.Optional[builtins.str] = None,
        target_document_attribute_value: typing.Optional[typing.Union["KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTargetTargetDocumentAttributeValue", typing.Dict[builtins.str, typing.Any]]] = None,
        target_document_attribute_value_deletion: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param target_document_attribute_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#target_document_attribute_key KendraDataSource#target_document_attribute_key}.
        :param target_document_attribute_value: target_document_attribute_value block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#target_document_attribute_value KendraDataSource#target_document_attribute_value}
        :param target_document_attribute_value_deletion: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#target_document_attribute_value_deletion KendraDataSource#target_document_attribute_value_deletion}.
        '''
        if isinstance(target_document_attribute_value, dict):
            target_document_attribute_value = KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTargetTargetDocumentAttributeValue(**target_document_attribute_value)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42bfe2b46257544bd7e61c0d4486002ee235caf065b3e533d73a3a79e1057ed0)
            check_type(argname="argument target_document_attribute_key", value=target_document_attribute_key, expected_type=type_hints["target_document_attribute_key"])
            check_type(argname="argument target_document_attribute_value", value=target_document_attribute_value, expected_type=type_hints["target_document_attribute_value"])
            check_type(argname="argument target_document_attribute_value_deletion", value=target_document_attribute_value_deletion, expected_type=type_hints["target_document_attribute_value_deletion"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if target_document_attribute_key is not None:
            self._values["target_document_attribute_key"] = target_document_attribute_key
        if target_document_attribute_value is not None:
            self._values["target_document_attribute_value"] = target_document_attribute_value
        if target_document_attribute_value_deletion is not None:
            self._values["target_document_attribute_value_deletion"] = target_document_attribute_value_deletion

    @builtins.property
    def target_document_attribute_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#target_document_attribute_key KendraDataSource#target_document_attribute_key}.'''
        result = self._values.get("target_document_attribute_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_document_attribute_value(
        self,
    ) -> typing.Optional["KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTargetTargetDocumentAttributeValue"]:
        '''target_document_attribute_value block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#target_document_attribute_value KendraDataSource#target_document_attribute_value}
        '''
        result = self._values.get("target_document_attribute_value")
        return typing.cast(typing.Optional["KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTargetTargetDocumentAttributeValue"], result)

    @builtins.property
    def target_document_attribute_value_deletion(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#target_document_attribute_value_deletion KendraDataSource#target_document_attribute_value_deletion}.'''
        result = self._values.get("target_document_attribute_value_deletion")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTarget(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTargetOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kendraDataSource.KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTargetOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__23fa383178a69bceee66cade33b3be49ef0601437789b5d9877032807a4137ed)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putTargetDocumentAttributeValue")
    def put_target_document_attribute_value(
        self,
        *,
        date_value: typing.Optional[builtins.str] = None,
        long_value: typing.Optional[jsii.Number] = None,
        string_list_value: typing.Optional[typing.Sequence[builtins.str]] = None,
        string_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param date_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#date_value KendraDataSource#date_value}.
        :param long_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#long_value KendraDataSource#long_value}.
        :param string_list_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#string_list_value KendraDataSource#string_list_value}.
        :param string_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#string_value KendraDataSource#string_value}.
        '''
        value = KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTargetTargetDocumentAttributeValue(
            date_value=date_value,
            long_value=long_value,
            string_list_value=string_list_value,
            string_value=string_value,
        )

        return typing.cast(None, jsii.invoke(self, "putTargetDocumentAttributeValue", [value]))

    @jsii.member(jsii_name="resetTargetDocumentAttributeKey")
    def reset_target_document_attribute_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetDocumentAttributeKey", []))

    @jsii.member(jsii_name="resetTargetDocumentAttributeValue")
    def reset_target_document_attribute_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetDocumentAttributeValue", []))

    @jsii.member(jsii_name="resetTargetDocumentAttributeValueDeletion")
    def reset_target_document_attribute_value_deletion(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetDocumentAttributeValueDeletion", []))

    @builtins.property
    @jsii.member(jsii_name="targetDocumentAttributeValue")
    def target_document_attribute_value(
        self,
    ) -> "KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTargetTargetDocumentAttributeValueOutputReference":
        return typing.cast("KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTargetTargetDocumentAttributeValueOutputReference", jsii.get(self, "targetDocumentAttributeValue"))

    @builtins.property
    @jsii.member(jsii_name="targetDocumentAttributeKeyInput")
    def target_document_attribute_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetDocumentAttributeKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="targetDocumentAttributeValueDeletionInput")
    def target_document_attribute_value_deletion_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "targetDocumentAttributeValueDeletionInput"))

    @builtins.property
    @jsii.member(jsii_name="targetDocumentAttributeValueInput")
    def target_document_attribute_value_input(
        self,
    ) -> typing.Optional["KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTargetTargetDocumentAttributeValue"]:
        return typing.cast(typing.Optional["KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTargetTargetDocumentAttributeValue"], jsii.get(self, "targetDocumentAttributeValueInput"))

    @builtins.property
    @jsii.member(jsii_name="targetDocumentAttributeKey")
    def target_document_attribute_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetDocumentAttributeKey"))

    @target_document_attribute_key.setter
    def target_document_attribute_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__040e8e8ab7e7636619844a5929e034e1f03f36a0fd4de1bd3f84d75789d76e7c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetDocumentAttributeKey", value)

    @builtins.property
    @jsii.member(jsii_name="targetDocumentAttributeValueDeletion")
    def target_document_attribute_value_deletion(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "targetDocumentAttributeValueDeletion"))

    @target_document_attribute_value_deletion.setter
    def target_document_attribute_value_deletion(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa028a1b195b2b0371aff214a9f1b1050273a5f1bef4fc0d1a11418a8410439b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetDocumentAttributeValueDeletion", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTarget]:
        return typing.cast(typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTarget], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTarget],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a964d5b7e5de37b447a1969b3e40b16adae03f44a83a96ed71346f0983c5f134)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kendraDataSource.KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTargetTargetDocumentAttributeValue",
    jsii_struct_bases=[],
    name_mapping={
        "date_value": "dateValue",
        "long_value": "longValue",
        "string_list_value": "stringListValue",
        "string_value": "stringValue",
    },
)
class KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTargetTargetDocumentAttributeValue:
    def __init__(
        self,
        *,
        date_value: typing.Optional[builtins.str] = None,
        long_value: typing.Optional[jsii.Number] = None,
        string_list_value: typing.Optional[typing.Sequence[builtins.str]] = None,
        string_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param date_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#date_value KendraDataSource#date_value}.
        :param long_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#long_value KendraDataSource#long_value}.
        :param string_list_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#string_list_value KendraDataSource#string_list_value}.
        :param string_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#string_value KendraDataSource#string_value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__962670366b83baa2432389879618b05cc3372c83d0d42a5ad80ba7afdccb3d26)
            check_type(argname="argument date_value", value=date_value, expected_type=type_hints["date_value"])
            check_type(argname="argument long_value", value=long_value, expected_type=type_hints["long_value"])
            check_type(argname="argument string_list_value", value=string_list_value, expected_type=type_hints["string_list_value"])
            check_type(argname="argument string_value", value=string_value, expected_type=type_hints["string_value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if date_value is not None:
            self._values["date_value"] = date_value
        if long_value is not None:
            self._values["long_value"] = long_value
        if string_list_value is not None:
            self._values["string_list_value"] = string_list_value
        if string_value is not None:
            self._values["string_value"] = string_value

    @builtins.property
    def date_value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#date_value KendraDataSource#date_value}.'''
        result = self._values.get("date_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def long_value(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#long_value KendraDataSource#long_value}.'''
        result = self._values.get("long_value")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def string_list_value(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#string_list_value KendraDataSource#string_list_value}.'''
        result = self._values.get("string_list_value")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def string_value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#string_value KendraDataSource#string_value}.'''
        result = self._values.get("string_value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTargetTargetDocumentAttributeValue(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTargetTargetDocumentAttributeValueOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kendraDataSource.KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTargetTargetDocumentAttributeValueOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2ca5af3a8e68cff6f5947214ead9088f252c363ebc773ec172d102c6906b4966)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDateValue")
    def reset_date_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDateValue", []))

    @jsii.member(jsii_name="resetLongValue")
    def reset_long_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLongValue", []))

    @jsii.member(jsii_name="resetStringListValue")
    def reset_string_list_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStringListValue", []))

    @jsii.member(jsii_name="resetStringValue")
    def reset_string_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStringValue", []))

    @builtins.property
    @jsii.member(jsii_name="dateValueInput")
    def date_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dateValueInput"))

    @builtins.property
    @jsii.member(jsii_name="longValueInput")
    def long_value_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "longValueInput"))

    @builtins.property
    @jsii.member(jsii_name="stringListValueInput")
    def string_list_value_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "stringListValueInput"))

    @builtins.property
    @jsii.member(jsii_name="stringValueInput")
    def string_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stringValueInput"))

    @builtins.property
    @jsii.member(jsii_name="dateValue")
    def date_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dateValue"))

    @date_value.setter
    def date_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1619e0f85b374173724e7fd79e37cbbc49566b6119278830367f86520fb9c25)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dateValue", value)

    @builtins.property
    @jsii.member(jsii_name="longValue")
    def long_value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "longValue"))

    @long_value.setter
    def long_value(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9cfb464ef9c3a19916fde2156b645b5d1df1830e1ff7d676653693b4ad80b284)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "longValue", value)

    @builtins.property
    @jsii.member(jsii_name="stringListValue")
    def string_list_value(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "stringListValue"))

    @string_list_value.setter
    def string_list_value(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__758db9d7302917588dadc56415a9acf109b7200419185f6bff20330b1ac2d8c8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stringListValue", value)

    @builtins.property
    @jsii.member(jsii_name="stringValue")
    def string_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "stringValue"))

    @string_value.setter
    def string_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f034b3d0f4f0ba915d896f5358478e6081134b12b1f7e7d13810ed90e89cf92)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stringValue", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTargetTargetDocumentAttributeValue]:
        return typing.cast(typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTargetTargetDocumentAttributeValue], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTargetTargetDocumentAttributeValue],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1ca7008a24714f2adf809193d7712a58ea96933af81d9cc273ce92dd72d9bef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KendraDataSourceCustomDocumentEnrichmentConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kendraDataSource.KendraDataSourceCustomDocumentEnrichmentConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b53abbaf97a1b00b60dc4f063ff5b904fc8d8e5f8fc9c09ffe724c7ba9f76fce)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putInlineConfigurations")
    def put_inline_configurations(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurations, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cbacd3409d6c1687f0936c3f1d7d34447fddc158d4857dd09bc66a3778447721)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putInlineConfigurations", [value]))

    @jsii.member(jsii_name="putPostExtractionHookConfiguration")
    def put_post_extraction_hook_configuration(
        self,
        *,
        lambda_arn: builtins.str,
        s3_bucket: builtins.str,
        invocation_condition: typing.Optional[typing.Union["KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationCondition", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param lambda_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#lambda_arn KendraDataSource#lambda_arn}.
        :param s3_bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#s3_bucket KendraDataSource#s3_bucket}.
        :param invocation_condition: invocation_condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#invocation_condition KendraDataSource#invocation_condition}
        '''
        value = KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfiguration(
            lambda_arn=lambda_arn,
            s3_bucket=s3_bucket,
            invocation_condition=invocation_condition,
        )

        return typing.cast(None, jsii.invoke(self, "putPostExtractionHookConfiguration", [value]))

    @jsii.member(jsii_name="putPreExtractionHookConfiguration")
    def put_pre_extraction_hook_configuration(
        self,
        *,
        lambda_arn: builtins.str,
        s3_bucket: builtins.str,
        invocation_condition: typing.Optional[typing.Union["KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationCondition", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param lambda_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#lambda_arn KendraDataSource#lambda_arn}.
        :param s3_bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#s3_bucket KendraDataSource#s3_bucket}.
        :param invocation_condition: invocation_condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#invocation_condition KendraDataSource#invocation_condition}
        '''
        value = KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfiguration(
            lambda_arn=lambda_arn,
            s3_bucket=s3_bucket,
            invocation_condition=invocation_condition,
        )

        return typing.cast(None, jsii.invoke(self, "putPreExtractionHookConfiguration", [value]))

    @jsii.member(jsii_name="resetInlineConfigurations")
    def reset_inline_configurations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInlineConfigurations", []))

    @jsii.member(jsii_name="resetPostExtractionHookConfiguration")
    def reset_post_extraction_hook_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPostExtractionHookConfiguration", []))

    @jsii.member(jsii_name="resetPreExtractionHookConfiguration")
    def reset_pre_extraction_hook_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreExtractionHookConfiguration", []))

    @jsii.member(jsii_name="resetRoleArn")
    def reset_role_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRoleArn", []))

    @builtins.property
    @jsii.member(jsii_name="inlineConfigurations")
    def inline_configurations(
        self,
    ) -> KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsList:
        return typing.cast(KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsList, jsii.get(self, "inlineConfigurations"))

    @builtins.property
    @jsii.member(jsii_name="postExtractionHookConfiguration")
    def post_extraction_hook_configuration(
        self,
    ) -> "KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationOutputReference":
        return typing.cast("KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationOutputReference", jsii.get(self, "postExtractionHookConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="preExtractionHookConfiguration")
    def pre_extraction_hook_configuration(
        self,
    ) -> "KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationOutputReference":
        return typing.cast("KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationOutputReference", jsii.get(self, "preExtractionHookConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="inlineConfigurationsInput")
    def inline_configurations_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurations]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurations]]], jsii.get(self, "inlineConfigurationsInput"))

    @builtins.property
    @jsii.member(jsii_name="postExtractionHookConfigurationInput")
    def post_extraction_hook_configuration_input(
        self,
    ) -> typing.Optional["KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfiguration"]:
        return typing.cast(typing.Optional["KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfiguration"], jsii.get(self, "postExtractionHookConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="preExtractionHookConfigurationInput")
    def pre_extraction_hook_configuration_input(
        self,
    ) -> typing.Optional["KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfiguration"]:
        return typing.cast(typing.Optional["KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfiguration"], jsii.get(self, "preExtractionHookConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c4aa40913db25750a3a0873f4d42d4df4de8be5edab9235d3f802af2f6a8289)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfiguration]:
        return typing.cast(typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ebdef59af62b06304d2f9bd34eab743dc5b096e4a65dec00491c35835fa30d6e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kendraDataSource.KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "lambda_arn": "lambdaArn",
        "s3_bucket": "s3Bucket",
        "invocation_condition": "invocationCondition",
    },
)
class KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfiguration:
    def __init__(
        self,
        *,
        lambda_arn: builtins.str,
        s3_bucket: builtins.str,
        invocation_condition: typing.Optional[typing.Union["KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationCondition", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param lambda_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#lambda_arn KendraDataSource#lambda_arn}.
        :param s3_bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#s3_bucket KendraDataSource#s3_bucket}.
        :param invocation_condition: invocation_condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#invocation_condition KendraDataSource#invocation_condition}
        '''
        if isinstance(invocation_condition, dict):
            invocation_condition = KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationCondition(**invocation_condition)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b9958b42f8fe2b466d7c3a6c1f915ab3642c0bb3e4b2d4bca852deccfd4eb0e0)
            check_type(argname="argument lambda_arn", value=lambda_arn, expected_type=type_hints["lambda_arn"])
            check_type(argname="argument s3_bucket", value=s3_bucket, expected_type=type_hints["s3_bucket"])
            check_type(argname="argument invocation_condition", value=invocation_condition, expected_type=type_hints["invocation_condition"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "lambda_arn": lambda_arn,
            "s3_bucket": s3_bucket,
        }
        if invocation_condition is not None:
            self._values["invocation_condition"] = invocation_condition

    @builtins.property
    def lambda_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#lambda_arn KendraDataSource#lambda_arn}.'''
        result = self._values.get("lambda_arn")
        assert result is not None, "Required property 'lambda_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def s3_bucket(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#s3_bucket KendraDataSource#s3_bucket}.'''
        result = self._values.get("s3_bucket")
        assert result is not None, "Required property 's3_bucket' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def invocation_condition(
        self,
    ) -> typing.Optional["KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationCondition"]:
        '''invocation_condition block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#invocation_condition KendraDataSource#invocation_condition}
        '''
        result = self._values.get("invocation_condition")
        return typing.cast(typing.Optional["KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationCondition"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.kendraDataSource.KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationCondition",
    jsii_struct_bases=[],
    name_mapping={
        "condition_document_attribute_key": "conditionDocumentAttributeKey",
        "operator": "operator",
        "condition_on_value": "conditionOnValue",
    },
)
class KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationCondition:
    def __init__(
        self,
        *,
        condition_document_attribute_key: builtins.str,
        operator: builtins.str,
        condition_on_value: typing.Optional[typing.Union["KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationConditionConditionOnValue", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param condition_document_attribute_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#condition_document_attribute_key KendraDataSource#condition_document_attribute_key}.
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#operator KendraDataSource#operator}.
        :param condition_on_value: condition_on_value block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#condition_on_value KendraDataSource#condition_on_value}
        '''
        if isinstance(condition_on_value, dict):
            condition_on_value = KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationConditionConditionOnValue(**condition_on_value)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__905be7243de550df7ccb4d71797e1a846a7d660edd009d6006a2cf3a2c568b42)
            check_type(argname="argument condition_document_attribute_key", value=condition_document_attribute_key, expected_type=type_hints["condition_document_attribute_key"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument condition_on_value", value=condition_on_value, expected_type=type_hints["condition_on_value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "condition_document_attribute_key": condition_document_attribute_key,
            "operator": operator,
        }
        if condition_on_value is not None:
            self._values["condition_on_value"] = condition_on_value

    @builtins.property
    def condition_document_attribute_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#condition_document_attribute_key KendraDataSource#condition_document_attribute_key}.'''
        result = self._values.get("condition_document_attribute_key")
        assert result is not None, "Required property 'condition_document_attribute_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def operator(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#operator KendraDataSource#operator}.'''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def condition_on_value(
        self,
    ) -> typing.Optional["KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationConditionConditionOnValue"]:
        '''condition_on_value block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#condition_on_value KendraDataSource#condition_on_value}
        '''
        result = self._values.get("condition_on_value")
        return typing.cast(typing.Optional["KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationConditionConditionOnValue"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationCondition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.kendraDataSource.KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationConditionConditionOnValue",
    jsii_struct_bases=[],
    name_mapping={
        "date_value": "dateValue",
        "long_value": "longValue",
        "string_list_value": "stringListValue",
        "string_value": "stringValue",
    },
)
class KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationConditionConditionOnValue:
    def __init__(
        self,
        *,
        date_value: typing.Optional[builtins.str] = None,
        long_value: typing.Optional[jsii.Number] = None,
        string_list_value: typing.Optional[typing.Sequence[builtins.str]] = None,
        string_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param date_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#date_value KendraDataSource#date_value}.
        :param long_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#long_value KendraDataSource#long_value}.
        :param string_list_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#string_list_value KendraDataSource#string_list_value}.
        :param string_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#string_value KendraDataSource#string_value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da099e5f694596908f0c73f3b94256abdb0cfbc1d60db529c4b4f2407f7bea8f)
            check_type(argname="argument date_value", value=date_value, expected_type=type_hints["date_value"])
            check_type(argname="argument long_value", value=long_value, expected_type=type_hints["long_value"])
            check_type(argname="argument string_list_value", value=string_list_value, expected_type=type_hints["string_list_value"])
            check_type(argname="argument string_value", value=string_value, expected_type=type_hints["string_value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if date_value is not None:
            self._values["date_value"] = date_value
        if long_value is not None:
            self._values["long_value"] = long_value
        if string_list_value is not None:
            self._values["string_list_value"] = string_list_value
        if string_value is not None:
            self._values["string_value"] = string_value

    @builtins.property
    def date_value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#date_value KendraDataSource#date_value}.'''
        result = self._values.get("date_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def long_value(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#long_value KendraDataSource#long_value}.'''
        result = self._values.get("long_value")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def string_list_value(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#string_list_value KendraDataSource#string_list_value}.'''
        result = self._values.get("string_list_value")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def string_value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#string_value KendraDataSource#string_value}.'''
        result = self._values.get("string_value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationConditionConditionOnValue(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationConditionConditionOnValueOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kendraDataSource.KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationConditionConditionOnValueOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9c9159d5d09ee9e3db2718d834313e23791884e2ff1ccde5bc6ef40357f8f4fb)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDateValue")
    def reset_date_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDateValue", []))

    @jsii.member(jsii_name="resetLongValue")
    def reset_long_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLongValue", []))

    @jsii.member(jsii_name="resetStringListValue")
    def reset_string_list_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStringListValue", []))

    @jsii.member(jsii_name="resetStringValue")
    def reset_string_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStringValue", []))

    @builtins.property
    @jsii.member(jsii_name="dateValueInput")
    def date_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dateValueInput"))

    @builtins.property
    @jsii.member(jsii_name="longValueInput")
    def long_value_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "longValueInput"))

    @builtins.property
    @jsii.member(jsii_name="stringListValueInput")
    def string_list_value_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "stringListValueInput"))

    @builtins.property
    @jsii.member(jsii_name="stringValueInput")
    def string_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stringValueInput"))

    @builtins.property
    @jsii.member(jsii_name="dateValue")
    def date_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dateValue"))

    @date_value.setter
    def date_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b9385921bec85623014d56a0f5436f713822ac4cc4d9bf85d653a372d7a6bf36)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dateValue", value)

    @builtins.property
    @jsii.member(jsii_name="longValue")
    def long_value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "longValue"))

    @long_value.setter
    def long_value(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7ba1b5beaf7b25ed1bd65878c8c73c9c09fb9883acc85328f582a693c9182ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "longValue", value)

    @builtins.property
    @jsii.member(jsii_name="stringListValue")
    def string_list_value(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "stringListValue"))

    @string_list_value.setter
    def string_list_value(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bea45efaeef769c8228544ce43e0a2fb01d6a165502351ead6a0179fc8647513)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stringListValue", value)

    @builtins.property
    @jsii.member(jsii_name="stringValue")
    def string_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "stringValue"))

    @string_value.setter
    def string_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bbf02254113cfb425b7d8ab8bcdb11535d19ab3a2f08bedce58d8de8f0e2f22b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stringValue", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationConditionConditionOnValue]:
        return typing.cast(typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationConditionConditionOnValue], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationConditionConditionOnValue],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e234c3abd950a1e25f2c012a95a5f8020f59aacea7978ffe18732493a7c4030)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationConditionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kendraDataSource.KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationConditionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__58e074cc0e614248dc209af194b02d0643fdd6719e6f42376572ad07d5ab24c5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putConditionOnValue")
    def put_condition_on_value(
        self,
        *,
        date_value: typing.Optional[builtins.str] = None,
        long_value: typing.Optional[jsii.Number] = None,
        string_list_value: typing.Optional[typing.Sequence[builtins.str]] = None,
        string_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param date_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#date_value KendraDataSource#date_value}.
        :param long_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#long_value KendraDataSource#long_value}.
        :param string_list_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#string_list_value KendraDataSource#string_list_value}.
        :param string_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#string_value KendraDataSource#string_value}.
        '''
        value = KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationConditionConditionOnValue(
            date_value=date_value,
            long_value=long_value,
            string_list_value=string_list_value,
            string_value=string_value,
        )

        return typing.cast(None, jsii.invoke(self, "putConditionOnValue", [value]))

    @jsii.member(jsii_name="resetConditionOnValue")
    def reset_condition_on_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConditionOnValue", []))

    @builtins.property
    @jsii.member(jsii_name="conditionOnValue")
    def condition_on_value(
        self,
    ) -> KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationConditionConditionOnValueOutputReference:
        return typing.cast(KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationConditionConditionOnValueOutputReference, jsii.get(self, "conditionOnValue"))

    @builtins.property
    @jsii.member(jsii_name="conditionDocumentAttributeKeyInput")
    def condition_document_attribute_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "conditionDocumentAttributeKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="conditionOnValueInput")
    def condition_on_value_input(
        self,
    ) -> typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationConditionConditionOnValue]:
        return typing.cast(typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationConditionConditionOnValue], jsii.get(self, "conditionOnValueInput"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="conditionDocumentAttributeKey")
    def condition_document_attribute_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "conditionDocumentAttributeKey"))

    @condition_document_attribute_key.setter
    def condition_document_attribute_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54ca29e8a13f9aaaebbe9bb62712b5fd7e0108248086a4352049fd322c11da5a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "conditionDocumentAttributeKey", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5032a49064101c5a3679293b8dbb25d5de252c28fe485886e8ecfdb7ee7bd9ea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationCondition]:
        return typing.cast(typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationCondition], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationCondition],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__249f70da9f2ca4ac619c2be25d8e0154bbc15da43c807602af21235f99eee929)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kendraDataSource.KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__00f9a72486d1b43c019352267ff06cf70169341883064a129970807deb7df194)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putInvocationCondition")
    def put_invocation_condition(
        self,
        *,
        condition_document_attribute_key: builtins.str,
        operator: builtins.str,
        condition_on_value: typing.Optional[typing.Union[KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationConditionConditionOnValue, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param condition_document_attribute_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#condition_document_attribute_key KendraDataSource#condition_document_attribute_key}.
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#operator KendraDataSource#operator}.
        :param condition_on_value: condition_on_value block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#condition_on_value KendraDataSource#condition_on_value}
        '''
        value = KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationCondition(
            condition_document_attribute_key=condition_document_attribute_key,
            operator=operator,
            condition_on_value=condition_on_value,
        )

        return typing.cast(None, jsii.invoke(self, "putInvocationCondition", [value]))

    @jsii.member(jsii_name="resetInvocationCondition")
    def reset_invocation_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInvocationCondition", []))

    @builtins.property
    @jsii.member(jsii_name="invocationCondition")
    def invocation_condition(
        self,
    ) -> KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationConditionOutputReference:
        return typing.cast(KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationConditionOutputReference, jsii.get(self, "invocationCondition"))

    @builtins.property
    @jsii.member(jsii_name="invocationConditionInput")
    def invocation_condition_input(
        self,
    ) -> typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationCondition]:
        return typing.cast(typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationCondition], jsii.get(self, "invocationConditionInput"))

    @builtins.property
    @jsii.member(jsii_name="lambdaArnInput")
    def lambda_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lambdaArnInput"))

    @builtins.property
    @jsii.member(jsii_name="s3BucketInput")
    def s3_bucket_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "s3BucketInput"))

    @builtins.property
    @jsii.member(jsii_name="lambdaArn")
    def lambda_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lambdaArn"))

    @lambda_arn.setter
    def lambda_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__846c546b82870ce6f95ea638c43ba1e5db293daf1b212bea9ec3a4096308f5b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lambdaArn", value)

    @builtins.property
    @jsii.member(jsii_name="s3Bucket")
    def s3_bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "s3Bucket"))

    @s3_bucket.setter
    def s3_bucket(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a0f7a74085af81d9a33f81738e374c36ebb9468de2d5a8e85a78968435ca634)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3Bucket", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfiguration]:
        return typing.cast(typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a9148cdb4fbf4340169b40618f1e3d715a97deb0385b01fadcfd4c68242d2c8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kendraDataSource.KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "lambda_arn": "lambdaArn",
        "s3_bucket": "s3Bucket",
        "invocation_condition": "invocationCondition",
    },
)
class KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfiguration:
    def __init__(
        self,
        *,
        lambda_arn: builtins.str,
        s3_bucket: builtins.str,
        invocation_condition: typing.Optional[typing.Union["KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationCondition", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param lambda_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#lambda_arn KendraDataSource#lambda_arn}.
        :param s3_bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#s3_bucket KendraDataSource#s3_bucket}.
        :param invocation_condition: invocation_condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#invocation_condition KendraDataSource#invocation_condition}
        '''
        if isinstance(invocation_condition, dict):
            invocation_condition = KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationCondition(**invocation_condition)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__332f4e83e9b9d35eddf5602e47f1344c79efe7fc7889fbe89a8862d27e02dfc2)
            check_type(argname="argument lambda_arn", value=lambda_arn, expected_type=type_hints["lambda_arn"])
            check_type(argname="argument s3_bucket", value=s3_bucket, expected_type=type_hints["s3_bucket"])
            check_type(argname="argument invocation_condition", value=invocation_condition, expected_type=type_hints["invocation_condition"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "lambda_arn": lambda_arn,
            "s3_bucket": s3_bucket,
        }
        if invocation_condition is not None:
            self._values["invocation_condition"] = invocation_condition

    @builtins.property
    def lambda_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#lambda_arn KendraDataSource#lambda_arn}.'''
        result = self._values.get("lambda_arn")
        assert result is not None, "Required property 'lambda_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def s3_bucket(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#s3_bucket KendraDataSource#s3_bucket}.'''
        result = self._values.get("s3_bucket")
        assert result is not None, "Required property 's3_bucket' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def invocation_condition(
        self,
    ) -> typing.Optional["KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationCondition"]:
        '''invocation_condition block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#invocation_condition KendraDataSource#invocation_condition}
        '''
        result = self._values.get("invocation_condition")
        return typing.cast(typing.Optional["KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationCondition"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.kendraDataSource.KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationCondition",
    jsii_struct_bases=[],
    name_mapping={
        "condition_document_attribute_key": "conditionDocumentAttributeKey",
        "operator": "operator",
        "condition_on_value": "conditionOnValue",
    },
)
class KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationCondition:
    def __init__(
        self,
        *,
        condition_document_attribute_key: builtins.str,
        operator: builtins.str,
        condition_on_value: typing.Optional[typing.Union["KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationConditionConditionOnValue", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param condition_document_attribute_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#condition_document_attribute_key KendraDataSource#condition_document_attribute_key}.
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#operator KendraDataSource#operator}.
        :param condition_on_value: condition_on_value block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#condition_on_value KendraDataSource#condition_on_value}
        '''
        if isinstance(condition_on_value, dict):
            condition_on_value = KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationConditionConditionOnValue(**condition_on_value)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d366902d5f94478499e0a798f1b56635a54c66ab6179e4d1dbe5c1329d72f9a3)
            check_type(argname="argument condition_document_attribute_key", value=condition_document_attribute_key, expected_type=type_hints["condition_document_attribute_key"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument condition_on_value", value=condition_on_value, expected_type=type_hints["condition_on_value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "condition_document_attribute_key": condition_document_attribute_key,
            "operator": operator,
        }
        if condition_on_value is not None:
            self._values["condition_on_value"] = condition_on_value

    @builtins.property
    def condition_document_attribute_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#condition_document_attribute_key KendraDataSource#condition_document_attribute_key}.'''
        result = self._values.get("condition_document_attribute_key")
        assert result is not None, "Required property 'condition_document_attribute_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def operator(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#operator KendraDataSource#operator}.'''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def condition_on_value(
        self,
    ) -> typing.Optional["KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationConditionConditionOnValue"]:
        '''condition_on_value block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#condition_on_value KendraDataSource#condition_on_value}
        '''
        result = self._values.get("condition_on_value")
        return typing.cast(typing.Optional["KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationConditionConditionOnValue"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationCondition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.kendraDataSource.KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationConditionConditionOnValue",
    jsii_struct_bases=[],
    name_mapping={
        "date_value": "dateValue",
        "long_value": "longValue",
        "string_list_value": "stringListValue",
        "string_value": "stringValue",
    },
)
class KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationConditionConditionOnValue:
    def __init__(
        self,
        *,
        date_value: typing.Optional[builtins.str] = None,
        long_value: typing.Optional[jsii.Number] = None,
        string_list_value: typing.Optional[typing.Sequence[builtins.str]] = None,
        string_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param date_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#date_value KendraDataSource#date_value}.
        :param long_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#long_value KendraDataSource#long_value}.
        :param string_list_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#string_list_value KendraDataSource#string_list_value}.
        :param string_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#string_value KendraDataSource#string_value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6634587a73095917955264b4ef8b95f77c238650f87df02ecabed4725b101f2a)
            check_type(argname="argument date_value", value=date_value, expected_type=type_hints["date_value"])
            check_type(argname="argument long_value", value=long_value, expected_type=type_hints["long_value"])
            check_type(argname="argument string_list_value", value=string_list_value, expected_type=type_hints["string_list_value"])
            check_type(argname="argument string_value", value=string_value, expected_type=type_hints["string_value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if date_value is not None:
            self._values["date_value"] = date_value
        if long_value is not None:
            self._values["long_value"] = long_value
        if string_list_value is not None:
            self._values["string_list_value"] = string_list_value
        if string_value is not None:
            self._values["string_value"] = string_value

    @builtins.property
    def date_value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#date_value KendraDataSource#date_value}.'''
        result = self._values.get("date_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def long_value(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#long_value KendraDataSource#long_value}.'''
        result = self._values.get("long_value")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def string_list_value(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#string_list_value KendraDataSource#string_list_value}.'''
        result = self._values.get("string_list_value")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def string_value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#string_value KendraDataSource#string_value}.'''
        result = self._values.get("string_value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationConditionConditionOnValue(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationConditionConditionOnValueOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kendraDataSource.KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationConditionConditionOnValueOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__42e06ebc2decda5be0ea807e3030a4e94edab28db661ca7782f1b95d08fb064c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDateValue")
    def reset_date_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDateValue", []))

    @jsii.member(jsii_name="resetLongValue")
    def reset_long_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLongValue", []))

    @jsii.member(jsii_name="resetStringListValue")
    def reset_string_list_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStringListValue", []))

    @jsii.member(jsii_name="resetStringValue")
    def reset_string_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStringValue", []))

    @builtins.property
    @jsii.member(jsii_name="dateValueInput")
    def date_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dateValueInput"))

    @builtins.property
    @jsii.member(jsii_name="longValueInput")
    def long_value_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "longValueInput"))

    @builtins.property
    @jsii.member(jsii_name="stringListValueInput")
    def string_list_value_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "stringListValueInput"))

    @builtins.property
    @jsii.member(jsii_name="stringValueInput")
    def string_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stringValueInput"))

    @builtins.property
    @jsii.member(jsii_name="dateValue")
    def date_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dateValue"))

    @date_value.setter
    def date_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de7de085d840f64cf5a8ef0bee6021d55b17582d353b53a93184a460b15e82e9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dateValue", value)

    @builtins.property
    @jsii.member(jsii_name="longValue")
    def long_value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "longValue"))

    @long_value.setter
    def long_value(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5995f0e00af6dba97f13f27e652bfeffa924ec3ce03c16ba3449146b161bea41)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "longValue", value)

    @builtins.property
    @jsii.member(jsii_name="stringListValue")
    def string_list_value(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "stringListValue"))

    @string_list_value.setter
    def string_list_value(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67b11d8b03a8c3229da9b0c67e73e32252d1a06397190dfc7dcf7e84b14b71ad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stringListValue", value)

    @builtins.property
    @jsii.member(jsii_name="stringValue")
    def string_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "stringValue"))

    @string_value.setter
    def string_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__655e2166b572814e96ea53ff8ad239d1befd865141de77601b9cdad7a7cdab70)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stringValue", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationConditionConditionOnValue]:
        return typing.cast(typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationConditionConditionOnValue], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationConditionConditionOnValue],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__320a2a35b03ac5ea01fa857fd7298dd0870c0cfc7d64489b81b848a0ea65d0ad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationConditionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kendraDataSource.KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationConditionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2e84008170dc6ef93aac74800df2783dc2000baadbb07727fdb52e4c2ba15e07)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putConditionOnValue")
    def put_condition_on_value(
        self,
        *,
        date_value: typing.Optional[builtins.str] = None,
        long_value: typing.Optional[jsii.Number] = None,
        string_list_value: typing.Optional[typing.Sequence[builtins.str]] = None,
        string_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param date_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#date_value KendraDataSource#date_value}.
        :param long_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#long_value KendraDataSource#long_value}.
        :param string_list_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#string_list_value KendraDataSource#string_list_value}.
        :param string_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#string_value KendraDataSource#string_value}.
        '''
        value = KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationConditionConditionOnValue(
            date_value=date_value,
            long_value=long_value,
            string_list_value=string_list_value,
            string_value=string_value,
        )

        return typing.cast(None, jsii.invoke(self, "putConditionOnValue", [value]))

    @jsii.member(jsii_name="resetConditionOnValue")
    def reset_condition_on_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConditionOnValue", []))

    @builtins.property
    @jsii.member(jsii_name="conditionOnValue")
    def condition_on_value(
        self,
    ) -> KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationConditionConditionOnValueOutputReference:
        return typing.cast(KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationConditionConditionOnValueOutputReference, jsii.get(self, "conditionOnValue"))

    @builtins.property
    @jsii.member(jsii_name="conditionDocumentAttributeKeyInput")
    def condition_document_attribute_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "conditionDocumentAttributeKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="conditionOnValueInput")
    def condition_on_value_input(
        self,
    ) -> typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationConditionConditionOnValue]:
        return typing.cast(typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationConditionConditionOnValue], jsii.get(self, "conditionOnValueInput"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="conditionDocumentAttributeKey")
    def condition_document_attribute_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "conditionDocumentAttributeKey"))

    @condition_document_attribute_key.setter
    def condition_document_attribute_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72429bebb472a7e18ea07a9530dd82367fbd6d34f357a5495c5fe168f8df5512)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "conditionDocumentAttributeKey", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cfaa553663a408ae699b69de6dd6badbd109200b292f8a1de9ba544d5712c979)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationCondition]:
        return typing.cast(typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationCondition], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationCondition],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c30e8655d1ef95e6ce761904a8cca5a00a83ce11592f3668b09fb14b0846f38)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kendraDataSource.KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3f28618eaa898760cd73da99d4c9ee53e5791b9364885fd065991b70f17aad5e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putInvocationCondition")
    def put_invocation_condition(
        self,
        *,
        condition_document_attribute_key: builtins.str,
        operator: builtins.str,
        condition_on_value: typing.Optional[typing.Union[KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationConditionConditionOnValue, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param condition_document_attribute_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#condition_document_attribute_key KendraDataSource#condition_document_attribute_key}.
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#operator KendraDataSource#operator}.
        :param condition_on_value: condition_on_value block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#condition_on_value KendraDataSource#condition_on_value}
        '''
        value = KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationCondition(
            condition_document_attribute_key=condition_document_attribute_key,
            operator=operator,
            condition_on_value=condition_on_value,
        )

        return typing.cast(None, jsii.invoke(self, "putInvocationCondition", [value]))

    @jsii.member(jsii_name="resetInvocationCondition")
    def reset_invocation_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInvocationCondition", []))

    @builtins.property
    @jsii.member(jsii_name="invocationCondition")
    def invocation_condition(
        self,
    ) -> KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationConditionOutputReference:
        return typing.cast(KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationConditionOutputReference, jsii.get(self, "invocationCondition"))

    @builtins.property
    @jsii.member(jsii_name="invocationConditionInput")
    def invocation_condition_input(
        self,
    ) -> typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationCondition]:
        return typing.cast(typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationCondition], jsii.get(self, "invocationConditionInput"))

    @builtins.property
    @jsii.member(jsii_name="lambdaArnInput")
    def lambda_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lambdaArnInput"))

    @builtins.property
    @jsii.member(jsii_name="s3BucketInput")
    def s3_bucket_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "s3BucketInput"))

    @builtins.property
    @jsii.member(jsii_name="lambdaArn")
    def lambda_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lambdaArn"))

    @lambda_arn.setter
    def lambda_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3633bc6f5cbb0b394245aaf1dd8e9d56509e46af3cafbb87170c4c310393405d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lambdaArn", value)

    @builtins.property
    @jsii.member(jsii_name="s3Bucket")
    def s3_bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "s3Bucket"))

    @s3_bucket.setter
    def s3_bucket(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9223023355eee7d00b19e624ec34806b9a00578ce55aa11090f290a43f6377a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3Bucket", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfiguration]:
        return typing.cast(typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dbd25f43a89056822b9eb9da90bdc9ab0e12f0b4b052023c88158bf5393139a4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kendraDataSource.KendraDataSourceTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class KendraDataSourceTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#create KendraDataSource#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#delete KendraDataSource#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#update KendraDataSource#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__655f16722b095cd6d42d96e6b92b04736730a0c233c67378611b29ef095b3b05)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#create KendraDataSource#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#delete KendraDataSource#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#update KendraDataSource#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraDataSourceTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KendraDataSourceTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kendraDataSource.KendraDataSourceTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a36bee1cdef5cdb17768abe982e35e7df54549e397aee4575a01e84e0468615d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4d6692f99f891d1152b9bc1a4ef11fad1864b650b7b913343e02bef9d8d8c2bf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66913893262f34b85127fb2e6791f70334333be73ca0a52b61c1ddf85ac29b76)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__307b4c51a967058529f02741d753cd53d8e1fe99fac64346b981d76a1726b7fe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[KendraDataSourceTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[KendraDataSourceTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[KendraDataSourceTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__473a2faa3704e5c0b6f82ebe526272100fd13022f4db0063085a57a0120ea860)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "KendraDataSource",
    "KendraDataSourceConfig",
    "KendraDataSourceConfiguration",
    "KendraDataSourceConfigurationOutputReference",
    "KendraDataSourceConfigurationS3Configuration",
    "KendraDataSourceConfigurationS3ConfigurationAccessControlListConfiguration",
    "KendraDataSourceConfigurationS3ConfigurationAccessControlListConfigurationOutputReference",
    "KendraDataSourceConfigurationS3ConfigurationDocumentsMetadataConfiguration",
    "KendraDataSourceConfigurationS3ConfigurationDocumentsMetadataConfigurationOutputReference",
    "KendraDataSourceConfigurationS3ConfigurationOutputReference",
    "KendraDataSourceConfigurationWebCrawlerConfiguration",
    "KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfiguration",
    "KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationBasicAuthentication",
    "KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationBasicAuthenticationList",
    "KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationBasicAuthenticationOutputReference",
    "KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationOutputReference",
    "KendraDataSourceConfigurationWebCrawlerConfigurationOutputReference",
    "KendraDataSourceConfigurationWebCrawlerConfigurationProxyConfiguration",
    "KendraDataSourceConfigurationWebCrawlerConfigurationProxyConfigurationOutputReference",
    "KendraDataSourceConfigurationWebCrawlerConfigurationUrls",
    "KendraDataSourceConfigurationWebCrawlerConfigurationUrlsOutputReference",
    "KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSeedUrlConfiguration",
    "KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSeedUrlConfigurationOutputReference",
    "KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSiteMapsConfiguration",
    "KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSiteMapsConfigurationOutputReference",
    "KendraDataSourceCustomDocumentEnrichmentConfiguration",
    "KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurations",
    "KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsCondition",
    "KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsConditionConditionOnValue",
    "KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsConditionConditionOnValueOutputReference",
    "KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsConditionOutputReference",
    "KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsList",
    "KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsOutputReference",
    "KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTarget",
    "KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTargetOutputReference",
    "KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTargetTargetDocumentAttributeValue",
    "KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTargetTargetDocumentAttributeValueOutputReference",
    "KendraDataSourceCustomDocumentEnrichmentConfigurationOutputReference",
    "KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfiguration",
    "KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationCondition",
    "KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationConditionConditionOnValue",
    "KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationConditionConditionOnValueOutputReference",
    "KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationConditionOutputReference",
    "KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationOutputReference",
    "KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfiguration",
    "KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationCondition",
    "KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationConditionConditionOnValue",
    "KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationConditionConditionOnValueOutputReference",
    "KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationConditionOutputReference",
    "KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationOutputReference",
    "KendraDataSourceTimeouts",
    "KendraDataSourceTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__60baf8b44110c732a4cd738c259e25fc807db3752bc22ef2f2dd94682d1696ef(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    index_id: builtins.str,
    name: builtins.str,
    type: builtins.str,
    configuration: typing.Optional[typing.Union[KendraDataSourceConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    custom_document_enrichment_configuration: typing.Optional[typing.Union[KendraDataSourceCustomDocumentEnrichmentConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    description: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    language_code: typing.Optional[builtins.str] = None,
    role_arn: typing.Optional[builtins.str] = None,
    schedule: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[KendraDataSourceTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__199e6169834a5c1ae52484b019d2fbe769d441dc4c8b7f68c2e9d0be328ba97b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__272b547feff976e273affe1902667da01e822b3cbb1af56498dcb7fc1d499046(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ecfc601d9470eb0a94aa6591da9bea496b0ea0c96d82525db85bc439387ed46(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5900e9235bec373253c99a5ba0008e11e70a29e444dcb1394259519babce5c78(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95b43b84a300a4a6cc1148a384923c551268640f2896b37019be3fe8c7d6db8a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67d3ebc470fc721eb050331e9c9e521ab682d392fdd5f07c105fa344cc5ac85b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24c6a9e0220405f7e2e46bb81175d34c326c1e0e8f19a1f96aa8d7831ed8f8b6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d8a7ee6566510bc41b8b98933ada52d13ec87f9f384d8b57cd487cbc856bf75(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bee823653548eaf77070e10804948c9a717dedbae6ff495c9e142acf44a8e41d(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87f8b80d2a765a9f1f9a6730c5cc2a6cefad45c75dd462dc0e8838f61c304c4a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02950fb7577167c63456bdd034f68dd907cf47880d5481fd4018b8aae9f59afb(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    index_id: builtins.str,
    name: builtins.str,
    type: builtins.str,
    configuration: typing.Optional[typing.Union[KendraDataSourceConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    custom_document_enrichment_configuration: typing.Optional[typing.Union[KendraDataSourceCustomDocumentEnrichmentConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    description: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    language_code: typing.Optional[builtins.str] = None,
    role_arn: typing.Optional[builtins.str] = None,
    schedule: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[KendraDataSourceTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41d1c880e481b0e5e9b5f3811c0316a97f7157781366b94cece21ce8745cab6c(
    *,
    s3_configuration: typing.Optional[typing.Union[KendraDataSourceConfigurationS3Configuration, typing.Dict[builtins.str, typing.Any]]] = None,
    web_crawler_configuration: typing.Optional[typing.Union[KendraDataSourceConfigurationWebCrawlerConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5eb453fde97188d6a89c2f0759f5a2f01dc1c8b0c491670ee33908256870df8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bbee117ed4ba080f85f63914824cb9bf66c43096d2515eaa39168124955de017(
    value: typing.Optional[KendraDataSourceConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac272edee0fc4616f2e89908126880ff7e37c22162963abe25d9949ffa3275ac(
    *,
    bucket_name: builtins.str,
    access_control_list_configuration: typing.Optional[typing.Union[KendraDataSourceConfigurationS3ConfigurationAccessControlListConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    documents_metadata_configuration: typing.Optional[typing.Union[KendraDataSourceConfigurationS3ConfigurationDocumentsMetadataConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    exclusion_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
    inclusion_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
    inclusion_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25fbc7e1cbf8e319a8057c92bd8ee18bcf9506f301c85652f209f0e05b69cf1a(
    *,
    key_path: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4af70d422045f46c5374f14a02125d13e4688503ed4ebb04b14559f2afdc65d3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ffe2104ba3b93bdf4dca8b319ecda284d019f505637a58551f4b2e901cd2de66(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7497b9c393cc5cdb7ef65192ff5cbc55a0dbed8f926b05349efba474697099ab(
    value: typing.Optional[KendraDataSourceConfigurationS3ConfigurationAccessControlListConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d968657f0a5be41c470a76a28059a90e59c5cc0582dddf95789a111204a9b50d(
    *,
    s3_prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa015ac8da967280b719b7d0ee2bac79b2dc59511ee209cb3141508fa3083758(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1027f0d8eb3b08bb18369110475a6ce9573ccaf790b9b2293604625f0ccd06c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__921ac1502713f35dcb733dd0938aa3c48ebeb042d4822d51c67369921b955ea8(
    value: typing.Optional[KendraDataSourceConfigurationS3ConfigurationDocumentsMetadataConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46ed771170b831bebf8d0036ceec8b2dc13db12f81645e497403d6215b619533(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad6c1a74d210b84183f81bc13ced7bea6ebc1b08b2bf89e3a42cff5ae3e32a2b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b579b54e68d4bb24fa34ac825207c386d770f2f79d561a06e75344a98cb3ed9(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ac25a4b409f1a023345b9e9975a3e0d0e03e7446a10ae898e8be5d6eaa475ef(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__651b60ee6ca573b83c8094ea457218613996447e3d5c4050f9bb7928231064eb(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f07b052d201fc6ce5f489c16363379ea3e17d56191e8ef168406be03ace30074(
    value: typing.Optional[KendraDataSourceConfigurationS3Configuration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88d9d4c6025ca3fea705401050fde4fb303518ad794ae4c3ad79712520c0b9bc(
    *,
    urls: typing.Union[KendraDataSourceConfigurationWebCrawlerConfigurationUrls, typing.Dict[builtins.str, typing.Any]],
    authentication_configuration: typing.Optional[typing.Union[KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    crawl_depth: typing.Optional[jsii.Number] = None,
    max_content_size_per_page_in_mega_bytes: typing.Optional[jsii.Number] = None,
    max_links_per_page: typing.Optional[jsii.Number] = None,
    max_urls_per_minute_crawl_rate: typing.Optional[jsii.Number] = None,
    proxy_configuration: typing.Optional[typing.Union[KendraDataSourceConfigurationWebCrawlerConfigurationProxyConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    url_exclusion_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
    url_inclusion_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d112e3ad2e361321f376f608d168f91b16f0c5d5247dfb05bd10cbd886a363f9(
    *,
    basic_authentication: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationBasicAuthentication, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c3e4ecc7ba273e89356c155547bff682c0315a940077dcfe89e6820f0a8288b(
    *,
    credentials: builtins.str,
    host: builtins.str,
    port: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ead29c352f94497ea690ebc13efdce25297ca999506b375836eb44c0336d7de4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb9163fcb9e7135c963f2437024ec13ed43cac3f7087421812d587e0b6187f25(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61bd3c18e74cea20dc5e382600f449e4e647667f6972f6b3c6447ccbb9138783(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__729c11149a6d9c6d518c99a84f6d56ff177a8bf8b82fb398e9f1ef275dde520b(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3da4d9b841da7ad76ae5d2ac1345c1ee337aef0f27138108ccef3a82ccadc8ff(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1e8c8d78d1ec402cfe572bb87db969873e2ddb442c49f9b69e2bfe820dbe284(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationBasicAuthentication]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7abc8f0d924d57833e508c59c14940f8d54dc30540bf5da7d94778be6ac4f0e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92f2fd0e2b7d89087db40c55be42c4bc5efdbc3dce9ec40151106fdc7e269597(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd3e1b2436a7ffc490cfcf5aca65da37cdb381ccacaa80378ceca1430f9bb151(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d8871fc58df39214e09c56322a7059200a0e1c610cf37f2411ead31d454de59(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3604560a7ed2a53803c3f0abcb6fc6229822a67c4727c03f45b7be58706169b(
    value: typing.Optional[typing.Union[KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationBasicAuthentication, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0256de35f772eb4103dbda3b2c533c230edd0467ca8411da502e5df23e554b1a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c20a96b6e761237e8a773c0ef3d100c5345e8d04388b28c7837f87af6582504(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationBasicAuthentication, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63e322859e79be33ae1b86c6e370fa6e05915accaf5e09a54c5d7608c35200fd(
    value: typing.Optional[KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9aa2507809a2a1892273cb38e58ee107ac6b3fdf29d2c0298ceefcc3051f682a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__061f17b8e671caca94ff0e1a36103b964514d4b25097a7f30f1ff050dda4d332(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38288170f8e072d24f2362979b359135be48653a5c2e079137680872d92718bd(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a2ab3038e59aaf7ba74b72f620f801002b402ce82c98f65a4a5f89f76c1d015(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b72f71aed0387b5c23bb3c959a597b073baadeaf6f5a97345dba1db7e51b3ac1(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b010a8f1b96c8caef2f4f7e53fd097294f3ee793d1baea66340614de7bfe43d4(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b112a217ee69ef1946340ba1ee93932a51acc5e329de4e0db9eb52a1b3e7e3b4(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e82249e21ac04dc3f51d490f1b27d9e1b76281dd507079f0d039d556e695cee9(
    value: typing.Optional[KendraDataSourceConfigurationWebCrawlerConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3de2a16c7e3edd16d8f7c03384f895efebf606d9e04de34825492e189ac4a98(
    *,
    host: builtins.str,
    port: jsii.Number,
    credentials: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38e9261de2852a82fff3fa371992876bd7261c37fd9a70c135e926db4dba5077(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9832e292f641a5ce97b40bb4f5b9dc55a5ae047f32ce5d76bd828e9bf21e7736(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e324ddb6899df21974ac68e163c7a14e370814f35dfd6d2ee02afdab356fa605(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf3ce887ccde107584c92146150048214668cf33ab17ef28fe9a2e47b5c32b55(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6335a511cb5d54b2ba1abbde3e6f101ea162d134705aaf49f5f05447407d7706(
    value: typing.Optional[KendraDataSourceConfigurationWebCrawlerConfigurationProxyConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8258b03cfe10d579a5c41b92a4995ccbcf911eec78631468a47b6f72bbe3ca59(
    *,
    seed_url_configuration: typing.Optional[typing.Union[KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSeedUrlConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    site_maps_configuration: typing.Optional[typing.Union[KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSiteMapsConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec32ea3efdea05a022b3e6bae0e08ef0a38c76e4d0cc212ff1e95c1fa70ddc9f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3d26b96169a59ffd3973c08c1d20981d237a81a61cda9fbe4f2273dae3dcedf(
    value: typing.Optional[KendraDataSourceConfigurationWebCrawlerConfigurationUrls],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08afcde04375ec2878ca7327b46cb5555de55498abeb50ce14f94def0a97402d(
    *,
    seed_urls: typing.Sequence[builtins.str],
    web_crawler_mode: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1462b655a166436e70c4ca329ef7a1d9d6ff724cb408eafd140f8d2d45c8aeb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7a01e2aa6e08deb10e36323e17d8a55b629e65809c6c931e06ced3746b4b256(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4919fdc5c50f07fb4c51b1c5d4779d0522b00f781c83e587213e87ee6a5111e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__249cc540d39cfae626cce0064da2c0394752ddb13978e53a489ddb3eacc4c046(
    value: typing.Optional[KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSeedUrlConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d76a0e683633760867f4992099fff7eeb2dc9b89fa32439effd2290543e0fad(
    *,
    site_maps: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ad0e6e086f1860b32c319afe0b8e0ac60ec8d01c727c99c6d415d74023ffd0a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ecdf20ce5c781957d0c057821aec5b10fe0ccd2a359d1cbf0dfa3aa90a6303ea(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8aac84ecd07d8f90d5c199982fff157ccde8fd7ff87caf237b13346de356e03a(
    value: typing.Optional[KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSiteMapsConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4307366fc5b9f720e9117582e2e37a3472b1121cc1331b4b6a45695a3f47ccd(
    *,
    inline_configurations: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurations, typing.Dict[builtins.str, typing.Any]]]]] = None,
    post_extraction_hook_configuration: typing.Optional[typing.Union[KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    pre_extraction_hook_configuration: typing.Optional[typing.Union[KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    role_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a46c385ef0d708a5103352ba6fd83b619f0b98eab134e84f8a933c014ed2b4e9(
    *,
    condition: typing.Optional[typing.Union[KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsCondition, typing.Dict[builtins.str, typing.Any]]] = None,
    document_content_deletion: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    target: typing.Optional[typing.Union[KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTarget, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee383b20a81fa94f80288cf156cff6c4a63c670b7a222c36ea7010452157228e(
    *,
    condition_document_attribute_key: builtins.str,
    operator: builtins.str,
    condition_on_value: typing.Optional[typing.Union[KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsConditionConditionOnValue, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8bcc5c631302e380b0ceb7172314316a5002a272dff82b14d8b7bbdeb313d53(
    *,
    date_value: typing.Optional[builtins.str] = None,
    long_value: typing.Optional[jsii.Number] = None,
    string_list_value: typing.Optional[typing.Sequence[builtins.str]] = None,
    string_value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2bc74abd5191d10fa6ad5e6e4dcb25bb9893055478dd64c75afe2e0789d3029f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d310c4db32cf8b82de679700889d9d34de7bb0d310d2f2ba8905a2243582e81(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05e85bfdd1dc1efe6f35a8cc5a0f65bcfcb4ee2725c9998cd513e5d162d500f7(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1dbb0e9ebd16e43de521763541d28b12579fa6bdb9f57ee477613c96354489cc(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5dbf72d6400dad3142f7d545f1f633d1a7f8870dee9a83287d8d8dc905deb8c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__955f54c3e4c39fa5616560f82310b9c5b80ef2d88b705f74fd1aff640b40cd04(
    value: typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsConditionConditionOnValue],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c0aa21b1e10ab5a1fe940519f0b1f1fa02517fa6e6ecd07b3a297c1caf79760(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d9f50eaf9f5201323bee3fec48a7c383603dca6299bd44087438861881f4be1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57cdb94f3b4412ac46c8d35da3a17305cf202641e89c4b515c1ffe9b3b9569fa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73842f950839dd64c923fce7fbe33be3dafed52631eff9f867a2b3fda85c5454(
    value: typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsCondition],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__953db39616a86cac88e8d43ecf786b4999d4c8d1eb893a12f8f746b039be9934(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de658b4fbd1857272d7e28367782294b29c2ca3ec745ffd8840f346f69b78951(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85d149276a7139d587a632b003b559499d61d966ecb988a040a158dded781f03(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6f62831534dba6c5caaa282a29b288ea43eb8f77fbbc1a6fda1418d900cc8e5(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad33accf57e856cea6bcb8ce170df9731c1d9f2d2510d0cdef658d3f577bb62d(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f53ff39a3239e1eeea36f49fbd09aacea7dda81097ecd1750df3c3659112d566(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurations]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c55a747658710fc260894259e572107e1370d850d1c6859db9f48992b036b30b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b47f22de26d9e4a02a96d7eeab7d3786428b73462d5d5bab8a1821faabb1638(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c48a9124b54739bd77169181e1c59f195e4f05361228ea98617eb64cbc5335b(
    value: typing.Optional[typing.Union[KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurations, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42bfe2b46257544bd7e61c0d4486002ee235caf065b3e533d73a3a79e1057ed0(
    *,
    target_document_attribute_key: typing.Optional[builtins.str] = None,
    target_document_attribute_value: typing.Optional[typing.Union[KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTargetTargetDocumentAttributeValue, typing.Dict[builtins.str, typing.Any]]] = None,
    target_document_attribute_value_deletion: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23fa383178a69bceee66cade33b3be49ef0601437789b5d9877032807a4137ed(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__040e8e8ab7e7636619844a5929e034e1f03f36a0fd4de1bd3f84d75789d76e7c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa028a1b195b2b0371aff214a9f1b1050273a5f1bef4fc0d1a11418a8410439b(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a964d5b7e5de37b447a1969b3e40b16adae03f44a83a96ed71346f0983c5f134(
    value: typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTarget],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__962670366b83baa2432389879618b05cc3372c83d0d42a5ad80ba7afdccb3d26(
    *,
    date_value: typing.Optional[builtins.str] = None,
    long_value: typing.Optional[jsii.Number] = None,
    string_list_value: typing.Optional[typing.Sequence[builtins.str]] = None,
    string_value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ca5af3a8e68cff6f5947214ead9088f252c363ebc773ec172d102c6906b4966(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1619e0f85b374173724e7fd79e37cbbc49566b6119278830367f86520fb9c25(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9cfb464ef9c3a19916fde2156b645b5d1df1830e1ff7d676653693b4ad80b284(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__758db9d7302917588dadc56415a9acf109b7200419185f6bff20330b1ac2d8c8(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f034b3d0f4f0ba915d896f5358478e6081134b12b1f7e7d13810ed90e89cf92(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1ca7008a24714f2adf809193d7712a58ea96933af81d9cc273ce92dd72d9bef(
    value: typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTargetTargetDocumentAttributeValue],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b53abbaf97a1b00b60dc4f063ff5b904fc8d8e5f8fc9c09ffe724c7ba9f76fce(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cbacd3409d6c1687f0936c3f1d7d34447fddc158d4857dd09bc66a3778447721(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurations, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c4aa40913db25750a3a0873f4d42d4df4de8be5edab9235d3f802af2f6a8289(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ebdef59af62b06304d2f9bd34eab743dc5b096e4a65dec00491c35835fa30d6e(
    value: typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9958b42f8fe2b466d7c3a6c1f915ab3642c0bb3e4b2d4bca852deccfd4eb0e0(
    *,
    lambda_arn: builtins.str,
    s3_bucket: builtins.str,
    invocation_condition: typing.Optional[typing.Union[KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationCondition, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__905be7243de550df7ccb4d71797e1a846a7d660edd009d6006a2cf3a2c568b42(
    *,
    condition_document_attribute_key: builtins.str,
    operator: builtins.str,
    condition_on_value: typing.Optional[typing.Union[KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationConditionConditionOnValue, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da099e5f694596908f0c73f3b94256abdb0cfbc1d60db529c4b4f2407f7bea8f(
    *,
    date_value: typing.Optional[builtins.str] = None,
    long_value: typing.Optional[jsii.Number] = None,
    string_list_value: typing.Optional[typing.Sequence[builtins.str]] = None,
    string_value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c9159d5d09ee9e3db2718d834313e23791884e2ff1ccde5bc6ef40357f8f4fb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9385921bec85623014d56a0f5436f713822ac4cc4d9bf85d653a372d7a6bf36(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7ba1b5beaf7b25ed1bd65878c8c73c9c09fb9883acc85328f582a693c9182ab(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bea45efaeef769c8228544ce43e0a2fb01d6a165502351ead6a0179fc8647513(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bbf02254113cfb425b7d8ab8bcdb11535d19ab3a2f08bedce58d8de8f0e2f22b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e234c3abd950a1e25f2c012a95a5f8020f59aacea7978ffe18732493a7c4030(
    value: typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationConditionConditionOnValue],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58e074cc0e614248dc209af194b02d0643fdd6719e6f42376572ad07d5ab24c5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54ca29e8a13f9aaaebbe9bb62712b5fd7e0108248086a4352049fd322c11da5a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5032a49064101c5a3679293b8dbb25d5de252c28fe485886e8ecfdb7ee7bd9ea(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__249f70da9f2ca4ac619c2be25d8e0154bbc15da43c807602af21235f99eee929(
    value: typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationCondition],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00f9a72486d1b43c019352267ff06cf70169341883064a129970807deb7df194(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__846c546b82870ce6f95ea638c43ba1e5db293daf1b212bea9ec3a4096308f5b8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a0f7a74085af81d9a33f81738e374c36ebb9468de2d5a8e85a78968435ca634(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a9148cdb4fbf4340169b40618f1e3d715a97deb0385b01fadcfd4c68242d2c8(
    value: typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__332f4e83e9b9d35eddf5602e47f1344c79efe7fc7889fbe89a8862d27e02dfc2(
    *,
    lambda_arn: builtins.str,
    s3_bucket: builtins.str,
    invocation_condition: typing.Optional[typing.Union[KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationCondition, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d366902d5f94478499e0a798f1b56635a54c66ab6179e4d1dbe5c1329d72f9a3(
    *,
    condition_document_attribute_key: builtins.str,
    operator: builtins.str,
    condition_on_value: typing.Optional[typing.Union[KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationConditionConditionOnValue, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6634587a73095917955264b4ef8b95f77c238650f87df02ecabed4725b101f2a(
    *,
    date_value: typing.Optional[builtins.str] = None,
    long_value: typing.Optional[jsii.Number] = None,
    string_list_value: typing.Optional[typing.Sequence[builtins.str]] = None,
    string_value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42e06ebc2decda5be0ea807e3030a4e94edab28db661ca7782f1b95d08fb064c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de7de085d840f64cf5a8ef0bee6021d55b17582d353b53a93184a460b15e82e9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5995f0e00af6dba97f13f27e652bfeffa924ec3ce03c16ba3449146b161bea41(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67b11d8b03a8c3229da9b0c67e73e32252d1a06397190dfc7dcf7e84b14b71ad(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__655e2166b572814e96ea53ff8ad239d1befd865141de77601b9cdad7a7cdab70(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__320a2a35b03ac5ea01fa857fd7298dd0870c0cfc7d64489b81b848a0ea65d0ad(
    value: typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationConditionConditionOnValue],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e84008170dc6ef93aac74800df2783dc2000baadbb07727fdb52e4c2ba15e07(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72429bebb472a7e18ea07a9530dd82367fbd6d34f357a5495c5fe168f8df5512(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfaa553663a408ae699b69de6dd6badbd109200b292f8a1de9ba544d5712c979(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c30e8655d1ef95e6ce761904a8cca5a00a83ce11592f3668b09fb14b0846f38(
    value: typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationCondition],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f28618eaa898760cd73da99d4c9ee53e5791b9364885fd065991b70f17aad5e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3633bc6f5cbb0b394245aaf1dd8e9d56509e46af3cafbb87170c4c310393405d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9223023355eee7d00b19e624ec34806b9a00578ce55aa11090f290a43f6377a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dbd25f43a89056822b9eb9da90bdc9ab0e12f0b4b052023c88158bf5393139a4(
    value: typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__655f16722b095cd6d42d96e6b92b04736730a0c233c67378611b29ef095b3b05(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a36bee1cdef5cdb17768abe982e35e7df54549e397aee4575a01e84e0468615d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d6692f99f891d1152b9bc1a4ef11fad1864b650b7b913343e02bef9d8d8c2bf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66913893262f34b85127fb2e6791f70334333be73ca0a52b61c1ddf85ac29b76(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__307b4c51a967058529f02741d753cd53d8e1fe99fac64346b981d76a1726b7fe(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__473a2faa3704e5c0b6f82ebe526272100fd13022f4db0063085a57a0120ea860(
    value: typing.Optional[typing.Union[KendraDataSourceTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
