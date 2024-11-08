'''
# `aws_ecs_task_definition`

Refer to the Terraform Registory for docs: [`aws_ecs_task_definition`](https://www.terraform.io/docs/providers/aws/r/ecs_task_definition).
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


class EcsTaskDefinition(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ecsTaskDefinition.EcsTaskDefinition",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition aws_ecs_task_definition}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        container_definitions: builtins.str,
        family: builtins.str,
        cpu: typing.Optional[builtins.str] = None,
        ephemeral_storage: typing.Optional[typing.Union["EcsTaskDefinitionEphemeralStorage", typing.Dict[builtins.str, typing.Any]]] = None,
        execution_role_arn: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        inference_accelerator: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EcsTaskDefinitionInferenceAccelerator", typing.Dict[builtins.str, typing.Any]]]]] = None,
        ipc_mode: typing.Optional[builtins.str] = None,
        memory: typing.Optional[builtins.str] = None,
        network_mode: typing.Optional[builtins.str] = None,
        pid_mode: typing.Optional[builtins.str] = None,
        placement_constraints: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EcsTaskDefinitionPlacementConstraints", typing.Dict[builtins.str, typing.Any]]]]] = None,
        proxy_configuration: typing.Optional[typing.Union["EcsTaskDefinitionProxyConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        requires_compatibilities: typing.Optional[typing.Sequence[builtins.str]] = None,
        runtime_platform: typing.Optional[typing.Union["EcsTaskDefinitionRuntimePlatform", typing.Dict[builtins.str, typing.Any]]] = None,
        skip_destroy: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        task_role_arn: typing.Optional[builtins.str] = None,
        volume: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EcsTaskDefinitionVolume", typing.Dict[builtins.str, typing.Any]]]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition aws_ecs_task_definition} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param container_definitions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#container_definitions EcsTaskDefinition#container_definitions}.
        :param family: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#family EcsTaskDefinition#family}.
        :param cpu: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#cpu EcsTaskDefinition#cpu}.
        :param ephemeral_storage: ephemeral_storage block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#ephemeral_storage EcsTaskDefinition#ephemeral_storage}
        :param execution_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#execution_role_arn EcsTaskDefinition#execution_role_arn}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#id EcsTaskDefinition#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param inference_accelerator: inference_accelerator block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#inference_accelerator EcsTaskDefinition#inference_accelerator}
        :param ipc_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#ipc_mode EcsTaskDefinition#ipc_mode}.
        :param memory: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#memory EcsTaskDefinition#memory}.
        :param network_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#network_mode EcsTaskDefinition#network_mode}.
        :param pid_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#pid_mode EcsTaskDefinition#pid_mode}.
        :param placement_constraints: placement_constraints block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#placement_constraints EcsTaskDefinition#placement_constraints}
        :param proxy_configuration: proxy_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#proxy_configuration EcsTaskDefinition#proxy_configuration}
        :param requires_compatibilities: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#requires_compatibilities EcsTaskDefinition#requires_compatibilities}.
        :param runtime_platform: runtime_platform block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#runtime_platform EcsTaskDefinition#runtime_platform}
        :param skip_destroy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#skip_destroy EcsTaskDefinition#skip_destroy}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#tags EcsTaskDefinition#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#tags_all EcsTaskDefinition#tags_all}.
        :param task_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#task_role_arn EcsTaskDefinition#task_role_arn}.
        :param volume: volume block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#volume EcsTaskDefinition#volume}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5016cc3736ae456900355e094294caaf2e97266d211531281daeed4dcdcf04e6)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = EcsTaskDefinitionConfig(
            container_definitions=container_definitions,
            family=family,
            cpu=cpu,
            ephemeral_storage=ephemeral_storage,
            execution_role_arn=execution_role_arn,
            id=id,
            inference_accelerator=inference_accelerator,
            ipc_mode=ipc_mode,
            memory=memory,
            network_mode=network_mode,
            pid_mode=pid_mode,
            placement_constraints=placement_constraints,
            proxy_configuration=proxy_configuration,
            requires_compatibilities=requires_compatibilities,
            runtime_platform=runtime_platform,
            skip_destroy=skip_destroy,
            tags=tags,
            tags_all=tags_all,
            task_role_arn=task_role_arn,
            volume=volume,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putEphemeralStorage")
    def put_ephemeral_storage(self, *, size_in_gib: jsii.Number) -> None:
        '''
        :param size_in_gib: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#size_in_gib EcsTaskDefinition#size_in_gib}.
        '''
        value = EcsTaskDefinitionEphemeralStorage(size_in_gib=size_in_gib)

        return typing.cast(None, jsii.invoke(self, "putEphemeralStorage", [value]))

    @jsii.member(jsii_name="putInferenceAccelerator")
    def put_inference_accelerator(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EcsTaskDefinitionInferenceAccelerator", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__86a6a610c1998bf3625af43f5bf07666846c4cb1f6f5ccf66f9192fa301ba4e7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putInferenceAccelerator", [value]))

    @jsii.member(jsii_name="putPlacementConstraints")
    def put_placement_constraints(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EcsTaskDefinitionPlacementConstraints", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3cee5e36feef94865ee57e4f8b105b65be8aec41a27cd2a90d4fad547b9475e9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPlacementConstraints", [value]))

    @jsii.member(jsii_name="putProxyConfiguration")
    def put_proxy_configuration(
        self,
        *,
        container_name: builtins.str,
        properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param container_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#container_name EcsTaskDefinition#container_name}.
        :param properties: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#properties EcsTaskDefinition#properties}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#type EcsTaskDefinition#type}.
        '''
        value = EcsTaskDefinitionProxyConfiguration(
            container_name=container_name, properties=properties, type=type
        )

        return typing.cast(None, jsii.invoke(self, "putProxyConfiguration", [value]))

    @jsii.member(jsii_name="putRuntimePlatform")
    def put_runtime_platform(
        self,
        *,
        cpu_architecture: typing.Optional[builtins.str] = None,
        operating_system_family: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cpu_architecture: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#cpu_architecture EcsTaskDefinition#cpu_architecture}.
        :param operating_system_family: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#operating_system_family EcsTaskDefinition#operating_system_family}.
        '''
        value = EcsTaskDefinitionRuntimePlatform(
            cpu_architecture=cpu_architecture,
            operating_system_family=operating_system_family,
        )

        return typing.cast(None, jsii.invoke(self, "putRuntimePlatform", [value]))

    @jsii.member(jsii_name="putVolume")
    def put_volume(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EcsTaskDefinitionVolume", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c9dbe3694625ac0a5ca4e8bac304518a3bfc6d5268363fce30a18be8d3ac2d7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putVolume", [value]))

    @jsii.member(jsii_name="resetCpu")
    def reset_cpu(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCpu", []))

    @jsii.member(jsii_name="resetEphemeralStorage")
    def reset_ephemeral_storage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEphemeralStorage", []))

    @jsii.member(jsii_name="resetExecutionRoleArn")
    def reset_execution_role_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExecutionRoleArn", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetInferenceAccelerator")
    def reset_inference_accelerator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInferenceAccelerator", []))

    @jsii.member(jsii_name="resetIpcMode")
    def reset_ipc_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpcMode", []))

    @jsii.member(jsii_name="resetMemory")
    def reset_memory(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMemory", []))

    @jsii.member(jsii_name="resetNetworkMode")
    def reset_network_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworkMode", []))

    @jsii.member(jsii_name="resetPidMode")
    def reset_pid_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPidMode", []))

    @jsii.member(jsii_name="resetPlacementConstraints")
    def reset_placement_constraints(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPlacementConstraints", []))

    @jsii.member(jsii_name="resetProxyConfiguration")
    def reset_proxy_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProxyConfiguration", []))

    @jsii.member(jsii_name="resetRequiresCompatibilities")
    def reset_requires_compatibilities(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequiresCompatibilities", []))

    @jsii.member(jsii_name="resetRuntimePlatform")
    def reset_runtime_platform(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRuntimePlatform", []))

    @jsii.member(jsii_name="resetSkipDestroy")
    def reset_skip_destroy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSkipDestroy", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetTaskRoleArn")
    def reset_task_role_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTaskRoleArn", []))

    @jsii.member(jsii_name="resetVolume")
    def reset_volume(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVolume", []))

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
    @jsii.member(jsii_name="ephemeralStorage")
    def ephemeral_storage(self) -> "EcsTaskDefinitionEphemeralStorageOutputReference":
        return typing.cast("EcsTaskDefinitionEphemeralStorageOutputReference", jsii.get(self, "ephemeralStorage"))

    @builtins.property
    @jsii.member(jsii_name="inferenceAccelerator")
    def inference_accelerator(self) -> "EcsTaskDefinitionInferenceAcceleratorList":
        return typing.cast("EcsTaskDefinitionInferenceAcceleratorList", jsii.get(self, "inferenceAccelerator"))

    @builtins.property
    @jsii.member(jsii_name="placementConstraints")
    def placement_constraints(self) -> "EcsTaskDefinitionPlacementConstraintsList":
        return typing.cast("EcsTaskDefinitionPlacementConstraintsList", jsii.get(self, "placementConstraints"))

    @builtins.property
    @jsii.member(jsii_name="proxyConfiguration")
    def proxy_configuration(
        self,
    ) -> "EcsTaskDefinitionProxyConfigurationOutputReference":
        return typing.cast("EcsTaskDefinitionProxyConfigurationOutputReference", jsii.get(self, "proxyConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="revision")
    def revision(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "revision"))

    @builtins.property
    @jsii.member(jsii_name="runtimePlatform")
    def runtime_platform(self) -> "EcsTaskDefinitionRuntimePlatformOutputReference":
        return typing.cast("EcsTaskDefinitionRuntimePlatformOutputReference", jsii.get(self, "runtimePlatform"))

    @builtins.property
    @jsii.member(jsii_name="volume")
    def volume(self) -> "EcsTaskDefinitionVolumeList":
        return typing.cast("EcsTaskDefinitionVolumeList", jsii.get(self, "volume"))

    @builtins.property
    @jsii.member(jsii_name="containerDefinitionsInput")
    def container_definitions_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "containerDefinitionsInput"))

    @builtins.property
    @jsii.member(jsii_name="cpuInput")
    def cpu_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cpuInput"))

    @builtins.property
    @jsii.member(jsii_name="ephemeralStorageInput")
    def ephemeral_storage_input(
        self,
    ) -> typing.Optional["EcsTaskDefinitionEphemeralStorage"]:
        return typing.cast(typing.Optional["EcsTaskDefinitionEphemeralStorage"], jsii.get(self, "ephemeralStorageInput"))

    @builtins.property
    @jsii.member(jsii_name="executionRoleArnInput")
    def execution_role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "executionRoleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="familyInput")
    def family_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "familyInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="inferenceAcceleratorInput")
    def inference_accelerator_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EcsTaskDefinitionInferenceAccelerator"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EcsTaskDefinitionInferenceAccelerator"]]], jsii.get(self, "inferenceAcceleratorInput"))

    @builtins.property
    @jsii.member(jsii_name="ipcModeInput")
    def ipc_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipcModeInput"))

    @builtins.property
    @jsii.member(jsii_name="memoryInput")
    def memory_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "memoryInput"))

    @builtins.property
    @jsii.member(jsii_name="networkModeInput")
    def network_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkModeInput"))

    @builtins.property
    @jsii.member(jsii_name="pidModeInput")
    def pid_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pidModeInput"))

    @builtins.property
    @jsii.member(jsii_name="placementConstraintsInput")
    def placement_constraints_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EcsTaskDefinitionPlacementConstraints"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EcsTaskDefinitionPlacementConstraints"]]], jsii.get(self, "placementConstraintsInput"))

    @builtins.property
    @jsii.member(jsii_name="proxyConfigurationInput")
    def proxy_configuration_input(
        self,
    ) -> typing.Optional["EcsTaskDefinitionProxyConfiguration"]:
        return typing.cast(typing.Optional["EcsTaskDefinitionProxyConfiguration"], jsii.get(self, "proxyConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="requiresCompatibilitiesInput")
    def requires_compatibilities_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "requiresCompatibilitiesInput"))

    @builtins.property
    @jsii.member(jsii_name="runtimePlatformInput")
    def runtime_platform_input(
        self,
    ) -> typing.Optional["EcsTaskDefinitionRuntimePlatform"]:
        return typing.cast(typing.Optional["EcsTaskDefinitionRuntimePlatform"], jsii.get(self, "runtimePlatformInput"))

    @builtins.property
    @jsii.member(jsii_name="skipDestroyInput")
    def skip_destroy_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "skipDestroyInput"))

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
    @jsii.member(jsii_name="taskRoleArnInput")
    def task_role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "taskRoleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="volumeInput")
    def volume_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EcsTaskDefinitionVolume"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EcsTaskDefinitionVolume"]]], jsii.get(self, "volumeInput"))

    @builtins.property
    @jsii.member(jsii_name="containerDefinitions")
    def container_definitions(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "containerDefinitions"))

    @container_definitions.setter
    def container_definitions(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01b43b3be86e0b135ebb1e478c1906378bd7266f2e507e4d366c436b11c0ab05)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerDefinitions", value)

    @builtins.property
    @jsii.member(jsii_name="cpu")
    def cpu(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cpu"))

    @cpu.setter
    def cpu(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2494fa0cbceff5092643f8a37feeae82560b0edfbaa8ae9102d888bceb9af184)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpu", value)

    @builtins.property
    @jsii.member(jsii_name="executionRoleArn")
    def execution_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "executionRoleArn"))

    @execution_role_arn.setter
    def execution_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9f5ff1776df8cd8c9e5eb2b01d1b422e8e53a4c76c08864f6ac1d48ae55029b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "executionRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="family")
    def family(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "family"))

    @family.setter
    def family(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ff72af2c739ffff14cbb87dc8314576593894898c5bcf00560acbd029941840)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "family", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8da7531f3599513f8954eca61c0e029952cba5b46a84881ae9c6a74f518b1c7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="ipcMode")
    def ipc_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipcMode"))

    @ipc_mode.setter
    def ipc_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7775b1761eab42d08c83b759a3ee5d47041809c694fdb69e6d691582c1a38d28)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipcMode", value)

    @builtins.property
    @jsii.member(jsii_name="memory")
    def memory(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "memory"))

    @memory.setter
    def memory(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e2b510c0015e787e8b5e15767c12d56451086f7757a55e72d10f54e93bcf003)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memory", value)

    @builtins.property
    @jsii.member(jsii_name="networkMode")
    def network_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "networkMode"))

    @network_mode.setter
    def network_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__751b2265e23def9f3b385ba436c6a9f180ac26298c753e24d422b569b49f901c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkMode", value)

    @builtins.property
    @jsii.member(jsii_name="pidMode")
    def pid_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pidMode"))

    @pid_mode.setter
    def pid_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e347ae82e237241fca28c39d3305e51ba6cc73bb9d07edbf3ef4771476ee909)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pidMode", value)

    @builtins.property
    @jsii.member(jsii_name="requiresCompatibilities")
    def requires_compatibilities(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "requiresCompatibilities"))

    @requires_compatibilities.setter
    def requires_compatibilities(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b2b793e5e562f770c6104d9bfe8c033ab1d787c038bcc65c481fa9b07ddcedf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requiresCompatibilities", value)

    @builtins.property
    @jsii.member(jsii_name="skipDestroy")
    def skip_destroy(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "skipDestroy"))

    @skip_destroy.setter
    def skip_destroy(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1eb0286078e8e91c609ed2cba5d11aa0c76db29713fe3b636f67e13c1e52acd0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "skipDestroy", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__652034a30cfd41b21a6ad87171ae2ce523ec97df9218b50289304eb16fbe4e6e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a8bffeb5253b72c67f10950e8565e7922b10b605c0fdc0700d36f96d4c7c78f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)

    @builtins.property
    @jsii.member(jsii_name="taskRoleArn")
    def task_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "taskRoleArn"))

    @task_role_arn.setter
    def task_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a80b39c39de2a764d9eb95f52411d3bd6911c6023c248335e37d20311a915dae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "taskRoleArn", value)


@jsii.data_type(
    jsii_type="aws.ecsTaskDefinition.EcsTaskDefinitionConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "container_definitions": "containerDefinitions",
        "family": "family",
        "cpu": "cpu",
        "ephemeral_storage": "ephemeralStorage",
        "execution_role_arn": "executionRoleArn",
        "id": "id",
        "inference_accelerator": "inferenceAccelerator",
        "ipc_mode": "ipcMode",
        "memory": "memory",
        "network_mode": "networkMode",
        "pid_mode": "pidMode",
        "placement_constraints": "placementConstraints",
        "proxy_configuration": "proxyConfiguration",
        "requires_compatibilities": "requiresCompatibilities",
        "runtime_platform": "runtimePlatform",
        "skip_destroy": "skipDestroy",
        "tags": "tags",
        "tags_all": "tagsAll",
        "task_role_arn": "taskRoleArn",
        "volume": "volume",
    },
)
class EcsTaskDefinitionConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        container_definitions: builtins.str,
        family: builtins.str,
        cpu: typing.Optional[builtins.str] = None,
        ephemeral_storage: typing.Optional[typing.Union["EcsTaskDefinitionEphemeralStorage", typing.Dict[builtins.str, typing.Any]]] = None,
        execution_role_arn: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        inference_accelerator: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EcsTaskDefinitionInferenceAccelerator", typing.Dict[builtins.str, typing.Any]]]]] = None,
        ipc_mode: typing.Optional[builtins.str] = None,
        memory: typing.Optional[builtins.str] = None,
        network_mode: typing.Optional[builtins.str] = None,
        pid_mode: typing.Optional[builtins.str] = None,
        placement_constraints: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EcsTaskDefinitionPlacementConstraints", typing.Dict[builtins.str, typing.Any]]]]] = None,
        proxy_configuration: typing.Optional[typing.Union["EcsTaskDefinitionProxyConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        requires_compatibilities: typing.Optional[typing.Sequence[builtins.str]] = None,
        runtime_platform: typing.Optional[typing.Union["EcsTaskDefinitionRuntimePlatform", typing.Dict[builtins.str, typing.Any]]] = None,
        skip_destroy: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        task_role_arn: typing.Optional[builtins.str] = None,
        volume: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EcsTaskDefinitionVolume", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param container_definitions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#container_definitions EcsTaskDefinition#container_definitions}.
        :param family: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#family EcsTaskDefinition#family}.
        :param cpu: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#cpu EcsTaskDefinition#cpu}.
        :param ephemeral_storage: ephemeral_storage block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#ephemeral_storage EcsTaskDefinition#ephemeral_storage}
        :param execution_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#execution_role_arn EcsTaskDefinition#execution_role_arn}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#id EcsTaskDefinition#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param inference_accelerator: inference_accelerator block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#inference_accelerator EcsTaskDefinition#inference_accelerator}
        :param ipc_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#ipc_mode EcsTaskDefinition#ipc_mode}.
        :param memory: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#memory EcsTaskDefinition#memory}.
        :param network_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#network_mode EcsTaskDefinition#network_mode}.
        :param pid_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#pid_mode EcsTaskDefinition#pid_mode}.
        :param placement_constraints: placement_constraints block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#placement_constraints EcsTaskDefinition#placement_constraints}
        :param proxy_configuration: proxy_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#proxy_configuration EcsTaskDefinition#proxy_configuration}
        :param requires_compatibilities: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#requires_compatibilities EcsTaskDefinition#requires_compatibilities}.
        :param runtime_platform: runtime_platform block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#runtime_platform EcsTaskDefinition#runtime_platform}
        :param skip_destroy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#skip_destroy EcsTaskDefinition#skip_destroy}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#tags EcsTaskDefinition#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#tags_all EcsTaskDefinition#tags_all}.
        :param task_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#task_role_arn EcsTaskDefinition#task_role_arn}.
        :param volume: volume block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#volume EcsTaskDefinition#volume}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(ephemeral_storage, dict):
            ephemeral_storage = EcsTaskDefinitionEphemeralStorage(**ephemeral_storage)
        if isinstance(proxy_configuration, dict):
            proxy_configuration = EcsTaskDefinitionProxyConfiguration(**proxy_configuration)
        if isinstance(runtime_platform, dict):
            runtime_platform = EcsTaskDefinitionRuntimePlatform(**runtime_platform)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb9a8868b7c913445ec7d92f02324dcc239e4fd239e670d165f4b611f7cd14ae)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument container_definitions", value=container_definitions, expected_type=type_hints["container_definitions"])
            check_type(argname="argument family", value=family, expected_type=type_hints["family"])
            check_type(argname="argument cpu", value=cpu, expected_type=type_hints["cpu"])
            check_type(argname="argument ephemeral_storage", value=ephemeral_storage, expected_type=type_hints["ephemeral_storage"])
            check_type(argname="argument execution_role_arn", value=execution_role_arn, expected_type=type_hints["execution_role_arn"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument inference_accelerator", value=inference_accelerator, expected_type=type_hints["inference_accelerator"])
            check_type(argname="argument ipc_mode", value=ipc_mode, expected_type=type_hints["ipc_mode"])
            check_type(argname="argument memory", value=memory, expected_type=type_hints["memory"])
            check_type(argname="argument network_mode", value=network_mode, expected_type=type_hints["network_mode"])
            check_type(argname="argument pid_mode", value=pid_mode, expected_type=type_hints["pid_mode"])
            check_type(argname="argument placement_constraints", value=placement_constraints, expected_type=type_hints["placement_constraints"])
            check_type(argname="argument proxy_configuration", value=proxy_configuration, expected_type=type_hints["proxy_configuration"])
            check_type(argname="argument requires_compatibilities", value=requires_compatibilities, expected_type=type_hints["requires_compatibilities"])
            check_type(argname="argument runtime_platform", value=runtime_platform, expected_type=type_hints["runtime_platform"])
            check_type(argname="argument skip_destroy", value=skip_destroy, expected_type=type_hints["skip_destroy"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument task_role_arn", value=task_role_arn, expected_type=type_hints["task_role_arn"])
            check_type(argname="argument volume", value=volume, expected_type=type_hints["volume"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "container_definitions": container_definitions,
            "family": family,
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
        if cpu is not None:
            self._values["cpu"] = cpu
        if ephemeral_storage is not None:
            self._values["ephemeral_storage"] = ephemeral_storage
        if execution_role_arn is not None:
            self._values["execution_role_arn"] = execution_role_arn
        if id is not None:
            self._values["id"] = id
        if inference_accelerator is not None:
            self._values["inference_accelerator"] = inference_accelerator
        if ipc_mode is not None:
            self._values["ipc_mode"] = ipc_mode
        if memory is not None:
            self._values["memory"] = memory
        if network_mode is not None:
            self._values["network_mode"] = network_mode
        if pid_mode is not None:
            self._values["pid_mode"] = pid_mode
        if placement_constraints is not None:
            self._values["placement_constraints"] = placement_constraints
        if proxy_configuration is not None:
            self._values["proxy_configuration"] = proxy_configuration
        if requires_compatibilities is not None:
            self._values["requires_compatibilities"] = requires_compatibilities
        if runtime_platform is not None:
            self._values["runtime_platform"] = runtime_platform
        if skip_destroy is not None:
            self._values["skip_destroy"] = skip_destroy
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if task_role_arn is not None:
            self._values["task_role_arn"] = task_role_arn
        if volume is not None:
            self._values["volume"] = volume

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
    def container_definitions(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#container_definitions EcsTaskDefinition#container_definitions}.'''
        result = self._values.get("container_definitions")
        assert result is not None, "Required property 'container_definitions' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def family(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#family EcsTaskDefinition#family}.'''
        result = self._values.get("family")
        assert result is not None, "Required property 'family' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cpu(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#cpu EcsTaskDefinition#cpu}.'''
        result = self._values.get("cpu")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ephemeral_storage(self) -> typing.Optional["EcsTaskDefinitionEphemeralStorage"]:
        '''ephemeral_storage block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#ephemeral_storage EcsTaskDefinition#ephemeral_storage}
        '''
        result = self._values.get("ephemeral_storage")
        return typing.cast(typing.Optional["EcsTaskDefinitionEphemeralStorage"], result)

    @builtins.property
    def execution_role_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#execution_role_arn EcsTaskDefinition#execution_role_arn}.'''
        result = self._values.get("execution_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#id EcsTaskDefinition#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def inference_accelerator(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EcsTaskDefinitionInferenceAccelerator"]]]:
        '''inference_accelerator block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#inference_accelerator EcsTaskDefinition#inference_accelerator}
        '''
        result = self._values.get("inference_accelerator")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EcsTaskDefinitionInferenceAccelerator"]]], result)

    @builtins.property
    def ipc_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#ipc_mode EcsTaskDefinition#ipc_mode}.'''
        result = self._values.get("ipc_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def memory(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#memory EcsTaskDefinition#memory}.'''
        result = self._values.get("memory")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def network_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#network_mode EcsTaskDefinition#network_mode}.'''
        result = self._values.get("network_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pid_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#pid_mode EcsTaskDefinition#pid_mode}.'''
        result = self._values.get("pid_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def placement_constraints(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EcsTaskDefinitionPlacementConstraints"]]]:
        '''placement_constraints block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#placement_constraints EcsTaskDefinition#placement_constraints}
        '''
        result = self._values.get("placement_constraints")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EcsTaskDefinitionPlacementConstraints"]]], result)

    @builtins.property
    def proxy_configuration(
        self,
    ) -> typing.Optional["EcsTaskDefinitionProxyConfiguration"]:
        '''proxy_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#proxy_configuration EcsTaskDefinition#proxy_configuration}
        '''
        result = self._values.get("proxy_configuration")
        return typing.cast(typing.Optional["EcsTaskDefinitionProxyConfiguration"], result)

    @builtins.property
    def requires_compatibilities(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#requires_compatibilities EcsTaskDefinition#requires_compatibilities}.'''
        result = self._values.get("requires_compatibilities")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def runtime_platform(self) -> typing.Optional["EcsTaskDefinitionRuntimePlatform"]:
        '''runtime_platform block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#runtime_platform EcsTaskDefinition#runtime_platform}
        '''
        result = self._values.get("runtime_platform")
        return typing.cast(typing.Optional["EcsTaskDefinitionRuntimePlatform"], result)

    @builtins.property
    def skip_destroy(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#skip_destroy EcsTaskDefinition#skip_destroy}.'''
        result = self._values.get("skip_destroy")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#tags EcsTaskDefinition#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#tags_all EcsTaskDefinition#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def task_role_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#task_role_arn EcsTaskDefinition#task_role_arn}.'''
        result = self._values.get("task_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def volume(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EcsTaskDefinitionVolume"]]]:
        '''volume block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#volume EcsTaskDefinition#volume}
        '''
        result = self._values.get("volume")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EcsTaskDefinitionVolume"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsTaskDefinitionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.ecsTaskDefinition.EcsTaskDefinitionEphemeralStorage",
    jsii_struct_bases=[],
    name_mapping={"size_in_gib": "sizeInGib"},
)
class EcsTaskDefinitionEphemeralStorage:
    def __init__(self, *, size_in_gib: jsii.Number) -> None:
        '''
        :param size_in_gib: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#size_in_gib EcsTaskDefinition#size_in_gib}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__064708fb17376a2811c0cc07a5f82be4c58c5492f43b2d4c225726bf5abf3cd3)
            check_type(argname="argument size_in_gib", value=size_in_gib, expected_type=type_hints["size_in_gib"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "size_in_gib": size_in_gib,
        }

    @builtins.property
    def size_in_gib(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#size_in_gib EcsTaskDefinition#size_in_gib}.'''
        result = self._values.get("size_in_gib")
        assert result is not None, "Required property 'size_in_gib' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsTaskDefinitionEphemeralStorage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcsTaskDefinitionEphemeralStorageOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ecsTaskDefinition.EcsTaskDefinitionEphemeralStorageOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5538fed11f302544fc1b9fde03004b79d1ea0fd4305876a4af12bc3d180f301f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="sizeInGibInput")
    def size_in_gib_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sizeInGibInput"))

    @builtins.property
    @jsii.member(jsii_name="sizeInGib")
    def size_in_gib(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "sizeInGib"))

    @size_in_gib.setter
    def size_in_gib(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9062481e05a86913a0524745ea65d4f223a6089e2037833cbd4eae29ded455b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sizeInGib", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[EcsTaskDefinitionEphemeralStorage]:
        return typing.cast(typing.Optional[EcsTaskDefinitionEphemeralStorage], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EcsTaskDefinitionEphemeralStorage],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec70883e15f99beb9777fc075be7b6c13d142e0bf8b9bf7c4fa286a2dd4e984b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ecsTaskDefinition.EcsTaskDefinitionInferenceAccelerator",
    jsii_struct_bases=[],
    name_mapping={"device_name": "deviceName", "device_type": "deviceType"},
)
class EcsTaskDefinitionInferenceAccelerator:
    def __init__(self, *, device_name: builtins.str, device_type: builtins.str) -> None:
        '''
        :param device_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#device_name EcsTaskDefinition#device_name}.
        :param device_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#device_type EcsTaskDefinition#device_type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__736187d21a344322b15fc043fc46447c2a795e472f859b8eeddc2d9ebe4d9b0b)
            check_type(argname="argument device_name", value=device_name, expected_type=type_hints["device_name"])
            check_type(argname="argument device_type", value=device_type, expected_type=type_hints["device_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "device_name": device_name,
            "device_type": device_type,
        }

    @builtins.property
    def device_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#device_name EcsTaskDefinition#device_name}.'''
        result = self._values.get("device_name")
        assert result is not None, "Required property 'device_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def device_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#device_type EcsTaskDefinition#device_type}.'''
        result = self._values.get("device_type")
        assert result is not None, "Required property 'device_type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsTaskDefinitionInferenceAccelerator(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcsTaskDefinitionInferenceAcceleratorList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ecsTaskDefinition.EcsTaskDefinitionInferenceAcceleratorList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__907aabb6f1c407809006e01cde014edceb8dc7b604451ea2fbee95003b95d44a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EcsTaskDefinitionInferenceAcceleratorOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd25861542c7c5e497c8fb7cd32acd34ba5db8a8c66beae6badeb288a87adca6)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EcsTaskDefinitionInferenceAcceleratorOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2cc28ee5b25a2e31963dfb66bc992ef00c75745ae21711d31d9bec173ac5df12)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4dd46ae81e5b48c9a5c1b5efa8c97d1b56faeddfe8ef23aaf22c6b7a5997dc84)
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
            type_hints = typing.get_type_hints(_typecheckingstub__312e72ac3059e4a8ab51a54946bbf6e1d6bbfd2dad7f84b7891c6ef87dc4f4c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EcsTaskDefinitionInferenceAccelerator]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EcsTaskDefinitionInferenceAccelerator]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EcsTaskDefinitionInferenceAccelerator]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c10416adbeb558b69340289387518d0529923dd875f1cbe1c0988dc6bd718dc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EcsTaskDefinitionInferenceAcceleratorOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ecsTaskDefinition.EcsTaskDefinitionInferenceAcceleratorOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__fbe46c94389b942edc148025126a82988304a9d2c5b004a584245996c886b913)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="deviceNameInput")
    def device_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deviceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="deviceTypeInput")
    def device_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deviceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="deviceName")
    def device_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deviceName"))

    @device_name.setter
    def device_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4555972c3ce0f039038520e945daf6a4f06bfd4f73240a08079590e5c6a0675)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deviceName", value)

    @builtins.property
    @jsii.member(jsii_name="deviceType")
    def device_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deviceType"))

    @device_type.setter
    def device_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04c772b99cd3a1b4c83ff8df361db9ef857d10609da4d40322b07af99bfb0720)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deviceType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EcsTaskDefinitionInferenceAccelerator, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EcsTaskDefinitionInferenceAccelerator, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EcsTaskDefinitionInferenceAccelerator, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__442f84f7f8c25a2ac37491442ad5ad0dfefd31717988484861f2908c99f382eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ecsTaskDefinition.EcsTaskDefinitionPlacementConstraints",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "expression": "expression"},
)
class EcsTaskDefinitionPlacementConstraints:
    def __init__(
        self,
        *,
        type: builtins.str,
        expression: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#type EcsTaskDefinition#type}.
        :param expression: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#expression EcsTaskDefinition#expression}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2302d092b4ea185e50e736db0151e65d4c12db59ccb1207c4383824a9c2dec06)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument expression", value=expression, expected_type=type_hints["expression"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }
        if expression is not None:
            self._values["expression"] = expression

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#type EcsTaskDefinition#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def expression(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#expression EcsTaskDefinition#expression}.'''
        result = self._values.get("expression")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsTaskDefinitionPlacementConstraints(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcsTaskDefinitionPlacementConstraintsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ecsTaskDefinition.EcsTaskDefinitionPlacementConstraintsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b66ab5321037e2e5e67e89f92d34e85cd52f5ed6fd67ba174e5ef8988a69ca5b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EcsTaskDefinitionPlacementConstraintsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a3f84a6ae8a6600ce7cd7e179d98af515f4f2a3768d9da9692273a597d59668c)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EcsTaskDefinitionPlacementConstraintsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e211eef5d826966e5175496afc1c872f5acc379af483c5840e06edac4970bd9d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__06b9273f1d6a131210b165d0553bad4139a8a369b89a62f766bcab3701099d8a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__15f3b2a9530b222893b0ff83aaaa565168dd3071499c7fdaa7ec454a8d4a10c4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EcsTaskDefinitionPlacementConstraints]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EcsTaskDefinitionPlacementConstraints]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EcsTaskDefinitionPlacementConstraints]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ebe69553b8385f05f486e5943250dd8a50f405bc7fe89b18ab171e94183a0561)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EcsTaskDefinitionPlacementConstraintsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ecsTaskDefinition.EcsTaskDefinitionPlacementConstraintsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__272adf4cd09b6a0685daaf2d29de908159ff3dc1d448531edfe94d379cd045f3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetExpression")
    def reset_expression(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExpression", []))

    @builtins.property
    @jsii.member(jsii_name="expressionInput")
    def expression_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "expressionInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="expression")
    def expression(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expression"))

    @expression.setter
    def expression(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__10bbdea7d95f7cad8b75719fde3cdf5e66cc6d593c8b1eab073d5730538d5279)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expression", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__526e4c7ac3243d1b0f96bbb76a7c0ed8d0ad73dda50bdb5838091d0e3de6c57b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EcsTaskDefinitionPlacementConstraints, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EcsTaskDefinitionPlacementConstraints, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EcsTaskDefinitionPlacementConstraints, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1c7e09956f0dfcf3558000cb992fefbd6533c8ca80a3ab1c9ef3bc5999c7957)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ecsTaskDefinition.EcsTaskDefinitionProxyConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "container_name": "containerName",
        "properties": "properties",
        "type": "type",
    },
)
class EcsTaskDefinitionProxyConfiguration:
    def __init__(
        self,
        *,
        container_name: builtins.str,
        properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param container_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#container_name EcsTaskDefinition#container_name}.
        :param properties: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#properties EcsTaskDefinition#properties}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#type EcsTaskDefinition#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39b1804ea7cbfc992c0f8e62dc7e885ef525afdb1efd99f1e6c75e84114b3f8a)
            check_type(argname="argument container_name", value=container_name, expected_type=type_hints["container_name"])
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "container_name": container_name,
        }
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def container_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#container_name EcsTaskDefinition#container_name}.'''
        result = self._values.get("container_name")
        assert result is not None, "Required property 'container_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def properties(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#properties EcsTaskDefinition#properties}.'''
        result = self._values.get("properties")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#type EcsTaskDefinition#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsTaskDefinitionProxyConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcsTaskDefinitionProxyConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ecsTaskDefinition.EcsTaskDefinitionProxyConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a2d469977be56e37e9677900b57169552965c8c1f7738eed25c355e2d20d93cb)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetProperties")
    def reset_properties(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProperties", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="containerNameInput")
    def container_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "containerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="propertiesInput")
    def properties_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "propertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="containerName")
    def container_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "containerName"))

    @container_name.setter
    def container_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__870fb12b7b1c60be8750cdb9dbb7e4560474b319a9a58923d846706bfffe5db4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerName", value)

    @builtins.property
    @jsii.member(jsii_name="properties")
    def properties(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "properties"))

    @properties.setter
    def properties(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__302504045eb37b094cc4756199c8cc4bb89cdcd7d2d2cb075d1340c2557b7622)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "properties", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d28c0141922254ac451af544cc6840a791a9beaf9304eba3c159c4ff0a12f75)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[EcsTaskDefinitionProxyConfiguration]:
        return typing.cast(typing.Optional[EcsTaskDefinitionProxyConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EcsTaskDefinitionProxyConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3639143af886e471359bd250d4398b340b1ef9c109a1d844e8ad6542834ba6e1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ecsTaskDefinition.EcsTaskDefinitionRuntimePlatform",
    jsii_struct_bases=[],
    name_mapping={
        "cpu_architecture": "cpuArchitecture",
        "operating_system_family": "operatingSystemFamily",
    },
)
class EcsTaskDefinitionRuntimePlatform:
    def __init__(
        self,
        *,
        cpu_architecture: typing.Optional[builtins.str] = None,
        operating_system_family: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cpu_architecture: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#cpu_architecture EcsTaskDefinition#cpu_architecture}.
        :param operating_system_family: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#operating_system_family EcsTaskDefinition#operating_system_family}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb1e8219dce015820bd51945cc253647107fafd9900750311456b0e2ebe67eb5)
            check_type(argname="argument cpu_architecture", value=cpu_architecture, expected_type=type_hints["cpu_architecture"])
            check_type(argname="argument operating_system_family", value=operating_system_family, expected_type=type_hints["operating_system_family"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if cpu_architecture is not None:
            self._values["cpu_architecture"] = cpu_architecture
        if operating_system_family is not None:
            self._values["operating_system_family"] = operating_system_family

    @builtins.property
    def cpu_architecture(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#cpu_architecture EcsTaskDefinition#cpu_architecture}.'''
        result = self._values.get("cpu_architecture")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def operating_system_family(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#operating_system_family EcsTaskDefinition#operating_system_family}.'''
        result = self._values.get("operating_system_family")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsTaskDefinitionRuntimePlatform(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcsTaskDefinitionRuntimePlatformOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ecsTaskDefinition.EcsTaskDefinitionRuntimePlatformOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6b5b270e0f730ebdaa8516849860aa44025e9a5626a9913c4e783ac5885ddb4f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCpuArchitecture")
    def reset_cpu_architecture(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCpuArchitecture", []))

    @jsii.member(jsii_name="resetOperatingSystemFamily")
    def reset_operating_system_family(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOperatingSystemFamily", []))

    @builtins.property
    @jsii.member(jsii_name="cpuArchitectureInput")
    def cpu_architecture_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cpuArchitectureInput"))

    @builtins.property
    @jsii.member(jsii_name="operatingSystemFamilyInput")
    def operating_system_family_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatingSystemFamilyInput"))

    @builtins.property
    @jsii.member(jsii_name="cpuArchitecture")
    def cpu_architecture(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cpuArchitecture"))

    @cpu_architecture.setter
    def cpu_architecture(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f51a5453337d1bab44c6f7693f3bf995e0dad3d71b7cacf3f0d2098199e36a70)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpuArchitecture", value)

    @builtins.property
    @jsii.member(jsii_name="operatingSystemFamily")
    def operating_system_family(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operatingSystemFamily"))

    @operating_system_family.setter
    def operating_system_family(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf8473788179556b43a0e59d0bff18ebfd03ff73c85350b90553cf43cd9e9cdf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operatingSystemFamily", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[EcsTaskDefinitionRuntimePlatform]:
        return typing.cast(typing.Optional[EcsTaskDefinitionRuntimePlatform], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EcsTaskDefinitionRuntimePlatform],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b92c600ccf6bd1cc67f0b141cee72ca5ae83c76d259a768d6de69b6f7b3048c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ecsTaskDefinition.EcsTaskDefinitionVolume",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "docker_volume_configuration": "dockerVolumeConfiguration",
        "efs_volume_configuration": "efsVolumeConfiguration",
        "fsx_windows_file_server_volume_configuration": "fsxWindowsFileServerVolumeConfiguration",
        "host_path": "hostPath",
    },
)
class EcsTaskDefinitionVolume:
    def __init__(
        self,
        *,
        name: builtins.str,
        docker_volume_configuration: typing.Optional[typing.Union["EcsTaskDefinitionVolumeDockerVolumeConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        efs_volume_configuration: typing.Optional[typing.Union["EcsTaskDefinitionVolumeEfsVolumeConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        fsx_windows_file_server_volume_configuration: typing.Optional[typing.Union["EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        host_path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#name EcsTaskDefinition#name}.
        :param docker_volume_configuration: docker_volume_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#docker_volume_configuration EcsTaskDefinition#docker_volume_configuration}
        :param efs_volume_configuration: efs_volume_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#efs_volume_configuration EcsTaskDefinition#efs_volume_configuration}
        :param fsx_windows_file_server_volume_configuration: fsx_windows_file_server_volume_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#fsx_windows_file_server_volume_configuration EcsTaskDefinition#fsx_windows_file_server_volume_configuration}
        :param host_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#host_path EcsTaskDefinition#host_path}.
        '''
        if isinstance(docker_volume_configuration, dict):
            docker_volume_configuration = EcsTaskDefinitionVolumeDockerVolumeConfiguration(**docker_volume_configuration)
        if isinstance(efs_volume_configuration, dict):
            efs_volume_configuration = EcsTaskDefinitionVolumeEfsVolumeConfiguration(**efs_volume_configuration)
        if isinstance(fsx_windows_file_server_volume_configuration, dict):
            fsx_windows_file_server_volume_configuration = EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfiguration(**fsx_windows_file_server_volume_configuration)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4aef0b4c058f156eb9ad1a50b5ba1371842b8849a68d50b7e6c66ec2f7711c41)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument docker_volume_configuration", value=docker_volume_configuration, expected_type=type_hints["docker_volume_configuration"])
            check_type(argname="argument efs_volume_configuration", value=efs_volume_configuration, expected_type=type_hints["efs_volume_configuration"])
            check_type(argname="argument fsx_windows_file_server_volume_configuration", value=fsx_windows_file_server_volume_configuration, expected_type=type_hints["fsx_windows_file_server_volume_configuration"])
            check_type(argname="argument host_path", value=host_path, expected_type=type_hints["host_path"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if docker_volume_configuration is not None:
            self._values["docker_volume_configuration"] = docker_volume_configuration
        if efs_volume_configuration is not None:
            self._values["efs_volume_configuration"] = efs_volume_configuration
        if fsx_windows_file_server_volume_configuration is not None:
            self._values["fsx_windows_file_server_volume_configuration"] = fsx_windows_file_server_volume_configuration
        if host_path is not None:
            self._values["host_path"] = host_path

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#name EcsTaskDefinition#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def docker_volume_configuration(
        self,
    ) -> typing.Optional["EcsTaskDefinitionVolumeDockerVolumeConfiguration"]:
        '''docker_volume_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#docker_volume_configuration EcsTaskDefinition#docker_volume_configuration}
        '''
        result = self._values.get("docker_volume_configuration")
        return typing.cast(typing.Optional["EcsTaskDefinitionVolumeDockerVolumeConfiguration"], result)

    @builtins.property
    def efs_volume_configuration(
        self,
    ) -> typing.Optional["EcsTaskDefinitionVolumeEfsVolumeConfiguration"]:
        '''efs_volume_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#efs_volume_configuration EcsTaskDefinition#efs_volume_configuration}
        '''
        result = self._values.get("efs_volume_configuration")
        return typing.cast(typing.Optional["EcsTaskDefinitionVolumeEfsVolumeConfiguration"], result)

    @builtins.property
    def fsx_windows_file_server_volume_configuration(
        self,
    ) -> typing.Optional["EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfiguration"]:
        '''fsx_windows_file_server_volume_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#fsx_windows_file_server_volume_configuration EcsTaskDefinition#fsx_windows_file_server_volume_configuration}
        '''
        result = self._values.get("fsx_windows_file_server_volume_configuration")
        return typing.cast(typing.Optional["EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfiguration"], result)

    @builtins.property
    def host_path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#host_path EcsTaskDefinition#host_path}.'''
        result = self._values.get("host_path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsTaskDefinitionVolume(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.ecsTaskDefinition.EcsTaskDefinitionVolumeDockerVolumeConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "autoprovision": "autoprovision",
        "driver": "driver",
        "driver_opts": "driverOpts",
        "labels": "labels",
        "scope": "scope",
    },
)
class EcsTaskDefinitionVolumeDockerVolumeConfiguration:
    def __init__(
        self,
        *,
        autoprovision: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        driver: typing.Optional[builtins.str] = None,
        driver_opts: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        scope: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param autoprovision: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#autoprovision EcsTaskDefinition#autoprovision}.
        :param driver: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#driver EcsTaskDefinition#driver}.
        :param driver_opts: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#driver_opts EcsTaskDefinition#driver_opts}.
        :param labels: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#labels EcsTaskDefinition#labels}.
        :param scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#scope EcsTaskDefinition#scope}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38db6082bee444ddf6c6a27543c4b3492a5fe2b224605fdf106056ddf21ca102)
            check_type(argname="argument autoprovision", value=autoprovision, expected_type=type_hints["autoprovision"])
            check_type(argname="argument driver", value=driver, expected_type=type_hints["driver"])
            check_type(argname="argument driver_opts", value=driver_opts, expected_type=type_hints["driver_opts"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if autoprovision is not None:
            self._values["autoprovision"] = autoprovision
        if driver is not None:
            self._values["driver"] = driver
        if driver_opts is not None:
            self._values["driver_opts"] = driver_opts
        if labels is not None:
            self._values["labels"] = labels
        if scope is not None:
            self._values["scope"] = scope

    @builtins.property
    def autoprovision(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#autoprovision EcsTaskDefinition#autoprovision}.'''
        result = self._values.get("autoprovision")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def driver(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#driver EcsTaskDefinition#driver}.'''
        result = self._values.get("driver")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def driver_opts(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#driver_opts EcsTaskDefinition#driver_opts}.'''
        result = self._values.get("driver_opts")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#labels EcsTaskDefinition#labels}.'''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def scope(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#scope EcsTaskDefinition#scope}.'''
        result = self._values.get("scope")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsTaskDefinitionVolumeDockerVolumeConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcsTaskDefinitionVolumeDockerVolumeConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ecsTaskDefinition.EcsTaskDefinitionVolumeDockerVolumeConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__58dbe50fbef94eeb6272c1017109c2f529f1be2b9603f93d200eb169e03a7dc7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAutoprovision")
    def reset_autoprovision(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoprovision", []))

    @jsii.member(jsii_name="resetDriver")
    def reset_driver(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDriver", []))

    @jsii.member(jsii_name="resetDriverOpts")
    def reset_driver_opts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDriverOpts", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetScope")
    def reset_scope(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScope", []))

    @builtins.property
    @jsii.member(jsii_name="autoprovisionInput")
    def autoprovision_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "autoprovisionInput"))

    @builtins.property
    @jsii.member(jsii_name="driverInput")
    def driver_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "driverInput"))

    @builtins.property
    @jsii.member(jsii_name="driverOptsInput")
    def driver_opts_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "driverOptsInput"))

    @builtins.property
    @jsii.member(jsii_name="labelsInput")
    def labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "labelsInput"))

    @builtins.property
    @jsii.member(jsii_name="scopeInput")
    def scope_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scopeInput"))

    @builtins.property
    @jsii.member(jsii_name="autoprovision")
    def autoprovision(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "autoprovision"))

    @autoprovision.setter
    def autoprovision(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08c084954d6f901487aec159286a0133af132bac3f478c3cf5ce219af9909ff2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoprovision", value)

    @builtins.property
    @jsii.member(jsii_name="driver")
    def driver(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "driver"))

    @driver.setter
    def driver(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58596a54a21ce5473be4d837acbb5456a35c73b09e440b694d64b6101a002bc8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "driver", value)

    @builtins.property
    @jsii.member(jsii_name="driverOpts")
    def driver_opts(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "driverOpts"))

    @driver_opts.setter
    def driver_opts(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99c5fd46bd8c31c468efb81734af349142ff2ab4e6391c90a47b884936f534f0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "driverOpts", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f5e577ebd734a99d62449ff32b523e7dd1871e7d89b1a5b69425c01106f1748)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="scope")
    def scope(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scope"))

    @scope.setter
    def scope(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53e8ebee2c6a90c09db84d06ed3b82f832ba1f7ca5bf20b9cc1ee56f2ac02a50)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scope", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[EcsTaskDefinitionVolumeDockerVolumeConfiguration]:
        return typing.cast(typing.Optional[EcsTaskDefinitionVolumeDockerVolumeConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EcsTaskDefinitionVolumeDockerVolumeConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6794ccc8d4e9a0050ad8512672882f8057c729786d29648fedfdec3e897cf4f2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ecsTaskDefinition.EcsTaskDefinitionVolumeEfsVolumeConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "file_system_id": "fileSystemId",
        "authorization_config": "authorizationConfig",
        "root_directory": "rootDirectory",
        "transit_encryption": "transitEncryption",
        "transit_encryption_port": "transitEncryptionPort",
    },
)
class EcsTaskDefinitionVolumeEfsVolumeConfiguration:
    def __init__(
        self,
        *,
        file_system_id: builtins.str,
        authorization_config: typing.Optional[typing.Union["EcsTaskDefinitionVolumeEfsVolumeConfigurationAuthorizationConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        root_directory: typing.Optional[builtins.str] = None,
        transit_encryption: typing.Optional[builtins.str] = None,
        transit_encryption_port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param file_system_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#file_system_id EcsTaskDefinition#file_system_id}.
        :param authorization_config: authorization_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#authorization_config EcsTaskDefinition#authorization_config}
        :param root_directory: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#root_directory EcsTaskDefinition#root_directory}.
        :param transit_encryption: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#transit_encryption EcsTaskDefinition#transit_encryption}.
        :param transit_encryption_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#transit_encryption_port EcsTaskDefinition#transit_encryption_port}.
        '''
        if isinstance(authorization_config, dict):
            authorization_config = EcsTaskDefinitionVolumeEfsVolumeConfigurationAuthorizationConfig(**authorization_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2943c8937c0a5d6157f3ade05e59f0ace48405431919cf6bbf266b65c7d99123)
            check_type(argname="argument file_system_id", value=file_system_id, expected_type=type_hints["file_system_id"])
            check_type(argname="argument authorization_config", value=authorization_config, expected_type=type_hints["authorization_config"])
            check_type(argname="argument root_directory", value=root_directory, expected_type=type_hints["root_directory"])
            check_type(argname="argument transit_encryption", value=transit_encryption, expected_type=type_hints["transit_encryption"])
            check_type(argname="argument transit_encryption_port", value=transit_encryption_port, expected_type=type_hints["transit_encryption_port"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "file_system_id": file_system_id,
        }
        if authorization_config is not None:
            self._values["authorization_config"] = authorization_config
        if root_directory is not None:
            self._values["root_directory"] = root_directory
        if transit_encryption is not None:
            self._values["transit_encryption"] = transit_encryption
        if transit_encryption_port is not None:
            self._values["transit_encryption_port"] = transit_encryption_port

    @builtins.property
    def file_system_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#file_system_id EcsTaskDefinition#file_system_id}.'''
        result = self._values.get("file_system_id")
        assert result is not None, "Required property 'file_system_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def authorization_config(
        self,
    ) -> typing.Optional["EcsTaskDefinitionVolumeEfsVolumeConfigurationAuthorizationConfig"]:
        '''authorization_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#authorization_config EcsTaskDefinition#authorization_config}
        '''
        result = self._values.get("authorization_config")
        return typing.cast(typing.Optional["EcsTaskDefinitionVolumeEfsVolumeConfigurationAuthorizationConfig"], result)

    @builtins.property
    def root_directory(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#root_directory EcsTaskDefinition#root_directory}.'''
        result = self._values.get("root_directory")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def transit_encryption(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#transit_encryption EcsTaskDefinition#transit_encryption}.'''
        result = self._values.get("transit_encryption")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def transit_encryption_port(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#transit_encryption_port EcsTaskDefinition#transit_encryption_port}.'''
        result = self._values.get("transit_encryption_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsTaskDefinitionVolumeEfsVolumeConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.ecsTaskDefinition.EcsTaskDefinitionVolumeEfsVolumeConfigurationAuthorizationConfig",
    jsii_struct_bases=[],
    name_mapping={"access_point_id": "accessPointId", "iam": "iam"},
)
class EcsTaskDefinitionVolumeEfsVolumeConfigurationAuthorizationConfig:
    def __init__(
        self,
        *,
        access_point_id: typing.Optional[builtins.str] = None,
        iam: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param access_point_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#access_point_id EcsTaskDefinition#access_point_id}.
        :param iam: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#iam EcsTaskDefinition#iam}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13560d1075ab6cc0d57dcc15a85543590f66b7ba282917a17483f91b319373fd)
            check_type(argname="argument access_point_id", value=access_point_id, expected_type=type_hints["access_point_id"])
            check_type(argname="argument iam", value=iam, expected_type=type_hints["iam"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if access_point_id is not None:
            self._values["access_point_id"] = access_point_id
        if iam is not None:
            self._values["iam"] = iam

    @builtins.property
    def access_point_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#access_point_id EcsTaskDefinition#access_point_id}.'''
        result = self._values.get("access_point_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def iam(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#iam EcsTaskDefinition#iam}.'''
        result = self._values.get("iam")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsTaskDefinitionVolumeEfsVolumeConfigurationAuthorizationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcsTaskDefinitionVolumeEfsVolumeConfigurationAuthorizationConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ecsTaskDefinition.EcsTaskDefinitionVolumeEfsVolumeConfigurationAuthorizationConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__fe9de39dde71d3a237ef1791c505823a4b3f3f24f60b3f4294459a62b0adc5c5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAccessPointId")
    def reset_access_point_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessPointId", []))

    @jsii.member(jsii_name="resetIam")
    def reset_iam(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIam", []))

    @builtins.property
    @jsii.member(jsii_name="accessPointIdInput")
    def access_point_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessPointIdInput"))

    @builtins.property
    @jsii.member(jsii_name="iamInput")
    def iam_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "iamInput"))

    @builtins.property
    @jsii.member(jsii_name="accessPointId")
    def access_point_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessPointId"))

    @access_point_id.setter
    def access_point_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0f77ddf33560342dff065e9ad97e7c67b1b1d106ec44ca6139c99c3ffcb32a3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessPointId", value)

    @builtins.property
    @jsii.member(jsii_name="iam")
    def iam(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "iam"))

    @iam.setter
    def iam(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac4820624f633d507dc55fbe1e70f4ca580f27530b60e2ca46f292c3eb6166b2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iam", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[EcsTaskDefinitionVolumeEfsVolumeConfigurationAuthorizationConfig]:
        return typing.cast(typing.Optional[EcsTaskDefinitionVolumeEfsVolumeConfigurationAuthorizationConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EcsTaskDefinitionVolumeEfsVolumeConfigurationAuthorizationConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84765addaeab23b081f8b2cfdbc8759a9ab72f6ba3e8bbb0d78e4249d4c69d9a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EcsTaskDefinitionVolumeEfsVolumeConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ecsTaskDefinition.EcsTaskDefinitionVolumeEfsVolumeConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f215de1d78054b91a0243f964441a285bc35a6dbefa39f05cb0c57a64ae04642)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAuthorizationConfig")
    def put_authorization_config(
        self,
        *,
        access_point_id: typing.Optional[builtins.str] = None,
        iam: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param access_point_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#access_point_id EcsTaskDefinition#access_point_id}.
        :param iam: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#iam EcsTaskDefinition#iam}.
        '''
        value = EcsTaskDefinitionVolumeEfsVolumeConfigurationAuthorizationConfig(
            access_point_id=access_point_id, iam=iam
        )

        return typing.cast(None, jsii.invoke(self, "putAuthorizationConfig", [value]))

    @jsii.member(jsii_name="resetAuthorizationConfig")
    def reset_authorization_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthorizationConfig", []))

    @jsii.member(jsii_name="resetRootDirectory")
    def reset_root_directory(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRootDirectory", []))

    @jsii.member(jsii_name="resetTransitEncryption")
    def reset_transit_encryption(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTransitEncryption", []))

    @jsii.member(jsii_name="resetTransitEncryptionPort")
    def reset_transit_encryption_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTransitEncryptionPort", []))

    @builtins.property
    @jsii.member(jsii_name="authorizationConfig")
    def authorization_config(
        self,
    ) -> EcsTaskDefinitionVolumeEfsVolumeConfigurationAuthorizationConfigOutputReference:
        return typing.cast(EcsTaskDefinitionVolumeEfsVolumeConfigurationAuthorizationConfigOutputReference, jsii.get(self, "authorizationConfig"))

    @builtins.property
    @jsii.member(jsii_name="authorizationConfigInput")
    def authorization_config_input(
        self,
    ) -> typing.Optional[EcsTaskDefinitionVolumeEfsVolumeConfigurationAuthorizationConfig]:
        return typing.cast(typing.Optional[EcsTaskDefinitionVolumeEfsVolumeConfigurationAuthorizationConfig], jsii.get(self, "authorizationConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="fileSystemIdInput")
    def file_system_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fileSystemIdInput"))

    @builtins.property
    @jsii.member(jsii_name="rootDirectoryInput")
    def root_directory_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rootDirectoryInput"))

    @builtins.property
    @jsii.member(jsii_name="transitEncryptionInput")
    def transit_encryption_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "transitEncryptionInput"))

    @builtins.property
    @jsii.member(jsii_name="transitEncryptionPortInput")
    def transit_encryption_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "transitEncryptionPortInput"))

    @builtins.property
    @jsii.member(jsii_name="fileSystemId")
    def file_system_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fileSystemId"))

    @file_system_id.setter
    def file_system_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9df258d47c5ff98aa38bcb43c5676609a2290f6f768134fa3e81c7965c1674d5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileSystemId", value)

    @builtins.property
    @jsii.member(jsii_name="rootDirectory")
    def root_directory(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rootDirectory"))

    @root_directory.setter
    def root_directory(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70fa3daae9a741b5862086a4121dbf574a569ae60dad7f5830f53b5d8c9df94b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rootDirectory", value)

    @builtins.property
    @jsii.member(jsii_name="transitEncryption")
    def transit_encryption(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "transitEncryption"))

    @transit_encryption.setter
    def transit_encryption(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a3d2645866839b7535952d9b60650a325c699eb488b9b9d11c484bf12c8d5cd7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "transitEncryption", value)

    @builtins.property
    @jsii.member(jsii_name="transitEncryptionPort")
    def transit_encryption_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "transitEncryptionPort"))

    @transit_encryption_port.setter
    def transit_encryption_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79c5e9663946a5e9a2d108f58fa8f5e2cf3303c32db56c389ba19c4dfc77bd09)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "transitEncryptionPort", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[EcsTaskDefinitionVolumeEfsVolumeConfiguration]:
        return typing.cast(typing.Optional[EcsTaskDefinitionVolumeEfsVolumeConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EcsTaskDefinitionVolumeEfsVolumeConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e0ea0ff987cc2a6d35409fde03b807c4dde2f1bdaf24b9782f99977088d90a37)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ecsTaskDefinition.EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "authorization_config": "authorizationConfig",
        "file_system_id": "fileSystemId",
        "root_directory": "rootDirectory",
    },
)
class EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfiguration:
    def __init__(
        self,
        *,
        authorization_config: typing.Union["EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationAuthorizationConfig", typing.Dict[builtins.str, typing.Any]],
        file_system_id: builtins.str,
        root_directory: builtins.str,
    ) -> None:
        '''
        :param authorization_config: authorization_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#authorization_config EcsTaskDefinition#authorization_config}
        :param file_system_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#file_system_id EcsTaskDefinition#file_system_id}.
        :param root_directory: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#root_directory EcsTaskDefinition#root_directory}.
        '''
        if isinstance(authorization_config, dict):
            authorization_config = EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationAuthorizationConfig(**authorization_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8d0f21c17a8138957f6ef155e96c21e27ff9052e46857204f2c5c48645076b9)
            check_type(argname="argument authorization_config", value=authorization_config, expected_type=type_hints["authorization_config"])
            check_type(argname="argument file_system_id", value=file_system_id, expected_type=type_hints["file_system_id"])
            check_type(argname="argument root_directory", value=root_directory, expected_type=type_hints["root_directory"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "authorization_config": authorization_config,
            "file_system_id": file_system_id,
            "root_directory": root_directory,
        }

    @builtins.property
    def authorization_config(
        self,
    ) -> "EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationAuthorizationConfig":
        '''authorization_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#authorization_config EcsTaskDefinition#authorization_config}
        '''
        result = self._values.get("authorization_config")
        assert result is not None, "Required property 'authorization_config' is missing"
        return typing.cast("EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationAuthorizationConfig", result)

    @builtins.property
    def file_system_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#file_system_id EcsTaskDefinition#file_system_id}.'''
        result = self._values.get("file_system_id")
        assert result is not None, "Required property 'file_system_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def root_directory(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#root_directory EcsTaskDefinition#root_directory}.'''
        result = self._values.get("root_directory")
        assert result is not None, "Required property 'root_directory' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.ecsTaskDefinition.EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationAuthorizationConfig",
    jsii_struct_bases=[],
    name_mapping={"credentials_parameter": "credentialsParameter", "domain": "domain"},
)
class EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationAuthorizationConfig:
    def __init__(
        self,
        *,
        credentials_parameter: builtins.str,
        domain: builtins.str,
    ) -> None:
        '''
        :param credentials_parameter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#credentials_parameter EcsTaskDefinition#credentials_parameter}.
        :param domain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#domain EcsTaskDefinition#domain}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29809d17fbf121df264b2fa5c1eb5429674aeff54e579c0e57dce8871ea4faac)
            check_type(argname="argument credentials_parameter", value=credentials_parameter, expected_type=type_hints["credentials_parameter"])
            check_type(argname="argument domain", value=domain, expected_type=type_hints["domain"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "credentials_parameter": credentials_parameter,
            "domain": domain,
        }

    @builtins.property
    def credentials_parameter(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#credentials_parameter EcsTaskDefinition#credentials_parameter}.'''
        result = self._values.get("credentials_parameter")
        assert result is not None, "Required property 'credentials_parameter' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def domain(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#domain EcsTaskDefinition#domain}.'''
        result = self._values.get("domain")
        assert result is not None, "Required property 'domain' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationAuthorizationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationAuthorizationConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ecsTaskDefinition.EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationAuthorizationConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__94107112bfe6de972af5b39ef3130fcaafa7badc0be500243ec774f9a1afa84f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="credentialsParameterInput")
    def credentials_parameter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "credentialsParameterInput"))

    @builtins.property
    @jsii.member(jsii_name="domainInput")
    def domain_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainInput"))

    @builtins.property
    @jsii.member(jsii_name="credentialsParameter")
    def credentials_parameter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "credentialsParameter"))

    @credentials_parameter.setter
    def credentials_parameter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3262146cbef5aa58c272834352b376ec8483ff3ca74939a847b9923e4ab6a66c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "credentialsParameter", value)

    @builtins.property
    @jsii.member(jsii_name="domain")
    def domain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domain"))

    @domain.setter
    def domain(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__28a8d624f988b57a06d447ab345c024240a59edc0a792db9817edb7187854967)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domain", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationAuthorizationConfig]:
        return typing.cast(typing.Optional[EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationAuthorizationConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationAuthorizationConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__baca4ea69ba2998dd790c626d7ea3c8a75fb2e7a10dff60ec2c0baf0946c0687)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ecsTaskDefinition.EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4f9e399edbf7633840558059d5c2e679d7a18585164326e97a174c0549bf9a7f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAuthorizationConfig")
    def put_authorization_config(
        self,
        *,
        credentials_parameter: builtins.str,
        domain: builtins.str,
    ) -> None:
        '''
        :param credentials_parameter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#credentials_parameter EcsTaskDefinition#credentials_parameter}.
        :param domain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#domain EcsTaskDefinition#domain}.
        '''
        value = EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationAuthorizationConfig(
            credentials_parameter=credentials_parameter, domain=domain
        )

        return typing.cast(None, jsii.invoke(self, "putAuthorizationConfig", [value]))

    @builtins.property
    @jsii.member(jsii_name="authorizationConfig")
    def authorization_config(
        self,
    ) -> EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationAuthorizationConfigOutputReference:
        return typing.cast(EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationAuthorizationConfigOutputReference, jsii.get(self, "authorizationConfig"))

    @builtins.property
    @jsii.member(jsii_name="authorizationConfigInput")
    def authorization_config_input(
        self,
    ) -> typing.Optional[EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationAuthorizationConfig]:
        return typing.cast(typing.Optional[EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationAuthorizationConfig], jsii.get(self, "authorizationConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="fileSystemIdInput")
    def file_system_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fileSystemIdInput"))

    @builtins.property
    @jsii.member(jsii_name="rootDirectoryInput")
    def root_directory_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rootDirectoryInput"))

    @builtins.property
    @jsii.member(jsii_name="fileSystemId")
    def file_system_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fileSystemId"))

    @file_system_id.setter
    def file_system_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd9b87654b9054beeb9a6ba8ee27c42a2f8294a8865a499aed4b1cc70d669814)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileSystemId", value)

    @builtins.property
    @jsii.member(jsii_name="rootDirectory")
    def root_directory(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rootDirectory"))

    @root_directory.setter
    def root_directory(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a633c65aafdc8de38a793f9e870e71d78ea651e8ef8b33eb761c35b303467562)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rootDirectory", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfiguration]:
        return typing.cast(typing.Optional[EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08e5bd2a8310b706b3a8d160533c4b194274ac68acd00c54c089335a33737587)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EcsTaskDefinitionVolumeList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ecsTaskDefinition.EcsTaskDefinitionVolumeList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__634ab45575b0a2c72de1879492f2a247b19d8e7172c3b76d8bcf77e0cd44bc3c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "EcsTaskDefinitionVolumeOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__408cac77448a7b48b1485c489d2ee135f7a561600e2525eb1eaf5ebf6f02ec48)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EcsTaskDefinitionVolumeOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b97c64e8348883d5034b0765e530dddbc9d4e78f16873ffb76b759b4fd5549d3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__cee0aa91ee97cfcb6334c341c257f188bf1cceaba3b1463ce93a060547831826)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8574eafc9a50a17297ae95d582ae2a04ef36c6d263f0b20c71ae1fc9399de724)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EcsTaskDefinitionVolume]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EcsTaskDefinitionVolume]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EcsTaskDefinitionVolume]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c46806b3b232cf30430643ef56aeec4c8459da756d8294083712ee233e5cd2e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EcsTaskDefinitionVolumeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ecsTaskDefinition.EcsTaskDefinitionVolumeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f5cfa21ecbeb7906f6832df887fca51e6c6adad41ff23812425c9f5cb06778c3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putDockerVolumeConfiguration")
    def put_docker_volume_configuration(
        self,
        *,
        autoprovision: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        driver: typing.Optional[builtins.str] = None,
        driver_opts: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        scope: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param autoprovision: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#autoprovision EcsTaskDefinition#autoprovision}.
        :param driver: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#driver EcsTaskDefinition#driver}.
        :param driver_opts: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#driver_opts EcsTaskDefinition#driver_opts}.
        :param labels: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#labels EcsTaskDefinition#labels}.
        :param scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#scope EcsTaskDefinition#scope}.
        '''
        value = EcsTaskDefinitionVolumeDockerVolumeConfiguration(
            autoprovision=autoprovision,
            driver=driver,
            driver_opts=driver_opts,
            labels=labels,
            scope=scope,
        )

        return typing.cast(None, jsii.invoke(self, "putDockerVolumeConfiguration", [value]))

    @jsii.member(jsii_name="putEfsVolumeConfiguration")
    def put_efs_volume_configuration(
        self,
        *,
        file_system_id: builtins.str,
        authorization_config: typing.Optional[typing.Union[EcsTaskDefinitionVolumeEfsVolumeConfigurationAuthorizationConfig, typing.Dict[builtins.str, typing.Any]]] = None,
        root_directory: typing.Optional[builtins.str] = None,
        transit_encryption: typing.Optional[builtins.str] = None,
        transit_encryption_port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param file_system_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#file_system_id EcsTaskDefinition#file_system_id}.
        :param authorization_config: authorization_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#authorization_config EcsTaskDefinition#authorization_config}
        :param root_directory: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#root_directory EcsTaskDefinition#root_directory}.
        :param transit_encryption: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#transit_encryption EcsTaskDefinition#transit_encryption}.
        :param transit_encryption_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#transit_encryption_port EcsTaskDefinition#transit_encryption_port}.
        '''
        value = EcsTaskDefinitionVolumeEfsVolumeConfiguration(
            file_system_id=file_system_id,
            authorization_config=authorization_config,
            root_directory=root_directory,
            transit_encryption=transit_encryption,
            transit_encryption_port=transit_encryption_port,
        )

        return typing.cast(None, jsii.invoke(self, "putEfsVolumeConfiguration", [value]))

    @jsii.member(jsii_name="putFsxWindowsFileServerVolumeConfiguration")
    def put_fsx_windows_file_server_volume_configuration(
        self,
        *,
        authorization_config: typing.Union[EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationAuthorizationConfig, typing.Dict[builtins.str, typing.Any]],
        file_system_id: builtins.str,
        root_directory: builtins.str,
    ) -> None:
        '''
        :param authorization_config: authorization_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#authorization_config EcsTaskDefinition#authorization_config}
        :param file_system_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#file_system_id EcsTaskDefinition#file_system_id}.
        :param root_directory: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#root_directory EcsTaskDefinition#root_directory}.
        '''
        value = EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfiguration(
            authorization_config=authorization_config,
            file_system_id=file_system_id,
            root_directory=root_directory,
        )

        return typing.cast(None, jsii.invoke(self, "putFsxWindowsFileServerVolumeConfiguration", [value]))

    @jsii.member(jsii_name="resetDockerVolumeConfiguration")
    def reset_docker_volume_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDockerVolumeConfiguration", []))

    @jsii.member(jsii_name="resetEfsVolumeConfiguration")
    def reset_efs_volume_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEfsVolumeConfiguration", []))

    @jsii.member(jsii_name="resetFsxWindowsFileServerVolumeConfiguration")
    def reset_fsx_windows_file_server_volume_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFsxWindowsFileServerVolumeConfiguration", []))

    @jsii.member(jsii_name="resetHostPath")
    def reset_host_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostPath", []))

    @builtins.property
    @jsii.member(jsii_name="dockerVolumeConfiguration")
    def docker_volume_configuration(
        self,
    ) -> EcsTaskDefinitionVolumeDockerVolumeConfigurationOutputReference:
        return typing.cast(EcsTaskDefinitionVolumeDockerVolumeConfigurationOutputReference, jsii.get(self, "dockerVolumeConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="efsVolumeConfiguration")
    def efs_volume_configuration(
        self,
    ) -> EcsTaskDefinitionVolumeEfsVolumeConfigurationOutputReference:
        return typing.cast(EcsTaskDefinitionVolumeEfsVolumeConfigurationOutputReference, jsii.get(self, "efsVolumeConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="fsxWindowsFileServerVolumeConfiguration")
    def fsx_windows_file_server_volume_configuration(
        self,
    ) -> EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationOutputReference:
        return typing.cast(EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationOutputReference, jsii.get(self, "fsxWindowsFileServerVolumeConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="dockerVolumeConfigurationInput")
    def docker_volume_configuration_input(
        self,
    ) -> typing.Optional[EcsTaskDefinitionVolumeDockerVolumeConfiguration]:
        return typing.cast(typing.Optional[EcsTaskDefinitionVolumeDockerVolumeConfiguration], jsii.get(self, "dockerVolumeConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="efsVolumeConfigurationInput")
    def efs_volume_configuration_input(
        self,
    ) -> typing.Optional[EcsTaskDefinitionVolumeEfsVolumeConfiguration]:
        return typing.cast(typing.Optional[EcsTaskDefinitionVolumeEfsVolumeConfiguration], jsii.get(self, "efsVolumeConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="fsxWindowsFileServerVolumeConfigurationInput")
    def fsx_windows_file_server_volume_configuration_input(
        self,
    ) -> typing.Optional[EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfiguration]:
        return typing.cast(typing.Optional[EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfiguration], jsii.get(self, "fsxWindowsFileServerVolumeConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="hostPathInput")
    def host_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostPathInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="hostPath")
    def host_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostPath"))

    @host_path.setter
    def host_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3b3c4c2090b6df04ebcc581c94243ee19fa87816a44c7bcd192e41e67e26d5e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostPath", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd7a846ef74fa398c28556e92ae69f3c196e3d4a9c8bb764dfd42a471b4c6214)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EcsTaskDefinitionVolume, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EcsTaskDefinitionVolume, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EcsTaskDefinitionVolume, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26878a3f75e136ea093d4dfb5d41e1981e2c4e40ffcf454ad03d56e270ef3b47)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "EcsTaskDefinition",
    "EcsTaskDefinitionConfig",
    "EcsTaskDefinitionEphemeralStorage",
    "EcsTaskDefinitionEphemeralStorageOutputReference",
    "EcsTaskDefinitionInferenceAccelerator",
    "EcsTaskDefinitionInferenceAcceleratorList",
    "EcsTaskDefinitionInferenceAcceleratorOutputReference",
    "EcsTaskDefinitionPlacementConstraints",
    "EcsTaskDefinitionPlacementConstraintsList",
    "EcsTaskDefinitionPlacementConstraintsOutputReference",
    "EcsTaskDefinitionProxyConfiguration",
    "EcsTaskDefinitionProxyConfigurationOutputReference",
    "EcsTaskDefinitionRuntimePlatform",
    "EcsTaskDefinitionRuntimePlatformOutputReference",
    "EcsTaskDefinitionVolume",
    "EcsTaskDefinitionVolumeDockerVolumeConfiguration",
    "EcsTaskDefinitionVolumeDockerVolumeConfigurationOutputReference",
    "EcsTaskDefinitionVolumeEfsVolumeConfiguration",
    "EcsTaskDefinitionVolumeEfsVolumeConfigurationAuthorizationConfig",
    "EcsTaskDefinitionVolumeEfsVolumeConfigurationAuthorizationConfigOutputReference",
    "EcsTaskDefinitionVolumeEfsVolumeConfigurationOutputReference",
    "EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfiguration",
    "EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationAuthorizationConfig",
    "EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationAuthorizationConfigOutputReference",
    "EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationOutputReference",
    "EcsTaskDefinitionVolumeList",
    "EcsTaskDefinitionVolumeOutputReference",
]

publication.publish()

def _typecheckingstub__5016cc3736ae456900355e094294caaf2e97266d211531281daeed4dcdcf04e6(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    container_definitions: builtins.str,
    family: builtins.str,
    cpu: typing.Optional[builtins.str] = None,
    ephemeral_storage: typing.Optional[typing.Union[EcsTaskDefinitionEphemeralStorage, typing.Dict[builtins.str, typing.Any]]] = None,
    execution_role_arn: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    inference_accelerator: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EcsTaskDefinitionInferenceAccelerator, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ipc_mode: typing.Optional[builtins.str] = None,
    memory: typing.Optional[builtins.str] = None,
    network_mode: typing.Optional[builtins.str] = None,
    pid_mode: typing.Optional[builtins.str] = None,
    placement_constraints: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EcsTaskDefinitionPlacementConstraints, typing.Dict[builtins.str, typing.Any]]]]] = None,
    proxy_configuration: typing.Optional[typing.Union[EcsTaskDefinitionProxyConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    requires_compatibilities: typing.Optional[typing.Sequence[builtins.str]] = None,
    runtime_platform: typing.Optional[typing.Union[EcsTaskDefinitionRuntimePlatform, typing.Dict[builtins.str, typing.Any]]] = None,
    skip_destroy: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    task_role_arn: typing.Optional[builtins.str] = None,
    volume: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EcsTaskDefinitionVolume, typing.Dict[builtins.str, typing.Any]]]]] = None,
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

def _typecheckingstub__86a6a610c1998bf3625af43f5bf07666846c4cb1f6f5ccf66f9192fa301ba4e7(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EcsTaskDefinitionInferenceAccelerator, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3cee5e36feef94865ee57e4f8b105b65be8aec41a27cd2a90d4fad547b9475e9(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EcsTaskDefinitionPlacementConstraints, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c9dbe3694625ac0a5ca4e8bac304518a3bfc6d5268363fce30a18be8d3ac2d7(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EcsTaskDefinitionVolume, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01b43b3be86e0b135ebb1e478c1906378bd7266f2e507e4d366c436b11c0ab05(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2494fa0cbceff5092643f8a37feeae82560b0edfbaa8ae9102d888bceb9af184(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9f5ff1776df8cd8c9e5eb2b01d1b422e8e53a4c76c08864f6ac1d48ae55029b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ff72af2c739ffff14cbb87dc8314576593894898c5bcf00560acbd029941840(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8da7531f3599513f8954eca61c0e029952cba5b46a84881ae9c6a74f518b1c7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7775b1761eab42d08c83b759a3ee5d47041809c694fdb69e6d691582c1a38d28(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e2b510c0015e787e8b5e15767c12d56451086f7757a55e72d10f54e93bcf003(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__751b2265e23def9f3b385ba436c6a9f180ac26298c753e24d422b569b49f901c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e347ae82e237241fca28c39d3305e51ba6cc73bb9d07edbf3ef4771476ee909(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b2b793e5e562f770c6104d9bfe8c033ab1d787c038bcc65c481fa9b07ddcedf(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1eb0286078e8e91c609ed2cba5d11aa0c76db29713fe3b636f67e13c1e52acd0(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__652034a30cfd41b21a6ad87171ae2ce523ec97df9218b50289304eb16fbe4e6e(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a8bffeb5253b72c67f10950e8565e7922b10b605c0fdc0700d36f96d4c7c78f(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a80b39c39de2a764d9eb95f52411d3bd6911c6023c248335e37d20311a915dae(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb9a8868b7c913445ec7d92f02324dcc239e4fd239e670d165f4b611f7cd14ae(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    container_definitions: builtins.str,
    family: builtins.str,
    cpu: typing.Optional[builtins.str] = None,
    ephemeral_storage: typing.Optional[typing.Union[EcsTaskDefinitionEphemeralStorage, typing.Dict[builtins.str, typing.Any]]] = None,
    execution_role_arn: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    inference_accelerator: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EcsTaskDefinitionInferenceAccelerator, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ipc_mode: typing.Optional[builtins.str] = None,
    memory: typing.Optional[builtins.str] = None,
    network_mode: typing.Optional[builtins.str] = None,
    pid_mode: typing.Optional[builtins.str] = None,
    placement_constraints: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EcsTaskDefinitionPlacementConstraints, typing.Dict[builtins.str, typing.Any]]]]] = None,
    proxy_configuration: typing.Optional[typing.Union[EcsTaskDefinitionProxyConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    requires_compatibilities: typing.Optional[typing.Sequence[builtins.str]] = None,
    runtime_platform: typing.Optional[typing.Union[EcsTaskDefinitionRuntimePlatform, typing.Dict[builtins.str, typing.Any]]] = None,
    skip_destroy: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    task_role_arn: typing.Optional[builtins.str] = None,
    volume: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EcsTaskDefinitionVolume, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__064708fb17376a2811c0cc07a5f82be4c58c5492f43b2d4c225726bf5abf3cd3(
    *,
    size_in_gib: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5538fed11f302544fc1b9fde03004b79d1ea0fd4305876a4af12bc3d180f301f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9062481e05a86913a0524745ea65d4f223a6089e2037833cbd4eae29ded455b4(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec70883e15f99beb9777fc075be7b6c13d142e0bf8b9bf7c4fa286a2dd4e984b(
    value: typing.Optional[EcsTaskDefinitionEphemeralStorage],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__736187d21a344322b15fc043fc46447c2a795e472f859b8eeddc2d9ebe4d9b0b(
    *,
    device_name: builtins.str,
    device_type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__907aabb6f1c407809006e01cde014edceb8dc7b604451ea2fbee95003b95d44a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd25861542c7c5e497c8fb7cd32acd34ba5db8a8c66beae6badeb288a87adca6(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2cc28ee5b25a2e31963dfb66bc992ef00c75745ae21711d31d9bec173ac5df12(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4dd46ae81e5b48c9a5c1b5efa8c97d1b56faeddfe8ef23aaf22c6b7a5997dc84(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__312e72ac3059e4a8ab51a54946bbf6e1d6bbfd2dad7f84b7891c6ef87dc4f4c6(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c10416adbeb558b69340289387518d0529923dd875f1cbe1c0988dc6bd718dc(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EcsTaskDefinitionInferenceAccelerator]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fbe46c94389b942edc148025126a82988304a9d2c5b004a584245996c886b913(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4555972c3ce0f039038520e945daf6a4f06bfd4f73240a08079590e5c6a0675(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04c772b99cd3a1b4c83ff8df361db9ef857d10609da4d40322b07af99bfb0720(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__442f84f7f8c25a2ac37491442ad5ad0dfefd31717988484861f2908c99f382eb(
    value: typing.Optional[typing.Union[EcsTaskDefinitionInferenceAccelerator, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2302d092b4ea185e50e736db0151e65d4c12db59ccb1207c4383824a9c2dec06(
    *,
    type: builtins.str,
    expression: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b66ab5321037e2e5e67e89f92d34e85cd52f5ed6fd67ba174e5ef8988a69ca5b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3f84a6ae8a6600ce7cd7e179d98af515f4f2a3768d9da9692273a597d59668c(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e211eef5d826966e5175496afc1c872f5acc379af483c5840e06edac4970bd9d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06b9273f1d6a131210b165d0553bad4139a8a369b89a62f766bcab3701099d8a(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15f3b2a9530b222893b0ff83aaaa565168dd3071499c7fdaa7ec454a8d4a10c4(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ebe69553b8385f05f486e5943250dd8a50f405bc7fe89b18ab171e94183a0561(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EcsTaskDefinitionPlacementConstraints]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__272adf4cd09b6a0685daaf2d29de908159ff3dc1d448531edfe94d379cd045f3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10bbdea7d95f7cad8b75719fde3cdf5e66cc6d593c8b1eab073d5730538d5279(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__526e4c7ac3243d1b0f96bbb76a7c0ed8d0ad73dda50bdb5838091d0e3de6c57b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1c7e09956f0dfcf3558000cb992fefbd6533c8ca80a3ab1c9ef3bc5999c7957(
    value: typing.Optional[typing.Union[EcsTaskDefinitionPlacementConstraints, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39b1804ea7cbfc992c0f8e62dc7e885ef525afdb1efd99f1e6c75e84114b3f8a(
    *,
    container_name: builtins.str,
    properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2d469977be56e37e9677900b57169552965c8c1f7738eed25c355e2d20d93cb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__870fb12b7b1c60be8750cdb9dbb7e4560474b319a9a58923d846706bfffe5db4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__302504045eb37b094cc4756199c8cc4bb89cdcd7d2d2cb075d1340c2557b7622(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d28c0141922254ac451af544cc6840a791a9beaf9304eba3c159c4ff0a12f75(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3639143af886e471359bd250d4398b340b1ef9c109a1d844e8ad6542834ba6e1(
    value: typing.Optional[EcsTaskDefinitionProxyConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb1e8219dce015820bd51945cc253647107fafd9900750311456b0e2ebe67eb5(
    *,
    cpu_architecture: typing.Optional[builtins.str] = None,
    operating_system_family: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b5b270e0f730ebdaa8516849860aa44025e9a5626a9913c4e783ac5885ddb4f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f51a5453337d1bab44c6f7693f3bf995e0dad3d71b7cacf3f0d2098199e36a70(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf8473788179556b43a0e59d0bff18ebfd03ff73c85350b90553cf43cd9e9cdf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b92c600ccf6bd1cc67f0b141cee72ca5ae83c76d259a768d6de69b6f7b3048c(
    value: typing.Optional[EcsTaskDefinitionRuntimePlatform],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4aef0b4c058f156eb9ad1a50b5ba1371842b8849a68d50b7e6c66ec2f7711c41(
    *,
    name: builtins.str,
    docker_volume_configuration: typing.Optional[typing.Union[EcsTaskDefinitionVolumeDockerVolumeConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    efs_volume_configuration: typing.Optional[typing.Union[EcsTaskDefinitionVolumeEfsVolumeConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    fsx_windows_file_server_volume_configuration: typing.Optional[typing.Union[EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    host_path: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38db6082bee444ddf6c6a27543c4b3492a5fe2b224605fdf106056ddf21ca102(
    *,
    autoprovision: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    driver: typing.Optional[builtins.str] = None,
    driver_opts: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    scope: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58dbe50fbef94eeb6272c1017109c2f529f1be2b9603f93d200eb169e03a7dc7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08c084954d6f901487aec159286a0133af132bac3f478c3cf5ce219af9909ff2(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58596a54a21ce5473be4d837acbb5456a35c73b09e440b694d64b6101a002bc8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99c5fd46bd8c31c468efb81734af349142ff2ab4e6391c90a47b884936f534f0(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f5e577ebd734a99d62449ff32b523e7dd1871e7d89b1a5b69425c01106f1748(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53e8ebee2c6a90c09db84d06ed3b82f832ba1f7ca5bf20b9cc1ee56f2ac02a50(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6794ccc8d4e9a0050ad8512672882f8057c729786d29648fedfdec3e897cf4f2(
    value: typing.Optional[EcsTaskDefinitionVolumeDockerVolumeConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2943c8937c0a5d6157f3ade05e59f0ace48405431919cf6bbf266b65c7d99123(
    *,
    file_system_id: builtins.str,
    authorization_config: typing.Optional[typing.Union[EcsTaskDefinitionVolumeEfsVolumeConfigurationAuthorizationConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    root_directory: typing.Optional[builtins.str] = None,
    transit_encryption: typing.Optional[builtins.str] = None,
    transit_encryption_port: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13560d1075ab6cc0d57dcc15a85543590f66b7ba282917a17483f91b319373fd(
    *,
    access_point_id: typing.Optional[builtins.str] = None,
    iam: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe9de39dde71d3a237ef1791c505823a4b3f3f24f60b3f4294459a62b0adc5c5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0f77ddf33560342dff065e9ad97e7c67b1b1d106ec44ca6139c99c3ffcb32a3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac4820624f633d507dc55fbe1e70f4ca580f27530b60e2ca46f292c3eb6166b2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84765addaeab23b081f8b2cfdbc8759a9ab72f6ba3e8bbb0d78e4249d4c69d9a(
    value: typing.Optional[EcsTaskDefinitionVolumeEfsVolumeConfigurationAuthorizationConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f215de1d78054b91a0243f964441a285bc35a6dbefa39f05cb0c57a64ae04642(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9df258d47c5ff98aa38bcb43c5676609a2290f6f768134fa3e81c7965c1674d5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70fa3daae9a741b5862086a4121dbf574a569ae60dad7f5830f53b5d8c9df94b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3d2645866839b7535952d9b60650a325c699eb488b9b9d11c484bf12c8d5cd7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79c5e9663946a5e9a2d108f58fa8f5e2cf3303c32db56c389ba19c4dfc77bd09(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0ea0ff987cc2a6d35409fde03b807c4dde2f1bdaf24b9782f99977088d90a37(
    value: typing.Optional[EcsTaskDefinitionVolumeEfsVolumeConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8d0f21c17a8138957f6ef155e96c21e27ff9052e46857204f2c5c48645076b9(
    *,
    authorization_config: typing.Union[EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationAuthorizationConfig, typing.Dict[builtins.str, typing.Any]],
    file_system_id: builtins.str,
    root_directory: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29809d17fbf121df264b2fa5c1eb5429674aeff54e579c0e57dce8871ea4faac(
    *,
    credentials_parameter: builtins.str,
    domain: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94107112bfe6de972af5b39ef3130fcaafa7badc0be500243ec774f9a1afa84f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3262146cbef5aa58c272834352b376ec8483ff3ca74939a847b9923e4ab6a66c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28a8d624f988b57a06d447ab345c024240a59edc0a792db9817edb7187854967(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__baca4ea69ba2998dd790c626d7ea3c8a75fb2e7a10dff60ec2c0baf0946c0687(
    value: typing.Optional[EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationAuthorizationConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f9e399edbf7633840558059d5c2e679d7a18585164326e97a174c0549bf9a7f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd9b87654b9054beeb9a6ba8ee27c42a2f8294a8865a499aed4b1cc70d669814(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a633c65aafdc8de38a793f9e870e71d78ea651e8ef8b33eb761c35b303467562(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08e5bd2a8310b706b3a8d160533c4b194274ac68acd00c54c089335a33737587(
    value: typing.Optional[EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__634ab45575b0a2c72de1879492f2a247b19d8e7172c3b76d8bcf77e0cd44bc3c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__408cac77448a7b48b1485c489d2ee135f7a561600e2525eb1eaf5ebf6f02ec48(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b97c64e8348883d5034b0765e530dddbc9d4e78f16873ffb76b759b4fd5549d3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cee0aa91ee97cfcb6334c341c257f188bf1cceaba3b1463ce93a060547831826(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8574eafc9a50a17297ae95d582ae2a04ef36c6d263f0b20c71ae1fc9399de724(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c46806b3b232cf30430643ef56aeec4c8459da756d8294083712ee233e5cd2e(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EcsTaskDefinitionVolume]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5cfa21ecbeb7906f6832df887fca51e6c6adad41ff23812425c9f5cb06778c3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3b3c4c2090b6df04ebcc581c94243ee19fa87816a44c7bcd192e41e67e26d5e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd7a846ef74fa398c28556e92ae69f3c196e3d4a9c8bb764dfd42a471b4c6214(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26878a3f75e136ea093d4dfb5d41e1981e2c4e40ffcf454ad03d56e270ef3b47(
    value: typing.Optional[typing.Union[EcsTaskDefinitionVolume, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
