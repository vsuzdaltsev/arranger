'''
# `aws_appstream_stack`

Refer to the Terraform Registory for docs: [`aws_appstream_stack`](https://www.terraform.io/docs/providers/aws/r/appstream_stack).
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


class AppstreamStack(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appstreamStack.AppstreamStack",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/appstream_stack aws_appstream_stack}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        access_endpoints: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["AppstreamStackAccessEndpoints", typing.Dict[builtins.str, typing.Any]]]]] = None,
        application_settings: typing.Optional[typing.Union["AppstreamStackApplicationSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        display_name: typing.Optional[builtins.str] = None,
        embed_host_domains: typing.Optional[typing.Sequence[builtins.str]] = None,
        feedback_url: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        redirect_url: typing.Optional[builtins.str] = None,
        storage_connectors: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["AppstreamStackStorageConnectors", typing.Dict[builtins.str, typing.Any]]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        user_settings: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["AppstreamStackUserSettings", typing.Dict[builtins.str, typing.Any]]]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/appstream_stack aws_appstream_stack} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_stack#name AppstreamStack#name}.
        :param access_endpoints: access_endpoints block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_stack#access_endpoints AppstreamStack#access_endpoints}
        :param application_settings: application_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_stack#application_settings AppstreamStack#application_settings}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_stack#description AppstreamStack#description}.
        :param display_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_stack#display_name AppstreamStack#display_name}.
        :param embed_host_domains: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_stack#embed_host_domains AppstreamStack#embed_host_domains}.
        :param feedback_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_stack#feedback_url AppstreamStack#feedback_url}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_stack#id AppstreamStack#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param redirect_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_stack#redirect_url AppstreamStack#redirect_url}.
        :param storage_connectors: storage_connectors block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_stack#storage_connectors AppstreamStack#storage_connectors}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_stack#tags AppstreamStack#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_stack#tags_all AppstreamStack#tags_all}.
        :param user_settings: user_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_stack#user_settings AppstreamStack#user_settings}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8702ef50c7ab9ad9bf543c164a5a822740175de9a03a7cdb14f8ebce98e207e8)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = AppstreamStackConfig(
            name=name,
            access_endpoints=access_endpoints,
            application_settings=application_settings,
            description=description,
            display_name=display_name,
            embed_host_domains=embed_host_domains,
            feedback_url=feedback_url,
            id=id,
            redirect_url=redirect_url,
            storage_connectors=storage_connectors,
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

    @jsii.member(jsii_name="putAccessEndpoints")
    def put_access_endpoints(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["AppstreamStackAccessEndpoints", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e4e275d5b48b7d37d81086ae9d318969279bcdd58e391b04549a54df5fc3fc2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAccessEndpoints", [value]))

    @jsii.member(jsii_name="putApplicationSettings")
    def put_application_settings(
        self,
        *,
        enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        settings_group: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_stack#enabled AppstreamStack#enabled}.
        :param settings_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_stack#settings_group AppstreamStack#settings_group}.
        '''
        value = AppstreamStackApplicationSettings(
            enabled=enabled, settings_group=settings_group
        )

        return typing.cast(None, jsii.invoke(self, "putApplicationSettings", [value]))

    @jsii.member(jsii_name="putStorageConnectors")
    def put_storage_connectors(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["AppstreamStackStorageConnectors", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4b5efb9f0a10351d7a6bc6ea4ddd3bc22240b0344e4ff90b028e4f7f2e8e9fc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putStorageConnectors", [value]))

    @jsii.member(jsii_name="putUserSettings")
    def put_user_settings(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["AppstreamStackUserSettings", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ee652bd41e4d1ff47fd2e0a7ef2aab18ebe124b1e7cd5a0b25172d2183dc3d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putUserSettings", [value]))

    @jsii.member(jsii_name="resetAccessEndpoints")
    def reset_access_endpoints(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessEndpoints", []))

    @jsii.member(jsii_name="resetApplicationSettings")
    def reset_application_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApplicationSettings", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetDisplayName")
    def reset_display_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisplayName", []))

    @jsii.member(jsii_name="resetEmbedHostDomains")
    def reset_embed_host_domains(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmbedHostDomains", []))

    @jsii.member(jsii_name="resetFeedbackUrl")
    def reset_feedback_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFeedbackUrl", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetRedirectUrl")
    def reset_redirect_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedirectUrl", []))

    @jsii.member(jsii_name="resetStorageConnectors")
    def reset_storage_connectors(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageConnectors", []))

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
    @jsii.member(jsii_name="accessEndpoints")
    def access_endpoints(self) -> "AppstreamStackAccessEndpointsList":
        return typing.cast("AppstreamStackAccessEndpointsList", jsii.get(self, "accessEndpoints"))

    @builtins.property
    @jsii.member(jsii_name="applicationSettings")
    def application_settings(
        self,
    ) -> "AppstreamStackApplicationSettingsOutputReference":
        return typing.cast("AppstreamStackApplicationSettingsOutputReference", jsii.get(self, "applicationSettings"))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="createdTime")
    def created_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdTime"))

    @builtins.property
    @jsii.member(jsii_name="storageConnectors")
    def storage_connectors(self) -> "AppstreamStackStorageConnectorsList":
        return typing.cast("AppstreamStackStorageConnectorsList", jsii.get(self, "storageConnectors"))

    @builtins.property
    @jsii.member(jsii_name="userSettings")
    def user_settings(self) -> "AppstreamStackUserSettingsList":
        return typing.cast("AppstreamStackUserSettingsList", jsii.get(self, "userSettings"))

    @builtins.property
    @jsii.member(jsii_name="accessEndpointsInput")
    def access_endpoints_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AppstreamStackAccessEndpoints"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AppstreamStackAccessEndpoints"]]], jsii.get(self, "accessEndpointsInput"))

    @builtins.property
    @jsii.member(jsii_name="applicationSettingsInput")
    def application_settings_input(
        self,
    ) -> typing.Optional["AppstreamStackApplicationSettings"]:
        return typing.cast(typing.Optional["AppstreamStackApplicationSettings"], jsii.get(self, "applicationSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="displayNameInput")
    def display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="embedHostDomainsInput")
    def embed_host_domains_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "embedHostDomainsInput"))

    @builtins.property
    @jsii.member(jsii_name="feedbackUrlInput")
    def feedback_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "feedbackUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="redirectUrlInput")
    def redirect_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "redirectUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="storageConnectorsInput")
    def storage_connectors_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AppstreamStackStorageConnectors"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AppstreamStackStorageConnectors"]]], jsii.get(self, "storageConnectorsInput"))

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
    @jsii.member(jsii_name="userSettingsInput")
    def user_settings_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AppstreamStackUserSettings"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AppstreamStackUserSettings"]]], jsii.get(self, "userSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f3e9ceca397a4044c44524eb570528c4a5dd299a5ca2ca624ddfacd73cad455)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12efed7f5760af092295b94731f49da7861bf850e34b405a5e72730ed759e888)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="embedHostDomains")
    def embed_host_domains(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "embedHostDomains"))

    @embed_host_domains.setter
    def embed_host_domains(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f57916b025a0f5ecf5455ce0448a415f727b5fbc4f0d6bda11277c52220f8a74)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "embedHostDomains", value)

    @builtins.property
    @jsii.member(jsii_name="feedbackUrl")
    def feedback_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "feedbackUrl"))

    @feedback_url.setter
    def feedback_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b38871b230519de69557a31ad8b991fd5b9b57d81f204aaecd5c02545a200c65)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "feedbackUrl", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50c72b817163831931feeb32c0794bba5bba1c144832e33ca04bdcfee11b05d6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b30344dc181a44452dbd0e558c568d99594d899b7374c24dc361392f0b06c59)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="redirectUrl")
    def redirect_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "redirectUrl"))

    @redirect_url.setter
    def redirect_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9bfa67bb24756e7e9d20ca23652bb9d5948ac0ec85b45ef2d21b41c94a0eee89)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redirectUrl", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01c8a442efaee73e902e6cbe9dfaff0180af8aa12a6e92ecbdf426cd511d7b14)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7037d74576b41dbdb7d3255d422eff46ca49ecf2b00132c14f8a2fd55a7875ba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)


