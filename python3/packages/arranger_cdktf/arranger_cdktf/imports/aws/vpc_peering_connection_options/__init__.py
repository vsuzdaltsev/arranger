'''
# `aws_vpc_peering_connection_options`

Refer to the Terraform Registory for docs: [`aws_vpc_peering_connection_options`](https://www.terraform.io/docs/providers/aws/r/vpc_peering_connection_options).
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


class VpcPeeringConnectionOptions(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.vpcPeeringConnectionOptions.VpcPeeringConnectionOptions",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/vpc_peering_connection_options aws_vpc_peering_connection_options}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        vpc_peering_connection_id: builtins.str,
        accepter: typing.Optional[typing.Union["VpcPeeringConnectionOptionsAccepter", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        requester: typing.Optional[typing.Union["VpcPeeringConnectionOptionsRequester", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/vpc_peering_connection_options aws_vpc_peering_connection_options} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param vpc_peering_connection_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_peering_connection_options#vpc_peering_connection_id VpcPeeringConnectionOptions#vpc_peering_connection_id}.
        :param accepter: accepter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_peering_connection_options#accepter VpcPeeringConnectionOptions#accepter}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_peering_connection_options#id VpcPeeringConnectionOptions#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param requester: requester block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_peering_connection_options#requester VpcPeeringConnectionOptions#requester}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__836e5e0ba57cf70c23a3d62ccdfca463cdd72c3795713e9b8b730a90febb78de)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = VpcPeeringConnectionOptionsConfig(
            vpc_peering_connection_id=vpc_peering_connection_id,
            accepter=accepter,
            id=id,
            requester=requester,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAccepter")
    def put_accepter(
        self,
        *,
        allow_classic_link_to_remote_vpc: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        allow_remote_vpc_dns_resolution: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        allow_vpc_to_remote_classic_link: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param allow_classic_link_to_remote_vpc: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_peering_connection_options#allow_classic_link_to_remote_vpc VpcPeeringConnectionOptions#allow_classic_link_to_remote_vpc}.
        :param allow_remote_vpc_dns_resolution: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_peering_connection_options#allow_remote_vpc_dns_resolution VpcPeeringConnectionOptions#allow_remote_vpc_dns_resolution}.
        :param allow_vpc_to_remote_classic_link: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_peering_connection_options#allow_vpc_to_remote_classic_link VpcPeeringConnectionOptions#allow_vpc_to_remote_classic_link}.
        '''
        value = VpcPeeringConnectionOptionsAccepter(
            allow_classic_link_to_remote_vpc=allow_classic_link_to_remote_vpc,
            allow_remote_vpc_dns_resolution=allow_remote_vpc_dns_resolution,
            allow_vpc_to_remote_classic_link=allow_vpc_to_remote_classic_link,
        )

        return typing.cast(None, jsii.invoke(self, "putAccepter", [value]))

    @jsii.member(jsii_name="putRequester")
    def put_requester(
        self,
        *,
        allow_classic_link_to_remote_vpc: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        allow_remote_vpc_dns_resolution: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        allow_vpc_to_remote_classic_link: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param allow_classic_link_to_remote_vpc: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_peering_connection_options#allow_classic_link_to_remote_vpc VpcPeeringConnectionOptions#allow_classic_link_to_remote_vpc}.
        :param allow_remote_vpc_dns_resolution: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_peering_connection_options#allow_remote_vpc_dns_resolution VpcPeeringConnectionOptions#allow_remote_vpc_dns_resolution}.
        :param allow_vpc_to_remote_classic_link: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_peering_connection_options#allow_vpc_to_remote_classic_link VpcPeeringConnectionOptions#allow_vpc_to_remote_classic_link}.
        '''
        value = VpcPeeringConnectionOptionsRequester(
            allow_classic_link_to_remote_vpc=allow_classic_link_to_remote_vpc,
            allow_remote_vpc_dns_resolution=allow_remote_vpc_dns_resolution,
            allow_vpc_to_remote_classic_link=allow_vpc_to_remote_classic_link,
        )

        return typing.cast(None, jsii.invoke(self, "putRequester", [value]))

    @jsii.member(jsii_name="resetAccepter")
    def reset_accepter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccepter", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetRequester")
    def reset_requester(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequester", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="accepter")
    def accepter(self) -> "VpcPeeringConnectionOptionsAccepterOutputReference":
        return typing.cast("VpcPeeringConnectionOptionsAccepterOutputReference", jsii.get(self, "accepter"))

    @builtins.property
    @jsii.member(jsii_name="requester")
    def requester(self) -> "VpcPeeringConnectionOptionsRequesterOutputReference":
        return typing.cast("VpcPeeringConnectionOptionsRequesterOutputReference", jsii.get(self, "requester"))

    @builtins.property
    @jsii.member(jsii_name="accepterInput")
    def accepter_input(self) -> typing.Optional["VpcPeeringConnectionOptionsAccepter"]:
        return typing.cast(typing.Optional["VpcPeeringConnectionOptionsAccepter"], jsii.get(self, "accepterInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="requesterInput")
    def requester_input(
        self,
    ) -> typing.Optional["VpcPeeringConnectionOptionsRequester"]:
        return typing.cast(typing.Optional["VpcPeeringConnectionOptionsRequester"], jsii.get(self, "requesterInput"))

    @builtins.property
    @jsii.member(jsii_name="vpcPeeringConnectionIdInput")
    def vpc_peering_connection_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vpcPeeringConnectionIdInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5016f84dd8a4dcdb7ae92c88a0ad048e7b2b7da4d0e9dbe221f36554cdd98933)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="vpcPeeringConnectionId")
    def vpc_peering_connection_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vpcPeeringConnectionId"))

    @vpc_peering_connection_id.setter
    def vpc_peering_connection_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11d5b827a78219eb0b3f0d4dafd72e48814880e7b257162423cc4f041b92a770)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcPeeringConnectionId", value)


@jsii.data_type(
    jsii_type="aws.vpcPeeringConnectionOptions.VpcPeeringConnectionOptionsAccepter",
    jsii_struct_bases=[],
    name_mapping={
        "allow_classic_link_to_remote_vpc": "allowClassicLinkToRemoteVpc",
        "allow_remote_vpc_dns_resolution": "allowRemoteVpcDnsResolution",
        "allow_vpc_to_remote_classic_link": "allowVpcToRemoteClassicLink",
    },
)
class VpcPeeringConnectionOptionsAccepter:
    def __init__(
        self,
        *,
        allow_classic_link_to_remote_vpc: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        allow_remote_vpc_dns_resolution: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        allow_vpc_to_remote_classic_link: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param allow_classic_link_to_remote_vpc: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_peering_connection_options#allow_classic_link_to_remote_vpc VpcPeeringConnectionOptions#allow_classic_link_to_remote_vpc}.
        :param allow_remote_vpc_dns_resolution: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_peering_connection_options#allow_remote_vpc_dns_resolution VpcPeeringConnectionOptions#allow_remote_vpc_dns_resolution}.
        :param allow_vpc_to_remote_classic_link: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_peering_connection_options#allow_vpc_to_remote_classic_link VpcPeeringConnectionOptions#allow_vpc_to_remote_classic_link}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c6eb585f17f840c3fe3739ba23138c9c5cf10aebc08c680724d99fddfadb97ed)
            check_type(argname="argument allow_classic_link_to_remote_vpc", value=allow_classic_link_to_remote_vpc, expected_type=type_hints["allow_classic_link_to_remote_vpc"])
            check_type(argname="argument allow_remote_vpc_dns_resolution", value=allow_remote_vpc_dns_resolution, expected_type=type_hints["allow_remote_vpc_dns_resolution"])
            check_type(argname="argument allow_vpc_to_remote_classic_link", value=allow_vpc_to_remote_classic_link, expected_type=type_hints["allow_vpc_to_remote_classic_link"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if allow_classic_link_to_remote_vpc is not None:
            self._values["allow_classic_link_to_remote_vpc"] = allow_classic_link_to_remote_vpc
        if allow_remote_vpc_dns_resolution is not None:
            self._values["allow_remote_vpc_dns_resolution"] = allow_remote_vpc_dns_resolution
        if allow_vpc_to_remote_classic_link is not None:
            self._values["allow_vpc_to_remote_classic_link"] = allow_vpc_to_remote_classic_link

    @builtins.property
    def allow_classic_link_to_remote_vpc(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_peering_connection_options#allow_classic_link_to_remote_vpc VpcPeeringConnectionOptions#allow_classic_link_to_remote_vpc}.'''
        result = self._values.get("allow_classic_link_to_remote_vpc")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def allow_remote_vpc_dns_resolution(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_peering_connection_options#allow_remote_vpc_dns_resolution VpcPeeringConnectionOptions#allow_remote_vpc_dns_resolution}.'''
        result = self._values.get("allow_remote_vpc_dns_resolution")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def allow_vpc_to_remote_classic_link(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_peering_connection_options#allow_vpc_to_remote_classic_link VpcPeeringConnectionOptions#allow_vpc_to_remote_classic_link}.'''
        result = self._values.get("allow_vpc_to_remote_classic_link")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VpcPeeringConnectionOptionsAccepter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VpcPeeringConnectionOptionsAccepterOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.vpcPeeringConnectionOptions.VpcPeeringConnectionOptionsAccepterOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f5e239e80ae1c6bcfbe4593a2f617f2b3c9468b3c0e65ae99e12b6326301d8fa)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAllowClassicLinkToRemoteVpc")
    def reset_allow_classic_link_to_remote_vpc(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowClassicLinkToRemoteVpc", []))

    @jsii.member(jsii_name="resetAllowRemoteVpcDnsResolution")
    def reset_allow_remote_vpc_dns_resolution(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowRemoteVpcDnsResolution", []))

    @jsii.member(jsii_name="resetAllowVpcToRemoteClassicLink")
    def reset_allow_vpc_to_remote_classic_link(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowVpcToRemoteClassicLink", []))

    @builtins.property
    @jsii.member(jsii_name="allowClassicLinkToRemoteVpcInput")
    def allow_classic_link_to_remote_vpc_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "allowClassicLinkToRemoteVpcInput"))

    @builtins.property
    @jsii.member(jsii_name="allowRemoteVpcDnsResolutionInput")
    def allow_remote_vpc_dns_resolution_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "allowRemoteVpcDnsResolutionInput"))

    @builtins.property
    @jsii.member(jsii_name="allowVpcToRemoteClassicLinkInput")
    def allow_vpc_to_remote_classic_link_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "allowVpcToRemoteClassicLinkInput"))

    @builtins.property
    @jsii.member(jsii_name="allowClassicLinkToRemoteVpc")
    def allow_classic_link_to_remote_vpc(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "allowClassicLinkToRemoteVpc"))

    @allow_classic_link_to_remote_vpc.setter
    def allow_classic_link_to_remote_vpc(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98d7cf6cc40794cc5596f4d3df2f4fd39f0c7b4041812d875fd5d8d84198e1bd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowClassicLinkToRemoteVpc", value)

    @builtins.property
    @jsii.member(jsii_name="allowRemoteVpcDnsResolution")
    def allow_remote_vpc_dns_resolution(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "allowRemoteVpcDnsResolution"))

    @allow_remote_vpc_dns_resolution.setter
    def allow_remote_vpc_dns_resolution(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c19d58fbbf9627613df3d7bb1b22a0ecb26c1f4de95eb1ded5c1b1ddd05f6e72)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowRemoteVpcDnsResolution", value)

    @builtins.property
    @jsii.member(jsii_name="allowVpcToRemoteClassicLink")
    def allow_vpc_to_remote_classic_link(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "allowVpcToRemoteClassicLink"))

    @allow_vpc_to_remote_classic_link.setter
    def allow_vpc_to_remote_classic_link(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f095190e319fb1416a9e28aa660a8ba907f62870652deede5bdd8cf2e011a1a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowVpcToRemoteClassicLink", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[VpcPeeringConnectionOptionsAccepter]:
        return typing.cast(typing.Optional[VpcPeeringConnectionOptionsAccepter], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[VpcPeeringConnectionOptionsAccepter],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7bebc8f0d7aa027b0e1bc923d61ce2f725d5a798c9faa4fae9e538b8abd9562d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.vpcPeeringConnectionOptions.VpcPeeringConnectionOptionsConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "vpc_peering_connection_id": "vpcPeeringConnectionId",
        "accepter": "accepter",
        "id": "id",
        "requester": "requester",
    },
)
class VpcPeeringConnectionOptionsConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        vpc_peering_connection_id: builtins.str,
        accepter: typing.Optional[typing.Union[VpcPeeringConnectionOptionsAccepter, typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        requester: typing.Optional[typing.Union["VpcPeeringConnectionOptionsRequester", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param vpc_peering_connection_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_peering_connection_options#vpc_peering_connection_id VpcPeeringConnectionOptions#vpc_peering_connection_id}.
        :param accepter: accepter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_peering_connection_options#accepter VpcPeeringConnectionOptions#accepter}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_peering_connection_options#id VpcPeeringConnectionOptions#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param requester: requester block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_peering_connection_options#requester VpcPeeringConnectionOptions#requester}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(accepter, dict):
            accepter = VpcPeeringConnectionOptionsAccepter(**accepter)
        if isinstance(requester, dict):
            requester = VpcPeeringConnectionOptionsRequester(**requester)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc1d25d4c21cc79d08d4297139214f067c9f76ec0707df5ed53a30fb6971d8eb)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument vpc_peering_connection_id", value=vpc_peering_connection_id, expected_type=type_hints["vpc_peering_connection_id"])
            check_type(argname="argument accepter", value=accepter, expected_type=type_hints["accepter"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument requester", value=requester, expected_type=type_hints["requester"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "vpc_peering_connection_id": vpc_peering_connection_id,
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
        if accepter is not None:
            self._values["accepter"] = accepter
        if id is not None:
            self._values["id"] = id
        if requester is not None:
            self._values["requester"] = requester

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
    def vpc_peering_connection_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_peering_connection_options#vpc_peering_connection_id VpcPeeringConnectionOptions#vpc_peering_connection_id}.'''
        result = self._values.get("vpc_peering_connection_id")
        assert result is not None, "Required property 'vpc_peering_connection_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def accepter(self) -> typing.Optional[VpcPeeringConnectionOptionsAccepter]:
        '''accepter block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_peering_connection_options#accepter VpcPeeringConnectionOptions#accepter}
        '''
        result = self._values.get("accepter")
        return typing.cast(typing.Optional[VpcPeeringConnectionOptionsAccepter], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_peering_connection_options#id VpcPeeringConnectionOptions#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def requester(self) -> typing.Optional["VpcPeeringConnectionOptionsRequester"]:
        '''requester block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_peering_connection_options#requester VpcPeeringConnectionOptions#requester}
        '''
        result = self._values.get("requester")
        return typing.cast(typing.Optional["VpcPeeringConnectionOptionsRequester"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VpcPeeringConnectionOptionsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.vpcPeeringConnectionOptions.VpcPeeringConnectionOptionsRequester",
    jsii_struct_bases=[],
    name_mapping={
        "allow_classic_link_to_remote_vpc": "allowClassicLinkToRemoteVpc",
        "allow_remote_vpc_dns_resolution": "allowRemoteVpcDnsResolution",
        "allow_vpc_to_remote_classic_link": "allowVpcToRemoteClassicLink",
    },
)
class VpcPeeringConnectionOptionsRequester:
    def __init__(
        self,
        *,
        allow_classic_link_to_remote_vpc: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        allow_remote_vpc_dns_resolution: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        allow_vpc_to_remote_classic_link: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param allow_classic_link_to_remote_vpc: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_peering_connection_options#allow_classic_link_to_remote_vpc VpcPeeringConnectionOptions#allow_classic_link_to_remote_vpc}.
        :param allow_remote_vpc_dns_resolution: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_peering_connection_options#allow_remote_vpc_dns_resolution VpcPeeringConnectionOptions#allow_remote_vpc_dns_resolution}.
        :param allow_vpc_to_remote_classic_link: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_peering_connection_options#allow_vpc_to_remote_classic_link VpcPeeringConnectionOptions#allow_vpc_to_remote_classic_link}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__408e8210ed2d99ec6fb410c13d9084bcf253fc861a63f925cd594c19aeb0fb33)
            check_type(argname="argument allow_classic_link_to_remote_vpc", value=allow_classic_link_to_remote_vpc, expected_type=type_hints["allow_classic_link_to_remote_vpc"])
            check_type(argname="argument allow_remote_vpc_dns_resolution", value=allow_remote_vpc_dns_resolution, expected_type=type_hints["allow_remote_vpc_dns_resolution"])
            check_type(argname="argument allow_vpc_to_remote_classic_link", value=allow_vpc_to_remote_classic_link, expected_type=type_hints["allow_vpc_to_remote_classic_link"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if allow_classic_link_to_remote_vpc is not None:
            self._values["allow_classic_link_to_remote_vpc"] = allow_classic_link_to_remote_vpc
        if allow_remote_vpc_dns_resolution is not None:
            self._values["allow_remote_vpc_dns_resolution"] = allow_remote_vpc_dns_resolution
        if allow_vpc_to_remote_classic_link is not None:
            self._values["allow_vpc_to_remote_classic_link"] = allow_vpc_to_remote_classic_link

    @builtins.property
    def allow_classic_link_to_remote_vpc(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_peering_connection_options#allow_classic_link_to_remote_vpc VpcPeeringConnectionOptions#allow_classic_link_to_remote_vpc}.'''
        result = self._values.get("allow_classic_link_to_remote_vpc")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def allow_remote_vpc_dns_resolution(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_peering_connection_options#allow_remote_vpc_dns_resolution VpcPeeringConnectionOptions#allow_remote_vpc_dns_resolution}.'''
        result = self._values.get("allow_remote_vpc_dns_resolution")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def allow_vpc_to_remote_classic_link(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_peering_connection_options#allow_vpc_to_remote_classic_link VpcPeeringConnectionOptions#allow_vpc_to_remote_classic_link}.'''
        result = self._values.get("allow_vpc_to_remote_classic_link")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VpcPeeringConnectionOptionsRequester(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VpcPeeringConnectionOptionsRequesterOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.vpcPeeringConnectionOptions.VpcPeeringConnectionOptionsRequesterOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6a963cee7791aa5f6f52149ae568368fb3949dd68179c4a90c6c80e76f93b434)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAllowClassicLinkToRemoteVpc")
    def reset_allow_classic_link_to_remote_vpc(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowClassicLinkToRemoteVpc", []))

    @jsii.member(jsii_name="resetAllowRemoteVpcDnsResolution")
    def reset_allow_remote_vpc_dns_resolution(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowRemoteVpcDnsResolution", []))

    @jsii.member(jsii_name="resetAllowVpcToRemoteClassicLink")
    def reset_allow_vpc_to_remote_classic_link(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowVpcToRemoteClassicLink", []))

    @builtins.property
    @jsii.member(jsii_name="allowClassicLinkToRemoteVpcInput")
    def allow_classic_link_to_remote_vpc_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "allowClassicLinkToRemoteVpcInput"))

    @builtins.property
    @jsii.member(jsii_name="allowRemoteVpcDnsResolutionInput")
    def allow_remote_vpc_dns_resolution_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "allowRemoteVpcDnsResolutionInput"))

    @builtins.property
    @jsii.member(jsii_name="allowVpcToRemoteClassicLinkInput")
    def allow_vpc_to_remote_classic_link_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "allowVpcToRemoteClassicLinkInput"))

    @builtins.property
    @jsii.member(jsii_name="allowClassicLinkToRemoteVpc")
    def allow_classic_link_to_remote_vpc(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "allowClassicLinkToRemoteVpc"))

    @allow_classic_link_to_remote_vpc.setter
    def allow_classic_link_to_remote_vpc(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a568ad5e02f3e58bbb66d6d045c53995e31c7000b14a5abac5bd986915862c96)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowClassicLinkToRemoteVpc", value)

    @builtins.property
    @jsii.member(jsii_name="allowRemoteVpcDnsResolution")
    def allow_remote_vpc_dns_resolution(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "allowRemoteVpcDnsResolution"))

    @allow_remote_vpc_dns_resolution.setter
    def allow_remote_vpc_dns_resolution(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9a30f236f1f330965715857a2bea3b24ae216394448dfdcc762f864d542ef38)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowRemoteVpcDnsResolution", value)

    @builtins.property
    @jsii.member(jsii_name="allowVpcToRemoteClassicLink")
    def allow_vpc_to_remote_classic_link(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "allowVpcToRemoteClassicLink"))

    @allow_vpc_to_remote_classic_link.setter
    def allow_vpc_to_remote_classic_link(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea8378a5899aebee0ac3a7c87b3b6a006aaeaea0755dffd51ea6ed1cef6a78e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowVpcToRemoteClassicLink", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[VpcPeeringConnectionOptionsRequester]:
        return typing.cast(typing.Optional[VpcPeeringConnectionOptionsRequester], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[VpcPeeringConnectionOptionsRequester],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1c38e34eea1ab8c87e133c511e315f3bf2d0735ffc0b9905819d409d60c0927)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "VpcPeeringConnectionOptions",
    "VpcPeeringConnectionOptionsAccepter",
    "VpcPeeringConnectionOptionsAccepterOutputReference",
    "VpcPeeringConnectionOptionsConfig",
    "VpcPeeringConnectionOptionsRequester",
    "VpcPeeringConnectionOptionsRequesterOutputReference",
]

publication.publish()

def _typecheckingstub__836e5e0ba57cf70c23a3d62ccdfca463cdd72c3795713e9b8b730a90febb78de(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    vpc_peering_connection_id: builtins.str,
    accepter: typing.Optional[typing.Union[VpcPeeringConnectionOptionsAccepter, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    requester: typing.Optional[typing.Union[VpcPeeringConnectionOptionsRequester, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__5016f84dd8a4dcdb7ae92c88a0ad048e7b2b7da4d0e9dbe221f36554cdd98933(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11d5b827a78219eb0b3f0d4dafd72e48814880e7b257162423cc4f041b92a770(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6eb585f17f840c3fe3739ba23138c9c5cf10aebc08c680724d99fddfadb97ed(
    *,
    allow_classic_link_to_remote_vpc: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    allow_remote_vpc_dns_resolution: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    allow_vpc_to_remote_classic_link: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5e239e80ae1c6bcfbe4593a2f617f2b3c9468b3c0e65ae99e12b6326301d8fa(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98d7cf6cc40794cc5596f4d3df2f4fd39f0c7b4041812d875fd5d8d84198e1bd(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c19d58fbbf9627613df3d7bb1b22a0ecb26c1f4de95eb1ded5c1b1ddd05f6e72(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f095190e319fb1416a9e28aa660a8ba907f62870652deede5bdd8cf2e011a1a(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7bebc8f0d7aa027b0e1bc923d61ce2f725d5a798c9faa4fae9e538b8abd9562d(
    value: typing.Optional[VpcPeeringConnectionOptionsAccepter],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc1d25d4c21cc79d08d4297139214f067c9f76ec0707df5ed53a30fb6971d8eb(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    vpc_peering_connection_id: builtins.str,
    accepter: typing.Optional[typing.Union[VpcPeeringConnectionOptionsAccepter, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    requester: typing.Optional[typing.Union[VpcPeeringConnectionOptionsRequester, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__408e8210ed2d99ec6fb410c13d9084bcf253fc861a63f925cd594c19aeb0fb33(
    *,
    allow_classic_link_to_remote_vpc: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    allow_remote_vpc_dns_resolution: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    allow_vpc_to_remote_classic_link: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a963cee7791aa5f6f52149ae568368fb3949dd68179c4a90c6c80e76f93b434(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a568ad5e02f3e58bbb66d6d045c53995e31c7000b14a5abac5bd986915862c96(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9a30f236f1f330965715857a2bea3b24ae216394448dfdcc762f864d542ef38(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea8378a5899aebee0ac3a7c87b3b6a006aaeaea0755dffd51ea6ed1cef6a78e6(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1c38e34eea1ab8c87e133c511e315f3bf2d0735ffc0b9905819d409d60c0927(
    value: typing.Optional[VpcPeeringConnectionOptionsRequester],
) -> None:
    """Type checking stubs"""
    pass
