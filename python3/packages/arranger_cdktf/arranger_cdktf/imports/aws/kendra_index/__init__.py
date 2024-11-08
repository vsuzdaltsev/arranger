'''
# `aws_kendra_index`

Refer to the Terraform Registory for docs: [`aws_kendra_index`](https://www.terraform.io/docs/providers/aws/r/kendra_index).
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


class KendraIndex(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kendraIndex.KendraIndex",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/kendra_index aws_kendra_index}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        role_arn: builtins.str,
        capacity_units: typing.Optional[typing.Union["KendraIndexCapacityUnits", typing.Dict[builtins.str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        document_metadata_configuration_updates: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KendraIndexDocumentMetadataConfigurationUpdates", typing.Dict[builtins.str, typing.Any]]]]] = None,
        edition: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        server_side_encryption_configuration: typing.Optional[typing.Union["KendraIndexServerSideEncryptionConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["KendraIndexTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        user_context_policy: typing.Optional[builtins.str] = None,
        user_group_resolution_configuration: typing.Optional[typing.Union["KendraIndexUserGroupResolutionConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        user_token_configurations: typing.Optional[typing.Union["KendraIndexUserTokenConfigurations", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/kendra_index aws_kendra_index} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#name KendraIndex#name}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#role_arn KendraIndex#role_arn}.
        :param capacity_units: capacity_units block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#capacity_units KendraIndex#capacity_units}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#description KendraIndex#description}.
        :param document_metadata_configuration_updates: document_metadata_configuration_updates block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#document_metadata_configuration_updates KendraIndex#document_metadata_configuration_updates}
        :param edition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#edition KendraIndex#edition}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#id KendraIndex#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param server_side_encryption_configuration: server_side_encryption_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#server_side_encryption_configuration KendraIndex#server_side_encryption_configuration}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#tags KendraIndex#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#tags_all KendraIndex#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#timeouts KendraIndex#timeouts}
        :param user_context_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#user_context_policy KendraIndex#user_context_policy}.
        :param user_group_resolution_configuration: user_group_resolution_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#user_group_resolution_configuration KendraIndex#user_group_resolution_configuration}
        :param user_token_configurations: user_token_configurations block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#user_token_configurations KendraIndex#user_token_configurations}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6cc05f833374c9542a540232dbe21c7cc75295c7e5f244fc02b3c722af1efae7)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = KendraIndexConfig(
            name=name,
            role_arn=role_arn,
            capacity_units=capacity_units,
            description=description,
            document_metadata_configuration_updates=document_metadata_configuration_updates,
            edition=edition,
            id=id,
            server_side_encryption_configuration=server_side_encryption_configuration,
            tags=tags,
            tags_all=tags_all,
            timeouts=timeouts,
            user_context_policy=user_context_policy,
            user_group_resolution_configuration=user_group_resolution_configuration,
            user_token_configurations=user_token_configurations,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putCapacityUnits")
    def put_capacity_units(
        self,
        *,
        query_capacity_units: typing.Optional[jsii.Number] = None,
        storage_capacity_units: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param query_capacity_units: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#query_capacity_units KendraIndex#query_capacity_units}.
        :param storage_capacity_units: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#storage_capacity_units KendraIndex#storage_capacity_units}.
        '''
        value = KendraIndexCapacityUnits(
            query_capacity_units=query_capacity_units,
            storage_capacity_units=storage_capacity_units,
        )

        return typing.cast(None, jsii.invoke(self, "putCapacityUnits", [value]))

    @jsii.member(jsii_name="putDocumentMetadataConfigurationUpdates")
    def put_document_metadata_configuration_updates(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KendraIndexDocumentMetadataConfigurationUpdates", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__317ad6c0ec67af5355f527272eb05a40e5ca24d96fa415da39ac8a37c7537b9f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDocumentMetadataConfigurationUpdates", [value]))

    @jsii.member(jsii_name="putServerSideEncryptionConfiguration")
    def put_server_side_encryption_configuration(
        self,
        *,
        kms_key_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#kms_key_id KendraIndex#kms_key_id}.
        '''
        value = KendraIndexServerSideEncryptionConfiguration(kms_key_id=kms_key_id)

        return typing.cast(None, jsii.invoke(self, "putServerSideEncryptionConfiguration", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#create KendraIndex#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#delete KendraIndex#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#update KendraIndex#update}.
        '''
        value = KendraIndexTimeouts(create=create, delete=delete, update=update)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putUserGroupResolutionConfiguration")
    def put_user_group_resolution_configuration(
        self,
        *,
        user_group_resolution_mode: builtins.str,
    ) -> None:
        '''
        :param user_group_resolution_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#user_group_resolution_mode KendraIndex#user_group_resolution_mode}.
        '''
        value = KendraIndexUserGroupResolutionConfiguration(
            user_group_resolution_mode=user_group_resolution_mode
        )

        return typing.cast(None, jsii.invoke(self, "putUserGroupResolutionConfiguration", [value]))

    @jsii.member(jsii_name="putUserTokenConfigurations")
    def put_user_token_configurations(
        self,
        *,
        json_token_type_configuration: typing.Optional[typing.Union["KendraIndexUserTokenConfigurationsJsonTokenTypeConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        jwt_token_type_configuration: typing.Optional[typing.Union["KendraIndexUserTokenConfigurationsJwtTokenTypeConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param json_token_type_configuration: json_token_type_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#json_token_type_configuration KendraIndex#json_token_type_configuration}
        :param jwt_token_type_configuration: jwt_token_type_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#jwt_token_type_configuration KendraIndex#jwt_token_type_configuration}
        '''
        value = KendraIndexUserTokenConfigurations(
            json_token_type_configuration=json_token_type_configuration,
            jwt_token_type_configuration=jwt_token_type_configuration,
        )

        return typing.cast(None, jsii.invoke(self, "putUserTokenConfigurations", [value]))

    @jsii.member(jsii_name="resetCapacityUnits")
    def reset_capacity_units(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCapacityUnits", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetDocumentMetadataConfigurationUpdates")
    def reset_document_metadata_configuration_updates(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDocumentMetadataConfigurationUpdates", []))

    @jsii.member(jsii_name="resetEdition")
    def reset_edition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEdition", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetServerSideEncryptionConfiguration")
    def reset_server_side_encryption_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServerSideEncryptionConfiguration", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetUserContextPolicy")
    def reset_user_context_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserContextPolicy", []))

    @jsii.member(jsii_name="resetUserGroupResolutionConfiguration")
    def reset_user_group_resolution_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserGroupResolutionConfiguration", []))

    @jsii.member(jsii_name="resetUserTokenConfigurations")
    def reset_user_token_configurations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserTokenConfigurations", []))

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
    @jsii.member(jsii_name="capacityUnits")
    def capacity_units(self) -> "KendraIndexCapacityUnitsOutputReference":
        return typing.cast("KendraIndexCapacityUnitsOutputReference", jsii.get(self, "capacityUnits"))

    @builtins.property
    @jsii.member(jsii_name="createdAt")
    def created_at(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdAt"))

    @builtins.property
    @jsii.member(jsii_name="documentMetadataConfigurationUpdates")
    def document_metadata_configuration_updates(
        self,
    ) -> "KendraIndexDocumentMetadataConfigurationUpdatesList":
        return typing.cast("KendraIndexDocumentMetadataConfigurationUpdatesList", jsii.get(self, "documentMetadataConfigurationUpdates"))

    @builtins.property
    @jsii.member(jsii_name="errorMessage")
    def error_message(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "errorMessage"))

    @builtins.property
    @jsii.member(jsii_name="indexStatistics")
    def index_statistics(self) -> "KendraIndexIndexStatisticsList":
        return typing.cast("KendraIndexIndexStatisticsList", jsii.get(self, "indexStatistics"))

    @builtins.property
    @jsii.member(jsii_name="serverSideEncryptionConfiguration")
    def server_side_encryption_configuration(
        self,
    ) -> "KendraIndexServerSideEncryptionConfigurationOutputReference":
        return typing.cast("KendraIndexServerSideEncryptionConfigurationOutputReference", jsii.get(self, "serverSideEncryptionConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "KendraIndexTimeoutsOutputReference":
        return typing.cast("KendraIndexTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="updatedAt")
    def updated_at(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "updatedAt"))

    @builtins.property
    @jsii.member(jsii_name="userGroupResolutionConfiguration")
    def user_group_resolution_configuration(
        self,
    ) -> "KendraIndexUserGroupResolutionConfigurationOutputReference":
        return typing.cast("KendraIndexUserGroupResolutionConfigurationOutputReference", jsii.get(self, "userGroupResolutionConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="userTokenConfigurations")
    def user_token_configurations(
        self,
    ) -> "KendraIndexUserTokenConfigurationsOutputReference":
        return typing.cast("KendraIndexUserTokenConfigurationsOutputReference", jsii.get(self, "userTokenConfigurations"))

    @builtins.property
    @jsii.member(jsii_name="capacityUnitsInput")
    def capacity_units_input(self) -> typing.Optional["KendraIndexCapacityUnits"]:
        return typing.cast(typing.Optional["KendraIndexCapacityUnits"], jsii.get(self, "capacityUnitsInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="documentMetadataConfigurationUpdatesInput")
    def document_metadata_configuration_updates_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KendraIndexDocumentMetadataConfigurationUpdates"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KendraIndexDocumentMetadataConfigurationUpdates"]]], jsii.get(self, "documentMetadataConfigurationUpdatesInput"))

    @builtins.property
    @jsii.member(jsii_name="editionInput")
    def edition_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "editionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="serverSideEncryptionConfigurationInput")
    def server_side_encryption_configuration_input(
        self,
    ) -> typing.Optional["KendraIndexServerSideEncryptionConfiguration"]:
        return typing.cast(typing.Optional["KendraIndexServerSideEncryptionConfiguration"], jsii.get(self, "serverSideEncryptionConfigurationInput"))

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
    ) -> typing.Optional[typing.Union["KendraIndexTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["KendraIndexTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="userContextPolicyInput")
    def user_context_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userContextPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="userGroupResolutionConfigurationInput")
    def user_group_resolution_configuration_input(
        self,
    ) -> typing.Optional["KendraIndexUserGroupResolutionConfiguration"]:
        return typing.cast(typing.Optional["KendraIndexUserGroupResolutionConfiguration"], jsii.get(self, "userGroupResolutionConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="userTokenConfigurationsInput")
    def user_token_configurations_input(
        self,
    ) -> typing.Optional["KendraIndexUserTokenConfigurations"]:
        return typing.cast(typing.Optional["KendraIndexUserTokenConfigurations"], jsii.get(self, "userTokenConfigurationsInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85b9c3a7a47b094f769bfdaa18b236f40540e142be44ffeaf6d653480048f59a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="edition")
    def edition(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "edition"))

    @edition.setter
    def edition(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4200f70d6b182bbe6d304dd57efa9054fef52710f2186c5335c000a5fef9bff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "edition", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc9ea64b34d57326fe8bca3de1fe170dd376aba15c6de57c0a740ba87878c867)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03af841c623ff3a31df66c6a2afb2782bb67d5386cc063bafffd1f525cd82313)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c82e6bb759da5f8c416069382b3728fea842d9d6675b1d95e6b667ad61d8291)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a78c71ab67b873d93d2c0ee88cfd363236adba79642b9874bdd1b5f11c52dbe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__942da8a169cdbc0605436c7c6fe02971fd8016ae1badbc1d50925c35f5539ac4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)

    @builtins.property
    @jsii.member(jsii_name="userContextPolicy")
    def user_context_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userContextPolicy"))

    @user_context_policy.setter
    def user_context_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dfa87804ac91333b7c1bd61dda6ec2879692cb125fd63566c585246dda720d2e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userContextPolicy", value)


@jsii.data_type(
    jsii_type="aws.kendraIndex.KendraIndexCapacityUnits",
    jsii_struct_bases=[],
    name_mapping={
        "query_capacity_units": "queryCapacityUnits",
        "storage_capacity_units": "storageCapacityUnits",
    },
)
class KendraIndexCapacityUnits:
    def __init__(
        self,
        *,
        query_capacity_units: typing.Optional[jsii.Number] = None,
        storage_capacity_units: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param query_capacity_units: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#query_capacity_units KendraIndex#query_capacity_units}.
        :param storage_capacity_units: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#storage_capacity_units KendraIndex#storage_capacity_units}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23cdc91c06b29947aa2f76415fb9a3f9639ec1eecc9b904663041077dab4b330)
            check_type(argname="argument query_capacity_units", value=query_capacity_units, expected_type=type_hints["query_capacity_units"])
            check_type(argname="argument storage_capacity_units", value=storage_capacity_units, expected_type=type_hints["storage_capacity_units"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if query_capacity_units is not None:
            self._values["query_capacity_units"] = query_capacity_units
        if storage_capacity_units is not None:
            self._values["storage_capacity_units"] = storage_capacity_units

    @builtins.property
    def query_capacity_units(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#query_capacity_units KendraIndex#query_capacity_units}.'''
        result = self._values.get("query_capacity_units")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def storage_capacity_units(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#storage_capacity_units KendraIndex#storage_capacity_units}.'''
        result = self._values.get("storage_capacity_units")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraIndexCapacityUnits(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KendraIndexCapacityUnitsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kendraIndex.KendraIndexCapacityUnitsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__079b647406565e98b37a3c998ce0ee4293136cdf65ae8e5018da703b72c0662e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetQueryCapacityUnits")
    def reset_query_capacity_units(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueryCapacityUnits", []))

    @jsii.member(jsii_name="resetStorageCapacityUnits")
    def reset_storage_capacity_units(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageCapacityUnits", []))

    @builtins.property
    @jsii.member(jsii_name="queryCapacityUnitsInput")
    def query_capacity_units_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "queryCapacityUnitsInput"))

    @builtins.property
    @jsii.member(jsii_name="storageCapacityUnitsInput")
    def storage_capacity_units_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "storageCapacityUnitsInput"))

    @builtins.property
    @jsii.member(jsii_name="queryCapacityUnits")
    def query_capacity_units(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "queryCapacityUnits"))

    @query_capacity_units.setter
    def query_capacity_units(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43b59a2bed2c4b7fcda264d1a2713c0ac9e97f18907a0d5ceda334cec9b4bf1f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queryCapacityUnits", value)

    @builtins.property
    @jsii.member(jsii_name="storageCapacityUnits")
    def storage_capacity_units(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "storageCapacityUnits"))

    @storage_capacity_units.setter
    def storage_capacity_units(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2522fa3202b012f8851e9c57e97530bceab8062a39473dfdd65286e809b4b792)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageCapacityUnits", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[KendraIndexCapacityUnits]:
        return typing.cast(typing.Optional[KendraIndexCapacityUnits], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[KendraIndexCapacityUnits]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec727b8ff63bc0b894caad06c2faced0b32e8890e059023d7b3a7ffe8fee782e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kendraIndex.KendraIndexConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "name": "name",
        "role_arn": "roleArn",
        "capacity_units": "capacityUnits",
        "description": "description",
        "document_metadata_configuration_updates": "documentMetadataConfigurationUpdates",
        "edition": "edition",
        "id": "id",
        "server_side_encryption_configuration": "serverSideEncryptionConfiguration",
        "tags": "tags",
        "tags_all": "tagsAll",
        "timeouts": "timeouts",
        "user_context_policy": "userContextPolicy",
        "user_group_resolution_configuration": "userGroupResolutionConfiguration",
        "user_token_configurations": "userTokenConfigurations",
    },
)
class KendraIndexConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        name: builtins.str,
        role_arn: builtins.str,
        capacity_units: typing.Optional[typing.Union[KendraIndexCapacityUnits, typing.Dict[builtins.str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        document_metadata_configuration_updates: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KendraIndexDocumentMetadataConfigurationUpdates", typing.Dict[builtins.str, typing.Any]]]]] = None,
        edition: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        server_side_encryption_configuration: typing.Optional[typing.Union["KendraIndexServerSideEncryptionConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["KendraIndexTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        user_context_policy: typing.Optional[builtins.str] = None,
        user_group_resolution_configuration: typing.Optional[typing.Union["KendraIndexUserGroupResolutionConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        user_token_configurations: typing.Optional[typing.Union["KendraIndexUserTokenConfigurations", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#name KendraIndex#name}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#role_arn KendraIndex#role_arn}.
        :param capacity_units: capacity_units block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#capacity_units KendraIndex#capacity_units}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#description KendraIndex#description}.
        :param document_metadata_configuration_updates: document_metadata_configuration_updates block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#document_metadata_configuration_updates KendraIndex#document_metadata_configuration_updates}
        :param edition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#edition KendraIndex#edition}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#id KendraIndex#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param server_side_encryption_configuration: server_side_encryption_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#server_side_encryption_configuration KendraIndex#server_side_encryption_configuration}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#tags KendraIndex#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#tags_all KendraIndex#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#timeouts KendraIndex#timeouts}
        :param user_context_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#user_context_policy KendraIndex#user_context_policy}.
        :param user_group_resolution_configuration: user_group_resolution_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#user_group_resolution_configuration KendraIndex#user_group_resolution_configuration}
        :param user_token_configurations: user_token_configurations block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#user_token_configurations KendraIndex#user_token_configurations}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(capacity_units, dict):
            capacity_units = KendraIndexCapacityUnits(**capacity_units)
        if isinstance(server_side_encryption_configuration, dict):
            server_side_encryption_configuration = KendraIndexServerSideEncryptionConfiguration(**server_side_encryption_configuration)
        if isinstance(timeouts, dict):
            timeouts = KendraIndexTimeouts(**timeouts)
        if isinstance(user_group_resolution_configuration, dict):
            user_group_resolution_configuration = KendraIndexUserGroupResolutionConfiguration(**user_group_resolution_configuration)
        if isinstance(user_token_configurations, dict):
            user_token_configurations = KendraIndexUserTokenConfigurations(**user_token_configurations)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4ff6fa56be947cd554947c8192e4239d1010054744709493a96ee9369abcc15)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument capacity_units", value=capacity_units, expected_type=type_hints["capacity_units"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument document_metadata_configuration_updates", value=document_metadata_configuration_updates, expected_type=type_hints["document_metadata_configuration_updates"])
            check_type(argname="argument edition", value=edition, expected_type=type_hints["edition"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument server_side_encryption_configuration", value=server_side_encryption_configuration, expected_type=type_hints["server_side_encryption_configuration"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument user_context_policy", value=user_context_policy, expected_type=type_hints["user_context_policy"])
            check_type(argname="argument user_group_resolution_configuration", value=user_group_resolution_configuration, expected_type=type_hints["user_group_resolution_configuration"])
            check_type(argname="argument user_token_configurations", value=user_token_configurations, expected_type=type_hints["user_token_configurations"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
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
        if capacity_units is not None:
            self._values["capacity_units"] = capacity_units
        if description is not None:
            self._values["description"] = description
        if document_metadata_configuration_updates is not None:
            self._values["document_metadata_configuration_updates"] = document_metadata_configuration_updates
        if edition is not None:
            self._values["edition"] = edition
        if id is not None:
            self._values["id"] = id
        if server_side_encryption_configuration is not None:
            self._values["server_side_encryption_configuration"] = server_side_encryption_configuration
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if user_context_policy is not None:
            self._values["user_context_policy"] = user_context_policy
        if user_group_resolution_configuration is not None:
            self._values["user_group_resolution_configuration"] = user_group_resolution_configuration
        if user_token_configurations is not None:
            self._values["user_token_configurations"] = user_token_configurations

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
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#name KendraIndex#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#role_arn KendraIndex#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def capacity_units(self) -> typing.Optional[KendraIndexCapacityUnits]:
        '''capacity_units block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#capacity_units KendraIndex#capacity_units}
        '''
        result = self._values.get("capacity_units")
        return typing.cast(typing.Optional[KendraIndexCapacityUnits], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#description KendraIndex#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def document_metadata_configuration_updates(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KendraIndexDocumentMetadataConfigurationUpdates"]]]:
        '''document_metadata_configuration_updates block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#document_metadata_configuration_updates KendraIndex#document_metadata_configuration_updates}
        '''
        result = self._values.get("document_metadata_configuration_updates")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KendraIndexDocumentMetadataConfigurationUpdates"]]], result)

    @builtins.property
    def edition(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#edition KendraIndex#edition}.'''
        result = self._values.get("edition")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#id KendraIndex#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def server_side_encryption_configuration(
        self,
    ) -> typing.Optional["KendraIndexServerSideEncryptionConfiguration"]:
        '''server_side_encryption_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#server_side_encryption_configuration KendraIndex#server_side_encryption_configuration}
        '''
        result = self._values.get("server_side_encryption_configuration")
        return typing.cast(typing.Optional["KendraIndexServerSideEncryptionConfiguration"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#tags KendraIndex#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#tags_all KendraIndex#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["KendraIndexTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#timeouts KendraIndex#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["KendraIndexTimeouts"], result)

    @builtins.property
    def user_context_policy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#user_context_policy KendraIndex#user_context_policy}.'''
        result = self._values.get("user_context_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_group_resolution_configuration(
        self,
    ) -> typing.Optional["KendraIndexUserGroupResolutionConfiguration"]:
        '''user_group_resolution_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#user_group_resolution_configuration KendraIndex#user_group_resolution_configuration}
        '''
        result = self._values.get("user_group_resolution_configuration")
        return typing.cast(typing.Optional["KendraIndexUserGroupResolutionConfiguration"], result)

    @builtins.property
    def user_token_configurations(
        self,
    ) -> typing.Optional["KendraIndexUserTokenConfigurations"]:
        '''user_token_configurations block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#user_token_configurations KendraIndex#user_token_configurations}
        '''
        result = self._values.get("user_token_configurations")
        return typing.cast(typing.Optional["KendraIndexUserTokenConfigurations"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraIndexConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.kendraIndex.KendraIndexDocumentMetadataConfigurationUpdates",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "type": "type",
        "relevance": "relevance",
        "search": "search",
    },
)
class KendraIndexDocumentMetadataConfigurationUpdates:
    def __init__(
        self,
        *,
        name: builtins.str,
        type: builtins.str,
        relevance: typing.Optional[typing.Union["KendraIndexDocumentMetadataConfigurationUpdatesRelevance", typing.Dict[builtins.str, typing.Any]]] = None,
        search: typing.Optional[typing.Union["KendraIndexDocumentMetadataConfigurationUpdatesSearch", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#name KendraIndex#name}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#type KendraIndex#type}.
        :param relevance: relevance block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#relevance KendraIndex#relevance}
        :param search: search block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#search KendraIndex#search}
        '''
        if isinstance(relevance, dict):
            relevance = KendraIndexDocumentMetadataConfigurationUpdatesRelevance(**relevance)
        if isinstance(search, dict):
            search = KendraIndexDocumentMetadataConfigurationUpdatesSearch(**search)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1432211c64fe1ef4e714835b86ef81f83ada0495f8dd31ec1e624613259e15ac)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument relevance", value=relevance, expected_type=type_hints["relevance"])
            check_type(argname="argument search", value=search, expected_type=type_hints["search"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "type": type,
        }
        if relevance is not None:
            self._values["relevance"] = relevance
        if search is not None:
            self._values["search"] = search

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#name KendraIndex#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#type KendraIndex#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def relevance(
        self,
    ) -> typing.Optional["KendraIndexDocumentMetadataConfigurationUpdatesRelevance"]:
        '''relevance block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#relevance KendraIndex#relevance}
        '''
        result = self._values.get("relevance")
        return typing.cast(typing.Optional["KendraIndexDocumentMetadataConfigurationUpdatesRelevance"], result)

    @builtins.property
    def search(
        self,
    ) -> typing.Optional["KendraIndexDocumentMetadataConfigurationUpdatesSearch"]:
        '''search block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#search KendraIndex#search}
        '''
        result = self._values.get("search")
        return typing.cast(typing.Optional["KendraIndexDocumentMetadataConfigurationUpdatesSearch"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraIndexDocumentMetadataConfigurationUpdates(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KendraIndexDocumentMetadataConfigurationUpdatesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kendraIndex.KendraIndexDocumentMetadataConfigurationUpdatesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5e9fdb36caf7237261e98c9b8f1e5e211c1179719d3fdb3e6665b2adef636ed0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "KendraIndexDocumentMetadataConfigurationUpdatesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8fd06100a4d52496c397089184231462f1027102a4ab53ee1c3a10b757f81db)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KendraIndexDocumentMetadataConfigurationUpdatesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__586462835eaf437a24854951415429904fd881e6bd0d168ea5eccb0e44a70d0c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__fb59be7686e61bc4d1f4388184d69c868d3e24d38ab6789b0463df251af2ebb6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__fc1a89e92eade101ebbe4ed33aeff5cba2d2af14dc43cd7a622bd7c71cdb8b8e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KendraIndexDocumentMetadataConfigurationUpdates]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KendraIndexDocumentMetadataConfigurationUpdates]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KendraIndexDocumentMetadataConfigurationUpdates]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a59d3df674310cf540f5c7457aecd2127f2e64dbe782d5f901a3eae551f4e86e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KendraIndexDocumentMetadataConfigurationUpdatesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kendraIndex.KendraIndexDocumentMetadataConfigurationUpdatesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cf9b0c810bd1503ec402e0870158989d3e22293bcb27873d7a54aed17a62ee0a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putRelevance")
    def put_relevance(
        self,
        *,
        duration: typing.Optional[builtins.str] = None,
        freshness: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        importance: typing.Optional[jsii.Number] = None,
        rank_order: typing.Optional[builtins.str] = None,
        values_importance_map: typing.Optional[typing.Mapping[builtins.str, jsii.Number]] = None,
    ) -> None:
        '''
        :param duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#duration KendraIndex#duration}.
        :param freshness: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#freshness KendraIndex#freshness}.
        :param importance: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#importance KendraIndex#importance}.
        :param rank_order: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#rank_order KendraIndex#rank_order}.
        :param values_importance_map: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#values_importance_map KendraIndex#values_importance_map}.
        '''
        value = KendraIndexDocumentMetadataConfigurationUpdatesRelevance(
            duration=duration,
            freshness=freshness,
            importance=importance,
            rank_order=rank_order,
            values_importance_map=values_importance_map,
        )

        return typing.cast(None, jsii.invoke(self, "putRelevance", [value]))

    @jsii.member(jsii_name="putSearch")
    def put_search(
        self,
        *,
        displayable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        facetable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        searchable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        sortable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param displayable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#displayable KendraIndex#displayable}.
        :param facetable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#facetable KendraIndex#facetable}.
        :param searchable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#searchable KendraIndex#searchable}.
        :param sortable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#sortable KendraIndex#sortable}.
        '''
        value = KendraIndexDocumentMetadataConfigurationUpdatesSearch(
            displayable=displayable,
            facetable=facetable,
            searchable=searchable,
            sortable=sortable,
        )

        return typing.cast(None, jsii.invoke(self, "putSearch", [value]))

    @jsii.member(jsii_name="resetRelevance")
    def reset_relevance(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRelevance", []))

    @jsii.member(jsii_name="resetSearch")
    def reset_search(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSearch", []))

    @builtins.property
    @jsii.member(jsii_name="relevance")
    def relevance(
        self,
    ) -> "KendraIndexDocumentMetadataConfigurationUpdatesRelevanceOutputReference":
        return typing.cast("KendraIndexDocumentMetadataConfigurationUpdatesRelevanceOutputReference", jsii.get(self, "relevance"))

    @builtins.property
    @jsii.member(jsii_name="search")
    def search(
        self,
    ) -> "KendraIndexDocumentMetadataConfigurationUpdatesSearchOutputReference":
        return typing.cast("KendraIndexDocumentMetadataConfigurationUpdatesSearchOutputReference", jsii.get(self, "search"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="relevanceInput")
    def relevance_input(
        self,
    ) -> typing.Optional["KendraIndexDocumentMetadataConfigurationUpdatesRelevance"]:
        return typing.cast(typing.Optional["KendraIndexDocumentMetadataConfigurationUpdatesRelevance"], jsii.get(self, "relevanceInput"))

    @builtins.property
    @jsii.member(jsii_name="searchInput")
    def search_input(
        self,
    ) -> typing.Optional["KendraIndexDocumentMetadataConfigurationUpdatesSearch"]:
        return typing.cast(typing.Optional["KendraIndexDocumentMetadataConfigurationUpdatesSearch"], jsii.get(self, "searchInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7304f008208c6e71cf48cc71999f566429719d2399457f88aa4e18b00a06317b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7470d9657792679f48c8896a1e1c5f4c31bc7622b2c7e79499bf4aca60e5bbc1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[KendraIndexDocumentMetadataConfigurationUpdates, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[KendraIndexDocumentMetadataConfigurationUpdates, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[KendraIndexDocumentMetadataConfigurationUpdates, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6f07c20e6d38d44ede62b39e1a259ac0406cf455200301f96cd4b0fd2c512fb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kendraIndex.KendraIndexDocumentMetadataConfigurationUpdatesRelevance",
    jsii_struct_bases=[],
    name_mapping={
        "duration": "duration",
        "freshness": "freshness",
        "importance": "importance",
        "rank_order": "rankOrder",
        "values_importance_map": "valuesImportanceMap",
    },
)
class KendraIndexDocumentMetadataConfigurationUpdatesRelevance:
    def __init__(
        self,
        *,
        duration: typing.Optional[builtins.str] = None,
        freshness: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        importance: typing.Optional[jsii.Number] = None,
        rank_order: typing.Optional[builtins.str] = None,
        values_importance_map: typing.Optional[typing.Mapping[builtins.str, jsii.Number]] = None,
    ) -> None:
        '''
        :param duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#duration KendraIndex#duration}.
        :param freshness: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#freshness KendraIndex#freshness}.
        :param importance: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#importance KendraIndex#importance}.
        :param rank_order: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#rank_order KendraIndex#rank_order}.
        :param values_importance_map: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#values_importance_map KendraIndex#values_importance_map}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__191fe18db0b51ef0920f9ffdbb2a5fba8903a149af9adf3f924f59ac11694713)
            check_type(argname="argument duration", value=duration, expected_type=type_hints["duration"])
            check_type(argname="argument freshness", value=freshness, expected_type=type_hints["freshness"])
            check_type(argname="argument importance", value=importance, expected_type=type_hints["importance"])
            check_type(argname="argument rank_order", value=rank_order, expected_type=type_hints["rank_order"])
            check_type(argname="argument values_importance_map", value=values_importance_map, expected_type=type_hints["values_importance_map"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if duration is not None:
            self._values["duration"] = duration
        if freshness is not None:
            self._values["freshness"] = freshness
        if importance is not None:
            self._values["importance"] = importance
        if rank_order is not None:
            self._values["rank_order"] = rank_order
        if values_importance_map is not None:
            self._values["values_importance_map"] = values_importance_map

    @builtins.property
    def duration(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#duration KendraIndex#duration}.'''
        result = self._values.get("duration")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def freshness(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#freshness KendraIndex#freshness}.'''
        result = self._values.get("freshness")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def importance(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#importance KendraIndex#importance}.'''
        result = self._values.get("importance")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def rank_order(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#rank_order KendraIndex#rank_order}.'''
        result = self._values.get("rank_order")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def values_importance_map(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, jsii.Number]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#values_importance_map KendraIndex#values_importance_map}.'''
        result = self._values.get("values_importance_map")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, jsii.Number]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraIndexDocumentMetadataConfigurationUpdatesRelevance(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KendraIndexDocumentMetadataConfigurationUpdatesRelevanceOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kendraIndex.KendraIndexDocumentMetadataConfigurationUpdatesRelevanceOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__844c8748f3768aee71b1ca973a2f5f896a1a32278c88446b857e039f284a79ea)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDuration")
    def reset_duration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDuration", []))

    @jsii.member(jsii_name="resetFreshness")
    def reset_freshness(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFreshness", []))

    @jsii.member(jsii_name="resetImportance")
    def reset_importance(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImportance", []))

    @jsii.member(jsii_name="resetRankOrder")
    def reset_rank_order(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRankOrder", []))

    @jsii.member(jsii_name="resetValuesImportanceMap")
    def reset_values_importance_map(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValuesImportanceMap", []))

    @builtins.property
    @jsii.member(jsii_name="durationInput")
    def duration_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "durationInput"))

    @builtins.property
    @jsii.member(jsii_name="freshnessInput")
    def freshness_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "freshnessInput"))

    @builtins.property
    @jsii.member(jsii_name="importanceInput")
    def importance_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "importanceInput"))

    @builtins.property
    @jsii.member(jsii_name="rankOrderInput")
    def rank_order_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rankOrderInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesImportanceMapInput")
    def values_importance_map_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, jsii.Number]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, jsii.Number]], jsii.get(self, "valuesImportanceMapInput"))

    @builtins.property
    @jsii.member(jsii_name="duration")
    def duration(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "duration"))

    @duration.setter
    def duration(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ff6f499d488d75de8aa1e2cb4b030314e48faabdabf9d6516936addce53eedb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "duration", value)

    @builtins.property
    @jsii.member(jsii_name="freshness")
    def freshness(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "freshness"))

    @freshness.setter
    def freshness(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58b4b3af7e3aa10f0c02b69e7ed0dd48073183c3c0299794a12981c2aba9c839)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "freshness", value)

    @builtins.property
    @jsii.member(jsii_name="importance")
    def importance(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "importance"))

    @importance.setter
    def importance(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e262f3bbb79727fb9a07ae5b16f10d809e4e43e937ae69a4de80b82b66d1bd4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "importance", value)

    @builtins.property
    @jsii.member(jsii_name="rankOrder")
    def rank_order(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rankOrder"))

    @rank_order.setter
    def rank_order(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aebd1de6a1e79bb4093fecbb8697c74db7467d94dbca32bd87d7cec691db1a85)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rankOrder", value)

    @builtins.property
    @jsii.member(jsii_name="valuesImportanceMap")
    def values_importance_map(self) -> typing.Mapping[builtins.str, jsii.Number]:
        return typing.cast(typing.Mapping[builtins.str, jsii.Number], jsii.get(self, "valuesImportanceMap"))

    @values_importance_map.setter
    def values_importance_map(
        self,
        value: typing.Mapping[builtins.str, jsii.Number],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4912b804d6e1d632ef23418000f8f70133a89cce2f877b4e278da9493b48b7fe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "valuesImportanceMap", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KendraIndexDocumentMetadataConfigurationUpdatesRelevance]:
        return typing.cast(typing.Optional[KendraIndexDocumentMetadataConfigurationUpdatesRelevance], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KendraIndexDocumentMetadataConfigurationUpdatesRelevance],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__537fcb26bd7dfd1ee1f8d6f92306298d5bb3b7d97228e436575f38ef63069258)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kendraIndex.KendraIndexDocumentMetadataConfigurationUpdatesSearch",
    jsii_struct_bases=[],
    name_mapping={
        "displayable": "displayable",
        "facetable": "facetable",
        "searchable": "searchable",
        "sortable": "sortable",
    },
)
class KendraIndexDocumentMetadataConfigurationUpdatesSearch:
    def __init__(
        self,
        *,
        displayable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        facetable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        searchable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        sortable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param displayable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#displayable KendraIndex#displayable}.
        :param facetable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#facetable KendraIndex#facetable}.
        :param searchable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#searchable KendraIndex#searchable}.
        :param sortable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#sortable KendraIndex#sortable}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b025e7a3bc854142b4eb81ae6bfa269ccaf37d4e98675a2a2f679e4d1a9f980)
            check_type(argname="argument displayable", value=displayable, expected_type=type_hints["displayable"])
            check_type(argname="argument facetable", value=facetable, expected_type=type_hints["facetable"])
            check_type(argname="argument searchable", value=searchable, expected_type=type_hints["searchable"])
            check_type(argname="argument sortable", value=sortable, expected_type=type_hints["sortable"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if displayable is not None:
            self._values["displayable"] = displayable
        if facetable is not None:
            self._values["facetable"] = facetable
        if searchable is not None:
            self._values["searchable"] = searchable
        if sortable is not None:
            self._values["sortable"] = sortable

    @builtins.property
    def displayable(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#displayable KendraIndex#displayable}.'''
        result = self._values.get("displayable")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def facetable(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#facetable KendraIndex#facetable}.'''
        result = self._values.get("facetable")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def searchable(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#searchable KendraIndex#searchable}.'''
        result = self._values.get("searchable")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def sortable(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#sortable KendraIndex#sortable}.'''
        result = self._values.get("sortable")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraIndexDocumentMetadataConfigurationUpdatesSearch(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KendraIndexDocumentMetadataConfigurationUpdatesSearchOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kendraIndex.KendraIndexDocumentMetadataConfigurationUpdatesSearchOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5aca906027681fb73aa0434b0a9b726c5a6d8a1da7867ef6d847e5dd1a12dc42)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDisplayable")
    def reset_displayable(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisplayable", []))

    @jsii.member(jsii_name="resetFacetable")
    def reset_facetable(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFacetable", []))

    @jsii.member(jsii_name="resetSearchable")
    def reset_searchable(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSearchable", []))

    @jsii.member(jsii_name="resetSortable")
    def reset_sortable(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSortable", []))

    @builtins.property
    @jsii.member(jsii_name="displayableInput")
    def displayable_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "displayableInput"))

    @builtins.property
    @jsii.member(jsii_name="facetableInput")
    def facetable_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "facetableInput"))

    @builtins.property
    @jsii.member(jsii_name="searchableInput")
    def searchable_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "searchableInput"))

    @builtins.property
    @jsii.member(jsii_name="sortableInput")
    def sortable_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "sortableInput"))

    @builtins.property
    @jsii.member(jsii_name="displayable")
    def displayable(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "displayable"))

    @displayable.setter
    def displayable(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92978cf4be165e80dfd543d3ca7257cdf28f9126190463e6c0acc3014ea11c72)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayable", value)

    @builtins.property
    @jsii.member(jsii_name="facetable")
    def facetable(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "facetable"))

    @facetable.setter
    def facetable(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59de78ac4f39e3d367253c83542ee600fc24f32612f36c60e288f3f8759f7652)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "facetable", value)

    @builtins.property
    @jsii.member(jsii_name="searchable")
    def searchable(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "searchable"))

    @searchable.setter
    def searchable(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a8b249c9a262cdd975f52fee727e75d34ff636214441d40e4ac7ce5930d7ae7c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "searchable", value)

    @builtins.property
    @jsii.member(jsii_name="sortable")
    def sortable(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "sortable"))

    @sortable.setter
    def sortable(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98dbf528dd03b5b833cde6cf73cae4b50091a70634e2b233896ed7ebd2c815cd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sortable", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KendraIndexDocumentMetadataConfigurationUpdatesSearch]:
        return typing.cast(typing.Optional[KendraIndexDocumentMetadataConfigurationUpdatesSearch], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KendraIndexDocumentMetadataConfigurationUpdatesSearch],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5068d2fca82dfddd3ef5011bdd564df8e6f0434e01e726cc2bda6f0f394d9232)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kendraIndex.KendraIndexIndexStatistics",
    jsii_struct_bases=[],
    name_mapping={},
)
class KendraIndexIndexStatistics:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraIndexIndexStatistics(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.kendraIndex.KendraIndexIndexStatisticsFaqStatistics",
    jsii_struct_bases=[],
    name_mapping={},
)
class KendraIndexIndexStatisticsFaqStatistics:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraIndexIndexStatisticsFaqStatistics(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KendraIndexIndexStatisticsFaqStatisticsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kendraIndex.KendraIndexIndexStatisticsFaqStatisticsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__fa1796639c1dffdf9566e44cc7b07ec830754e38ac0c159b07d34ed85d9a0953)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "KendraIndexIndexStatisticsFaqStatisticsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58f0dab61a67c6498a474091dece91b02e9e9175b34434e2279de1b54a068192)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KendraIndexIndexStatisticsFaqStatisticsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c74f6f572da75fe994fe62cd9bc88790abe550854f027aac96d7c044d5bbe06c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__48d05c5ed7f286ba33cc4ee45b8625ff56a227e385a077cad6cd898feaa4b8c3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4b06b0bb1fb3e9a78a161dd1e99e02afaebbe366e446b84f7eaccf1ac57fc65a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class KendraIndexIndexStatisticsFaqStatisticsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kendraIndex.KendraIndexIndexStatisticsFaqStatisticsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7b9b05033295e5c3042610dcc190f4e1ebbe548b9c0430547ca31acb444dd93d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="indexedQuestionAnswersCount")
    def indexed_question_answers_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "indexedQuestionAnswersCount"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KendraIndexIndexStatisticsFaqStatistics]:
        return typing.cast(typing.Optional[KendraIndexIndexStatisticsFaqStatistics], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KendraIndexIndexStatisticsFaqStatistics],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89e9ba22f965e2c87f5c70da1d021af415f8bc9df81f903f8d9bed74e56b91b0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KendraIndexIndexStatisticsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kendraIndex.KendraIndexIndexStatisticsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__719dda1a32f4c740130b4054fc72696170454ffcb9aa69cb580ec2b5ee57ba81)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "KendraIndexIndexStatisticsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f33f863d39fedd2982736263f89e3c185371cb001687f21f71d3e8afb30f203a)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KendraIndexIndexStatisticsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92b6a62297e17fb7e851abcdd4832bd8f988d0a62e066952b348108106a7c95a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b963b3f294e4b106f9e21eac546a5c7d33d249eb2f2bcd92706d8678b96c8dcd)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2376248be3f846e7f05963904be7c7f94691b575e11cfb846b59a20f77b67b7c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class KendraIndexIndexStatisticsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kendraIndex.KendraIndexIndexStatisticsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__232f1a943b0f0d96f419a60d2510072c367a51cf703018200190519eef909634)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="faqStatistics")
    def faq_statistics(self) -> KendraIndexIndexStatisticsFaqStatisticsList:
        return typing.cast(KendraIndexIndexStatisticsFaqStatisticsList, jsii.get(self, "faqStatistics"))

    @builtins.property
    @jsii.member(jsii_name="textDocumentStatistics")
    def text_document_statistics(
        self,
    ) -> "KendraIndexIndexStatisticsTextDocumentStatisticsList":
        return typing.cast("KendraIndexIndexStatisticsTextDocumentStatisticsList", jsii.get(self, "textDocumentStatistics"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[KendraIndexIndexStatistics]:
        return typing.cast(typing.Optional[KendraIndexIndexStatistics], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KendraIndexIndexStatistics],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f903c27aec73a56a43e62d7f4b1354be6119d5c3c637a102741e3f30cb1d020)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kendraIndex.KendraIndexIndexStatisticsTextDocumentStatistics",
    jsii_struct_bases=[],
    name_mapping={},
)
class KendraIndexIndexStatisticsTextDocumentStatistics:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraIndexIndexStatisticsTextDocumentStatistics(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KendraIndexIndexStatisticsTextDocumentStatisticsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kendraIndex.KendraIndexIndexStatisticsTextDocumentStatisticsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__443480c8be136e2d50f89bf247ee18724847bd923d701f29560eab77f704b5e8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "KendraIndexIndexStatisticsTextDocumentStatisticsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c973f4e1d86cdefea1a9e3af8f2740c232c255b7e899109f754310086f68419)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KendraIndexIndexStatisticsTextDocumentStatisticsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__10bb04ba34a726de2e32213402e730e8a325b5259934d0af83d92db13f9be151)
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
            type_hints = typing.get_type_hints(_typecheckingstub__578654f5e8b112520f04de7e1606201840edf02a527fd5c845439f9db4148cb1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4377113fb3dffd43266d9f6198a5d09142fdd7c31523fc6948ddb7ffe71df2cd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class KendraIndexIndexStatisticsTextDocumentStatisticsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kendraIndex.KendraIndexIndexStatisticsTextDocumentStatisticsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__87be49f2d5648a96aff24be86cae7f8f266c02502b7461e6f2b8ec6591b4dfb1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="indexedTextBytes")
    def indexed_text_bytes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "indexedTextBytes"))

    @builtins.property
    @jsii.member(jsii_name="indexedTextDocumentsCount")
    def indexed_text_documents_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "indexedTextDocumentsCount"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KendraIndexIndexStatisticsTextDocumentStatistics]:
        return typing.cast(typing.Optional[KendraIndexIndexStatisticsTextDocumentStatistics], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KendraIndexIndexStatisticsTextDocumentStatistics],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e75d396ab6072debce7280f2579c385f3d02354a67c6d81141d9d2377294cb3c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kendraIndex.KendraIndexServerSideEncryptionConfiguration",
    jsii_struct_bases=[],
    name_mapping={"kms_key_id": "kmsKeyId"},
)
class KendraIndexServerSideEncryptionConfiguration:
    def __init__(self, *, kms_key_id: typing.Optional[builtins.str] = None) -> None:
        '''
        :param kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#kms_key_id KendraIndex#kms_key_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c17a0777718e2fab857521dfb4afc9c2c7543ac6cab0c5058bb9fe598d241030)
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#kms_key_id KendraIndex#kms_key_id}.'''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraIndexServerSideEncryptionConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KendraIndexServerSideEncryptionConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kendraIndex.KendraIndexServerSideEncryptionConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__459966a2dd4acf63c0e80c30d67acf6612f3b651db4f498a3876a524578f8a38)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e657097717c22142701b9d7d7da68cb8d74018e8de0147b6d158d1553c6b4f9b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KendraIndexServerSideEncryptionConfiguration]:
        return typing.cast(typing.Optional[KendraIndexServerSideEncryptionConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KendraIndexServerSideEncryptionConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d8591676f114920e96cb7118e40171e0f461393ab5d5b325655c1ed40319f55)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kendraIndex.KendraIndexTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class KendraIndexTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#create KendraIndex#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#delete KendraIndex#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#update KendraIndex#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67a155ba84fb94702e1f2b8ec4feecbabb468282e2e335d151f59a4570c5c1fc)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#create KendraIndex#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#delete KendraIndex#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#update KendraIndex#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraIndexTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KendraIndexTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kendraIndex.KendraIndexTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__61b30ecbf143f97261cd4691a09a40020b632aae5693fbad5a36c22380a28ed0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3ed4c23ae43c2673afbb450942d0971c117066c1649d3887f924920daaf8919d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0dfad4d1f97828943a4a04f45433da5554c69d299f3a8bf59a1035d9c1ed0f3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80cbdc951787b2c3296fd56cc4a69fcde03860a17f620df16f63aeacca56c995)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[KendraIndexTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[KendraIndexTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[KendraIndexTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f40b9d2b4f7086c82ff82e8c9267ca596ce511b118518f860abf2735a301de29)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kendraIndex.KendraIndexUserGroupResolutionConfiguration",
    jsii_struct_bases=[],
    name_mapping={"user_group_resolution_mode": "userGroupResolutionMode"},
)
class KendraIndexUserGroupResolutionConfiguration:
    def __init__(self, *, user_group_resolution_mode: builtins.str) -> None:
        '''
        :param user_group_resolution_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#user_group_resolution_mode KendraIndex#user_group_resolution_mode}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35d72b19451c0d70c5bbfbe10fd7f6dce83d82c9d691caeb38d7d84c1d2378ca)
            check_type(argname="argument user_group_resolution_mode", value=user_group_resolution_mode, expected_type=type_hints["user_group_resolution_mode"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "user_group_resolution_mode": user_group_resolution_mode,
        }

    @builtins.property
    def user_group_resolution_mode(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#user_group_resolution_mode KendraIndex#user_group_resolution_mode}.'''
        result = self._values.get("user_group_resolution_mode")
        assert result is not None, "Required property 'user_group_resolution_mode' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraIndexUserGroupResolutionConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KendraIndexUserGroupResolutionConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kendraIndex.KendraIndexUserGroupResolutionConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f981222c4dcba374ad4fb1529e024cd7d3b865f3503acedf61d5b39d72b7bd49)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="userGroupResolutionModeInput")
    def user_group_resolution_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userGroupResolutionModeInput"))

    @builtins.property
    @jsii.member(jsii_name="userGroupResolutionMode")
    def user_group_resolution_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userGroupResolutionMode"))

    @user_group_resolution_mode.setter
    def user_group_resolution_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3867aaeba638541995b4c91fd937895931aa05eab813594ab6f3d9eb65d2b8fb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userGroupResolutionMode", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KendraIndexUserGroupResolutionConfiguration]:
        return typing.cast(typing.Optional[KendraIndexUserGroupResolutionConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KendraIndexUserGroupResolutionConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__177986dc33defa107ebeeff8f116434b1c9bbb8d4a3a154379ccd26058210976)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kendraIndex.KendraIndexUserTokenConfigurations",
    jsii_struct_bases=[],
    name_mapping={
        "json_token_type_configuration": "jsonTokenTypeConfiguration",
        "jwt_token_type_configuration": "jwtTokenTypeConfiguration",
    },
)
class KendraIndexUserTokenConfigurations:
    def __init__(
        self,
        *,
        json_token_type_configuration: typing.Optional[typing.Union["KendraIndexUserTokenConfigurationsJsonTokenTypeConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        jwt_token_type_configuration: typing.Optional[typing.Union["KendraIndexUserTokenConfigurationsJwtTokenTypeConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param json_token_type_configuration: json_token_type_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#json_token_type_configuration KendraIndex#json_token_type_configuration}
        :param jwt_token_type_configuration: jwt_token_type_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#jwt_token_type_configuration KendraIndex#jwt_token_type_configuration}
        '''
        if isinstance(json_token_type_configuration, dict):
            json_token_type_configuration = KendraIndexUserTokenConfigurationsJsonTokenTypeConfiguration(**json_token_type_configuration)
        if isinstance(jwt_token_type_configuration, dict):
            jwt_token_type_configuration = KendraIndexUserTokenConfigurationsJwtTokenTypeConfiguration(**jwt_token_type_configuration)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ecdfa6cfd97e1f6cf88ba9cd3a23cf358bc23ae4c9a0dd39fa123dbd8151950b)
            check_type(argname="argument json_token_type_configuration", value=json_token_type_configuration, expected_type=type_hints["json_token_type_configuration"])
            check_type(argname="argument jwt_token_type_configuration", value=jwt_token_type_configuration, expected_type=type_hints["jwt_token_type_configuration"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if json_token_type_configuration is not None:
            self._values["json_token_type_configuration"] = json_token_type_configuration
        if jwt_token_type_configuration is not None:
            self._values["jwt_token_type_configuration"] = jwt_token_type_configuration

    @builtins.property
    def json_token_type_configuration(
        self,
    ) -> typing.Optional["KendraIndexUserTokenConfigurationsJsonTokenTypeConfiguration"]:
        '''json_token_type_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#json_token_type_configuration KendraIndex#json_token_type_configuration}
        '''
        result = self._values.get("json_token_type_configuration")
        return typing.cast(typing.Optional["KendraIndexUserTokenConfigurationsJsonTokenTypeConfiguration"], result)

    @builtins.property
    def jwt_token_type_configuration(
        self,
    ) -> typing.Optional["KendraIndexUserTokenConfigurationsJwtTokenTypeConfiguration"]:
        '''jwt_token_type_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#jwt_token_type_configuration KendraIndex#jwt_token_type_configuration}
        '''
        result = self._values.get("jwt_token_type_configuration")
        return typing.cast(typing.Optional["KendraIndexUserTokenConfigurationsJwtTokenTypeConfiguration"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraIndexUserTokenConfigurations(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.kendraIndex.KendraIndexUserTokenConfigurationsJsonTokenTypeConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "group_attribute_field": "groupAttributeField",
        "user_name_attribute_field": "userNameAttributeField",
    },
)
class KendraIndexUserTokenConfigurationsJsonTokenTypeConfiguration:
    def __init__(
        self,
        *,
        group_attribute_field: builtins.str,
        user_name_attribute_field: builtins.str,
    ) -> None:
        '''
        :param group_attribute_field: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#group_attribute_field KendraIndex#group_attribute_field}.
        :param user_name_attribute_field: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#user_name_attribute_field KendraIndex#user_name_attribute_field}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac3b0311dc299f5c66335497e916dd453a7e0bb18af5fdff679d56153c1cf3cf)
            check_type(argname="argument group_attribute_field", value=group_attribute_field, expected_type=type_hints["group_attribute_field"])
            check_type(argname="argument user_name_attribute_field", value=user_name_attribute_field, expected_type=type_hints["user_name_attribute_field"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "group_attribute_field": group_attribute_field,
            "user_name_attribute_field": user_name_attribute_field,
        }

    @builtins.property
    def group_attribute_field(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#group_attribute_field KendraIndex#group_attribute_field}.'''
        result = self._values.get("group_attribute_field")
        assert result is not None, "Required property 'group_attribute_field' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_name_attribute_field(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#user_name_attribute_field KendraIndex#user_name_attribute_field}.'''
        result = self._values.get("user_name_attribute_field")
        assert result is not None, "Required property 'user_name_attribute_field' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraIndexUserTokenConfigurationsJsonTokenTypeConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KendraIndexUserTokenConfigurationsJsonTokenTypeConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kendraIndex.KendraIndexUserTokenConfigurationsJsonTokenTypeConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__70615b1fdf1aa1a84f31d4938efd49fbfa90082dfe4acd8c60f9da0b2a4064e1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="groupAttributeFieldInput")
    def group_attribute_field_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "groupAttributeFieldInput"))

    @builtins.property
    @jsii.member(jsii_name="userNameAttributeFieldInput")
    def user_name_attribute_field_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userNameAttributeFieldInput"))

    @builtins.property
    @jsii.member(jsii_name="groupAttributeField")
    def group_attribute_field(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "groupAttributeField"))

    @group_attribute_field.setter
    def group_attribute_field(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f7082c7c7bd4076f08e6efa1e630ff26072636a0b09b00529e31c8be858024d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupAttributeField", value)

    @builtins.property
    @jsii.member(jsii_name="userNameAttributeField")
    def user_name_attribute_field(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userNameAttributeField"))

    @user_name_attribute_field.setter
    def user_name_attribute_field(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61a757653d381572b5ba312c9ee90f77c8cf44ce9570825a03582d2c6a5b1e26)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userNameAttributeField", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KendraIndexUserTokenConfigurationsJsonTokenTypeConfiguration]:
        return typing.cast(typing.Optional[KendraIndexUserTokenConfigurationsJsonTokenTypeConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KendraIndexUserTokenConfigurationsJsonTokenTypeConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f49d35aa1415f9bbf7f28e6e156e3a53c0cc7b7c3314b9b649c6795b3b2f2e3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kendraIndex.KendraIndexUserTokenConfigurationsJwtTokenTypeConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "key_location": "keyLocation",
        "claim_regex": "claimRegex",
        "group_attribute_field": "groupAttributeField",
        "issuer": "issuer",
        "secrets_manager_arn": "secretsManagerArn",
        "url": "url",
        "user_name_attribute_field": "userNameAttributeField",
    },
)
class KendraIndexUserTokenConfigurationsJwtTokenTypeConfiguration:
    def __init__(
        self,
        *,
        key_location: builtins.str,
        claim_regex: typing.Optional[builtins.str] = None,
        group_attribute_field: typing.Optional[builtins.str] = None,
        issuer: typing.Optional[builtins.str] = None,
        secrets_manager_arn: typing.Optional[builtins.str] = None,
        url: typing.Optional[builtins.str] = None,
        user_name_attribute_field: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param key_location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#key_location KendraIndex#key_location}.
        :param claim_regex: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#claim_regex KendraIndex#claim_regex}.
        :param group_attribute_field: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#group_attribute_field KendraIndex#group_attribute_field}.
        :param issuer: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#issuer KendraIndex#issuer}.
        :param secrets_manager_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#secrets_manager_arn KendraIndex#secrets_manager_arn}.
        :param url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#url KendraIndex#url}.
        :param user_name_attribute_field: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#user_name_attribute_field KendraIndex#user_name_attribute_field}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e840cf5a68a8e4348923b1037e42335df0c67eddca0a038da5b620178bceaa7)
            check_type(argname="argument key_location", value=key_location, expected_type=type_hints["key_location"])
            check_type(argname="argument claim_regex", value=claim_regex, expected_type=type_hints["claim_regex"])
            check_type(argname="argument group_attribute_field", value=group_attribute_field, expected_type=type_hints["group_attribute_field"])
            check_type(argname="argument issuer", value=issuer, expected_type=type_hints["issuer"])
            check_type(argname="argument secrets_manager_arn", value=secrets_manager_arn, expected_type=type_hints["secrets_manager_arn"])
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            check_type(argname="argument user_name_attribute_field", value=user_name_attribute_field, expected_type=type_hints["user_name_attribute_field"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key_location": key_location,
        }
        if claim_regex is not None:
            self._values["claim_regex"] = claim_regex
        if group_attribute_field is not None:
            self._values["group_attribute_field"] = group_attribute_field
        if issuer is not None:
            self._values["issuer"] = issuer
        if secrets_manager_arn is not None:
            self._values["secrets_manager_arn"] = secrets_manager_arn
        if url is not None:
            self._values["url"] = url
        if user_name_attribute_field is not None:
            self._values["user_name_attribute_field"] = user_name_attribute_field

    @builtins.property
    def key_location(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#key_location KendraIndex#key_location}.'''
        result = self._values.get("key_location")
        assert result is not None, "Required property 'key_location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def claim_regex(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#claim_regex KendraIndex#claim_regex}.'''
        result = self._values.get("claim_regex")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def group_attribute_field(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#group_attribute_field KendraIndex#group_attribute_field}.'''
        result = self._values.get("group_attribute_field")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def issuer(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#issuer KendraIndex#issuer}.'''
        result = self._values.get("issuer")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def secrets_manager_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#secrets_manager_arn KendraIndex#secrets_manager_arn}.'''
        result = self._values.get("secrets_manager_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#url KendraIndex#url}.'''
        result = self._values.get("url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_name_attribute_field(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#user_name_attribute_field KendraIndex#user_name_attribute_field}.'''
        result = self._values.get("user_name_attribute_field")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraIndexUserTokenConfigurationsJwtTokenTypeConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KendraIndexUserTokenConfigurationsJwtTokenTypeConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kendraIndex.KendraIndexUserTokenConfigurationsJwtTokenTypeConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__56083affe4f797da793b970766bd5ba393a8040fb5ad360980275646ae41de36)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetClaimRegex")
    def reset_claim_regex(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClaimRegex", []))

    @jsii.member(jsii_name="resetGroupAttributeField")
    def reset_group_attribute_field(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroupAttributeField", []))

    @jsii.member(jsii_name="resetIssuer")
    def reset_issuer(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIssuer", []))

    @jsii.member(jsii_name="resetSecretsManagerArn")
    def reset_secrets_manager_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecretsManagerArn", []))

    @jsii.member(jsii_name="resetUrl")
    def reset_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUrl", []))

    @jsii.member(jsii_name="resetUserNameAttributeField")
    def reset_user_name_attribute_field(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserNameAttributeField", []))

    @builtins.property
    @jsii.member(jsii_name="claimRegexInput")
    def claim_regex_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "claimRegexInput"))

    @builtins.property
    @jsii.member(jsii_name="groupAttributeFieldInput")
    def group_attribute_field_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "groupAttributeFieldInput"))

    @builtins.property
    @jsii.member(jsii_name="issuerInput")
    def issuer_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "issuerInput"))

    @builtins.property
    @jsii.member(jsii_name="keyLocationInput")
    def key_location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyLocationInput"))

    @builtins.property
    @jsii.member(jsii_name="secretsManagerArnInput")
    def secrets_manager_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretsManagerArnInput"))

    @builtins.property
    @jsii.member(jsii_name="urlInput")
    def url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlInput"))

    @builtins.property
    @jsii.member(jsii_name="userNameAttributeFieldInput")
    def user_name_attribute_field_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userNameAttributeFieldInput"))

    @builtins.property
    @jsii.member(jsii_name="claimRegex")
    def claim_regex(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "claimRegex"))

    @claim_regex.setter
    def claim_regex(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c758ae3f88f1e2d0e0e27056e139f13c563fd0b9537cba1f70c1cf01eb65fd3f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "claimRegex", value)

    @builtins.property
    @jsii.member(jsii_name="groupAttributeField")
    def group_attribute_field(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "groupAttributeField"))

    @group_attribute_field.setter
    def group_attribute_field(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bdc66ef85eeb841ffa1ea75b4a24011d3ca6c1fcabbc169d45eaa4f9e37fe883)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupAttributeField", value)

    @builtins.property
    @jsii.member(jsii_name="issuer")
    def issuer(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "issuer"))

    @issuer.setter
    def issuer(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__feffd125916ff3163b32a2f3e9faadd3f28e5629ebf128d6a94b0d7444948830)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "issuer", value)

    @builtins.property
    @jsii.member(jsii_name="keyLocation")
    def key_location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyLocation"))

    @key_location.setter
    def key_location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6a9be2e6376601a0a70d7eb52adde2b3a3dc25afa1b4deca0afcd724cf94dbc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyLocation", value)

    @builtins.property
    @jsii.member(jsii_name="secretsManagerArn")
    def secrets_manager_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretsManagerArn"))

    @secrets_manager_arn.setter
    def secrets_manager_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e78641311c63c5c0896654934acd3006ea877d566a28cbdbf079d0436d49d57)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretsManagerArn", value)

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @url.setter
    def url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b9c1c5aff5e5f07956215f703f941089ef7d6041f8532e70c230d31bdffd3e9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)

    @builtins.property
    @jsii.member(jsii_name="userNameAttributeField")
    def user_name_attribute_field(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userNameAttributeField"))

    @user_name_attribute_field.setter
    def user_name_attribute_field(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7914b4354fe3253ebddf8321334fafdbdc2fb7c6be6897ab7a1ee020fbdee2c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userNameAttributeField", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KendraIndexUserTokenConfigurationsJwtTokenTypeConfiguration]:
        return typing.cast(typing.Optional[KendraIndexUserTokenConfigurationsJwtTokenTypeConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KendraIndexUserTokenConfigurationsJwtTokenTypeConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1789fdcd3baaeb3cf099e02b232ff2369eef8e7fdb6c7dac220eed7ee36c5aa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KendraIndexUserTokenConfigurationsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kendraIndex.KendraIndexUserTokenConfigurationsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9d562d3625b6a2647b08ed3d9f06ebbf0259e295177e4f7ac8f27b5c56cb0974)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putJsonTokenTypeConfiguration")
    def put_json_token_type_configuration(
        self,
        *,
        group_attribute_field: builtins.str,
        user_name_attribute_field: builtins.str,
    ) -> None:
        '''
        :param group_attribute_field: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#group_attribute_field KendraIndex#group_attribute_field}.
        :param user_name_attribute_field: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#user_name_attribute_field KendraIndex#user_name_attribute_field}.
        '''
        value = KendraIndexUserTokenConfigurationsJsonTokenTypeConfiguration(
            group_attribute_field=group_attribute_field,
            user_name_attribute_field=user_name_attribute_field,
        )

        return typing.cast(None, jsii.invoke(self, "putJsonTokenTypeConfiguration", [value]))

    @jsii.member(jsii_name="putJwtTokenTypeConfiguration")
    def put_jwt_token_type_configuration(
        self,
        *,
        key_location: builtins.str,
        claim_regex: typing.Optional[builtins.str] = None,
        group_attribute_field: typing.Optional[builtins.str] = None,
        issuer: typing.Optional[builtins.str] = None,
        secrets_manager_arn: typing.Optional[builtins.str] = None,
        url: typing.Optional[builtins.str] = None,
        user_name_attribute_field: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param key_location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#key_location KendraIndex#key_location}.
        :param claim_regex: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#claim_regex KendraIndex#claim_regex}.
        :param group_attribute_field: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#group_attribute_field KendraIndex#group_attribute_field}.
        :param issuer: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#issuer KendraIndex#issuer}.
        :param secrets_manager_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#secrets_manager_arn KendraIndex#secrets_manager_arn}.
        :param url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#url KendraIndex#url}.
        :param user_name_attribute_field: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#user_name_attribute_field KendraIndex#user_name_attribute_field}.
        '''
        value = KendraIndexUserTokenConfigurationsJwtTokenTypeConfiguration(
            key_location=key_location,
            claim_regex=claim_regex,
            group_attribute_field=group_attribute_field,
            issuer=issuer,
            secrets_manager_arn=secrets_manager_arn,
            url=url,
            user_name_attribute_field=user_name_attribute_field,
        )

        return typing.cast(None, jsii.invoke(self, "putJwtTokenTypeConfiguration", [value]))

    @jsii.member(jsii_name="resetJsonTokenTypeConfiguration")
    def reset_json_token_type_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJsonTokenTypeConfiguration", []))

    @jsii.member(jsii_name="resetJwtTokenTypeConfiguration")
    def reset_jwt_token_type_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJwtTokenTypeConfiguration", []))

    @builtins.property
    @jsii.member(jsii_name="jsonTokenTypeConfiguration")
    def json_token_type_configuration(
        self,
    ) -> KendraIndexUserTokenConfigurationsJsonTokenTypeConfigurationOutputReference:
        return typing.cast(KendraIndexUserTokenConfigurationsJsonTokenTypeConfigurationOutputReference, jsii.get(self, "jsonTokenTypeConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="jwtTokenTypeConfiguration")
    def jwt_token_type_configuration(
        self,
    ) -> KendraIndexUserTokenConfigurationsJwtTokenTypeConfigurationOutputReference:
        return typing.cast(KendraIndexUserTokenConfigurationsJwtTokenTypeConfigurationOutputReference, jsii.get(self, "jwtTokenTypeConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="jsonTokenTypeConfigurationInput")
    def json_token_type_configuration_input(
        self,
    ) -> typing.Optional[KendraIndexUserTokenConfigurationsJsonTokenTypeConfiguration]:
        return typing.cast(typing.Optional[KendraIndexUserTokenConfigurationsJsonTokenTypeConfiguration], jsii.get(self, "jsonTokenTypeConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="jwtTokenTypeConfigurationInput")
    def jwt_token_type_configuration_input(
        self,
    ) -> typing.Optional[KendraIndexUserTokenConfigurationsJwtTokenTypeConfiguration]:
        return typing.cast(typing.Optional[KendraIndexUserTokenConfigurationsJwtTokenTypeConfiguration], jsii.get(self, "jwtTokenTypeConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[KendraIndexUserTokenConfigurations]:
        return typing.cast(typing.Optional[KendraIndexUserTokenConfigurations], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KendraIndexUserTokenConfigurations],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a783e5d373e498bef5128a5854ae38da2d58301fc2387d4a8a91077ae8bfe59)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "KendraIndex",
    "KendraIndexCapacityUnits",
    "KendraIndexCapacityUnitsOutputReference",
    "KendraIndexConfig",
    "KendraIndexDocumentMetadataConfigurationUpdates",
    "KendraIndexDocumentMetadataConfigurationUpdatesList",
    "KendraIndexDocumentMetadataConfigurationUpdatesOutputReference",
    "KendraIndexDocumentMetadataConfigurationUpdatesRelevance",
    "KendraIndexDocumentMetadataConfigurationUpdatesRelevanceOutputReference",
    "KendraIndexDocumentMetadataConfigurationUpdatesSearch",
    "KendraIndexDocumentMetadataConfigurationUpdatesSearchOutputReference",
    "KendraIndexIndexStatistics",
    "KendraIndexIndexStatisticsFaqStatistics",
    "KendraIndexIndexStatisticsFaqStatisticsList",
    "KendraIndexIndexStatisticsFaqStatisticsOutputReference",
    "KendraIndexIndexStatisticsList",
    "KendraIndexIndexStatisticsOutputReference",
    "KendraIndexIndexStatisticsTextDocumentStatistics",
    "KendraIndexIndexStatisticsTextDocumentStatisticsList",
    "KendraIndexIndexStatisticsTextDocumentStatisticsOutputReference",
    "KendraIndexServerSideEncryptionConfiguration",
    "KendraIndexServerSideEncryptionConfigurationOutputReference",
    "KendraIndexTimeouts",
    "KendraIndexTimeoutsOutputReference",
    "KendraIndexUserGroupResolutionConfiguration",
    "KendraIndexUserGroupResolutionConfigurationOutputReference",
    "KendraIndexUserTokenConfigurations",
    "KendraIndexUserTokenConfigurationsJsonTokenTypeConfiguration",
    "KendraIndexUserTokenConfigurationsJsonTokenTypeConfigurationOutputReference",
    "KendraIndexUserTokenConfigurationsJwtTokenTypeConfiguration",
    "KendraIndexUserTokenConfigurationsJwtTokenTypeConfigurationOutputReference",
    "KendraIndexUserTokenConfigurationsOutputReference",
]

publication.publish()

def _typecheckingstub__6cc05f833374c9542a540232dbe21c7cc75295c7e5f244fc02b3c722af1efae7(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    role_arn: builtins.str,
    capacity_units: typing.Optional[typing.Union[KendraIndexCapacityUnits, typing.Dict[builtins.str, typing.Any]]] = None,
    description: typing.Optional[builtins.str] = None,
    document_metadata_configuration_updates: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KendraIndexDocumentMetadataConfigurationUpdates, typing.Dict[builtins.str, typing.Any]]]]] = None,
    edition: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    server_side_encryption_configuration: typing.Optional[typing.Union[KendraIndexServerSideEncryptionConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[KendraIndexTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    user_context_policy: typing.Optional[builtins.str] = None,
    user_group_resolution_configuration: typing.Optional[typing.Union[KendraIndexUserGroupResolutionConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    user_token_configurations: typing.Optional[typing.Union[KendraIndexUserTokenConfigurations, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__317ad6c0ec67af5355f527272eb05a40e5ca24d96fa415da39ac8a37c7537b9f(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KendraIndexDocumentMetadataConfigurationUpdates, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85b9c3a7a47b094f769bfdaa18b236f40540e142be44ffeaf6d653480048f59a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4200f70d6b182bbe6d304dd57efa9054fef52710f2186c5335c000a5fef9bff(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc9ea64b34d57326fe8bca3de1fe170dd376aba15c6de57c0a740ba87878c867(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03af841c623ff3a31df66c6a2afb2782bb67d5386cc063bafffd1f525cd82313(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c82e6bb759da5f8c416069382b3728fea842d9d6675b1d95e6b667ad61d8291(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a78c71ab67b873d93d2c0ee88cfd363236adba79642b9874bdd1b5f11c52dbe(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__942da8a169cdbc0605436c7c6fe02971fd8016ae1badbc1d50925c35f5539ac4(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dfa87804ac91333b7c1bd61dda6ec2879692cb125fd63566c585246dda720d2e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23cdc91c06b29947aa2f76415fb9a3f9639ec1eecc9b904663041077dab4b330(
    *,
    query_capacity_units: typing.Optional[jsii.Number] = None,
    storage_capacity_units: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__079b647406565e98b37a3c998ce0ee4293136cdf65ae8e5018da703b72c0662e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43b59a2bed2c4b7fcda264d1a2713c0ac9e97f18907a0d5ceda334cec9b4bf1f(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2522fa3202b012f8851e9c57e97530bceab8062a39473dfdd65286e809b4b792(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec727b8ff63bc0b894caad06c2faced0b32e8890e059023d7b3a7ffe8fee782e(
    value: typing.Optional[KendraIndexCapacityUnits],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4ff6fa56be947cd554947c8192e4239d1010054744709493a96ee9369abcc15(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: builtins.str,
    role_arn: builtins.str,
    capacity_units: typing.Optional[typing.Union[KendraIndexCapacityUnits, typing.Dict[builtins.str, typing.Any]]] = None,
    description: typing.Optional[builtins.str] = None,
    document_metadata_configuration_updates: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KendraIndexDocumentMetadataConfigurationUpdates, typing.Dict[builtins.str, typing.Any]]]]] = None,
    edition: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    server_side_encryption_configuration: typing.Optional[typing.Union[KendraIndexServerSideEncryptionConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[KendraIndexTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    user_context_policy: typing.Optional[builtins.str] = None,
    user_group_resolution_configuration: typing.Optional[typing.Union[KendraIndexUserGroupResolutionConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    user_token_configurations: typing.Optional[typing.Union[KendraIndexUserTokenConfigurations, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1432211c64fe1ef4e714835b86ef81f83ada0495f8dd31ec1e624613259e15ac(
    *,
    name: builtins.str,
    type: builtins.str,
    relevance: typing.Optional[typing.Union[KendraIndexDocumentMetadataConfigurationUpdatesRelevance, typing.Dict[builtins.str, typing.Any]]] = None,
    search: typing.Optional[typing.Union[KendraIndexDocumentMetadataConfigurationUpdatesSearch, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e9fdb36caf7237261e98c9b8f1e5e211c1179719d3fdb3e6665b2adef636ed0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8fd06100a4d52496c397089184231462f1027102a4ab53ee1c3a10b757f81db(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__586462835eaf437a24854951415429904fd881e6bd0d168ea5eccb0e44a70d0c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb59be7686e61bc4d1f4388184d69c868d3e24d38ab6789b0463df251af2ebb6(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc1a89e92eade101ebbe4ed33aeff5cba2d2af14dc43cd7a622bd7c71cdb8b8e(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a59d3df674310cf540f5c7457aecd2127f2e64dbe782d5f901a3eae551f4e86e(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KendraIndexDocumentMetadataConfigurationUpdates]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf9b0c810bd1503ec402e0870158989d3e22293bcb27873d7a54aed17a62ee0a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7304f008208c6e71cf48cc71999f566429719d2399457f88aa4e18b00a06317b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7470d9657792679f48c8896a1e1c5f4c31bc7622b2c7e79499bf4aca60e5bbc1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6f07c20e6d38d44ede62b39e1a259ac0406cf455200301f96cd4b0fd2c512fb(
    value: typing.Optional[typing.Union[KendraIndexDocumentMetadataConfigurationUpdates, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__191fe18db0b51ef0920f9ffdbb2a5fba8903a149af9adf3f924f59ac11694713(
    *,
    duration: typing.Optional[builtins.str] = None,
    freshness: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    importance: typing.Optional[jsii.Number] = None,
    rank_order: typing.Optional[builtins.str] = None,
    values_importance_map: typing.Optional[typing.Mapping[builtins.str, jsii.Number]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__844c8748f3768aee71b1ca973a2f5f896a1a32278c88446b857e039f284a79ea(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ff6f499d488d75de8aa1e2cb4b030314e48faabdabf9d6516936addce53eedb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58b4b3af7e3aa10f0c02b69e7ed0dd48073183c3c0299794a12981c2aba9c839(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e262f3bbb79727fb9a07ae5b16f10d809e4e43e937ae69a4de80b82b66d1bd4(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aebd1de6a1e79bb4093fecbb8697c74db7467d94dbca32bd87d7cec691db1a85(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4912b804d6e1d632ef23418000f8f70133a89cce2f877b4e278da9493b48b7fe(
    value: typing.Mapping[builtins.str, jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__537fcb26bd7dfd1ee1f8d6f92306298d5bb3b7d97228e436575f38ef63069258(
    value: typing.Optional[KendraIndexDocumentMetadataConfigurationUpdatesRelevance],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b025e7a3bc854142b4eb81ae6bfa269ccaf37d4e98675a2a2f679e4d1a9f980(
    *,
    displayable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    facetable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    searchable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    sortable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5aca906027681fb73aa0434b0a9b726c5a6d8a1da7867ef6d847e5dd1a12dc42(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92978cf4be165e80dfd543d3ca7257cdf28f9126190463e6c0acc3014ea11c72(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59de78ac4f39e3d367253c83542ee600fc24f32612f36c60e288f3f8759f7652(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8b249c9a262cdd975f52fee727e75d34ff636214441d40e4ac7ce5930d7ae7c(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98dbf528dd03b5b833cde6cf73cae4b50091a70634e2b233896ed7ebd2c815cd(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5068d2fca82dfddd3ef5011bdd564df8e6f0434e01e726cc2bda6f0f394d9232(
    value: typing.Optional[KendraIndexDocumentMetadataConfigurationUpdatesSearch],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa1796639c1dffdf9566e44cc7b07ec830754e38ac0c159b07d34ed85d9a0953(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58f0dab61a67c6498a474091dece91b02e9e9175b34434e2279de1b54a068192(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c74f6f572da75fe994fe62cd9bc88790abe550854f027aac96d7c044d5bbe06c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48d05c5ed7f286ba33cc4ee45b8625ff56a227e385a077cad6cd898feaa4b8c3(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b06b0bb1fb3e9a78a161dd1e99e02afaebbe366e446b84f7eaccf1ac57fc65a(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b9b05033295e5c3042610dcc190f4e1ebbe548b9c0430547ca31acb444dd93d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89e9ba22f965e2c87f5c70da1d021af415f8bc9df81f903f8d9bed74e56b91b0(
    value: typing.Optional[KendraIndexIndexStatisticsFaqStatistics],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__719dda1a32f4c740130b4054fc72696170454ffcb9aa69cb580ec2b5ee57ba81(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f33f863d39fedd2982736263f89e3c185371cb001687f21f71d3e8afb30f203a(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92b6a62297e17fb7e851abcdd4832bd8f988d0a62e066952b348108106a7c95a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b963b3f294e4b106f9e21eac546a5c7d33d249eb2f2bcd92706d8678b96c8dcd(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2376248be3f846e7f05963904be7c7f94691b575e11cfb846b59a20f77b67b7c(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__232f1a943b0f0d96f419a60d2510072c367a51cf703018200190519eef909634(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f903c27aec73a56a43e62d7f4b1354be6119d5c3c637a102741e3f30cb1d020(
    value: typing.Optional[KendraIndexIndexStatistics],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__443480c8be136e2d50f89bf247ee18724847bd923d701f29560eab77f704b5e8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c973f4e1d86cdefea1a9e3af8f2740c232c255b7e899109f754310086f68419(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10bb04ba34a726de2e32213402e730e8a325b5259934d0af83d92db13f9be151(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__578654f5e8b112520f04de7e1606201840edf02a527fd5c845439f9db4148cb1(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4377113fb3dffd43266d9f6198a5d09142fdd7c31523fc6948ddb7ffe71df2cd(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87be49f2d5648a96aff24be86cae7f8f266c02502b7461e6f2b8ec6591b4dfb1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e75d396ab6072debce7280f2579c385f3d02354a67c6d81141d9d2377294cb3c(
    value: typing.Optional[KendraIndexIndexStatisticsTextDocumentStatistics],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c17a0777718e2fab857521dfb4afc9c2c7543ac6cab0c5058bb9fe598d241030(
    *,
    kms_key_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__459966a2dd4acf63c0e80c30d67acf6612f3b651db4f498a3876a524578f8a38(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e657097717c22142701b9d7d7da68cb8d74018e8de0147b6d158d1553c6b4f9b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d8591676f114920e96cb7118e40171e0f461393ab5d5b325655c1ed40319f55(
    value: typing.Optional[KendraIndexServerSideEncryptionConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67a155ba84fb94702e1f2b8ec4feecbabb468282e2e335d151f59a4570c5c1fc(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61b30ecbf143f97261cd4691a09a40020b632aae5693fbad5a36c22380a28ed0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ed4c23ae43c2673afbb450942d0971c117066c1649d3887f924920daaf8919d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0dfad4d1f97828943a4a04f45433da5554c69d299f3a8bf59a1035d9c1ed0f3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80cbdc951787b2c3296fd56cc4a69fcde03860a17f620df16f63aeacca56c995(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f40b9d2b4f7086c82ff82e8c9267ca596ce511b118518f860abf2735a301de29(
    value: typing.Optional[typing.Union[KendraIndexTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35d72b19451c0d70c5bbfbe10fd7f6dce83d82c9d691caeb38d7d84c1d2378ca(
    *,
    user_group_resolution_mode: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f981222c4dcba374ad4fb1529e024cd7d3b865f3503acedf61d5b39d72b7bd49(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3867aaeba638541995b4c91fd937895931aa05eab813594ab6f3d9eb65d2b8fb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__177986dc33defa107ebeeff8f116434b1c9bbb8d4a3a154379ccd26058210976(
    value: typing.Optional[KendraIndexUserGroupResolutionConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ecdfa6cfd97e1f6cf88ba9cd3a23cf358bc23ae4c9a0dd39fa123dbd8151950b(
    *,
    json_token_type_configuration: typing.Optional[typing.Union[KendraIndexUserTokenConfigurationsJsonTokenTypeConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    jwt_token_type_configuration: typing.Optional[typing.Union[KendraIndexUserTokenConfigurationsJwtTokenTypeConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac3b0311dc299f5c66335497e916dd453a7e0bb18af5fdff679d56153c1cf3cf(
    *,
    group_attribute_field: builtins.str,
    user_name_attribute_field: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70615b1fdf1aa1a84f31d4938efd49fbfa90082dfe4acd8c60f9da0b2a4064e1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f7082c7c7bd4076f08e6efa1e630ff26072636a0b09b00529e31c8be858024d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61a757653d381572b5ba312c9ee90f77c8cf44ce9570825a03582d2c6a5b1e26(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f49d35aa1415f9bbf7f28e6e156e3a53c0cc7b7c3314b9b649c6795b3b2f2e3(
    value: typing.Optional[KendraIndexUserTokenConfigurationsJsonTokenTypeConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e840cf5a68a8e4348923b1037e42335df0c67eddca0a038da5b620178bceaa7(
    *,
    key_location: builtins.str,
    claim_regex: typing.Optional[builtins.str] = None,
    group_attribute_field: typing.Optional[builtins.str] = None,
    issuer: typing.Optional[builtins.str] = None,
    secrets_manager_arn: typing.Optional[builtins.str] = None,
    url: typing.Optional[builtins.str] = None,
    user_name_attribute_field: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56083affe4f797da793b970766bd5ba393a8040fb5ad360980275646ae41de36(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c758ae3f88f1e2d0e0e27056e139f13c563fd0b9537cba1f70c1cf01eb65fd3f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bdc66ef85eeb841ffa1ea75b4a24011d3ca6c1fcabbc169d45eaa4f9e37fe883(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__feffd125916ff3163b32a2f3e9faadd3f28e5629ebf128d6a94b0d7444948830(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6a9be2e6376601a0a70d7eb52adde2b3a3dc25afa1b4deca0afcd724cf94dbc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e78641311c63c5c0896654934acd3006ea877d566a28cbdbf079d0436d49d57(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b9c1c5aff5e5f07956215f703f941089ef7d6041f8532e70c230d31bdffd3e9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7914b4354fe3253ebddf8321334fafdbdc2fb7c6be6897ab7a1ee020fbdee2c5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1789fdcd3baaeb3cf099e02b232ff2369eef8e7fdb6c7dac220eed7ee36c5aa(
    value: typing.Optional[KendraIndexUserTokenConfigurationsJwtTokenTypeConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d562d3625b6a2647b08ed3d9f06ebbf0259e295177e4f7ac8f27b5c56cb0974(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a783e5d373e498bef5128a5854ae38da2d58301fc2387d4a8a91077ae8bfe59(
    value: typing.Optional[KendraIndexUserTokenConfigurations],
) -> None:
    """Type checking stubs"""
    pass