@jsii.data_type(
    jsii_type="aws.appstreamStack.AppstreamStackAccessEndpoints",
    jsii_struct_bases=[],
    name_mapping={"endpoint_type": "endpointType", "vpce_id": "vpceId"},
)
class AppstreamStackAccessEndpoints:
    def __init__(
        self,
        *,
        endpoint_type: builtins.str,
        vpce_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param endpoint_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_stack#endpoint_type AppstreamStack#endpoint_type}.
        :param vpce_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_stack#vpce_id AppstreamStack#vpce_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f91c350a6b80db9600695edd625d713216726246a8b3196ff5cf1ac002888486)
            check_type(argname="argument endpoint_type", value=endpoint_type, expected_type=type_hints["endpoint_type"])
            check_type(argname="argument vpce_id", value=vpce_id, expected_type=type_hints["vpce_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "endpoint_type": endpoint_type,
        }
        if vpce_id is not None:
            self._values["vpce_id"] = vpce_id

    @builtins.property
    def endpoint_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_stack#endpoint_type AppstreamStack#endpoint_type}.'''
        result = self._values.get("endpoint_type")
        assert result is not None, "Required property 'endpoint_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vpce_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_stack#vpce_id AppstreamStack#vpce_id}.'''
        result = self._values.get("vpce_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppstreamStackAccessEndpoints(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppstreamStackAccessEndpointsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appstreamStack.AppstreamStackAccessEndpointsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2cea85c17e8874f54634086ef41338eadccd28cca32f9659800b513e3c5dda04)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AppstreamStackAccessEndpointsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd47d85b069c7a2ddf2c6b204586a83ac07891d062799ba815df3052359796d3)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AppstreamStackAccessEndpointsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa062829079de20e74df09eb702d329e8289feee711af11e7c6a6ccebeb77aa8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4f2ff21c9d728221a6bcfe94f4559bb665f1a478b0b28375a19f6f15d0d45aeb)
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
            type_hints = typing.get_type_hints(_typecheckingstub__56e853c7cb589018df2c5809922c9350d37ab9c42e4583ab6c1ea457332648a8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppstreamStackAccessEndpoints]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppstreamStackAccessEndpoints]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppstreamStackAccessEndpoints]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__55779766162af62e987bfc5efe0762bf0f59a46b30d8404a49e13f34caacf666)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppstreamStackAccessEndpointsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appstreamStack.AppstreamStackAccessEndpointsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__086ebcd5b60055665fd75a5261c4cbe35187f1eea4b1482fad410bde9748f43d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetVpceId")
    def reset_vpce_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVpceId", []))

    @builtins.property
    @jsii.member(jsii_name="endpointTypeInput")
    def endpoint_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="vpceIdInput")
    def vpce_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vpceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="endpointType")
    def endpoint_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpointType"))

    @endpoint_type.setter
    def endpoint_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dea287ef748fc995f95c7ef149b51f57ecb1c63c1a9700a0214398b16bed7c79)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpointType", value)

    @builtins.property
    @jsii.member(jsii_name="vpceId")
    def vpce_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vpceId"))

    @vpce_id.setter
    def vpce_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ab03acc561b701033d0e651056ca2b74bb50dba2cb9effee425b4d78a930a18)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpceId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AppstreamStackAccessEndpoints, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AppstreamStackAccessEndpoints, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AppstreamStackAccessEndpoints, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06323afd584cee7d009de00d8b590593e58514b45dd49b560468469796382f02)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appstreamStack.AppstreamStackApplicationSettings",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "settings_group": "settingsGroup"},
)
class AppstreamStackApplicationSettings:
    def __init__(
        self,
        *,
        enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        settings_group: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_stack#enabled AppstreamStack#enabled}.
        :param settings_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_stack#settings_group AppstreamStack#settings_group}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6948b06e6eebdfa3a7f6816ce3591e90004efb3bac92e073d52bb9815f7f907b)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument settings_group", value=settings_group, expected_type=type_hints["settings_group"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "enabled": enabled,
        }
        if settings_group is not None:
            self._values["settings_group"] = settings_group

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_stack#enabled AppstreamStack#enabled}.'''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    @builtins.property
    def settings_group(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_stack#settings_group AppstreamStack#settings_group}.'''
        result = self._values.get("settings_group")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppstreamStackApplicationSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppstreamStackApplicationSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appstreamStack.AppstreamStackApplicationSettingsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9355b794d75ad66c53c20220678fcb23f6eee6b9ecb619255f97daa50a3f42ce)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetSettingsGroup")
    def reset_settings_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSettingsGroup", []))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="settingsGroupInput")
    def settings_group_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "settingsGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb0b390165bfea8aee78620f4c6331ae267faf4c613333d382f460d3a563bbbf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="settingsGroup")
    def settings_group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "settingsGroup"))

    @settings_group.setter
    def settings_group(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__afcc3cb8ced413c5b4ea1a52e37be247785af4fb9235efedaf3390198a57443f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "settingsGroup", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppstreamStackApplicationSettings]:
        return typing.cast(typing.Optional[AppstreamStackApplicationSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppstreamStackApplicationSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__46ef7541cc8c33f9cacc0aa822a1e197bc52c44331025d84be3be9bf3bb977f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appstreamStack.AppstreamStackConfig",
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
        "access_endpoints": "accessEndpoints",
        "application_settings": "applicationSettings",
        "description": "description",
        "display_name": "displayName",
        "embed_host_domains": "embedHostDomains",
        "feedback_url": "feedbackUrl",
        "id": "id",
        "redirect_url": "redirectUrl",
        "storage_connectors": "storageConnectors",
        "tags": "tags",
        "tags_all": "tagsAll",
        "user_settings": "userSettings",
    },
)
class AppstreamStackConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        access_endpoints: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AppstreamStackAccessEndpoints, typing.Dict[builtins.str, typing.Any]]]]] = None,
        application_settings: typing.Optional[typing.Union[AppstreamStackApplicationSettings, typing.Dict[builtins.str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        display_name: typing.Optional[builtins.str] = None,
        embed_host_domains: typing.Optional[typing.Sequence[builtins.str]] = None,
        feedback_url: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        redirect_url: typing.Optional[builtins.str] = None,
        storage_connectors: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["AppstreamStackStorageConnectors", typing.Dict[builtins.str, typing.Any]]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        user_settings: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["AppstreamStackUserSettings", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_stack#name AppstreamStack#name}.
        :param access_endpoints: access_endpoints block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_stack#access_endpoints AppstreamStack#access_endpoints}
        :param application_settings: application_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_stack#application_settings AppstreamStack#application_settings}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_stack#description AppstreamStack#description}.
        :param display_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_stack#display_name AppstreamStack#display_name}.
        :param embed_host_domains: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_stack#embed_host_domains AppstreamStack#embed_host_domains}.
        :param feedback_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_stack#feedback_url AppstreamStack#feedback_url}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_stack#id AppstreamStack#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param redirect_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_stack#redirect_url AppstreamStack#redirect_url}.
        :param storage_connectors: storage_connectors block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_stack#storage_connectors AppstreamStack#storage_connectors}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_stack#tags AppstreamStack#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_stack#tags_all AppstreamStack#tags_all}.
        :param user_settings: user_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_stack#user_settings AppstreamStack#user_settings}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(application_settings, dict):
            application_settings = AppstreamStackApplicationSettings(**application_settings)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3aeb1666e2db23a72488c8bd277b963c108e1ba6808a520eeace0157d4b2e2d)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument access_endpoints", value=access_endpoints, expected_type=type_hints["access_endpoints"])
            check_type(argname="argument application_settings", value=application_settings, expected_type=type_hints["application_settings"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument embed_host_domains", value=embed_host_domains, expected_type=type_hints["embed_host_domains"])
            check_type(argname="argument feedback_url", value=feedback_url, expected_type=type_hints["feedback_url"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument redirect_url", value=redirect_url, expected_type=type_hints["redirect_url"])
            check_type(argname="argument storage_connectors", value=storage_connectors, expected_type=type_hints["storage_connectors"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument user_settings", value=user_settings, expected_type=type_hints["user_settings"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
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
        if access_endpoints is not None:
            self._values["access_endpoints"] = access_endpoints
        if application_settings is not None:
            self._values["application_settings"] = application_settings
        if description is not None:
            self._values["description"] = description
        if display_name is not None:
            self._values["display_name"] = display_name
        if embed_host_domains is not None:
            self._values["embed_host_domains"] = embed_host_domains
        if feedback_url is not None:
            self._values["feedback_url"] = feedback_url
        if id is not None:
            self._values["id"] = id
        if redirect_url is not None:
            self._values["redirect_url"] = redirect_url
        if storage_connectors is not None:
            self._values["storage_connectors"] = storage_connectors
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
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_stack#name AppstreamStack#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_endpoints(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppstreamStackAccessEndpoints]]]:
        '''access_endpoints block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_stack#access_endpoints AppstreamStack#access_endpoints}
        '''
        result = self._values.get("access_endpoints")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppstreamStackAccessEndpoints]]], result)

    @builtins.property
    def application_settings(
        self,
    ) -> typing.Optional[AppstreamStackApplicationSettings]:
        '''application_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_stack#application_settings AppstreamStack#application_settings}
        '''
        result = self._values.get("application_settings")
        return typing.cast(typing.Optional[AppstreamStackApplicationSettings], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_stack#description AppstreamStack#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def display_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_stack#display_name AppstreamStack#display_name}.'''
        result = self._values.get("display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def embed_host_domains(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_stack#embed_host_domains AppstreamStack#embed_host_domains}.'''
        result = self._values.get("embed_host_domains")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def feedback_url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_stack#feedback_url AppstreamStack#feedback_url}.'''
        result = self._values.get("feedback_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_stack#id AppstreamStack#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def redirect_url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_stack#redirect_url AppstreamStack#redirect_url}.'''
        result = self._values.get("redirect_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def storage_connectors(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AppstreamStackStorageConnectors"]]]:
        '''storage_connectors block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_stack#storage_connectors AppstreamStack#storage_connectors}
        '''
        result = self._values.get("storage_connectors")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AppstreamStackStorageConnectors"]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_stack#tags AppstreamStack#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_stack#tags_all AppstreamStack#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def user_settings(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AppstreamStackUserSettings"]]]:
        '''user_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_stack#user_settings AppstreamStack#user_settings}
        '''
        result = self._values.get("user_settings")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AppstreamStackUserSettings"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppstreamStackConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appstreamStack.AppstreamStackStorageConnectors",
    jsii_struct_bases=[],
    name_mapping={
        "connector_type": "connectorType",
        "domains": "domains",
        "resource_identifier": "resourceIdentifier",
    },
)
class AppstreamStackStorageConnectors:
    def __init__(
        self,
        *,
        connector_type: builtins.str,
        domains: typing.Optional[typing.Sequence[builtins.str]] = None,
        resource_identifier: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connector_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_stack#connector_type AppstreamStack#connector_type}.
        :param domains: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_stack#domains AppstreamStack#domains}.
        :param resource_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_stack#resource_identifier AppstreamStack#resource_identifier}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e0a81d5f5a3618df2824838f2eec6550c864314ac59be2a066bf678ce5e5a15c)
            check_type(argname="argument connector_type", value=connector_type, expected_type=type_hints["connector_type"])
            check_type(argname="argument domains", value=domains, expected_type=type_hints["domains"])
            check_type(argname="argument resource_identifier", value=resource_identifier, expected_type=type_hints["resource_identifier"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "connector_type": connector_type,
        }
        if domains is not None:
            self._values["domains"] = domains
        if resource_identifier is not None:
            self._values["resource_identifier"] = resource_identifier

    @builtins.property
    def connector_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_stack#connector_type AppstreamStack#connector_type}.'''
        result = self._values.get("connector_type")
        assert result is not None, "Required property 'connector_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def domains(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_stack#domains AppstreamStack#domains}.'''
        result = self._values.get("domains")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def resource_identifier(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_stack#resource_identifier AppstreamStack#resource_identifier}.'''
        result = self._values.get("resource_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppstreamStackStorageConnectors(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppstreamStackStorageConnectorsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appstreamStack.AppstreamStackStorageConnectorsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3e1ae8fd0b580dc20dc7df44881e7207f18d2098d0d84b8df4923f0c1e716ac3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "AppstreamStackStorageConnectorsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0232d7944bb396599bb2bb0185e6bf44e2a35fc4f6e1fea355f3f61fa0094a75)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AppstreamStackStorageConnectorsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d993eb9c29b4551563e495d2f0fedac1c19c4993a7fe7aaababbf17cebbdc259)
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
            type_hints = typing.get_type_hints(_typecheckingstub__eb697c7a024850e5ef5e5904376d4605441d598d96331c67b7c6ce249db89f72)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3b9e3672f8aa0a7c513dff3ab01815dcdc699d0ac7a775764bcb395077400402)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppstreamStackStorageConnectors]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppstreamStackStorageConnectors]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppstreamStackStorageConnectors]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__784ded21f34e0223a52393e7857db6305869f2c376fb1270fc1a3d5a9ae695d3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppstreamStackStorageConnectorsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appstreamStack.AppstreamStackStorageConnectorsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f199a50f72fe95078a3e21cc511f7a6eeb447b34861bb641dfbcee256b09fdf4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDomains")
    def reset_domains(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDomains", []))

    @jsii.member(jsii_name="resetResourceIdentifier")
    def reset_resource_identifier(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourceIdentifier", []))

    @builtins.property
    @jsii.member(jsii_name="connectorTypeInput")
    def connector_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectorTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="domainsInput")
    def domains_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "domainsInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceIdentifierInput")
    def resource_identifier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceIdentifierInput"))

    @builtins.property
    @jsii.member(jsii_name="connectorType")
    def connector_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectorType"))

    @connector_type.setter
    def connector_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c38e2c1b68f5ec54598a6a699196b27ee7e69c62329b1b4a4cb3df488a00f9ea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectorType", value)

    @builtins.property
    @jsii.member(jsii_name="domains")
    def domains(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "domains"))

    @domains.setter
    def domains(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__342a0451177cdb4de0951e5aac404742d9d56c44fbb9bc0ae93d24dd787f8a9e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domains", value)

    @builtins.property
    @jsii.member(jsii_name="resourceIdentifier")
    def resource_identifier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceIdentifier"))

    @resource_identifier.setter
    def resource_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__269614d75a813dcad0e5c37e4da57c9db521679e2287a2f4fb35cacac6c48f26)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AppstreamStackStorageConnectors, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AppstreamStackStorageConnectors, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AppstreamStackStorageConnectors, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53ede34485b914bda55cec5a6580c619bbfa746eebff8ae413abdfa4228f5dbb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appstreamStack.AppstreamStackUserSettings",
    jsii_struct_bases=[],
    name_mapping={"action": "action", "permission": "permission"},
)
class AppstreamStackUserSettings:
    def __init__(self, *, action: builtins.str, permission: builtins.str) -> None:
        '''
        :param action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_stack#action AppstreamStack#action}.
        :param permission: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_stack#permission AppstreamStack#permission}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7e796b9858b8d0f74386e436c8e8f14f4155a995b91d767e257282cf8ec1219)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument permission", value=permission, expected_type=type_hints["permission"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "action": action,
            "permission": permission,
        }

    @builtins.property
    def action(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_stack#action AppstreamStack#action}.'''
        result = self._values.get("action")
        assert result is not None, "Required property 'action' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def permission(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_stack#permission AppstreamStack#permission}.'''
        result = self._values.get("permission")
        assert result is not None, "Required property 'permission' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppstreamStackUserSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppstreamStackUserSettingsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appstreamStack.AppstreamStackUserSettingsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__987397a34a7d1aa6a8672239cbe8fbe55a3e617e657520d667ff019b3b9094c3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AppstreamStackUserSettingsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc3faec4d7018d194e1079373f804765383d63c949b2b1ac171117efeb7f59a1)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AppstreamStackUserSettingsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96798898258393511c5a978801689844d72eb10e689e54e5c9b47478c304c4be)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1ecbe1a6a577cf4f010fbd3dfbfbe51dcebc75c017a0c447e2061b8770430c8e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f0e0408fa63c19eaa00c6ab7d9e9a496925ee49486e7f34320edcf44b56d7cca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppstreamStackUserSettings]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppstreamStackUserSettings]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppstreamStackUserSettings]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9472acf10062ae8d3987703abc456d20e2175df0e3b8de218a3b1e5d15eaca0b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppstreamStackUserSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appstreamStack.AppstreamStackUserSettingsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__63cf5094d6212ee3d2f65904a32370f40d2d1b5cfad59ecebf38719f4ad924c3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="permissionInput")
    def permission_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "permissionInput"))

    @builtins.property
    @jsii.member(jsii_name="action")
    def action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "action"))

    @action.setter
    def action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e40f4ed39c76ced2939f8078a3afa1ef0578f732597c614d807e5c2ae1c5f57c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "action", value)

    @builtins.property
    @jsii.member(jsii_name="permission")
    def permission(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "permission"))

    @permission.setter
    def permission(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__782de757cc068715cea41f03a997eb1eba016b61a3c176fb8a27ccb9d5e7b77d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "permission", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AppstreamStackUserSettings, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AppstreamStackUserSettings, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AppstreamStackUserSettings, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99617765ef606b16dbcf1593717da099ee9957d1d8dd9efa698d994c0757fb39)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "AppstreamStack",
    "AppstreamStackAccessEndpoints",
    "AppstreamStackAccessEndpointsList",
    "AppstreamStackAccessEndpointsOutputReference",
    "AppstreamStackApplicationSettings",
    "AppstreamStackApplicationSettingsOutputReference",
    "AppstreamStackConfig",
    "AppstreamStackStorageConnectors",
    "AppstreamStackStorageConnectorsList",
    "AppstreamStackStorageConnectorsOutputReference",
    "AppstreamStackUserSettings",
    "AppstreamStackUserSettingsList",
    "AppstreamStackUserSettingsOutputReference",
]

