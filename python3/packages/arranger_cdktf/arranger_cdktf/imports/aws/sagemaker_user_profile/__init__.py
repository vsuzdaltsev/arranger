'''
# `aws_sagemaker_user_profile`

Refer to the Terraform Registory for docs: [`aws_sagemaker_user_profile`](https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile).
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


class SagemakerUserProfile(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerUserProfile.SagemakerUserProfile",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile aws_sagemaker_user_profile}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        domain_id: builtins.str,
        user_profile_name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        single_sign_on_user_identifier: typing.Optional[builtins.str] = None,
        single_sign_on_user_value: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        user_settings: typing.Optional[typing.Union["SagemakerUserProfileUserSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile aws_sagemaker_user_profile} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param domain_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#domain_id SagemakerUserProfile#domain_id}.
        :param user_profile_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#user_profile_name SagemakerUserProfile#user_profile_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#id SagemakerUserProfile#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param single_sign_on_user_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#single_sign_on_user_identifier SagemakerUserProfile#single_sign_on_user_identifier}.
        :param single_sign_on_user_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#single_sign_on_user_value SagemakerUserProfile#single_sign_on_user_value}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#tags SagemakerUserProfile#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#tags_all SagemakerUserProfile#tags_all}.
        :param user_settings: user_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#user_settings SagemakerUserProfile#user_settings}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd3ea87bdcd92be1b32a569209e58887a4b8cf0a1129184e09781056af0e21c7)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = SagemakerUserProfileConfig(
            domain_id=domain_id,
            user_profile_name=user_profile_name,
            id=id,
            single_sign_on_user_identifier=single_sign_on_user_identifier,
            single_sign_on_user_value=single_sign_on_user_value,
            tags=tags,
            tags_all=tags_all,
            user_settings=user_settings,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putUserSettings")
    def put_user_settings(
        self,
        *,
        execution_role: builtins.str,
        canvas_app_settings: typing.Optional[typing.Union["SagemakerUserProfileUserSettingsCanvasAppSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        jupyter_server_app_settings: typing.Optional[typing.Union["SagemakerUserProfileUserSettingsJupyterServerAppSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        kernel_gateway_app_settings: typing.Optional[typing.Union["SagemakerUserProfileUserSettingsKernelGatewayAppSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        r_session_app_settings: typing.Optional[typing.Union["SagemakerUserProfileUserSettingsRSessionAppSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        sharing_settings: typing.Optional[typing.Union["SagemakerUserProfileUserSettingsSharingSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        tensor_board_app_settings: typing.Optional[typing.Union["SagemakerUserProfileUserSettingsTensorBoardAppSettings", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param execution_role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#execution_role SagemakerUserProfile#execution_role}.
        :param canvas_app_settings: canvas_app_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#canvas_app_settings SagemakerUserProfile#canvas_app_settings}
        :param jupyter_server_app_settings: jupyter_server_app_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#jupyter_server_app_settings SagemakerUserProfile#jupyter_server_app_settings}
        :param kernel_gateway_app_settings: kernel_gateway_app_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#kernel_gateway_app_settings SagemakerUserProfile#kernel_gateway_app_settings}
        :param r_session_app_settings: r_session_app_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#r_session_app_settings SagemakerUserProfile#r_session_app_settings}
        :param security_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#security_groups SagemakerUserProfile#security_groups}.
        :param sharing_settings: sharing_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#sharing_settings SagemakerUserProfile#sharing_settings}
        :param tensor_board_app_settings: tensor_board_app_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#tensor_board_app_settings SagemakerUserProfile#tensor_board_app_settings}
        '''
        value = SagemakerUserProfileUserSettings(
            execution_role=execution_role,
            canvas_app_settings=canvas_app_settings,
            jupyter_server_app_settings=jupyter_server_app_settings,
            kernel_gateway_app_settings=kernel_gateway_app_settings,
            r_session_app_settings=r_session_app_settings,
            security_groups=security_groups,
            sharing_settings=sharing_settings,
            tensor_board_app_settings=tensor_board_app_settings,
        )

        return typing.cast(None, jsii.invoke(self, "putUserSettings", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetSingleSignOnUserIdentifier")
    def reset_single_sign_on_user_identifier(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSingleSignOnUserIdentifier", []))

    @jsii.member(jsii_name="resetSingleSignOnUserValue")
    def reset_single_sign_on_user_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSingleSignOnUserValue", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetUserSettings")
    def reset_user_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserSettings", []))

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
    @jsii.member(jsii_name="homeEfsFileSystemUid")
    def home_efs_file_system_uid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "homeEfsFileSystemUid"))

    @builtins.property
    @jsii.member(jsii_name="userSettings")
    def user_settings(self) -> "SagemakerUserProfileUserSettingsOutputReference":
        return typing.cast("SagemakerUserProfileUserSettingsOutputReference", jsii.get(self, "userSettings"))

    @builtins.property
    @jsii.member(jsii_name="domainIdInput")
    def domain_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="singleSignOnUserIdentifierInput")
    def single_sign_on_user_identifier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "singleSignOnUserIdentifierInput"))

    @builtins.property
    @jsii.member(jsii_name="singleSignOnUserValueInput")
    def single_sign_on_user_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "singleSignOnUserValueInput"))

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
    @jsii.member(jsii_name="userProfileNameInput")
    def user_profile_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userProfileNameInput"))

    @builtins.property
    @jsii.member(jsii_name="userSettingsInput")
    def user_settings_input(
        self,
    ) -> typing.Optional["SagemakerUserProfileUserSettings"]:
        return typing.cast(typing.Optional["SagemakerUserProfileUserSettings"], jsii.get(self, "userSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="domainId")
    def domain_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domainId"))

    @domain_id.setter
    def domain_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f191d7eca73a9f60a900618beb667ee009bebe2670ccecfe43d60e6d438cfd88)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__808b16b8d7c4ea3f2731d5af691fce921dd7435185f039b66b4b260c24a1dabe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="singleSignOnUserIdentifier")
    def single_sign_on_user_identifier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "singleSignOnUserIdentifier"))

    @single_sign_on_user_identifier.setter
    def single_sign_on_user_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd3cb9bd75b15bf6e99b0beb2380934cb7b45f235ad47337fc9e5b263441ce87)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "singleSignOnUserIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="singleSignOnUserValue")
    def single_sign_on_user_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "singleSignOnUserValue"))

    @single_sign_on_user_value.setter
    def single_sign_on_user_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35363910df4c7179a01ce3816eed74e3adfc522587c04b7e7968b5a243bd8c71)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "singleSignOnUserValue", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24516786d954c54762fef986c2eede5291c4f6a14a7776c9dfb4afedc49dec8a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ff0dd72283a8b4a3a327bd40b9ff2042f99605d1c166fb80bc960211d0b3ecb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)

    @builtins.property
    @jsii.member(jsii_name="userProfileName")
    def user_profile_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userProfileName"))

    @user_profile_name.setter
    def user_profile_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2fc6398015cf63d1543035ffbb9dd11c4d0e50146d3796b1de861f58c034e4cf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userProfileName", value)


