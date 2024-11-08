'''
# `aws_emr_instance_fleet`

Refer to the Terraform Registory for docs: [`aws_emr_instance_fleet`](https://www.terraform.io/docs/providers/aws/r/emr_instance_fleet).
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


class EmrInstanceFleet(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.emrInstanceFleet.EmrInstanceFleet",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/emr_instance_fleet aws_emr_instance_fleet}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        cluster_id: builtins.str,
        id: typing.Optional[builtins.str] = None,
        instance_type_configs: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EmrInstanceFleetInstanceTypeConfigs", typing.Dict[builtins.str, typing.Any]]]]] = None,
        launch_specifications: typing.Optional[typing.Union["EmrInstanceFleetLaunchSpecifications", typing.Dict[builtins.str, typing.Any]]] = None,
        name: typing.Optional[builtins.str] = None,
        target_on_demand_capacity: typing.Optional[jsii.Number] = None,
        target_spot_capacity: typing.Optional[jsii.Number] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/emr_instance_fleet aws_emr_instance_fleet} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param cluster_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_instance_fleet#cluster_id EmrInstanceFleet#cluster_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_instance_fleet#id EmrInstanceFleet#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param instance_type_configs: instance_type_configs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_instance_fleet#instance_type_configs EmrInstanceFleet#instance_type_configs}
        :param launch_specifications: launch_specifications block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_instance_fleet#launch_specifications EmrInstanceFleet#launch_specifications}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_instance_fleet#name EmrInstanceFleet#name}.
        :param target_on_demand_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_instance_fleet#target_on_demand_capacity EmrInstanceFleet#target_on_demand_capacity}.
        :param target_spot_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_instance_fleet#target_spot_capacity EmrInstanceFleet#target_spot_capacity}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97d9f24fc9726abc0a884cb8006305658dd53fda6fc8b2a796ba2cea8cc2ccd7)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = EmrInstanceFleetConfig(
            cluster_id=cluster_id,
            id=id,
            instance_type_configs=instance_type_configs,
            launch_specifications=launch_specifications,
            name=name,
            target_on_demand_capacity=target_on_demand_capacity,
            target_spot_capacity=target_spot_capacity,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putInstanceTypeConfigs")
    def put_instance_type_configs(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EmrInstanceFleetInstanceTypeConfigs", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e88c5cf7e5502990e8fa8b97f133b50167e544c358d64bd0e002218aa64f27db)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putInstanceTypeConfigs", [value]))

    @jsii.member(jsii_name="putLaunchSpecifications")
    def put_launch_specifications(
        self,
        *,
        on_demand_specification: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EmrInstanceFleetLaunchSpecificationsOnDemandSpecification", typing.Dict[builtins.str, typing.Any]]]]] = None,
        spot_specification: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EmrInstanceFleetLaunchSpecificationsSpotSpecification", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param on_demand_specification: on_demand_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_instance_fleet#on_demand_specification EmrInstanceFleet#on_demand_specification}
        :param spot_specification: spot_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_instance_fleet#spot_specification EmrInstanceFleet#spot_specification}
        '''
        value = EmrInstanceFleetLaunchSpecifications(
            on_demand_specification=on_demand_specification,
            spot_specification=spot_specification,
        )

        return typing.cast(None, jsii.invoke(self, "putLaunchSpecifications", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetInstanceTypeConfigs")
    def reset_instance_type_configs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceTypeConfigs", []))

    @jsii.member(jsii_name="resetLaunchSpecifications")
    def reset_launch_specifications(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLaunchSpecifications", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetTargetOnDemandCapacity")
    def reset_target_on_demand_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetOnDemandCapacity", []))

    @jsii.member(jsii_name="resetTargetSpotCapacity")
    def reset_target_spot_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetSpotCapacity", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="instanceTypeConfigs")
    def instance_type_configs(self) -> "EmrInstanceFleetInstanceTypeConfigsList":
        return typing.cast("EmrInstanceFleetInstanceTypeConfigsList", jsii.get(self, "instanceTypeConfigs"))

    @builtins.property
    @jsii.member(jsii_name="launchSpecifications")
    def launch_specifications(
        self,
    ) -> "EmrInstanceFleetLaunchSpecificationsOutputReference":
        return typing.cast("EmrInstanceFleetLaunchSpecificationsOutputReference", jsii.get(self, "launchSpecifications"))

    @builtins.property
    @jsii.member(jsii_name="provisionedOnDemandCapacity")
    def provisioned_on_demand_capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "provisionedOnDemandCapacity"))

    @builtins.property
    @jsii.member(jsii_name="provisionedSpotCapacity")
    def provisioned_spot_capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "provisionedSpotCapacity"))

    @builtins.property
    @jsii.member(jsii_name="clusterIdInput")
    def cluster_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceTypeConfigsInput")
    def instance_type_configs_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EmrInstanceFleetInstanceTypeConfigs"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EmrInstanceFleetInstanceTypeConfigs"]]], jsii.get(self, "instanceTypeConfigsInput"))

    @builtins.property
    @jsii.member(jsii_name="launchSpecificationsInput")
    def launch_specifications_input(
        self,
    ) -> typing.Optional["EmrInstanceFleetLaunchSpecifications"]:
        return typing.cast(typing.Optional["EmrInstanceFleetLaunchSpecifications"], jsii.get(self, "launchSpecificationsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="targetOnDemandCapacityInput")
    def target_on_demand_capacity_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "targetOnDemandCapacityInput"))

    @builtins.property
    @jsii.member(jsii_name="targetSpotCapacityInput")
    def target_spot_capacity_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "targetSpotCapacityInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterId")
    def cluster_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterId"))

    @cluster_id.setter
    def cluster_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e93f004a65c896a912667e94c48e76918f1159796f3e6eb1ba57625eb0cd3d7f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60185f0b7c296a6f1c6ae6874483968701eeb5b642d682c08b20c057e072e0d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe027095b92ee7235c2233433eaf4f43f302a5be78e6e6a5767a7a117fc3fcd4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="targetOnDemandCapacity")
    def target_on_demand_capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "targetOnDemandCapacity"))

    @target_on_demand_capacity.setter
    def target_on_demand_capacity(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3221d2006d429a628ec218b11fbb6bb8b65c073dcb45f90a793e5865100ce8fd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetOnDemandCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="targetSpotCapacity")
    def target_spot_capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "targetSpotCapacity"))

    @target_spot_capacity.setter
    def target_spot_capacity(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0bc688a59f3c83c894c98afe73b021060e1aea1ef6ab61d7419ae2052e42db7d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetSpotCapacity", value)


@jsii.data_type(
    jsii_type="aws.emrInstanceFleet.EmrInstanceFleetConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "cluster_id": "clusterId",
        "id": "id",
        "instance_type_configs": "instanceTypeConfigs",
        "launch_specifications": "launchSpecifications",
        "name": "name",
        "target_on_demand_capacity": "targetOnDemandCapacity",
        "target_spot_capacity": "targetSpotCapacity",
    },
)
class EmrInstanceFleetConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        cluster_id: builtins.str,
        id: typing.Optional[builtins.str] = None,
        instance_type_configs: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EmrInstanceFleetInstanceTypeConfigs", typing.Dict[builtins.str, typing.Any]]]]] = None,
        launch_specifications: typing.Optional[typing.Union["EmrInstanceFleetLaunchSpecifications", typing.Dict[builtins.str, typing.Any]]] = None,
        name: typing.Optional[builtins.str] = None,
        target_on_demand_capacity: typing.Optional[jsii.Number] = None,
        target_spot_capacity: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param cluster_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_instance_fleet#cluster_id EmrInstanceFleet#cluster_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_instance_fleet#id EmrInstanceFleet#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param instance_type_configs: instance_type_configs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_instance_fleet#instance_type_configs EmrInstanceFleet#instance_type_configs}
        :param launch_specifications: launch_specifications block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_instance_fleet#launch_specifications EmrInstanceFleet#launch_specifications}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_instance_fleet#name EmrInstanceFleet#name}.
        :param target_on_demand_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_instance_fleet#target_on_demand_capacity EmrInstanceFleet#target_on_demand_capacity}.
        :param target_spot_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_instance_fleet#target_spot_capacity EmrInstanceFleet#target_spot_capacity}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(launch_specifications, dict):
            launch_specifications = EmrInstanceFleetLaunchSpecifications(**launch_specifications)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__447642bb86d6caed80f2d1495caac82c24216169f0ffcd8f7186e33d192a567f)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument cluster_id", value=cluster_id, expected_type=type_hints["cluster_id"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument instance_type_configs", value=instance_type_configs, expected_type=type_hints["instance_type_configs"])
            check_type(argname="argument launch_specifications", value=launch_specifications, expected_type=type_hints["launch_specifications"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument target_on_demand_capacity", value=target_on_demand_capacity, expected_type=type_hints["target_on_demand_capacity"])
            check_type(argname="argument target_spot_capacity", value=target_spot_capacity, expected_type=type_hints["target_spot_capacity"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cluster_id": cluster_id,
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
        if instance_type_configs is not None:
            self._values["instance_type_configs"] = instance_type_configs
        if launch_specifications is not None:
            self._values["launch_specifications"] = launch_specifications
        if name is not None:
            self._values["name"] = name
        if target_on_demand_capacity is not None:
            self._values["target_on_demand_capacity"] = target_on_demand_capacity
        if target_spot_capacity is not None:
            self._values["target_spot_capacity"] = target_spot_capacity

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
    def cluster_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_instance_fleet#cluster_id EmrInstanceFleet#cluster_id}.'''
        result = self._values.get("cluster_id")
        assert result is not None, "Required property 'cluster_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_instance_fleet#id EmrInstanceFleet#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance_type_configs(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EmrInstanceFleetInstanceTypeConfigs"]]]:
        '''instance_type_configs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_instance_fleet#instance_type_configs EmrInstanceFleet#instance_type_configs}
        '''
        result = self._values.get("instance_type_configs")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EmrInstanceFleetInstanceTypeConfigs"]]], result)

    @builtins.property
    def launch_specifications(
        self,
    ) -> typing.Optional["EmrInstanceFleetLaunchSpecifications"]:
        '''launch_specifications block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_instance_fleet#launch_specifications EmrInstanceFleet#launch_specifications}
        '''
        result = self._values.get("launch_specifications")
        return typing.cast(typing.Optional["EmrInstanceFleetLaunchSpecifications"], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_instance_fleet#name EmrInstanceFleet#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_on_demand_capacity(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_instance_fleet#target_on_demand_capacity EmrInstanceFleet#target_on_demand_capacity}.'''
        result = self._values.get("target_on_demand_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def target_spot_capacity(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_instance_fleet#target_spot_capacity EmrInstanceFleet#target_spot_capacity}.'''
        result = self._values.get("target_spot_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmrInstanceFleetConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.emrInstanceFleet.EmrInstanceFleetInstanceTypeConfigs",
    jsii_struct_bases=[],
    name_mapping={
        "instance_type": "instanceType",
        "bid_price": "bidPrice",
        "bid_price_as_percentage_of_on_demand_price": "bidPriceAsPercentageOfOnDemandPrice",
        "configurations": "configurations",
        "ebs_config": "ebsConfig",
        "weighted_capacity": "weightedCapacity",
    },
)
class EmrInstanceFleetInstanceTypeConfigs:
    def __init__(
        self,
        *,
        instance_type: builtins.str,
        bid_price: typing.Optional[builtins.str] = None,
        bid_price_as_percentage_of_on_demand_price: typing.Optional[jsii.Number] = None,
        configurations: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EmrInstanceFleetInstanceTypeConfigsConfigurations", typing.Dict[builtins.str, typing.Any]]]]] = None,
        ebs_config: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EmrInstanceFleetInstanceTypeConfigsEbsConfig", typing.Dict[builtins.str, typing.Any]]]]] = None,
        weighted_capacity: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param instance_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_instance_fleet#instance_type EmrInstanceFleet#instance_type}.
        :param bid_price: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_instance_fleet#bid_price EmrInstanceFleet#bid_price}.
        :param bid_price_as_percentage_of_on_demand_price: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_instance_fleet#bid_price_as_percentage_of_on_demand_price EmrInstanceFleet#bid_price_as_percentage_of_on_demand_price}.
        :param configurations: configurations block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_instance_fleet#configurations EmrInstanceFleet#configurations}
        :param ebs_config: ebs_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_instance_fleet#ebs_config EmrInstanceFleet#ebs_config}
        :param weighted_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_instance_fleet#weighted_capacity EmrInstanceFleet#weighted_capacity}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f22bf6c233574f6010c7096de639a3ecd10ba342b1269f63fecc1b7454c3dbf)
            check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
            check_type(argname="argument bid_price", value=bid_price, expected_type=type_hints["bid_price"])
            check_type(argname="argument bid_price_as_percentage_of_on_demand_price", value=bid_price_as_percentage_of_on_demand_price, expected_type=type_hints["bid_price_as_percentage_of_on_demand_price"])
            check_type(argname="argument configurations", value=configurations, expected_type=type_hints["configurations"])
            check_type(argname="argument ebs_config", value=ebs_config, expected_type=type_hints["ebs_config"])
            check_type(argname="argument weighted_capacity", value=weighted_capacity, expected_type=type_hints["weighted_capacity"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "instance_type": instance_type,
        }
        if bid_price is not None:
            self._values["bid_price"] = bid_price
        if bid_price_as_percentage_of_on_demand_price is not None:
            self._values["bid_price_as_percentage_of_on_demand_price"] = bid_price_as_percentage_of_on_demand_price
        if configurations is not None:
            self._values["configurations"] = configurations
        if ebs_config is not None:
            self._values["ebs_config"] = ebs_config
        if weighted_capacity is not None:
            self._values["weighted_capacity"] = weighted_capacity

    @builtins.property
    def instance_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_instance_fleet#instance_type EmrInstanceFleet#instance_type}.'''
        result = self._values.get("instance_type")
        assert result is not None, "Required property 'instance_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bid_price(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_instance_fleet#bid_price EmrInstanceFleet#bid_price}.'''
        result = self._values.get("bid_price")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bid_price_as_percentage_of_on_demand_price(
        self,
    ) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_instance_fleet#bid_price_as_percentage_of_on_demand_price EmrInstanceFleet#bid_price_as_percentage_of_on_demand_price}.'''
        result = self._values.get("bid_price_as_percentage_of_on_demand_price")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def configurations(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EmrInstanceFleetInstanceTypeConfigsConfigurations"]]]:
        '''configurations block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_instance_fleet#configurations EmrInstanceFleet#configurations}
        '''
        result = self._values.get("configurations")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EmrInstanceFleetInstanceTypeConfigsConfigurations"]]], result)

    @builtins.property
    def ebs_config(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EmrInstanceFleetInstanceTypeConfigsEbsConfig"]]]:
        '''ebs_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_instance_fleet#ebs_config EmrInstanceFleet#ebs_config}
        '''
        result = self._values.get("ebs_config")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EmrInstanceFleetInstanceTypeConfigsEbsConfig"]]], result)

    @builtins.property
    def weighted_capacity(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_instance_fleet#weighted_capacity EmrInstanceFleet#weighted_capacity}.'''
        result = self._values.get("weighted_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmrInstanceFleetInstanceTypeConfigs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.emrInstanceFleet.EmrInstanceFleetInstanceTypeConfigsConfigurations",
    jsii_struct_bases=[],
    name_mapping={"classification": "classification", "properties": "properties"},
)
class EmrInstanceFleetInstanceTypeConfigsConfigurations:
    def __init__(
        self,
        *,
        classification: typing.Optional[builtins.str] = None,
        properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param classification: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_instance_fleet#classification EmrInstanceFleet#classification}.
        :param properties: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_instance_fleet#properties EmrInstanceFleet#properties}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c6221ac198241297891dd65f74f885d8a46c89167d0be81f0b8c5bf13f4e03f)
            check_type(argname="argument classification", value=classification, expected_type=type_hints["classification"])
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if classification is not None:
            self._values["classification"] = classification
        if properties is not None:
            self._values["properties"] = properties

    @builtins.property
    def classification(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_instance_fleet#classification EmrInstanceFleet#classification}.'''
        result = self._values.get("classification")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def properties(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_instance_fleet#properties EmrInstanceFleet#properties}.'''
        result = self._values.get("properties")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmrInstanceFleetInstanceTypeConfigsConfigurations(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EmrInstanceFleetInstanceTypeConfigsConfigurationsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.emrInstanceFleet.EmrInstanceFleetInstanceTypeConfigsConfigurationsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6c888c35954436ea0efb4b51ff5d99f10a458ad50d5a7f1c327f3cbade5b08e3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EmrInstanceFleetInstanceTypeConfigsConfigurationsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a8be9780709d873f31fe8f6e9c4308ec20b4c8da9d07ff01650dd9ec8195834)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EmrInstanceFleetInstanceTypeConfigsConfigurationsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f0b2d66aabdb2f2caef5d893a935d84ab6ba8e11a488b31d899c98a09ef0891d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d4b624cd6cfc125fc7fb1b84912f131417009f825ba3e28eafdd25035e7b0ab6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8b2dbcc4b957ec16300f766cfaa1a54f263a35bb81472b582cbb490a7ec48452)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrInstanceFleetInstanceTypeConfigsConfigurations]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrInstanceFleetInstanceTypeConfigsConfigurations]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrInstanceFleetInstanceTypeConfigsConfigurations]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0db2e05c32e9222f73a427d8fc0a7c3c4a819a8d3ef4ff4a661d3f412555c0d8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EmrInstanceFleetInstanceTypeConfigsConfigurationsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.emrInstanceFleet.EmrInstanceFleetInstanceTypeConfigsConfigurationsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__aa599114593dd463d8d45d95411dfa09e0e10a3c41325df654d528c9f2fbcda5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetClassification")
    def reset_classification(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClassification", []))

    @jsii.member(jsii_name="resetProperties")
    def reset_properties(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProperties", []))

    @builtins.property
    @jsii.member(jsii_name="classificationInput")
    def classification_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "classificationInput"))

    @builtins.property
    @jsii.member(jsii_name="propertiesInput")
    def properties_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "propertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="classification")
    def classification(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "classification"))

    @classification.setter
    def classification(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e86d860016614482d01195b3c5f8f77798d7ed276f89d9a2ec3af2c340a32888)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "classification", value)

    @builtins.property
    @jsii.member(jsii_name="properties")
    def properties(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "properties"))

    @properties.setter
    def properties(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b27bacf7eb6a9c7288978c197a675d26cb571fd256ca8f66995d0d861c6bf479)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "properties", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EmrInstanceFleetInstanceTypeConfigsConfigurations, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EmrInstanceFleetInstanceTypeConfigsConfigurations, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EmrInstanceFleetInstanceTypeConfigsConfigurations, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce18d6c4ca483effd32c9b957e213dda6df3757699ff4e9293da3ff6230cc04d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.emrInstanceFleet.EmrInstanceFleetInstanceTypeConfigsEbsConfig",
    jsii_struct_bases=[],
    name_mapping={
        "size": "size",
        "type": "type",
        "iops": "iops",
        "volumes_per_instance": "volumesPerInstance",
    },
)
class EmrInstanceFleetInstanceTypeConfigsEbsConfig:
    def __init__(
        self,
        *,
        size: jsii.Number,
        type: builtins.str,
        iops: typing.Optional[jsii.Number] = None,
        volumes_per_instance: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_instance_fleet#size EmrInstanceFleet#size}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_instance_fleet#type EmrInstanceFleet#type}.
        :param iops: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_instance_fleet#iops EmrInstanceFleet#iops}.
        :param volumes_per_instance: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_instance_fleet#volumes_per_instance EmrInstanceFleet#volumes_per_instance}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__488d6f67b4d15a9365b832e04ca0acb3b2cf54798081e2f3be2f54f1fbe31bb8)
            check_type(argname="argument size", value=size, expected_type=type_hints["size"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument iops", value=iops, expected_type=type_hints["iops"])
            check_type(argname="argument volumes_per_instance", value=volumes_per_instance, expected_type=type_hints["volumes_per_instance"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "size": size,
            "type": type,
        }
        if iops is not None:
            self._values["iops"] = iops
        if volumes_per_instance is not None:
            self._values["volumes_per_instance"] = volumes_per_instance

    @builtins.property
    def size(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_instance_fleet#size EmrInstanceFleet#size}.'''
        result = self._values.get("size")
        assert result is not None, "Required property 'size' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_instance_fleet#type EmrInstanceFleet#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def iops(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_instance_fleet#iops EmrInstanceFleet#iops}.'''
        result = self._values.get("iops")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def volumes_per_instance(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_instance_fleet#volumes_per_instance EmrInstanceFleet#volumes_per_instance}.'''
        result = self._values.get("volumes_per_instance")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmrInstanceFleetInstanceTypeConfigsEbsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EmrInstanceFleetInstanceTypeConfigsEbsConfigList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.emrInstanceFleet.EmrInstanceFleetInstanceTypeConfigsEbsConfigList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c6ee913aa12a7722059f7afadf6915ca6e73c281c1e9b0f763a245c43affb305)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EmrInstanceFleetInstanceTypeConfigsEbsConfigOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7087ef1a8cc9f3d2c6dd67b816dc6c0893092ea36730dec3ad1725519a20971f)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EmrInstanceFleetInstanceTypeConfigsEbsConfigOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca208c630ea0a09892d73e273392391b33417cebd3c63d9bb916922379dfcf3f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__98c932f863a0de9d3d2fd55811f0777b0378ea3d56f81ead2196d38825006b18)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b1c5de39a31bfdab958dd7c77cc7c7654a6114ed0a26223f3daee77d07186765)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrInstanceFleetInstanceTypeConfigsEbsConfig]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrInstanceFleetInstanceTypeConfigsEbsConfig]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrInstanceFleetInstanceTypeConfigsEbsConfig]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9beab370524ab66524d323fe7e8fa7da28cd61029b4e196a634deb7153c79663)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EmrInstanceFleetInstanceTypeConfigsEbsConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.emrInstanceFleet.EmrInstanceFleetInstanceTypeConfigsEbsConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__00a73520ad12b39803f39c6c6d11a6ad40fd3af75e26707c595fd3683af3baa3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetIops")
    def reset_iops(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIops", []))

    @jsii.member(jsii_name="resetVolumesPerInstance")
    def reset_volumes_per_instance(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVolumesPerInstance", []))

    @builtins.property
    @jsii.member(jsii_name="iopsInput")
    def iops_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "iopsInput"))

    @builtins.property
    @jsii.member(jsii_name="sizeInput")
    def size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sizeInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="volumesPerInstanceInput")
    def volumes_per_instance_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "volumesPerInstanceInput"))

    @builtins.property
    @jsii.member(jsii_name="iops")
    def iops(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "iops"))

    @iops.setter
    def iops(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c67970c4b83f4800d5c34d21f956dd194124b4c0e59e968185e1f8eee476251)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iops", value)

    @builtins.property
    @jsii.member(jsii_name="size")
    def size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "size"))

    @size.setter
    def size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e0bb4d661bdadab921d0d41c021aff18960e06f5b932f86ea66ec858034e2fc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "size", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b4193cc2d09fc748978b5ea5b581d451438af049da702e6eeeaaf4fd71f3373)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="volumesPerInstance")
    def volumes_per_instance(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "volumesPerInstance"))

    @volumes_per_instance.setter
    def volumes_per_instance(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__efaf2b97b7b5a455f30bfb3bdfbf01747c6d37262bd3cfcf37d7c2f40371c3d9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumesPerInstance", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EmrInstanceFleetInstanceTypeConfigsEbsConfig, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EmrInstanceFleetInstanceTypeConfigsEbsConfig, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EmrInstanceFleetInstanceTypeConfigsEbsConfig, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b019589cde479e5221dc1d40e9abd1c2227ab1cb05bd0cfb53d5cca943cf350)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EmrInstanceFleetInstanceTypeConfigsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.emrInstanceFleet.EmrInstanceFleetInstanceTypeConfigsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7e2644b5b9947f40d242ade1ac43572237d2ed93f7db02caa9ec7284718715f5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EmrInstanceFleetInstanceTypeConfigsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cbe93ca9011009789b44022a8b761dc56de11dc249d93e59837b77aa8dd91709)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EmrInstanceFleetInstanceTypeConfigsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5279f7949cb8e9f63aa995ff14d367125b86fa075d152a322ffa5e6046392808)
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
            type_hints = typing.get_type_hints(_typecheckingstub__885abff783588a44608cb492fff2110bc1f9ca588a50cd5ff60da2d2754c43b4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0190527ab6e0687330eaf013dd3f68d47e179be5cd9367ec5161c1bf0b6616ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrInstanceFleetInstanceTypeConfigs]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrInstanceFleetInstanceTypeConfigs]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrInstanceFleetInstanceTypeConfigs]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__65b820f2a5370a5c05755f78dcd6236d45b1e886372d43480a02bc57f9f2898b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EmrInstanceFleetInstanceTypeConfigsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.emrInstanceFleet.EmrInstanceFleetInstanceTypeConfigsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__efa07460fa2691e788f7408f03ee40b82f67b8dfcadeea749b381cfe3e1fdaf3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putConfigurations")
    def put_configurations(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EmrInstanceFleetInstanceTypeConfigsConfigurations, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8426dabe8949a7b61789c4d1be60abb6dfa820f91df9ff93f2c6b8fbe1aeaea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putConfigurations", [value]))

    @jsii.member(jsii_name="putEbsConfig")
    def put_ebs_config(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EmrInstanceFleetInstanceTypeConfigsEbsConfig, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7fb537091f20b4b2d3a662fc7e6048d28506a074292f7c3b033e9a83d4eafb2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putEbsConfig", [value]))

    @jsii.member(jsii_name="resetBidPrice")
    def reset_bid_price(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBidPrice", []))

    @jsii.member(jsii_name="resetBidPriceAsPercentageOfOnDemandPrice")
    def reset_bid_price_as_percentage_of_on_demand_price(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBidPriceAsPercentageOfOnDemandPrice", []))

    @jsii.member(jsii_name="resetConfigurations")
    def reset_configurations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfigurations", []))

    @jsii.member(jsii_name="resetEbsConfig")
    def reset_ebs_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEbsConfig", []))

    @jsii.member(jsii_name="resetWeightedCapacity")
    def reset_weighted_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWeightedCapacity", []))

    @builtins.property
    @jsii.member(jsii_name="configurations")
    def configurations(self) -> EmrInstanceFleetInstanceTypeConfigsConfigurationsList:
        return typing.cast(EmrInstanceFleetInstanceTypeConfigsConfigurationsList, jsii.get(self, "configurations"))

    @builtins.property
    @jsii.member(jsii_name="ebsConfig")
    def ebs_config(self) -> EmrInstanceFleetInstanceTypeConfigsEbsConfigList:
        return typing.cast(EmrInstanceFleetInstanceTypeConfigsEbsConfigList, jsii.get(self, "ebsConfig"))

    @builtins.property
    @jsii.member(jsii_name="bidPriceAsPercentageOfOnDemandPriceInput")
    def bid_price_as_percentage_of_on_demand_price_input(
        self,
    ) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "bidPriceAsPercentageOfOnDemandPriceInput"))

    @builtins.property
    @jsii.member(jsii_name="bidPriceInput")
    def bid_price_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bidPriceInput"))

    @builtins.property
    @jsii.member(jsii_name="configurationsInput")
    def configurations_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrInstanceFleetInstanceTypeConfigsConfigurations]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrInstanceFleetInstanceTypeConfigsConfigurations]]], jsii.get(self, "configurationsInput"))

    @builtins.property
    @jsii.member(jsii_name="ebsConfigInput")
    def ebs_config_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrInstanceFleetInstanceTypeConfigsEbsConfig]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrInstanceFleetInstanceTypeConfigsEbsConfig]]], jsii.get(self, "ebsConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceTypeInput")
    def instance_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="weightedCapacityInput")
    def weighted_capacity_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "weightedCapacityInput"))

    @builtins.property
    @jsii.member(jsii_name="bidPrice")
    def bid_price(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bidPrice"))

    @bid_price.setter
    def bid_price(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b3092962cb832dc4eefdcaf83e482e9ec8eaa9b2fabdc5bca16c7c1894667a6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bidPrice", value)

    @builtins.property
    @jsii.member(jsii_name="bidPriceAsPercentageOfOnDemandPrice")
    def bid_price_as_percentage_of_on_demand_price(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "bidPriceAsPercentageOfOnDemandPrice"))

    @bid_price_as_percentage_of_on_demand_price.setter
    def bid_price_as_percentage_of_on_demand_price(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3930cf73b6e5c295e744de4b4ada307335c18dd15d4f0c07ae5187e297337605)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bidPriceAsPercentageOfOnDemandPrice", value)

    @builtins.property
    @jsii.member(jsii_name="instanceType")
    def instance_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceType"))

    @instance_type.setter
    def instance_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b30cba33fdc84d59deff9a744234d211b7f345263924bfb922151647dc589ee9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceType", value)

    @builtins.property
    @jsii.member(jsii_name="weightedCapacity")
    def weighted_capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "weightedCapacity"))

    @weighted_capacity.setter
    def weighted_capacity(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc093b362deeaa16ff3d7c87c4504e1aff57db0de9c9feedad906c2b52f80cb5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "weightedCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EmrInstanceFleetInstanceTypeConfigs, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EmrInstanceFleetInstanceTypeConfigs, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EmrInstanceFleetInstanceTypeConfigs, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e34918f1fe71c863855cf096829f55dde28d5895315ebb92896a077537ccbcb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.emrInstanceFleet.EmrInstanceFleetLaunchSpecifications",
    jsii_struct_bases=[],
    name_mapping={
        "on_demand_specification": "onDemandSpecification",
        "spot_specification": "spotSpecification",
    },
)
class EmrInstanceFleetLaunchSpecifications:
    def __init__(
        self,
        *,
        on_demand_specification: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EmrInstanceFleetLaunchSpecificationsOnDemandSpecification", typing.Dict[builtins.str, typing.Any]]]]] = None,
        spot_specification: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EmrInstanceFleetLaunchSpecificationsSpotSpecification", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param on_demand_specification: on_demand_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_instance_fleet#on_demand_specification EmrInstanceFleet#on_demand_specification}
        :param spot_specification: spot_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_instance_fleet#spot_specification EmrInstanceFleet#spot_specification}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2e7e56fe327bc6e88dc4ddea43ea346441eca911e0ac6c182c2582328d1d242)
            check_type(argname="argument on_demand_specification", value=on_demand_specification, expected_type=type_hints["on_demand_specification"])
            check_type(argname="argument spot_specification", value=spot_specification, expected_type=type_hints["spot_specification"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if on_demand_specification is not None:
            self._values["on_demand_specification"] = on_demand_specification
        if spot_specification is not None:
            self._values["spot_specification"] = spot_specification

    @builtins.property
    def on_demand_specification(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EmrInstanceFleetLaunchSpecificationsOnDemandSpecification"]]]:
        '''on_demand_specification block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_instance_fleet#on_demand_specification EmrInstanceFleet#on_demand_specification}
        '''
        result = self._values.get("on_demand_specification")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EmrInstanceFleetLaunchSpecificationsOnDemandSpecification"]]], result)

    @builtins.property
    def spot_specification(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EmrInstanceFleetLaunchSpecificationsSpotSpecification"]]]:
        '''spot_specification block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_instance_fleet#spot_specification EmrInstanceFleet#spot_specification}
        '''
        result = self._values.get("spot_specification")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EmrInstanceFleetLaunchSpecificationsSpotSpecification"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmrInstanceFleetLaunchSpecifications(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.emrInstanceFleet.EmrInstanceFleetLaunchSpecificationsOnDemandSpecification",
    jsii_struct_bases=[],
    name_mapping={"allocation_strategy": "allocationStrategy"},
)
class EmrInstanceFleetLaunchSpecificationsOnDemandSpecification:
    def __init__(self, *, allocation_strategy: builtins.str) -> None:
        '''
        :param allocation_strategy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_instance_fleet#allocation_strategy EmrInstanceFleet#allocation_strategy}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa2d269e73e5bef30cb480399a452d2f8ac4f6d6a020226d1f1a130fa5e07aae)
            check_type(argname="argument allocation_strategy", value=allocation_strategy, expected_type=type_hints["allocation_strategy"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "allocation_strategy": allocation_strategy,
        }

    @builtins.property
    def allocation_strategy(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_instance_fleet#allocation_strategy EmrInstanceFleet#allocation_strategy}.'''
        result = self._values.get("allocation_strategy")
        assert result is not None, "Required property 'allocation_strategy' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmrInstanceFleetLaunchSpecificationsOnDemandSpecification(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EmrInstanceFleetLaunchSpecificationsOnDemandSpecificationList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.emrInstanceFleet.EmrInstanceFleetLaunchSpecificationsOnDemandSpecificationList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c11034f7fe2a2d9d86a51de3620a5c27aef7746dd70cd0c39d01b48d4aeb729b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EmrInstanceFleetLaunchSpecificationsOnDemandSpecificationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63bf9da47203442a93937cc5ceab94660afc4e789973215fa8bd734b47006409)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EmrInstanceFleetLaunchSpecificationsOnDemandSpecificationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be89ee5204b59c89497b746e4e64fca07fe988a98337b8b25e6df19c52a68396)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6a6748594e66fa0c2e804e72c9a47a27540ae3202614703fa3d8f2036f06227c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5c9c03e925462f709c99d9309e4b0e39752e75f75cf37a21ef5c504e73e16708)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrInstanceFleetLaunchSpecificationsOnDemandSpecification]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrInstanceFleetLaunchSpecificationsOnDemandSpecification]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrInstanceFleetLaunchSpecificationsOnDemandSpecification]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__add74f899ea3f790f0e109a2a66db0bc6095885c90ca4c9b820041a5321d713d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EmrInstanceFleetLaunchSpecificationsOnDemandSpecificationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.emrInstanceFleet.EmrInstanceFleetLaunchSpecificationsOnDemandSpecificationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__158f86c89d4c5024f1b26fab573e3fff056747c5c28a19e179734b8b902074c6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="allocationStrategyInput")
    def allocation_strategy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "allocationStrategyInput"))

    @builtins.property
    @jsii.member(jsii_name="allocationStrategy")
    def allocation_strategy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "allocationStrategy"))

    @allocation_strategy.setter
    def allocation_strategy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2215e7ee79ba452f04d591dd2c70d35792714b1141503fdb07f9336310087ea8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allocationStrategy", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EmrInstanceFleetLaunchSpecificationsOnDemandSpecification, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EmrInstanceFleetLaunchSpecificationsOnDemandSpecification, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EmrInstanceFleetLaunchSpecificationsOnDemandSpecification, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7d0f36d7e2077622139e11ccadb31c35908a9fa598dd102252a4387bff974b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EmrInstanceFleetLaunchSpecificationsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.emrInstanceFleet.EmrInstanceFleetLaunchSpecificationsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d5bbdf9272c6b26361231848941ff84b42059a99b90d799c48c4e4d313c8f7a7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putOnDemandSpecification")
    def put_on_demand_specification(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EmrInstanceFleetLaunchSpecificationsOnDemandSpecification, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__009bbecc02911a9d8db9785a11be0be6a9ce2a21b50ac300e44ade0ac672258c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putOnDemandSpecification", [value]))

    @jsii.member(jsii_name="putSpotSpecification")
    def put_spot_specification(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EmrInstanceFleetLaunchSpecificationsSpotSpecification", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a897f898c51a661b89833de861ac07b1d1b4ab55dfb4d1f9db4ce1c810059c3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSpotSpecification", [value]))

    @jsii.member(jsii_name="resetOnDemandSpecification")
    def reset_on_demand_specification(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOnDemandSpecification", []))

    @jsii.member(jsii_name="resetSpotSpecification")
    def reset_spot_specification(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSpotSpecification", []))

    @builtins.property
    @jsii.member(jsii_name="onDemandSpecification")
    def on_demand_specification(
        self,
    ) -> EmrInstanceFleetLaunchSpecificationsOnDemandSpecificationList:
        return typing.cast(EmrInstanceFleetLaunchSpecificationsOnDemandSpecificationList, jsii.get(self, "onDemandSpecification"))

    @builtins.property
    @jsii.member(jsii_name="spotSpecification")
    def spot_specification(
        self,
    ) -> "EmrInstanceFleetLaunchSpecificationsSpotSpecificationList":
        return typing.cast("EmrInstanceFleetLaunchSpecificationsSpotSpecificationList", jsii.get(self, "spotSpecification"))

    @builtins.property
    @jsii.member(jsii_name="onDemandSpecificationInput")
    def on_demand_specification_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrInstanceFleetLaunchSpecificationsOnDemandSpecification]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrInstanceFleetLaunchSpecificationsOnDemandSpecification]]], jsii.get(self, "onDemandSpecificationInput"))

    @builtins.property
    @jsii.member(jsii_name="spotSpecificationInput")
    def spot_specification_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EmrInstanceFleetLaunchSpecificationsSpotSpecification"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EmrInstanceFleetLaunchSpecificationsSpotSpecification"]]], jsii.get(self, "spotSpecificationInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[EmrInstanceFleetLaunchSpecifications]:
        return typing.cast(typing.Optional[EmrInstanceFleetLaunchSpecifications], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EmrInstanceFleetLaunchSpecifications],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d70eb80addf51f7cffe899631bd8bd3f03ca6367136292dac329636714999629)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.emrInstanceFleet.EmrInstanceFleetLaunchSpecificationsSpotSpecification",
    jsii_struct_bases=[],
    name_mapping={
        "allocation_strategy": "allocationStrategy",
        "timeout_action": "timeoutAction",
        "timeout_duration_minutes": "timeoutDurationMinutes",
        "block_duration_minutes": "blockDurationMinutes",
    },
)
class EmrInstanceFleetLaunchSpecificationsSpotSpecification:
    def __init__(
        self,
        *,
        allocation_strategy: builtins.str,
        timeout_action: builtins.str,
        timeout_duration_minutes: jsii.Number,
        block_duration_minutes: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param allocation_strategy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_instance_fleet#allocation_strategy EmrInstanceFleet#allocation_strategy}.
        :param timeout_action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_instance_fleet#timeout_action EmrInstanceFleet#timeout_action}.
        :param timeout_duration_minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_instance_fleet#timeout_duration_minutes EmrInstanceFleet#timeout_duration_minutes}.
        :param block_duration_minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_instance_fleet#block_duration_minutes EmrInstanceFleet#block_duration_minutes}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89bc06f389f00019aabdd4de734876ff9f9b8b3a7a6ea29890e94df9842241b2)
            check_type(argname="argument allocation_strategy", value=allocation_strategy, expected_type=type_hints["allocation_strategy"])
            check_type(argname="argument timeout_action", value=timeout_action, expected_type=type_hints["timeout_action"])
            check_type(argname="argument timeout_duration_minutes", value=timeout_duration_minutes, expected_type=type_hints["timeout_duration_minutes"])
            check_type(argname="argument block_duration_minutes", value=block_duration_minutes, expected_type=type_hints["block_duration_minutes"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "allocation_strategy": allocation_strategy,
            "timeout_action": timeout_action,
            "timeout_duration_minutes": timeout_duration_minutes,
        }
        if block_duration_minutes is not None:
            self._values["block_duration_minutes"] = block_duration_minutes

    @builtins.property
    def allocation_strategy(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_instance_fleet#allocation_strategy EmrInstanceFleet#allocation_strategy}.'''
        result = self._values.get("allocation_strategy")
        assert result is not None, "Required property 'allocation_strategy' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def timeout_action(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_instance_fleet#timeout_action EmrInstanceFleet#timeout_action}.'''
        result = self._values.get("timeout_action")
        assert result is not None, "Required property 'timeout_action' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def timeout_duration_minutes(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_instance_fleet#timeout_duration_minutes EmrInstanceFleet#timeout_duration_minutes}.'''
        result = self._values.get("timeout_duration_minutes")
        assert result is not None, "Required property 'timeout_duration_minutes' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def block_duration_minutes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_instance_fleet#block_duration_minutes EmrInstanceFleet#block_duration_minutes}.'''
        result = self._values.get("block_duration_minutes")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmrInstanceFleetLaunchSpecificationsSpotSpecification(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EmrInstanceFleetLaunchSpecificationsSpotSpecificationList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.emrInstanceFleet.EmrInstanceFleetLaunchSpecificationsSpotSpecificationList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__578187ab2da5332e04352cc0805d2f00273c0917f2b599465c94a907751a1190)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EmrInstanceFleetLaunchSpecificationsSpotSpecificationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__174219bb0fa41b2941c3cf410ac2d1cde0d7c30c1717360bcd7b5652294605b9)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EmrInstanceFleetLaunchSpecificationsSpotSpecificationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f29ccd94f10da496512485799a86242669874bdf0a7c3b0da96e40f42ab5e5b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9519cd93ed415b0b8bd69be7ff1b18e2ebce0c3ba51478c2e5d5ff247e3ca0b1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__844c99193736a801016d91bd12968770f4becc14e18b19f37b71953ba88e8098)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrInstanceFleetLaunchSpecificationsSpotSpecification]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrInstanceFleetLaunchSpecificationsSpotSpecification]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrInstanceFleetLaunchSpecificationsSpotSpecification]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__212834c3d7edad9a9b70f63e9f4d855f8dfb419f29d6ee29ff83d72154a54124)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EmrInstanceFleetLaunchSpecificationsSpotSpecificationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.emrInstanceFleet.EmrInstanceFleetLaunchSpecificationsSpotSpecificationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__154f18c999dc6ca36c5f9831db390fd8c66c0ce8c0314f1f67f42d1901938afc)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetBlockDurationMinutes")
    def reset_block_duration_minutes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBlockDurationMinutes", []))

    @builtins.property
    @jsii.member(jsii_name="allocationStrategyInput")
    def allocation_strategy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "allocationStrategyInput"))

    @builtins.property
    @jsii.member(jsii_name="blockDurationMinutesInput")
    def block_duration_minutes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "blockDurationMinutesInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutActionInput")
    def timeout_action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timeoutActionInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutDurationMinutesInput")
    def timeout_duration_minutes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "timeoutDurationMinutesInput"))

    @builtins.property
    @jsii.member(jsii_name="allocationStrategy")
    def allocation_strategy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "allocationStrategy"))

    @allocation_strategy.setter
    def allocation_strategy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6ecc282b21785334ce03bc40aab8e3d7d76bb3d3096c7bd209d07fe552d8e8f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allocationStrategy", value)

    @builtins.property
    @jsii.member(jsii_name="blockDurationMinutes")
    def block_duration_minutes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "blockDurationMinutes"))

    @block_duration_minutes.setter
    def block_duration_minutes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5d5572fc83ad0d3d45e006d8cf89866d03a6886360001655b2644727c8736a4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "blockDurationMinutes", value)

    @builtins.property
    @jsii.member(jsii_name="timeoutAction")
    def timeout_action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timeoutAction"))

    @timeout_action.setter
    def timeout_action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50dfb77542bfe2252be7043eaea793b76ed5894b90c4136dd890e76d16fb77e9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeoutAction", value)

    @builtins.property
    @jsii.member(jsii_name="timeoutDurationMinutes")
    def timeout_duration_minutes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "timeoutDurationMinutes"))

    @timeout_duration_minutes.setter
    def timeout_duration_minutes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__90d5bada468391e57dde8ff397d702dcd7615356207cf57fc61fa7933a9bd29c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeoutDurationMinutes", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EmrInstanceFleetLaunchSpecificationsSpotSpecification, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EmrInstanceFleetLaunchSpecificationsSpotSpecification, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EmrInstanceFleetLaunchSpecificationsSpotSpecification, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__996e26e0d6c70ec762e4bebe757825e17c2a6cb6a509f798fbafc5355905d600)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "EmrInstanceFleet",
    "EmrInstanceFleetConfig",
    "EmrInstanceFleetInstanceTypeConfigs",
    "EmrInstanceFleetInstanceTypeConfigsConfigurations",
    "EmrInstanceFleetInstanceTypeConfigsConfigurationsList",
    "EmrInstanceFleetInstanceTypeConfigsConfigurationsOutputReference",
    "EmrInstanceFleetInstanceTypeConfigsEbsConfig",
    "EmrInstanceFleetInstanceTypeConfigsEbsConfigList",
    "EmrInstanceFleetInstanceTypeConfigsEbsConfigOutputReference",
    "EmrInstanceFleetInstanceTypeConfigsList",
    "EmrInstanceFleetInstanceTypeConfigsOutputReference",
    "EmrInstanceFleetLaunchSpecifications",
    "EmrInstanceFleetLaunchSpecificationsOnDemandSpecification",
    "EmrInstanceFleetLaunchSpecificationsOnDemandSpecificationList",
    "EmrInstanceFleetLaunchSpecificationsOnDemandSpecificationOutputReference",
    "EmrInstanceFleetLaunchSpecificationsOutputReference",
    "EmrInstanceFleetLaunchSpecificationsSpotSpecification",
    "EmrInstanceFleetLaunchSpecificationsSpotSpecificationList",
    "EmrInstanceFleetLaunchSpecificationsSpotSpecificationOutputReference",
]

