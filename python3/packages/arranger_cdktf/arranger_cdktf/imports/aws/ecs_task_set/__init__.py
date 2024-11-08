'''
# `aws_ecs_task_set`

Refer to the Terraform Registory for docs: [`aws_ecs_task_set`](https://www.terraform.io/docs/providers/aws/r/ecs_task_set).
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


class EcsTaskSet(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ecsTaskSet.EcsTaskSet",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set aws_ecs_task_set}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        cluster: builtins.str,
        service: builtins.str,
        task_definition: builtins.str,
        capacity_provider_strategy: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EcsTaskSetCapacityProviderStrategy", typing.Dict[builtins.str, typing.Any]]]]] = None,
        external_id: typing.Optional[builtins.str] = None,
        force_delete: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        launch_type: typing.Optional[builtins.str] = None,
        load_balancer: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EcsTaskSetLoadBalancer", typing.Dict[builtins.str, typing.Any]]]]] = None,
        network_configuration: typing.Optional[typing.Union["EcsTaskSetNetworkConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        platform_version: typing.Optional[builtins.str] = None,
        scale: typing.Optional[typing.Union["EcsTaskSetScale", typing.Dict[builtins.str, typing.Any]]] = None,
        service_registries: typing.Optional[typing.Union["EcsTaskSetServiceRegistries", typing.Dict[builtins.str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        wait_until_stable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        wait_until_stable_timeout: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set aws_ecs_task_set} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param cluster: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#cluster EcsTaskSet#cluster}.
        :param service: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#service EcsTaskSet#service}.
        :param task_definition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#task_definition EcsTaskSet#task_definition}.
        :param capacity_provider_strategy: capacity_provider_strategy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#capacity_provider_strategy EcsTaskSet#capacity_provider_strategy}
        :param external_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#external_id EcsTaskSet#external_id}.
        :param force_delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#force_delete EcsTaskSet#force_delete}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#id EcsTaskSet#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param launch_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#launch_type EcsTaskSet#launch_type}.
        :param load_balancer: load_balancer block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#load_balancer EcsTaskSet#load_balancer}
        :param network_configuration: network_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#network_configuration EcsTaskSet#network_configuration}
        :param platform_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#platform_version EcsTaskSet#platform_version}.
        :param scale: scale block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#scale EcsTaskSet#scale}
        :param service_registries: service_registries block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#service_registries EcsTaskSet#service_registries}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#tags EcsTaskSet#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#tags_all EcsTaskSet#tags_all}.
        :param wait_until_stable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#wait_until_stable EcsTaskSet#wait_until_stable}.
        :param wait_until_stable_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#wait_until_stable_timeout EcsTaskSet#wait_until_stable_timeout}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__142d22979688ef4a5e16e476a6e02ed53b617b97803dd000ccdd877ed80e63ff)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = EcsTaskSetConfig(
            cluster=cluster,
            service=service,
            task_definition=task_definition,
            capacity_provider_strategy=capacity_provider_strategy,
            external_id=external_id,
            force_delete=force_delete,
            id=id,
            launch_type=launch_type,
            load_balancer=load_balancer,
            network_configuration=network_configuration,
            platform_version=platform_version,
            scale=scale,
            service_registries=service_registries,
            tags=tags,
            tags_all=tags_all,
            wait_until_stable=wait_until_stable,
            wait_until_stable_timeout=wait_until_stable_timeout,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putCapacityProviderStrategy")
    def put_capacity_provider_strategy(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EcsTaskSetCapacityProviderStrategy", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b88ac474c2f9fe552ab824df35d678de322e5212428e7903c75329840619131)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCapacityProviderStrategy", [value]))

    @jsii.member(jsii_name="putLoadBalancer")
    def put_load_balancer(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EcsTaskSetLoadBalancer", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6677cb11cc54d17e9718bc4b9638e90159d2f48f2f5d3d10d98e1d2d677e6d43)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLoadBalancer", [value]))

    @jsii.member(jsii_name="putNetworkConfiguration")
    def put_network_configuration(
        self,
        *,
        subnets: typing.Sequence[builtins.str],
        assign_public_ip: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param subnets: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#subnets EcsTaskSet#subnets}.
        :param assign_public_ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#assign_public_ip EcsTaskSet#assign_public_ip}.
        :param security_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#security_groups EcsTaskSet#security_groups}.
        '''
        value = EcsTaskSetNetworkConfiguration(
            subnets=subnets,
            assign_public_ip=assign_public_ip,
            security_groups=security_groups,
        )

        return typing.cast(None, jsii.invoke(self, "putNetworkConfiguration", [value]))

    @jsii.member(jsii_name="putScale")
    def put_scale(
        self,
        *,
        unit: typing.Optional[builtins.str] = None,
        value: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#unit EcsTaskSet#unit}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#value EcsTaskSet#value}.
        '''
        value_ = EcsTaskSetScale(unit=unit, value=value)

        return typing.cast(None, jsii.invoke(self, "putScale", [value_]))

    @jsii.member(jsii_name="putServiceRegistries")
    def put_service_registries(
        self,
        *,
        registry_arn: builtins.str,
        container_name: typing.Optional[builtins.str] = None,
        container_port: typing.Optional[jsii.Number] = None,
        port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param registry_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#registry_arn EcsTaskSet#registry_arn}.
        :param container_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#container_name EcsTaskSet#container_name}.
        :param container_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#container_port EcsTaskSet#container_port}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#port EcsTaskSet#port}.
        '''
        value = EcsTaskSetServiceRegistries(
            registry_arn=registry_arn,
            container_name=container_name,
            container_port=container_port,
            port=port,
        )

        return typing.cast(None, jsii.invoke(self, "putServiceRegistries", [value]))

    @jsii.member(jsii_name="resetCapacityProviderStrategy")
    def reset_capacity_provider_strategy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCapacityProviderStrategy", []))

    @jsii.member(jsii_name="resetExternalId")
    def reset_external_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExternalId", []))

    @jsii.member(jsii_name="resetForceDelete")
    def reset_force_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForceDelete", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLaunchType")
    def reset_launch_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLaunchType", []))

    @jsii.member(jsii_name="resetLoadBalancer")
    def reset_load_balancer(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoadBalancer", []))

    @jsii.member(jsii_name="resetNetworkConfiguration")
    def reset_network_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworkConfiguration", []))

    @jsii.member(jsii_name="resetPlatformVersion")
    def reset_platform_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPlatformVersion", []))

    @jsii.member(jsii_name="resetScale")
    def reset_scale(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScale", []))

    @jsii.member(jsii_name="resetServiceRegistries")
    def reset_service_registries(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceRegistries", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetWaitUntilStable")
    def reset_wait_until_stable(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWaitUntilStable", []))

    @jsii.member(jsii_name="resetWaitUntilStableTimeout")
    def reset_wait_until_stable_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWaitUntilStableTimeout", []))

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
    @jsii.member(jsii_name="capacityProviderStrategy")
    def capacity_provider_strategy(self) -> "EcsTaskSetCapacityProviderStrategyList":
        return typing.cast("EcsTaskSetCapacityProviderStrategyList", jsii.get(self, "capacityProviderStrategy"))

    @builtins.property
    @jsii.member(jsii_name="loadBalancer")
    def load_balancer(self) -> "EcsTaskSetLoadBalancerList":
        return typing.cast("EcsTaskSetLoadBalancerList", jsii.get(self, "loadBalancer"))

    @builtins.property
    @jsii.member(jsii_name="networkConfiguration")
    def network_configuration(self) -> "EcsTaskSetNetworkConfigurationOutputReference":
        return typing.cast("EcsTaskSetNetworkConfigurationOutputReference", jsii.get(self, "networkConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="scale")
    def scale(self) -> "EcsTaskSetScaleOutputReference":
        return typing.cast("EcsTaskSetScaleOutputReference", jsii.get(self, "scale"))

    @builtins.property
    @jsii.member(jsii_name="serviceRegistries")
    def service_registries(self) -> "EcsTaskSetServiceRegistriesOutputReference":
        return typing.cast("EcsTaskSetServiceRegistriesOutputReference", jsii.get(self, "serviceRegistries"))

    @builtins.property
    @jsii.member(jsii_name="stabilityStatus")
    def stability_status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "stabilityStatus"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="taskSetId")
    def task_set_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "taskSetId"))

    @builtins.property
    @jsii.member(jsii_name="capacityProviderStrategyInput")
    def capacity_provider_strategy_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EcsTaskSetCapacityProviderStrategy"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EcsTaskSetCapacityProviderStrategy"]]], jsii.get(self, "capacityProviderStrategyInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterInput")
    def cluster_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterInput"))

    @builtins.property
    @jsii.member(jsii_name="externalIdInput")
    def external_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "externalIdInput"))

    @builtins.property
    @jsii.member(jsii_name="forceDeleteInput")
    def force_delete_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "forceDeleteInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="launchTypeInput")
    def launch_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "launchTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="loadBalancerInput")
    def load_balancer_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EcsTaskSetLoadBalancer"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EcsTaskSetLoadBalancer"]]], jsii.get(self, "loadBalancerInput"))

    @builtins.property
    @jsii.member(jsii_name="networkConfigurationInput")
    def network_configuration_input(
        self,
    ) -> typing.Optional["EcsTaskSetNetworkConfiguration"]:
        return typing.cast(typing.Optional["EcsTaskSetNetworkConfiguration"], jsii.get(self, "networkConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="platformVersionInput")
    def platform_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "platformVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="scaleInput")
    def scale_input(self) -> typing.Optional["EcsTaskSetScale"]:
        return typing.cast(typing.Optional["EcsTaskSetScale"], jsii.get(self, "scaleInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceInput")
    def service_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceRegistriesInput")
    def service_registries_input(
        self,
    ) -> typing.Optional["EcsTaskSetServiceRegistries"]:
        return typing.cast(typing.Optional["EcsTaskSetServiceRegistries"], jsii.get(self, "serviceRegistriesInput"))

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
    @jsii.member(jsii_name="taskDefinitionInput")
    def task_definition_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "taskDefinitionInput"))

    @builtins.property
    @jsii.member(jsii_name="waitUntilStableInput")
    def wait_until_stable_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "waitUntilStableInput"))

    @builtins.property
    @jsii.member(jsii_name="waitUntilStableTimeoutInput")
    def wait_until_stable_timeout_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "waitUntilStableTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="cluster")
    def cluster(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cluster"))

    @cluster.setter
    def cluster(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27ef6798289c9b29c22ecaca79d42b41ae4cba112f731bb0ac449889a4657963)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cluster", value)

    @builtins.property
    @jsii.member(jsii_name="externalId")
    def external_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "externalId"))

    @external_id.setter
    def external_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f371d83789efd5c482cf74a16479ae28bb5ec805a49b1c78ad224f334bd3d94)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "externalId", value)

    @builtins.property
    @jsii.member(jsii_name="forceDelete")
    def force_delete(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "forceDelete"))

    @force_delete.setter
    def force_delete(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14c5dc8c426e6023106f0d30f63746cd5332dc889782be95208309729638a76e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forceDelete", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cbdba5a54eb06706a07d77eaaa23c4159bdf74a6fc78cd951e4af9562004993b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="launchType")
    def launch_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "launchType"))

    @launch_type.setter
    def launch_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f81e3098778993155bc109e0866e848d9beba8f3cab132bdfb90145b40c33e5a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "launchType", value)

    @builtins.property
    @jsii.member(jsii_name="platformVersion")
    def platform_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "platformVersion"))

    @platform_version.setter
    def platform_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__569a392df4378bb264e958b5617b5074e5b8bd2062b0cfd930a71770c957550b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "platformVersion", value)

    @builtins.property
    @jsii.member(jsii_name="service")
    def service(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "service"))

    @service.setter
    def service(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56f19c15ba3d28a25de050a26dc0a842402701683d1c4d0dc060b42574904768)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "service", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c20b48d87c3928a61abbf33e512714de85311b3e70b84d7878686c5095d90df8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84174defc102d58611736cff764e968af97eac57b13f75ee6aed07edf4250318)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)

    @builtins.property
    @jsii.member(jsii_name="taskDefinition")
    def task_definition(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "taskDefinition"))

    @task_definition.setter
    def task_definition(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56d42fe270dae5fc0c99f6a0263a5c55dcbb98d6604b19f4207c7ffe76ed170d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "taskDefinition", value)

    @builtins.property
    @jsii.member(jsii_name="waitUntilStable")
    def wait_until_stable(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "waitUntilStable"))

    @wait_until_stable.setter
    def wait_until_stable(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f4ee7261c8871457ecf974514d7081039321300e9fd6a358f13c36de1aa46e9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "waitUntilStable", value)

    @builtins.property
    @jsii.member(jsii_name="waitUntilStableTimeout")
    def wait_until_stable_timeout(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "waitUntilStableTimeout"))

    @wait_until_stable_timeout.setter
    def wait_until_stable_timeout(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a4d79e9d5e3b16cf86cbe5e774c7a43abdebfafa6380051f0cf704cf5b87d72)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "waitUntilStableTimeout", value)


