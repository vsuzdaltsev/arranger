'''
# `data_aws_ec2_instance_type`

Refer to the Terraform Registory for docs: [`data_aws_ec2_instance_type`](https://www.terraform.io/docs/providers/aws/d/ec2_instance_type).
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


class DataAwsEc2InstanceType(
    _cdktf_9a9027ec.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dataAwsEc2InstanceType.DataAwsEc2InstanceType",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/d/ec2_instance_type aws_ec2_instance_type}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        instance_type: builtins.str,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["DataAwsEc2InstanceTypeTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/d/ec2_instance_type aws_ec2_instance_type} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param instance_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ec2_instance_type#instance_type DataAwsEc2InstanceType#instance_type}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ec2_instance_type#id DataAwsEc2InstanceType#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ec2_instance_type#timeouts DataAwsEc2InstanceType#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d84874e9a7c54940ed64d39ed0e8364de333e59a7dd67585f173eb1db5820eb6)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataAwsEc2InstanceTypeConfig(
            instance_type=instance_type,
            id=id,
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
    def put_timeouts(self, *, read: typing.Optional[builtins.str] = None) -> None:
        '''
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ec2_instance_type#read DataAwsEc2InstanceType#read}.
        '''
        value = DataAwsEc2InstanceTypeTimeouts(read=read)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

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
    @jsii.member(jsii_name="autoRecoverySupported")
    def auto_recovery_supported(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "autoRecoverySupported"))

    @builtins.property
    @jsii.member(jsii_name="bareMetal")
    def bare_metal(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "bareMetal"))

    @builtins.property
    @jsii.member(jsii_name="burstablePerformanceSupported")
    def burstable_performance_supported(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "burstablePerformanceSupported"))

    @builtins.property
    @jsii.member(jsii_name="currentGeneration")
    def current_generation(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "currentGeneration"))

    @builtins.property
    @jsii.member(jsii_name="dedicatedHostsSupported")
    def dedicated_hosts_supported(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "dedicatedHostsSupported"))

    @builtins.property
    @jsii.member(jsii_name="defaultCores")
    def default_cores(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "defaultCores"))

    @builtins.property
    @jsii.member(jsii_name="defaultThreadsPerCore")
    def default_threads_per_core(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "defaultThreadsPerCore"))

    @builtins.property
    @jsii.member(jsii_name="defaultVcpus")
    def default_vcpus(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "defaultVcpus"))

    @builtins.property
    @jsii.member(jsii_name="ebsEncryptionSupport")
    def ebs_encryption_support(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ebsEncryptionSupport"))

    @builtins.property
    @jsii.member(jsii_name="ebsNvmeSupport")
    def ebs_nvme_support(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ebsNvmeSupport"))

    @builtins.property
    @jsii.member(jsii_name="ebsOptimizedSupport")
    def ebs_optimized_support(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ebsOptimizedSupport"))

    @builtins.property
    @jsii.member(jsii_name="ebsPerformanceBaselineBandwidth")
    def ebs_performance_baseline_bandwidth(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ebsPerformanceBaselineBandwidth"))

    @builtins.property
    @jsii.member(jsii_name="ebsPerformanceBaselineIops")
    def ebs_performance_baseline_iops(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ebsPerformanceBaselineIops"))

    @builtins.property
    @jsii.member(jsii_name="ebsPerformanceBaselineThroughput")
    def ebs_performance_baseline_throughput(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ebsPerformanceBaselineThroughput"))

    @builtins.property
    @jsii.member(jsii_name="ebsPerformanceMaximumBandwidth")
    def ebs_performance_maximum_bandwidth(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ebsPerformanceMaximumBandwidth"))

    @builtins.property
    @jsii.member(jsii_name="ebsPerformanceMaximumIops")
    def ebs_performance_maximum_iops(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ebsPerformanceMaximumIops"))

    @builtins.property
    @jsii.member(jsii_name="ebsPerformanceMaximumThroughput")
    def ebs_performance_maximum_throughput(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ebsPerformanceMaximumThroughput"))

    @builtins.property
    @jsii.member(jsii_name="efaSupported")
    def efa_supported(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "efaSupported"))

    @builtins.property
    @jsii.member(jsii_name="enaSupport")
    def ena_support(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "enaSupport"))

    @builtins.property
    @jsii.member(jsii_name="encryptionInTransitSupported")
    def encryption_in_transit_supported(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "encryptionInTransitSupported"))

    @builtins.property
    @jsii.member(jsii_name="fpgas")
    def fpgas(self) -> "DataAwsEc2InstanceTypeFpgasList":
        return typing.cast("DataAwsEc2InstanceTypeFpgasList", jsii.get(self, "fpgas"))

    @builtins.property
    @jsii.member(jsii_name="freeTierEligible")
    def free_tier_eligible(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "freeTierEligible"))

    @builtins.property
    @jsii.member(jsii_name="gpus")
    def gpus(self) -> "DataAwsEc2InstanceTypeGpusList":
        return typing.cast("DataAwsEc2InstanceTypeGpusList", jsii.get(self, "gpus"))

    @builtins.property
    @jsii.member(jsii_name="hibernationSupported")
    def hibernation_supported(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "hibernationSupported"))

    @builtins.property
    @jsii.member(jsii_name="hypervisor")
    def hypervisor(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hypervisor"))

    @builtins.property
    @jsii.member(jsii_name="inferenceAccelerators")
    def inference_accelerators(
        self,
    ) -> "DataAwsEc2InstanceTypeInferenceAcceleratorsList":
        return typing.cast("DataAwsEc2InstanceTypeInferenceAcceleratorsList", jsii.get(self, "inferenceAccelerators"))

    @builtins.property
    @jsii.member(jsii_name="instanceDisks")
    def instance_disks(self) -> "DataAwsEc2InstanceTypeInstanceDisksList":
        return typing.cast("DataAwsEc2InstanceTypeInstanceDisksList", jsii.get(self, "instanceDisks"))

    @builtins.property
    @jsii.member(jsii_name="instanceStorageSupported")
    def instance_storage_supported(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "instanceStorageSupported"))

    @builtins.property
    @jsii.member(jsii_name="ipv6Supported")
    def ipv6_supported(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "ipv6Supported"))

    @builtins.property
    @jsii.member(jsii_name="maximumIpv4AddressesPerInterface")
    def maximum_ipv4_addresses_per_interface(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maximumIpv4AddressesPerInterface"))

    @builtins.property
    @jsii.member(jsii_name="maximumIpv6AddressesPerInterface")
    def maximum_ipv6_addresses_per_interface(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maximumIpv6AddressesPerInterface"))

    @builtins.property
    @jsii.member(jsii_name="maximumNetworkInterfaces")
    def maximum_network_interfaces(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maximumNetworkInterfaces"))

    @builtins.property
    @jsii.member(jsii_name="memorySize")
    def memory_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "memorySize"))

    @builtins.property
    @jsii.member(jsii_name="networkPerformance")
    def network_performance(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "networkPerformance"))

    @builtins.property
    @jsii.member(jsii_name="supportedArchitectures")
    def supported_architectures(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "supportedArchitectures"))

    @builtins.property
    @jsii.member(jsii_name="supportedPlacementStrategies")
    def supported_placement_strategies(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "supportedPlacementStrategies"))

    @builtins.property
    @jsii.member(jsii_name="supportedRootDeviceTypes")
    def supported_root_device_types(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "supportedRootDeviceTypes"))

    @builtins.property
    @jsii.member(jsii_name="supportedUsagesClasses")
    def supported_usages_classes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "supportedUsagesClasses"))

    @builtins.property
    @jsii.member(jsii_name="supportedVirtualizationTypes")
    def supported_virtualization_types(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "supportedVirtualizationTypes"))

    @builtins.property
    @jsii.member(jsii_name="sustainedClockSpeed")
    def sustained_clock_speed(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "sustainedClockSpeed"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "DataAwsEc2InstanceTypeTimeoutsOutputReference":
        return typing.cast("DataAwsEc2InstanceTypeTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="totalFpgaMemory")
    def total_fpga_memory(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "totalFpgaMemory"))

    @builtins.property
    @jsii.member(jsii_name="totalGpuMemory")
    def total_gpu_memory(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "totalGpuMemory"))

    @builtins.property
    @jsii.member(jsii_name="totalInstanceStorage")
    def total_instance_storage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "totalInstanceStorage"))

    @builtins.property
    @jsii.member(jsii_name="validCores")
    def valid_cores(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "validCores"))

    @builtins.property
    @jsii.member(jsii_name="validThreadsPerCore")
    def valid_threads_per_core(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "validThreadsPerCore"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceTypeInput")
    def instance_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["DataAwsEc2InstanceTypeTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["DataAwsEc2InstanceTypeTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7344aa640c35023a9ee776c8d1f65215f29357b467e26fd8ee08d00aedcc84d3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="instanceType")
    def instance_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceType"))

    @instance_type.setter
    def instance_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7488b0652751a9db2ebc5107e7f56d16a88baa1a21d6904f54b3073f4330581a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceType", value)


@jsii.data_type(
    jsii_type="aws.dataAwsEc2InstanceType.DataAwsEc2InstanceTypeConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "instance_type": "instanceType",
        "id": "id",
        "timeouts": "timeouts",
    },
)
class DataAwsEc2InstanceTypeConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        instance_type: builtins.str,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["DataAwsEc2InstanceTypeTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param instance_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ec2_instance_type#instance_type DataAwsEc2InstanceType#instance_type}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ec2_instance_type#id DataAwsEc2InstanceType#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ec2_instance_type#timeouts DataAwsEc2InstanceType#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = DataAwsEc2InstanceTypeTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d9b20513bdb666cf6dcfecb5cba76495b140fffc14670098376da5c87219db5)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "instance_type": instance_type,
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
    def instance_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ec2_instance_type#instance_type DataAwsEc2InstanceType#instance_type}.'''
        result = self._values.get("instance_type")
        assert result is not None, "Required property 'instance_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ec2_instance_type#id DataAwsEc2InstanceType#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["DataAwsEc2InstanceTypeTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ec2_instance_type#timeouts DataAwsEc2InstanceType#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["DataAwsEc2InstanceTypeTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsEc2InstanceTypeConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.dataAwsEc2InstanceType.DataAwsEc2InstanceTypeFpgas",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAwsEc2InstanceTypeFpgas:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsEc2InstanceTypeFpgas(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsEc2InstanceTypeFpgasList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dataAwsEc2InstanceType.DataAwsEc2InstanceTypeFpgasList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ccb9958ae16920ad60e8f1e6c9c0bc118cfba8865c17c6779ba4e3030cc6da50)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "DataAwsEc2InstanceTypeFpgasOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b54406afda279291757c535485b6ca758a3de5226e2ead7638e0cebf77916c5)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAwsEc2InstanceTypeFpgasOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52277f1c1a6eda62a77ef0dba4bfd0a2915a5cf9c1f472dd44f62d8e1d8c8c82)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ef3da36e51248ef0b020d0d05bec1b004c19472cd54cbd6fb74054e84e87ecdd)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d3d5c0f84dc25d483736a4ccaff7117387b516f2655e60516c37fc92918ec189)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataAwsEc2InstanceTypeFpgasOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dataAwsEc2InstanceType.DataAwsEc2InstanceTypeFpgasOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7a551c050ecab0d90a5662ccafef5f44847d7890f7c6f382a5e3ea18d80445d0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="count")
    def count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "count"))

    @builtins.property
    @jsii.member(jsii_name="manufacturer")
    def manufacturer(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "manufacturer"))

    @builtins.property
    @jsii.member(jsii_name="memorySize")
    def memory_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "memorySize"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataAwsEc2InstanceTypeFpgas]:
        return typing.cast(typing.Optional[DataAwsEc2InstanceTypeFpgas], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAwsEc2InstanceTypeFpgas],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab80a4c9b2854e4a64bc2cae32883544b1098be813ee2dfcaf955798199ff264)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.dataAwsEc2InstanceType.DataAwsEc2InstanceTypeGpus",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAwsEc2InstanceTypeGpus:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsEc2InstanceTypeGpus(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsEc2InstanceTypeGpusList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dataAwsEc2InstanceType.DataAwsEc2InstanceTypeGpusList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0ed712dfb779313f290c92c956bba0c6cdd3470ed0354a59b9397b319d79eaed)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "DataAwsEc2InstanceTypeGpusOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dee147abb17538e3c1411bc875b351b7740e92fa0e64d20bb7615f828474ab6c)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAwsEc2InstanceTypeGpusOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__620c441b9ddc11156a556150ca044588c8b445b822fafcb72cac87d1a597da8b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6aebf0f0d497bbdfef2785b65ca1e7c0549dc2a73fbd9214fd64c07665a9b8ec)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8935cd72c1fd09aafe9c8f50e200bfcc28f4a444c26a7300892eba098f8fadfe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataAwsEc2InstanceTypeGpusOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dataAwsEc2InstanceType.DataAwsEc2InstanceTypeGpusOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__25b9226425214dde905ac64fdca35a2b8cc10d1179d8b0d7a21c49bb3d4f9232)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="count")
    def count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "count"))

    @builtins.property
    @jsii.member(jsii_name="manufacturer")
    def manufacturer(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "manufacturer"))

    @builtins.property
    @jsii.member(jsii_name="memorySize")
    def memory_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "memorySize"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataAwsEc2InstanceTypeGpus]:
        return typing.cast(typing.Optional[DataAwsEc2InstanceTypeGpus], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAwsEc2InstanceTypeGpus],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64f6b744cd60aba937723f7d4c66ea157bd18aad5e6ca19d38a48f11338f5f8d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.dataAwsEc2InstanceType.DataAwsEc2InstanceTypeInferenceAccelerators",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAwsEc2InstanceTypeInferenceAccelerators:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsEc2InstanceTypeInferenceAccelerators(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsEc2InstanceTypeInferenceAcceleratorsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dataAwsEc2InstanceType.DataAwsEc2InstanceTypeInferenceAcceleratorsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__20fd672646160c9d971427e49f762084af54d6204b5c576ebba66cc85697459c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAwsEc2InstanceTypeInferenceAcceleratorsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75496ee6b7c9a4bab744eb6114c6f02048e35007cc97a60f9735596196e6caaf)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAwsEc2InstanceTypeInferenceAcceleratorsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__81508c7d2fcc47f847793ecbd39fa8dfe6423a645becc5327365e7b93312c491)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f1cbc67a59b7585146c618be4122cf33c4e270609e9859575aeda242d341b301)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d9066f221e7c3f1008180db1941867c51f44728a750e1b92ac83c21873333ecd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataAwsEc2InstanceTypeInferenceAcceleratorsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dataAwsEc2InstanceType.DataAwsEc2InstanceTypeInferenceAcceleratorsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__70d7b2295d9ce35ce919dff72ae251a731bfe303b4fe8f54a1d08b4d482a60b5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="count")
    def count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "count"))

    @builtins.property
    @jsii.member(jsii_name="manufacturer")
    def manufacturer(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "manufacturer"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataAwsEc2InstanceTypeInferenceAccelerators]:
        return typing.cast(typing.Optional[DataAwsEc2InstanceTypeInferenceAccelerators], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAwsEc2InstanceTypeInferenceAccelerators],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42858c3514538b0a63614fd8919e8e679b80ec944780190a6dd1649e8502b4d9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.dataAwsEc2InstanceType.DataAwsEc2InstanceTypeInstanceDisks",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAwsEc2InstanceTypeInstanceDisks:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsEc2InstanceTypeInstanceDisks(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsEc2InstanceTypeInstanceDisksList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dataAwsEc2InstanceType.DataAwsEc2InstanceTypeInstanceDisksList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__12fa1d6c65ee616f312d6028e009a5253bedaa6b3e918ff2df28f26ee74a046a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAwsEc2InstanceTypeInstanceDisksOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97b68707762ee8bc957de56e66742cee3c849c94b61c8ee4306b854492b7b51f)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAwsEc2InstanceTypeInstanceDisksOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__916d4bb489a22c177a0a22d30b025f7c07d172500e3d3d9aae3685817f6023d1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__71f1cbbc86d8e143962f581768455bac8c3c6a36f7d1a611968407b1d74428ec)
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
            type_hints = typing.get_type_hints(_typecheckingstub__63101ec6e98987ba6f9e7572b7918cbf007a7f6ed78369a6c870c02d2f20df54)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataAwsEc2InstanceTypeInstanceDisksOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dataAwsEc2InstanceType.DataAwsEc2InstanceTypeInstanceDisksOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__71cde97c316a88f6920742ffcd4c8e36f8e90a3930b0c83a44e2163b85a830c1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="count")
    def count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "count"))

    @builtins.property
    @jsii.member(jsii_name="size")
    def size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "size"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataAwsEc2InstanceTypeInstanceDisks]:
        return typing.cast(typing.Optional[DataAwsEc2InstanceTypeInstanceDisks], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAwsEc2InstanceTypeInstanceDisks],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6de1738e80e7ea030a8e112e9729858cc92abb58f348a12e28f1b66dc01182f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.dataAwsEc2InstanceType.DataAwsEc2InstanceTypeTimeouts",
    jsii_struct_bases=[],
    name_mapping={"read": "read"},
)
class DataAwsEc2InstanceTypeTimeouts:
    def __init__(self, *, read: typing.Optional[builtins.str] = None) -> None:
        '''
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ec2_instance_type#read DataAwsEc2InstanceType#read}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca34c90aec7b8b8748755d022c5cd9ae799d92c868733e59c4c8da2d412f9d33)
            check_type(argname="argument read", value=read, expected_type=type_hints["read"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if read is not None:
            self._values["read"] = read

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ec2_instance_type#read DataAwsEc2InstanceType#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsEc2InstanceTypeTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsEc2InstanceTypeTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dataAwsEc2InstanceType.DataAwsEc2InstanceTypeTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8a0e7cbdefe54c9f813c1330d11eb4e804170c048d308b29d79471dd3a9260dc)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetRead")
    def reset_read(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRead", []))

    @builtins.property
    @jsii.member(jsii_name="readInput")
    def read_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "readInput"))

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a66382f01024f56ef7df14e8a9d8f1116dfe74cbab87df5f7606e5ab0eae5f96)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DataAwsEc2InstanceTypeTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DataAwsEc2InstanceTypeTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DataAwsEc2InstanceTypeTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e556db8615236144fa06dcbffd022638323a29e92b36aa14b1284e17c4e8db0e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DataAwsEc2InstanceType",
    "DataAwsEc2InstanceTypeConfig",
    "DataAwsEc2InstanceTypeFpgas",
    "DataAwsEc2InstanceTypeFpgasList",
    "DataAwsEc2InstanceTypeFpgasOutputReference",
    "DataAwsEc2InstanceTypeGpus",
    "DataAwsEc2InstanceTypeGpusList",
    "DataAwsEc2InstanceTypeGpusOutputReference",
    "DataAwsEc2InstanceTypeInferenceAccelerators",
    "DataAwsEc2InstanceTypeInferenceAcceleratorsList",
    "DataAwsEc2InstanceTypeInferenceAcceleratorsOutputReference",
    "DataAwsEc2InstanceTypeInstanceDisks",
    "DataAwsEc2InstanceTypeInstanceDisksList",
    "DataAwsEc2InstanceTypeInstanceDisksOutputReference",
    "DataAwsEc2InstanceTypeTimeouts",
    "DataAwsEc2InstanceTypeTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__d84874e9a7c54940ed64d39ed0e8364de333e59a7dd67585f173eb1db5820eb6(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    instance_type: builtins.str,
    id: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[DataAwsEc2InstanceTypeTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__7344aa640c35023a9ee776c8d1f65215f29357b467e26fd8ee08d00aedcc84d3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7488b0652751a9db2ebc5107e7f56d16a88baa1a21d6904f54b3073f4330581a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d9b20513bdb666cf6dcfecb5cba76495b140fffc14670098376da5c87219db5(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    instance_type: builtins.str,
    id: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[DataAwsEc2InstanceTypeTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ccb9958ae16920ad60e8f1e6c9c0bc118cfba8865c17c6779ba4e3030cc6da50(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b54406afda279291757c535485b6ca758a3de5226e2ead7638e0cebf77916c5(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52277f1c1a6eda62a77ef0dba4bfd0a2915a5cf9c1f472dd44f62d8e1d8c8c82(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef3da36e51248ef0b020d0d05bec1b004c19472cd54cbd6fb74054e84e87ecdd(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3d5c0f84dc25d483736a4ccaff7117387b516f2655e60516c37fc92918ec189(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a551c050ecab0d90a5662ccafef5f44847d7890f7c6f382a5e3ea18d80445d0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab80a4c9b2854e4a64bc2cae32883544b1098be813ee2dfcaf955798199ff264(
    value: typing.Optional[DataAwsEc2InstanceTypeFpgas],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ed712dfb779313f290c92c956bba0c6cdd3470ed0354a59b9397b319d79eaed(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dee147abb17538e3c1411bc875b351b7740e92fa0e64d20bb7615f828474ab6c(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__620c441b9ddc11156a556150ca044588c8b445b822fafcb72cac87d1a597da8b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6aebf0f0d497bbdfef2785b65ca1e7c0549dc2a73fbd9214fd64c07665a9b8ec(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8935cd72c1fd09aafe9c8f50e200bfcc28f4a444c26a7300892eba098f8fadfe(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25b9226425214dde905ac64fdca35a2b8cc10d1179d8b0d7a21c49bb3d4f9232(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64f6b744cd60aba937723f7d4c66ea157bd18aad5e6ca19d38a48f11338f5f8d(
    value: typing.Optional[DataAwsEc2InstanceTypeGpus],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20fd672646160c9d971427e49f762084af54d6204b5c576ebba66cc85697459c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75496ee6b7c9a4bab744eb6114c6f02048e35007cc97a60f9735596196e6caaf(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81508c7d2fcc47f847793ecbd39fa8dfe6423a645becc5327365e7b93312c491(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1cbc67a59b7585146c618be4122cf33c4e270609e9859575aeda242d341b301(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9066f221e7c3f1008180db1941867c51f44728a750e1b92ac83c21873333ecd(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70d7b2295d9ce35ce919dff72ae251a731bfe303b4fe8f54a1d08b4d482a60b5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42858c3514538b0a63614fd8919e8e679b80ec944780190a6dd1649e8502b4d9(
    value: typing.Optional[DataAwsEc2InstanceTypeInferenceAccelerators],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12fa1d6c65ee616f312d6028e009a5253bedaa6b3e918ff2df28f26ee74a046a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97b68707762ee8bc957de56e66742cee3c849c94b61c8ee4306b854492b7b51f(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__916d4bb489a22c177a0a22d30b025f7c07d172500e3d3d9aae3685817f6023d1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71f1cbbc86d8e143962f581768455bac8c3c6a36f7d1a611968407b1d74428ec(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63101ec6e98987ba6f9e7572b7918cbf007a7f6ed78369a6c870c02d2f20df54(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71cde97c316a88f6920742ffcd4c8e36f8e90a3930b0c83a44e2163b85a830c1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6de1738e80e7ea030a8e112e9729858cc92abb58f348a12e28f1b66dc01182f(
    value: typing.Optional[DataAwsEc2InstanceTypeInstanceDisks],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca34c90aec7b8b8748755d022c5cd9ae799d92c868733e59c4c8da2d412f9d33(
    *,
    read: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a0e7cbdefe54c9f813c1330d11eb4e804170c048d308b29d79471dd3a9260dc(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a66382f01024f56ef7df14e8a9d8f1116dfe74cbab87df5f7606e5ab0eae5f96(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e556db8615236144fa06dcbffd022638323a29e92b36aa14b1284e17c4e8db0e(
    value: typing.Optional[typing.Union[DataAwsEc2InstanceTypeTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
