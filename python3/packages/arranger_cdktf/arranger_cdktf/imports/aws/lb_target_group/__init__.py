'''
# `aws_lb_target_group`

Refer to the Terraform Registory for docs: [`aws_lb_target_group`](https://www.terraform.io/docs/providers/aws/r/lb_target_group).
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


class LbTargetGroup(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lbTargetGroup.LbTargetGroup",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group aws_lb_target_group}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        connection_termination: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        deregistration_delay: typing.Optional[builtins.str] = None,
        health_check: typing.Optional[typing.Union["LbTargetGroupHealthCheck", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        ip_address_type: typing.Optional[builtins.str] = None,
        lambda_multi_value_headers_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        load_balancing_algorithm_type: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        name_prefix: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        preserve_client_ip: typing.Optional[builtins.str] = None,
        protocol: typing.Optional[builtins.str] = None,
        protocol_version: typing.Optional[builtins.str] = None,
        proxy_protocol_v2: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        slow_start: typing.Optional[jsii.Number] = None,
        stickiness: typing.Optional[typing.Union["LbTargetGroupStickiness", typing.Dict[builtins.str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        target_failover: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LbTargetGroupTargetFailover", typing.Dict[builtins.str, typing.Any]]]]] = None,
        target_type: typing.Optional[builtins.str] = None,
        vpc_id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group aws_lb_target_group} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param connection_termination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#connection_termination LbTargetGroup#connection_termination}.
        :param deregistration_delay: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#deregistration_delay LbTargetGroup#deregistration_delay}.
        :param health_check: health_check block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#health_check LbTargetGroup#health_check}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#id LbTargetGroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ip_address_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#ip_address_type LbTargetGroup#ip_address_type}.
        :param lambda_multi_value_headers_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#lambda_multi_value_headers_enabled LbTargetGroup#lambda_multi_value_headers_enabled}.
        :param load_balancing_algorithm_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#load_balancing_algorithm_type LbTargetGroup#load_balancing_algorithm_type}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#name LbTargetGroup#name}.
        :param name_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#name_prefix LbTargetGroup#name_prefix}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#port LbTargetGroup#port}.
        :param preserve_client_ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#preserve_client_ip LbTargetGroup#preserve_client_ip}.
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#protocol LbTargetGroup#protocol}.
        :param protocol_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#protocol_version LbTargetGroup#protocol_version}.
        :param proxy_protocol_v2: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#proxy_protocol_v2 LbTargetGroup#proxy_protocol_v2}.
        :param slow_start: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#slow_start LbTargetGroup#slow_start}.
        :param stickiness: stickiness block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#stickiness LbTargetGroup#stickiness}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#tags LbTargetGroup#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#tags_all LbTargetGroup#tags_all}.
        :param target_failover: target_failover block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#target_failover LbTargetGroup#target_failover}
        :param target_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#target_type LbTargetGroup#target_type}.
        :param vpc_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#vpc_id LbTargetGroup#vpc_id}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f79e2265cfb634c62980845c8a8d7446a23f259229c1a34d4b17eff506dc9b4d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = LbTargetGroupConfig(
            connection_termination=connection_termination,
            deregistration_delay=deregistration_delay,
            health_check=health_check,
            id=id,
            ip_address_type=ip_address_type,
            lambda_multi_value_headers_enabled=lambda_multi_value_headers_enabled,
            load_balancing_algorithm_type=load_balancing_algorithm_type,
            name=name,
            name_prefix=name_prefix,
            port=port,
            preserve_client_ip=preserve_client_ip,
            protocol=protocol,
            protocol_version=protocol_version,
            proxy_protocol_v2=proxy_protocol_v2,
            slow_start=slow_start,
            stickiness=stickiness,
            tags=tags,
            tags_all=tags_all,
            target_failover=target_failover,
            target_type=target_type,
            vpc_id=vpc_id,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putHealthCheck")
    def put_health_check(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        healthy_threshold: typing.Optional[jsii.Number] = None,
        interval: typing.Optional[jsii.Number] = None,
        matcher: typing.Optional[builtins.str] = None,
        path: typing.Optional[builtins.str] = None,
        port: typing.Optional[builtins.str] = None,
        protocol: typing.Optional[builtins.str] = None,
        timeout: typing.Optional[jsii.Number] = None,
        unhealthy_threshold: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#enabled LbTargetGroup#enabled}.
        :param healthy_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#healthy_threshold LbTargetGroup#healthy_threshold}.
        :param interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#interval LbTargetGroup#interval}.
        :param matcher: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#matcher LbTargetGroup#matcher}.
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#path LbTargetGroup#path}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#port LbTargetGroup#port}.
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#protocol LbTargetGroup#protocol}.
        :param timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#timeout LbTargetGroup#timeout}.
        :param unhealthy_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#unhealthy_threshold LbTargetGroup#unhealthy_threshold}.
        '''
        value = LbTargetGroupHealthCheck(
            enabled=enabled,
            healthy_threshold=healthy_threshold,
            interval=interval,
            matcher=matcher,
            path=path,
            port=port,
            protocol=protocol,
            timeout=timeout,
            unhealthy_threshold=unhealthy_threshold,
        )

        return typing.cast(None, jsii.invoke(self, "putHealthCheck", [value]))

    @jsii.member(jsii_name="putStickiness")
    def put_stickiness(
        self,
        *,
        type: builtins.str,
        cookie_duration: typing.Optional[jsii.Number] = None,
        cookie_name: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#type LbTargetGroup#type}.
        :param cookie_duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#cookie_duration LbTargetGroup#cookie_duration}.
        :param cookie_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#cookie_name LbTargetGroup#cookie_name}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#enabled LbTargetGroup#enabled}.
        '''
        value = LbTargetGroupStickiness(
            type=type,
            cookie_duration=cookie_duration,
            cookie_name=cookie_name,
            enabled=enabled,
        )

        return typing.cast(None, jsii.invoke(self, "putStickiness", [value]))

    @jsii.member(jsii_name="putTargetFailover")
    def put_target_failover(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LbTargetGroupTargetFailover", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0fc68ae5d4029db6b2ddb4dfed075be1933db34abd5c238ea6a161ad7e66c6d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTargetFailover", [value]))

    @jsii.member(jsii_name="resetConnectionTermination")
    def reset_connection_termination(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectionTermination", []))

    @jsii.member(jsii_name="resetDeregistrationDelay")
    def reset_deregistration_delay(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeregistrationDelay", []))

    @jsii.member(jsii_name="resetHealthCheck")
    def reset_health_check(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHealthCheck", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIpAddressType")
    def reset_ip_address_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpAddressType", []))

    @jsii.member(jsii_name="resetLambdaMultiValueHeadersEnabled")
    def reset_lambda_multi_value_headers_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLambdaMultiValueHeadersEnabled", []))

    @jsii.member(jsii_name="resetLoadBalancingAlgorithmType")
    def reset_load_balancing_algorithm_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoadBalancingAlgorithmType", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetNamePrefix")
    def reset_name_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamePrefix", []))

    @jsii.member(jsii_name="resetPort")
    def reset_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPort", []))

    @jsii.member(jsii_name="resetPreserveClientIp")
    def reset_preserve_client_ip(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreserveClientIp", []))

    @jsii.member(jsii_name="resetProtocol")
    def reset_protocol(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProtocol", []))

    @jsii.member(jsii_name="resetProtocolVersion")
    def reset_protocol_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProtocolVersion", []))

    @jsii.member(jsii_name="resetProxyProtocolV2")
    def reset_proxy_protocol_v2(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProxyProtocolV2", []))

    @jsii.member(jsii_name="resetSlowStart")
    def reset_slow_start(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSlowStart", []))

    @jsii.member(jsii_name="resetStickiness")
    def reset_stickiness(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStickiness", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetTargetFailover")
    def reset_target_failover(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetFailover", []))

    @jsii.member(jsii_name="resetTargetType")
    def reset_target_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetType", []))

    @jsii.member(jsii_name="resetVpcId")
    def reset_vpc_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVpcId", []))

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
    @jsii.member(jsii_name="arnSuffix")
    def arn_suffix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arnSuffix"))

    @builtins.property
    @jsii.member(jsii_name="healthCheck")
    def health_check(self) -> "LbTargetGroupHealthCheckOutputReference":
        return typing.cast("LbTargetGroupHealthCheckOutputReference", jsii.get(self, "healthCheck"))

    @builtins.property
    @jsii.member(jsii_name="stickiness")
    def stickiness(self) -> "LbTargetGroupStickinessOutputReference":
        return typing.cast("LbTargetGroupStickinessOutputReference", jsii.get(self, "stickiness"))

    @builtins.property
    @jsii.member(jsii_name="targetFailover")
    def target_failover(self) -> "LbTargetGroupTargetFailoverList":
        return typing.cast("LbTargetGroupTargetFailoverList", jsii.get(self, "targetFailover"))

    @builtins.property
    @jsii.member(jsii_name="connectionTerminationInput")
    def connection_termination_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "connectionTerminationInput"))

    @builtins.property
    @jsii.member(jsii_name="deregistrationDelayInput")
    def deregistration_delay_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deregistrationDelayInput"))

    @builtins.property
    @jsii.member(jsii_name="healthCheckInput")
    def health_check_input(self) -> typing.Optional["LbTargetGroupHealthCheck"]:
        return typing.cast(typing.Optional["LbTargetGroupHealthCheck"], jsii.get(self, "healthCheckInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="ipAddressTypeInput")
    def ip_address_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipAddressTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="lambdaMultiValueHeadersEnabledInput")
    def lambda_multi_value_headers_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "lambdaMultiValueHeadersEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="loadBalancingAlgorithmTypeInput")
    def load_balancing_algorithm_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "loadBalancingAlgorithmTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="namePrefixInput")
    def name_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namePrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="preserveClientIpInput")
    def preserve_client_ip_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "preserveClientIpInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolInput")
    def protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocolInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolVersionInput")
    def protocol_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocolVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="proxyProtocolV2Input")
    def proxy_protocol_v2_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "proxyProtocolV2Input"))

    @builtins.property
    @jsii.member(jsii_name="slowStartInput")
    def slow_start_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "slowStartInput"))

    @builtins.property
    @jsii.member(jsii_name="stickinessInput")
    def stickiness_input(self) -> typing.Optional["LbTargetGroupStickiness"]:
        return typing.cast(typing.Optional["LbTargetGroupStickiness"], jsii.get(self, "stickinessInput"))

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
    @jsii.member(jsii_name="targetFailoverInput")
    def target_failover_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LbTargetGroupTargetFailover"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LbTargetGroupTargetFailover"]]], jsii.get(self, "targetFailoverInput"))

    @builtins.property
    @jsii.member(jsii_name="targetTypeInput")
    def target_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="vpcIdInput")
    def vpc_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vpcIdInput"))

    @builtins.property
    @jsii.member(jsii_name="connectionTermination")
    def connection_termination(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "connectionTermination"))

    @connection_termination.setter
    def connection_termination(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__307923bbb0664d88b3bb002c7122f7ac1860a32ba3eab0c08dd28a57a3a12fc3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionTermination", value)

    @builtins.property
    @jsii.member(jsii_name="deregistrationDelay")
    def deregistration_delay(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deregistrationDelay"))

    @deregistration_delay.setter
    def deregistration_delay(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__954baff4e50fed24f6b10fa7b70528b6c26c9da05260c3030ba03a796bfc8f7d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deregistrationDelay", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5a0a76e75afefa07dac4fb9388c5a96f22e82fc453f754dd5162ae47820c76c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="ipAddressType")
    def ip_address_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipAddressType"))

    @ip_address_type.setter
    def ip_address_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c1af20432fd82ae52c4ecdcf636e5e692a0f1f968fc43e05576fa5237e27b00)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipAddressType", value)

    @builtins.property
    @jsii.member(jsii_name="lambdaMultiValueHeadersEnabled")
    def lambda_multi_value_headers_enabled(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "lambdaMultiValueHeadersEnabled"))

    @lambda_multi_value_headers_enabled.setter
    def lambda_multi_value_headers_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e73f56c9cb022f2b251ad0999aab3ea01970d6dedad2ef68fe98ad15b7de34ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lambdaMultiValueHeadersEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="loadBalancingAlgorithmType")
    def load_balancing_algorithm_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "loadBalancingAlgorithmType"))

    @load_balancing_algorithm_type.setter
    def load_balancing_algorithm_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8399ca07d6628acd76771c6ec9be4c9eafee50eddd2ae364f08e0888b19d68f6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loadBalancingAlgorithmType", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38dc1c098beab16c4f9f4170ff64ca13ad0ebd0f20242e9d227734ded04e90d8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namePrefix")
    def name_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namePrefix"))

    @name_prefix.setter
    def name_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3504871caac871d0e716f49aa225ae60dfe4a5a909bd88364fff8504f3f7f0e7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namePrefix", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc97bce0545f1766d75f51cd0abac026facfc1d652226f690a1434e4770dd4aa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="preserveClientIp")
    def preserve_client_ip(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "preserveClientIp"))

    @preserve_client_ip.setter
    def preserve_client_ip(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8a015023bd1625e36b02c2470793875451d0e099dd758402d0ea788867c1e08)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preserveClientIp", value)

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ef4357770b94bbebd388d81f986b7ccedc371ae2d04fb9d9eeb5b23d6986f79)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="protocolVersion")
    def protocol_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocolVersion"))

    @protocol_version.setter
    def protocol_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ac01eb2c42c6b9f0ab444d042477ccea77cbf970ddc353204d0bb32fc10927a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocolVersion", value)

    @builtins.property
    @jsii.member(jsii_name="proxyProtocolV2")
    def proxy_protocol_v2(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "proxyProtocolV2"))

    @proxy_protocol_v2.setter
    def proxy_protocol_v2(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33a8163976f84cd90322bc526107f6125a4994ffbd98cc5a240e7173ae46f787)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "proxyProtocolV2", value)

    @builtins.property
    @jsii.member(jsii_name="slowStart")
    def slow_start(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "slowStart"))

    @slow_start.setter
    def slow_start(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db550c83576105eaf06c09bf250e57ff9e2d6d52336e4377281553a659911d25)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "slowStart", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5dca32396a583cd54ed4d2f88bbe6fe0244437af7481cc348747d76d4c03588b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee7e66f863bbe94ba4754b5eddc033e72a96c9334c77a33bf0c2a4d5978dfbc8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)

    @builtins.property
    @jsii.member(jsii_name="targetType")
    def target_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetType"))

    @target_type.setter
    def target_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__daf83572a42727d65ff26b61a4818c5939d1bf70d027ebfc7a07a3fc02ede9a5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetType", value)

    @builtins.property
    @jsii.member(jsii_name="vpcId")
    def vpc_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vpcId"))

    @vpc_id.setter
    def vpc_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa53a18cb287ddbb69e1c3d1bfa728666e862a76938ca3fa436b077a13cad7eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcId", value)


@jsii.data_type(
    jsii_type="aws.lbTargetGroup.LbTargetGroupConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "connection_termination": "connectionTermination",
        "deregistration_delay": "deregistrationDelay",
        "health_check": "healthCheck",
        "id": "id",
        "ip_address_type": "ipAddressType",
        "lambda_multi_value_headers_enabled": "lambdaMultiValueHeadersEnabled",
        "load_balancing_algorithm_type": "loadBalancingAlgorithmType",
        "name": "name",
        "name_prefix": "namePrefix",
        "port": "port",
        "preserve_client_ip": "preserveClientIp",
        "protocol": "protocol",
        "protocol_version": "protocolVersion",
        "proxy_protocol_v2": "proxyProtocolV2",
        "slow_start": "slowStart",
        "stickiness": "stickiness",
        "tags": "tags",
        "tags_all": "tagsAll",
        "target_failover": "targetFailover",
        "target_type": "targetType",
        "vpc_id": "vpcId",
    },
)
class LbTargetGroupConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        connection_termination: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        deregistration_delay: typing.Optional[builtins.str] = None,
        health_check: typing.Optional[typing.Union["LbTargetGroupHealthCheck", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        ip_address_type: typing.Optional[builtins.str] = None,
        lambda_multi_value_headers_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        load_balancing_algorithm_type: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        name_prefix: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        preserve_client_ip: typing.Optional[builtins.str] = None,
        protocol: typing.Optional[builtins.str] = None,
        protocol_version: typing.Optional[builtins.str] = None,
        proxy_protocol_v2: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        slow_start: typing.Optional[jsii.Number] = None,
        stickiness: typing.Optional[typing.Union["LbTargetGroupStickiness", typing.Dict[builtins.str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        target_failover: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LbTargetGroupTargetFailover", typing.Dict[builtins.str, typing.Any]]]]] = None,
        target_type: typing.Optional[builtins.str] = None,
        vpc_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param connection_termination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#connection_termination LbTargetGroup#connection_termination}.
        :param deregistration_delay: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#deregistration_delay LbTargetGroup#deregistration_delay}.
        :param health_check: health_check block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#health_check LbTargetGroup#health_check}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#id LbTargetGroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ip_address_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#ip_address_type LbTargetGroup#ip_address_type}.
        :param lambda_multi_value_headers_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#lambda_multi_value_headers_enabled LbTargetGroup#lambda_multi_value_headers_enabled}.
        :param load_balancing_algorithm_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#load_balancing_algorithm_type LbTargetGroup#load_balancing_algorithm_type}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#name LbTargetGroup#name}.
        :param name_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#name_prefix LbTargetGroup#name_prefix}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#port LbTargetGroup#port}.
        :param preserve_client_ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#preserve_client_ip LbTargetGroup#preserve_client_ip}.
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#protocol LbTargetGroup#protocol}.
        :param protocol_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#protocol_version LbTargetGroup#protocol_version}.
        :param proxy_protocol_v2: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#proxy_protocol_v2 LbTargetGroup#proxy_protocol_v2}.
        :param slow_start: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#slow_start LbTargetGroup#slow_start}.
        :param stickiness: stickiness block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#stickiness LbTargetGroup#stickiness}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#tags LbTargetGroup#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#tags_all LbTargetGroup#tags_all}.
        :param target_failover: target_failover block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#target_failover LbTargetGroup#target_failover}
        :param target_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#target_type LbTargetGroup#target_type}.
        :param vpc_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#vpc_id LbTargetGroup#vpc_id}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(health_check, dict):
            health_check = LbTargetGroupHealthCheck(**health_check)
        if isinstance(stickiness, dict):
            stickiness = LbTargetGroupStickiness(**stickiness)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9248f3c06fcd83fd2681d369fecb90bf3d1f2fcb77a1265607c49f2f590b6704)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument connection_termination", value=connection_termination, expected_type=type_hints["connection_termination"])
            check_type(argname="argument deregistration_delay", value=deregistration_delay, expected_type=type_hints["deregistration_delay"])
            check_type(argname="argument health_check", value=health_check, expected_type=type_hints["health_check"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument ip_address_type", value=ip_address_type, expected_type=type_hints["ip_address_type"])
            check_type(argname="argument lambda_multi_value_headers_enabled", value=lambda_multi_value_headers_enabled, expected_type=type_hints["lambda_multi_value_headers_enabled"])
            check_type(argname="argument load_balancing_algorithm_type", value=load_balancing_algorithm_type, expected_type=type_hints["load_balancing_algorithm_type"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument name_prefix", value=name_prefix, expected_type=type_hints["name_prefix"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument preserve_client_ip", value=preserve_client_ip, expected_type=type_hints["preserve_client_ip"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument protocol_version", value=protocol_version, expected_type=type_hints["protocol_version"])
            check_type(argname="argument proxy_protocol_v2", value=proxy_protocol_v2, expected_type=type_hints["proxy_protocol_v2"])
            check_type(argname="argument slow_start", value=slow_start, expected_type=type_hints["slow_start"])
            check_type(argname="argument stickiness", value=stickiness, expected_type=type_hints["stickiness"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument target_failover", value=target_failover, expected_type=type_hints["target_failover"])
            check_type(argname="argument target_type", value=target_type, expected_type=type_hints["target_type"])
            check_type(argname="argument vpc_id", value=vpc_id, expected_type=type_hints["vpc_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
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
        if connection_termination is not None:
            self._values["connection_termination"] = connection_termination
        if deregistration_delay is not None:
            self._values["deregistration_delay"] = deregistration_delay
        if health_check is not None:
            self._values["health_check"] = health_check
        if id is not None:
            self._values["id"] = id
        if ip_address_type is not None:
            self._values["ip_address_type"] = ip_address_type
        if lambda_multi_value_headers_enabled is not None:
            self._values["lambda_multi_value_headers_enabled"] = lambda_multi_value_headers_enabled
        if load_balancing_algorithm_type is not None:
            self._values["load_balancing_algorithm_type"] = load_balancing_algorithm_type
        if name is not None:
            self._values["name"] = name
        if name_prefix is not None:
            self._values["name_prefix"] = name_prefix
        if port is not None:
            self._values["port"] = port
        if preserve_client_ip is not None:
            self._values["preserve_client_ip"] = preserve_client_ip
        if protocol is not None:
            self._values["protocol"] = protocol
        if protocol_version is not None:
            self._values["protocol_version"] = protocol_version
        if proxy_protocol_v2 is not None:
            self._values["proxy_protocol_v2"] = proxy_protocol_v2
        if slow_start is not None:
            self._values["slow_start"] = slow_start
        if stickiness is not None:
            self._values["stickiness"] = stickiness
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if target_failover is not None:
            self._values["target_failover"] = target_failover
        if target_type is not None:
            self._values["target_type"] = target_type
        if vpc_id is not None:
            self._values["vpc_id"] = vpc_id

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
    def connection_termination(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#connection_termination LbTargetGroup#connection_termination}.'''
        result = self._values.get("connection_termination")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def deregistration_delay(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#deregistration_delay LbTargetGroup#deregistration_delay}.'''
        result = self._values.get("deregistration_delay")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def health_check(self) -> typing.Optional["LbTargetGroupHealthCheck"]:
        '''health_check block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#health_check LbTargetGroup#health_check}
        '''
        result = self._values.get("health_check")
        return typing.cast(typing.Optional["LbTargetGroupHealthCheck"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#id LbTargetGroup#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ip_address_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#ip_address_type LbTargetGroup#ip_address_type}.'''
        result = self._values.get("ip_address_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lambda_multi_value_headers_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#lambda_multi_value_headers_enabled LbTargetGroup#lambda_multi_value_headers_enabled}.'''
        result = self._values.get("lambda_multi_value_headers_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def load_balancing_algorithm_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#load_balancing_algorithm_type LbTargetGroup#load_balancing_algorithm_type}.'''
        result = self._values.get("load_balancing_algorithm_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#name LbTargetGroup#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#name_prefix LbTargetGroup#name_prefix}.'''
        result = self._values.get("name_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#port LbTargetGroup#port}.'''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def preserve_client_ip(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#preserve_client_ip LbTargetGroup#preserve_client_ip}.'''
        result = self._values.get("preserve_client_ip")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def protocol(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#protocol LbTargetGroup#protocol}.'''
        result = self._values.get("protocol")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def protocol_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#protocol_version LbTargetGroup#protocol_version}.'''
        result = self._values.get("protocol_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def proxy_protocol_v2(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#proxy_protocol_v2 LbTargetGroup#proxy_protocol_v2}.'''
        result = self._values.get("proxy_protocol_v2")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def slow_start(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#slow_start LbTargetGroup#slow_start}.'''
        result = self._values.get("slow_start")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def stickiness(self) -> typing.Optional["LbTargetGroupStickiness"]:
        '''stickiness block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#stickiness LbTargetGroup#stickiness}
        '''
        result = self._values.get("stickiness")
        return typing.cast(typing.Optional["LbTargetGroupStickiness"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#tags LbTargetGroup#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#tags_all LbTargetGroup#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def target_failover(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LbTargetGroupTargetFailover"]]]:
        '''target_failover block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#target_failover LbTargetGroup#target_failover}
        '''
        result = self._values.get("target_failover")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LbTargetGroupTargetFailover"]]], result)

    @builtins.property
    def target_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#target_type LbTargetGroup#target_type}.'''
        result = self._values.get("target_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vpc_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#vpc_id LbTargetGroup#vpc_id}.'''
        result = self._values.get("vpc_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LbTargetGroupConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.lbTargetGroup.LbTargetGroupHealthCheck",
    jsii_struct_bases=[],
    name_mapping={
        "enabled": "enabled",
        "healthy_threshold": "healthyThreshold",
        "interval": "interval",
        "matcher": "matcher",
        "path": "path",
        "port": "port",
        "protocol": "protocol",
        "timeout": "timeout",
        "unhealthy_threshold": "unhealthyThreshold",
    },
)
class LbTargetGroupHealthCheck:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        healthy_threshold: typing.Optional[jsii.Number] = None,
        interval: typing.Optional[jsii.Number] = None,
        matcher: typing.Optional[builtins.str] = None,
        path: typing.Optional[builtins.str] = None,
        port: typing.Optional[builtins.str] = None,
        protocol: typing.Optional[builtins.str] = None,
        timeout: typing.Optional[jsii.Number] = None,
        unhealthy_threshold: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#enabled LbTargetGroup#enabled}.
        :param healthy_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#healthy_threshold LbTargetGroup#healthy_threshold}.
        :param interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#interval LbTargetGroup#interval}.
        :param matcher: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#matcher LbTargetGroup#matcher}.
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#path LbTargetGroup#path}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#port LbTargetGroup#port}.
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#protocol LbTargetGroup#protocol}.
        :param timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#timeout LbTargetGroup#timeout}.
        :param unhealthy_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#unhealthy_threshold LbTargetGroup#unhealthy_threshold}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__484da0892cafde33064fd0bc23311c40d7426b666a61a1c3f973ed2790d82af0)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument healthy_threshold", value=healthy_threshold, expected_type=type_hints["healthy_threshold"])
            check_type(argname="argument interval", value=interval, expected_type=type_hints["interval"])
            check_type(argname="argument matcher", value=matcher, expected_type=type_hints["matcher"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
            check_type(argname="argument unhealthy_threshold", value=unhealthy_threshold, expected_type=type_hints["unhealthy_threshold"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled
        if healthy_threshold is not None:
            self._values["healthy_threshold"] = healthy_threshold
        if interval is not None:
            self._values["interval"] = interval
        if matcher is not None:
            self._values["matcher"] = matcher
        if path is not None:
            self._values["path"] = path
        if port is not None:
            self._values["port"] = port
        if protocol is not None:
            self._values["protocol"] = protocol
        if timeout is not None:
            self._values["timeout"] = timeout
        if unhealthy_threshold is not None:
            self._values["unhealthy_threshold"] = unhealthy_threshold

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#enabled LbTargetGroup#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def healthy_threshold(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#healthy_threshold LbTargetGroup#healthy_threshold}.'''
        result = self._values.get("healthy_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def interval(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#interval LbTargetGroup#interval}.'''
        result = self._values.get("interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def matcher(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#matcher LbTargetGroup#matcher}.'''
        result = self._values.get("matcher")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#path LbTargetGroup#path}.'''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#port LbTargetGroup#port}.'''
        result = self._values.get("port")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def protocol(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#protocol LbTargetGroup#protocol}.'''
        result = self._values.get("protocol")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeout(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#timeout LbTargetGroup#timeout}.'''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def unhealthy_threshold(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#unhealthy_threshold LbTargetGroup#unhealthy_threshold}.'''
        result = self._values.get("unhealthy_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LbTargetGroupHealthCheck(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LbTargetGroupHealthCheckOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lbTargetGroup.LbTargetGroupHealthCheckOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e79a711f6795878f224c462ea913b9c9e304121112cfee46b6579bc113377af0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetHealthyThreshold")
    def reset_healthy_threshold(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHealthyThreshold", []))

    @jsii.member(jsii_name="resetInterval")
    def reset_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInterval", []))

    @jsii.member(jsii_name="resetMatcher")
    def reset_matcher(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatcher", []))

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @jsii.member(jsii_name="resetPort")
    def reset_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPort", []))

    @jsii.member(jsii_name="resetProtocol")
    def reset_protocol(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProtocol", []))

    @jsii.member(jsii_name="resetTimeout")
    def reset_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeout", []))

    @jsii.member(jsii_name="resetUnhealthyThreshold")
    def reset_unhealthy_threshold(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUnhealthyThreshold", []))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="healthyThresholdInput")
    def healthy_threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "healthyThresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="intervalInput")
    def interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "intervalInput"))

    @builtins.property
    @jsii.member(jsii_name="matcherInput")
    def matcher_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "matcherInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolInput")
    def protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocolInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutInput")
    def timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "timeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="unhealthyThresholdInput")
    def unhealthy_threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "unhealthyThresholdInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__88361a00174ab9a754c4a58c93e21d1eb18858264a6d70f9a67da1f5e639e80d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="healthyThreshold")
    def healthy_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "healthyThreshold"))

    @healthy_threshold.setter
    def healthy_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9e1fe53edee6dca6f0ae3f51f0133d52baa57a8a3d4686587a380cdaa22bf6e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "healthyThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="interval")
    def interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "interval"))

    @interval.setter
    def interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab7fadb2d1923588fae4740ab268021628815a1e112c52966460d28ee7e82d43)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "interval", value)

    @builtins.property
    @jsii.member(jsii_name="matcher")
    def matcher(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "matcher"))

    @matcher.setter
    def matcher(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5e9d02fe57662168c34995b745ff73cf8f0f37f896acaf7b2eba247a481b6e5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matcher", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb6216cb991826dfbd96588a3ab55500584e3d059a1714c4225243d1454a08fc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "port"))

    @port.setter
    def port(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cfb840b88280460e193fdc0c7f4012406f5ae172674724351d7e3ab4487b3952)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26023c54e087d6c096af34895cabb80e517eb53874add085d4b1d01365071d70)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="timeout")
    def timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "timeout"))

    @timeout.setter
    def timeout(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02d664a978e56466af2544c965dba1f9afed7b6032d23e0497860d02af613fe7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeout", value)

    @builtins.property
    @jsii.member(jsii_name="unhealthyThreshold")
    def unhealthy_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "unhealthyThreshold"))

    @unhealthy_threshold.setter
    def unhealthy_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2a38ca1d1bc845c31aea3514e3b9af68c5068693852fe6b350e3981f1c43ad6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unhealthyThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LbTargetGroupHealthCheck]:
        return typing.cast(typing.Optional[LbTargetGroupHealthCheck], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[LbTargetGroupHealthCheck]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02ec03aa13d904a21838b71feeb828f04ee9c2ba0c37956232d034bba01e6305)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.lbTargetGroup.LbTargetGroupStickiness",
    jsii_struct_bases=[],
    name_mapping={
        "type": "type",
        "cookie_duration": "cookieDuration",
        "cookie_name": "cookieName",
        "enabled": "enabled",
    },
)
class LbTargetGroupStickiness:
    def __init__(
        self,
        *,
        type: builtins.str,
        cookie_duration: typing.Optional[jsii.Number] = None,
        cookie_name: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#type LbTargetGroup#type}.
        :param cookie_duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#cookie_duration LbTargetGroup#cookie_duration}.
        :param cookie_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#cookie_name LbTargetGroup#cookie_name}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#enabled LbTargetGroup#enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c730bb0f40b0d136c252c28bfa117c5d3ac66c0a151463194a6c032fd5951ca)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument cookie_duration", value=cookie_duration, expected_type=type_hints["cookie_duration"])
            check_type(argname="argument cookie_name", value=cookie_name, expected_type=type_hints["cookie_name"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }
        if cookie_duration is not None:
            self._values["cookie_duration"] = cookie_duration
        if cookie_name is not None:
            self._values["cookie_name"] = cookie_name
        if enabled is not None:
            self._values["enabled"] = enabled

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#type LbTargetGroup#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cookie_duration(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#cookie_duration LbTargetGroup#cookie_duration}.'''
        result = self._values.get("cookie_duration")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def cookie_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#cookie_name LbTargetGroup#cookie_name}.'''
        result = self._values.get("cookie_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#enabled LbTargetGroup#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LbTargetGroupStickiness(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LbTargetGroupStickinessOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lbTargetGroup.LbTargetGroupStickinessOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a43c5da68cea4a17633f5d7554000fd83ef219d1d5f0af7a47cb103ae3cc0206)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCookieDuration")
    def reset_cookie_duration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCookieDuration", []))

    @jsii.member(jsii_name="resetCookieName")
    def reset_cookie_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCookieName", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @builtins.property
    @jsii.member(jsii_name="cookieDurationInput")
    def cookie_duration_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "cookieDurationInput"))

    @builtins.property
    @jsii.member(jsii_name="cookieNameInput")
    def cookie_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cookieNameInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="cookieDuration")
    def cookie_duration(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "cookieDuration"))

    @cookie_duration.setter
    def cookie_duration(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21ff0109fd2c8f319bcac34a381ed80d670b564070d8e3753d3daf60cc38ec3f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cookieDuration", value)

    @builtins.property
    @jsii.member(jsii_name="cookieName")
    def cookie_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cookieName"))

    @cookie_name.setter
    def cookie_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e91b0c477fdb92bc53ffdaa6ded8faf6b4e465198217947faadb7e1a311a6517)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cookieName", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__ed781971bec835b22c08dc31b396a8ba7b74d127fe5dd444089bd17ec307ba1e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de7b2bdeb55f2786ff43c1c7aa5a3bbb7d2855da798ec8886c8a81bf722119bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LbTargetGroupStickiness]:
        return typing.cast(typing.Optional[LbTargetGroupStickiness], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[LbTargetGroupStickiness]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2eb481171d6d2791fc41dd76491dc9ced1b6d4d9a3aa336a6542ebcc8ebb8abd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.lbTargetGroup.LbTargetGroupTargetFailover",
    jsii_struct_bases=[],
    name_mapping={
        "on_deregistration": "onDeregistration",
        "on_unhealthy": "onUnhealthy",
    },
)
class LbTargetGroupTargetFailover:
    def __init__(
        self,
        *,
        on_deregistration: builtins.str,
        on_unhealthy: builtins.str,
    ) -> None:
        '''
        :param on_deregistration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#on_deregistration LbTargetGroup#on_deregistration}.
        :param on_unhealthy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#on_unhealthy LbTargetGroup#on_unhealthy}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ebd9d3b91b32b19bf18dc83d906597df545e32c208089581f9c02bf450ecec67)
            check_type(argname="argument on_deregistration", value=on_deregistration, expected_type=type_hints["on_deregistration"])
            check_type(argname="argument on_unhealthy", value=on_unhealthy, expected_type=type_hints["on_unhealthy"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "on_deregistration": on_deregistration,
            "on_unhealthy": on_unhealthy,
        }

    @builtins.property
    def on_deregistration(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#on_deregistration LbTargetGroup#on_deregistration}.'''
        result = self._values.get("on_deregistration")
        assert result is not None, "Required property 'on_deregistration' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def on_unhealthy(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_target_group#on_unhealthy LbTargetGroup#on_unhealthy}.'''
        result = self._values.get("on_unhealthy")
        assert result is not None, "Required property 'on_unhealthy' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LbTargetGroupTargetFailover(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LbTargetGroupTargetFailoverList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lbTargetGroup.LbTargetGroupTargetFailoverList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__05805188df6933cd6ac3009c90289e41f9d7e969b7823b386e3a61f61a1de83d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "LbTargetGroupTargetFailoverOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b2aae9d7ac3215f4cf6f86638d1d5d9856f26770358d6bb4b6dfcc09d136c7a)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LbTargetGroupTargetFailoverOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0dae27d7258083ca070c9b5b18eddaaf94cbb4ce545148a00370e02b464f90b1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b6db678584d458b176951ad2a6c6e8a15968f3166cdde635c197c39d2ac56164)
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
            type_hints = typing.get_type_hints(_typecheckingstub__eb843cdabc0e3d852f04e40ef4a3551675a39a12f9c5783841d4aca64cdfe68d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LbTargetGroupTargetFailover]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LbTargetGroupTargetFailover]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LbTargetGroupTargetFailover]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5fd192ee150e7cb64b5e1238d378aa7beb878ad9f33e5c5a4ea0e2f046b4316d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LbTargetGroupTargetFailoverOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lbTargetGroup.LbTargetGroupTargetFailoverOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5d77d93beff97b193553aa09401e553c4d884ea7b94189ec180510ce26394b1c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="onDeregistrationInput")
    def on_deregistration_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "onDeregistrationInput"))

    @builtins.property
    @jsii.member(jsii_name="onUnhealthyInput")
    def on_unhealthy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "onUnhealthyInput"))

    @builtins.property
    @jsii.member(jsii_name="onDeregistration")
    def on_deregistration(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "onDeregistration"))

    @on_deregistration.setter
    def on_deregistration(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__30e89d97fbde9bde5d64efbb005894f9826c8ed7aaece304508e6948a130bdbd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "onDeregistration", value)

    @builtins.property
    @jsii.member(jsii_name="onUnhealthy")
    def on_unhealthy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "onUnhealthy"))

    @on_unhealthy.setter
    def on_unhealthy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__110c9492e0559ff0b8c94629d0f68a69ff2d25a3518712eb4a9e9e133472f8f1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "onUnhealthy", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LbTargetGroupTargetFailover, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LbTargetGroupTargetFailover, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LbTargetGroupTargetFailover, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe6037df95b571bca5585e7de5ff52c707b14856f8f496c13d5d5a1835bbb664)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "LbTargetGroup",
    "LbTargetGroupConfig",
    "LbTargetGroupHealthCheck",
    "LbTargetGroupHealthCheckOutputReference",
    "LbTargetGroupStickiness",
    "LbTargetGroupStickinessOutputReference",
    "LbTargetGroupTargetFailover",
    "LbTargetGroupTargetFailoverList",
    "LbTargetGroupTargetFailoverOutputReference",
]

