'''
# `aws_connect_user`

Refer to the Terraform Registory for docs: [`aws_connect_user`](https://www.terraform.io/docs/providers/aws/r/connect_user).
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


class ConnectUser(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.connectUser.ConnectUser",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/connect_user aws_connect_user}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        instance_id: builtins.str,
        name: builtins.str,
        phone_config: typing.Union["ConnectUserPhoneConfig", typing.Dict[builtins.str, typing.Any]],
        routing_profile_id: builtins.str,
        security_profile_ids: typing.Sequence[builtins.str],
        directory_user_id: typing.Optional[builtins.str] = None,
        hierarchy_group_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        identity_info: typing.Optional[typing.Union["ConnectUserIdentityInfo", typing.Dict[builtins.str, typing.Any]]] = None,
        password: typing.Optional[builtins.str] = None,
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
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/connect_user aws_connect_user} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param instance_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user#instance_id ConnectUser#instance_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user#name ConnectUser#name}.
        :param phone_config: phone_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user#phone_config ConnectUser#phone_config}
        :param routing_profile_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user#routing_profile_id ConnectUser#routing_profile_id}.
        :param security_profile_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user#security_profile_ids ConnectUser#security_profile_ids}.
        :param directory_user_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user#directory_user_id ConnectUser#directory_user_id}.
        :param hierarchy_group_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user#hierarchy_group_id ConnectUser#hierarchy_group_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user#id ConnectUser#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identity_info: identity_info block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user#identity_info ConnectUser#identity_info}
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user#password ConnectUser#password}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user#tags ConnectUser#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user#tags_all ConnectUser#tags_all}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9526f9fd092f333eb6195c962ea8580b546434eedc1767d604ddf2dfae3a807)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ConnectUserConfig(
            instance_id=instance_id,
            name=name,
            phone_config=phone_config,
            routing_profile_id=routing_profile_id,
            security_profile_ids=security_profile_ids,
            directory_user_id=directory_user_id,
            hierarchy_group_id=hierarchy_group_id,
            id=id,
            identity_info=identity_info,
            password=password,
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

    @jsii.member(jsii_name="putIdentityInfo")
    def put_identity_info(
        self,
        *,
        email: typing.Optional[builtins.str] = None,
        first_name: typing.Optional[builtins.str] = None,
        last_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param email: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user#email ConnectUser#email}.
        :param first_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user#first_name ConnectUser#first_name}.
        :param last_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user#last_name ConnectUser#last_name}.
        '''
        value = ConnectUserIdentityInfo(
            email=email, first_name=first_name, last_name=last_name
        )

        return typing.cast(None, jsii.invoke(self, "putIdentityInfo", [value]))

    @jsii.member(jsii_name="putPhoneConfig")
    def put_phone_config(
        self,
        *,
        phone_type: builtins.str,
        after_contact_work_time_limit: typing.Optional[jsii.Number] = None,
        auto_accept: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        desk_phone_number: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param phone_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user#phone_type ConnectUser#phone_type}.
        :param after_contact_work_time_limit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user#after_contact_work_time_limit ConnectUser#after_contact_work_time_limit}.
        :param auto_accept: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user#auto_accept ConnectUser#auto_accept}.
        :param desk_phone_number: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user#desk_phone_number ConnectUser#desk_phone_number}.
        '''
        value = ConnectUserPhoneConfig(
            phone_type=phone_type,
            after_contact_work_time_limit=after_contact_work_time_limit,
            auto_accept=auto_accept,
            desk_phone_number=desk_phone_number,
        )

        return typing.cast(None, jsii.invoke(self, "putPhoneConfig", [value]))

    @jsii.member(jsii_name="resetDirectoryUserId")
    def reset_directory_user_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDirectoryUserId", []))

    @jsii.member(jsii_name="resetHierarchyGroupId")
    def reset_hierarchy_group_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHierarchyGroupId", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIdentityInfo")
    def reset_identity_info(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentityInfo", []))

    @jsii.member(jsii_name="resetPassword")
    def reset_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassword", []))

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
    @jsii.member(jsii_name="identityInfo")
    def identity_info(self) -> "ConnectUserIdentityInfoOutputReference":
        return typing.cast("ConnectUserIdentityInfoOutputReference", jsii.get(self, "identityInfo"))

    @builtins.property
    @jsii.member(jsii_name="phoneConfig")
    def phone_config(self) -> "ConnectUserPhoneConfigOutputReference":
        return typing.cast("ConnectUserPhoneConfigOutputReference", jsii.get(self, "phoneConfig"))

    @builtins.property
    @jsii.member(jsii_name="userId")
    def user_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userId"))

    @builtins.property
    @jsii.member(jsii_name="directoryUserIdInput")
    def directory_user_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "directoryUserIdInput"))

    @builtins.property
    @jsii.member(jsii_name="hierarchyGroupIdInput")
    def hierarchy_group_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hierarchyGroupIdInput"))

    @builtins.property
    @jsii.member(jsii_name="identityInfoInput")
    def identity_info_input(self) -> typing.Optional["ConnectUserIdentityInfo"]:
        return typing.cast(typing.Optional["ConnectUserIdentityInfo"], jsii.get(self, "identityInfoInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceIdInput")
    def instance_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="phoneConfigInput")
    def phone_config_input(self) -> typing.Optional["ConnectUserPhoneConfig"]:
        return typing.cast(typing.Optional["ConnectUserPhoneConfig"], jsii.get(self, "phoneConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="routingProfileIdInput")
    def routing_profile_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "routingProfileIdInput"))

    @builtins.property
    @jsii.member(jsii_name="securityProfileIdsInput")
    def security_profile_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityProfileIdsInput"))

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
    @jsii.member(jsii_name="directoryUserId")
    def directory_user_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "directoryUserId"))

    @directory_user_id.setter
    def directory_user_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50105c91ce3ada7ab4f6fe9cfb25bf8404fa13440148bd0d869cdee9da10a547)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "directoryUserId", value)

    @builtins.property
    @jsii.member(jsii_name="hierarchyGroupId")
    def hierarchy_group_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hierarchyGroupId"))

    @hierarchy_group_id.setter
    def hierarchy_group_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc6d8b76a601fcb456a9c309440a199aa832dd2777ce2eeb3db024433cf59a0d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hierarchyGroupId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ea4cdeeef25945c1ebb1d1d61fbe1d96f6c90c97efa43cdb020fcf0408dd031)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="instanceId")
    def instance_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceId"))

    @instance_id.setter
    def instance_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6be9d169066a46855d121e31f5a2dd67e553883f3dcbe96948c7353d39238fc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceId", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f69c0b982c540d40d183aa481c10a3fa148d26bc41540c8352ad317ca96a7c0a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9eb524ec48e04c201eb4a1625802511ffdf113583bbc6a9e7fbe6604875708c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="routingProfileId")
    def routing_profile_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "routingProfileId"))

    @routing_profile_id.setter
    def routing_profile_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45c16316645a58bafda966ac887cbb3941e803ab8cd85086f6a342384455e0c4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "routingProfileId", value)

    @builtins.property
    @jsii.member(jsii_name="securityProfileIds")
    def security_profile_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "securityProfileIds"))

    @security_profile_ids.setter
    def security_profile_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9281fbca467c405da2f9aa34ac090cedebdc956d90be66b582acaeeb8f71e39f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityProfileIds", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9cf8a56bee9bc0c8be065e8d0268f8563e0be5e46389e94cb1cbaddd35d3be71)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__48387d34dc6a668a3767dac8e84b2df22b9721c20255a285c2acf474fac812e2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)


@jsii.data_type(
    jsii_type="aws.connectUser.ConnectUserConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "instance_id": "instanceId",
        "name": "name",
        "phone_config": "phoneConfig",
        "routing_profile_id": "routingProfileId",
        "security_profile_ids": "securityProfileIds",
        "directory_user_id": "directoryUserId",
        "hierarchy_group_id": "hierarchyGroupId",
        "id": "id",
        "identity_info": "identityInfo",
        "password": "password",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class ConnectUserConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        instance_id: builtins.str,
        name: builtins.str,
        phone_config: typing.Union["ConnectUserPhoneConfig", typing.Dict[builtins.str, typing.Any]],
        routing_profile_id: builtins.str,
        security_profile_ids: typing.Sequence[builtins.str],
        directory_user_id: typing.Optional[builtins.str] = None,
        hierarchy_group_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        identity_info: typing.Optional[typing.Union["ConnectUserIdentityInfo", typing.Dict[builtins.str, typing.Any]]] = None,
        password: typing.Optional[builtins.str] = None,
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
        :param instance_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user#instance_id ConnectUser#instance_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user#name ConnectUser#name}.
        :param phone_config: phone_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user#phone_config ConnectUser#phone_config}
        :param routing_profile_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user#routing_profile_id ConnectUser#routing_profile_id}.
        :param security_profile_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user#security_profile_ids ConnectUser#security_profile_ids}.
        :param directory_user_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user#directory_user_id ConnectUser#directory_user_id}.
        :param hierarchy_group_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user#hierarchy_group_id ConnectUser#hierarchy_group_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user#id ConnectUser#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identity_info: identity_info block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user#identity_info ConnectUser#identity_info}
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user#password ConnectUser#password}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user#tags ConnectUser#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user#tags_all ConnectUser#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(phone_config, dict):
            phone_config = ConnectUserPhoneConfig(**phone_config)
        if isinstance(identity_info, dict):
            identity_info = ConnectUserIdentityInfo(**identity_info)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3cda3eac9f3195dbdc76dfa6e28b176ce4938e107317c843976b4b9d4673ff7)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument instance_id", value=instance_id, expected_type=type_hints["instance_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument phone_config", value=phone_config, expected_type=type_hints["phone_config"])
            check_type(argname="argument routing_profile_id", value=routing_profile_id, expected_type=type_hints["routing_profile_id"])
            check_type(argname="argument security_profile_ids", value=security_profile_ids, expected_type=type_hints["security_profile_ids"])
            check_type(argname="argument directory_user_id", value=directory_user_id, expected_type=type_hints["directory_user_id"])
            check_type(argname="argument hierarchy_group_id", value=hierarchy_group_id, expected_type=type_hints["hierarchy_group_id"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument identity_info", value=identity_info, expected_type=type_hints["identity_info"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "instance_id": instance_id,
            "name": name,
            "phone_config": phone_config,
            "routing_profile_id": routing_profile_id,
            "security_profile_ids": security_profile_ids,
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
        if directory_user_id is not None:
            self._values["directory_user_id"] = directory_user_id
        if hierarchy_group_id is not None:
            self._values["hierarchy_group_id"] = hierarchy_group_id
        if id is not None:
            self._values["id"] = id
        if identity_info is not None:
            self._values["identity_info"] = identity_info
        if password is not None:
            self._values["password"] = password
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
    def instance_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user#instance_id ConnectUser#instance_id}.'''
        result = self._values.get("instance_id")
        assert result is not None, "Required property 'instance_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user#name ConnectUser#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def phone_config(self) -> "ConnectUserPhoneConfig":
        '''phone_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user#phone_config ConnectUser#phone_config}
        '''
        result = self._values.get("phone_config")
        assert result is not None, "Required property 'phone_config' is missing"
        return typing.cast("ConnectUserPhoneConfig", result)

    @builtins.property
    def routing_profile_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user#routing_profile_id ConnectUser#routing_profile_id}.'''
        result = self._values.get("routing_profile_id")
        assert result is not None, "Required property 'routing_profile_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def security_profile_ids(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user#security_profile_ids ConnectUser#security_profile_ids}.'''
        result = self._values.get("security_profile_ids")
        assert result is not None, "Required property 'security_profile_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def directory_user_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user#directory_user_id ConnectUser#directory_user_id}.'''
        result = self._values.get("directory_user_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def hierarchy_group_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user#hierarchy_group_id ConnectUser#hierarchy_group_id}.'''
        result = self._values.get("hierarchy_group_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user#id ConnectUser#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def identity_info(self) -> typing.Optional["ConnectUserIdentityInfo"]:
        '''identity_info block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user#identity_info ConnectUser#identity_info}
        '''
        result = self._values.get("identity_info")
        return typing.cast(typing.Optional["ConnectUserIdentityInfo"], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user#password ConnectUser#password}.'''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user#tags ConnectUser#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user#tags_all ConnectUser#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConnectUserConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.connectUser.ConnectUserIdentityInfo",
    jsii_struct_bases=[],
    name_mapping={
        "email": "email",
        "first_name": "firstName",
        "last_name": "lastName",
    },
)
class ConnectUserIdentityInfo:
    def __init__(
        self,
        *,
        email: typing.Optional[builtins.str] = None,
        first_name: typing.Optional[builtins.str] = None,
        last_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param email: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user#email ConnectUser#email}.
        :param first_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user#first_name ConnectUser#first_name}.
        :param last_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user#last_name ConnectUser#last_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f992e08476b1ab7bab109d152c2cddfc6efd8d74236e748aaa9344d5d6e508e9)
            check_type(argname="argument email", value=email, expected_type=type_hints["email"])
            check_type(argname="argument first_name", value=first_name, expected_type=type_hints["first_name"])
            check_type(argname="argument last_name", value=last_name, expected_type=type_hints["last_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if email is not None:
            self._values["email"] = email
        if first_name is not None:
            self._values["first_name"] = first_name
        if last_name is not None:
            self._values["last_name"] = last_name

    @builtins.property
    def email(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user#email ConnectUser#email}.'''
        result = self._values.get("email")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def first_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user#first_name ConnectUser#first_name}.'''
        result = self._values.get("first_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def last_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user#last_name ConnectUser#last_name}.'''
        result = self._values.get("last_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConnectUserIdentityInfo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ConnectUserIdentityInfoOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.connectUser.ConnectUserIdentityInfoOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3075a924f4c5be656972c099810bbe0465f6d7fce977d8ee5d8b2c5294df0c5a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEmail")
    def reset_email(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmail", []))

    @jsii.member(jsii_name="resetFirstName")
    def reset_first_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFirstName", []))

    @jsii.member(jsii_name="resetLastName")
    def reset_last_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLastName", []))

    @builtins.property
    @jsii.member(jsii_name="emailInput")
    def email_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "emailInput"))

    @builtins.property
    @jsii.member(jsii_name="firstNameInput")
    def first_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "firstNameInput"))

    @builtins.property
    @jsii.member(jsii_name="lastNameInput")
    def last_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lastNameInput"))

    @builtins.property
    @jsii.member(jsii_name="email")
    def email(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "email"))

    @email.setter
    def email(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1883c2eb8d79e2569af6a37b031d3842edf8ddbbc2a9abc386b03f90d408c7c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "email", value)

    @builtins.property
    @jsii.member(jsii_name="firstName")
    def first_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "firstName"))

    @first_name.setter
    def first_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49937c1ae14df82f4dad8d41adc94905b02d3734f78f363e6f0c96c20569d501)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "firstName", value)

    @builtins.property
    @jsii.member(jsii_name="lastName")
    def last_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastName"))

    @last_name.setter
    def last_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd0fdab54f7262bf5c2b21270870e872ebccd163c63bfb4bc7d27c1d3f07f728)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lastName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ConnectUserIdentityInfo]:
        return typing.cast(typing.Optional[ConnectUserIdentityInfo], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ConnectUserIdentityInfo]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__86f50a4d21c94ae7342fee6c22d07e1d9d2172aa2c0ee5725a64cfcea659be25)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.connectUser.ConnectUserPhoneConfig",
    jsii_struct_bases=[],
    name_mapping={
        "phone_type": "phoneType",
        "after_contact_work_time_limit": "afterContactWorkTimeLimit",
        "auto_accept": "autoAccept",
        "desk_phone_number": "deskPhoneNumber",
    },
)
class ConnectUserPhoneConfig:
    def __init__(
        self,
        *,
        phone_type: builtins.str,
        after_contact_work_time_limit: typing.Optional[jsii.Number] = None,
        auto_accept: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        desk_phone_number: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param phone_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user#phone_type ConnectUser#phone_type}.
        :param after_contact_work_time_limit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user#after_contact_work_time_limit ConnectUser#after_contact_work_time_limit}.
        :param auto_accept: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user#auto_accept ConnectUser#auto_accept}.
        :param desk_phone_number: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user#desk_phone_number ConnectUser#desk_phone_number}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4826c73e9e12aa1adbf658460e23bd5c2e83ed95cefc088114d4cdd423b72fa6)
            check_type(argname="argument phone_type", value=phone_type, expected_type=type_hints["phone_type"])
            check_type(argname="argument after_contact_work_time_limit", value=after_contact_work_time_limit, expected_type=type_hints["after_contact_work_time_limit"])
            check_type(argname="argument auto_accept", value=auto_accept, expected_type=type_hints["auto_accept"])
            check_type(argname="argument desk_phone_number", value=desk_phone_number, expected_type=type_hints["desk_phone_number"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "phone_type": phone_type,
        }
        if after_contact_work_time_limit is not None:
            self._values["after_contact_work_time_limit"] = after_contact_work_time_limit
        if auto_accept is not None:
            self._values["auto_accept"] = auto_accept
        if desk_phone_number is not None:
            self._values["desk_phone_number"] = desk_phone_number

    @builtins.property
    def phone_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user#phone_type ConnectUser#phone_type}.'''
        result = self._values.get("phone_type")
        assert result is not None, "Required property 'phone_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def after_contact_work_time_limit(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user#after_contact_work_time_limit ConnectUser#after_contact_work_time_limit}.'''
        result = self._values.get("after_contact_work_time_limit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def auto_accept(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user#auto_accept ConnectUser#auto_accept}.'''
        result = self._values.get("auto_accept")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def desk_phone_number(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user#desk_phone_number ConnectUser#desk_phone_number}.'''
        result = self._values.get("desk_phone_number")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConnectUserPhoneConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ConnectUserPhoneConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.connectUser.ConnectUserPhoneConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9246c2afb440d3c69491d6ccefee9fa273b26a6b32cb36207ccee95d120d52aa)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAfterContactWorkTimeLimit")
    def reset_after_contact_work_time_limit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAfterContactWorkTimeLimit", []))

    @jsii.member(jsii_name="resetAutoAccept")
    def reset_auto_accept(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoAccept", []))

    @jsii.member(jsii_name="resetDeskPhoneNumber")
    def reset_desk_phone_number(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeskPhoneNumber", []))

    @builtins.property
    @jsii.member(jsii_name="afterContactWorkTimeLimitInput")
    def after_contact_work_time_limit_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "afterContactWorkTimeLimitInput"))

    @builtins.property
    @jsii.member(jsii_name="autoAcceptInput")
    def auto_accept_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "autoAcceptInput"))

    @builtins.property
    @jsii.member(jsii_name="deskPhoneNumberInput")
    def desk_phone_number_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deskPhoneNumberInput"))

    @builtins.property
    @jsii.member(jsii_name="phoneTypeInput")
    def phone_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "phoneTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="afterContactWorkTimeLimit")
    def after_contact_work_time_limit(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "afterContactWorkTimeLimit"))

    @after_contact_work_time_limit.setter
    def after_contact_work_time_limit(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6800c263d941d941f8a1789543536511abdba8f02c49b504d1c7a81082e6558c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "afterContactWorkTimeLimit", value)

    @builtins.property
    @jsii.member(jsii_name="autoAccept")
    def auto_accept(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "autoAccept"))

    @auto_accept.setter
    def auto_accept(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fadf71df799e6db6f11632f8c8088dad2c3ba45e0008acfbdadc20f59889a298)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoAccept", value)

    @builtins.property
    @jsii.member(jsii_name="deskPhoneNumber")
    def desk_phone_number(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deskPhoneNumber"))

    @desk_phone_number.setter
    def desk_phone_number(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d81f51269679769e64abc233d8bcc63b11dfe6d0583e58cd7d7f067af16d7a09)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deskPhoneNumber", value)

    @builtins.property
    @jsii.member(jsii_name="phoneType")
    def phone_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "phoneType"))

    @phone_type.setter
    def phone_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__934a013c936a3d5c60c7ef29219fef7242f82e613ff68786c8e2803a65124d4e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "phoneType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ConnectUserPhoneConfig]:
        return typing.cast(typing.Optional[ConnectUserPhoneConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ConnectUserPhoneConfig]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c2f77d3a275c68180c32b50e376b1d70af4ca6cd98652f35557aae65259cb577)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ConnectUser",
    "ConnectUserConfig",
    "ConnectUserIdentityInfo",
    "ConnectUserIdentityInfoOutputReference",
    "ConnectUserPhoneConfig",
    "ConnectUserPhoneConfigOutputReference",
]

