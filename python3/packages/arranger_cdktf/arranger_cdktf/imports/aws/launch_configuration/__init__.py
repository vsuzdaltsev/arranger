'''
# `aws_launch_configuration`

Refer to the Terraform Registory for docs: [`aws_launch_configuration`](https://www.terraform.io/docs/providers/aws/r/launch_configuration).
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


class LaunchConfiguration(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.launchConfiguration.LaunchConfiguration",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration aws_launch_configuration}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        image_id: builtins.str,
        instance_type: builtins.str,
        associate_public_ip_address: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        ebs_block_device: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LaunchConfigurationEbsBlockDevice", typing.Dict[builtins.str, typing.Any]]]]] = None,
        ebs_optimized: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_monitoring: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        ephemeral_block_device: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LaunchConfigurationEphemeralBlockDevice", typing.Dict[builtins.str, typing.Any]]]]] = None,
        iam_instance_profile: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        key_name: typing.Optional[builtins.str] = None,
        metadata_options: typing.Optional[typing.Union["LaunchConfigurationMetadataOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        name: typing.Optional[builtins.str] = None,
        name_prefix: typing.Optional[builtins.str] = None,
        placement_tenancy: typing.Optional[builtins.str] = None,
        root_block_device: typing.Optional[typing.Union["LaunchConfigurationRootBlockDevice", typing.Dict[builtins.str, typing.Any]]] = None,
        security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        spot_price: typing.Optional[builtins.str] = None,
        user_data: typing.Optional[builtins.str] = None,
        user_data_base64: typing.Optional[builtins.str] = None,
        vpc_classic_link_id: typing.Optional[builtins.str] = None,
        vpc_classic_link_security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration aws_launch_configuration} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param image_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#image_id LaunchConfiguration#image_id}.
        :param instance_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#instance_type LaunchConfiguration#instance_type}.
        :param associate_public_ip_address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#associate_public_ip_address LaunchConfiguration#associate_public_ip_address}.
        :param ebs_block_device: ebs_block_device block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#ebs_block_device LaunchConfiguration#ebs_block_device}
        :param ebs_optimized: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#ebs_optimized LaunchConfiguration#ebs_optimized}.
        :param enable_monitoring: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#enable_monitoring LaunchConfiguration#enable_monitoring}.
        :param ephemeral_block_device: ephemeral_block_device block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#ephemeral_block_device LaunchConfiguration#ephemeral_block_device}
        :param iam_instance_profile: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#iam_instance_profile LaunchConfiguration#iam_instance_profile}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#id LaunchConfiguration#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param key_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#key_name LaunchConfiguration#key_name}.
        :param metadata_options: metadata_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#metadata_options LaunchConfiguration#metadata_options}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#name LaunchConfiguration#name}.
        :param name_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#name_prefix LaunchConfiguration#name_prefix}.
        :param placement_tenancy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#placement_tenancy LaunchConfiguration#placement_tenancy}.
        :param root_block_device: root_block_device block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#root_block_device LaunchConfiguration#root_block_device}
        :param security_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#security_groups LaunchConfiguration#security_groups}.
        :param spot_price: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#spot_price LaunchConfiguration#spot_price}.
        :param user_data: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#user_data LaunchConfiguration#user_data}.
        :param user_data_base64: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#user_data_base64 LaunchConfiguration#user_data_base64}.
        :param vpc_classic_link_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#vpc_classic_link_id LaunchConfiguration#vpc_classic_link_id}.
        :param vpc_classic_link_security_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#vpc_classic_link_security_groups LaunchConfiguration#vpc_classic_link_security_groups}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ae94500549626be2ff7531a79a5a88c38d3c00888b29a837c84a3a13fa96b1a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = LaunchConfigurationConfig(
            image_id=image_id,
            instance_type=instance_type,
            associate_public_ip_address=associate_public_ip_address,
            ebs_block_device=ebs_block_device,
            ebs_optimized=ebs_optimized,
            enable_monitoring=enable_monitoring,
            ephemeral_block_device=ephemeral_block_device,
            iam_instance_profile=iam_instance_profile,
            id=id,
            key_name=key_name,
            metadata_options=metadata_options,
            name=name,
            name_prefix=name_prefix,
            placement_tenancy=placement_tenancy,
            root_block_device=root_block_device,
            security_groups=security_groups,
            spot_price=spot_price,
            user_data=user_data,
            user_data_base64=user_data_base64,
            vpc_classic_link_id=vpc_classic_link_id,
            vpc_classic_link_security_groups=vpc_classic_link_security_groups,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putEbsBlockDevice")
    def put_ebs_block_device(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LaunchConfigurationEbsBlockDevice", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9abdf965511cdd80605a2a2297ac13064f0a2089775a7cb6d1c103c10bbe9381)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putEbsBlockDevice", [value]))

    @jsii.member(jsii_name="putEphemeralBlockDevice")
    def put_ephemeral_block_device(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LaunchConfigurationEphemeralBlockDevice", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0f86b2e3ba0244305bb39729f0cf94f21092bdada1057e73ee4ef6a16ffbf78)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putEphemeralBlockDevice", [value]))

    @jsii.member(jsii_name="putMetadataOptions")
    def put_metadata_options(
        self,
        *,
        http_endpoint: typing.Optional[builtins.str] = None,
        http_put_response_hop_limit: typing.Optional[jsii.Number] = None,
        http_tokens: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param http_endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#http_endpoint LaunchConfiguration#http_endpoint}.
        :param http_put_response_hop_limit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#http_put_response_hop_limit LaunchConfiguration#http_put_response_hop_limit}.
        :param http_tokens: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#http_tokens LaunchConfiguration#http_tokens}.
        '''
        value = LaunchConfigurationMetadataOptions(
            http_endpoint=http_endpoint,
            http_put_response_hop_limit=http_put_response_hop_limit,
            http_tokens=http_tokens,
        )

        return typing.cast(None, jsii.invoke(self, "putMetadataOptions", [value]))

    @jsii.member(jsii_name="putRootBlockDevice")
    def put_root_block_device(
        self,
        *,
        delete_on_termination: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        encrypted: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        iops: typing.Optional[jsii.Number] = None,
        throughput: typing.Optional[jsii.Number] = None,
        volume_size: typing.Optional[jsii.Number] = None,
        volume_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param delete_on_termination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#delete_on_termination LaunchConfiguration#delete_on_termination}.
        :param encrypted: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#encrypted LaunchConfiguration#encrypted}.
        :param iops: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#iops LaunchConfiguration#iops}.
        :param throughput: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#throughput LaunchConfiguration#throughput}.
        :param volume_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#volume_size LaunchConfiguration#volume_size}.
        :param volume_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#volume_type LaunchConfiguration#volume_type}.
        '''
        value = LaunchConfigurationRootBlockDevice(
            delete_on_termination=delete_on_termination,
            encrypted=encrypted,
            iops=iops,
            throughput=throughput,
            volume_size=volume_size,
            volume_type=volume_type,
        )

        return typing.cast(None, jsii.invoke(self, "putRootBlockDevice", [value]))

    @jsii.member(jsii_name="resetAssociatePublicIpAddress")
    def reset_associate_public_ip_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAssociatePublicIpAddress", []))

    @jsii.member(jsii_name="resetEbsBlockDevice")
    def reset_ebs_block_device(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEbsBlockDevice", []))

    @jsii.member(jsii_name="resetEbsOptimized")
    def reset_ebs_optimized(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEbsOptimized", []))

    @jsii.member(jsii_name="resetEnableMonitoring")
    def reset_enable_monitoring(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableMonitoring", []))

    @jsii.member(jsii_name="resetEphemeralBlockDevice")
    def reset_ephemeral_block_device(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEphemeralBlockDevice", []))

    @jsii.member(jsii_name="resetIamInstanceProfile")
    def reset_iam_instance_profile(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIamInstanceProfile", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetKeyName")
    def reset_key_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyName", []))

    @jsii.member(jsii_name="resetMetadataOptions")
    def reset_metadata_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetadataOptions", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetNamePrefix")
    def reset_name_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamePrefix", []))

    @jsii.member(jsii_name="resetPlacementTenancy")
    def reset_placement_tenancy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPlacementTenancy", []))

    @jsii.member(jsii_name="resetRootBlockDevice")
    def reset_root_block_device(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRootBlockDevice", []))

    @jsii.member(jsii_name="resetSecurityGroups")
    def reset_security_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecurityGroups", []))

    @jsii.member(jsii_name="resetSpotPrice")
    def reset_spot_price(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSpotPrice", []))

    @jsii.member(jsii_name="resetUserData")
    def reset_user_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserData", []))

    @jsii.member(jsii_name="resetUserDataBase64")
    def reset_user_data_base64(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserDataBase64", []))

    @jsii.member(jsii_name="resetVpcClassicLinkId")
    def reset_vpc_classic_link_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVpcClassicLinkId", []))

    @jsii.member(jsii_name="resetVpcClassicLinkSecurityGroups")
    def reset_vpc_classic_link_security_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVpcClassicLinkSecurityGroups", []))

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
    @jsii.member(jsii_name="ebsBlockDevice")
    def ebs_block_device(self) -> "LaunchConfigurationEbsBlockDeviceList":
        return typing.cast("LaunchConfigurationEbsBlockDeviceList", jsii.get(self, "ebsBlockDevice"))

    @builtins.property
    @jsii.member(jsii_name="ephemeralBlockDevice")
    def ephemeral_block_device(self) -> "LaunchConfigurationEphemeralBlockDeviceList":
        return typing.cast("LaunchConfigurationEphemeralBlockDeviceList", jsii.get(self, "ephemeralBlockDevice"))

    @builtins.property
    @jsii.member(jsii_name="metadataOptions")
    def metadata_options(self) -> "LaunchConfigurationMetadataOptionsOutputReference":
        return typing.cast("LaunchConfigurationMetadataOptionsOutputReference", jsii.get(self, "metadataOptions"))

    @builtins.property
    @jsii.member(jsii_name="rootBlockDevice")
    def root_block_device(self) -> "LaunchConfigurationRootBlockDeviceOutputReference":
        return typing.cast("LaunchConfigurationRootBlockDeviceOutputReference", jsii.get(self, "rootBlockDevice"))

    @builtins.property
    @jsii.member(jsii_name="associatePublicIpAddressInput")
    def associate_public_ip_address_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "associatePublicIpAddressInput"))

    @builtins.property
    @jsii.member(jsii_name="ebsBlockDeviceInput")
    def ebs_block_device_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LaunchConfigurationEbsBlockDevice"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LaunchConfigurationEbsBlockDevice"]]], jsii.get(self, "ebsBlockDeviceInput"))

    @builtins.property
    @jsii.member(jsii_name="ebsOptimizedInput")
    def ebs_optimized_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "ebsOptimizedInput"))

    @builtins.property
    @jsii.member(jsii_name="enableMonitoringInput")
    def enable_monitoring_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableMonitoringInput"))

    @builtins.property
    @jsii.member(jsii_name="ephemeralBlockDeviceInput")
    def ephemeral_block_device_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LaunchConfigurationEphemeralBlockDevice"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LaunchConfigurationEphemeralBlockDevice"]]], jsii.get(self, "ephemeralBlockDeviceInput"))

    @builtins.property
    @jsii.member(jsii_name="iamInstanceProfileInput")
    def iam_instance_profile_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "iamInstanceProfileInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="imageIdInput")
    def image_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageIdInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceTypeInput")
    def instance_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="keyNameInput")
    def key_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyNameInput"))

    @builtins.property
    @jsii.member(jsii_name="metadataOptionsInput")
    def metadata_options_input(
        self,
    ) -> typing.Optional["LaunchConfigurationMetadataOptions"]:
        return typing.cast(typing.Optional["LaunchConfigurationMetadataOptions"], jsii.get(self, "metadataOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="namePrefixInput")
    def name_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namePrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="placementTenancyInput")
    def placement_tenancy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "placementTenancyInput"))

    @builtins.property
    @jsii.member(jsii_name="rootBlockDeviceInput")
    def root_block_device_input(
        self,
    ) -> typing.Optional["LaunchConfigurationRootBlockDevice"]:
        return typing.cast(typing.Optional["LaunchConfigurationRootBlockDevice"], jsii.get(self, "rootBlockDeviceInput"))

    @builtins.property
    @jsii.member(jsii_name="securityGroupsInput")
    def security_groups_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="spotPriceInput")
    def spot_price_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "spotPriceInput"))

    @builtins.property
    @jsii.member(jsii_name="userDataBase64Input")
    def user_data_base64_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userDataBase64Input"))

    @builtins.property
    @jsii.member(jsii_name="userDataInput")
    def user_data_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userDataInput"))

    @builtins.property
    @jsii.member(jsii_name="vpcClassicLinkIdInput")
    def vpc_classic_link_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vpcClassicLinkIdInput"))

    @builtins.property
    @jsii.member(jsii_name="vpcClassicLinkSecurityGroupsInput")
    def vpc_classic_link_security_groups_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "vpcClassicLinkSecurityGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="associatePublicIpAddress")
    def associate_public_ip_address(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "associatePublicIpAddress"))

    @associate_public_ip_address.setter
    def associate_public_ip_address(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__835b670aa51e466b59cc54dea74e46da1a1c1d825d614169f8065ce7a4c320d6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "associatePublicIpAddress", value)

    @builtins.property
    @jsii.member(jsii_name="ebsOptimized")
    def ebs_optimized(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "ebsOptimized"))

    @ebs_optimized.setter
    def ebs_optimized(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7dff581c93c8d85b3171914a8afef27c627b4ae72f700fe236bff8c0581d6cf6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ebsOptimized", value)

    @builtins.property
    @jsii.member(jsii_name="enableMonitoring")
    def enable_monitoring(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enableMonitoring"))

    @enable_monitoring.setter
    def enable_monitoring(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8440dcb66c07c8ce76abd8663da3408c77e221294446e632e487867909e55dc0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableMonitoring", value)

    @builtins.property
    @jsii.member(jsii_name="iamInstanceProfile")
    def iam_instance_profile(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "iamInstanceProfile"))

    @iam_instance_profile.setter
    def iam_instance_profile(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8eb0626ea3177c9ddec9ac3a095bc4c7be1a75bd08503e2c3534a029d89b7d7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iamInstanceProfile", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f5e4caabee12981d93d538cddaf66ce04a4e1f9bb617c5e71147797a4547df92)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="imageId")
    def image_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "imageId"))

    @image_id.setter
    def image_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09f96f4df954464fd0ba2bcca240eebeab7e344686472fac6a514cf994358881)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageId", value)

    @builtins.property
    @jsii.member(jsii_name="instanceType")
    def instance_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceType"))

    @instance_type.setter
    def instance_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d64a6feec08555eae824a9c2c56806ee6a6a64ab5472e152be1358c31ffb1c1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceType", value)

    @builtins.property
    @jsii.member(jsii_name="keyName")
    def key_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyName"))

    @key_name.setter
    def key_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b28f19ea17063b720d10e0c1248a4ff1fa16a845a0867fb01d1eeb74e83ffea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyName", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ffc96bc4817b197951a3fab3d675d7191961dcbd2a0a7f35fcf0fadbe3c6a850)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namePrefix")
    def name_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namePrefix"))

    @name_prefix.setter
    def name_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d685982e798c36fd3fe62630e64ddae0a629b50f8b13498d189952c2ee9620f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namePrefix", value)

    @builtins.property
    @jsii.member(jsii_name="placementTenancy")
    def placement_tenancy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "placementTenancy"))

    @placement_tenancy.setter
    def placement_tenancy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f7ab9fe3c02ac09592ae230b612ae94dc542e3ba64c3588600febe9d8a4dc73)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "placementTenancy", value)

    @builtins.property
    @jsii.member(jsii_name="securityGroups")
    def security_groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "securityGroups"))

    @security_groups.setter
    def security_groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ec40e260949ac58a70440201f1ea8e11ee6a01080dab6aac9b2934f71c7b553)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroups", value)

    @builtins.property
    @jsii.member(jsii_name="spotPrice")
    def spot_price(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "spotPrice"))

    @spot_price.setter
    def spot_price(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03ab86778ee7ca6605ac3f3ddce95d9e782c830e7945d65ba601ecb31534d1d9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "spotPrice", value)

    @builtins.property
    @jsii.member(jsii_name="userData")
    def user_data(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userData"))

    @user_data.setter
    def user_data(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dfaac1d506e47b3e4672a088f4507a41d7dfcceb8fc3708f681fa678f6959a30)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userData", value)

    @builtins.property
    @jsii.member(jsii_name="userDataBase64")
    def user_data_base64(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userDataBase64"))

    @user_data_base64.setter
    def user_data_base64(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60fb32e2d9995c7c409c82f065f05976f89da84f07586443fab81c583665bd11)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userDataBase64", value)

    @builtins.property
    @jsii.member(jsii_name="vpcClassicLinkId")
    def vpc_classic_link_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vpcClassicLinkId"))

    @vpc_classic_link_id.setter
    def vpc_classic_link_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06a4127640cbf3cb90e92fc39ba02423a7eeeb8143b4c328eeab1c13cba581b2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcClassicLinkId", value)

    @builtins.property
    @jsii.member(jsii_name="vpcClassicLinkSecurityGroups")
    def vpc_classic_link_security_groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "vpcClassicLinkSecurityGroups"))

    @vpc_classic_link_security_groups.setter
    def vpc_classic_link_security_groups(
        self,
        value: typing.List[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e8d07afe8549a1fad88a0c16dbc24911e6c9561814f4da6f1650177d4114317)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcClassicLinkSecurityGroups", value)


@jsii.data_type(
    jsii_type="aws.launchConfiguration.LaunchConfigurationConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "image_id": "imageId",
        "instance_type": "instanceType",
        "associate_public_ip_address": "associatePublicIpAddress",
        "ebs_block_device": "ebsBlockDevice",
        "ebs_optimized": "ebsOptimized",
        "enable_monitoring": "enableMonitoring",
        "ephemeral_block_device": "ephemeralBlockDevice",
        "iam_instance_profile": "iamInstanceProfile",
        "id": "id",
        "key_name": "keyName",
        "metadata_options": "metadataOptions",
        "name": "name",
        "name_prefix": "namePrefix",
        "placement_tenancy": "placementTenancy",
        "root_block_device": "rootBlockDevice",
        "security_groups": "securityGroups",
        "spot_price": "spotPrice",
        "user_data": "userData",
        "user_data_base64": "userDataBase64",
        "vpc_classic_link_id": "vpcClassicLinkId",
        "vpc_classic_link_security_groups": "vpcClassicLinkSecurityGroups",
    },
)
class LaunchConfigurationConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        image_id: builtins.str,
        instance_type: builtins.str,
        associate_public_ip_address: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        ebs_block_device: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LaunchConfigurationEbsBlockDevice", typing.Dict[builtins.str, typing.Any]]]]] = None,
        ebs_optimized: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_monitoring: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        ephemeral_block_device: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LaunchConfigurationEphemeralBlockDevice", typing.Dict[builtins.str, typing.Any]]]]] = None,
        iam_instance_profile: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        key_name: typing.Optional[builtins.str] = None,
        metadata_options: typing.Optional[typing.Union["LaunchConfigurationMetadataOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        name: typing.Optional[builtins.str] = None,
        name_prefix: typing.Optional[builtins.str] = None,
        placement_tenancy: typing.Optional[builtins.str] = None,
        root_block_device: typing.Optional[typing.Union["LaunchConfigurationRootBlockDevice", typing.Dict[builtins.str, typing.Any]]] = None,
        security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        spot_price: typing.Optional[builtins.str] = None,
        user_data: typing.Optional[builtins.str] = None,
        user_data_base64: typing.Optional[builtins.str] = None,
        vpc_classic_link_id: typing.Optional[builtins.str] = None,
        vpc_classic_link_security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param image_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#image_id LaunchConfiguration#image_id}.
        :param instance_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#instance_type LaunchConfiguration#instance_type}.
        :param associate_public_ip_address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#associate_public_ip_address LaunchConfiguration#associate_public_ip_address}.
        :param ebs_block_device: ebs_block_device block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#ebs_block_device LaunchConfiguration#ebs_block_device}
        :param ebs_optimized: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#ebs_optimized LaunchConfiguration#ebs_optimized}.
        :param enable_monitoring: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#enable_monitoring LaunchConfiguration#enable_monitoring}.
        :param ephemeral_block_device: ephemeral_block_device block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#ephemeral_block_device LaunchConfiguration#ephemeral_block_device}
        :param iam_instance_profile: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#iam_instance_profile LaunchConfiguration#iam_instance_profile}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#id LaunchConfiguration#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param key_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#key_name LaunchConfiguration#key_name}.
        :param metadata_options: metadata_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#metadata_options LaunchConfiguration#metadata_options}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#name LaunchConfiguration#name}.
        :param name_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#name_prefix LaunchConfiguration#name_prefix}.
        :param placement_tenancy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#placement_tenancy LaunchConfiguration#placement_tenancy}.
        :param root_block_device: root_block_device block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#root_block_device LaunchConfiguration#root_block_device}
        :param security_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#security_groups LaunchConfiguration#security_groups}.
        :param spot_price: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#spot_price LaunchConfiguration#spot_price}.
        :param user_data: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#user_data LaunchConfiguration#user_data}.
        :param user_data_base64: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#user_data_base64 LaunchConfiguration#user_data_base64}.
        :param vpc_classic_link_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#vpc_classic_link_id LaunchConfiguration#vpc_classic_link_id}.
        :param vpc_classic_link_security_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#vpc_classic_link_security_groups LaunchConfiguration#vpc_classic_link_security_groups}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(metadata_options, dict):
            metadata_options = LaunchConfigurationMetadataOptions(**metadata_options)
        if isinstance(root_block_device, dict):
            root_block_device = LaunchConfigurationRootBlockDevice(**root_block_device)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f38a2a61958968c67781b38c0539c3b90d16262c3359402af75a9c0e929043d7)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument image_id", value=image_id, expected_type=type_hints["image_id"])
            check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
            check_type(argname="argument associate_public_ip_address", value=associate_public_ip_address, expected_type=type_hints["associate_public_ip_address"])
            check_type(argname="argument ebs_block_device", value=ebs_block_device, expected_type=type_hints["ebs_block_device"])
            check_type(argname="argument ebs_optimized", value=ebs_optimized, expected_type=type_hints["ebs_optimized"])
            check_type(argname="argument enable_monitoring", value=enable_monitoring, expected_type=type_hints["enable_monitoring"])
            check_type(argname="argument ephemeral_block_device", value=ephemeral_block_device, expected_type=type_hints["ephemeral_block_device"])
            check_type(argname="argument iam_instance_profile", value=iam_instance_profile, expected_type=type_hints["iam_instance_profile"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument key_name", value=key_name, expected_type=type_hints["key_name"])
            check_type(argname="argument metadata_options", value=metadata_options, expected_type=type_hints["metadata_options"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument name_prefix", value=name_prefix, expected_type=type_hints["name_prefix"])
            check_type(argname="argument placement_tenancy", value=placement_tenancy, expected_type=type_hints["placement_tenancy"])
            check_type(argname="argument root_block_device", value=root_block_device, expected_type=type_hints["root_block_device"])
            check_type(argname="argument security_groups", value=security_groups, expected_type=type_hints["security_groups"])
            check_type(argname="argument spot_price", value=spot_price, expected_type=type_hints["spot_price"])
            check_type(argname="argument user_data", value=user_data, expected_type=type_hints["user_data"])
            check_type(argname="argument user_data_base64", value=user_data_base64, expected_type=type_hints["user_data_base64"])
            check_type(argname="argument vpc_classic_link_id", value=vpc_classic_link_id, expected_type=type_hints["vpc_classic_link_id"])
            check_type(argname="argument vpc_classic_link_security_groups", value=vpc_classic_link_security_groups, expected_type=type_hints["vpc_classic_link_security_groups"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "image_id": image_id,
            "instance_type": instance_type,
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
        if associate_public_ip_address is not None:
            self._values["associate_public_ip_address"] = associate_public_ip_address
        if ebs_block_device is not None:
            self._values["ebs_block_device"] = ebs_block_device
        if ebs_optimized is not None:
            self._values["ebs_optimized"] = ebs_optimized
        if enable_monitoring is not None:
            self._values["enable_monitoring"] = enable_monitoring
        if ephemeral_block_device is not None:
            self._values["ephemeral_block_device"] = ephemeral_block_device
        if iam_instance_profile is not None:
            self._values["iam_instance_profile"] = iam_instance_profile
        if id is not None:
            self._values["id"] = id
        if key_name is not None:
            self._values["key_name"] = key_name
        if metadata_options is not None:
            self._values["metadata_options"] = metadata_options
        if name is not None:
            self._values["name"] = name
        if name_prefix is not None:
            self._values["name_prefix"] = name_prefix
        if placement_tenancy is not None:
            self._values["placement_tenancy"] = placement_tenancy
        if root_block_device is not None:
            self._values["root_block_device"] = root_block_device
        if security_groups is not None:
            self._values["security_groups"] = security_groups
        if spot_price is not None:
            self._values["spot_price"] = spot_price
        if user_data is not None:
            self._values["user_data"] = user_data
        if user_data_base64 is not None:
            self._values["user_data_base64"] = user_data_base64
        if vpc_classic_link_id is not None:
            self._values["vpc_classic_link_id"] = vpc_classic_link_id
        if vpc_classic_link_security_groups is not None:
            self._values["vpc_classic_link_security_groups"] = vpc_classic_link_security_groups

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
    def image_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#image_id LaunchConfiguration#image_id}.'''
        result = self._values.get("image_id")
        assert result is not None, "Required property 'image_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def instance_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#instance_type LaunchConfiguration#instance_type}.'''
        result = self._values.get("instance_type")
        assert result is not None, "Required property 'instance_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def associate_public_ip_address(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#associate_public_ip_address LaunchConfiguration#associate_public_ip_address}.'''
        result = self._values.get("associate_public_ip_address")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def ebs_block_device(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LaunchConfigurationEbsBlockDevice"]]]:
        '''ebs_block_device block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#ebs_block_device LaunchConfiguration#ebs_block_device}
        '''
        result = self._values.get("ebs_block_device")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LaunchConfigurationEbsBlockDevice"]]], result)

    @builtins.property
    def ebs_optimized(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#ebs_optimized LaunchConfiguration#ebs_optimized}.'''
        result = self._values.get("ebs_optimized")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def enable_monitoring(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#enable_monitoring LaunchConfiguration#enable_monitoring}.'''
        result = self._values.get("enable_monitoring")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def ephemeral_block_device(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LaunchConfigurationEphemeralBlockDevice"]]]:
        '''ephemeral_block_device block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#ephemeral_block_device LaunchConfiguration#ephemeral_block_device}
        '''
        result = self._values.get("ephemeral_block_device")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LaunchConfigurationEphemeralBlockDevice"]]], result)

    @builtins.property
    def iam_instance_profile(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#iam_instance_profile LaunchConfiguration#iam_instance_profile}.'''
        result = self._values.get("iam_instance_profile")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#id LaunchConfiguration#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#key_name LaunchConfiguration#key_name}.'''
        result = self._values.get("key_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def metadata_options(self) -> typing.Optional["LaunchConfigurationMetadataOptions"]:
        '''metadata_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#metadata_options LaunchConfiguration#metadata_options}
        '''
        result = self._values.get("metadata_options")
        return typing.cast(typing.Optional["LaunchConfigurationMetadataOptions"], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#name LaunchConfiguration#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#name_prefix LaunchConfiguration#name_prefix}.'''
        result = self._values.get("name_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def placement_tenancy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#placement_tenancy LaunchConfiguration#placement_tenancy}.'''
        result = self._values.get("placement_tenancy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def root_block_device(
        self,
    ) -> typing.Optional["LaunchConfigurationRootBlockDevice"]:
        '''root_block_device block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#root_block_device LaunchConfiguration#root_block_device}
        '''
        result = self._values.get("root_block_device")
        return typing.cast(typing.Optional["LaunchConfigurationRootBlockDevice"], result)

    @builtins.property
    def security_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#security_groups LaunchConfiguration#security_groups}.'''
        result = self._values.get("security_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def spot_price(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#spot_price LaunchConfiguration#spot_price}.'''
        result = self._values.get("spot_price")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_data(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#user_data LaunchConfiguration#user_data}.'''
        result = self._values.get("user_data")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_data_base64(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#user_data_base64 LaunchConfiguration#user_data_base64}.'''
        result = self._values.get("user_data_base64")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vpc_classic_link_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#vpc_classic_link_id LaunchConfiguration#vpc_classic_link_id}.'''
        result = self._values.get("vpc_classic_link_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vpc_classic_link_security_groups(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#vpc_classic_link_security_groups LaunchConfiguration#vpc_classic_link_security_groups}.'''
        result = self._values.get("vpc_classic_link_security_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LaunchConfigurationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.launchConfiguration.LaunchConfigurationEbsBlockDevice",
    jsii_struct_bases=[],
    name_mapping={
        "device_name": "deviceName",
        "delete_on_termination": "deleteOnTermination",
        "encrypted": "encrypted",
        "iops": "iops",
        "no_device": "noDevice",
        "snapshot_id": "snapshotId",
        "throughput": "throughput",
        "volume_size": "volumeSize",
        "volume_type": "volumeType",
    },
)
class LaunchConfigurationEbsBlockDevice:
    def __init__(
        self,
        *,
        device_name: builtins.str,
        delete_on_termination: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        encrypted: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        iops: typing.Optional[jsii.Number] = None,
        no_device: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        snapshot_id: typing.Optional[builtins.str] = None,
        throughput: typing.Optional[jsii.Number] = None,
        volume_size: typing.Optional[jsii.Number] = None,
        volume_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param device_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#device_name LaunchConfiguration#device_name}.
        :param delete_on_termination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#delete_on_termination LaunchConfiguration#delete_on_termination}.
        :param encrypted: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#encrypted LaunchConfiguration#encrypted}.
        :param iops: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#iops LaunchConfiguration#iops}.
        :param no_device: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#no_device LaunchConfiguration#no_device}.
        :param snapshot_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#snapshot_id LaunchConfiguration#snapshot_id}.
        :param throughput: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#throughput LaunchConfiguration#throughput}.
        :param volume_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#volume_size LaunchConfiguration#volume_size}.
        :param volume_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#volume_type LaunchConfiguration#volume_type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__65f6f7562613d49e121c1b81d891683b555efea97ee7cbd553a7d1f6917633eb)
            check_type(argname="argument device_name", value=device_name, expected_type=type_hints["device_name"])
            check_type(argname="argument delete_on_termination", value=delete_on_termination, expected_type=type_hints["delete_on_termination"])
            check_type(argname="argument encrypted", value=encrypted, expected_type=type_hints["encrypted"])
            check_type(argname="argument iops", value=iops, expected_type=type_hints["iops"])
            check_type(argname="argument no_device", value=no_device, expected_type=type_hints["no_device"])
            check_type(argname="argument snapshot_id", value=snapshot_id, expected_type=type_hints["snapshot_id"])
            check_type(argname="argument throughput", value=throughput, expected_type=type_hints["throughput"])
            check_type(argname="argument volume_size", value=volume_size, expected_type=type_hints["volume_size"])
            check_type(argname="argument volume_type", value=volume_type, expected_type=type_hints["volume_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "device_name": device_name,
        }
        if delete_on_termination is not None:
            self._values["delete_on_termination"] = delete_on_termination
        if encrypted is not None:
            self._values["encrypted"] = encrypted
        if iops is not None:
            self._values["iops"] = iops
        if no_device is not None:
            self._values["no_device"] = no_device
        if snapshot_id is not None:
            self._values["snapshot_id"] = snapshot_id
        if throughput is not None:
            self._values["throughput"] = throughput
        if volume_size is not None:
            self._values["volume_size"] = volume_size
        if volume_type is not None:
            self._values["volume_type"] = volume_type

    @builtins.property
    def device_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#device_name LaunchConfiguration#device_name}.'''
        result = self._values.get("device_name")
        assert result is not None, "Required property 'device_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def delete_on_termination(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#delete_on_termination LaunchConfiguration#delete_on_termination}.'''
        result = self._values.get("delete_on_termination")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def encrypted(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#encrypted LaunchConfiguration#encrypted}.'''
        result = self._values.get("encrypted")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def iops(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#iops LaunchConfiguration#iops}.'''
        result = self._values.get("iops")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def no_device(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#no_device LaunchConfiguration#no_device}.'''
        result = self._values.get("no_device")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def snapshot_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#snapshot_id LaunchConfiguration#snapshot_id}.'''
        result = self._values.get("snapshot_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def throughput(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#throughput LaunchConfiguration#throughput}.'''
        result = self._values.get("throughput")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def volume_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#volume_size LaunchConfiguration#volume_size}.'''
        result = self._values.get("volume_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def volume_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#volume_type LaunchConfiguration#volume_type}.'''
        result = self._values.get("volume_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LaunchConfigurationEbsBlockDevice(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LaunchConfigurationEbsBlockDeviceList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.launchConfiguration.LaunchConfigurationEbsBlockDeviceList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e2b64e4e0250f856704b01c61e8a28baf0115df7516cbd9445e38b3f6933bdf1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LaunchConfigurationEbsBlockDeviceOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc79faf11ce0aff1d78d03e5efe37ce35fb36f1b463500814700b56a913a4468)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LaunchConfigurationEbsBlockDeviceOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__784c3574111130bcdbf7768f466411c39301617dd0a1e17b5f3301480cd3f6f7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__97b48ec5bf3ca31a1a8401cfedef952719fba7206935c61a7d45d74610df2b78)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d54a132259d06af62d97a5d24f3e9609f3aebb37f47d0a3adbe644d979f6b876)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LaunchConfigurationEbsBlockDevice]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LaunchConfigurationEbsBlockDevice]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LaunchConfigurationEbsBlockDevice]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1cbec0f0405edd55d5248782bda156c0ac05654b0a48ba74b1f2d420916a78b5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LaunchConfigurationEbsBlockDeviceOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.launchConfiguration.LaunchConfigurationEbsBlockDeviceOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6a9de52735f4eda7d5ce84c67a08a21d0fade4e021f841c6ba1a50ba774742b3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDeleteOnTermination")
    def reset_delete_on_termination(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeleteOnTermination", []))

    @jsii.member(jsii_name="resetEncrypted")
    def reset_encrypted(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncrypted", []))

    @jsii.member(jsii_name="resetIops")
    def reset_iops(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIops", []))

    @jsii.member(jsii_name="resetNoDevice")
    def reset_no_device(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNoDevice", []))

    @jsii.member(jsii_name="resetSnapshotId")
    def reset_snapshot_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSnapshotId", []))

    @jsii.member(jsii_name="resetThroughput")
    def reset_throughput(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetThroughput", []))

    @jsii.member(jsii_name="resetVolumeSize")
    def reset_volume_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVolumeSize", []))

    @jsii.member(jsii_name="resetVolumeType")
    def reset_volume_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVolumeType", []))

    @builtins.property
    @jsii.member(jsii_name="deleteOnTerminationInput")
    def delete_on_termination_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "deleteOnTerminationInput"))

    @builtins.property
    @jsii.member(jsii_name="deviceNameInput")
    def device_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deviceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptedInput")
    def encrypted_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "encryptedInput"))

    @builtins.property
    @jsii.member(jsii_name="iopsInput")
    def iops_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "iopsInput"))

    @builtins.property
    @jsii.member(jsii_name="noDeviceInput")
    def no_device_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "noDeviceInput"))

    @builtins.property
    @jsii.member(jsii_name="snapshotIdInput")
    def snapshot_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "snapshotIdInput"))

    @builtins.property
    @jsii.member(jsii_name="throughputInput")
    def throughput_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "throughputInput"))

    @builtins.property
    @jsii.member(jsii_name="volumeSizeInput")
    def volume_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "volumeSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="volumeTypeInput")
    def volume_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "volumeTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteOnTermination")
    def delete_on_termination(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "deleteOnTermination"))

    @delete_on_termination.setter
    def delete_on_termination(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__decbec6748b19066a27b44c094d94fb0d06ed46903d5e721c1319d4c9780d089)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deleteOnTermination", value)

    @builtins.property
    @jsii.member(jsii_name="deviceName")
    def device_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deviceName"))

    @device_name.setter
    def device_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__993dc3fac9159e0e4b8327f5cc8dc10c6da720f9e0e268833a48fdffd49e4432)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deviceName", value)

    @builtins.property
    @jsii.member(jsii_name="encrypted")
    def encrypted(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "encrypted"))

    @encrypted.setter
    def encrypted(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bbf7bc1edfbbb8aa02f504a7e75e0515f344dac11a835a6576237e4b053d6021)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encrypted", value)

    @builtins.property
    @jsii.member(jsii_name="iops")
    def iops(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "iops"))

    @iops.setter
    def iops(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__137e6da6eb01c4417dc4713b3320e5cd3a1516870c3dd802326a3705ba83f6e9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iops", value)

    @builtins.property
    @jsii.member(jsii_name="noDevice")
    def no_device(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "noDevice"))

    @no_device.setter
    def no_device(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__83a42306cdeafce539af58159cc25c431102c8c12e2c34df72bc562d33585338)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "noDevice", value)

    @builtins.property
    @jsii.member(jsii_name="snapshotId")
    def snapshot_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "snapshotId"))

    @snapshot_id.setter
    def snapshot_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eeb2da202b221933450f4280475148ec26551f58298dd0f1071250ada1ecafa3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snapshotId", value)

    @builtins.property
    @jsii.member(jsii_name="throughput")
    def throughput(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "throughput"))

    @throughput.setter
    def throughput(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aea039b0c8a89c3a432a715bd82495d7d3a9c42241e7f88792a7cacd915946f0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "throughput", value)

    @builtins.property
    @jsii.member(jsii_name="volumeSize")
    def volume_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "volumeSize"))

    @volume_size.setter
    def volume_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4d48a2659cb8f5848bc3cb1c744a15ccba7f8bcbd1b72110fbc141c712e8b89)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeSize", value)

    @builtins.property
    @jsii.member(jsii_name="volumeType")
    def volume_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "volumeType"))

    @volume_type.setter
    def volume_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c82c31cc2e2ab8b246f1fad2ed8d9626a55b72ff4077ed9df1931967ce5a1123)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LaunchConfigurationEbsBlockDevice, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LaunchConfigurationEbsBlockDevice, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LaunchConfigurationEbsBlockDevice, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91b4e4527b72a64ae3e168a870eb90b8ef6c6bcfd3c18efb8b3390d339347884)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.launchConfiguration.LaunchConfigurationEphemeralBlockDevice",
    jsii_struct_bases=[],
    name_mapping={
        "device_name": "deviceName",
        "no_device": "noDevice",
        "virtual_name": "virtualName",
    },
)
class LaunchConfigurationEphemeralBlockDevice:
    def __init__(
        self,
        *,
        device_name: builtins.str,
        no_device: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        virtual_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param device_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#device_name LaunchConfiguration#device_name}.
        :param no_device: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#no_device LaunchConfiguration#no_device}.
        :param virtual_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#virtual_name LaunchConfiguration#virtual_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d92178673f7b9e22180bfd655a585bb46a4d316376c70a8e696e74f27428edd7)
            check_type(argname="argument device_name", value=device_name, expected_type=type_hints["device_name"])
            check_type(argname="argument no_device", value=no_device, expected_type=type_hints["no_device"])
            check_type(argname="argument virtual_name", value=virtual_name, expected_type=type_hints["virtual_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "device_name": device_name,
        }
        if no_device is not None:
            self._values["no_device"] = no_device
        if virtual_name is not None:
            self._values["virtual_name"] = virtual_name

    @builtins.property
    def device_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#device_name LaunchConfiguration#device_name}.'''
        result = self._values.get("device_name")
        assert result is not None, "Required property 'device_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def no_device(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#no_device LaunchConfiguration#no_device}.'''
        result = self._values.get("no_device")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def virtual_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#virtual_name LaunchConfiguration#virtual_name}.'''
        result = self._values.get("virtual_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LaunchConfigurationEphemeralBlockDevice(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LaunchConfigurationEphemeralBlockDeviceList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.launchConfiguration.LaunchConfigurationEphemeralBlockDeviceList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5804866a4c6e510177c7b363f9e9ea22610197fc609959be5581cf6a97519032)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LaunchConfigurationEphemeralBlockDeviceOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f7d12ead99df930bb891d3c2767c54cf02ba978680efaa2f9c351f0f213659f)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LaunchConfigurationEphemeralBlockDeviceOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__990f1eb0acb8b67c462c07cc699462438d838791946e26dc6af34f8279bcebf2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8a3f42457e395dddf30324e3354d94a7646e0ef8ff08f0ce53f9a81e15e43240)
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
            type_hints = typing.get_type_hints(_typecheckingstub__590b68a637aed2d52b507a795340b60cf90ea64846c6c4500cebf93433bc70ad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LaunchConfigurationEphemeralBlockDevice]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LaunchConfigurationEphemeralBlockDevice]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LaunchConfigurationEphemeralBlockDevice]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__198c92f64b3180f2107a8be734d6ffabad4670d92df183d64dcf4d224b7fdc5e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LaunchConfigurationEphemeralBlockDeviceOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.launchConfiguration.LaunchConfigurationEphemeralBlockDeviceOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__220540007f06a96f19b45361a76e9f73107a0d6c2f8be6e9238fe4d1fc33cde0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetNoDevice")
    def reset_no_device(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNoDevice", []))

    @jsii.member(jsii_name="resetVirtualName")
    def reset_virtual_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVirtualName", []))

    @builtins.property
    @jsii.member(jsii_name="deviceNameInput")
    def device_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deviceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="noDeviceInput")
    def no_device_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "noDeviceInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualNameInput")
    def virtual_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "virtualNameInput"))

    @builtins.property
    @jsii.member(jsii_name="deviceName")
    def device_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deviceName"))

    @device_name.setter
    def device_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7f5bac06e541c9dddcc3c671a0c6700269a1b9d736a202c80d576cec9f58537)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deviceName", value)

    @builtins.property
    @jsii.member(jsii_name="noDevice")
    def no_device(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "noDevice"))

    @no_device.setter
    def no_device(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b20194218b7e649e6a33e493b5a4f23fae0749c0f95575a751946117d7c2aac4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "noDevice", value)

    @builtins.property
    @jsii.member(jsii_name="virtualName")
    def virtual_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "virtualName"))

    @virtual_name.setter
    def virtual_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e76598194a77a910aac7ef9e8d16922f5dd30669fb6dbcdbe9e9c5f155c6e25)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LaunchConfigurationEphemeralBlockDevice, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LaunchConfigurationEphemeralBlockDevice, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LaunchConfigurationEphemeralBlockDevice, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__246eb82dd6f2d7b323ce824535144a8ea05682cd01390e1f713d165e0aeb0d47)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.launchConfiguration.LaunchConfigurationMetadataOptions",
    jsii_struct_bases=[],
    name_mapping={
        "http_endpoint": "httpEndpoint",
        "http_put_response_hop_limit": "httpPutResponseHopLimit",
        "http_tokens": "httpTokens",
    },
)
class LaunchConfigurationMetadataOptions:
    def __init__(
        self,
        *,
        http_endpoint: typing.Optional[builtins.str] = None,
        http_put_response_hop_limit: typing.Optional[jsii.Number] = None,
        http_tokens: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param http_endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#http_endpoint LaunchConfiguration#http_endpoint}.
        :param http_put_response_hop_limit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#http_put_response_hop_limit LaunchConfiguration#http_put_response_hop_limit}.
        :param http_tokens: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#http_tokens LaunchConfiguration#http_tokens}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb59f1c86c06b973de09a6a9126194997586f63b075557e8de3aa4918548f38b)
            check_type(argname="argument http_endpoint", value=http_endpoint, expected_type=type_hints["http_endpoint"])
            check_type(argname="argument http_put_response_hop_limit", value=http_put_response_hop_limit, expected_type=type_hints["http_put_response_hop_limit"])
            check_type(argname="argument http_tokens", value=http_tokens, expected_type=type_hints["http_tokens"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if http_endpoint is not None:
            self._values["http_endpoint"] = http_endpoint
        if http_put_response_hop_limit is not None:
            self._values["http_put_response_hop_limit"] = http_put_response_hop_limit
        if http_tokens is not None:
            self._values["http_tokens"] = http_tokens

    @builtins.property
    def http_endpoint(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#http_endpoint LaunchConfiguration#http_endpoint}.'''
        result = self._values.get("http_endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def http_put_response_hop_limit(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#http_put_response_hop_limit LaunchConfiguration#http_put_response_hop_limit}.'''
        result = self._values.get("http_put_response_hop_limit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def http_tokens(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#http_tokens LaunchConfiguration#http_tokens}.'''
        result = self._values.get("http_tokens")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LaunchConfigurationMetadataOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LaunchConfigurationMetadataOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.launchConfiguration.LaunchConfigurationMetadataOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b825bb3b25def9696df06247a0198b5068226318eb2c512cc26e6d510edaa48b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetHttpEndpoint")
    def reset_http_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpEndpoint", []))

    @jsii.member(jsii_name="resetHttpPutResponseHopLimit")
    def reset_http_put_response_hop_limit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpPutResponseHopLimit", []))

    @jsii.member(jsii_name="resetHttpTokens")
    def reset_http_tokens(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpTokens", []))

    @builtins.property
    @jsii.member(jsii_name="httpEndpointInput")
    def http_endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "httpEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="httpPutResponseHopLimitInput")
    def http_put_response_hop_limit_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "httpPutResponseHopLimitInput"))

    @builtins.property
    @jsii.member(jsii_name="httpTokensInput")
    def http_tokens_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "httpTokensInput"))

    @builtins.property
    @jsii.member(jsii_name="httpEndpoint")
    def http_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "httpEndpoint"))

    @http_endpoint.setter
    def http_endpoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dcaa8cd053fd2322fab79f00d7b2467eeb7aaf70f2ffd30401fa56a8dd3ac6d7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="httpPutResponseHopLimit")
    def http_put_response_hop_limit(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "httpPutResponseHopLimit"))

    @http_put_response_hop_limit.setter
    def http_put_response_hop_limit(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__557f9290aa3eb89aaa99d1c63122d3d8060c4db3bdaf709415bb94223663a414)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpPutResponseHopLimit", value)

    @builtins.property
    @jsii.member(jsii_name="httpTokens")
    def http_tokens(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "httpTokens"))

    @http_tokens.setter
    def http_tokens(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f33163efc8732afa673e6798a58975293aef3cda79692360c2c16f61429d890a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpTokens", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LaunchConfigurationMetadataOptions]:
        return typing.cast(typing.Optional[LaunchConfigurationMetadataOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LaunchConfigurationMetadataOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__490cedfc9e4a2960454cdf768371794b47c730fc81b23d634397515e71b3da72)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.launchConfiguration.LaunchConfigurationRootBlockDevice",
    jsii_struct_bases=[],
    name_mapping={
        "delete_on_termination": "deleteOnTermination",
        "encrypted": "encrypted",
        "iops": "iops",
        "throughput": "throughput",
        "volume_size": "volumeSize",
        "volume_type": "volumeType",
    },
)
class LaunchConfigurationRootBlockDevice:
    def __init__(
        self,
        *,
        delete_on_termination: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        encrypted: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        iops: typing.Optional[jsii.Number] = None,
        throughput: typing.Optional[jsii.Number] = None,
        volume_size: typing.Optional[jsii.Number] = None,
        volume_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param delete_on_termination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#delete_on_termination LaunchConfiguration#delete_on_termination}.
        :param encrypted: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#encrypted LaunchConfiguration#encrypted}.
        :param iops: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#iops LaunchConfiguration#iops}.
        :param throughput: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#throughput LaunchConfiguration#throughput}.
        :param volume_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#volume_size LaunchConfiguration#volume_size}.
        :param volume_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#volume_type LaunchConfiguration#volume_type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66702487553b91245c2a71fb90ef77900114d1ed5cc1740f9a9c56bbf52ca681)
            check_type(argname="argument delete_on_termination", value=delete_on_termination, expected_type=type_hints["delete_on_termination"])
            check_type(argname="argument encrypted", value=encrypted, expected_type=type_hints["encrypted"])
            check_type(argname="argument iops", value=iops, expected_type=type_hints["iops"])
            check_type(argname="argument throughput", value=throughput, expected_type=type_hints["throughput"])
            check_type(argname="argument volume_size", value=volume_size, expected_type=type_hints["volume_size"])
            check_type(argname="argument volume_type", value=volume_type, expected_type=type_hints["volume_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if delete_on_termination is not None:
            self._values["delete_on_termination"] = delete_on_termination
        if encrypted is not None:
            self._values["encrypted"] = encrypted
        if iops is not None:
            self._values["iops"] = iops
        if throughput is not None:
            self._values["throughput"] = throughput
        if volume_size is not None:
            self._values["volume_size"] = volume_size
        if volume_type is not None:
            self._values["volume_type"] = volume_type

    @builtins.property
    def delete_on_termination(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#delete_on_termination LaunchConfiguration#delete_on_termination}.'''
        result = self._values.get("delete_on_termination")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def encrypted(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#encrypted LaunchConfiguration#encrypted}.'''
        result = self._values.get("encrypted")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def iops(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#iops LaunchConfiguration#iops}.'''
        result = self._values.get("iops")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def throughput(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#throughput LaunchConfiguration#throughput}.'''
        result = self._values.get("throughput")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def volume_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#volume_size LaunchConfiguration#volume_size}.'''
        result = self._values.get("volume_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def volume_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_configuration#volume_type LaunchConfiguration#volume_type}.'''
        result = self._values.get("volume_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LaunchConfigurationRootBlockDevice(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LaunchConfigurationRootBlockDeviceOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.launchConfiguration.LaunchConfigurationRootBlockDeviceOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3f967104deb992a096a88f40411b05d6d3d6320e1764a1f54528ec2ebf5eaf40)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDeleteOnTermination")
    def reset_delete_on_termination(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeleteOnTermination", []))

    @jsii.member(jsii_name="resetEncrypted")
    def reset_encrypted(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncrypted", []))

    @jsii.member(jsii_name="resetIops")
    def reset_iops(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIops", []))

    @jsii.member(jsii_name="resetThroughput")
    def reset_throughput(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetThroughput", []))

    @jsii.member(jsii_name="resetVolumeSize")
    def reset_volume_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVolumeSize", []))

    @jsii.member(jsii_name="resetVolumeType")
    def reset_volume_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVolumeType", []))

    @builtins.property
    @jsii.member(jsii_name="deleteOnTerminationInput")
    def delete_on_termination_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "deleteOnTerminationInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptedInput")
    def encrypted_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "encryptedInput"))

    @builtins.property
    @jsii.member(jsii_name="iopsInput")
    def iops_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "iopsInput"))

    @builtins.property
    @jsii.member(jsii_name="throughputInput")
    def throughput_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "throughputInput"))

    @builtins.property
    @jsii.member(jsii_name="volumeSizeInput")
    def volume_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "volumeSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="volumeTypeInput")
    def volume_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "volumeTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteOnTermination")
    def delete_on_termination(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "deleteOnTermination"))

    @delete_on_termination.setter
    def delete_on_termination(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c74a6243fddb8e5eccd9986cf7dee755a06f8790ac98bc86d42e25a479d870f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deleteOnTermination", value)

    @builtins.property
    @jsii.member(jsii_name="encrypted")
    def encrypted(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "encrypted"))

    @encrypted.setter
    def encrypted(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae23884940d58654534b3f6bee59a5b0ff3eca12dc5c28e10e4b6628a7db8d98)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encrypted", value)

    @builtins.property
    @jsii.member(jsii_name="iops")
    def iops(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "iops"))

    @iops.setter
    def iops(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f0717dfda67a79e64c7e9be9cc154dccfb612767969b1e3cd5e73190dce8b96f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iops", value)

    @builtins.property
    @jsii.member(jsii_name="throughput")
    def throughput(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "throughput"))

    @throughput.setter
    def throughput(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e995d02ddfca01e10cda722c45056770fa44906600f728745cf6a31dbe713d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "throughput", value)

    @builtins.property
    @jsii.member(jsii_name="volumeSize")
    def volume_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "volumeSize"))

    @volume_size.setter
    def volume_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e0c6e8a731bd174c6acf34856cecd52efad50c6647201e45965c8084e34855e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeSize", value)

    @builtins.property
    @jsii.member(jsii_name="volumeType")
    def volume_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "volumeType"))

    @volume_type.setter
    def volume_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__88d9c7e6ad53b188d45c664c81c797768289ca22f6577124615099979edc4c07)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LaunchConfigurationRootBlockDevice]:
        return typing.cast(typing.Optional[LaunchConfigurationRootBlockDevice], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LaunchConfigurationRootBlockDevice],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__422417fc76164e038049906b41e6e95db2872325ee030970b03767dee3afb3b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "LaunchConfiguration",
    "LaunchConfigurationConfig",
    "LaunchConfigurationEbsBlockDevice",
    "LaunchConfigurationEbsBlockDeviceList",
    "LaunchConfigurationEbsBlockDeviceOutputReference",
    "LaunchConfigurationEphemeralBlockDevice",
    "LaunchConfigurationEphemeralBlockDeviceList",
    "LaunchConfigurationEphemeralBlockDeviceOutputReference",
    "LaunchConfigurationMetadataOptions",
    "LaunchConfigurationMetadataOptionsOutputReference",
    "LaunchConfigurationRootBlockDevice",
    "LaunchConfigurationRootBlockDeviceOutputReference",
]

