'''
# `aws_storagegateway_gateway`

Refer to the Terraform Registory for docs: [`aws_storagegateway_gateway`](https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway).
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


class StoragegatewayGateway(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.storagegatewayGateway.StoragegatewayGateway",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway aws_storagegateway_gateway}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        gateway_name: builtins.str,
        gateway_timezone: builtins.str,
        activation_key: typing.Optional[builtins.str] = None,
        average_download_rate_limit_in_bits_per_sec: typing.Optional[jsii.Number] = None,
        average_upload_rate_limit_in_bits_per_sec: typing.Optional[jsii.Number] = None,
        cloudwatch_log_group_arn: typing.Optional[builtins.str] = None,
        gateway_ip_address: typing.Optional[builtins.str] = None,
        gateway_type: typing.Optional[builtins.str] = None,
        gateway_vpc_endpoint: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        maintenance_start_time: typing.Optional[typing.Union["StoragegatewayGatewayMaintenanceStartTime", typing.Dict[builtins.str, typing.Any]]] = None,
        medium_changer_type: typing.Optional[builtins.str] = None,
        smb_active_directory_settings: typing.Optional[typing.Union["StoragegatewayGatewaySmbActiveDirectorySettings", typing.Dict[builtins.str, typing.Any]]] = None,
        smb_file_share_visibility: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        smb_guest_password: typing.Optional[builtins.str] = None,
        smb_security_strategy: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tape_drive_type: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["StoragegatewayGatewayTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway aws_storagegateway_gateway} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param gateway_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#gateway_name StoragegatewayGateway#gateway_name}.
        :param gateway_timezone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#gateway_timezone StoragegatewayGateway#gateway_timezone}.
        :param activation_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#activation_key StoragegatewayGateway#activation_key}.
        :param average_download_rate_limit_in_bits_per_sec: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#average_download_rate_limit_in_bits_per_sec StoragegatewayGateway#average_download_rate_limit_in_bits_per_sec}.
        :param average_upload_rate_limit_in_bits_per_sec: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#average_upload_rate_limit_in_bits_per_sec StoragegatewayGateway#average_upload_rate_limit_in_bits_per_sec}.
        :param cloudwatch_log_group_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#cloudwatch_log_group_arn StoragegatewayGateway#cloudwatch_log_group_arn}.
        :param gateway_ip_address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#gateway_ip_address StoragegatewayGateway#gateway_ip_address}.
        :param gateway_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#gateway_type StoragegatewayGateway#gateway_type}.
        :param gateway_vpc_endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#gateway_vpc_endpoint StoragegatewayGateway#gateway_vpc_endpoint}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#id StoragegatewayGateway#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param maintenance_start_time: maintenance_start_time block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#maintenance_start_time StoragegatewayGateway#maintenance_start_time}
        :param medium_changer_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#medium_changer_type StoragegatewayGateway#medium_changer_type}.
        :param smb_active_directory_settings: smb_active_directory_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#smb_active_directory_settings StoragegatewayGateway#smb_active_directory_settings}
        :param smb_file_share_visibility: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#smb_file_share_visibility StoragegatewayGateway#smb_file_share_visibility}.
        :param smb_guest_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#smb_guest_password StoragegatewayGateway#smb_guest_password}.
        :param smb_security_strategy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#smb_security_strategy StoragegatewayGateway#smb_security_strategy}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#tags StoragegatewayGateway#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#tags_all StoragegatewayGateway#tags_all}.
        :param tape_drive_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#tape_drive_type StoragegatewayGateway#tape_drive_type}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#timeouts StoragegatewayGateway#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a8b22476c0b0e0c29f1f81668590cb21bcc8f5f8cf21f529981dc91db97cb237)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = StoragegatewayGatewayConfig(
            gateway_name=gateway_name,
            gateway_timezone=gateway_timezone,
            activation_key=activation_key,
            average_download_rate_limit_in_bits_per_sec=average_download_rate_limit_in_bits_per_sec,
            average_upload_rate_limit_in_bits_per_sec=average_upload_rate_limit_in_bits_per_sec,
            cloudwatch_log_group_arn=cloudwatch_log_group_arn,
            gateway_ip_address=gateway_ip_address,
            gateway_type=gateway_type,
            gateway_vpc_endpoint=gateway_vpc_endpoint,
            id=id,
            maintenance_start_time=maintenance_start_time,
            medium_changer_type=medium_changer_type,
            smb_active_directory_settings=smb_active_directory_settings,
            smb_file_share_visibility=smb_file_share_visibility,
            smb_guest_password=smb_guest_password,
            smb_security_strategy=smb_security_strategy,
            tags=tags,
            tags_all=tags_all,
            tape_drive_type=tape_drive_type,
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

    @jsii.member(jsii_name="putMaintenanceStartTime")
    def put_maintenance_start_time(
        self,
        *,
        hour_of_day: jsii.Number,
        day_of_month: typing.Optional[builtins.str] = None,
        day_of_week: typing.Optional[builtins.str] = None,
        minute_of_hour: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param hour_of_day: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#hour_of_day StoragegatewayGateway#hour_of_day}.
        :param day_of_month: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#day_of_month StoragegatewayGateway#day_of_month}.
        :param day_of_week: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#day_of_week StoragegatewayGateway#day_of_week}.
        :param minute_of_hour: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#minute_of_hour StoragegatewayGateway#minute_of_hour}.
        '''
        value = StoragegatewayGatewayMaintenanceStartTime(
            hour_of_day=hour_of_day,
            day_of_month=day_of_month,
            day_of_week=day_of_week,
            minute_of_hour=minute_of_hour,
        )

        return typing.cast(None, jsii.invoke(self, "putMaintenanceStartTime", [value]))

    @jsii.member(jsii_name="putSmbActiveDirectorySettings")
    def put_smb_active_directory_settings(
        self,
        *,
        domain_name: builtins.str,
        password: builtins.str,
        username: builtins.str,
        domain_controllers: typing.Optional[typing.Sequence[builtins.str]] = None,
        organizational_unit: typing.Optional[builtins.str] = None,
        timeout_in_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param domain_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#domain_name StoragegatewayGateway#domain_name}.
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#password StoragegatewayGateway#password}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#username StoragegatewayGateway#username}.
        :param domain_controllers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#domain_controllers StoragegatewayGateway#domain_controllers}.
        :param organizational_unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#organizational_unit StoragegatewayGateway#organizational_unit}.
        :param timeout_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#timeout_in_seconds StoragegatewayGateway#timeout_in_seconds}.
        '''
        value = StoragegatewayGatewaySmbActiveDirectorySettings(
            domain_name=domain_name,
            password=password,
            username=username,
            domain_controllers=domain_controllers,
            organizational_unit=organizational_unit,
            timeout_in_seconds=timeout_in_seconds,
        )

        return typing.cast(None, jsii.invoke(self, "putSmbActiveDirectorySettings", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(self, *, create: typing.Optional[builtins.str] = None) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#create StoragegatewayGateway#create}.
        '''
        value = StoragegatewayGatewayTimeouts(create=create)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetActivationKey")
    def reset_activation_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetActivationKey", []))

    @jsii.member(jsii_name="resetAverageDownloadRateLimitInBitsPerSec")
    def reset_average_download_rate_limit_in_bits_per_sec(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAverageDownloadRateLimitInBitsPerSec", []))

    @jsii.member(jsii_name="resetAverageUploadRateLimitInBitsPerSec")
    def reset_average_upload_rate_limit_in_bits_per_sec(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAverageUploadRateLimitInBitsPerSec", []))

    @jsii.member(jsii_name="resetCloudwatchLogGroupArn")
    def reset_cloudwatch_log_group_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudwatchLogGroupArn", []))

    @jsii.member(jsii_name="resetGatewayIpAddress")
    def reset_gateway_ip_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGatewayIpAddress", []))

    @jsii.member(jsii_name="resetGatewayType")
    def reset_gateway_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGatewayType", []))

    @jsii.member(jsii_name="resetGatewayVpcEndpoint")
    def reset_gateway_vpc_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGatewayVpcEndpoint", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMaintenanceStartTime")
    def reset_maintenance_start_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaintenanceStartTime", []))

    @jsii.member(jsii_name="resetMediumChangerType")
    def reset_medium_changer_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMediumChangerType", []))

    @jsii.member(jsii_name="resetSmbActiveDirectorySettings")
    def reset_smb_active_directory_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSmbActiveDirectorySettings", []))

    @jsii.member(jsii_name="resetSmbFileShareVisibility")
    def reset_smb_file_share_visibility(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSmbFileShareVisibility", []))

    @jsii.member(jsii_name="resetSmbGuestPassword")
    def reset_smb_guest_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSmbGuestPassword", []))

    @jsii.member(jsii_name="resetSmbSecurityStrategy")
    def reset_smb_security_strategy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSmbSecurityStrategy", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetTapeDriveType")
    def reset_tape_drive_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTapeDriveType", []))

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
    @jsii.member(jsii_name="ec2InstanceId")
    def ec2_instance_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ec2InstanceId"))

    @builtins.property
    @jsii.member(jsii_name="endpointType")
    def endpoint_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpointType"))

    @builtins.property
    @jsii.member(jsii_name="gatewayId")
    def gateway_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gatewayId"))

    @builtins.property
    @jsii.member(jsii_name="gatewayNetworkInterface")
    def gateway_network_interface(
        self,
    ) -> "StoragegatewayGatewayGatewayNetworkInterfaceList":
        return typing.cast("StoragegatewayGatewayGatewayNetworkInterfaceList", jsii.get(self, "gatewayNetworkInterface"))

    @builtins.property
    @jsii.member(jsii_name="hostEnvironment")
    def host_environment(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostEnvironment"))

    @builtins.property
    @jsii.member(jsii_name="maintenanceStartTime")
    def maintenance_start_time(
        self,
    ) -> "StoragegatewayGatewayMaintenanceStartTimeOutputReference":
        return typing.cast("StoragegatewayGatewayMaintenanceStartTimeOutputReference", jsii.get(self, "maintenanceStartTime"))

    @builtins.property
    @jsii.member(jsii_name="smbActiveDirectorySettings")
    def smb_active_directory_settings(
        self,
    ) -> "StoragegatewayGatewaySmbActiveDirectorySettingsOutputReference":
        return typing.cast("StoragegatewayGatewaySmbActiveDirectorySettingsOutputReference", jsii.get(self, "smbActiveDirectorySettings"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "StoragegatewayGatewayTimeoutsOutputReference":
        return typing.cast("StoragegatewayGatewayTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="activationKeyInput")
    def activation_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "activationKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="averageDownloadRateLimitInBitsPerSecInput")
    def average_download_rate_limit_in_bits_per_sec_input(
        self,
    ) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "averageDownloadRateLimitInBitsPerSecInput"))

    @builtins.property
    @jsii.member(jsii_name="averageUploadRateLimitInBitsPerSecInput")
    def average_upload_rate_limit_in_bits_per_sec_input(
        self,
    ) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "averageUploadRateLimitInBitsPerSecInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchLogGroupArnInput")
    def cloudwatch_log_group_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cloudwatchLogGroupArnInput"))

    @builtins.property
    @jsii.member(jsii_name="gatewayIpAddressInput")
    def gateway_ip_address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "gatewayIpAddressInput"))

    @builtins.property
    @jsii.member(jsii_name="gatewayNameInput")
    def gateway_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "gatewayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="gatewayTimezoneInput")
    def gateway_timezone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "gatewayTimezoneInput"))

    @builtins.property
    @jsii.member(jsii_name="gatewayTypeInput")
    def gateway_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "gatewayTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="gatewayVpcEndpointInput")
    def gateway_vpc_endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "gatewayVpcEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="maintenanceStartTimeInput")
    def maintenance_start_time_input(
        self,
    ) -> typing.Optional["StoragegatewayGatewayMaintenanceStartTime"]:
        return typing.cast(typing.Optional["StoragegatewayGatewayMaintenanceStartTime"], jsii.get(self, "maintenanceStartTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="mediumChangerTypeInput")
    def medium_changer_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mediumChangerTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="smbActiveDirectorySettingsInput")
    def smb_active_directory_settings_input(
        self,
    ) -> typing.Optional["StoragegatewayGatewaySmbActiveDirectorySettings"]:
        return typing.cast(typing.Optional["StoragegatewayGatewaySmbActiveDirectorySettings"], jsii.get(self, "smbActiveDirectorySettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="smbFileShareVisibilityInput")
    def smb_file_share_visibility_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "smbFileShareVisibilityInput"))

    @builtins.property
    @jsii.member(jsii_name="smbGuestPasswordInput")
    def smb_guest_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "smbGuestPasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="smbSecurityStrategyInput")
    def smb_security_strategy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "smbSecurityStrategyInput"))

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
    @jsii.member(jsii_name="tapeDriveTypeInput")
    def tape_drive_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tapeDriveTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["StoragegatewayGatewayTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["StoragegatewayGatewayTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="activationKey")
    def activation_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "activationKey"))

    @activation_key.setter
    def activation_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__28f7fe0b669c8ea23b4e035ece6cf748eb741a797a12b12294b2329959b2854c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "activationKey", value)

    @builtins.property
    @jsii.member(jsii_name="averageDownloadRateLimitInBitsPerSec")
    def average_download_rate_limit_in_bits_per_sec(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "averageDownloadRateLimitInBitsPerSec"))

    @average_download_rate_limit_in_bits_per_sec.setter
    def average_download_rate_limit_in_bits_per_sec(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f19bf11fd3cf6f378bd60a7729b7645e16c5f7532b549e1bea40a2b68d27f605)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "averageDownloadRateLimitInBitsPerSec", value)

    @builtins.property
    @jsii.member(jsii_name="averageUploadRateLimitInBitsPerSec")
    def average_upload_rate_limit_in_bits_per_sec(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "averageUploadRateLimitInBitsPerSec"))

    @average_upload_rate_limit_in_bits_per_sec.setter
    def average_upload_rate_limit_in_bits_per_sec(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c680832afd4e5da176a1719b7aacd14c0dc3472388260880dae7454cf1edf6d3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "averageUploadRateLimitInBitsPerSec", value)

    @builtins.property
    @jsii.member(jsii_name="cloudwatchLogGroupArn")
    def cloudwatch_log_group_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cloudwatchLogGroupArn"))

    @cloudwatch_log_group_arn.setter
    def cloudwatch_log_group_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e661c0b81a9151cd5cb9ee8ac010cefafee9857394a49f049be8ee911724951)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloudwatchLogGroupArn", value)

    @builtins.property
    @jsii.member(jsii_name="gatewayIpAddress")
    def gateway_ip_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gatewayIpAddress"))

    @gateway_ip_address.setter
    def gateway_ip_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19babfd143764e888da8090082f263c5838f75806afe628c535d0562c7566c89)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gatewayIpAddress", value)

    @builtins.property
    @jsii.member(jsii_name="gatewayName")
    def gateway_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gatewayName"))

    @gateway_name.setter
    def gateway_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75b5e2fa2bcbfedd26c35f375534a8a670ac5a49430b97dcb030a033cccc2d05)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gatewayName", value)

    @builtins.property
    @jsii.member(jsii_name="gatewayTimezone")
    def gateway_timezone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gatewayTimezone"))

    @gateway_timezone.setter
    def gateway_timezone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3975b19fe4989f688ef40b0e8a1be9d803b9b00755199b39eba3cef3e10ad3fb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gatewayTimezone", value)

    @builtins.property
    @jsii.member(jsii_name="gatewayType")
    def gateway_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gatewayType"))

    @gateway_type.setter
    def gateway_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__007816211d33d2a5cf92d8137e1291412f87d52dea2265129c5d992721f7d1a3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gatewayType", value)

    @builtins.property
    @jsii.member(jsii_name="gatewayVpcEndpoint")
    def gateway_vpc_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gatewayVpcEndpoint"))

    @gateway_vpc_endpoint.setter
    def gateway_vpc_endpoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00bc7a409de11febdcc7d0e3c3746f34ff4b8ca467ee1f313c5c7a2f7607729b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gatewayVpcEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95b677e90132c063fb483a24a0fac2733800092a6497c66a0f61e75b9cc8500e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="mediumChangerType")
    def medium_changer_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mediumChangerType"))

    @medium_changer_type.setter
    def medium_changer_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5058a964bf987f642980679084aa2236addf90d49f8d2f5c4226691a3bc06453)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mediumChangerType", value)

    @builtins.property
    @jsii.member(jsii_name="smbFileShareVisibility")
    def smb_file_share_visibility(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "smbFileShareVisibility"))

    @smb_file_share_visibility.setter
    def smb_file_share_visibility(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f786ae2607a6338d0e4a91b04693f2b311e77e063f66cf365999d93221971f5b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "smbFileShareVisibility", value)

    @builtins.property
    @jsii.member(jsii_name="smbGuestPassword")
    def smb_guest_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "smbGuestPassword"))

    @smb_guest_password.setter
    def smb_guest_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5a598d2d8f39ffab318fb9d35e0d88227067b7eed902ba264d938d61f163d32)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "smbGuestPassword", value)

    @builtins.property
    @jsii.member(jsii_name="smbSecurityStrategy")
    def smb_security_strategy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "smbSecurityStrategy"))

    @smb_security_strategy.setter
    def smb_security_strategy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f28a91dbefa188bdcb4765a4602c85d59c14f4efe0f853f003805f661a9e6aff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "smbSecurityStrategy", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a8ffd3b0f8fb239cfaacbc71f9ecbae7f88c036b82159e11ae030b49dea61aea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11b78697db52078737162fc0d7ef0f23c3e800321214d3cbf83f2ed4925218c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)

    @builtins.property
    @jsii.member(jsii_name="tapeDriveType")
    def tape_drive_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tapeDriveType"))

    @tape_drive_type.setter
    def tape_drive_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42b8be1ca0fe4aad07c3001aad32bf9517177719bbab6e5dded39d7c8dc9b078)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tapeDriveType", value)