publication.publish()

def _typecheckingstub__f9526f9fd092f333eb6195c962ea8580b546434eedc1767d604ddf2dfae3a807(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    instance_id: builtins.str,
    name: builtins.str,
    phone_config: typing.Union[ConnectUserPhoneConfig, typing.Dict[builtins.str, typing.Any]],
    routing_profile_id: builtins.str,
    security_profile_ids: typing.Sequence[builtins.str],
    directory_user_id: typing.Optional[builtins.str] = None,
    hierarchy_group_id: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    identity_info: typing.Optional[typing.Union[ConnectUserIdentityInfo, typing.Dict[builtins.str, typing.Any]]] = None,
    password: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__50105c91ce3ada7ab4f6fe9cfb25bf8404fa13440148bd0d869cdee9da10a547(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc6d8b76a601fcb456a9c309440a199aa832dd2777ce2eeb3db024433cf59a0d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ea4cdeeef25945c1ebb1d1d61fbe1d96f6c90c97efa43cdb020fcf0408dd031(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6be9d169066a46855d121e31f5a2dd67e553883f3dcbe96948c7353d39238fc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f69c0b982c540d40d183aa481c10a3fa148d26bc41540c8352ad317ca96a7c0a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9eb524ec48e04c201eb4a1625802511ffdf113583bbc6a9e7fbe6604875708c2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45c16316645a58bafda966ac887cbb3941e803ab8cd85086f6a342384455e0c4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9281fbca467c405da2f9aa34ac090cedebdc956d90be66b582acaeeb8f71e39f(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9cf8a56bee9bc0c8be065e8d0268f8563e0be5e46389e94cb1cbaddd35d3be71(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48387d34dc6a668a3767dac8e84b2df22b9721c20255a285c2acf474fac812e2(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3cda3eac9f3195dbdc76dfa6e28b176ce4938e107317c843976b4b9d4673ff7(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    instance_id: builtins.str,
    name: builtins.str,
    phone_config: typing.Union[ConnectUserPhoneConfig, typing.Dict[builtins.str, typing.Any]],
    routing_profile_id: builtins.str,
    security_profile_ids: typing.Sequence[builtins.str],
    directory_user_id: typing.Optional[builtins.str] = None,
    hierarchy_group_id: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    identity_info: typing.Optional[typing.Union[ConnectUserIdentityInfo, typing.Dict[builtins.str, typing.Any]]] = None,
    password: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f992e08476b1ab7bab109d152c2cddfc6efd8d74236e748aaa9344d5d6e508e9(
    *,
    email: typing.Optional[builtins.str] = None,
    first_name: typing.Optional[builtins.str] = None,
    last_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3075a924f4c5be656972c099810bbe0465f6d7fce977d8ee5d8b2c5294df0c5a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1883c2eb8d79e2569af6a37b031d3842edf8ddbbc2a9abc386b03f90d408c7c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49937c1ae14df82f4dad8d41adc94905b02d3734f78f363e6f0c96c20569d501(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd0fdab54f7262bf5c2b21270870e872ebccd163c63bfb4bc7d27c1d3f07f728(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86f50a4d21c94ae7342fee6c22d07e1d9d2172aa2c0ee5725a64cfcea659be25(
    value: typing.Optional[ConnectUserIdentityInfo],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4826c73e9e12aa1adbf658460e23bd5c2e83ed95cefc088114d4cdd423b72fa6(
    *,
    phone_type: builtins.str,
    after_contact_work_time_limit: typing.Optional[jsii.Number] = None,
    auto_accept: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    desk_phone_number: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9246c2afb440d3c69491d6ccefee9fa273b26a6b32cb36207ccee95d120d52aa(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6800c263d941d941f8a1789543536511abdba8f02c49b504d1c7a81082e6558c(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fadf71df799e6db6f11632f8c8088dad2c3ba45e0008acfbdadc20f59889a298(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d81f51269679769e64abc233d8bcc63b11dfe6d0583e58cd7d7f067af16d7a09(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__934a013c936a3d5c60c7ef29219fef7242f82e613ff68786c8e2803a65124d4e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2f77d3a275c68180c32b50e376b1d70af4ca6cd98652f35557aae65259cb577(
    value: typing.Optional[ConnectUserPhoneConfig],
) -> None:
    """Type checking stubs"""
    pass
