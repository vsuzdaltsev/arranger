'''
# `aws_appstream_fleet`

Refer to the Terraform Registory for docs: [`aws_appstream_fleet`](https://www.terraform.io/docs/providers/aws/r/appstream_fleet).
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


class AppstreamFleet(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appstreamFleet.AppstreamFleet",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/appstream_fleet aws_appstream_fleet}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        compute_capacity: typing.Union["AppstreamFleetComputeCapacity", typing.Dict[builtins.str, typing.Any]],
        instance_type: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        disconnect_timeout_in_seconds: typing.Optional[jsii.Number] = None,
        display_name: typing.Optional[builtins.str] = None,
        domain_join_info: typing.Optional[typing.Union["AppstreamFleetDomainJoinInfo", typing.Dict[builtins.str, typing.Any]]] = None,
        enable_default_internet_access: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        fleet_type: typing.Optional[builtins.str] = None,
        iam_role_arn: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        idle_disconnect_timeout_in_seconds: typing.Optional[jsii.Number] = None,
        image_arn: typing.Optional[builtins.str] = None,
        image_name: typing.Optional[builtins.str] = None,
        max_user_duration_in_seconds: typing.Optional[jsii.Number] = None,
        stream_view: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        vpc_config: typing.Optional[typing.Union["AppstreamFleetVpcConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/appstream_fleet aws_appstream_fleet} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param compute_capacity: compute_capacity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_fleet#compute_capacity AppstreamFleet#compute_capacity}
        :param instance_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_fleet#instance_type AppstreamFleet#instance_type}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_fleet#name AppstreamFleet#name}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_fleet#description AppstreamFleet#description}.
        :param disconnect_timeout_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_fleet#disconnect_timeout_in_seconds AppstreamFleet#disconnect_timeout_in_seconds}.
        :param display_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_fleet#display_name AppstreamFleet#display_name}.
        :param domain_join_info: domain_join_info block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_fleet#domain_join_info AppstreamFleet#domain_join_info}
        :param enable_default_internet_access: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_fleet#enable_default_internet_access AppstreamFleet#enable_default_internet_access}.
        :param fleet_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_fleet#fleet_type AppstreamFleet#fleet_type}.
        :param iam_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_fleet#iam_role_arn AppstreamFleet#iam_role_arn}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_fleet#id AppstreamFleet#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param idle_disconnect_timeout_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_fleet#idle_disconnect_timeout_in_seconds AppstreamFleet#idle_disconnect_timeout_in_seconds}.
        :param image_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_fleet#image_arn AppstreamFleet#image_arn}.
        :param image_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_fleet#image_name AppstreamFleet#image_name}.
        :param max_user_duration_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_fleet#max_user_duration_in_seconds AppstreamFleet#max_user_duration_in_seconds}.
        :param stream_view: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_fleet#stream_view AppstreamFleet#stream_view}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_fleet#tags AppstreamFleet#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_fleet#tags_all AppstreamFleet#tags_all}.
        :param vpc_config: vpc_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_fleet#vpc_config AppstreamFleet#vpc_config}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e782992d3429815399a73af26a0cb8794b262dbc3c9133350e35dd0c7ddf5feb)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = AppstreamFleetConfig(
            compute_capacity=compute_capacity,
            instance_type=instance_type,
            name=name,
            description=description,
            disconnect_timeout_in_seconds=disconnect_timeout_in_seconds,
            display_name=display_name,
            domain_join_info=domain_join_info,
            enable_default_internet_access=enable_default_internet_access,
            fleet_type=fleet_type,
            iam_role_arn=iam_role_arn,
            id=id,
            idle_disconnect_timeout_in_seconds=idle_disconnect_timeout_in_seconds,
            image_arn=image_arn,
            image_name=image_name,
            max_user_duration_in_seconds=max_user_duration_in_seconds,
            stream_view=stream_view,
            tags=tags,
            tags_all=tags_all,
            vpc_config=vpc_config,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putComputeCapacity")
    def put_compute_capacity(self, *, desired_instances: jsii.Number) -> None:
        '''
        :param desired_instances: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_fleet#desired_instances AppstreamFleet#desired_instances}.
        '''
        value = AppstreamFleetComputeCapacity(desired_instances=desired_instances)

        return typing.cast(None, jsii.invoke(self, "putComputeCapacity", [value]))

    @jsii.member(jsii_name="putDomainJoinInfo")
    def put_domain_join_info(
        self,
        *,
        directory_name: typing.Optional[builtins.str] = None,
        organizational_unit_distinguished_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param directory_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_fleet#directory_name AppstreamFleet#directory_name}.
        :param organizational_unit_distinguished_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_fleet#organizational_unit_distinguished_name AppstreamFleet#organizational_unit_distinguished_name}.
        '''
        value = AppstreamFleetDomainJoinInfo(
            directory_name=directory_name,
            organizational_unit_distinguished_name=organizational_unit_distinguished_name,
        )

        return typing.cast(None, jsii.invoke(self, "putDomainJoinInfo", [value]))

    @jsii.member(jsii_name="putVpcConfig")
    def put_vpc_config(
        self,
        *,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_fleet#security_group_ids AppstreamFleet#security_group_ids}.
        :param subnet_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_fleet#subnet_ids AppstreamFleet#subnet_ids}.
        '''
        value = AppstreamFleetVpcConfig(
            security_group_ids=security_group_ids, subnet_ids=subnet_ids
        )

        return typing.cast(None, jsii.invoke(self, "putVpcConfig", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetDisconnectTimeoutInSeconds")
    def reset_disconnect_timeout_in_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisconnectTimeoutInSeconds", []))

    @jsii.member(jsii_name="resetDisplayName")
    def reset_display_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisplayName", []))

    @jsii.member(jsii_name="resetDomainJoinInfo")
    def reset_domain_join_info(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDomainJoinInfo", []))

    @jsii.member(jsii_name="resetEnableDefaultInternetAccess")
    def reset_enable_default_internet_access(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableDefaultInternetAccess", []))

    @jsii.member(jsii_name="resetFleetType")
    def reset_fleet_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFleetType", []))

    @jsii.member(jsii_name="resetIamRoleArn")
    def reset_iam_role_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIamRoleArn", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIdleDisconnectTimeoutInSeconds")
    def reset_idle_disconnect_timeout_in_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdleDisconnectTimeoutInSeconds", []))

    @jsii.member(jsii_name="resetImageArn")
    def reset_image_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImageArn", []))

    @jsii.member(jsii_name="resetImageName")
    def reset_image_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImageName", []))

    @jsii.member(jsii_name="resetMaxUserDurationInSeconds")
    def reset_max_user_duration_in_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxUserDurationInSeconds", []))

    @jsii.member(jsii_name="resetStreamView")
    def reset_stream_view(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStreamView", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetVpcConfig")
    def reset_vpc_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVpcConfig", []))

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
    @jsii.member(jsii_name="computeCapacity")
    def compute_capacity(self) -> "AppstreamFleetComputeCapacityOutputReference":
        return typing.cast("AppstreamFleetComputeCapacityOutputReference", jsii.get(self, "computeCapacity"))

    @builtins.property
    @jsii.member(jsii_name="createdTime")
    def created_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdTime"))

    @builtins.property
    @jsii.member(jsii_name="domainJoinInfo")
    def domain_join_info(self) -> "AppstreamFleetDomainJoinInfoOutputReference":
        return typing.cast("AppstreamFleetDomainJoinInfoOutputReference", jsii.get(self, "domainJoinInfo"))

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @builtins.property
    @jsii.member(jsii_name="vpcConfig")
    def vpc_config(self) -> "AppstreamFleetVpcConfigOutputReference":
        return typing.cast("AppstreamFleetVpcConfigOutputReference", jsii.get(self, "vpcConfig"))

    @builtins.property
    @jsii.member(jsii_name="computeCapacityInput")
    def compute_capacity_input(
        self,
    ) -> typing.Optional["AppstreamFleetComputeCapacity"]:
        return typing.cast(typing.Optional["AppstreamFleetComputeCapacity"], jsii.get(self, "computeCapacityInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="disconnectTimeoutInSecondsInput")
    def disconnect_timeout_in_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "disconnectTimeoutInSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="displayNameInput")
    def display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="domainJoinInfoInput")
    def domain_join_info_input(self) -> typing.Optional["AppstreamFleetDomainJoinInfo"]:
        return typing.cast(typing.Optional["AppstreamFleetDomainJoinInfo"], jsii.get(self, "domainJoinInfoInput"))

    @builtins.property
    @jsii.member(jsii_name="enableDefaultInternetAccessInput")
    def enable_default_internet_access_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableDefaultInternetAccessInput"))

    @builtins.property
    @jsii.member(jsii_name="fleetTypeInput")
    def fleet_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fleetTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="iamRoleArnInput")
    def iam_role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "iamRoleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="idleDisconnectTimeoutInSecondsInput")
    def idle_disconnect_timeout_in_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "idleDisconnectTimeoutInSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="imageArnInput")
    def image_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageArnInput"))

    @builtins.property
    @jsii.member(jsii_name="imageNameInput")
    def image_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageNameInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceTypeInput")
    def instance_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="maxUserDurationInSecondsInput")
    def max_user_duration_in_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxUserDurationInSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="streamViewInput")
    def stream_view_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "streamViewInput"))

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
    @jsii.member(jsii_name="vpcConfigInput")
    def vpc_config_input(self) -> typing.Optional["AppstreamFleetVpcConfig"]:
        return typing.cast(typing.Optional["AppstreamFleetVpcConfig"], jsii.get(self, "vpcConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80cf322109fc61f1fdfbf130f157ae3075d95bd8875afb7d05c089ac9fbe6ffd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="disconnectTimeoutInSeconds")
    def disconnect_timeout_in_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "disconnectTimeoutInSeconds"))

    @disconnect_timeout_in_seconds.setter
    def disconnect_timeout_in_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe6f20cadc734846634a38fea0aa9b924baae06966f3c51a9f30f1d9749b51eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disconnectTimeoutInSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd178f8fdc85c54d0c2241713f5155072915627fb24c17a8cce908d28e332a9c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="enableDefaultInternetAccess")
    def enable_default_internet_access(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enableDefaultInternetAccess"))

    @enable_default_internet_access.setter
    def enable_default_internet_access(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44acbb78b7df46c70a0dcc1f003a87178149352ff527d03f5d91589f34308db9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableDefaultInternetAccess", value)

    @builtins.property
    @jsii.member(jsii_name="fleetType")
    def fleet_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fleetType"))

    @fleet_type.setter
    def fleet_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95d4ff6d2a0c3277cbadbfcd0ec9cac804c3ebf63ae1823469115c4a039bcdd4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fleetType", value)

    @builtins.property
    @jsii.member(jsii_name="iamRoleArn")
    def iam_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "iamRoleArn"))

    @iam_role_arn.setter
    def iam_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85a13f8570bd8760bddba6040038d08db2775d230ed6876c624f7c13ff16a064)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iamRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__226b38d49c8c689a1c9662ae8c8aec638f43205fa291e2083d71b52e02989590)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="idleDisconnectTimeoutInSeconds")
    def idle_disconnect_timeout_in_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "idleDisconnectTimeoutInSeconds"))

    @idle_disconnect_timeout_in_seconds.setter
    def idle_disconnect_timeout_in_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53fc13f0729bf7022a5065bb22520500c404c7855505e3c82c80c8c3af007c37)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "idleDisconnectTimeoutInSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="imageArn")
    def image_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "imageArn"))

    @image_arn.setter
    def image_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__28a129d6ec99c6b847f22c806f9a2a38ef68b8f66767e7e36e01344e2a82c4f9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageArn", value)

    @builtins.property
    @jsii.member(jsii_name="imageName")
    def image_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "imageName"))

    @image_name.setter
    def image_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9773d12d940d4fefbcb7e7c50845b8da6674437f85660ada451948343167b48a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageName", value)

    @builtins.property
    @jsii.member(jsii_name="instanceType")
    def instance_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceType"))

    @instance_type.setter
    def instance_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9cbb3ee8bc2dfd743dea2556f8d8277780265d7398b2704fedc7f511e1be2ccd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceType", value)

    @builtins.property
    @jsii.member(jsii_name="maxUserDurationInSeconds")
    def max_user_duration_in_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxUserDurationInSeconds"))

    @max_user_duration_in_seconds.setter
    def max_user_duration_in_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c556214a90a7cc0e7d4dd58ea5e94137c7075663f695a5650f9807ae2dc4229f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxUserDurationInSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78f0db5a6447f3c7bf112c852135eb8e88825c7cf91c7931bbac95505594e43e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="streamView")
    def stream_view(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "streamView"))

    @stream_view.setter
    def stream_view(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42c2808318a590c026741022592033bf9f90512fd68aff571a36cf63fa886ab1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "streamView", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a40ca8f52110f12ea66c17a1bcff7b2b92d073db264978f721d8c029bf7ccfcd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43b2702d04c771131feb95d0e66dcde31112111523794cce719e74e9186b9712)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)


@jsii.data_type(
    jsii_type="aws.appstreamFleet.AppstreamFleetComputeCapacity",
    jsii_struct_bases=[],
    name_mapping={"desired_instances": "desiredInstances"},
)
class AppstreamFleetComputeCapacity:
    def __init__(self, *, desired_instances: jsii.Number) -> None:
        '''
        :param desired_instances: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_fleet#desired_instances AppstreamFleet#desired_instances}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8a2ae398982ef2521641b5a25f2322d9668c925b51011277569f76dd567b331)
            check_type(argname="argument desired_instances", value=desired_instances, expected_type=type_hints["desired_instances"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "desired_instances": desired_instances,
        }

    @builtins.property
    def desired_instances(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_fleet#desired_instances AppstreamFleet#desired_instances}.'''
        result = self._values.get("desired_instances")
        assert result is not None, "Required property 'desired_instances' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppstreamFleetComputeCapacity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppstreamFleetComputeCapacityOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appstreamFleet.AppstreamFleetComputeCapacityOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0a53abfa779b83fb7c683fbac53db82434f6ebf8cf569c63ad3044d60672d74e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="available")
    def available(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "available"))

    @builtins.property
    @jsii.member(jsii_name="inUse")
    def in_use(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "inUse"))

    @builtins.property
    @jsii.member(jsii_name="running")
    def running(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "running"))

    @builtins.property
    @jsii.member(jsii_name="desiredInstancesInput")
    def desired_instances_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "desiredInstancesInput"))

    @builtins.property
    @jsii.member(jsii_name="desiredInstances")
    def desired_instances(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "desiredInstances"))

    @desired_instances.setter
    def desired_instances(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b5b6d02a6fc1275b9fbc119c192db395810b4503734f101befbb9c048cd42c8b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "desiredInstances", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppstreamFleetComputeCapacity]:
        return typing.cast(typing.Optional[AppstreamFleetComputeCapacity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppstreamFleetComputeCapacity],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e85caf096423a95b43bff912b3b52c45f4f3c2f4879a17d980ff6c96841c84e8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appstreamFleet.AppstreamFleetConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "compute_capacity": "computeCapacity",
        "instance_type": "instanceType",
        "name": "name",
        "description": "description",
        "disconnect_timeout_in_seconds": "disconnectTimeoutInSeconds",
        "display_name": "displayName",
        "domain_join_info": "domainJoinInfo",
        "enable_default_internet_access": "enableDefaultInternetAccess",
        "fleet_type": "fleetType",
        "iam_role_arn": "iamRoleArn",
        "id": "id",
        "idle_disconnect_timeout_in_seconds": "idleDisconnectTimeoutInSeconds",
        "image_arn": "imageArn",
        "image_name": "imageName",
        "max_user_duration_in_seconds": "maxUserDurationInSeconds",
        "stream_view": "streamView",
        "tags": "tags",
        "tags_all": "tagsAll",
        "vpc_config": "vpcConfig",
    },
)
class AppstreamFleetConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        compute_capacity: typing.Union[AppstreamFleetComputeCapacity, typing.Dict[builtins.str, typing.Any]],
        instance_type: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        disconnect_timeout_in_seconds: typing.Optional[jsii.Number] = None,
        display_name: typing.Optional[builtins.str] = None,
        domain_join_info: typing.Optional[typing.Union["AppstreamFleetDomainJoinInfo", typing.Dict[builtins.str, typing.Any]]] = None,
        enable_default_internet_access: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        fleet_type: typing.Optional[builtins.str] = None,
        iam_role_arn: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        idle_disconnect_timeout_in_seconds: typing.Optional[jsii.Number] = None,
        image_arn: typing.Optional[builtins.str] = None,
        image_name: typing.Optional[builtins.str] = None,
        max_user_duration_in_seconds: typing.Optional[jsii.Number] = None,
        stream_view: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        vpc_config: typing.Optional[typing.Union["AppstreamFleetVpcConfig", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param compute_capacity: compute_capacity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_fleet#compute_capacity AppstreamFleet#compute_capacity}
        :param instance_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_fleet#instance_type AppstreamFleet#instance_type}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_fleet#name AppstreamFleet#name}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_fleet#description AppstreamFleet#description}.
        :param disconnect_timeout_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_fleet#disconnect_timeout_in_seconds AppstreamFleet#disconnect_timeout_in_seconds}.
        :param display_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_fleet#display_name AppstreamFleet#display_name}.
        :param domain_join_info: domain_join_info block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_fleet#domain_join_info AppstreamFleet#domain_join_info}
        :param enable_default_internet_access: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_fleet#enable_default_internet_access AppstreamFleet#enable_default_internet_access}.
        :param fleet_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_fleet#fleet_type AppstreamFleet#fleet_type}.
        :param iam_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_fleet#iam_role_arn AppstreamFleet#iam_role_arn}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_fleet#id AppstreamFleet#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param idle_disconnect_timeout_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_fleet#idle_disconnect_timeout_in_seconds AppstreamFleet#idle_disconnect_timeout_in_seconds}.
        :param image_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_fleet#image_arn AppstreamFleet#image_arn}.
        :param image_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_fleet#image_name AppstreamFleet#image_name}.
        :param max_user_duration_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_fleet#max_user_duration_in_seconds AppstreamFleet#max_user_duration_in_seconds}.
        :param stream_view: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_fleet#stream_view AppstreamFleet#stream_view}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_fleet#tags AppstreamFleet#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_fleet#tags_all AppstreamFleet#tags_all}.
        :param vpc_config: vpc_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_fleet#vpc_config AppstreamFleet#vpc_config}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(compute_capacity, dict):
            compute_capacity = AppstreamFleetComputeCapacity(**compute_capacity)
        if isinstance(domain_join_info, dict):
            domain_join_info = AppstreamFleetDomainJoinInfo(**domain_join_info)
        if isinstance(vpc_config, dict):
            vpc_config = AppstreamFleetVpcConfig(**vpc_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__602b8f06f8c886d2a3bc3a910bf163a66f20e82eea4eabb897ee04071e3a04bc)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument compute_capacity", value=compute_capacity, expected_type=type_hints["compute_capacity"])
            check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument disconnect_timeout_in_seconds", value=disconnect_timeout_in_seconds, expected_type=type_hints["disconnect_timeout_in_seconds"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument domain_join_info", value=domain_join_info, expected_type=type_hints["domain_join_info"])
            check_type(argname="argument enable_default_internet_access", value=enable_default_internet_access, expected_type=type_hints["enable_default_internet_access"])
            check_type(argname="argument fleet_type", value=fleet_type, expected_type=type_hints["fleet_type"])
            check_type(argname="argument iam_role_arn", value=iam_role_arn, expected_type=type_hints["iam_role_arn"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument idle_disconnect_timeout_in_seconds", value=idle_disconnect_timeout_in_seconds, expected_type=type_hints["idle_disconnect_timeout_in_seconds"])
            check_type(argname="argument image_arn", value=image_arn, expected_type=type_hints["image_arn"])
            check_type(argname="argument image_name", value=image_name, expected_type=type_hints["image_name"])
            check_type(argname="argument max_user_duration_in_seconds", value=max_user_duration_in_seconds, expected_type=type_hints["max_user_duration_in_seconds"])
            check_type(argname="argument stream_view", value=stream_view, expected_type=type_hints["stream_view"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument vpc_config", value=vpc_config, expected_type=type_hints["vpc_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "compute_capacity": compute_capacity,
            "instance_type": instance_type,
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
        if description is not None:
            self._values["description"] = description
        if disconnect_timeout_in_seconds is not None:
            self._values["disconnect_timeout_in_seconds"] = disconnect_timeout_in_seconds
        if display_name is not None:
            self._values["display_name"] = display_name
        if domain_join_info is not None:
            self._values["domain_join_info"] = domain_join_info
        if enable_default_internet_access is not None:
            self._values["enable_default_internet_access"] = enable_default_internet_access
        if fleet_type is not None:
            self._values["fleet_type"] = fleet_type
        if iam_role_arn is not None:
            self._values["iam_role_arn"] = iam_role_arn
        if id is not None:
            self._values["id"] = id
        if idle_disconnect_timeout_in_seconds is not None:
            self._values["idle_disconnect_timeout_in_seconds"] = idle_disconnect_timeout_in_seconds
        if image_arn is not None:
            self._values["image_arn"] = image_arn
        if image_name is not None:
            self._values["image_name"] = image_name
        if max_user_duration_in_seconds is not None:
            self._values["max_user_duration_in_seconds"] = max_user_duration_in_seconds
        if stream_view is not None:
            self._values["stream_view"] = stream_view
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if vpc_config is not None:
            self._values["vpc_config"] = vpc_config

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
    def compute_capacity(self) -> AppstreamFleetComputeCapacity:
        '''compute_capacity block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_fleet#compute_capacity AppstreamFleet#compute_capacity}
        '''
        result = self._values.get("compute_capacity")
        assert result is not None, "Required property 'compute_capacity' is missing"
        return typing.cast(AppstreamFleetComputeCapacity, result)

    @builtins.property
    def instance_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_fleet#instance_type AppstreamFleet#instance_type}.'''
        result = self._values.get("instance_type")
        assert result is not None, "Required property 'instance_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_fleet#name AppstreamFleet#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_fleet#description AppstreamFleet#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disconnect_timeout_in_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_fleet#disconnect_timeout_in_seconds AppstreamFleet#disconnect_timeout_in_seconds}.'''
        result = self._values.get("disconnect_timeout_in_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def display_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_fleet#display_name AppstreamFleet#display_name}.'''
        result = self._values.get("display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def domain_join_info(self) -> typing.Optional["AppstreamFleetDomainJoinInfo"]:
        '''domain_join_info block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_fleet#domain_join_info AppstreamFleet#domain_join_info}
        '''
        result = self._values.get("domain_join_info")
        return typing.cast(typing.Optional["AppstreamFleetDomainJoinInfo"], result)

    @builtins.property
    def enable_default_internet_access(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_fleet#enable_default_internet_access AppstreamFleet#enable_default_internet_access}.'''
        result = self._values.get("enable_default_internet_access")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def fleet_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_fleet#fleet_type AppstreamFleet#fleet_type}.'''
        result = self._values.get("fleet_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def iam_role_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_fleet#iam_role_arn AppstreamFleet#iam_role_arn}.'''
        result = self._values.get("iam_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_fleet#id AppstreamFleet#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def idle_disconnect_timeout_in_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_fleet#idle_disconnect_timeout_in_seconds AppstreamFleet#idle_disconnect_timeout_in_seconds}.'''
        result = self._values.get("idle_disconnect_timeout_in_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def image_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_fleet#image_arn AppstreamFleet#image_arn}.'''
        result = self._values.get("image_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def image_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_fleet#image_name AppstreamFleet#image_name}.'''
        result = self._values.get("image_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_user_duration_in_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_fleet#max_user_duration_in_seconds AppstreamFleet#max_user_duration_in_seconds}.'''
        result = self._values.get("max_user_duration_in_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def stream_view(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_fleet#stream_view AppstreamFleet#stream_view}.'''
        result = self._values.get("stream_view")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_fleet#tags AppstreamFleet#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_fleet#tags_all AppstreamFleet#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def vpc_config(self) -> typing.Optional["AppstreamFleetVpcConfig"]:
        '''vpc_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_fleet#vpc_config AppstreamFleet#vpc_config}
        '''
        result = self._values.get("vpc_config")
        return typing.cast(typing.Optional["AppstreamFleetVpcConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppstreamFleetConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appstreamFleet.AppstreamFleetDomainJoinInfo",
    jsii_struct_bases=[],
    name_mapping={
        "directory_name": "directoryName",
        "organizational_unit_distinguished_name": "organizationalUnitDistinguishedName",
    },
)
class AppstreamFleetDomainJoinInfo:
    def __init__(
        self,
        *,
        directory_name: typing.Optional[builtins.str] = None,
        organizational_unit_distinguished_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param directory_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_fleet#directory_name AppstreamFleet#directory_name}.
        :param organizational_unit_distinguished_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_fleet#organizational_unit_distinguished_name AppstreamFleet#organizational_unit_distinguished_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0ed82dd6d48e57634ba5dee01181f2ff8a854fff0b388bf81856bfd21b76e75)
            check_type(argname="argument directory_name", value=directory_name, expected_type=type_hints["directory_name"])
            check_type(argname="argument organizational_unit_distinguished_name", value=organizational_unit_distinguished_name, expected_type=type_hints["organizational_unit_distinguished_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if directory_name is not None:
            self._values["directory_name"] = directory_name
        if organizational_unit_distinguished_name is not None:
            self._values["organizational_unit_distinguished_name"] = organizational_unit_distinguished_name

    @builtins.property
    def directory_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_fleet#directory_name AppstreamFleet#directory_name}.'''
        result = self._values.get("directory_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def organizational_unit_distinguished_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_fleet#organizational_unit_distinguished_name AppstreamFleet#organizational_unit_distinguished_name}.'''
        result = self._values.get("organizational_unit_distinguished_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppstreamFleetDomainJoinInfo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppstreamFleetDomainJoinInfoOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appstreamFleet.AppstreamFleetDomainJoinInfoOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8b9287e5fb85a0cecb99b56acb5ce73c7b44d3da81e150ce68da5b8e5b478fdd)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDirectoryName")
    def reset_directory_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDirectoryName", []))

    @jsii.member(jsii_name="resetOrganizationalUnitDistinguishedName")
    def reset_organizational_unit_distinguished_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOrganizationalUnitDistinguishedName", []))

    @builtins.property
    @jsii.member(jsii_name="directoryNameInput")
    def directory_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "directoryNameInput"))

    @builtins.property
    @jsii.member(jsii_name="organizationalUnitDistinguishedNameInput")
    def organizational_unit_distinguished_name_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "organizationalUnitDistinguishedNameInput"))

    @builtins.property
    @jsii.member(jsii_name="directoryName")
    def directory_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "directoryName"))

    @directory_name.setter
    def directory_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce2639b9f5716fb63f31b0db739e60f3c48bdd70120377701a0da6d034c51258)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "directoryName", value)

    @builtins.property
    @jsii.member(jsii_name="organizationalUnitDistinguishedName")
    def organizational_unit_distinguished_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "organizationalUnitDistinguishedName"))

    @organizational_unit_distinguished_name.setter
    def organizational_unit_distinguished_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__795466495ae2521f392dc32e514eeae5b45b039f757ae7f2a982cf74feaee803)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "organizationalUnitDistinguishedName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppstreamFleetDomainJoinInfo]:
        return typing.cast(typing.Optional[AppstreamFleetDomainJoinInfo], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppstreamFleetDomainJoinInfo],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7ca49cf5a79ddb80a5a6a67202184449b7016d5f2db5ce594053e2eb08d9c72)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appstreamFleet.AppstreamFleetVpcConfig",
    jsii_struct_bases=[],
    name_mapping={"security_group_ids": "securityGroupIds", "subnet_ids": "subnetIds"},
)
class AppstreamFleetVpcConfig:
    def __init__(
        self,
        *,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_fleet#security_group_ids AppstreamFleet#security_group_ids}.
        :param subnet_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_fleet#subnet_ids AppstreamFleet#subnet_ids}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d362eba2b7a10113ab243990e533bee87ce87545bd5673596feb5256174c1b88)
            check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
            check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if security_group_ids is not None:
            self._values["security_group_ids"] = security_group_ids
        if subnet_ids is not None:
            self._values["subnet_ids"] = subnet_ids

    @builtins.property
    def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_fleet#security_group_ids AppstreamFleet#security_group_ids}.'''
        result = self._values.get("security_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appstream_fleet#subnet_ids AppstreamFleet#subnet_ids}.'''
        result = self._values.get("subnet_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppstreamFleetVpcConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppstreamFleetVpcConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appstreamFleet.AppstreamFleetVpcConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0cc3d60f1c52602e8f5cc0a410357b7b0e18ecea20b27407a9fc89e0f04250ec)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetSecurityGroupIds")
    def reset_security_group_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecurityGroupIds", []))

    @jsii.member(jsii_name="resetSubnetIds")
    def reset_subnet_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubnetIds", []))

    @builtins.property
    @jsii.member(jsii_name="securityGroupIdsInput")
    def security_group_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityGroupIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetIdsInput")
    def subnet_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "subnetIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="securityGroupIds")
    def security_group_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "securityGroupIds"))

    @security_group_ids.setter
    def security_group_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6bc07994abce58a2fcf825561a7fac0654d0324f8ac9e516cff0bb27e4a48b3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroupIds", value)

    @builtins.property
    @jsii.member(jsii_name="subnetIds")
    def subnet_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subnetIds"))

    @subnet_ids.setter
    def subnet_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96cd616de8957976037098e1d73a96db22656ce7e54d7c5d020eb4d5a72768ba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetIds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppstreamFleetVpcConfig]:
        return typing.cast(typing.Optional[AppstreamFleetVpcConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[AppstreamFleetVpcConfig]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d03cf240f5bc6ba895151518d210f20c741c4a74aa8a407d1c43e3d337da74ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "AppstreamFleet",
    "AppstreamFleetComputeCapacity",
    "AppstreamFleetComputeCapacityOutputReference",
    "AppstreamFleetConfig",
    "AppstreamFleetDomainJoinInfo",
    "AppstreamFleetDomainJoinInfoOutputReference",
    "AppstreamFleetVpcConfig",
    "AppstreamFleetVpcConfigOutputReference",
]

publication.publish()

def _typecheckingstub__e782992d3429815399a73af26a0cb8794b262dbc3c9133350e35dd0c7ddf5feb(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    compute_capacity: typing.Union[AppstreamFleetComputeCapacity, typing.Dict[builtins.str, typing.Any]],
    instance_type: builtins.str,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    disconnect_timeout_in_seconds: typing.Optional[jsii.Number] = None,
    display_name: typing.Optional[builtins.str] = None,
    domain_join_info: typing.Optional[typing.Union[AppstreamFleetDomainJoinInfo, typing.Dict[builtins.str, typing.Any]]] = None,
    enable_default_internet_access: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    fleet_type: typing.Optional[builtins.str] = None,
    iam_role_arn: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    idle_disconnect_timeout_in_seconds: typing.Optional[jsii.Number] = None,
    image_arn: typing.Optional[builtins.str] = None,
    image_name: typing.Optional[builtins.str] = None,
    max_user_duration_in_seconds: typing.Optional[jsii.Number] = None,
    stream_view: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    vpc_config: typing.Optional[typing.Union[AppstreamFleetVpcConfig, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__80cf322109fc61f1fdfbf130f157ae3075d95bd8875afb7d05c089ac9fbe6ffd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe6f20cadc734846634a38fea0aa9b924baae06966f3c51a9f30f1d9749b51eb(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd178f8fdc85c54d0c2241713f5155072915627fb24c17a8cce908d28e332a9c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44acbb78b7df46c70a0dcc1f003a87178149352ff527d03f5d91589f34308db9(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95d4ff6d2a0c3277cbadbfcd0ec9cac804c3ebf63ae1823469115c4a039bcdd4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85a13f8570bd8760bddba6040038d08db2775d230ed6876c624f7c13ff16a064(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__226b38d49c8c689a1c9662ae8c8aec638f43205fa291e2083d71b52e02989590(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53fc13f0729bf7022a5065bb22520500c404c7855505e3c82c80c8c3af007c37(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28a129d6ec99c6b847f22c806f9a2a38ef68b8f66767e7e36e01344e2a82c4f9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9773d12d940d4fefbcb7e7c50845b8da6674437f85660ada451948343167b48a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9cbb3ee8bc2dfd743dea2556f8d8277780265d7398b2704fedc7f511e1be2ccd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c556214a90a7cc0e7d4dd58ea5e94137c7075663f695a5650f9807ae2dc4229f(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78f0db5a6447f3c7bf112c852135eb8e88825c7cf91c7931bbac95505594e43e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42c2808318a590c026741022592033bf9f90512fd68aff571a36cf63fa886ab1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a40ca8f52110f12ea66c17a1bcff7b2b92d073db264978f721d8c029bf7ccfcd(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43b2702d04c771131feb95d0e66dcde31112111523794cce719e74e9186b9712(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8a2ae398982ef2521641b5a25f2322d9668c925b51011277569f76dd567b331(
    *,
    desired_instances: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a53abfa779b83fb7c683fbac53db82434f6ebf8cf569c63ad3044d60672d74e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5b6d02a6fc1275b9fbc119c192db395810b4503734f101befbb9c048cd42c8b(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e85caf096423a95b43bff912b3b52c45f4f3c2f4879a17d980ff6c96841c84e8(
    value: typing.Optional[AppstreamFleetComputeCapacity],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__602b8f06f8c886d2a3bc3a910bf163a66f20e82eea4eabb897ee04071e3a04bc(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    compute_capacity: typing.Union[AppstreamFleetComputeCapacity, typing.Dict[builtins.str, typing.Any]],
    instance_type: builtins.str,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    disconnect_timeout_in_seconds: typing.Optional[jsii.Number] = None,
    display_name: typing.Optional[builtins.str] = None,
    domain_join_info: typing.Optional[typing.Union[AppstreamFleetDomainJoinInfo, typing.Dict[builtins.str, typing.Any]]] = None,
    enable_default_internet_access: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    fleet_type: typing.Optional[builtins.str] = None,
    iam_role_arn: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    idle_disconnect_timeout_in_seconds: typing.Optional[jsii.Number] = None,
    image_arn: typing.Optional[builtins.str] = None,
    image_name: typing.Optional[builtins.str] = None,
    max_user_duration_in_seconds: typing.Optional[jsii.Number] = None,
    stream_view: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    vpc_config: typing.Optional[typing.Union[AppstreamFleetVpcConfig, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0ed82dd6d48e57634ba5dee01181f2ff8a854fff0b388bf81856bfd21b76e75(
    *,
    directory_name: typing.Optional[builtins.str] = None,
    organizational_unit_distinguished_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b9287e5fb85a0cecb99b56acb5ce73c7b44d3da81e150ce68da5b8e5b478fdd(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce2639b9f5716fb63f31b0db739e60f3c48bdd70120377701a0da6d034c51258(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__795466495ae2521f392dc32e514eeae5b45b039f757ae7f2a982cf74feaee803(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7ca49cf5a79ddb80a5a6a67202184449b7016d5f2db5ce594053e2eb08d9c72(
    value: typing.Optional[AppstreamFleetDomainJoinInfo],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d362eba2b7a10113ab243990e533bee87ce87545bd5673596feb5256174c1b88(
    *,
    security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0cc3d60f1c52602e8f5cc0a410357b7b0e18ecea20b27407a9fc89e0f04250ec(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6bc07994abce58a2fcf825561a7fac0654d0324f8ac9e516cff0bb27e4a48b3(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96cd616de8957976037098e1d73a96db22656ce7e54d7c5d020eb4d5a72768ba(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d03cf240f5bc6ba895151518d210f20c741c4a74aa8a407d1c43e3d337da74ae(
    value: typing.Optional[AppstreamFleetVpcConfig],
) -> None:
    """Type checking stubs"""
    pass