@jsii.data_type(
    jsii_type="aws.sagemakerUserProfile.SagemakerUserProfileConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "domain_id": "domainId",
        "user_profile_name": "userProfileName",
        "id": "id",
        "single_sign_on_user_identifier": "singleSignOnUserIdentifier",
        "single_sign_on_user_value": "singleSignOnUserValue",
        "tags": "tags",
        "tags_all": "tagsAll",
        "user_settings": "userSettings",
    },
)
class SagemakerUserProfileConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        domain_id: builtins.str,
        user_profile_name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        single_sign_on_user_identifier: typing.Optional[builtins.str] = None,
        single_sign_on_user_value: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        user_settings: typing.Optional[typing.Union["SagemakerUserProfileUserSettings", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param domain_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#domain_id SagemakerUserProfile#domain_id}.
        :param user_profile_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#user_profile_name SagemakerUserProfile#user_profile_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#id SagemakerUserProfile#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param single_sign_on_user_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#single_sign_on_user_identifier SagemakerUserProfile#single_sign_on_user_identifier}.
        :param single_sign_on_user_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#single_sign_on_user_value SagemakerUserProfile#single_sign_on_user_value}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#tags SagemakerUserProfile#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#tags_all SagemakerUserProfile#tags_all}.
        :param user_settings: user_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#user_settings SagemakerUserProfile#user_settings}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(user_settings, dict):
            user_settings = SagemakerUserProfileUserSettings(**user_settings)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73cd0fc9769617e44b2bd2cdd0bc0b572bb10551fe90a1cc4970a84d40792226)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument domain_id", value=domain_id, expected_type=type_hints["domain_id"])
            check_type(argname="argument user_profile_name", value=user_profile_name, expected_type=type_hints["user_profile_name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument single_sign_on_user_identifier", value=single_sign_on_user_identifier, expected_type=type_hints["single_sign_on_user_identifier"])
            check_type(argname="argument single_sign_on_user_value", value=single_sign_on_user_value, expected_type=type_hints["single_sign_on_user_value"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument user_settings", value=user_settings, expected_type=type_hints["user_settings"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_id": domain_id,
            "user_profile_name": user_profile_name,
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
        if id is not None:
            self._values["id"] = id
        if single_sign_on_user_identifier is not None:
            self._values["single_sign_on_user_identifier"] = single_sign_on_user_identifier
        if single_sign_on_user_value is not None:
            self._values["single_sign_on_user_value"] = single_sign_on_user_value
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if user_settings is not None:
            self._values["user_settings"] = user_settings

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
    def domain_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#domain_id SagemakerUserProfile#domain_id}.'''
        result = self._values.get("domain_id")
        assert result is not None, "Required property 'domain_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_profile_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#user_profile_name SagemakerUserProfile#user_profile_name}.'''
        result = self._values.get("user_profile_name")
        assert result is not None, "Required property 'user_profile_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#id SagemakerUserProfile#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def single_sign_on_user_identifier(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#single_sign_on_user_identifier SagemakerUserProfile#single_sign_on_user_identifier}.'''
        result = self._values.get("single_sign_on_user_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def single_sign_on_user_value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#single_sign_on_user_value SagemakerUserProfile#single_sign_on_user_value}.'''
        result = self._values.get("single_sign_on_user_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#tags SagemakerUserProfile#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#tags_all SagemakerUserProfile#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def user_settings(self) -> typing.Optional["SagemakerUserProfileUserSettings"]:
        '''user_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#user_settings SagemakerUserProfile#user_settings}
        '''
        result = self._values.get("user_settings")
        return typing.cast(typing.Optional["SagemakerUserProfileUserSettings"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerUserProfileConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.sagemakerUserProfile.SagemakerUserProfileUserSettings",
    jsii_struct_bases=[],
    name_mapping={
        "execution_role": "executionRole",
        "canvas_app_settings": "canvasAppSettings",
        "jupyter_server_app_settings": "jupyterServerAppSettings",
        "kernel_gateway_app_settings": "kernelGatewayAppSettings",
        "r_session_app_settings": "rSessionAppSettings",
        "security_groups": "securityGroups",
        "sharing_settings": "sharingSettings",
        "tensor_board_app_settings": "tensorBoardAppSettings",
    },
)
class SagemakerUserProfileUserSettings:
    def __init__(
        self,
        *,
        execution_role: builtins.str,
        canvas_app_settings: typing.Optional[typing.Union["SagemakerUserProfileUserSettingsCanvasAppSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        jupyter_server_app_settings: typing.Optional[typing.Union["SagemakerUserProfileUserSettingsJupyterServerAppSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        kernel_gateway_app_settings: typing.Optional[typing.Union["SagemakerUserProfileUserSettingsKernelGatewayAppSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        r_session_app_settings: typing.Optional[typing.Union["SagemakerUserProfileUserSettingsRSessionAppSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        sharing_settings: typing.Optional[typing.Union["SagemakerUserProfileUserSettingsSharingSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        tensor_board_app_settings: typing.Optional[typing.Union["SagemakerUserProfileUserSettingsTensorBoardAppSettings", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param execution_role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#execution_role SagemakerUserProfile#execution_role}.
        :param canvas_app_settings: canvas_app_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#canvas_app_settings SagemakerUserProfile#canvas_app_settings}
        :param jupyter_server_app_settings: jupyter_server_app_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#jupyter_server_app_settings SagemakerUserProfile#jupyter_server_app_settings}
        :param kernel_gateway_app_settings: kernel_gateway_app_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#kernel_gateway_app_settings SagemakerUserProfile#kernel_gateway_app_settings}
        :param r_session_app_settings: r_session_app_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#r_session_app_settings SagemakerUserProfile#r_session_app_settings}
        :param security_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#security_groups SagemakerUserProfile#security_groups}.
        :param sharing_settings: sharing_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#sharing_settings SagemakerUserProfile#sharing_settings}
        :param tensor_board_app_settings: tensor_board_app_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#tensor_board_app_settings SagemakerUserProfile#tensor_board_app_settings}
        '''
        if isinstance(canvas_app_settings, dict):
            canvas_app_settings = SagemakerUserProfileUserSettingsCanvasAppSettings(**canvas_app_settings)
        if isinstance(jupyter_server_app_settings, dict):
            jupyter_server_app_settings = SagemakerUserProfileUserSettingsJupyterServerAppSettings(**jupyter_server_app_settings)
        if isinstance(kernel_gateway_app_settings, dict):
            kernel_gateway_app_settings = SagemakerUserProfileUserSettingsKernelGatewayAppSettings(**kernel_gateway_app_settings)
        if isinstance(r_session_app_settings, dict):
            r_session_app_settings = SagemakerUserProfileUserSettingsRSessionAppSettings(**r_session_app_settings)
        if isinstance(sharing_settings, dict):
            sharing_settings = SagemakerUserProfileUserSettingsSharingSettings(**sharing_settings)
        if isinstance(tensor_board_app_settings, dict):
            tensor_board_app_settings = SagemakerUserProfileUserSettingsTensorBoardAppSettings(**tensor_board_app_settings)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__306f063596160d1b52135ff7326478b4dcbf6bbe28cf5f64751f4aa83fe1d572)
            check_type(argname="argument execution_role", value=execution_role, expected_type=type_hints["execution_role"])
            check_type(argname="argument canvas_app_settings", value=canvas_app_settings, expected_type=type_hints["canvas_app_settings"])
            check_type(argname="argument jupyter_server_app_settings", value=jupyter_server_app_settings, expected_type=type_hints["jupyter_server_app_settings"])
            check_type(argname="argument kernel_gateway_app_settings", value=kernel_gateway_app_settings, expected_type=type_hints["kernel_gateway_app_settings"])
            check_type(argname="argument r_session_app_settings", value=r_session_app_settings, expected_type=type_hints["r_session_app_settings"])
            check_type(argname="argument security_groups", value=security_groups, expected_type=type_hints["security_groups"])
            check_type(argname="argument sharing_settings", value=sharing_settings, expected_type=type_hints["sharing_settings"])
            check_type(argname="argument tensor_board_app_settings", value=tensor_board_app_settings, expected_type=type_hints["tensor_board_app_settings"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "execution_role": execution_role,
        }
        if canvas_app_settings is not None:
            self._values["canvas_app_settings"] = canvas_app_settings
        if jupyter_server_app_settings is not None:
            self._values["jupyter_server_app_settings"] = jupyter_server_app_settings
        if kernel_gateway_app_settings is not None:
            self._values["kernel_gateway_app_settings"] = kernel_gateway_app_settings
        if r_session_app_settings is not None:
            self._values["r_session_app_settings"] = r_session_app_settings
        if security_groups is not None:
            self._values["security_groups"] = security_groups
        if sharing_settings is not None:
            self._values["sharing_settings"] = sharing_settings
        if tensor_board_app_settings is not None:
            self._values["tensor_board_app_settings"] = tensor_board_app_settings

    @builtins.property
    def execution_role(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#execution_role SagemakerUserProfile#execution_role}.'''
        result = self._values.get("execution_role")
        assert result is not None, "Required property 'execution_role' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def canvas_app_settings(
        self,
    ) -> typing.Optional["SagemakerUserProfileUserSettingsCanvasAppSettings"]:
        '''canvas_app_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#canvas_app_settings SagemakerUserProfile#canvas_app_settings}
        '''
        result = self._values.get("canvas_app_settings")
        return typing.cast(typing.Optional["SagemakerUserProfileUserSettingsCanvasAppSettings"], result)

    @builtins.property
    def jupyter_server_app_settings(
        self,
    ) -> typing.Optional["SagemakerUserProfileUserSettingsJupyterServerAppSettings"]:
        '''jupyter_server_app_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#jupyter_server_app_settings SagemakerUserProfile#jupyter_server_app_settings}
        '''
        result = self._values.get("jupyter_server_app_settings")
        return typing.cast(typing.Optional["SagemakerUserProfileUserSettingsJupyterServerAppSettings"], result)

    @builtins.property
    def kernel_gateway_app_settings(
        self,
    ) -> typing.Optional["SagemakerUserProfileUserSettingsKernelGatewayAppSettings"]:
        '''kernel_gateway_app_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#kernel_gateway_app_settings SagemakerUserProfile#kernel_gateway_app_settings}
        '''
        result = self._values.get("kernel_gateway_app_settings")
        return typing.cast(typing.Optional["SagemakerUserProfileUserSettingsKernelGatewayAppSettings"], result)

    @builtins.property
    def r_session_app_settings(
        self,
    ) -> typing.Optional["SagemakerUserProfileUserSettingsRSessionAppSettings"]:
        '''r_session_app_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#r_session_app_settings SagemakerUserProfile#r_session_app_settings}
        '''
        result = self._values.get("r_session_app_settings")
        return typing.cast(typing.Optional["SagemakerUserProfileUserSettingsRSessionAppSettings"], result)

    @builtins.property
    def security_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#security_groups SagemakerUserProfile#security_groups}.'''
        result = self._values.get("security_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def sharing_settings(
        self,
    ) -> typing.Optional["SagemakerUserProfileUserSettingsSharingSettings"]:
        '''sharing_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#sharing_settings SagemakerUserProfile#sharing_settings}
        '''
        result = self._values.get("sharing_settings")
        return typing.cast(typing.Optional["SagemakerUserProfileUserSettingsSharingSettings"], result)

    @builtins.property
    def tensor_board_app_settings(
        self,
    ) -> typing.Optional["SagemakerUserProfileUserSettingsTensorBoardAppSettings"]:
        '''tensor_board_app_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#tensor_board_app_settings SagemakerUserProfile#tensor_board_app_settings}
        '''
        result = self._values.get("tensor_board_app_settings")
        return typing.cast(typing.Optional["SagemakerUserProfileUserSettingsTensorBoardAppSettings"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerUserProfileUserSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.sagemakerUserProfile.SagemakerUserProfileUserSettingsCanvasAppSettings",
    jsii_struct_bases=[],
    name_mapping={"time_series_forecasting_settings": "timeSeriesForecastingSettings"},
)
class SagemakerUserProfileUserSettingsCanvasAppSettings:
    def __init__(
        self,
        *,
        time_series_forecasting_settings: typing.Optional[typing.Union["SagemakerUserProfileUserSettingsCanvasAppSettingsTimeSeriesForecastingSettings", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param time_series_forecasting_settings: time_series_forecasting_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#time_series_forecasting_settings SagemakerUserProfile#time_series_forecasting_settings}
        '''
        if isinstance(time_series_forecasting_settings, dict):
            time_series_forecasting_settings = SagemakerUserProfileUserSettingsCanvasAppSettingsTimeSeriesForecastingSettings(**time_series_forecasting_settings)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__16d09b2bc3f03a9bad901b1527d6ad9c7de8c5f2c8308c536adb5d4fa855deea)
            check_type(argname="argument time_series_forecasting_settings", value=time_series_forecasting_settings, expected_type=type_hints["time_series_forecasting_settings"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if time_series_forecasting_settings is not None:
            self._values["time_series_forecasting_settings"] = time_series_forecasting_settings

    @builtins.property
    def time_series_forecasting_settings(
        self,
    ) -> typing.Optional["SagemakerUserProfileUserSettingsCanvasAppSettingsTimeSeriesForecastingSettings"]:
        '''time_series_forecasting_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#time_series_forecasting_settings SagemakerUserProfile#time_series_forecasting_settings}
        '''
        result = self._values.get("time_series_forecasting_settings")
        return typing.cast(typing.Optional["SagemakerUserProfileUserSettingsCanvasAppSettingsTimeSeriesForecastingSettings"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerUserProfileUserSettingsCanvasAppSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerUserProfileUserSettingsCanvasAppSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerUserProfile.SagemakerUserProfileUserSettingsCanvasAppSettingsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__69a4b6ffa730b8ca119734580eae653bc5bcd3d9d1b1ec694fdbef1c25069405)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putTimeSeriesForecastingSettings")
    def put_time_series_forecasting_settings(
        self,
        *,
        amazon_forecast_role_arn: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param amazon_forecast_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#amazon_forecast_role_arn SagemakerUserProfile#amazon_forecast_role_arn}.
        :param status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#status SagemakerUserProfile#status}.
        '''
        value = SagemakerUserProfileUserSettingsCanvasAppSettingsTimeSeriesForecastingSettings(
            amazon_forecast_role_arn=amazon_forecast_role_arn, status=status
        )

        return typing.cast(None, jsii.invoke(self, "putTimeSeriesForecastingSettings", [value]))

    @jsii.member(jsii_name="resetTimeSeriesForecastingSettings")
    def reset_time_series_forecasting_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeSeriesForecastingSettings", []))

    @builtins.property
    @jsii.member(jsii_name="timeSeriesForecastingSettings")
    def time_series_forecasting_settings(
        self,
    ) -> "SagemakerUserProfileUserSettingsCanvasAppSettingsTimeSeriesForecastingSettingsOutputReference":
        return typing.cast("SagemakerUserProfileUserSettingsCanvasAppSettingsTimeSeriesForecastingSettingsOutputReference", jsii.get(self, "timeSeriesForecastingSettings"))

    @builtins.property
    @jsii.member(jsii_name="timeSeriesForecastingSettingsInput")
    def time_series_forecasting_settings_input(
        self,
    ) -> typing.Optional["SagemakerUserProfileUserSettingsCanvasAppSettingsTimeSeriesForecastingSettings"]:
        return typing.cast(typing.Optional["SagemakerUserProfileUserSettingsCanvasAppSettingsTimeSeriesForecastingSettings"], jsii.get(self, "timeSeriesForecastingSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerUserProfileUserSettingsCanvasAppSettings]:
        return typing.cast(typing.Optional[SagemakerUserProfileUserSettingsCanvasAppSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerUserProfileUserSettingsCanvasAppSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61c5a6523896991c5be0a0e4b84781da8513bc369ac8fe9c47e0beed006d6544)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.sagemakerUserProfile.SagemakerUserProfileUserSettingsCanvasAppSettingsTimeSeriesForecastingSettings",
    jsii_struct_bases=[],
    name_mapping={
        "amazon_forecast_role_arn": "amazonForecastRoleArn",
        "status": "status",
    },
)
class SagemakerUserProfileUserSettingsCanvasAppSettingsTimeSeriesForecastingSettings:
    def __init__(
        self,
        *,
        amazon_forecast_role_arn: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param amazon_forecast_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#amazon_forecast_role_arn SagemakerUserProfile#amazon_forecast_role_arn}.
        :param status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#status SagemakerUserProfile#status}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__112770e3f4de92edb14572763999d4b0fa2adef5718365d58c265d3c39763f13)
            check_type(argname="argument amazon_forecast_role_arn", value=amazon_forecast_role_arn, expected_type=type_hints["amazon_forecast_role_arn"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if amazon_forecast_role_arn is not None:
            self._values["amazon_forecast_role_arn"] = amazon_forecast_role_arn
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def amazon_forecast_role_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#amazon_forecast_role_arn SagemakerUserProfile#amazon_forecast_role_arn}.'''
        result = self._values.get("amazon_forecast_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#status SagemakerUserProfile#status}.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerUserProfileUserSettingsCanvasAppSettingsTimeSeriesForecastingSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerUserProfileUserSettingsCanvasAppSettingsTimeSeriesForecastingSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerUserProfile.SagemakerUserProfileUserSettingsCanvasAppSettingsTimeSeriesForecastingSettingsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2c2afc809c01888df468e9803ecd1497355c28776f2bc7d23470f32758588804)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAmazonForecastRoleArn")
    def reset_amazon_forecast_role_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAmazonForecastRoleArn", []))

    @jsii.member(jsii_name="resetStatus")
    def reset_status(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatus", []))

    @builtins.property
    @jsii.member(jsii_name="amazonForecastRoleArnInput")
    def amazon_forecast_role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "amazonForecastRoleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="statusInput")
    def status_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statusInput"))

    @builtins.property
    @jsii.member(jsii_name="amazonForecastRoleArn")
    def amazon_forecast_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "amazonForecastRoleArn"))

    @amazon_forecast_role_arn.setter
    def amazon_forecast_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40598666bdd057a11549bf592d1408ed5b297533b83a58ba9ae3cb2ae4ef0499)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "amazonForecastRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @status.setter
    def status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__204389a718c4f7ac1e7e645058c4802816deb176e3d667ba5a4256ac40c4b6fb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerUserProfileUserSettingsCanvasAppSettingsTimeSeriesForecastingSettings]:
        return typing.cast(typing.Optional[SagemakerUserProfileUserSettingsCanvasAppSettingsTimeSeriesForecastingSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerUserProfileUserSettingsCanvasAppSettingsTimeSeriesForecastingSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27b47a6cf1716cdeea9d008b4eff25700650bb104504cafdb46c90886ae93321)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.sagemakerUserProfile.SagemakerUserProfileUserSettingsJupyterServerAppSettings",
    jsii_struct_bases=[],
    name_mapping={
        "default_resource_spec": "defaultResourceSpec",
        "code_repository": "codeRepository",
        "lifecycle_config_arns": "lifecycleConfigArns",
    },
)
class SagemakerUserProfileUserSettingsJupyterServerAppSettings:
    def __init__(
        self,
        *,
        default_resource_spec: typing.Union["SagemakerUserProfileUserSettingsJupyterServerAppSettingsDefaultResourceSpec", typing.Dict[builtins.str, typing.Any]],
        code_repository: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SagemakerUserProfileUserSettingsJupyterServerAppSettingsCodeRepository", typing.Dict[builtins.str, typing.Any]]]]] = None,
        lifecycle_config_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param default_resource_spec: default_resource_spec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#default_resource_spec SagemakerUserProfile#default_resource_spec}
        :param code_repository: code_repository block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#code_repository SagemakerUserProfile#code_repository}
        :param lifecycle_config_arns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#lifecycle_config_arns SagemakerUserProfile#lifecycle_config_arns}.
        '''
        if isinstance(default_resource_spec, dict):
            default_resource_spec = SagemakerUserProfileUserSettingsJupyterServerAppSettingsDefaultResourceSpec(**default_resource_spec)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04fcf7b5687bdfe532a8a064fca0e6906d3e302cfed15dee44db46ff212fa6f4)
            check_type(argname="argument default_resource_spec", value=default_resource_spec, expected_type=type_hints["default_resource_spec"])
            check_type(argname="argument code_repository", value=code_repository, expected_type=type_hints["code_repository"])
            check_type(argname="argument lifecycle_config_arns", value=lifecycle_config_arns, expected_type=type_hints["lifecycle_config_arns"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "default_resource_spec": default_resource_spec,
        }
        if code_repository is not None:
            self._values["code_repository"] = code_repository
        if lifecycle_config_arns is not None:
            self._values["lifecycle_config_arns"] = lifecycle_config_arns

    @builtins.property
    def default_resource_spec(
        self,
    ) -> "SagemakerUserProfileUserSettingsJupyterServerAppSettingsDefaultResourceSpec":
        '''default_resource_spec block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#default_resource_spec SagemakerUserProfile#default_resource_spec}
        '''
        result = self._values.get("default_resource_spec")
        assert result is not None, "Required property 'default_resource_spec' is missing"
        return typing.cast("SagemakerUserProfileUserSettingsJupyterServerAppSettingsDefaultResourceSpec", result)

    @builtins.property
    def code_repository(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SagemakerUserProfileUserSettingsJupyterServerAppSettingsCodeRepository"]]]:
        '''code_repository block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#code_repository SagemakerUserProfile#code_repository}
        '''
        result = self._values.get("code_repository")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SagemakerUserProfileUserSettingsJupyterServerAppSettingsCodeRepository"]]], result)

    @builtins.property
    def lifecycle_config_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#lifecycle_config_arns SagemakerUserProfile#lifecycle_config_arns}.'''
        result = self._values.get("lifecycle_config_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerUserProfileUserSettingsJupyterServerAppSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.sagemakerUserProfile.SagemakerUserProfileUserSettingsJupyterServerAppSettingsCodeRepository",
    jsii_struct_bases=[],
    name_mapping={"repository_url": "repositoryUrl"},
)
class SagemakerUserProfileUserSettingsJupyterServerAppSettingsCodeRepository:
    def __init__(self, *, repository_url: builtins.str) -> None:
        '''
        :param repository_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#repository_url SagemakerUserProfile#repository_url}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15aec08afdb643490a5d3adc86ab690923bd8dc5d0de509a0b506f908b28fb89)
            check_type(argname="argument repository_url", value=repository_url, expected_type=type_hints["repository_url"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "repository_url": repository_url,
        }

    @builtins.property
    def repository_url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#repository_url SagemakerUserProfile#repository_url}.'''
        result = self._values.get("repository_url")
        assert result is not None, "Required property 'repository_url' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerUserProfileUserSettingsJupyterServerAppSettingsCodeRepository(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerUserProfileUserSettingsJupyterServerAppSettingsCodeRepositoryList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerUserProfile.SagemakerUserProfileUserSettingsJupyterServerAppSettingsCodeRepositoryList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4e563758f5d09b0484f056aa2aff747b21211ce1a200cc5bcdbdd2c98ad8be65)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "SagemakerUserProfileUserSettingsJupyterServerAppSettingsCodeRepositoryOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50572d71de37e8c322cffc1d33aab92b6122442738db0cf94971f4248b0395f4)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SagemakerUserProfileUserSettingsJupyterServerAppSettingsCodeRepositoryOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d5db4b5512e74fabf118e17f8622cad42ec8a8868a1c1fade0700e565379894)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8abeeb7863c8daa380a0cbc92b08d561a2bfe6a71a1ae42e758871fea10dae87)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a3762feedcb5e283dcdf784ebdf5ea19ea35c6ea3f36dba40edd7e1d9ae35f79)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerUserProfileUserSettingsJupyterServerAppSettingsCodeRepository]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerUserProfileUserSettingsJupyterServerAppSettingsCodeRepository]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerUserProfileUserSettingsJupyterServerAppSettingsCodeRepository]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3765f96c603f6488b0d4db0431f4f97daef18f61995843bdd7b2763a4264df18)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SagemakerUserProfileUserSettingsJupyterServerAppSettingsCodeRepositoryOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerUserProfile.SagemakerUserProfileUserSettingsJupyterServerAppSettingsCodeRepositoryOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a0ed1b206c66fad8eb894d47c58536113e883392cf6b0668926577b3cce06037)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="repositoryUrlInput")
    def repository_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "repositoryUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="repositoryUrl")
    def repository_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "repositoryUrl"))

    @repository_url.setter
    def repository_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4868df7444601ccf15262cb7e4d14ac3099e912ce6bc8e71727c06960de7650f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repositoryUrl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SagemakerUserProfileUserSettingsJupyterServerAppSettingsCodeRepository, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SagemakerUserProfileUserSettingsJupyterServerAppSettingsCodeRepository, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SagemakerUserProfileUserSettingsJupyterServerAppSettingsCodeRepository, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd287730ad069041a0dd48aac409169763267bcb4f57f4bae41adf69a1a8ab3e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.sagemakerUserProfile.SagemakerUserProfileUserSettingsJupyterServerAppSettingsDefaultResourceSpec",
    jsii_struct_bases=[],
    name_mapping={
        "instance_type": "instanceType",
        "lifecycle_config_arn": "lifecycleConfigArn",
        "sagemaker_image_arn": "sagemakerImageArn",
        "sagemaker_image_version_arn": "sagemakerImageVersionArn",
    },
)
class SagemakerUserProfileUserSettingsJupyterServerAppSettingsDefaultResourceSpec:
    def __init__(
        self,
        *,
        instance_type: typing.Optional[builtins.str] = None,
        lifecycle_config_arn: typing.Optional[builtins.str] = None,
        sagemaker_image_arn: typing.Optional[builtins.str] = None,
        sagemaker_image_version_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param instance_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#instance_type SagemakerUserProfile#instance_type}.
        :param lifecycle_config_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#lifecycle_config_arn SagemakerUserProfile#lifecycle_config_arn}.
        :param sagemaker_image_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#sagemaker_image_arn SagemakerUserProfile#sagemaker_image_arn}.
        :param sagemaker_image_version_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#sagemaker_image_version_arn SagemakerUserProfile#sagemaker_image_version_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac8c7168539cae31994e1528bc892d22833a459587905ec742bab1c1e5fc310f)
            check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
            check_type(argname="argument lifecycle_config_arn", value=lifecycle_config_arn, expected_type=type_hints["lifecycle_config_arn"])
            check_type(argname="argument sagemaker_image_arn", value=sagemaker_image_arn, expected_type=type_hints["sagemaker_image_arn"])
            check_type(argname="argument sagemaker_image_version_arn", value=sagemaker_image_version_arn, expected_type=type_hints["sagemaker_image_version_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if instance_type is not None:
            self._values["instance_type"] = instance_type
        if lifecycle_config_arn is not None:
            self._values["lifecycle_config_arn"] = lifecycle_config_arn
        if sagemaker_image_arn is not None:
            self._values["sagemaker_image_arn"] = sagemaker_image_arn
        if sagemaker_image_version_arn is not None:
            self._values["sagemaker_image_version_arn"] = sagemaker_image_version_arn

    @builtins.property
    def instance_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#instance_type SagemakerUserProfile#instance_type}.'''
        result = self._values.get("instance_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lifecycle_config_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#lifecycle_config_arn SagemakerUserProfile#lifecycle_config_arn}.'''
        result = self._values.get("lifecycle_config_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sagemaker_image_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#sagemaker_image_arn SagemakerUserProfile#sagemaker_image_arn}.'''
        result = self._values.get("sagemaker_image_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sagemaker_image_version_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#sagemaker_image_version_arn SagemakerUserProfile#sagemaker_image_version_arn}.'''
        result = self._values.get("sagemaker_image_version_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerUserProfileUserSettingsJupyterServerAppSettingsDefaultResourceSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerUserProfileUserSettingsJupyterServerAppSettingsDefaultResourceSpecOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerUserProfile.SagemakerUserProfileUserSettingsJupyterServerAppSettingsDefaultResourceSpecOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__68dac719f8098a672cc6b80891627ef3dff4548679a64a83218934fc3a70fba7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetInstanceType")
    def reset_instance_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceType", []))

    @jsii.member(jsii_name="resetLifecycleConfigArn")
    def reset_lifecycle_config_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLifecycleConfigArn", []))

    @jsii.member(jsii_name="resetSagemakerImageArn")
    def reset_sagemaker_image_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSagemakerImageArn", []))

    @jsii.member(jsii_name="resetSagemakerImageVersionArn")
    def reset_sagemaker_image_version_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSagemakerImageVersionArn", []))

    @builtins.property
    @jsii.member(jsii_name="instanceTypeInput")
    def instance_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="lifecycleConfigArnInput")
    def lifecycle_config_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lifecycleConfigArnInput"))

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageArnInput")
    def sagemaker_image_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sagemakerImageArnInput"))

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageVersionArnInput")
    def sagemaker_image_version_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sagemakerImageVersionArnInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceType")
    def instance_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceType"))

    @instance_type.setter
    def instance_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73cd5601cc3bfa904b5eb21412967989f8df794170a6c0825ec32e1ffa93803d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceType", value)

    @builtins.property
    @jsii.member(jsii_name="lifecycleConfigArn")
    def lifecycle_config_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lifecycleConfigArn"))

    @lifecycle_config_arn.setter
    def lifecycle_config_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ecf9d2adf8f81491458127074fdde5edb2ba300f4f9cbc22a95af3bd6e9a140)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lifecycleConfigArn", value)

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageArn")
    def sagemaker_image_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sagemakerImageArn"))

    @sagemaker_image_arn.setter
    def sagemaker_image_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f51d1563515d70f94344fee03b301fd5f312efbacedf4f76a340a86296e19ee8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sagemakerImageArn", value)

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageVersionArn")
    def sagemaker_image_version_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sagemakerImageVersionArn"))

    @sagemaker_image_version_arn.setter
    def sagemaker_image_version_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e8af36d100fa85c26642e6a743b2b0359b9490bf451b1310ee7c615e8e0153d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sagemakerImageVersionArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerUserProfileUserSettingsJupyterServerAppSettingsDefaultResourceSpec]:
        return typing.cast(typing.Optional[SagemakerUserProfileUserSettingsJupyterServerAppSettingsDefaultResourceSpec], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerUserProfileUserSettingsJupyterServerAppSettingsDefaultResourceSpec],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d586dc6ebbc9f8d5ccd4e59a54ca60d2f90fedfc1d934f0f97d868cdf0af5c7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SagemakerUserProfileUserSettingsJupyterServerAppSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerUserProfile.SagemakerUserProfileUserSettingsJupyterServerAppSettingsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__937ac3e1ba3ddb39ec99f6d4e92effa287defcb0f00b92153c64f9ac3dd4a61f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCodeRepository")
    def put_code_repository(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerUserProfileUserSettingsJupyterServerAppSettingsCodeRepository, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd69df47f582fc37a000b8188395c7f18b35d88eb0b60c7522ef9c2b9e02e406)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCodeRepository", [value]))

    @jsii.member(jsii_name="putDefaultResourceSpec")
    def put_default_resource_spec(
        self,
        *,
        instance_type: typing.Optional[builtins.str] = None,
        lifecycle_config_arn: typing.Optional[builtins.str] = None,
        sagemaker_image_arn: typing.Optional[builtins.str] = None,
        sagemaker_image_version_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param instance_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#instance_type SagemakerUserProfile#instance_type}.
        :param lifecycle_config_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#lifecycle_config_arn SagemakerUserProfile#lifecycle_config_arn}.
        :param sagemaker_image_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#sagemaker_image_arn SagemakerUserProfile#sagemaker_image_arn}.
        :param sagemaker_image_version_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#sagemaker_image_version_arn SagemakerUserProfile#sagemaker_image_version_arn}.
        '''
        value = SagemakerUserProfileUserSettingsJupyterServerAppSettingsDefaultResourceSpec(
            instance_type=instance_type,
            lifecycle_config_arn=lifecycle_config_arn,
            sagemaker_image_arn=sagemaker_image_arn,
            sagemaker_image_version_arn=sagemaker_image_version_arn,
        )

        return typing.cast(None, jsii.invoke(self, "putDefaultResourceSpec", [value]))

    @jsii.member(jsii_name="resetCodeRepository")
    def reset_code_repository(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCodeRepository", []))

    @jsii.member(jsii_name="resetLifecycleConfigArns")
    def reset_lifecycle_config_arns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLifecycleConfigArns", []))

    @builtins.property
    @jsii.member(jsii_name="codeRepository")
    def code_repository(
        self,
    ) -> SagemakerUserProfileUserSettingsJupyterServerAppSettingsCodeRepositoryList:
        return typing.cast(SagemakerUserProfileUserSettingsJupyterServerAppSettingsCodeRepositoryList, jsii.get(self, "codeRepository"))

    @builtins.property
    @jsii.member(jsii_name="defaultResourceSpec")
    def default_resource_spec(
        self,
    ) -> SagemakerUserProfileUserSettingsJupyterServerAppSettingsDefaultResourceSpecOutputReference:
        return typing.cast(SagemakerUserProfileUserSettingsJupyterServerAppSettingsDefaultResourceSpecOutputReference, jsii.get(self, "defaultResourceSpec"))

    @builtins.property
    @jsii.member(jsii_name="codeRepositoryInput")
    def code_repository_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerUserProfileUserSettingsJupyterServerAppSettingsCodeRepository]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerUserProfileUserSettingsJupyterServerAppSettingsCodeRepository]]], jsii.get(self, "codeRepositoryInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultResourceSpecInput")
    def default_resource_spec_input(
        self,
    ) -> typing.Optional[SagemakerUserProfileUserSettingsJupyterServerAppSettingsDefaultResourceSpec]:
        return typing.cast(typing.Optional[SagemakerUserProfileUserSettingsJupyterServerAppSettingsDefaultResourceSpec], jsii.get(self, "defaultResourceSpecInput"))

    @builtins.property
    @jsii.member(jsii_name="lifecycleConfigArnsInput")
    def lifecycle_config_arns_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "lifecycleConfigArnsInput"))

    @builtins.property
    @jsii.member(jsii_name="lifecycleConfigArns")
    def lifecycle_config_arns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "lifecycleConfigArns"))

    @lifecycle_config_arns.setter
    def lifecycle_config_arns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c25c999871628efd294de82ea81ccea9abecce9d907f6b5369abbe21b97dae4e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lifecycleConfigArns", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerUserProfileUserSettingsJupyterServerAppSettings]:
        return typing.cast(typing.Optional[SagemakerUserProfileUserSettingsJupyterServerAppSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerUserProfileUserSettingsJupyterServerAppSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97a3aa76918f1ed3df7a15dc17d04538f5bbbcfb2acbce0e0253eac72158ff3b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.sagemakerUserProfile.SagemakerUserProfileUserSettingsKernelGatewayAppSettings",
    jsii_struct_bases=[],
    name_mapping={
        "default_resource_spec": "defaultResourceSpec",
        "custom_image": "customImage",
        "lifecycle_config_arns": "lifecycleConfigArns",
    },
)
class SagemakerUserProfileUserSettingsKernelGatewayAppSettings:
    def __init__(
        self,
        *,
        default_resource_spec: typing.Union["SagemakerUserProfileUserSettingsKernelGatewayAppSettingsDefaultResourceSpec", typing.Dict[builtins.str, typing.Any]],
        custom_image: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SagemakerUserProfileUserSettingsKernelGatewayAppSettingsCustomImage", typing.Dict[builtins.str, typing.Any]]]]] = None,
        lifecycle_config_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param default_resource_spec: default_resource_spec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#default_resource_spec SagemakerUserProfile#default_resource_spec}
        :param custom_image: custom_image block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#custom_image SagemakerUserProfile#custom_image}
        :param lifecycle_config_arns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#lifecycle_config_arns SagemakerUserProfile#lifecycle_config_arns}.
        '''
        if isinstance(default_resource_spec, dict):
            default_resource_spec = SagemakerUserProfileUserSettingsKernelGatewayAppSettingsDefaultResourceSpec(**default_resource_spec)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__346ca577f5fb3b958a7dab690897b6d3acb033cf8d0048b0827f793fa8bcb47d)
            check_type(argname="argument default_resource_spec", value=default_resource_spec, expected_type=type_hints["default_resource_spec"])
            check_type(argname="argument custom_image", value=custom_image, expected_type=type_hints["custom_image"])
            check_type(argname="argument lifecycle_config_arns", value=lifecycle_config_arns, expected_type=type_hints["lifecycle_config_arns"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "default_resource_spec": default_resource_spec,
        }
        if custom_image is not None:
            self._values["custom_image"] = custom_image
        if lifecycle_config_arns is not None:
            self._values["lifecycle_config_arns"] = lifecycle_config_arns

    @builtins.property
    def default_resource_spec(
        self,
    ) -> "SagemakerUserProfileUserSettingsKernelGatewayAppSettingsDefaultResourceSpec":
        '''default_resource_spec block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#default_resource_spec SagemakerUserProfile#default_resource_spec}
        '''
        result = self._values.get("default_resource_spec")
        assert result is not None, "Required property 'default_resource_spec' is missing"
        return typing.cast("SagemakerUserProfileUserSettingsKernelGatewayAppSettingsDefaultResourceSpec", result)

    @builtins.property
    def custom_image(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SagemakerUserProfileUserSettingsKernelGatewayAppSettingsCustomImage"]]]:
        '''custom_image block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#custom_image SagemakerUserProfile#custom_image}
        '''
        result = self._values.get("custom_image")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SagemakerUserProfileUserSettingsKernelGatewayAppSettingsCustomImage"]]], result)

    @builtins.property
    def lifecycle_config_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#lifecycle_config_arns SagemakerUserProfile#lifecycle_config_arns}.'''
        result = self._values.get("lifecycle_config_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerUserProfileUserSettingsKernelGatewayAppSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.sagemakerUserProfile.SagemakerUserProfileUserSettingsKernelGatewayAppSettingsCustomImage",
    jsii_struct_bases=[],
    name_mapping={
        "app_image_config_name": "appImageConfigName",
        "image_name": "imageName",
        "image_version_number": "imageVersionNumber",
    },
)
class SagemakerUserProfileUserSettingsKernelGatewayAppSettingsCustomImage:
    def __init__(
        self,
        *,
        app_image_config_name: builtins.str,
        image_name: builtins.str,
        image_version_number: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param app_image_config_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#app_image_config_name SagemakerUserProfile#app_image_config_name}.
        :param image_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#image_name SagemakerUserProfile#image_name}.
        :param image_version_number: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#image_version_number SagemakerUserProfile#image_version_number}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba94295c8afeace5e45e4c2d3d849316f40dca1c9eb2d77492b8867bda645ffe)
            check_type(argname="argument app_image_config_name", value=app_image_config_name, expected_type=type_hints["app_image_config_name"])
            check_type(argname="argument image_name", value=image_name, expected_type=type_hints["image_name"])
            check_type(argname="argument image_version_number", value=image_version_number, expected_type=type_hints["image_version_number"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "app_image_config_name": app_image_config_name,
            "image_name": image_name,
        }
        if image_version_number is not None:
            self._values["image_version_number"] = image_version_number

    @builtins.property
    def app_image_config_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#app_image_config_name SagemakerUserProfile#app_image_config_name}.'''
        result = self._values.get("app_image_config_name")
        assert result is not None, "Required property 'app_image_config_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def image_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#image_name SagemakerUserProfile#image_name}.'''
        result = self._values.get("image_name")
        assert result is not None, "Required property 'image_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def image_version_number(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#image_version_number SagemakerUserProfile#image_version_number}.'''
        result = self._values.get("image_version_number")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerUserProfileUserSettingsKernelGatewayAppSettingsCustomImage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerUserProfileUserSettingsKernelGatewayAppSettingsCustomImageList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerUserProfile.SagemakerUserProfileUserSettingsKernelGatewayAppSettingsCustomImageList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__228bd0b6b9395c15ebef4731ef962febf92fd3b733e56ddbe5f5635cda9f01a6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "SagemakerUserProfileUserSettingsKernelGatewayAppSettingsCustomImageOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7e9b85453f6a196c20084557ee9df6c7cee619be469a28e5b306673af411b4f)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SagemakerUserProfileUserSettingsKernelGatewayAppSettingsCustomImageOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b679d9e84d10515c04235088890fcebec58300182b1a8ca1a4f2db34568cfe4d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7ba1f5730df4755f3cc699d03670b2229818fdf82874dc35dd8370a6722c609a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b31a07c3e335505cea00bcd36ae163b07e4a93a5920c3c2dad072ca6cddd92bf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerUserProfileUserSettingsKernelGatewayAppSettingsCustomImage]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerUserProfileUserSettingsKernelGatewayAppSettingsCustomImage]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerUserProfileUserSettingsKernelGatewayAppSettingsCustomImage]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bbdee080a48812a455fa0a2e374026b7e3a3a2e7234ff71069d372c1038a6fc1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SagemakerUserProfileUserSettingsKernelGatewayAppSettingsCustomImageOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerUserProfile.SagemakerUserProfileUserSettingsKernelGatewayAppSettingsCustomImageOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__76c1bdf133aeeeb394b3d611947334076b4f0a513468d39c52904d8b8ad7c206)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetImageVersionNumber")
    def reset_image_version_number(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImageVersionNumber", []))

    @builtins.property
    @jsii.member(jsii_name="appImageConfigNameInput")
    def app_image_config_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "appImageConfigNameInput"))

    @builtins.property
    @jsii.member(jsii_name="imageNameInput")
    def image_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageNameInput"))

    @builtins.property
    @jsii.member(jsii_name="imageVersionNumberInput")
    def image_version_number_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "imageVersionNumberInput"))

    @builtins.property
    @jsii.member(jsii_name="appImageConfigName")
    def app_image_config_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "appImageConfigName"))

    @app_image_config_name.setter
    def app_image_config_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c61cb794f464815dc32f5a220de2fa3639d240bcf995e32a7ec2974b94eac099)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appImageConfigName", value)

    @builtins.property
    @jsii.member(jsii_name="imageName")
    def image_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "imageName"))

    @image_name.setter
    def image_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__122c997d837e6d10228c7c702850da9aa90adfff33ea464b9329f85098961865)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageName", value)

    @builtins.property
    @jsii.member(jsii_name="imageVersionNumber")
    def image_version_number(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "imageVersionNumber"))

    @image_version_number.setter
    def image_version_number(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc83a303d6e65c230c693e4d000970fff4420d960a9d3e6ef429237f85dc6bcb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageVersionNumber", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SagemakerUserProfileUserSettingsKernelGatewayAppSettingsCustomImage, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SagemakerUserProfileUserSettingsKernelGatewayAppSettingsCustomImage, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SagemakerUserProfileUserSettingsKernelGatewayAppSettingsCustomImage, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__efd715ac7ef21d63421454edd6ef3a4bb811badf05d5889a7406433485bbd4c4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.sagemakerUserProfile.SagemakerUserProfileUserSettingsKernelGatewayAppSettingsDefaultResourceSpec",
    jsii_struct_bases=[],
    name_mapping={
        "instance_type": "instanceType",
        "lifecycle_config_arn": "lifecycleConfigArn",
        "sagemaker_image_arn": "sagemakerImageArn",
        "sagemaker_image_version_arn": "sagemakerImageVersionArn",
    },
)
class SagemakerUserProfileUserSettingsKernelGatewayAppSettingsDefaultResourceSpec:
    def __init__(
        self,
        *,
        instance_type: typing.Optional[builtins.str] = None,
        lifecycle_config_arn: typing.Optional[builtins.str] = None,
        sagemaker_image_arn: typing.Optional[builtins.str] = None,
        sagemaker_image_version_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param instance_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#instance_type SagemakerUserProfile#instance_type}.
        :param lifecycle_config_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#lifecycle_config_arn SagemakerUserProfile#lifecycle_config_arn}.
        :param sagemaker_image_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#sagemaker_image_arn SagemakerUserProfile#sagemaker_image_arn}.
        :param sagemaker_image_version_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#sagemaker_image_version_arn SagemakerUserProfile#sagemaker_image_version_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5cf658faaa3c5ae2b7c61a5944ea284c77b49a322ae658dfe40d2803e93a0fc1)
            check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
            check_type(argname="argument lifecycle_config_arn", value=lifecycle_config_arn, expected_type=type_hints["lifecycle_config_arn"])
            check_type(argname="argument sagemaker_image_arn", value=sagemaker_image_arn, expected_type=type_hints["sagemaker_image_arn"])
            check_type(argname="argument sagemaker_image_version_arn", value=sagemaker_image_version_arn, expected_type=type_hints["sagemaker_image_version_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if instance_type is not None:
            self._values["instance_type"] = instance_type
        if lifecycle_config_arn is not None:
            self._values["lifecycle_config_arn"] = lifecycle_config_arn
        if sagemaker_image_arn is not None:
            self._values["sagemaker_image_arn"] = sagemaker_image_arn
        if sagemaker_image_version_arn is not None:
            self._values["sagemaker_image_version_arn"] = sagemaker_image_version_arn

    @builtins.property
    def instance_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#instance_type SagemakerUserProfile#instance_type}.'''
        result = self._values.get("instance_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lifecycle_config_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#lifecycle_config_arn SagemakerUserProfile#lifecycle_config_arn}.'''
        result = self._values.get("lifecycle_config_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sagemaker_image_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#sagemaker_image_arn SagemakerUserProfile#sagemaker_image_arn}.'''
        result = self._values.get("sagemaker_image_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sagemaker_image_version_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#sagemaker_image_version_arn SagemakerUserProfile#sagemaker_image_version_arn}.'''
        result = self._values.get("sagemaker_image_version_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerUserProfileUserSettingsKernelGatewayAppSettingsDefaultResourceSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerUserProfileUserSettingsKernelGatewayAppSettingsDefaultResourceSpecOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerUserProfile.SagemakerUserProfileUserSettingsKernelGatewayAppSettingsDefaultResourceSpecOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4362b8fa84107e5028acee923367b89350434eefebdbfb972ffdc27ee3068a96)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetInstanceType")
    def reset_instance_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceType", []))

    @jsii.member(jsii_name="resetLifecycleConfigArn")
    def reset_lifecycle_config_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLifecycleConfigArn", []))

    @jsii.member(jsii_name="resetSagemakerImageArn")
    def reset_sagemaker_image_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSagemakerImageArn", []))

    @jsii.member(jsii_name="resetSagemakerImageVersionArn")
    def reset_sagemaker_image_version_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSagemakerImageVersionArn", []))

    @builtins.property
    @jsii.member(jsii_name="instanceTypeInput")
    def instance_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="lifecycleConfigArnInput")
    def lifecycle_config_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lifecycleConfigArnInput"))

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageArnInput")
    def sagemaker_image_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sagemakerImageArnInput"))

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageVersionArnInput")
    def sagemaker_image_version_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sagemakerImageVersionArnInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceType")
    def instance_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceType"))

    @instance_type.setter
    def instance_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dff61fd52136fda177c5e3b437998c1ff3b2451051c2d6fe3ca578e89cb85795)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceType", value)

    @builtins.property
    @jsii.member(jsii_name="lifecycleConfigArn")
    def lifecycle_config_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lifecycleConfigArn"))

    @lifecycle_config_arn.setter
    def lifecycle_config_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c18c6ec3ca84fe6a03a764a2335b7be0ad27faf5dd2496b2d6523bf81346379)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lifecycleConfigArn", value)

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageArn")
    def sagemaker_image_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sagemakerImageArn"))

    @sagemaker_image_arn.setter
    def sagemaker_image_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19c4eb45e2d2e3844a5052861ff096742055e8020dddcee3a224096a232eefc4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sagemakerImageArn", value)

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageVersionArn")
    def sagemaker_image_version_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sagemakerImageVersionArn"))

    @sagemaker_image_version_arn.setter
    def sagemaker_image_version_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed53ac962a92899eb98184a2e1c24b979089a6bd461d40d06f1f8d5436d83610)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sagemakerImageVersionArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerUserProfileUserSettingsKernelGatewayAppSettingsDefaultResourceSpec]:
        return typing.cast(typing.Optional[SagemakerUserProfileUserSettingsKernelGatewayAppSettingsDefaultResourceSpec], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerUserProfileUserSettingsKernelGatewayAppSettingsDefaultResourceSpec],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__606e80f16417061c02469c300bfe306250da2d412f246b4c2533feb03c3ca421)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SagemakerUserProfileUserSettingsKernelGatewayAppSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerUserProfile.SagemakerUserProfileUserSettingsKernelGatewayAppSettingsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f94329f77f18be7b5602e4ac1fc47e1edb2f29b208ef663f8c0d88ff0ad231f0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCustomImage")
    def put_custom_image(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerUserProfileUserSettingsKernelGatewayAppSettingsCustomImage, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e765526e93b6120844d2b24b0c782b5788bea2ee156fae755cfd809f4606f339)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCustomImage", [value]))

    @jsii.member(jsii_name="putDefaultResourceSpec")
    def put_default_resource_spec(
        self,
        *,
        instance_type: typing.Optional[builtins.str] = None,
        lifecycle_config_arn: typing.Optional[builtins.str] = None,
        sagemaker_image_arn: typing.Optional[builtins.str] = None,
        sagemaker_image_version_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param instance_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#instance_type SagemakerUserProfile#instance_type}.
        :param lifecycle_config_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#lifecycle_config_arn SagemakerUserProfile#lifecycle_config_arn}.
        :param sagemaker_image_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#sagemaker_image_arn SagemakerUserProfile#sagemaker_image_arn}.
        :param sagemaker_image_version_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#sagemaker_image_version_arn SagemakerUserProfile#sagemaker_image_version_arn}.
        '''
        value = SagemakerUserProfileUserSettingsKernelGatewayAppSettingsDefaultResourceSpec(
            instance_type=instance_type,
            lifecycle_config_arn=lifecycle_config_arn,
            sagemaker_image_arn=sagemaker_image_arn,
            sagemaker_image_version_arn=sagemaker_image_version_arn,
        )

        return typing.cast(None, jsii.invoke(self, "putDefaultResourceSpec", [value]))

    @jsii.member(jsii_name="resetCustomImage")
    def reset_custom_image(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomImage", []))

    @jsii.member(jsii_name="resetLifecycleConfigArns")
    def reset_lifecycle_config_arns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLifecycleConfigArns", []))

    @builtins.property
    @jsii.member(jsii_name="customImage")
    def custom_image(
        self,
    ) -> SagemakerUserProfileUserSettingsKernelGatewayAppSettingsCustomImageList:
        return typing.cast(SagemakerUserProfileUserSettingsKernelGatewayAppSettingsCustomImageList, jsii.get(self, "customImage"))

    @builtins.property
    @jsii.member(jsii_name="defaultResourceSpec")
    def default_resource_spec(
        self,
    ) -> SagemakerUserProfileUserSettingsKernelGatewayAppSettingsDefaultResourceSpecOutputReference:
        return typing.cast(SagemakerUserProfileUserSettingsKernelGatewayAppSettingsDefaultResourceSpecOutputReference, jsii.get(self, "defaultResourceSpec"))

    @builtins.property
    @jsii.member(jsii_name="customImageInput")
    def custom_image_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerUserProfileUserSettingsKernelGatewayAppSettingsCustomImage]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerUserProfileUserSettingsKernelGatewayAppSettingsCustomImage]]], jsii.get(self, "customImageInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultResourceSpecInput")
    def default_resource_spec_input(
        self,
    ) -> typing.Optional[SagemakerUserProfileUserSettingsKernelGatewayAppSettingsDefaultResourceSpec]:
        return typing.cast(typing.Optional[SagemakerUserProfileUserSettingsKernelGatewayAppSettingsDefaultResourceSpec], jsii.get(self, "defaultResourceSpecInput"))

    @builtins.property
    @jsii.member(jsii_name="lifecycleConfigArnsInput")
    def lifecycle_config_arns_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "lifecycleConfigArnsInput"))

    @builtins.property
    @jsii.member(jsii_name="lifecycleConfigArns")
    def lifecycle_config_arns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "lifecycleConfigArns"))

    @lifecycle_config_arns.setter
    def lifecycle_config_arns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5540576825666600376d746abb42b3f3e6088e86508b43b3539690f536c92aa4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lifecycleConfigArns", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerUserProfileUserSettingsKernelGatewayAppSettings]:
        return typing.cast(typing.Optional[SagemakerUserProfileUserSettingsKernelGatewayAppSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerUserProfileUserSettingsKernelGatewayAppSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4eb0a8fefc73ed9d1684d5a617788f610149e0cf1aa69338ec9b3a9474c84919)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SagemakerUserProfileUserSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerUserProfile.SagemakerUserProfileUserSettingsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e0fdf84024a2e8f6fcc9a18f2c7a3ed1612d95ee2d9ae078de089cff8fd72176)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCanvasAppSettings")
    def put_canvas_app_settings(
        self,
        *,
        time_series_forecasting_settings: typing.Optional[typing.Union[SagemakerUserProfileUserSettingsCanvasAppSettingsTimeSeriesForecastingSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param time_series_forecasting_settings: time_series_forecasting_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#time_series_forecasting_settings SagemakerUserProfile#time_series_forecasting_settings}
        '''
        value = SagemakerUserProfileUserSettingsCanvasAppSettings(
            time_series_forecasting_settings=time_series_forecasting_settings
        )

        return typing.cast(None, jsii.invoke(self, "putCanvasAppSettings", [value]))

    @jsii.member(jsii_name="putJupyterServerAppSettings")
    def put_jupyter_server_app_settings(
        self,
        *,
        default_resource_spec: typing.Union[SagemakerUserProfileUserSettingsJupyterServerAppSettingsDefaultResourceSpec, typing.Dict[builtins.str, typing.Any]],
        code_repository: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerUserProfileUserSettingsJupyterServerAppSettingsCodeRepository, typing.Dict[builtins.str, typing.Any]]]]] = None,
        lifecycle_config_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param default_resource_spec: default_resource_spec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#default_resource_spec SagemakerUserProfile#default_resource_spec}
        :param code_repository: code_repository block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#code_repository SagemakerUserProfile#code_repository}
        :param lifecycle_config_arns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#lifecycle_config_arns SagemakerUserProfile#lifecycle_config_arns}.
        '''
        value = SagemakerUserProfileUserSettingsJupyterServerAppSettings(
            default_resource_spec=default_resource_spec,
            code_repository=code_repository,
            lifecycle_config_arns=lifecycle_config_arns,
        )

        return typing.cast(None, jsii.invoke(self, "putJupyterServerAppSettings", [value]))

    @jsii.member(jsii_name="putKernelGatewayAppSettings")
    def put_kernel_gateway_app_settings(
        self,
        *,
        default_resource_spec: typing.Union[SagemakerUserProfileUserSettingsKernelGatewayAppSettingsDefaultResourceSpec, typing.Dict[builtins.str, typing.Any]],
        custom_image: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerUserProfileUserSettingsKernelGatewayAppSettingsCustomImage, typing.Dict[builtins.str, typing.Any]]]]] = None,
        lifecycle_config_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param default_resource_spec: default_resource_spec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#default_resource_spec SagemakerUserProfile#default_resource_spec}
        :param custom_image: custom_image block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#custom_image SagemakerUserProfile#custom_image}
        :param lifecycle_config_arns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#lifecycle_config_arns SagemakerUserProfile#lifecycle_config_arns}.
        '''
        value = SagemakerUserProfileUserSettingsKernelGatewayAppSettings(
            default_resource_spec=default_resource_spec,
            custom_image=custom_image,
            lifecycle_config_arns=lifecycle_config_arns,
        )

        return typing.cast(None, jsii.invoke(self, "putKernelGatewayAppSettings", [value]))

    @jsii.member(jsii_name="putRSessionAppSettings")
    def put_r_session_app_settings(
        self,
        *,
        custom_image: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SagemakerUserProfileUserSettingsRSessionAppSettingsCustomImage", typing.Dict[builtins.str, typing.Any]]]]] = None,
        default_resource_spec: typing.Optional[typing.Union["SagemakerUserProfileUserSettingsRSessionAppSettingsDefaultResourceSpec", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param custom_image: custom_image block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#custom_image SagemakerUserProfile#custom_image}
        :param default_resource_spec: default_resource_spec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#default_resource_spec SagemakerUserProfile#default_resource_spec}
        '''
        value = SagemakerUserProfileUserSettingsRSessionAppSettings(
            custom_image=custom_image, default_resource_spec=default_resource_spec
        )

        return typing.cast(None, jsii.invoke(self, "putRSessionAppSettings", [value]))

    @jsii.member(jsii_name="putSharingSettings")
    def put_sharing_settings(
        self,
        *,
        notebook_output_option: typing.Optional[builtins.str] = None,
        s3_kms_key_id: typing.Optional[builtins.str] = None,
        s3_output_path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param notebook_output_option: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#notebook_output_option SagemakerUserProfile#notebook_output_option}.
        :param s3_kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#s3_kms_key_id SagemakerUserProfile#s3_kms_key_id}.
        :param s3_output_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#s3_output_path SagemakerUserProfile#s3_output_path}.
        '''
        value = SagemakerUserProfileUserSettingsSharingSettings(
            notebook_output_option=notebook_output_option,
            s3_kms_key_id=s3_kms_key_id,
            s3_output_path=s3_output_path,
        )

        return typing.cast(None, jsii.invoke(self, "putSharingSettings", [value]))

    @jsii.member(jsii_name="putTensorBoardAppSettings")
    def put_tensor_board_app_settings(
        self,
        *,
        default_resource_spec: typing.Union["SagemakerUserProfileUserSettingsTensorBoardAppSettingsDefaultResourceSpec", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param default_resource_spec: default_resource_spec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#default_resource_spec SagemakerUserProfile#default_resource_spec}
        '''
        value = SagemakerUserProfileUserSettingsTensorBoardAppSettings(
            default_resource_spec=default_resource_spec
        )

        return typing.cast(None, jsii.invoke(self, "putTensorBoardAppSettings", [value]))

    @jsii.member(jsii_name="resetCanvasAppSettings")
    def reset_canvas_app_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCanvasAppSettings", []))

    @jsii.member(jsii_name="resetJupyterServerAppSettings")
    def reset_jupyter_server_app_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJupyterServerAppSettings", []))

    @jsii.member(jsii_name="resetKernelGatewayAppSettings")
    def reset_kernel_gateway_app_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKernelGatewayAppSettings", []))

    @jsii.member(jsii_name="resetRSessionAppSettings")
    def reset_r_session_app_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRSessionAppSettings", []))

    @jsii.member(jsii_name="resetSecurityGroups")
    def reset_security_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecurityGroups", []))

    @jsii.member(jsii_name="resetSharingSettings")
    def reset_sharing_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSharingSettings", []))

    @jsii.member(jsii_name="resetTensorBoardAppSettings")
    def reset_tensor_board_app_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTensorBoardAppSettings", []))

    @builtins.property
    @jsii.member(jsii_name="canvasAppSettings")
    def canvas_app_settings(
        self,
    ) -> SagemakerUserProfileUserSettingsCanvasAppSettingsOutputReference:
        return typing.cast(SagemakerUserProfileUserSettingsCanvasAppSettingsOutputReference, jsii.get(self, "canvasAppSettings"))

    @builtins.property
    @jsii.member(jsii_name="jupyterServerAppSettings")
    def jupyter_server_app_settings(
        self,
    ) -> SagemakerUserProfileUserSettingsJupyterServerAppSettingsOutputReference:
        return typing.cast(SagemakerUserProfileUserSettingsJupyterServerAppSettingsOutputReference, jsii.get(self, "jupyterServerAppSettings"))

    @builtins.property
    @jsii.member(jsii_name="kernelGatewayAppSettings")
    def kernel_gateway_app_settings(
        self,
    ) -> SagemakerUserProfileUserSettingsKernelGatewayAppSettingsOutputReference:
        return typing.cast(SagemakerUserProfileUserSettingsKernelGatewayAppSettingsOutputReference, jsii.get(self, "kernelGatewayAppSettings"))

    @builtins.property
    @jsii.member(jsii_name="rSessionAppSettings")
    def r_session_app_settings(
        self,
    ) -> "SagemakerUserProfileUserSettingsRSessionAppSettingsOutputReference":
        return typing.cast("SagemakerUserProfileUserSettingsRSessionAppSettingsOutputReference", jsii.get(self, "rSessionAppSettings"))

    @builtins.property
    @jsii.member(jsii_name="sharingSettings")
    def sharing_settings(
        self,
    ) -> "SagemakerUserProfileUserSettingsSharingSettingsOutputReference":
        return typing.cast("SagemakerUserProfileUserSettingsSharingSettingsOutputReference", jsii.get(self, "sharingSettings"))

    @builtins.property
    @jsii.member(jsii_name="tensorBoardAppSettings")
    def tensor_board_app_settings(
        self,
    ) -> "SagemakerUserProfileUserSettingsTensorBoardAppSettingsOutputReference":
        return typing.cast("SagemakerUserProfileUserSettingsTensorBoardAppSettingsOutputReference", jsii.get(self, "tensorBoardAppSettings"))

    @builtins.property
    @jsii.member(jsii_name="canvasAppSettingsInput")
    def canvas_app_settings_input(
        self,
    ) -> typing.Optional[SagemakerUserProfileUserSettingsCanvasAppSettings]:
        return typing.cast(typing.Optional[SagemakerUserProfileUserSettingsCanvasAppSettings], jsii.get(self, "canvasAppSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="executionRoleInput")
    def execution_role_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "executionRoleInput"))

    @builtins.property
    @jsii.member(jsii_name="jupyterServerAppSettingsInput")
    def jupyter_server_app_settings_input(
        self,
    ) -> typing.Optional[SagemakerUserProfileUserSettingsJupyterServerAppSettings]:
        return typing.cast(typing.Optional[SagemakerUserProfileUserSettingsJupyterServerAppSettings], jsii.get(self, "jupyterServerAppSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="kernelGatewayAppSettingsInput")
    def kernel_gateway_app_settings_input(
        self,
    ) -> typing.Optional[SagemakerUserProfileUserSettingsKernelGatewayAppSettings]:
        return typing.cast(typing.Optional[SagemakerUserProfileUserSettingsKernelGatewayAppSettings], jsii.get(self, "kernelGatewayAppSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="rSessionAppSettingsInput")
    def r_session_app_settings_input(
        self,
    ) -> typing.Optional["SagemakerUserProfileUserSettingsRSessionAppSettings"]:
        return typing.cast(typing.Optional["SagemakerUserProfileUserSettingsRSessionAppSettings"], jsii.get(self, "rSessionAppSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="securityGroupsInput")
    def security_groups_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="sharingSettingsInput")
    def sharing_settings_input(
        self,
    ) -> typing.Optional["SagemakerUserProfileUserSettingsSharingSettings"]:
        return typing.cast(typing.Optional["SagemakerUserProfileUserSettingsSharingSettings"], jsii.get(self, "sharingSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="tensorBoardAppSettingsInput")
    def tensor_board_app_settings_input(
        self,
    ) -> typing.Optional["SagemakerUserProfileUserSettingsTensorBoardAppSettings"]:
        return typing.cast(typing.Optional["SagemakerUserProfileUserSettingsTensorBoardAppSettings"], jsii.get(self, "tensorBoardAppSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="executionRole")
    def execution_role(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "executionRole"))

    @execution_role.setter
    def execution_role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52b2305cb5c73a2c8925fe08e8d2795109fa915d63d798e22c8ff7aab4a8635c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "executionRole", value)

    @builtins.property
    @jsii.member(jsii_name="securityGroups")
    def security_groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "securityGroups"))

    @security_groups.setter
    def security_groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c71b3abb19c91dd873ef075a2142b11e8d8c6b5245b6f8ae991ae1661c01ba3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroups", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SagemakerUserProfileUserSettings]:
        return typing.cast(typing.Optional[SagemakerUserProfileUserSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerUserProfileUserSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2e8ea95865b6cbc30e615f8d8068596ea23f4ff82ce957508d8b4bfba1fd3c0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.sagemakerUserProfile.SagemakerUserProfileUserSettingsRSessionAppSettings",
    jsii_struct_bases=[],
    name_mapping={
        "custom_image": "customImage",
        "default_resource_spec": "defaultResourceSpec",
    },
)
class SagemakerUserProfileUserSettingsRSessionAppSettings:
    def __init__(
        self,
        *,
        custom_image: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SagemakerUserProfileUserSettingsRSessionAppSettingsCustomImage", typing.Dict[builtins.str, typing.Any]]]]] = None,
        default_resource_spec: typing.Optional[typing.Union["SagemakerUserProfileUserSettingsRSessionAppSettingsDefaultResourceSpec", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param custom_image: custom_image block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#custom_image SagemakerUserProfile#custom_image}
        :param default_resource_spec: default_resource_spec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#default_resource_spec SagemakerUserProfile#default_resource_spec}
        '''
        if isinstance(default_resource_spec, dict):
            default_resource_spec = SagemakerUserProfileUserSettingsRSessionAppSettingsDefaultResourceSpec(**default_resource_spec)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bdbe038d0bed961b1fb376f45204b64817ab1f61535428affa5715505a74b1ff)
            check_type(argname="argument custom_image", value=custom_image, expected_type=type_hints["custom_image"])
            check_type(argname="argument default_resource_spec", value=default_resource_spec, expected_type=type_hints["default_resource_spec"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if custom_image is not None:
            self._values["custom_image"] = custom_image
        if default_resource_spec is not None:
            self._values["default_resource_spec"] = default_resource_spec

    @builtins.property
    def custom_image(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SagemakerUserProfileUserSettingsRSessionAppSettingsCustomImage"]]]:
        '''custom_image block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#custom_image SagemakerUserProfile#custom_image}
        '''
        result = self._values.get("custom_image")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SagemakerUserProfileUserSettingsRSessionAppSettingsCustomImage"]]], result)

    @builtins.property
    def default_resource_spec(
        self,
    ) -> typing.Optional["SagemakerUserProfileUserSettingsRSessionAppSettingsDefaultResourceSpec"]:
        '''default_resource_spec block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#default_resource_spec SagemakerUserProfile#default_resource_spec}
        '''
        result = self._values.get("default_resource_spec")
        return typing.cast(typing.Optional["SagemakerUserProfileUserSettingsRSessionAppSettingsDefaultResourceSpec"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerUserProfileUserSettingsRSessionAppSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.sagemakerUserProfile.SagemakerUserProfileUserSettingsRSessionAppSettingsCustomImage",
    jsii_struct_bases=[],
    name_mapping={
        "app_image_config_name": "appImageConfigName",
        "image_name": "imageName",
        "image_version_number": "imageVersionNumber",
    },
)
class SagemakerUserProfileUserSettingsRSessionAppSettingsCustomImage:
    def __init__(
        self,
        *,
        app_image_config_name: builtins.str,
        image_name: builtins.str,
        image_version_number: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param app_image_config_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#app_image_config_name SagemakerUserProfile#app_image_config_name}.
        :param image_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#image_name SagemakerUserProfile#image_name}.
        :param image_version_number: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#image_version_number SagemakerUserProfile#image_version_number}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e6c1abc16529a431be2db568a6f454f7a2189b3d22f7ca90b0e4ba04547054f)
            check_type(argname="argument app_image_config_name", value=app_image_config_name, expected_type=type_hints["app_image_config_name"])
            check_type(argname="argument image_name", value=image_name, expected_type=type_hints["image_name"])
            check_type(argname="argument image_version_number", value=image_version_number, expected_type=type_hints["image_version_number"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "app_image_config_name": app_image_config_name,
            "image_name": image_name,
        }
        if image_version_number is not None:
            self._values["image_version_number"] = image_version_number

    @builtins.property
    def app_image_config_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#app_image_config_name SagemakerUserProfile#app_image_config_name}.'''
        result = self._values.get("app_image_config_name")
        assert result is not None, "Required property 'app_image_config_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def image_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#image_name SagemakerUserProfile#image_name}.'''
        result = self._values.get("image_name")
        assert result is not None, "Required property 'image_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def image_version_number(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#image_version_number SagemakerUserProfile#image_version_number}.'''
        result = self._values.get("image_version_number")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerUserProfileUserSettingsRSessionAppSettingsCustomImage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerUserProfileUserSettingsRSessionAppSettingsCustomImageList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerUserProfile.SagemakerUserProfileUserSettingsRSessionAppSettingsCustomImageList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__79e8f7d2124d98a472e2d7ed43d893cb03612e5b485d5ba6cc5b8f3b6df64b29)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "SagemakerUserProfileUserSettingsRSessionAppSettingsCustomImageOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39dde61ab1d0b2c22580ab951e88de2d0b68717834d5515e24f5f5cf289c7a2f)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SagemakerUserProfileUserSettingsRSessionAppSettingsCustomImageOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49c7678b26d40300064092996443fce86a609707b0da62a8b5b29d8058a367e8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__461399be1f0fe04633dc50dad9516e2d9c7a057f15d910f52b18d73f098c98fc)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6d7c33965955e711ac5d83d41c4c6846f9c990d197ba39fae8e77a5aaac4e09b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerUserProfileUserSettingsRSessionAppSettingsCustomImage]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerUserProfileUserSettingsRSessionAppSettingsCustomImage]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerUserProfileUserSettingsRSessionAppSettingsCustomImage]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ba328e76c57024d4c7aaba9e71e1a140e29953e796b4222d0d5cb4b1925212e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SagemakerUserProfileUserSettingsRSessionAppSettingsCustomImageOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerUserProfile.SagemakerUserProfileUserSettingsRSessionAppSettingsCustomImageOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8f3a1f6a6704046b278b67a5bd95960cf6bd11f88e6b53bbc2bf586f80436be2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetImageVersionNumber")
    def reset_image_version_number(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImageVersionNumber", []))

    @builtins.property
    @jsii.member(jsii_name="appImageConfigNameInput")
    def app_image_config_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "appImageConfigNameInput"))

    @builtins.property
    @jsii.member(jsii_name="imageNameInput")
    def image_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageNameInput"))

    @builtins.property
    @jsii.member(jsii_name="imageVersionNumberInput")
    def image_version_number_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "imageVersionNumberInput"))

    @builtins.property
    @jsii.member(jsii_name="appImageConfigName")
    def app_image_config_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "appImageConfigName"))

    @app_image_config_name.setter
    def app_image_config_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e4cda8886f78838067eebf975aef0adb5e5fcc8b93819db6c46aba600c647e1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appImageConfigName", value)

    @builtins.property
    @jsii.member(jsii_name="imageName")
    def image_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "imageName"))

    @image_name.setter
    def image_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__763f0bf2d169d8f2b1e98521a3901f6d0ecbb72615db6199e01819eb5db62e00)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageName", value)

    @builtins.property
    @jsii.member(jsii_name="imageVersionNumber")
    def image_version_number(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "imageVersionNumber"))

    @image_version_number.setter
    def image_version_number(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c763070e4c4ca574d519593dc8467be681ae66f6ebe0545c0ee58d7f1a187c1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageVersionNumber", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SagemakerUserProfileUserSettingsRSessionAppSettingsCustomImage, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SagemakerUserProfileUserSettingsRSessionAppSettingsCustomImage, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SagemakerUserProfileUserSettingsRSessionAppSettingsCustomImage, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6deca565b3083d1b1f0788108ec0678b6fde06f6ae05317482521bff131a58a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.sagemakerUserProfile.SagemakerUserProfileUserSettingsRSessionAppSettingsDefaultResourceSpec",
    jsii_struct_bases=[],
    name_mapping={
        "instance_type": "instanceType",
        "lifecycle_config_arn": "lifecycleConfigArn",
        "sagemaker_image_arn": "sagemakerImageArn",
        "sagemaker_image_version_arn": "sagemakerImageVersionArn",
    },
)
class SagemakerUserProfileUserSettingsRSessionAppSettingsDefaultResourceSpec:
    def __init__(
        self,
        *,
        instance_type: typing.Optional[builtins.str] = None,
        lifecycle_config_arn: typing.Optional[builtins.str] = None,
        sagemaker_image_arn: typing.Optional[builtins.str] = None,
        sagemaker_image_version_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param instance_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#instance_type SagemakerUserProfile#instance_type}.
        :param lifecycle_config_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#lifecycle_config_arn SagemakerUserProfile#lifecycle_config_arn}.
        :param sagemaker_image_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#sagemaker_image_arn SagemakerUserProfile#sagemaker_image_arn}.
        :param sagemaker_image_version_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#sagemaker_image_version_arn SagemakerUserProfile#sagemaker_image_version_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec7b40e124ec3583b199b405a75b1f3f0310d906a14156be1f0d538bf9f6f401)
            check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
            check_type(argname="argument lifecycle_config_arn", value=lifecycle_config_arn, expected_type=type_hints["lifecycle_config_arn"])
            check_type(argname="argument sagemaker_image_arn", value=sagemaker_image_arn, expected_type=type_hints["sagemaker_image_arn"])
            check_type(argname="argument sagemaker_image_version_arn", value=sagemaker_image_version_arn, expected_type=type_hints["sagemaker_image_version_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if instance_type is not None:
            self._values["instance_type"] = instance_type
        if lifecycle_config_arn is not None:
            self._values["lifecycle_config_arn"] = lifecycle_config_arn
        if sagemaker_image_arn is not None:
            self._values["sagemaker_image_arn"] = sagemaker_image_arn
        if sagemaker_image_version_arn is not None:
            self._values["sagemaker_image_version_arn"] = sagemaker_image_version_arn

    @builtins.property
    def instance_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#instance_type SagemakerUserProfile#instance_type}.'''
        result = self._values.get("instance_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lifecycle_config_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#lifecycle_config_arn SagemakerUserProfile#lifecycle_config_arn}.'''
        result = self._values.get("lifecycle_config_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sagemaker_image_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#sagemaker_image_arn SagemakerUserProfile#sagemaker_image_arn}.'''
        result = self._values.get("sagemaker_image_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sagemaker_image_version_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#sagemaker_image_version_arn SagemakerUserProfile#sagemaker_image_version_arn}.'''
        result = self._values.get("sagemaker_image_version_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerUserProfileUserSettingsRSessionAppSettingsDefaultResourceSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerUserProfileUserSettingsRSessionAppSettingsDefaultResourceSpecOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerUserProfile.SagemakerUserProfileUserSettingsRSessionAppSettingsDefaultResourceSpecOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4f0575430b5b2e83594ea329c61aa8e90b0451dc6d1b287bfa5bb6872a5e6b60)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetInstanceType")
    def reset_instance_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceType", []))

    @jsii.member(jsii_name="resetLifecycleConfigArn")
    def reset_lifecycle_config_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLifecycleConfigArn", []))

    @jsii.member(jsii_name="resetSagemakerImageArn")
    def reset_sagemaker_image_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSagemakerImageArn", []))

    @jsii.member(jsii_name="resetSagemakerImageVersionArn")
    def reset_sagemaker_image_version_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSagemakerImageVersionArn", []))

    @builtins.property
    @jsii.member(jsii_name="instanceTypeInput")
    def instance_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="lifecycleConfigArnInput")
    def lifecycle_config_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lifecycleConfigArnInput"))

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageArnInput")
    def sagemaker_image_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sagemakerImageArnInput"))

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageVersionArnInput")
    def sagemaker_image_version_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sagemakerImageVersionArnInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceType")
    def instance_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceType"))

    @instance_type.setter
    def instance_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2bcc96e38a6b57d9e61b3723be5ed532e1973bf6012c41ee959eb931463934ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceType", value)

    @builtins.property
    @jsii.member(jsii_name="lifecycleConfigArn")
    def lifecycle_config_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lifecycleConfigArn"))

    @lifecycle_config_arn.setter
    def lifecycle_config_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8a3fa47e8c338146451d9f1fd6983a0caf1d7957824a64827ce27ac91fdaaa7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lifecycleConfigArn", value)

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageArn")
    def sagemaker_image_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sagemakerImageArn"))

    @sagemaker_image_arn.setter
    def sagemaker_image_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d64ef0730db40bad386ff2eb499e7469cc30c3e1caa3a7213b601f87ad8b5807)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sagemakerImageArn", value)

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageVersionArn")
    def sagemaker_image_version_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sagemakerImageVersionArn"))

    @sagemaker_image_version_arn.setter
    def sagemaker_image_version_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2415d512337376730038d66c0e369a1c6f54617c6d2b90d07233ed78cf58d74)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sagemakerImageVersionArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerUserProfileUserSettingsRSessionAppSettingsDefaultResourceSpec]:
        return typing.cast(typing.Optional[SagemakerUserProfileUserSettingsRSessionAppSettingsDefaultResourceSpec], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerUserProfileUserSettingsRSessionAppSettingsDefaultResourceSpec],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__890000032619ec7cd7f5c6be20d91a59e48cf8cb309a9b508de3a1ee81e639c1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SagemakerUserProfileUserSettingsRSessionAppSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerUserProfile.SagemakerUserProfileUserSettingsRSessionAppSettingsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__44a643204443c0d1a0654f9762ed40a68efef186a8a31b31976a12a03e506120)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCustomImage")
    def put_custom_image(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerUserProfileUserSettingsRSessionAppSettingsCustomImage, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54fc407bd22fb507e5b6d027f2ca1cc2395b7b11fae8c8f7de0282ee357eb4da)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCustomImage", [value]))

    @jsii.member(jsii_name="putDefaultResourceSpec")
    def put_default_resource_spec(
        self,
        *,
        instance_type: typing.Optional[builtins.str] = None,
        lifecycle_config_arn: typing.Optional[builtins.str] = None,
        sagemaker_image_arn: typing.Optional[builtins.str] = None,
        sagemaker_image_version_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param instance_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#instance_type SagemakerUserProfile#instance_type}.
        :param lifecycle_config_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#lifecycle_config_arn SagemakerUserProfile#lifecycle_config_arn}.
        :param sagemaker_image_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#sagemaker_image_arn SagemakerUserProfile#sagemaker_image_arn}.
        :param sagemaker_image_version_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#sagemaker_image_version_arn SagemakerUserProfile#sagemaker_image_version_arn}.
        '''
        value = SagemakerUserProfileUserSettingsRSessionAppSettingsDefaultResourceSpec(
            instance_type=instance_type,
            lifecycle_config_arn=lifecycle_config_arn,
            sagemaker_image_arn=sagemaker_image_arn,
            sagemaker_image_version_arn=sagemaker_image_version_arn,
        )

        return typing.cast(None, jsii.invoke(self, "putDefaultResourceSpec", [value]))

    @jsii.member(jsii_name="resetCustomImage")
    def reset_custom_image(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomImage", []))

    @jsii.member(jsii_name="resetDefaultResourceSpec")
    def reset_default_resource_spec(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultResourceSpec", []))

    @builtins.property
    @jsii.member(jsii_name="customImage")
    def custom_image(
        self,
    ) -> SagemakerUserProfileUserSettingsRSessionAppSettingsCustomImageList:
        return typing.cast(SagemakerUserProfileUserSettingsRSessionAppSettingsCustomImageList, jsii.get(self, "customImage"))

    @builtins.property
    @jsii.member(jsii_name="defaultResourceSpec")
    def default_resource_spec(
        self,
    ) -> SagemakerUserProfileUserSettingsRSessionAppSettingsDefaultResourceSpecOutputReference:
        return typing.cast(SagemakerUserProfileUserSettingsRSessionAppSettingsDefaultResourceSpecOutputReference, jsii.get(self, "defaultResourceSpec"))

    @builtins.property
    @jsii.member(jsii_name="customImageInput")
    def custom_image_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerUserProfileUserSettingsRSessionAppSettingsCustomImage]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerUserProfileUserSettingsRSessionAppSettingsCustomImage]]], jsii.get(self, "customImageInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultResourceSpecInput")
    def default_resource_spec_input(
        self,
    ) -> typing.Optional[SagemakerUserProfileUserSettingsRSessionAppSettingsDefaultResourceSpec]:
        return typing.cast(typing.Optional[SagemakerUserProfileUserSettingsRSessionAppSettingsDefaultResourceSpec], jsii.get(self, "defaultResourceSpecInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerUserProfileUserSettingsRSessionAppSettings]:
        return typing.cast(typing.Optional[SagemakerUserProfileUserSettingsRSessionAppSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerUserProfileUserSettingsRSessionAppSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f033f31c1d9d63a298ca056292d7deb98489b0baf2f5832bbd6065f57359a69a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.sagemakerUserProfile.SagemakerUserProfileUserSettingsSharingSettings",
    jsii_struct_bases=[],
    name_mapping={
        "notebook_output_option": "notebookOutputOption",
        "s3_kms_key_id": "s3KmsKeyId",
        "s3_output_path": "s3OutputPath",
    },
)
class SagemakerUserProfileUserSettingsSharingSettings:
    def __init__(
        self,
        *,
        notebook_output_option: typing.Optional[builtins.str] = None,
        s3_kms_key_id: typing.Optional[builtins.str] = None,
        s3_output_path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param notebook_output_option: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#notebook_output_option SagemakerUserProfile#notebook_output_option}.
        :param s3_kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#s3_kms_key_id SagemakerUserProfile#s3_kms_key_id}.
        :param s3_output_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#s3_output_path SagemakerUserProfile#s3_output_path}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c670df9fb49d4ba8edabed0a2391809bddb6ecf89563b4369669b5da1786b7f0)
            check_type(argname="argument notebook_output_option", value=notebook_output_option, expected_type=type_hints["notebook_output_option"])
            check_type(argname="argument s3_kms_key_id", value=s3_kms_key_id, expected_type=type_hints["s3_kms_key_id"])
            check_type(argname="argument s3_output_path", value=s3_output_path, expected_type=type_hints["s3_output_path"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if notebook_output_option is not None:
            self._values["notebook_output_option"] = notebook_output_option
        if s3_kms_key_id is not None:
            self._values["s3_kms_key_id"] = s3_kms_key_id
        if s3_output_path is not None:
            self._values["s3_output_path"] = s3_output_path

    @builtins.property
    def notebook_output_option(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#notebook_output_option SagemakerUserProfile#notebook_output_option}.'''
        result = self._values.get("notebook_output_option")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def s3_kms_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#s3_kms_key_id SagemakerUserProfile#s3_kms_key_id}.'''
        result = self._values.get("s3_kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def s3_output_path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#s3_output_path SagemakerUserProfile#s3_output_path}.'''
        result = self._values.get("s3_output_path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerUserProfileUserSettingsSharingSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerUserProfileUserSettingsSharingSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerUserProfile.SagemakerUserProfileUserSettingsSharingSettingsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2f8916c8ea93b66bb13bf9cbb94796572806c7b7fa6a71f097bbab44d983b95a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetNotebookOutputOption")
    def reset_notebook_output_option(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotebookOutputOption", []))

    @jsii.member(jsii_name="resetS3KmsKeyId")
    def reset_s3_kms_key_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3KmsKeyId", []))

    @jsii.member(jsii_name="resetS3OutputPath")
    def reset_s3_output_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3OutputPath", []))

    @builtins.property
    @jsii.member(jsii_name="notebookOutputOptionInput")
    def notebook_output_option_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "notebookOutputOptionInput"))

    @builtins.property
    @jsii.member(jsii_name="s3KmsKeyIdInput")
    def s3_kms_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "s3KmsKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="s3OutputPathInput")
    def s3_output_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "s3OutputPathInput"))

    @builtins.property
    @jsii.member(jsii_name="notebookOutputOption")
    def notebook_output_option(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "notebookOutputOption"))

    @notebook_output_option.setter
    def notebook_output_option(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aeb803a1eb0537e178312aec98bf49d3799e25776f64bc51f84da5d057767f58)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notebookOutputOption", value)

    @builtins.property
    @jsii.member(jsii_name="s3KmsKeyId")
    def s3_kms_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "s3KmsKeyId"))

    @s3_kms_key_id.setter
    def s3_kms_key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__944fb1d453419777b5ed7be9ef6276e4a101f6980b0940c8f4e17fbe3d74769b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3KmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="s3OutputPath")
    def s3_output_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "s3OutputPath"))

    @s3_output_path.setter
    def s3_output_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec1446063e71b73984ae53acdec6127e2f46da2afa81736e41d87e770106a72b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3OutputPath", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerUserProfileUserSettingsSharingSettings]:
        return typing.cast(typing.Optional[SagemakerUserProfileUserSettingsSharingSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerUserProfileUserSettingsSharingSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c79b09548a50aaf1b617ed5d402dec09fd56f767671f5dcb35fac86db522b5a9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.sagemakerUserProfile.SagemakerUserProfileUserSettingsTensorBoardAppSettings",
    jsii_struct_bases=[],
    name_mapping={"default_resource_spec": "defaultResourceSpec"},
)
class SagemakerUserProfileUserSettingsTensorBoardAppSettings:
    def __init__(
        self,
        *,
        default_resource_spec: typing.Union["SagemakerUserProfileUserSettingsTensorBoardAppSettingsDefaultResourceSpec", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param default_resource_spec: default_resource_spec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#default_resource_spec SagemakerUserProfile#default_resource_spec}
        '''
        if isinstance(default_resource_spec, dict):
            default_resource_spec = SagemakerUserProfileUserSettingsTensorBoardAppSettingsDefaultResourceSpec(**default_resource_spec)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d042887c89681349a407a7c56d1db06bb1a37a1e347c5f6e020b260a0d6f460e)
            check_type(argname="argument default_resource_spec", value=default_resource_spec, expected_type=type_hints["default_resource_spec"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "default_resource_spec": default_resource_spec,
        }

    @builtins.property
    def default_resource_spec(
        self,
    ) -> "SagemakerUserProfileUserSettingsTensorBoardAppSettingsDefaultResourceSpec":
        '''default_resource_spec block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#default_resource_spec SagemakerUserProfile#default_resource_spec}
        '''
        result = self._values.get("default_resource_spec")
        assert result is not None, "Required property 'default_resource_spec' is missing"
        return typing.cast("SagemakerUserProfileUserSettingsTensorBoardAppSettingsDefaultResourceSpec", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerUserProfileUserSettingsTensorBoardAppSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.sagemakerUserProfile.SagemakerUserProfileUserSettingsTensorBoardAppSettingsDefaultResourceSpec",
    jsii_struct_bases=[],
    name_mapping={
        "instance_type": "instanceType",
        "lifecycle_config_arn": "lifecycleConfigArn",
        "sagemaker_image_arn": "sagemakerImageArn",
        "sagemaker_image_version_arn": "sagemakerImageVersionArn",
    },
)
class SagemakerUserProfileUserSettingsTensorBoardAppSettingsDefaultResourceSpec:
    def __init__(
        self,
        *,
        instance_type: typing.Optional[builtins.str] = None,
        lifecycle_config_arn: typing.Optional[builtins.str] = None,
        sagemaker_image_arn: typing.Optional[builtins.str] = None,
        sagemaker_image_version_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param instance_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#instance_type SagemakerUserProfile#instance_type}.
        :param lifecycle_config_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#lifecycle_config_arn SagemakerUserProfile#lifecycle_config_arn}.
        :param sagemaker_image_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#sagemaker_image_arn SagemakerUserProfile#sagemaker_image_arn}.
        :param sagemaker_image_version_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#sagemaker_image_version_arn SagemakerUserProfile#sagemaker_image_version_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6471adfa33d4489ed7646aac01752ebb8cc3f799856a34e0aa52457e9ebf52d6)
            check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
            check_type(argname="argument lifecycle_config_arn", value=lifecycle_config_arn, expected_type=type_hints["lifecycle_config_arn"])
            check_type(argname="argument sagemaker_image_arn", value=sagemaker_image_arn, expected_type=type_hints["sagemaker_image_arn"])
            check_type(argname="argument sagemaker_image_version_arn", value=sagemaker_image_version_arn, expected_type=type_hints["sagemaker_image_version_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if instance_type is not None:
            self._values["instance_type"] = instance_type
        if lifecycle_config_arn is not None:
            self._values["lifecycle_config_arn"] = lifecycle_config_arn
        if sagemaker_image_arn is not None:
            self._values["sagemaker_image_arn"] = sagemaker_image_arn
        if sagemaker_image_version_arn is not None:
            self._values["sagemaker_image_version_arn"] = sagemaker_image_version_arn

    @builtins.property
    def instance_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#instance_type SagemakerUserProfile#instance_type}.'''
        result = self._values.get("instance_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lifecycle_config_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#lifecycle_config_arn SagemakerUserProfile#lifecycle_config_arn}.'''
        result = self._values.get("lifecycle_config_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sagemaker_image_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#sagemaker_image_arn SagemakerUserProfile#sagemaker_image_arn}.'''
        result = self._values.get("sagemaker_image_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sagemaker_image_version_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#sagemaker_image_version_arn SagemakerUserProfile#sagemaker_image_version_arn}.'''
        result = self._values.get("sagemaker_image_version_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerUserProfileUserSettingsTensorBoardAppSettingsDefaultResourceSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerUserProfileUserSettingsTensorBoardAppSettingsDefaultResourceSpecOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerUserProfile.SagemakerUserProfileUserSettingsTensorBoardAppSettingsDefaultResourceSpecOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f93023bf4003d35b381687c59a1f710e25179b87779c7f481d7e5fb1882167bc)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetInstanceType")
    def reset_instance_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceType", []))

    @jsii.member(jsii_name="resetLifecycleConfigArn")
    def reset_lifecycle_config_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLifecycleConfigArn", []))

    @jsii.member(jsii_name="resetSagemakerImageArn")
    def reset_sagemaker_image_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSagemakerImageArn", []))

    @jsii.member(jsii_name="resetSagemakerImageVersionArn")
    def reset_sagemaker_image_version_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSagemakerImageVersionArn", []))

    @builtins.property
    @jsii.member(jsii_name="instanceTypeInput")
    def instance_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="lifecycleConfigArnInput")
    def lifecycle_config_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lifecycleConfigArnInput"))

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageArnInput")
    def sagemaker_image_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sagemakerImageArnInput"))

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageVersionArnInput")
    def sagemaker_image_version_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sagemakerImageVersionArnInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceType")
    def instance_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceType"))

    @instance_type.setter
    def instance_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__860e56164b3d739f9f84926f783975e03fa0625e55a96b1bebe17427088b41a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceType", value)

    @builtins.property
    @jsii.member(jsii_name="lifecycleConfigArn")
    def lifecycle_config_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lifecycleConfigArn"))

    @lifecycle_config_arn.setter
    def lifecycle_config_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__350c1495f1a9dc24b35421322ecdaedcff933926ae0b7579b45961e57994e5fb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lifecycleConfigArn", value)

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageArn")
    def sagemaker_image_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sagemakerImageArn"))

    @sagemaker_image_arn.setter
    def sagemaker_image_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__781d70e60663336d831ba58d813d1ac8aac4357c80f0a034bad531421a980486)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sagemakerImageArn", value)

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageVersionArn")
    def sagemaker_image_version_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sagemakerImageVersionArn"))

    @sagemaker_image_version_arn.setter
    def sagemaker_image_version_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52159f5de86ad154189be3ee5d977cf170e28c040f96af1234cce753be73e272)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sagemakerImageVersionArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerUserProfileUserSettingsTensorBoardAppSettingsDefaultResourceSpec]:
        return typing.cast(typing.Optional[SagemakerUserProfileUserSettingsTensorBoardAppSettingsDefaultResourceSpec], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerUserProfileUserSettingsTensorBoardAppSettingsDefaultResourceSpec],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7305a30990c4a1c5ed404f4ed89ceca1cf4ef0527a0e04cdd3f5a8e5b9c4db7c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SagemakerUserProfileUserSettingsTensorBoardAppSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerUserProfile.SagemakerUserProfileUserSettingsTensorBoardAppSettingsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__14957314c3a4d6ee856cad43fed4aaecd93c1b94983432431fc92fce420bb548)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDefaultResourceSpec")
    def put_default_resource_spec(
        self,
        *,
        instance_type: typing.Optional[builtins.str] = None,
        lifecycle_config_arn: typing.Optional[builtins.str] = None,
        sagemaker_image_arn: typing.Optional[builtins.str] = None,
        sagemaker_image_version_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param instance_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#instance_type SagemakerUserProfile#instance_type}.
        :param lifecycle_config_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#lifecycle_config_arn SagemakerUserProfile#lifecycle_config_arn}.
        :param sagemaker_image_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#sagemaker_image_arn SagemakerUserProfile#sagemaker_image_arn}.
        :param sagemaker_image_version_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_user_profile#sagemaker_image_version_arn SagemakerUserProfile#sagemaker_image_version_arn}.
        '''
        value = SagemakerUserProfileUserSettingsTensorBoardAppSettingsDefaultResourceSpec(
            instance_type=instance_type,
            lifecycle_config_arn=lifecycle_config_arn,
            sagemaker_image_arn=sagemaker_image_arn,
            sagemaker_image_version_arn=sagemaker_image_version_arn,
        )

        return typing.cast(None, jsii.invoke(self, "putDefaultResourceSpec", [value]))

    @builtins.property
    @jsii.member(jsii_name="defaultResourceSpec")
    def default_resource_spec(
        self,
    ) -> SagemakerUserProfileUserSettingsTensorBoardAppSettingsDefaultResourceSpecOutputReference:
        return typing.cast(SagemakerUserProfileUserSettingsTensorBoardAppSettingsDefaultResourceSpecOutputReference, jsii.get(self, "defaultResourceSpec"))

    @builtins.property
    @jsii.member(jsii_name="defaultResourceSpecInput")
    def default_resource_spec_input(
        self,
    ) -> typing.Optional[SagemakerUserProfileUserSettingsTensorBoardAppSettingsDefaultResourceSpec]:
        return typing.cast(typing.Optional[SagemakerUserProfileUserSettingsTensorBoardAppSettingsDefaultResourceSpec], jsii.get(self, "defaultResourceSpecInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerUserProfileUserSettingsTensorBoardAppSettings]:
        return typing.cast(typing.Optional[SagemakerUserProfileUserSettingsTensorBoardAppSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerUserProfileUserSettingsTensorBoardAppSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb9ce70cdb7515db33d8a364317adaac407c4887a717f70e88fbf5bf179c3288)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "SagemakerUserProfile",
    "SagemakerUserProfileConfig",
    "SagemakerUserProfileUserSettings",
    "SagemakerUserProfileUserSettingsCanvasAppSettings",
    "SagemakerUserProfileUserSettingsCanvasAppSettingsOutputReference",
    "SagemakerUserProfileUserSettingsCanvasAppSettingsTimeSeriesForecastingSettings",
    "SagemakerUserProfileUserSettingsCanvasAppSettingsTimeSeriesForecastingSettingsOutputReference",
    "SagemakerUserProfileUserSettingsJupyterServerAppSettings",
    "SagemakerUserProfileUserSettingsJupyterServerAppSettingsCodeRepository",
    "SagemakerUserProfileUserSettingsJupyterServerAppSettingsCodeRepositoryList",
    "SagemakerUserProfileUserSettingsJupyterServerAppSettingsCodeRepositoryOutputReference",
    "SagemakerUserProfileUserSettingsJupyterServerAppSettingsDefaultResourceSpec",
    "SagemakerUserProfileUserSettingsJupyterServerAppSettingsDefaultResourceSpecOutputReference",
    "SagemakerUserProfileUserSettingsJupyterServerAppSettingsOutputReference",
    "SagemakerUserProfileUserSettingsKernelGatewayAppSettings",
    "SagemakerUserProfileUserSettingsKernelGatewayAppSettingsCustomImage",
    "SagemakerUserProfileUserSettingsKernelGatewayAppSettingsCustomImageList",
    "SagemakerUserProfileUserSettingsKernelGatewayAppSettingsCustomImageOutputReference",
    "SagemakerUserProfileUserSettingsKernelGatewayAppSettingsDefaultResourceSpec",
    "SagemakerUserProfileUserSettingsKernelGatewayAppSettingsDefaultResourceSpecOutputReference",
    "SagemakerUserProfileUserSettingsKernelGatewayAppSettingsOutputReference",
    "SagemakerUserProfileUserSettingsOutputReference",
    "SagemakerUserProfileUserSettingsRSessionAppSettings",
    "SagemakerUserProfileUserSettingsRSessionAppSettingsCustomImage",
    "SagemakerUserProfileUserSettingsRSessionAppSettingsCustomImageList",
    "SagemakerUserProfileUserSettingsRSessionAppSettingsCustomImageOutputReference",
    "SagemakerUserProfileUserSettingsRSessionAppSettingsDefaultResourceSpec",
    "SagemakerUserProfileUserSettingsRSessionAppSettingsDefaultResourceSpecOutputReference",
    "SagemakerUserProfileUserSettingsRSessionAppSettingsOutputReference",
    "SagemakerUserProfileUserSettingsSharingSettings",
    "SagemakerUserProfileUserSettingsSharingSettingsOutputReference",
    "SagemakerUserProfileUserSettingsTensorBoardAppSettings",
    "SagemakerUserProfileUserSettingsTensorBoardAppSettingsDefaultResourceSpec",
    "SagemakerUserProfileUserSettingsTensorBoardAppSettingsDefaultResourceSpecOutputReference",
    "SagemakerUserProfileUserSettingsTensorBoardAppSettingsOutputReference",
]

publication.publish()

def _typecheckingstub__dd3ea87bdcd92be1b32a569209e58887a4b8cf0a1129184e09781056af0e21c7(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    domain_id: builtins.str,
    user_profile_name: builtins.str,
    id: typing.Optional[builtins.str] = None,
    single_sign_on_user_identifier: typing.Optional[builtins.str] = None,
    single_sign_on_user_value: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    user_settings: typing.Optional[typing.Union[SagemakerUserProfileUserSettings, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__f191d7eca73a9f60a900618beb667ee009bebe2670ccecfe43d60e6d438cfd88(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__808b16b8d7c4ea3f2731d5af691fce921dd7435185f039b66b4b260c24a1dabe(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd3cb9bd75b15bf6e99b0beb2380934cb7b45f235ad47337fc9e5b263441ce87(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35363910df4c7179a01ce3816eed74e3adfc522587c04b7e7968b5a243bd8c71(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24516786d954c54762fef986c2eede5291c4f6a14a7776c9dfb4afedc49dec8a(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ff0dd72283a8b4a3a327bd40b9ff2042f99605d1c166fb80bc960211d0b3ecb(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2fc6398015cf63d1543035ffbb9dd11c4d0e50146d3796b1de861f58c034e4cf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73cd0fc9769617e44b2bd2cdd0bc0b572bb10551fe90a1cc4970a84d40792226(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    domain_id: builtins.str,
    user_profile_name: builtins.str,
    id: typing.Optional[builtins.str] = None,
    single_sign_on_user_identifier: typing.Optional[builtins.str] = None,
    single_sign_on_user_value: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    user_settings: typing.Optional[typing.Union[SagemakerUserProfileUserSettings, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__306f063596160d1b52135ff7326478b4dcbf6bbe28cf5f64751f4aa83fe1d572(
    *,
    execution_role: builtins.str,
    canvas_app_settings: typing.Optional[typing.Union[SagemakerUserProfileUserSettingsCanvasAppSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    jupyter_server_app_settings: typing.Optional[typing.Union[SagemakerUserProfileUserSettingsJupyterServerAppSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    kernel_gateway_app_settings: typing.Optional[typing.Union[SagemakerUserProfileUserSettingsKernelGatewayAppSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    r_session_app_settings: typing.Optional[typing.Union[SagemakerUserProfileUserSettingsRSessionAppSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    sharing_settings: typing.Optional[typing.Union[SagemakerUserProfileUserSettingsSharingSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    tensor_board_app_settings: typing.Optional[typing.Union[SagemakerUserProfileUserSettingsTensorBoardAppSettings, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16d09b2bc3f03a9bad901b1527d6ad9c7de8c5f2c8308c536adb5d4fa855deea(
    *,
    time_series_forecasting_settings: typing.Optional[typing.Union[SagemakerUserProfileUserSettingsCanvasAppSettingsTimeSeriesForecastingSettings, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69a4b6ffa730b8ca119734580eae653bc5bcd3d9d1b1ec694fdbef1c25069405(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61c5a6523896991c5be0a0e4b84781da8513bc369ac8fe9c47e0beed006d6544(
    value: typing.Optional[SagemakerUserProfileUserSettingsCanvasAppSettings],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__112770e3f4de92edb14572763999d4b0fa2adef5718365d58c265d3c39763f13(
    *,
    amazon_forecast_role_arn: typing.Optional[builtins.str] = None,
    status: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c2afc809c01888df468e9803ecd1497355c28776f2bc7d23470f32758588804(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40598666bdd057a11549bf592d1408ed5b297533b83a58ba9ae3cb2ae4ef0499(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__204389a718c4f7ac1e7e645058c4802816deb176e3d667ba5a4256ac40c4b6fb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27b47a6cf1716cdeea9d008b4eff25700650bb104504cafdb46c90886ae93321(
    value: typing.Optional[SagemakerUserProfileUserSettingsCanvasAppSettingsTimeSeriesForecastingSettings],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04fcf7b5687bdfe532a8a064fca0e6906d3e302cfed15dee44db46ff212fa6f4(
    *,
    default_resource_spec: typing.Union[SagemakerUserProfileUserSettingsJupyterServerAppSettingsDefaultResourceSpec, typing.Dict[builtins.str, typing.Any]],
    code_repository: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerUserProfileUserSettingsJupyterServerAppSettingsCodeRepository, typing.Dict[builtins.str, typing.Any]]]]] = None,
    lifecycle_config_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15aec08afdb643490a5d3adc86ab690923bd8dc5d0de509a0b506f908b28fb89(
    *,
    repository_url: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e563758f5d09b0484f056aa2aff747b21211ce1a200cc5bcdbdd2c98ad8be65(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50572d71de37e8c322cffc1d33aab92b6122442738db0cf94971f4248b0395f4(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d5db4b5512e74fabf118e17f8622cad42ec8a8868a1c1fade0700e565379894(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8abeeb7863c8daa380a0cbc92b08d561a2bfe6a71a1ae42e758871fea10dae87(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3762feedcb5e283dcdf784ebdf5ea19ea35c6ea3f36dba40edd7e1d9ae35f79(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3765f96c603f6488b0d4db0431f4f97daef18f61995843bdd7b2763a4264df18(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerUserProfileUserSettingsJupyterServerAppSettingsCodeRepository]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0ed1b206c66fad8eb894d47c58536113e883392cf6b0668926577b3cce06037(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4868df7444601ccf15262cb7e4d14ac3099e912ce6bc8e71727c06960de7650f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd287730ad069041a0dd48aac409169763267bcb4f57f4bae41adf69a1a8ab3e(
    value: typing.Optional[typing.Union[SagemakerUserProfileUserSettingsJupyterServerAppSettingsCodeRepository, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac8c7168539cae31994e1528bc892d22833a459587905ec742bab1c1e5fc310f(
    *,
    instance_type: typing.Optional[builtins.str] = None,
    lifecycle_config_arn: typing.Optional[builtins.str] = None,
    sagemaker_image_arn: typing.Optional[builtins.str] = None,
    sagemaker_image_version_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68dac719f8098a672cc6b80891627ef3dff4548679a64a83218934fc3a70fba7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73cd5601cc3bfa904b5eb21412967989f8df794170a6c0825ec32e1ffa93803d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ecf9d2adf8f81491458127074fdde5edb2ba300f4f9cbc22a95af3bd6e9a140(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f51d1563515d70f94344fee03b301fd5f312efbacedf4f76a340a86296e19ee8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e8af36d100fa85c26642e6a743b2b0359b9490bf451b1310ee7c615e8e0153d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d586dc6ebbc9f8d5ccd4e59a54ca60d2f90fedfc1d934f0f97d868cdf0af5c7(
    value: typing.Optional[SagemakerUserProfileUserSettingsJupyterServerAppSettingsDefaultResourceSpec],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__937ac3e1ba3ddb39ec99f6d4e92effa287defcb0f00b92153c64f9ac3dd4a61f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd69df47f582fc37a000b8188395c7f18b35d88eb0b60c7522ef9c2b9e02e406(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerUserProfileUserSettingsJupyterServerAppSettingsCodeRepository, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c25c999871628efd294de82ea81ccea9abecce9d907f6b5369abbe21b97dae4e(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97a3aa76918f1ed3df7a15dc17d04538f5bbbcfb2acbce0e0253eac72158ff3b(
    value: typing.Optional[SagemakerUserProfileUserSettingsJupyterServerAppSettings],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__346ca577f5fb3b958a7dab690897b6d3acb033cf8d0048b0827f793fa8bcb47d(
    *,
    default_resource_spec: typing.Union[SagemakerUserProfileUserSettingsKernelGatewayAppSettingsDefaultResourceSpec, typing.Dict[builtins.str, typing.Any]],
    custom_image: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerUserProfileUserSettingsKernelGatewayAppSettingsCustomImage, typing.Dict[builtins.str, typing.Any]]]]] = None,
    lifecycle_config_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba94295c8afeace5e45e4c2d3d849316f40dca1c9eb2d77492b8867bda645ffe(
    *,
    app_image_config_name: builtins.str,
    image_name: builtins.str,
    image_version_number: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__228bd0b6b9395c15ebef4731ef962febf92fd3b733e56ddbe5f5635cda9f01a6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7e9b85453f6a196c20084557ee9df6c7cee619be469a28e5b306673af411b4f(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b679d9e84d10515c04235088890fcebec58300182b1a8ca1a4f2db34568cfe4d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ba1f5730df4755f3cc699d03670b2229818fdf82874dc35dd8370a6722c609a(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b31a07c3e335505cea00bcd36ae163b07e4a93a5920c3c2dad072ca6cddd92bf(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bbdee080a48812a455fa0a2e374026b7e3a3a2e7234ff71069d372c1038a6fc1(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerUserProfileUserSettingsKernelGatewayAppSettingsCustomImage]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76c1bdf133aeeeb394b3d611947334076b4f0a513468d39c52904d8b8ad7c206(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c61cb794f464815dc32f5a220de2fa3639d240bcf995e32a7ec2974b94eac099(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__122c997d837e6d10228c7c702850da9aa90adfff33ea464b9329f85098961865(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc83a303d6e65c230c693e4d000970fff4420d960a9d3e6ef429237f85dc6bcb(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__efd715ac7ef21d63421454edd6ef3a4bb811badf05d5889a7406433485bbd4c4(
    value: typing.Optional[typing.Union[SagemakerUserProfileUserSettingsKernelGatewayAppSettingsCustomImage, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5cf658faaa3c5ae2b7c61a5944ea284c77b49a322ae658dfe40d2803e93a0fc1(
    *,
    instance_type: typing.Optional[builtins.str] = None,
    lifecycle_config_arn: typing.Optional[builtins.str] = None,
    sagemaker_image_arn: typing.Optional[builtins.str] = None,
    sagemaker_image_version_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4362b8fa84107e5028acee923367b89350434eefebdbfb972ffdc27ee3068a96(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dff61fd52136fda177c5e3b437998c1ff3b2451051c2d6fe3ca578e89cb85795(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c18c6ec3ca84fe6a03a764a2335b7be0ad27faf5dd2496b2d6523bf81346379(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19c4eb45e2d2e3844a5052861ff096742055e8020dddcee3a224096a232eefc4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed53ac962a92899eb98184a2e1c24b979089a6bd461d40d06f1f8d5436d83610(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__606e80f16417061c02469c300bfe306250da2d412f246b4c2533feb03c3ca421(
    value: typing.Optional[SagemakerUserProfileUserSettingsKernelGatewayAppSettingsDefaultResourceSpec],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f94329f77f18be7b5602e4ac1fc47e1edb2f29b208ef663f8c0d88ff0ad231f0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e765526e93b6120844d2b24b0c782b5788bea2ee156fae755cfd809f4606f339(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerUserProfileUserSettingsKernelGatewayAppSettingsCustomImage, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5540576825666600376d746abb42b3f3e6088e86508b43b3539690f536c92aa4(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4eb0a8fefc73ed9d1684d5a617788f610149e0cf1aa69338ec9b3a9474c84919(
    value: typing.Optional[SagemakerUserProfileUserSettingsKernelGatewayAppSettings],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0fdf84024a2e8f6fcc9a18f2c7a3ed1612d95ee2d9ae078de089cff8fd72176(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52b2305cb5c73a2c8925fe08e8d2795109fa915d63d798e22c8ff7aab4a8635c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c71b3abb19c91dd873ef075a2142b11e8d8c6b5245b6f8ae991ae1661c01ba3(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2e8ea95865b6cbc30e615f8d8068596ea23f4ff82ce957508d8b4bfba1fd3c0(
    value: typing.Optional[SagemakerUserProfileUserSettings],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bdbe038d0bed961b1fb376f45204b64817ab1f61535428affa5715505a74b1ff(
    *,
    custom_image: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerUserProfileUserSettingsRSessionAppSettingsCustomImage, typing.Dict[builtins.str, typing.Any]]]]] = None,
    default_resource_spec: typing.Optional[typing.Union[SagemakerUserProfileUserSettingsRSessionAppSettingsDefaultResourceSpec, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e6c1abc16529a431be2db568a6f454f7a2189b3d22f7ca90b0e4ba04547054f(
    *,
    app_image_config_name: builtins.str,
    image_name: builtins.str,
    image_version_number: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79e8f7d2124d98a472e2d7ed43d893cb03612e5b485d5ba6cc5b8f3b6df64b29(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39dde61ab1d0b2c22580ab951e88de2d0b68717834d5515e24f5f5cf289c7a2f(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49c7678b26d40300064092996443fce86a609707b0da62a8b5b29d8058a367e8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__461399be1f0fe04633dc50dad9516e2d9c7a057f15d910f52b18d73f098c98fc(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d7c33965955e711ac5d83d41c4c6846f9c990d197ba39fae8e77a5aaac4e09b(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ba328e76c57024d4c7aaba9e71e1a140e29953e796b4222d0d5cb4b1925212e(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerUserProfileUserSettingsRSessionAppSettingsCustomImage]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f3a1f6a6704046b278b67a5bd95960cf6bd11f88e6b53bbc2bf586f80436be2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e4cda8886f78838067eebf975aef0adb5e5fcc8b93819db6c46aba600c647e1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__763f0bf2d169d8f2b1e98521a3901f6d0ecbb72615db6199e01819eb5db62e00(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c763070e4c4ca574d519593dc8467be681ae66f6ebe0545c0ee58d7f1a187c1(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6deca565b3083d1b1f0788108ec0678b6fde06f6ae05317482521bff131a58a(
    value: typing.Optional[typing.Union[SagemakerUserProfileUserSettingsRSessionAppSettingsCustomImage, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec7b40e124ec3583b199b405a75b1f3f0310d906a14156be1f0d538bf9f6f401(
    *,
    instance_type: typing.Optional[builtins.str] = None,
    lifecycle_config_arn: typing.Optional[builtins.str] = None,
    sagemaker_image_arn: typing.Optional[builtins.str] = None,
    sagemaker_image_version_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f0575430b5b2e83594ea329c61aa8e90b0451dc6d1b287bfa5bb6872a5e6b60(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2bcc96e38a6b57d9e61b3723be5ed532e1973bf6012c41ee959eb931463934ab(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8a3fa47e8c338146451d9f1fd6983a0caf1d7957824a64827ce27ac91fdaaa7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d64ef0730db40bad386ff2eb499e7469cc30c3e1caa3a7213b601f87ad8b5807(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2415d512337376730038d66c0e369a1c6f54617c6d2b90d07233ed78cf58d74(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__890000032619ec7cd7f5c6be20d91a59e48cf8cb309a9b508de3a1ee81e639c1(
    value: typing.Optional[SagemakerUserProfileUserSettingsRSessionAppSettingsDefaultResourceSpec],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44a643204443c0d1a0654f9762ed40a68efef186a8a31b31976a12a03e506120(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54fc407bd22fb507e5b6d027f2ca1cc2395b7b11fae8c8f7de0282ee357eb4da(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerUserProfileUserSettingsRSessionAppSettingsCustomImage, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f033f31c1d9d63a298ca056292d7deb98489b0baf2f5832bbd6065f57359a69a(
    value: typing.Optional[SagemakerUserProfileUserSettingsRSessionAppSettings],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c670df9fb49d4ba8edabed0a2391809bddb6ecf89563b4369669b5da1786b7f0(
    *,
    notebook_output_option: typing.Optional[builtins.str] = None,
    s3_kms_key_id: typing.Optional[builtins.str] = None,
    s3_output_path: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f8916c8ea93b66bb13bf9cbb94796572806c7b7fa6a71f097bbab44d983b95a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aeb803a1eb0537e178312aec98bf49d3799e25776f64bc51f84da5d057767f58(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__944fb1d453419777b5ed7be9ef6276e4a101f6980b0940c8f4e17fbe3d74769b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec1446063e71b73984ae53acdec6127e2f46da2afa81736e41d87e770106a72b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c79b09548a50aaf1b617ed5d402dec09fd56f767671f5dcb35fac86db522b5a9(
    value: typing.Optional[SagemakerUserProfileUserSettingsSharingSettings],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d042887c89681349a407a7c56d1db06bb1a37a1e347c5f6e020b260a0d6f460e(
    *,
    default_resource_spec: typing.Union[SagemakerUserProfileUserSettingsTensorBoardAppSettingsDefaultResourceSpec, typing.Dict[builtins.str, typing.Any]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6471adfa33d4489ed7646aac01752ebb8cc3f799856a34e0aa52457e9ebf52d6(
    *,
    instance_type: typing.Optional[builtins.str] = None,
    lifecycle_config_arn: typing.Optional[builtins.str] = None,
    sagemaker_image_arn: typing.Optional[builtins.str] = None,
    sagemaker_image_version_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f93023bf4003d35b381687c59a1f710e25179b87779c7f481d7e5fb1882167bc(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__860e56164b3d739f9f84926f783975e03fa0625e55a96b1bebe17427088b41a2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__350c1495f1a9dc24b35421322ecdaedcff933926ae0b7579b45961e57994e5fb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__781d70e60663336d831ba58d813d1ac8aac4357c80f0a034bad531421a980486(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52159f5de86ad154189be3ee5d977cf170e28c040f96af1234cce753be73e272(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7305a30990c4a1c5ed404f4ed89ceca1cf4ef0527a0e04cdd3f5a8e5b9c4db7c(
    value: typing.Optional[SagemakerUserProfileUserSettingsTensorBoardAppSettingsDefaultResourceSpec],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14957314c3a4d6ee856cad43fed4aaecd93c1b94983432431fc92fce420bb548(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb9ce70cdb7515db33d8a364317adaac407c4887a717f70e88fbf5bf179c3288(
    value: typing.Optional[SagemakerUserProfileUserSettingsTensorBoardAppSettings],
) -> None:
    """Type checking stubs"""
    pass
