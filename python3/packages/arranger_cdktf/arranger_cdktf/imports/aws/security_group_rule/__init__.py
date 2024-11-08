'''
# `aws_security_group_rule`

Refer to the Terraform Registory for docs: [`aws_security_group_rule`](https://www.terraform.io/docs/providers/aws/r/security_group_rule).
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


class SecurityGroupRule(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.securityGroupRule.SecurityGroupRule",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/security_group_rule aws_security_group_rule}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        from_port: jsii.Number,
        protocol: builtins.str,
        security_group_id: builtins.str,
        to_port: jsii.Number,
        type: builtins.str,
        cidr_blocks: typing.Optional[typing.Sequence[builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        ipv6_cidr_blocks: typing.Optional[typing.Sequence[builtins.str]] = None,
        prefix_list_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        self_attribute: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        source_security_group_id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["SecurityGroupRuleTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/security_group_rule aws_security_group_rule} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param from_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/security_group_rule#from_port SecurityGroupRule#from_port}.
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/security_group_rule#protocol SecurityGroupRule#protocol}.
        :param security_group_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/security_group_rule#security_group_id SecurityGroupRule#security_group_id}.
        :param to_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/security_group_rule#to_port SecurityGroupRule#to_port}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/security_group_rule#type SecurityGroupRule#type}.
        :param cidr_blocks: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/security_group_rule#cidr_blocks SecurityGroupRule#cidr_blocks}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/security_group_rule#description SecurityGroupRule#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/security_group_rule#id SecurityGroupRule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ipv6_cidr_blocks: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/security_group_rule#ipv6_cidr_blocks SecurityGroupRule#ipv6_cidr_blocks}.
        :param prefix_list_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/security_group_rule#prefix_list_ids SecurityGroupRule#prefix_list_ids}.
        :param self_attribute: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/security_group_rule#self SecurityGroupRule#self}.
        :param source_security_group_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/security_group_rule#source_security_group_id SecurityGroupRule#source_security_group_id}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/security_group_rule#timeouts SecurityGroupRule#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5fa3df0b3f6b3ae3c6d91609fce3906c1d1947cbb577481d0619553a66f8f14f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = SecurityGroupRuleConfig(
            from_port=from_port,
            protocol=protocol,
            security_group_id=security_group_id,
            to_port=to_port,
            type=type,
            cidr_blocks=cidr_blocks,
            description=description,
            id=id,
            ipv6_cidr_blocks=ipv6_cidr_blocks,
            prefix_list_ids=prefix_list_ids,
            self_attribute=self_attribute,
            source_security_group_id=source_security_group_id,
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

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(self, *, create: typing.Optional[builtins.str] = None) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/security_group_rule#create SecurityGroupRule#create}.
        '''
        value = SecurityGroupRuleTimeouts(create=create)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetCidrBlocks")
    def reset_cidr_blocks(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCidrBlocks", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIpv6CidrBlocks")
    def reset_ipv6_cidr_blocks(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpv6CidrBlocks", []))

    @jsii.member(jsii_name="resetPrefixListIds")
    def reset_prefix_list_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrefixListIds", []))

    @jsii.member(jsii_name="resetSelfAttribute")
    def reset_self_attribute(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSelfAttribute", []))

    @jsii.member(jsii_name="resetSourceSecurityGroupId")
    def reset_source_security_group_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceSecurityGroupId", []))

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
    @jsii.member(jsii_name="securityGroupRuleId")
    def security_group_rule_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "securityGroupRuleId"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "SecurityGroupRuleTimeoutsOutputReference":
        return typing.cast("SecurityGroupRuleTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="cidrBlocksInput")
    def cidr_blocks_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "cidrBlocksInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="fromPortInput")
    def from_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "fromPortInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="ipv6CidrBlocksInput")
    def ipv6_cidr_blocks_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "ipv6CidrBlocksInput"))

    @builtins.property
    @jsii.member(jsii_name="prefixListIdsInput")
    def prefix_list_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "prefixListIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolInput")
    def protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocolInput"))

    @builtins.property
    @jsii.member(jsii_name="securityGroupIdInput")
    def security_group_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "securityGroupIdInput"))

    @builtins.property
    @jsii.member(jsii_name="selfAttributeInput")
    def self_attribute_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "selfAttributeInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceSecurityGroupIdInput")
    def source_security_group_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceSecurityGroupIdInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["SecurityGroupRuleTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["SecurityGroupRuleTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="toPortInput")
    def to_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "toPortInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="cidrBlocks")
    def cidr_blocks(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "cidrBlocks"))

    @cidr_blocks.setter
    def cidr_blocks(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21fd737920f8388cadf277a02a64a6f2b5d83d82c3ffe717e2f90cd874c10214)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cidrBlocks", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a7727365843130fec0fbe34ae82f63ac34db9d55f6f5bec5553129fa59c0548)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="fromPort")
    def from_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "fromPort"))

    @from_port.setter
    def from_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d6bceb2a2f5cf6af9d14eb5d6b6b03df1cd851eb408dd322e32644d7b0f0874)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fromPort", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a8b180ab3eebfc360629c344f310144c5aa26bcb2cf4d3a074461c85154091dd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="ipv6CidrBlocks")
    def ipv6_cidr_blocks(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "ipv6CidrBlocks"))

    @ipv6_cidr_blocks.setter
    def ipv6_cidr_blocks(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fbca8c98850dd67b2d2c571e5398c8278851456de09a155694e72dd2580b2428)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipv6CidrBlocks", value)

    @builtins.property
    @jsii.member(jsii_name="prefixListIds")
    def prefix_list_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "prefixListIds"))

    @prefix_list_ids.setter
    def prefix_list_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad68e1ea79eb425aa6379a57817e41d7b43180307751bf6fbb39409ac4799335)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefixListIds", value)

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__902691b601ac092181ede371ebe91544b4f406e7e6f06d2452e4d8ee6ed5b746)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="securityGroupId")
    def security_group_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "securityGroupId"))

    @security_group_id.setter
    def security_group_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c94fb30e404fc25d037c05f461634e5a8d4cd9ab4d418220fc7ca1fc54aa40d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroupId", value)

    @builtins.property
    @jsii.member(jsii_name="selfAttribute")
    def self_attribute(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "selfAttribute"))

    @self_attribute.setter
    def self_attribute(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__496881e5e57dc9ec8a74463a862db44e6e136df2a3d9e7d78567dacb4b2aa4e5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "selfAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="sourceSecurityGroupId")
    def source_security_group_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceSecurityGroupId"))

    @source_security_group_id.setter
    def source_security_group_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__723e3592a953333f7c582293ab88f1f0ac90d17553d53040d82a67cbc989a82a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceSecurityGroupId", value)

    @builtins.property
    @jsii.member(jsii_name="toPort")
    def to_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "toPort"))

    @to_port.setter
    def to_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__369dd76a144add526572e4aa6dcc484253f9245e6cef6c7a02dcb469a5191075)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "toPort", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2652847173c48c01e9ee1e151f9bb78989683432fd87509ee591cb0143f0c1a3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)