publication.publish()

def _typecheckingstub__f79e2265cfb634c62980845c8a8d7446a23f259229c1a34d4b17eff506dc9b4d(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    connection_termination: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    deregistration_delay: typing.Optional[builtins.str] = None,
    health_check: typing.Optional[typing.Union[LbTargetGroupHealthCheck, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    ip_address_type: typing.Optional[builtins.str] = None,
    lambda_multi_value_headers_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    load_balancing_algorithm_type: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    name_prefix: typing.Optional[builtins.str] = None,
    port: typing.Optional[jsii.Number] = None,
    preserve_client_ip: typing.Optional[builtins.str] = None,
    protocol: typing.Optional[builtins.str] = None,
    protocol_version: typing.Optional[builtins.str] = None,
    proxy_protocol_v2: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    slow_start: typing.Optional[jsii.Number] = None,
    stickiness: typing.Optional[typing.Union[LbTargetGroupStickiness, typing.Dict[builtins.str, typing.Any]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    target_failover: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LbTargetGroupTargetFailover, typing.Dict[builtins.str, typing.Any]]]]] = None,
    target_type: typing.Optional[builtins.str] = None,
    vpc_id: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__d0fc68ae5d4029db6b2ddb4dfed075be1933db34abd5c238ea6a161ad7e66c6d(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LbTargetGroupTargetFailover, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__307923bbb0664d88b3bb002c7122f7ac1860a32ba3eab0c08dd28a57a3a12fc3(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__954baff4e50fed24f6b10fa7b70528b6c26c9da05260c3030ba03a796bfc8f7d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5a0a76e75afefa07dac4fb9388c5a96f22e82fc453f754dd5162ae47820c76c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c1af20432fd82ae52c4ecdcf636e5e692a0f1f968fc43e05576fa5237e27b00(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e73f56c9cb022f2b251ad0999aab3ea01970d6dedad2ef68fe98ad15b7de34ab(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8399ca07d6628acd76771c6ec9be4c9eafee50eddd2ae364f08e0888b19d68f6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38dc1c098beab16c4f9f4170ff64ca13ad0ebd0f20242e9d227734ded04e90d8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3504871caac871d0e716f49aa225ae60dfe4a5a909bd88364fff8504f3f7f0e7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc97bce0545f1766d75f51cd0abac026facfc1d652226f690a1434e4770dd4aa(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8a015023bd1625e36b02c2470793875451d0e099dd758402d0ea788867c1e08(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ef4357770b94bbebd388d81f986b7ccedc371ae2d04fb9d9eeb5b23d6986f79(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ac01eb2c42c6b9f0ab444d042477ccea77cbf970ddc353204d0bb32fc10927a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33a8163976f84cd90322bc526107f6125a4994ffbd98cc5a240e7173ae46f787(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db550c83576105eaf06c09bf250e57ff9e2d6d52336e4377281553a659911d25(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5dca32396a583cd54ed4d2f88bbe6fe0244437af7481cc348747d76d4c03588b(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee7e66f863bbe94ba4754b5eddc033e72a96c9334c77a33bf0c2a4d5978dfbc8(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__daf83572a42727d65ff26b61a4818c5939d1bf70d027ebfc7a07a3fc02ede9a5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa53a18cb287ddbb69e1c3d1bfa728666e862a76938ca3fa436b077a13cad7eb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9248f3c06fcd83fd2681d369fecb90bf3d1f2fcb77a1265607c49f2f590b6704(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    connection_termination: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    deregistration_delay: typing.Optional[builtins.str] = None,
    health_check: typing.Optional[typing.Union[LbTargetGroupHealthCheck, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    ip_address_type: typing.Optional[builtins.str] = None,
    lambda_multi_value_headers_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    load_balancing_algorithm_type: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    name_prefix: typing.Optional[builtins.str] = None,
    port: typing.Optional[jsii.Number] = None,
    preserve_client_ip: typing.Optional[builtins.str] = None,
    protocol: typing.Optional[builtins.str] = None,
    protocol_version: typing.Optional[builtins.str] = None,
    proxy_protocol_v2: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    slow_start: typing.Optional[jsii.Number] = None,
    stickiness: typing.Optional[typing.Union[LbTargetGroupStickiness, typing.Dict[builtins.str, typing.Any]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    target_failover: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LbTargetGroupTargetFailover, typing.Dict[builtins.str, typing.Any]]]]] = None,
    target_type: typing.Optional[builtins.str] = None,
    vpc_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__484da0892cafde33064fd0bc23311c40d7426b666a61a1c3f973ed2790d82af0(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    healthy_threshold: typing.Optional[jsii.Number] = None,
    interval: typing.Optional[jsii.Number] = None,
    matcher: typing.Optional[builtins.str] = None,
    path: typing.Optional[builtins.str] = None,
    port: typing.Optional[builtins.str] = None,
    protocol: typing.Optional[builtins.str] = None,
    timeout: typing.Optional[jsii.Number] = None,
    unhealthy_threshold: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e79a711f6795878f224c462ea913b9c9e304121112cfee46b6579bc113377af0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88361a00174ab9a754c4a58c93e21d1eb18858264a6d70f9a67da1f5e639e80d(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9e1fe53edee6dca6f0ae3f51f0133d52baa57a8a3d4686587a380cdaa22bf6e(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab7fadb2d1923588fae4740ab268021628815a1e112c52966460d28ee7e82d43(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5e9d02fe57662168c34995b745ff73cf8f0f37f896acaf7b2eba247a481b6e5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb6216cb991826dfbd96588a3ab55500584e3d059a1714c4225243d1454a08fc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfb840b88280460e193fdc0c7f4012406f5ae172674724351d7e3ab4487b3952(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26023c54e087d6c096af34895cabb80e517eb53874add085d4b1d01365071d70(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02d664a978e56466af2544c965dba1f9afed7b6032d23e0497860d02af613fe7(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2a38ca1d1bc845c31aea3514e3b9af68c5068693852fe6b350e3981f1c43ad6(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02ec03aa13d904a21838b71feeb828f04ee9c2ba0c37956232d034bba01e6305(
    value: typing.Optional[LbTargetGroupHealthCheck],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c730bb0f40b0d136c252c28bfa117c5d3ac66c0a151463194a6c032fd5951ca(
    *,
    type: builtins.str,
    cookie_duration: typing.Optional[jsii.Number] = None,
    cookie_name: typing.Optional[builtins.str] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a43c5da68cea4a17633f5d7554000fd83ef219d1d5f0af7a47cb103ae3cc0206(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21ff0109fd2c8f319bcac34a381ed80d670b564070d8e3753d3daf60cc38ec3f(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e91b0c477fdb92bc53ffdaa6ded8faf6b4e465198217947faadb7e1a311a6517(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed781971bec835b22c08dc31b396a8ba7b74d127fe5dd444089bd17ec307ba1e(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de7b2bdeb55f2786ff43c1c7aa5a3bbb7d2855da798ec8886c8a81bf722119bc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2eb481171d6d2791fc41dd76491dc9ced1b6d4d9a3aa336a6542ebcc8ebb8abd(
    value: typing.Optional[LbTargetGroupStickiness],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ebd9d3b91b32b19bf18dc83d906597df545e32c208089581f9c02bf450ecec67(
    *,
    on_deregistration: builtins.str,
    on_unhealthy: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05805188df6933cd6ac3009c90289e41f9d7e969b7823b386e3a61f61a1de83d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b2aae9d7ac3215f4cf6f86638d1d5d9856f26770358d6bb4b6dfcc09d136c7a(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0dae27d7258083ca070c9b5b18eddaaf94cbb4ce545148a00370e02b464f90b1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6db678584d458b176951ad2a6c6e8a15968f3166cdde635c197c39d2ac56164(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb843cdabc0e3d852f04e40ef4a3551675a39a12f9c5783841d4aca64cdfe68d(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5fd192ee150e7cb64b5e1238d378aa7beb878ad9f33e5c5a4ea0e2f046b4316d(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LbTargetGroupTargetFailover]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d77d93beff97b193553aa09401e553c4d884ea7b94189ec180510ce26394b1c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30e89d97fbde9bde5d64efbb005894f9826c8ed7aaece304508e6948a130bdbd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__110c9492e0559ff0b8c94629d0f68a69ff2d25a3518712eb4a9e9e133472f8f1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe6037df95b571bca5585e7de5ff52c707b14856f8f496c13d5d5a1835bbb664(
    value: typing.Optional[typing.Union[LbTargetGroupTargetFailover, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
