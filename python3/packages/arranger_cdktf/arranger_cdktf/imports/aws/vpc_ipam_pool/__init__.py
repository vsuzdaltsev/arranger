'''
# `aws_vpc_ipam_pool`

Refer to the Terraform Registory for docs: [`aws_vpc_ipam_pool`](https://www.terraform.io/docs/providers/aws/r/vpc_ipam_pool).
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


class VpcIpamPool(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.vpcIpamPool.VpcIpamPool",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/vpc_ipam_pool aws_vpc_ipam_pool}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        address_family: builtins.str,
        ipam_scope_id: builtins.str,
        allocation_default_netmask_length: typing.Optional[jsii.Number] = None,
        allocation_max_netmask_length: typing.Optional[jsii.Number] = None,
        allocation_min_netmask_length: typing.Optional[jsii.Number] = None,
        allocation_resource_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        auto_import: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        aws_service: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        locale: typing.Optional[builtins.str] = None,
        publicly_advertisable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        source_ipam_pool_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["VpcIpamPoolTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/vpc_ipam_pool aws_vpc_ipam_pool} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param address_family: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_ipam_pool#address_family VpcIpamPool#address_family}.
        :param ipam_scope_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_ipam_pool#ipam_scope_id VpcIpamPool#ipam_scope_id}.
        :param allocation_default_netmask_length: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_ipam_pool#allocation_default_netmask_length VpcIpamPool#allocation_default_netmask_length}.
        :param allocation_max_netmask_length: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_ipam_pool#allocation_max_netmask_length VpcIpamPool#allocation_max_netmask_length}.
        :param allocation_min_netmask_length: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_ipam_pool#allocation_min_netmask_length VpcIpamPool#allocation_min_netmask_length}.
        :param allocation_resource_tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_ipam_pool#allocation_resource_tags VpcIpamPool#allocation_resource_tags}.
        :param auto_import: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_ipam_pool#auto_import VpcIpamPool#auto_import}.
        :param aws_service: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_ipam_pool#aws_service VpcIpamPool#aws_service}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_ipam_pool#description VpcIpamPool#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_ipam_pool#id VpcIpamPool#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param locale: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_ipam_pool#locale VpcIpamPool#locale}.
        :param publicly_advertisable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_ipam_pool#publicly_advertisable VpcIpamPool#publicly_advertisable}.
        :param source_ipam_pool_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_ipam_pool#source_ipam_pool_id VpcIpamPool#source_ipam_pool_id}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_ipam_pool#tags VpcIpamPool#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_ipam_pool#tags_all VpcIpamPool#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_ipam_pool#timeouts VpcIpamPool#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bdeca4f09ce164b3914b0f534d2c36972dba33d27d409fc0d819b94d9dfdab87)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = VpcIpamPoolConfig(
            address_family=address_family,
            ipam_scope_id=ipam_scope_id,
            allocation_default_netmask_length=allocation_default_netmask_length,
            allocation_max_netmask_length=allocation_max_netmask_length,
            allocation_min_netmask_length=allocation_min_netmask_length,
            allocation_resource_tags=allocation_resource_tags,
            auto_import=auto_import,
            aws_service=aws_service,
            description=description,
            id=id,
            locale=locale,
            publicly_advertisable=publicly_advertisable,
            source_ipam_pool_id=source_ipam_pool_id,
            tags=tags,
            tags_all=tags_all,
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
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_ipam_pool#create VpcIpamPool#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_ipam_pool#delete VpcIpamPool#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_ipam_pool#update VpcIpamPool#update}.
        '''
        value = VpcIpamPoolTimeouts(create=create, delete=delete, update=update)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAllocationDefaultNetmaskLength")
    def reset_allocation_default_netmask_length(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllocationDefaultNetmaskLength", []))

    @jsii.member(jsii_name="resetAllocationMaxNetmaskLength")
    def reset_allocation_max_netmask_length(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllocationMaxNetmaskLength", []))

    @jsii.member(jsii_name="resetAllocationMinNetmaskLength")
    def reset_allocation_min_netmask_length(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllocationMinNetmaskLength", []))

    @jsii.member(jsii_name="resetAllocationResourceTags")
    def reset_allocation_resource_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllocationResourceTags", []))

    @jsii.member(jsii_name="resetAutoImport")
    def reset_auto_import(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoImport", []))

    @jsii.member(jsii_name="resetAwsService")
    def reset_aws_service(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsService", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLocale")
    def reset_locale(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocale", []))

    @jsii.member(jsii_name="resetPubliclyAdvertisable")
    def reset_publicly_advertisable(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPubliclyAdvertisable", []))

    @jsii.member(jsii_name="resetSourceIpamPoolId")
    def reset_source_ipam_pool_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceIpamPoolId", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

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
    @jsii.member(jsii_name="ipamScopeType")
    def ipam_scope_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipamScopeType"))

    @builtins.property
    @jsii.member(jsii_name="poolDepth")
    def pool_depth(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "poolDepth"))

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "VpcIpamPoolTimeoutsOutputReference":
        return typing.cast("VpcIpamPoolTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="addressFamilyInput")
    def address_family_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "addressFamilyInput"))

    @builtins.property
    @jsii.member(jsii_name="allocationDefaultNetmaskLengthInput")
    def allocation_default_netmask_length_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "allocationDefaultNetmaskLengthInput"))

    @builtins.property
    @jsii.member(jsii_name="allocationMaxNetmaskLengthInput")
    def allocation_max_netmask_length_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "allocationMaxNetmaskLengthInput"))

    @builtins.property
    @jsii.member(jsii_name="allocationMinNetmaskLengthInput")
    def allocation_min_netmask_length_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "allocationMinNetmaskLengthInput"))

    @builtins.property
    @jsii.member(jsii_name="allocationResourceTagsInput")
    def allocation_resource_tags_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "allocationResourceTagsInput"))

    @builtins.property
    @jsii.member(jsii_name="autoImportInput")
    def auto_import_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "autoImportInput"))

    @builtins.property
    @jsii.member(jsii_name="awsServiceInput")
    def aws_service_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "awsServiceInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="ipamScopeIdInput")
    def ipam_scope_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipamScopeIdInput"))

    @builtins.property
    @jsii.member(jsii_name="localeInput")
    def locale_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "localeInput"))

    @builtins.property
    @jsii.member(jsii_name="publiclyAdvertisableInput")
    def publicly_advertisable_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "publiclyAdvertisableInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceIpamPoolIdInput")
    def source_ipam_pool_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceIpamPoolIdInput"))

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
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["VpcIpamPoolTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["VpcIpamPoolTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="addressFamily")
    def address_family(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "addressFamily"))

    @address_family.setter
    def address_family(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__842e3c7d3e58b5d2e3b87d36626f2a7c1482edcd985de98025002fc0d19a837a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "addressFamily", value)

    @builtins.property
    @jsii.member(jsii_name="allocationDefaultNetmaskLength")
    def allocation_default_netmask_length(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "allocationDefaultNetmaskLength"))

    @allocation_default_netmask_length.setter
    def allocation_default_netmask_length(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c841d9b9a0debdc687a90345295ff6219b15206766f9d3326b451b97de3b66bb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allocationDefaultNetmaskLength", value)

    @builtins.property
    @jsii.member(jsii_name="allocationMaxNetmaskLength")
    def allocation_max_netmask_length(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "allocationMaxNetmaskLength"))

    @allocation_max_netmask_length.setter
    def allocation_max_netmask_length(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92ddde30fb381f44d1d26e1692dfbe5d5e816c6c551c1aaf15a19d86849a7d36)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allocationMaxNetmaskLength", value)

    @builtins.property
    @jsii.member(jsii_name="allocationMinNetmaskLength")
    def allocation_min_netmask_length(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "allocationMinNetmaskLength"))

    @allocation_min_netmask_length.setter
    def allocation_min_netmask_length(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aed56f3dc0a1937d27b59432a14cc0eceb2d6090fce227247ac48a2ac4b0f2be)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allocationMinNetmaskLength", value)

    @builtins.property
    @jsii.member(jsii_name="allocationResourceTags")
    def allocation_resource_tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "allocationResourceTags"))

    @allocation_resource_tags.setter
    def allocation_resource_tags(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf4554dfa808dcea718c9224845b36b8a3eb67e34e8ddd9e362b250272ad8ee5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allocationResourceTags", value)

    @builtins.property
    @jsii.member(jsii_name="autoImport")
    def auto_import(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "autoImport"))

    @auto_import.setter
    def auto_import(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49c6c421deb6999cc232e9f4c038369f4d78a9cfe75be997be82e200ea029c8b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoImport", value)

    @builtins.property
    @jsii.member(jsii_name="awsService")
    def aws_service(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "awsService"))

    @aws_service.setter
    def aws_service(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14082f1a151f7da52849c186ebfa2e5882e82b9b78e6bcccd63408bf0b77d27f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsService", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__199d8582fae1c4cb08b6f1484b3e17ada970150f247e219d034402ef00a3b6d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c902fb88b6cc08c9420f8b347992616f37ed4e4b17c2dc7f78fa51de8ef8752)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="ipamScopeId")
    def ipam_scope_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipamScopeId"))

    @ipam_scope_id.setter
    def ipam_scope_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab2860aaff2aba5e0bf1f648c8e87aa13111673dfdf7c5e06d91de27dcb5df77)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipamScopeId", value)

    @builtins.property
    @jsii.member(jsii_name="locale")
    def locale(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "locale"))

    @locale.setter
    def locale(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ffe6de6571c36c226428f7734e3ae11dbb7b608d01c97ae42896d6b577d09ad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "locale", value)

    @builtins.property
    @jsii.member(jsii_name="publiclyAdvertisable")
    def publicly_advertisable(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "publiclyAdvertisable"))

    @publicly_advertisable.setter
    def publicly_advertisable(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7766d1133d0d30c80593f190e6f5d4c9c87501f6e4fe401a1671235c4c6bee29)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publiclyAdvertisable", value)

    @builtins.property
    @jsii.member(jsii_name="sourceIpamPoolId")
    def source_ipam_pool_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceIpamPoolId"))

    @source_ipam_pool_id.setter
    def source_ipam_pool_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c659f42ddcbf412f5df55538d20c22e1c3938739d76b90f16d1e9def87f93d4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceIpamPoolId", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__395343f701d5c198bb83dcda978980e7189558660535de0728d2dc1268050903)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b056b1514fadd73c9988364a11f6d94a48cad6db351c2277397bfe96de8dbf7a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)


