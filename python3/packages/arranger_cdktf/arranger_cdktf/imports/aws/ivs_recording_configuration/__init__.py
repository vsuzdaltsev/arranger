'''
# `aws_ivs_recording_configuration`

Refer to the Terraform Registory for docs: [`aws_ivs_recording_configuration`](https://www.terraform.io/docs/providers/aws/r/ivs_recording_configuration).
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


class IvsRecordingConfiguration(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ivsRecordingConfiguration.IvsRecordingConfiguration",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/ivs_recording_configuration aws_ivs_recording_configuration}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        destination_configuration: typing.Union["IvsRecordingConfigurationDestinationConfiguration", typing.Dict[builtins.str, typing.Any]],
        id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        recording_reconnect_window_seconds: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        thumbnail_configuration: typing.Optional[typing.Union["IvsRecordingConfigurationThumbnailConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["IvsRecordingConfigurationTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/ivs_recording_configuration aws_ivs_recording_configuration} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param destination_configuration: destination_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivs_recording_configuration#destination_configuration IvsRecordingConfiguration#destination_configuration}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivs_recording_configuration#id IvsRecordingConfiguration#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivs_recording_configuration#name IvsRecordingConfiguration#name}.
        :param recording_reconnect_window_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivs_recording_configuration#recording_reconnect_window_seconds IvsRecordingConfiguration#recording_reconnect_window_seconds}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivs_recording_configuration#tags IvsRecordingConfiguration#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivs_recording_configuration#tags_all IvsRecordingConfiguration#tags_all}.
        :param thumbnail_configuration: thumbnail_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivs_recording_configuration#thumbnail_configuration IvsRecordingConfiguration#thumbnail_configuration}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivs_recording_configuration#timeouts IvsRecordingConfiguration#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f90c7065f85d1b94848c441d7da5c9809b637f645ab700f5be17df27ec5ad2f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = IvsRecordingConfigurationConfig(
            destination_configuration=destination_configuration,
            id=id,
            name=name,
            recording_reconnect_window_seconds=recording_reconnect_window_seconds,
            tags=tags,
            tags_all=tags_all,
            thumbnail_configuration=thumbnail_configuration,
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

    @jsii.member(jsii_name="putDestinationConfiguration")
    def put_destination_configuration(
        self,
        *,
        s3: typing.Union["IvsRecordingConfigurationDestinationConfigurationS3", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param s3: s3 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivs_recording_configuration#s3 IvsRecordingConfiguration#s3}
        '''
        value = IvsRecordingConfigurationDestinationConfiguration(s3=s3)

        return typing.cast(None, jsii.invoke(self, "putDestinationConfiguration", [value]))

    @jsii.member(jsii_name="putThumbnailConfiguration")
    def put_thumbnail_configuration(
        self,
        *,
        recording_mode: typing.Optional[builtins.str] = None,
        target_interval_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param recording_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivs_recording_configuration#recording_mode IvsRecordingConfiguration#recording_mode}.
        :param target_interval_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivs_recording_configuration#target_interval_seconds IvsRecordingConfiguration#target_interval_seconds}.
        '''
        value = IvsRecordingConfigurationThumbnailConfiguration(
            recording_mode=recording_mode,
            target_interval_seconds=target_interval_seconds,
        )

        return typing.cast(None, jsii.invoke(self, "putThumbnailConfiguration", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivs_recording_configuration#create IvsRecordingConfiguration#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivs_recording_configuration#delete IvsRecordingConfiguration#delete}.
        '''
        value = IvsRecordingConfigurationTimeouts(create=create, delete=delete)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetRecordingReconnectWindowSeconds")
    def reset_recording_reconnect_window_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRecordingReconnectWindowSeconds", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetThumbnailConfiguration")
    def reset_thumbnail_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetThumbnailConfiguration", []))

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
    @jsii.member(jsii_name="destinationConfiguration")
    def destination_configuration(
        self,
    ) -> "IvsRecordingConfigurationDestinationConfigurationOutputReference":
        return typing.cast("IvsRecordingConfigurationDestinationConfigurationOutputReference", jsii.get(self, "destinationConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @builtins.property
    @jsii.member(jsii_name="thumbnailConfiguration")
    def thumbnail_configuration(
        self,
    ) -> "IvsRecordingConfigurationThumbnailConfigurationOutputReference":
        return typing.cast("IvsRecordingConfigurationThumbnailConfigurationOutputReference", jsii.get(self, "thumbnailConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "IvsRecordingConfigurationTimeoutsOutputReference":
        return typing.cast("IvsRecordingConfigurationTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="destinationConfigurationInput")
    def destination_configuration_input(
        self,
    ) -> typing.Optional["IvsRecordingConfigurationDestinationConfiguration"]:
        return typing.cast(typing.Optional["IvsRecordingConfigurationDestinationConfiguration"], jsii.get(self, "destinationConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="recordingReconnectWindowSecondsInput")
    def recording_reconnect_window_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "recordingReconnectWindowSecondsInput"))

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
    @jsii.member(jsii_name="thumbnailConfigurationInput")
    def thumbnail_configuration_input(
        self,
    ) -> typing.Optional["IvsRecordingConfigurationThumbnailConfiguration"]:
        return typing.cast(typing.Optional["IvsRecordingConfigurationThumbnailConfiguration"], jsii.get(self, "thumbnailConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["IvsRecordingConfigurationTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["IvsRecordingConfigurationTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c89041a119f465b945d317c071fe4b75b4e9ffbc00a65bb67d7c06280314f1a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec0f5a6fe3393f232d04af54fe28a2eca67c212a5188a24763a64f3bbeac4815)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="recordingReconnectWindowSeconds")
    def recording_reconnect_window_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "recordingReconnectWindowSeconds"))

    @recording_reconnect_window_seconds.setter
    def recording_reconnect_window_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a2f8d66558ea824b644d6984aa660e0e499cde763a4cca0114640c39f82e27e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recordingReconnectWindowSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c70ca2a0c99c0f28fa0c5627b6ff4dc065bed1472b765d22483fdbe397f6ccc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8509c3150618373af2c62b57a262469b866f75aef3605e4d2448a613cd1d4d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)


@jsii.data_type(
    jsii_type="aws.ivsRecordingConfiguration.IvsRecordingConfigurationConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "destination_configuration": "destinationConfiguration",
        "id": "id",
        "name": "name",
        "recording_reconnect_window_seconds": "recordingReconnectWindowSeconds",
        "tags": "tags",
        "tags_all": "tagsAll",
        "thumbnail_configuration": "thumbnailConfiguration",
        "timeouts": "timeouts",
    },
)
class IvsRecordingConfigurationConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        destination_configuration: typing.Union["IvsRecordingConfigurationDestinationConfiguration", typing.Dict[builtins.str, typing.Any]],
        id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        recording_reconnect_window_seconds: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        thumbnail_configuration: typing.Optional[typing.Union["IvsRecordingConfigurationThumbnailConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["IvsRecordingConfigurationTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param destination_configuration: destination_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivs_recording_configuration#destination_configuration IvsRecordingConfiguration#destination_configuration}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivs_recording_configuration#id IvsRecordingConfiguration#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivs_recording_configuration#name IvsRecordingConfiguration#name}.
        :param recording_reconnect_window_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivs_recording_configuration#recording_reconnect_window_seconds IvsRecordingConfiguration#recording_reconnect_window_seconds}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivs_recording_configuration#tags IvsRecordingConfiguration#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivs_recording_configuration#tags_all IvsRecordingConfiguration#tags_all}.
        :param thumbnail_configuration: thumbnail_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivs_recording_configuration#thumbnail_configuration IvsRecordingConfiguration#thumbnail_configuration}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivs_recording_configuration#timeouts IvsRecordingConfiguration#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(destination_configuration, dict):
            destination_configuration = IvsRecordingConfigurationDestinationConfiguration(**destination_configuration)
        if isinstance(thumbnail_configuration, dict):
            thumbnail_configuration = IvsRecordingConfigurationThumbnailConfiguration(**thumbnail_configuration)
        if isinstance(timeouts, dict):
            timeouts = IvsRecordingConfigurationTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80b9fc0d28a4cc441410f6339cec5ec49a37dec3d36d2048db2ee36fb6559e69)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument destination_configuration", value=destination_configuration, expected_type=type_hints["destination_configuration"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument recording_reconnect_window_seconds", value=recording_reconnect_window_seconds, expected_type=type_hints["recording_reconnect_window_seconds"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument thumbnail_configuration", value=thumbnail_configuration, expected_type=type_hints["thumbnail_configuration"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "destination_configuration": destination_configuration,
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
        if name is not None:
            self._values["name"] = name
        if recording_reconnect_window_seconds is not None:
            self._values["recording_reconnect_window_seconds"] = recording_reconnect_window_seconds
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if thumbnail_configuration is not None:
            self._values["thumbnail_configuration"] = thumbnail_configuration
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
    def destination_configuration(
        self,
    ) -> "IvsRecordingConfigurationDestinationConfiguration":
        '''destination_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivs_recording_configuration#destination_configuration IvsRecordingConfiguration#destination_configuration}
        '''
        result = self._values.get("destination_configuration")
        assert result is not None, "Required property 'destination_configuration' is missing"
        return typing.cast("IvsRecordingConfigurationDestinationConfiguration", result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivs_recording_configuration#id IvsRecordingConfiguration#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivs_recording_configuration#name IvsRecordingConfiguration#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def recording_reconnect_window_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivs_recording_configuration#recording_reconnect_window_seconds IvsRecordingConfiguration#recording_reconnect_window_seconds}.'''
        result = self._values.get("recording_reconnect_window_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivs_recording_configuration#tags IvsRecordingConfiguration#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivs_recording_configuration#tags_all IvsRecordingConfiguration#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def thumbnail_configuration(
        self,
    ) -> typing.Optional["IvsRecordingConfigurationThumbnailConfiguration"]:
        '''thumbnail_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivs_recording_configuration#thumbnail_configuration IvsRecordingConfiguration#thumbnail_configuration}
        '''
        result = self._values.get("thumbnail_configuration")
        return typing.cast(typing.Optional["IvsRecordingConfigurationThumbnailConfiguration"], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["IvsRecordingConfigurationTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivs_recording_configuration#timeouts IvsRecordingConfiguration#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["IvsRecordingConfigurationTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IvsRecordingConfigurationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.ivsRecordingConfiguration.IvsRecordingConfigurationDestinationConfiguration",
    jsii_struct_bases=[],
    name_mapping={"s3": "s3"},
)
class IvsRecordingConfigurationDestinationConfiguration:
    def __init__(
        self,
        *,
        s3: typing.Union["IvsRecordingConfigurationDestinationConfigurationS3", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param s3: s3 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivs_recording_configuration#s3 IvsRecordingConfiguration#s3}
        '''
        if isinstance(s3, dict):
            s3 = IvsRecordingConfigurationDestinationConfigurationS3(**s3)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__938d4859d966eb0cc09dfb7df4362df1119addc5f397b8594ecb1f46062f325f)
            check_type(argname="argument s3", value=s3, expected_type=type_hints["s3"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "s3": s3,
        }

    @builtins.property
    def s3(self) -> "IvsRecordingConfigurationDestinationConfigurationS3":
        '''s3 block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivs_recording_configuration#s3 IvsRecordingConfiguration#s3}
        '''
        result = self._values.get("s3")
        assert result is not None, "Required property 's3' is missing"
        return typing.cast("IvsRecordingConfigurationDestinationConfigurationS3", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IvsRecordingConfigurationDestinationConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IvsRecordingConfigurationDestinationConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ivsRecordingConfiguration.IvsRecordingConfigurationDestinationConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__eb03f1bfafd2f465c5adeaad5076ea24ac7d5494365493bb1aed9ff360a8f849)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putS3")
    def put_s3(self, *, bucket_name: builtins.str) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivs_recording_configuration#bucket_name IvsRecordingConfiguration#bucket_name}.
        '''
        value = IvsRecordingConfigurationDestinationConfigurationS3(
            bucket_name=bucket_name
        )

        return typing.cast(None, jsii.invoke(self, "putS3", [value]))

    @builtins.property
    @jsii.member(jsii_name="s3")
    def s3(
        self,
    ) -> "IvsRecordingConfigurationDestinationConfigurationS3OutputReference":
        return typing.cast("IvsRecordingConfigurationDestinationConfigurationS3OutputReference", jsii.get(self, "s3"))

    @builtins.property
    @jsii.member(jsii_name="s3Input")
    def s3_input(
        self,
    ) -> typing.Optional["IvsRecordingConfigurationDestinationConfigurationS3"]:
        return typing.cast(typing.Optional["IvsRecordingConfigurationDestinationConfigurationS3"], jsii.get(self, "s3Input"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[IvsRecordingConfigurationDestinationConfiguration]:
        return typing.cast(typing.Optional[IvsRecordingConfigurationDestinationConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[IvsRecordingConfigurationDestinationConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5503c75004837230c55cc79036a7badbfee2a3136483d77416a259847f289ba3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ivsRecordingConfiguration.IvsRecordingConfigurationDestinationConfigurationS3",
    jsii_struct_bases=[],
    name_mapping={"bucket_name": "bucketName"},
)
class IvsRecordingConfigurationDestinationConfigurationS3:
    def __init__(self, *, bucket_name: builtins.str) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivs_recording_configuration#bucket_name IvsRecordingConfiguration#bucket_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4390d698f6264cf54cd0c8e11c3d90cd2cbfa5a2d9e277ca67ef782e1316095c)
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bucket_name": bucket_name,
        }

    @builtins.property
    def bucket_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivs_recording_configuration#bucket_name IvsRecordingConfiguration#bucket_name}.'''
        result = self._values.get("bucket_name")
        assert result is not None, "Required property 'bucket_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IvsRecordingConfigurationDestinationConfigurationS3(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IvsRecordingConfigurationDestinationConfigurationS3OutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ivsRecordingConfiguration.IvsRecordingConfigurationDestinationConfigurationS3OutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__34c495db2a5769cdd5ae98f4987604f9d0132f269c65d751577b3a94218bd137)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="bucketNameInput")
    def bucket_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketNameInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketName")
    def bucket_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketName"))

    @bucket_name.setter
    def bucket_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac876b405e1451f55d47284cc86a208bbe1444a97d25c31e507a0ff37e51f259)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[IvsRecordingConfigurationDestinationConfigurationS3]:
        return typing.cast(typing.Optional[IvsRecordingConfigurationDestinationConfigurationS3], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[IvsRecordingConfigurationDestinationConfigurationS3],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ef35cc56810a6a2f4e0b85a39223e71df33ce6cbef89657115b6cfecda90344)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ivsRecordingConfiguration.IvsRecordingConfigurationThumbnailConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "recording_mode": "recordingMode",
        "target_interval_seconds": "targetIntervalSeconds",
    },
)
class IvsRecordingConfigurationThumbnailConfiguration:
    def __init__(
        self,
        *,
        recording_mode: typing.Optional[builtins.str] = None,
        target_interval_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param recording_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivs_recording_configuration#recording_mode IvsRecordingConfiguration#recording_mode}.
        :param target_interval_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivs_recording_configuration#target_interval_seconds IvsRecordingConfiguration#target_interval_seconds}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7bcdf3d24c51bf165f7c884b6c2ed3254d0781864b3cfbb41eee58e1e2f906e8)
            check_type(argname="argument recording_mode", value=recording_mode, expected_type=type_hints["recording_mode"])
            check_type(argname="argument target_interval_seconds", value=target_interval_seconds, expected_type=type_hints["target_interval_seconds"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if recording_mode is not None:
            self._values["recording_mode"] = recording_mode
        if target_interval_seconds is not None:
            self._values["target_interval_seconds"] = target_interval_seconds

    @builtins.property
    def recording_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivs_recording_configuration#recording_mode IvsRecordingConfiguration#recording_mode}.'''
        result = self._values.get("recording_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_interval_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivs_recording_configuration#target_interval_seconds IvsRecordingConfiguration#target_interval_seconds}.'''
        result = self._values.get("target_interval_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IvsRecordingConfigurationThumbnailConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IvsRecordingConfigurationThumbnailConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ivsRecordingConfiguration.IvsRecordingConfigurationThumbnailConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c1c5a33fe918f8bd8703ffe5369c65d9d180e7f1b0daf5012cb554a0d47800f6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetRecordingMode")
    def reset_recording_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRecordingMode", []))

    @jsii.member(jsii_name="resetTargetIntervalSeconds")
    def reset_target_interval_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetIntervalSeconds", []))

    @builtins.property
    @jsii.member(jsii_name="recordingModeInput")
    def recording_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "recordingModeInput"))

    @builtins.property
    @jsii.member(jsii_name="targetIntervalSecondsInput")
    def target_interval_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "targetIntervalSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="recordingMode")
    def recording_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "recordingMode"))

    @recording_mode.setter
    def recording_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__952085cc3d1e5499327b33eacf3b2eedc3fe8f15e8560e78ab89d030d44ad826)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recordingMode", value)

    @builtins.property
    @jsii.member(jsii_name="targetIntervalSeconds")
    def target_interval_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "targetIntervalSeconds"))

    @target_interval_seconds.setter
    def target_interval_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__362f5c190483e4dffba0272bf25dcfdf3ff535eefc983a74a676fa83d07ddb52)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetIntervalSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[IvsRecordingConfigurationThumbnailConfiguration]:
        return typing.cast(typing.Optional[IvsRecordingConfigurationThumbnailConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[IvsRecordingConfigurationThumbnailConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13ae8739e06a0655ae749ca1a043fbdfbdd3593a42ea23b0c219283136db626d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ivsRecordingConfiguration.IvsRecordingConfigurationTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete"},
)
class IvsRecordingConfigurationTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivs_recording_configuration#create IvsRecordingConfiguration#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivs_recording_configuration#delete IvsRecordingConfiguration#delete}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e95563731c4b16aef9787f109229dcfd9b321acd3e711a8872ea24516b6b17d7)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivs_recording_configuration#create IvsRecordingConfiguration#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivs_recording_configuration#delete IvsRecordingConfiguration#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IvsRecordingConfigurationTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IvsRecordingConfigurationTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ivsRecordingConfiguration.IvsRecordingConfigurationTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e76917640c873fc11881761a982494ebd9852aacd85ae91f2fa48adb090a3ad0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c1c5d08c28728ca9c9722c67366354373d8afa9d408e3bdcfc07e6c5c9bdd0a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b8dd27ab18b84f23a7bac0e74fb04c99e4720c95382fcb5c1f05ca8eb510b1c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[IvsRecordingConfigurationTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[IvsRecordingConfigurationTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[IvsRecordingConfigurationTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0998ccfbace300bceca41c83d1dbba34257afd50c54c3875e95ab14d37b13a47)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "IvsRecordingConfiguration",
    "IvsRecordingConfigurationConfig",
    "IvsRecordingConfigurationDestinationConfiguration",
    "IvsRecordingConfigurationDestinationConfigurationOutputReference",
    "IvsRecordingConfigurationDestinationConfigurationS3",
    "IvsRecordingConfigurationDestinationConfigurationS3OutputReference",
    "IvsRecordingConfigurationThumbnailConfiguration",
    "IvsRecordingConfigurationThumbnailConfigurationOutputReference",
    "IvsRecordingConfigurationTimeouts",
    "IvsRecordingConfigurationTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__4f90c7065f85d1b94848c441d7da5c9809b637f645ab700f5be17df27ec5ad2f(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    destination_configuration: typing.Union[IvsRecordingConfigurationDestinationConfiguration, typing.Dict[builtins.str, typing.Any]],
    id: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    recording_reconnect_window_seconds: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    thumbnail_configuration: typing.Optional[typing.Union[IvsRecordingConfigurationThumbnailConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    timeouts: typing.Optional[typing.Union[IvsRecordingConfigurationTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__7c89041a119f465b945d317c071fe4b75b4e9ffbc00a65bb67d7c06280314f1a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec0f5a6fe3393f232d04af54fe28a2eca67c212a5188a24763a64f3bbeac4815(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a2f8d66558ea824b644d6984aa660e0e499cde763a4cca0114640c39f82e27e(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c70ca2a0c99c0f28fa0c5627b6ff4dc065bed1472b765d22483fdbe397f6ccc(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8509c3150618373af2c62b57a262469b866f75aef3605e4d2448a613cd1d4d2(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80b9fc0d28a4cc441410f6339cec5ec49a37dec3d36d2048db2ee36fb6559e69(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    destination_configuration: typing.Union[IvsRecordingConfigurationDestinationConfiguration, typing.Dict[builtins.str, typing.Any]],
    id: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    recording_reconnect_window_seconds: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    thumbnail_configuration: typing.Optional[typing.Union[IvsRecordingConfigurationThumbnailConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    timeouts: typing.Optional[typing.Union[IvsRecordingConfigurationTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__938d4859d966eb0cc09dfb7df4362df1119addc5f397b8594ecb1f46062f325f(
    *,
    s3: typing.Union[IvsRecordingConfigurationDestinationConfigurationS3, typing.Dict[builtins.str, typing.Any]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb03f1bfafd2f465c5adeaad5076ea24ac7d5494365493bb1aed9ff360a8f849(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5503c75004837230c55cc79036a7badbfee2a3136483d77416a259847f289ba3(
    value: typing.Optional[IvsRecordingConfigurationDestinationConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4390d698f6264cf54cd0c8e11c3d90cd2cbfa5a2d9e277ca67ef782e1316095c(
    *,
    bucket_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34c495db2a5769cdd5ae98f4987604f9d0132f269c65d751577b3a94218bd137(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac876b405e1451f55d47284cc86a208bbe1444a97d25c31e507a0ff37e51f259(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ef35cc56810a6a2f4e0b85a39223e71df33ce6cbef89657115b6cfecda90344(
    value: typing.Optional[IvsRecordingConfigurationDestinationConfigurationS3],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7bcdf3d24c51bf165f7c884b6c2ed3254d0781864b3cfbb41eee58e1e2f906e8(
    *,
    recording_mode: typing.Optional[builtins.str] = None,
    target_interval_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1c5a33fe918f8bd8703ffe5369c65d9d180e7f1b0daf5012cb554a0d47800f6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__952085cc3d1e5499327b33eacf3b2eedc3fe8f15e8560e78ab89d030d44ad826(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__362f5c190483e4dffba0272bf25dcfdf3ff535eefc983a74a676fa83d07ddb52(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13ae8739e06a0655ae749ca1a043fbdfbdd3593a42ea23b0c219283136db626d(
    value: typing.Optional[IvsRecordingConfigurationThumbnailConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e95563731c4b16aef9787f109229dcfd9b321acd3e711a8872ea24516b6b17d7(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e76917640c873fc11881761a982494ebd9852aacd85ae91f2fa48adb090a3ad0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c1c5d08c28728ca9c9722c67366354373d8afa9d408e3bdcfc07e6c5c9bdd0a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b8dd27ab18b84f23a7bac0e74fb04c99e4720c95382fcb5c1f05ca8eb510b1c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0998ccfbace300bceca41c83d1dbba34257afd50c54c3875e95ab14d37b13a47(
    value: typing.Optional[typing.Union[IvsRecordingConfigurationTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
