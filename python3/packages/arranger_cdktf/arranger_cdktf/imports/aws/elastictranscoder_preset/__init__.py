'''
# `aws_elastictranscoder_preset`

Refer to the Terraform Registory for docs: [`aws_elastictranscoder_preset`](https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset).
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


class ElastictranscoderPreset(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.elastictranscoderPreset.ElastictranscoderPreset",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset aws_elastictranscoder_preset}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        container: builtins.str,
        audio: typing.Optional[typing.Union["ElastictranscoderPresetAudio", typing.Dict[builtins.str, typing.Any]]] = None,
        audio_codec_options: typing.Optional[typing.Union["ElastictranscoderPresetAudioCodecOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        thumbnails: typing.Optional[typing.Union["ElastictranscoderPresetThumbnails", typing.Dict[builtins.str, typing.Any]]] = None,
        type: typing.Optional[builtins.str] = None,
        video: typing.Optional[typing.Union["ElastictranscoderPresetVideo", typing.Dict[builtins.str, typing.Any]]] = None,
        video_codec_options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        video_watermarks: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ElastictranscoderPresetVideoWatermarks", typing.Dict[builtins.str, typing.Any]]]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset aws_elastictranscoder_preset} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param container: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#container ElastictranscoderPreset#container}.
        :param audio: audio block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#audio ElastictranscoderPreset#audio}
        :param audio_codec_options: audio_codec_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#audio_codec_options ElastictranscoderPreset#audio_codec_options}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#description ElastictranscoderPreset#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#id ElastictranscoderPreset#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#name ElastictranscoderPreset#name}.
        :param thumbnails: thumbnails block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#thumbnails ElastictranscoderPreset#thumbnails}
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#type ElastictranscoderPreset#type}.
        :param video: video block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#video ElastictranscoderPreset#video}
        :param video_codec_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#video_codec_options ElastictranscoderPreset#video_codec_options}.
        :param video_watermarks: video_watermarks block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#video_watermarks ElastictranscoderPreset#video_watermarks}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__10ef401fd3963f9db42ea789f76e13b7b11aacd7699b07c8880228e9bc43b8f5)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ElastictranscoderPresetConfig(
            container=container,
            audio=audio,
            audio_codec_options=audio_codec_options,
            description=description,
            id=id,
            name=name,
            thumbnails=thumbnails,
            type=type,
            video=video,
            video_codec_options=video_codec_options,
            video_watermarks=video_watermarks,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAudio")
    def put_audio(
        self,
        *,
        audio_packing_mode: typing.Optional[builtins.str] = None,
        bit_rate: typing.Optional[builtins.str] = None,
        channels: typing.Optional[builtins.str] = None,
        codec: typing.Optional[builtins.str] = None,
        sample_rate: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param audio_packing_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#audio_packing_mode ElastictranscoderPreset#audio_packing_mode}.
        :param bit_rate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#bit_rate ElastictranscoderPreset#bit_rate}.
        :param channels: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#channels ElastictranscoderPreset#channels}.
        :param codec: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#codec ElastictranscoderPreset#codec}.
        :param sample_rate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#sample_rate ElastictranscoderPreset#sample_rate}.
        '''
        value = ElastictranscoderPresetAudio(
            audio_packing_mode=audio_packing_mode,
            bit_rate=bit_rate,
            channels=channels,
            codec=codec,
            sample_rate=sample_rate,
        )

        return typing.cast(None, jsii.invoke(self, "putAudio", [value]))

    @jsii.member(jsii_name="putAudioCodecOptions")
    def put_audio_codec_options(
        self,
        *,
        bit_depth: typing.Optional[builtins.str] = None,
        bit_order: typing.Optional[builtins.str] = None,
        profile: typing.Optional[builtins.str] = None,
        signed: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bit_depth: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#bit_depth ElastictranscoderPreset#bit_depth}.
        :param bit_order: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#bit_order ElastictranscoderPreset#bit_order}.
        :param profile: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#profile ElastictranscoderPreset#profile}.
        :param signed: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#signed ElastictranscoderPreset#signed}.
        '''
        value = ElastictranscoderPresetAudioCodecOptions(
            bit_depth=bit_depth, bit_order=bit_order, profile=profile, signed=signed
        )

        return typing.cast(None, jsii.invoke(self, "putAudioCodecOptions", [value]))

    @jsii.member(jsii_name="putThumbnails")
    def put_thumbnails(
        self,
        *,
        aspect_ratio: typing.Optional[builtins.str] = None,
        format: typing.Optional[builtins.str] = None,
        interval: typing.Optional[builtins.str] = None,
        max_height: typing.Optional[builtins.str] = None,
        max_width: typing.Optional[builtins.str] = None,
        padding_policy: typing.Optional[builtins.str] = None,
        resolution: typing.Optional[builtins.str] = None,
        sizing_policy: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aspect_ratio: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#aspect_ratio ElastictranscoderPreset#aspect_ratio}.
        :param format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#format ElastictranscoderPreset#format}.
        :param interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#interval ElastictranscoderPreset#interval}.
        :param max_height: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#max_height ElastictranscoderPreset#max_height}.
        :param max_width: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#max_width ElastictranscoderPreset#max_width}.
        :param padding_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#padding_policy ElastictranscoderPreset#padding_policy}.
        :param resolution: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#resolution ElastictranscoderPreset#resolution}.
        :param sizing_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#sizing_policy ElastictranscoderPreset#sizing_policy}.
        '''
        value = ElastictranscoderPresetThumbnails(
            aspect_ratio=aspect_ratio,
            format=format,
            interval=interval,
            max_height=max_height,
            max_width=max_width,
            padding_policy=padding_policy,
            resolution=resolution,
            sizing_policy=sizing_policy,
        )

        return typing.cast(None, jsii.invoke(self, "putThumbnails", [value]))

    @jsii.member(jsii_name="putVideo")
    def put_video(
        self,
        *,
        aspect_ratio: typing.Optional[builtins.str] = None,
        bit_rate: typing.Optional[builtins.str] = None,
        codec: typing.Optional[builtins.str] = None,
        display_aspect_ratio: typing.Optional[builtins.str] = None,
        fixed_gop: typing.Optional[builtins.str] = None,
        frame_rate: typing.Optional[builtins.str] = None,
        keyframes_max_dist: typing.Optional[builtins.str] = None,
        max_frame_rate: typing.Optional[builtins.str] = None,
        max_height: typing.Optional[builtins.str] = None,
        max_width: typing.Optional[builtins.str] = None,
        padding_policy: typing.Optional[builtins.str] = None,
        resolution: typing.Optional[builtins.str] = None,
        sizing_policy: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aspect_ratio: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#aspect_ratio ElastictranscoderPreset#aspect_ratio}.
        :param bit_rate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#bit_rate ElastictranscoderPreset#bit_rate}.
        :param codec: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#codec ElastictranscoderPreset#codec}.
        :param display_aspect_ratio: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#display_aspect_ratio ElastictranscoderPreset#display_aspect_ratio}.
        :param fixed_gop: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#fixed_gop ElastictranscoderPreset#fixed_gop}.
        :param frame_rate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#frame_rate ElastictranscoderPreset#frame_rate}.
        :param keyframes_max_dist: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#keyframes_max_dist ElastictranscoderPreset#keyframes_max_dist}.
        :param max_frame_rate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#max_frame_rate ElastictranscoderPreset#max_frame_rate}.
        :param max_height: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#max_height ElastictranscoderPreset#max_height}.
        :param max_width: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#max_width ElastictranscoderPreset#max_width}.
        :param padding_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#padding_policy ElastictranscoderPreset#padding_policy}.
        :param resolution: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#resolution ElastictranscoderPreset#resolution}.
        :param sizing_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#sizing_policy ElastictranscoderPreset#sizing_policy}.
        '''
        value = ElastictranscoderPresetVideo(
            aspect_ratio=aspect_ratio,
            bit_rate=bit_rate,
            codec=codec,
            display_aspect_ratio=display_aspect_ratio,
            fixed_gop=fixed_gop,
            frame_rate=frame_rate,
            keyframes_max_dist=keyframes_max_dist,
            max_frame_rate=max_frame_rate,
            max_height=max_height,
            max_width=max_width,
            padding_policy=padding_policy,
            resolution=resolution,
            sizing_policy=sizing_policy,
        )

        return typing.cast(None, jsii.invoke(self, "putVideo", [value]))

    @jsii.member(jsii_name="putVideoWatermarks")
    def put_video_watermarks(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ElastictranscoderPresetVideoWatermarks", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af43dc071b33424a01edac5501889ccac7a31677274be0c9243b252cf0048f2d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putVideoWatermarks", [value]))

    @jsii.member(jsii_name="resetAudio")
    def reset_audio(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAudio", []))

    @jsii.member(jsii_name="resetAudioCodecOptions")
    def reset_audio_codec_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAudioCodecOptions", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetThumbnails")
    def reset_thumbnails(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetThumbnails", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @jsii.member(jsii_name="resetVideo")
    def reset_video(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVideo", []))

    @jsii.member(jsii_name="resetVideoCodecOptions")
    def reset_video_codec_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVideoCodecOptions", []))

    @jsii.member(jsii_name="resetVideoWatermarks")
    def reset_video_watermarks(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVideoWatermarks", []))

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
    @jsii.member(jsii_name="audio")
    def audio(self) -> "ElastictranscoderPresetAudioOutputReference":
        return typing.cast("ElastictranscoderPresetAudioOutputReference", jsii.get(self, "audio"))

    @builtins.property
    @jsii.member(jsii_name="audioCodecOptions")
    def audio_codec_options(
        self,
    ) -> "ElastictranscoderPresetAudioCodecOptionsOutputReference":
        return typing.cast("ElastictranscoderPresetAudioCodecOptionsOutputReference", jsii.get(self, "audioCodecOptions"))

    @builtins.property
    @jsii.member(jsii_name="thumbnails")
    def thumbnails(self) -> "ElastictranscoderPresetThumbnailsOutputReference":
        return typing.cast("ElastictranscoderPresetThumbnailsOutputReference", jsii.get(self, "thumbnails"))

    @builtins.property
    @jsii.member(jsii_name="video")
    def video(self) -> "ElastictranscoderPresetVideoOutputReference":
        return typing.cast("ElastictranscoderPresetVideoOutputReference", jsii.get(self, "video"))

    @builtins.property
    @jsii.member(jsii_name="videoWatermarks")
    def video_watermarks(self) -> "ElastictranscoderPresetVideoWatermarksList":
        return typing.cast("ElastictranscoderPresetVideoWatermarksList", jsii.get(self, "videoWatermarks"))

    @builtins.property
    @jsii.member(jsii_name="audioCodecOptionsInput")
    def audio_codec_options_input(
        self,
    ) -> typing.Optional["ElastictranscoderPresetAudioCodecOptions"]:
        return typing.cast(typing.Optional["ElastictranscoderPresetAudioCodecOptions"], jsii.get(self, "audioCodecOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="audioInput")
    def audio_input(self) -> typing.Optional["ElastictranscoderPresetAudio"]:
        return typing.cast(typing.Optional["ElastictranscoderPresetAudio"], jsii.get(self, "audioInput"))

    @builtins.property
    @jsii.member(jsii_name="containerInput")
    def container_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "containerInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="thumbnailsInput")
    def thumbnails_input(self) -> typing.Optional["ElastictranscoderPresetThumbnails"]:
        return typing.cast(typing.Optional["ElastictranscoderPresetThumbnails"], jsii.get(self, "thumbnailsInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="videoCodecOptionsInput")
    def video_codec_options_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "videoCodecOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="videoInput")
    def video_input(self) -> typing.Optional["ElastictranscoderPresetVideo"]:
        return typing.cast(typing.Optional["ElastictranscoderPresetVideo"], jsii.get(self, "videoInput"))

    @builtins.property
    @jsii.member(jsii_name="videoWatermarksInput")
    def video_watermarks_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ElastictranscoderPresetVideoWatermarks"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ElastictranscoderPresetVideoWatermarks"]]], jsii.get(self, "videoWatermarksInput"))

    @builtins.property
    @jsii.member(jsii_name="container")
    def container(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "container"))

    @container.setter
    def container(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76853a538e211d84637eea667f6a0941ea72d0d2ea644253be248583154ee499)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "container", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18bbcf6157d2ad789562dbe87568bbd05800089dbcbc3e1fe45e6f05896c04af)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ddfc3ddcf107ee55b4e160b52eb687816546d5e4d6e540928ab7974efc5cd4fa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__acdac5343727ccf0f8d8f949bb70d683840c7fce43a151bb7341f27be6ece359)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a615e34df50c50b4864fe2d6eb9e3213049f861ec25211271c9237e85cd45fa2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="videoCodecOptions")
    def video_codec_options(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "videoCodecOptions"))

    @video_codec_options.setter
    def video_codec_options(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ad151199cddc0e2c081193845bd67d9052bdc4be04ed090616ba614e8db1049)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "videoCodecOptions", value)


@jsii.data_type(
    jsii_type="aws.elastictranscoderPreset.ElastictranscoderPresetAudio",
    jsii_struct_bases=[],
    name_mapping={
        "audio_packing_mode": "audioPackingMode",
        "bit_rate": "bitRate",
        "channels": "channels",
        "codec": "codec",
        "sample_rate": "sampleRate",
    },
)
class ElastictranscoderPresetAudio:
    def __init__(
        self,
        *,
        audio_packing_mode: typing.Optional[builtins.str] = None,
        bit_rate: typing.Optional[builtins.str] = None,
        channels: typing.Optional[builtins.str] = None,
        codec: typing.Optional[builtins.str] = None,
        sample_rate: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param audio_packing_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#audio_packing_mode ElastictranscoderPreset#audio_packing_mode}.
        :param bit_rate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#bit_rate ElastictranscoderPreset#bit_rate}.
        :param channels: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#channels ElastictranscoderPreset#channels}.
        :param codec: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#codec ElastictranscoderPreset#codec}.
        :param sample_rate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#sample_rate ElastictranscoderPreset#sample_rate}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07ad60d23a4091e127dbcc2ab27445c99b4a135bfb48f274b22640525960f4f7)
            check_type(argname="argument audio_packing_mode", value=audio_packing_mode, expected_type=type_hints["audio_packing_mode"])
            check_type(argname="argument bit_rate", value=bit_rate, expected_type=type_hints["bit_rate"])
            check_type(argname="argument channels", value=channels, expected_type=type_hints["channels"])
            check_type(argname="argument codec", value=codec, expected_type=type_hints["codec"])
            check_type(argname="argument sample_rate", value=sample_rate, expected_type=type_hints["sample_rate"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if audio_packing_mode is not None:
            self._values["audio_packing_mode"] = audio_packing_mode
        if bit_rate is not None:
            self._values["bit_rate"] = bit_rate
        if channels is not None:
            self._values["channels"] = channels
        if codec is not None:
            self._values["codec"] = codec
        if sample_rate is not None:
            self._values["sample_rate"] = sample_rate

    @builtins.property
    def audio_packing_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#audio_packing_mode ElastictranscoderPreset#audio_packing_mode}.'''
        result = self._values.get("audio_packing_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bit_rate(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#bit_rate ElastictranscoderPreset#bit_rate}.'''
        result = self._values.get("bit_rate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def channels(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#channels ElastictranscoderPreset#channels}.'''
        result = self._values.get("channels")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def codec(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#codec ElastictranscoderPreset#codec}.'''
        result = self._values.get("codec")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sample_rate(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#sample_rate ElastictranscoderPreset#sample_rate}.'''
        result = self._values.get("sample_rate")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastictranscoderPresetAudio(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.elastictranscoderPreset.ElastictranscoderPresetAudioCodecOptions",
    jsii_struct_bases=[],
    name_mapping={
        "bit_depth": "bitDepth",
        "bit_order": "bitOrder",
        "profile": "profile",
        "signed": "signed",
    },
)
class ElastictranscoderPresetAudioCodecOptions:
    def __init__(
        self,
        *,
        bit_depth: typing.Optional[builtins.str] = None,
        bit_order: typing.Optional[builtins.str] = None,
        profile: typing.Optional[builtins.str] = None,
        signed: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bit_depth: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#bit_depth ElastictranscoderPreset#bit_depth}.
        :param bit_order: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#bit_order ElastictranscoderPreset#bit_order}.
        :param profile: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#profile ElastictranscoderPreset#profile}.
        :param signed: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#signed ElastictranscoderPreset#signed}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b655f414e27186cbb98c757125a690902c2683c9c2d05f9ee885e1d184a2fddc)
            check_type(argname="argument bit_depth", value=bit_depth, expected_type=type_hints["bit_depth"])
            check_type(argname="argument bit_order", value=bit_order, expected_type=type_hints["bit_order"])
            check_type(argname="argument profile", value=profile, expected_type=type_hints["profile"])
            check_type(argname="argument signed", value=signed, expected_type=type_hints["signed"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if bit_depth is not None:
            self._values["bit_depth"] = bit_depth
        if bit_order is not None:
            self._values["bit_order"] = bit_order
        if profile is not None:
            self._values["profile"] = profile
        if signed is not None:
            self._values["signed"] = signed

    @builtins.property
    def bit_depth(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#bit_depth ElastictranscoderPreset#bit_depth}.'''
        result = self._values.get("bit_depth")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bit_order(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#bit_order ElastictranscoderPreset#bit_order}.'''
        result = self._values.get("bit_order")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def profile(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#profile ElastictranscoderPreset#profile}.'''
        result = self._values.get("profile")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def signed(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#signed ElastictranscoderPreset#signed}.'''
        result = self._values.get("signed")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastictranscoderPresetAudioCodecOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElastictranscoderPresetAudioCodecOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.elastictranscoderPreset.ElastictranscoderPresetAudioCodecOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ce502d0f76105e7b958837c796d54138a4597051e65988091b4fd9a56baf1f7b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBitDepth")
    def reset_bit_depth(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBitDepth", []))

    @jsii.member(jsii_name="resetBitOrder")
    def reset_bit_order(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBitOrder", []))

    @jsii.member(jsii_name="resetProfile")
    def reset_profile(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProfile", []))

    @jsii.member(jsii_name="resetSigned")
    def reset_signed(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSigned", []))

    @builtins.property
    @jsii.member(jsii_name="bitDepthInput")
    def bit_depth_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bitDepthInput"))

    @builtins.property
    @jsii.member(jsii_name="bitOrderInput")
    def bit_order_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bitOrderInput"))

    @builtins.property
    @jsii.member(jsii_name="profileInput")
    def profile_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "profileInput"))

    @builtins.property
    @jsii.member(jsii_name="signedInput")
    def signed_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "signedInput"))

    @builtins.property
    @jsii.member(jsii_name="bitDepth")
    def bit_depth(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bitDepth"))

    @bit_depth.setter
    def bit_depth(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73a6efb93dd83f2ca4b12c25674eb6ac92ecc8fb67b673fa706e3192f1e62163)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bitDepth", value)

    @builtins.property
    @jsii.member(jsii_name="bitOrder")
    def bit_order(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bitOrder"))

    @bit_order.setter
    def bit_order(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64e8a98fc511d3806984c91f61e7babe011f396eaa14662ee417d34db45142e9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bitOrder", value)

    @builtins.property
    @jsii.member(jsii_name="profile")
    def profile(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "profile"))

    @profile.setter
    def profile(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ac5aa1edbf48cff6f813fb33c7cb75138600d04b2f740c453eabd0eddd4e186)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "profile", value)

    @builtins.property
    @jsii.member(jsii_name="signed")
    def signed(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "signed"))

    @signed.setter
    def signed(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b901e52cfbaa3358a5eacd45135b200b91a02c0f9d0aa863289ef61dbf996a7f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "signed", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ElastictranscoderPresetAudioCodecOptions]:
        return typing.cast(typing.Optional[ElastictranscoderPresetAudioCodecOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ElastictranscoderPresetAudioCodecOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2267d06f3262e918526319b9d1394596f8938e61308c4f878ab62923fd7ca6dc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElastictranscoderPresetAudioOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.elastictranscoderPreset.ElastictranscoderPresetAudioOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__989b8032c8ba76c8252013548473f21fc07a83fe7c6632afd3f60d96bcf6de68)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAudioPackingMode")
    def reset_audio_packing_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAudioPackingMode", []))

    @jsii.member(jsii_name="resetBitRate")
    def reset_bit_rate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBitRate", []))

    @jsii.member(jsii_name="resetChannels")
    def reset_channels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetChannels", []))

    @jsii.member(jsii_name="resetCodec")
    def reset_codec(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCodec", []))

    @jsii.member(jsii_name="resetSampleRate")
    def reset_sample_rate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSampleRate", []))

    @builtins.property
    @jsii.member(jsii_name="audioPackingModeInput")
    def audio_packing_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "audioPackingModeInput"))

    @builtins.property
    @jsii.member(jsii_name="bitRateInput")
    def bit_rate_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bitRateInput"))

    @builtins.property
    @jsii.member(jsii_name="channelsInput")
    def channels_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "channelsInput"))

    @builtins.property
    @jsii.member(jsii_name="codecInput")
    def codec_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "codecInput"))

    @builtins.property
    @jsii.member(jsii_name="sampleRateInput")
    def sample_rate_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sampleRateInput"))

    @builtins.property
    @jsii.member(jsii_name="audioPackingMode")
    def audio_packing_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "audioPackingMode"))

    @audio_packing_mode.setter
    def audio_packing_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09293015ac2173a3c401ba2657a38214804f81a7e5ac72e246d14fd0bd821008)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "audioPackingMode", value)

    @builtins.property
    @jsii.member(jsii_name="bitRate")
    def bit_rate(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bitRate"))

    @bit_rate.setter
    def bit_rate(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1bcdf8fde74ad21a29536b4637ffd9ad250c8096d1c5fa0b667261c54a82a86f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bitRate", value)

    @builtins.property
    @jsii.member(jsii_name="channels")
    def channels(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "channels"))

    @channels.setter
    def channels(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__244c623aa93fea8f4b0c39a863508287b079423034afabaed0762aa063dc0e90)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "channels", value)

    @builtins.property
    @jsii.member(jsii_name="codec")
    def codec(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "codec"))

    @codec.setter
    def codec(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c37c45ef408c9b5ea39be76c07ab0a2649aa72564c706b952a34b9961d313152)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "codec", value)

    @builtins.property
    @jsii.member(jsii_name="sampleRate")
    def sample_rate(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sampleRate"))

    @sample_rate.setter
    def sample_rate(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f667169ddfeb9b845bfeae0cf8aeed0332ba8c3eb01007bea6ac8ff0a8927361)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sampleRate", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ElastictranscoderPresetAudio]:
        return typing.cast(typing.Optional[ElastictranscoderPresetAudio], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ElastictranscoderPresetAudio],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__28ca5b21f15e06d4b313746731cae7922128a7b4f7175a663610fb7a9467ba8b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.elastictranscoderPreset.ElastictranscoderPresetConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "container": "container",
        "audio": "audio",
        "audio_codec_options": "audioCodecOptions",
        "description": "description",
        "id": "id",
        "name": "name",
        "thumbnails": "thumbnails",
        "type": "type",
        "video": "video",
        "video_codec_options": "videoCodecOptions",
        "video_watermarks": "videoWatermarks",
    },
)
class ElastictranscoderPresetConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        container: builtins.str,
        audio: typing.Optional[typing.Union[ElastictranscoderPresetAudio, typing.Dict[builtins.str, typing.Any]]] = None,
        audio_codec_options: typing.Optional[typing.Union[ElastictranscoderPresetAudioCodecOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        thumbnails: typing.Optional[typing.Union["ElastictranscoderPresetThumbnails", typing.Dict[builtins.str, typing.Any]]] = None,
        type: typing.Optional[builtins.str] = None,
        video: typing.Optional[typing.Union["ElastictranscoderPresetVideo", typing.Dict[builtins.str, typing.Any]]] = None,
        video_codec_options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        video_watermarks: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ElastictranscoderPresetVideoWatermarks", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param container: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#container ElastictranscoderPreset#container}.
        :param audio: audio block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#audio ElastictranscoderPreset#audio}
        :param audio_codec_options: audio_codec_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#audio_codec_options ElastictranscoderPreset#audio_codec_options}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#description ElastictranscoderPreset#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#id ElastictranscoderPreset#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#name ElastictranscoderPreset#name}.
        :param thumbnails: thumbnails block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#thumbnails ElastictranscoderPreset#thumbnails}
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#type ElastictranscoderPreset#type}.
        :param video: video block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#video ElastictranscoderPreset#video}
        :param video_codec_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#video_codec_options ElastictranscoderPreset#video_codec_options}.
        :param video_watermarks: video_watermarks block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#video_watermarks ElastictranscoderPreset#video_watermarks}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(audio, dict):
            audio = ElastictranscoderPresetAudio(**audio)
        if isinstance(audio_codec_options, dict):
            audio_codec_options = ElastictranscoderPresetAudioCodecOptions(**audio_codec_options)
        if isinstance(thumbnails, dict):
            thumbnails = ElastictranscoderPresetThumbnails(**thumbnails)
        if isinstance(video, dict):
            video = ElastictranscoderPresetVideo(**video)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e0c9efa688ab2dde752f3a134d257d76427b986e801723dddb7051fac736b301)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument container", value=container, expected_type=type_hints["container"])
            check_type(argname="argument audio", value=audio, expected_type=type_hints["audio"])
            check_type(argname="argument audio_codec_options", value=audio_codec_options, expected_type=type_hints["audio_codec_options"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument thumbnails", value=thumbnails, expected_type=type_hints["thumbnails"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument video", value=video, expected_type=type_hints["video"])
            check_type(argname="argument video_codec_options", value=video_codec_options, expected_type=type_hints["video_codec_options"])
            check_type(argname="argument video_watermarks", value=video_watermarks, expected_type=type_hints["video_watermarks"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "container": container,
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
        if audio is not None:
            self._values["audio"] = audio
        if audio_codec_options is not None:
            self._values["audio_codec_options"] = audio_codec_options
        if description is not None:
            self._values["description"] = description
        if id is not None:
            self._values["id"] = id
        if name is not None:
            self._values["name"] = name
        if thumbnails is not None:
            self._values["thumbnails"] = thumbnails
        if type is not None:
            self._values["type"] = type
        if video is not None:
            self._values["video"] = video
        if video_codec_options is not None:
            self._values["video_codec_options"] = video_codec_options
        if video_watermarks is not None:
            self._values["video_watermarks"] = video_watermarks

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
    def container(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#container ElastictranscoderPreset#container}.'''
        result = self._values.get("container")
        assert result is not None, "Required property 'container' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def audio(self) -> typing.Optional[ElastictranscoderPresetAudio]:
        '''audio block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#audio ElastictranscoderPreset#audio}
        '''
        result = self._values.get("audio")
        return typing.cast(typing.Optional[ElastictranscoderPresetAudio], result)

    @builtins.property
    def audio_codec_options(
        self,
    ) -> typing.Optional[ElastictranscoderPresetAudioCodecOptions]:
        '''audio_codec_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#audio_codec_options ElastictranscoderPreset#audio_codec_options}
        '''
        result = self._values.get("audio_codec_options")
        return typing.cast(typing.Optional[ElastictranscoderPresetAudioCodecOptions], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#description ElastictranscoderPreset#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#id ElastictranscoderPreset#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#name ElastictranscoderPreset#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def thumbnails(self) -> typing.Optional["ElastictranscoderPresetThumbnails"]:
        '''thumbnails block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#thumbnails ElastictranscoderPreset#thumbnails}
        '''
        result = self._values.get("thumbnails")
        return typing.cast(typing.Optional["ElastictranscoderPresetThumbnails"], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#type ElastictranscoderPreset#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def video(self) -> typing.Optional["ElastictranscoderPresetVideo"]:
        '''video block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#video ElastictranscoderPreset#video}
        '''
        result = self._values.get("video")
        return typing.cast(typing.Optional["ElastictranscoderPresetVideo"], result)

    @builtins.property
    def video_codec_options(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#video_codec_options ElastictranscoderPreset#video_codec_options}.'''
        result = self._values.get("video_codec_options")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def video_watermarks(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ElastictranscoderPresetVideoWatermarks"]]]:
        '''video_watermarks block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#video_watermarks ElastictranscoderPreset#video_watermarks}
        '''
        result = self._values.get("video_watermarks")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ElastictranscoderPresetVideoWatermarks"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastictranscoderPresetConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.elastictranscoderPreset.ElastictranscoderPresetThumbnails",
    jsii_struct_bases=[],
    name_mapping={
        "aspect_ratio": "aspectRatio",
        "format": "format",
        "interval": "interval",
        "max_height": "maxHeight",
        "max_width": "maxWidth",
        "padding_policy": "paddingPolicy",
        "resolution": "resolution",
        "sizing_policy": "sizingPolicy",
    },
)
class ElastictranscoderPresetThumbnails:
    def __init__(
        self,
        *,
        aspect_ratio: typing.Optional[builtins.str] = None,
        format: typing.Optional[builtins.str] = None,
        interval: typing.Optional[builtins.str] = None,
        max_height: typing.Optional[builtins.str] = None,
        max_width: typing.Optional[builtins.str] = None,
        padding_policy: typing.Optional[builtins.str] = None,
        resolution: typing.Optional[builtins.str] = None,
        sizing_policy: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aspect_ratio: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#aspect_ratio ElastictranscoderPreset#aspect_ratio}.
        :param format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#format ElastictranscoderPreset#format}.
        :param interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#interval ElastictranscoderPreset#interval}.
        :param max_height: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#max_height ElastictranscoderPreset#max_height}.
        :param max_width: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#max_width ElastictranscoderPreset#max_width}.
        :param padding_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#padding_policy ElastictranscoderPreset#padding_policy}.
        :param resolution: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#resolution ElastictranscoderPreset#resolution}.
        :param sizing_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#sizing_policy ElastictranscoderPreset#sizing_policy}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89692e9001d68018a2ff568658e7f7c5b70dd654385f415569a2fc355479baec)
            check_type(argname="argument aspect_ratio", value=aspect_ratio, expected_type=type_hints["aspect_ratio"])
            check_type(argname="argument format", value=format, expected_type=type_hints["format"])
            check_type(argname="argument interval", value=interval, expected_type=type_hints["interval"])
            check_type(argname="argument max_height", value=max_height, expected_type=type_hints["max_height"])
            check_type(argname="argument max_width", value=max_width, expected_type=type_hints["max_width"])
            check_type(argname="argument padding_policy", value=padding_policy, expected_type=type_hints["padding_policy"])
            check_type(argname="argument resolution", value=resolution, expected_type=type_hints["resolution"])
            check_type(argname="argument sizing_policy", value=sizing_policy, expected_type=type_hints["sizing_policy"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if aspect_ratio is not None:
            self._values["aspect_ratio"] = aspect_ratio
        if format is not None:
            self._values["format"] = format
        if interval is not None:
            self._values["interval"] = interval
        if max_height is not None:
            self._values["max_height"] = max_height
        if max_width is not None:
            self._values["max_width"] = max_width
        if padding_policy is not None:
            self._values["padding_policy"] = padding_policy
        if resolution is not None:
            self._values["resolution"] = resolution
        if sizing_policy is not None:
            self._values["sizing_policy"] = sizing_policy

    @builtins.property
    def aspect_ratio(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#aspect_ratio ElastictranscoderPreset#aspect_ratio}.'''
        result = self._values.get("aspect_ratio")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def format(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#format ElastictranscoderPreset#format}.'''
        result = self._values.get("format")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def interval(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#interval ElastictranscoderPreset#interval}.'''
        result = self._values.get("interval")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_height(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#max_height ElastictranscoderPreset#max_height}.'''
        result = self._values.get("max_height")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_width(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#max_width ElastictranscoderPreset#max_width}.'''
        result = self._values.get("max_width")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def padding_policy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#padding_policy ElastictranscoderPreset#padding_policy}.'''
        result = self._values.get("padding_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resolution(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#resolution ElastictranscoderPreset#resolution}.'''
        result = self._values.get("resolution")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sizing_policy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#sizing_policy ElastictranscoderPreset#sizing_policy}.'''
        result = self._values.get("sizing_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastictranscoderPresetThumbnails(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElastictranscoderPresetThumbnailsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.elastictranscoderPreset.ElastictranscoderPresetThumbnailsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__dc18a7be691959aa40876331606de8a7f5e9e239d717f4400c58f3391189d56e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAspectRatio")
    def reset_aspect_ratio(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAspectRatio", []))

    @jsii.member(jsii_name="resetFormat")
    def reset_format(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFormat", []))

    @jsii.member(jsii_name="resetInterval")
    def reset_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInterval", []))

    @jsii.member(jsii_name="resetMaxHeight")
    def reset_max_height(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxHeight", []))

    @jsii.member(jsii_name="resetMaxWidth")
    def reset_max_width(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxWidth", []))

    @jsii.member(jsii_name="resetPaddingPolicy")
    def reset_padding_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPaddingPolicy", []))

    @jsii.member(jsii_name="resetResolution")
    def reset_resolution(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResolution", []))

    @jsii.member(jsii_name="resetSizingPolicy")
    def reset_sizing_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSizingPolicy", []))

    @builtins.property
    @jsii.member(jsii_name="aspectRatioInput")
    def aspect_ratio_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aspectRatioInput"))

    @builtins.property
    @jsii.member(jsii_name="formatInput")
    def format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "formatInput"))

    @builtins.property
    @jsii.member(jsii_name="intervalInput")
    def interval_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "intervalInput"))

    @builtins.property
    @jsii.member(jsii_name="maxHeightInput")
    def max_height_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxHeightInput"))

    @builtins.property
    @jsii.member(jsii_name="maxWidthInput")
    def max_width_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxWidthInput"))

    @builtins.property
    @jsii.member(jsii_name="paddingPolicyInput")
    def padding_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "paddingPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="resolutionInput")
    def resolution_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resolutionInput"))

    @builtins.property
    @jsii.member(jsii_name="sizingPolicyInput")
    def sizing_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sizingPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="aspectRatio")
    def aspect_ratio(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "aspectRatio"))

    @aspect_ratio.setter
    def aspect_ratio(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e3a3319f2e6b76a44f00eed4bfa5715ba09a64a1817ef66e4f9b466d1774b1e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "aspectRatio", value)

    @builtins.property
    @jsii.member(jsii_name="format")
    def format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "format"))

    @format.setter
    def format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec3044316cb5352972fe7dfd3df41815745481dd11393e42b2068fe7dd7016b3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "format", value)

    @builtins.property
    @jsii.member(jsii_name="interval")
    def interval(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "interval"))

    @interval.setter
    def interval(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ccf43428725f9cf1aa14a58c5844e3b93fe5bc7481cbeb0ef2aafeddfc120569)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "interval", value)

    @builtins.property
    @jsii.member(jsii_name="maxHeight")
    def max_height(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maxHeight"))

    @max_height.setter
    def max_height(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c355e27abcc51845d31db000deb2dbc92a854faba3b1d7ad8a2ffb91f17191ed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxHeight", value)

    @builtins.property
    @jsii.member(jsii_name="maxWidth")
    def max_width(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maxWidth"))

    @max_width.setter
    def max_width(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__466e2a890d0536aa0d746d92f43a4839b4efc35047ff17ac7e709777a3f56a8b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxWidth", value)

    @builtins.property
    @jsii.member(jsii_name="paddingPolicy")
    def padding_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "paddingPolicy"))

    @padding_policy.setter
    def padding_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c7ff74dc0c02303046a484e4ec8d2618c1bb8166b5f0ce0084b3a8f63798e6d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "paddingPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="resolution")
    def resolution(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resolution"))

    @resolution.setter
    def resolution(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95993ed182c4eaa577e289b345271aad6b2482686f45232fbb1d8187d948b375)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resolution", value)

    @builtins.property
    @jsii.member(jsii_name="sizingPolicy")
    def sizing_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sizingPolicy"))

    @sizing_policy.setter
    def sizing_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85dd0cf8e2f4388dcff487e51bc1b13d0634f25b17358a07e35674e42110704c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sizingPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ElastictranscoderPresetThumbnails]:
        return typing.cast(typing.Optional[ElastictranscoderPresetThumbnails], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ElastictranscoderPresetThumbnails],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__167d4857495263b4e70777af7f04ba8615057e6aeb42234e6149cf376691afa1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.elastictranscoderPreset.ElastictranscoderPresetVideo",
    jsii_struct_bases=[],
    name_mapping={
        "aspect_ratio": "aspectRatio",
        "bit_rate": "bitRate",
        "codec": "codec",
        "display_aspect_ratio": "displayAspectRatio",
        "fixed_gop": "fixedGop",
        "frame_rate": "frameRate",
        "keyframes_max_dist": "keyframesMaxDist",
        "max_frame_rate": "maxFrameRate",
        "max_height": "maxHeight",
        "max_width": "maxWidth",
        "padding_policy": "paddingPolicy",
        "resolution": "resolution",
        "sizing_policy": "sizingPolicy",
    },
)
class ElastictranscoderPresetVideo:
    def __init__(
        self,
        *,
        aspect_ratio: typing.Optional[builtins.str] = None,
        bit_rate: typing.Optional[builtins.str] = None,
        codec: typing.Optional[builtins.str] = None,
        display_aspect_ratio: typing.Optional[builtins.str] = None,
        fixed_gop: typing.Optional[builtins.str] = None,
        frame_rate: typing.Optional[builtins.str] = None,
        keyframes_max_dist: typing.Optional[builtins.str] = None,
        max_frame_rate: typing.Optional[builtins.str] = None,
        max_height: typing.Optional[builtins.str] = None,
        max_width: typing.Optional[builtins.str] = None,
        padding_policy: typing.Optional[builtins.str] = None,
        resolution: typing.Optional[builtins.str] = None,
        sizing_policy: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aspect_ratio: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#aspect_ratio ElastictranscoderPreset#aspect_ratio}.
        :param bit_rate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#bit_rate ElastictranscoderPreset#bit_rate}.
        :param codec: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#codec ElastictranscoderPreset#codec}.
        :param display_aspect_ratio: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#display_aspect_ratio ElastictranscoderPreset#display_aspect_ratio}.
        :param fixed_gop: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#fixed_gop ElastictranscoderPreset#fixed_gop}.
        :param frame_rate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#frame_rate ElastictranscoderPreset#frame_rate}.
        :param keyframes_max_dist: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#keyframes_max_dist ElastictranscoderPreset#keyframes_max_dist}.
        :param max_frame_rate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#max_frame_rate ElastictranscoderPreset#max_frame_rate}.
        :param max_height: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#max_height ElastictranscoderPreset#max_height}.
        :param max_width: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#max_width ElastictranscoderPreset#max_width}.
        :param padding_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#padding_policy ElastictranscoderPreset#padding_policy}.
        :param resolution: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#resolution ElastictranscoderPreset#resolution}.
        :param sizing_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#sizing_policy ElastictranscoderPreset#sizing_policy}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__efe7e5a35a36d1dd151be1a1c3df6f9465903e2903c6e94f65fd0071769ff846)
            check_type(argname="argument aspect_ratio", value=aspect_ratio, expected_type=type_hints["aspect_ratio"])
            check_type(argname="argument bit_rate", value=bit_rate, expected_type=type_hints["bit_rate"])
            check_type(argname="argument codec", value=codec, expected_type=type_hints["codec"])
            check_type(argname="argument display_aspect_ratio", value=display_aspect_ratio, expected_type=type_hints["display_aspect_ratio"])
            check_type(argname="argument fixed_gop", value=fixed_gop, expected_type=type_hints["fixed_gop"])
            check_type(argname="argument frame_rate", value=frame_rate, expected_type=type_hints["frame_rate"])
            check_type(argname="argument keyframes_max_dist", value=keyframes_max_dist, expected_type=type_hints["keyframes_max_dist"])
            check_type(argname="argument max_frame_rate", value=max_frame_rate, expected_type=type_hints["max_frame_rate"])
            check_type(argname="argument max_height", value=max_height, expected_type=type_hints["max_height"])
            check_type(argname="argument max_width", value=max_width, expected_type=type_hints["max_width"])
            check_type(argname="argument padding_policy", value=padding_policy, expected_type=type_hints["padding_policy"])
            check_type(argname="argument resolution", value=resolution, expected_type=type_hints["resolution"])
            check_type(argname="argument sizing_policy", value=sizing_policy, expected_type=type_hints["sizing_policy"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if aspect_ratio is not None:
            self._values["aspect_ratio"] = aspect_ratio
        if bit_rate is not None:
            self._values["bit_rate"] = bit_rate
        if codec is not None:
            self._values["codec"] = codec
        if display_aspect_ratio is not None:
            self._values["display_aspect_ratio"] = display_aspect_ratio
        if fixed_gop is not None:
            self._values["fixed_gop"] = fixed_gop
        if frame_rate is not None:
            self._values["frame_rate"] = frame_rate
        if keyframes_max_dist is not None:
            self._values["keyframes_max_dist"] = keyframes_max_dist
        if max_frame_rate is not None:
            self._values["max_frame_rate"] = max_frame_rate
        if max_height is not None:
            self._values["max_height"] = max_height
        if max_width is not None:
            self._values["max_width"] = max_width
        if padding_policy is not None:
            self._values["padding_policy"] = padding_policy
        if resolution is not None:
            self._values["resolution"] = resolution
        if sizing_policy is not None:
            self._values["sizing_policy"] = sizing_policy

    @builtins.property
    def aspect_ratio(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#aspect_ratio ElastictranscoderPreset#aspect_ratio}.'''
        result = self._values.get("aspect_ratio")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bit_rate(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#bit_rate ElastictranscoderPreset#bit_rate}.'''
        result = self._values.get("bit_rate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def codec(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#codec ElastictranscoderPreset#codec}.'''
        result = self._values.get("codec")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def display_aspect_ratio(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#display_aspect_ratio ElastictranscoderPreset#display_aspect_ratio}.'''
        result = self._values.get("display_aspect_ratio")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def fixed_gop(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#fixed_gop ElastictranscoderPreset#fixed_gop}.'''
        result = self._values.get("fixed_gop")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def frame_rate(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#frame_rate ElastictranscoderPreset#frame_rate}.'''
        result = self._values.get("frame_rate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def keyframes_max_dist(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#keyframes_max_dist ElastictranscoderPreset#keyframes_max_dist}.'''
        result = self._values.get("keyframes_max_dist")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_frame_rate(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#max_frame_rate ElastictranscoderPreset#max_frame_rate}.'''
        result = self._values.get("max_frame_rate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_height(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#max_height ElastictranscoderPreset#max_height}.'''
        result = self._values.get("max_height")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_width(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#max_width ElastictranscoderPreset#max_width}.'''
        result = self._values.get("max_width")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def padding_policy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#padding_policy ElastictranscoderPreset#padding_policy}.'''
        result = self._values.get("padding_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resolution(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#resolution ElastictranscoderPreset#resolution}.'''
        result = self._values.get("resolution")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sizing_policy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#sizing_policy ElastictranscoderPreset#sizing_policy}.'''
        result = self._values.get("sizing_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastictranscoderPresetVideo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElastictranscoderPresetVideoOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.elastictranscoderPreset.ElastictranscoderPresetVideoOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a9726155c81e95d319027f86b9c276eae19959d1f069eddfc2ea5b35fd67c498)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAspectRatio")
    def reset_aspect_ratio(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAspectRatio", []))

    @jsii.member(jsii_name="resetBitRate")
    def reset_bit_rate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBitRate", []))

    @jsii.member(jsii_name="resetCodec")
    def reset_codec(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCodec", []))

    @jsii.member(jsii_name="resetDisplayAspectRatio")
    def reset_display_aspect_ratio(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisplayAspectRatio", []))

    @jsii.member(jsii_name="resetFixedGop")
    def reset_fixed_gop(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFixedGop", []))

    @jsii.member(jsii_name="resetFrameRate")
    def reset_frame_rate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFrameRate", []))

    @jsii.member(jsii_name="resetKeyframesMaxDist")
    def reset_keyframes_max_dist(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyframesMaxDist", []))

    @jsii.member(jsii_name="resetMaxFrameRate")
    def reset_max_frame_rate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxFrameRate", []))

    @jsii.member(jsii_name="resetMaxHeight")
    def reset_max_height(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxHeight", []))

    @jsii.member(jsii_name="resetMaxWidth")
    def reset_max_width(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxWidth", []))

    @jsii.member(jsii_name="resetPaddingPolicy")
    def reset_padding_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPaddingPolicy", []))

    @jsii.member(jsii_name="resetResolution")
    def reset_resolution(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResolution", []))

    @jsii.member(jsii_name="resetSizingPolicy")
    def reset_sizing_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSizingPolicy", []))

    @builtins.property
    @jsii.member(jsii_name="aspectRatioInput")
    def aspect_ratio_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aspectRatioInput"))

    @builtins.property
    @jsii.member(jsii_name="bitRateInput")
    def bit_rate_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bitRateInput"))

    @builtins.property
    @jsii.member(jsii_name="codecInput")
    def codec_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "codecInput"))

    @builtins.property
    @jsii.member(jsii_name="displayAspectRatioInput")
    def display_aspect_ratio_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayAspectRatioInput"))

    @builtins.property
    @jsii.member(jsii_name="fixedGopInput")
    def fixed_gop_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fixedGopInput"))

    @builtins.property
    @jsii.member(jsii_name="frameRateInput")
    def frame_rate_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "frameRateInput"))

    @builtins.property
    @jsii.member(jsii_name="keyframesMaxDistInput")
    def keyframes_max_dist_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyframesMaxDistInput"))

    @builtins.property
    @jsii.member(jsii_name="maxFrameRateInput")
    def max_frame_rate_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxFrameRateInput"))

    @builtins.property
    @jsii.member(jsii_name="maxHeightInput")
    def max_height_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxHeightInput"))

    @builtins.property
    @jsii.member(jsii_name="maxWidthInput")
    def max_width_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxWidthInput"))

    @builtins.property
    @jsii.member(jsii_name="paddingPolicyInput")
    def padding_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "paddingPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="resolutionInput")
    def resolution_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resolutionInput"))

    @builtins.property
    @jsii.member(jsii_name="sizingPolicyInput")
    def sizing_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sizingPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="aspectRatio")
    def aspect_ratio(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "aspectRatio"))

    @aspect_ratio.setter
    def aspect_ratio(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4168892d784be21d4acf253bdab64283fed60a43811e8a8356b495f6547fcb7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "aspectRatio", value)

    @builtins.property
    @jsii.member(jsii_name="bitRate")
    def bit_rate(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bitRate"))

    @bit_rate.setter
    def bit_rate(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bca88d739cbd55a2faa1fc10a071843b03c8d561322b3df139fdb164808310ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bitRate", value)

    @builtins.property
    @jsii.member(jsii_name="codec")
    def codec(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "codec"))

    @codec.setter
    def codec(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8ac8c2d82163670810b4080f63adc4e24e24f2a30d8ee1433dfa38ac440fa7e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "codec", value)

    @builtins.property
    @jsii.member(jsii_name="displayAspectRatio")
    def display_aspect_ratio(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayAspectRatio"))

    @display_aspect_ratio.setter
    def display_aspect_ratio(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b4a46801040cc88971bc968f34e3c3f6f9bd7070046116f00750049196ed58f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayAspectRatio", value)

    @builtins.property
    @jsii.member(jsii_name="fixedGop")
    def fixed_gop(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fixedGop"))

    @fixed_gop.setter
    def fixed_gop(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35cf3343a998c27d8c6084d34a190523d6c893bfb4fcb3080777fc9208c33c8a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fixedGop", value)

    @builtins.property
    @jsii.member(jsii_name="frameRate")
    def frame_rate(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "frameRate"))

    @frame_rate.setter
    def frame_rate(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39ad4404d53b429740d700f830cb79e8cb3eea28312f6a58419453c631ad4ba1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "frameRate", value)

    @builtins.property
    @jsii.member(jsii_name="keyframesMaxDist")
    def keyframes_max_dist(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyframesMaxDist"))

    @keyframes_max_dist.setter
    def keyframes_max_dist(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e02535e5f943f67487055ef04afbab4ed2aca9cbdda7fabacce0f403df311d88)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyframesMaxDist", value)

    @builtins.property
    @jsii.member(jsii_name="maxFrameRate")
    def max_frame_rate(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maxFrameRate"))

    @max_frame_rate.setter
    def max_frame_rate(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cbb4d9dfba6ba3ca12bbaa7c63b36ad2b5dd38ed98c830afbfd5329dc48a8419)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxFrameRate", value)

    @builtins.property
    @jsii.member(jsii_name="maxHeight")
    def max_height(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maxHeight"))

    @max_height.setter
    def max_height(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6e9b1cbad86b2e9d46c831c3bfae20a8e98ab42e9124599a3e479ef9d8dbcbe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxHeight", value)

    @builtins.property
    @jsii.member(jsii_name="maxWidth")
    def max_width(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maxWidth"))

    @max_width.setter
    def max_width(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6623d7b193b2216f266ec9b35808754bbfe98e302b63e02d9aa1687341d72f62)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxWidth", value)

    @builtins.property
    @jsii.member(jsii_name="paddingPolicy")
    def padding_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "paddingPolicy"))

    @padding_policy.setter
    def padding_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3be5fa3b0440628b5a4d9edf61a399ee5575c8ff3823675f6390bba05748559)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "paddingPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="resolution")
    def resolution(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resolution"))

    @resolution.setter
    def resolution(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__029ecc51b520afe8ea86b2695eda2bab202dc50229dec20417b80d5493bac788)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resolution", value)

    @builtins.property
    @jsii.member(jsii_name="sizingPolicy")
    def sizing_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sizingPolicy"))

    @sizing_policy.setter
    def sizing_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d6b15a3bd65e75d7f416d39398f86af87f5b3c659f5497ee4342df688209c8b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sizingPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ElastictranscoderPresetVideo]:
        return typing.cast(typing.Optional[ElastictranscoderPresetVideo], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ElastictranscoderPresetVideo],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19f5bab04176aa2db3fb5bc4e724efc1e4687d0c536320cba1a70bba56806c77)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.elastictranscoderPreset.ElastictranscoderPresetVideoWatermarks",
    jsii_struct_bases=[],
    name_mapping={
        "horizontal_align": "horizontalAlign",
        "horizontal_offset": "horizontalOffset",
        "id": "id",
        "max_height": "maxHeight",
        "max_width": "maxWidth",
        "opacity": "opacity",
        "sizing_policy": "sizingPolicy",
        "target": "target",
        "vertical_align": "verticalAlign",
        "vertical_offset": "verticalOffset",
    },
)
class ElastictranscoderPresetVideoWatermarks:
    def __init__(
        self,
        *,
        horizontal_align: typing.Optional[builtins.str] = None,
        horizontal_offset: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        max_height: typing.Optional[builtins.str] = None,
        max_width: typing.Optional[builtins.str] = None,
        opacity: typing.Optional[builtins.str] = None,
        sizing_policy: typing.Optional[builtins.str] = None,
        target: typing.Optional[builtins.str] = None,
        vertical_align: typing.Optional[builtins.str] = None,
        vertical_offset: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param horizontal_align: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#horizontal_align ElastictranscoderPreset#horizontal_align}.
        :param horizontal_offset: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#horizontal_offset ElastictranscoderPreset#horizontal_offset}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#id ElastictranscoderPreset#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param max_height: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#max_height ElastictranscoderPreset#max_height}.
        :param max_width: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#max_width ElastictranscoderPreset#max_width}.
        :param opacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#opacity ElastictranscoderPreset#opacity}.
        :param sizing_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#sizing_policy ElastictranscoderPreset#sizing_policy}.
        :param target: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#target ElastictranscoderPreset#target}.
        :param vertical_align: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#vertical_align ElastictranscoderPreset#vertical_align}.
        :param vertical_offset: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#vertical_offset ElastictranscoderPreset#vertical_offset}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98dd6f4ce8b10afe8237a5bf660266d03d594758705d5a82b33064ebafb2c30e)
            check_type(argname="argument horizontal_align", value=horizontal_align, expected_type=type_hints["horizontal_align"])
            check_type(argname="argument horizontal_offset", value=horizontal_offset, expected_type=type_hints["horizontal_offset"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument max_height", value=max_height, expected_type=type_hints["max_height"])
            check_type(argname="argument max_width", value=max_width, expected_type=type_hints["max_width"])
            check_type(argname="argument opacity", value=opacity, expected_type=type_hints["opacity"])
            check_type(argname="argument sizing_policy", value=sizing_policy, expected_type=type_hints["sizing_policy"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument vertical_align", value=vertical_align, expected_type=type_hints["vertical_align"])
            check_type(argname="argument vertical_offset", value=vertical_offset, expected_type=type_hints["vertical_offset"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if horizontal_align is not None:
            self._values["horizontal_align"] = horizontal_align
        if horizontal_offset is not None:
            self._values["horizontal_offset"] = horizontal_offset
        if id is not None:
            self._values["id"] = id
        if max_height is not None:
            self._values["max_height"] = max_height
        if max_width is not None:
            self._values["max_width"] = max_width
        if opacity is not None:
            self._values["opacity"] = opacity
        if sizing_policy is not None:
            self._values["sizing_policy"] = sizing_policy
        if target is not None:
            self._values["target"] = target
        if vertical_align is not None:
            self._values["vertical_align"] = vertical_align
        if vertical_offset is not None:
            self._values["vertical_offset"] = vertical_offset

    @builtins.property
    def horizontal_align(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#horizontal_align ElastictranscoderPreset#horizontal_align}.'''
        result = self._values.get("horizontal_align")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def horizontal_offset(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#horizontal_offset ElastictranscoderPreset#horizontal_offset}.'''
        result = self._values.get("horizontal_offset")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#id ElastictranscoderPreset#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_height(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#max_height ElastictranscoderPreset#max_height}.'''
        result = self._values.get("max_height")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_width(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#max_width ElastictranscoderPreset#max_width}.'''
        result = self._values.get("max_width")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def opacity(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#opacity ElastictranscoderPreset#opacity}.'''
        result = self._values.get("opacity")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sizing_policy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#sizing_policy ElastictranscoderPreset#sizing_policy}.'''
        result = self._values.get("sizing_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#target ElastictranscoderPreset#target}.'''
        result = self._values.get("target")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vertical_align(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#vertical_align ElastictranscoderPreset#vertical_align}.'''
        result = self._values.get("vertical_align")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vertical_offset(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#vertical_offset ElastictranscoderPreset#vertical_offset}.'''
        result = self._values.get("vertical_offset")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastictranscoderPresetVideoWatermarks(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElastictranscoderPresetVideoWatermarksList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.elastictranscoderPreset.ElastictranscoderPresetVideoWatermarksList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7e7242c6c76d020ad06d6b60649202a4f3d19f00023f8133d6344884d92cb153)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ElastictranscoderPresetVideoWatermarksOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f4b6cf7abd295a79a95e5316c0956fd0b1cdef7f6ad7d3f42768c0d540d87bc)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ElastictranscoderPresetVideoWatermarksOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b9fa17fec1ba5ac039df95bced161b5bfbae06b28c468f2daf482da769e277a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6f1961762293b5b7f4523815ada997afd645b6485f92ba7a843002330fb5ce9e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__de95d170a1b8b4c8073083614ec3e49ca63304c61fdc19054e3a5b2729652feb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ElastictranscoderPresetVideoWatermarks]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ElastictranscoderPresetVideoWatermarks]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ElastictranscoderPresetVideoWatermarks]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c258b09485b6d8775b5ecaa054098d8424118c42675864870bdb4bf0af7f67e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElastictranscoderPresetVideoWatermarksOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.elastictranscoderPreset.ElastictranscoderPresetVideoWatermarksOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__65d8e6a19971525f39eb731fe30f657e71059f2f7a5022949a401ab22df8f181)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetHorizontalAlign")
    def reset_horizontal_align(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHorizontalAlign", []))

    @jsii.member(jsii_name="resetHorizontalOffset")
    def reset_horizontal_offset(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHorizontalOffset", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMaxHeight")
    def reset_max_height(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxHeight", []))

    @jsii.member(jsii_name="resetMaxWidth")
    def reset_max_width(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxWidth", []))

    @jsii.member(jsii_name="resetOpacity")
    def reset_opacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOpacity", []))

    @jsii.member(jsii_name="resetSizingPolicy")
    def reset_sizing_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSizingPolicy", []))

    @jsii.member(jsii_name="resetTarget")
    def reset_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTarget", []))

    @jsii.member(jsii_name="resetVerticalAlign")
    def reset_vertical_align(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVerticalAlign", []))

    @jsii.member(jsii_name="resetVerticalOffset")
    def reset_vertical_offset(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVerticalOffset", []))

    @builtins.property
    @jsii.member(jsii_name="horizontalAlignInput")
    def horizontal_align_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "horizontalAlignInput"))

    @builtins.property
    @jsii.member(jsii_name="horizontalOffsetInput")
    def horizontal_offset_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "horizontalOffsetInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="maxHeightInput")
    def max_height_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxHeightInput"))

    @builtins.property
    @jsii.member(jsii_name="maxWidthInput")
    def max_width_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxWidthInput"))

    @builtins.property
    @jsii.member(jsii_name="opacityInput")
    def opacity_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "opacityInput"))

    @builtins.property
    @jsii.member(jsii_name="sizingPolicyInput")
    def sizing_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sizingPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="verticalAlignInput")
    def vertical_align_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "verticalAlignInput"))

    @builtins.property
    @jsii.member(jsii_name="verticalOffsetInput")
    def vertical_offset_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "verticalOffsetInput"))

    @builtins.property
    @jsii.member(jsii_name="horizontalAlign")
    def horizontal_align(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "horizontalAlign"))

    @horizontal_align.setter
    def horizontal_align(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18984473a2e2a32107215855e55fefc89d74ce7ef20130b6556d44d2d2ec4b50)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "horizontalAlign", value)

    @builtins.property
    @jsii.member(jsii_name="horizontalOffset")
    def horizontal_offset(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "horizontalOffset"))

    @horizontal_offset.setter
    def horizontal_offset(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2cb88b9246836abe3078ed435680e74c53536787d8068cd30214935590c3e25)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "horizontalOffset", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__48544f09438bda646dc0112c6f5fa66ead59c75a47f920e09cb7732a5d8657a4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="maxHeight")
    def max_height(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maxHeight"))

    @max_height.setter
    def max_height(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__628e05e0b02dee6ffce2d170da161089c940d71bc31b4399624c6e8e8a272ae3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxHeight", value)

    @builtins.property
    @jsii.member(jsii_name="maxWidth")
    def max_width(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maxWidth"))

    @max_width.setter
    def max_width(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8c403a14015efba3d7588d1920a854e83ffc389037929376790f47421a0fd6e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxWidth", value)

    @builtins.property
    @jsii.member(jsii_name="opacity")
    def opacity(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "opacity"))

    @opacity.setter
    def opacity(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6f56d5095454164881785982e4dbb6db2bc017e22e190b0d635325f159e5ba5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "opacity", value)

    @builtins.property
    @jsii.member(jsii_name="sizingPolicy")
    def sizing_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sizingPolicy"))

    @sizing_policy.setter
    def sizing_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b4273ea04c8581192754e1a9ee0b5f8422a29f87ff38d7302a048a1bfa9ecfb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sizingPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "target"))

    @target.setter
    def target(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a435b2189d0d12deaa0c093e759320a5b96a3aac72b3c8303b2a436ff6c75f1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "target", value)

    @builtins.property
    @jsii.member(jsii_name="verticalAlign")
    def vertical_align(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "verticalAlign"))

    @vertical_align.setter
    def vertical_align(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1269bdf1d4fd9934fe984704474acdd42ef62b26d4c443316dc73c1dc3e8bc8b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "verticalAlign", value)

    @builtins.property
    @jsii.member(jsii_name="verticalOffset")
    def vertical_offset(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "verticalOffset"))

    @vertical_offset.setter
    def vertical_offset(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5ec63fd8891de7d4c8775649b4a934860e8757c17bf5f1bd20be50844b23d53)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "verticalOffset", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ElastictranscoderPresetVideoWatermarks, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ElastictranscoderPresetVideoWatermarks, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ElastictranscoderPresetVideoWatermarks, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aca736a66e41e58da461e8155546467dc9bbddda6e85b01deeb584b4e3516b05)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ElastictranscoderPreset",
    "ElastictranscoderPresetAudio",
    "ElastictranscoderPresetAudioCodecOptions",
    "ElastictranscoderPresetAudioCodecOptionsOutputReference",
    "ElastictranscoderPresetAudioOutputReference",
    "ElastictranscoderPresetConfig",
    "ElastictranscoderPresetThumbnails",
    "ElastictranscoderPresetThumbnailsOutputReference",
    "ElastictranscoderPresetVideo",
    "ElastictranscoderPresetVideoOutputReference",
    "ElastictranscoderPresetVideoWatermarks",
    "ElastictranscoderPresetVideoWatermarksList",
    "ElastictranscoderPresetVideoWatermarksOutputReference",
]

publication.publish()

def _typecheckingstub__10ef401fd3963f9db42ea789f76e13b7b11aacd7699b07c8880228e9bc43b8f5(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    container: builtins.str,
    audio: typing.Optional[typing.Union[ElastictranscoderPresetAudio, typing.Dict[builtins.str, typing.Any]]] = None,
    audio_codec_options: typing.Optional[typing.Union[ElastictranscoderPresetAudioCodecOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    description: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    thumbnails: typing.Optional[typing.Union[ElastictranscoderPresetThumbnails, typing.Dict[builtins.str, typing.Any]]] = None,
    type: typing.Optional[builtins.str] = None,
    video: typing.Optional[typing.Union[ElastictranscoderPresetVideo, typing.Dict[builtins.str, typing.Any]]] = None,
    video_codec_options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    video_watermarks: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ElastictranscoderPresetVideoWatermarks, typing.Dict[builtins.str, typing.Any]]]]] = None,
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

def _typecheckingstub__af43dc071b33424a01edac5501889ccac7a31677274be0c9243b252cf0048f2d(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ElastictranscoderPresetVideoWatermarks, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76853a538e211d84637eea667f6a0941ea72d0d2ea644253be248583154ee499(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18bbcf6157d2ad789562dbe87568bbd05800089dbcbc3e1fe45e6f05896c04af(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ddfc3ddcf107ee55b4e160b52eb687816546d5e4d6e540928ab7974efc5cd4fa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__acdac5343727ccf0f8d8f949bb70d683840c7fce43a151bb7341f27be6ece359(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a615e34df50c50b4864fe2d6eb9e3213049f861ec25211271c9237e85cd45fa2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ad151199cddc0e2c081193845bd67d9052bdc4be04ed090616ba614e8db1049(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07ad60d23a4091e127dbcc2ab27445c99b4a135bfb48f274b22640525960f4f7(
    *,
    audio_packing_mode: typing.Optional[builtins.str] = None,
    bit_rate: typing.Optional[builtins.str] = None,
    channels: typing.Optional[builtins.str] = None,
    codec: typing.Optional[builtins.str] = None,
    sample_rate: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b655f414e27186cbb98c757125a690902c2683c9c2d05f9ee885e1d184a2fddc(
    *,
    bit_depth: typing.Optional[builtins.str] = None,
    bit_order: typing.Optional[builtins.str] = None,
    profile: typing.Optional[builtins.str] = None,
    signed: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce502d0f76105e7b958837c796d54138a4597051e65988091b4fd9a56baf1f7b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73a6efb93dd83f2ca4b12c25674eb6ac92ecc8fb67b673fa706e3192f1e62163(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64e8a98fc511d3806984c91f61e7babe011f396eaa14662ee417d34db45142e9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ac5aa1edbf48cff6f813fb33c7cb75138600d04b2f740c453eabd0eddd4e186(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b901e52cfbaa3358a5eacd45135b200b91a02c0f9d0aa863289ef61dbf996a7f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2267d06f3262e918526319b9d1394596f8938e61308c4f878ab62923fd7ca6dc(
    value: typing.Optional[ElastictranscoderPresetAudioCodecOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__989b8032c8ba76c8252013548473f21fc07a83fe7c6632afd3f60d96bcf6de68(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09293015ac2173a3c401ba2657a38214804f81a7e5ac72e246d14fd0bd821008(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1bcdf8fde74ad21a29536b4637ffd9ad250c8096d1c5fa0b667261c54a82a86f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__244c623aa93fea8f4b0c39a863508287b079423034afabaed0762aa063dc0e90(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c37c45ef408c9b5ea39be76c07ab0a2649aa72564c706b952a34b9961d313152(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f667169ddfeb9b845bfeae0cf8aeed0332ba8c3eb01007bea6ac8ff0a8927361(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28ca5b21f15e06d4b313746731cae7922128a7b4f7175a663610fb7a9467ba8b(
    value: typing.Optional[ElastictranscoderPresetAudio],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0c9efa688ab2dde752f3a134d257d76427b986e801723dddb7051fac736b301(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    container: builtins.str,
    audio: typing.Optional[typing.Union[ElastictranscoderPresetAudio, typing.Dict[builtins.str, typing.Any]]] = None,
    audio_codec_options: typing.Optional[typing.Union[ElastictranscoderPresetAudioCodecOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    description: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    thumbnails: typing.Optional[typing.Union[ElastictranscoderPresetThumbnails, typing.Dict[builtins.str, typing.Any]]] = None,
    type: typing.Optional[builtins.str] = None,
    video: typing.Optional[typing.Union[ElastictranscoderPresetVideo, typing.Dict[builtins.str, typing.Any]]] = None,
    video_codec_options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    video_watermarks: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ElastictranscoderPresetVideoWatermarks, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89692e9001d68018a2ff568658e7f7c5b70dd654385f415569a2fc355479baec(
    *,
    aspect_ratio: typing.Optional[builtins.str] = None,
    format: typing.Optional[builtins.str] = None,
    interval: typing.Optional[builtins.str] = None,
    max_height: typing.Optional[builtins.str] = None,
    max_width: typing.Optional[builtins.str] = None,
    padding_policy: typing.Optional[builtins.str] = None,
    resolution: typing.Optional[builtins.str] = None,
    sizing_policy: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc18a7be691959aa40876331606de8a7f5e9e239d717f4400c58f3391189d56e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e3a3319f2e6b76a44f00eed4bfa5715ba09a64a1817ef66e4f9b466d1774b1e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec3044316cb5352972fe7dfd3df41815745481dd11393e42b2068fe7dd7016b3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ccf43428725f9cf1aa14a58c5844e3b93fe5bc7481cbeb0ef2aafeddfc120569(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c355e27abcc51845d31db000deb2dbc92a854faba3b1d7ad8a2ffb91f17191ed(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__466e2a890d0536aa0d746d92f43a4839b4efc35047ff17ac7e709777a3f56a8b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c7ff74dc0c02303046a484e4ec8d2618c1bb8166b5f0ce0084b3a8f63798e6d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95993ed182c4eaa577e289b345271aad6b2482686f45232fbb1d8187d948b375(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85dd0cf8e2f4388dcff487e51bc1b13d0634f25b17358a07e35674e42110704c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__167d4857495263b4e70777af7f04ba8615057e6aeb42234e6149cf376691afa1(
    value: typing.Optional[ElastictranscoderPresetThumbnails],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__efe7e5a35a36d1dd151be1a1c3df6f9465903e2903c6e94f65fd0071769ff846(
    *,
    aspect_ratio: typing.Optional[builtins.str] = None,
    bit_rate: typing.Optional[builtins.str] = None,
    codec: typing.Optional[builtins.str] = None,
    display_aspect_ratio: typing.Optional[builtins.str] = None,
    fixed_gop: typing.Optional[builtins.str] = None,
    frame_rate: typing.Optional[builtins.str] = None,
    keyframes_max_dist: typing.Optional[builtins.str] = None,
    max_frame_rate: typing.Optional[builtins.str] = None,
    max_height: typing.Optional[builtins.str] = None,
    max_width: typing.Optional[builtins.str] = None,
    padding_policy: typing.Optional[builtins.str] = None,
    resolution: typing.Optional[builtins.str] = None,
    sizing_policy: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9726155c81e95d319027f86b9c276eae19959d1f069eddfc2ea5b35fd67c498(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4168892d784be21d4acf253bdab64283fed60a43811e8a8356b495f6547fcb7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bca88d739cbd55a2faa1fc10a071843b03c8d561322b3df139fdb164808310ec(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8ac8c2d82163670810b4080f63adc4e24e24f2a30d8ee1433dfa38ac440fa7e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b4a46801040cc88971bc968f34e3c3f6f9bd7070046116f00750049196ed58f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35cf3343a998c27d8c6084d34a190523d6c893bfb4fcb3080777fc9208c33c8a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39ad4404d53b429740d700f830cb79e8cb3eea28312f6a58419453c631ad4ba1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e02535e5f943f67487055ef04afbab4ed2aca9cbdda7fabacce0f403df311d88(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cbb4d9dfba6ba3ca12bbaa7c63b36ad2b5dd38ed98c830afbfd5329dc48a8419(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6e9b1cbad86b2e9d46c831c3bfae20a8e98ab42e9124599a3e479ef9d8dbcbe(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6623d7b193b2216f266ec9b35808754bbfe98e302b63e02d9aa1687341d72f62(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3be5fa3b0440628b5a4d9edf61a399ee5575c8ff3823675f6390bba05748559(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__029ecc51b520afe8ea86b2695eda2bab202dc50229dec20417b80d5493bac788(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d6b15a3bd65e75d7f416d39398f86af87f5b3c659f5497ee4342df688209c8b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19f5bab04176aa2db3fb5bc4e724efc1e4687d0c536320cba1a70bba56806c77(
    value: typing.Optional[ElastictranscoderPresetVideo],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98dd6f4ce8b10afe8237a5bf660266d03d594758705d5a82b33064ebafb2c30e(
    *,
    horizontal_align: typing.Optional[builtins.str] = None,
    horizontal_offset: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    max_height: typing.Optional[builtins.str] = None,
    max_width: typing.Optional[builtins.str] = None,
    opacity: typing.Optional[builtins.str] = None,
    sizing_policy: typing.Optional[builtins.str] = None,
    target: typing.Optional[builtins.str] = None,
    vertical_align: typing.Optional[builtins.str] = None,
    vertical_offset: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e7242c6c76d020ad06d6b60649202a4f3d19f00023f8133d6344884d92cb153(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f4b6cf7abd295a79a95e5316c0956fd0b1cdef7f6ad7d3f42768c0d540d87bc(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b9fa17fec1ba5ac039df95bced161b5bfbae06b28c468f2daf482da769e277a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f1961762293b5b7f4523815ada997afd645b6485f92ba7a843002330fb5ce9e(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de95d170a1b8b4c8073083614ec3e49ca63304c61fdc19054e3a5b2729652feb(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c258b09485b6d8775b5ecaa054098d8424118c42675864870bdb4bf0af7f67e(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ElastictranscoderPresetVideoWatermarks]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65d8e6a19971525f39eb731fe30f657e71059f2f7a5022949a401ab22df8f181(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18984473a2e2a32107215855e55fefc89d74ce7ef20130b6556d44d2d2ec4b50(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2cb88b9246836abe3078ed435680e74c53536787d8068cd30214935590c3e25(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48544f09438bda646dc0112c6f5fa66ead59c75a47f920e09cb7732a5d8657a4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__628e05e0b02dee6ffce2d170da161089c940d71bc31b4399624c6e8e8a272ae3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8c403a14015efba3d7588d1920a854e83ffc389037929376790f47421a0fd6e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6f56d5095454164881785982e4dbb6db2bc017e22e190b0d635325f159e5ba5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b4273ea04c8581192754e1a9ee0b5f8422a29f87ff38d7302a048a1bfa9ecfb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a435b2189d0d12deaa0c093e759320a5b96a3aac72b3c8303b2a436ff6c75f1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1269bdf1d4fd9934fe984704474acdd42ef62b26d4c443316dc73c1dc3e8bc8b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5ec63fd8891de7d4c8775649b4a934860e8757c17bf5f1bd20be50844b23d53(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aca736a66e41e58da461e8155546467dc9bbddda6e85b01deeb584b4e3516b05(
    value: typing.Optional[typing.Union[ElastictranscoderPresetVideoWatermarks, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