publication.publish()

def _typecheckingstub__8ae94500549626be2ff7531a79a5a88c38d3c00888b29a837c84a3a13fa96b1a(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    image_id: builtins.str,
    instance_type: builtins.str,
    associate_public_ip_address: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ebs_block_device: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LaunchConfigurationEbsBlockDevice, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ebs_optimized: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    enable_monitoring: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ephemeral_block_device: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LaunchConfigurationEphemeralBlockDevice, typing.Dict[builtins.str, typing.Any]]]]] = None,
    iam_instance_profile: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    key_name: typing.Optional[builtins.str] = None,
    metadata_options: typing.Optional[typing.Union[LaunchConfigurationMetadataOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    name: typing.Optional[builtins.str] = None,
    name_prefix: typing.Optional[builtins.str] = None,
    placement_tenancy: typing.Optional[builtins.str] = None,
    root_block_device: typing.Optional[typing.Union[LaunchConfigurationRootBlockDevice, typing.Dict[builtins.str, typing.Any]]] = None,
    security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    spot_price: typing.Optional[builtins.str] = None,
    user_data: typing.Optional[builtins.str] = None,
    user_data_base64: typing.Optional[builtins.str] = None,
    vpc_classic_link_id: typing.Optional[builtins.str] = None,
    vpc_classic_link_security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
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

def _typecheckingstub__9abdf965511cdd80605a2a2297ac13064f0a2089775a7cb6d1c103c10bbe9381(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LaunchConfigurationEbsBlockDevice, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0f86b2e3ba0244305bb39729f0cf94f21092bdada1057e73ee4ef6a16ffbf78(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LaunchConfigurationEphemeralBlockDevice, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__835b670aa51e466b59cc54dea74e46da1a1c1d825d614169f8065ce7a4c320d6(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7dff581c93c8d85b3171914a8afef27c627b4ae72f700fe236bff8c0581d6cf6(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8440dcb66c07c8ce76abd8663da3408c77e221294446e632e487867909e55dc0(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8eb0626ea3177c9ddec9ac3a095bc4c7be1a75bd08503e2c3534a029d89b7d7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5e4caabee12981d93d538cddaf66ce04a4e1f9bb617c5e71147797a4547df92(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09f96f4df954464fd0ba2bcca240eebeab7e344686472fac6a514cf994358881(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d64a6feec08555eae824a9c2c56806ee6a6a64ab5472e152be1358c31ffb1c1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b28f19ea17063b720d10e0c1248a4ff1fa16a845a0867fb01d1eeb74e83ffea(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ffc96bc4817b197951a3fab3d675d7191961dcbd2a0a7f35fcf0fadbe3c6a850(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d685982e798c36fd3fe62630e64ddae0a629b50f8b13498d189952c2ee9620f7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f7ab9fe3c02ac09592ae230b612ae94dc542e3ba64c3588600febe9d8a4dc73(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ec40e260949ac58a70440201f1ea8e11ee6a01080dab6aac9b2934f71c7b553(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03ab86778ee7ca6605ac3f3ddce95d9e782c830e7945d65ba601ecb31534d1d9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dfaac1d506e47b3e4672a088f4507a41d7dfcceb8fc3708f681fa678f6959a30(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60fb32e2d9995c7c409c82f065f05976f89da84f07586443fab81c583665bd11(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06a4127640cbf3cb90e92fc39ba02423a7eeeb8143b4c328eeab1c13cba581b2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e8d07afe8549a1fad88a0c16dbc24911e6c9561814f4da6f1650177d4114317(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f38a2a61958968c67781b38c0539c3b90d16262c3359402af75a9c0e929043d7(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    image_id: builtins.str,
    instance_type: builtins.str,
    associate_public_ip_address: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ebs_block_device: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LaunchConfigurationEbsBlockDevice, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ebs_optimized: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    enable_monitoring: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ephemeral_block_device: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LaunchConfigurationEphemeralBlockDevice, typing.Dict[builtins.str, typing.Any]]]]] = None,
    iam_instance_profile: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    key_name: typing.Optional[builtins.str] = None,
    metadata_options: typing.Optional[typing.Union[LaunchConfigurationMetadataOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    name: typing.Optional[builtins.str] = None,
    name_prefix: typing.Optional[builtins.str] = None,
    placement_tenancy: typing.Optional[builtins.str] = None,
    root_block_device: typing.Optional[typing.Union[LaunchConfigurationRootBlockDevice, typing.Dict[builtins.str, typing.Any]]] = None,
    security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    spot_price: typing.Optional[builtins.str] = None,
    user_data: typing.Optional[builtins.str] = None,
    user_data_base64: typing.Optional[builtins.str] = None,
    vpc_classic_link_id: typing.Optional[builtins.str] = None,
    vpc_classic_link_security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65f6f7562613d49e121c1b81d891683b555efea97ee7cbd553a7d1f6917633eb(
    *,
    device_name: builtins.str,
    delete_on_termination: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    encrypted: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    iops: typing.Optional[jsii.Number] = None,
    no_device: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    snapshot_id: typing.Optional[builtins.str] = None,
    throughput: typing.Optional[jsii.Number] = None,
    volume_size: typing.Optional[jsii.Number] = None,
    volume_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2b64e4e0250f856704b01c61e8a28baf0115df7516cbd9445e38b3f6933bdf1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc79faf11ce0aff1d78d03e5efe37ce35fb36f1b463500814700b56a913a4468(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__784c3574111130bcdbf7768f466411c39301617dd0a1e17b5f3301480cd3f6f7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97b48ec5bf3ca31a1a8401cfedef952719fba7206935c61a7d45d74610df2b78(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d54a132259d06af62d97a5d24f3e9609f3aebb37f47d0a3adbe644d979f6b876(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1cbec0f0405edd55d5248782bda156c0ac05654b0a48ba74b1f2d420916a78b5(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LaunchConfigurationEbsBlockDevice]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a9de52735f4eda7d5ce84c67a08a21d0fade4e021f841c6ba1a50ba774742b3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__decbec6748b19066a27b44c094d94fb0d06ed46903d5e721c1319d4c9780d089(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__993dc3fac9159e0e4b8327f5cc8dc10c6da720f9e0e268833a48fdffd49e4432(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bbf7bc1edfbbb8aa02f504a7e75e0515f344dac11a835a6576237e4b053d6021(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__137e6da6eb01c4417dc4713b3320e5cd3a1516870c3dd802326a3705ba83f6e9(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83a42306cdeafce539af58159cc25c431102c8c12e2c34df72bc562d33585338(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eeb2da202b221933450f4280475148ec26551f58298dd0f1071250ada1ecafa3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aea039b0c8a89c3a432a715bd82495d7d3a9c42241e7f88792a7cacd915946f0(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4d48a2659cb8f5848bc3cb1c744a15ccba7f8bcbd1b72110fbc141c712e8b89(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c82c31cc2e2ab8b246f1fad2ed8d9626a55b72ff4077ed9df1931967ce5a1123(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91b4e4527b72a64ae3e168a870eb90b8ef6c6bcfd3c18efb8b3390d339347884(
    value: typing.Optional[typing.Union[LaunchConfigurationEbsBlockDevice, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d92178673f7b9e22180bfd655a585bb46a4d316376c70a8e696e74f27428edd7(
    *,
    device_name: builtins.str,
    no_device: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    virtual_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5804866a4c6e510177c7b363f9e9ea22610197fc609959be5581cf6a97519032(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f7d12ead99df930bb891d3c2767c54cf02ba978680efaa2f9c351f0f213659f(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__990f1eb0acb8b67c462c07cc699462438d838791946e26dc6af34f8279bcebf2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a3f42457e395dddf30324e3354d94a7646e0ef8ff08f0ce53f9a81e15e43240(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__590b68a637aed2d52b507a795340b60cf90ea64846c6c4500cebf93433bc70ad(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__198c92f64b3180f2107a8be734d6ffabad4670d92df183d64dcf4d224b7fdc5e(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LaunchConfigurationEphemeralBlockDevice]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__220540007f06a96f19b45361a76e9f73107a0d6c2f8be6e9238fe4d1fc33cde0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7f5bac06e541c9dddcc3c671a0c6700269a1b9d736a202c80d576cec9f58537(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b20194218b7e649e6a33e493b5a4f23fae0749c0f95575a751946117d7c2aac4(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e76598194a77a910aac7ef9e8d16922f5dd30669fb6dbcdbe9e9c5f155c6e25(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__246eb82dd6f2d7b323ce824535144a8ea05682cd01390e1f713d165e0aeb0d47(
    value: typing.Optional[typing.Union[LaunchConfigurationEphemeralBlockDevice, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb59f1c86c06b973de09a6a9126194997586f63b075557e8de3aa4918548f38b(
    *,
    http_endpoint: typing.Optional[builtins.str] = None,
    http_put_response_hop_limit: typing.Optional[jsii.Number] = None,
    http_tokens: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b825bb3b25def9696df06247a0198b5068226318eb2c512cc26e6d510edaa48b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dcaa8cd053fd2322fab79f00d7b2467eeb7aaf70f2ffd30401fa56a8dd3ac6d7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__557f9290aa3eb89aaa99d1c63122d3d8060c4db3bdaf709415bb94223663a414(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f33163efc8732afa673e6798a58975293aef3cda79692360c2c16f61429d890a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__490cedfc9e4a2960454cdf768371794b47c730fc81b23d634397515e71b3da72(
    value: typing.Optional[LaunchConfigurationMetadataOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66702487553b91245c2a71fb90ef77900114d1ed5cc1740f9a9c56bbf52ca681(
    *,
    delete_on_termination: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    encrypted: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    iops: typing.Optional[jsii.Number] = None,
    throughput: typing.Optional[jsii.Number] = None,
    volume_size: typing.Optional[jsii.Number] = None,
    volume_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f967104deb992a096a88f40411b05d6d3d6320e1764a1f54528ec2ebf5eaf40(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c74a6243fddb8e5eccd9986cf7dee755a06f8790ac98bc86d42e25a479d870f(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae23884940d58654534b3f6bee59a5b0ff3eca12dc5c28e10e4b6628a7db8d98(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0717dfda67a79e64c7e9be9cc154dccfb612767969b1e3cd5e73190dce8b96f(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e995d02ddfca01e10cda722c45056770fa44906600f728745cf6a31dbe713d2(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0c6e8a731bd174c6acf34856cecd52efad50c6647201e45965c8084e34855e0(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88d9c7e6ad53b188d45c664c81c797768289ca22f6577124615099979edc4c07(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__422417fc76164e038049906b41e6e95db2872325ee030970b03767dee3afb3b1(
    value: typing.Optional[LaunchConfigurationRootBlockDevice],
) -> None:
    """Type checking stubs"""
    pass
