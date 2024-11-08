'''
# `aws_codepipeline_custom_action_type`

Refer to the Terraform Registory for docs: [`aws_codepipeline_custom_action_type`](https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type).
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


class CodepipelineCustomActionType(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.codepipelineCustomActionType.CodepipelineCustomActionType",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type aws_codepipeline_custom_action_type}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        category: builtins.str,
        input_artifact_details: typing.Union["CodepipelineCustomActionTypeInputArtifactDetails", typing.Dict[builtins.str, typing.Any]],
        output_artifact_details: typing.Union["CodepipelineCustomActionTypeOutputArtifactDetails", typing.Dict[builtins.str, typing.Any]],
        provider_name: builtins.str,
        version: builtins.str,
        configuration_property: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CodepipelineCustomActionTypeConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        settings: typing.Optional[typing.Union["CodepipelineCustomActionTypeSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type aws_codepipeline_custom_action_type} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param category: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#category CodepipelineCustomActionType#category}.
        :param input_artifact_details: input_artifact_details block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#input_artifact_details CodepipelineCustomActionType#input_artifact_details}
        :param output_artifact_details: output_artifact_details block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#output_artifact_details CodepipelineCustomActionType#output_artifact_details}
        :param provider_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#provider_name CodepipelineCustomActionType#provider_name}.
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#version CodepipelineCustomActionType#version}.
        :param configuration_property: configuration_property block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#configuration_property CodepipelineCustomActionType#configuration_property}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#id CodepipelineCustomActionType#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param settings: settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#settings CodepipelineCustomActionType#settings}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#tags CodepipelineCustomActionType#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#tags_all CodepipelineCustomActionType#tags_all}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73ad63c8adbf03cef81669b17e8a02a5d697f23a1e5d9031c02674c659a7d2c9)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = CodepipelineCustomActionTypeConfig(
            category=category,
            input_artifact_details=input_artifact_details,
            output_artifact_details=output_artifact_details,
            provider_name=provider_name,
            version=version,
            configuration_property=configuration_property,
            id=id,
            settings=settings,
            tags=tags,
            tags_all=tags_all,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putConfigurationProperty")
    def put_configuration_property(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CodepipelineCustomActionTypeConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05ca6a541d56dfd8fd195b04b1fa76b6885d3932ddce2ae5f77cd55637d7b4af)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putConfigurationProperty", [value]))

    @jsii.member(jsii_name="putInputArtifactDetails")
    def put_input_artifact_details(
        self,
        *,
        maximum_count: jsii.Number,
        minimum_count: jsii.Number,
    ) -> None:
        '''
        :param maximum_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#maximum_count CodepipelineCustomActionType#maximum_count}.
        :param minimum_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#minimum_count CodepipelineCustomActionType#minimum_count}.
        '''
        value = CodepipelineCustomActionTypeInputArtifactDetails(
            maximum_count=maximum_count, minimum_count=minimum_count
        )

        return typing.cast(None, jsii.invoke(self, "putInputArtifactDetails", [value]))

    @jsii.member(jsii_name="putOutputArtifactDetails")
    def put_output_artifact_details(
        self,
        *,
        maximum_count: jsii.Number,
        minimum_count: jsii.Number,
    ) -> None:
        '''
        :param maximum_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#maximum_count CodepipelineCustomActionType#maximum_count}.
        :param minimum_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#minimum_count CodepipelineCustomActionType#minimum_count}.
        '''
        value = CodepipelineCustomActionTypeOutputArtifactDetails(
            maximum_count=maximum_count, minimum_count=minimum_count
        )

        return typing.cast(None, jsii.invoke(self, "putOutputArtifactDetails", [value]))

    @jsii.member(jsii_name="putSettings")
    def put_settings(
        self,
        *,
        entity_url_template: typing.Optional[builtins.str] = None,
        execution_url_template: typing.Optional[builtins.str] = None,
        revision_url_template: typing.Optional[builtins.str] = None,
        third_party_configuration_url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param entity_url_template: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#entity_url_template CodepipelineCustomActionType#entity_url_template}.
        :param execution_url_template: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#execution_url_template CodepipelineCustomActionType#execution_url_template}.
        :param revision_url_template: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#revision_url_template CodepipelineCustomActionType#revision_url_template}.
        :param third_party_configuration_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#third_party_configuration_url CodepipelineCustomActionType#third_party_configuration_url}.
        '''
        value = CodepipelineCustomActionTypeSettings(
            entity_url_template=entity_url_template,
            execution_url_template=execution_url_template,
            revision_url_template=revision_url_template,
            third_party_configuration_url=third_party_configuration_url,
        )

        return typing.cast(None, jsii.invoke(self, "putSettings", [value]))

    @jsii.member(jsii_name="resetConfigurationProperty")
    def reset_configuration_property(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfigurationProperty", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetSettings")
    def reset_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSettings", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

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
    @jsii.member(jsii_name="configurationProperty")
    def configuration_property(
        self,
    ) -> "CodepipelineCustomActionTypeConfigurationPropertyList":
        return typing.cast("CodepipelineCustomActionTypeConfigurationPropertyList", jsii.get(self, "configurationProperty"))

    @builtins.property
    @jsii.member(jsii_name="inputArtifactDetails")
    def input_artifact_details(
        self,
    ) -> "CodepipelineCustomActionTypeInputArtifactDetailsOutputReference":
        return typing.cast("CodepipelineCustomActionTypeInputArtifactDetailsOutputReference", jsii.get(self, "inputArtifactDetails"))

    @builtins.property
    @jsii.member(jsii_name="outputArtifactDetails")
    def output_artifact_details(
        self,
    ) -> "CodepipelineCustomActionTypeOutputArtifactDetailsOutputReference":
        return typing.cast("CodepipelineCustomActionTypeOutputArtifactDetailsOutputReference", jsii.get(self, "outputArtifactDetails"))

    @builtins.property
    @jsii.member(jsii_name="owner")
    def owner(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "owner"))

    @builtins.property
    @jsii.member(jsii_name="settings")
    def settings(self) -> "CodepipelineCustomActionTypeSettingsOutputReference":
        return typing.cast("CodepipelineCustomActionTypeSettingsOutputReference", jsii.get(self, "settings"))

    @builtins.property
    @jsii.member(jsii_name="categoryInput")
    def category_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "categoryInput"))

    @builtins.property
    @jsii.member(jsii_name="configurationPropertyInput")
    def configuration_property_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CodepipelineCustomActionTypeConfigurationProperty"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CodepipelineCustomActionTypeConfigurationProperty"]]], jsii.get(self, "configurationPropertyInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="inputArtifactDetailsInput")
    def input_artifact_details_input(
        self,
    ) -> typing.Optional["CodepipelineCustomActionTypeInputArtifactDetails"]:
        return typing.cast(typing.Optional["CodepipelineCustomActionTypeInputArtifactDetails"], jsii.get(self, "inputArtifactDetailsInput"))

    @builtins.property
    @jsii.member(jsii_name="outputArtifactDetailsInput")
    def output_artifact_details_input(
        self,
    ) -> typing.Optional["CodepipelineCustomActionTypeOutputArtifactDetails"]:
        return typing.cast(typing.Optional["CodepipelineCustomActionTypeOutputArtifactDetails"], jsii.get(self, "outputArtifactDetailsInput"))

    @builtins.property
    @jsii.member(jsii_name="providerNameInput")
    def provider_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "providerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="settingsInput")
    def settings_input(self) -> typing.Optional["CodepipelineCustomActionTypeSettings"]:
        return typing.cast(typing.Optional["CodepipelineCustomActionTypeSettings"], jsii.get(self, "settingsInput"))

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
    @jsii.member(jsii_name="versionInput")
    def version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionInput"))

    @builtins.property
    @jsii.member(jsii_name="category")
    def category(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "category"))

    @category.setter
    def category(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc2c2ea5fc75ec61c9e69b0b42c8098a3f28e57b1017c0f2b5e9ea3d34b04a6d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "category", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__16ccb0c0c60abe8eb34ea8c76667947b67a060cc82dde4aba3df8ed30ccd9a94)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="providerName")
    def provider_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "providerName"))

    @provider_name.setter
    def provider_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__36c8be18aa694a68d9175468accd68d6404762acaca16ed37663acd09003b44d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "providerName", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0fbd8c6c9fd1c956d14c0e7b00de282dc246c2b30bc66a6313f30e005ca7afce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__545de1353c22e0e9586c2e544f1eee4f8ac6a302e4c92623403d13d768e94591)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a09b14a6163a78ed2a3c358c3c93052ddc17dc7953ad9b8c13457f8f0554b4b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)