@jsii.data_type(
    jsii_type="aws.ecsTaskSet.EcsTaskSetCapacityProviderStrategy",
    jsii_struct_bases=[],
    name_mapping={
        "capacity_provider": "capacityProvider",
        "weight": "weight",
        "base": "base",
    },
)
class EcsTaskSetCapacityProviderStrategy:
    def __init__(
        self,
        *,
        capacity_provider: builtins.str,
        weight: jsii.Number,
        base: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param capacity_provider: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#capacity_provider EcsTaskSet#capacity_provider}.
        :param weight: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#weight EcsTaskSet#weight}.
        :param base: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#base EcsTaskSet#base}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e762bd3d25388eaf5ed6bda6233f3ea316e8945159c91890c2ce0fde85b56256)
            check_type(argname="argument capacity_provider", value=capacity_provider, expected_type=type_hints["capacity_provider"])
            check_type(argname="argument weight", value=weight, expected_type=type_hints["weight"])
            check_type(argname="argument base", value=base, expected_type=type_hints["base"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "capacity_provider": capacity_provider,
            "weight": weight,
        }
        if base is not None:
            self._values["base"] = base

    @builtins.property
    def capacity_provider(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#capacity_provider EcsTaskSet#capacity_provider}.'''
        result = self._values.get("capacity_provider")
        assert result is not None, "Required property 'capacity_provider' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def weight(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#weight EcsTaskSet#weight}.'''
        result = self._values.get("weight")
        assert result is not None, "Required property 'weight' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def base(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#base EcsTaskSet#base}.'''
        result = self._values.get("base")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsTaskSetCapacityProviderStrategy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcsTaskSetCapacityProviderStrategyList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ecsTaskSet.EcsTaskSetCapacityProviderStrategyList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9316b3bb44594a9222bb4dcc67d76e6d415a660da8ae1a9bd252f775a6a0e2a4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EcsTaskSetCapacityProviderStrategyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db9ffee31dee6c5f34f31a5f12462398af284c1383e8ec4d2cdf66cac5513b1b)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EcsTaskSetCapacityProviderStrategyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60578c12ba7190967a2f0c260a50cba7a71c15cea4443ea5f8e63a63c29979d5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f8c9bcfa944127a3da8e8e9a955ba6e923cc4137a15427c37068c33ceafa7c7b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5c4f6b26bdd89f6d6c91ee64c6f07d02fadffc8c4c8ce425d963ef7a04f40438)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EcsTaskSetCapacityProviderStrategy]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EcsTaskSetCapacityProviderStrategy]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EcsTaskSetCapacityProviderStrategy]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee440e91f61930d007850559694ccf253f46be9a24902f170a3bd0825693fb92)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EcsTaskSetCapacityProviderStrategyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ecsTaskSet.EcsTaskSetCapacityProviderStrategyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b9365ab9fbe76fd0bd3893dc487bbfc694272242056bf9f66ae9db4a4053c3d2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetBase")
    def reset_base(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBase", []))

    @builtins.property
    @jsii.member(jsii_name="baseInput")
    def base_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "baseInput"))

    @builtins.property
    @jsii.member(jsii_name="capacityProviderInput")
    def capacity_provider_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "capacityProviderInput"))

    @builtins.property
    @jsii.member(jsii_name="weightInput")
    def weight_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "weightInput"))

    @builtins.property
    @jsii.member(jsii_name="base")
    def base(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "base"))

    @base.setter
    def base(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d24d4ba82eaab0e357d291f8d4bdc7a2410b6097666a4726d22b6080f066a53b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "base", value)

    @builtins.property
    @jsii.member(jsii_name="capacityProvider")
    def capacity_provider(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "capacityProvider"))

    @capacity_provider.setter
    def capacity_provider(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63abdf2dba34b3ed22264826d864afe948ae03a7513b0f5de9cc45d075d3e386)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "capacityProvider", value)

    @builtins.property
    @jsii.member(jsii_name="weight")
    def weight(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "weight"))

    @weight.setter
    def weight(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61e78b90254a771ed22c04910e55bc3f13cb9047d91cad0328ebc5684970eb01)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "weight", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EcsTaskSetCapacityProviderStrategy, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EcsTaskSetCapacityProviderStrategy, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EcsTaskSetCapacityProviderStrategy, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4fe22180f3e8acc859c00a00805c1813449bf082f6eaef9283b14226c9e92f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ecsTaskSet.EcsTaskSetConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "cluster": "cluster",
        "service": "service",
        "task_definition": "taskDefinition",
        "capacity_provider_strategy": "capacityProviderStrategy",
        "external_id": "externalId",
        "force_delete": "forceDelete",
        "id": "id",
        "launch_type": "launchType",
        "load_balancer": "loadBalancer",
        "network_configuration": "networkConfiguration",
        "platform_version": "platformVersion",
        "scale": "scale",
        "service_registries": "serviceRegistries",
        "tags": "tags",
        "tags_all": "tagsAll",
        "wait_until_stable": "waitUntilStable",
        "wait_until_stable_timeout": "waitUntilStableTimeout",
    },
)
class EcsTaskSetConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        cluster: builtins.str,
        service: builtins.str,
        task_definition: builtins.str,
        capacity_provider_strategy: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EcsTaskSetCapacityProviderStrategy, typing.Dict[builtins.str, typing.Any]]]]] = None,
        external_id: typing.Optional[builtins.str] = None,
        force_delete: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        launch_type: typing.Optional[builtins.str] = None,
        load_balancer: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EcsTaskSetLoadBalancer", typing.Dict[builtins.str, typing.Any]]]]] = None,
        network_configuration: typing.Optional[typing.Union["EcsTaskSetNetworkConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        platform_version: typing.Optional[builtins.str] = None,
        scale: typing.Optional[typing.Union["EcsTaskSetScale", typing.Dict[builtins.str, typing.Any]]] = None,
        service_registries: typing.Optional[typing.Union["EcsTaskSetServiceRegistries", typing.Dict[builtins.str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        wait_until_stable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        wait_until_stable_timeout: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param cluster: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#cluster EcsTaskSet#cluster}.
        :param service: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#service EcsTaskSet#service}.
        :param task_definition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#task_definition EcsTaskSet#task_definition}.
        :param capacity_provider_strategy: capacity_provider_strategy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#capacity_provider_strategy EcsTaskSet#capacity_provider_strategy}
        :param external_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#external_id EcsTaskSet#external_id}.
        :param force_delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#force_delete EcsTaskSet#force_delete}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#id EcsTaskSet#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param launch_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#launch_type EcsTaskSet#launch_type}.
        :param load_balancer: load_balancer block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#load_balancer EcsTaskSet#load_balancer}
        :param network_configuration: network_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#network_configuration EcsTaskSet#network_configuration}
        :param platform_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#platform_version EcsTaskSet#platform_version}.
        :param scale: scale block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#scale EcsTaskSet#scale}
        :param service_registries: service_registries block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#service_registries EcsTaskSet#service_registries}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#tags EcsTaskSet#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#tags_all EcsTaskSet#tags_all}.
        :param wait_until_stable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#wait_until_stable EcsTaskSet#wait_until_stable}.
        :param wait_until_stable_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#wait_until_stable_timeout EcsTaskSet#wait_until_stable_timeout}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(network_configuration, dict):
            network_configuration = EcsTaskSetNetworkConfiguration(**network_configuration)
        if isinstance(scale, dict):
            scale = EcsTaskSetScale(**scale)
        if isinstance(service_registries, dict):
            service_registries = EcsTaskSetServiceRegistries(**service_registries)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3bea7232650be1278ec33bd9fb8b974700aa25ac2a6c0b26482c3fd6a4030f7c)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument cluster", value=cluster, expected_type=type_hints["cluster"])
            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
            check_type(argname="argument task_definition", value=task_definition, expected_type=type_hints["task_definition"])
            check_type(argname="argument capacity_provider_strategy", value=capacity_provider_strategy, expected_type=type_hints["capacity_provider_strategy"])
            check_type(argname="argument external_id", value=external_id, expected_type=type_hints["external_id"])
            check_type(argname="argument force_delete", value=force_delete, expected_type=type_hints["force_delete"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument launch_type", value=launch_type, expected_type=type_hints["launch_type"])
            check_type(argname="argument load_balancer", value=load_balancer, expected_type=type_hints["load_balancer"])
            check_type(argname="argument network_configuration", value=network_configuration, expected_type=type_hints["network_configuration"])
            check_type(argname="argument platform_version", value=platform_version, expected_type=type_hints["platform_version"])
            check_type(argname="argument scale", value=scale, expected_type=type_hints["scale"])
            check_type(argname="argument service_registries", value=service_registries, expected_type=type_hints["service_registries"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument wait_until_stable", value=wait_until_stable, expected_type=type_hints["wait_until_stable"])
            check_type(argname="argument wait_until_stable_timeout", value=wait_until_stable_timeout, expected_type=type_hints["wait_until_stable_timeout"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cluster": cluster,
            "service": service,
            "task_definition": task_definition,
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
        if capacity_provider_strategy is not None:
            self._values["capacity_provider_strategy"] = capacity_provider_strategy
        if external_id is not None:
            self._values["external_id"] = external_id
        if force_delete is not None:
            self._values["force_delete"] = force_delete
        if id is not None:
            self._values["id"] = id
        if launch_type is not None:
            self._values["launch_type"] = launch_type
        if load_balancer is not None:
            self._values["load_balancer"] = load_balancer
        if network_configuration is not None:
            self._values["network_configuration"] = network_configuration
        if platform_version is not None:
            self._values["platform_version"] = platform_version
        if scale is not None:
            self._values["scale"] = scale
        if service_registries is not None:
            self._values["service_registries"] = service_registries
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if wait_until_stable is not None:
            self._values["wait_until_stable"] = wait_until_stable
        if wait_until_stable_timeout is not None:
            self._values["wait_until_stable_timeout"] = wait_until_stable_timeout

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
    def cluster(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#cluster EcsTaskSet#cluster}.'''
        result = self._values.get("cluster")
        assert result is not None, "Required property 'cluster' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#service EcsTaskSet#service}.'''
        result = self._values.get("service")
        assert result is not None, "Required property 'service' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def task_definition(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#task_definition EcsTaskSet#task_definition}.'''
        result = self._values.get("task_definition")
        assert result is not None, "Required property 'task_definition' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def capacity_provider_strategy(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EcsTaskSetCapacityProviderStrategy]]]:
        '''capacity_provider_strategy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#capacity_provider_strategy EcsTaskSet#capacity_provider_strategy}
        '''
        result = self._values.get("capacity_provider_strategy")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EcsTaskSetCapacityProviderStrategy]]], result)

    @builtins.property
    def external_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#external_id EcsTaskSet#external_id}.'''
        result = self._values.get("external_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def force_delete(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#force_delete EcsTaskSet#force_delete}.'''
        result = self._values.get("force_delete")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#id EcsTaskSet#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def launch_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#launch_type EcsTaskSet#launch_type}.'''
        result = self._values.get("launch_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def load_balancer(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EcsTaskSetLoadBalancer"]]]:
        '''load_balancer block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#load_balancer EcsTaskSet#load_balancer}
        '''
        result = self._values.get("load_balancer")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EcsTaskSetLoadBalancer"]]], result)

    @builtins.property
    def network_configuration(
        self,
    ) -> typing.Optional["EcsTaskSetNetworkConfiguration"]:
        '''network_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#network_configuration EcsTaskSet#network_configuration}
        '''
        result = self._values.get("network_configuration")
        return typing.cast(typing.Optional["EcsTaskSetNetworkConfiguration"], result)

    @builtins.property
    def platform_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#platform_version EcsTaskSet#platform_version}.'''
        result = self._values.get("platform_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scale(self) -> typing.Optional["EcsTaskSetScale"]:
        '''scale block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#scale EcsTaskSet#scale}
        '''
        result = self._values.get("scale")
        return typing.cast(typing.Optional["EcsTaskSetScale"], result)

    @builtins.property
    def service_registries(self) -> typing.Optional["EcsTaskSetServiceRegistries"]:
        '''service_registries block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#service_registries EcsTaskSet#service_registries}
        '''
        result = self._values.get("service_registries")
        return typing.cast(typing.Optional["EcsTaskSetServiceRegistries"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#tags EcsTaskSet#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#tags_all EcsTaskSet#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def wait_until_stable(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#wait_until_stable EcsTaskSet#wait_until_stable}.'''
        result = self._values.get("wait_until_stable")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def wait_until_stable_timeout(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#wait_until_stable_timeout EcsTaskSet#wait_until_stable_timeout}.'''
        result = self._values.get("wait_until_stable_timeout")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsTaskSetConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.ecsTaskSet.EcsTaskSetLoadBalancer",
    jsii_struct_bases=[],
    name_mapping={
        "container_name": "containerName",
        "container_port": "containerPort",
        "load_balancer_name": "loadBalancerName",
        "target_group_arn": "targetGroupArn",
    },
)
class EcsTaskSetLoadBalancer:
    def __init__(
        self,
        *,
        container_name: builtins.str,
        container_port: typing.Optional[jsii.Number] = None,
        load_balancer_name: typing.Optional[builtins.str] = None,
        target_group_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param container_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#container_name EcsTaskSet#container_name}.
        :param container_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#container_port EcsTaskSet#container_port}.
        :param load_balancer_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#load_balancer_name EcsTaskSet#load_balancer_name}.
        :param target_group_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#target_group_arn EcsTaskSet#target_group_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06b0da03fd394f2aa639c14704f0872cf75aa30f244b422ce3530227d89cd0b4)
            check_type(argname="argument container_name", value=container_name, expected_type=type_hints["container_name"])
            check_type(argname="argument container_port", value=container_port, expected_type=type_hints["container_port"])
            check_type(argname="argument load_balancer_name", value=load_balancer_name, expected_type=type_hints["load_balancer_name"])
            check_type(argname="argument target_group_arn", value=target_group_arn, expected_type=type_hints["target_group_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "container_name": container_name,
        }
        if container_port is not None:
            self._values["container_port"] = container_port
        if load_balancer_name is not None:
            self._values["load_balancer_name"] = load_balancer_name
        if target_group_arn is not None:
            self._values["target_group_arn"] = target_group_arn

    @builtins.property
    def container_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#container_name EcsTaskSet#container_name}.'''
        result = self._values.get("container_name")
        assert result is not None, "Required property 'container_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def container_port(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#container_port EcsTaskSet#container_port}.'''
        result = self._values.get("container_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def load_balancer_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#load_balancer_name EcsTaskSet#load_balancer_name}.'''
        result = self._values.get("load_balancer_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_group_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#target_group_arn EcsTaskSet#target_group_arn}.'''
        result = self._values.get("target_group_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsTaskSetLoadBalancer(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcsTaskSetLoadBalancerList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ecsTaskSet.EcsTaskSetLoadBalancerList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__20082d932726760ee9fc84a7eb7a52e246125e1bb394856eb4f4929734dfd6f1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "EcsTaskSetLoadBalancerOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4659f7ad2f0f35976b3b8d8d0c7bb0b10f6d9b14fb6c4966bb926d1798dc4541)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EcsTaskSetLoadBalancerOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd9cee18512c7a27e5e59c86a8f463989b3b4868635fa66da00fca65493ae62b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6646322a79cee6f3d0d9cba7b4a299afeb5edae565ccef17f48849a14971d1a8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0cdf3c5fc3250b928b44298ef2355cafcf8af36cac217f63c6cc17b42f5440ef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EcsTaskSetLoadBalancer]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EcsTaskSetLoadBalancer]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EcsTaskSetLoadBalancer]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e732296ae984652d2a27bfe7a3a30d333a6f89d2fc1befdfa734be1c010b85bf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EcsTaskSetLoadBalancerOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ecsTaskSet.EcsTaskSetLoadBalancerOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__886060626df90d5b09b801801a9427d623bd0b5f3686b14d62a2a60c5c54d8a8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetContainerPort")
    def reset_container_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContainerPort", []))

    @jsii.member(jsii_name="resetLoadBalancerName")
    def reset_load_balancer_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoadBalancerName", []))

    @jsii.member(jsii_name="resetTargetGroupArn")
    def reset_target_group_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetGroupArn", []))

    @builtins.property
    @jsii.member(jsii_name="containerNameInput")
    def container_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "containerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="containerPortInput")
    def container_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "containerPortInput"))

    @builtins.property
    @jsii.member(jsii_name="loadBalancerNameInput")
    def load_balancer_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "loadBalancerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="targetGroupArnInput")
    def target_group_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetGroupArnInput"))

    @builtins.property
    @jsii.member(jsii_name="containerName")
    def container_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "containerName"))

    @container_name.setter
    def container_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02a3315626aa0e65e63c4f725b3ed5602b450a61df373aa639a6292199116557)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerName", value)

    @builtins.property
    @jsii.member(jsii_name="containerPort")
    def container_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "containerPort"))

    @container_port.setter
    def container_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dba028690e852185b3e0939e35a9de6dfc7bd715a88c7bfd91616bf24e07cc11)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerPort", value)

    @builtins.property
    @jsii.member(jsii_name="loadBalancerName")
    def load_balancer_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "loadBalancerName"))

    @load_balancer_name.setter
    def load_balancer_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__30a1f90d6974140d3d0308cd8c6767c440b94540bd4ba6f838af9ed4b08149a5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loadBalancerName", value)

    @builtins.property
    @jsii.member(jsii_name="targetGroupArn")
    def target_group_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetGroupArn"))

    @target_group_arn.setter
    def target_group_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26958c1aa34c2ee2594e7000a8995dff29e6f4ecf656d210b0de47deeeabab40)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetGroupArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EcsTaskSetLoadBalancer, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EcsTaskSetLoadBalancer, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EcsTaskSetLoadBalancer, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__646883ee36d73983e6926cac5c88d37f4b1680249e100872fe42cab9eee4b112)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ecsTaskSet.EcsTaskSetNetworkConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "subnets": "subnets",
        "assign_public_ip": "assignPublicIp",
        "security_groups": "securityGroups",
    },
)
class EcsTaskSetNetworkConfiguration:
    def __init__(
        self,
        *,
        subnets: typing.Sequence[builtins.str],
        assign_public_ip: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param subnets: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#subnets EcsTaskSet#subnets}.
        :param assign_public_ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#assign_public_ip EcsTaskSet#assign_public_ip}.
        :param security_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#security_groups EcsTaskSet#security_groups}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b09ccb25329fae58eb9050f54e6d6904fe0a58513a32fddaccf0de05665c7fe)
            check_type(argname="argument subnets", value=subnets, expected_type=type_hints["subnets"])
            check_type(argname="argument assign_public_ip", value=assign_public_ip, expected_type=type_hints["assign_public_ip"])
            check_type(argname="argument security_groups", value=security_groups, expected_type=type_hints["security_groups"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "subnets": subnets,
        }
        if assign_public_ip is not None:
            self._values["assign_public_ip"] = assign_public_ip
        if security_groups is not None:
            self._values["security_groups"] = security_groups

    @builtins.property
    def subnets(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#subnets EcsTaskSet#subnets}.'''
        result = self._values.get("subnets")
        assert result is not None, "Required property 'subnets' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def assign_public_ip(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#assign_public_ip EcsTaskSet#assign_public_ip}.'''
        result = self._values.get("assign_public_ip")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def security_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#security_groups EcsTaskSet#security_groups}.'''
        result = self._values.get("security_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsTaskSetNetworkConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcsTaskSetNetworkConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ecsTaskSet.EcsTaskSetNetworkConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__44dea451ff4dbef4464e5bd09648f85dd7285689b876f8a928a1d21457d97bba)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAssignPublicIp")
    def reset_assign_public_ip(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAssignPublicIp", []))

    @jsii.member(jsii_name="resetSecurityGroups")
    def reset_security_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecurityGroups", []))

    @builtins.property
    @jsii.member(jsii_name="assignPublicIpInput")
    def assign_public_ip_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "assignPublicIpInput"))

    @builtins.property
    @jsii.member(jsii_name="securityGroupsInput")
    def security_groups_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetsInput")
    def subnets_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "subnetsInput"))

    @builtins.property
    @jsii.member(jsii_name="assignPublicIp")
    def assign_public_ip(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "assignPublicIp"))

    @assign_public_ip.setter
    def assign_public_ip(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__381d51432a11aca2b1d5337511e871e92551a2ba6e7fd175efda838b3bba806a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "assignPublicIp", value)

    @builtins.property
    @jsii.member(jsii_name="securityGroups")
    def security_groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "securityGroups"))

    @security_groups.setter
    def security_groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a3b6a59aad31f32a0e76396eed37616051aecbe376226f3468a61666d00d428)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroups", value)

    @builtins.property
    @jsii.member(jsii_name="subnets")
    def subnets(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subnets"))

    @subnets.setter
    def subnets(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a5f6f8acecdfd59cec5f927c3a9e85a4480da147dfc134546bf4302e49bf7e8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnets", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[EcsTaskSetNetworkConfiguration]:
        return typing.cast(typing.Optional[EcsTaskSetNetworkConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EcsTaskSetNetworkConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__159cba0fdd865e4d72e6f7a3cb808a9c60b5b969a50f6927ea0212ad7696029b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ecsTaskSet.EcsTaskSetScale",
    jsii_struct_bases=[],
    name_mapping={"unit": "unit", "value": "value"},
)
class EcsTaskSetScale:
    def __init__(
        self,
        *,
        unit: typing.Optional[builtins.str] = None,
        value: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#unit EcsTaskSet#unit}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#value EcsTaskSet#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9db4faa3e8295bb6cbb2d7bdb7569b3dccd20cddf8f84b86f4e0b6fd060e9654)
            check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if unit is not None:
            self._values["unit"] = unit
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def unit(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#unit EcsTaskSet#unit}.'''
        result = self._values.get("unit")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#value EcsTaskSet#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsTaskSetScale(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcsTaskSetScaleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ecsTaskSet.EcsTaskSetScaleOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5628f24eb59acc0e1e082a27fb641d51e684c6216797d1e7ded6648c526d252f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetUnit")
    def reset_unit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUnit", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="unitInput")
    def unit_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "unitInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="unit")
    def unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "unit"))

    @unit.setter
    def unit(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b2a0155263cd839baf48e74c2529e5c5ffa98a962d81d18771016b8dbe2234c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unit", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "value"))

    @value.setter
    def value(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76d4973bf245da520bfc90588867d8a3582404153a9d7ba64b773f3918080435)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[EcsTaskSetScale]:
        return typing.cast(typing.Optional[EcsTaskSetScale], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[EcsTaskSetScale]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c6d408beaebea83c35d5a7f8592b5cf032d6dac634759b7bcb5ebeb67a60bbb8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ecsTaskSet.EcsTaskSetServiceRegistries",
    jsii_struct_bases=[],
    name_mapping={
        "registry_arn": "registryArn",
        "container_name": "containerName",
        "container_port": "containerPort",
        "port": "port",
    },
)
class EcsTaskSetServiceRegistries:
    def __init__(
        self,
        *,
        registry_arn: builtins.str,
        container_name: typing.Optional[builtins.str] = None,
        container_port: typing.Optional[jsii.Number] = None,
        port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param registry_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#registry_arn EcsTaskSet#registry_arn}.
        :param container_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#container_name EcsTaskSet#container_name}.
        :param container_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#container_port EcsTaskSet#container_port}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#port EcsTaskSet#port}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6be007f8708aea0c24a09b191de3ad6e83159e0c6f2a8c2874e75bfb456a6264)
            check_type(argname="argument registry_arn", value=registry_arn, expected_type=type_hints["registry_arn"])
            check_type(argname="argument container_name", value=container_name, expected_type=type_hints["container_name"])
            check_type(argname="argument container_port", value=container_port, expected_type=type_hints["container_port"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "registry_arn": registry_arn,
        }
        if container_name is not None:
            self._values["container_name"] = container_name
        if container_port is not None:
            self._values["container_port"] = container_port
        if port is not None:
            self._values["port"] = port

    @builtins.property
    def registry_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#registry_arn EcsTaskSet#registry_arn}.'''
        result = self._values.get("registry_arn")
        assert result is not None, "Required property 'registry_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def container_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#container_name EcsTaskSet#container_name}.'''
        result = self._values.get("container_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def container_port(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#container_port EcsTaskSet#container_port}.'''
        result = self._values.get("container_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#port EcsTaskSet#port}.'''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsTaskSetServiceRegistries(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcsTaskSetServiceRegistriesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ecsTaskSet.EcsTaskSetServiceRegistriesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ef16491d919b131ace6218e29df4ac9b18dd1333385626ad4752ccda6a1f1512)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetContainerName")
    def reset_container_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContainerName", []))

    @jsii.member(jsii_name="resetContainerPort")
    def reset_container_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContainerPort", []))

    @jsii.member(jsii_name="resetPort")
    def reset_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPort", []))

    @builtins.property
    @jsii.member(jsii_name="containerNameInput")
    def container_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "containerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="containerPortInput")
    def container_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "containerPortInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="registryArnInput")
    def registry_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "registryArnInput"))

    @builtins.property
    @jsii.member(jsii_name="containerName")
    def container_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "containerName"))

    @container_name.setter
    def container_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__861c844d85ec2eb57aa73c88339579be725b0b2bef0a68d7504bce708c1e8fa8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerName", value)

    @builtins.property
    @jsii.member(jsii_name="containerPort")
    def container_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "containerPort"))

    @container_port.setter
    def container_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__922074a0bc2711cd9c1ee8435fa2cf31aa2588597108534954923220182348e4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerPort", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f184461ba7a246ec6fb0634789d6f25053c8e17c242717a904deb52010ff607)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="registryArn")
    def registry_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "registryArn"))

    @registry_arn.setter
    def registry_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c37c1657b6d707c53651c427c5f7941851813255cee51f19b9f2ae0c54abc510)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "registryArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[EcsTaskSetServiceRegistries]:
        return typing.cast(typing.Optional[EcsTaskSetServiceRegistries], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EcsTaskSetServiceRegistries],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4f30d9a81f305dca1e6e13eca6d499829b3442fd9812c5a59bd7e25bad276b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "EcsTaskSet",
    "EcsTaskSetCapacityProviderStrategy",
    "EcsTaskSetCapacityProviderStrategyList",
    "EcsTaskSetCapacityProviderStrategyOutputReference",
    "EcsTaskSetConfig",
    "EcsTaskSetLoadBalancer",
    "EcsTaskSetLoadBalancerList",
    "EcsTaskSetLoadBalancerOutputReference",
    "EcsTaskSetNetworkConfiguration",
    "EcsTaskSetNetworkConfigurationOutputReference",
    "EcsTaskSetScale",
    "EcsTaskSetScaleOutputReference",
    "EcsTaskSetServiceRegistries",
    "EcsTaskSetServiceRegistriesOutputReference",
]

