'''
# `aws_ec2_client_vpn_endpoint`

Refer to the Terraform Registory for docs: [`aws_ec2_client_vpn_endpoint`](https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint).
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


class Ec2ClientVpnEndpoint(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2ClientVpnEndpoint.Ec2ClientVpnEndpoint",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint aws_ec2_client_vpn_endpoint}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        authentication_options: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["Ec2ClientVpnEndpointAuthenticationOptions", typing.Dict[builtins.str, typing.Any]]]],
        client_cidr_block: builtins.str,
        connection_log_options: typing.Union["Ec2ClientVpnEndpointConnectionLogOptions", typing.Dict[builtins.str, typing.Any]],
        server_certificate_arn: builtins.str,
        client_connect_options: typing.Optional[typing.Union["Ec2ClientVpnEndpointClientConnectOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        client_login_banner_options: typing.Optional[typing.Union["Ec2ClientVpnEndpointClientLoginBannerOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        dns_servers: typing.Optional[typing.Sequence[builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        self_service_portal: typing.Optional[builtins.str] = None,
        session_timeout_hours: typing.Optional[jsii.Number] = None,
        split_tunnel: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        transport_protocol: typing.Optional[builtins.str] = None,
        vpc_id: typing.Optional[builtins.str] = None,
        vpn_port: typing.Optional[jsii.Number] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint aws_ec2_client_vpn_endpoint} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param authentication_options: authentication_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#authentication_options Ec2ClientVpnEndpoint#authentication_options}
        :param client_cidr_block: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#client_cidr_block Ec2ClientVpnEndpoint#client_cidr_block}.
        :param connection_log_options: connection_log_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#connection_log_options Ec2ClientVpnEndpoint#connection_log_options}
        :param server_certificate_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#server_certificate_arn Ec2ClientVpnEndpoint#server_certificate_arn}.
        :param client_connect_options: client_connect_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#client_connect_options Ec2ClientVpnEndpoint#client_connect_options}
        :param client_login_banner_options: client_login_banner_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#client_login_banner_options Ec2ClientVpnEndpoint#client_login_banner_options}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#description Ec2ClientVpnEndpoint#description}.
        :param dns_servers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#dns_servers Ec2ClientVpnEndpoint#dns_servers}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#id Ec2ClientVpnEndpoint#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#security_group_ids Ec2ClientVpnEndpoint#security_group_ids}.
        :param self_service_portal: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#self_service_portal Ec2ClientVpnEndpoint#self_service_portal}.
        :param session_timeout_hours: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#session_timeout_hours Ec2ClientVpnEndpoint#session_timeout_hours}.
        :param split_tunnel: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#split_tunnel Ec2ClientVpnEndpoint#split_tunnel}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#tags Ec2ClientVpnEndpoint#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#tags_all Ec2ClientVpnEndpoint#tags_all}.
        :param transport_protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#transport_protocol Ec2ClientVpnEndpoint#transport_protocol}.
        :param vpc_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#vpc_id Ec2ClientVpnEndpoint#vpc_id}.
        :param vpn_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#vpn_port Ec2ClientVpnEndpoint#vpn_port}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7616e1ee7003d6e747bcd3afa4e5353ab8b3d6fe5aca9120da2a241ca228d99)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = Ec2ClientVpnEndpointConfig(
            authentication_options=authentication_options,
            client_cidr_block=client_cidr_block,
            connection_log_options=connection_log_options,
            server_certificate_arn=server_certificate_arn,
            client_connect_options=client_connect_options,
            client_login_banner_options=client_login_banner_options,
            description=description,
            dns_servers=dns_servers,
            id=id,
            security_group_ids=security_group_ids,
            self_service_portal=self_service_portal,
            session_timeout_hours=session_timeout_hours,
            split_tunnel=split_tunnel,
            tags=tags,
            tags_all=tags_all,
            transport_protocol=transport_protocol,
            vpc_id=vpc_id,
            vpn_port=vpn_port,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAuthenticationOptions")
    def put_authentication_options(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["Ec2ClientVpnEndpointAuthenticationOptions", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b4f99315fdf3795a2d21d3cd80b1d97e29ddec41243400074d0e5b65c07999a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAuthenticationOptions", [value]))

    @jsii.member(jsii_name="putClientConnectOptions")
    def put_client_connect_options(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        lambda_function_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#enabled Ec2ClientVpnEndpoint#enabled}.
        :param lambda_function_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#lambda_function_arn Ec2ClientVpnEndpoint#lambda_function_arn}.
        '''
        value = Ec2ClientVpnEndpointClientConnectOptions(
            enabled=enabled, lambda_function_arn=lambda_function_arn
        )

        return typing.cast(None, jsii.invoke(self, "putClientConnectOptions", [value]))

    @jsii.member(jsii_name="putClientLoginBannerOptions")
    def put_client_login_banner_options(
        self,
        *,
        banner_text: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param banner_text: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#banner_text Ec2ClientVpnEndpoint#banner_text}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#enabled Ec2ClientVpnEndpoint#enabled}.
        '''
        value = Ec2ClientVpnEndpointClientLoginBannerOptions(
            banner_text=banner_text, enabled=enabled
        )

        return typing.cast(None, jsii.invoke(self, "putClientLoginBannerOptions", [value]))

    @jsii.member(jsii_name="putConnectionLogOptions")
    def put_connection_log_options(
        self,
        *,
        enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        cloudwatch_log_group: typing.Optional[builtins.str] = None,
        cloudwatch_log_stream: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#enabled Ec2ClientVpnEndpoint#enabled}.
        :param cloudwatch_log_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#cloudwatch_log_group Ec2ClientVpnEndpoint#cloudwatch_log_group}.
        :param cloudwatch_log_stream: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#cloudwatch_log_stream Ec2ClientVpnEndpoint#cloudwatch_log_stream}.
        '''
        value = Ec2ClientVpnEndpointConnectionLogOptions(
            enabled=enabled,
            cloudwatch_log_group=cloudwatch_log_group,
            cloudwatch_log_stream=cloudwatch_log_stream,
        )

        return typing.cast(None, jsii.invoke(self, "putConnectionLogOptions", [value]))

    @jsii.member(jsii_name="resetClientConnectOptions")
    def reset_client_connect_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientConnectOptions", []))

    @jsii.member(jsii_name="resetClientLoginBannerOptions")
    def reset_client_login_banner_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientLoginBannerOptions", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetDnsServers")
    def reset_dns_servers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDnsServers", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetSecurityGroupIds")
    def reset_security_group_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecurityGroupIds", []))

    @jsii.member(jsii_name="resetSelfServicePortal")
    def reset_self_service_portal(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSelfServicePortal", []))

    @jsii.member(jsii_name="resetSessionTimeoutHours")
    def reset_session_timeout_hours(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSessionTimeoutHours", []))

    @jsii.member(jsii_name="resetSplitTunnel")
    def reset_split_tunnel(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSplitTunnel", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetTransportProtocol")
    def reset_transport_protocol(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTransportProtocol", []))

    @jsii.member(jsii_name="resetVpcId")
    def reset_vpc_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVpcId", []))

    @jsii.member(jsii_name="resetVpnPort")
    def reset_vpn_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVpnPort", []))

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
    @jsii.member(jsii_name="authenticationOptions")
    def authentication_options(self) -> "Ec2ClientVpnEndpointAuthenticationOptionsList":
        return typing.cast("Ec2ClientVpnEndpointAuthenticationOptionsList", jsii.get(self, "authenticationOptions"))

    @builtins.property
    @jsii.member(jsii_name="clientConnectOptions")
    def client_connect_options(
        self,
    ) -> "Ec2ClientVpnEndpointClientConnectOptionsOutputReference":
        return typing.cast("Ec2ClientVpnEndpointClientConnectOptionsOutputReference", jsii.get(self, "clientConnectOptions"))

    @builtins.property
    @jsii.member(jsii_name="clientLoginBannerOptions")
    def client_login_banner_options(
        self,
    ) -> "Ec2ClientVpnEndpointClientLoginBannerOptionsOutputReference":
        return typing.cast("Ec2ClientVpnEndpointClientLoginBannerOptionsOutputReference", jsii.get(self, "clientLoginBannerOptions"))

    @builtins.property
    @jsii.member(jsii_name="connectionLogOptions")
    def connection_log_options(
        self,
    ) -> "Ec2ClientVpnEndpointConnectionLogOptionsOutputReference":
        return typing.cast("Ec2ClientVpnEndpointConnectionLogOptionsOutputReference", jsii.get(self, "connectionLogOptions"))

    @builtins.property
    @jsii.member(jsii_name="dnsName")
    def dns_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dnsName"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="authenticationOptionsInput")
    def authentication_options_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["Ec2ClientVpnEndpointAuthenticationOptions"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["Ec2ClientVpnEndpointAuthenticationOptions"]]], jsii.get(self, "authenticationOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="clientCidrBlockInput")
    def client_cidr_block_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientCidrBlockInput"))

    @builtins.property
    @jsii.member(jsii_name="clientConnectOptionsInput")
    def client_connect_options_input(
        self,
    ) -> typing.Optional["Ec2ClientVpnEndpointClientConnectOptions"]:
        return typing.cast(typing.Optional["Ec2ClientVpnEndpointClientConnectOptions"], jsii.get(self, "clientConnectOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="clientLoginBannerOptionsInput")
    def client_login_banner_options_input(
        self,
    ) -> typing.Optional["Ec2ClientVpnEndpointClientLoginBannerOptions"]:
        return typing.cast(typing.Optional["Ec2ClientVpnEndpointClientLoginBannerOptions"], jsii.get(self, "clientLoginBannerOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="connectionLogOptionsInput")
    def connection_log_options_input(
        self,
    ) -> typing.Optional["Ec2ClientVpnEndpointConnectionLogOptions"]:
        return typing.cast(typing.Optional["Ec2ClientVpnEndpointConnectionLogOptions"], jsii.get(self, "connectionLogOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="dnsServersInput")
    def dns_servers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "dnsServersInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="securityGroupIdsInput")
    def security_group_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityGroupIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="selfServicePortalInput")
    def self_service_portal_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "selfServicePortalInput"))

    @builtins.property
    @jsii.member(jsii_name="serverCertificateArnInput")
    def server_certificate_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serverCertificateArnInput"))

    @builtins.property
    @jsii.member(jsii_name="sessionTimeoutHoursInput")
    def session_timeout_hours_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sessionTimeoutHoursInput"))

    @builtins.property
    @jsii.member(jsii_name="splitTunnelInput")
    def split_tunnel_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "splitTunnelInput"))

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
    @jsii.member(jsii_name="transportProtocolInput")
    def transport_protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "transportProtocolInput"))

    @builtins.property
    @jsii.member(jsii_name="vpcIdInput")
    def vpc_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vpcIdInput"))

    @builtins.property
    @jsii.member(jsii_name="vpnPortInput")
    def vpn_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "vpnPortInput"))

    @builtins.property
    @jsii.member(jsii_name="clientCidrBlock")
    def client_cidr_block(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientCidrBlock"))

    @client_cidr_block.setter
    def client_cidr_block(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25801627a2ec2572b0f110f089cb66fa201a5215a3f8093660ce9ba10d0d5837)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientCidrBlock", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a769b5e15b1bb912b0f57e41e2f68a961000b9d690eaf96aee9058e63e607e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="dnsServers")
    def dns_servers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "dnsServers"))

    @dns_servers.setter
    def dns_servers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__acea71dc20e83b740c10dd0cf4e43047b91c5c16903f3f3d5a132d17843c3b42)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dnsServers", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1687e256e321537ca819ff1374fb22c678e613560e28b4d66437d83ce926bfd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="securityGroupIds")
    def security_group_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "securityGroupIds"))

    @security_group_ids.setter
    def security_group_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21f8cbc63e4441d37c7bafeaef5d370a51f7352092be171fc9af7d87365e7307)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroupIds", value)

    @builtins.property
    @jsii.member(jsii_name="selfServicePortal")
    def self_service_portal(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "selfServicePortal"))

    @self_service_portal.setter
    def self_service_portal(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f07f9cdde496a5c9a5e415129770456dca1dbe9acccdbba839f71fb0b429b100)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "selfServicePortal", value)

    @builtins.property
    @jsii.member(jsii_name="serverCertificateArn")
    def server_certificate_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serverCertificateArn"))

    @server_certificate_arn.setter
    def server_certificate_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c1cac72d30e73946b461d12fc2c24adcbe820216ded62b8f59676b4b099a017)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverCertificateArn", value)

    @builtins.property
    @jsii.member(jsii_name="sessionTimeoutHours")
    def session_timeout_hours(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "sessionTimeoutHours"))

    @session_timeout_hours.setter
    def session_timeout_hours(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab491f2baa6878648e5370a4749cb48ef1011f292baf398635daec9611d9e94b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sessionTimeoutHours", value)

    @builtins.property
    @jsii.member(jsii_name="splitTunnel")
    def split_tunnel(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "splitTunnel"))

    @split_tunnel.setter
    def split_tunnel(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b98af37308746c44b40bca4d053759df6cebda83f02a96a59151de320e1db97)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "splitTunnel", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a951f7969c29a188611ac9c57181326daf2654391241ec3ec817f265fa4c5efd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__48882e5374242f16946c6212cdb467468e61eb964f14c0436f9c4d94f5e2e7c8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)

    @builtins.property
    @jsii.member(jsii_name="transportProtocol")
    def transport_protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "transportProtocol"))

    @transport_protocol.setter
    def transport_protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4061a3d1339c958dc3fe7a55825a0b66b0c105175b0e5f1fe0dac7e55b104310)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "transportProtocol", value)

    @builtins.property
    @jsii.member(jsii_name="vpcId")
    def vpc_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vpcId"))

    @vpc_id.setter
    def vpc_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d90fbfac90b068c011874b0e8b39a4af5b8cbb57f75cdf18279f270081d96c9e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcId", value)

    @builtins.property
    @jsii.member(jsii_name="vpnPort")
    def vpn_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "vpnPort"))

    @vpn_port.setter
    def vpn_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c75f46336159148e7dbbe85092f98855c7a3167aa59d695ca6d0febada744914)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpnPort", value)