@jsii.data_type(
    jsii_type="aws.codepipelineCustomActionType.CodepipelineCustomActionTypeConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "category": "category",
        "input_artifact_details": "inputArtifactDetails",
        "output_artifact_details": "outputArtifactDetails",
        "provider_name": "providerName",
        "version": "version",
        "configuration_property": "configurationProperty",
        "id": "id",
        "settings": "settings",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class CodepipelineCustomActionTypeConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        category: builtins.str,
        input_artifact_details: typing.Union["CodepipelineCustomActionTypeInputArtifactDetails", typing.Dict[builtins.str, typing.Any]],
        output_artifact_details: typing.Union["CodepipelineCustomActionTypeOutputArtifactDetails", typing.Dict[builtins.str, typing.Any]],
        provider_name: builtins.str,
        version: builtins.str,
        configuration_property: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CodepipelineCustomActionTypeConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        settings: typing.Optional[typing.Union["CodepipelineCustomActionTypeSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param category: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#category CodepipelineCustomActionType#category}.
        :param input_artifact_details: input_artifact_details block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#input_artifact_details CodepipelineCustomActionType#input_artifact_details}
        :param output_artifact_details: output_artifact_details block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#output_artifact_details CodepipelineCustomActionType#output_artifact_details}
        :param provider_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#provider_name CodepipelineCustomActionType#provider_name}.
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#version CodepipelineCustomActionType#version}.
        :param configuration_property: configuration_property block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#configuration_property CodepipelineCustomActionType#configuration_property}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#id CodepipelineCustomActionType#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param settings: settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#settings CodepipelineCustomActionType#settings}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#tags CodepipelineCustomActionType#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#tags_all CodepipelineCustomActionType#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(input_artifact_details, dict):
            input_artifact_details = CodepipelineCustomActionTypeInputArtifactDetails(**input_artifact_details)
        if isinstance(output_artifact_details, dict):
            output_artifact_details = CodepipelineCustomActionTypeOutputArtifactDetails(**output_artifact_details)
        if isinstance(settings, dict):
            settings = CodepipelineCustomActionTypeSettings(**settings)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c4eecf0318e25b5b6ec826e53094923428fff029f872014adbe12d0a2492337)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument category", value=category, expected_type=type_hints["category"])
            check_type(argname="argument input_artifact_details", value=input_artifact_details, expected_type=type_hints["input_artifact_details"])
            check_type(argname="argument output_artifact_details", value=output_artifact_details, expected_type=type_hints["output_artifact_details"])
            check_type(argname="argument provider_name", value=provider_name, expected_type=type_hints["provider_name"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            check_type(argname="argument configuration_property", value=configuration_property, expected_type=type_hints["configuration_property"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument settings", value=settings, expected_type=type_hints["settings"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "category": category,
            "input_artifact_details": input_artifact_details,
            "output_artifact_details": output_artifact_details,
            "provider_name": provider_name,
            "version": version,
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
        if configuration_property is not None:
            self._values["configuration_property"] = configuration_property
        if id is not None:
            self._values["id"] = id
        if settings is not None:
            self._values["settings"] = settings
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all

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
    def category(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#category CodepipelineCustomActionType#category}.'''
        result = self._values.get("category")
        assert result is not None, "Required property 'category' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def input_artifact_details(
        self,
    ) -> "CodepipelineCustomActionTypeInputArtifactDetails":
        '''input_artifact_details block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#input_artifact_details CodepipelineCustomActionType#input_artifact_details}
        '''
        result = self._values.get("input_artifact_details")
        assert result is not None, "Required property 'input_artifact_details' is missing"
        return typing.cast("CodepipelineCustomActionTypeInputArtifactDetails", result)

    @builtins.property
    def output_artifact_details(
        self,
    ) -> "CodepipelineCustomActionTypeOutputArtifactDetails":
        '''output_artifact_details block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#output_artifact_details CodepipelineCustomActionType#output_artifact_details}
        '''
        result = self._values.get("output_artifact_details")
        assert result is not None, "Required property 'output_artifact_details' is missing"
        return typing.cast("CodepipelineCustomActionTypeOutputArtifactDetails", result)

    @builtins.property
    def provider_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#provider_name CodepipelineCustomActionType#provider_name}.'''
        result = self._values.get("provider_name")
        assert result is not None, "Required property 'provider_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def version(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#version CodepipelineCustomActionType#version}.'''
        result = self._values.get("version")
        assert result is not None, "Required property 'version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def configuration_property(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CodepipelineCustomActionTypeConfigurationProperty"]]]:
        '''configuration_property block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#configuration_property CodepipelineCustomActionType#configuration_property}
        '''
        result = self._values.get("configuration_property")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CodepipelineCustomActionTypeConfigurationProperty"]]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#id CodepipelineCustomActionType#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def settings(self) -> typing.Optional["CodepipelineCustomActionTypeSettings"]:
        '''settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#settings CodepipelineCustomActionType#settings}
        '''
        result = self._values.get("settings")
        return typing.cast(typing.Optional["CodepipelineCustomActionTypeSettings"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#tags CodepipelineCustomActionType#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#tags_all CodepipelineCustomActionType#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodepipelineCustomActionTypeConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.codepipelineCustomActionType.CodepipelineCustomActionTypeConfigurationProperty",
    jsii_struct_bases=[],
    name_mapping={
        "key": "key",
        "name": "name",
        "required": "required",
        "secret": "secret",
        "description": "description",
        "queryable": "queryable",
        "type": "type",
    },
)
class CodepipelineCustomActionTypeConfigurationProperty:
    def __init__(
        self,
        *,
        key: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        name: builtins.str,
        required: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        secret: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        description: typing.Optional[builtins.str] = None,
        queryable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#key CodepipelineCustomActionType#key}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#name CodepipelineCustomActionType#name}.
        :param required: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#required CodepipelineCustomActionType#required}.
        :param secret: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#secret CodepipelineCustomActionType#secret}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#description CodepipelineCustomActionType#description}.
        :param queryable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#queryable CodepipelineCustomActionType#queryable}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#type CodepipelineCustomActionType#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__831674f58210e9ee175858b33598f808cf93d9ef98361885470dee540c7fbbfb)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument required", value=required, expected_type=type_hints["required"])
            check_type(argname="argument secret", value=secret, expected_type=type_hints["secret"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument queryable", value=queryable, expected_type=type_hints["queryable"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
            "name": name,
            "required": required,
            "secret": secret,
        }
        if description is not None:
            self._values["description"] = description
        if queryable is not None:
            self._values["queryable"] = queryable
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def key(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#key CodepipelineCustomActionType#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#name CodepipelineCustomActionType#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def required(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#required CodepipelineCustomActionType#required}.'''
        result = self._values.get("required")
        assert result is not None, "Required property 'required' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    @builtins.property
    def secret(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#secret CodepipelineCustomActionType#secret}.'''
        result = self._values.get("secret")
        assert result is not None, "Required property 'secret' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#description CodepipelineCustomActionType#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def queryable(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#queryable CodepipelineCustomActionType#queryable}.'''
        result = self._values.get("queryable")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#type CodepipelineCustomActionType#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodepipelineCustomActionTypeConfigurationProperty(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodepipelineCustomActionTypeConfigurationPropertyList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.codepipelineCustomActionType.CodepipelineCustomActionTypeConfigurationPropertyList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9f20b203af73fae0a824caefc1096c958a8e6f200ff602cc4814d9cd3062b91e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CodepipelineCustomActionTypeConfigurationPropertyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__30c0ff0438d2cba74ce97fbfa1734dc68ce69567f25e457428fb0d4b5c2643a7)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CodepipelineCustomActionTypeConfigurationPropertyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c51e0cec528f43e240010f84471efe730e1621232ed6b6ecc1bdc61f0a069fb9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b9abc8154207bd83a90439ace1402f1afc0f0ccecadb87892c31cddc16ed962e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__536030b9f1fcffe2b6aca31576b33a420cdc781be3d0d6bc7194e8c3370d7c6e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CodepipelineCustomActionTypeConfigurationProperty]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CodepipelineCustomActionTypeConfigurationProperty]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CodepipelineCustomActionTypeConfigurationProperty]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d7f4d3c1a6f5bc12bbbce7be00cf8da91929af45a8f58ffe6580671c3f13f82)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CodepipelineCustomActionTypeConfigurationPropertyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.codepipelineCustomActionType.CodepipelineCustomActionTypeConfigurationPropertyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__19907f8cf4c5bdd3328a886bd809c9b175617f2050c62313fdd264bfa4c96d62)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetQueryable")
    def reset_queryable(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueryable", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="queryableInput")
    def queryable_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "queryableInput"))

    @builtins.property
    @jsii.member(jsii_name="requiredInput")
    def required_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "requiredInput"))

    @builtins.property
    @jsii.member(jsii_name="secretInput")
    def secret_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "secretInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__622eef6f263253c1182d1aeec3d5ae3312e2ffe8d3386bbf3a8e45002991a818)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "key"))

    @key.setter
    def key(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ee793857e0cd3208c5ec8cfd3e5353dd39b5906533e9c8574ef7fd91983bd25)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bda575048ad82f4763ccd730d427411c2fa65aeeef7b061b5d95ad17b37c35bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="queryable")
    def queryable(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "queryable"))

    @queryable.setter
    def queryable(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c0a34425284b53237ae80ab08ef0a37485bd76adedb0b5ba168f884bf05388e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queryable", value)

    @builtins.property
    @jsii.member(jsii_name="required")
    def required(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "required"))

    @required.setter
    def required(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bfbeb2e060e5d71426534b83d45a74dca0c65ae7ab380a3c695c0fb4601896bf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "required", value)

    @builtins.property
    @jsii.member(jsii_name="secret")
    def secret(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "secret"))

    @secret.setter
    def secret(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__901335210fdafcf938a683ab6a2a1586e40c792341bf0d0d5effa15a991fde2c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secret", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__264308a255ccc5e1b7919e37cb792912016669e3d11834b0956ff3f5a82beab7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CodepipelineCustomActionTypeConfigurationProperty, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CodepipelineCustomActionTypeConfigurationProperty, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CodepipelineCustomActionTypeConfigurationProperty, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__071cdb5429ef8468b8ef7aa63698ac341ede0205f88e6500e3a2c65eb4454a10)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.codepipelineCustomActionType.CodepipelineCustomActionTypeInputArtifactDetails",
    jsii_struct_bases=[],
    name_mapping={"maximum_count": "maximumCount", "minimum_count": "minimumCount"},
)
class CodepipelineCustomActionTypeInputArtifactDetails:
    def __init__(
        self,
        *,
        maximum_count: jsii.Number,
        minimum_count: jsii.Number,
    ) -> None:
        '''
        :param maximum_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#maximum_count CodepipelineCustomActionType#maximum_count}.
        :param minimum_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#minimum_count CodepipelineCustomActionType#minimum_count}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e6dab122b4e73b7a1ca8c8b8de850167329b322d97f46165f6bc5b344901131)
            check_type(argname="argument maximum_count", value=maximum_count, expected_type=type_hints["maximum_count"])
            check_type(argname="argument minimum_count", value=minimum_count, expected_type=type_hints["minimum_count"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "maximum_count": maximum_count,
            "minimum_count": minimum_count,
        }

    @builtins.property
    def maximum_count(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#maximum_count CodepipelineCustomActionType#maximum_count}.'''
        result = self._values.get("maximum_count")
        assert result is not None, "Required property 'maximum_count' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def minimum_count(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#minimum_count CodepipelineCustomActionType#minimum_count}.'''
        result = self._values.get("minimum_count")
        assert result is not None, "Required property 'minimum_count' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodepipelineCustomActionTypeInputArtifactDetails(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodepipelineCustomActionTypeInputArtifactDetailsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.codepipelineCustomActionType.CodepipelineCustomActionTypeInputArtifactDetailsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d6f3dd3fa2df0c7e24c33bcfa16e8da60d04fd595dd2842f62fea369d248e9b2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="maximumCountInput")
    def maximum_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maximumCountInput"))

    @builtins.property
    @jsii.member(jsii_name="minimumCountInput")
    def minimum_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minimumCountInput"))

    @builtins.property
    @jsii.member(jsii_name="maximumCount")
    def maximum_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maximumCount"))

    @maximum_count.setter
    def maximum_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a819788930e4fd0daf70ceb35f234cd8f4e145298f326c24f7149c7f61aeadc0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maximumCount", value)

    @builtins.property
    @jsii.member(jsii_name="minimumCount")
    def minimum_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minimumCount"))

    @minimum_count.setter
    def minimum_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__623d76fd6a095c586a67ac30d843376f8176f63f89f413f1358db7da50b197b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minimumCount", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CodepipelineCustomActionTypeInputArtifactDetails]:
        return typing.cast(typing.Optional[CodepipelineCustomActionTypeInputArtifactDetails], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CodepipelineCustomActionTypeInputArtifactDetails],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f94126239805a543c39130c539521a775231e5528e598dd430041d67d8d52705)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.codepipelineCustomActionType.CodepipelineCustomActionTypeOutputArtifactDetails",
    jsii_struct_bases=[],
    name_mapping={"maximum_count": "maximumCount", "minimum_count": "minimumCount"},
)
class CodepipelineCustomActionTypeOutputArtifactDetails:
    def __init__(
        self,
        *,
        maximum_count: jsii.Number,
        minimum_count: jsii.Number,
    ) -> None:
        '''
        :param maximum_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#maximum_count CodepipelineCustomActionType#maximum_count}.
        :param minimum_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#minimum_count CodepipelineCustomActionType#minimum_count}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ebad31f1fb7233723afa6660ae9bb277250eef8c947ca949e03fe01b18d6e32)
            check_type(argname="argument maximum_count", value=maximum_count, expected_type=type_hints["maximum_count"])
            check_type(argname="argument minimum_count", value=minimum_count, expected_type=type_hints["minimum_count"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "maximum_count": maximum_count,
            "minimum_count": minimum_count,
        }

    @builtins.property
    def maximum_count(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#maximum_count CodepipelineCustomActionType#maximum_count}.'''
        result = self._values.get("maximum_count")
        assert result is not None, "Required property 'maximum_count' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def minimum_count(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#minimum_count CodepipelineCustomActionType#minimum_count}.'''
        result = self._values.get("minimum_count")
        assert result is not None, "Required property 'minimum_count' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodepipelineCustomActionTypeOutputArtifactDetails(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodepipelineCustomActionTypeOutputArtifactDetailsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.codepipelineCustomActionType.CodepipelineCustomActionTypeOutputArtifactDetailsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d83db43a71ba56d05bb575eaa78ef8e3766b03e6c1ca8b8ddff429e3dd74e26d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="maximumCountInput")
    def maximum_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maximumCountInput"))

    @builtins.property
    @jsii.member(jsii_name="minimumCountInput")
    def minimum_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minimumCountInput"))

    @builtins.property
    @jsii.member(jsii_name="maximumCount")
    def maximum_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maximumCount"))

    @maximum_count.setter
    def maximum_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2076176b3b29275fb690af6e6cd6bfe4b870cae7fec415aa1d4c9ac9d388552)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maximumCount", value)

    @builtins.property
    @jsii.member(jsii_name="minimumCount")
    def minimum_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minimumCount"))

    @minimum_count.setter
    def minimum_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f099898a682ffc5e1bdb82b647913f97ca7c92448da99a1a77d4eb6a2a77851)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minimumCount", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CodepipelineCustomActionTypeOutputArtifactDetails]:
        return typing.cast(typing.Optional[CodepipelineCustomActionTypeOutputArtifactDetails], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CodepipelineCustomActionTypeOutputArtifactDetails],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c731e27a7e83f5e8e9f27e07a3369d3e175db04f6b18a25d3e2d0c1d08e3560)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.codepipelineCustomActionType.CodepipelineCustomActionTypeSettings",
    jsii_struct_bases=[],
    name_mapping={
        "entity_url_template": "entityUrlTemplate",
        "execution_url_template": "executionUrlTemplate",
        "revision_url_template": "revisionUrlTemplate",
        "third_party_configuration_url": "thirdPartyConfigurationUrl",
    },
)
class CodepipelineCustomActionTypeSettings:
    def __init__(
        self,
        *,
        entity_url_template: typing.Optional[builtins.str] = None,
        execution_url_template: typing.Optional[builtins.str] = None,
        revision_url_template: typing.Optional[builtins.str] = None,
        third_party_configuration_url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param entity_url_template: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#entity_url_template CodepipelineCustomActionType#entity_url_template}.
        :param execution_url_template: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#execution_url_template CodepipelineCustomActionType#execution_url_template}.
        :param revision_url_template: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#revision_url_template CodepipelineCustomActionType#revision_url_template}.
        :param third_party_configuration_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#third_party_configuration_url CodepipelineCustomActionType#third_party_configuration_url}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08441fe637167bce7624c3cce2801e84a306be0c2cebce5f8dfd9a7cfb9979e4)
            check_type(argname="argument entity_url_template", value=entity_url_template, expected_type=type_hints["entity_url_template"])
            check_type(argname="argument execution_url_template", value=execution_url_template, expected_type=type_hints["execution_url_template"])
            check_type(argname="argument revision_url_template", value=revision_url_template, expected_type=type_hints["revision_url_template"])
            check_type(argname="argument third_party_configuration_url", value=third_party_configuration_url, expected_type=type_hints["third_party_configuration_url"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if entity_url_template is not None:
            self._values["entity_url_template"] = entity_url_template
        if execution_url_template is not None:
            self._values["execution_url_template"] = execution_url_template
        if revision_url_template is not None:
            self._values["revision_url_template"] = revision_url_template
        if third_party_configuration_url is not None:
            self._values["third_party_configuration_url"] = third_party_configuration_url

    @builtins.property
    def entity_url_template(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#entity_url_template CodepipelineCustomActionType#entity_url_template}.'''
        result = self._values.get("entity_url_template")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def execution_url_template(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#execution_url_template CodepipelineCustomActionType#execution_url_template}.'''
        result = self._values.get("execution_url_template")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def revision_url_template(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#revision_url_template CodepipelineCustomActionType#revision_url_template}.'''
        result = self._values.get("revision_url_template")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def third_party_configuration_url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#third_party_configuration_url CodepipelineCustomActionType#third_party_configuration_url}.'''
        result = self._values.get("third_party_configuration_url")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodepipelineCustomActionTypeSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodepipelineCustomActionTypeSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.codepipelineCustomActionType.CodepipelineCustomActionTypeSettingsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b9d32ea7336738c646291983ba5078c1b8111233ee40c74c4764e9614d19132d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEntityUrlTemplate")
    def reset_entity_url_template(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEntityUrlTemplate", []))

    @jsii.member(jsii_name="resetExecutionUrlTemplate")
    def reset_execution_url_template(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExecutionUrlTemplate", []))

    @jsii.member(jsii_name="resetRevisionUrlTemplate")
    def reset_revision_url_template(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRevisionUrlTemplate", []))

    @jsii.member(jsii_name="resetThirdPartyConfigurationUrl")
    def reset_third_party_configuration_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetThirdPartyConfigurationUrl", []))

    @builtins.property
    @jsii.member(jsii_name="entityUrlTemplateInput")
    def entity_url_template_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "entityUrlTemplateInput"))

    @builtins.property
    @jsii.member(jsii_name="executionUrlTemplateInput")
    def execution_url_template_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "executionUrlTemplateInput"))

    @builtins.property
    @jsii.member(jsii_name="revisionUrlTemplateInput")
    def revision_url_template_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "revisionUrlTemplateInput"))

    @builtins.property
    @jsii.member(jsii_name="thirdPartyConfigurationUrlInput")
    def third_party_configuration_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "thirdPartyConfigurationUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="entityUrlTemplate")
    def entity_url_template(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "entityUrlTemplate"))

    @entity_url_template.setter
    def entity_url_template(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57acee6122fb5b9990ced845a00719770c829b8bb875525f26aa72e34dc3722a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "entityUrlTemplate", value)

    @builtins.property
    @jsii.member(jsii_name="executionUrlTemplate")
    def execution_url_template(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "executionUrlTemplate"))

    @execution_url_template.setter
    def execution_url_template(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e83650da8312ed3877e25307b267ce433a650a8f6934b87ef2c97443387cee6c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "executionUrlTemplate", value)

    @builtins.property
    @jsii.member(jsii_name="revisionUrlTemplate")
    def revision_url_template(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "revisionUrlTemplate"))

    @revision_url_template.setter
    def revision_url_template(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fff1d48a14d257301b2dba6f59dc01f1648d6b56cb4bc289d25da70984285bf4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "revisionUrlTemplate", value)

    @builtins.property
    @jsii.member(jsii_name="thirdPartyConfigurationUrl")
    def third_party_configuration_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "thirdPartyConfigurationUrl"))

    @third_party_configuration_url.setter
    def third_party_configuration_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__558c936cdf3eb74fba1951a12a6e2db29fa1a60b9517d49bec93669a60227076)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "thirdPartyConfigurationUrl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CodepipelineCustomActionTypeSettings]:
        return typing.cast(typing.Optional[CodepipelineCustomActionTypeSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CodepipelineCustomActionTypeSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e253528437b36b2979d3a57b2cefb1b0af4a96f3978265ff987a9e3ea28d855)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "CodepipelineCustomActionType",
    "CodepipelineCustomActionTypeConfig",
    "CodepipelineCustomActionTypeConfigurationProperty",
    "CodepipelineCustomActionTypeConfigurationPropertyList",
    "CodepipelineCustomActionTypeConfigurationPropertyOutputReference",
    "CodepipelineCustomActionTypeInputArtifactDetails",
    "CodepipelineCustomActionTypeInputArtifactDetailsOutputReference",
    "CodepipelineCustomActionTypeOutputArtifactDetails",
    "CodepipelineCustomActionTypeOutputArtifactDetailsOutputReference",
    "CodepipelineCustomActionTypeSettings",
    "CodepipelineCustomActionTypeSettingsOutputReference",
]