publication.publish()

def _typecheckingstub__142d22979688ef4a5e16e476a6e02ed53b617b97803dd000ccdd877ed80e63ff(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    cluster: builtins.str,
    service: builtins.str,
    task_definition: builtins.str,
    capacity_provider_strategy: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EcsTaskSetCapacityProviderStrategy, typing.Dict[builtins.str, typing.Any]]]]] = None,
    external_id: typing.Optional[builtins.str] = None,
    force_delete: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    launch_type: typing.Optional[builtins.str] = None,
    load_balancer: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EcsTaskSetLoadBalancer, typing.Dict[builtins.str, typing.Any]]]]] = None,
    network_configuration: typing.Optional[typing.Union[EcsTaskSetNetworkConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    platform_version: typing.Optional[builtins.str] = None,
    scale: typing.Optional[typing.Union[EcsTaskSetScale, typing.Dict[builtins.str, typing.Any]]] = None,
    service_registries: typing.Optional[typing.Union[EcsTaskSetServiceRegistries, typing.Dict[builtins.str, typing.Any]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    wait_until_stable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    wait_until_stable_timeout: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__0b88ac474c2f9fe552ab824df35d678de322e5212428e7903c75329840619131(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EcsTaskSetCapacityProviderStrategy, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6677cb11cc54d17e9718bc4b9638e90159d2f48f2f5d3d10d98e1d2d677e6d43(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EcsTaskSetLoadBalancer, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27ef6798289c9b29c22ecaca79d42b41ae4cba112f731bb0ac449889a4657963(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f371d83789efd5c482cf74a16479ae28bb5ec805a49b1c78ad224f334bd3d94(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14c5dc8c426e6023106f0d30f63746cd5332dc889782be95208309729638a76e(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cbdba5a54eb06706a07d77eaaa23c4159bdf74a6fc78cd951e4af9562004993b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f81e3098778993155bc109e0866e848d9beba8f3cab132bdfb90145b40c33e5a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__569a392df4378bb264e958b5617b5074e5b8bd2062b0cfd930a71770c957550b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56f19c15ba3d28a25de050a26dc0a842402701683d1c4d0dc060b42574904768(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c20b48d87c3928a61abbf33e512714de85311b3e70b84d7878686c5095d90df8(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84174defc102d58611736cff764e968af97eac57b13f75ee6aed07edf4250318(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56d42fe270dae5fc0c99f6a0263a5c55dcbb98d6604b19f4207c7ffe76ed170d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f4ee7261c8871457ecf974514d7081039321300e9fd6a358f13c36de1aa46e9(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a4d79e9d5e3b16cf86cbe5e774c7a43abdebfafa6380051f0cf704cf5b87d72(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e762bd3d25388eaf5ed6bda6233f3ea316e8945159c91890c2ce0fde85b56256(
    *,
    capacity_provider: builtins.str,
    weight: jsii.Number,
    base: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9316b3bb44594a9222bb4dcc67d76e6d415a660da8ae1a9bd252f775a6a0e2a4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db9ffee31dee6c5f34f31a5f12462398af284c1383e8ec4d2cdf66cac5513b1b(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60578c12ba7190967a2f0c260a50cba7a71c15cea4443ea5f8e63a63c29979d5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8c9bcfa944127a3da8e8e9a955ba6e923cc4137a15427c37068c33ceafa7c7b(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c4f6b26bdd89f6d6c91ee64c6f07d02fadffc8c4c8ce425d963ef7a04f40438(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee440e91f61930d007850559694ccf253f46be9a24902f170a3bd0825693fb92(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EcsTaskSetCapacityProviderStrategy]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9365ab9fbe76fd0bd3893dc487bbfc694272242056bf9f66ae9db4a4053c3d2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d24d4ba82eaab0e357d291f8d4bdc7a2410b6097666a4726d22b6080f066a53b(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63abdf2dba34b3ed22264826d864afe948ae03a7513b0f5de9cc45d075d3e386(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61e78b90254a771ed22c04910e55bc3f13cb9047d91cad0328ebc5684970eb01(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4fe22180f3e8acc859c00a00805c1813449bf082f6eaef9283b14226c9e92f8(
    value: typing.Optional[typing.Union[EcsTaskSetCapacityProviderStrategy, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3bea7232650be1278ec33bd9fb8b974700aa25ac2a6c0b26482c3fd6a4030f7c(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    cluster: builtins.str,
    service: builtins.str,
    task_definition: builtins.str,
    capacity_provider_strategy: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EcsTaskSetCapacityProviderStrategy, typing.Dict[builtins.str, typing.Any]]]]] = None,
    external_id: typing.Optional[builtins.str] = None,
    force_delete: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    launch_type: typing.Optional[builtins.str] = None,
    load_balancer: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EcsTaskSetLoadBalancer, typing.Dict[builtins.str, typing.Any]]]]] = None,
    network_configuration: typing.Optional[typing.Union[EcsTaskSetNetworkConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    platform_version: typing.Optional[builtins.str] = None,
    scale: typing.Optional[typing.Union[EcsTaskSetScale, typing.Dict[builtins.str, typing.Any]]] = None,
    service_registries: typing.Optional[typing.Union[EcsTaskSetServiceRegistries, typing.Dict[builtins.str, typing.Any]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    wait_until_stable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    wait_until_stable_timeout: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06b0da03fd394f2aa639c14704f0872cf75aa30f244b422ce3530227d89cd0b4(
    *,
    container_name: builtins.str,
    container_port: typing.Optional[jsii.Number] = None,
    load_balancer_name: typing.Optional[builtins.str] = None,
    target_group_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20082d932726760ee9fc84a7eb7a52e246125e1bb394856eb4f4929734dfd6f1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4659f7ad2f0f35976b3b8d8d0c7bb0b10f6d9b14fb6c4966bb926d1798dc4541(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd9cee18512c7a27e5e59c86a8f463989b3b4868635fa66da00fca65493ae62b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6646322a79cee6f3d0d9cba7b4a299afeb5edae565ccef17f48849a14971d1a8(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0cdf3c5fc3250b928b44298ef2355cafcf8af36cac217f63c6cc17b42f5440ef(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e732296ae984652d2a27bfe7a3a30d333a6f89d2fc1befdfa734be1c010b85bf(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EcsTaskSetLoadBalancer]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__886060626df90d5b09b801801a9427d623bd0b5f3686b14d62a2a60c5c54d8a8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02a3315626aa0e65e63c4f725b3ed5602b450a61df373aa639a6292199116557(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dba028690e852185b3e0939e35a9de6dfc7bd715a88c7bfd91616bf24e07cc11(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30a1f90d6974140d3d0308cd8c6767c440b94540bd4ba6f838af9ed4b08149a5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26958c1aa34c2ee2594e7000a8995dff29e6f4ecf656d210b0de47deeeabab40(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__646883ee36d73983e6926cac5c88d37f4b1680249e100872fe42cab9eee4b112(
    value: typing.Optional[typing.Union[EcsTaskSetLoadBalancer, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b09ccb25329fae58eb9050f54e6d6904fe0a58513a32fddaccf0de05665c7fe(
    *,
    subnets: typing.Sequence[builtins.str],
    assign_public_ip: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44dea451ff4dbef4464e5bd09648f85dd7285689b876f8a928a1d21457d97bba(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__381d51432a11aca2b1d5337511e871e92551a2ba6e7fd175efda838b3bba806a(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a3b6a59aad31f32a0e76396eed37616051aecbe376226f3468a61666d00d428(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a5f6f8acecdfd59cec5f927c3a9e85a4480da147dfc134546bf4302e49bf7e8(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__159cba0fdd865e4d72e6f7a3cb808a9c60b5b969a50f6927ea0212ad7696029b(
    value: typing.Optional[EcsTaskSetNetworkConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9db4faa3e8295bb6cbb2d7bdb7569b3dccd20cddf8f84b86f4e0b6fd060e9654(
    *,
    unit: typing.Optional[builtins.str] = None,
    value: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5628f24eb59acc0e1e082a27fb641d51e684c6216797d1e7ded6648c526d252f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b2a0155263cd839baf48e74c2529e5c5ffa98a962d81d18771016b8dbe2234c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76d4973bf245da520bfc90588867d8a3582404153a9d7ba64b773f3918080435(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6d408beaebea83c35d5a7f8592b5cf032d6dac634759b7bcb5ebeb67a60bbb8(
    value: typing.Optional[EcsTaskSetScale],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6be007f8708aea0c24a09b191de3ad6e83159e0c6f2a8c2874e75bfb456a6264(
    *,
    registry_arn: builtins.str,
    container_name: typing.Optional[builtins.str] = None,
    container_port: typing.Optional[jsii.Number] = None,
    port: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef16491d919b131ace6218e29df4ac9b18dd1333385626ad4752ccda6a1f1512(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__861c844d85ec2eb57aa73c88339579be725b0b2bef0a68d7504bce708c1e8fa8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__922074a0bc2711cd9c1ee8435fa2cf31aa2588597108534954923220182348e4(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f184461ba7a246ec6fb0634789d6f25053c8e17c242717a904deb52010ff607(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c37c1657b6d707c53651c427c5f7941851813255cee51f19b9f2ae0c54abc510(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4f30d9a81f305dca1e6e13eca6d499829b3442fd9812c5a59bd7e25bad276b4(
    value: typing.Optional[EcsTaskSetServiceRegistries],
) -> None:
    """Type checking stubs"""
    pass
