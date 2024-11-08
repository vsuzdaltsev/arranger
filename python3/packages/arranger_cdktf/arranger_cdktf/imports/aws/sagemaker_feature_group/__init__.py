'''
# `aws_sagemaker_feature_group`

Refer to the Terraform Registory for docs: [`aws_sagemaker_feature_group`](https://www.terraform.io/docs/providers/aws/r/sagemaker_feature_group).
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


class SagemakerFeatureGroup(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerFeatureGroup.SagemakerFeatureGroup",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_feature_group aws_sagemaker_feature_group}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        event_time_feature_name: builtins.str,
        feature_definition: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SagemakerFeatureGroupFeatureDefinition", typing.Dict[builtins.str, typing.Any]]]],
        feature_group_name: builtins.str,
        record_identifier_feature_name: builtins.str,
        role_arn: builtins.str,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        offline_store_config: typing.Optional[typing.Union["SagemakerFeatureGroupOfflineStoreConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        online_store_config: typing.Optional[typing.Union["SagemakerFeatureGroupOnlineStoreConfig", typing.Dict[builtins.str, typing.Any]]] = None,
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
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_feature_group aws_sagemaker_feature_group} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param event_time_feature_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_feature_group#event_time_feature_name SagemakerFeatureGroup#event_time_feature_name}.
        :param feature_definition: feature_definition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_feature_group#feature_definition SagemakerFeatureGroup#feature_definition}
        :param feature_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_feature_group#feature_group_name SagemakerFeatureGroup#feature_group_name}.
        :param record_identifier_feature_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_feature_group#record_identifier_feature_name SagemakerFeatureGroup#record_identifier_feature_name}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_feature_group#role_arn SagemakerFeatureGroup#role_arn}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_feature_group#description SagemakerFeatureGroup#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_feature_group#id SagemakerFeatureGroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param offline_store_config: offline_store_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_feature_group#offline_store_config SagemakerFeatureGroup#offline_store_config}
        :param online_store_config: online_store_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_feature_group#online_store_config SagemakerFeatureGroup#online_store_config}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_feature_group#tags SagemakerFeatureGroup#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_feature_group#tags_all SagemakerFeatureGroup#tags_all}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5414136a517f8fa0c8659805fc2c929d22ca9718c4ba6fe9e2d1c8f2c3c5b4c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = SagemakerFeatureGroupConfig(
            event_time_feature_name=event_time_feature_name,
            feature_definition=feature_definition,
            feature_group_name=feature_group_name,
            record_identifier_feature_name=record_identifier_feature_name,
            role_arn=role_arn,
            description=description,
            id=id,
            offline_store_config=offline_store_config,
            online_store_config=online_store_config,
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

    @jsii.member(jsii_name="putFeatureDefinition")
    def put_feature_definition(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SagemakerFeatureGroupFeatureDefinition", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a215231d5f1e290f7635e02eab04ccecfc1d0664b7a5727575ae6c8e1078a850)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putFeatureDefinition", [value]))

    @jsii.member(jsii_name="putOfflineStoreConfig")
    def put_offline_store_config(
        self,
        *,
        s3_storage_config: typing.Union["SagemakerFeatureGroupOfflineStoreConfigS3StorageConfig", typing.Dict[builtins.str, typing.Any]],
        data_catalog_config: typing.Optional[typing.Union["SagemakerFeatureGroupOfflineStoreConfigDataCatalogConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        disable_glue_table_creation: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param s3_storage_config: s3_storage_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_feature_group#s3_storage_config SagemakerFeatureGroup#s3_storage_config}
        :param data_catalog_config: data_catalog_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_feature_group#data_catalog_config SagemakerFeatureGroup#data_catalog_config}
        :param disable_glue_table_creation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_feature_group#disable_glue_table_creation SagemakerFeatureGroup#disable_glue_table_creation}.
        '''
        value = SagemakerFeatureGroupOfflineStoreConfig(
            s3_storage_config=s3_storage_config,
            data_catalog_config=data_catalog_config,
            disable_glue_table_creation=disable_glue_table_creation,
        )

        return typing.cast(None, jsii.invoke(self, "putOfflineStoreConfig", [value]))

    @jsii.member(jsii_name="putOnlineStoreConfig")
    def put_online_store_config(
        self,
        *,
        enable_online_store: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        security_config: typing.Optional[typing.Union["SagemakerFeatureGroupOnlineStoreConfigSecurityConfig", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param enable_online_store: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_feature_group#enable_online_store SagemakerFeatureGroup#enable_online_store}.
        :param security_config: security_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_feature_group#security_config SagemakerFeatureGroup#security_config}
        '''
        value = SagemakerFeatureGroupOnlineStoreConfig(
            enable_online_store=enable_online_store, security_config=security_config
        )

        return typing.cast(None, jsii.invoke(self, "putOnlineStoreConfig", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetOfflineStoreConfig")
    def reset_offline_store_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOfflineStoreConfig", []))

    @jsii.member(jsii_name="resetOnlineStoreConfig")
    def reset_online_store_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOnlineStoreConfig", []))

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
    @jsii.member(jsii_name="featureDefinition")
    def feature_definition(self) -> "SagemakerFeatureGroupFeatureDefinitionList":
        return typing.cast("SagemakerFeatureGroupFeatureDefinitionList", jsii.get(self, "featureDefinition"))

    @builtins.property
    @jsii.member(jsii_name="offlineStoreConfig")
    def offline_store_config(
        self,
    ) -> "SagemakerFeatureGroupOfflineStoreConfigOutputReference":
        return typing.cast("SagemakerFeatureGroupOfflineStoreConfigOutputReference", jsii.get(self, "offlineStoreConfig"))

    @builtins.property
    @jsii.member(jsii_name="onlineStoreConfig")
    def online_store_config(
        self,
    ) -> "SagemakerFeatureGroupOnlineStoreConfigOutputReference":
        return typing.cast("SagemakerFeatureGroupOnlineStoreConfigOutputReference", jsii.get(self, "onlineStoreConfig"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="eventTimeFeatureNameInput")
    def event_time_feature_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "eventTimeFeatureNameInput"))

    @builtins.property
    @jsii.member(jsii_name="featureDefinitionInput")
    def feature_definition_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SagemakerFeatureGroupFeatureDefinition"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SagemakerFeatureGroupFeatureDefinition"]]], jsii.get(self, "featureDefinitionInput"))

    @builtins.property
    @jsii.member(jsii_name="featureGroupNameInput")
    def feature_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "featureGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="offlineStoreConfigInput")
    def offline_store_config_input(
        self,
    ) -> typing.Optional["SagemakerFeatureGroupOfflineStoreConfig"]:
        return typing.cast(typing.Optional["SagemakerFeatureGroupOfflineStoreConfig"], jsii.get(self, "offlineStoreConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="onlineStoreConfigInput")
    def online_store_config_input(
        self,
    ) -> typing.Optional["SagemakerFeatureGroupOnlineStoreConfig"]:
        return typing.cast(typing.Optional["SagemakerFeatureGroupOnlineStoreConfig"], jsii.get(self, "onlineStoreConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="recordIdentifierFeatureNameInput")
    def record_identifier_feature_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "recordIdentifierFeatureNameInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

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
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9fdae966f4bdb3383860438d62282105142452170ccdfe8aab0e98c6b6b5d783)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="eventTimeFeatureName")
    def event_time_feature_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "eventTimeFeatureName"))

    @event_time_feature_name.setter
    def event_time_feature_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7c1deefc8dd0ecade6680d09b66df50d1f68d17cbb46d3b4e70d0045654c8d1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventTimeFeatureName", value)

    @builtins.property
    @jsii.member(jsii_name="featureGroupName")
    def feature_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "featureGroupName"))

    @feature_group_name.setter
    def feature_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b276082402406b1ecd8659a95937a3914217b5121ee5accb40055c854f9e3dc5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "featureGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ff19ff3962cc6935b451a35dc34874ae5db3b6c4a3dd3a1cbcd59a96486d704)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="recordIdentifierFeatureName")
    def record_identifier_feature_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "recordIdentifierFeatureName"))

    @record_identifier_feature_name.setter
    def record_identifier_feature_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__34542618cbbddf01341f37bad2a13a1c3e5428eb7a63a409d5ca98487fe881d3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recordIdentifierFeatureName", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e51c1e26e5ef70af9225bfa6096e72073135c458b53dac11b9172c9ad95663a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a65458ec84dd1cfb48b7d2c583c0ce1db9e718afd38827acc61fecfafee4998f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__88205029ff25f1ae472cd5a7eb886bdd8cdd3ded245ace4709a3d607e158428f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)


@jsii.data_type(
    jsii_type="aws.sagemakerFeatureGroup.SagemakerFeatureGroupConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "event_time_feature_name": "eventTimeFeatureName",
        "feature_definition": "featureDefinition",
        "feature_group_name": "featureGroupName",
        "record_identifier_feature_name": "recordIdentifierFeatureName",
        "role_arn": "roleArn",
        "description": "description",
        "id": "id",
        "offline_store_config": "offlineStoreConfig",
        "online_store_config": "onlineStoreConfig",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class SagemakerFeatureGroupConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        event_time_feature_name: builtins.str,
        feature_definition: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SagemakerFeatureGroupFeatureDefinition", typing.Dict[builtins.str, typing.Any]]]],
        feature_group_name: builtins.str,
        record_identifier_feature_name: builtins.str,
        role_arn: builtins.str,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        offline_store_config: typing.Optional[typing.Union["SagemakerFeatureGroupOfflineStoreConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        online_store_config: typing.Optional[typing.Union["SagemakerFeatureGroupOnlineStoreConfig", typing.Dict[builtins.str, typing.Any]]] = None,
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
        :param event_time_feature_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_feature_group#event_time_feature_name SagemakerFeatureGroup#event_time_feature_name}.
        :param feature_definition: feature_definition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_feature_group#feature_definition SagemakerFeatureGroup#feature_definition}
        :param feature_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_feature_group#feature_group_name SagemakerFeatureGroup#feature_group_name}.
        :param record_identifier_feature_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_feature_group#record_identifier_feature_name SagemakerFeatureGroup#record_identifier_feature_name}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_feature_group#role_arn SagemakerFeatureGroup#role_arn}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_feature_group#description SagemakerFeatureGroup#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_feature_group#id SagemakerFeatureGroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param offline_store_config: offline_store_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_feature_group#offline_store_config SagemakerFeatureGroup#offline_store_config}
        :param online_store_config: online_store_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_feature_group#online_store_config SagemakerFeatureGroup#online_store_config}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_feature_group#tags SagemakerFeatureGroup#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_feature_group#tags_all SagemakerFeatureGroup#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(offline_store_config, dict):
            offline_store_config = SagemakerFeatureGroupOfflineStoreConfig(**offline_store_config)
        if isinstance(online_store_config, dict):
            online_store_config = SagemakerFeatureGroupOnlineStoreConfig(**online_store_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d77bc45b0f69742c9e8aea1bf3b29abfc12e17565910453b4cc3ba07c0d22fc3)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument event_time_feature_name", value=event_time_feature_name, expected_type=type_hints["event_time_feature_name"])
            check_type(argname="argument feature_definition", value=feature_definition, expected_type=type_hints["feature_definition"])
            check_type(argname="argument feature_group_name", value=feature_group_name, expected_type=type_hints["feature_group_name"])
            check_type(argname="argument record_identifier_feature_name", value=record_identifier_feature_name, expected_type=type_hints["record_identifier_feature_name"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument offline_store_config", value=offline_store_config, expected_type=type_hints["offline_store_config"])
            check_type(argname="argument online_store_config", value=online_store_config, expected_type=type_hints["online_store_config"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "event_time_feature_name": event_time_feature_name,
            "feature_definition": feature_definition,
            "feature_group_name": feature_group_name,
            "record_identifier_feature_name": record_identifier_feature_name,
            "role_arn": role_arn,
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
        if description is not None:
            self._values["description"] = description
        if id is not None:
            self._values["id"] = id
        if offline_store_config is not None:
            self._values["offline_store_config"] = offline_store_config
        if online_store_config is not None:
            self._values["online_store_config"] = online_store_config
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
    def event_time_feature_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_feature_group#event_time_feature_name SagemakerFeatureGroup#event_time_feature_name}.'''
        result = self._values.get("event_time_feature_name")
        assert result is not None, "Required property 'event_time_feature_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def feature_definition(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SagemakerFeatureGroupFeatureDefinition"]]:
        '''feature_definition block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_feature_group#feature_definition SagemakerFeatureGroup#feature_definition}
        '''
        result = self._values.get("feature_definition")
        assert result is not None, "Required property 'feature_definition' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SagemakerFeatureGroupFeatureDefinition"]], result)

    @builtins.property
    def feature_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_feature_group#feature_group_name SagemakerFeatureGroup#feature_group_name}.'''
        result = self._values.get("feature_group_name")
        assert result is not None, "Required property 'feature_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def record_identifier_feature_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_feature_group#record_identifier_feature_name SagemakerFeatureGroup#record_identifier_feature_name}.'''
        result = self._values.get("record_identifier_feature_name")
        assert result is not None, "Required property 'record_identifier_feature_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_feature_group#role_arn SagemakerFeatureGroup#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_feature_group#description SagemakerFeatureGroup#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_feature_group#id SagemakerFeatureGroup#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def offline_store_config(
        self,
    ) -> typing.Optional["SagemakerFeatureGroupOfflineStoreConfig"]:
        '''offline_store_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_feature_group#offline_store_config SagemakerFeatureGroup#offline_store_config}
        '''
        result = self._values.get("offline_store_config")
        return typing.cast(typing.Optional["SagemakerFeatureGroupOfflineStoreConfig"], result)

    @builtins.property
    def online_store_config(
        self,
    ) -> typing.Optional["SagemakerFeatureGroupOnlineStoreConfig"]:
        '''online_store_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_feature_group#online_store_config SagemakerFeatureGroup#online_store_config}
        '''
        result = self._values.get("online_store_config")
        return typing.cast(typing.Optional["SagemakerFeatureGroupOnlineStoreConfig"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_feature_group#tags SagemakerFeatureGroup#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_feature_group#tags_all SagemakerFeatureGroup#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerFeatureGroupConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.sagemakerFeatureGroup.SagemakerFeatureGroupFeatureDefinition",
    jsii_struct_bases=[],
    name_mapping={"feature_name": "featureName", "feature_type": "featureType"},
)
class SagemakerFeatureGroupFeatureDefinition:
    def __init__(
        self,
        *,
        feature_name: typing.Optional[builtins.str] = None,
        feature_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param feature_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_feature_group#feature_name SagemakerFeatureGroup#feature_name}.
        :param feature_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_feature_group#feature_type SagemakerFeatureGroup#feature_type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bee70fef910171d5815918967d2537fc93ab8164bb34ed4b1e552d90641ac27f)
            check_type(argname="argument feature_name", value=feature_name, expected_type=type_hints["feature_name"])
            check_type(argname="argument feature_type", value=feature_type, expected_type=type_hints["feature_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if feature_name is not None:
            self._values["feature_name"] = feature_name
        if feature_type is not None:
            self._values["feature_type"] = feature_type

    @builtins.property
    def feature_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_feature_group#feature_name SagemakerFeatureGroup#feature_name}.'''
        result = self._values.get("feature_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def feature_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_feature_group#feature_type SagemakerFeatureGroup#feature_type}.'''
        result = self._values.get("feature_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerFeatureGroupFeatureDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerFeatureGroupFeatureDefinitionList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerFeatureGroup.SagemakerFeatureGroupFeatureDefinitionList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__509f71c17dfb1b62141ada16c3e1c58afe1de273f36a760ef859303c91995756)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "SagemakerFeatureGroupFeatureDefinitionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44796cda71e3a88b2d25c7c41d01bf63ba354ecac1a6bddad13052e4e22edc3e)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SagemakerFeatureGroupFeatureDefinitionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0635ce7245581dc86dc8cb756254244a434c2bfd55f2208a23036e6b9d1281f1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a4c3d199b1f9a5b7060995104e62dd25a4f134ccef81e5187d2fa7d945751dc6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__61079ce656db229090f45c577660361faec11239ea5d4b2ba3917be3ecac5b1e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerFeatureGroupFeatureDefinition]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerFeatureGroupFeatureDefinition]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerFeatureGroupFeatureDefinition]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c404c001388a4ae682a6fe4a9ca3b00bd7b56f52bb7927d484277e9828c127f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SagemakerFeatureGroupFeatureDefinitionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerFeatureGroup.SagemakerFeatureGroupFeatureDefinitionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e6c86e4a758a69bc4728f099ef4360cf54dc7bab18e3e025b640216911e052d5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetFeatureName")
    def reset_feature_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFeatureName", []))

    @jsii.member(jsii_name="resetFeatureType")
    def reset_feature_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFeatureType", []))

    @builtins.property
    @jsii.member(jsii_name="featureNameInput")
    def feature_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "featureNameInput"))

    @builtins.property
    @jsii.member(jsii_name="featureTypeInput")
    def feature_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "featureTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="featureName")
    def feature_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "featureName"))

    @feature_name.setter
    def feature_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c50f38f4d06ceaf9eeb62f48c0412870db568aabdfa3e9f8419e3a5a792541fe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "featureName", value)

    @builtins.property
    @jsii.member(jsii_name="featureType")
    def feature_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "featureType"))

    @feature_type.setter
    def feature_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__65a30c4e167f8c796efb66a7259fb2766eb803d975041543b8929d59403201a4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "featureType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SagemakerFeatureGroupFeatureDefinition, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SagemakerFeatureGroupFeatureDefinition, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SagemakerFeatureGroupFeatureDefinition, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd9145c95e51c2a77e76856c3b49c77ab7b2be1929c4e692da8111555480dbc6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.sagemakerFeatureGroup.SagemakerFeatureGroupOfflineStoreConfig",
    jsii_struct_bases=[],
    name_mapping={
        "s3_storage_config": "s3StorageConfig",
        "data_catalog_config": "dataCatalogConfig",
        "disable_glue_table_creation": "disableGlueTableCreation",
    },
)
class SagemakerFeatureGroupOfflineStoreConfig:
    def __init__(
        self,
        *,
        s3_storage_config: typing.Union["SagemakerFeatureGroupOfflineStoreConfigS3StorageConfig", typing.Dict[builtins.str, typing.Any]],
        data_catalog_config: typing.Optional[typing.Union["SagemakerFeatureGroupOfflineStoreConfigDataCatalogConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        disable_glue_table_creation: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param s3_storage_config: s3_storage_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_feature_group#s3_storage_config SagemakerFeatureGroup#s3_storage_config}
        :param data_catalog_config: data_catalog_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_feature_group#data_catalog_config SagemakerFeatureGroup#data_catalog_config}
        :param disable_glue_table_creation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_feature_group#disable_glue_table_creation SagemakerFeatureGroup#disable_glue_table_creation}.
        '''
        if isinstance(s3_storage_config, dict):
            s3_storage_config = SagemakerFeatureGroupOfflineStoreConfigS3StorageConfig(**s3_storage_config)
        if isinstance(data_catalog_config, dict):
            data_catalog_config = SagemakerFeatureGroupOfflineStoreConfigDataCatalogConfig(**data_catalog_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__058f0983bc0deefa1eb80701b3c07388041b9699c8eaa52c46295edf938b00ae)
            check_type(argname="argument s3_storage_config", value=s3_storage_config, expected_type=type_hints["s3_storage_config"])
            check_type(argname="argument data_catalog_config", value=data_catalog_config, expected_type=type_hints["data_catalog_config"])
            check_type(argname="argument disable_glue_table_creation", value=disable_glue_table_creation, expected_type=type_hints["disable_glue_table_creation"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "s3_storage_config": s3_storage_config,
        }
        if data_catalog_config is not None:
            self._values["data_catalog_config"] = data_catalog_config
        if disable_glue_table_creation is not None:
            self._values["disable_glue_table_creation"] = disable_glue_table_creation

    @builtins.property
    def s3_storage_config(
        self,
    ) -> "SagemakerFeatureGroupOfflineStoreConfigS3StorageConfig":
        '''s3_storage_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_feature_group#s3_storage_config SagemakerFeatureGroup#s3_storage_config}
        '''
        result = self._values.get("s3_storage_config")
        assert result is not None, "Required property 's3_storage_config' is missing"
        return typing.cast("SagemakerFeatureGroupOfflineStoreConfigS3StorageConfig", result)

    @builtins.property
    def data_catalog_config(
        self,
    ) -> typing.Optional["SagemakerFeatureGroupOfflineStoreConfigDataCatalogConfig"]:
        '''data_catalog_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_feature_group#data_catalog_config SagemakerFeatureGroup#data_catalog_config}
        '''
        result = self._values.get("data_catalog_config")
        return typing.cast(typing.Optional["SagemakerFeatureGroupOfflineStoreConfigDataCatalogConfig"], result)

    @builtins.property
    def disable_glue_table_creation(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_feature_group#disable_glue_table_creation SagemakerFeatureGroup#disable_glue_table_creation}.'''
        result = self._values.get("disable_glue_table_creation")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerFeatureGroupOfflineStoreConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.sagemakerFeatureGroup.SagemakerFeatureGroupOfflineStoreConfigDataCatalogConfig",
    jsii_struct_bases=[],
    name_mapping={
        "catalog": "catalog",
        "database": "database",
        "table_name": "tableName",
    },
)
class SagemakerFeatureGroupOfflineStoreConfigDataCatalogConfig:
    def __init__(
        self,
        *,
        catalog: typing.Optional[builtins.str] = None,
        database: typing.Optional[builtins.str] = None,
        table_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param catalog: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_feature_group#catalog SagemakerFeatureGroup#catalog}.
        :param database: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_feature_group#database SagemakerFeatureGroup#database}.
        :param table_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_feature_group#table_name SagemakerFeatureGroup#table_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d645e4403c6835c31e20c83afe5c9226461654bb5b3e967717bdf89eea543ff4)
            check_type(argname="argument catalog", value=catalog, expected_type=type_hints["catalog"])
            check_type(argname="argument database", value=database, expected_type=type_hints["database"])
            check_type(argname="argument table_name", value=table_name, expected_type=type_hints["table_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if catalog is not None:
            self._values["catalog"] = catalog
        if database is not None:
            self._values["database"] = database
        if table_name is not None:
            self._values["table_name"] = table_name

    @builtins.property
    def catalog(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_feature_group#catalog SagemakerFeatureGroup#catalog}.'''
        result = self._values.get("catalog")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def database(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_feature_group#database SagemakerFeatureGroup#database}.'''
        result = self._values.get("database")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def table_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_feature_group#table_name SagemakerFeatureGroup#table_name}.'''
        result = self._values.get("table_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerFeatureGroupOfflineStoreConfigDataCatalogConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerFeatureGroupOfflineStoreConfigDataCatalogConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerFeatureGroup.SagemakerFeatureGroupOfflineStoreConfigDataCatalogConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__16aa00e7495a107027694b9d3928bdaf9bf8ea8ac57c6fe844d30a0a1de96e04)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCatalog")
    def reset_catalog(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCatalog", []))

    @jsii.member(jsii_name="resetDatabase")
    def reset_database(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatabase", []))

    @jsii.member(jsii_name="resetTableName")
    def reset_table_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTableName", []))

    @builtins.property
    @jsii.member(jsii_name="catalogInput")
    def catalog_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "catalogInput"))

    @builtins.property
    @jsii.member(jsii_name="databaseInput")
    def database_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseInput"))

    @builtins.property
    @jsii.member(jsii_name="tableNameInput")
    def table_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tableNameInput"))

    @builtins.property
    @jsii.member(jsii_name="catalog")
    def catalog(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "catalog"))

    @catalog.setter
    def catalog(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c303c9018c9a1b95fbc7b8ddcda498509737a7aa7e40d63ad2adf19fcbdab46)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "catalog", value)

    @builtins.property
    @jsii.member(jsii_name="database")
    def database(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "database"))

    @database.setter
    def database(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95cee81e0524a840448c854cbaa72208262449c9b0cab7caab138c204972ef5a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "database", value)

    @builtins.property
    @jsii.member(jsii_name="tableName")
    def table_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tableName"))

    @table_name.setter
    def table_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3862e2211e202dc10cda2aaed8dae5b83634f7f71193f206fd0f073268d21eb3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tableName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerFeatureGroupOfflineStoreConfigDataCatalogConfig]:
        return typing.cast(typing.Optional[SagemakerFeatureGroupOfflineStoreConfigDataCatalogConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerFeatureGroupOfflineStoreConfigDataCatalogConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9fc27c47e02f2125aa0a1cc15daeb439d2110269cbc17fef25f0d91c70524454)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SagemakerFeatureGroupOfflineStoreConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerFeatureGroup.SagemakerFeatureGroupOfflineStoreConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d49a3c5a2652c76b3b336838ffddf421b53e895a08bd51dc50f7bdefca1ba049)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDataCatalogConfig")
    def put_data_catalog_config(
        self,
        *,
        catalog: typing.Optional[builtins.str] = None,
        database: typing.Optional[builtins.str] = None,
        table_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param catalog: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_feature_group#catalog SagemakerFeatureGroup#catalog}.
        :param database: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_feature_group#database SagemakerFeatureGroup#database}.
        :param table_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_feature_group#table_name SagemakerFeatureGroup#table_name}.
        '''
        value = SagemakerFeatureGroupOfflineStoreConfigDataCatalogConfig(
            catalog=catalog, database=database, table_name=table_name
        )

        return typing.cast(None, jsii.invoke(self, "putDataCatalogConfig", [value]))

    @jsii.member(jsii_name="putS3StorageConfig")
    def put_s3_storage_config(
        self,
        *,
        s3_uri: builtins.str,
        kms_key_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param s3_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_feature_group#s3_uri SagemakerFeatureGroup#s3_uri}.
        :param kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_feature_group#kms_key_id SagemakerFeatureGroup#kms_key_id}.
        '''
        value = SagemakerFeatureGroupOfflineStoreConfigS3StorageConfig(
            s3_uri=s3_uri, kms_key_id=kms_key_id
        )

        return typing.cast(None, jsii.invoke(self, "putS3StorageConfig", [value]))

    @jsii.member(jsii_name="resetDataCatalogConfig")
    def reset_data_catalog_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataCatalogConfig", []))

    @jsii.member(jsii_name="resetDisableGlueTableCreation")
    def reset_disable_glue_table_creation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisableGlueTableCreation", []))

    @builtins.property
    @jsii.member(jsii_name="dataCatalogConfig")
    def data_catalog_config(
        self,
    ) -> SagemakerFeatureGroupOfflineStoreConfigDataCatalogConfigOutputReference:
        return typing.cast(SagemakerFeatureGroupOfflineStoreConfigDataCatalogConfigOutputReference, jsii.get(self, "dataCatalogConfig"))

    @builtins.property
    @jsii.member(jsii_name="s3StorageConfig")
    def s3_storage_config(
        self,
    ) -> "SagemakerFeatureGroupOfflineStoreConfigS3StorageConfigOutputReference":
        return typing.cast("SagemakerFeatureGroupOfflineStoreConfigS3StorageConfigOutputReference", jsii.get(self, "s3StorageConfig"))

    @builtins.property
    @jsii.member(jsii_name="dataCatalogConfigInput")
    def data_catalog_config_input(
        self,
    ) -> typing.Optional[SagemakerFeatureGroupOfflineStoreConfigDataCatalogConfig]:
        return typing.cast(typing.Optional[SagemakerFeatureGroupOfflineStoreConfigDataCatalogConfig], jsii.get(self, "dataCatalogConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="disableGlueTableCreationInput")
    def disable_glue_table_creation_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "disableGlueTableCreationInput"))

    @builtins.property
    @jsii.member(jsii_name="s3StorageConfigInput")
    def s3_storage_config_input(
        self,
    ) -> typing.Optional["SagemakerFeatureGroupOfflineStoreConfigS3StorageConfig"]:
        return typing.cast(typing.Optional["SagemakerFeatureGroupOfflineStoreConfigS3StorageConfig"], jsii.get(self, "s3StorageConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="disableGlueTableCreation")
    def disable_glue_table_creation(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "disableGlueTableCreation"))

    @disable_glue_table_creation.setter
    def disable_glue_table_creation(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9be490cdc33e3c7330aa01c0d66cc67da61c9ac06739d1229e8ad2f00e53f58e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableGlueTableCreation", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerFeatureGroupOfflineStoreConfig]:
        return typing.cast(typing.Optional[SagemakerFeatureGroupOfflineStoreConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerFeatureGroupOfflineStoreConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea7e5a93dc202abccecedd8dff22f5afce8bade1f7d97fadd565a6c475cdf4c0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.sagemakerFeatureGroup.SagemakerFeatureGroupOfflineStoreConfigS3StorageConfig",
    jsii_struct_bases=[],
    name_mapping={"s3_uri": "s3Uri", "kms_key_id": "kmsKeyId"},
)
class SagemakerFeatureGroupOfflineStoreConfigS3StorageConfig:
    def __init__(
        self,
        *,
        s3_uri: builtins.str,
        kms_key_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param s3_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_feature_group#s3_uri SagemakerFeatureGroup#s3_uri}.
        :param kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_feature_group#kms_key_id SagemakerFeatureGroup#kms_key_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7419876d1fb6ea60a09e67d0bac99b15aed0732441801f9e39df647029171ad0)
            check_type(argname="argument s3_uri", value=s3_uri, expected_type=type_hints["s3_uri"])
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "s3_uri": s3_uri,
        }
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id

    @builtins.property
    def s3_uri(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_feature_group#s3_uri SagemakerFeatureGroup#s3_uri}.'''
        result = self._values.get("s3_uri")
        assert result is not None, "Required property 's3_uri' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_feature_group#kms_key_id SagemakerFeatureGroup#kms_key_id}.'''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerFeatureGroupOfflineStoreConfigS3StorageConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerFeatureGroupOfflineStoreConfigS3StorageConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerFeatureGroup.SagemakerFeatureGroupOfflineStoreConfigS3StorageConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__74290d0a807a4e954b90bf956197beeebf5e6811036e6d3b7c7f7411f26bfa69)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetKmsKeyId")
    def reset_kms_key_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKeyId", []))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyIdInput")
    def kms_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="s3UriInput")
    def s3_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "s3UriInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1da60ac4e25fc47138f236351e60fac22922ba6c69c3e4cec9d264dea84c0266)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="s3Uri")
    def s3_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "s3Uri"))

    @s3_uri.setter
    def s3_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a7e9ae99238bad4e0687006aa99fe16e465a7b7ea475fe82bd7cf9ea39bb1a1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3Uri", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerFeatureGroupOfflineStoreConfigS3StorageConfig]:
        return typing.cast(typing.Optional[SagemakerFeatureGroupOfflineStoreConfigS3StorageConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerFeatureGroupOfflineStoreConfigS3StorageConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f5200fe2e6c8559f9210c56901350abeeb615bae58b8ad8efd79e4ac08bd9b7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.sagemakerFeatureGroup.SagemakerFeatureGroupOnlineStoreConfig",
    jsii_struct_bases=[],
    name_mapping={
        "enable_online_store": "enableOnlineStore",
        "security_config": "securityConfig",
    },
)
class SagemakerFeatureGroupOnlineStoreConfig:
    def __init__(
        self,
        *,
        enable_online_store: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        security_config: typing.Optional[typing.Union["SagemakerFeatureGroupOnlineStoreConfigSecurityConfig", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param enable_online_store: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_feature_group#enable_online_store SagemakerFeatureGroup#enable_online_store}.
        :param security_config: security_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_feature_group#security_config SagemakerFeatureGroup#security_config}
        '''
        if isinstance(security_config, dict):
            security_config = SagemakerFeatureGroupOnlineStoreConfigSecurityConfig(**security_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f7440024893129c29bebd60d09445eed96f78c85d36fa9dc7186235dc8ca8b8)
            check_type(argname="argument enable_online_store", value=enable_online_store, expected_type=type_hints["enable_online_store"])
            check_type(argname="argument security_config", value=security_config, expected_type=type_hints["security_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if enable_online_store is not None:
            self._values["enable_online_store"] = enable_online_store
        if security_config is not None:
            self._values["security_config"] = security_config

    @builtins.property
    def enable_online_store(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_feature_group#enable_online_store SagemakerFeatureGroup#enable_online_store}.'''
        result = self._values.get("enable_online_store")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def security_config(
        self,
    ) -> typing.Optional["SagemakerFeatureGroupOnlineStoreConfigSecurityConfig"]:
        '''security_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_feature_group#security_config SagemakerFeatureGroup#security_config}
        '''
        result = self._values.get("security_config")
        return typing.cast(typing.Optional["SagemakerFeatureGroupOnlineStoreConfigSecurityConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerFeatureGroupOnlineStoreConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerFeatureGroupOnlineStoreConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerFeatureGroup.SagemakerFeatureGroupOnlineStoreConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__89ef5df0e7cdda55725ee60a8eae546eee7e7b8d826906dacc3c365cfbea5c6d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putSecurityConfig")
    def put_security_config(
        self,
        *,
        kms_key_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_feature_group#kms_key_id SagemakerFeatureGroup#kms_key_id}.
        '''
        value = SagemakerFeatureGroupOnlineStoreConfigSecurityConfig(
            kms_key_id=kms_key_id
        )

        return typing.cast(None, jsii.invoke(self, "putSecurityConfig", [value]))

    @jsii.member(jsii_name="resetEnableOnlineStore")
    def reset_enable_online_store(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableOnlineStore", []))

    @jsii.member(jsii_name="resetSecurityConfig")
    def reset_security_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecurityConfig", []))

    @builtins.property
    @jsii.member(jsii_name="securityConfig")
    def security_config(
        self,
    ) -> "SagemakerFeatureGroupOnlineStoreConfigSecurityConfigOutputReference":
        return typing.cast("SagemakerFeatureGroupOnlineStoreConfigSecurityConfigOutputReference", jsii.get(self, "securityConfig"))

    @builtins.property
    @jsii.member(jsii_name="enableOnlineStoreInput")
    def enable_online_store_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableOnlineStoreInput"))

    @builtins.property
    @jsii.member(jsii_name="securityConfigInput")
    def security_config_input(
        self,
    ) -> typing.Optional["SagemakerFeatureGroupOnlineStoreConfigSecurityConfig"]:
        return typing.cast(typing.Optional["SagemakerFeatureGroupOnlineStoreConfigSecurityConfig"], jsii.get(self, "securityConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="enableOnlineStore")
    def enable_online_store(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enableOnlineStore"))

    @enable_online_store.setter
    def enable_online_store(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3c11dcfd0a0800fb709b52dace3cfdfe0f5d1595f999992a4e48d106374f45b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableOnlineStore", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SagemakerFeatureGroupOnlineStoreConfig]:
        return typing.cast(typing.Optional[SagemakerFeatureGroupOnlineStoreConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerFeatureGroupOnlineStoreConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0051989030db1f905d16b6a152171db32b76b63a1d61dfb2807df07eb251c5b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.sagemakerFeatureGroup.SagemakerFeatureGroupOnlineStoreConfigSecurityConfig",
    jsii_struct_bases=[],
    name_mapping={"kms_key_id": "kmsKeyId"},
)
class SagemakerFeatureGroupOnlineStoreConfigSecurityConfig:
    def __init__(self, *, kms_key_id: typing.Optional[builtins.str] = None) -> None:
        '''
        :param kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_feature_group#kms_key_id SagemakerFeatureGroup#kms_key_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2223fa04f21f1bc32ae8bf5b285f0ff7393342a27c932f42e08c3fa34ed74c1a)
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_feature_group#kms_key_id SagemakerFeatureGroup#kms_key_id}.'''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerFeatureGroupOnlineStoreConfigSecurityConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerFeatureGroupOnlineStoreConfigSecurityConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerFeatureGroup.SagemakerFeatureGroupOnlineStoreConfigSecurityConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1ac599c5e79f345c117d9e3b615dd4e1eb285d4422d173cc1d6828dc45c7e687)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetKmsKeyId")
    def reset_kms_key_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKeyId", []))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyIdInput")
    def kms_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c3302a8d6b4a45955a9afaab943aa1d4ddf61a7c49989b86673e9f2b37ae48a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerFeatureGroupOnlineStoreConfigSecurityConfig]:
        return typing.cast(typing.Optional[SagemakerFeatureGroupOnlineStoreConfigSecurityConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerFeatureGroupOnlineStoreConfigSecurityConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b5426b5fc26d076f3d2dd3ee6d7ceebbd35e68ca272b7251af1c8e939506839)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "SagemakerFeatureGroup",
    "SagemakerFeatureGroupConfig",
    "SagemakerFeatureGroupFeatureDefinition",
    "SagemakerFeatureGroupFeatureDefinitionList",
    "SagemakerFeatureGroupFeatureDefinitionOutputReference",
    "SagemakerFeatureGroupOfflineStoreConfig",
    "SagemakerFeatureGroupOfflineStoreConfigDataCatalogConfig",
    "SagemakerFeatureGroupOfflineStoreConfigDataCatalogConfigOutputReference",
    "SagemakerFeatureGroupOfflineStoreConfigOutputReference",
    "SagemakerFeatureGroupOfflineStoreConfigS3StorageConfig",
    "SagemakerFeatureGroupOfflineStoreConfigS3StorageConfigOutputReference",
    "SagemakerFeatureGroupOnlineStoreConfig",
    "SagemakerFeatureGroupOnlineStoreConfigOutputReference",
    "SagemakerFeatureGroupOnlineStoreConfigSecurityConfig",
    "SagemakerFeatureGroupOnlineStoreConfigSecurityConfigOutputReference",
]

publication.publish()

def _typecheckingstub__a5414136a517f8fa0c8659805fc2c929d22ca9718c4ba6fe9e2d1c8f2c3c5b4c(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    event_time_feature_name: builtins.str,
    feature_definition: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerFeatureGroupFeatureDefinition, typing.Dict[builtins.str, typing.Any]]]],
    feature_group_name: builtins.str,
    record_identifier_feature_name: builtins.str,
    role_arn: builtins.str,
    description: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    offline_store_config: typing.Optional[typing.Union[SagemakerFeatureGroupOfflineStoreConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    online_store_config: typing.Optional[typing.Union[SagemakerFeatureGroupOnlineStoreConfig, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__a215231d5f1e290f7635e02eab04ccecfc1d0664b7a5727575ae6c8e1078a850(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerFeatureGroupFeatureDefinition, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9fdae966f4bdb3383860438d62282105142452170ccdfe8aab0e98c6b6b5d783(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7c1deefc8dd0ecade6680d09b66df50d1f68d17cbb46d3b4e70d0045654c8d1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b276082402406b1ecd8659a95937a3914217b5121ee5accb40055c854f9e3dc5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ff19ff3962cc6935b451a35dc34874ae5db3b6c4a3dd3a1cbcd59a96486d704(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34542618cbbddf01341f37bad2a13a1c3e5428eb7a63a409d5ca98487fe881d3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e51c1e26e5ef70af9225bfa6096e72073135c458b53dac11b9172c9ad95663a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a65458ec84dd1cfb48b7d2c583c0ce1db9e718afd38827acc61fecfafee4998f(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88205029ff25f1ae472cd5a7eb886bdd8cdd3ded245ace4709a3d607e158428f(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d77bc45b0f69742c9e8aea1bf3b29abfc12e17565910453b4cc3ba07c0d22fc3(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    event_time_feature_name: builtins.str,
    feature_definition: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerFeatureGroupFeatureDefinition, typing.Dict[builtins.str, typing.Any]]]],
    feature_group_name: builtins.str,
    record_identifier_feature_name: builtins.str,
    role_arn: builtins.str,
    description: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    offline_store_config: typing.Optional[typing.Union[SagemakerFeatureGroupOfflineStoreConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    online_store_config: typing.Optional[typing.Union[SagemakerFeatureGroupOnlineStoreConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bee70fef910171d5815918967d2537fc93ab8164bb34ed4b1e552d90641ac27f(
    *,
    feature_name: typing.Optional[builtins.str] = None,
    feature_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__509f71c17dfb1b62141ada16c3e1c58afe1de273f36a760ef859303c91995756(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44796cda71e3a88b2d25c7c41d01bf63ba354ecac1a6bddad13052e4e22edc3e(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0635ce7245581dc86dc8cb756254244a434c2bfd55f2208a23036e6b9d1281f1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4c3d199b1f9a5b7060995104e62dd25a4f134ccef81e5187d2fa7d945751dc6(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61079ce656db229090f45c577660361faec11239ea5d4b2ba3917be3ecac5b1e(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c404c001388a4ae682a6fe4a9ca3b00bd7b56f52bb7927d484277e9828c127f(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerFeatureGroupFeatureDefinition]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6c86e4a758a69bc4728f099ef4360cf54dc7bab18e3e025b640216911e052d5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c50f38f4d06ceaf9eeb62f48c0412870db568aabdfa3e9f8419e3a5a792541fe(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65a30c4e167f8c796efb66a7259fb2766eb803d975041543b8929d59403201a4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd9145c95e51c2a77e76856c3b49c77ab7b2be1929c4e692da8111555480dbc6(
    value: typing.Optional[typing.Union[SagemakerFeatureGroupFeatureDefinition, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__058f0983bc0deefa1eb80701b3c07388041b9699c8eaa52c46295edf938b00ae(
    *,
    s3_storage_config: typing.Union[SagemakerFeatureGroupOfflineStoreConfigS3StorageConfig, typing.Dict[builtins.str, typing.Any]],
    data_catalog_config: typing.Optional[typing.Union[SagemakerFeatureGroupOfflineStoreConfigDataCatalogConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    disable_glue_table_creation: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d645e4403c6835c31e20c83afe5c9226461654bb5b3e967717bdf89eea543ff4(
    *,
    catalog: typing.Optional[builtins.str] = None,
    database: typing.Optional[builtins.str] = None,
    table_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16aa00e7495a107027694b9d3928bdaf9bf8ea8ac57c6fe844d30a0a1de96e04(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c303c9018c9a1b95fbc7b8ddcda498509737a7aa7e40d63ad2adf19fcbdab46(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95cee81e0524a840448c854cbaa72208262449c9b0cab7caab138c204972ef5a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3862e2211e202dc10cda2aaed8dae5b83634f7f71193f206fd0f073268d21eb3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9fc27c47e02f2125aa0a1cc15daeb439d2110269cbc17fef25f0d91c70524454(
    value: typing.Optional[SagemakerFeatureGroupOfflineStoreConfigDataCatalogConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d49a3c5a2652c76b3b336838ffddf421b53e895a08bd51dc50f7bdefca1ba049(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9be490cdc33e3c7330aa01c0d66cc67da61c9ac06739d1229e8ad2f00e53f58e(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea7e5a93dc202abccecedd8dff22f5afce8bade1f7d97fadd565a6c475cdf4c0(
    value: typing.Optional[SagemakerFeatureGroupOfflineStoreConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7419876d1fb6ea60a09e67d0bac99b15aed0732441801f9e39df647029171ad0(
    *,
    s3_uri: builtins.str,
    kms_key_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74290d0a807a4e954b90bf956197beeebf5e6811036e6d3b7c7f7411f26bfa69(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1da60ac4e25fc47138f236351e60fac22922ba6c69c3e4cec9d264dea84c0266(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a7e9ae99238bad4e0687006aa99fe16e465a7b7ea475fe82bd7cf9ea39bb1a1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f5200fe2e6c8559f9210c56901350abeeb615bae58b8ad8efd79e4ac08bd9b7(
    value: typing.Optional[SagemakerFeatureGroupOfflineStoreConfigS3StorageConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f7440024893129c29bebd60d09445eed96f78c85d36fa9dc7186235dc8ca8b8(
    *,
    enable_online_store: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    security_config: typing.Optional[typing.Union[SagemakerFeatureGroupOnlineStoreConfigSecurityConfig, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89ef5df0e7cdda55725ee60a8eae546eee7e7b8d826906dacc3c365cfbea5c6d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3c11dcfd0a0800fb709b52dace3cfdfe0f5d1595f999992a4e48d106374f45b(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0051989030db1f905d16b6a152171db32b76b63a1d61dfb2807df07eb251c5b1(
    value: typing.Optional[SagemakerFeatureGroupOnlineStoreConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2223fa04f21f1bc32ae8bf5b285f0ff7393342a27c932f42e08c3fa34ed74c1a(
    *,
    kms_key_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ac599c5e79f345c117d9e3b615dd4e1eb285d4422d173cc1d6828dc45c7e687(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c3302a8d6b4a45955a9afaab943aa1d4ddf61a7c49989b86673e9f2b37ae48a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b5426b5fc26d076f3d2dd3ee6d7ceebbd35e68ca272b7251af1c8e939506839(
    value: typing.Optional[SagemakerFeatureGroupOnlineStoreConfigSecurityConfig],
) -> None:
    """Type checking stubs"""
    pass