publication.publish()

def _typecheckingstub__97d9f24fc9726abc0a884cb8006305658dd53fda6fc8b2a796ba2cea8cc2ccd7(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    cluster_id: builtins.str,
    id: typing.Optional[builtins.str] = None,
    instance_type_configs: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EmrInstanceFleetInstanceTypeConfigs, typing.Dict[builtins.str, typing.Any]]]]] = None,
    launch_specifications: typing.Optional[typing.Union[EmrInstanceFleetLaunchSpecifications, typing.Dict[builtins.str, typing.Any]]] = None,
    name: typing.Optional[builtins.str] = None,
    target_on_demand_capacity: typing.Optional[jsii.Number] = None,
    target_spot_capacity: typing.Optional[jsii.Number] = None,
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

def _typecheckingstub__e88c5cf7e5502990e8fa8b97f133b50167e544c358d64bd0e002218aa64f27db(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EmrInstanceFleetInstanceTypeConfigs, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e93f004a65c896a912667e94c48e76918f1159796f3e6eb1ba57625eb0cd3d7f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60185f0b7c296a6f1c6ae6874483968701eeb5b642d682c08b20c057e072e0d2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe027095b92ee7235c2233433eaf4f43f302a5be78e6e6a5767a7a117fc3fcd4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3221d2006d429a628ec218b11fbb6bb8b65c073dcb45f90a793e5865100ce8fd(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0bc688a59f3c83c894c98afe73b021060e1aea1ef6ab61d7419ae2052e42db7d(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__447642bb86d6caed80f2d1495caac82c24216169f0ffcd8f7186e33d192a567f(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    cluster_id: builtins.str,
    id: typing.Optional[builtins.str] = None,
    instance_type_configs: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EmrInstanceFleetInstanceTypeConfigs, typing.Dict[builtins.str, typing.Any]]]]] = None,
    launch_specifications: typing.Optional[typing.Union[EmrInstanceFleetLaunchSpecifications, typing.Dict[builtins.str, typing.Any]]] = None,
    name: typing.Optional[builtins.str] = None,
    target_on_demand_capacity: typing.Optional[jsii.Number] = None,
    target_spot_capacity: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f22bf6c233574f6010c7096de639a3ecd10ba342b1269f63fecc1b7454c3dbf(
    *,
    instance_type: builtins.str,
    bid_price: typing.Optional[builtins.str] = None,
    bid_price_as_percentage_of_on_demand_price: typing.Optional[jsii.Number] = None,
    configurations: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EmrInstanceFleetInstanceTypeConfigsConfigurations, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ebs_config: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EmrInstanceFleetInstanceTypeConfigsEbsConfig, typing.Dict[builtins.str, typing.Any]]]]] = None,
    weighted_capacity: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c6221ac198241297891dd65f74f885d8a46c89167d0be81f0b8c5bf13f4e03f(
    *,
    classification: typing.Optional[builtins.str] = None,
    properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c888c35954436ea0efb4b51ff5d99f10a458ad50d5a7f1c327f3cbade5b08e3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a8be9780709d873f31fe8f6e9c4308ec20b4c8da9d07ff01650dd9ec8195834(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0b2d66aabdb2f2caef5d893a935d84ab6ba8e11a488b31d899c98a09ef0891d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4b624cd6cfc125fc7fb1b84912f131417009f825ba3e28eafdd25035e7b0ab6(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b2dbcc4b957ec16300f766cfaa1a54f263a35bb81472b582cbb490a7ec48452(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0db2e05c32e9222f73a427d8fc0a7c3c4a819a8d3ef4ff4a661d3f412555c0d8(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrInstanceFleetInstanceTypeConfigsConfigurations]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa599114593dd463d8d45d95411dfa09e0e10a3c41325df654d528c9f2fbcda5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e86d860016614482d01195b3c5f8f77798d7ed276f89d9a2ec3af2c340a32888(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b27bacf7eb6a9c7288978c197a675d26cb571fd256ca8f66995d0d861c6bf479(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce18d6c4ca483effd32c9b957e213dda6df3757699ff4e9293da3ff6230cc04d(
    value: typing.Optional[typing.Union[EmrInstanceFleetInstanceTypeConfigsConfigurations, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__488d6f67b4d15a9365b832e04ca0acb3b2cf54798081e2f3be2f54f1fbe31bb8(
    *,
    size: jsii.Number,
    type: builtins.str,
    iops: typing.Optional[jsii.Number] = None,
    volumes_per_instance: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6ee913aa12a7722059f7afadf6915ca6e73c281c1e9b0f763a245c43affb305(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7087ef1a8cc9f3d2c6dd67b816dc6c0893092ea36730dec3ad1725519a20971f(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca208c630ea0a09892d73e273392391b33417cebd3c63d9bb916922379dfcf3f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98c932f863a0de9d3d2fd55811f0777b0378ea3d56f81ead2196d38825006b18(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1c5de39a31bfdab958dd7c77cc7c7654a6114ed0a26223f3daee77d07186765(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9beab370524ab66524d323fe7e8fa7da28cd61029b4e196a634deb7153c79663(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrInstanceFleetInstanceTypeConfigsEbsConfig]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00a73520ad12b39803f39c6c6d11a6ad40fd3af75e26707c595fd3683af3baa3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c67970c4b83f4800d5c34d21f956dd194124b4c0e59e968185e1f8eee476251(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e0bb4d661bdadab921d0d41c021aff18960e06f5b932f86ea66ec858034e2fc(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b4193cc2d09fc748978b5ea5b581d451438af049da702e6eeeaaf4fd71f3373(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__efaf2b97b7b5a455f30bfb3bdfbf01747c6d37262bd3cfcf37d7c2f40371c3d9(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b019589cde479e5221dc1d40e9abd1c2227ab1cb05bd0cfb53d5cca943cf350(
    value: typing.Optional[typing.Union[EmrInstanceFleetInstanceTypeConfigsEbsConfig, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e2644b5b9947f40d242ade1ac43572237d2ed93f7db02caa9ec7284718715f5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cbe93ca9011009789b44022a8b761dc56de11dc249d93e59837b77aa8dd91709(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5279f7949cb8e9f63aa995ff14d367125b86fa075d152a322ffa5e6046392808(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__885abff783588a44608cb492fff2110bc1f9ca588a50cd5ff60da2d2754c43b4(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0190527ab6e0687330eaf013dd3f68d47e179be5cd9367ec5161c1bf0b6616ab(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65b820f2a5370a5c05755f78dcd6236d45b1e886372d43480a02bc57f9f2898b(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrInstanceFleetInstanceTypeConfigs]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__efa07460fa2691e788f7408f03ee40b82f67b8dfcadeea749b381cfe3e1fdaf3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8426dabe8949a7b61789c4d1be60abb6dfa820f91df9ff93f2c6b8fbe1aeaea(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EmrInstanceFleetInstanceTypeConfigsConfigurations, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7fb537091f20b4b2d3a662fc7e6048d28506a074292f7c3b033e9a83d4eafb2(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EmrInstanceFleetInstanceTypeConfigsEbsConfig, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b3092962cb832dc4eefdcaf83e482e9ec8eaa9b2fabdc5bca16c7c1894667a6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3930cf73b6e5c295e744de4b4ada307335c18dd15d4f0c07ae5187e297337605(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b30cba33fdc84d59deff9a744234d211b7f345263924bfb922151647dc589ee9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc093b362deeaa16ff3d7c87c4504e1aff57db0de9c9feedad906c2b52f80cb5(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e34918f1fe71c863855cf096829f55dde28d5895315ebb92896a077537ccbcb(
    value: typing.Optional[typing.Union[EmrInstanceFleetInstanceTypeConfigs, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2e7e56fe327bc6e88dc4ddea43ea346441eca911e0ac6c182c2582328d1d242(
    *,
    on_demand_specification: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EmrInstanceFleetLaunchSpecificationsOnDemandSpecification, typing.Dict[builtins.str, typing.Any]]]]] = None,
    spot_specification: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EmrInstanceFleetLaunchSpecificationsSpotSpecification, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa2d269e73e5bef30cb480399a452d2f8ac4f6d6a020226d1f1a130fa5e07aae(
    *,
    allocation_strategy: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c11034f7fe2a2d9d86a51de3620a5c27aef7746dd70cd0c39d01b48d4aeb729b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63bf9da47203442a93937cc5ceab94660afc4e789973215fa8bd734b47006409(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be89ee5204b59c89497b746e4e64fca07fe988a98337b8b25e6df19c52a68396(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a6748594e66fa0c2e804e72c9a47a27540ae3202614703fa3d8f2036f06227c(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c9c03e925462f709c99d9309e4b0e39752e75f75cf37a21ef5c504e73e16708(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__add74f899ea3f790f0e109a2a66db0bc6095885c90ca4c9b820041a5321d713d(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrInstanceFleetLaunchSpecificationsOnDemandSpecification]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__158f86c89d4c5024f1b26fab573e3fff056747c5c28a19e179734b8b902074c6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2215e7ee79ba452f04d591dd2c70d35792714b1141503fdb07f9336310087ea8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7d0f36d7e2077622139e11ccadb31c35908a9fa598dd102252a4387bff974b6(
    value: typing.Optional[typing.Union[EmrInstanceFleetLaunchSpecificationsOnDemandSpecification, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5bbdf9272c6b26361231848941ff84b42059a99b90d799c48c4e4d313c8f7a7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__009bbecc02911a9d8db9785a11be0be6a9ce2a21b50ac300e44ade0ac672258c(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EmrInstanceFleetLaunchSpecificationsOnDemandSpecification, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a897f898c51a661b89833de861ac07b1d1b4ab55dfb4d1f9db4ce1c810059c3(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EmrInstanceFleetLaunchSpecificationsSpotSpecification, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d70eb80addf51f7cffe899631bd8bd3f03ca6367136292dac329636714999629(
    value: typing.Optional[EmrInstanceFleetLaunchSpecifications],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89bc06f389f00019aabdd4de734876ff9f9b8b3a7a6ea29890e94df9842241b2(
    *,
    allocation_strategy: builtins.str,
    timeout_action: builtins.str,
    timeout_duration_minutes: jsii.Number,
    block_duration_minutes: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__578187ab2da5332e04352cc0805d2f00273c0917f2b599465c94a907751a1190(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__174219bb0fa41b2941c3cf410ac2d1cde0d7c30c1717360bcd7b5652294605b9(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f29ccd94f10da496512485799a86242669874bdf0a7c3b0da96e40f42ab5e5b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9519cd93ed415b0b8bd69be7ff1b18e2ebce0c3ba51478c2e5d5ff247e3ca0b1(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__844c99193736a801016d91bd12968770f4becc14e18b19f37b71953ba88e8098(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__212834c3d7edad9a9b70f63e9f4d855f8dfb419f29d6ee29ff83d72154a54124(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrInstanceFleetLaunchSpecificationsSpotSpecification]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__154f18c999dc6ca36c5f9831db390fd8c66c0ce8c0314f1f67f42d1901938afc(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6ecc282b21785334ce03bc40aab8e3d7d76bb3d3096c7bd209d07fe552d8e8f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5d5572fc83ad0d3d45e006d8cf89866d03a6886360001655b2644727c8736a4(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50dfb77542bfe2252be7043eaea793b76ed5894b90c4136dd890e76d16fb77e9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90d5bada468391e57dde8ff397d702dcd7615356207cf57fc61fa7933a9bd29c(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__996e26e0d6c70ec762e4bebe757825e17c2a6cb6a509f798fbafc5355905d600(
    value: typing.Optional[typing.Union[EmrInstanceFleetLaunchSpecificationsSpotSpecification, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