@jsii.data_type(
    jsii_type="aws.securityGroupRule.SecurityGroupRuleConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "from_port": "fromPort",
        "protocol": "protocol",
        "security_group_id": "securityGroupId",
        "to_port": "toPort",
        "type": "type",
        "cidr_blocks": "cidrBlocks",
        "description": "description",
        "id": "id",
        "ipv6_cidr_blocks": "ipv6CidrBlocks",
        "prefix_list_ids": "prefixListIds",
        "self_attribute": "selfAttribute",
        "source_security_group_id": "sourceSecurityGroupId",
        "timeouts": "timeouts",
    },
)
class SecurityGroupRuleConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        from_port: jsii.Number,
        protocol: builtins.str,
        security_group_id: builtins.str,
        to_port: jsii.Number,
        type: builtins.str,
        cidr_blocks: typing.Optional[typing.Sequence[builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        ipv6_cidr_blocks: typing.Optional[typing.Sequence[builtins.str]] = None,
        prefix_list_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        self_attribute: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        source_security_group_id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["SecurityGroupRuleTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param from_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/security_group_rule#from_port SecurityGroupRule#from_port}.
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/security_group_rule#protocol SecurityGroupRule#protocol}.
        :param security_group_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/security_group_rule#security_group_id SecurityGroupRule#security_group_id}.
        :param to_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/security_group_rule#to_port SecurityGroupRule#to_port}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/security_group_rule#type SecurityGroupRule#type}.
        :param cidr_blocks: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/security_group_rule#cidr_blocks SecurityGroupRule#cidr_blocks}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/security_group_rule#description SecurityGroupRule#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/security_group_rule#id SecurityGroupRule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ipv6_cidr_blocks: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/security_group_rule#ipv6_cidr_blocks SecurityGroupRule#ipv6_cidr_blocks}.
        :param prefix_list_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/security_group_rule#prefix_list_ids SecurityGroupRule#prefix_list_ids}.
        :param self_attribute: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/security_group_rule#self SecurityGroupRule#self}.
        :param source_security_group_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/security_group_rule#source_security_group_id SecurityGroupRule#source_security_group_id}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/security_group_rule#timeouts SecurityGroupRule#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = SecurityGroupRuleTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b20f2a254e4be8726e9237ba180e3c2f20746f9b6fbb6970022d33ad2f357c50)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument from_port", value=from_port, expected_type=type_hints["from_port"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument security_group_id", value=security_group_id, expected_type=type_hints["security_group_id"])
            check_type(argname="argument to_port", value=to_port, expected_type=type_hints["to_port"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument cidr_blocks", value=cidr_blocks, expected_type=type_hints["cidr_blocks"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument ipv6_cidr_blocks", value=ipv6_cidr_blocks, expected_type=type_hints["ipv6_cidr_blocks"])
            check_type(argname="argument prefix_list_ids", value=prefix_list_ids, expected_type=type_hints["prefix_list_ids"])
            check_type(argname="argument self_attribute", value=self_attribute, expected_type=type_hints["self_attribute"])
            check_type(argname="argument source_security_group_id", value=source_security_group_id, expected_type=type_hints["source_security_group_id"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "from_port": from_port,
            "protocol": protocol,
            "security_group_id": security_group_id,
            "to_port": to_port,
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
        if cidr_blocks is not None:
            self._values["cidr_blocks"] = cidr_blocks
        if description is not None:
            self._values["description"] = description
        if id is not None:
            self._values["id"] = id
        if ipv6_cidr_blocks is not None:
            self._values["ipv6_cidr_blocks"] = ipv6_cidr_blocks
        if prefix_list_ids is not None:
            self._values["prefix_list_ids"] = prefix_list_ids
        if self_attribute is not None:
            self._values["self_attribute"] = self_attribute
        if source_security_group_id is not None:
            self._values["source_security_group_id"] = source_security_group_id
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
    def from_port(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/security_group_rule#from_port SecurityGroupRule#from_port}.'''
        result = self._values.get("from_port")
        assert result is not None, "Required property 'from_port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def protocol(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/security_group_rule#protocol SecurityGroupRule#protocol}.'''
        result = self._values.get("protocol")
        assert result is not None, "Required property 'protocol' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def security_group_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/security_group_rule#security_group_id SecurityGroupRule#security_group_id}.'''
        result = self._values.get("security_group_id")
        assert result is not None, "Required property 'security_group_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def to_port(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/security_group_rule#to_port SecurityGroupRule#to_port}.'''
        result = self._values.get("to_port")
        assert result is not None, "Required property 'to_port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/security_group_rule#type SecurityGroupRule#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cidr_blocks(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/security_group_rule#cidr_blocks SecurityGroupRule#cidr_blocks}.'''
        result = self._values.get("cidr_blocks")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/security_group_rule#description SecurityGroupRule#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/security_group_rule#id SecurityGroupRule#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ipv6_cidr_blocks(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/security_group_rule#ipv6_cidr_blocks SecurityGroupRule#ipv6_cidr_blocks}.'''
        result = self._values.get("ipv6_cidr_blocks")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def prefix_list_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/security_group_rule#prefix_list_ids SecurityGroupRule#prefix_list_ids}.'''
        result = self._values.get("prefix_list_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def self_attribute(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/security_group_rule#self SecurityGroupRule#self}.'''
        result = self._values.get("self_attribute")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def source_security_group_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/security_group_rule#source_security_group_id SecurityGroupRule#source_security_group_id}.'''
        result = self._values.get("source_security_group_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["SecurityGroupRuleTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/security_group_rule#timeouts SecurityGroupRule#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["SecurityGroupRuleTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SecurityGroupRuleConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.securityGroupRule.SecurityGroupRuleTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create"},
)
class SecurityGroupRuleTimeouts:
    def __init__(self, *, create: typing.Optional[builtins.str] = None) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/security_group_rule#create SecurityGroupRule#create}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29851237df67779f33733c573d75e88014b81aea646f424118717dd8083fa89d)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/security_group_rule#create SecurityGroupRule#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SecurityGroupRuleTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SecurityGroupRuleTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.securityGroupRule.SecurityGroupRuleTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4404bd9553bebb09553aaff689c598d3ac642000146f97992575a9317036ef5a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__bfcb3a5fd6553911668128b370d8be85863f911e4344024b399912fb499f9bcd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SecurityGroupRuleTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SecurityGroupRuleTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SecurityGroupRuleTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76d808493522fe3303ca553ff9d4d038956e222f3108d0732195f2bc791f290f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "SecurityGroupRule",
    "SecurityGroupRuleConfig",
    "SecurityGroupRuleTimeouts",
    "SecurityGroupRuleTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__5fa3df0b3f6b3ae3c6d91609fce3906c1d1947cbb577481d0619553a66f8f14f(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    from_port: jsii.Number,
    protocol: builtins.str,
    security_group_id: builtins.str,
    to_port: jsii.Number,
    type: builtins.str,
    cidr_blocks: typing.Optional[typing.Sequence[builtins.str]] = None,
    description: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    ipv6_cidr_blocks: typing.Optional[typing.Sequence[builtins.str]] = None,
    prefix_list_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    self_attribute: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    source_security_group_id: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[SecurityGroupRuleTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__21fd737920f8388cadf277a02a64a6f2b5d83d82c3ffe717e2f90cd874c10214(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a7727365843130fec0fbe34ae82f63ac34db9d55f6f5bec5553129fa59c0548(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d6bceb2a2f5cf6af9d14eb5d6b6b03df1cd851eb408dd322e32644d7b0f0874(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8b180ab3eebfc360629c344f310144c5aa26bcb2cf4d3a074461c85154091dd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fbca8c98850dd67b2d2c571e5398c8278851456de09a155694e72dd2580b2428(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad68e1ea79eb425aa6379a57817e41d7b43180307751bf6fbb39409ac4799335(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__902691b601ac092181ede371ebe91544b4f406e7e6f06d2452e4d8ee6ed5b746(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c94fb30e404fc25d037c05f461634e5a8d4cd9ab4d418220fc7ca1fc54aa40d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__496881e5e57dc9ec8a74463a862db44e6e136df2a3d9e7d78567dacb4b2aa4e5(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__723e3592a953333f7c582293ab88f1f0ac90d17553d53040d82a67cbc989a82a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__369dd76a144add526572e4aa6dcc484253f9245e6cef6c7a02dcb469a5191075(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2652847173c48c01e9ee1e151f9bb78989683432fd87509ee591cb0143f0c1a3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b20f2a254e4be8726e9237ba180e3c2f20746f9b6fbb6970022d33ad2f357c50(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    from_port: jsii.Number,
    protocol: builtins.str,
    security_group_id: builtins.str,
    to_port: jsii.Number,
    type: builtins.str,
    cidr_blocks: typing.Optional[typing.Sequence[builtins.str]] = None,
    description: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    ipv6_cidr_blocks: typing.Optional[typing.Sequence[builtins.str]] = None,
    prefix_list_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    self_attribute: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    source_security_group_id: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[SecurityGroupRuleTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29851237df67779f33733c573d75e88014b81aea646f424118717dd8083fa89d(
    *,
    create: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4404bd9553bebb09553aaff689c598d3ac642000146f97992575a9317036ef5a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bfcb3a5fd6553911668128b370d8be85863f911e4344024b399912fb499f9bcd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76d808493522fe3303ca553ff9d4d038956e222f3108d0732195f2bc791f290f(
    value: typing.Optional[typing.Union[SecurityGroupRuleTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