publication.publish()

def _typecheckingstub__8702ef50c7ab9ad9bf543c164a5a822740175de9a03a7cdb14f8ebce98e207e8(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    access_endpoints: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AppstreamStackAccessEndpoints, typing.Dict[builtins.str, typing.Any]]]]] = None,
    application_settings: typing.Optional[typing.Union[AppstreamStackApplicationSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    description: typing.Optional[builtins.str] = None,
    display_name: typing.Optional[builtins.str] = None,
    embed_host_domains: typing.Optional[typing.Sequence[builtins.str]] = None,
    feedback_url: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    redirect_url: typing.Optional[builtins.str] = None,
    storage_connectors: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AppstreamStackStorageConnectors, typing.Dict[builtins.str, typing.Any]]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    user_settings: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AppstreamStackUserSettings, typing.Dict[builtins.str, typing.Any]]]]] = None,
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

def _typecheckingstub__7e4e275d5b48b7d37d81086ae9d318969279bcdd58e391b04549a54df5fc3fc2(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AppstreamStackAccessEndpoints, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4b5efb9f0a10351d7a6bc6ea4ddd3bc22240b0344e4ff90b028e4f7f2e8e9fc(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AppstreamStackStorageConnectors, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ee652bd41e4d1ff47fd2e0a7ef2aab18ebe124b1e7cd5a0b25172d2183dc3d0(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AppstreamStackUserSettings, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f3e9ceca397a4044c44524eb570528c4a5dd299a5ca2ca624ddfacd73cad455(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12efed7f5760af092295b94731f49da7861bf850e34b405a5e72730ed759e888(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f57916b025a0f5ecf5455ce0448a415f727b5fbc4f0d6bda11277c52220f8a74(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b38871b230519de69557a31ad8b991fd5b9b57d81f204aaecd5c02545a200c65(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50c72b817163831931feeb32c0794bba5bba1c144832e33ca04bdcfee11b05d6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b30344dc181a44452dbd0e558c568d99594d899b7374c24dc361392f0b06c59(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9bfa67bb24756e7e9d20ca23652bb9d5948ac0ec85b45ef2d21b41c94a0eee89(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01c8a442efaee73e902e6cbe9dfaff0180af8aa12a6e92ecbdf426cd511d7b14(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7037d74576b41dbdb7d3255d422eff46ca49ecf2b00132c14f8a2fd55a7875ba(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f91c350a6b80db9600695edd625d713216726246a8b3196ff5cf1ac002888486(
    *,
    endpoint_type: builtins.str,
    vpce_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2cea85c17e8874f54634086ef41338eadccd28cca32f9659800b513e3c5dda04(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd47d85b069c7a2ddf2c6b204586a83ac07891d062799ba815df3052359796d3(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa062829079de20e74df09eb702d329e8289feee711af11e7c6a6ccebeb77aa8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f2ff21c9d728221a6bcfe94f4559bb665f1a478b0b28375a19f6f15d0d45aeb(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56e853c7cb589018df2c5809922c9350d37ab9c42e4583ab6c1ea457332648a8(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55779766162af62e987bfc5efe0762bf0f59a46b30d8404a49e13f34caacf666(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppstreamStackAccessEndpoints]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__086ebcd5b60055665fd75a5261c4cbe35187f1eea4b1482fad410bde9748f43d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dea287ef748fc995f95c7ef149b51f57ecb1c63c1a9700a0214398b16bed7c79(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ab03acc561b701033d0e651056ca2b74bb50dba2cb9effee425b4d78a930a18(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06323afd584cee7d009de00d8b590593e58514b45dd49b560468469796382f02(
    value: typing.Optional[typing.Union[AppstreamStackAccessEndpoints, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6948b06e6eebdfa3a7f6816ce3591e90004efb3bac92e073d52bb9815f7f907b(
    *,
    enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    settings_group: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9355b794d75ad66c53c20220678fcb23f6eee6b9ecb619255f97daa50a3f42ce(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb0b390165bfea8aee78620f4c6331ae267faf4c613333d382f460d3a563bbbf(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afcc3cb8ced413c5b4ea1a52e37be247785af4fb9235efedaf3390198a57443f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46ef7541cc8c33f9cacc0aa822a1e197bc52c44331025d84be3be9bf3bb977f8(
    value: typing.Optional[AppstreamStackApplicationSettings],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3aeb1666e2db23a72488c8bd277b963c108e1ba6808a520eeace0157d4b2e2d(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: builtins.str,
    access_endpoints: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AppstreamStackAccessEndpoints, typing.Dict[builtins.str, typing.Any]]]]] = None,
    application_settings: typing.Optional[typing.Union[AppstreamStackApplicationSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    description: typing.Optional[builtins.str] = None,
    display_name: typing.Optional[builtins.str] = None,
    embed_host_domains: typing.Optional[typing.Sequence[builtins.str]] = None,
    feedback_url: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    redirect_url: typing.Optional[builtins.str] = None,
    storage_connectors: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AppstreamStackStorageConnectors, typing.Dict[builtins.str, typing.Any]]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    user_settings: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AppstreamStackUserSettings, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0a81d5f5a3618df2824838f2eec6550c864314ac59be2a066bf678ce5e5a15c(
    *,
    connector_type: builtins.str,
    domains: typing.Optional[typing.Sequence[builtins.str]] = None,
    resource_identifier: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e1ae8fd0b580dc20dc7df44881e7207f18d2098d0d84b8df4923f0c1e716ac3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0232d7944bb396599bb2bb0185e6bf44e2a35fc4f6e1fea355f3f61fa0094a75(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d993eb9c29b4551563e495d2f0fedac1c19c4993a7fe7aaababbf17cebbdc259(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb697c7a024850e5ef5e5904376d4605441d598d96331c67b7c6ce249db89f72(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b9e3672f8aa0a7c513dff3ab01815dcdc699d0ac7a775764bcb395077400402(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__784ded21f34e0223a52393e7857db6305869f2c376fb1270fc1a3d5a9ae695d3(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppstreamStackStorageConnectors]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f199a50f72fe95078a3e21cc511f7a6eeb447b34861bb641dfbcee256b09fdf4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c38e2c1b68f5ec54598a6a699196b27ee7e69c62329b1b4a4cb3df488a00f9ea(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__342a0451177cdb4de0951e5aac404742d9d56c44fbb9bc0ae93d24dd787f8a9e(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__269614d75a813dcad0e5c37e4da57c9db521679e2287a2f4fb35cacac6c48f26(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53ede34485b914bda55cec5a6580c619bbfa746eebff8ae413abdfa4228f5dbb(
    value: typing.Optional[typing.Union[AppstreamStackStorageConnectors, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7e796b9858b8d0f74386e436c8e8f14f4155a995b91d767e257282cf8ec1219(
    *,
    action: builtins.str,
    permission: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__987397a34a7d1aa6a8672239cbe8fbe55a3e617e657520d667ff019b3b9094c3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc3faec4d7018d194e1079373f804765383d63c949b2b1ac171117efeb7f59a1(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96798898258393511c5a978801689844d72eb10e689e54e5c9b47478c304c4be(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ecbe1a6a577cf4f010fbd3dfbfbe51dcebc75c017a0c447e2061b8770430c8e(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0e0408fa63c19eaa00c6ab7d9e9a496925ee49486e7f34320edcf44b56d7cca(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9472acf10062ae8d3987703abc456d20e2175df0e3b8de218a3b1e5d15eaca0b(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppstreamStackUserSettings]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63cf5094d6212ee3d2f65904a32370f40d2d1b5cfad59ecebf38719f4ad924c3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e40f4ed39c76ced2939f8078a3afa1ef0578f732597c614d807e5c2ae1c5f57c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__782de757cc068715cea41f03a997eb1eba016b61a3c176fb8a27ccb9d5e7b77d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99617765ef606b16dbcf1593717da099ee9957d1d8dd9efa698d994c0757fb39(
    value: typing.Optional[typing.Union[AppstreamStackUserSettings, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