publication.publish()

def _typecheckingstub__73ad63c8adbf03cef81669b17e8a02a5d697f23a1e5d9031c02674c659a7d2c9(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    category: builtins.str,
    input_artifact_details: typing.Union[CodepipelineCustomActionTypeInputArtifactDetails, typing.Dict[builtins.str, typing.Any]],
    output_artifact_details: typing.Union[CodepipelineCustomActionTypeOutputArtifactDetails, typing.Dict[builtins.str, typing.Any]],
    provider_name: builtins.str,
    version: builtins.str,
    configuration_property: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CodepipelineCustomActionTypeConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]] = None,
    id: typing.Optional[builtins.str] = None,
    settings: typing.Optional[typing.Union[CodepipelineCustomActionTypeSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
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

def _typecheckingstub__05ca6a541d56dfd8fd195b04b1fa76b6885d3932ddce2ae5f77cd55637d7b4af(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CodepipelineCustomActionTypeConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc2c2ea5fc75ec61c9e69b0b42c8098a3f28e57b1017c0f2b5e9ea3d34b04a6d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16ccb0c0c60abe8eb34ea8c76667947b67a060cc82dde4aba3df8ed30ccd9a94(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36c8be18aa694a68d9175468accd68d6404762acaca16ed37663acd09003b44d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0fbd8c6c9fd1c956d14c0e7b00de282dc246c2b30bc66a6313f30e005ca7afce(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__545de1353c22e0e9586c2e544f1eee4f8ac6a302e4c92623403d13d768e94591(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a09b14a6163a78ed2a3c358c3c93052ddc17dc7953ad9b8c13457f8f0554b4b8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c4eecf0318e25b5b6ec826e53094923428fff029f872014adbe12d0a2492337(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    category: builtins.str,
    input_artifact_details: typing.Union[CodepipelineCustomActionTypeInputArtifactDetails, typing.Dict[builtins.str, typing.Any]],
    output_artifact_details: typing.Union[CodepipelineCustomActionTypeOutputArtifactDetails, typing.Dict[builtins.str, typing.Any]],
    provider_name: builtins.str,
    version: builtins.str,
    configuration_property: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CodepipelineCustomActionTypeConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]] = None,
    id: typing.Optional[builtins.str] = None,
    settings: typing.Optional[typing.Union[CodepipelineCustomActionTypeSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__831674f58210e9ee175858b33598f808cf93d9ef98361885470dee540c7fbbfb(
    *,
    key: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    name: builtins.str,
    required: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    secret: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    description: typing.Optional[builtins.str] = None,
    queryable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f20b203af73fae0a824caefc1096c958a8e6f200ff602cc4814d9cd3062b91e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30c0ff0438d2cba74ce97fbfa1734dc68ce69567f25e457428fb0d4b5c2643a7(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c51e0cec528f43e240010f84471efe730e1621232ed6b6ecc1bdc61f0a069fb9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9abc8154207bd83a90439ace1402f1afc0f0ccecadb87892c31cddc16ed962e(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__536030b9f1fcffe2b6aca31576b33a420cdc781be3d0d6bc7194e8c3370d7c6e(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d7f4d3c1a6f5bc12bbbce7be00cf8da91929af45a8f58ffe6580671c3f13f82(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CodepipelineCustomActionTypeConfigurationProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19907f8cf4c5bdd3328a886bd809c9b175617f2050c62313fdd264bfa4c96d62(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__622eef6f263253c1182d1aeec3d5ae3312e2ffe8d3386bbf3a8e45002991a818(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ee793857e0cd3208c5ec8cfd3e5353dd39b5906533e9c8574ef7fd91983bd25(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bda575048ad82f4763ccd730d427411c2fa65aeeef7b061b5d95ad17b37c35bc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c0a34425284b53237ae80ab08ef0a37485bd76adedb0b5ba168f884bf05388e(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bfbeb2e060e5d71426534b83d45a74dca0c65ae7ab380a3c695c0fb4601896bf(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__901335210fdafcf938a683ab6a2a1586e40c792341bf0d0d5effa15a991fde2c(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__264308a255ccc5e1b7919e37cb792912016669e3d11834b0956ff3f5a82beab7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__071cdb5429ef8468b8ef7aa63698ac341ede0205f88e6500e3a2c65eb4454a10(
    value: typing.Optional[typing.Union[CodepipelineCustomActionTypeConfigurationProperty, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e6dab122b4e73b7a1ca8c8b8de850167329b322d97f46165f6bc5b344901131(
    *,
    maximum_count: jsii.Number,
    minimum_count: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6f3dd3fa2df0c7e24c33bcfa16e8da60d04fd595dd2842f62fea369d248e9b2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a819788930e4fd0daf70ceb35f234cd8f4e145298f326c24f7149c7f61aeadc0(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__623d76fd6a095c586a67ac30d843376f8176f63f89f413f1358db7da50b197b1(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f94126239805a543c39130c539521a775231e5528e598dd430041d67d8d52705(
    value: typing.Optional[CodepipelineCustomActionTypeInputArtifactDetails],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ebad31f1fb7233723afa6660ae9bb277250eef8c947ca949e03fe01b18d6e32(
    *,
    maximum_count: jsii.Number,
    minimum_count: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d83db43a71ba56d05bb575eaa78ef8e3766b03e6c1ca8b8ddff429e3dd74e26d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2076176b3b29275fb690af6e6cd6bfe4b870cae7fec415aa1d4c9ac9d388552(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f099898a682ffc5e1bdb82b647913f97ca7c92448da99a1a77d4eb6a2a77851(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c731e27a7e83f5e8e9f27e07a3369d3e175db04f6b18a25d3e2d0c1d08e3560(
    value: typing.Optional[CodepipelineCustomActionTypeOutputArtifactDetails],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08441fe637167bce7624c3cce2801e84a306be0c2cebce5f8dfd9a7cfb9979e4(
    *,
    entity_url_template: typing.Optional[builtins.str] = None,
    execution_url_template: typing.Optional[builtins.str] = None,
    revision_url_template: typing.Optional[builtins.str] = None,
    third_party_configuration_url: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9d32ea7336738c646291983ba5078c1b8111233ee40c74c4764e9614d19132d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57acee6122fb5b9990ced845a00719770c829b8bb875525f26aa72e34dc3722a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e83650da8312ed3877e25307b267ce433a650a8f6934b87ef2c97443387cee6c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fff1d48a14d257301b2dba6f59dc01f1648d6b56cb4bc289d25da70984285bf4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__558c936cdf3eb74fba1951a12a6e2db29fa1a60b9517d49bec93669a60227076(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e253528437b36b2979d3a57b2cefb1b0af4a96f3978265ff987a9e3ea28d855(
    value: typing.Optional[CodepipelineCustomActionTypeSettings],
) -> None:
    """Type checking stubs"""
    pass