@jsii.data_type(
    jsii_type="aws.storagegatewayGateway.StoragegatewayGatewayConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "gateway_name": "gatewayName",
        "gateway_timezone": "gatewayTimezone",
        "activation_key": "activationKey",
        "average_download_rate_limit_in_bits_per_sec": "averageDownloadRateLimitInBitsPerSec",
        "average_upload_rate_limit_in_bits_per_sec": "averageUploadRateLimitInBitsPerSec",
        "cloudwatch_log_group_arn": "cloudwatchLogGroupArn",
        "gateway_ip_address": "gatewayIpAddress",
        "gateway_type": "gatewayType",
        "gateway_vpc_endpoint": "gatewayVpcEndpoint",
        "id": "id",
        "maintenance_start_time": "maintenanceStartTime",
        "medium_changer_type": "mediumChangerType",
        "smb_active_directory_settings": "smbActiveDirectorySettings",
        "smb_file_share_visibility": "smbFileShareVisibility",
        "smb_guest_password": "smbGuestPassword",
        "smb_security_strategy": "smbSecurityStrategy",
        "tags": "tags",
        "tags_all": "tagsAll",
        "tape_drive_type": "tapeDriveType",
        "timeouts": "timeouts",
    },
)
class StoragegatewayGatewayConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        gateway_name: builtins.str,
        gateway_timezone: builtins.str,
        activation_key: typing.Optional[builtins.str] = None,
        average_download_rate_limit_in_bits_per_sec: typing.Optional[jsii.Number] = None,
        average_upload_rate_limit_in_bits_per_sec: typing.Optional[jsii.Number] = None,
        cloudwatch_log_group_arn: typing.Optional[builtins.str] = None,
        gateway_ip_address: typing.Optional[builtins.str] = None,
        gateway_type: typing.Optional[builtins.str] = None,
        gateway_vpc_endpoint: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        maintenance_start_time: typing.Optional[typing.Union["StoragegatewayGatewayMaintenanceStartTime", typing.Dict[builtins.str, typing.Any]]] = None,
        medium_changer_type: typing.Optional[builtins.str] = None,
        smb_active_directory_settings: typing.Optional[typing.Union["StoragegatewayGatewaySmbActiveDirectorySettings", typing.Dict[builtins.str, typing.Any]]] = None,
        smb_file_share_visibility: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        smb_guest_password: typing.Optional[builtins.str] = None,
        smb_security_strategy: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tape_drive_type: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["StoragegatewayGatewayTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param gateway_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#gateway_name StoragegatewayGateway#gateway_name}.
        :param gateway_timezone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#gateway_timezone StoragegatewayGateway#gateway_timezone}.
        :param activation_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#activation_key StoragegatewayGateway#activation_key}.
        :param average_download_rate_limit_in_bits_per_sec: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#average_download_rate_limit_in_bits_per_sec StoragegatewayGateway#average_download_rate_limit_in_bits_per_sec}.
        :param average_upload_rate_limit_in_bits_per_sec: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#average_upload_rate_limit_in_bits_per_sec StoragegatewayGateway#average_upload_rate_limit_in_bits_per_sec}.
        :param cloudwatch_log_group_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#cloudwatch_log_group_arn StoragegatewayGateway#cloudwatch_log_group_arn}.
        :param gateway_ip_address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#gateway_ip_address StoragegatewayGateway#gateway_ip_address}.
        :param gateway_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#gateway_type StoragegatewayGateway#gateway_type}.
        :param gateway_vpc_endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#gateway_vpc_endpoint StoragegatewayGateway#gateway_vpc_endpoint}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#id StoragegatewayGateway#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param maintenance_start_time: maintenance_start_time block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#maintenance_start_time StoragegatewayGateway#maintenance_start_time}
        :param medium_changer_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#medium_changer_type StoragegatewayGateway#medium_changer_type}.
        :param smb_active_directory_settings: smb_active_directory_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#smb_active_directory_settings StoragegatewayGateway#smb_active_directory_settings}
        :param smb_file_share_visibility: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#smb_file_share_visibility StoragegatewayGateway#smb_file_share_visibility}.
        :param smb_guest_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#smb_guest_password StoragegatewayGateway#smb_guest_password}.
        :param smb_security_strategy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#smb_security_strategy StoragegatewayGateway#smb_security_strategy}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#tags StoragegatewayGateway#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#tags_all StoragegatewayGateway#tags_all}.
        :param tape_drive_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#tape_drive_type StoragegatewayGateway#tape_drive_type}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#timeouts StoragegatewayGateway#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(maintenance_start_time, dict):
            maintenance_start_time = StoragegatewayGatewayMaintenanceStartTime(**maintenance_start_time)
        if isinstance(smb_active_directory_settings, dict):
            smb_active_directory_settings = StoragegatewayGatewaySmbActiveDirectorySettings(**smb_active_directory_settings)
        if isinstance(timeouts, dict):
            timeouts = StoragegatewayGatewayTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3e014d7c1008dcb433ce3d6d2e2bab7fc4274485f28299ed99de67f2ec18c5a)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument gateway_name", value=gateway_name, expected_type=type_hints["gateway_name"])
            check_type(argname="argument gateway_timezone", value=gateway_timezone, expected_type=type_hints["gateway_timezone"])
            check_type(argname="argument activation_key", value=activation_key, expected_type=type_hints["activation_key"])
            check_type(argname="argument average_download_rate_limit_in_bits_per_sec", value=average_download_rate_limit_in_bits_per_sec, expected_type=type_hints["average_download_rate_limit_in_bits_per_sec"])
            check_type(argname="argument average_upload_rate_limit_in_bits_per_sec", value=average_upload_rate_limit_in_bits_per_sec, expected_type=type_hints["average_upload_rate_limit_in_bits_per_sec"])
            check_type(argname="argument cloudwatch_log_group_arn", value=cloudwatch_log_group_arn, expected_type=type_hints["cloudwatch_log_group_arn"])
            check_type(argname="argument gateway_ip_address", value=gateway_ip_address, expected_type=type_hints["gateway_ip_address"])
            check_type(argname="argument gateway_type", value=gateway_type, expected_type=type_hints["gateway_type"])
            check_type(argname="argument gateway_vpc_endpoint", value=gateway_vpc_endpoint, expected_type=type_hints["gateway_vpc_endpoint"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument maintenance_start_time", value=maintenance_start_time, expected_type=type_hints["maintenance_start_time"])
            check_type(argname="argument medium_changer_type", value=medium_changer_type, expected_type=type_hints["medium_changer_type"])
            check_type(argname="argument smb_active_directory_settings", value=smb_active_directory_settings, expected_type=type_hints["smb_active_directory_settings"])
            check_type(argname="argument smb_file_share_visibility", value=smb_file_share_visibility, expected_type=type_hints["smb_file_share_visibility"])
            check_type(argname="argument smb_guest_password", value=smb_guest_password, expected_type=type_hints["smb_guest_password"])
            check_type(argname="argument smb_security_strategy", value=smb_security_strategy, expected_type=type_hints["smb_security_strategy"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument tape_drive_type", value=tape_drive_type, expected_type=type_hints["tape_drive_type"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "gateway_name": gateway_name,
            "gateway_timezone": gateway_timezone,
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
        if activation_key is not None:
            self._values["activation_key"] = activation_key
        if average_download_rate_limit_in_bits_per_sec is not None:
            self._values["average_download_rate_limit_in_bits_per_sec"] = average_download_rate_limit_in_bits_per_sec
        if average_upload_rate_limit_in_bits_per_sec is not None:
            self._values["average_upload_rate_limit_in_bits_per_sec"] = average_upload_rate_limit_in_bits_per_sec
        if cloudwatch_log_group_arn is not None:
            self._values["cloudwatch_log_group_arn"] = cloudwatch_log_group_arn
        if gateway_ip_address is not None:
            self._values["gateway_ip_address"] = gateway_ip_address
        if gateway_type is not None:
            self._values["gateway_type"] = gateway_type
        if gateway_vpc_endpoint is not None:
            self._values["gateway_vpc_endpoint"] = gateway_vpc_endpoint
        if id is not None:
            self._values["id"] = id
        if maintenance_start_time is not None:
            self._values["maintenance_start_time"] = maintenance_start_time
        if medium_changer_type is not None:
            self._values["medium_changer_type"] = medium_changer_type
        if smb_active_directory_settings is not None:
            self._values["smb_active_directory_settings"] = smb_active_directory_settings
        if smb_file_share_visibility is not None:
            self._values["smb_file_share_visibility"] = smb_file_share_visibility
        if smb_guest_password is not None:
            self._values["smb_guest_password"] = smb_guest_password
        if smb_security_strategy is not None:
            self._values["smb_security_strategy"] = smb_security_strategy
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if tape_drive_type is not None:
            self._values["tape_drive_type"] = tape_drive_type
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
    def gateway_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#gateway_name StoragegatewayGateway#gateway_name}.'''
        result = self._values.get("gateway_name")
        assert result is not None, "Required property 'gateway_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def gateway_timezone(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#gateway_timezone StoragegatewayGateway#gateway_timezone}.'''
        result = self._values.get("gateway_timezone")
        assert result is not None, "Required property 'gateway_timezone' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def activation_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#activation_key StoragegatewayGateway#activation_key}.'''
        result = self._values.get("activation_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def average_download_rate_limit_in_bits_per_sec(
        self,
    ) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#average_download_rate_limit_in_bits_per_sec StoragegatewayGateway#average_download_rate_limit_in_bits_per_sec}.'''
        result = self._values.get("average_download_rate_limit_in_bits_per_sec")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def average_upload_rate_limit_in_bits_per_sec(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#average_upload_rate_limit_in_bits_per_sec StoragegatewayGateway#average_upload_rate_limit_in_bits_per_sec}.'''
        result = self._values.get("average_upload_rate_limit_in_bits_per_sec")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def cloudwatch_log_group_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#cloudwatch_log_group_arn StoragegatewayGateway#cloudwatch_log_group_arn}.'''
        result = self._values.get("cloudwatch_log_group_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def gateway_ip_address(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#gateway_ip_address StoragegatewayGateway#gateway_ip_address}.'''
        result = self._values.get("gateway_ip_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def gateway_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#gateway_type StoragegatewayGateway#gateway_type}.'''
        result = self._values.get("gateway_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def gateway_vpc_endpoint(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#gateway_vpc_endpoint StoragegatewayGateway#gateway_vpc_endpoint}.'''
        result = self._values.get("gateway_vpc_endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#id StoragegatewayGateway#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def maintenance_start_time(
        self,
    ) -> typing.Optional["StoragegatewayGatewayMaintenanceStartTime"]:
        '''maintenance_start_time block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#maintenance_start_time StoragegatewayGateway#maintenance_start_time}
        '''
        result = self._values.get("maintenance_start_time")
        return typing.cast(typing.Optional["StoragegatewayGatewayMaintenanceStartTime"], result)

    @builtins.property
    def medium_changer_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#medium_changer_type StoragegatewayGateway#medium_changer_type}.'''
        result = self._values.get("medium_changer_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def smb_active_directory_settings(
        self,
    ) -> typing.Optional["StoragegatewayGatewaySmbActiveDirectorySettings"]:
        '''smb_active_directory_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#smb_active_directory_settings StoragegatewayGateway#smb_active_directory_settings}
        '''
        result = self._values.get("smb_active_directory_settings")
        return typing.cast(typing.Optional["StoragegatewayGatewaySmbActiveDirectorySettings"], result)

    @builtins.property
    def smb_file_share_visibility(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#smb_file_share_visibility StoragegatewayGateway#smb_file_share_visibility}.'''
        result = self._values.get("smb_file_share_visibility")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def smb_guest_password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#smb_guest_password StoragegatewayGateway#smb_guest_password}.'''
        result = self._values.get("smb_guest_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def smb_security_strategy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#smb_security_strategy StoragegatewayGateway#smb_security_strategy}.'''
        result = self._values.get("smb_security_strategy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#tags StoragegatewayGateway#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#tags_all StoragegatewayGateway#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tape_drive_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#tape_drive_type StoragegatewayGateway#tape_drive_type}.'''
        result = self._values.get("tape_drive_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["StoragegatewayGatewayTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#timeouts StoragegatewayGateway#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["StoragegatewayGatewayTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StoragegatewayGatewayConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.storagegatewayGateway.StoragegatewayGatewayGatewayNetworkInterface",
    jsii_struct_bases=[],
    name_mapping={},
)
class StoragegatewayGatewayGatewayNetworkInterface:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StoragegatewayGatewayGatewayNetworkInterface(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StoragegatewayGatewayGatewayNetworkInterfaceList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.storagegatewayGateway.StoragegatewayGatewayGatewayNetworkInterfaceList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8e846f64a242223456a05d0d963d1a8693648fb8f63440b2c56153eb3f5b434a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "StoragegatewayGatewayGatewayNetworkInterfaceOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f465108711e0ad203dc61e2db588f3eb9cd6cac5e54a5c7d4bab810138e3aaaf)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("StoragegatewayGatewayGatewayNetworkInterfaceOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__426255a50c2752366f8b30abc7ad668d83ce20a4236208d69475b62116cc2972)
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
            type_hints = typing.get_type_hints(_typecheckingstub__52e97c85a3cbd9cfa1bb8d97980b8053f6b86ae5370773323b6e9db4c8de659c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__888d0b41b2d1783247bb35d7a58d560a4d77556baf3e2dc4ca3925ff247e6f10)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class StoragegatewayGatewayGatewayNetworkInterfaceOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.storagegatewayGateway.StoragegatewayGatewayGatewayNetworkInterfaceOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e9f86ad9299503b3fd2129172424081d1d445c7b75939f39a2843fba5f49804c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="ipv4Address")
    def ipv4_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipv4Address"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[StoragegatewayGatewayGatewayNetworkInterface]:
        return typing.cast(typing.Optional[StoragegatewayGatewayGatewayNetworkInterface], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[StoragegatewayGatewayGatewayNetworkInterface],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8326968b3b5ad2fd914d5d62a634af4891f6e684f126bb8b589540c81d7a3d6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.storagegatewayGateway.StoragegatewayGatewayMaintenanceStartTime",
    jsii_struct_bases=[],
    name_mapping={
        "hour_of_day": "hourOfDay",
        "day_of_month": "dayOfMonth",
        "day_of_week": "dayOfWeek",
        "minute_of_hour": "minuteOfHour",
    },
)
class StoragegatewayGatewayMaintenanceStartTime:
    def __init__(
        self,
        *,
        hour_of_day: jsii.Number,
        day_of_month: typing.Optional[builtins.str] = None,
        day_of_week: typing.Optional[builtins.str] = None,
        minute_of_hour: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param hour_of_day: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#hour_of_day StoragegatewayGateway#hour_of_day}.
        :param day_of_month: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#day_of_month StoragegatewayGateway#day_of_month}.
        :param day_of_week: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#day_of_week StoragegatewayGateway#day_of_week}.
        :param minute_of_hour: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#minute_of_hour StoragegatewayGateway#minute_of_hour}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29e5e393e285a96638c50a477c06cba92e54624156fa02f60ee859a90450727c)
            check_type(argname="argument hour_of_day", value=hour_of_day, expected_type=type_hints["hour_of_day"])
            check_type(argname="argument day_of_month", value=day_of_month, expected_type=type_hints["day_of_month"])
            check_type(argname="argument day_of_week", value=day_of_week, expected_type=type_hints["day_of_week"])
            check_type(argname="argument minute_of_hour", value=minute_of_hour, expected_type=type_hints["minute_of_hour"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "hour_of_day": hour_of_day,
        }
        if day_of_month is not None:
            self._values["day_of_month"] = day_of_month
        if day_of_week is not None:
            self._values["day_of_week"] = day_of_week
        if minute_of_hour is not None:
            self._values["minute_of_hour"] = minute_of_hour

    @builtins.property
    def hour_of_day(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#hour_of_day StoragegatewayGateway#hour_of_day}.'''
        result = self._values.get("hour_of_day")
        assert result is not None, "Required property 'hour_of_day' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def day_of_month(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#day_of_month StoragegatewayGateway#day_of_month}.'''
        result = self._values.get("day_of_month")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def day_of_week(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#day_of_week StoragegatewayGateway#day_of_week}.'''
        result = self._values.get("day_of_week")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def minute_of_hour(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#minute_of_hour StoragegatewayGateway#minute_of_hour}.'''
        result = self._values.get("minute_of_hour")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StoragegatewayGatewayMaintenanceStartTime(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StoragegatewayGatewayMaintenanceStartTimeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.storagegatewayGateway.StoragegatewayGatewayMaintenanceStartTimeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a9be326a7bb0527df9bf51eccf0c7062fd4072dbcf9df048cccc7bcce28f6a0c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDayOfMonth")
    def reset_day_of_month(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDayOfMonth", []))

    @jsii.member(jsii_name="resetDayOfWeek")
    def reset_day_of_week(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDayOfWeek", []))

    @jsii.member(jsii_name="resetMinuteOfHour")
    def reset_minute_of_hour(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinuteOfHour", []))

    @builtins.property
    @jsii.member(jsii_name="dayOfMonthInput")
    def day_of_month_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dayOfMonthInput"))

    @builtins.property
    @jsii.member(jsii_name="dayOfWeekInput")
    def day_of_week_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dayOfWeekInput"))

    @builtins.property
    @jsii.member(jsii_name="hourOfDayInput")
    def hour_of_day_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "hourOfDayInput"))

    @builtins.property
    @jsii.member(jsii_name="minuteOfHourInput")
    def minute_of_hour_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minuteOfHourInput"))

    @builtins.property
    @jsii.member(jsii_name="dayOfMonth")
    def day_of_month(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dayOfMonth"))

    @day_of_month.setter
    def day_of_month(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c45a697eec8b0d9a5c483ba386c68ebc15c4a0918d11065e3104c4a85c47cd3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dayOfMonth", value)

    @builtins.property
    @jsii.member(jsii_name="dayOfWeek")
    def day_of_week(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dayOfWeek"))

    @day_of_week.setter
    def day_of_week(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4b1466b428eeef81e3ec1d2e638c99246f0df2d4e89e1b6f92e2e13a960597e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dayOfWeek", value)

    @builtins.property
    @jsii.member(jsii_name="hourOfDay")
    def hour_of_day(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "hourOfDay"))

    @hour_of_day.setter
    def hour_of_day(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26e33a4eba34068cdcb4c6c7c60a7f7dc8d222027728c8e09c53f115c7825319)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hourOfDay", value)

    @builtins.property
    @jsii.member(jsii_name="minuteOfHour")
    def minute_of_hour(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minuteOfHour"))

    @minute_of_hour.setter
    def minute_of_hour(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b14946cdc0cc32eaaee24b1d20576cc3965970e90676335e7964a0df521f774a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minuteOfHour", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[StoragegatewayGatewayMaintenanceStartTime]:
        return typing.cast(typing.Optional[StoragegatewayGatewayMaintenanceStartTime], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[StoragegatewayGatewayMaintenanceStartTime],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e0ee955de035985e0a2d828c5aa7cc76957c280ffffbae43364ac567ac7396b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.storagegatewayGateway.StoragegatewayGatewaySmbActiveDirectorySettings",
    jsii_struct_bases=[],
    name_mapping={
        "domain_name": "domainName",
        "password": "password",
        "username": "username",
        "domain_controllers": "domainControllers",
        "organizational_unit": "organizationalUnit",
        "timeout_in_seconds": "timeoutInSeconds",
    },
)
class StoragegatewayGatewaySmbActiveDirectorySettings:
    def __init__(
        self,
        *,
        domain_name: builtins.str,
        password: builtins.str,
        username: builtins.str,
        domain_controllers: typing.Optional[typing.Sequence[builtins.str]] = None,
        organizational_unit: typing.Optional[builtins.str] = None,
        timeout_in_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param domain_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#domain_name StoragegatewayGateway#domain_name}.
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#password StoragegatewayGateway#password}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#username StoragegatewayGateway#username}.
        :param domain_controllers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#domain_controllers StoragegatewayGateway#domain_controllers}.
        :param organizational_unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#organizational_unit StoragegatewayGateway#organizational_unit}.
        :param timeout_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#timeout_in_seconds StoragegatewayGateway#timeout_in_seconds}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd8ea3df43c10149dbf6d2017772614cb58a1abcaea82faba6ef00fa2cc73687)
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            check_type(argname="argument domain_controllers", value=domain_controllers, expected_type=type_hints["domain_controllers"])
            check_type(argname="argument organizational_unit", value=organizational_unit, expected_type=type_hints["organizational_unit"])
            check_type(argname="argument timeout_in_seconds", value=timeout_in_seconds, expected_type=type_hints["timeout_in_seconds"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_name": domain_name,
            "password": password,
            "username": username,
        }
        if domain_controllers is not None:
            self._values["domain_controllers"] = domain_controllers
        if organizational_unit is not None:
            self._values["organizational_unit"] = organizational_unit
        if timeout_in_seconds is not None:
            self._values["timeout_in_seconds"] = timeout_in_seconds

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#domain_name StoragegatewayGateway#domain_name}.'''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def password(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#password StoragegatewayGateway#password}.'''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def username(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#username StoragegatewayGateway#username}.'''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def domain_controllers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#domain_controllers StoragegatewayGateway#domain_controllers}.'''
        result = self._values.get("domain_controllers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def organizational_unit(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#organizational_unit StoragegatewayGateway#organizational_unit}.'''
        result = self._values.get("organizational_unit")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeout_in_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#timeout_in_seconds StoragegatewayGateway#timeout_in_seconds}.'''
        result = self._values.get("timeout_in_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StoragegatewayGatewaySmbActiveDirectorySettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StoragegatewayGatewaySmbActiveDirectorySettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.storagegatewayGateway.StoragegatewayGatewaySmbActiveDirectorySettingsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5d0584593a2fcf1cebc1743d27121feea3171d784b4fa868c5cfe5a73437af8d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDomainControllers")
    def reset_domain_controllers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDomainControllers", []))

    @jsii.member(jsii_name="resetOrganizationalUnit")
    def reset_organizational_unit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOrganizationalUnit", []))

    @jsii.member(jsii_name="resetTimeoutInSeconds")
    def reset_timeout_in_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeoutInSeconds", []))

    @builtins.property
    @jsii.member(jsii_name="activeDirectoryStatus")
    def active_directory_status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "activeDirectoryStatus"))

    @builtins.property
    @jsii.member(jsii_name="domainControllersInput")
    def domain_controllers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "domainControllersInput"))

    @builtins.property
    @jsii.member(jsii_name="domainNameInput")
    def domain_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainNameInput"))

    @builtins.property
    @jsii.member(jsii_name="organizationalUnitInput")
    def organizational_unit_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "organizationalUnitInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutInSecondsInput")
    def timeout_in_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "timeoutInSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="domainControllers")
    def domain_controllers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "domainControllers"))

    @domain_controllers.setter
    def domain_controllers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b52b3e6ac0f72b646ef347f77aa4c208f6d0f19788b45a31bc22da2868668a47)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainControllers", value)

    @builtins.property
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domainName"))

    @domain_name.setter
    def domain_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad819d96223ae13535175bcb9e244d989a2a58e481117d91323fc95df886fe6a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainName", value)

    @builtins.property
    @jsii.member(jsii_name="organizationalUnit")
    def organizational_unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "organizationalUnit"))

    @organizational_unit.setter
    def organizational_unit(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__305ff40425aa68c0c477be013b30c55318dc59a1f0e90f4fc734b93e089302a0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "organizationalUnit", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9fbdbf3a7bcb88593748474b283a0a2e3332972f837d034b6b73478506c0952)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="timeoutInSeconds")
    def timeout_in_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "timeoutInSeconds"))

    @timeout_in_seconds.setter
    def timeout_in_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e853d2a09a97f9ead5e8fca55a1853716dc69fa85f5a39d4a30f8ba94f759efe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeoutInSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cff35c64bb6acfb41b2c4aa2b8beddd61e389b281fe9df16142f492457250f58)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[StoragegatewayGatewaySmbActiveDirectorySettings]:
        return typing.cast(typing.Optional[StoragegatewayGatewaySmbActiveDirectorySettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[StoragegatewayGatewaySmbActiveDirectorySettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29d4997c48cd01759a478d967be8e46060e7f91384c8ffc991a011f67d364f06)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.storagegatewayGateway.StoragegatewayGatewayTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create"},
)
class StoragegatewayGatewayTimeouts:
    def __init__(self, *, create: typing.Optional[builtins.str] = None) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#create StoragegatewayGateway#create}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e134ef6a9f79e7da02b2ec7572e930786bea00a093cf9090ffffb4b2adc901bc)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#create StoragegatewayGateway#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StoragegatewayGatewayTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StoragegatewayGatewayTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.storagegatewayGateway.StoragegatewayGatewayTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9536a884f32f81495e3ff6cd6339346d244f35a1d0fe007c6c719dec53c1c60e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ebf085a2265da9ef3df98382c0e7d87d3416e497da8cf45c52db2fb31bb74245)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[StoragegatewayGatewayTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[StoragegatewayGatewayTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[StoragegatewayGatewayTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c854595d0117674f2023975663f6102a67988b52ba0b6f1949a6b667ef65db1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "StoragegatewayGateway",
    "StoragegatewayGatewayConfig",
    "StoragegatewayGatewayGatewayNetworkInterface",
    "StoragegatewayGatewayGatewayNetworkInterfaceList",
    "StoragegatewayGatewayGatewayNetworkInterfaceOutputReference",
    "StoragegatewayGatewayMaintenanceStartTime",
    "StoragegatewayGatewayMaintenanceStartTimeOutputReference",
    "StoragegatewayGatewaySmbActiveDirectorySettings",
    "StoragegatewayGatewaySmbActiveDirectorySettingsOutputReference",
    "StoragegatewayGatewayTimeouts",
    "StoragegatewayGatewayTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__a8b22476c0b0e0c29f1f81668590cb21bcc8f5f8cf21f529981dc91db97cb237(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    gateway_name: builtins.str,
    gateway_timezone: builtins.str,
    activation_key: typing.Optional[builtins.str] = None,
    average_download_rate_limit_in_bits_per_sec: typing.Optional[jsii.Number] = None,
    average_upload_rate_limit_in_bits_per_sec: typing.Optional[jsii.Number] = None,
    cloudwatch_log_group_arn: typing.Optional[builtins.str] = None,
    gateway_ip_address: typing.Optional[builtins.str] = None,
    gateway_type: typing.Optional[builtins.str] = None,
    gateway_vpc_endpoint: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    maintenance_start_time: typing.Optional[typing.Union[StoragegatewayGatewayMaintenanceStartTime, typing.Dict[builtins.str, typing.Any]]] = None,
    medium_changer_type: typing.Optional[builtins.str] = None,
    smb_active_directory_settings: typing.Optional[typing.Union[StoragegatewayGatewaySmbActiveDirectorySettings, typing.Dict[builtins.str, typing.Any]]] = None,
    smb_file_share_visibility: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    smb_guest_password: typing.Optional[builtins.str] = None,
    smb_security_strategy: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tape_drive_type: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[StoragegatewayGatewayTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__28f7fe0b669c8ea23b4e035ece6cf748eb741a797a12b12294b2329959b2854c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f19bf11fd3cf6f378bd60a7729b7645e16c5f7532b549e1bea40a2b68d27f605(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c680832afd4e5da176a1719b7aacd14c0dc3472388260880dae7454cf1edf6d3(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e661c0b81a9151cd5cb9ee8ac010cefafee9857394a49f049be8ee911724951(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19babfd143764e888da8090082f263c5838f75806afe628c535d0562c7566c89(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75b5e2fa2bcbfedd26c35f375534a8a670ac5a49430b97dcb030a033cccc2d05(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3975b19fe4989f688ef40b0e8a1be9d803b9b00755199b39eba3cef3e10ad3fb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__007816211d33d2a5cf92d8137e1291412f87d52dea2265129c5d992721f7d1a3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00bc7a409de11febdcc7d0e3c3746f34ff4b8ca467ee1f313c5c7a2f7607729b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95b677e90132c063fb483a24a0fac2733800092a6497c66a0f61e75b9cc8500e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5058a964bf987f642980679084aa2236addf90d49f8d2f5c4226691a3bc06453(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f786ae2607a6338d0e4a91b04693f2b311e77e063f66cf365999d93221971f5b(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5a598d2d8f39ffab318fb9d35e0d88227067b7eed902ba264d938d61f163d32(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f28a91dbefa188bdcb4765a4602c85d59c14f4efe0f853f003805f661a9e6aff(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8ffd3b0f8fb239cfaacbc71f9ecbae7f88c036b82159e11ae030b49dea61aea(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11b78697db52078737162fc0d7ef0f23c3e800321214d3cbf83f2ed4925218c2(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42b8be1ca0fe4aad07c3001aad32bf9517177719bbab6e5dded39d7c8dc9b078(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3e014d7c1008dcb433ce3d6d2e2bab7fc4274485f28299ed99de67f2ec18c5a(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    gateway_name: builtins.str,
    gateway_timezone: builtins.str,
    activation_key: typing.Optional[builtins.str] = None,
    average_download_rate_limit_in_bits_per_sec: typing.Optional[jsii.Number] = None,
    average_upload_rate_limit_in_bits_per_sec: typing.Optional[jsii.Number] = None,
    cloudwatch_log_group_arn: typing.Optional[builtins.str] = None,
    gateway_ip_address: typing.Optional[builtins.str] = None,
    gateway_type: typing.Optional[builtins.str] = None,
    gateway_vpc_endpoint: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    maintenance_start_time: typing.Optional[typing.Union[StoragegatewayGatewayMaintenanceStartTime, typing.Dict[builtins.str, typing.Any]]] = None,
    medium_changer_type: typing.Optional[builtins.str] = None,
    smb_active_directory_settings: typing.Optional[typing.Union[StoragegatewayGatewaySmbActiveDirectorySettings, typing.Dict[builtins.str, typing.Any]]] = None,
    smb_file_share_visibility: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    smb_guest_password: typing.Optional[builtins.str] = None,
    smb_security_strategy: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tape_drive_type: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[StoragegatewayGatewayTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e846f64a242223456a05d0d963d1a8693648fb8f63440b2c56153eb3f5b434a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f465108711e0ad203dc61e2db588f3eb9cd6cac5e54a5c7d4bab810138e3aaaf(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__426255a50c2752366f8b30abc7ad668d83ce20a4236208d69475b62116cc2972(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52e97c85a3cbd9cfa1bb8d97980b8053f6b86ae5370773323b6e9db4c8de659c(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__888d0b41b2d1783247bb35d7a58d560a4d77556baf3e2dc4ca3925ff247e6f10(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9f86ad9299503b3fd2129172424081d1d445c7b75939f39a2843fba5f49804c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8326968b3b5ad2fd914d5d62a634af4891f6e684f126bb8b589540c81d7a3d6(
    value: typing.Optional[StoragegatewayGatewayGatewayNetworkInterface],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29e5e393e285a96638c50a477c06cba92e54624156fa02f60ee859a90450727c(
    *,
    hour_of_day: jsii.Number,
    day_of_month: typing.Optional[builtins.str] = None,
    day_of_week: typing.Optional[builtins.str] = None,
    minute_of_hour: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9be326a7bb0527df9bf51eccf0c7062fd4072dbcf9df048cccc7bcce28f6a0c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c45a697eec8b0d9a5c483ba386c68ebc15c4a0918d11065e3104c4a85c47cd3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4b1466b428eeef81e3ec1d2e638c99246f0df2d4e89e1b6f92e2e13a960597e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26e33a4eba34068cdcb4c6c7c60a7f7dc8d222027728c8e09c53f115c7825319(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b14946cdc0cc32eaaee24b1d20576cc3965970e90676335e7964a0df521f774a(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0ee955de035985e0a2d828c5aa7cc76957c280ffffbae43364ac567ac7396b4(
    value: typing.Optional[StoragegatewayGatewayMaintenanceStartTime],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd8ea3df43c10149dbf6d2017772614cb58a1abcaea82faba6ef00fa2cc73687(
    *,
    domain_name: builtins.str,
    password: builtins.str,
    username: builtins.str,
    domain_controllers: typing.Optional[typing.Sequence[builtins.str]] = None,
    organizational_unit: typing.Optional[builtins.str] = None,
    timeout_in_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d0584593a2fcf1cebc1743d27121feea3171d784b4fa868c5cfe5a73437af8d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b52b3e6ac0f72b646ef347f77aa4c208f6d0f19788b45a31bc22da2868668a47(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad819d96223ae13535175bcb9e244d989a2a58e481117d91323fc95df886fe6a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__305ff40425aa68c0c477be013b30c55318dc59a1f0e90f4fc734b93e089302a0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9fbdbf3a7bcb88593748474b283a0a2e3332972f837d034b6b73478506c0952(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e853d2a09a97f9ead5e8fca55a1853716dc69fa85f5a39d4a30f8ba94f759efe(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cff35c64bb6acfb41b2c4aa2b8beddd61e389b281fe9df16142f492457250f58(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29d4997c48cd01759a478d967be8e46060e7f91384c8ffc991a011f67d364f06(
    value: typing.Optional[StoragegatewayGatewaySmbActiveDirectorySettings],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e134ef6a9f79e7da02b2ec7572e930786bea00a093cf9090ffffb4b2adc901bc(
    *,
    create: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9536a884f32f81495e3ff6cd6339346d244f35a1d0fe007c6c719dec53c1c60e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ebf085a2265da9ef3df98382c0e7d87d3416e497da8cf45c52db2fb31bb74245(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c854595d0117674f2023975663f6102a67988b52ba0b6f1949a6b667ef65db1(
    value: typing.Optional[typing.Union[StoragegatewayGatewayTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
