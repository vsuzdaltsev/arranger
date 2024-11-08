'''
# `aws_emr_studio`

Refer to the Terraform Registory for docs: [`aws_emr_studio`](https://www.terraform.io/docs/providers/aws/r/emr_studio).
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


class EmrStudio(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.emrStudio.EmrStudio",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/emr_studio aws_emr_studio}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        auth_mode: builtins.str,
        default_s3_location: builtins.str,
        engine_security_group_id: builtins.str,
        name: builtins.str,
        service_role: builtins.str,
        subnet_ids: typing.Sequence[builtins.str],
        vpc_id: builtins.str,
        workspace_security_group_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        idp_auth_url: typing.Optional[builtins.str] = None,
        idp_relay_state_parameter_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        user_role: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/emr_studio aws_emr_studio} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param auth_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_studio#auth_mode EmrStudio#auth_mode}.
        :param default_s3_location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_studio#default_s3_location EmrStudio#default_s3_location}.
        :param engine_security_group_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_studio#engine_security_group_id EmrStudio#engine_security_group_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_studio#name EmrStudio#name}.
        :param service_role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_studio#service_role EmrStudio#service_role}.
        :param subnet_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_studio#subnet_ids EmrStudio#subnet_ids}.
        :param vpc_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_studio#vpc_id EmrStudio#vpc_id}.
        :param workspace_security_group_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_studio#workspace_security_group_id EmrStudio#workspace_security_group_id}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_studio#description EmrStudio#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_studio#id EmrStudio#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param idp_auth_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_studio#idp_auth_url EmrStudio#idp_auth_url}.
        :param idp_relay_state_parameter_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_studio#idp_relay_state_parameter_name EmrStudio#idp_relay_state_parameter_name}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_studio#tags EmrStudio#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_studio#tags_all EmrStudio#tags_all}.
        :param user_role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_studio#user_role EmrStudio#user_role}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b90b77af43b9f5ea85bc5b0edc85e86eb9c0c9e8021abcc2b1c12cbcaf7099c0)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = EmrStudioConfig(
            auth_mode=auth_mode,
            default_s3_location=default_s3_location,
            engine_security_group_id=engine_security_group_id,
            name=name,
            service_role=service_role,
            subnet_ids=subnet_ids,
            vpc_id=vpc_id,
            workspace_security_group_id=workspace_security_group_id,
            description=description,
            id=id,
            idp_auth_url=idp_auth_url,
            idp_relay_state_parameter_name=idp_relay_state_parameter_name,
            tags=tags,
            tags_all=tags_all,
            user_role=user_role,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIdpAuthUrl")
    def reset_idp_auth_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdpAuthUrl", []))

    @jsii.member(jsii_name="resetIdpRelayStateParameterName")
    def reset_idp_relay_state_parameter_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdpRelayStateParameterName", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetUserRole")
    def reset_user_role(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserRole", []))

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
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @builtins.property
    @jsii.member(jsii_name="authModeInput")
    def auth_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authModeInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultS3LocationInput")
    def default_s3_location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultS3LocationInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="engineSecurityGroupIdInput")
    def engine_security_group_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "engineSecurityGroupIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="idpAuthUrlInput")
    def idp_auth_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idpAuthUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="idpRelayStateParameterNameInput")
    def idp_relay_state_parameter_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idpRelayStateParameterNameInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceRoleInput")
    def service_role_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceRoleInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetIdsInput")
    def subnet_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "subnetIdsInput"))

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
    @jsii.member(jsii_name="userRoleInput")
    def user_role_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userRoleInput"))

    @builtins.property
    @jsii.member(jsii_name="vpcIdInput")
    def vpc_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vpcIdInput"))

    @builtins.property
    @jsii.member(jsii_name="workspaceSecurityGroupIdInput")
    def workspace_security_group_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "workspaceSecurityGroupIdInput"))

    @builtins.property
    @jsii.member(jsii_name="authMode")
    def auth_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authMode"))

    @auth_mode.setter
    def auth_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e9cb4f2bf157fe47f60b092b41d9c1173ecf8959dfca750ab70013ef49299b0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authMode", value)

    @builtins.property
    @jsii.member(jsii_name="defaultS3Location")
    def default_s3_location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultS3Location"))

    @default_s3_location.setter
    def default_s3_location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3eb904a3c5648bfa6e05d90a39ca0ae46d29b68e280634eaf2fd9ed8310bf38)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultS3Location", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__119df41ff7e060f9f655964f35913087a9bd1b829ba2be520bf304ffcb657974)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="engineSecurityGroupId")
    def engine_security_group_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "engineSecurityGroupId"))

    @engine_security_group_id.setter
    def engine_security_group_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5080e9f404383e8b3678d281229586be9d090920535f8adc0978b1fe9edb2b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "engineSecurityGroupId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9de2cad629b8fd9b5a002c821a30bc6b01b37705b48acda5a91d5dd29984d024)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="idpAuthUrl")
    def idp_auth_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "idpAuthUrl"))

    @idp_auth_url.setter
    def idp_auth_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f81342e3182f5a605acee7e94333bcc3f626422aa6869d9880a58960bbcab87)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "idpAuthUrl", value)

    @builtins.property
    @jsii.member(jsii_name="idpRelayStateParameterName")
    def idp_relay_state_parameter_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "idpRelayStateParameterName"))

    @idp_relay_state_parameter_name.setter
    def idp_relay_state_parameter_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cbca01357b6cc6a9066fdd3e303de6572c4e14415d1249627628b269dd9918f5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "idpRelayStateParameterName", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4c8b253aea6bb0a0d0575ca4d1e08783e5ab52dba7015d4cc053031c36035ef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="serviceRole")
    def service_role(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceRole"))

    @service_role.setter
    def service_role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91a553cc30e13b9f19e01452fbd01976e04596a897b524e0fa704e49bf23d899)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceRole", value)

    @builtins.property
    @jsii.member(jsii_name="subnetIds")
    def subnet_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subnetIds"))

    @subnet_ids.setter
    def subnet_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aeb845b5e491d506bdda94827b0feb32343b2d4145ab5fce5a2bad739bd8b573)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetIds", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e9da980e40cc7797495de2ac5170e9684bb18ecf5982029481c4b3951cc35ff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f7d58c71fbbbd11dd2a6892733c37c137c85c090766124a0f36024295db7c239)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)

    @builtins.property
    @jsii.member(jsii_name="userRole")
    def user_role(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userRole"))

    @user_role.setter
    def user_role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94e6f558c5be9d795bc0a3b4c7785f0a5788a7e84d70b9b30bd73f778682aa3f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userRole", value)

    @builtins.property
    @jsii.member(jsii_name="vpcId")
    def vpc_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vpcId"))

    @vpc_id.setter
    def vpc_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00a170b69c912748f96cb0d92c3779bea7ce29e9156ba73ecdcb6ef82c5c32b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcId", value)

    @builtins.property
    @jsii.member(jsii_name="workspaceSecurityGroupId")
    def workspace_security_group_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "workspaceSecurityGroupId"))

    @workspace_security_group_id.setter
    def workspace_security_group_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7104e0dd61044eeb2f1d26ce776954331f2afa2d8fbbe5fcef338097cd8c815)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workspaceSecurityGroupId", value)


@jsii.data_type(
    jsii_type="aws.emrStudio.EmrStudioConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "auth_mode": "authMode",
        "default_s3_location": "defaultS3Location",
        "engine_security_group_id": "engineSecurityGroupId",
        "name": "name",
        "service_role": "serviceRole",
        "subnet_ids": "subnetIds",
        "vpc_id": "vpcId",
        "workspace_security_group_id": "workspaceSecurityGroupId",
        "description": "description",
        "id": "id",
        "idp_auth_url": "idpAuthUrl",
        "idp_relay_state_parameter_name": "idpRelayStateParameterName",
        "tags": "tags",
        "tags_all": "tagsAll",
        "user_role": "userRole",
    },
)
class EmrStudioConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        auth_mode: builtins.str,
        default_s3_location: builtins.str,
        engine_security_group_id: builtins.str,
        name: builtins.str,
        service_role: builtins.str,
        subnet_ids: typing.Sequence[builtins.str],
        vpc_id: builtins.str,
        workspace_security_group_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        idp_auth_url: typing.Optional[builtins.str] = None,
        idp_relay_state_parameter_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        user_role: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param auth_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_studio#auth_mode EmrStudio#auth_mode}.
        :param default_s3_location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_studio#default_s3_location EmrStudio#default_s3_location}.
        :param engine_security_group_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_studio#engine_security_group_id EmrStudio#engine_security_group_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_studio#name EmrStudio#name}.
        :param service_role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_studio#service_role EmrStudio#service_role}.
        :param subnet_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_studio#subnet_ids EmrStudio#subnet_ids}.
        :param vpc_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_studio#vpc_id EmrStudio#vpc_id}.
        :param workspace_security_group_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_studio#workspace_security_group_id EmrStudio#workspace_security_group_id}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_studio#description EmrStudio#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_studio#id EmrStudio#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param idp_auth_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_studio#idp_auth_url EmrStudio#idp_auth_url}.
        :param idp_relay_state_parameter_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_studio#idp_relay_state_parameter_name EmrStudio#idp_relay_state_parameter_name}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_studio#tags EmrStudio#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_studio#tags_all EmrStudio#tags_all}.
        :param user_role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_studio#user_role EmrStudio#user_role}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4accb5e2df1cd6a18711ed6e4181012a4b1849f35ac7fc9352ac9965d471c5b)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument auth_mode", value=auth_mode, expected_type=type_hints["auth_mode"])
            check_type(argname="argument default_s3_location", value=default_s3_location, expected_type=type_hints["default_s3_location"])
            check_type(argname="argument engine_security_group_id", value=engine_security_group_id, expected_type=type_hints["engine_security_group_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument service_role", value=service_role, expected_type=type_hints["service_role"])
            check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
            check_type(argname="argument vpc_id", value=vpc_id, expected_type=type_hints["vpc_id"])
            check_type(argname="argument workspace_security_group_id", value=workspace_security_group_id, expected_type=type_hints["workspace_security_group_id"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument idp_auth_url", value=idp_auth_url, expected_type=type_hints["idp_auth_url"])
            check_type(argname="argument idp_relay_state_parameter_name", value=idp_relay_state_parameter_name, expected_type=type_hints["idp_relay_state_parameter_name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument user_role", value=user_role, expected_type=type_hints["user_role"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "auth_mode": auth_mode,
            "default_s3_location": default_s3_location,
            "engine_security_group_id": engine_security_group_id,
            "name": name,
            "service_role": service_role,
            "subnet_ids": subnet_ids,
            "vpc_id": vpc_id,
            "workspace_security_group_id": workspace_security_group_id,
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
        if idp_auth_url is not None:
            self._values["idp_auth_url"] = idp_auth_url
        if idp_relay_state_parameter_name is not None:
            self._values["idp_relay_state_parameter_name"] = idp_relay_state_parameter_name
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if user_role is not None:
            self._values["user_role"] = user_role

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
    def auth_mode(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_studio#auth_mode EmrStudio#auth_mode}.'''
        result = self._values.get("auth_mode")
        assert result is not None, "Required property 'auth_mode' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def default_s3_location(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_studio#default_s3_location EmrStudio#default_s3_location}.'''
        result = self._values.get("default_s3_location")
        assert result is not None, "Required property 'default_s3_location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def engine_security_group_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_studio#engine_security_group_id EmrStudio#engine_security_group_id}.'''
        result = self._values.get("engine_security_group_id")
        assert result is not None, "Required property 'engine_security_group_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_studio#name EmrStudio#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_role(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_studio#service_role EmrStudio#service_role}.'''
        result = self._values.get("service_role")
        assert result is not None, "Required property 'service_role' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subnet_ids(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_studio#subnet_ids EmrStudio#subnet_ids}.'''
        result = self._values.get("subnet_ids")
        assert result is not None, "Required property 'subnet_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def vpc_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_studio#vpc_id EmrStudio#vpc_id}.'''
        result = self._values.get("vpc_id")
        assert result is not None, "Required property 'vpc_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def workspace_security_group_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_studio#workspace_security_group_id EmrStudio#workspace_security_group_id}.'''
        result = self._values.get("workspace_security_group_id")
        assert result is not None, "Required property 'workspace_security_group_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_studio#description EmrStudio#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_studio#id EmrStudio#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def idp_auth_url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_studio#idp_auth_url EmrStudio#idp_auth_url}.'''
        result = self._values.get("idp_auth_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def idp_relay_state_parameter_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_studio#idp_relay_state_parameter_name EmrStudio#idp_relay_state_parameter_name}.'''
        result = self._values.get("idp_relay_state_parameter_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_studio#tags EmrStudio#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_studio#tags_all EmrStudio#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def user_role(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_studio#user_role EmrStudio#user_role}.'''
        result = self._values.get("user_role")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmrStudioConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "EmrStudio",
    "EmrStudioConfig",
]

publication.publish()

def _typecheckingstub__b90b77af43b9f5ea85bc5b0edc85e86eb9c0c9e8021abcc2b1c12cbcaf7099c0(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    auth_mode: builtins.str,
    default_s3_location: builtins.str,
    engine_security_group_id: builtins.str,
    name: builtins.str,
    service_role: builtins.str,
    subnet_ids: typing.Sequence[builtins.str],
    vpc_id: builtins.str,
    workspace_security_group_id: builtins.str,
    description: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    idp_auth_url: typing.Optional[builtins.str] = None,
    idp_relay_state_parameter_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    user_role: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__9e9cb4f2bf157fe47f60b092b41d9c1173ecf8959dfca750ab70013ef49299b0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3eb904a3c5648bfa6e05d90a39ca0ae46d29b68e280634eaf2fd9ed8310bf38(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__119df41ff7e060f9f655964f35913087a9bd1b829ba2be520bf304ffcb657974(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5080e9f404383e8b3678d281229586be9d090920535f8adc0978b1fe9edb2b8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9de2cad629b8fd9b5a002c821a30bc6b01b37705b48acda5a91d5dd29984d024(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f81342e3182f5a605acee7e94333bcc3f626422aa6869d9880a58960bbcab87(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cbca01357b6cc6a9066fdd3e303de6572c4e14415d1249627628b269dd9918f5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4c8b253aea6bb0a0d0575ca4d1e08783e5ab52dba7015d4cc053031c36035ef(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91a553cc30e13b9f19e01452fbd01976e04596a897b524e0fa704e49bf23d899(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aeb845b5e491d506bdda94827b0feb32343b2d4145ab5fce5a2bad739bd8b573(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e9da980e40cc7797495de2ac5170e9684bb18ecf5982029481c4b3951cc35ff(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7d58c71fbbbd11dd2a6892733c37c137c85c090766124a0f36024295db7c239(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94e6f558c5be9d795bc0a3b4c7785f0a5788a7e84d70b9b30bd73f778682aa3f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00a170b69c912748f96cb0d92c3779bea7ce29e9156ba73ecdcb6ef82c5c32b6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7104e0dd61044eeb2f1d26ce776954331f2afa2d8fbbe5fcef338097cd8c815(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4accb5e2df1cd6a18711ed6e4181012a4b1849f35ac7fc9352ac9965d471c5b(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    auth_mode: builtins.str,
    default_s3_location: builtins.str,
    engine_security_group_id: builtins.str,
    name: builtins.str,
    service_role: builtins.str,
    subnet_ids: typing.Sequence[builtins.str],
    vpc_id: builtins.str,
    workspace_security_group_id: builtins.str,
    description: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    idp_auth_url: typing.Optional[builtins.str] = None,
    idp_relay_state_parameter_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    user_role: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
