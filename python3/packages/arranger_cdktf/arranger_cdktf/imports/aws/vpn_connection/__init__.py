'''
# `aws_vpn_connection`

Refer to the Terraform Registory for docs: [`aws_vpn_connection`](https://www.terraform.io/docs/providers/aws/r/vpn_connection).
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


class VpnConnection(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.vpnConnection.VpnConnection",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection aws_vpn_connection}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        customer_gateway_id: builtins.str,
        type: builtins.str,
        enable_acceleration: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        local_ipv4_network_cidr: typing.Optional[builtins.str] = None,
        local_ipv6_network_cidr: typing.Optional[builtins.str] = None,
        outside_ip_address_type: typing.Optional[builtins.str] = None,
        remote_ipv4_network_cidr: typing.Optional[builtins.str] = None,
        remote_ipv6_network_cidr: typing.Optional[builtins.str] = None,
        static_routes_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        transit_gateway_id: typing.Optional[builtins.str] = None,
        transport_transit_gateway_attachment_id: typing.Optional[builtins.str] = None,
        tunnel1_dpd_timeout_action: typing.Optional[builtins.str] = None,
        tunnel1_dpd_timeout_seconds: typing.Optional[jsii.Number] = None,
        tunnel1_ike_versions: typing.Optional[typing.Sequence[builtins.str]] = None,
        tunnel1_inside_cidr: typing.Optional[builtins.str] = None,
        tunnel1_inside_ipv6_cidr: typing.Optional[builtins.str] = None,
        tunnel1_log_options: typing.Optional[typing.Union["VpnConnectionTunnel1LogOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        tunnel1_phase1_dh_group_numbers: typing.Optional[typing.Sequence[jsii.Number]] = None,
        tunnel1_phase1_encryption_algorithms: typing.Optional[typing.Sequence[builtins.str]] = None,
        tunnel1_phase1_integrity_algorithms: typing.Optional[typing.Sequence[builtins.str]] = None,
        tunnel1_phase1_lifetime_seconds: typing.Optional[jsii.Number] = None,
        tunnel1_phase2_dh_group_numbers: typing.Optional[typing.Sequence[jsii.Number]] = None,
        tunnel1_phase2_encryption_algorithms: typing.Optional[typing.Sequence[builtins.str]] = None,
        tunnel1_phase2_integrity_algorithms: typing.Optional[typing.Sequence[builtins.str]] = None,
        tunnel1_phase2_lifetime_seconds: typing.Optional[jsii.Number] = None,
        tunnel1_preshared_key: typing.Optional[builtins.str] = None,
        tunnel1_rekey_fuzz_percentage: typing.Optional[jsii.Number] = None,
        tunnel1_rekey_margin_time_seconds: typing.Optional[jsii.Number] = None,
        tunnel1_replay_window_size: typing.Optional[jsii.Number] = None,
        tunnel1_startup_action: typing.Optional[builtins.str] = None,
        tunnel2_dpd_timeout_action: typing.Optional[builtins.str] = None,
        tunnel2_dpd_timeout_seconds: typing.Optional[jsii.Number] = None,
        tunnel2_ike_versions: typing.Optional[typing.Sequence[builtins.str]] = None,
        tunnel2_inside_cidr: typing.Optional[builtins.str] = None,
        tunnel2_inside_ipv6_cidr: typing.Optional[builtins.str] = None,
        tunnel2_log_options: typing.Optional[typing.Union["VpnConnectionTunnel2LogOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        tunnel2_phase1_dh_group_numbers: typing.Optional[typing.Sequence[jsii.Number]] = None,
        tunnel2_phase1_encryption_algorithms: typing.Optional[typing.Sequence[builtins.str]] = None,
        tunnel2_phase1_integrity_algorithms: typing.Optional[typing.Sequence[builtins.str]] = None,
        tunnel2_phase1_lifetime_seconds: typing.Optional[jsii.Number] = None,
        tunnel2_phase2_dh_group_numbers: typing.Optional[typing.Sequence[jsii.Number]] = None,
        tunnel2_phase2_encryption_algorithms: typing.Optional[typing.Sequence[builtins.str]] = None,
        tunnel2_phase2_integrity_algorithms: typing.Optional[typing.Sequence[builtins.str]] = None,
        tunnel2_phase2_lifetime_seconds: typing.Optional[jsii.Number] = None,
        tunnel2_preshared_key: typing.Optional[builtins.str] = None,
        tunnel2_rekey_fuzz_percentage: typing.Optional[jsii.Number] = None,
        tunnel2_rekey_margin_time_seconds: typing.Optional[jsii.Number] = None,
        tunnel2_replay_window_size: typing.Optional[jsii.Number] = None,
        tunnel2_startup_action: typing.Optional[builtins.str] = None,
        tunnel_inside_ip_version: typing.Optional[builtins.str] = None,
        vpn_gateway_id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection aws_vpn_connection} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param customer_gateway_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#customer_gateway_id VpnConnection#customer_gateway_id}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#type VpnConnection#type}.
        :param enable_acceleration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#enable_acceleration VpnConnection#enable_acceleration}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#id VpnConnection#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param local_ipv4_network_cidr: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#local_ipv4_network_cidr VpnConnection#local_ipv4_network_cidr}.
        :param local_ipv6_network_cidr: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#local_ipv6_network_cidr VpnConnection#local_ipv6_network_cidr}.
        :param outside_ip_address_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#outside_ip_address_type VpnConnection#outside_ip_address_type}.
        :param remote_ipv4_network_cidr: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#remote_ipv4_network_cidr VpnConnection#remote_ipv4_network_cidr}.
        :param remote_ipv6_network_cidr: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#remote_ipv6_network_cidr VpnConnection#remote_ipv6_network_cidr}.
        :param static_routes_only: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#static_routes_only VpnConnection#static_routes_only}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tags VpnConnection#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tags_all VpnConnection#tags_all}.
        :param transit_gateway_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#transit_gateway_id VpnConnection#transit_gateway_id}.
        :param transport_transit_gateway_attachment_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#transport_transit_gateway_attachment_id VpnConnection#transport_transit_gateway_attachment_id}.
        :param tunnel1_dpd_timeout_action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_dpd_timeout_action VpnConnection#tunnel1_dpd_timeout_action}.
        :param tunnel1_dpd_timeout_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_dpd_timeout_seconds VpnConnection#tunnel1_dpd_timeout_seconds}.
        :param tunnel1_ike_versions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_ike_versions VpnConnection#tunnel1_ike_versions}.
        :param tunnel1_inside_cidr: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_inside_cidr VpnConnection#tunnel1_inside_cidr}.
        :param tunnel1_inside_ipv6_cidr: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_inside_ipv6_cidr VpnConnection#tunnel1_inside_ipv6_cidr}.
        :param tunnel1_log_options: tunnel1_log_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_log_options VpnConnection#tunnel1_log_options}
        :param tunnel1_phase1_dh_group_numbers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_phase1_dh_group_numbers VpnConnection#tunnel1_phase1_dh_group_numbers}.
        :param tunnel1_phase1_encryption_algorithms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_phase1_encryption_algorithms VpnConnection#tunnel1_phase1_encryption_algorithms}.
        :param tunnel1_phase1_integrity_algorithms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_phase1_integrity_algorithms VpnConnection#tunnel1_phase1_integrity_algorithms}.
        :param tunnel1_phase1_lifetime_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_phase1_lifetime_seconds VpnConnection#tunnel1_phase1_lifetime_seconds}.
        :param tunnel1_phase2_dh_group_numbers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_phase2_dh_group_numbers VpnConnection#tunnel1_phase2_dh_group_numbers}.
        :param tunnel1_phase2_encryption_algorithms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_phase2_encryption_algorithms VpnConnection#tunnel1_phase2_encryption_algorithms}.
        :param tunnel1_phase2_integrity_algorithms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_phase2_integrity_algorithms VpnConnection#tunnel1_phase2_integrity_algorithms}.
        :param tunnel1_phase2_lifetime_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_phase2_lifetime_seconds VpnConnection#tunnel1_phase2_lifetime_seconds}.
        :param tunnel1_preshared_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_preshared_key VpnConnection#tunnel1_preshared_key}.
        :param tunnel1_rekey_fuzz_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_rekey_fuzz_percentage VpnConnection#tunnel1_rekey_fuzz_percentage}.
        :param tunnel1_rekey_margin_time_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_rekey_margin_time_seconds VpnConnection#tunnel1_rekey_margin_time_seconds}.
        :param tunnel1_replay_window_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_replay_window_size VpnConnection#tunnel1_replay_window_size}.
        :param tunnel1_startup_action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_startup_action VpnConnection#tunnel1_startup_action}.
        :param tunnel2_dpd_timeout_action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_dpd_timeout_action VpnConnection#tunnel2_dpd_timeout_action}.
        :param tunnel2_dpd_timeout_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_dpd_timeout_seconds VpnConnection#tunnel2_dpd_timeout_seconds}.
        :param tunnel2_ike_versions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_ike_versions VpnConnection#tunnel2_ike_versions}.
        :param tunnel2_inside_cidr: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_inside_cidr VpnConnection#tunnel2_inside_cidr}.
        :param tunnel2_inside_ipv6_cidr: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_inside_ipv6_cidr VpnConnection#tunnel2_inside_ipv6_cidr}.
        :param tunnel2_log_options: tunnel2_log_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_log_options VpnConnection#tunnel2_log_options}
        :param tunnel2_phase1_dh_group_numbers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_phase1_dh_group_numbers VpnConnection#tunnel2_phase1_dh_group_numbers}.
        :param tunnel2_phase1_encryption_algorithms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_phase1_encryption_algorithms VpnConnection#tunnel2_phase1_encryption_algorithms}.
        :param tunnel2_phase1_integrity_algorithms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_phase1_integrity_algorithms VpnConnection#tunnel2_phase1_integrity_algorithms}.
        :param tunnel2_phase1_lifetime_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_phase1_lifetime_seconds VpnConnection#tunnel2_phase1_lifetime_seconds}.
        :param tunnel2_phase2_dh_group_numbers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_phase2_dh_group_numbers VpnConnection#tunnel2_phase2_dh_group_numbers}.
        :param tunnel2_phase2_encryption_algorithms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_phase2_encryption_algorithms VpnConnection#tunnel2_phase2_encryption_algorithms}.
        :param tunnel2_phase2_integrity_algorithms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_phase2_integrity_algorithms VpnConnection#tunnel2_phase2_integrity_algorithms}.
        :param tunnel2_phase2_lifetime_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_phase2_lifetime_seconds VpnConnection#tunnel2_phase2_lifetime_seconds}.
        :param tunnel2_preshared_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_preshared_key VpnConnection#tunnel2_preshared_key}.
        :param tunnel2_rekey_fuzz_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_rekey_fuzz_percentage VpnConnection#tunnel2_rekey_fuzz_percentage}.
        :param tunnel2_rekey_margin_time_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_rekey_margin_time_seconds VpnConnection#tunnel2_rekey_margin_time_seconds}.
        :param tunnel2_replay_window_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_replay_window_size VpnConnection#tunnel2_replay_window_size}.
        :param tunnel2_startup_action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_startup_action VpnConnection#tunnel2_startup_action}.
        :param tunnel_inside_ip_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel_inside_ip_version VpnConnection#tunnel_inside_ip_version}.
        :param vpn_gateway_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#vpn_gateway_id VpnConnection#vpn_gateway_id}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7be62f7a12ef9cca95b6db621ab4092170cd6ada5fa01e8aa445cc07c7ef2e36)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = VpnConnectionConfig(
            customer_gateway_id=customer_gateway_id,
            type=type,
            enable_acceleration=enable_acceleration,
            id=id,
            local_ipv4_network_cidr=local_ipv4_network_cidr,
            local_ipv6_network_cidr=local_ipv6_network_cidr,
            outside_ip_address_type=outside_ip_address_type,
            remote_ipv4_network_cidr=remote_ipv4_network_cidr,
            remote_ipv6_network_cidr=remote_ipv6_network_cidr,
            static_routes_only=static_routes_only,
            tags=tags,
            tags_all=tags_all,
            transit_gateway_id=transit_gateway_id,
            transport_transit_gateway_attachment_id=transport_transit_gateway_attachment_id,
            tunnel1_dpd_timeout_action=tunnel1_dpd_timeout_action,
            tunnel1_dpd_timeout_seconds=tunnel1_dpd_timeout_seconds,
            tunnel1_ike_versions=tunnel1_ike_versions,
            tunnel1_inside_cidr=tunnel1_inside_cidr,
            tunnel1_inside_ipv6_cidr=tunnel1_inside_ipv6_cidr,
            tunnel1_log_options=tunnel1_log_options,
            tunnel1_phase1_dh_group_numbers=tunnel1_phase1_dh_group_numbers,
            tunnel1_phase1_encryption_algorithms=tunnel1_phase1_encryption_algorithms,
            tunnel1_phase1_integrity_algorithms=tunnel1_phase1_integrity_algorithms,
            tunnel1_phase1_lifetime_seconds=tunnel1_phase1_lifetime_seconds,
            tunnel1_phase2_dh_group_numbers=tunnel1_phase2_dh_group_numbers,
            tunnel1_phase2_encryption_algorithms=tunnel1_phase2_encryption_algorithms,
            tunnel1_phase2_integrity_algorithms=tunnel1_phase2_integrity_algorithms,
            tunnel1_phase2_lifetime_seconds=tunnel1_phase2_lifetime_seconds,
            tunnel1_preshared_key=tunnel1_preshared_key,
            tunnel1_rekey_fuzz_percentage=tunnel1_rekey_fuzz_percentage,
            tunnel1_rekey_margin_time_seconds=tunnel1_rekey_margin_time_seconds,
            tunnel1_replay_window_size=tunnel1_replay_window_size,
            tunnel1_startup_action=tunnel1_startup_action,
            tunnel2_dpd_timeout_action=tunnel2_dpd_timeout_action,
            tunnel2_dpd_timeout_seconds=tunnel2_dpd_timeout_seconds,
            tunnel2_ike_versions=tunnel2_ike_versions,
            tunnel2_inside_cidr=tunnel2_inside_cidr,
            tunnel2_inside_ipv6_cidr=tunnel2_inside_ipv6_cidr,
            tunnel2_log_options=tunnel2_log_options,
            tunnel2_phase1_dh_group_numbers=tunnel2_phase1_dh_group_numbers,
            tunnel2_phase1_encryption_algorithms=tunnel2_phase1_encryption_algorithms,
            tunnel2_phase1_integrity_algorithms=tunnel2_phase1_integrity_algorithms,
            tunnel2_phase1_lifetime_seconds=tunnel2_phase1_lifetime_seconds,
            tunnel2_phase2_dh_group_numbers=tunnel2_phase2_dh_group_numbers,
            tunnel2_phase2_encryption_algorithms=tunnel2_phase2_encryption_algorithms,
            tunnel2_phase2_integrity_algorithms=tunnel2_phase2_integrity_algorithms,
            tunnel2_phase2_lifetime_seconds=tunnel2_phase2_lifetime_seconds,
            tunnel2_preshared_key=tunnel2_preshared_key,
            tunnel2_rekey_fuzz_percentage=tunnel2_rekey_fuzz_percentage,
            tunnel2_rekey_margin_time_seconds=tunnel2_rekey_margin_time_seconds,
            tunnel2_replay_window_size=tunnel2_replay_window_size,
            tunnel2_startup_action=tunnel2_startup_action,
            tunnel_inside_ip_version=tunnel_inside_ip_version,
            vpn_gateway_id=vpn_gateway_id,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putTunnel1LogOptions")
    def put_tunnel1_log_options(
        self,
        *,
        cloudwatch_log_options: typing.Optional[typing.Union["VpnConnectionTunnel1LogOptionsCloudwatchLogOptions", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param cloudwatch_log_options: cloudwatch_log_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#cloudwatch_log_options VpnConnection#cloudwatch_log_options}
        '''
        value = VpnConnectionTunnel1LogOptions(
            cloudwatch_log_options=cloudwatch_log_options
        )

        return typing.cast(None, jsii.invoke(self, "putTunnel1LogOptions", [value]))

    @jsii.member(jsii_name="putTunnel2LogOptions")
    def put_tunnel2_log_options(
        self,
        *,
        cloudwatch_log_options: typing.Optional[typing.Union["VpnConnectionTunnel2LogOptionsCloudwatchLogOptions", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param cloudwatch_log_options: cloudwatch_log_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#cloudwatch_log_options VpnConnection#cloudwatch_log_options}
        '''
        value = VpnConnectionTunnel2LogOptions(
            cloudwatch_log_options=cloudwatch_log_options
        )

        return typing.cast(None, jsii.invoke(self, "putTunnel2LogOptions", [value]))

    @jsii.member(jsii_name="resetEnableAcceleration")
    def reset_enable_acceleration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableAcceleration", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLocalIpv4NetworkCidr")
    def reset_local_ipv4_network_cidr(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocalIpv4NetworkCidr", []))

    @jsii.member(jsii_name="resetLocalIpv6NetworkCidr")
    def reset_local_ipv6_network_cidr(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocalIpv6NetworkCidr", []))

    @jsii.member(jsii_name="resetOutsideIpAddressType")
    def reset_outside_ip_address_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOutsideIpAddressType", []))

    @jsii.member(jsii_name="resetRemoteIpv4NetworkCidr")
    def reset_remote_ipv4_network_cidr(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRemoteIpv4NetworkCidr", []))

    @jsii.member(jsii_name="resetRemoteIpv6NetworkCidr")
    def reset_remote_ipv6_network_cidr(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRemoteIpv6NetworkCidr", []))

    @jsii.member(jsii_name="resetStaticRoutesOnly")
    def reset_static_routes_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStaticRoutesOnly", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetTransitGatewayId")
    def reset_transit_gateway_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTransitGatewayId", []))

    @jsii.member(jsii_name="resetTransportTransitGatewayAttachmentId")
    def reset_transport_transit_gateway_attachment_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTransportTransitGatewayAttachmentId", []))

    @jsii.member(jsii_name="resetTunnel1DpdTimeoutAction")
    def reset_tunnel1_dpd_timeout_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnel1DpdTimeoutAction", []))

    @jsii.member(jsii_name="resetTunnel1DpdTimeoutSeconds")
    def reset_tunnel1_dpd_timeout_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnel1DpdTimeoutSeconds", []))

    @jsii.member(jsii_name="resetTunnel1IkeVersions")
    def reset_tunnel1_ike_versions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnel1IkeVersions", []))

    @jsii.member(jsii_name="resetTunnel1InsideCidr")
    def reset_tunnel1_inside_cidr(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnel1InsideCidr", []))

    @jsii.member(jsii_name="resetTunnel1InsideIpv6Cidr")
    def reset_tunnel1_inside_ipv6_cidr(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnel1InsideIpv6Cidr", []))

    @jsii.member(jsii_name="resetTunnel1LogOptions")
    def reset_tunnel1_log_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnel1LogOptions", []))

    @jsii.member(jsii_name="resetTunnel1Phase1DhGroupNumbers")
    def reset_tunnel1_phase1_dh_group_numbers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnel1Phase1DhGroupNumbers", []))

    @jsii.member(jsii_name="resetTunnel1Phase1EncryptionAlgorithms")
    def reset_tunnel1_phase1_encryption_algorithms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnel1Phase1EncryptionAlgorithms", []))

    @jsii.member(jsii_name="resetTunnel1Phase1IntegrityAlgorithms")
    def reset_tunnel1_phase1_integrity_algorithms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnel1Phase1IntegrityAlgorithms", []))

    @jsii.member(jsii_name="resetTunnel1Phase1LifetimeSeconds")
    def reset_tunnel1_phase1_lifetime_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnel1Phase1LifetimeSeconds", []))

    @jsii.member(jsii_name="resetTunnel1Phase2DhGroupNumbers")
    def reset_tunnel1_phase2_dh_group_numbers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnel1Phase2DhGroupNumbers", []))

    @jsii.member(jsii_name="resetTunnel1Phase2EncryptionAlgorithms")
    def reset_tunnel1_phase2_encryption_algorithms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnel1Phase2EncryptionAlgorithms", []))

    @jsii.member(jsii_name="resetTunnel1Phase2IntegrityAlgorithms")
    def reset_tunnel1_phase2_integrity_algorithms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnel1Phase2IntegrityAlgorithms", []))

    @jsii.member(jsii_name="resetTunnel1Phase2LifetimeSeconds")
    def reset_tunnel1_phase2_lifetime_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnel1Phase2LifetimeSeconds", []))

    @jsii.member(jsii_name="resetTunnel1PresharedKey")
    def reset_tunnel1_preshared_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnel1PresharedKey", []))

    @jsii.member(jsii_name="resetTunnel1RekeyFuzzPercentage")
    def reset_tunnel1_rekey_fuzz_percentage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnel1RekeyFuzzPercentage", []))

    @jsii.member(jsii_name="resetTunnel1RekeyMarginTimeSeconds")
    def reset_tunnel1_rekey_margin_time_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnel1RekeyMarginTimeSeconds", []))

    @jsii.member(jsii_name="resetTunnel1ReplayWindowSize")
    def reset_tunnel1_replay_window_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnel1ReplayWindowSize", []))

    @jsii.member(jsii_name="resetTunnel1StartupAction")
    def reset_tunnel1_startup_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnel1StartupAction", []))

    @jsii.member(jsii_name="resetTunnel2DpdTimeoutAction")
    def reset_tunnel2_dpd_timeout_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnel2DpdTimeoutAction", []))

    @jsii.member(jsii_name="resetTunnel2DpdTimeoutSeconds")
    def reset_tunnel2_dpd_timeout_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnel2DpdTimeoutSeconds", []))

    @jsii.member(jsii_name="resetTunnel2IkeVersions")
    def reset_tunnel2_ike_versions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnel2IkeVersions", []))

    @jsii.member(jsii_name="resetTunnel2InsideCidr")
    def reset_tunnel2_inside_cidr(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnel2InsideCidr", []))

    @jsii.member(jsii_name="resetTunnel2InsideIpv6Cidr")
    def reset_tunnel2_inside_ipv6_cidr(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnel2InsideIpv6Cidr", []))

    @jsii.member(jsii_name="resetTunnel2LogOptions")
    def reset_tunnel2_log_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnel2LogOptions", []))

    @jsii.member(jsii_name="resetTunnel2Phase1DhGroupNumbers")
    def reset_tunnel2_phase1_dh_group_numbers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnel2Phase1DhGroupNumbers", []))

    @jsii.member(jsii_name="resetTunnel2Phase1EncryptionAlgorithms")
    def reset_tunnel2_phase1_encryption_algorithms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnel2Phase1EncryptionAlgorithms", []))

    @jsii.member(jsii_name="resetTunnel2Phase1IntegrityAlgorithms")
    def reset_tunnel2_phase1_integrity_algorithms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnel2Phase1IntegrityAlgorithms", []))

    @jsii.member(jsii_name="resetTunnel2Phase1LifetimeSeconds")
    def reset_tunnel2_phase1_lifetime_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnel2Phase1LifetimeSeconds", []))

    @jsii.member(jsii_name="resetTunnel2Phase2DhGroupNumbers")
    def reset_tunnel2_phase2_dh_group_numbers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnel2Phase2DhGroupNumbers", []))

    @jsii.member(jsii_name="resetTunnel2Phase2EncryptionAlgorithms")
    def reset_tunnel2_phase2_encryption_algorithms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnel2Phase2EncryptionAlgorithms", []))

    @jsii.member(jsii_name="resetTunnel2Phase2IntegrityAlgorithms")
    def reset_tunnel2_phase2_integrity_algorithms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnel2Phase2IntegrityAlgorithms", []))

    @jsii.member(jsii_name="resetTunnel2Phase2LifetimeSeconds")
    def reset_tunnel2_phase2_lifetime_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnel2Phase2LifetimeSeconds", []))

    @jsii.member(jsii_name="resetTunnel2PresharedKey")
    def reset_tunnel2_preshared_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnel2PresharedKey", []))

    @jsii.member(jsii_name="resetTunnel2RekeyFuzzPercentage")
    def reset_tunnel2_rekey_fuzz_percentage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnel2RekeyFuzzPercentage", []))

    @jsii.member(jsii_name="resetTunnel2RekeyMarginTimeSeconds")
    def reset_tunnel2_rekey_margin_time_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnel2RekeyMarginTimeSeconds", []))

    @jsii.member(jsii_name="resetTunnel2ReplayWindowSize")
    def reset_tunnel2_replay_window_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnel2ReplayWindowSize", []))

    @jsii.member(jsii_name="resetTunnel2StartupAction")
    def reset_tunnel2_startup_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnel2StartupAction", []))

    @jsii.member(jsii_name="resetTunnelInsideIpVersion")
    def reset_tunnel_inside_ip_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnelInsideIpVersion", []))

    @jsii.member(jsii_name="resetVpnGatewayId")
    def reset_vpn_gateway_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVpnGatewayId", []))

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
    @jsii.member(jsii_name="coreNetworkArn")
    def core_network_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "coreNetworkArn"))

    @builtins.property
    @jsii.member(jsii_name="coreNetworkAttachmentArn")
    def core_network_attachment_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "coreNetworkAttachmentArn"))

    @builtins.property
    @jsii.member(jsii_name="customerGatewayConfiguration")
    def customer_gateway_configuration(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customerGatewayConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="routes")
    def routes(self) -> "VpnConnectionRoutesList":
        return typing.cast("VpnConnectionRoutesList", jsii.get(self, "routes"))

    @builtins.property
    @jsii.member(jsii_name="transitGatewayAttachmentId")
    def transit_gateway_attachment_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "transitGatewayAttachmentId"))

    @builtins.property
    @jsii.member(jsii_name="tunnel1Address")
    def tunnel1_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tunnel1Address"))

    @builtins.property
    @jsii.member(jsii_name="tunnel1BgpAsn")
    def tunnel1_bgp_asn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tunnel1BgpAsn"))

    @builtins.property
    @jsii.member(jsii_name="tunnel1BgpHoldtime")
    def tunnel1_bgp_holdtime(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "tunnel1BgpHoldtime"))

    @builtins.property
    @jsii.member(jsii_name="tunnel1CgwInsideAddress")
    def tunnel1_cgw_inside_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tunnel1CgwInsideAddress"))

    @builtins.property
    @jsii.member(jsii_name="tunnel1LogOptions")
    def tunnel1_log_options(self) -> "VpnConnectionTunnel1LogOptionsOutputReference":
        return typing.cast("VpnConnectionTunnel1LogOptionsOutputReference", jsii.get(self, "tunnel1LogOptions"))

    @builtins.property
    @jsii.member(jsii_name="tunnel1VgwInsideAddress")
    def tunnel1_vgw_inside_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tunnel1VgwInsideAddress"))

    @builtins.property
    @jsii.member(jsii_name="tunnel2Address")
    def tunnel2_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tunnel2Address"))

    @builtins.property
    @jsii.member(jsii_name="tunnel2BgpAsn")
    def tunnel2_bgp_asn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tunnel2BgpAsn"))

    @builtins.property
    @jsii.member(jsii_name="tunnel2BgpHoldtime")
    def tunnel2_bgp_holdtime(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "tunnel2BgpHoldtime"))

    @builtins.property
    @jsii.member(jsii_name="tunnel2CgwInsideAddress")
    def tunnel2_cgw_inside_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tunnel2CgwInsideAddress"))

    @builtins.property
    @jsii.member(jsii_name="tunnel2LogOptions")
    def tunnel2_log_options(self) -> "VpnConnectionTunnel2LogOptionsOutputReference":
        return typing.cast("VpnConnectionTunnel2LogOptionsOutputReference", jsii.get(self, "tunnel2LogOptions"))

    @builtins.property
    @jsii.member(jsii_name="tunnel2VgwInsideAddress")
    def tunnel2_vgw_inside_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tunnel2VgwInsideAddress"))

    @builtins.property
    @jsii.member(jsii_name="vgwTelemetry")
    def vgw_telemetry(self) -> "VpnConnectionVgwTelemetryList":
        return typing.cast("VpnConnectionVgwTelemetryList", jsii.get(self, "vgwTelemetry"))

    @builtins.property
    @jsii.member(jsii_name="customerGatewayIdInput")
    def customer_gateway_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customerGatewayIdInput"))

    @builtins.property
    @jsii.member(jsii_name="enableAccelerationInput")
    def enable_acceleration_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableAccelerationInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="localIpv4NetworkCidrInput")
    def local_ipv4_network_cidr_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "localIpv4NetworkCidrInput"))

    @builtins.property
    @jsii.member(jsii_name="localIpv6NetworkCidrInput")
    def local_ipv6_network_cidr_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "localIpv6NetworkCidrInput"))

    @builtins.property
    @jsii.member(jsii_name="outsideIpAddressTypeInput")
    def outside_ip_address_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "outsideIpAddressTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="remoteIpv4NetworkCidrInput")
    def remote_ipv4_network_cidr_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "remoteIpv4NetworkCidrInput"))

    @builtins.property
    @jsii.member(jsii_name="remoteIpv6NetworkCidrInput")
    def remote_ipv6_network_cidr_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "remoteIpv6NetworkCidrInput"))

    @builtins.property
    @jsii.member(jsii_name="staticRoutesOnlyInput")
    def static_routes_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "staticRoutesOnlyInput"))

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
    @jsii.member(jsii_name="transitGatewayIdInput")
    def transit_gateway_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "transitGatewayIdInput"))

    @builtins.property
    @jsii.member(jsii_name="transportTransitGatewayAttachmentIdInput")
    def transport_transit_gateway_attachment_id_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "transportTransitGatewayAttachmentIdInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnel1DpdTimeoutActionInput")
    def tunnel1_dpd_timeout_action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tunnel1DpdTimeoutActionInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnel1DpdTimeoutSecondsInput")
    def tunnel1_dpd_timeout_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "tunnel1DpdTimeoutSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnel1IkeVersionsInput")
    def tunnel1_ike_versions_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tunnel1IkeVersionsInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnel1InsideCidrInput")
    def tunnel1_inside_cidr_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tunnel1InsideCidrInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnel1InsideIpv6CidrInput")
    def tunnel1_inside_ipv6_cidr_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tunnel1InsideIpv6CidrInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnel1LogOptionsInput")
    def tunnel1_log_options_input(
        self,
    ) -> typing.Optional["VpnConnectionTunnel1LogOptions"]:
        return typing.cast(typing.Optional["VpnConnectionTunnel1LogOptions"], jsii.get(self, "tunnel1LogOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnel1Phase1DhGroupNumbersInput")
    def tunnel1_phase1_dh_group_numbers_input(
        self,
    ) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "tunnel1Phase1DhGroupNumbersInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnel1Phase1EncryptionAlgorithmsInput")
    def tunnel1_phase1_encryption_algorithms_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tunnel1Phase1EncryptionAlgorithmsInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnel1Phase1IntegrityAlgorithmsInput")
    def tunnel1_phase1_integrity_algorithms_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tunnel1Phase1IntegrityAlgorithmsInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnel1Phase1LifetimeSecondsInput")
    def tunnel1_phase1_lifetime_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "tunnel1Phase1LifetimeSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnel1Phase2DhGroupNumbersInput")
    def tunnel1_phase2_dh_group_numbers_input(
        self,
    ) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "tunnel1Phase2DhGroupNumbersInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnel1Phase2EncryptionAlgorithmsInput")
    def tunnel1_phase2_encryption_algorithms_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tunnel1Phase2EncryptionAlgorithmsInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnel1Phase2IntegrityAlgorithmsInput")
    def tunnel1_phase2_integrity_algorithms_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tunnel1Phase2IntegrityAlgorithmsInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnel1Phase2LifetimeSecondsInput")
    def tunnel1_phase2_lifetime_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "tunnel1Phase2LifetimeSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnel1PresharedKeyInput")
    def tunnel1_preshared_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tunnel1PresharedKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnel1RekeyFuzzPercentageInput")
    def tunnel1_rekey_fuzz_percentage_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "tunnel1RekeyFuzzPercentageInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnel1RekeyMarginTimeSecondsInput")
    def tunnel1_rekey_margin_time_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "tunnel1RekeyMarginTimeSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnel1ReplayWindowSizeInput")
    def tunnel1_replay_window_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "tunnel1ReplayWindowSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnel1StartupActionInput")
    def tunnel1_startup_action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tunnel1StartupActionInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnel2DpdTimeoutActionInput")
    def tunnel2_dpd_timeout_action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tunnel2DpdTimeoutActionInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnel2DpdTimeoutSecondsInput")
    def tunnel2_dpd_timeout_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "tunnel2DpdTimeoutSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnel2IkeVersionsInput")
    def tunnel2_ike_versions_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tunnel2IkeVersionsInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnel2InsideCidrInput")
    def tunnel2_inside_cidr_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tunnel2InsideCidrInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnel2InsideIpv6CidrInput")
    def tunnel2_inside_ipv6_cidr_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tunnel2InsideIpv6CidrInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnel2LogOptionsInput")
    def tunnel2_log_options_input(
        self,
    ) -> typing.Optional["VpnConnectionTunnel2LogOptions"]:
        return typing.cast(typing.Optional["VpnConnectionTunnel2LogOptions"], jsii.get(self, "tunnel2LogOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnel2Phase1DhGroupNumbersInput")
    def tunnel2_phase1_dh_group_numbers_input(
        self,
    ) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "tunnel2Phase1DhGroupNumbersInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnel2Phase1EncryptionAlgorithmsInput")
    def tunnel2_phase1_encryption_algorithms_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tunnel2Phase1EncryptionAlgorithmsInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnel2Phase1IntegrityAlgorithmsInput")
    def tunnel2_phase1_integrity_algorithms_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tunnel2Phase1IntegrityAlgorithmsInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnel2Phase1LifetimeSecondsInput")
    def tunnel2_phase1_lifetime_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "tunnel2Phase1LifetimeSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnel2Phase2DhGroupNumbersInput")
    def tunnel2_phase2_dh_group_numbers_input(
        self,
    ) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "tunnel2Phase2DhGroupNumbersInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnel2Phase2EncryptionAlgorithmsInput")
    def tunnel2_phase2_encryption_algorithms_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tunnel2Phase2EncryptionAlgorithmsInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnel2Phase2IntegrityAlgorithmsInput")
    def tunnel2_phase2_integrity_algorithms_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tunnel2Phase2IntegrityAlgorithmsInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnel2Phase2LifetimeSecondsInput")
    def tunnel2_phase2_lifetime_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "tunnel2Phase2LifetimeSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnel2PresharedKeyInput")
    def tunnel2_preshared_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tunnel2PresharedKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnel2RekeyFuzzPercentageInput")
    def tunnel2_rekey_fuzz_percentage_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "tunnel2RekeyFuzzPercentageInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnel2RekeyMarginTimeSecondsInput")
    def tunnel2_rekey_margin_time_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "tunnel2RekeyMarginTimeSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnel2ReplayWindowSizeInput")
    def tunnel2_replay_window_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "tunnel2ReplayWindowSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnel2StartupActionInput")
    def tunnel2_startup_action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tunnel2StartupActionInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnelInsideIpVersionInput")
    def tunnel_inside_ip_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tunnelInsideIpVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="vpnGatewayIdInput")
    def vpn_gateway_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vpnGatewayIdInput"))

    @builtins.property
    @jsii.member(jsii_name="customerGatewayId")
    def customer_gateway_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customerGatewayId"))

    @customer_gateway_id.setter
    def customer_gateway_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6bfd1511e4b29f207a98220d44aacd3d26da23db8f17538231b149d91ff6033)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customerGatewayId", value)

    @builtins.property
    @jsii.member(jsii_name="enableAcceleration")
    def enable_acceleration(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enableAcceleration"))

    @enable_acceleration.setter
    def enable_acceleration(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9127334e429ef407ddbe02246a42f66d3be24b78c51e6c9e7ebc4e7d0dbcbda9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableAcceleration", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2b93b0f8d4f693cc8f21f3c8c72a86285d65448324383d411fad4a38e8ff0c8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="localIpv4NetworkCidr")
    def local_ipv4_network_cidr(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "localIpv4NetworkCidr"))

    @local_ipv4_network_cidr.setter
    def local_ipv4_network_cidr(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6cd8faf5fa50c111a3847bd04a778c3c415102bd5df94bac9bac99141144b727)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "localIpv4NetworkCidr", value)

    @builtins.property
    @jsii.member(jsii_name="localIpv6NetworkCidr")
    def local_ipv6_network_cidr(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "localIpv6NetworkCidr"))

    @local_ipv6_network_cidr.setter
    def local_ipv6_network_cidr(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d94f92231963bc89f8225e9635c524f940a0b53a113a29d1adfff1c5d517632e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "localIpv6NetworkCidr", value)

    @builtins.property
    @jsii.member(jsii_name="outsideIpAddressType")
    def outside_ip_address_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "outsideIpAddressType"))

    @outside_ip_address_type.setter
    def outside_ip_address_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__899fb965bce16dfde63bcee942cdcd1a253f88cc477eb1c7795886ed41d19369)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "outsideIpAddressType", value)

    @builtins.property
    @jsii.member(jsii_name="remoteIpv4NetworkCidr")
    def remote_ipv4_network_cidr(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "remoteIpv4NetworkCidr"))

    @remote_ipv4_network_cidr.setter
    def remote_ipv4_network_cidr(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38a4762d396e4738755286247b3d53c1bb1b6bececfe5aa0b997f35e4106b871)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "remoteIpv4NetworkCidr", value)

    @builtins.property
    @jsii.member(jsii_name="remoteIpv6NetworkCidr")
    def remote_ipv6_network_cidr(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "remoteIpv6NetworkCidr"))

    @remote_ipv6_network_cidr.setter
    def remote_ipv6_network_cidr(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__151ecee5376b5f1a092e433e3f29696f8e509bc8d5522f26a38643bf6a4a9c03)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "remoteIpv6NetworkCidr", value)

    @builtins.property
    @jsii.member(jsii_name="staticRoutesOnly")
    def static_routes_only(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "staticRoutesOnly"))

    @static_routes_only.setter
    def static_routes_only(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d58f22b3932203aa8a8ab2add7fface8e5690cfe05d464be1ad412c6b9cfe52)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "staticRoutesOnly", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b9daa7a058bac94e78e25a6d0889b2bd9fb8b257adf7b900dcfddaca77ff3ec3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60b72bc5357d96870ad0b46d24188ff321bbebfdd9425ab5a536f1b02d4dbfbe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)

    @builtins.property
    @jsii.member(jsii_name="transitGatewayId")
    def transit_gateway_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "transitGatewayId"))

    @transit_gateway_id.setter
    def transit_gateway_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c80ba96081f031e7831a35e984541394b4d600cebcdd5e6589d23895c5c8ae68)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "transitGatewayId", value)

    @builtins.property
    @jsii.member(jsii_name="transportTransitGatewayAttachmentId")
    def transport_transit_gateway_attachment_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "transportTransitGatewayAttachmentId"))

    @transport_transit_gateway_attachment_id.setter
    def transport_transit_gateway_attachment_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cbaf33621f33415167aa4b52d6202bd0b60e66fbe6e63f7b82be999e538832e3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "transportTransitGatewayAttachmentId", value)

    @builtins.property
    @jsii.member(jsii_name="tunnel1DpdTimeoutAction")
    def tunnel1_dpd_timeout_action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tunnel1DpdTimeoutAction"))

    @tunnel1_dpd_timeout_action.setter
    def tunnel1_dpd_timeout_action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29acec0673c7baabefeb7d1c522bc01a393183974a7b05ff5360698b3039de2a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tunnel1DpdTimeoutAction", value)

    @builtins.property
    @jsii.member(jsii_name="tunnel1DpdTimeoutSeconds")
    def tunnel1_dpd_timeout_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "tunnel1DpdTimeoutSeconds"))

    @tunnel1_dpd_timeout_seconds.setter
    def tunnel1_dpd_timeout_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18c2d086d72ea0d1fdaad5a8ed63b4a740691a1ebd341fe2832aea109d5c56f1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tunnel1DpdTimeoutSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="tunnel1IkeVersions")
    def tunnel1_ike_versions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tunnel1IkeVersions"))

    @tunnel1_ike_versions.setter
    def tunnel1_ike_versions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c14380765a8016c6822dc837d5fc568fe40fecb513503188054cb2782cdde47)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tunnel1IkeVersions", value)

    @builtins.property
    @jsii.member(jsii_name="tunnel1InsideCidr")
    def tunnel1_inside_cidr(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tunnel1InsideCidr"))

    @tunnel1_inside_cidr.setter
    def tunnel1_inside_cidr(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f3b4c375dcb9d7373078310b87debe1c34fb900eb506c4f2286fef60834df46)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tunnel1InsideCidr", value)

    @builtins.property
    @jsii.member(jsii_name="tunnel1InsideIpv6Cidr")
    def tunnel1_inside_ipv6_cidr(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tunnel1InsideIpv6Cidr"))

    @tunnel1_inside_ipv6_cidr.setter
    def tunnel1_inside_ipv6_cidr(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70a362885e4ca68915e4a3457e5d6689df213ee1739bd54346476f3a84984f30)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tunnel1InsideIpv6Cidr", value)

    @builtins.property
    @jsii.member(jsii_name="tunnel1Phase1DhGroupNumbers")
    def tunnel1_phase1_dh_group_numbers(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "tunnel1Phase1DhGroupNumbers"))

    @tunnel1_phase1_dh_group_numbers.setter
    def tunnel1_phase1_dh_group_numbers(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__adacadebf5035261db93e0430865347cfcb9837bd68282cbde04d48c7eaa553a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tunnel1Phase1DhGroupNumbers", value)

    @builtins.property
    @jsii.member(jsii_name="tunnel1Phase1EncryptionAlgorithms")
    def tunnel1_phase1_encryption_algorithms(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tunnel1Phase1EncryptionAlgorithms"))

    @tunnel1_phase1_encryption_algorithms.setter
    def tunnel1_phase1_encryption_algorithms(
        self,
        value: typing.List[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c201028791245fdd30db3c44e05d909bb1553785c6b265c321d2b99ddc6e81e5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tunnel1Phase1EncryptionAlgorithms", value)

    @builtins.property
    @jsii.member(jsii_name="tunnel1Phase1IntegrityAlgorithms")
    def tunnel1_phase1_integrity_algorithms(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tunnel1Phase1IntegrityAlgorithms"))

    @tunnel1_phase1_integrity_algorithms.setter
    def tunnel1_phase1_integrity_algorithms(
        self,
        value: typing.List[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61294bd545aaa272c0ee06494090a0cbf9a1a75fbf6967c17e2aabe3f0bd99d8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tunnel1Phase1IntegrityAlgorithms", value)

    @builtins.property
    @jsii.member(jsii_name="tunnel1Phase1LifetimeSeconds")
    def tunnel1_phase1_lifetime_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "tunnel1Phase1LifetimeSeconds"))

    @tunnel1_phase1_lifetime_seconds.setter
    def tunnel1_phase1_lifetime_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7c735335a1b0d70b380007c85d3e66d8af635b2e8bd0c3dd7c37bb384b67c21)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tunnel1Phase1LifetimeSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="tunnel1Phase2DhGroupNumbers")
    def tunnel1_phase2_dh_group_numbers(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "tunnel1Phase2DhGroupNumbers"))

    @tunnel1_phase2_dh_group_numbers.setter
    def tunnel1_phase2_dh_group_numbers(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b399bc6a6d99016f9651926032377edde62af435a8439361526f5256919581a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tunnel1Phase2DhGroupNumbers", value)

    @builtins.property
    @jsii.member(jsii_name="tunnel1Phase2EncryptionAlgorithms")
    def tunnel1_phase2_encryption_algorithms(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tunnel1Phase2EncryptionAlgorithms"))

    @tunnel1_phase2_encryption_algorithms.setter
    def tunnel1_phase2_encryption_algorithms(
        self,
        value: typing.List[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b69610665e422eadd8ef42f40cd6002b3e245c65d933d6a0c0be482601569a75)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tunnel1Phase2EncryptionAlgorithms", value)

    @builtins.property
    @jsii.member(jsii_name="tunnel1Phase2IntegrityAlgorithms")
    def tunnel1_phase2_integrity_algorithms(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tunnel1Phase2IntegrityAlgorithms"))

    @tunnel1_phase2_integrity_algorithms.setter
    def tunnel1_phase2_integrity_algorithms(
        self,
        value: typing.List[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0bbe722f6bbac073cd3743150a073d7e070d87a3bee5280c56c0822d5e397bac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tunnel1Phase2IntegrityAlgorithms", value)

    @builtins.property
    @jsii.member(jsii_name="tunnel1Phase2LifetimeSeconds")
    def tunnel1_phase2_lifetime_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "tunnel1Phase2LifetimeSeconds"))

    @tunnel1_phase2_lifetime_seconds.setter
    def tunnel1_phase2_lifetime_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8380952122a02891c0d83af24234b36f65f3394e363c07c0c4b95e8cf0e180c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tunnel1Phase2LifetimeSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="tunnel1PresharedKey")
    def tunnel1_preshared_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tunnel1PresharedKey"))

    @tunnel1_preshared_key.setter
    def tunnel1_preshared_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0abcfa1ebf9eebe6827496611dd0f853fe95b843115b85b5c7be04bf8121e6ac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tunnel1PresharedKey", value)

    @builtins.property
    @jsii.member(jsii_name="tunnel1RekeyFuzzPercentage")
    def tunnel1_rekey_fuzz_percentage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "tunnel1RekeyFuzzPercentage"))

    @tunnel1_rekey_fuzz_percentage.setter
    def tunnel1_rekey_fuzz_percentage(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb8dd4cfd093b4ecd6731c756aadd3329d5d6cbd3a63c3bab906d33c2d8c3d50)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tunnel1RekeyFuzzPercentage", value)

    @builtins.property
    @jsii.member(jsii_name="tunnel1RekeyMarginTimeSeconds")
    def tunnel1_rekey_margin_time_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "tunnel1RekeyMarginTimeSeconds"))

    @tunnel1_rekey_margin_time_seconds.setter
    def tunnel1_rekey_margin_time_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__721bbda036a39be1425bc421a970aaaf550ba4a8181aec41338a3183463c0735)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tunnel1RekeyMarginTimeSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="tunnel1ReplayWindowSize")
    def tunnel1_replay_window_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "tunnel1ReplayWindowSize"))

    @tunnel1_replay_window_size.setter
    def tunnel1_replay_window_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e7b42e497a2bdb48704843070fb64c5b3ddec65f68f37d95f1d8ea7893dcfde)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tunnel1ReplayWindowSize", value)

    @builtins.property
    @jsii.member(jsii_name="tunnel1StartupAction")
    def tunnel1_startup_action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tunnel1StartupAction"))

    @tunnel1_startup_action.setter
    def tunnel1_startup_action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__31a48077527a9ec9b33b36b2c28f388a8584aa9f06353858247d2ce3079c9f34)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tunnel1StartupAction", value)

    @builtins.property
    @jsii.member(jsii_name="tunnel2DpdTimeoutAction")
    def tunnel2_dpd_timeout_action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tunnel2DpdTimeoutAction"))

    @tunnel2_dpd_timeout_action.setter
    def tunnel2_dpd_timeout_action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fde2a31ac9ee3fd1008dc5c669a41e598362453b1c835bfaed8fe99e0af25a9c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tunnel2DpdTimeoutAction", value)

    @builtins.property
    @jsii.member(jsii_name="tunnel2DpdTimeoutSeconds")
    def tunnel2_dpd_timeout_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "tunnel2DpdTimeoutSeconds"))

    @tunnel2_dpd_timeout_seconds.setter
    def tunnel2_dpd_timeout_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60d427c94c279349b8e79a2de7f25290a6ca26acf17502e25dc094c6ab9a641e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tunnel2DpdTimeoutSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="tunnel2IkeVersions")
    def tunnel2_ike_versions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tunnel2IkeVersions"))

    @tunnel2_ike_versions.setter
    def tunnel2_ike_versions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c5855f491eb6a7c0c51029215749eb3875e081f9cfa7a5e36da0c83a7a1fb63)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tunnel2IkeVersions", value)

    @builtins.property
    @jsii.member(jsii_name="tunnel2InsideCidr")
    def tunnel2_inside_cidr(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tunnel2InsideCidr"))

    @tunnel2_inside_cidr.setter
    def tunnel2_inside_cidr(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9f8db832f7bef9582aaec012f27617cbab68be99d1924f4fc20d94c56dfc99e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tunnel2InsideCidr", value)

    @builtins.property
    @jsii.member(jsii_name="tunnel2InsideIpv6Cidr")
    def tunnel2_inside_ipv6_cidr(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tunnel2InsideIpv6Cidr"))

    @tunnel2_inside_ipv6_cidr.setter
    def tunnel2_inside_ipv6_cidr(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d91dd11aa46be5cf232e4d8cfda5a22e2bfa1af2b7095af1b1d265ee5d0a482b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tunnel2InsideIpv6Cidr", value)

    @builtins.property
    @jsii.member(jsii_name="tunnel2Phase1DhGroupNumbers")
    def tunnel2_phase1_dh_group_numbers(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "tunnel2Phase1DhGroupNumbers"))

    @tunnel2_phase1_dh_group_numbers.setter
    def tunnel2_phase1_dh_group_numbers(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__486905d4b259c578f9b403caa928bd0088a178e20e34938592950e1243950b49)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tunnel2Phase1DhGroupNumbers", value)

    @builtins.property
    @jsii.member(jsii_name="tunnel2Phase1EncryptionAlgorithms")
    def tunnel2_phase1_encryption_algorithms(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tunnel2Phase1EncryptionAlgorithms"))

    @tunnel2_phase1_encryption_algorithms.setter
    def tunnel2_phase1_encryption_algorithms(
        self,
        value: typing.List[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb4459090b916a5ee529b1043e20aa725ecf13b76eb1163f891ad5eafe6286c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tunnel2Phase1EncryptionAlgorithms", value)

    @builtins.property
    @jsii.member(jsii_name="tunnel2Phase1IntegrityAlgorithms")
    def tunnel2_phase1_integrity_algorithms(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tunnel2Phase1IntegrityAlgorithms"))

    @tunnel2_phase1_integrity_algorithms.setter
    def tunnel2_phase1_integrity_algorithms(
        self,
        value: typing.List[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f06e3a2d1e444e884ac55ee556abfa582d0d98855c702dbd6cdba74ebb8517a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tunnel2Phase1IntegrityAlgorithms", value)

    @builtins.property
    @jsii.member(jsii_name="tunnel2Phase1LifetimeSeconds")
    def tunnel2_phase1_lifetime_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "tunnel2Phase1LifetimeSeconds"))

    @tunnel2_phase1_lifetime_seconds.setter
    def tunnel2_phase1_lifetime_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__262d9466750aebc1a2de3c7bec4563cb57d458fc88d70164a905985f34c9049c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tunnel2Phase1LifetimeSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="tunnel2Phase2DhGroupNumbers")
    def tunnel2_phase2_dh_group_numbers(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "tunnel2Phase2DhGroupNumbers"))

    @tunnel2_phase2_dh_group_numbers.setter
    def tunnel2_phase2_dh_group_numbers(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__faa7d37c5977b283fe60cc7fcc55e3c7c46686963253ecf95bceacdb2b299abb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tunnel2Phase2DhGroupNumbers", value)

    @builtins.property
    @jsii.member(jsii_name="tunnel2Phase2EncryptionAlgorithms")
    def tunnel2_phase2_encryption_algorithms(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tunnel2Phase2EncryptionAlgorithms"))

    @tunnel2_phase2_encryption_algorithms.setter
    def tunnel2_phase2_encryption_algorithms(
        self,
        value: typing.List[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d78286e6e5256508132f950ca5d3233e0ac5115e05e785d493c3342635a312eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tunnel2Phase2EncryptionAlgorithms", value)

    @builtins.property
    @jsii.member(jsii_name="tunnel2Phase2IntegrityAlgorithms")
    def tunnel2_phase2_integrity_algorithms(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tunnel2Phase2IntegrityAlgorithms"))

    @tunnel2_phase2_integrity_algorithms.setter
    def tunnel2_phase2_integrity_algorithms(
        self,
        value: typing.List[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a3cf09c43b618be20a9419b2e992a05d6f6933637dcc6066a3e17945de51d9c4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tunnel2Phase2IntegrityAlgorithms", value)

    @builtins.property
    @jsii.member(jsii_name="tunnel2Phase2LifetimeSeconds")
    def tunnel2_phase2_lifetime_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "tunnel2Phase2LifetimeSeconds"))

    @tunnel2_phase2_lifetime_seconds.setter
    def tunnel2_phase2_lifetime_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2fd664268b2376ace72f5e71c66f12522e83d1d35836cb06704ebcc73646be16)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tunnel2Phase2LifetimeSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="tunnel2PresharedKey")
    def tunnel2_preshared_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tunnel2PresharedKey"))

    @tunnel2_preshared_key.setter
    def tunnel2_preshared_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8924119467b45580d97808647a058f9c675c4cdad4db4d0646ca30ec8679246d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tunnel2PresharedKey", value)

    @builtins.property
    @jsii.member(jsii_name="tunnel2RekeyFuzzPercentage")
    def tunnel2_rekey_fuzz_percentage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "tunnel2RekeyFuzzPercentage"))

    @tunnel2_rekey_fuzz_percentage.setter
    def tunnel2_rekey_fuzz_percentage(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8064330a0fca896c02552d73d690fff8d635f00235fea74462a47971568d6ee3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tunnel2RekeyFuzzPercentage", value)

    @builtins.property
    @jsii.member(jsii_name="tunnel2RekeyMarginTimeSeconds")
    def tunnel2_rekey_margin_time_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "tunnel2RekeyMarginTimeSeconds"))

    @tunnel2_rekey_margin_time_seconds.setter
    def tunnel2_rekey_margin_time_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78a0e4ee1b7f1e36c3b648937030b559dd6921b800c6d82b3f990a499ca8a4f3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tunnel2RekeyMarginTimeSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="tunnel2ReplayWindowSize")
    def tunnel2_replay_window_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "tunnel2ReplayWindowSize"))

    @tunnel2_replay_window_size.setter
    def tunnel2_replay_window_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5426ccfd75015845356983450a9243d2d3fc44fe8036f6cb112ca62f644806f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tunnel2ReplayWindowSize", value)

    @builtins.property
    @jsii.member(jsii_name="tunnel2StartupAction")
    def tunnel2_startup_action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tunnel2StartupAction"))

    @tunnel2_startup_action.setter
    def tunnel2_startup_action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__643c8fc7c3263a421f9fdfbbe887566a58a81c162e209e14a3b527993978578a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tunnel2StartupAction", value)

    @builtins.property
    @jsii.member(jsii_name="tunnelInsideIpVersion")
    def tunnel_inside_ip_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tunnelInsideIpVersion"))

    @tunnel_inside_ip_version.setter
    def tunnel_inside_ip_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5204f7727a09104fcaa8f2e85ae0f253aad609450567f6e087306b97b49c2627)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tunnelInsideIpVersion", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d54960b533163e297d271f030743b91635b6588c84ba14e52822dccf9505484)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="vpnGatewayId")
    def vpn_gateway_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vpnGatewayId"))

    @vpn_gateway_id.setter
    def vpn_gateway_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__51778d06553e52be5a32a7d52d194d975360c3b723b4c91ac7db503fe9320bbf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpnGatewayId", value)


@jsii.data_type(
    jsii_type="aws.vpnConnection.VpnConnectionConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "customer_gateway_id": "customerGatewayId",
        "type": "type",
        "enable_acceleration": "enableAcceleration",
        "id": "id",
        "local_ipv4_network_cidr": "localIpv4NetworkCidr",
        "local_ipv6_network_cidr": "localIpv6NetworkCidr",
        "outside_ip_address_type": "outsideIpAddressType",
        "remote_ipv4_network_cidr": "remoteIpv4NetworkCidr",
        "remote_ipv6_network_cidr": "remoteIpv6NetworkCidr",
        "static_routes_only": "staticRoutesOnly",
        "tags": "tags",
        "tags_all": "tagsAll",
        "transit_gateway_id": "transitGatewayId",
        "transport_transit_gateway_attachment_id": "transportTransitGatewayAttachmentId",
        "tunnel1_dpd_timeout_action": "tunnel1DpdTimeoutAction",
        "tunnel1_dpd_timeout_seconds": "tunnel1DpdTimeoutSeconds",
        "tunnel1_ike_versions": "tunnel1IkeVersions",
        "tunnel1_inside_cidr": "tunnel1InsideCidr",
        "tunnel1_inside_ipv6_cidr": "tunnel1InsideIpv6Cidr",
        "tunnel1_log_options": "tunnel1LogOptions",
        "tunnel1_phase1_dh_group_numbers": "tunnel1Phase1DhGroupNumbers",
        "tunnel1_phase1_encryption_algorithms": "tunnel1Phase1EncryptionAlgorithms",
        "tunnel1_phase1_integrity_algorithms": "tunnel1Phase1IntegrityAlgorithms",
        "tunnel1_phase1_lifetime_seconds": "tunnel1Phase1LifetimeSeconds",
        "tunnel1_phase2_dh_group_numbers": "tunnel1Phase2DhGroupNumbers",
        "tunnel1_phase2_encryption_algorithms": "tunnel1Phase2EncryptionAlgorithms",
        "tunnel1_phase2_integrity_algorithms": "tunnel1Phase2IntegrityAlgorithms",
        "tunnel1_phase2_lifetime_seconds": "tunnel1Phase2LifetimeSeconds",
        "tunnel1_preshared_key": "tunnel1PresharedKey",
        "tunnel1_rekey_fuzz_percentage": "tunnel1RekeyFuzzPercentage",
        "tunnel1_rekey_margin_time_seconds": "tunnel1RekeyMarginTimeSeconds",
        "tunnel1_replay_window_size": "tunnel1ReplayWindowSize",
        "tunnel1_startup_action": "tunnel1StartupAction",
        "tunnel2_dpd_timeout_action": "tunnel2DpdTimeoutAction",
        "tunnel2_dpd_timeout_seconds": "tunnel2DpdTimeoutSeconds",
        "tunnel2_ike_versions": "tunnel2IkeVersions",
        "tunnel2_inside_cidr": "tunnel2InsideCidr",
        "tunnel2_inside_ipv6_cidr": "tunnel2InsideIpv6Cidr",
        "tunnel2_log_options": "tunnel2LogOptions",
        "tunnel2_phase1_dh_group_numbers": "tunnel2Phase1DhGroupNumbers",
        "tunnel2_phase1_encryption_algorithms": "tunnel2Phase1EncryptionAlgorithms",
        "tunnel2_phase1_integrity_algorithms": "tunnel2Phase1IntegrityAlgorithms",
        "tunnel2_phase1_lifetime_seconds": "tunnel2Phase1LifetimeSeconds",
        "tunnel2_phase2_dh_group_numbers": "tunnel2Phase2DhGroupNumbers",
        "tunnel2_phase2_encryption_algorithms": "tunnel2Phase2EncryptionAlgorithms",
        "tunnel2_phase2_integrity_algorithms": "tunnel2Phase2IntegrityAlgorithms",
        "tunnel2_phase2_lifetime_seconds": "tunnel2Phase2LifetimeSeconds",
        "tunnel2_preshared_key": "tunnel2PresharedKey",
        "tunnel2_rekey_fuzz_percentage": "tunnel2RekeyFuzzPercentage",
        "tunnel2_rekey_margin_time_seconds": "tunnel2RekeyMarginTimeSeconds",
        "tunnel2_replay_window_size": "tunnel2ReplayWindowSize",
        "tunnel2_startup_action": "tunnel2StartupAction",
        "tunnel_inside_ip_version": "tunnelInsideIpVersion",
        "vpn_gateway_id": "vpnGatewayId",
    },
)
class VpnConnectionConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        customer_gateway_id: builtins.str,
        type: builtins.str,
        enable_acceleration: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        local_ipv4_network_cidr: typing.Optional[builtins.str] = None,
        local_ipv6_network_cidr: typing.Optional[builtins.str] = None,
        outside_ip_address_type: typing.Optional[builtins.str] = None,
        remote_ipv4_network_cidr: typing.Optional[builtins.str] = None,
        remote_ipv6_network_cidr: typing.Optional[builtins.str] = None,
        static_routes_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        transit_gateway_id: typing.Optional[builtins.str] = None,
        transport_transit_gateway_attachment_id: typing.Optional[builtins.str] = None,
        tunnel1_dpd_timeout_action: typing.Optional[builtins.str] = None,
        tunnel1_dpd_timeout_seconds: typing.Optional[jsii.Number] = None,
        tunnel1_ike_versions: typing.Optional[typing.Sequence[builtins.str]] = None,
        tunnel1_inside_cidr: typing.Optional[builtins.str] = None,
        tunnel1_inside_ipv6_cidr: typing.Optional[builtins.str] = None,
        tunnel1_log_options: typing.Optional[typing.Union["VpnConnectionTunnel1LogOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        tunnel1_phase1_dh_group_numbers: typing.Optional[typing.Sequence[jsii.Number]] = None,
        tunnel1_phase1_encryption_algorithms: typing.Optional[typing.Sequence[builtins.str]] = None,
        tunnel1_phase1_integrity_algorithms: typing.Optional[typing.Sequence[builtins.str]] = None,
        tunnel1_phase1_lifetime_seconds: typing.Optional[jsii.Number] = None,
        tunnel1_phase2_dh_group_numbers: typing.Optional[typing.Sequence[jsii.Number]] = None,
        tunnel1_phase2_encryption_algorithms: typing.Optional[typing.Sequence[builtins.str]] = None,
        tunnel1_phase2_integrity_algorithms: typing.Optional[typing.Sequence[builtins.str]] = None,
        tunnel1_phase2_lifetime_seconds: typing.Optional[jsii.Number] = None,
        tunnel1_preshared_key: typing.Optional[builtins.str] = None,
        tunnel1_rekey_fuzz_percentage: typing.Optional[jsii.Number] = None,
        tunnel1_rekey_margin_time_seconds: typing.Optional[jsii.Number] = None,
        tunnel1_replay_window_size: typing.Optional[jsii.Number] = None,
        tunnel1_startup_action: typing.Optional[builtins.str] = None,
        tunnel2_dpd_timeout_action: typing.Optional[builtins.str] = None,
        tunnel2_dpd_timeout_seconds: typing.Optional[jsii.Number] = None,
        tunnel2_ike_versions: typing.Optional[typing.Sequence[builtins.str]] = None,
        tunnel2_inside_cidr: typing.Optional[builtins.str] = None,
        tunnel2_inside_ipv6_cidr: typing.Optional[builtins.str] = None,
        tunnel2_log_options: typing.Optional[typing.Union["VpnConnectionTunnel2LogOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        tunnel2_phase1_dh_group_numbers: typing.Optional[typing.Sequence[jsii.Number]] = None,
        tunnel2_phase1_encryption_algorithms: typing.Optional[typing.Sequence[builtins.str]] = None,
        tunnel2_phase1_integrity_algorithms: typing.Optional[typing.Sequence[builtins.str]] = None,
        tunnel2_phase1_lifetime_seconds: typing.Optional[jsii.Number] = None,
        tunnel2_phase2_dh_group_numbers: typing.Optional[typing.Sequence[jsii.Number]] = None,
        tunnel2_phase2_encryption_algorithms: typing.Optional[typing.Sequence[builtins.str]] = None,
        tunnel2_phase2_integrity_algorithms: typing.Optional[typing.Sequence[builtins.str]] = None,
        tunnel2_phase2_lifetime_seconds: typing.Optional[jsii.Number] = None,
        tunnel2_preshared_key: typing.Optional[builtins.str] = None,
        tunnel2_rekey_fuzz_percentage: typing.Optional[jsii.Number] = None,
        tunnel2_rekey_margin_time_seconds: typing.Optional[jsii.Number] = None,
        tunnel2_replay_window_size: typing.Optional[jsii.Number] = None,
        tunnel2_startup_action: typing.Optional[builtins.str] = None,
        tunnel_inside_ip_version: typing.Optional[builtins.str] = None,
        vpn_gateway_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param customer_gateway_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#customer_gateway_id VpnConnection#customer_gateway_id}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#type VpnConnection#type}.
        :param enable_acceleration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#enable_acceleration VpnConnection#enable_acceleration}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#id VpnConnection#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param local_ipv4_network_cidr: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#local_ipv4_network_cidr VpnConnection#local_ipv4_network_cidr}.
        :param local_ipv6_network_cidr: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#local_ipv6_network_cidr VpnConnection#local_ipv6_network_cidr}.
        :param outside_ip_address_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#outside_ip_address_type VpnConnection#outside_ip_address_type}.
        :param remote_ipv4_network_cidr: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#remote_ipv4_network_cidr VpnConnection#remote_ipv4_network_cidr}.
        :param remote_ipv6_network_cidr: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#remote_ipv6_network_cidr VpnConnection#remote_ipv6_network_cidr}.
        :param static_routes_only: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#static_routes_only VpnConnection#static_routes_only}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tags VpnConnection#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tags_all VpnConnection#tags_all}.
        :param transit_gateway_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#transit_gateway_id VpnConnection#transit_gateway_id}.
        :param transport_transit_gateway_attachment_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#transport_transit_gateway_attachment_id VpnConnection#transport_transit_gateway_attachment_id}.
        :param tunnel1_dpd_timeout_action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_dpd_timeout_action VpnConnection#tunnel1_dpd_timeout_action}.
        :param tunnel1_dpd_timeout_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_dpd_timeout_seconds VpnConnection#tunnel1_dpd_timeout_seconds}.
        :param tunnel1_ike_versions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_ike_versions VpnConnection#tunnel1_ike_versions}.
        :param tunnel1_inside_cidr: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_inside_cidr VpnConnection#tunnel1_inside_cidr}.
        :param tunnel1_inside_ipv6_cidr: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_inside_ipv6_cidr VpnConnection#tunnel1_inside_ipv6_cidr}.
        :param tunnel1_log_options: tunnel1_log_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_log_options VpnConnection#tunnel1_log_options}
        :param tunnel1_phase1_dh_group_numbers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_phase1_dh_group_numbers VpnConnection#tunnel1_phase1_dh_group_numbers}.
        :param tunnel1_phase1_encryption_algorithms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_phase1_encryption_algorithms VpnConnection#tunnel1_phase1_encryption_algorithms}.
        :param tunnel1_phase1_integrity_algorithms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_phase1_integrity_algorithms VpnConnection#tunnel1_phase1_integrity_algorithms}.
        :param tunnel1_phase1_lifetime_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_phase1_lifetime_seconds VpnConnection#tunnel1_phase1_lifetime_seconds}.
        :param tunnel1_phase2_dh_group_numbers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_phase2_dh_group_numbers VpnConnection#tunnel1_phase2_dh_group_numbers}.
        :param tunnel1_phase2_encryption_algorithms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_phase2_encryption_algorithms VpnConnection#tunnel1_phase2_encryption_algorithms}.
        :param tunnel1_phase2_integrity_algorithms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_phase2_integrity_algorithms VpnConnection#tunnel1_phase2_integrity_algorithms}.
        :param tunnel1_phase2_lifetime_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_phase2_lifetime_seconds VpnConnection#tunnel1_phase2_lifetime_seconds}.
        :param tunnel1_preshared_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_preshared_key VpnConnection#tunnel1_preshared_key}.
        :param tunnel1_rekey_fuzz_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_rekey_fuzz_percentage VpnConnection#tunnel1_rekey_fuzz_percentage}.
        :param tunnel1_rekey_margin_time_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_rekey_margin_time_seconds VpnConnection#tunnel1_rekey_margin_time_seconds}.
        :param tunnel1_replay_window_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_replay_window_size VpnConnection#tunnel1_replay_window_size}.
        :param tunnel1_startup_action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_startup_action VpnConnection#tunnel1_startup_action}.
        :param tunnel2_dpd_timeout_action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_dpd_timeout_action VpnConnection#tunnel2_dpd_timeout_action}.
        :param tunnel2_dpd_timeout_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_dpd_timeout_seconds VpnConnection#tunnel2_dpd_timeout_seconds}.
        :param tunnel2_ike_versions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_ike_versions VpnConnection#tunnel2_ike_versions}.
        :param tunnel2_inside_cidr: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_inside_cidr VpnConnection#tunnel2_inside_cidr}.
        :param tunnel2_inside_ipv6_cidr: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_inside_ipv6_cidr VpnConnection#tunnel2_inside_ipv6_cidr}.
        :param tunnel2_log_options: tunnel2_log_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_log_options VpnConnection#tunnel2_log_options}
        :param tunnel2_phase1_dh_group_numbers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_phase1_dh_group_numbers VpnConnection#tunnel2_phase1_dh_group_numbers}.
        :param tunnel2_phase1_encryption_algorithms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_phase1_encryption_algorithms VpnConnection#tunnel2_phase1_encryption_algorithms}.
        :param tunnel2_phase1_integrity_algorithms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_phase1_integrity_algorithms VpnConnection#tunnel2_phase1_integrity_algorithms}.
        :param tunnel2_phase1_lifetime_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_phase1_lifetime_seconds VpnConnection#tunnel2_phase1_lifetime_seconds}.
        :param tunnel2_phase2_dh_group_numbers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_phase2_dh_group_numbers VpnConnection#tunnel2_phase2_dh_group_numbers}.
        :param tunnel2_phase2_encryption_algorithms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_phase2_encryption_algorithms VpnConnection#tunnel2_phase2_encryption_algorithms}.
        :param tunnel2_phase2_integrity_algorithms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_phase2_integrity_algorithms VpnConnection#tunnel2_phase2_integrity_algorithms}.
        :param tunnel2_phase2_lifetime_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_phase2_lifetime_seconds VpnConnection#tunnel2_phase2_lifetime_seconds}.
        :param tunnel2_preshared_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_preshared_key VpnConnection#tunnel2_preshared_key}.
        :param tunnel2_rekey_fuzz_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_rekey_fuzz_percentage VpnConnection#tunnel2_rekey_fuzz_percentage}.
        :param tunnel2_rekey_margin_time_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_rekey_margin_time_seconds VpnConnection#tunnel2_rekey_margin_time_seconds}.
        :param tunnel2_replay_window_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_replay_window_size VpnConnection#tunnel2_replay_window_size}.
        :param tunnel2_startup_action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_startup_action VpnConnection#tunnel2_startup_action}.
        :param tunnel_inside_ip_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel_inside_ip_version VpnConnection#tunnel_inside_ip_version}.
        :param vpn_gateway_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#vpn_gateway_id VpnConnection#vpn_gateway_id}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(tunnel1_log_options, dict):
            tunnel1_log_options = VpnConnectionTunnel1LogOptions(**tunnel1_log_options)
        if isinstance(tunnel2_log_options, dict):
            tunnel2_log_options = VpnConnectionTunnel2LogOptions(**tunnel2_log_options)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a94768fd856d3f11ad4339d86c6bd005579eafe549e0970427a7101c862d90bd)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument customer_gateway_id", value=customer_gateway_id, expected_type=type_hints["customer_gateway_id"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument enable_acceleration", value=enable_acceleration, expected_type=type_hints["enable_acceleration"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument local_ipv4_network_cidr", value=local_ipv4_network_cidr, expected_type=type_hints["local_ipv4_network_cidr"])
            check_type(argname="argument local_ipv6_network_cidr", value=local_ipv6_network_cidr, expected_type=type_hints["local_ipv6_network_cidr"])
            check_type(argname="argument outside_ip_address_type", value=outside_ip_address_type, expected_type=type_hints["outside_ip_address_type"])
            check_type(argname="argument remote_ipv4_network_cidr", value=remote_ipv4_network_cidr, expected_type=type_hints["remote_ipv4_network_cidr"])
            check_type(argname="argument remote_ipv6_network_cidr", value=remote_ipv6_network_cidr, expected_type=type_hints["remote_ipv6_network_cidr"])
            check_type(argname="argument static_routes_only", value=static_routes_only, expected_type=type_hints["static_routes_only"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument transit_gateway_id", value=transit_gateway_id, expected_type=type_hints["transit_gateway_id"])
            check_type(argname="argument transport_transit_gateway_attachment_id", value=transport_transit_gateway_attachment_id, expected_type=type_hints["transport_transit_gateway_attachment_id"])
            check_type(argname="argument tunnel1_dpd_timeout_action", value=tunnel1_dpd_timeout_action, expected_type=type_hints["tunnel1_dpd_timeout_action"])
            check_type(argname="argument tunnel1_dpd_timeout_seconds", value=tunnel1_dpd_timeout_seconds, expected_type=type_hints["tunnel1_dpd_timeout_seconds"])
            check_type(argname="argument tunnel1_ike_versions", value=tunnel1_ike_versions, expected_type=type_hints["tunnel1_ike_versions"])
            check_type(argname="argument tunnel1_inside_cidr", value=tunnel1_inside_cidr, expected_type=type_hints["tunnel1_inside_cidr"])
            check_type(argname="argument tunnel1_inside_ipv6_cidr", value=tunnel1_inside_ipv6_cidr, expected_type=type_hints["tunnel1_inside_ipv6_cidr"])
            check_type(argname="argument tunnel1_log_options", value=tunnel1_log_options, expected_type=type_hints["tunnel1_log_options"])
            check_type(argname="argument tunnel1_phase1_dh_group_numbers", value=tunnel1_phase1_dh_group_numbers, expected_type=type_hints["tunnel1_phase1_dh_group_numbers"])
            check_type(argname="argument tunnel1_phase1_encryption_algorithms", value=tunnel1_phase1_encryption_algorithms, expected_type=type_hints["tunnel1_phase1_encryption_algorithms"])
            check_type(argname="argument tunnel1_phase1_integrity_algorithms", value=tunnel1_phase1_integrity_algorithms, expected_type=type_hints["tunnel1_phase1_integrity_algorithms"])
            check_type(argname="argument tunnel1_phase1_lifetime_seconds", value=tunnel1_phase1_lifetime_seconds, expected_type=type_hints["tunnel1_phase1_lifetime_seconds"])
            check_type(argname="argument tunnel1_phase2_dh_group_numbers", value=tunnel1_phase2_dh_group_numbers, expected_type=type_hints["tunnel1_phase2_dh_group_numbers"])
            check_type(argname="argument tunnel1_phase2_encryption_algorithms", value=tunnel1_phase2_encryption_algorithms, expected_type=type_hints["tunnel1_phase2_encryption_algorithms"])
            check_type(argname="argument tunnel1_phase2_integrity_algorithms", value=tunnel1_phase2_integrity_algorithms, expected_type=type_hints["tunnel1_phase2_integrity_algorithms"])
            check_type(argname="argument tunnel1_phase2_lifetime_seconds", value=tunnel1_phase2_lifetime_seconds, expected_type=type_hints["tunnel1_phase2_lifetime_seconds"])
            check_type(argname="argument tunnel1_preshared_key", value=tunnel1_preshared_key, expected_type=type_hints["tunnel1_preshared_key"])
            check_type(argname="argument tunnel1_rekey_fuzz_percentage", value=tunnel1_rekey_fuzz_percentage, expected_type=type_hints["tunnel1_rekey_fuzz_percentage"])
            check_type(argname="argument tunnel1_rekey_margin_time_seconds", value=tunnel1_rekey_margin_time_seconds, expected_type=type_hints["tunnel1_rekey_margin_time_seconds"])
            check_type(argname="argument tunnel1_replay_window_size", value=tunnel1_replay_window_size, expected_type=type_hints["tunnel1_replay_window_size"])
            check_type(argname="argument tunnel1_startup_action", value=tunnel1_startup_action, expected_type=type_hints["tunnel1_startup_action"])
            check_type(argname="argument tunnel2_dpd_timeout_action", value=tunnel2_dpd_timeout_action, expected_type=type_hints["tunnel2_dpd_timeout_action"])
            check_type(argname="argument tunnel2_dpd_timeout_seconds", value=tunnel2_dpd_timeout_seconds, expected_type=type_hints["tunnel2_dpd_timeout_seconds"])
            check_type(argname="argument tunnel2_ike_versions", value=tunnel2_ike_versions, expected_type=type_hints["tunnel2_ike_versions"])
            check_type(argname="argument tunnel2_inside_cidr", value=tunnel2_inside_cidr, expected_type=type_hints["tunnel2_inside_cidr"])
            check_type(argname="argument tunnel2_inside_ipv6_cidr", value=tunnel2_inside_ipv6_cidr, expected_type=type_hints["tunnel2_inside_ipv6_cidr"])
            check_type(argname="argument tunnel2_log_options", value=tunnel2_log_options, expected_type=type_hints["tunnel2_log_options"])
            check_type(argname="argument tunnel2_phase1_dh_group_numbers", value=tunnel2_phase1_dh_group_numbers, expected_type=type_hints["tunnel2_phase1_dh_group_numbers"])
            check_type(argname="argument tunnel2_phase1_encryption_algorithms", value=tunnel2_phase1_encryption_algorithms, expected_type=type_hints["tunnel2_phase1_encryption_algorithms"])
            check_type(argname="argument tunnel2_phase1_integrity_algorithms", value=tunnel2_phase1_integrity_algorithms, expected_type=type_hints["tunnel2_phase1_integrity_algorithms"])
            check_type(argname="argument tunnel2_phase1_lifetime_seconds", value=tunnel2_phase1_lifetime_seconds, expected_type=type_hints["tunnel2_phase1_lifetime_seconds"])
            check_type(argname="argument tunnel2_phase2_dh_group_numbers", value=tunnel2_phase2_dh_group_numbers, expected_type=type_hints["tunnel2_phase2_dh_group_numbers"])
            check_type(argname="argument tunnel2_phase2_encryption_algorithms", value=tunnel2_phase2_encryption_algorithms, expected_type=type_hints["tunnel2_phase2_encryption_algorithms"])
            check_type(argname="argument tunnel2_phase2_integrity_algorithms", value=tunnel2_phase2_integrity_algorithms, expected_type=type_hints["tunnel2_phase2_integrity_algorithms"])
            check_type(argname="argument tunnel2_phase2_lifetime_seconds", value=tunnel2_phase2_lifetime_seconds, expected_type=type_hints["tunnel2_phase2_lifetime_seconds"])
            check_type(argname="argument tunnel2_preshared_key", value=tunnel2_preshared_key, expected_type=type_hints["tunnel2_preshared_key"])
            check_type(argname="argument tunnel2_rekey_fuzz_percentage", value=tunnel2_rekey_fuzz_percentage, expected_type=type_hints["tunnel2_rekey_fuzz_percentage"])
            check_type(argname="argument tunnel2_rekey_margin_time_seconds", value=tunnel2_rekey_margin_time_seconds, expected_type=type_hints["tunnel2_rekey_margin_time_seconds"])
            check_type(argname="argument tunnel2_replay_window_size", value=tunnel2_replay_window_size, expected_type=type_hints["tunnel2_replay_window_size"])
            check_type(argname="argument tunnel2_startup_action", value=tunnel2_startup_action, expected_type=type_hints["tunnel2_startup_action"])
            check_type(argname="argument tunnel_inside_ip_version", value=tunnel_inside_ip_version, expected_type=type_hints["tunnel_inside_ip_version"])
            check_type(argname="argument vpn_gateway_id", value=vpn_gateway_id, expected_type=type_hints["vpn_gateway_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "customer_gateway_id": customer_gateway_id,
            "type": type,
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
        if enable_acceleration is not None:
            self._values["enable_acceleration"] = enable_acceleration
        if id is not None:
            self._values["id"] = id
        if local_ipv4_network_cidr is not None:
            self._values["local_ipv4_network_cidr"] = local_ipv4_network_cidr
        if local_ipv6_network_cidr is not None:
            self._values["local_ipv6_network_cidr"] = local_ipv6_network_cidr
        if outside_ip_address_type is not None:
            self._values["outside_ip_address_type"] = outside_ip_address_type
        if remote_ipv4_network_cidr is not None:
            self._values["remote_ipv4_network_cidr"] = remote_ipv4_network_cidr
        if remote_ipv6_network_cidr is not None:
            self._values["remote_ipv6_network_cidr"] = remote_ipv6_network_cidr
        if static_routes_only is not None:
            self._values["static_routes_only"] = static_routes_only
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if transit_gateway_id is not None:
            self._values["transit_gateway_id"] = transit_gateway_id
        if transport_transit_gateway_attachment_id is not None:
            self._values["transport_transit_gateway_attachment_id"] = transport_transit_gateway_attachment_id
        if tunnel1_dpd_timeout_action is not None:
            self._values["tunnel1_dpd_timeout_action"] = tunnel1_dpd_timeout_action
        if tunnel1_dpd_timeout_seconds is not None:
            self._values["tunnel1_dpd_timeout_seconds"] = tunnel1_dpd_timeout_seconds
        if tunnel1_ike_versions is not None:
            self._values["tunnel1_ike_versions"] = tunnel1_ike_versions
        if tunnel1_inside_cidr is not None:
            self._values["tunnel1_inside_cidr"] = tunnel1_inside_cidr
        if tunnel1_inside_ipv6_cidr is not None:
            self._values["tunnel1_inside_ipv6_cidr"] = tunnel1_inside_ipv6_cidr
        if tunnel1_log_options is not None:
            self._values["tunnel1_log_options"] = tunnel1_log_options
        if tunnel1_phase1_dh_group_numbers is not None:
            self._values["tunnel1_phase1_dh_group_numbers"] = tunnel1_phase1_dh_group_numbers
        if tunnel1_phase1_encryption_algorithms is not None:
            self._values["tunnel1_phase1_encryption_algorithms"] = tunnel1_phase1_encryption_algorithms
        if tunnel1_phase1_integrity_algorithms is not None:
            self._values["tunnel1_phase1_integrity_algorithms"] = tunnel1_phase1_integrity_algorithms
        if tunnel1_phase1_lifetime_seconds is not None:
            self._values["tunnel1_phase1_lifetime_seconds"] = tunnel1_phase1_lifetime_seconds
        if tunnel1_phase2_dh_group_numbers is not None:
            self._values["tunnel1_phase2_dh_group_numbers"] = tunnel1_phase2_dh_group_numbers
        if tunnel1_phase2_encryption_algorithms is not None:
            self._values["tunnel1_phase2_encryption_algorithms"] = tunnel1_phase2_encryption_algorithms
        if tunnel1_phase2_integrity_algorithms is not None:
            self._values["tunnel1_phase2_integrity_algorithms"] = tunnel1_phase2_integrity_algorithms
        if tunnel1_phase2_lifetime_seconds is not None:
            self._values["tunnel1_phase2_lifetime_seconds"] = tunnel1_phase2_lifetime_seconds
        if tunnel1_preshared_key is not None:
            self._values["tunnel1_preshared_key"] = tunnel1_preshared_key
        if tunnel1_rekey_fuzz_percentage is not None:
            self._values["tunnel1_rekey_fuzz_percentage"] = tunnel1_rekey_fuzz_percentage
        if tunnel1_rekey_margin_time_seconds is not None:
            self._values["tunnel1_rekey_margin_time_seconds"] = tunnel1_rekey_margin_time_seconds
        if tunnel1_replay_window_size is not None:
            self._values["tunnel1_replay_window_size"] = tunnel1_replay_window_size
        if tunnel1_startup_action is not None:
            self._values["tunnel1_startup_action"] = tunnel1_startup_action
        if tunnel2_dpd_timeout_action is not None:
            self._values["tunnel2_dpd_timeout_action"] = tunnel2_dpd_timeout_action
        if tunnel2_dpd_timeout_seconds is not None:
            self._values["tunnel2_dpd_timeout_seconds"] = tunnel2_dpd_timeout_seconds
        if tunnel2_ike_versions is not None:
            self._values["tunnel2_ike_versions"] = tunnel2_ike_versions
        if tunnel2_inside_cidr is not None:
            self._values["tunnel2_inside_cidr"] = tunnel2_inside_cidr
        if tunnel2_inside_ipv6_cidr is not None:
            self._values["tunnel2_inside_ipv6_cidr"] = tunnel2_inside_ipv6_cidr
        if tunnel2_log_options is not None:
            self._values["tunnel2_log_options"] = tunnel2_log_options
        if tunnel2_phase1_dh_group_numbers is not None:
            self._values["tunnel2_phase1_dh_group_numbers"] = tunnel2_phase1_dh_group_numbers
        if tunnel2_phase1_encryption_algorithms is not None:
            self._values["tunnel2_phase1_encryption_algorithms"] = tunnel2_phase1_encryption_algorithms
        if tunnel2_phase1_integrity_algorithms is not None:
            self._values["tunnel2_phase1_integrity_algorithms"] = tunnel2_phase1_integrity_algorithms
        if tunnel2_phase1_lifetime_seconds is not None:
            self._values["tunnel2_phase1_lifetime_seconds"] = tunnel2_phase1_lifetime_seconds
        if tunnel2_phase2_dh_group_numbers is not None:
            self._values["tunnel2_phase2_dh_group_numbers"] = tunnel2_phase2_dh_group_numbers
        if tunnel2_phase2_encryption_algorithms is not None:
            self._values["tunnel2_phase2_encryption_algorithms"] = tunnel2_phase2_encryption_algorithms
        if tunnel2_phase2_integrity_algorithms is not None:
            self._values["tunnel2_phase2_integrity_algorithms"] = tunnel2_phase2_integrity_algorithms
        if tunnel2_phase2_lifetime_seconds is not None:
            self._values["tunnel2_phase2_lifetime_seconds"] = tunnel2_phase2_lifetime_seconds
        if tunnel2_preshared_key is not None:
            self._values["tunnel2_preshared_key"] = tunnel2_preshared_key
        if tunnel2_rekey_fuzz_percentage is not None:
            self._values["tunnel2_rekey_fuzz_percentage"] = tunnel2_rekey_fuzz_percentage
        if tunnel2_rekey_margin_time_seconds is not None:
            self._values["tunnel2_rekey_margin_time_seconds"] = tunnel2_rekey_margin_time_seconds
        if tunnel2_replay_window_size is not None:
            self._values["tunnel2_replay_window_size"] = tunnel2_replay_window_size
        if tunnel2_startup_action is not None:
            self._values["tunnel2_startup_action"] = tunnel2_startup_action
        if tunnel_inside_ip_version is not None:
            self._values["tunnel_inside_ip_version"] = tunnel_inside_ip_version
        if vpn_gateway_id is not None:
            self._values["vpn_gateway_id"] = vpn_gateway_id

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
    def customer_gateway_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#customer_gateway_id VpnConnection#customer_gateway_id}.'''
        result = self._values.get("customer_gateway_id")
        assert result is not None, "Required property 'customer_gateway_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#type VpnConnection#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enable_acceleration(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#enable_acceleration VpnConnection#enable_acceleration}.'''
        result = self._values.get("enable_acceleration")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#id VpnConnection#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def local_ipv4_network_cidr(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#local_ipv4_network_cidr VpnConnection#local_ipv4_network_cidr}.'''
        result = self._values.get("local_ipv4_network_cidr")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def local_ipv6_network_cidr(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#local_ipv6_network_cidr VpnConnection#local_ipv6_network_cidr}.'''
        result = self._values.get("local_ipv6_network_cidr")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def outside_ip_address_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#outside_ip_address_type VpnConnection#outside_ip_address_type}.'''
        result = self._values.get("outside_ip_address_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def remote_ipv4_network_cidr(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#remote_ipv4_network_cidr VpnConnection#remote_ipv4_network_cidr}.'''
        result = self._values.get("remote_ipv4_network_cidr")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def remote_ipv6_network_cidr(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#remote_ipv6_network_cidr VpnConnection#remote_ipv6_network_cidr}.'''
        result = self._values.get("remote_ipv6_network_cidr")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def static_routes_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#static_routes_only VpnConnection#static_routes_only}.'''
        result = self._values.get("static_routes_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tags VpnConnection#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tags_all VpnConnection#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def transit_gateway_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#transit_gateway_id VpnConnection#transit_gateway_id}.'''
        result = self._values.get("transit_gateway_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def transport_transit_gateway_attachment_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#transport_transit_gateway_attachment_id VpnConnection#transport_transit_gateway_attachment_id}.'''
        result = self._values.get("transport_transit_gateway_attachment_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tunnel1_dpd_timeout_action(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_dpd_timeout_action VpnConnection#tunnel1_dpd_timeout_action}.'''
        result = self._values.get("tunnel1_dpd_timeout_action")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tunnel1_dpd_timeout_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_dpd_timeout_seconds VpnConnection#tunnel1_dpd_timeout_seconds}.'''
        result = self._values.get("tunnel1_dpd_timeout_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tunnel1_ike_versions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_ike_versions VpnConnection#tunnel1_ike_versions}.'''
        result = self._values.get("tunnel1_ike_versions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tunnel1_inside_cidr(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_inside_cidr VpnConnection#tunnel1_inside_cidr}.'''
        result = self._values.get("tunnel1_inside_cidr")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tunnel1_inside_ipv6_cidr(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_inside_ipv6_cidr VpnConnection#tunnel1_inside_ipv6_cidr}.'''
        result = self._values.get("tunnel1_inside_ipv6_cidr")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tunnel1_log_options(self) -> typing.Optional["VpnConnectionTunnel1LogOptions"]:
        '''tunnel1_log_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_log_options VpnConnection#tunnel1_log_options}
        '''
        result = self._values.get("tunnel1_log_options")
        return typing.cast(typing.Optional["VpnConnectionTunnel1LogOptions"], result)

    @builtins.property
    def tunnel1_phase1_dh_group_numbers(
        self,
    ) -> typing.Optional[typing.List[jsii.Number]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_phase1_dh_group_numbers VpnConnection#tunnel1_phase1_dh_group_numbers}.'''
        result = self._values.get("tunnel1_phase1_dh_group_numbers")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    @builtins.property
    def tunnel1_phase1_encryption_algorithms(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_phase1_encryption_algorithms VpnConnection#tunnel1_phase1_encryption_algorithms}.'''
        result = self._values.get("tunnel1_phase1_encryption_algorithms")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tunnel1_phase1_integrity_algorithms(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_phase1_integrity_algorithms VpnConnection#tunnel1_phase1_integrity_algorithms}.'''
        result = self._values.get("tunnel1_phase1_integrity_algorithms")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tunnel1_phase1_lifetime_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_phase1_lifetime_seconds VpnConnection#tunnel1_phase1_lifetime_seconds}.'''
        result = self._values.get("tunnel1_phase1_lifetime_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tunnel1_phase2_dh_group_numbers(
        self,
    ) -> typing.Optional[typing.List[jsii.Number]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_phase2_dh_group_numbers VpnConnection#tunnel1_phase2_dh_group_numbers}.'''
        result = self._values.get("tunnel1_phase2_dh_group_numbers")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    @builtins.property
    def tunnel1_phase2_encryption_algorithms(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_phase2_encryption_algorithms VpnConnection#tunnel1_phase2_encryption_algorithms}.'''
        result = self._values.get("tunnel1_phase2_encryption_algorithms")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tunnel1_phase2_integrity_algorithms(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_phase2_integrity_algorithms VpnConnection#tunnel1_phase2_integrity_algorithms}.'''
        result = self._values.get("tunnel1_phase2_integrity_algorithms")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tunnel1_phase2_lifetime_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_phase2_lifetime_seconds VpnConnection#tunnel1_phase2_lifetime_seconds}.'''
        result = self._values.get("tunnel1_phase2_lifetime_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tunnel1_preshared_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_preshared_key VpnConnection#tunnel1_preshared_key}.'''
        result = self._values.get("tunnel1_preshared_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tunnel1_rekey_fuzz_percentage(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_rekey_fuzz_percentage VpnConnection#tunnel1_rekey_fuzz_percentage}.'''
        result = self._values.get("tunnel1_rekey_fuzz_percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tunnel1_rekey_margin_time_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_rekey_margin_time_seconds VpnConnection#tunnel1_rekey_margin_time_seconds}.'''
        result = self._values.get("tunnel1_rekey_margin_time_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tunnel1_replay_window_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_replay_window_size VpnConnection#tunnel1_replay_window_size}.'''
        result = self._values.get("tunnel1_replay_window_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tunnel1_startup_action(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_startup_action VpnConnection#tunnel1_startup_action}.'''
        result = self._values.get("tunnel1_startup_action")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tunnel2_dpd_timeout_action(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_dpd_timeout_action VpnConnection#tunnel2_dpd_timeout_action}.'''
        result = self._values.get("tunnel2_dpd_timeout_action")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tunnel2_dpd_timeout_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_dpd_timeout_seconds VpnConnection#tunnel2_dpd_timeout_seconds}.'''
        result = self._values.get("tunnel2_dpd_timeout_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tunnel2_ike_versions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_ike_versions VpnConnection#tunnel2_ike_versions}.'''
        result = self._values.get("tunnel2_ike_versions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tunnel2_inside_cidr(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_inside_cidr VpnConnection#tunnel2_inside_cidr}.'''
        result = self._values.get("tunnel2_inside_cidr")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tunnel2_inside_ipv6_cidr(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_inside_ipv6_cidr VpnConnection#tunnel2_inside_ipv6_cidr}.'''
        result = self._values.get("tunnel2_inside_ipv6_cidr")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tunnel2_log_options(self) -> typing.Optional["VpnConnectionTunnel2LogOptions"]:
        '''tunnel2_log_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_log_options VpnConnection#tunnel2_log_options}
        '''
        result = self._values.get("tunnel2_log_options")
        return typing.cast(typing.Optional["VpnConnectionTunnel2LogOptions"], result)

    @builtins.property
    def tunnel2_phase1_dh_group_numbers(
        self,
    ) -> typing.Optional[typing.List[jsii.Number]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_phase1_dh_group_numbers VpnConnection#tunnel2_phase1_dh_group_numbers}.'''
        result = self._values.get("tunnel2_phase1_dh_group_numbers")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    @builtins.property
    def tunnel2_phase1_encryption_algorithms(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_phase1_encryption_algorithms VpnConnection#tunnel2_phase1_encryption_algorithms}.'''
        result = self._values.get("tunnel2_phase1_encryption_algorithms")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tunnel2_phase1_integrity_algorithms(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_phase1_integrity_algorithms VpnConnection#tunnel2_phase1_integrity_algorithms}.'''
        result = self._values.get("tunnel2_phase1_integrity_algorithms")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tunnel2_phase1_lifetime_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_phase1_lifetime_seconds VpnConnection#tunnel2_phase1_lifetime_seconds}.'''
        result = self._values.get("tunnel2_phase1_lifetime_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tunnel2_phase2_dh_group_numbers(
        self,
    ) -> typing.Optional[typing.List[jsii.Number]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_phase2_dh_group_numbers VpnConnection#tunnel2_phase2_dh_group_numbers}.'''
        result = self._values.get("tunnel2_phase2_dh_group_numbers")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    @builtins.property
    def tunnel2_phase2_encryption_algorithms(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_phase2_encryption_algorithms VpnConnection#tunnel2_phase2_encryption_algorithms}.'''
        result = self._values.get("tunnel2_phase2_encryption_algorithms")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tunnel2_phase2_integrity_algorithms(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_phase2_integrity_algorithms VpnConnection#tunnel2_phase2_integrity_algorithms}.'''
        result = self._values.get("tunnel2_phase2_integrity_algorithms")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tunnel2_phase2_lifetime_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_phase2_lifetime_seconds VpnConnection#tunnel2_phase2_lifetime_seconds}.'''
        result = self._values.get("tunnel2_phase2_lifetime_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tunnel2_preshared_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_preshared_key VpnConnection#tunnel2_preshared_key}.'''
        result = self._values.get("tunnel2_preshared_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tunnel2_rekey_fuzz_percentage(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_rekey_fuzz_percentage VpnConnection#tunnel2_rekey_fuzz_percentage}.'''
        result = self._values.get("tunnel2_rekey_fuzz_percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tunnel2_rekey_margin_time_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_rekey_margin_time_seconds VpnConnection#tunnel2_rekey_margin_time_seconds}.'''
        result = self._values.get("tunnel2_rekey_margin_time_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tunnel2_replay_window_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_replay_window_size VpnConnection#tunnel2_replay_window_size}.'''
        result = self._values.get("tunnel2_replay_window_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tunnel2_startup_action(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_startup_action VpnConnection#tunnel2_startup_action}.'''
        result = self._values.get("tunnel2_startup_action")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tunnel_inside_ip_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel_inside_ip_version VpnConnection#tunnel_inside_ip_version}.'''
        result = self._values.get("tunnel_inside_ip_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vpn_gateway_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#vpn_gateway_id VpnConnection#vpn_gateway_id}.'''
        result = self._values.get("vpn_gateway_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VpnConnectionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.vpnConnection.VpnConnectionRoutes",
    jsii_struct_bases=[],
    name_mapping={},
)
class VpnConnectionRoutes:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VpnConnectionRoutes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VpnConnectionRoutesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.vpnConnection.VpnConnectionRoutesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4f112d55822e1fd80bfc66d47602f1e709e030a3853a053b1c7c391cfcd6734f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "VpnConnectionRoutesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19b19fb27e0136833055699673f488a6074efe04e74dc1640937a78deea1d25d)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("VpnConnectionRoutesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c415208a9cc3b7df94d679f8d1a7832fd52fa716ff83068a23b141f7f7a443dd)
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
            type_hints = typing.get_type_hints(_typecheckingstub__41468a688e7ea816cbbd836a43db74c6717671adec92526e0cd8aceb69089420)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a82a8022e57ffbf312de914ee8f4d5c401b75e0a2de71d8c4f69e6763250dbf0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class VpnConnectionRoutesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.vpnConnection.VpnConnectionRoutesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cf6071a221b30146abdbd49cd5b2a1017f0429f022b4cbe5f7987a58fd67eca3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="destinationCidrBlock")
    def destination_cidr_block(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destinationCidrBlock"))

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "source"))

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[VpnConnectionRoutes]:
        return typing.cast(typing.Optional[VpnConnectionRoutes], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[VpnConnectionRoutes]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__577abee7ffb7052569fc51094b65c6ca5252a6205082345639830793e2118284)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.vpnConnection.VpnConnectionTunnel1LogOptions",
    jsii_struct_bases=[],
    name_mapping={"cloudwatch_log_options": "cloudwatchLogOptions"},
)
class VpnConnectionTunnel1LogOptions:
    def __init__(
        self,
        *,
        cloudwatch_log_options: typing.Optional[typing.Union["VpnConnectionTunnel1LogOptionsCloudwatchLogOptions", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param cloudwatch_log_options: cloudwatch_log_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#cloudwatch_log_options VpnConnection#cloudwatch_log_options}
        '''
        if isinstance(cloudwatch_log_options, dict):
            cloudwatch_log_options = VpnConnectionTunnel1LogOptionsCloudwatchLogOptions(**cloudwatch_log_options)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad226062cb5f2360619d38d86ac80880f423709fd16786760ebc5e2180c25cb3)
            check_type(argname="argument cloudwatch_log_options", value=cloudwatch_log_options, expected_type=type_hints["cloudwatch_log_options"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if cloudwatch_log_options is not None:
            self._values["cloudwatch_log_options"] = cloudwatch_log_options

    @builtins.property
    def cloudwatch_log_options(
        self,
    ) -> typing.Optional["VpnConnectionTunnel1LogOptionsCloudwatchLogOptions"]:
        '''cloudwatch_log_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#cloudwatch_log_options VpnConnection#cloudwatch_log_options}
        '''
        result = self._values.get("cloudwatch_log_options")
        return typing.cast(typing.Optional["VpnConnectionTunnel1LogOptionsCloudwatchLogOptions"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VpnConnectionTunnel1LogOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.vpnConnection.VpnConnectionTunnel1LogOptionsCloudwatchLogOptions",
    jsii_struct_bases=[],
    name_mapping={
        "log_enabled": "logEnabled",
        "log_group_arn": "logGroupArn",
        "log_output_format": "logOutputFormat",
    },
)
class VpnConnectionTunnel1LogOptionsCloudwatchLogOptions:
    def __init__(
        self,
        *,
        log_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        log_group_arn: typing.Optional[builtins.str] = None,
        log_output_format: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param log_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#log_enabled VpnConnection#log_enabled}.
        :param log_group_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#log_group_arn VpnConnection#log_group_arn}.
        :param log_output_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#log_output_format VpnConnection#log_output_format}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__615738bc50ccdde8055ee1071c24502001419466689245894b3437d64ca1bcdf)
            check_type(argname="argument log_enabled", value=log_enabled, expected_type=type_hints["log_enabled"])
            check_type(argname="argument log_group_arn", value=log_group_arn, expected_type=type_hints["log_group_arn"])
            check_type(argname="argument log_output_format", value=log_output_format, expected_type=type_hints["log_output_format"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if log_enabled is not None:
            self._values["log_enabled"] = log_enabled
        if log_group_arn is not None:
            self._values["log_group_arn"] = log_group_arn
        if log_output_format is not None:
            self._values["log_output_format"] = log_output_format

    @builtins.property
    def log_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#log_enabled VpnConnection#log_enabled}.'''
        result = self._values.get("log_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def log_group_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#log_group_arn VpnConnection#log_group_arn}.'''
        result = self._values.get("log_group_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_output_format(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#log_output_format VpnConnection#log_output_format}.'''
        result = self._values.get("log_output_format")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VpnConnectionTunnel1LogOptionsCloudwatchLogOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VpnConnectionTunnel1LogOptionsCloudwatchLogOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.vpnConnection.VpnConnectionTunnel1LogOptionsCloudwatchLogOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__bb3bc94ec3d2d20081633b98aa994a752cf46fc1c4a03a0db976948851a9d959)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetLogEnabled")
    def reset_log_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogEnabled", []))

    @jsii.member(jsii_name="resetLogGroupArn")
    def reset_log_group_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogGroupArn", []))

    @jsii.member(jsii_name="resetLogOutputFormat")
    def reset_log_output_format(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogOutputFormat", []))

    @builtins.property
    @jsii.member(jsii_name="logEnabledInput")
    def log_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "logEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="logGroupArnInput")
    def log_group_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logGroupArnInput"))

    @builtins.property
    @jsii.member(jsii_name="logOutputFormatInput")
    def log_output_format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logOutputFormatInput"))

    @builtins.property
    @jsii.member(jsii_name="logEnabled")
    def log_enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "logEnabled"))

    @log_enabled.setter
    def log_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd830e6e66ca0f0c9dd211047683147f2c2075ced5bbeb4958229385703a707f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="logGroupArn")
    def log_group_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logGroupArn"))

    @log_group_arn.setter
    def log_group_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9dbf9c5e179a1a90f2b1d5a9ff6f766331fdb283818aaf8f511be359feeb660)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logGroupArn", value)

    @builtins.property
    @jsii.member(jsii_name="logOutputFormat")
    def log_output_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logOutputFormat"))

    @log_output_format.setter
    def log_output_format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5529f42d1d9b18543d244d7808d210a49a7b06248ef8f8c90ad02c8ea9476c50)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logOutputFormat", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[VpnConnectionTunnel1LogOptionsCloudwatchLogOptions]:
        return typing.cast(typing.Optional[VpnConnectionTunnel1LogOptionsCloudwatchLogOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[VpnConnectionTunnel1LogOptionsCloudwatchLogOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d75d054f1ede6164e87165539d335c2dc37855d36dbac747b949a0d4157ec1bb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class VpnConnectionTunnel1LogOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.vpnConnection.VpnConnectionTunnel1LogOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__88baa6f0425bb8d11569092108daf786a4ddeba3d3a511e2a05fc21d2e726ae3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCloudwatchLogOptions")
    def put_cloudwatch_log_options(
        self,
        *,
        log_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        log_group_arn: typing.Optional[builtins.str] = None,
        log_output_format: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param log_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#log_enabled VpnConnection#log_enabled}.
        :param log_group_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#log_group_arn VpnConnection#log_group_arn}.
        :param log_output_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#log_output_format VpnConnection#log_output_format}.
        '''
        value = VpnConnectionTunnel1LogOptionsCloudwatchLogOptions(
            log_enabled=log_enabled,
            log_group_arn=log_group_arn,
            log_output_format=log_output_format,
        )

        return typing.cast(None, jsii.invoke(self, "putCloudwatchLogOptions", [value]))

    @jsii.member(jsii_name="resetCloudwatchLogOptions")
    def reset_cloudwatch_log_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudwatchLogOptions", []))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchLogOptions")
    def cloudwatch_log_options(
        self,
    ) -> VpnConnectionTunnel1LogOptionsCloudwatchLogOptionsOutputReference:
        return typing.cast(VpnConnectionTunnel1LogOptionsCloudwatchLogOptionsOutputReference, jsii.get(self, "cloudwatchLogOptions"))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchLogOptionsInput")
    def cloudwatch_log_options_input(
        self,
    ) -> typing.Optional[VpnConnectionTunnel1LogOptionsCloudwatchLogOptions]:
        return typing.cast(typing.Optional[VpnConnectionTunnel1LogOptionsCloudwatchLogOptions], jsii.get(self, "cloudwatchLogOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[VpnConnectionTunnel1LogOptions]:
        return typing.cast(typing.Optional[VpnConnectionTunnel1LogOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[VpnConnectionTunnel1LogOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4ab5beb0756709b684ded94369b6b1d97c903de2cbb71d1926b3d680046518c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.vpnConnection.VpnConnectionTunnel2LogOptions",
    jsii_struct_bases=[],
    name_mapping={"cloudwatch_log_options": "cloudwatchLogOptions"},
)
class VpnConnectionTunnel2LogOptions:
    def __init__(
        self,
        *,
        cloudwatch_log_options: typing.Optional[typing.Union["VpnConnectionTunnel2LogOptionsCloudwatchLogOptions", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param cloudwatch_log_options: cloudwatch_log_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#cloudwatch_log_options VpnConnection#cloudwatch_log_options}
        '''
        if isinstance(cloudwatch_log_options, dict):
            cloudwatch_log_options = VpnConnectionTunnel2LogOptionsCloudwatchLogOptions(**cloudwatch_log_options)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__178deaca308ca8f35bc7d0065b24d50873026c9e81477fff2f4ffdb087aa8dba)
            check_type(argname="argument cloudwatch_log_options", value=cloudwatch_log_options, expected_type=type_hints["cloudwatch_log_options"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if cloudwatch_log_options is not None:
            self._values["cloudwatch_log_options"] = cloudwatch_log_options

    @builtins.property
    def cloudwatch_log_options(
        self,
    ) -> typing.Optional["VpnConnectionTunnel2LogOptionsCloudwatchLogOptions"]:
        '''cloudwatch_log_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#cloudwatch_log_options VpnConnection#cloudwatch_log_options}
        '''
        result = self._values.get("cloudwatch_log_options")
        return typing.cast(typing.Optional["VpnConnectionTunnel2LogOptionsCloudwatchLogOptions"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VpnConnectionTunnel2LogOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.vpnConnection.VpnConnectionTunnel2LogOptionsCloudwatchLogOptions",
    jsii_struct_bases=[],
    name_mapping={
        "log_enabled": "logEnabled",
        "log_group_arn": "logGroupArn",
        "log_output_format": "logOutputFormat",
    },
)
class VpnConnectionTunnel2LogOptionsCloudwatchLogOptions:
    def __init__(
        self,
        *,
        log_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        log_group_arn: typing.Optional[builtins.str] = None,
        log_output_format: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param log_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#log_enabled VpnConnection#log_enabled}.
        :param log_group_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#log_group_arn VpnConnection#log_group_arn}.
        :param log_output_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#log_output_format VpnConnection#log_output_format}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c20e9be4049e94c72e39df92a6874c2454c8c3c33dc470bdf06d7ee3e12b642d)
            check_type(argname="argument log_enabled", value=log_enabled, expected_type=type_hints["log_enabled"])
            check_type(argname="argument log_group_arn", value=log_group_arn, expected_type=type_hints["log_group_arn"])
            check_type(argname="argument log_output_format", value=log_output_format, expected_type=type_hints["log_output_format"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if log_enabled is not None:
            self._values["log_enabled"] = log_enabled
        if log_group_arn is not None:
            self._values["log_group_arn"] = log_group_arn
        if log_output_format is not None:
            self._values["log_output_format"] = log_output_format

    @builtins.property
    def log_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#log_enabled VpnConnection#log_enabled}.'''
        result = self._values.get("log_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def log_group_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#log_group_arn VpnConnection#log_group_arn}.'''
        result = self._values.get("log_group_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_output_format(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#log_output_format VpnConnection#log_output_format}.'''
        result = self._values.get("log_output_format")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VpnConnectionTunnel2LogOptionsCloudwatchLogOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VpnConnectionTunnel2LogOptionsCloudwatchLogOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.vpnConnection.VpnConnectionTunnel2LogOptionsCloudwatchLogOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ee321aff7651179c4b2ab0e172061a152b70896dbd417cf3e7325a6903141bfb)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetLogEnabled")
    def reset_log_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogEnabled", []))

    @jsii.member(jsii_name="resetLogGroupArn")
    def reset_log_group_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogGroupArn", []))

    @jsii.member(jsii_name="resetLogOutputFormat")
    def reset_log_output_format(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogOutputFormat", []))

    @builtins.property
    @jsii.member(jsii_name="logEnabledInput")
    def log_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "logEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="logGroupArnInput")
    def log_group_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logGroupArnInput"))

    @builtins.property
    @jsii.member(jsii_name="logOutputFormatInput")
    def log_output_format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logOutputFormatInput"))

    @builtins.property
    @jsii.member(jsii_name="logEnabled")
    def log_enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "logEnabled"))

    @log_enabled.setter
    def log_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1c8769ba88250fbe787a5e8d2c9d53d3295cc31f544062c1d529556b32d41a3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="logGroupArn")
    def log_group_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logGroupArn"))

    @log_group_arn.setter
    def log_group_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ebd75e3951d9b1fe5b8915d850d3757de78221f9004ef7afbf84251402494794)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logGroupArn", value)

    @builtins.property
    @jsii.member(jsii_name="logOutputFormat")
    def log_output_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logOutputFormat"))

    @log_output_format.setter
    def log_output_format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7dd004c250028111ce78d75c8e161d7747b82652e6d90b9ddf1cbd4a8d1ce87d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logOutputFormat", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[VpnConnectionTunnel2LogOptionsCloudwatchLogOptions]:
        return typing.cast(typing.Optional[VpnConnectionTunnel2LogOptionsCloudwatchLogOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[VpnConnectionTunnel2LogOptionsCloudwatchLogOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38ae759d931a4f70a1e65cb1a6e0603594e81587f8addbb437c6bace49d963de)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class VpnConnectionTunnel2LogOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.vpnConnection.VpnConnectionTunnel2LogOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a370c8d62a4e3a8e87cff84a4d1c7577a36e7c60ead1e396553dc7fd510d93c7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCloudwatchLogOptions")
    def put_cloudwatch_log_options(
        self,
        *,
        log_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        log_group_arn: typing.Optional[builtins.str] = None,
        log_output_format: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param log_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#log_enabled VpnConnection#log_enabled}.
        :param log_group_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#log_group_arn VpnConnection#log_group_arn}.
        :param log_output_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#log_output_format VpnConnection#log_output_format}.
        '''
        value = VpnConnectionTunnel2LogOptionsCloudwatchLogOptions(
            log_enabled=log_enabled,
            log_group_arn=log_group_arn,
            log_output_format=log_output_format,
        )

        return typing.cast(None, jsii.invoke(self, "putCloudwatchLogOptions", [value]))

    @jsii.member(jsii_name="resetCloudwatchLogOptions")
    def reset_cloudwatch_log_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudwatchLogOptions", []))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchLogOptions")
    def cloudwatch_log_options(
        self,
    ) -> VpnConnectionTunnel2LogOptionsCloudwatchLogOptionsOutputReference:
        return typing.cast(VpnConnectionTunnel2LogOptionsCloudwatchLogOptionsOutputReference, jsii.get(self, "cloudwatchLogOptions"))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchLogOptionsInput")
    def cloudwatch_log_options_input(
        self,
    ) -> typing.Optional[VpnConnectionTunnel2LogOptionsCloudwatchLogOptions]:
        return typing.cast(typing.Optional[VpnConnectionTunnel2LogOptionsCloudwatchLogOptions], jsii.get(self, "cloudwatchLogOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[VpnConnectionTunnel2LogOptions]:
        return typing.cast(typing.Optional[VpnConnectionTunnel2LogOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[VpnConnectionTunnel2LogOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7462c9235dff68626c7b7f253944ea03534c8eeff7f4b5c919a828c4e4c14a3c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.vpnConnection.VpnConnectionVgwTelemetry",
    jsii_struct_bases=[],
    name_mapping={},
)
class VpnConnectionVgwTelemetry:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VpnConnectionVgwTelemetry(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VpnConnectionVgwTelemetryList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.vpnConnection.VpnConnectionVgwTelemetryList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ffed9fe6a41a3b664f5cc4ce34743509dc17fd1a46a506bc862b01345321d5c4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "VpnConnectionVgwTelemetryOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b521ffd4aa488511333ba0dd103340ca0d335729fc4aae57ae114b150d1c6bd)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("VpnConnectionVgwTelemetryOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bcff1c15e6fe00489a86a9fcd9e0aaa00b9a5a04baf88a3e6d5fbf15e03335af)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2e8aa0e6d4ab4363f6ade918ad6ecd6468944b00502cb931d3fd3b681677cc84)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f3af3bf74914174437ce47ac2d66fedc8ca6a3ca9aaf2d1e97d788bae533bd67)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class VpnConnectionVgwTelemetryOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.vpnConnection.VpnConnectionVgwTelemetryOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9b6554da44df061c8686e53341da9e16b5294e29c7bb6794e1ec610dd1fe06ff)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="acceptedRouteCount")
    def accepted_route_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "acceptedRouteCount"))

    @builtins.property
    @jsii.member(jsii_name="certificateArn")
    def certificate_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateArn"))

    @builtins.property
    @jsii.member(jsii_name="lastStatusChange")
    def last_status_change(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastStatusChange"))

    @builtins.property
    @jsii.member(jsii_name="outsideIpAddress")
    def outside_ip_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "outsideIpAddress"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="statusMessage")
    def status_message(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "statusMessage"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[VpnConnectionVgwTelemetry]:
        return typing.cast(typing.Optional[VpnConnectionVgwTelemetry], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[VpnConnectionVgwTelemetry]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e04818460dddc79e6c5e4ffd3c550c5374c237d5b769a72903c4e4419da85de9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "VpnConnection",
    "VpnConnectionConfig",
    "VpnConnectionRoutes",
    "VpnConnectionRoutesList",
    "VpnConnectionRoutesOutputReference",
    "VpnConnectionTunnel1LogOptions",
    "VpnConnectionTunnel1LogOptionsCloudwatchLogOptions",
    "VpnConnectionTunnel1LogOptionsCloudwatchLogOptionsOutputReference",
    "VpnConnectionTunnel1LogOptionsOutputReference",
    "VpnConnectionTunnel2LogOptions",
    "VpnConnectionTunnel2LogOptionsCloudwatchLogOptions",
    "VpnConnectionTunnel2LogOptionsCloudwatchLogOptionsOutputReference",
    "VpnConnectionTunnel2LogOptionsOutputReference",
    "VpnConnectionVgwTelemetry",
    "VpnConnectionVgwTelemetryList",
    "VpnConnectionVgwTelemetryOutputReference",
]

publication.publish()

def _typecheckingstub__7be62f7a12ef9cca95b6db621ab4092170cd6ada5fa01e8aa445cc07c7ef2e36(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    customer_gateway_id: builtins.str,
    type: builtins.str,
    enable_acceleration: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    local_ipv4_network_cidr: typing.Optional[builtins.str] = None,
    local_ipv6_network_cidr: typing.Optional[builtins.str] = None,
    outside_ip_address_type: typing.Optional[builtins.str] = None,
    remote_ipv4_network_cidr: typing.Optional[builtins.str] = None,
    remote_ipv6_network_cidr: typing.Optional[builtins.str] = None,
    static_routes_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    transit_gateway_id: typing.Optional[builtins.str] = None,
    transport_transit_gateway_attachment_id: typing.Optional[builtins.str] = None,
    tunnel1_dpd_timeout_action: typing.Optional[builtins.str] = None,
    tunnel1_dpd_timeout_seconds: typing.Optional[jsii.Number] = None,
    tunnel1_ike_versions: typing.Optional[typing.Sequence[builtins.str]] = None,
    tunnel1_inside_cidr: typing.Optional[builtins.str] = None,
    tunnel1_inside_ipv6_cidr: typing.Optional[builtins.str] = None,
    tunnel1_log_options: typing.Optional[typing.Union[VpnConnectionTunnel1LogOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    tunnel1_phase1_dh_group_numbers: typing.Optional[typing.Sequence[jsii.Number]] = None,
    tunnel1_phase1_encryption_algorithms: typing.Optional[typing.Sequence[builtins.str]] = None,
    tunnel1_phase1_integrity_algorithms: typing.Optional[typing.Sequence[builtins.str]] = None,
    tunnel1_phase1_lifetime_seconds: typing.Optional[jsii.Number] = None,
    tunnel1_phase2_dh_group_numbers: typing.Optional[typing.Sequence[jsii.Number]] = None,
    tunnel1_phase2_encryption_algorithms: typing.Optional[typing.Sequence[builtins.str]] = None,
    tunnel1_phase2_integrity_algorithms: typing.Optional[typing.Sequence[builtins.str]] = None,
    tunnel1_phase2_lifetime_seconds: typing.Optional[jsii.Number] = None,
    tunnel1_preshared_key: typing.Optional[builtins.str] = None,
    tunnel1_rekey_fuzz_percentage: typing.Optional[jsii.Number] = None,
    tunnel1_rekey_margin_time_seconds: typing.Optional[jsii.Number] = None,
    tunnel1_replay_window_size: typing.Optional[jsii.Number] = None,
    tunnel1_startup_action: typing.Optional[builtins.str] = None,
    tunnel2_dpd_timeout_action: typing.Optional[builtins.str] = None,
    tunnel2_dpd_timeout_seconds: typing.Optional[jsii.Number] = None,
    tunnel2_ike_versions: typing.Optional[typing.Sequence[builtins.str]] = None,
    tunnel2_inside_cidr: typing.Optional[builtins.str] = None,
    tunnel2_inside_ipv6_cidr: typing.Optional[builtins.str] = None,
    tunnel2_log_options: typing.Optional[typing.Union[VpnConnectionTunnel2LogOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    tunnel2_phase1_dh_group_numbers: typing.Optional[typing.Sequence[jsii.Number]] = None,
    tunnel2_phase1_encryption_algorithms: typing.Optional[typing.Sequence[builtins.str]] = None,
    tunnel2_phase1_integrity_algorithms: typing.Optional[typing.Sequence[builtins.str]] = None,
    tunnel2_phase1_lifetime_seconds: typing.Optional[jsii.Number] = None,
    tunnel2_phase2_dh_group_numbers: typing.Optional[typing.Sequence[jsii.Number]] = None,
    tunnel2_phase2_encryption_algorithms: typing.Optional[typing.Sequence[builtins.str]] = None,
    tunnel2_phase2_integrity_algorithms: typing.Optional[typing.Sequence[builtins.str]] = None,
    tunnel2_phase2_lifetime_seconds: typing.Optional[jsii.Number] = None,
    tunnel2_preshared_key: typing.Optional[builtins.str] = None,
    tunnel2_rekey_fuzz_percentage: typing.Optional[jsii.Number] = None,
    tunnel2_rekey_margin_time_seconds: typing.Optional[jsii.Number] = None,
    tunnel2_replay_window_size: typing.Optional[jsii.Number] = None,
    tunnel2_startup_action: typing.Optional[builtins.str] = None,
    tunnel_inside_ip_version: typing.Optional[builtins.str] = None,
    vpn_gateway_id: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__d6bfd1511e4b29f207a98220d44aacd3d26da23db8f17538231b149d91ff6033(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9127334e429ef407ddbe02246a42f66d3be24b78c51e6c9e7ebc4e7d0dbcbda9(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2b93b0f8d4f693cc8f21f3c8c72a86285d65448324383d411fad4a38e8ff0c8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6cd8faf5fa50c111a3847bd04a778c3c415102bd5df94bac9bac99141144b727(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d94f92231963bc89f8225e9635c524f940a0b53a113a29d1adfff1c5d517632e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__899fb965bce16dfde63bcee942cdcd1a253f88cc477eb1c7795886ed41d19369(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38a4762d396e4738755286247b3d53c1bb1b6bececfe5aa0b997f35e4106b871(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__151ecee5376b5f1a092e433e3f29696f8e509bc8d5522f26a38643bf6a4a9c03(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d58f22b3932203aa8a8ab2add7fface8e5690cfe05d464be1ad412c6b9cfe52(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9daa7a058bac94e78e25a6d0889b2bd9fb8b257adf7b900dcfddaca77ff3ec3(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60b72bc5357d96870ad0b46d24188ff321bbebfdd9425ab5a536f1b02d4dbfbe(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c80ba96081f031e7831a35e984541394b4d600cebcdd5e6589d23895c5c8ae68(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cbaf33621f33415167aa4b52d6202bd0b60e66fbe6e63f7b82be999e538832e3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29acec0673c7baabefeb7d1c522bc01a393183974a7b05ff5360698b3039de2a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18c2d086d72ea0d1fdaad5a8ed63b4a740691a1ebd341fe2832aea109d5c56f1(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c14380765a8016c6822dc837d5fc568fe40fecb513503188054cb2782cdde47(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f3b4c375dcb9d7373078310b87debe1c34fb900eb506c4f2286fef60834df46(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70a362885e4ca68915e4a3457e5d6689df213ee1739bd54346476f3a84984f30(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__adacadebf5035261db93e0430865347cfcb9837bd68282cbde04d48c7eaa553a(
    value: typing.List[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c201028791245fdd30db3c44e05d909bb1553785c6b265c321d2b99ddc6e81e5(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61294bd545aaa272c0ee06494090a0cbf9a1a75fbf6967c17e2aabe3f0bd99d8(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7c735335a1b0d70b380007c85d3e66d8af635b2e8bd0c3dd7c37bb384b67c21(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b399bc6a6d99016f9651926032377edde62af435a8439361526f5256919581a2(
    value: typing.List[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b69610665e422eadd8ef42f40cd6002b3e245c65d933d6a0c0be482601569a75(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0bbe722f6bbac073cd3743150a073d7e070d87a3bee5280c56c0822d5e397bac(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8380952122a02891c0d83af24234b36f65f3394e363c07c0c4b95e8cf0e180c(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0abcfa1ebf9eebe6827496611dd0f853fe95b843115b85b5c7be04bf8121e6ac(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb8dd4cfd093b4ecd6731c756aadd3329d5d6cbd3a63c3bab906d33c2d8c3d50(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__721bbda036a39be1425bc421a970aaaf550ba4a8181aec41338a3183463c0735(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e7b42e497a2bdb48704843070fb64c5b3ddec65f68f37d95f1d8ea7893dcfde(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31a48077527a9ec9b33b36b2c28f388a8584aa9f06353858247d2ce3079c9f34(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fde2a31ac9ee3fd1008dc5c669a41e598362453b1c835bfaed8fe99e0af25a9c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60d427c94c279349b8e79a2de7f25290a6ca26acf17502e25dc094c6ab9a641e(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c5855f491eb6a7c0c51029215749eb3875e081f9cfa7a5e36da0c83a7a1fb63(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9f8db832f7bef9582aaec012f27617cbab68be99d1924f4fc20d94c56dfc99e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d91dd11aa46be5cf232e4d8cfda5a22e2bfa1af2b7095af1b1d265ee5d0a482b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__486905d4b259c578f9b403caa928bd0088a178e20e34938592950e1243950b49(
    value: typing.List[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb4459090b916a5ee529b1043e20aa725ecf13b76eb1163f891ad5eafe6286c2(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f06e3a2d1e444e884ac55ee556abfa582d0d98855c702dbd6cdba74ebb8517a(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__262d9466750aebc1a2de3c7bec4563cb57d458fc88d70164a905985f34c9049c(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__faa7d37c5977b283fe60cc7fcc55e3c7c46686963253ecf95bceacdb2b299abb(
    value: typing.List[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d78286e6e5256508132f950ca5d3233e0ac5115e05e785d493c3342635a312eb(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3cf09c43b618be20a9419b2e992a05d6f6933637dcc6066a3e17945de51d9c4(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2fd664268b2376ace72f5e71c66f12522e83d1d35836cb06704ebcc73646be16(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8924119467b45580d97808647a058f9c675c4cdad4db4d0646ca30ec8679246d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8064330a0fca896c02552d73d690fff8d635f00235fea74462a47971568d6ee3(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78a0e4ee1b7f1e36c3b648937030b559dd6921b800c6d82b3f990a499ca8a4f3(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5426ccfd75015845356983450a9243d2d3fc44fe8036f6cb112ca62f644806f(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__643c8fc7c3263a421f9fdfbbe887566a58a81c162e209e14a3b527993978578a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5204f7727a09104fcaa8f2e85ae0f253aad609450567f6e087306b97b49c2627(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d54960b533163e297d271f030743b91635b6588c84ba14e52822dccf9505484(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51778d06553e52be5a32a7d52d194d975360c3b723b4c91ac7db503fe9320bbf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a94768fd856d3f11ad4339d86c6bd005579eafe549e0970427a7101c862d90bd(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    customer_gateway_id: builtins.str,
    type: builtins.str,
    enable_acceleration: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    local_ipv4_network_cidr: typing.Optional[builtins.str] = None,
    local_ipv6_network_cidr: typing.Optional[builtins.str] = None,
    outside_ip_address_type: typing.Optional[builtins.str] = None,
    remote_ipv4_network_cidr: typing.Optional[builtins.str] = None,
    remote_ipv6_network_cidr: typing.Optional[builtins.str] = None,
    static_routes_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    transit_gateway_id: typing.Optional[builtins.str] = None,
    transport_transit_gateway_attachment_id: typing.Optional[builtins.str] = None,
    tunnel1_dpd_timeout_action: typing.Optional[builtins.str] = None,
    tunnel1_dpd_timeout_seconds: typing.Optional[jsii.Number] = None,
    tunnel1_ike_versions: typing.Optional[typing.Sequence[builtins.str]] = None,
    tunnel1_inside_cidr: typing.Optional[builtins.str] = None,
    tunnel1_inside_ipv6_cidr: typing.Optional[builtins.str] = None,
    tunnel1_log_options: typing.Optional[typing.Union[VpnConnectionTunnel1LogOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    tunnel1_phase1_dh_group_numbers: typing.Optional[typing.Sequence[jsii.Number]] = None,
    tunnel1_phase1_encryption_algorithms: typing.Optional[typing.Sequence[builtins.str]] = None,
    tunnel1_phase1_integrity_algorithms: typing.Optional[typing.Sequence[builtins.str]] = None,
    tunnel1_phase1_lifetime_seconds: typing.Optional[jsii.Number] = None,
    tunnel1_phase2_dh_group_numbers: typing.Optional[typing.Sequence[jsii.Number]] = None,
    tunnel1_phase2_encryption_algorithms: typing.Optional[typing.Sequence[builtins.str]] = None,
    tunnel1_phase2_integrity_algorithms: typing.Optional[typing.Sequence[builtins.str]] = None,
    tunnel1_phase2_lifetime_seconds: typing.Optional[jsii.Number] = None,
    tunnel1_preshared_key: typing.Optional[builtins.str] = None,
    tunnel1_rekey_fuzz_percentage: typing.Optional[jsii.Number] = None,
    tunnel1_rekey_margin_time_seconds: typing.Optional[jsii.Number] = None,
    tunnel1_replay_window_size: typing.Optional[jsii.Number] = None,
    tunnel1_startup_action: typing.Optional[builtins.str] = None,
    tunnel2_dpd_timeout_action: typing.Optional[builtins.str] = None,
    tunnel2_dpd_timeout_seconds: typing.Optional[jsii.Number] = None,
    tunnel2_ike_versions: typing.Optional[typing.Sequence[builtins.str]] = None,
    tunnel2_inside_cidr: typing.Optional[builtins.str] = None,
    tunnel2_inside_ipv6_cidr: typing.Optional[builtins.str] = None,
    tunnel2_log_options: typing.Optional[typing.Union[VpnConnectionTunnel2LogOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    tunnel2_phase1_dh_group_numbers: typing.Optional[typing.Sequence[jsii.Number]] = None,
    tunnel2_phase1_encryption_algorithms: typing.Optional[typing.Sequence[builtins.str]] = None,
    tunnel2_phase1_integrity_algorithms: typing.Optional[typing.Sequence[builtins.str]] = None,
    tunnel2_phase1_lifetime_seconds: typing.Optional[jsii.Number] = None,
    tunnel2_phase2_dh_group_numbers: typing.Optional[typing.Sequence[jsii.Number]] = None,
    tunnel2_phase2_encryption_algorithms: typing.Optional[typing.Sequence[builtins.str]] = None,
    tunnel2_phase2_integrity_algorithms: typing.Optional[typing.Sequence[builtins.str]] = None,
    tunnel2_phase2_lifetime_seconds: typing.Optional[jsii.Number] = None,
    tunnel2_preshared_key: typing.Optional[builtins.str] = None,
    tunnel2_rekey_fuzz_percentage: typing.Optional[jsii.Number] = None,
    tunnel2_rekey_margin_time_seconds: typing.Optional[jsii.Number] = None,
    tunnel2_replay_window_size: typing.Optional[jsii.Number] = None,
    tunnel2_startup_action: typing.Optional[builtins.str] = None,
    tunnel_inside_ip_version: typing.Optional[builtins.str] = None,
    vpn_gateway_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f112d55822e1fd80bfc66d47602f1e709e030a3853a053b1c7c391cfcd6734f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19b19fb27e0136833055699673f488a6074efe04e74dc1640937a78deea1d25d(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c415208a9cc3b7df94d679f8d1a7832fd52fa716ff83068a23b141f7f7a443dd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41468a688e7ea816cbbd836a43db74c6717671adec92526e0cd8aceb69089420(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a82a8022e57ffbf312de914ee8f4d5c401b75e0a2de71d8c4f69e6763250dbf0(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf6071a221b30146abdbd49cd5b2a1017f0429f022b4cbe5f7987a58fd67eca3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__577abee7ffb7052569fc51094b65c6ca5252a6205082345639830793e2118284(
    value: typing.Optional[VpnConnectionRoutes],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad226062cb5f2360619d38d86ac80880f423709fd16786760ebc5e2180c25cb3(
    *,
    cloudwatch_log_options: typing.Optional[typing.Union[VpnConnectionTunnel1LogOptionsCloudwatchLogOptions, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__615738bc50ccdde8055ee1071c24502001419466689245894b3437d64ca1bcdf(
    *,
    log_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    log_group_arn: typing.Optional[builtins.str] = None,
    log_output_format: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb3bc94ec3d2d20081633b98aa994a752cf46fc1c4a03a0db976948851a9d959(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd830e6e66ca0f0c9dd211047683147f2c2075ced5bbeb4958229385703a707f(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9dbf9c5e179a1a90f2b1d5a9ff6f766331fdb283818aaf8f511be359feeb660(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5529f42d1d9b18543d244d7808d210a49a7b06248ef8f8c90ad02c8ea9476c50(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d75d054f1ede6164e87165539d335c2dc37855d36dbac747b949a0d4157ec1bb(
    value: typing.Optional[VpnConnectionTunnel1LogOptionsCloudwatchLogOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88baa6f0425bb8d11569092108daf786a4ddeba3d3a511e2a05fc21d2e726ae3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4ab5beb0756709b684ded94369b6b1d97c903de2cbb71d1926b3d680046518c(
    value: typing.Optional[VpnConnectionTunnel1LogOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__178deaca308ca8f35bc7d0065b24d50873026c9e81477fff2f4ffdb087aa8dba(
    *,
    cloudwatch_log_options: typing.Optional[typing.Union[VpnConnectionTunnel2LogOptionsCloudwatchLogOptions, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c20e9be4049e94c72e39df92a6874c2454c8c3c33dc470bdf06d7ee3e12b642d(
    *,
    log_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    log_group_arn: typing.Optional[builtins.str] = None,
    log_output_format: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee321aff7651179c4b2ab0e172061a152b70896dbd417cf3e7325a6903141bfb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1c8769ba88250fbe787a5e8d2c9d53d3295cc31f544062c1d529556b32d41a3(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ebd75e3951d9b1fe5b8915d850d3757de78221f9004ef7afbf84251402494794(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7dd004c250028111ce78d75c8e161d7747b82652e6d90b9ddf1cbd4a8d1ce87d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38ae759d931a4f70a1e65cb1a6e0603594e81587f8addbb437c6bace49d963de(
    value: typing.Optional[VpnConnectionTunnel2LogOptionsCloudwatchLogOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a370c8d62a4e3a8e87cff84a4d1c7577a36e7c60ead1e396553dc7fd510d93c7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7462c9235dff68626c7b7f253944ea03534c8eeff7f4b5c919a828c4e4c14a3c(
    value: typing.Optional[VpnConnectionTunnel2LogOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ffed9fe6a41a3b664f5cc4ce34743509dc17fd1a46a506bc862b01345321d5c4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b521ffd4aa488511333ba0dd103340ca0d335729fc4aae57ae114b150d1c6bd(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bcff1c15e6fe00489a86a9fcd9e0aaa00b9a5a04baf88a3e6d5fbf15e03335af(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e8aa0e6d4ab4363f6ade918ad6ecd6468944b00502cb931d3fd3b681677cc84(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3af3bf74914174437ce47ac2d66fedc8ca6a3ca9aaf2d1e97d788bae533bd67(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b6554da44df061c8686e53341da9e16b5294e29c7bb6794e1ec610dd1fe06ff(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e04818460dddc79e6c5e4ffd3c550c5374c237d5b769a72903c4e4419da85de9(
    value: typing.Optional[VpnConnectionVgwTelemetry],
) -> None:
    """Type checking stubs"""
    pass