@jsii.data_type(
    jsii_type="aws.vpcIpamPool.VpcIpamPoolConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "address_family": "addressFamily",
        "ipam_scope_id": "ipamScopeId",
        "allocation_default_netmask_length": "allocationDefaultNetmaskLength",
        "allocation_max_netmask_length": "allocationMaxNetmaskLength",
        "allocation_min_netmask_length": "allocationMinNetmaskLength",
        "allocation_resource_tags": "allocationResourceTags",
        "auto_import": "autoImport",
        "aws_service": "awsService",
        "description": "description",
        "id": "id",
        "locale": "locale",
        "publicly_advertisable": "publiclyAdvertisable",
        "source_ipam_pool_id": "sourceIpamPoolId",
        "tags": "tags",
        "tags_all": "tagsAll",
        "timeouts": "timeouts",
    },
)
class VpcIpamPoolConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        address_family: builtins.str,
        ipam_scope_id: builtins.str,
        allocation_default_netmask_length: typing.Optional[jsii.Number] = None,
        allocation_max_netmask_length: typing.Optional[jsii.Number] = None,
        allocation_min_netmask_length: typing.Optional[jsii.Number] = None,
        allocation_resource_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        auto_import: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        aws_service: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        locale: typing.Optional[builtins.str] = None,
        publicly_advertisable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        source_ipam_pool_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["VpcIpamPoolTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param address_family: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_ipam_pool#address_family VpcIpamPool#address_family}.
        :param ipam_scope_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_ipam_pool#ipam_scope_id VpcIpamPool#ipam_scope_id}.
        :param allocation_default_netmask_length: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_ipam_pool#allocation_default_netmask_length VpcIpamPool#allocation_default_netmask_length}.
        :param allocation_max_netmask_length: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_ipam_pool#allocation_max_netmask_length VpcIpamPool#allocation_max_netmask_length}.
        :param allocation_min_netmask_length: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_ipam_pool#allocation_min_netmask_length VpcIpamPool#allocation_min_netmask_length}.
        :param allocation_resource_tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_ipam_pool#allocation_resource_tags VpcIpamPool#allocation_resource_tags}.
        :param auto_import: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_ipam_pool#auto_import VpcIpamPool#auto_import}.
        :param aws_service: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_ipam_pool#aws_service VpcIpamPool#aws_service}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_ipam_pool#description VpcIpamPool#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_ipam_pool#id VpcIpamPool#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param locale: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_ipam_pool#locale VpcIpamPool#locale}.
        :param publicly_advertisable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_ipam_pool#publicly_advertisable VpcIpamPool#publicly_advertisable}.
        :param source_ipam_pool_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_ipam_pool#source_ipam_pool_id VpcIpamPool#source_ipam_pool_id}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_ipam_pool#tags VpcIpamPool#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_ipam_pool#tags_all VpcIpamPool#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_ipam_pool#timeouts VpcIpamPool#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = VpcIpamPoolTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2dc2d022c5b932dd0eceadbcefcf6a415691ad3190280ab3d25fbed03f979b1b)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument address_family", value=address_family, expected_type=type_hints["address_family"])
            check_type(argname="argument ipam_scope_id", value=ipam_scope_id, expected_type=type_hints["ipam_scope_id"])
            check_type(argname="argument allocation_default_netmask_length", value=allocation_default_netmask_length, expected_type=type_hints["allocation_default_netmask_length"])
            check_type(argname="argument allocation_max_netmask_length", value=allocation_max_netmask_length, expected_type=type_hints["allocation_max_netmask_length"])
            check_type(argname="argument allocation_min_netmask_length", value=allocation_min_netmask_length, expected_type=type_hints["allocation_min_netmask_length"])
            check_type(argname="argument allocation_resource_tags", value=allocation_resource_tags, expected_type=type_hints["allocation_resource_tags"])
            check_type(argname="argument auto_import", value=auto_import, expected_type=type_hints["auto_import"])
            check_type(argname="argument aws_service", value=aws_service, expected_type=type_hints["aws_service"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument locale", value=locale, expected_type=type_hints["locale"])
            check_type(argname="argument publicly_advertisable", value=publicly_advertisable, expected_type=type_hints["publicly_advertisable"])
            check_type(argname="argument source_ipam_pool_id", value=source_ipam_pool_id, expected_type=type_hints["source_ipam_pool_id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "address_family": address_family,
            "ipam_scope_id": ipam_scope_id,
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
        if allocation_default_netmask_length is not None:
            self._values["allocation_default_netmask_length"] = allocation_default_netmask_length
        if allocation_max_netmask_length is not None:
            self._values["allocation_max_netmask_length"] = allocation_max_netmask_length
        if allocation_min_netmask_length is not None:
            self._values["allocation_min_netmask_length"] = allocation_min_netmask_length
        if allocation_resource_tags is not None:
            self._values["allocation_resource_tags"] = allocation_resource_tags
        if auto_import is not None:
            self._values["auto_import"] = auto_import
        if aws_service is not None:
            self._values["aws_service"] = aws_service
        if description is not None:
            self._values["description"] = description
        if id is not None:
            self._values["id"] = id
        if locale is not None:
            self._values["locale"] = locale
        if publicly_advertisable is not None:
            self._values["publicly_advertisable"] = publicly_advertisable
        if source_ipam_pool_id is not None:
            self._values["source_ipam_pool_id"] = source_ipam_pool_id
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
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
    def address_family(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_ipam_pool#address_family VpcIpamPool#address_family}.'''
        result = self._values.get("address_family")
        assert result is not None, "Required property 'address_family' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ipam_scope_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_ipam_pool#ipam_scope_id VpcIpamPool#ipam_scope_id}.'''
        result = self._values.get("ipam_scope_id")
        assert result is not None, "Required property 'ipam_scope_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allocation_default_netmask_length(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_ipam_pool#allocation_default_netmask_length VpcIpamPool#allocation_default_netmask_length}.'''
        result = self._values.get("allocation_default_netmask_length")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def allocation_max_netmask_length(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_ipam_pool#allocation_max_netmask_length VpcIpamPool#allocation_max_netmask_length}.'''
        result = self._values.get("allocation_max_netmask_length")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def allocation_min_netmask_length(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_ipam_pool#allocation_min_netmask_length VpcIpamPool#allocation_min_netmask_length}.'''
        result = self._values.get("allocation_min_netmask_length")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def allocation_resource_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_ipam_pool#allocation_resource_tags VpcIpamPool#allocation_resource_tags}.'''
        result = self._values.get("allocation_resource_tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def auto_import(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_ipam_pool#auto_import VpcIpamPool#auto_import}.'''
        result = self._values.get("auto_import")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def aws_service(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_ipam_pool#aws_service VpcIpamPool#aws_service}.'''
        result = self._values.get("aws_service")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_ipam_pool#description VpcIpamPool#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_ipam_pool#id VpcIpamPool#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def locale(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_ipam_pool#locale VpcIpamPool#locale}.'''
        result = self._values.get("locale")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def publicly_advertisable(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_ipam_pool#publicly_advertisable VpcIpamPool#publicly_advertisable}.'''
        result = self._values.get("publicly_advertisable")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def source_ipam_pool_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_ipam_pool#source_ipam_pool_id VpcIpamPool#source_ipam_pool_id}.'''
        result = self._values.get("source_ipam_pool_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_ipam_pool#tags VpcIpamPool#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_ipam_pool#tags_all VpcIpamPool#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["VpcIpamPoolTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_ipam_pool#timeouts VpcIpamPool#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["VpcIpamPoolTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VpcIpamPoolConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.vpcIpamPool.VpcIpamPoolTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class VpcIpamPoolTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_ipam_pool#create VpcIpamPool#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_ipam_pool#delete VpcIpamPool#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_ipam_pool#update VpcIpamPool#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d120ea195b3d4d34d7115bbb76f21e41c063cb4abdfd064197990bed63af9f92)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_ipam_pool#create VpcIpamPool#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_ipam_pool#delete VpcIpamPool#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_ipam_pool#update VpcIpamPool#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VpcIpamPoolTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VpcIpamPoolTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.vpcIpamPool.VpcIpamPoolTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__28e5af9c0d14177d645029f36339827b3a62353346b167cf67f817c589364875)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @jsii.member(jsii_name="resetUpdate")
    def reset_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdate", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

    @builtins.property
    @jsii.member(jsii_name="updateInput")
    def update_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "updateInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d56f93a6c5b13cc5aa5e171db121c9201fb46924adcc2128457c3b5ae441223)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c0e4d67fb03d45a4193f32ed75a97c4201003261396c87c5c94568e0e81ce8f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c6234fe32b69e8eb720a823831d464c119c24c3f903f4b6e363f1407009edfe2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[VpcIpamPoolTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[VpcIpamPoolTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[VpcIpamPoolTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05f3cd750b186361dfbeec51df98d6ddd9d9b3737e5be2911f19529143c60d8c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "VpcIpamPool",
    "VpcIpamPoolConfig",
    "VpcIpamPoolTimeouts",
    "VpcIpamPoolTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__bdeca4f09ce164b3914b0f534d2c36972dba33d27d409fc0d819b94d9dfdab87(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    address_family: builtins.str,
    ipam_scope_id: builtins.str,
    allocation_default_netmask_length: typing.Optional[jsii.Number] = None,
    allocation_max_netmask_length: typing.Optional[jsii.Number] = None,
    allocation_min_netmask_length: typing.Optional[jsii.Number] = None,
    allocation_resource_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    auto_import: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    aws_service: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    locale: typing.Optional[builtins.str] = None,
    publicly_advertisable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    source_ipam_pool_id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[VpcIpamPoolTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__842e3c7d3e58b5d2e3b87d36626f2a7c1482edcd985de98025002fc0d19a837a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c841d9b9a0debdc687a90345295ff6219b15206766f9d3326b451b97de3b66bb(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92ddde30fb381f44d1d26e1692dfbe5d5e816c6c551c1aaf15a19d86849a7d36(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aed56f3dc0a1937d27b59432a14cc0eceb2d6090fce227247ac48a2ac4b0f2be(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf4554dfa808dcea718c9224845b36b8a3eb67e34e8ddd9e362b250272ad8ee5(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49c6c421deb6999cc232e9f4c038369f4d78a9cfe75be997be82e200ea029c8b(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14082f1a151f7da52849c186ebfa2e5882e82b9b78e6bcccd63408bf0b77d27f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__199d8582fae1c4cb08b6f1484b3e17ada970150f247e219d034402ef00a3b6d0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c902fb88b6cc08c9420f8b347992616f37ed4e4b17c2dc7f78fa51de8ef8752(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab2860aaff2aba5e0bf1f648c8e87aa13111673dfdf7c5e06d91de27dcb5df77(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ffe6de6571c36c226428f7734e3ae11dbb7b608d01c97ae42896d6b577d09ad(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7766d1133d0d30c80593f190e6f5d4c9c87501f6e4fe401a1671235c4c6bee29(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c659f42ddcbf412f5df55538d20c22e1c3938739d76b90f16d1e9def87f93d4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__395343f701d5c198bb83dcda978980e7189558660535de0728d2dc1268050903(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b056b1514fadd73c9988364a11f6d94a48cad6db351c2277397bfe96de8dbf7a(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2dc2d022c5b932dd0eceadbcefcf6a415691ad3190280ab3d25fbed03f979b1b(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    address_family: builtins.str,
    ipam_scope_id: builtins.str,
    allocation_default_netmask_length: typing.Optional[jsii.Number] = None,
    allocation_max_netmask_length: typing.Optional[jsii.Number] = None,
    allocation_min_netmask_length: typing.Optional[jsii.Number] = None,
    allocation_resource_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    auto_import: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    aws_service: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    locale: typing.Optional[builtins.str] = None,
    publicly_advertisable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    source_ipam_pool_id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[VpcIpamPoolTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d120ea195b3d4d34d7115bbb76f21e41c063cb4abdfd064197990bed63af9f92(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28e5af9c0d14177d645029f36339827b3a62353346b167cf67f817c589364875(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d56f93a6c5b13cc5aa5e171db121c9201fb46924adcc2128457c3b5ae441223(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c0e4d67fb03d45a4193f32ed75a97c4201003261396c87c5c94568e0e81ce8f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6234fe32b69e8eb720a823831d464c119c24c3f903f4b6e363f1407009edfe2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05f3cd750b186361dfbeec51df98d6ddd9d9b3737e5be2911f19529143c60d8c(
    value: typing.Optional[typing.Union[VpcIpamPoolTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
