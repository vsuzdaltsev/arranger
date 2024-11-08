'''
# `aws_backup_region_settings`

Refer to the Terraform Registory for docs: [`aws_backup_region_settings`](https://www.terraform.io/docs/providers/aws/r/backup_region_settings).
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


class BackupRegionSettings(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.backupRegionSettings.BackupRegionSettings",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/backup_region_settings aws_backup_region_settings}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        resource_type_opt_in_preference: typing.Mapping[builtins.str, typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
        id: typing.Optional[builtins.str] = None,
        resource_type_management_preference: typing.Optional[typing.Mapping[builtins.str, typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/backup_region_settings aws_backup_region_settings} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param resource_type_opt_in_preference: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_region_settings#resource_type_opt_in_preference BackupRegionSettings#resource_type_opt_in_preference}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_region_settings#id BackupRegionSettings#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param resource_type_management_preference: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_region_settings#resource_type_management_preference BackupRegionSettings#resource_type_management_preference}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4fe4a97679f9dafed7468865aeef4b4024b40eb1712a003d3526e901323e531)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = BackupRegionSettingsConfig(
            resource_type_opt_in_preference=resource_type_opt_in_preference,
            id=id,
            resource_type_management_preference=resource_type_management_preference,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetResourceTypeManagementPreference")
    def reset_resource_type_management_preference(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourceTypeManagementPreference", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceTypeManagementPreferenceInput")
    def resource_type_management_preference_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]], jsii.get(self, "resourceTypeManagementPreferenceInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceTypeOptInPreferenceInput")
    def resource_type_opt_in_preference_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]], jsii.get(self, "resourceTypeOptInPreferenceInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__808baa7f010b3d00b8bfd84ce282d487e6a562a336f14e7e69b7e21fe964e499)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="resourceTypeManagementPreference")
    def resource_type_management_preference(
        self,
    ) -> typing.Mapping[builtins.str, typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Mapping[builtins.str, typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "resourceTypeManagementPreference"))

    @resource_type_management_preference.setter
    def resource_type_management_preference(
        self,
        value: typing.Mapping[builtins.str, typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__264cea9bff3ebe3becadce3b625604a758e7122a13fdcc8e6005e9ebe69d3956)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceTypeManagementPreference", value)

    @builtins.property
    @jsii.member(jsii_name="resourceTypeOptInPreference")
    def resource_type_opt_in_preference(
        self,
    ) -> typing.Mapping[builtins.str, typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Mapping[builtins.str, typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "resourceTypeOptInPreference"))

    @resource_type_opt_in_preference.setter
    def resource_type_opt_in_preference(
        self,
        value: typing.Mapping[builtins.str, typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d04beaf6af434de43fd02aaddfc1e3dc096ba5a2787fe9662cdf4ba8cf0dd73)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceTypeOptInPreference", value)


@jsii.data_type(
    jsii_type="aws.backupRegionSettings.BackupRegionSettingsConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "resource_type_opt_in_preference": "resourceTypeOptInPreference",
        "id": "id",
        "resource_type_management_preference": "resourceTypeManagementPreference",
    },
)
class BackupRegionSettingsConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        resource_type_opt_in_preference: typing.Mapping[builtins.str, typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
        id: typing.Optional[builtins.str] = None,
        resource_type_management_preference: typing.Optional[typing.Mapping[builtins.str, typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param resource_type_opt_in_preference: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_region_settings#resource_type_opt_in_preference BackupRegionSettings#resource_type_opt_in_preference}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_region_settings#id BackupRegionSettings#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param resource_type_management_preference: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_region_settings#resource_type_management_preference BackupRegionSettings#resource_type_management_preference}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7a5452678884488a52a9c7a3573173df2d6b39c8b3e14c76e0ea253d2980daa)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument resource_type_opt_in_preference", value=resource_type_opt_in_preference, expected_type=type_hints["resource_type_opt_in_preference"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument resource_type_management_preference", value=resource_type_management_preference, expected_type=type_hints["resource_type_management_preference"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "resource_type_opt_in_preference": resource_type_opt_in_preference,
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
        if id is not None:
            self._values["id"] = id
        if resource_type_management_preference is not None:
            self._values["resource_type_management_preference"] = resource_type_management_preference

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
    def resource_type_opt_in_preference(
        self,
    ) -> typing.Mapping[builtins.str, typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_region_settings#resource_type_opt_in_preference BackupRegionSettings#resource_type_opt_in_preference}.'''
        result = self._values.get("resource_type_opt_in_preference")
        assert result is not None, "Required property 'resource_type_opt_in_preference' is missing"
        return typing.cast(typing.Mapping[builtins.str, typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_region_settings#id BackupRegionSettings#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resource_type_management_preference(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_region_settings#resource_type_management_preference BackupRegionSettings#resource_type_management_preference}.'''
        result = self._values.get("resource_type_management_preference")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BackupRegionSettingsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "BackupRegionSettings",
    "BackupRegionSettingsConfig",
]

publication.publish()

def _typecheckingstub__c4fe4a97679f9dafed7468865aeef4b4024b40eb1712a003d3526e901323e531(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    resource_type_opt_in_preference: typing.Mapping[builtins.str, typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
    id: typing.Optional[builtins.str] = None,
    resource_type_management_preference: typing.Optional[typing.Mapping[builtins.str, typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]] = None,
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

def _typecheckingstub__808baa7f010b3d00b8bfd84ce282d487e6a562a336f14e7e69b7e21fe964e499(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__264cea9bff3ebe3becadce3b625604a758e7122a13fdcc8e6005e9ebe69d3956(
    value: typing.Mapping[builtins.str, typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d04beaf6af434de43fd02aaddfc1e3dc096ba5a2787fe9662cdf4ba8cf0dd73(
    value: typing.Mapping[builtins.str, typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7a5452678884488a52a9c7a3573173df2d6b39c8b3e14c76e0ea253d2980daa(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    resource_type_opt_in_preference: typing.Mapping[builtins.str, typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
    id: typing.Optional[builtins.str] = None,
    resource_type_management_preference: typing.Optional[typing.Mapping[builtins.str, typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]] = None,
) -> None:
    """Type checking stubs"""
    pass