@jsii.data_type(
    jsii_type="aws.ec2ClientVpnEndpoint.Ec2ClientVpnEndpointAuthenticationOptions",
    jsii_struct_bases=[],
    name_mapping={
        "type": "type",
        "active_directory_id": "activeDirectoryId",
        "root_certificate_chain_arn": "rootCertificateChainArn",
        "saml_provider_arn": "samlProviderArn",
        "self_service_saml_provider_arn": "selfServiceSamlProviderArn",
    },
)
class Ec2ClientVpnEndpointAuthenticationOptions:
    def __init__(
        self,
        *,
        type: builtins.str,
        active_directory_id: typing.Optional[builtins.str] = None,
        root_certificate_chain_arn: typing.Optional[builtins.str] = None,
        saml_provider_arn: typing.Optional[builtins.str] = None,
        self_service_saml_provider_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#type Ec2ClientVpnEndpoint#type}.
        :param active_directory_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#active_directory_id Ec2ClientVpnEndpoint#active_directory_id}.
        :param root_certificate_chain_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#root_certificate_chain_arn Ec2ClientVpnEndpoint#root_certificate_chain_arn}.
        :param saml_provider_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#saml_provider_arn Ec2ClientVpnEndpoint#saml_provider_arn}.
        :param self_service_saml_provider_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#self_service_saml_provider_arn Ec2ClientVpnEndpoint#self_service_saml_provider_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1609f0c9cc07a27b9903ee86af85ac0eb107bfbaab380d9d44726083a54f3855)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument active_directory_id", value=active_directory_id, expected_type=type_hints["active_directory_id"])
            check_type(argname="argument root_certificate_chain_arn", value=root_certificate_chain_arn, expected_type=type_hints["root_certificate_chain_arn"])
            check_type(argname="argument saml_provider_arn", value=saml_provider_arn, expected_type=type_hints["saml_provider_arn"])
            check_type(argname="argument self_service_saml_provider_arn", value=self_service_saml_provider_arn, expected_type=type_hints["self_service_saml_provider_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }
        if active_directory_id is not None:
            self._values["active_directory_id"] = active_directory_id
        if root_certificate_chain_arn is not None:
            self._values["root_certificate_chain_arn"] = root_certificate_chain_arn
        if saml_provider_arn is not None:
            self._values["saml_provider_arn"] = saml_provider_arn
        if self_service_saml_provider_arn is not None:
            self._values["self_service_saml_provider_arn"] = self_service_saml_provider_arn

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#type Ec2ClientVpnEndpoint#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def active_directory_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#active_directory_id Ec2ClientVpnEndpoint#active_directory_id}.'''
        result = self._values.get("active_directory_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def root_certificate_chain_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#root_certificate_chain_arn Ec2ClientVpnEndpoint#root_certificate_chain_arn}.'''
        result = self._values.get("root_certificate_chain_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def saml_provider_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#saml_provider_arn Ec2ClientVpnEndpoint#saml_provider_arn}.'''
        result = self._values.get("saml_provider_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def self_service_saml_provider_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#self_service_saml_provider_arn Ec2ClientVpnEndpoint#self_service_saml_provider_arn}.'''
        result = self._values.get("self_service_saml_provider_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2ClientVpnEndpointAuthenticationOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Ec2ClientVpnEndpointAuthenticationOptionsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2ClientVpnEndpoint.Ec2ClientVpnEndpointAuthenticationOptionsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5ca29f65bc9ae991d19617b54660d1f1f954ba5c27021a7303030bcd2ccd39ca)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2ClientVpnEndpointAuthenticationOptionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c77ce619fe48fca294a747ebdebd14f69bf716e0dadc7e64afd475e416db2db)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2ClientVpnEndpointAuthenticationOptionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8929bd90a92e7aca9ae4bc2721527f9619cdfe817d324593784067c424128ebd)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b308b8052bb47525b0eab25ee26f1d05e9262fbf54397f49e5b50d6d779a8eb4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e230b5de12373019a7db589c22ae1acb83d708a5829cab8c1d78f84b78bfcafb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Ec2ClientVpnEndpointAuthenticationOptions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Ec2ClientVpnEndpointAuthenticationOptions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Ec2ClientVpnEndpointAuthenticationOptions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c8683e5be76297f2a87eb6622131eecd534cda02f3529af489397f45502f60f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Ec2ClientVpnEndpointAuthenticationOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2ClientVpnEndpoint.Ec2ClientVpnEndpointAuthenticationOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c7caffd7346293a6a44f8bf306a15467f817561a5bce17d4c330c825e1233daf)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetActiveDirectoryId")
    def reset_active_directory_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetActiveDirectoryId", []))

    @jsii.member(jsii_name="resetRootCertificateChainArn")
    def reset_root_certificate_chain_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRootCertificateChainArn", []))

    @jsii.member(jsii_name="resetSamlProviderArn")
    def reset_saml_provider_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSamlProviderArn", []))

    @jsii.member(jsii_name="resetSelfServiceSamlProviderArn")
    def reset_self_service_saml_provider_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSelfServiceSamlProviderArn", []))

    @builtins.property
    @jsii.member(jsii_name="activeDirectoryIdInput")
    def active_directory_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "activeDirectoryIdInput"))

    @builtins.property
    @jsii.member(jsii_name="rootCertificateChainArnInput")
    def root_certificate_chain_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rootCertificateChainArnInput"))

    @builtins.property
    @jsii.member(jsii_name="samlProviderArnInput")
    def saml_provider_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "samlProviderArnInput"))

    @builtins.property
    @jsii.member(jsii_name="selfServiceSamlProviderArnInput")
    def self_service_saml_provider_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "selfServiceSamlProviderArnInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="activeDirectoryId")
    def active_directory_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "activeDirectoryId"))

    @active_directory_id.setter
    def active_directory_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f208584389510e4da3c5f0582e0fff0d97b167ca508d398d754050bba05e4f9f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "activeDirectoryId", value)

    @builtins.property
    @jsii.member(jsii_name="rootCertificateChainArn")
    def root_certificate_chain_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rootCertificateChainArn"))

    @root_certificate_chain_arn.setter
    def root_certificate_chain_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e60189e3a74d2a7252e7b0e9ede691127f731a6d9d8e3d471b274f72b601a13)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rootCertificateChainArn", value)

    @builtins.property
    @jsii.member(jsii_name="samlProviderArn")
    def saml_provider_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "samlProviderArn"))

    @saml_provider_arn.setter
    def saml_provider_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c031dc398ad4bb50d164c0804b446b7bb356589aee5565abe9a181262a48065a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "samlProviderArn", value)

    @builtins.property
    @jsii.member(jsii_name="selfServiceSamlProviderArn")
    def self_service_saml_provider_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "selfServiceSamlProviderArn"))

    @self_service_saml_provider_arn.setter
    def self_service_saml_provider_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__86b6e1fc4a852b13acb7203bdf338727e874004b80237cca7f24aa4bcf6ef7fb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "selfServiceSamlProviderArn", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45eec6c71b6341a91f268d3b1a9a1312846e363666dc4bb585b2697109c3c9b3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[Ec2ClientVpnEndpointAuthenticationOptions, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[Ec2ClientVpnEndpointAuthenticationOptions, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[Ec2ClientVpnEndpointAuthenticationOptions, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f96229bd09e86b2364a5710b11d48c9841b82456941d99b01d4659f802b6d879)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ec2ClientVpnEndpoint.Ec2ClientVpnEndpointClientConnectOptions",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "lambda_function_arn": "lambdaFunctionArn"},
)
class Ec2ClientVpnEndpointClientConnectOptions:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        lambda_function_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#enabled Ec2ClientVpnEndpoint#enabled}.
        :param lambda_function_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#lambda_function_arn Ec2ClientVpnEndpoint#lambda_function_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21f7c4e5e6c74f755a0376741fcf92709c8a5bb7996d283af44bbb55cd44c736)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument lambda_function_arn", value=lambda_function_arn, expected_type=type_hints["lambda_function_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled
        if lambda_function_arn is not None:
            self._values["lambda_function_arn"] = lambda_function_arn

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#enabled Ec2ClientVpnEndpoint#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def lambda_function_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#lambda_function_arn Ec2ClientVpnEndpoint#lambda_function_arn}.'''
        result = self._values.get("lambda_function_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2ClientVpnEndpointClientConnectOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Ec2ClientVpnEndpointClientConnectOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2ClientVpnEndpoint.Ec2ClientVpnEndpointClientConnectOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__32611838a4db95ac4cca7872f4a9d0e4fe52449049c92d9213ac9f6ad81ef8e7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetLambdaFunctionArn")
    def reset_lambda_function_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLambdaFunctionArn", []))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="lambdaFunctionArnInput")
    def lambda_function_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lambdaFunctionArnInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__809cb0a6a4c6f533d25f79fd178e3258df883732fb6839566ee50c144b875057)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="lambdaFunctionArn")
    def lambda_function_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lambdaFunctionArn"))

    @lambda_function_arn.setter
    def lambda_function_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__28da80be32a79f84415d11346c477c7514da8e39911b7c2f68da6d2ae8296861)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lambdaFunctionArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2ClientVpnEndpointClientConnectOptions]:
        return typing.cast(typing.Optional[Ec2ClientVpnEndpointClientConnectOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2ClientVpnEndpointClientConnectOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9350467a8a20ecda5812ef665bc0225f64632183f1521c4c8ef6f277ff76215)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ec2ClientVpnEndpoint.Ec2ClientVpnEndpointClientLoginBannerOptions",
    jsii_struct_bases=[],
    name_mapping={"banner_text": "bannerText", "enabled": "enabled"},
)
class Ec2ClientVpnEndpointClientLoginBannerOptions:
    def __init__(
        self,
        *,
        banner_text: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param banner_text: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#banner_text Ec2ClientVpnEndpoint#banner_text}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#enabled Ec2ClientVpnEndpoint#enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6552ced0f55e96652c1a190234f1c73124f3d4bd05e47ee7f29fb751b7f7485c)
            check_type(argname="argument banner_text", value=banner_text, expected_type=type_hints["banner_text"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if banner_text is not None:
            self._values["banner_text"] = banner_text
        if enabled is not None:
            self._values["enabled"] = enabled

    @builtins.property
    def banner_text(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#banner_text Ec2ClientVpnEndpoint#banner_text}.'''
        result = self._values.get("banner_text")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#enabled Ec2ClientVpnEndpoint#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2ClientVpnEndpointClientLoginBannerOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Ec2ClientVpnEndpointClientLoginBannerOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2ClientVpnEndpoint.Ec2ClientVpnEndpointClientLoginBannerOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cefc67d046512bf6106523b7fbf9060c73cb542db6956f3142f810e454fe51ce)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBannerText")
    def reset_banner_text(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBannerText", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @builtins.property
    @jsii.member(jsii_name="bannerTextInput")
    def banner_text_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bannerTextInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="bannerText")
    def banner_text(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bannerText"))

    @banner_text.setter
    def banner_text(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5cd992056f2775edf1d8b80a961bd4248cb990e803679c0c3734718bd788e095)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bannerText", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__147fff6ab8bd00cf1aeac51a1da4ceeb1f3e96746e9668cbdd0e9f97c71b0ce4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2ClientVpnEndpointClientLoginBannerOptions]:
        return typing.cast(typing.Optional[Ec2ClientVpnEndpointClientLoginBannerOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2ClientVpnEndpointClientLoginBannerOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24795d4f3a1abb489630cca244a9aa504983d6b21238e7274b1defe96640e5ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ec2ClientVpnEndpoint.Ec2ClientVpnEndpointConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "authentication_options": "authenticationOptions",
        "client_cidr_block": "clientCidrBlock",
        "connection_log_options": "connectionLogOptions",
        "server_certificate_arn": "serverCertificateArn",
        "client_connect_options": "clientConnectOptions",
        "client_login_banner_options": "clientLoginBannerOptions",
        "description": "description",
        "dns_servers": "dnsServers",
        "id": "id",
        "security_group_ids": "securityGroupIds",
        "self_service_portal": "selfServicePortal",
        "session_timeout_hours": "sessionTimeoutHours",
        "split_tunnel": "splitTunnel",
        "tags": "tags",
        "tags_all": "tagsAll",
        "transport_protocol": "transportProtocol",
        "vpc_id": "vpcId",
        "vpn_port": "vpnPort",
    },
)
class Ec2ClientVpnEndpointConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        authentication_options: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[Ec2ClientVpnEndpointAuthenticationOptions, typing.Dict[builtins.str, typing.Any]]]],
        client_cidr_block: builtins.str,
        connection_log_options: typing.Union["Ec2ClientVpnEndpointConnectionLogOptions", typing.Dict[builtins.str, typing.Any]],
        server_certificate_arn: builtins.str,
        client_connect_options: typing.Optional[typing.Union[Ec2ClientVpnEndpointClientConnectOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        client_login_banner_options: typing.Optional[typing.Union[Ec2ClientVpnEndpointClientLoginBannerOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        dns_servers: typing.Optional[typing.Sequence[builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        self_service_portal: typing.Optional[builtins.str] = None,
        session_timeout_hours: typing.Optional[jsii.Number] = None,
        split_tunnel: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        transport_protocol: typing.Optional[builtins.str] = None,
        vpc_id: typing.Optional[builtins.str] = None,
        vpn_port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param authentication_options: authentication_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#authentication_options Ec2ClientVpnEndpoint#authentication_options}
        :param client_cidr_block: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#client_cidr_block Ec2ClientVpnEndpoint#client_cidr_block}.
        :param connection_log_options: connection_log_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#connection_log_options Ec2ClientVpnEndpoint#connection_log_options}
        :param server_certificate_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#server_certificate_arn Ec2ClientVpnEndpoint#server_certificate_arn}.
        :param client_connect_options: client_connect_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#client_connect_options Ec2ClientVpnEndpoint#client_connect_options}
        :param client_login_banner_options: client_login_banner_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#client_login_banner_options Ec2ClientVpnEndpoint#client_login_banner_options}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#description Ec2ClientVpnEndpoint#description}.
        :param dns_servers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#dns_servers Ec2ClientVpnEndpoint#dns_servers}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#id Ec2ClientVpnEndpoint#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#security_group_ids Ec2ClientVpnEndpoint#security_group_ids}.
        :param self_service_portal: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#self_service_portal Ec2ClientVpnEndpoint#self_service_portal}.
        :param session_timeout_hours: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#session_timeout_hours Ec2ClientVpnEndpoint#session_timeout_hours}.
        :param split_tunnel: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#split_tunnel Ec2ClientVpnEndpoint#split_tunnel}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#tags Ec2ClientVpnEndpoint#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#tags_all Ec2ClientVpnEndpoint#tags_all}.
        :param transport_protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#transport_protocol Ec2ClientVpnEndpoint#transport_protocol}.
        :param vpc_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#vpc_id Ec2ClientVpnEndpoint#vpc_id}.
        :param vpn_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#vpn_port Ec2ClientVpnEndpoint#vpn_port}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(connection_log_options, dict):
            connection_log_options = Ec2ClientVpnEndpointConnectionLogOptions(**connection_log_options)
        if isinstance(client_connect_options, dict):
            client_connect_options = Ec2ClientVpnEndpointClientConnectOptions(**client_connect_options)
        if isinstance(client_login_banner_options, dict):
            client_login_banner_options = Ec2ClientVpnEndpointClientLoginBannerOptions(**client_login_banner_options)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94d8f1fa97b8dc0a869cec075001a26ba74ce58259c76e53425d9721b16ba29c)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument authentication_options", value=authentication_options, expected_type=type_hints["authentication_options"])
            check_type(argname="argument client_cidr_block", value=client_cidr_block, expected_type=type_hints["client_cidr_block"])
            check_type(argname="argument connection_log_options", value=connection_log_options, expected_type=type_hints["connection_log_options"])
            check_type(argname="argument server_certificate_arn", value=server_certificate_arn, expected_type=type_hints["server_certificate_arn"])
            check_type(argname="argument client_connect_options", value=client_connect_options, expected_type=type_hints["client_connect_options"])
            check_type(argname="argument client_login_banner_options", value=client_login_banner_options, expected_type=type_hints["client_login_banner_options"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument dns_servers", value=dns_servers, expected_type=type_hints["dns_servers"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
            check_type(argname="argument self_service_portal", value=self_service_portal, expected_type=type_hints["self_service_portal"])
            check_type(argname="argument session_timeout_hours", value=session_timeout_hours, expected_type=type_hints["session_timeout_hours"])
            check_type(argname="argument split_tunnel", value=split_tunnel, expected_type=type_hints["split_tunnel"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument transport_protocol", value=transport_protocol, expected_type=type_hints["transport_protocol"])
            check_type(argname="argument vpc_id", value=vpc_id, expected_type=type_hints["vpc_id"])
            check_type(argname="argument vpn_port", value=vpn_port, expected_type=type_hints["vpn_port"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "authentication_options": authentication_options,
            "client_cidr_block": client_cidr_block,
            "connection_log_options": connection_log_options,
            "server_certificate_arn": server_certificate_arn,
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
        if client_connect_options is not None:
            self._values["client_connect_options"] = client_connect_options
        if client_login_banner_options is not None:
            self._values["client_login_banner_options"] = client_login_banner_options
        if description is not None:
            self._values["description"] = description
        if dns_servers is not None:
            self._values["dns_servers"] = dns_servers
        if id is not None:
            self._values["id"] = id
        if security_group_ids is not None:
            self._values["security_group_ids"] = security_group_ids
        if self_service_portal is not None:
            self._values["self_service_portal"] = self_service_portal
        if session_timeout_hours is not None:
            self._values["session_timeout_hours"] = session_timeout_hours
        if split_tunnel is not None:
            self._values["split_tunnel"] = split_tunnel
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if transport_protocol is not None:
            self._values["transport_protocol"] = transport_protocol
        if vpc_id is not None:
            self._values["vpc_id"] = vpc_id
        if vpn_port is not None:
            self._values["vpn_port"] = vpn_port

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
    def authentication_options(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Ec2ClientVpnEndpointAuthenticationOptions]]:
        '''authentication_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#authentication_options Ec2ClientVpnEndpoint#authentication_options}
        '''
        result = self._values.get("authentication_options")
        assert result is not None, "Required property 'authentication_options' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Ec2ClientVpnEndpointAuthenticationOptions]], result)

    @builtins.property
    def client_cidr_block(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#client_cidr_block Ec2ClientVpnEndpoint#client_cidr_block}.'''
        result = self._values.get("client_cidr_block")
        assert result is not None, "Required property 'client_cidr_block' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def connection_log_options(self) -> "Ec2ClientVpnEndpointConnectionLogOptions":
        '''connection_log_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#connection_log_options Ec2ClientVpnEndpoint#connection_log_options}
        '''
        result = self._values.get("connection_log_options")
        assert result is not None, "Required property 'connection_log_options' is missing"
        return typing.cast("Ec2ClientVpnEndpointConnectionLogOptions", result)

    @builtins.property
    def server_certificate_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#server_certificate_arn Ec2ClientVpnEndpoint#server_certificate_arn}.'''
        result = self._values.get("server_certificate_arn")
        assert result is not None, "Required property 'server_certificate_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_connect_options(
        self,
    ) -> typing.Optional[Ec2ClientVpnEndpointClientConnectOptions]:
        '''client_connect_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#client_connect_options Ec2ClientVpnEndpoint#client_connect_options}
        '''
        result = self._values.get("client_connect_options")
        return typing.cast(typing.Optional[Ec2ClientVpnEndpointClientConnectOptions], result)

    @builtins.property
    def client_login_banner_options(
        self,
    ) -> typing.Optional[Ec2ClientVpnEndpointClientLoginBannerOptions]:
        '''client_login_banner_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#client_login_banner_options Ec2ClientVpnEndpoint#client_login_banner_options}
        '''
        result = self._values.get("client_login_banner_options")
        return typing.cast(typing.Optional[Ec2ClientVpnEndpointClientLoginBannerOptions], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#description Ec2ClientVpnEndpoint#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dns_servers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#dns_servers Ec2ClientVpnEndpoint#dns_servers}.'''
        result = self._values.get("dns_servers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#id Ec2ClientVpnEndpoint#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#security_group_ids Ec2ClientVpnEndpoint#security_group_ids}.'''
        result = self._values.get("security_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def self_service_portal(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#self_service_portal Ec2ClientVpnEndpoint#self_service_portal}.'''
        result = self._values.get("self_service_portal")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def session_timeout_hours(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#session_timeout_hours Ec2ClientVpnEndpoint#session_timeout_hours}.'''
        result = self._values.get("session_timeout_hours")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def split_tunnel(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#split_tunnel Ec2ClientVpnEndpoint#split_tunnel}.'''
        result = self._values.get("split_tunnel")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#tags Ec2ClientVpnEndpoint#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#tags_all Ec2ClientVpnEndpoint#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def transport_protocol(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#transport_protocol Ec2ClientVpnEndpoint#transport_protocol}.'''
        result = self._values.get("transport_protocol")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vpc_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#vpc_id Ec2ClientVpnEndpoint#vpc_id}.'''
        result = self._values.get("vpc_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vpn_port(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#vpn_port Ec2ClientVpnEndpoint#vpn_port}.'''
        result = self._values.get("vpn_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2ClientVpnEndpointConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.ec2ClientVpnEndpoint.Ec2ClientVpnEndpointConnectionLogOptions",
    jsii_struct_bases=[],
    name_mapping={
        "enabled": "enabled",
        "cloudwatch_log_group": "cloudwatchLogGroup",
        "cloudwatch_log_stream": "cloudwatchLogStream",
    },
)
class Ec2ClientVpnEndpointConnectionLogOptions:
    def __init__(
        self,
        *,
        enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        cloudwatch_log_group: typing.Optional[builtins.str] = None,
        cloudwatch_log_stream: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#enabled Ec2ClientVpnEndpoint#enabled}.
        :param cloudwatch_log_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#cloudwatch_log_group Ec2ClientVpnEndpoint#cloudwatch_log_group}.
        :param cloudwatch_log_stream: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#cloudwatch_log_stream Ec2ClientVpnEndpoint#cloudwatch_log_stream}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b81caf4ceaa2efe645c2723029ad39017b77010fbcec73883a634ea84f7492f4)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument cloudwatch_log_group", value=cloudwatch_log_group, expected_type=type_hints["cloudwatch_log_group"])
            check_type(argname="argument cloudwatch_log_stream", value=cloudwatch_log_stream, expected_type=type_hints["cloudwatch_log_stream"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "enabled": enabled,
        }
        if cloudwatch_log_group is not None:
            self._values["cloudwatch_log_group"] = cloudwatch_log_group
        if cloudwatch_log_stream is not None:
            self._values["cloudwatch_log_stream"] = cloudwatch_log_stream

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#enabled Ec2ClientVpnEndpoint#enabled}.'''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    @builtins.property
    def cloudwatch_log_group(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#cloudwatch_log_group Ec2ClientVpnEndpoint#cloudwatch_log_group}.'''
        result = self._values.get("cloudwatch_log_group")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cloudwatch_log_stream(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_client_vpn_endpoint#cloudwatch_log_stream Ec2ClientVpnEndpoint#cloudwatch_log_stream}.'''
        result = self._values.get("cloudwatch_log_stream")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2ClientVpnEndpointConnectionLogOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Ec2ClientVpnEndpointConnectionLogOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2ClientVpnEndpoint.Ec2ClientVpnEndpointConnectionLogOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0a72354aebd657dda81e61e90c989e55e47ea9c989b65f1107a6db1537f2869b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCloudwatchLogGroup")
    def reset_cloudwatch_log_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudwatchLogGroup", []))

    @jsii.member(jsii_name="resetCloudwatchLogStream")
    def reset_cloudwatch_log_stream(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudwatchLogStream", []))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchLogGroupInput")
    def cloudwatch_log_group_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cloudwatchLogGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchLogStreamInput")
    def cloudwatch_log_stream_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cloudwatchLogStreamInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchLogGroup")
    def cloudwatch_log_group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cloudwatchLogGroup"))

    @cloudwatch_log_group.setter
    def cloudwatch_log_group(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eeec6afb4924ac9abd3ad7e882a6a137ece8dcc1eacd85a43e4133001130abd1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloudwatchLogGroup", value)

    @builtins.property
    @jsii.member(jsii_name="cloudwatchLogStream")
    def cloudwatch_log_stream(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cloudwatchLogStream"))

    @cloudwatch_log_stream.setter
    def cloudwatch_log_stream(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__691f04a76842ec85610a410bdd45d8efef5d11663eb8ed2ee6a09d15b2cdcc73)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloudwatchLogStream", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__bb9ff2e737ed75a2a975420ca51ba81347aed11b556b061eea5dea276bdd9369)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2ClientVpnEndpointConnectionLogOptions]:
        return typing.cast(typing.Optional[Ec2ClientVpnEndpointConnectionLogOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2ClientVpnEndpointConnectionLogOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e161f6e3ea8f0940ead5baf54501a20f3eb8d176e3e36f35a8fd6ed9aa07293)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Ec2ClientVpnEndpoint",
    "Ec2ClientVpnEndpointAuthenticationOptions",
    "Ec2ClientVpnEndpointAuthenticationOptionsList",
    "Ec2ClientVpnEndpointAuthenticationOptionsOutputReference",
    "Ec2ClientVpnEndpointClientConnectOptions",
    "Ec2ClientVpnEndpointClientConnectOptionsOutputReference",
    "Ec2ClientVpnEndpointClientLoginBannerOptions",
    "Ec2ClientVpnEndpointClientLoginBannerOptionsOutputReference",
    "Ec2ClientVpnEndpointConfig",
    "Ec2ClientVpnEndpointConnectionLogOptions",
    "Ec2ClientVpnEndpointConnectionLogOptionsOutputReference",
]

publication.publish()

def _typecheckingstub__a7616e1ee7003d6e747bcd3afa4e5353ab8b3d6fe5aca9120da2a241ca228d99(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    authentication_options: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[Ec2ClientVpnEndpointAuthenticationOptions, typing.Dict[builtins.str, typing.Any]]]],
    client_cidr_block: builtins.str,
    connection_log_options: typing.Union[Ec2ClientVpnEndpointConnectionLogOptions, typing.Dict[builtins.str, typing.Any]],
    server_certificate_arn: builtins.str,
    client_connect_options: typing.Optional[typing.Union[Ec2ClientVpnEndpointClientConnectOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    client_login_banner_options: typing.Optional[typing.Union[Ec2ClientVpnEndpointClientLoginBannerOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    description: typing.Optional[builtins.str] = None,
    dns_servers: typing.Optional[typing.Sequence[builtins.str]] = None,
    id: typing.Optional[builtins.str] = None,
    security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    self_service_portal: typing.Optional[builtins.str] = None,
    session_timeout_hours: typing.Optional[jsii.Number] = None,
    split_tunnel: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    transport_protocol: typing.Optional[builtins.str] = None,
    vpc_id: typing.Optional[builtins.str] = None,
    vpn_port: typing.Optional[jsii.Number] = None,
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

def _typecheckingstub__8b4f99315fdf3795a2d21d3cd80b1d97e29ddec41243400074d0e5b65c07999a(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[Ec2ClientVpnEndpointAuthenticationOptions, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25801627a2ec2572b0f110f089cb66fa201a5215a3f8093660ce9ba10d0d5837(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a769b5e15b1bb912b0f57e41e2f68a961000b9d690eaf96aee9058e63e607e0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__acea71dc20e83b740c10dd0cf4e43047b91c5c16903f3f3d5a132d17843c3b42(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1687e256e321537ca819ff1374fb22c678e613560e28b4d66437d83ce926bfd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21f8cbc63e4441d37c7bafeaef5d370a51f7352092be171fc9af7d87365e7307(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f07f9cdde496a5c9a5e415129770456dca1dbe9acccdbba839f71fb0b429b100(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c1cac72d30e73946b461d12fc2c24adcbe820216ded62b8f59676b4b099a017(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab491f2baa6878648e5370a4749cb48ef1011f292baf398635daec9611d9e94b(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b98af37308746c44b40bca4d053759df6cebda83f02a96a59151de320e1db97(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a951f7969c29a188611ac9c57181326daf2654391241ec3ec817f265fa4c5efd(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48882e5374242f16946c6212cdb467468e61eb964f14c0436f9c4d94f5e2e7c8(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4061a3d1339c958dc3fe7a55825a0b66b0c105175b0e5f1fe0dac7e55b104310(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d90fbfac90b068c011874b0e8b39a4af5b8cbb57f75cdf18279f270081d96c9e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c75f46336159148e7dbbe85092f98855c7a3167aa59d695ca6d0febada744914(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1609f0c9cc07a27b9903ee86af85ac0eb107bfbaab380d9d44726083a54f3855(
    *,
    type: builtins.str,
    active_directory_id: typing.Optional[builtins.str] = None,
    root_certificate_chain_arn: typing.Optional[builtins.str] = None,
    saml_provider_arn: typing.Optional[builtins.str] = None,
    self_service_saml_provider_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ca29f65bc9ae991d19617b54660d1f1f954ba5c27021a7303030bcd2ccd39ca(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c77ce619fe48fca294a747ebdebd14f69bf716e0dadc7e64afd475e416db2db(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8929bd90a92e7aca9ae4bc2721527f9619cdfe817d324593784067c424128ebd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b308b8052bb47525b0eab25ee26f1d05e9262fbf54397f49e5b50d6d779a8eb4(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e230b5de12373019a7db589c22ae1acb83d708a5829cab8c1d78f84b78bfcafb(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c8683e5be76297f2a87eb6622131eecd534cda02f3529af489397f45502f60f(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Ec2ClientVpnEndpointAuthenticationOptions]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7caffd7346293a6a44f8bf306a15467f817561a5bce17d4c330c825e1233daf(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f208584389510e4da3c5f0582e0fff0d97b167ca508d398d754050bba05e4f9f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e60189e3a74d2a7252e7b0e9ede691127f731a6d9d8e3d471b274f72b601a13(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c031dc398ad4bb50d164c0804b446b7bb356589aee5565abe9a181262a48065a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86b6e1fc4a852b13acb7203bdf338727e874004b80237cca7f24aa4bcf6ef7fb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45eec6c71b6341a91f268d3b1a9a1312846e363666dc4bb585b2697109c3c9b3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f96229bd09e86b2364a5710b11d48c9841b82456941d99b01d4659f802b6d879(
    value: typing.Optional[typing.Union[Ec2ClientVpnEndpointAuthenticationOptions, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21f7c4e5e6c74f755a0376741fcf92709c8a5bb7996d283af44bbb55cd44c736(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    lambda_function_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32611838a4db95ac4cca7872f4a9d0e4fe52449049c92d9213ac9f6ad81ef8e7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__809cb0a6a4c6f533d25f79fd178e3258df883732fb6839566ee50c144b875057(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28da80be32a79f84415d11346c477c7514da8e39911b7c2f68da6d2ae8296861(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9350467a8a20ecda5812ef665bc0225f64632183f1521c4c8ef6f277ff76215(
    value: typing.Optional[Ec2ClientVpnEndpointClientConnectOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6552ced0f55e96652c1a190234f1c73124f3d4bd05e47ee7f29fb751b7f7485c(
    *,
    banner_text: typing.Optional[builtins.str] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cefc67d046512bf6106523b7fbf9060c73cb542db6956f3142f810e454fe51ce(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5cd992056f2775edf1d8b80a961bd4248cb990e803679c0c3734718bd788e095(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__147fff6ab8bd00cf1aeac51a1da4ceeb1f3e96746e9668cbdd0e9f97c71b0ce4(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24795d4f3a1abb489630cca244a9aa504983d6b21238e7274b1defe96640e5ec(
    value: typing.Optional[Ec2ClientVpnEndpointClientLoginBannerOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94d8f1fa97b8dc0a869cec075001a26ba74ce58259c76e53425d9721b16ba29c(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    authentication_options: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[Ec2ClientVpnEndpointAuthenticationOptions, typing.Dict[builtins.str, typing.Any]]]],
    client_cidr_block: builtins.str,
    connection_log_options: typing.Union[Ec2ClientVpnEndpointConnectionLogOptions, typing.Dict[builtins.str, typing.Any]],
    server_certificate_arn: builtins.str,
    client_connect_options: typing.Optional[typing.Union[Ec2ClientVpnEndpointClientConnectOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    client_login_banner_options: typing.Optional[typing.Union[Ec2ClientVpnEndpointClientLoginBannerOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    description: typing.Optional[builtins.str] = None,
    dns_servers: typing.Optional[typing.Sequence[builtins.str]] = None,
    id: typing.Optional[builtins.str] = None,
    security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    self_service_portal: typing.Optional[builtins.str] = None,
    session_timeout_hours: typing.Optional[jsii.Number] = None,
    split_tunnel: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    transport_protocol: typing.Optional[builtins.str] = None,
    vpc_id: typing.Optional[builtins.str] = None,
    vpn_port: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b81caf4ceaa2efe645c2723029ad39017b77010fbcec73883a634ea84f7492f4(
    *,
    enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    cloudwatch_log_group: typing.Optional[builtins.str] = None,
    cloudwatch_log_stream: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a72354aebd657dda81e61e90c989e55e47ea9c989b65f1107a6db1537f2869b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eeec6afb4924ac9abd3ad7e882a6a137ece8dcc1eacd85a43e4133001130abd1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__691f04a76842ec85610a410bdd45d8efef5d11663eb8ed2ee6a09d15b2cdcc73(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb9ff2e737ed75a2a975420ca51ba81347aed11b556b061eea5dea276bdd9369(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e161f6e3ea8f0940ead5baf54501a20f3eb8d176e3e36f35a8fd6ed9aa07293(
    value: typing.Optional[Ec2ClientVpnEndpointConnectionLogOptions],
) -> None:
    """Type checking stubs"""
    pass
