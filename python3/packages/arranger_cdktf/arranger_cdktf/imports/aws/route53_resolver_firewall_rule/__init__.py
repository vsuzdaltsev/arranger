'''
# `aws_route53_resolver_firewall_rule`

Refer to the Terraform Registory for docs: [`aws_route53_resolver_firewall_rule`](https://www.terraform.io/docs/providers/aws/r/route53_resolver_firewall_rule).
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


class Route53ResolverFirewallRule(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.route53ResolverFirewallRule.Route53ResolverFirewallRule",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/route53_resolver_firewall_rule aws_route53_resolver_firewall_rule}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        action: builtins.str,
        firewall_domain_list_id: builtins.str,
        firewall_rule_group_id: builtins.str,
        name: builtins.str,
        priority: jsii.Number,
        block_override_dns_type: typing.Optional[builtins.str] = None,
        block_override_domain: typing.Optional[builtins.str] = None,
        block_override_ttl: typing.Optional[jsii.Number] = None,
        block_response: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/route53_resolver_firewall_rule aws_route53_resolver_firewall_rule} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53_resolver_firewall_rule#action Route53ResolverFirewallRule#action}.
        :param firewall_domain_list_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53_resolver_firewall_rule#firewall_domain_list_id Route53ResolverFirewallRule#firewall_domain_list_id}.
        :param firewall_rule_group_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53_resolver_firewall_rule#firewall_rule_group_id Route53ResolverFirewallRule#firewall_rule_group_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53_resolver_firewall_rule#name Route53ResolverFirewallRule#name}.
        :param priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53_resolver_firewall_rule#priority Route53ResolverFirewallRule#priority}.
        :param block_override_dns_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53_resolver_firewall_rule#block_override_dns_type Route53ResolverFirewallRule#block_override_dns_type}.
        :param block_override_domain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53_resolver_firewall_rule#block_override_domain Route53ResolverFirewallRule#block_override_domain}.
        :param block_override_ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53_resolver_firewall_rule#block_override_ttl Route53ResolverFirewallRule#block_override_ttl}.
        :param block_response: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53_resolver_firewall_rule#block_response Route53ResolverFirewallRule#block_response}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53_resolver_firewall_rule#id Route53ResolverFirewallRule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b179a3c57843fe43e65223d6891c3aa4f54e3d1996a0e4cb2f2ab570f364b47e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = Route53ResolverFirewallRuleConfig(
            action=action,
            firewall_domain_list_id=firewall_domain_list_id,
            firewall_rule_group_id=firewall_rule_group_id,
            name=name,
            priority=priority,
            block_override_dns_type=block_override_dns_type,
            block_override_domain=block_override_domain,
            block_override_ttl=block_override_ttl,
            block_response=block_response,
            id=id,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetBlockOverrideDnsType")
    def reset_block_override_dns_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBlockOverrideDnsType", []))

    @jsii.member(jsii_name="resetBlockOverrideDomain")
    def reset_block_override_domain(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBlockOverrideDomain", []))

    @jsii.member(jsii_name="resetBlockOverrideTtl")
    def reset_block_override_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBlockOverrideTtl", []))

    @jsii.member(jsii_name="resetBlockResponse")
    def reset_block_response(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBlockResponse", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="blockOverrideDnsTypeInput")
    def block_override_dns_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "blockOverrideDnsTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="blockOverrideDomainInput")
    def block_override_domain_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "blockOverrideDomainInput"))

    @builtins.property
    @jsii.member(jsii_name="blockOverrideTtlInput")
    def block_override_ttl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "blockOverrideTtlInput"))

    @builtins.property
    @jsii.member(jsii_name="blockResponseInput")
    def block_response_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "blockResponseInput"))

    @builtins.property
    @jsii.member(jsii_name="firewallDomainListIdInput")
    def firewall_domain_list_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "firewallDomainListIdInput"))

    @builtins.property
    @jsii.member(jsii_name="firewallRuleGroupIdInput")
    def firewall_rule_group_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "firewallRuleGroupIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="priorityInput")
    def priority_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "priorityInput"))

    @builtins.property
    @jsii.member(jsii_name="action")
    def action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "action"))

    @action.setter
    def action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e193b1b7b157fee81f8c3e2c4db6cf8120ecfdbcde6820124e62c39d5401fd69)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "action", value)

    @builtins.property
    @jsii.member(jsii_name="blockOverrideDnsType")
    def block_override_dns_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "blockOverrideDnsType"))

    @block_override_dns_type.setter
    def block_override_dns_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__177c35e5a9f7eba1c2765d64c3e8fb861a4f6f148a73f864af7a2dbf6e55b36a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "blockOverrideDnsType", value)

    @builtins.property
    @jsii.member(jsii_name="blockOverrideDomain")
    def block_override_domain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "blockOverrideDomain"))

    @block_override_domain.setter
    def block_override_domain(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ef2f151e5f00a00df7602c98b26f2aa0006c1c1bc8528fd1df2f0300bb5c1c4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "blockOverrideDomain", value)

    @builtins.property
    @jsii.member(jsii_name="blockOverrideTtl")
    def block_override_ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "blockOverrideTtl"))

    @block_override_ttl.setter
    def block_override_ttl(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e29b8103cc1538de65c29d99c81f712639df17a7dca532859417bd76fdb29fc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "blockOverrideTtl", value)

    @builtins.property
    @jsii.member(jsii_name="blockResponse")
    def block_response(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "blockResponse"))

    @block_response.setter
    def block_response(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1436a6eea63ffa18c4fd65d6ecd037ecebd34ff1fa0b9d4811d5a635e145206b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "blockResponse", value)

    @builtins.property
    @jsii.member(jsii_name="firewallDomainListId")
    def firewall_domain_list_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "firewallDomainListId"))

    @firewall_domain_list_id.setter
    def firewall_domain_list_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a1e713d34227a7c02fc643aff4f39d70cd205a75b1c8b12133b32ab5a1ecf71)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "firewallDomainListId", value)

    @builtins.property
    @jsii.member(jsii_name="firewallRuleGroupId")
    def firewall_rule_group_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "firewallRuleGroupId"))

    @firewall_rule_group_id.setter
    def firewall_rule_group_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc6c15df898c523f28d227dc20814d90444c240a1d3a7f157b38feec8f709263)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "firewallRuleGroupId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9184a56fbd50301748b5bb6ee840879e855b664ef7abf0bb59d810104293b11)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b49702d861ef16315a006fac5ceed9fd1c847743b530e30b774b3cc5a5efac49)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d96f439fca9a3e8d07ab48e6fc1cf09cda119f30e90ccf5c280a819d8e70635)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)


@jsii.data_type(
    jsii_type="aws.route53ResolverFirewallRule.Route53ResolverFirewallRuleConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "action": "action",
        "firewall_domain_list_id": "firewallDomainListId",
        "firewall_rule_group_id": "firewallRuleGroupId",
        "name": "name",
        "priority": "priority",
        "block_override_dns_type": "blockOverrideDnsType",
        "block_override_domain": "blockOverrideDomain",
        "block_override_ttl": "blockOverrideTtl",
        "block_response": "blockResponse",
        "id": "id",
    },
)
class Route53ResolverFirewallRuleConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        action: builtins.str,
        firewall_domain_list_id: builtins.str,
        firewall_rule_group_id: builtins.str,
        name: builtins.str,
        priority: jsii.Number,
        block_override_dns_type: typing.Optional[builtins.str] = None,
        block_override_domain: typing.Optional[builtins.str] = None,
        block_override_ttl: typing.Optional[jsii.Number] = None,
        block_response: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53_resolver_firewall_rule#action Route53ResolverFirewallRule#action}.
        :param firewall_domain_list_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53_resolver_firewall_rule#firewall_domain_list_id Route53ResolverFirewallRule#firewall_domain_list_id}.
        :param firewall_rule_group_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53_resolver_firewall_rule#firewall_rule_group_id Route53ResolverFirewallRule#firewall_rule_group_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53_resolver_firewall_rule#name Route53ResolverFirewallRule#name}.
        :param priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53_resolver_firewall_rule#priority Route53ResolverFirewallRule#priority}.
        :param block_override_dns_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53_resolver_firewall_rule#block_override_dns_type Route53ResolverFirewallRule#block_override_dns_type}.
        :param block_override_domain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53_resolver_firewall_rule#block_override_domain Route53ResolverFirewallRule#block_override_domain}.
        :param block_override_ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53_resolver_firewall_rule#block_override_ttl Route53ResolverFirewallRule#block_override_ttl}.
        :param block_response: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53_resolver_firewall_rule#block_response Route53ResolverFirewallRule#block_response}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53_resolver_firewall_rule#id Route53ResolverFirewallRule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a524200b40c0ee6c85edf76e10c4fb2755ae441aafec5ba4d3cddcce4c7995c)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument firewall_domain_list_id", value=firewall_domain_list_id, expected_type=type_hints["firewall_domain_list_id"])
            check_type(argname="argument firewall_rule_group_id", value=firewall_rule_group_id, expected_type=type_hints["firewall_rule_group_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument block_override_dns_type", value=block_override_dns_type, expected_type=type_hints["block_override_dns_type"])
            check_type(argname="argument block_override_domain", value=block_override_domain, expected_type=type_hints["block_override_domain"])
            check_type(argname="argument block_override_ttl", value=block_override_ttl, expected_type=type_hints["block_override_ttl"])
            check_type(argname="argument block_response", value=block_response, expected_type=type_hints["block_response"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "action": action,
            "firewall_domain_list_id": firewall_domain_list_id,
            "firewall_rule_group_id": firewall_rule_group_id,
            "name": name,
            "priority": priority,
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
        if block_override_dns_type is not None:
            self._values["block_override_dns_type"] = block_override_dns_type
        if block_override_domain is not None:
            self._values["block_override_domain"] = block_override_domain
        if block_override_ttl is not None:
            self._values["block_override_ttl"] = block_override_ttl
        if block_response is not None:
            self._values["block_response"] = block_response
        if id is not None:
            self._values["id"] = id

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
    def action(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53_resolver_firewall_rule#action Route53ResolverFirewallRule#action}.'''
        result = self._values.get("action")
        assert result is not None, "Required property 'action' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def firewall_domain_list_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53_resolver_firewall_rule#firewall_domain_list_id Route53ResolverFirewallRule#firewall_domain_list_id}.'''
        result = self._values.get("firewall_domain_list_id")
        assert result is not None, "Required property 'firewall_domain_list_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def firewall_rule_group_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53_resolver_firewall_rule#firewall_rule_group_id Route53ResolverFirewallRule#firewall_rule_group_id}.'''
        result = self._values.get("firewall_rule_group_id")
        assert result is not None, "Required property 'firewall_rule_group_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53_resolver_firewall_rule#name Route53ResolverFirewallRule#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def priority(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53_resolver_firewall_rule#priority Route53ResolverFirewallRule#priority}.'''
        result = self._values.get("priority")
        assert result is not None, "Required property 'priority' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def block_override_dns_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53_resolver_firewall_rule#block_override_dns_type Route53ResolverFirewallRule#block_override_dns_type}.'''
        result = self._values.get("block_override_dns_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def block_override_domain(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53_resolver_firewall_rule#block_override_domain Route53ResolverFirewallRule#block_override_domain}.'''
        result = self._values.get("block_override_domain")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def block_override_ttl(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53_resolver_firewall_rule#block_override_ttl Route53ResolverFirewallRule#block_override_ttl}.'''
        result = self._values.get("block_override_ttl")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def block_response(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53_resolver_firewall_rule#block_response Route53ResolverFirewallRule#block_response}.'''
        result = self._values.get("block_response")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53_resolver_firewall_rule#id Route53ResolverFirewallRule#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Route53ResolverFirewallRuleConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "Route53ResolverFirewallRule",
    "Route53ResolverFirewallRuleConfig",
]

publication.publish()

def _typecheckingstub__b179a3c57843fe43e65223d6891c3aa4f54e3d1996a0e4cb2f2ab570f364b47e(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    action: builtins.str,
    firewall_domain_list_id: builtins.str,
    firewall_rule_group_id: builtins.str,
    name: builtins.str,
    priority: jsii.Number,
    block_override_dns_type: typing.Optional[builtins.str] = None,
    block_override_domain: typing.Optional[builtins.str] = None,
    block_override_ttl: typing.Optional[jsii.Number] = None,
    block_response: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__e193b1b7b157fee81f8c3e2c4db6cf8120ecfdbcde6820124e62c39d5401fd69(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__177c35e5a9f7eba1c2765d64c3e8fb861a4f6f148a73f864af7a2dbf6e55b36a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ef2f151e5f00a00df7602c98b26f2aa0006c1c1bc8528fd1df2f0300bb5c1c4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e29b8103cc1538de65c29d99c81f712639df17a7dca532859417bd76fdb29fc(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1436a6eea63ffa18c4fd65d6ecd037ecebd34ff1fa0b9d4811d5a635e145206b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a1e713d34227a7c02fc643aff4f39d70cd205a75b1c8b12133b32ab5a1ecf71(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc6c15df898c523f28d227dc20814d90444c240a1d3a7f157b38feec8f709263(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9184a56fbd50301748b5bb6ee840879e855b664ef7abf0bb59d810104293b11(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b49702d861ef16315a006fac5ceed9fd1c847743b530e30b774b3cc5a5efac49(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d96f439fca9a3e8d07ab48e6fc1cf09cda119f30e90ccf5c280a819d8e70635(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a524200b40c0ee6c85edf76e10c4fb2755ae441aafec5ba4d3cddcce4c7995c(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    action: builtins.str,
    firewall_domain_list_id: builtins.str,
    firewall_rule_group_id: builtins.str,
    name: builtins.str,
    priority: jsii.Number,
    block_override_dns_type: typing.Optional[builtins.str] = None,
    block_override_domain: typing.Optional[builtins.str] = None,
    block_override_ttl: typing.Optional[jsii.Number] = None,
    block_response: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
