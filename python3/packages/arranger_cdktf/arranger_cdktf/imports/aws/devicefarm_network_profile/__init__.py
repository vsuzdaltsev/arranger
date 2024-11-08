'''
# `aws_devicefarm_network_profile`

Refer to the Terraform Registory for docs: [`aws_devicefarm_network_profile`](https://www.terraform.io/docs/providers/aws/r/devicefarm_network_profile).
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


class DevicefarmNetworkProfile(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.devicefarmNetworkProfile.DevicefarmNetworkProfile",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/devicefarm_network_profile aws_devicefarm_network_profile}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        project_arn: builtins.str,
        description: typing.Optional[builtins.str] = None,
        downlink_bandwidth_bits: typing.Optional[jsii.Number] = None,
        downlink_delay_ms: typing.Optional[jsii.Number] = None,
        downlink_jitter_ms: typing.Optional[jsii.Number] = None,
        downlink_loss_percent: typing.Optional[jsii.Number] = None,
        id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        type: typing.Optional[builtins.str] = None,
        uplink_bandwidth_bits: typing.Optional[jsii.Number] = None,
        uplink_delay_ms: typing.Optional[jsii.Number] = None,
        uplink_jitter_ms: typing.Optional[jsii.Number] = None,
        uplink_loss_percent: typing.Optional[jsii.Number] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/devicefarm_network_profile aws_devicefarm_network_profile} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/devicefarm_network_profile#name DevicefarmNetworkProfile#name}.
        :param project_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/devicefarm_network_profile#project_arn DevicefarmNetworkProfile#project_arn}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/devicefarm_network_profile#description DevicefarmNetworkProfile#description}.
        :param downlink_bandwidth_bits: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/devicefarm_network_profile#downlink_bandwidth_bits DevicefarmNetworkProfile#downlink_bandwidth_bits}.
        :param downlink_delay_ms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/devicefarm_network_profile#downlink_delay_ms DevicefarmNetworkProfile#downlink_delay_ms}.
        :param downlink_jitter_ms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/devicefarm_network_profile#downlink_jitter_ms DevicefarmNetworkProfile#downlink_jitter_ms}.
        :param downlink_loss_percent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/devicefarm_network_profile#downlink_loss_percent DevicefarmNetworkProfile#downlink_loss_percent}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/devicefarm_network_profile#id DevicefarmNetworkProfile#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/devicefarm_network_profile#tags DevicefarmNetworkProfile#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/devicefarm_network_profile#tags_all DevicefarmNetworkProfile#tags_all}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/devicefarm_network_profile#type DevicefarmNetworkProfile#type}.
        :param uplink_bandwidth_bits: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/devicefarm_network_profile#uplink_bandwidth_bits DevicefarmNetworkProfile#uplink_bandwidth_bits}.
        :param uplink_delay_ms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/devicefarm_network_profile#uplink_delay_ms DevicefarmNetworkProfile#uplink_delay_ms}.
        :param uplink_jitter_ms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/devicefarm_network_profile#uplink_jitter_ms DevicefarmNetworkProfile#uplink_jitter_ms}.
        :param uplink_loss_percent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/devicefarm_network_profile#uplink_loss_percent DevicefarmNetworkProfile#uplink_loss_percent}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c7ab8cfb828134435301b462b18fb4ea1a16a4347aceddae78b74c082fa7df5)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DevicefarmNetworkProfileConfig(
            name=name,
            project_arn=project_arn,
            description=description,
            downlink_bandwidth_bits=downlink_bandwidth_bits,
            downlink_delay_ms=downlink_delay_ms,
            downlink_jitter_ms=downlink_jitter_ms,
            downlink_loss_percent=downlink_loss_percent,
            id=id,
            tags=tags,
            tags_all=tags_all,
            type=type,
            uplink_bandwidth_bits=uplink_bandwidth_bits,
            uplink_delay_ms=uplink_delay_ms,
            uplink_jitter_ms=uplink_jitter_ms,
            uplink_loss_percent=uplink_loss_percent,
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

    @jsii.member(jsii_name="resetDownlinkBandwidthBits")
    def reset_downlink_bandwidth_bits(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDownlinkBandwidthBits", []))

    @jsii.member(jsii_name="resetDownlinkDelayMs")
    def reset_downlink_delay_ms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDownlinkDelayMs", []))

    @jsii.member(jsii_name="resetDownlinkJitterMs")
    def reset_downlink_jitter_ms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDownlinkJitterMs", []))

    @jsii.member(jsii_name="resetDownlinkLossPercent")
    def reset_downlink_loss_percent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDownlinkLossPercent", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @jsii.member(jsii_name="resetUplinkBandwidthBits")
    def reset_uplink_bandwidth_bits(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUplinkBandwidthBits", []))

    @jsii.member(jsii_name="resetUplinkDelayMs")
    def reset_uplink_delay_ms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUplinkDelayMs", []))

    @jsii.member(jsii_name="resetUplinkJitterMs")
    def reset_uplink_jitter_ms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUplinkJitterMs", []))

    @jsii.member(jsii_name="resetUplinkLossPercent")
    def reset_uplink_loss_percent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUplinkLossPercent", []))

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
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="downlinkBandwidthBitsInput")
    def downlink_bandwidth_bits_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "downlinkBandwidthBitsInput"))

    @builtins.property
    @jsii.member(jsii_name="downlinkDelayMsInput")
    def downlink_delay_ms_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "downlinkDelayMsInput"))

    @builtins.property
    @jsii.member(jsii_name="downlinkJitterMsInput")
    def downlink_jitter_ms_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "downlinkJitterMsInput"))

    @builtins.property
    @jsii.member(jsii_name="downlinkLossPercentInput")
    def downlink_loss_percent_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "downlinkLossPercentInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="projectArnInput")
    def project_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectArnInput"))

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
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="uplinkBandwidthBitsInput")
    def uplink_bandwidth_bits_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "uplinkBandwidthBitsInput"))

    @builtins.property
    @jsii.member(jsii_name="uplinkDelayMsInput")
    def uplink_delay_ms_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "uplinkDelayMsInput"))

    @builtins.property
    @jsii.member(jsii_name="uplinkJitterMsInput")
    def uplink_jitter_ms_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "uplinkJitterMsInput"))

    @builtins.property
    @jsii.member(jsii_name="uplinkLossPercentInput")
    def uplink_loss_percent_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "uplinkLossPercentInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b93e39b585f9eeb5348af638f3eec2cd3d4c9c8ba2b4dd8a6a2d8c271416b09)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="downlinkBandwidthBits")
    def downlink_bandwidth_bits(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "downlinkBandwidthBits"))

    @downlink_bandwidth_bits.setter
    def downlink_bandwidth_bits(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f66d7e4eaeb2eb5d1dc86f9dd048948d40dca0763996cd8c1d6aeb198d7a274c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "downlinkBandwidthBits", value)

    @builtins.property
    @jsii.member(jsii_name="downlinkDelayMs")
    def downlink_delay_ms(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "downlinkDelayMs"))

    @downlink_delay_ms.setter
    def downlink_delay_ms(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f76495041c38bee056cb3269cabdbd6c20130f1bc2c76e52fab44dc793453c77)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "downlinkDelayMs", value)

    @builtins.property
    @jsii.member(jsii_name="downlinkJitterMs")
    def downlink_jitter_ms(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "downlinkJitterMs"))

    @downlink_jitter_ms.setter
    def downlink_jitter_ms(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a53c174963639b5b58d2e43cf31f37e2fdd96545de05505c02a0b1363602edde)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "downlinkJitterMs", value)

    @builtins.property
    @jsii.member(jsii_name="downlinkLossPercent")
    def downlink_loss_percent(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "downlinkLossPercent"))

    @downlink_loss_percent.setter
    def downlink_loss_percent(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5c12719524389a59462402ef815668f7100850a3a30afb6a26acefd0294353d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "downlinkLossPercent", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9bc6e7a0a7007d5c699c5d8fbb95416ab0fbf1451bcea2d9197484c035d44dc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__afddb90d3d6d6d2a47f4df153bc8170a0fdc68cdfd2d80c0a899ead33db5190b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="projectArn")
    def project_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "projectArn"))

    @project_arn.setter
    def project_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__389acadead701d580cb48e59e69a1d301e2f0c7079b6d2809b89b03a9c5c34fe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projectArn", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b481e040bef3d23e53bef4193c3826e173af589ed49c0fcdf1b3d1e5473ebeb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c956ac75c044c174a491fd24de18c5ea496e7961e668555d2b6ab854adbe544)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3d56639539ef225974739b5f3bb9072c87f1f2136784008f61e8cb3baa6ac36)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="uplinkBandwidthBits")
    def uplink_bandwidth_bits(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "uplinkBandwidthBits"))

    @uplink_bandwidth_bits.setter
    def uplink_bandwidth_bits(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9184fa89685a1261f86a219690fd5c23e8e1e7aee3321a633926270ba50a8a6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "uplinkBandwidthBits", value)

    @builtins.property
    @jsii.member(jsii_name="uplinkDelayMs")
    def uplink_delay_ms(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "uplinkDelayMs"))

    @uplink_delay_ms.setter
    def uplink_delay_ms(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c015dd91022debaa384fd2ff85544ecc99a2ec39f2fb37470f9fb339c36ad364)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "uplinkDelayMs", value)

    @builtins.property
    @jsii.member(jsii_name="uplinkJitterMs")
    def uplink_jitter_ms(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "uplinkJitterMs"))

    @uplink_jitter_ms.setter
    def uplink_jitter_ms(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0599edc798548c49dbe280e5fbd1e18fcb038fe8118881aac03b709badf68922)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "uplinkJitterMs", value)

    @builtins.property
    @jsii.member(jsii_name="uplinkLossPercent")
    def uplink_loss_percent(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "uplinkLossPercent"))

    @uplink_loss_percent.setter
    def uplink_loss_percent(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2b056c4c1bd7535b0a37d52c597094d069f4371cf61b642aeb00c1628aae2d1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "uplinkLossPercent", value)


@jsii.data_type(
    jsii_type="aws.devicefarmNetworkProfile.DevicefarmNetworkProfileConfig",
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
        "project_arn": "projectArn",
        "description": "description",
        "downlink_bandwidth_bits": "downlinkBandwidthBits",
        "downlink_delay_ms": "downlinkDelayMs",
        "downlink_jitter_ms": "downlinkJitterMs",
        "downlink_loss_percent": "downlinkLossPercent",
        "id": "id",
        "tags": "tags",
        "tags_all": "tagsAll",
        "type": "type",
        "uplink_bandwidth_bits": "uplinkBandwidthBits",
        "uplink_delay_ms": "uplinkDelayMs",
        "uplink_jitter_ms": "uplinkJitterMs",
        "uplink_loss_percent": "uplinkLossPercent",
    },
)
class DevicefarmNetworkProfileConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        project_arn: builtins.str,
        description: typing.Optional[builtins.str] = None,
        downlink_bandwidth_bits: typing.Optional[jsii.Number] = None,
        downlink_delay_ms: typing.Optional[jsii.Number] = None,
        downlink_jitter_ms: typing.Optional[jsii.Number] = None,
        downlink_loss_percent: typing.Optional[jsii.Number] = None,
        id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        type: typing.Optional[builtins.str] = None,
        uplink_bandwidth_bits: typing.Optional[jsii.Number] = None,
        uplink_delay_ms: typing.Optional[jsii.Number] = None,
        uplink_jitter_ms: typing.Optional[jsii.Number] = None,
        uplink_loss_percent: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/devicefarm_network_profile#name DevicefarmNetworkProfile#name}.
        :param project_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/devicefarm_network_profile#project_arn DevicefarmNetworkProfile#project_arn}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/devicefarm_network_profile#description DevicefarmNetworkProfile#description}.
        :param downlink_bandwidth_bits: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/devicefarm_network_profile#downlink_bandwidth_bits DevicefarmNetworkProfile#downlink_bandwidth_bits}.
        :param downlink_delay_ms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/devicefarm_network_profile#downlink_delay_ms DevicefarmNetworkProfile#downlink_delay_ms}.
        :param downlink_jitter_ms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/devicefarm_network_profile#downlink_jitter_ms DevicefarmNetworkProfile#downlink_jitter_ms}.
        :param downlink_loss_percent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/devicefarm_network_profile#downlink_loss_percent DevicefarmNetworkProfile#downlink_loss_percent}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/devicefarm_network_profile#id DevicefarmNetworkProfile#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/devicefarm_network_profile#tags DevicefarmNetworkProfile#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/devicefarm_network_profile#tags_all DevicefarmNetworkProfile#tags_all}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/devicefarm_network_profile#type DevicefarmNetworkProfile#type}.
        :param uplink_bandwidth_bits: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/devicefarm_network_profile#uplink_bandwidth_bits DevicefarmNetworkProfile#uplink_bandwidth_bits}.
        :param uplink_delay_ms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/devicefarm_network_profile#uplink_delay_ms DevicefarmNetworkProfile#uplink_delay_ms}.
        :param uplink_jitter_ms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/devicefarm_network_profile#uplink_jitter_ms DevicefarmNetworkProfile#uplink_jitter_ms}.
        :param uplink_loss_percent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/devicefarm_network_profile#uplink_loss_percent DevicefarmNetworkProfile#uplink_loss_percent}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f106273daea22aa0143a8d9d2c04b03384db678d9b0e5729f988155b110e4e4b)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument project_arn", value=project_arn, expected_type=type_hints["project_arn"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument downlink_bandwidth_bits", value=downlink_bandwidth_bits, expected_type=type_hints["downlink_bandwidth_bits"])
            check_type(argname="argument downlink_delay_ms", value=downlink_delay_ms, expected_type=type_hints["downlink_delay_ms"])
            check_type(argname="argument downlink_jitter_ms", value=downlink_jitter_ms, expected_type=type_hints["downlink_jitter_ms"])
            check_type(argname="argument downlink_loss_percent", value=downlink_loss_percent, expected_type=type_hints["downlink_loss_percent"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument uplink_bandwidth_bits", value=uplink_bandwidth_bits, expected_type=type_hints["uplink_bandwidth_bits"])
            check_type(argname="argument uplink_delay_ms", value=uplink_delay_ms, expected_type=type_hints["uplink_delay_ms"])
            check_type(argname="argument uplink_jitter_ms", value=uplink_jitter_ms, expected_type=type_hints["uplink_jitter_ms"])
            check_type(argname="argument uplink_loss_percent", value=uplink_loss_percent, expected_type=type_hints["uplink_loss_percent"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "project_arn": project_arn,
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
        if downlink_bandwidth_bits is not None:
            self._values["downlink_bandwidth_bits"] = downlink_bandwidth_bits
        if downlink_delay_ms is not None:
            self._values["downlink_delay_ms"] = downlink_delay_ms
        if downlink_jitter_ms is not None:
            self._values["downlink_jitter_ms"] = downlink_jitter_ms
        if downlink_loss_percent is not None:
            self._values["downlink_loss_percent"] = downlink_loss_percent
        if id is not None:
            self._values["id"] = id
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if type is not None:
            self._values["type"] = type
        if uplink_bandwidth_bits is not None:
            self._values["uplink_bandwidth_bits"] = uplink_bandwidth_bits
        if uplink_delay_ms is not None:
            self._values["uplink_delay_ms"] = uplink_delay_ms
        if uplink_jitter_ms is not None:
            self._values["uplink_jitter_ms"] = uplink_jitter_ms
        if uplink_loss_percent is not None:
            self._values["uplink_loss_percent"] = uplink_loss_percent

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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/devicefarm_network_profile#name DevicefarmNetworkProfile#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def project_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/devicefarm_network_profile#project_arn DevicefarmNetworkProfile#project_arn}.'''
        result = self._values.get("project_arn")
        assert result is not None, "Required property 'project_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/devicefarm_network_profile#description DevicefarmNetworkProfile#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def downlink_bandwidth_bits(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/devicefarm_network_profile#downlink_bandwidth_bits DevicefarmNetworkProfile#downlink_bandwidth_bits}.'''
        result = self._values.get("downlink_bandwidth_bits")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def downlink_delay_ms(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/devicefarm_network_profile#downlink_delay_ms DevicefarmNetworkProfile#downlink_delay_ms}.'''
        result = self._values.get("downlink_delay_ms")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def downlink_jitter_ms(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/devicefarm_network_profile#downlink_jitter_ms DevicefarmNetworkProfile#downlink_jitter_ms}.'''
        result = self._values.get("downlink_jitter_ms")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def downlink_loss_percent(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/devicefarm_network_profile#downlink_loss_percent DevicefarmNetworkProfile#downlink_loss_percent}.'''
        result = self._values.get("downlink_loss_percent")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/devicefarm_network_profile#id DevicefarmNetworkProfile#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/devicefarm_network_profile#tags DevicefarmNetworkProfile#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/devicefarm_network_profile#tags_all DevicefarmNetworkProfile#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/devicefarm_network_profile#type DevicefarmNetworkProfile#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def uplink_bandwidth_bits(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/devicefarm_network_profile#uplink_bandwidth_bits DevicefarmNetworkProfile#uplink_bandwidth_bits}.'''
        result = self._values.get("uplink_bandwidth_bits")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def uplink_delay_ms(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/devicefarm_network_profile#uplink_delay_ms DevicefarmNetworkProfile#uplink_delay_ms}.'''
        result = self._values.get("uplink_delay_ms")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def uplink_jitter_ms(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/devicefarm_network_profile#uplink_jitter_ms DevicefarmNetworkProfile#uplink_jitter_ms}.'''
        result = self._values.get("uplink_jitter_ms")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def uplink_loss_percent(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/devicefarm_network_profile#uplink_loss_percent DevicefarmNetworkProfile#uplink_loss_percent}.'''
        result = self._values.get("uplink_loss_percent")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DevicefarmNetworkProfileConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "DevicefarmNetworkProfile",
    "DevicefarmNetworkProfileConfig",
]

publication.publish()

def _typecheckingstub__7c7ab8cfb828134435301b462b18fb4ea1a16a4347aceddae78b74c082fa7df5(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    project_arn: builtins.str,
    description: typing.Optional[builtins.str] = None,
    downlink_bandwidth_bits: typing.Optional[jsii.Number] = None,
    downlink_delay_ms: typing.Optional[jsii.Number] = None,
    downlink_jitter_ms: typing.Optional[jsii.Number] = None,
    downlink_loss_percent: typing.Optional[jsii.Number] = None,
    id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    type: typing.Optional[builtins.str] = None,
    uplink_bandwidth_bits: typing.Optional[jsii.Number] = None,
    uplink_delay_ms: typing.Optional[jsii.Number] = None,
    uplink_jitter_ms: typing.Optional[jsii.Number] = None,
    uplink_loss_percent: typing.Optional[jsii.Number] = None,
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

def _typecheckingstub__4b93e39b585f9eeb5348af638f3eec2cd3d4c9c8ba2b4dd8a6a2d8c271416b09(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f66d7e4eaeb2eb5d1dc86f9dd048948d40dca0763996cd8c1d6aeb198d7a274c(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f76495041c38bee056cb3269cabdbd6c20130f1bc2c76e52fab44dc793453c77(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a53c174963639b5b58d2e43cf31f37e2fdd96545de05505c02a0b1363602edde(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5c12719524389a59462402ef815668f7100850a3a30afb6a26acefd0294353d(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9bc6e7a0a7007d5c699c5d8fbb95416ab0fbf1451bcea2d9197484c035d44dc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afddb90d3d6d6d2a47f4df153bc8170a0fdc68cdfd2d80c0a899ead33db5190b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__389acadead701d580cb48e59e69a1d301e2f0c7079b6d2809b89b03a9c5c34fe(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b481e040bef3d23e53bef4193c3826e173af589ed49c0fcdf1b3d1e5473ebeb(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c956ac75c044c174a491fd24de18c5ea496e7961e668555d2b6ab854adbe544(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3d56639539ef225974739b5f3bb9072c87f1f2136784008f61e8cb3baa6ac36(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9184fa89685a1261f86a219690fd5c23e8e1e7aee3321a633926270ba50a8a6(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c015dd91022debaa384fd2ff85544ecc99a2ec39f2fb37470f9fb339c36ad364(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0599edc798548c49dbe280e5fbd1e18fcb038fe8118881aac03b709badf68922(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2b056c4c1bd7535b0a37d52c597094d069f4371cf61b642aeb00c1628aae2d1(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f106273daea22aa0143a8d9d2c04b03384db678d9b0e5729f988155b110e4e4b(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: builtins.str,
    project_arn: builtins.str,
    description: typing.Optional[builtins.str] = None,
    downlink_bandwidth_bits: typing.Optional[jsii.Number] = None,
    downlink_delay_ms: typing.Optional[jsii.Number] = None,
    downlink_jitter_ms: typing.Optional[jsii.Number] = None,
    downlink_loss_percent: typing.Optional[jsii.Number] = None,
    id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    type: typing.Optional[builtins.str] = None,
    uplink_bandwidth_bits: typing.Optional[jsii.Number] = None,
    uplink_delay_ms: typing.Optional[jsii.Number] = None,
    uplink_jitter_ms: typing.Optional[jsii.Number] = None,
    uplink_loss_percent: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass
