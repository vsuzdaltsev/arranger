'''
# `aws_iot_indexing_configuration`

Refer to the Terraform Registory for docs: [`aws_iot_indexing_configuration`](https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration).
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


class IotIndexingConfiguration(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotIndexingConfiguration.IotIndexingConfiguration",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration aws_iot_indexing_configuration}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        id: typing.Optional[builtins.str] = None,
        thing_group_indexing_configuration: typing.Optional[typing.Union["IotIndexingConfigurationThingGroupIndexingConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        thing_indexing_configuration: typing.Optional[typing.Union["IotIndexingConfigurationThingIndexingConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration aws_iot_indexing_configuration} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#id IotIndexingConfiguration#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param thing_group_indexing_configuration: thing_group_indexing_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#thing_group_indexing_configuration IotIndexingConfiguration#thing_group_indexing_configuration}
        :param thing_indexing_configuration: thing_indexing_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#thing_indexing_configuration IotIndexingConfiguration#thing_indexing_configuration}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3efdb565162c570328dc80c98445a7c8e8bb6b868798382a073d234fd7fcd5e9)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = IotIndexingConfigurationConfig(
            id=id,
            thing_group_indexing_configuration=thing_group_indexing_configuration,
            thing_indexing_configuration=thing_indexing_configuration,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putThingGroupIndexingConfiguration")
    def put_thing_group_indexing_configuration(
        self,
        *,
        thing_group_indexing_mode: builtins.str,
        custom_field: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IotIndexingConfigurationThingGroupIndexingConfigurationCustomField", typing.Dict[builtins.str, typing.Any]]]]] = None,
        managed_field: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IotIndexingConfigurationThingGroupIndexingConfigurationManagedField", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param thing_group_indexing_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#thing_group_indexing_mode IotIndexingConfiguration#thing_group_indexing_mode}.
        :param custom_field: custom_field block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#custom_field IotIndexingConfiguration#custom_field}
        :param managed_field: managed_field block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#managed_field IotIndexingConfiguration#managed_field}
        '''
        value = IotIndexingConfigurationThingGroupIndexingConfiguration(
            thing_group_indexing_mode=thing_group_indexing_mode,
            custom_field=custom_field,
            managed_field=managed_field,
        )

        return typing.cast(None, jsii.invoke(self, "putThingGroupIndexingConfiguration", [value]))

    @jsii.member(jsii_name="putThingIndexingConfiguration")
    def put_thing_indexing_configuration(
        self,
        *,
        thing_indexing_mode: builtins.str,
        custom_field: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IotIndexingConfigurationThingIndexingConfigurationCustomField", typing.Dict[builtins.str, typing.Any]]]]] = None,
        device_defender_indexing_mode: typing.Optional[builtins.str] = None,
        managed_field: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IotIndexingConfigurationThingIndexingConfigurationManagedField", typing.Dict[builtins.str, typing.Any]]]]] = None,
        named_shadow_indexing_mode: typing.Optional[builtins.str] = None,
        thing_connectivity_indexing_mode: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param thing_indexing_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#thing_indexing_mode IotIndexingConfiguration#thing_indexing_mode}.
        :param custom_field: custom_field block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#custom_field IotIndexingConfiguration#custom_field}
        :param device_defender_indexing_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#device_defender_indexing_mode IotIndexingConfiguration#device_defender_indexing_mode}.
        :param managed_field: managed_field block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#managed_field IotIndexingConfiguration#managed_field}
        :param named_shadow_indexing_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#named_shadow_indexing_mode IotIndexingConfiguration#named_shadow_indexing_mode}.
        :param thing_connectivity_indexing_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#thing_connectivity_indexing_mode IotIndexingConfiguration#thing_connectivity_indexing_mode}.
        '''
        value = IotIndexingConfigurationThingIndexingConfiguration(
            thing_indexing_mode=thing_indexing_mode,
            custom_field=custom_field,
            device_defender_indexing_mode=device_defender_indexing_mode,
            managed_field=managed_field,
            named_shadow_indexing_mode=named_shadow_indexing_mode,
            thing_connectivity_indexing_mode=thing_connectivity_indexing_mode,
        )

        return typing.cast(None, jsii.invoke(self, "putThingIndexingConfiguration", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetThingGroupIndexingConfiguration")
    def reset_thing_group_indexing_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetThingGroupIndexingConfiguration", []))

    @jsii.member(jsii_name="resetThingIndexingConfiguration")
    def reset_thing_indexing_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetThingIndexingConfiguration", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="thingGroupIndexingConfiguration")
    def thing_group_indexing_configuration(
        self,
    ) -> "IotIndexingConfigurationThingGroupIndexingConfigurationOutputReference":
        return typing.cast("IotIndexingConfigurationThingGroupIndexingConfigurationOutputReference", jsii.get(self, "thingGroupIndexingConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="thingIndexingConfiguration")
    def thing_indexing_configuration(
        self,
    ) -> "IotIndexingConfigurationThingIndexingConfigurationOutputReference":
        return typing.cast("IotIndexingConfigurationThingIndexingConfigurationOutputReference", jsii.get(self, "thingIndexingConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="thingGroupIndexingConfigurationInput")
    def thing_group_indexing_configuration_input(
        self,
    ) -> typing.Optional["IotIndexingConfigurationThingGroupIndexingConfiguration"]:
        return typing.cast(typing.Optional["IotIndexingConfigurationThingGroupIndexingConfiguration"], jsii.get(self, "thingGroupIndexingConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="thingIndexingConfigurationInput")
    def thing_indexing_configuration_input(
        self,
    ) -> typing.Optional["IotIndexingConfigurationThingIndexingConfiguration"]:
        return typing.cast(typing.Optional["IotIndexingConfigurationThingIndexingConfiguration"], jsii.get(self, "thingIndexingConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__211e24a0da2926b1fa00e13c845c548fd74761c80cc7db2994e794e991959977)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)


@jsii.data_type(
    jsii_type="aws.iotIndexingConfiguration.IotIndexingConfigurationConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "id": "id",
        "thing_group_indexing_configuration": "thingGroupIndexingConfiguration",
        "thing_indexing_configuration": "thingIndexingConfiguration",
    },
)
class IotIndexingConfigurationConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        id: typing.Optional[builtins.str] = None,
        thing_group_indexing_configuration: typing.Optional[typing.Union["IotIndexingConfigurationThingGroupIndexingConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        thing_indexing_configuration: typing.Optional[typing.Union["IotIndexingConfigurationThingIndexingConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#id IotIndexingConfiguration#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param thing_group_indexing_configuration: thing_group_indexing_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#thing_group_indexing_configuration IotIndexingConfiguration#thing_group_indexing_configuration}
        :param thing_indexing_configuration: thing_indexing_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#thing_indexing_configuration IotIndexingConfiguration#thing_indexing_configuration}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(thing_group_indexing_configuration, dict):
            thing_group_indexing_configuration = IotIndexingConfigurationThingGroupIndexingConfiguration(**thing_group_indexing_configuration)
        if isinstance(thing_indexing_configuration, dict):
            thing_indexing_configuration = IotIndexingConfigurationThingIndexingConfiguration(**thing_indexing_configuration)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0d8f5b7c127265003063a7e89a140a46f26eb3ae31a5a6af0f94eb32d594165)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument thing_group_indexing_configuration", value=thing_group_indexing_configuration, expected_type=type_hints["thing_group_indexing_configuration"])
            check_type(argname="argument thing_indexing_configuration", value=thing_indexing_configuration, expected_type=type_hints["thing_indexing_configuration"])
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
        if id is not None:
            self._values["id"] = id
        if thing_group_indexing_configuration is not None:
            self._values["thing_group_indexing_configuration"] = thing_group_indexing_configuration
        if thing_indexing_configuration is not None:
            self._values["thing_indexing_configuration"] = thing_indexing_configuration

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
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#id IotIndexingConfiguration#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def thing_group_indexing_configuration(
        self,
    ) -> typing.Optional["IotIndexingConfigurationThingGroupIndexingConfiguration"]:
        '''thing_group_indexing_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#thing_group_indexing_configuration IotIndexingConfiguration#thing_group_indexing_configuration}
        '''
        result = self._values.get("thing_group_indexing_configuration")
        return typing.cast(typing.Optional["IotIndexingConfigurationThingGroupIndexingConfiguration"], result)

    @builtins.property
    def thing_indexing_configuration(
        self,
    ) -> typing.Optional["IotIndexingConfigurationThingIndexingConfiguration"]:
        '''thing_indexing_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#thing_indexing_configuration IotIndexingConfiguration#thing_indexing_configuration}
        '''
        result = self._values.get("thing_indexing_configuration")
        return typing.cast(typing.Optional["IotIndexingConfigurationThingIndexingConfiguration"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IotIndexingConfigurationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.iotIndexingConfiguration.IotIndexingConfigurationThingGroupIndexingConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "thing_group_indexing_mode": "thingGroupIndexingMode",
        "custom_field": "customField",
        "managed_field": "managedField",
    },
)
class IotIndexingConfigurationThingGroupIndexingConfiguration:
    def __init__(
        self,
        *,
        thing_group_indexing_mode: builtins.str,
        custom_field: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IotIndexingConfigurationThingGroupIndexingConfigurationCustomField", typing.Dict[builtins.str, typing.Any]]]]] = None,
        managed_field: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IotIndexingConfigurationThingGroupIndexingConfigurationManagedField", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param thing_group_indexing_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#thing_group_indexing_mode IotIndexingConfiguration#thing_group_indexing_mode}.
        :param custom_field: custom_field block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#custom_field IotIndexingConfiguration#custom_field}
        :param managed_field: managed_field block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#managed_field IotIndexingConfiguration#managed_field}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa022887575e447d44ca0453b033110a7be50d17e49bc98bb0a4d0aba4176ee6)
            check_type(argname="argument thing_group_indexing_mode", value=thing_group_indexing_mode, expected_type=type_hints["thing_group_indexing_mode"])
            check_type(argname="argument custom_field", value=custom_field, expected_type=type_hints["custom_field"])
            check_type(argname="argument managed_field", value=managed_field, expected_type=type_hints["managed_field"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "thing_group_indexing_mode": thing_group_indexing_mode,
        }
        if custom_field is not None:
            self._values["custom_field"] = custom_field
        if managed_field is not None:
            self._values["managed_field"] = managed_field

    @builtins.property
    def thing_group_indexing_mode(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#thing_group_indexing_mode IotIndexingConfiguration#thing_group_indexing_mode}.'''
        result = self._values.get("thing_group_indexing_mode")
        assert result is not None, "Required property 'thing_group_indexing_mode' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def custom_field(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotIndexingConfigurationThingGroupIndexingConfigurationCustomField"]]]:
        '''custom_field block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#custom_field IotIndexingConfiguration#custom_field}
        '''
        result = self._values.get("custom_field")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotIndexingConfigurationThingGroupIndexingConfigurationCustomField"]]], result)

    @builtins.property
    def managed_field(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotIndexingConfigurationThingGroupIndexingConfigurationManagedField"]]]:
        '''managed_field block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#managed_field IotIndexingConfiguration#managed_field}
        '''
        result = self._values.get("managed_field")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotIndexingConfigurationThingGroupIndexingConfigurationManagedField"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IotIndexingConfigurationThingGroupIndexingConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.iotIndexingConfiguration.IotIndexingConfigurationThingGroupIndexingConfigurationCustomField",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "type": "type"},
)
class IotIndexingConfigurationThingGroupIndexingConfigurationCustomField:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#name IotIndexingConfiguration#name}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#type IotIndexingConfiguration#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf5a162cf38837a247806b3b86f6b214e3636b378da5e5c94c007b50fe9a756d)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#name IotIndexingConfiguration#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#type IotIndexingConfiguration#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IotIndexingConfigurationThingGroupIndexingConfigurationCustomField(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IotIndexingConfigurationThingGroupIndexingConfigurationCustomFieldList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotIndexingConfiguration.IotIndexingConfigurationThingGroupIndexingConfigurationCustomFieldList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2b64929951f8bcb9bf9ab6876d3ae3cfe439e0c2999e5b92cd4d7418769f4600)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "IotIndexingConfigurationThingGroupIndexingConfigurationCustomFieldOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__318a88d75457c2176562fa7d910c6a8a1f4b8502d3141996a403acb5058f816a)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("IotIndexingConfigurationThingGroupIndexingConfigurationCustomFieldOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03c022ef1475eedad7ececd844a85268a770670570bfeca05ad3986e6675a88c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8174a6dcc8efa13124f8c27f89d37c741cb416a7fa5e4b8846ba9f2cb75bcc7d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5c6735a0b8e6045b26f7b4f166975e95ef9672d9aa4ff55e6bf62af739853b77)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotIndexingConfigurationThingGroupIndexingConfigurationCustomField]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotIndexingConfigurationThingGroupIndexingConfigurationCustomField]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotIndexingConfigurationThingGroupIndexingConfigurationCustomField]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2eb55f89bc887c70cc6a74fbb97a9334f2b504d51bd29745b02b9c4bb9b2e25e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class IotIndexingConfigurationThingGroupIndexingConfigurationCustomFieldOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotIndexingConfiguration.IotIndexingConfigurationThingGroupIndexingConfigurationCustomFieldOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__df1a46a05479e27c928a118853f05d4b2541b8e91d3ac8b40377d4fbefa479ba)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__badae39cea91d5ccbf8d10fd7f8589b16ba5a86e4188dded25b72ef3c5722a10)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc30c57bb6b674d6d47d82fdc06bde3ee9e4f8cae89ff513ee2ce7cd7cf3bc16)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[IotIndexingConfigurationThingGroupIndexingConfigurationCustomField, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[IotIndexingConfigurationThingGroupIndexingConfigurationCustomField, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[IotIndexingConfigurationThingGroupIndexingConfigurationCustomField, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13816674c8aeb938f9a5b62b302d47e9d187611022c5046efc0da1959e9942e5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.iotIndexingConfiguration.IotIndexingConfigurationThingGroupIndexingConfigurationManagedField",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "type": "type"},
)
class IotIndexingConfigurationThingGroupIndexingConfigurationManagedField:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#name IotIndexingConfiguration#name}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#type IotIndexingConfiguration#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9cdf96e29c97fb33d0c1c3bc1331b19fa4147bb0a1f173e8afd7ee4207e046d3)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#name IotIndexingConfiguration#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#type IotIndexingConfiguration#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IotIndexingConfigurationThingGroupIndexingConfigurationManagedField(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IotIndexingConfigurationThingGroupIndexingConfigurationManagedFieldList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotIndexingConfiguration.IotIndexingConfigurationThingGroupIndexingConfigurationManagedFieldList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5732104826e919347258cc4dcd9be2f04b5799e07dbcc7e487c55062459ba53b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "IotIndexingConfigurationThingGroupIndexingConfigurationManagedFieldOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1526428d44c4306b684403809d851de1bf97581c057b944dbc908adbbdddcbcb)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("IotIndexingConfigurationThingGroupIndexingConfigurationManagedFieldOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c2cf5775d7dd518338511cf2526f570f8878d7bdd62acef39babbbeeae240128)
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
            type_hints = typing.get_type_hints(_typecheckingstub__441a90db19566c59ad536dbefa7a645dbf1ab094071e2fc2a003b8a2e9ba0900)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4d6fa8272e848a4f73bf14357f0585b28a3fd1b4eb699200782c67a0a277a103)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotIndexingConfigurationThingGroupIndexingConfigurationManagedField]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotIndexingConfigurationThingGroupIndexingConfigurationManagedField]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotIndexingConfigurationThingGroupIndexingConfigurationManagedField]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1fa2f13b62f7eb7baf03d28671ff8039b9a0e8f6a3837edc0b3e02a50b5d28c7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class IotIndexingConfigurationThingGroupIndexingConfigurationManagedFieldOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotIndexingConfiguration.IotIndexingConfigurationThingGroupIndexingConfigurationManagedFieldOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6b15059f6f1cf7925d018055c5688a491df9b58c8a248c3fe4b87261d85f9963)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94b76a2cd76cfa02216129d979cdff9284dfc24b192a73372620a881008cf561)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc97c113026969c32a176ececad3414cd823830e337750bc7e2cc00d30fc3407)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[IotIndexingConfigurationThingGroupIndexingConfigurationManagedField, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[IotIndexingConfigurationThingGroupIndexingConfigurationManagedField, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[IotIndexingConfigurationThingGroupIndexingConfigurationManagedField, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26e1e744a0ca622dbb456cb19b409a15ab329cff0447e63c0603c3baa7b7a9af)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class IotIndexingConfigurationThingGroupIndexingConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotIndexingConfiguration.IotIndexingConfigurationThingGroupIndexingConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__97ef81a105f782492790ea955404e12e790eb862a64d5a241076aeb5a6a5d4a1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCustomField")
    def put_custom_field(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotIndexingConfigurationThingGroupIndexingConfigurationCustomField, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b726ebb5d1516cf4ea8e42a67853b2e66b717d0eea407af0d27659cea8e3c8d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCustomField", [value]))

    @jsii.member(jsii_name="putManagedField")
    def put_managed_field(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotIndexingConfigurationThingGroupIndexingConfigurationManagedField, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d43994d5a4bacd0eb4012dd2ea3580a0993b984599416f8e8a91dfb0922dff0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putManagedField", [value]))

    @jsii.member(jsii_name="resetCustomField")
    def reset_custom_field(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomField", []))

    @jsii.member(jsii_name="resetManagedField")
    def reset_managed_field(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManagedField", []))

    @builtins.property
    @jsii.member(jsii_name="customField")
    def custom_field(
        self,
    ) -> IotIndexingConfigurationThingGroupIndexingConfigurationCustomFieldList:
        return typing.cast(IotIndexingConfigurationThingGroupIndexingConfigurationCustomFieldList, jsii.get(self, "customField"))

    @builtins.property
    @jsii.member(jsii_name="managedField")
    def managed_field(
        self,
    ) -> IotIndexingConfigurationThingGroupIndexingConfigurationManagedFieldList:
        return typing.cast(IotIndexingConfigurationThingGroupIndexingConfigurationManagedFieldList, jsii.get(self, "managedField"))

    @builtins.property
    @jsii.member(jsii_name="customFieldInput")
    def custom_field_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotIndexingConfigurationThingGroupIndexingConfigurationCustomField]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotIndexingConfigurationThingGroupIndexingConfigurationCustomField]]], jsii.get(self, "customFieldInput"))

    @builtins.property
    @jsii.member(jsii_name="managedFieldInput")
    def managed_field_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotIndexingConfigurationThingGroupIndexingConfigurationManagedField]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotIndexingConfigurationThingGroupIndexingConfigurationManagedField]]], jsii.get(self, "managedFieldInput"))

    @builtins.property
    @jsii.member(jsii_name="thingGroupIndexingModeInput")
    def thing_group_indexing_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "thingGroupIndexingModeInput"))

    @builtins.property
    @jsii.member(jsii_name="thingGroupIndexingMode")
    def thing_group_indexing_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "thingGroupIndexingMode"))

    @thing_group_indexing_mode.setter
    def thing_group_indexing_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77475e1d14a11b8a29e6946801cecdc19cf4eba6edfe723c1d452fec8b16781e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "thingGroupIndexingMode", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[IotIndexingConfigurationThingGroupIndexingConfiguration]:
        return typing.cast(typing.Optional[IotIndexingConfigurationThingGroupIndexingConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[IotIndexingConfigurationThingGroupIndexingConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d09ffb466e0c3dafa758f4721e1112a6b002da3c2462a85374feee4c604966d5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.iotIndexingConfiguration.IotIndexingConfigurationThingIndexingConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "thing_indexing_mode": "thingIndexingMode",
        "custom_field": "customField",
        "device_defender_indexing_mode": "deviceDefenderIndexingMode",
        "managed_field": "managedField",
        "named_shadow_indexing_mode": "namedShadowIndexingMode",
        "thing_connectivity_indexing_mode": "thingConnectivityIndexingMode",
    },
)
class IotIndexingConfigurationThingIndexingConfiguration:
    def __init__(
        self,
        *,
        thing_indexing_mode: builtins.str,
        custom_field: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IotIndexingConfigurationThingIndexingConfigurationCustomField", typing.Dict[builtins.str, typing.Any]]]]] = None,
        device_defender_indexing_mode: typing.Optional[builtins.str] = None,
        managed_field: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IotIndexingConfigurationThingIndexingConfigurationManagedField", typing.Dict[builtins.str, typing.Any]]]]] = None,
        named_shadow_indexing_mode: typing.Optional[builtins.str] = None,
        thing_connectivity_indexing_mode: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param thing_indexing_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#thing_indexing_mode IotIndexingConfiguration#thing_indexing_mode}.
        :param custom_field: custom_field block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#custom_field IotIndexingConfiguration#custom_field}
        :param device_defender_indexing_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#device_defender_indexing_mode IotIndexingConfiguration#device_defender_indexing_mode}.
        :param managed_field: managed_field block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#managed_field IotIndexingConfiguration#managed_field}
        :param named_shadow_indexing_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#named_shadow_indexing_mode IotIndexingConfiguration#named_shadow_indexing_mode}.
        :param thing_connectivity_indexing_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#thing_connectivity_indexing_mode IotIndexingConfiguration#thing_connectivity_indexing_mode}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2933ab96c91b9882ea8563cb53bd04ba55efa8904eb799e51cd6517e41660d33)
            check_type(argname="argument thing_indexing_mode", value=thing_indexing_mode, expected_type=type_hints["thing_indexing_mode"])
            check_type(argname="argument custom_field", value=custom_field, expected_type=type_hints["custom_field"])
            check_type(argname="argument device_defender_indexing_mode", value=device_defender_indexing_mode, expected_type=type_hints["device_defender_indexing_mode"])
            check_type(argname="argument managed_field", value=managed_field, expected_type=type_hints["managed_field"])
            check_type(argname="argument named_shadow_indexing_mode", value=named_shadow_indexing_mode, expected_type=type_hints["named_shadow_indexing_mode"])
            check_type(argname="argument thing_connectivity_indexing_mode", value=thing_connectivity_indexing_mode, expected_type=type_hints["thing_connectivity_indexing_mode"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "thing_indexing_mode": thing_indexing_mode,
        }
        if custom_field is not None:
            self._values["custom_field"] = custom_field
        if device_defender_indexing_mode is not None:
            self._values["device_defender_indexing_mode"] = device_defender_indexing_mode
        if managed_field is not None:
            self._values["managed_field"] = managed_field
        if named_shadow_indexing_mode is not None:
            self._values["named_shadow_indexing_mode"] = named_shadow_indexing_mode
        if thing_connectivity_indexing_mode is not None:
            self._values["thing_connectivity_indexing_mode"] = thing_connectivity_indexing_mode

    @builtins.property
    def thing_indexing_mode(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#thing_indexing_mode IotIndexingConfiguration#thing_indexing_mode}.'''
        result = self._values.get("thing_indexing_mode")
        assert result is not None, "Required property 'thing_indexing_mode' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def custom_field(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotIndexingConfigurationThingIndexingConfigurationCustomField"]]]:
        '''custom_field block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#custom_field IotIndexingConfiguration#custom_field}
        '''
        result = self._values.get("custom_field")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotIndexingConfigurationThingIndexingConfigurationCustomField"]]], result)

    @builtins.property
    def device_defender_indexing_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#device_defender_indexing_mode IotIndexingConfiguration#device_defender_indexing_mode}.'''
        result = self._values.get("device_defender_indexing_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def managed_field(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotIndexingConfigurationThingIndexingConfigurationManagedField"]]]:
        '''managed_field block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#managed_field IotIndexingConfiguration#managed_field}
        '''
        result = self._values.get("managed_field")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotIndexingConfigurationThingIndexingConfigurationManagedField"]]], result)

    @builtins.property
    def named_shadow_indexing_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#named_shadow_indexing_mode IotIndexingConfiguration#named_shadow_indexing_mode}.'''
        result = self._values.get("named_shadow_indexing_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def thing_connectivity_indexing_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#thing_connectivity_indexing_mode IotIndexingConfiguration#thing_connectivity_indexing_mode}.'''
        result = self._values.get("thing_connectivity_indexing_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IotIndexingConfigurationThingIndexingConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.iotIndexingConfiguration.IotIndexingConfigurationThingIndexingConfigurationCustomField",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "type": "type"},
)
class IotIndexingConfigurationThingIndexingConfigurationCustomField:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#name IotIndexingConfiguration#name}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#type IotIndexingConfiguration#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9526c2ef7fb55f470f6522f687d09d9e8a1d9cfe8ddee10d17760d9e25f44af6)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#name IotIndexingConfiguration#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#type IotIndexingConfiguration#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IotIndexingConfigurationThingIndexingConfigurationCustomField(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IotIndexingConfigurationThingIndexingConfigurationCustomFieldList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotIndexingConfiguration.IotIndexingConfigurationThingIndexingConfigurationCustomFieldList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8c3ed5450921a75737afc014e191e52531056c2405a1a09fac3de173d96bd16e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "IotIndexingConfigurationThingIndexingConfigurationCustomFieldOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea624f3664959bdcb028150c914e62c6e9806305468bd784e10504a970f1f352)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("IotIndexingConfigurationThingIndexingConfigurationCustomFieldOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf041f2d804ee127276d2fa1b2d7aa104f7da4726da9381827be332f4e18e797)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ab7acb0c6efdb1ec58cae2084f0d166f6f442032a17f920c15c153f4ce68d11f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f72e3fbda98586e043b830ae17766f7318d05f6f7116f30dff7b7bd1f3c35525)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotIndexingConfigurationThingIndexingConfigurationCustomField]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotIndexingConfigurationThingIndexingConfigurationCustomField]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotIndexingConfigurationThingIndexingConfigurationCustomField]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e961c799f4c6949dd3ace65b31c8a96dfb8bbd86f8b06891e64dbe89a962db8e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class IotIndexingConfigurationThingIndexingConfigurationCustomFieldOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotIndexingConfiguration.IotIndexingConfigurationThingIndexingConfigurationCustomFieldOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__095be104886faa85a7a32f317040adecb70ca2b83d667ea93387c362e5e2e479)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c2b77f86bb03a343d082b4dc63fc31c692e5ff2747a5be731b184a57a429c79)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a7650215cb10c7e8b529f07d4128aec22c56f71f0508cd3803aea2975e393e9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[IotIndexingConfigurationThingIndexingConfigurationCustomField, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[IotIndexingConfigurationThingIndexingConfigurationCustomField, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[IotIndexingConfigurationThingIndexingConfigurationCustomField, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be40ed4ebe8b765215d8858bf96cf8eea25da03b54b66308fc1f92f7e90ce90f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.iotIndexingConfiguration.IotIndexingConfigurationThingIndexingConfigurationManagedField",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "type": "type"},
)
class IotIndexingConfigurationThingIndexingConfigurationManagedField:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#name IotIndexingConfiguration#name}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#type IotIndexingConfiguration#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4950d77a771f58bb0254ae92cc09d78252dac7eb2b7b7a456f26b6f551875709)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#name IotIndexingConfiguration#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#type IotIndexingConfiguration#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IotIndexingConfigurationThingIndexingConfigurationManagedField(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IotIndexingConfigurationThingIndexingConfigurationManagedFieldList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotIndexingConfiguration.IotIndexingConfigurationThingIndexingConfigurationManagedFieldList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9ad1ea20b53f7e0ee2be1b879f2d570f9abce55200df2693c86927d4e3a2fc03)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "IotIndexingConfigurationThingIndexingConfigurationManagedFieldOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__093c2a25530b94bc7abb204f759e09598d5037abd8731113cb64248afc5110a5)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("IotIndexingConfigurationThingIndexingConfigurationManagedFieldOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a3c5a1a7f7496191b9ff3bd653b4eea9c43de88d2fffcc1ec42e51e14ae1080)
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
            type_hints = typing.get_type_hints(_typecheckingstub__30dbe7b15a250adc384b631bf62ebbc7eb2bf54c138083d4640d61f62eec5e47)
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
            type_hints = typing.get_type_hints(_typecheckingstub__fc188c5257479b0f58d1f6ee03385a04b2ed5282edf2ccb7527f5fac129e0df7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotIndexingConfigurationThingIndexingConfigurationManagedField]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotIndexingConfigurationThingIndexingConfigurationManagedField]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotIndexingConfigurationThingIndexingConfigurationManagedField]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3bb6c54354fae9154393cc851411846225a21db95c58a11f8f5fcbb30b17ed4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class IotIndexingConfigurationThingIndexingConfigurationManagedFieldOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotIndexingConfiguration.IotIndexingConfigurationThingIndexingConfigurationManagedFieldOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__92ac9adf0a43f1c4f8783963d607a9e82d2db198d472602e203671ec09a693b7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba5156d0a7ce1f7b9334696d00ed2295dd0a8c7948d72bcf4b4b81e5f1044417)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7295a02a0f4ecd155402f5cc25422dd7247dd31dd55605124722cf4206e68f2d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[IotIndexingConfigurationThingIndexingConfigurationManagedField, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[IotIndexingConfigurationThingIndexingConfigurationManagedField, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[IotIndexingConfigurationThingIndexingConfigurationManagedField, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5fc0f2ce65c442775e421c88b12d6bd14679ac576ebb983d78736a815728c2bd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class IotIndexingConfigurationThingIndexingConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotIndexingConfiguration.IotIndexingConfigurationThingIndexingConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__78d98b356a6f591b31bcc4720e43ea9dfc6466c2dcdc16625ab343d200332bbd)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCustomField")
    def put_custom_field(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotIndexingConfigurationThingIndexingConfigurationCustomField, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6b3487ad21b33b5fb3ac5f4bd451315cac1b18c0e905d55cf5a5e68b32d9802)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCustomField", [value]))

    @jsii.member(jsii_name="putManagedField")
    def put_managed_field(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotIndexingConfigurationThingIndexingConfigurationManagedField, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__904275f8627c5e525f7d5f9de3a4ff8d968aef77f6f2b3ad96022b3f2fe7fc2a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putManagedField", [value]))

    @jsii.member(jsii_name="resetCustomField")
    def reset_custom_field(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomField", []))

    @jsii.member(jsii_name="resetDeviceDefenderIndexingMode")
    def reset_device_defender_indexing_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeviceDefenderIndexingMode", []))

    @jsii.member(jsii_name="resetManagedField")
    def reset_managed_field(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManagedField", []))

    @jsii.member(jsii_name="resetNamedShadowIndexingMode")
    def reset_named_shadow_indexing_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamedShadowIndexingMode", []))

    @jsii.member(jsii_name="resetThingConnectivityIndexingMode")
    def reset_thing_connectivity_indexing_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetThingConnectivityIndexingMode", []))

    @builtins.property
    @jsii.member(jsii_name="customField")
    def custom_field(
        self,
    ) -> IotIndexingConfigurationThingIndexingConfigurationCustomFieldList:
        return typing.cast(IotIndexingConfigurationThingIndexingConfigurationCustomFieldList, jsii.get(self, "customField"))

    @builtins.property
    @jsii.member(jsii_name="managedField")
    def managed_field(
        self,
    ) -> IotIndexingConfigurationThingIndexingConfigurationManagedFieldList:
        return typing.cast(IotIndexingConfigurationThingIndexingConfigurationManagedFieldList, jsii.get(self, "managedField"))

    @builtins.property
    @jsii.member(jsii_name="customFieldInput")
    def custom_field_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotIndexingConfigurationThingIndexingConfigurationCustomField]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotIndexingConfigurationThingIndexingConfigurationCustomField]]], jsii.get(self, "customFieldInput"))

    @builtins.property
    @jsii.member(jsii_name="deviceDefenderIndexingModeInput")
    def device_defender_indexing_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deviceDefenderIndexingModeInput"))

    @builtins.property
    @jsii.member(jsii_name="managedFieldInput")
    def managed_field_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotIndexingConfigurationThingIndexingConfigurationManagedField]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotIndexingConfigurationThingIndexingConfigurationManagedField]]], jsii.get(self, "managedFieldInput"))

    @builtins.property
    @jsii.member(jsii_name="namedShadowIndexingModeInput")
    def named_shadow_indexing_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namedShadowIndexingModeInput"))

    @builtins.property
    @jsii.member(jsii_name="thingConnectivityIndexingModeInput")
    def thing_connectivity_indexing_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "thingConnectivityIndexingModeInput"))

    @builtins.property
    @jsii.member(jsii_name="thingIndexingModeInput")
    def thing_indexing_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "thingIndexingModeInput"))

    @builtins.property
    @jsii.member(jsii_name="deviceDefenderIndexingMode")
    def device_defender_indexing_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deviceDefenderIndexingMode"))

    @device_defender_indexing_mode.setter
    def device_defender_indexing_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1faa7ca805f05219df0ca02821ff447935b3166d2feaa67d137eb0dd1a21a747)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deviceDefenderIndexingMode", value)

    @builtins.property
    @jsii.member(jsii_name="namedShadowIndexingMode")
    def named_shadow_indexing_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namedShadowIndexingMode"))

    @named_shadow_indexing_mode.setter
    def named_shadow_indexing_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8dffd43961d209428932c910f4a3a2b870e9ce542db56467b7f26a3c4ac9aec1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namedShadowIndexingMode", value)

    @builtins.property
    @jsii.member(jsii_name="thingConnectivityIndexingMode")
    def thing_connectivity_indexing_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "thingConnectivityIndexingMode"))

    @thing_connectivity_indexing_mode.setter
    def thing_connectivity_indexing_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__012e6dd8fb6f136473cdcadfbd4515aa72fbd781297b0dc2836d8f0b8c2056a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "thingConnectivityIndexingMode", value)

    @builtins.property
    @jsii.member(jsii_name="thingIndexingMode")
    def thing_indexing_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "thingIndexingMode"))

    @thing_indexing_mode.setter
    def thing_indexing_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9447c20cef25bc1c07c48bf59ee498199dd146806877392ad2b8c7702f4654e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "thingIndexingMode", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[IotIndexingConfigurationThingIndexingConfiguration]:
        return typing.cast(typing.Optional[IotIndexingConfigurationThingIndexingConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[IotIndexingConfigurationThingIndexingConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__55d9e10c4a16d0e342ccd08a1d9323f29ef372f69360b7dbc786314183e682bf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "IotIndexingConfiguration",
    "IotIndexingConfigurationConfig",
    "IotIndexingConfigurationThingGroupIndexingConfiguration",
    "IotIndexingConfigurationThingGroupIndexingConfigurationCustomField",
    "IotIndexingConfigurationThingGroupIndexingConfigurationCustomFieldList",
    "IotIndexingConfigurationThingGroupIndexingConfigurationCustomFieldOutputReference",
    "IotIndexingConfigurationThingGroupIndexingConfigurationManagedField",
    "IotIndexingConfigurationThingGroupIndexingConfigurationManagedFieldList",
    "IotIndexingConfigurationThingGroupIndexingConfigurationManagedFieldOutputReference",
    "IotIndexingConfigurationThingGroupIndexingConfigurationOutputReference",
    "IotIndexingConfigurationThingIndexingConfiguration",
    "IotIndexingConfigurationThingIndexingConfigurationCustomField",
    "IotIndexingConfigurationThingIndexingConfigurationCustomFieldList",
    "IotIndexingConfigurationThingIndexingConfigurationCustomFieldOutputReference",
    "IotIndexingConfigurationThingIndexingConfigurationManagedField",
    "IotIndexingConfigurationThingIndexingConfigurationManagedFieldList",
    "IotIndexingConfigurationThingIndexingConfigurationManagedFieldOutputReference",
    "IotIndexingConfigurationThingIndexingConfigurationOutputReference",
]

publication.publish()

def _typecheckingstub__3efdb565162c570328dc80c98445a7c8e8bb6b868798382a073d234fd7fcd5e9(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    id: typing.Optional[builtins.str] = None,
    thing_group_indexing_configuration: typing.Optional[typing.Union[IotIndexingConfigurationThingGroupIndexingConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    thing_indexing_configuration: typing.Optional[typing.Union[IotIndexingConfigurationThingIndexingConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__211e24a0da2926b1fa00e13c845c548fd74761c80cc7db2994e794e991959977(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0d8f5b7c127265003063a7e89a140a46f26eb3ae31a5a6af0f94eb32d594165(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    id: typing.Optional[builtins.str] = None,
    thing_group_indexing_configuration: typing.Optional[typing.Union[IotIndexingConfigurationThingGroupIndexingConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    thing_indexing_configuration: typing.Optional[typing.Union[IotIndexingConfigurationThingIndexingConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa022887575e447d44ca0453b033110a7be50d17e49bc98bb0a4d0aba4176ee6(
    *,
    thing_group_indexing_mode: builtins.str,
    custom_field: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotIndexingConfigurationThingGroupIndexingConfigurationCustomField, typing.Dict[builtins.str, typing.Any]]]]] = None,
    managed_field: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotIndexingConfigurationThingGroupIndexingConfigurationManagedField, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf5a162cf38837a247806b3b86f6b214e3636b378da5e5c94c007b50fe9a756d(
    *,
    name: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b64929951f8bcb9bf9ab6876d3ae3cfe439e0c2999e5b92cd4d7418769f4600(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__318a88d75457c2176562fa7d910c6a8a1f4b8502d3141996a403acb5058f816a(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03c022ef1475eedad7ececd844a85268a770670570bfeca05ad3986e6675a88c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8174a6dcc8efa13124f8c27f89d37c741cb416a7fa5e4b8846ba9f2cb75bcc7d(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c6735a0b8e6045b26f7b4f166975e95ef9672d9aa4ff55e6bf62af739853b77(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2eb55f89bc887c70cc6a74fbb97a9334f2b504d51bd29745b02b9c4bb9b2e25e(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotIndexingConfigurationThingGroupIndexingConfigurationCustomField]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df1a46a05479e27c928a118853f05d4b2541b8e91d3ac8b40377d4fbefa479ba(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__badae39cea91d5ccbf8d10fd7f8589b16ba5a86e4188dded25b72ef3c5722a10(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc30c57bb6b674d6d47d82fdc06bde3ee9e4f8cae89ff513ee2ce7cd7cf3bc16(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13816674c8aeb938f9a5b62b302d47e9d187611022c5046efc0da1959e9942e5(
    value: typing.Optional[typing.Union[IotIndexingConfigurationThingGroupIndexingConfigurationCustomField, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9cdf96e29c97fb33d0c1c3bc1331b19fa4147bb0a1f173e8afd7ee4207e046d3(
    *,
    name: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5732104826e919347258cc4dcd9be2f04b5799e07dbcc7e487c55062459ba53b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1526428d44c4306b684403809d851de1bf97581c057b944dbc908adbbdddcbcb(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2cf5775d7dd518338511cf2526f570f8878d7bdd62acef39babbbeeae240128(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__441a90db19566c59ad536dbefa7a645dbf1ab094071e2fc2a003b8a2e9ba0900(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d6fa8272e848a4f73bf14357f0585b28a3fd1b4eb699200782c67a0a277a103(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1fa2f13b62f7eb7baf03d28671ff8039b9a0e8f6a3837edc0b3e02a50b5d28c7(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotIndexingConfigurationThingGroupIndexingConfigurationManagedField]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b15059f6f1cf7925d018055c5688a491df9b58c8a248c3fe4b87261d85f9963(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94b76a2cd76cfa02216129d979cdff9284dfc24b192a73372620a881008cf561(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc97c113026969c32a176ececad3414cd823830e337750bc7e2cc00d30fc3407(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26e1e744a0ca622dbb456cb19b409a15ab329cff0447e63c0603c3baa7b7a9af(
    value: typing.Optional[typing.Union[IotIndexingConfigurationThingGroupIndexingConfigurationManagedField, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97ef81a105f782492790ea955404e12e790eb862a64d5a241076aeb5a6a5d4a1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b726ebb5d1516cf4ea8e42a67853b2e66b717d0eea407af0d27659cea8e3c8d(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotIndexingConfigurationThingGroupIndexingConfigurationCustomField, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d43994d5a4bacd0eb4012dd2ea3580a0993b984599416f8e8a91dfb0922dff0(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotIndexingConfigurationThingGroupIndexingConfigurationManagedField, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77475e1d14a11b8a29e6946801cecdc19cf4eba6edfe723c1d452fec8b16781e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d09ffb466e0c3dafa758f4721e1112a6b002da3c2462a85374feee4c604966d5(
    value: typing.Optional[IotIndexingConfigurationThingGroupIndexingConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2933ab96c91b9882ea8563cb53bd04ba55efa8904eb799e51cd6517e41660d33(
    *,
    thing_indexing_mode: builtins.str,
    custom_field: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotIndexingConfigurationThingIndexingConfigurationCustomField, typing.Dict[builtins.str, typing.Any]]]]] = None,
    device_defender_indexing_mode: typing.Optional[builtins.str] = None,
    managed_field: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotIndexingConfigurationThingIndexingConfigurationManagedField, typing.Dict[builtins.str, typing.Any]]]]] = None,
    named_shadow_indexing_mode: typing.Optional[builtins.str] = None,
    thing_connectivity_indexing_mode: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9526c2ef7fb55f470f6522f687d09d9e8a1d9cfe8ddee10d17760d9e25f44af6(
    *,
    name: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c3ed5450921a75737afc014e191e52531056c2405a1a09fac3de173d96bd16e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea624f3664959bdcb028150c914e62c6e9806305468bd784e10504a970f1f352(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf041f2d804ee127276d2fa1b2d7aa104f7da4726da9381827be332f4e18e797(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab7acb0c6efdb1ec58cae2084f0d166f6f442032a17f920c15c153f4ce68d11f(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f72e3fbda98586e043b830ae17766f7318d05f6f7116f30dff7b7bd1f3c35525(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e961c799f4c6949dd3ace65b31c8a96dfb8bbd86f8b06891e64dbe89a962db8e(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotIndexingConfigurationThingIndexingConfigurationCustomField]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__095be104886faa85a7a32f317040adecb70ca2b83d667ea93387c362e5e2e479(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c2b77f86bb03a343d082b4dc63fc31c692e5ff2747a5be731b184a57a429c79(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a7650215cb10c7e8b529f07d4128aec22c56f71f0508cd3803aea2975e393e9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be40ed4ebe8b765215d8858bf96cf8eea25da03b54b66308fc1f92f7e90ce90f(
    value: typing.Optional[typing.Union[IotIndexingConfigurationThingIndexingConfigurationCustomField, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4950d77a771f58bb0254ae92cc09d78252dac7eb2b7b7a456f26b6f551875709(
    *,
    name: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ad1ea20b53f7e0ee2be1b879f2d570f9abce55200df2693c86927d4e3a2fc03(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__093c2a25530b94bc7abb204f759e09598d5037abd8731113cb64248afc5110a5(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a3c5a1a7f7496191b9ff3bd653b4eea9c43de88d2fffcc1ec42e51e14ae1080(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30dbe7b15a250adc384b631bf62ebbc7eb2bf54c138083d4640d61f62eec5e47(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc188c5257479b0f58d1f6ee03385a04b2ed5282edf2ccb7527f5fac129e0df7(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3bb6c54354fae9154393cc851411846225a21db95c58a11f8f5fcbb30b17ed4(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotIndexingConfigurationThingIndexingConfigurationManagedField]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92ac9adf0a43f1c4f8783963d607a9e82d2db198d472602e203671ec09a693b7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba5156d0a7ce1f7b9334696d00ed2295dd0a8c7948d72bcf4b4b81e5f1044417(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7295a02a0f4ecd155402f5cc25422dd7247dd31dd55605124722cf4206e68f2d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5fc0f2ce65c442775e421c88b12d6bd14679ac576ebb983d78736a815728c2bd(
    value: typing.Optional[typing.Union[IotIndexingConfigurationThingIndexingConfigurationManagedField, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78d98b356a6f591b31bcc4720e43ea9dfc6466c2dcdc16625ab343d200332bbd(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6b3487ad21b33b5fb3ac5f4bd451315cac1b18c0e905d55cf5a5e68b32d9802(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotIndexingConfigurationThingIndexingConfigurationCustomField, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__904275f8627c5e525f7d5f9de3a4ff8d968aef77f6f2b3ad96022b3f2fe7fc2a(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotIndexingConfigurationThingIndexingConfigurationManagedField, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1faa7ca805f05219df0ca02821ff447935b3166d2feaa67d137eb0dd1a21a747(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8dffd43961d209428932c910f4a3a2b870e9ce542db56467b7f26a3c4ac9aec1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__012e6dd8fb6f136473cdcadfbd4515aa72fbd781297b0dc2836d8f0b8c2056a2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9447c20cef25bc1c07c48bf59ee498199dd146806877392ad2b8c7702f4654e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55d9e10c4a16d0e342ccd08a1d9323f29ef372f69360b7dbc786314183e682bf(
    value: typing.Optional[IotIndexingConfigurationThingIndexingConfiguration],
) -> None:
    """Type checking stubs"""
    pass
