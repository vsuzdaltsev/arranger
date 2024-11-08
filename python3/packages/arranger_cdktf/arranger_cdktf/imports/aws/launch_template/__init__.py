'''
# `aws_launch_template`

Refer to the Terraform Registory for docs: [`aws_launch_template`](https://www.terraform.io/docs/providers/aws/r/launch_template).
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


class LaunchTemplate(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.launchTemplate.LaunchTemplate",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/launch_template aws_launch_template}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        block_device_mappings: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LaunchTemplateBlockDeviceMappings", typing.Dict[builtins.str, typing.Any]]]]] = None,
        capacity_reservation_specification: typing.Optional[typing.Union["LaunchTemplateCapacityReservationSpecification", typing.Dict[builtins.str, typing.Any]]] = None,
        cpu_options: typing.Optional[typing.Union["LaunchTemplateCpuOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        credit_specification: typing.Optional[typing.Union["LaunchTemplateCreditSpecification", typing.Dict[builtins.str, typing.Any]]] = None,
        default_version: typing.Optional[jsii.Number] = None,
        description: typing.Optional[builtins.str] = None,
        disable_api_stop: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        disable_api_termination: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        ebs_optimized: typing.Optional[builtins.str] = None,
        elastic_gpu_specifications: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LaunchTemplateElasticGpuSpecifications", typing.Dict[builtins.str, typing.Any]]]]] = None,
        elastic_inference_accelerator: typing.Optional[typing.Union["LaunchTemplateElasticInferenceAccelerator", typing.Dict[builtins.str, typing.Any]]] = None,
        enclave_options: typing.Optional[typing.Union["LaunchTemplateEnclaveOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        hibernation_options: typing.Optional[typing.Union["LaunchTemplateHibernationOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        iam_instance_profile: typing.Optional[typing.Union["LaunchTemplateIamInstanceProfile", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        image_id: typing.Optional[builtins.str] = None,
        instance_initiated_shutdown_behavior: typing.Optional[builtins.str] = None,
        instance_market_options: typing.Optional[typing.Union["LaunchTemplateInstanceMarketOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        instance_requirements: typing.Optional[typing.Union["LaunchTemplateInstanceRequirements", typing.Dict[builtins.str, typing.Any]]] = None,
        instance_type: typing.Optional[builtins.str] = None,
        kernel_id: typing.Optional[builtins.str] = None,
        key_name: typing.Optional[builtins.str] = None,
        license_specification: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LaunchTemplateLicenseSpecification", typing.Dict[builtins.str, typing.Any]]]]] = None,
        maintenance_options: typing.Optional[typing.Union["LaunchTemplateMaintenanceOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        metadata_options: typing.Optional[typing.Union["LaunchTemplateMetadataOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        monitoring: typing.Optional[typing.Union["LaunchTemplateMonitoring", typing.Dict[builtins.str, typing.Any]]] = None,
        name: typing.Optional[builtins.str] = None,
        name_prefix: typing.Optional[builtins.str] = None,
        network_interfaces: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LaunchTemplateNetworkInterfaces", typing.Dict[builtins.str, typing.Any]]]]] = None,
        placement: typing.Optional[typing.Union["LaunchTemplatePlacement", typing.Dict[builtins.str, typing.Any]]] = None,
        private_dns_name_options: typing.Optional[typing.Union["LaunchTemplatePrivateDnsNameOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        ram_disk_id: typing.Optional[builtins.str] = None,
        security_group_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tag_specifications: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LaunchTemplateTagSpecifications", typing.Dict[builtins.str, typing.Any]]]]] = None,
        update_default_version: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        user_data: typing.Optional[builtins.str] = None,
        vpc_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/launch_template aws_launch_template} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param block_device_mappings: block_device_mappings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#block_device_mappings LaunchTemplate#block_device_mappings}
        :param capacity_reservation_specification: capacity_reservation_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#capacity_reservation_specification LaunchTemplate#capacity_reservation_specification}
        :param cpu_options: cpu_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#cpu_options LaunchTemplate#cpu_options}
        :param credit_specification: credit_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#credit_specification LaunchTemplate#credit_specification}
        :param default_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#default_version LaunchTemplate#default_version}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#description LaunchTemplate#description}.
        :param disable_api_stop: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#disable_api_stop LaunchTemplate#disable_api_stop}.
        :param disable_api_termination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#disable_api_termination LaunchTemplate#disable_api_termination}.
        :param ebs_optimized: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#ebs_optimized LaunchTemplate#ebs_optimized}.
        :param elastic_gpu_specifications: elastic_gpu_specifications block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#elastic_gpu_specifications LaunchTemplate#elastic_gpu_specifications}
        :param elastic_inference_accelerator: elastic_inference_accelerator block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#elastic_inference_accelerator LaunchTemplate#elastic_inference_accelerator}
        :param enclave_options: enclave_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#enclave_options LaunchTemplate#enclave_options}
        :param hibernation_options: hibernation_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#hibernation_options LaunchTemplate#hibernation_options}
        :param iam_instance_profile: iam_instance_profile block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#iam_instance_profile LaunchTemplate#iam_instance_profile}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#id LaunchTemplate#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param image_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#image_id LaunchTemplate#image_id}.
        :param instance_initiated_shutdown_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#instance_initiated_shutdown_behavior LaunchTemplate#instance_initiated_shutdown_behavior}.
        :param instance_market_options: instance_market_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#instance_market_options LaunchTemplate#instance_market_options}
        :param instance_requirements: instance_requirements block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#instance_requirements LaunchTemplate#instance_requirements}
        :param instance_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#instance_type LaunchTemplate#instance_type}.
        :param kernel_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#kernel_id LaunchTemplate#kernel_id}.
        :param key_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#key_name LaunchTemplate#key_name}.
        :param license_specification: license_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#license_specification LaunchTemplate#license_specification}
        :param maintenance_options: maintenance_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#maintenance_options LaunchTemplate#maintenance_options}
        :param metadata_options: metadata_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#metadata_options LaunchTemplate#metadata_options}
        :param monitoring: monitoring block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#monitoring LaunchTemplate#monitoring}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#name LaunchTemplate#name}.
        :param name_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#name_prefix LaunchTemplate#name_prefix}.
        :param network_interfaces: network_interfaces block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#network_interfaces LaunchTemplate#network_interfaces}
        :param placement: placement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#placement LaunchTemplate#placement}
        :param private_dns_name_options: private_dns_name_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#private_dns_name_options LaunchTemplate#private_dns_name_options}
        :param ram_disk_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#ram_disk_id LaunchTemplate#ram_disk_id}.
        :param security_group_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#security_group_names LaunchTemplate#security_group_names}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#tags LaunchTemplate#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#tags_all LaunchTemplate#tags_all}.
        :param tag_specifications: tag_specifications block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#tag_specifications LaunchTemplate#tag_specifications}
        :param update_default_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#update_default_version LaunchTemplate#update_default_version}.
        :param user_data: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#user_data LaunchTemplate#user_data}.
        :param vpc_security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#vpc_security_group_ids LaunchTemplate#vpc_security_group_ids}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0470f207412cb167faa928dd6ec400239ba967a5d726981daff67fb008b33b8)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = LaunchTemplateConfig(
            block_device_mappings=block_device_mappings,
            capacity_reservation_specification=capacity_reservation_specification,
            cpu_options=cpu_options,
            credit_specification=credit_specification,
            default_version=default_version,
            description=description,
            disable_api_stop=disable_api_stop,
            disable_api_termination=disable_api_termination,
            ebs_optimized=ebs_optimized,
            elastic_gpu_specifications=elastic_gpu_specifications,
            elastic_inference_accelerator=elastic_inference_accelerator,
            enclave_options=enclave_options,
            hibernation_options=hibernation_options,
            iam_instance_profile=iam_instance_profile,
            id=id,
            image_id=image_id,
            instance_initiated_shutdown_behavior=instance_initiated_shutdown_behavior,
            instance_market_options=instance_market_options,
            instance_requirements=instance_requirements,
            instance_type=instance_type,
            kernel_id=kernel_id,
            key_name=key_name,
            license_specification=license_specification,
            maintenance_options=maintenance_options,
            metadata_options=metadata_options,
            monitoring=monitoring,
            name=name,
            name_prefix=name_prefix,
            network_interfaces=network_interfaces,
            placement=placement,
            private_dns_name_options=private_dns_name_options,
            ram_disk_id=ram_disk_id,
            security_group_names=security_group_names,
            tags=tags,
            tags_all=tags_all,
            tag_specifications=tag_specifications,
            update_default_version=update_default_version,
            user_data=user_data,
            vpc_security_group_ids=vpc_security_group_ids,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putBlockDeviceMappings")
    def put_block_device_mappings(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LaunchTemplateBlockDeviceMappings", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bde12f9bd6fc9f77a76aacb1ea1830fadc85ad3c463e23974d682a4efce46774)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putBlockDeviceMappings", [value]))

    @jsii.member(jsii_name="putCapacityReservationSpecification")
    def put_capacity_reservation_specification(
        self,
        *,
        capacity_reservation_preference: typing.Optional[builtins.str] = None,
        capacity_reservation_target: typing.Optional[typing.Union["LaunchTemplateCapacityReservationSpecificationCapacityReservationTarget", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param capacity_reservation_preference: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#capacity_reservation_preference LaunchTemplate#capacity_reservation_preference}.
        :param capacity_reservation_target: capacity_reservation_target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#capacity_reservation_target LaunchTemplate#capacity_reservation_target}
        '''
        value = LaunchTemplateCapacityReservationSpecification(
            capacity_reservation_preference=capacity_reservation_preference,
            capacity_reservation_target=capacity_reservation_target,
        )

        return typing.cast(None, jsii.invoke(self, "putCapacityReservationSpecification", [value]))

    @jsii.member(jsii_name="putCpuOptions")
    def put_cpu_options(
        self,
        *,
        core_count: typing.Optional[jsii.Number] = None,
        threads_per_core: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param core_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#core_count LaunchTemplate#core_count}.
        :param threads_per_core: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#threads_per_core LaunchTemplate#threads_per_core}.
        '''
        value = LaunchTemplateCpuOptions(
            core_count=core_count, threads_per_core=threads_per_core
        )

        return typing.cast(None, jsii.invoke(self, "putCpuOptions", [value]))

    @jsii.member(jsii_name="putCreditSpecification")
    def put_credit_specification(
        self,
        *,
        cpu_credits: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cpu_credits: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#cpu_credits LaunchTemplate#cpu_credits}.
        '''
        value = LaunchTemplateCreditSpecification(cpu_credits=cpu_credits)

        return typing.cast(None, jsii.invoke(self, "putCreditSpecification", [value]))

    @jsii.member(jsii_name="putElasticGpuSpecifications")
    def put_elastic_gpu_specifications(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LaunchTemplateElasticGpuSpecifications", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c036765e0274fa46aee9719df2d45de6892f4023be58ae045e594d2a85200786)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putElasticGpuSpecifications", [value]))

    @jsii.member(jsii_name="putElasticInferenceAccelerator")
    def put_elastic_inference_accelerator(self, *, type: builtins.str) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#type LaunchTemplate#type}.
        '''
        value = LaunchTemplateElasticInferenceAccelerator(type=type)

        return typing.cast(None, jsii.invoke(self, "putElasticInferenceAccelerator", [value]))

    @jsii.member(jsii_name="putEnclaveOptions")
    def put_enclave_options(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#enabled LaunchTemplate#enabled}.
        '''
        value = LaunchTemplateEnclaveOptions(enabled=enabled)

        return typing.cast(None, jsii.invoke(self, "putEnclaveOptions", [value]))

    @jsii.member(jsii_name="putHibernationOptions")
    def put_hibernation_options(
        self,
        *,
        configured: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        '''
        :param configured: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#configured LaunchTemplate#configured}.
        '''
        value = LaunchTemplateHibernationOptions(configured=configured)

        return typing.cast(None, jsii.invoke(self, "putHibernationOptions", [value]))

    @jsii.member(jsii_name="putIamInstanceProfile")
    def put_iam_instance_profile(
        self,
        *,
        arn: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#arn LaunchTemplate#arn}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#name LaunchTemplate#name}.
        '''
        value = LaunchTemplateIamInstanceProfile(arn=arn, name=name)

        return typing.cast(None, jsii.invoke(self, "putIamInstanceProfile", [value]))

    @jsii.member(jsii_name="putInstanceMarketOptions")
    def put_instance_market_options(
        self,
        *,
        market_type: typing.Optional[builtins.str] = None,
        spot_options: typing.Optional[typing.Union["LaunchTemplateInstanceMarketOptionsSpotOptions", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param market_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#market_type LaunchTemplate#market_type}.
        :param spot_options: spot_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#spot_options LaunchTemplate#spot_options}
        '''
        value = LaunchTemplateInstanceMarketOptions(
            market_type=market_type, spot_options=spot_options
        )

        return typing.cast(None, jsii.invoke(self, "putInstanceMarketOptions", [value]))

    @jsii.member(jsii_name="putInstanceRequirements")
    def put_instance_requirements(
        self,
        *,
        memory_mib: typing.Union["LaunchTemplateInstanceRequirementsMemoryMib", typing.Dict[builtins.str, typing.Any]],
        vcpu_count: typing.Union["LaunchTemplateInstanceRequirementsVcpuCount", typing.Dict[builtins.str, typing.Any]],
        accelerator_count: typing.Optional[typing.Union["LaunchTemplateInstanceRequirementsAcceleratorCount", typing.Dict[builtins.str, typing.Any]]] = None,
        accelerator_manufacturers: typing.Optional[typing.Sequence[builtins.str]] = None,
        accelerator_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        accelerator_total_memory_mib: typing.Optional[typing.Union["LaunchTemplateInstanceRequirementsAcceleratorTotalMemoryMib", typing.Dict[builtins.str, typing.Any]]] = None,
        accelerator_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        bare_metal: typing.Optional[builtins.str] = None,
        baseline_ebs_bandwidth_mbps: typing.Optional[typing.Union["LaunchTemplateInstanceRequirementsBaselineEbsBandwidthMbps", typing.Dict[builtins.str, typing.Any]]] = None,
        burstable_performance: typing.Optional[builtins.str] = None,
        cpu_manufacturers: typing.Optional[typing.Sequence[builtins.str]] = None,
        excluded_instance_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        instance_generations: typing.Optional[typing.Sequence[builtins.str]] = None,
        local_storage: typing.Optional[builtins.str] = None,
        local_storage_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        memory_gib_per_vcpu: typing.Optional[typing.Union["LaunchTemplateInstanceRequirementsMemoryGibPerVcpu", typing.Dict[builtins.str, typing.Any]]] = None,
        network_interface_count: typing.Optional[typing.Union["LaunchTemplateInstanceRequirementsNetworkInterfaceCount", typing.Dict[builtins.str, typing.Any]]] = None,
        on_demand_max_price_percentage_over_lowest_price: typing.Optional[jsii.Number] = None,
        require_hibernate_support: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        spot_max_price_percentage_over_lowest_price: typing.Optional[jsii.Number] = None,
        total_local_storage_gb: typing.Optional[typing.Union["LaunchTemplateInstanceRequirementsTotalLocalStorageGb", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param memory_mib: memory_mib block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#memory_mib LaunchTemplate#memory_mib}
        :param vcpu_count: vcpu_count block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#vcpu_count LaunchTemplate#vcpu_count}
        :param accelerator_count: accelerator_count block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#accelerator_count LaunchTemplate#accelerator_count}
        :param accelerator_manufacturers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#accelerator_manufacturers LaunchTemplate#accelerator_manufacturers}.
        :param accelerator_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#accelerator_names LaunchTemplate#accelerator_names}.
        :param accelerator_total_memory_mib: accelerator_total_memory_mib block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#accelerator_total_memory_mib LaunchTemplate#accelerator_total_memory_mib}
        :param accelerator_types: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#accelerator_types LaunchTemplate#accelerator_types}.
        :param bare_metal: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#bare_metal LaunchTemplate#bare_metal}.
        :param baseline_ebs_bandwidth_mbps: baseline_ebs_bandwidth_mbps block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#baseline_ebs_bandwidth_mbps LaunchTemplate#baseline_ebs_bandwidth_mbps}
        :param burstable_performance: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#burstable_performance LaunchTemplate#burstable_performance}.
        :param cpu_manufacturers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#cpu_manufacturers LaunchTemplate#cpu_manufacturers}.
        :param excluded_instance_types: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#excluded_instance_types LaunchTemplate#excluded_instance_types}.
        :param instance_generations: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#instance_generations LaunchTemplate#instance_generations}.
        :param local_storage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#local_storage LaunchTemplate#local_storage}.
        :param local_storage_types: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#local_storage_types LaunchTemplate#local_storage_types}.
        :param memory_gib_per_vcpu: memory_gib_per_vcpu block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#memory_gib_per_vcpu LaunchTemplate#memory_gib_per_vcpu}
        :param network_interface_count: network_interface_count block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#network_interface_count LaunchTemplate#network_interface_count}
        :param on_demand_max_price_percentage_over_lowest_price: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#on_demand_max_price_percentage_over_lowest_price LaunchTemplate#on_demand_max_price_percentage_over_lowest_price}.
        :param require_hibernate_support: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#require_hibernate_support LaunchTemplate#require_hibernate_support}.
        :param spot_max_price_percentage_over_lowest_price: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#spot_max_price_percentage_over_lowest_price LaunchTemplate#spot_max_price_percentage_over_lowest_price}.
        :param total_local_storage_gb: total_local_storage_gb block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#total_local_storage_gb LaunchTemplate#total_local_storage_gb}
        '''
        value = LaunchTemplateInstanceRequirements(
            memory_mib=memory_mib,
            vcpu_count=vcpu_count,
            accelerator_count=accelerator_count,
            accelerator_manufacturers=accelerator_manufacturers,
            accelerator_names=accelerator_names,
            accelerator_total_memory_mib=accelerator_total_memory_mib,
            accelerator_types=accelerator_types,
            bare_metal=bare_metal,
            baseline_ebs_bandwidth_mbps=baseline_ebs_bandwidth_mbps,
            burstable_performance=burstable_performance,
            cpu_manufacturers=cpu_manufacturers,
            excluded_instance_types=excluded_instance_types,
            instance_generations=instance_generations,
            local_storage=local_storage,
            local_storage_types=local_storage_types,
            memory_gib_per_vcpu=memory_gib_per_vcpu,
            network_interface_count=network_interface_count,
            on_demand_max_price_percentage_over_lowest_price=on_demand_max_price_percentage_over_lowest_price,
            require_hibernate_support=require_hibernate_support,
            spot_max_price_percentage_over_lowest_price=spot_max_price_percentage_over_lowest_price,
            total_local_storage_gb=total_local_storage_gb,
        )

        return typing.cast(None, jsii.invoke(self, "putInstanceRequirements", [value]))

    @jsii.member(jsii_name="putLicenseSpecification")
    def put_license_specification(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LaunchTemplateLicenseSpecification", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f12a1bc7e0ea7259c260bf4380bc79aafa776200d9178cbc1d05305dfe1ff184)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLicenseSpecification", [value]))

    @jsii.member(jsii_name="putMaintenanceOptions")
    def put_maintenance_options(
        self,
        *,
        auto_recovery: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param auto_recovery: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#auto_recovery LaunchTemplate#auto_recovery}.
        '''
        value = LaunchTemplateMaintenanceOptions(auto_recovery=auto_recovery)

        return typing.cast(None, jsii.invoke(self, "putMaintenanceOptions", [value]))

    @jsii.member(jsii_name="putMetadataOptions")
    def put_metadata_options(
        self,
        *,
        http_endpoint: typing.Optional[builtins.str] = None,
        http_protocol_ipv6: typing.Optional[builtins.str] = None,
        http_put_response_hop_limit: typing.Optional[jsii.Number] = None,
        http_tokens: typing.Optional[builtins.str] = None,
        instance_metadata_tags: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param http_endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#http_endpoint LaunchTemplate#http_endpoint}.
        :param http_protocol_ipv6: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#http_protocol_ipv6 LaunchTemplate#http_protocol_ipv6}.
        :param http_put_response_hop_limit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#http_put_response_hop_limit LaunchTemplate#http_put_response_hop_limit}.
        :param http_tokens: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#http_tokens LaunchTemplate#http_tokens}.
        :param instance_metadata_tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#instance_metadata_tags LaunchTemplate#instance_metadata_tags}.
        '''
        value = LaunchTemplateMetadataOptions(
            http_endpoint=http_endpoint,
            http_protocol_ipv6=http_protocol_ipv6,
            http_put_response_hop_limit=http_put_response_hop_limit,
            http_tokens=http_tokens,
            instance_metadata_tags=instance_metadata_tags,
        )

        return typing.cast(None, jsii.invoke(self, "putMetadataOptions", [value]))

    @jsii.member(jsii_name="putMonitoring")
    def put_monitoring(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#enabled LaunchTemplate#enabled}.
        '''
        value = LaunchTemplateMonitoring(enabled=enabled)

        return typing.cast(None, jsii.invoke(self, "putMonitoring", [value]))

    @jsii.member(jsii_name="putNetworkInterfaces")
    def put_network_interfaces(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LaunchTemplateNetworkInterfaces", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8778b09eaec1830690cca41dfaaa59f633a32578460dc99a648de4772e0c054b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNetworkInterfaces", [value]))

    @jsii.member(jsii_name="putPlacement")
    def put_placement(
        self,
        *,
        affinity: typing.Optional[builtins.str] = None,
        availability_zone: typing.Optional[builtins.str] = None,
        group_name: typing.Optional[builtins.str] = None,
        host_id: typing.Optional[builtins.str] = None,
        host_resource_group_arn: typing.Optional[builtins.str] = None,
        partition_number: typing.Optional[jsii.Number] = None,
        spread_domain: typing.Optional[builtins.str] = None,
        tenancy: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param affinity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#affinity LaunchTemplate#affinity}.
        :param availability_zone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#availability_zone LaunchTemplate#availability_zone}.
        :param group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#group_name LaunchTemplate#group_name}.
        :param host_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#host_id LaunchTemplate#host_id}.
        :param host_resource_group_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#host_resource_group_arn LaunchTemplate#host_resource_group_arn}.
        :param partition_number: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#partition_number LaunchTemplate#partition_number}.
        :param spread_domain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#spread_domain LaunchTemplate#spread_domain}.
        :param tenancy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#tenancy LaunchTemplate#tenancy}.
        '''
        value = LaunchTemplatePlacement(
            affinity=affinity,
            availability_zone=availability_zone,
            group_name=group_name,
            host_id=host_id,
            host_resource_group_arn=host_resource_group_arn,
            partition_number=partition_number,
            spread_domain=spread_domain,
            tenancy=tenancy,
        )

        return typing.cast(None, jsii.invoke(self, "putPlacement", [value]))

    @jsii.member(jsii_name="putPrivateDnsNameOptions")
    def put_private_dns_name_options(
        self,
        *,
        enable_resource_name_dns_aaaa_record: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_resource_name_dns_a_record: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        hostname_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enable_resource_name_dns_aaaa_record: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#enable_resource_name_dns_aaaa_record LaunchTemplate#enable_resource_name_dns_aaaa_record}.
        :param enable_resource_name_dns_a_record: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#enable_resource_name_dns_a_record LaunchTemplate#enable_resource_name_dns_a_record}.
        :param hostname_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#hostname_type LaunchTemplate#hostname_type}.
        '''
        value = LaunchTemplatePrivateDnsNameOptions(
            enable_resource_name_dns_aaaa_record=enable_resource_name_dns_aaaa_record,
            enable_resource_name_dns_a_record=enable_resource_name_dns_a_record,
            hostname_type=hostname_type,
        )

        return typing.cast(None, jsii.invoke(self, "putPrivateDnsNameOptions", [value]))

    @jsii.member(jsii_name="putTagSpecifications")
    def put_tag_specifications(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LaunchTemplateTagSpecifications", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__853919fb79eabaf8a5f887a4a71d76cb4ed897ecfce24667184b653b125bd99d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTagSpecifications", [value]))

    @jsii.member(jsii_name="resetBlockDeviceMappings")
    def reset_block_device_mappings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBlockDeviceMappings", []))

    @jsii.member(jsii_name="resetCapacityReservationSpecification")
    def reset_capacity_reservation_specification(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCapacityReservationSpecification", []))

    @jsii.member(jsii_name="resetCpuOptions")
    def reset_cpu_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCpuOptions", []))

    @jsii.member(jsii_name="resetCreditSpecification")
    def reset_credit_specification(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreditSpecification", []))

    @jsii.member(jsii_name="resetDefaultVersion")
    def reset_default_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultVersion", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetDisableApiStop")
    def reset_disable_api_stop(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisableApiStop", []))

    @jsii.member(jsii_name="resetDisableApiTermination")
    def reset_disable_api_termination(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisableApiTermination", []))

    @jsii.member(jsii_name="resetEbsOptimized")
    def reset_ebs_optimized(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEbsOptimized", []))

    @jsii.member(jsii_name="resetElasticGpuSpecifications")
    def reset_elastic_gpu_specifications(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetElasticGpuSpecifications", []))

    @jsii.member(jsii_name="resetElasticInferenceAccelerator")
    def reset_elastic_inference_accelerator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetElasticInferenceAccelerator", []))

    @jsii.member(jsii_name="resetEnclaveOptions")
    def reset_enclave_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnclaveOptions", []))

    @jsii.member(jsii_name="resetHibernationOptions")
    def reset_hibernation_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHibernationOptions", []))

    @jsii.member(jsii_name="resetIamInstanceProfile")
    def reset_iam_instance_profile(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIamInstanceProfile", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetImageId")
    def reset_image_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImageId", []))

    @jsii.member(jsii_name="resetInstanceInitiatedShutdownBehavior")
    def reset_instance_initiated_shutdown_behavior(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceInitiatedShutdownBehavior", []))

    @jsii.member(jsii_name="resetInstanceMarketOptions")
    def reset_instance_market_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceMarketOptions", []))

    @jsii.member(jsii_name="resetInstanceRequirements")
    def reset_instance_requirements(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceRequirements", []))

    @jsii.member(jsii_name="resetInstanceType")
    def reset_instance_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceType", []))

    @jsii.member(jsii_name="resetKernelId")
    def reset_kernel_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKernelId", []))

    @jsii.member(jsii_name="resetKeyName")
    def reset_key_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyName", []))

    @jsii.member(jsii_name="resetLicenseSpecification")
    def reset_license_specification(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLicenseSpecification", []))

    @jsii.member(jsii_name="resetMaintenanceOptions")
    def reset_maintenance_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaintenanceOptions", []))

    @jsii.member(jsii_name="resetMetadataOptions")
    def reset_metadata_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetadataOptions", []))

    @jsii.member(jsii_name="resetMonitoring")
    def reset_monitoring(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMonitoring", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetNamePrefix")
    def reset_name_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamePrefix", []))

    @jsii.member(jsii_name="resetNetworkInterfaces")
    def reset_network_interfaces(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworkInterfaces", []))

    @jsii.member(jsii_name="resetPlacement")
    def reset_placement(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPlacement", []))

    @jsii.member(jsii_name="resetPrivateDnsNameOptions")
    def reset_private_dns_name_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateDnsNameOptions", []))

    @jsii.member(jsii_name="resetRamDiskId")
    def reset_ram_disk_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRamDiskId", []))

    @jsii.member(jsii_name="resetSecurityGroupNames")
    def reset_security_group_names(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecurityGroupNames", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetTagSpecifications")
    def reset_tag_specifications(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagSpecifications", []))

    @jsii.member(jsii_name="resetUpdateDefaultVersion")
    def reset_update_default_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdateDefaultVersion", []))

    @jsii.member(jsii_name="resetUserData")
    def reset_user_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserData", []))

    @jsii.member(jsii_name="resetVpcSecurityGroupIds")
    def reset_vpc_security_group_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVpcSecurityGroupIds", []))

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
    @jsii.member(jsii_name="blockDeviceMappings")
    def block_device_mappings(self) -> "LaunchTemplateBlockDeviceMappingsList":
        return typing.cast("LaunchTemplateBlockDeviceMappingsList", jsii.get(self, "blockDeviceMappings"))

    @builtins.property
    @jsii.member(jsii_name="capacityReservationSpecification")
    def capacity_reservation_specification(
        self,
    ) -> "LaunchTemplateCapacityReservationSpecificationOutputReference":
        return typing.cast("LaunchTemplateCapacityReservationSpecificationOutputReference", jsii.get(self, "capacityReservationSpecification"))

    @builtins.property
    @jsii.member(jsii_name="cpuOptions")
    def cpu_options(self) -> "LaunchTemplateCpuOptionsOutputReference":
        return typing.cast("LaunchTemplateCpuOptionsOutputReference", jsii.get(self, "cpuOptions"))

    @builtins.property
    @jsii.member(jsii_name="creditSpecification")
    def credit_specification(
        self,
    ) -> "LaunchTemplateCreditSpecificationOutputReference":
        return typing.cast("LaunchTemplateCreditSpecificationOutputReference", jsii.get(self, "creditSpecification"))

    @builtins.property
    @jsii.member(jsii_name="elasticGpuSpecifications")
    def elastic_gpu_specifications(
        self,
    ) -> "LaunchTemplateElasticGpuSpecificationsList":
        return typing.cast("LaunchTemplateElasticGpuSpecificationsList", jsii.get(self, "elasticGpuSpecifications"))

    @builtins.property
    @jsii.member(jsii_name="elasticInferenceAccelerator")
    def elastic_inference_accelerator(
        self,
    ) -> "LaunchTemplateElasticInferenceAcceleratorOutputReference":
        return typing.cast("LaunchTemplateElasticInferenceAcceleratorOutputReference", jsii.get(self, "elasticInferenceAccelerator"))

    @builtins.property
    @jsii.member(jsii_name="enclaveOptions")
    def enclave_options(self) -> "LaunchTemplateEnclaveOptionsOutputReference":
        return typing.cast("LaunchTemplateEnclaveOptionsOutputReference", jsii.get(self, "enclaveOptions"))

    @builtins.property
    @jsii.member(jsii_name="hibernationOptions")
    def hibernation_options(self) -> "LaunchTemplateHibernationOptionsOutputReference":
        return typing.cast("LaunchTemplateHibernationOptionsOutputReference", jsii.get(self, "hibernationOptions"))

    @builtins.property
    @jsii.member(jsii_name="iamInstanceProfile")
    def iam_instance_profile(self) -> "LaunchTemplateIamInstanceProfileOutputReference":
        return typing.cast("LaunchTemplateIamInstanceProfileOutputReference", jsii.get(self, "iamInstanceProfile"))

    @builtins.property
    @jsii.member(jsii_name="instanceMarketOptions")
    def instance_market_options(
        self,
    ) -> "LaunchTemplateInstanceMarketOptionsOutputReference":
        return typing.cast("LaunchTemplateInstanceMarketOptionsOutputReference", jsii.get(self, "instanceMarketOptions"))

    @builtins.property
    @jsii.member(jsii_name="instanceRequirements")
    def instance_requirements(
        self,
    ) -> "LaunchTemplateInstanceRequirementsOutputReference":
        return typing.cast("LaunchTemplateInstanceRequirementsOutputReference", jsii.get(self, "instanceRequirements"))

    @builtins.property
    @jsii.member(jsii_name="latestVersion")
    def latest_version(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "latestVersion"))

    @builtins.property
    @jsii.member(jsii_name="licenseSpecification")
    def license_specification(self) -> "LaunchTemplateLicenseSpecificationList":
        return typing.cast("LaunchTemplateLicenseSpecificationList", jsii.get(self, "licenseSpecification"))

    @builtins.property
    @jsii.member(jsii_name="maintenanceOptions")
    def maintenance_options(self) -> "LaunchTemplateMaintenanceOptionsOutputReference":
        return typing.cast("LaunchTemplateMaintenanceOptionsOutputReference", jsii.get(self, "maintenanceOptions"))

    @builtins.property
    @jsii.member(jsii_name="metadataOptions")
    def metadata_options(self) -> "LaunchTemplateMetadataOptionsOutputReference":
        return typing.cast("LaunchTemplateMetadataOptionsOutputReference", jsii.get(self, "metadataOptions"))

    @builtins.property
    @jsii.member(jsii_name="monitoring")
    def monitoring(self) -> "LaunchTemplateMonitoringOutputReference":
        return typing.cast("LaunchTemplateMonitoringOutputReference", jsii.get(self, "monitoring"))

    @builtins.property
    @jsii.member(jsii_name="networkInterfaces")
    def network_interfaces(self) -> "LaunchTemplateNetworkInterfacesList":
        return typing.cast("LaunchTemplateNetworkInterfacesList", jsii.get(self, "networkInterfaces"))

    @builtins.property
    @jsii.member(jsii_name="placement")
    def placement(self) -> "LaunchTemplatePlacementOutputReference":
        return typing.cast("LaunchTemplatePlacementOutputReference", jsii.get(self, "placement"))

    @builtins.property
    @jsii.member(jsii_name="privateDnsNameOptions")
    def private_dns_name_options(
        self,
    ) -> "LaunchTemplatePrivateDnsNameOptionsOutputReference":
        return typing.cast("LaunchTemplatePrivateDnsNameOptionsOutputReference", jsii.get(self, "privateDnsNameOptions"))

    @builtins.property
    @jsii.member(jsii_name="tagSpecifications")
    def tag_specifications(self) -> "LaunchTemplateTagSpecificationsList":
        return typing.cast("LaunchTemplateTagSpecificationsList", jsii.get(self, "tagSpecifications"))

    @builtins.property
    @jsii.member(jsii_name="blockDeviceMappingsInput")
    def block_device_mappings_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LaunchTemplateBlockDeviceMappings"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LaunchTemplateBlockDeviceMappings"]]], jsii.get(self, "blockDeviceMappingsInput"))

    @builtins.property
    @jsii.member(jsii_name="capacityReservationSpecificationInput")
    def capacity_reservation_specification_input(
        self,
    ) -> typing.Optional["LaunchTemplateCapacityReservationSpecification"]:
        return typing.cast(typing.Optional["LaunchTemplateCapacityReservationSpecification"], jsii.get(self, "capacityReservationSpecificationInput"))

    @builtins.property
    @jsii.member(jsii_name="cpuOptionsInput")
    def cpu_options_input(self) -> typing.Optional["LaunchTemplateCpuOptions"]:
        return typing.cast(typing.Optional["LaunchTemplateCpuOptions"], jsii.get(self, "cpuOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="creditSpecificationInput")
    def credit_specification_input(
        self,
    ) -> typing.Optional["LaunchTemplateCreditSpecification"]:
        return typing.cast(typing.Optional["LaunchTemplateCreditSpecification"], jsii.get(self, "creditSpecificationInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultVersionInput")
    def default_version_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "defaultVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="disableApiStopInput")
    def disable_api_stop_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "disableApiStopInput"))

    @builtins.property
    @jsii.member(jsii_name="disableApiTerminationInput")
    def disable_api_termination_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "disableApiTerminationInput"))

    @builtins.property
    @jsii.member(jsii_name="ebsOptimizedInput")
    def ebs_optimized_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ebsOptimizedInput"))

    @builtins.property
    @jsii.member(jsii_name="elasticGpuSpecificationsInput")
    def elastic_gpu_specifications_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LaunchTemplateElasticGpuSpecifications"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LaunchTemplateElasticGpuSpecifications"]]], jsii.get(self, "elasticGpuSpecificationsInput"))

    @builtins.property
    @jsii.member(jsii_name="elasticInferenceAcceleratorInput")
    def elastic_inference_accelerator_input(
        self,
    ) -> typing.Optional["LaunchTemplateElasticInferenceAccelerator"]:
        return typing.cast(typing.Optional["LaunchTemplateElasticInferenceAccelerator"], jsii.get(self, "elasticInferenceAcceleratorInput"))

    @builtins.property
    @jsii.member(jsii_name="enclaveOptionsInput")
    def enclave_options_input(self) -> typing.Optional["LaunchTemplateEnclaveOptions"]:
        return typing.cast(typing.Optional["LaunchTemplateEnclaveOptions"], jsii.get(self, "enclaveOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="hibernationOptionsInput")
    def hibernation_options_input(
        self,
    ) -> typing.Optional["LaunchTemplateHibernationOptions"]:
        return typing.cast(typing.Optional["LaunchTemplateHibernationOptions"], jsii.get(self, "hibernationOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="iamInstanceProfileInput")
    def iam_instance_profile_input(
        self,
    ) -> typing.Optional["LaunchTemplateIamInstanceProfile"]:
        return typing.cast(typing.Optional["LaunchTemplateIamInstanceProfile"], jsii.get(self, "iamInstanceProfileInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="imageIdInput")
    def image_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageIdInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceInitiatedShutdownBehaviorInput")
    def instance_initiated_shutdown_behavior_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceInitiatedShutdownBehaviorInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceMarketOptionsInput")
    def instance_market_options_input(
        self,
    ) -> typing.Optional["LaunchTemplateInstanceMarketOptions"]:
        return typing.cast(typing.Optional["LaunchTemplateInstanceMarketOptions"], jsii.get(self, "instanceMarketOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceRequirementsInput")
    def instance_requirements_input(
        self,
    ) -> typing.Optional["LaunchTemplateInstanceRequirements"]:
        return typing.cast(typing.Optional["LaunchTemplateInstanceRequirements"], jsii.get(self, "instanceRequirementsInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceTypeInput")
    def instance_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="kernelIdInput")
    def kernel_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kernelIdInput"))

    @builtins.property
    @jsii.member(jsii_name="keyNameInput")
    def key_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyNameInput"))

    @builtins.property
    @jsii.member(jsii_name="licenseSpecificationInput")
    def license_specification_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LaunchTemplateLicenseSpecification"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LaunchTemplateLicenseSpecification"]]], jsii.get(self, "licenseSpecificationInput"))

    @builtins.property
    @jsii.member(jsii_name="maintenanceOptionsInput")
    def maintenance_options_input(
        self,
    ) -> typing.Optional["LaunchTemplateMaintenanceOptions"]:
        return typing.cast(typing.Optional["LaunchTemplateMaintenanceOptions"], jsii.get(self, "maintenanceOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="metadataOptionsInput")
    def metadata_options_input(
        self,
    ) -> typing.Optional["LaunchTemplateMetadataOptions"]:
        return typing.cast(typing.Optional["LaunchTemplateMetadataOptions"], jsii.get(self, "metadataOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="monitoringInput")
    def monitoring_input(self) -> typing.Optional["LaunchTemplateMonitoring"]:
        return typing.cast(typing.Optional["LaunchTemplateMonitoring"], jsii.get(self, "monitoringInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="namePrefixInput")
    def name_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namePrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="networkInterfacesInput")
    def network_interfaces_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LaunchTemplateNetworkInterfaces"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LaunchTemplateNetworkInterfaces"]]], jsii.get(self, "networkInterfacesInput"))

    @builtins.property
    @jsii.member(jsii_name="placementInput")
    def placement_input(self) -> typing.Optional["LaunchTemplatePlacement"]:
        return typing.cast(typing.Optional["LaunchTemplatePlacement"], jsii.get(self, "placementInput"))

    @builtins.property
    @jsii.member(jsii_name="privateDnsNameOptionsInput")
    def private_dns_name_options_input(
        self,
    ) -> typing.Optional["LaunchTemplatePrivateDnsNameOptions"]:
        return typing.cast(typing.Optional["LaunchTemplatePrivateDnsNameOptions"], jsii.get(self, "privateDnsNameOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="ramDiskIdInput")
    def ram_disk_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ramDiskIdInput"))

    @builtins.property
    @jsii.member(jsii_name="securityGroupNamesInput")
    def security_group_names_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityGroupNamesInput"))

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
    @jsii.member(jsii_name="tagSpecificationsInput")
    def tag_specifications_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LaunchTemplateTagSpecifications"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LaunchTemplateTagSpecifications"]]], jsii.get(self, "tagSpecificationsInput"))

    @builtins.property
    @jsii.member(jsii_name="updateDefaultVersionInput")
    def update_default_version_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "updateDefaultVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="userDataInput")
    def user_data_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userDataInput"))

    @builtins.property
    @jsii.member(jsii_name="vpcSecurityGroupIdsInput")
    def vpc_security_group_ids_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "vpcSecurityGroupIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultVersion")
    def default_version(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "defaultVersion"))

    @default_version.setter
    def default_version(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4559e3ce7f9d9f897bf8512487632f790ef6ae165f7bca55078d6a167666c7cc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultVersion", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7e914bafa8f31fe20a4ffa290cceb470201240f6f2419bdd484ba098bf42cc0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="disableApiStop")
    def disable_api_stop(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "disableApiStop"))

    @disable_api_stop.setter
    def disable_api_stop(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b9a2141580710a2f0a51745ad9bf72f4d60097ebca04083e9c4a9a82063b11e1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableApiStop", value)

    @builtins.property
    @jsii.member(jsii_name="disableApiTermination")
    def disable_api_termination(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "disableApiTermination"))

    @disable_api_termination.setter
    def disable_api_termination(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__efb5f7c734499b17cf2cc05803d0bacd0233f73ba26fd73edd520ac777f212f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableApiTermination", value)

    @builtins.property
    @jsii.member(jsii_name="ebsOptimized")
    def ebs_optimized(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ebsOptimized"))

    @ebs_optimized.setter
    def ebs_optimized(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c426201ed3599c2aef4eaf9df0f87dfb0fcc88c43821e79fd76b8eea846faab2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ebsOptimized", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5aeab1788f2156b906dd2c939ac370fb323f4688f58cc495dc410e0486ae2450)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="imageId")
    def image_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "imageId"))

    @image_id.setter
    def image_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79ca8d99502ee10a3bf3bb3a77876434b0897b9b1606b831ffc8c649c148e534)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageId", value)

    @builtins.property
    @jsii.member(jsii_name="instanceInitiatedShutdownBehavior")
    def instance_initiated_shutdown_behavior(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceInitiatedShutdownBehavior"))

    @instance_initiated_shutdown_behavior.setter
    def instance_initiated_shutdown_behavior(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__902fd9c5cb76741508c99b42b86f4fbf4a1475484505e5438532acbdf3346c92)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceInitiatedShutdownBehavior", value)

    @builtins.property
    @jsii.member(jsii_name="instanceType")
    def instance_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceType"))

    @instance_type.setter
    def instance_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82a5e5215195bc7b2be2ddcf3794ca737372efd75145069ff4be29f9ba211a7b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceType", value)

    @builtins.property
    @jsii.member(jsii_name="kernelId")
    def kernel_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kernelId"))

    @kernel_id.setter
    def kernel_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39c9e70123250a416454a0ea5b750d2aeaf34569afee619c91f5034056fd8f01)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kernelId", value)

    @builtins.property
    @jsii.member(jsii_name="keyName")
    def key_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyName"))

    @key_name.setter
    def key_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d178dd21963f2b24e231bfcdf7c2c60ad9fbfba2669b21ba9657280f2e54a1f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyName", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a656dbbc81bfa5e607c8ab4f35191b4c0fd557dc66b9ebaf3501261dc57ba8f0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namePrefix")
    def name_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namePrefix"))

    @name_prefix.setter
    def name_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d71257311c82cbd4ba496307a78b79ddfe51d7fa165c15534c40a1024477393)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namePrefix", value)

    @builtins.property
    @jsii.member(jsii_name="ramDiskId")
    def ram_disk_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ramDiskId"))

    @ram_disk_id.setter
    def ram_disk_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__758331a3236117c94645153819fc470c15928324519bff1a26056f996dd3966e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ramDiskId", value)

    @builtins.property
    @jsii.member(jsii_name="securityGroupNames")
    def security_group_names(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "securityGroupNames"))

    @security_group_names.setter
    def security_group_names(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9210b48f682385fd160e167d0d2f406a7a24e095e94d09d9a195f81765e9f714)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroupNames", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72c20db47193864194e94983168089de27d7949749cef189cd3010581e9f71ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6d55a3b550c48f1a0c007e10d0c070a7935901a708a2dd0a98c46740f38babc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)

    @builtins.property
    @jsii.member(jsii_name="updateDefaultVersion")
    def update_default_version(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "updateDefaultVersion"))

    @update_default_version.setter
    def update_default_version(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3954be3f86317a8fffe24666a6d2b29b07359bd5dd70de3583113aeeb1b4cb7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "updateDefaultVersion", value)

    @builtins.property
    @jsii.member(jsii_name="userData")
    def user_data(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userData"))

    @user_data.setter
    def user_data(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__627bf7e8296d7d33206faa59b4a49a704ac1bbee7e683ff82e59ebfc18c3a170)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userData", value)

    @builtins.property
    @jsii.member(jsii_name="vpcSecurityGroupIds")
    def vpc_security_group_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "vpcSecurityGroupIds"))

    @vpc_security_group_ids.setter
    def vpc_security_group_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f3a1b84763a2e6b5db7b89af787349002a0cf127a068128beac5d9d193f2f2d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcSecurityGroupIds", value)


@jsii.data_type(
    jsii_type="aws.launchTemplate.LaunchTemplateBlockDeviceMappings",
    jsii_struct_bases=[],
    name_mapping={
        "device_name": "deviceName",
        "ebs": "ebs",
        "no_device": "noDevice",
        "virtual_name": "virtualName",
    },
)
class LaunchTemplateBlockDeviceMappings:
    def __init__(
        self,
        *,
        device_name: typing.Optional[builtins.str] = None,
        ebs: typing.Optional[typing.Union["LaunchTemplateBlockDeviceMappingsEbs", typing.Dict[builtins.str, typing.Any]]] = None,
        no_device: typing.Optional[builtins.str] = None,
        virtual_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param device_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#device_name LaunchTemplate#device_name}.
        :param ebs: ebs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#ebs LaunchTemplate#ebs}
        :param no_device: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#no_device LaunchTemplate#no_device}.
        :param virtual_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#virtual_name LaunchTemplate#virtual_name}.
        '''
        if isinstance(ebs, dict):
            ebs = LaunchTemplateBlockDeviceMappingsEbs(**ebs)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6abe3b45efee3f1d547bd9fbdce5d9da58f6c3ad2770b684beab536236c19919)
            check_type(argname="argument device_name", value=device_name, expected_type=type_hints["device_name"])
            check_type(argname="argument ebs", value=ebs, expected_type=type_hints["ebs"])
            check_type(argname="argument no_device", value=no_device, expected_type=type_hints["no_device"])
            check_type(argname="argument virtual_name", value=virtual_name, expected_type=type_hints["virtual_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if device_name is not None:
            self._values["device_name"] = device_name
        if ebs is not None:
            self._values["ebs"] = ebs
        if no_device is not None:
            self._values["no_device"] = no_device
        if virtual_name is not None:
            self._values["virtual_name"] = virtual_name

    @builtins.property
    def device_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#device_name LaunchTemplate#device_name}.'''
        result = self._values.get("device_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ebs(self) -> typing.Optional["LaunchTemplateBlockDeviceMappingsEbs"]:
        '''ebs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#ebs LaunchTemplate#ebs}
        '''
        result = self._values.get("ebs")
        return typing.cast(typing.Optional["LaunchTemplateBlockDeviceMappingsEbs"], result)

    @builtins.property
    def no_device(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#no_device LaunchTemplate#no_device}.'''
        result = self._values.get("no_device")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def virtual_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#virtual_name LaunchTemplate#virtual_name}.'''
        result = self._values.get("virtual_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LaunchTemplateBlockDeviceMappings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.launchTemplate.LaunchTemplateBlockDeviceMappingsEbs",
    jsii_struct_bases=[],
    name_mapping={
        "delete_on_termination": "deleteOnTermination",
        "encrypted": "encrypted",
        "iops": "iops",
        "kms_key_id": "kmsKeyId",
        "snapshot_id": "snapshotId",
        "throughput": "throughput",
        "volume_size": "volumeSize",
        "volume_type": "volumeType",
    },
)
class LaunchTemplateBlockDeviceMappingsEbs:
    def __init__(
        self,
        *,
        delete_on_termination: typing.Optional[builtins.str] = None,
        encrypted: typing.Optional[builtins.str] = None,
        iops: typing.Optional[jsii.Number] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        snapshot_id: typing.Optional[builtins.str] = None,
        throughput: typing.Optional[jsii.Number] = None,
        volume_size: typing.Optional[jsii.Number] = None,
        volume_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param delete_on_termination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#delete_on_termination LaunchTemplate#delete_on_termination}.
        :param encrypted: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#encrypted LaunchTemplate#encrypted}.
        :param iops: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#iops LaunchTemplate#iops}.
        :param kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#kms_key_id LaunchTemplate#kms_key_id}.
        :param snapshot_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#snapshot_id LaunchTemplate#snapshot_id}.
        :param throughput: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#throughput LaunchTemplate#throughput}.
        :param volume_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#volume_size LaunchTemplate#volume_size}.
        :param volume_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#volume_type LaunchTemplate#volume_type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82d54e2898f7a02489de9a607f8ee28ffb148a0869af5360d0bc3a80b5c40545)
            check_type(argname="argument delete_on_termination", value=delete_on_termination, expected_type=type_hints["delete_on_termination"])
            check_type(argname="argument encrypted", value=encrypted, expected_type=type_hints["encrypted"])
            check_type(argname="argument iops", value=iops, expected_type=type_hints["iops"])
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            check_type(argname="argument snapshot_id", value=snapshot_id, expected_type=type_hints["snapshot_id"])
            check_type(argname="argument throughput", value=throughput, expected_type=type_hints["throughput"])
            check_type(argname="argument volume_size", value=volume_size, expected_type=type_hints["volume_size"])
            check_type(argname="argument volume_type", value=volume_type, expected_type=type_hints["volume_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if delete_on_termination is not None:
            self._values["delete_on_termination"] = delete_on_termination
        if encrypted is not None:
            self._values["encrypted"] = encrypted
        if iops is not None:
            self._values["iops"] = iops
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if snapshot_id is not None:
            self._values["snapshot_id"] = snapshot_id
        if throughput is not None:
            self._values["throughput"] = throughput
        if volume_size is not None:
            self._values["volume_size"] = volume_size
        if volume_type is not None:
            self._values["volume_type"] = volume_type

    @builtins.property
    def delete_on_termination(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#delete_on_termination LaunchTemplate#delete_on_termination}.'''
        result = self._values.get("delete_on_termination")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encrypted(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#encrypted LaunchTemplate#encrypted}.'''
        result = self._values.get("encrypted")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def iops(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#iops LaunchTemplate#iops}.'''
        result = self._values.get("iops")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#kms_key_id LaunchTemplate#kms_key_id}.'''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def snapshot_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#snapshot_id LaunchTemplate#snapshot_id}.'''
        result = self._values.get("snapshot_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def throughput(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#throughput LaunchTemplate#throughput}.'''
        result = self._values.get("throughput")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def volume_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#volume_size LaunchTemplate#volume_size}.'''
        result = self._values.get("volume_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def volume_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#volume_type LaunchTemplate#volume_type}.'''
        result = self._values.get("volume_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LaunchTemplateBlockDeviceMappingsEbs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LaunchTemplateBlockDeviceMappingsEbsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.launchTemplate.LaunchTemplateBlockDeviceMappingsEbsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__761b4bc1d6b32644519d919be53ac3751e59a8d587e346ddaaebbb61f0f0195c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDeleteOnTermination")
    def reset_delete_on_termination(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeleteOnTermination", []))

    @jsii.member(jsii_name="resetEncrypted")
    def reset_encrypted(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncrypted", []))

    @jsii.member(jsii_name="resetIops")
    def reset_iops(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIops", []))

    @jsii.member(jsii_name="resetKmsKeyId")
    def reset_kms_key_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKeyId", []))

    @jsii.member(jsii_name="resetSnapshotId")
    def reset_snapshot_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSnapshotId", []))

    @jsii.member(jsii_name="resetThroughput")
    def reset_throughput(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetThroughput", []))

    @jsii.member(jsii_name="resetVolumeSize")
    def reset_volume_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVolumeSize", []))

    @jsii.member(jsii_name="resetVolumeType")
    def reset_volume_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVolumeType", []))

    @builtins.property
    @jsii.member(jsii_name="deleteOnTerminationInput")
    def delete_on_termination_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteOnTerminationInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptedInput")
    def encrypted_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "encryptedInput"))

    @builtins.property
    @jsii.member(jsii_name="iopsInput")
    def iops_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "iopsInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyIdInput")
    def kms_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="snapshotIdInput")
    def snapshot_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "snapshotIdInput"))

    @builtins.property
    @jsii.member(jsii_name="throughputInput")
    def throughput_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "throughputInput"))

    @builtins.property
    @jsii.member(jsii_name="volumeSizeInput")
    def volume_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "volumeSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="volumeTypeInput")
    def volume_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "volumeTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteOnTermination")
    def delete_on_termination(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deleteOnTermination"))

    @delete_on_termination.setter
    def delete_on_termination(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3bb9ef6965d31623006966973cce6f58b66600f3499dac8d3c3264347c70edfc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deleteOnTermination", value)

    @builtins.property
    @jsii.member(jsii_name="encrypted")
    def encrypted(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "encrypted"))

    @encrypted.setter
    def encrypted(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6094b1f082c1899dcf4fe4c676bb0c7de019ccc948a9819ba0d6e15cbdbb1481)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encrypted", value)

    @builtins.property
    @jsii.member(jsii_name="iops")
    def iops(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "iops"))

    @iops.setter
    def iops(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__345495ce39e2785758252d3356bb76da80e6838a124e3b9ff677f14de955ceb9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iops", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7a480a560d05e892c0b016f136f840a544988271e6c3e3877bbef8593b32183)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="snapshotId")
    def snapshot_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "snapshotId"))

    @snapshot_id.setter
    def snapshot_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__291c4c6f01517aaf324274ab7d777c37d2ef9095a992ff5c75e1c6ebe9873366)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snapshotId", value)

    @builtins.property
    @jsii.member(jsii_name="throughput")
    def throughput(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "throughput"))

    @throughput.setter
    def throughput(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ba36c664f3798a445d409b24a7fda555c10dd1f14069d2085426085c0fd0c5e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "throughput", value)

    @builtins.property
    @jsii.member(jsii_name="volumeSize")
    def volume_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "volumeSize"))

    @volume_size.setter
    def volume_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__784cae271a58339148460db47a1d65e854b2f3ed44d29d26c27dec1533e95172)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeSize", value)

    @builtins.property
    @jsii.member(jsii_name="volumeType")
    def volume_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "volumeType"))

    @volume_type.setter
    def volume_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12ff0e463b14f4e542bb8abd3556e00826c467581263f3bc9e63f649ceef4107)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LaunchTemplateBlockDeviceMappingsEbs]:
        return typing.cast(typing.Optional[LaunchTemplateBlockDeviceMappingsEbs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LaunchTemplateBlockDeviceMappingsEbs],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5bfa9df2bcd15f7ec3796d09f6c8f71f772ac5b1a02853359e409c299dc3c6c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LaunchTemplateBlockDeviceMappingsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.launchTemplate.LaunchTemplateBlockDeviceMappingsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__de27766becdfc5b93c46e7c6d01090c39a80f8b70bc8f5e5793f226c0cfeb421)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LaunchTemplateBlockDeviceMappingsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2961dde1c5517e326e589526f1a8b4e4b3f86216f2d6c10ae760473616802933)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LaunchTemplateBlockDeviceMappingsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ccd22f4d78ebff3b56b656c7186ef741471a4e346d3675d3074ace0656773e8b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__480a551086dbe6d867cf3f8811872e8de069721b47355e3bb6f1f5df337c9e62)
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
            type_hints = typing.get_type_hints(_typecheckingstub__09d52645fae0b863c296fd667912169390a7c6e922c6bf54b42d0932f887ace1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LaunchTemplateBlockDeviceMappings]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LaunchTemplateBlockDeviceMappings]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LaunchTemplateBlockDeviceMappings]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dbcb31f038735cf9cccbdcee36d23b630c647a3c1835c60e9bb3839a0063a08b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LaunchTemplateBlockDeviceMappingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.launchTemplate.LaunchTemplateBlockDeviceMappingsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__25b4ff7b5a85bfa47c1f8b705efd51ae601c298447fa5e3d20ab003a1ee0070b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putEbs")
    def put_ebs(
        self,
        *,
        delete_on_termination: typing.Optional[builtins.str] = None,
        encrypted: typing.Optional[builtins.str] = None,
        iops: typing.Optional[jsii.Number] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        snapshot_id: typing.Optional[builtins.str] = None,
        throughput: typing.Optional[jsii.Number] = None,
        volume_size: typing.Optional[jsii.Number] = None,
        volume_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param delete_on_termination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#delete_on_termination LaunchTemplate#delete_on_termination}.
        :param encrypted: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#encrypted LaunchTemplate#encrypted}.
        :param iops: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#iops LaunchTemplate#iops}.
        :param kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#kms_key_id LaunchTemplate#kms_key_id}.
        :param snapshot_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#snapshot_id LaunchTemplate#snapshot_id}.
        :param throughput: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#throughput LaunchTemplate#throughput}.
        :param volume_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#volume_size LaunchTemplate#volume_size}.
        :param volume_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#volume_type LaunchTemplate#volume_type}.
        '''
        value = LaunchTemplateBlockDeviceMappingsEbs(
            delete_on_termination=delete_on_termination,
            encrypted=encrypted,
            iops=iops,
            kms_key_id=kms_key_id,
            snapshot_id=snapshot_id,
            throughput=throughput,
            volume_size=volume_size,
            volume_type=volume_type,
        )

        return typing.cast(None, jsii.invoke(self, "putEbs", [value]))

    @jsii.member(jsii_name="resetDeviceName")
    def reset_device_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeviceName", []))

    @jsii.member(jsii_name="resetEbs")
    def reset_ebs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEbs", []))

    @jsii.member(jsii_name="resetNoDevice")
    def reset_no_device(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNoDevice", []))

    @jsii.member(jsii_name="resetVirtualName")
    def reset_virtual_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVirtualName", []))

    @builtins.property
    @jsii.member(jsii_name="ebs")
    def ebs(self) -> LaunchTemplateBlockDeviceMappingsEbsOutputReference:
        return typing.cast(LaunchTemplateBlockDeviceMappingsEbsOutputReference, jsii.get(self, "ebs"))

    @builtins.property
    @jsii.member(jsii_name="deviceNameInput")
    def device_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deviceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="ebsInput")
    def ebs_input(self) -> typing.Optional[LaunchTemplateBlockDeviceMappingsEbs]:
        return typing.cast(typing.Optional[LaunchTemplateBlockDeviceMappingsEbs], jsii.get(self, "ebsInput"))

    @builtins.property
    @jsii.member(jsii_name="noDeviceInput")
    def no_device_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "noDeviceInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualNameInput")
    def virtual_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "virtualNameInput"))

    @builtins.property
    @jsii.member(jsii_name="deviceName")
    def device_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deviceName"))

    @device_name.setter
    def device_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a4402ea582a9d8e5850e1b86ff06fb9cd661abb305ce3d4a85eac149696b098)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deviceName", value)

    @builtins.property
    @jsii.member(jsii_name="noDevice")
    def no_device(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "noDevice"))

    @no_device.setter
    def no_device(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__145f56bfd39894290e4b0bb66599f810af830031795109e4dcbaa1594f1eb6df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "noDevice", value)

    @builtins.property
    @jsii.member(jsii_name="virtualName")
    def virtual_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "virtualName"))

    @virtual_name.setter
    def virtual_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b91547071acc58d056347d431aa5a5dc183106170e097a70ffe7e5a274a8603)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LaunchTemplateBlockDeviceMappings, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LaunchTemplateBlockDeviceMappings, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LaunchTemplateBlockDeviceMappings, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__858cd6a9b3314fdd286980c8aa76fa19048ffb5a2d5adae377e939dc00b67268)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.launchTemplate.LaunchTemplateCapacityReservationSpecification",
    jsii_struct_bases=[],
    name_mapping={
        "capacity_reservation_preference": "capacityReservationPreference",
        "capacity_reservation_target": "capacityReservationTarget",
    },
)
class LaunchTemplateCapacityReservationSpecification:
    def __init__(
        self,
        *,
        capacity_reservation_preference: typing.Optional[builtins.str] = None,
        capacity_reservation_target: typing.Optional[typing.Union["LaunchTemplateCapacityReservationSpecificationCapacityReservationTarget", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param capacity_reservation_preference: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#capacity_reservation_preference LaunchTemplate#capacity_reservation_preference}.
        :param capacity_reservation_target: capacity_reservation_target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#capacity_reservation_target LaunchTemplate#capacity_reservation_target}
        '''
        if isinstance(capacity_reservation_target, dict):
            capacity_reservation_target = LaunchTemplateCapacityReservationSpecificationCapacityReservationTarget(**capacity_reservation_target)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62193771ae313af4090564e8796213a59581230a7c3936af428d4637da8375bd)
            check_type(argname="argument capacity_reservation_preference", value=capacity_reservation_preference, expected_type=type_hints["capacity_reservation_preference"])
            check_type(argname="argument capacity_reservation_target", value=capacity_reservation_target, expected_type=type_hints["capacity_reservation_target"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if capacity_reservation_preference is not None:
            self._values["capacity_reservation_preference"] = capacity_reservation_preference
        if capacity_reservation_target is not None:
            self._values["capacity_reservation_target"] = capacity_reservation_target

    @builtins.property
    def capacity_reservation_preference(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#capacity_reservation_preference LaunchTemplate#capacity_reservation_preference}.'''
        result = self._values.get("capacity_reservation_preference")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def capacity_reservation_target(
        self,
    ) -> typing.Optional["LaunchTemplateCapacityReservationSpecificationCapacityReservationTarget"]:
        '''capacity_reservation_target block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#capacity_reservation_target LaunchTemplate#capacity_reservation_target}
        '''
        result = self._values.get("capacity_reservation_target")
        return typing.cast(typing.Optional["LaunchTemplateCapacityReservationSpecificationCapacityReservationTarget"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LaunchTemplateCapacityReservationSpecification(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.launchTemplate.LaunchTemplateCapacityReservationSpecificationCapacityReservationTarget",
    jsii_struct_bases=[],
    name_mapping={
        "capacity_reservation_id": "capacityReservationId",
        "capacity_reservation_resource_group_arn": "capacityReservationResourceGroupArn",
    },
)
class LaunchTemplateCapacityReservationSpecificationCapacityReservationTarget:
    def __init__(
        self,
        *,
        capacity_reservation_id: typing.Optional[builtins.str] = None,
        capacity_reservation_resource_group_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param capacity_reservation_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#capacity_reservation_id LaunchTemplate#capacity_reservation_id}.
        :param capacity_reservation_resource_group_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#capacity_reservation_resource_group_arn LaunchTemplate#capacity_reservation_resource_group_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61efb44ae748820ad8961342c3eb8229dd7ae92d9bdacbf85725ae8fa3a3d4c0)
            check_type(argname="argument capacity_reservation_id", value=capacity_reservation_id, expected_type=type_hints["capacity_reservation_id"])
            check_type(argname="argument capacity_reservation_resource_group_arn", value=capacity_reservation_resource_group_arn, expected_type=type_hints["capacity_reservation_resource_group_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if capacity_reservation_id is not None:
            self._values["capacity_reservation_id"] = capacity_reservation_id
        if capacity_reservation_resource_group_arn is not None:
            self._values["capacity_reservation_resource_group_arn"] = capacity_reservation_resource_group_arn

    @builtins.property
    def capacity_reservation_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#capacity_reservation_id LaunchTemplate#capacity_reservation_id}.'''
        result = self._values.get("capacity_reservation_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def capacity_reservation_resource_group_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#capacity_reservation_resource_group_arn LaunchTemplate#capacity_reservation_resource_group_arn}.'''
        result = self._values.get("capacity_reservation_resource_group_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LaunchTemplateCapacityReservationSpecificationCapacityReservationTarget(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LaunchTemplateCapacityReservationSpecificationCapacityReservationTargetOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.launchTemplate.LaunchTemplateCapacityReservationSpecificationCapacityReservationTargetOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__835ba0d542bc5b87fc32559306e0441b6a226a4a9e3e39d75f566b0ad3c9d10f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCapacityReservationId")
    def reset_capacity_reservation_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCapacityReservationId", []))

    @jsii.member(jsii_name="resetCapacityReservationResourceGroupArn")
    def reset_capacity_reservation_resource_group_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCapacityReservationResourceGroupArn", []))

    @builtins.property
    @jsii.member(jsii_name="capacityReservationIdInput")
    def capacity_reservation_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "capacityReservationIdInput"))

    @builtins.property
    @jsii.member(jsii_name="capacityReservationResourceGroupArnInput")
    def capacity_reservation_resource_group_arn_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "capacityReservationResourceGroupArnInput"))

    @builtins.property
    @jsii.member(jsii_name="capacityReservationId")
    def capacity_reservation_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "capacityReservationId"))

    @capacity_reservation_id.setter
    def capacity_reservation_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ffe04bc09de317c86c1fcf3262d86aca00252dcc0c6309bc5261e19886f5200c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "capacityReservationId", value)

    @builtins.property
    @jsii.member(jsii_name="capacityReservationResourceGroupArn")
    def capacity_reservation_resource_group_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "capacityReservationResourceGroupArn"))

    @capacity_reservation_resource_group_arn.setter
    def capacity_reservation_resource_group_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02745dccbb0de89ecd38cc29aa465a5af2a1ac5a2ff16e3ced1ad14be9fec49a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "capacityReservationResourceGroupArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LaunchTemplateCapacityReservationSpecificationCapacityReservationTarget]:
        return typing.cast(typing.Optional[LaunchTemplateCapacityReservationSpecificationCapacityReservationTarget], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LaunchTemplateCapacityReservationSpecificationCapacityReservationTarget],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ebff3557d14f128e4ade22bc738f7427105736e98f13ffafff13e244829d4479)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LaunchTemplateCapacityReservationSpecificationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.launchTemplate.LaunchTemplateCapacityReservationSpecificationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ff9b7094a1fcdfc47adab9a41d0f0e0e5fe541d574e0c66b3732df2abcc3129d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCapacityReservationTarget")
    def put_capacity_reservation_target(
        self,
        *,
        capacity_reservation_id: typing.Optional[builtins.str] = None,
        capacity_reservation_resource_group_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param capacity_reservation_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#capacity_reservation_id LaunchTemplate#capacity_reservation_id}.
        :param capacity_reservation_resource_group_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#capacity_reservation_resource_group_arn LaunchTemplate#capacity_reservation_resource_group_arn}.
        '''
        value = LaunchTemplateCapacityReservationSpecificationCapacityReservationTarget(
            capacity_reservation_id=capacity_reservation_id,
            capacity_reservation_resource_group_arn=capacity_reservation_resource_group_arn,
        )

        return typing.cast(None, jsii.invoke(self, "putCapacityReservationTarget", [value]))

    @jsii.member(jsii_name="resetCapacityReservationPreference")
    def reset_capacity_reservation_preference(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCapacityReservationPreference", []))

    @jsii.member(jsii_name="resetCapacityReservationTarget")
    def reset_capacity_reservation_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCapacityReservationTarget", []))

    @builtins.property
    @jsii.member(jsii_name="capacityReservationTarget")
    def capacity_reservation_target(
        self,
    ) -> LaunchTemplateCapacityReservationSpecificationCapacityReservationTargetOutputReference:
        return typing.cast(LaunchTemplateCapacityReservationSpecificationCapacityReservationTargetOutputReference, jsii.get(self, "capacityReservationTarget"))

    @builtins.property
    @jsii.member(jsii_name="capacityReservationPreferenceInput")
    def capacity_reservation_preference_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "capacityReservationPreferenceInput"))

    @builtins.property
    @jsii.member(jsii_name="capacityReservationTargetInput")
    def capacity_reservation_target_input(
        self,
    ) -> typing.Optional[LaunchTemplateCapacityReservationSpecificationCapacityReservationTarget]:
        return typing.cast(typing.Optional[LaunchTemplateCapacityReservationSpecificationCapacityReservationTarget], jsii.get(self, "capacityReservationTargetInput"))

    @builtins.property
    @jsii.member(jsii_name="capacityReservationPreference")
    def capacity_reservation_preference(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "capacityReservationPreference"))

    @capacity_reservation_preference.setter
    def capacity_reservation_preference(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f5a744b87edce96d2ddbc852c8ed65fe1cd15ac6535fc31a72a48c1cf12649a4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "capacityReservationPreference", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LaunchTemplateCapacityReservationSpecification]:
        return typing.cast(typing.Optional[LaunchTemplateCapacityReservationSpecification], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LaunchTemplateCapacityReservationSpecification],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c630dd386b16ad3f79ff934c37178b7ade413d4c20b81ca04f1c75d71e467ff2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.launchTemplate.LaunchTemplateConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "block_device_mappings": "blockDeviceMappings",
        "capacity_reservation_specification": "capacityReservationSpecification",
        "cpu_options": "cpuOptions",
        "credit_specification": "creditSpecification",
        "default_version": "defaultVersion",
        "description": "description",
        "disable_api_stop": "disableApiStop",
        "disable_api_termination": "disableApiTermination",
        "ebs_optimized": "ebsOptimized",
        "elastic_gpu_specifications": "elasticGpuSpecifications",
        "elastic_inference_accelerator": "elasticInferenceAccelerator",
        "enclave_options": "enclaveOptions",
        "hibernation_options": "hibernationOptions",
        "iam_instance_profile": "iamInstanceProfile",
        "id": "id",
        "image_id": "imageId",
        "instance_initiated_shutdown_behavior": "instanceInitiatedShutdownBehavior",
        "instance_market_options": "instanceMarketOptions",
        "instance_requirements": "instanceRequirements",
        "instance_type": "instanceType",
        "kernel_id": "kernelId",
        "key_name": "keyName",
        "license_specification": "licenseSpecification",
        "maintenance_options": "maintenanceOptions",
        "metadata_options": "metadataOptions",
        "monitoring": "monitoring",
        "name": "name",
        "name_prefix": "namePrefix",
        "network_interfaces": "networkInterfaces",
        "placement": "placement",
        "private_dns_name_options": "privateDnsNameOptions",
        "ram_disk_id": "ramDiskId",
        "security_group_names": "securityGroupNames",
        "tags": "tags",
        "tags_all": "tagsAll",
        "tag_specifications": "tagSpecifications",
        "update_default_version": "updateDefaultVersion",
        "user_data": "userData",
        "vpc_security_group_ids": "vpcSecurityGroupIds",
    },
)
class LaunchTemplateConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        block_device_mappings: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LaunchTemplateBlockDeviceMappings, typing.Dict[builtins.str, typing.Any]]]]] = None,
        capacity_reservation_specification: typing.Optional[typing.Union[LaunchTemplateCapacityReservationSpecification, typing.Dict[builtins.str, typing.Any]]] = None,
        cpu_options: typing.Optional[typing.Union["LaunchTemplateCpuOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        credit_specification: typing.Optional[typing.Union["LaunchTemplateCreditSpecification", typing.Dict[builtins.str, typing.Any]]] = None,
        default_version: typing.Optional[jsii.Number] = None,
        description: typing.Optional[builtins.str] = None,
        disable_api_stop: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        disable_api_termination: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        ebs_optimized: typing.Optional[builtins.str] = None,
        elastic_gpu_specifications: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LaunchTemplateElasticGpuSpecifications", typing.Dict[builtins.str, typing.Any]]]]] = None,
        elastic_inference_accelerator: typing.Optional[typing.Union["LaunchTemplateElasticInferenceAccelerator", typing.Dict[builtins.str, typing.Any]]] = None,
        enclave_options: typing.Optional[typing.Union["LaunchTemplateEnclaveOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        hibernation_options: typing.Optional[typing.Union["LaunchTemplateHibernationOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        iam_instance_profile: typing.Optional[typing.Union["LaunchTemplateIamInstanceProfile", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        image_id: typing.Optional[builtins.str] = None,
        instance_initiated_shutdown_behavior: typing.Optional[builtins.str] = None,
        instance_market_options: typing.Optional[typing.Union["LaunchTemplateInstanceMarketOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        instance_requirements: typing.Optional[typing.Union["LaunchTemplateInstanceRequirements", typing.Dict[builtins.str, typing.Any]]] = None,
        instance_type: typing.Optional[builtins.str] = None,
        kernel_id: typing.Optional[builtins.str] = None,
        key_name: typing.Optional[builtins.str] = None,
        license_specification: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LaunchTemplateLicenseSpecification", typing.Dict[builtins.str, typing.Any]]]]] = None,
        maintenance_options: typing.Optional[typing.Union["LaunchTemplateMaintenanceOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        metadata_options: typing.Optional[typing.Union["LaunchTemplateMetadataOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        monitoring: typing.Optional[typing.Union["LaunchTemplateMonitoring", typing.Dict[builtins.str, typing.Any]]] = None,
        name: typing.Optional[builtins.str] = None,
        name_prefix: typing.Optional[builtins.str] = None,
        network_interfaces: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LaunchTemplateNetworkInterfaces", typing.Dict[builtins.str, typing.Any]]]]] = None,
        placement: typing.Optional[typing.Union["LaunchTemplatePlacement", typing.Dict[builtins.str, typing.Any]]] = None,
        private_dns_name_options: typing.Optional[typing.Union["LaunchTemplatePrivateDnsNameOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        ram_disk_id: typing.Optional[builtins.str] = None,
        security_group_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tag_specifications: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LaunchTemplateTagSpecifications", typing.Dict[builtins.str, typing.Any]]]]] = None,
        update_default_version: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        user_data: typing.Optional[builtins.str] = None,
        vpc_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param block_device_mappings: block_device_mappings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#block_device_mappings LaunchTemplate#block_device_mappings}
        :param capacity_reservation_specification: capacity_reservation_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#capacity_reservation_specification LaunchTemplate#capacity_reservation_specification}
        :param cpu_options: cpu_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#cpu_options LaunchTemplate#cpu_options}
        :param credit_specification: credit_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#credit_specification LaunchTemplate#credit_specification}
        :param default_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#default_version LaunchTemplate#default_version}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#description LaunchTemplate#description}.
        :param disable_api_stop: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#disable_api_stop LaunchTemplate#disable_api_stop}.
        :param disable_api_termination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#disable_api_termination LaunchTemplate#disable_api_termination}.
        :param ebs_optimized: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#ebs_optimized LaunchTemplate#ebs_optimized}.
        :param elastic_gpu_specifications: elastic_gpu_specifications block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#elastic_gpu_specifications LaunchTemplate#elastic_gpu_specifications}
        :param elastic_inference_accelerator: elastic_inference_accelerator block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#elastic_inference_accelerator LaunchTemplate#elastic_inference_accelerator}
        :param enclave_options: enclave_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#enclave_options LaunchTemplate#enclave_options}
        :param hibernation_options: hibernation_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#hibernation_options LaunchTemplate#hibernation_options}
        :param iam_instance_profile: iam_instance_profile block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#iam_instance_profile LaunchTemplate#iam_instance_profile}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#id LaunchTemplate#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param image_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#image_id LaunchTemplate#image_id}.
        :param instance_initiated_shutdown_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#instance_initiated_shutdown_behavior LaunchTemplate#instance_initiated_shutdown_behavior}.
        :param instance_market_options: instance_market_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#instance_market_options LaunchTemplate#instance_market_options}
        :param instance_requirements: instance_requirements block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#instance_requirements LaunchTemplate#instance_requirements}
        :param instance_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#instance_type LaunchTemplate#instance_type}.
        :param kernel_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#kernel_id LaunchTemplate#kernel_id}.
        :param key_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#key_name LaunchTemplate#key_name}.
        :param license_specification: license_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#license_specification LaunchTemplate#license_specification}
        :param maintenance_options: maintenance_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#maintenance_options LaunchTemplate#maintenance_options}
        :param metadata_options: metadata_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#metadata_options LaunchTemplate#metadata_options}
        :param monitoring: monitoring block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#monitoring LaunchTemplate#monitoring}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#name LaunchTemplate#name}.
        :param name_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#name_prefix LaunchTemplate#name_prefix}.
        :param network_interfaces: network_interfaces block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#network_interfaces LaunchTemplate#network_interfaces}
        :param placement: placement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#placement LaunchTemplate#placement}
        :param private_dns_name_options: private_dns_name_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#private_dns_name_options LaunchTemplate#private_dns_name_options}
        :param ram_disk_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#ram_disk_id LaunchTemplate#ram_disk_id}.
        :param security_group_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#security_group_names LaunchTemplate#security_group_names}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#tags LaunchTemplate#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#tags_all LaunchTemplate#tags_all}.
        :param tag_specifications: tag_specifications block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#tag_specifications LaunchTemplate#tag_specifications}
        :param update_default_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#update_default_version LaunchTemplate#update_default_version}.
        :param user_data: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#user_data LaunchTemplate#user_data}.
        :param vpc_security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#vpc_security_group_ids LaunchTemplate#vpc_security_group_ids}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(capacity_reservation_specification, dict):
            capacity_reservation_specification = LaunchTemplateCapacityReservationSpecification(**capacity_reservation_specification)
        if isinstance(cpu_options, dict):
            cpu_options = LaunchTemplateCpuOptions(**cpu_options)
        if isinstance(credit_specification, dict):
            credit_specification = LaunchTemplateCreditSpecification(**credit_specification)
        if isinstance(elastic_inference_accelerator, dict):
            elastic_inference_accelerator = LaunchTemplateElasticInferenceAccelerator(**elastic_inference_accelerator)
        if isinstance(enclave_options, dict):
            enclave_options = LaunchTemplateEnclaveOptions(**enclave_options)
        if isinstance(hibernation_options, dict):
            hibernation_options = LaunchTemplateHibernationOptions(**hibernation_options)
        if isinstance(iam_instance_profile, dict):
            iam_instance_profile = LaunchTemplateIamInstanceProfile(**iam_instance_profile)
        if isinstance(instance_market_options, dict):
            instance_market_options = LaunchTemplateInstanceMarketOptions(**instance_market_options)
        if isinstance(instance_requirements, dict):
            instance_requirements = LaunchTemplateInstanceRequirements(**instance_requirements)
        if isinstance(maintenance_options, dict):
            maintenance_options = LaunchTemplateMaintenanceOptions(**maintenance_options)
        if isinstance(metadata_options, dict):
            metadata_options = LaunchTemplateMetadataOptions(**metadata_options)
        if isinstance(monitoring, dict):
            monitoring = LaunchTemplateMonitoring(**monitoring)
        if isinstance(placement, dict):
            placement = LaunchTemplatePlacement(**placement)
        if isinstance(private_dns_name_options, dict):
            private_dns_name_options = LaunchTemplatePrivateDnsNameOptions(**private_dns_name_options)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5bb06656946ef75df102afcb0b4a7723d3f54f3c484f13b789bcabacb86368e2)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument block_device_mappings", value=block_device_mappings, expected_type=type_hints["block_device_mappings"])
            check_type(argname="argument capacity_reservation_specification", value=capacity_reservation_specification, expected_type=type_hints["capacity_reservation_specification"])
            check_type(argname="argument cpu_options", value=cpu_options, expected_type=type_hints["cpu_options"])
            check_type(argname="argument credit_specification", value=credit_specification, expected_type=type_hints["credit_specification"])
            check_type(argname="argument default_version", value=default_version, expected_type=type_hints["default_version"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument disable_api_stop", value=disable_api_stop, expected_type=type_hints["disable_api_stop"])
            check_type(argname="argument disable_api_termination", value=disable_api_termination, expected_type=type_hints["disable_api_termination"])
            check_type(argname="argument ebs_optimized", value=ebs_optimized, expected_type=type_hints["ebs_optimized"])
            check_type(argname="argument elastic_gpu_specifications", value=elastic_gpu_specifications, expected_type=type_hints["elastic_gpu_specifications"])
            check_type(argname="argument elastic_inference_accelerator", value=elastic_inference_accelerator, expected_type=type_hints["elastic_inference_accelerator"])
            check_type(argname="argument enclave_options", value=enclave_options, expected_type=type_hints["enclave_options"])
            check_type(argname="argument hibernation_options", value=hibernation_options, expected_type=type_hints["hibernation_options"])
            check_type(argname="argument iam_instance_profile", value=iam_instance_profile, expected_type=type_hints["iam_instance_profile"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument image_id", value=image_id, expected_type=type_hints["image_id"])
            check_type(argname="argument instance_initiated_shutdown_behavior", value=instance_initiated_shutdown_behavior, expected_type=type_hints["instance_initiated_shutdown_behavior"])
            check_type(argname="argument instance_market_options", value=instance_market_options, expected_type=type_hints["instance_market_options"])
            check_type(argname="argument instance_requirements", value=instance_requirements, expected_type=type_hints["instance_requirements"])
            check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
            check_type(argname="argument kernel_id", value=kernel_id, expected_type=type_hints["kernel_id"])
            check_type(argname="argument key_name", value=key_name, expected_type=type_hints["key_name"])
            check_type(argname="argument license_specification", value=license_specification, expected_type=type_hints["license_specification"])
            check_type(argname="argument maintenance_options", value=maintenance_options, expected_type=type_hints["maintenance_options"])
            check_type(argname="argument metadata_options", value=metadata_options, expected_type=type_hints["metadata_options"])
            check_type(argname="argument monitoring", value=monitoring, expected_type=type_hints["monitoring"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument name_prefix", value=name_prefix, expected_type=type_hints["name_prefix"])
            check_type(argname="argument network_interfaces", value=network_interfaces, expected_type=type_hints["network_interfaces"])
            check_type(argname="argument placement", value=placement, expected_type=type_hints["placement"])
            check_type(argname="argument private_dns_name_options", value=private_dns_name_options, expected_type=type_hints["private_dns_name_options"])
            check_type(argname="argument ram_disk_id", value=ram_disk_id, expected_type=type_hints["ram_disk_id"])
            check_type(argname="argument security_group_names", value=security_group_names, expected_type=type_hints["security_group_names"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument tag_specifications", value=tag_specifications, expected_type=type_hints["tag_specifications"])
            check_type(argname="argument update_default_version", value=update_default_version, expected_type=type_hints["update_default_version"])
            check_type(argname="argument user_data", value=user_data, expected_type=type_hints["user_data"])
            check_type(argname="argument vpc_security_group_ids", value=vpc_security_group_ids, expected_type=type_hints["vpc_security_group_ids"])
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
        if block_device_mappings is not None:
            self._values["block_device_mappings"] = block_device_mappings
        if capacity_reservation_specification is not None:
            self._values["capacity_reservation_specification"] = capacity_reservation_specification
        if cpu_options is not None:
            self._values["cpu_options"] = cpu_options
        if credit_specification is not None:
            self._values["credit_specification"] = credit_specification
        if default_version is not None:
            self._values["default_version"] = default_version
        if description is not None:
            self._values["description"] = description
        if disable_api_stop is not None:
            self._values["disable_api_stop"] = disable_api_stop
        if disable_api_termination is not None:
            self._values["disable_api_termination"] = disable_api_termination
        if ebs_optimized is not None:
            self._values["ebs_optimized"] = ebs_optimized
        if elastic_gpu_specifications is not None:
            self._values["elastic_gpu_specifications"] = elastic_gpu_specifications
        if elastic_inference_accelerator is not None:
            self._values["elastic_inference_accelerator"] = elastic_inference_accelerator
        if enclave_options is not None:
            self._values["enclave_options"] = enclave_options
        if hibernation_options is not None:
            self._values["hibernation_options"] = hibernation_options
        if iam_instance_profile is not None:
            self._values["iam_instance_profile"] = iam_instance_profile
        if id is not None:
            self._values["id"] = id
        if image_id is not None:
            self._values["image_id"] = image_id
        if instance_initiated_shutdown_behavior is not None:
            self._values["instance_initiated_shutdown_behavior"] = instance_initiated_shutdown_behavior
        if instance_market_options is not None:
            self._values["instance_market_options"] = instance_market_options
        if instance_requirements is not None:
            self._values["instance_requirements"] = instance_requirements
        if instance_type is not None:
            self._values["instance_type"] = instance_type
        if kernel_id is not None:
            self._values["kernel_id"] = kernel_id
        if key_name is not None:
            self._values["key_name"] = key_name
        if license_specification is not None:
            self._values["license_specification"] = license_specification
        if maintenance_options is not None:
            self._values["maintenance_options"] = maintenance_options
        if metadata_options is not None:
            self._values["metadata_options"] = metadata_options
        if monitoring is not None:
            self._values["monitoring"] = monitoring
        if name is not None:
            self._values["name"] = name
        if name_prefix is not None:
            self._values["name_prefix"] = name_prefix
        if network_interfaces is not None:
            self._values["network_interfaces"] = network_interfaces
        if placement is not None:
            self._values["placement"] = placement
        if private_dns_name_options is not None:
            self._values["private_dns_name_options"] = private_dns_name_options
        if ram_disk_id is not None:
            self._values["ram_disk_id"] = ram_disk_id
        if security_group_names is not None:
            self._values["security_group_names"] = security_group_names
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if tag_specifications is not None:
            self._values["tag_specifications"] = tag_specifications
        if update_default_version is not None:
            self._values["update_default_version"] = update_default_version
        if user_data is not None:
            self._values["user_data"] = user_data
        if vpc_security_group_ids is not None:
            self._values["vpc_security_group_ids"] = vpc_security_group_ids

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
    def block_device_mappings(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LaunchTemplateBlockDeviceMappings]]]:
        '''block_device_mappings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#block_device_mappings LaunchTemplate#block_device_mappings}
        '''
        result = self._values.get("block_device_mappings")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LaunchTemplateBlockDeviceMappings]]], result)

    @builtins.property
    def capacity_reservation_specification(
        self,
    ) -> typing.Optional[LaunchTemplateCapacityReservationSpecification]:
        '''capacity_reservation_specification block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#capacity_reservation_specification LaunchTemplate#capacity_reservation_specification}
        '''
        result = self._values.get("capacity_reservation_specification")
        return typing.cast(typing.Optional[LaunchTemplateCapacityReservationSpecification], result)

    @builtins.property
    def cpu_options(self) -> typing.Optional["LaunchTemplateCpuOptions"]:
        '''cpu_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#cpu_options LaunchTemplate#cpu_options}
        '''
        result = self._values.get("cpu_options")
        return typing.cast(typing.Optional["LaunchTemplateCpuOptions"], result)

    @builtins.property
    def credit_specification(
        self,
    ) -> typing.Optional["LaunchTemplateCreditSpecification"]:
        '''credit_specification block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#credit_specification LaunchTemplate#credit_specification}
        '''
        result = self._values.get("credit_specification")
        return typing.cast(typing.Optional["LaunchTemplateCreditSpecification"], result)

    @builtins.property
    def default_version(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#default_version LaunchTemplate#default_version}.'''
        result = self._values.get("default_version")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#description LaunchTemplate#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disable_api_stop(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#disable_api_stop LaunchTemplate#disable_api_stop}.'''
        result = self._values.get("disable_api_stop")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def disable_api_termination(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#disable_api_termination LaunchTemplate#disable_api_termination}.'''
        result = self._values.get("disable_api_termination")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def ebs_optimized(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#ebs_optimized LaunchTemplate#ebs_optimized}.'''
        result = self._values.get("ebs_optimized")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def elastic_gpu_specifications(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LaunchTemplateElasticGpuSpecifications"]]]:
        '''elastic_gpu_specifications block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#elastic_gpu_specifications LaunchTemplate#elastic_gpu_specifications}
        '''
        result = self._values.get("elastic_gpu_specifications")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LaunchTemplateElasticGpuSpecifications"]]], result)

    @builtins.property
    def elastic_inference_accelerator(
        self,
    ) -> typing.Optional["LaunchTemplateElasticInferenceAccelerator"]:
        '''elastic_inference_accelerator block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#elastic_inference_accelerator LaunchTemplate#elastic_inference_accelerator}
        '''
        result = self._values.get("elastic_inference_accelerator")
        return typing.cast(typing.Optional["LaunchTemplateElasticInferenceAccelerator"], result)

    @builtins.property
    def enclave_options(self) -> typing.Optional["LaunchTemplateEnclaveOptions"]:
        '''enclave_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#enclave_options LaunchTemplate#enclave_options}
        '''
        result = self._values.get("enclave_options")
        return typing.cast(typing.Optional["LaunchTemplateEnclaveOptions"], result)

    @builtins.property
    def hibernation_options(
        self,
    ) -> typing.Optional["LaunchTemplateHibernationOptions"]:
        '''hibernation_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#hibernation_options LaunchTemplate#hibernation_options}
        '''
        result = self._values.get("hibernation_options")
        return typing.cast(typing.Optional["LaunchTemplateHibernationOptions"], result)

    @builtins.property
    def iam_instance_profile(
        self,
    ) -> typing.Optional["LaunchTemplateIamInstanceProfile"]:
        '''iam_instance_profile block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#iam_instance_profile LaunchTemplate#iam_instance_profile}
        '''
        result = self._values.get("iam_instance_profile")
        return typing.cast(typing.Optional["LaunchTemplateIamInstanceProfile"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#id LaunchTemplate#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def image_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#image_id LaunchTemplate#image_id}.'''
        result = self._values.get("image_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance_initiated_shutdown_behavior(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#instance_initiated_shutdown_behavior LaunchTemplate#instance_initiated_shutdown_behavior}.'''
        result = self._values.get("instance_initiated_shutdown_behavior")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance_market_options(
        self,
    ) -> typing.Optional["LaunchTemplateInstanceMarketOptions"]:
        '''instance_market_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#instance_market_options LaunchTemplate#instance_market_options}
        '''
        result = self._values.get("instance_market_options")
        return typing.cast(typing.Optional["LaunchTemplateInstanceMarketOptions"], result)

    @builtins.property
    def instance_requirements(
        self,
    ) -> typing.Optional["LaunchTemplateInstanceRequirements"]:
        '''instance_requirements block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#instance_requirements LaunchTemplate#instance_requirements}
        '''
        result = self._values.get("instance_requirements")
        return typing.cast(typing.Optional["LaunchTemplateInstanceRequirements"], result)

    @builtins.property
    def instance_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#instance_type LaunchTemplate#instance_type}.'''
        result = self._values.get("instance_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kernel_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#kernel_id LaunchTemplate#kernel_id}.'''
        result = self._values.get("kernel_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#key_name LaunchTemplate#key_name}.'''
        result = self._values.get("key_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def license_specification(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LaunchTemplateLicenseSpecification"]]]:
        '''license_specification block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#license_specification LaunchTemplate#license_specification}
        '''
        result = self._values.get("license_specification")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LaunchTemplateLicenseSpecification"]]], result)

    @builtins.property
    def maintenance_options(
        self,
    ) -> typing.Optional["LaunchTemplateMaintenanceOptions"]:
        '''maintenance_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#maintenance_options LaunchTemplate#maintenance_options}
        '''
        result = self._values.get("maintenance_options")
        return typing.cast(typing.Optional["LaunchTemplateMaintenanceOptions"], result)

    @builtins.property
    def metadata_options(self) -> typing.Optional["LaunchTemplateMetadataOptions"]:
        '''metadata_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#metadata_options LaunchTemplate#metadata_options}
        '''
        result = self._values.get("metadata_options")
        return typing.cast(typing.Optional["LaunchTemplateMetadataOptions"], result)

    @builtins.property
    def monitoring(self) -> typing.Optional["LaunchTemplateMonitoring"]:
        '''monitoring block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#monitoring LaunchTemplate#monitoring}
        '''
        result = self._values.get("monitoring")
        return typing.cast(typing.Optional["LaunchTemplateMonitoring"], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#name LaunchTemplate#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#name_prefix LaunchTemplate#name_prefix}.'''
        result = self._values.get("name_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def network_interfaces(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LaunchTemplateNetworkInterfaces"]]]:
        '''network_interfaces block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#network_interfaces LaunchTemplate#network_interfaces}
        '''
        result = self._values.get("network_interfaces")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LaunchTemplateNetworkInterfaces"]]], result)

    @builtins.property
    def placement(self) -> typing.Optional["LaunchTemplatePlacement"]:
        '''placement block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#placement LaunchTemplate#placement}
        '''
        result = self._values.get("placement")
        return typing.cast(typing.Optional["LaunchTemplatePlacement"], result)

    @builtins.property
    def private_dns_name_options(
        self,
    ) -> typing.Optional["LaunchTemplatePrivateDnsNameOptions"]:
        '''private_dns_name_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#private_dns_name_options LaunchTemplate#private_dns_name_options}
        '''
        result = self._values.get("private_dns_name_options")
        return typing.cast(typing.Optional["LaunchTemplatePrivateDnsNameOptions"], result)

    @builtins.property
    def ram_disk_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#ram_disk_id LaunchTemplate#ram_disk_id}.'''
        result = self._values.get("ram_disk_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def security_group_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#security_group_names LaunchTemplate#security_group_names}.'''
        result = self._values.get("security_group_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#tags LaunchTemplate#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#tags_all LaunchTemplate#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tag_specifications(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LaunchTemplateTagSpecifications"]]]:
        '''tag_specifications block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#tag_specifications LaunchTemplate#tag_specifications}
        '''
        result = self._values.get("tag_specifications")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LaunchTemplateTagSpecifications"]]], result)

    @builtins.property
    def update_default_version(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#update_default_version LaunchTemplate#update_default_version}.'''
        result = self._values.get("update_default_version")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def user_data(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#user_data LaunchTemplate#user_data}.'''
        result = self._values.get("user_data")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vpc_security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#vpc_security_group_ids LaunchTemplate#vpc_security_group_ids}.'''
        result = self._values.get("vpc_security_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LaunchTemplateConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.launchTemplate.LaunchTemplateCpuOptions",
    jsii_struct_bases=[],
    name_mapping={"core_count": "coreCount", "threads_per_core": "threadsPerCore"},
)
class LaunchTemplateCpuOptions:
    def __init__(
        self,
        *,
        core_count: typing.Optional[jsii.Number] = None,
        threads_per_core: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param core_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#core_count LaunchTemplate#core_count}.
        :param threads_per_core: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#threads_per_core LaunchTemplate#threads_per_core}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3821d62ebcc8a437ec1e8e1b08bad8e8140e9b7279369e3d739cd764b900b36c)
            check_type(argname="argument core_count", value=core_count, expected_type=type_hints["core_count"])
            check_type(argname="argument threads_per_core", value=threads_per_core, expected_type=type_hints["threads_per_core"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if core_count is not None:
            self._values["core_count"] = core_count
        if threads_per_core is not None:
            self._values["threads_per_core"] = threads_per_core

    @builtins.property
    def core_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#core_count LaunchTemplate#core_count}.'''
        result = self._values.get("core_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def threads_per_core(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#threads_per_core LaunchTemplate#threads_per_core}.'''
        result = self._values.get("threads_per_core")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LaunchTemplateCpuOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LaunchTemplateCpuOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.launchTemplate.LaunchTemplateCpuOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8a1b03755352ad65764746171f906c7ee8f6f9a1eea9469cd61a37756c806534)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCoreCount")
    def reset_core_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCoreCount", []))

    @jsii.member(jsii_name="resetThreadsPerCore")
    def reset_threads_per_core(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetThreadsPerCore", []))

    @builtins.property
    @jsii.member(jsii_name="coreCountInput")
    def core_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "coreCountInput"))

    @builtins.property
    @jsii.member(jsii_name="threadsPerCoreInput")
    def threads_per_core_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "threadsPerCoreInput"))

    @builtins.property
    @jsii.member(jsii_name="coreCount")
    def core_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "coreCount"))

    @core_count.setter
    def core_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b856e0b70260e1dc7c83973a2bbe3b12d255635901f99ad770efca6a22ddf10a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "coreCount", value)

    @builtins.property
    @jsii.member(jsii_name="threadsPerCore")
    def threads_per_core(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "threadsPerCore"))

    @threads_per_core.setter
    def threads_per_core(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8bf0e5797b346014a316eed87b75941bfc4104ece916af9edee5b216ba6a2b09)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "threadsPerCore", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LaunchTemplateCpuOptions]:
        return typing.cast(typing.Optional[LaunchTemplateCpuOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[LaunchTemplateCpuOptions]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b7ab34adfa6d654b51d538458f20813053c59a81c31b4a6c7df7abacc3d7082)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.launchTemplate.LaunchTemplateCreditSpecification",
    jsii_struct_bases=[],
    name_mapping={"cpu_credits": "cpuCredits"},
)
class LaunchTemplateCreditSpecification:
    def __init__(self, *, cpu_credits: typing.Optional[builtins.str] = None) -> None:
        '''
        :param cpu_credits: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#cpu_credits LaunchTemplate#cpu_credits}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7999115e17091a9ddaaeae011e07d4cf65d07effff3a9ad80d614b9e72d40f39)
            check_type(argname="argument cpu_credits", value=cpu_credits, expected_type=type_hints["cpu_credits"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if cpu_credits is not None:
            self._values["cpu_credits"] = cpu_credits

    @builtins.property
    def cpu_credits(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#cpu_credits LaunchTemplate#cpu_credits}.'''
        result = self._values.get("cpu_credits")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LaunchTemplateCreditSpecification(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LaunchTemplateCreditSpecificationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.launchTemplate.LaunchTemplateCreditSpecificationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__09d5810a51f64e54cb259c6aad922b474d01ed56fbe2ea34e95495b299419e34)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCpuCredits")
    def reset_cpu_credits(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCpuCredits", []))

    @builtins.property
    @jsii.member(jsii_name="cpuCreditsInput")
    def cpu_credits_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cpuCreditsInput"))

    @builtins.property
    @jsii.member(jsii_name="cpuCredits")
    def cpu_credits(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cpuCredits"))

    @cpu_credits.setter
    def cpu_credits(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6e23da63b390818205e681cf0536e2b2e98dc7e52185afa512ceb5dbee71dc9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpuCredits", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LaunchTemplateCreditSpecification]:
        return typing.cast(typing.Optional[LaunchTemplateCreditSpecification], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LaunchTemplateCreditSpecification],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cdfcec7af0051d6e1a883d11698307ec02e7a6ec84eb8c71c228ec4a5e445942)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.launchTemplate.LaunchTemplateElasticGpuSpecifications",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class LaunchTemplateElasticGpuSpecifications:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#type LaunchTemplate#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3fea3586fc475da8574bcd06a8ddb22672ffc60f64b5baa44d2e61523f5a035)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#type LaunchTemplate#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LaunchTemplateElasticGpuSpecifications(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LaunchTemplateElasticGpuSpecificationsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.launchTemplate.LaunchTemplateElasticGpuSpecificationsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__30aeeeb925bb1652cb99598aff0c5ff3cf0c3d1dbeb168dffe4aa3925781096c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LaunchTemplateElasticGpuSpecificationsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c486bfa7d686f2c9b88f269a084267310fb8760eff16ebb377eccf0f00f57ac9)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LaunchTemplateElasticGpuSpecificationsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__387e7ee519fa4582155bc70c5dffae6a377a1eaeb1366b4f4a8601bbffea4299)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4f2578d3a8abaad6bf93a9f9700cfea11a4886a627399b7a7e8c584c5d5f2c24)
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
            type_hints = typing.get_type_hints(_typecheckingstub__87a11d02d4a96477112aa05bbdb965d6d1d2252671d77eb9067ce32fc8592e39)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LaunchTemplateElasticGpuSpecifications]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LaunchTemplateElasticGpuSpecifications]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LaunchTemplateElasticGpuSpecifications]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__442ea892ba1d0a9482b7f9187a75911d388e624fa2ac3a197c9d19393cd1ac0c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LaunchTemplateElasticGpuSpecificationsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.launchTemplate.LaunchTemplateElasticGpuSpecificationsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a81f70736341d7d575138f6ee8a6aefb4f4221a513d4a62d7ea7a9e134c322f6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d231a0d5ca28941516c0fd698ca764c1961bdd4c746226043a304ca5c6e56e1b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LaunchTemplateElasticGpuSpecifications, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LaunchTemplateElasticGpuSpecifications, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LaunchTemplateElasticGpuSpecifications, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e21d9f7aec4c4d272daa862fc4c0f8a730f28e7def9f51479a6f48cb10096253)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.launchTemplate.LaunchTemplateElasticInferenceAccelerator",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class LaunchTemplateElasticInferenceAccelerator:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#type LaunchTemplate#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3e3173f1c88b6cdb59709a5fa299a070d3fd77bc97282a16be00e51e7153171)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#type LaunchTemplate#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LaunchTemplateElasticInferenceAccelerator(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LaunchTemplateElasticInferenceAcceleratorOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.launchTemplate.LaunchTemplateElasticInferenceAcceleratorOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__00933cf4bd28fa99da9a5915851da3e3c4bef809ae46ef06d2413f9d33638799)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7369eeb24dbeed199dc0b03e76171342f70fee1e9b503eb92f8f5499dcf5c7cb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LaunchTemplateElasticInferenceAccelerator]:
        return typing.cast(typing.Optional[LaunchTemplateElasticInferenceAccelerator], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LaunchTemplateElasticInferenceAccelerator],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5208ad541a2ff42ec9d0472df5ad3cc9becbdf24386f84f7e47fed98d3bfcca8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.launchTemplate.LaunchTemplateEnclaveOptions",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled"},
)
class LaunchTemplateEnclaveOptions:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#enabled LaunchTemplate#enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f02f0e38e951218e042a3be6d57210a4a16d26607ee67ba5708b7518c2409100)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#enabled LaunchTemplate#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LaunchTemplateEnclaveOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LaunchTemplateEnclaveOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.launchTemplate.LaunchTemplateEnclaveOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9dadecdfacf3f9ff44d7610897d2a22b1da7ae3ca7efe87f5a2d882f2f610d07)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a3e184d13fe920a555bb7b34d224d37b6e94f0dab91f9f39e1cde0e1c264ba54)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LaunchTemplateEnclaveOptions]:
        return typing.cast(typing.Optional[LaunchTemplateEnclaveOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LaunchTemplateEnclaveOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed40a24685a0222baedee215e29fce2ee9e58d04ca2704b722d7024e3e1db68b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.launchTemplate.LaunchTemplateHibernationOptions",
    jsii_struct_bases=[],
    name_mapping={"configured": "configured"},
)
class LaunchTemplateHibernationOptions:
    def __init__(
        self,
        *,
        configured: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        '''
        :param configured: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#configured LaunchTemplate#configured}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60970343b4cc3a3adf99ee3f0da4a99d9603bad2643737d7a20c47d407e22293)
            check_type(argname="argument configured", value=configured, expected_type=type_hints["configured"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "configured": configured,
        }

    @builtins.property
    def configured(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#configured LaunchTemplate#configured}.'''
        result = self._values.get("configured")
        assert result is not None, "Required property 'configured' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LaunchTemplateHibernationOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LaunchTemplateHibernationOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.launchTemplate.LaunchTemplateHibernationOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__178948ca0485650d4674f5bc9186a5212823c88aab15d4a0fdc67dcdcbe6776f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="configuredInput")
    def configured_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "configuredInput"))

    @builtins.property
    @jsii.member(jsii_name="configured")
    def configured(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "configured"))

    @configured.setter
    def configured(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33aa1cb651b2792cd58a624250a228318aac672b4e69b784c7beb9f0d56c244d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configured", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LaunchTemplateHibernationOptions]:
        return typing.cast(typing.Optional[LaunchTemplateHibernationOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LaunchTemplateHibernationOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__912616f9e53fca614c9b78b9269a8b97c5629df6397a9e0949cba0e7168ff803)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.launchTemplate.LaunchTemplateIamInstanceProfile",
    jsii_struct_bases=[],
    name_mapping={"arn": "arn", "name": "name"},
)
class LaunchTemplateIamInstanceProfile:
    def __init__(
        self,
        *,
        arn: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#arn LaunchTemplate#arn}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#name LaunchTemplate#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1df29693a0a28e146b745d8797ee7e9481d867a28df9a96160eeb32e42b1378a)
            check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if arn is not None:
            self._values["arn"] = arn
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#arn LaunchTemplate#arn}.'''
        result = self._values.get("arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#name LaunchTemplate#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LaunchTemplateIamInstanceProfile(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LaunchTemplateIamInstanceProfileOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.launchTemplate.LaunchTemplateIamInstanceProfileOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a4fc04aeefbf55b51b56a42b5099a2d8b18c6bb1985f5befcabbd6c4de7ff309)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetArn")
    def reset_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetArn", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @builtins.property
    @jsii.member(jsii_name="arnInput")
    def arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "arnInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @arn.setter
    def arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__51606d7136d1cfddc7085ffda57b0ad04d8c5ebfe3ed85330b13f536bef8eb5c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "arn", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d324c7626334669715f012b3ed3ed14df539b53a010f4e9c5f9fc78425c62985)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LaunchTemplateIamInstanceProfile]:
        return typing.cast(typing.Optional[LaunchTemplateIamInstanceProfile], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LaunchTemplateIamInstanceProfile],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af2817f69148d098f8ba77a902bbd247c3a46950e588136f0f5144eca7f4ddb7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.launchTemplate.LaunchTemplateInstanceMarketOptions",
    jsii_struct_bases=[],
    name_mapping={"market_type": "marketType", "spot_options": "spotOptions"},
)
class LaunchTemplateInstanceMarketOptions:
    def __init__(
        self,
        *,
        market_type: typing.Optional[builtins.str] = None,
        spot_options: typing.Optional[typing.Union["LaunchTemplateInstanceMarketOptionsSpotOptions", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param market_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#market_type LaunchTemplate#market_type}.
        :param spot_options: spot_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#spot_options LaunchTemplate#spot_options}
        '''
        if isinstance(spot_options, dict):
            spot_options = LaunchTemplateInstanceMarketOptionsSpotOptions(**spot_options)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4cc9bd83dc3d052fb4c5c6997a559e225fd8f7cea8c45deb1c8fc9bbbfc327ae)
            check_type(argname="argument market_type", value=market_type, expected_type=type_hints["market_type"])
            check_type(argname="argument spot_options", value=spot_options, expected_type=type_hints["spot_options"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if market_type is not None:
            self._values["market_type"] = market_type
        if spot_options is not None:
            self._values["spot_options"] = spot_options

    @builtins.property
    def market_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#market_type LaunchTemplate#market_type}.'''
        result = self._values.get("market_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def spot_options(
        self,
    ) -> typing.Optional["LaunchTemplateInstanceMarketOptionsSpotOptions"]:
        '''spot_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#spot_options LaunchTemplate#spot_options}
        '''
        result = self._values.get("spot_options")
        return typing.cast(typing.Optional["LaunchTemplateInstanceMarketOptionsSpotOptions"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LaunchTemplateInstanceMarketOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LaunchTemplateInstanceMarketOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.launchTemplate.LaunchTemplateInstanceMarketOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6a691eb5315c0269badb1c023434aa869f97593eaddeb3e291b062fb684af8e2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putSpotOptions")
    def put_spot_options(
        self,
        *,
        block_duration_minutes: typing.Optional[jsii.Number] = None,
        instance_interruption_behavior: typing.Optional[builtins.str] = None,
        max_price: typing.Optional[builtins.str] = None,
        spot_instance_type: typing.Optional[builtins.str] = None,
        valid_until: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param block_duration_minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#block_duration_minutes LaunchTemplate#block_duration_minutes}.
        :param instance_interruption_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#instance_interruption_behavior LaunchTemplate#instance_interruption_behavior}.
        :param max_price: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#max_price LaunchTemplate#max_price}.
        :param spot_instance_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#spot_instance_type LaunchTemplate#spot_instance_type}.
        :param valid_until: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#valid_until LaunchTemplate#valid_until}.
        '''
        value = LaunchTemplateInstanceMarketOptionsSpotOptions(
            block_duration_minutes=block_duration_minutes,
            instance_interruption_behavior=instance_interruption_behavior,
            max_price=max_price,
            spot_instance_type=spot_instance_type,
            valid_until=valid_until,
        )

        return typing.cast(None, jsii.invoke(self, "putSpotOptions", [value]))

    @jsii.member(jsii_name="resetMarketType")
    def reset_market_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMarketType", []))

    @jsii.member(jsii_name="resetSpotOptions")
    def reset_spot_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSpotOptions", []))

    @builtins.property
    @jsii.member(jsii_name="spotOptions")
    def spot_options(
        self,
    ) -> "LaunchTemplateInstanceMarketOptionsSpotOptionsOutputReference":
        return typing.cast("LaunchTemplateInstanceMarketOptionsSpotOptionsOutputReference", jsii.get(self, "spotOptions"))

    @builtins.property
    @jsii.member(jsii_name="marketTypeInput")
    def market_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "marketTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="spotOptionsInput")
    def spot_options_input(
        self,
    ) -> typing.Optional["LaunchTemplateInstanceMarketOptionsSpotOptions"]:
        return typing.cast(typing.Optional["LaunchTemplateInstanceMarketOptionsSpotOptions"], jsii.get(self, "spotOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="marketType")
    def market_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "marketType"))

    @market_type.setter
    def market_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__36441bd509eecd79e0c6dac3ba845579506799a4e7a694b9be8c8c7a9faf4d99)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "marketType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LaunchTemplateInstanceMarketOptions]:
        return typing.cast(typing.Optional[LaunchTemplateInstanceMarketOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LaunchTemplateInstanceMarketOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0174fe7cdacf31e9a60e7e7d63653a43f8367f319dcc11a10360b140ff8ca603)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.launchTemplate.LaunchTemplateInstanceMarketOptionsSpotOptions",
    jsii_struct_bases=[],
    name_mapping={
        "block_duration_minutes": "blockDurationMinutes",
        "instance_interruption_behavior": "instanceInterruptionBehavior",
        "max_price": "maxPrice",
        "spot_instance_type": "spotInstanceType",
        "valid_until": "validUntil",
    },
)
class LaunchTemplateInstanceMarketOptionsSpotOptions:
    def __init__(
        self,
        *,
        block_duration_minutes: typing.Optional[jsii.Number] = None,
        instance_interruption_behavior: typing.Optional[builtins.str] = None,
        max_price: typing.Optional[builtins.str] = None,
        spot_instance_type: typing.Optional[builtins.str] = None,
        valid_until: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param block_duration_minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#block_duration_minutes LaunchTemplate#block_duration_minutes}.
        :param instance_interruption_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#instance_interruption_behavior LaunchTemplate#instance_interruption_behavior}.
        :param max_price: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#max_price LaunchTemplate#max_price}.
        :param spot_instance_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#spot_instance_type LaunchTemplate#spot_instance_type}.
        :param valid_until: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#valid_until LaunchTemplate#valid_until}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9be6f6d5f5ff3d177a3cc9e587bab78addb78bfa1e8ed1ec99cf48d71e694f8)
            check_type(argname="argument block_duration_minutes", value=block_duration_minutes, expected_type=type_hints["block_duration_minutes"])
            check_type(argname="argument instance_interruption_behavior", value=instance_interruption_behavior, expected_type=type_hints["instance_interruption_behavior"])
            check_type(argname="argument max_price", value=max_price, expected_type=type_hints["max_price"])
            check_type(argname="argument spot_instance_type", value=spot_instance_type, expected_type=type_hints["spot_instance_type"])
            check_type(argname="argument valid_until", value=valid_until, expected_type=type_hints["valid_until"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if block_duration_minutes is not None:
            self._values["block_duration_minutes"] = block_duration_minutes
        if instance_interruption_behavior is not None:
            self._values["instance_interruption_behavior"] = instance_interruption_behavior
        if max_price is not None:
            self._values["max_price"] = max_price
        if spot_instance_type is not None:
            self._values["spot_instance_type"] = spot_instance_type
        if valid_until is not None:
            self._values["valid_until"] = valid_until

    @builtins.property
    def block_duration_minutes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#block_duration_minutes LaunchTemplate#block_duration_minutes}.'''
        result = self._values.get("block_duration_minutes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def instance_interruption_behavior(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#instance_interruption_behavior LaunchTemplate#instance_interruption_behavior}.'''
        result = self._values.get("instance_interruption_behavior")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_price(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#max_price LaunchTemplate#max_price}.'''
        result = self._values.get("max_price")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def spot_instance_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#spot_instance_type LaunchTemplate#spot_instance_type}.'''
        result = self._values.get("spot_instance_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def valid_until(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#valid_until LaunchTemplate#valid_until}.'''
        result = self._values.get("valid_until")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LaunchTemplateInstanceMarketOptionsSpotOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LaunchTemplateInstanceMarketOptionsSpotOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.launchTemplate.LaunchTemplateInstanceMarketOptionsSpotOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2a80d6f60dfb179691d04918aca242144cda05e08ac1ccbca444d48d61bc8cdc)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBlockDurationMinutes")
    def reset_block_duration_minutes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBlockDurationMinutes", []))

    @jsii.member(jsii_name="resetInstanceInterruptionBehavior")
    def reset_instance_interruption_behavior(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceInterruptionBehavior", []))

    @jsii.member(jsii_name="resetMaxPrice")
    def reset_max_price(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxPrice", []))

    @jsii.member(jsii_name="resetSpotInstanceType")
    def reset_spot_instance_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSpotInstanceType", []))

    @jsii.member(jsii_name="resetValidUntil")
    def reset_valid_until(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValidUntil", []))

    @builtins.property
    @jsii.member(jsii_name="blockDurationMinutesInput")
    def block_duration_minutes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "blockDurationMinutesInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceInterruptionBehaviorInput")
    def instance_interruption_behavior_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceInterruptionBehaviorInput"))

    @builtins.property
    @jsii.member(jsii_name="maxPriceInput")
    def max_price_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxPriceInput"))

    @builtins.property
    @jsii.member(jsii_name="spotInstanceTypeInput")
    def spot_instance_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "spotInstanceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="validUntilInput")
    def valid_until_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "validUntilInput"))

    @builtins.property
    @jsii.member(jsii_name="blockDurationMinutes")
    def block_duration_minutes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "blockDurationMinutes"))

    @block_duration_minutes.setter
    def block_duration_minutes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96fb75b8933cfd143ec4cb8118958f20f50f721009c7df6c5c45807a014812b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "blockDurationMinutes", value)

    @builtins.property
    @jsii.member(jsii_name="instanceInterruptionBehavior")
    def instance_interruption_behavior(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceInterruptionBehavior"))

    @instance_interruption_behavior.setter
    def instance_interruption_behavior(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7833ee9acbcb5d732346f239e97e35376e649ddbfc507fd39a6423ba1611a8ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceInterruptionBehavior", value)

    @builtins.property
    @jsii.member(jsii_name="maxPrice")
    def max_price(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maxPrice"))

    @max_price.setter
    def max_price(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af3804236b9e83a8039ace2dcbd6df78909d417a464b96c7d98fcca2bea431f6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxPrice", value)

    @builtins.property
    @jsii.member(jsii_name="spotInstanceType")
    def spot_instance_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "spotInstanceType"))

    @spot_instance_type.setter
    def spot_instance_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8cee3f92a4fed3e89edcac154dbe457aaa3130ac65b13211a866ff63fcc7cd4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "spotInstanceType", value)

    @builtins.property
    @jsii.member(jsii_name="validUntil")
    def valid_until(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "validUntil"))

    @valid_until.setter
    def valid_until(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2495312cf363a8b098e095f104372c54cecfb55786e68c87bebbfcc68ad405a9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "validUntil", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LaunchTemplateInstanceMarketOptionsSpotOptions]:
        return typing.cast(typing.Optional[LaunchTemplateInstanceMarketOptionsSpotOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LaunchTemplateInstanceMarketOptionsSpotOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b55f57b3797ced4cb973c45b287fa07b33d12607a788a7120d8cec4d4a2dd953)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.launchTemplate.LaunchTemplateInstanceRequirements",
    jsii_struct_bases=[],
    name_mapping={
        "memory_mib": "memoryMib",
        "vcpu_count": "vcpuCount",
        "accelerator_count": "acceleratorCount",
        "accelerator_manufacturers": "acceleratorManufacturers",
        "accelerator_names": "acceleratorNames",
        "accelerator_total_memory_mib": "acceleratorTotalMemoryMib",
        "accelerator_types": "acceleratorTypes",
        "bare_metal": "bareMetal",
        "baseline_ebs_bandwidth_mbps": "baselineEbsBandwidthMbps",
        "burstable_performance": "burstablePerformance",
        "cpu_manufacturers": "cpuManufacturers",
        "excluded_instance_types": "excludedInstanceTypes",
        "instance_generations": "instanceGenerations",
        "local_storage": "localStorage",
        "local_storage_types": "localStorageTypes",
        "memory_gib_per_vcpu": "memoryGibPerVcpu",
        "network_interface_count": "networkInterfaceCount",
        "on_demand_max_price_percentage_over_lowest_price": "onDemandMaxPricePercentageOverLowestPrice",
        "require_hibernate_support": "requireHibernateSupport",
        "spot_max_price_percentage_over_lowest_price": "spotMaxPricePercentageOverLowestPrice",
        "total_local_storage_gb": "totalLocalStorageGb",
    },
)
class LaunchTemplateInstanceRequirements:
    def __init__(
        self,
        *,
        memory_mib: typing.Union["LaunchTemplateInstanceRequirementsMemoryMib", typing.Dict[builtins.str, typing.Any]],
        vcpu_count: typing.Union["LaunchTemplateInstanceRequirementsVcpuCount", typing.Dict[builtins.str, typing.Any]],
        accelerator_count: typing.Optional[typing.Union["LaunchTemplateInstanceRequirementsAcceleratorCount", typing.Dict[builtins.str, typing.Any]]] = None,
        accelerator_manufacturers: typing.Optional[typing.Sequence[builtins.str]] = None,
        accelerator_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        accelerator_total_memory_mib: typing.Optional[typing.Union["LaunchTemplateInstanceRequirementsAcceleratorTotalMemoryMib", typing.Dict[builtins.str, typing.Any]]] = None,
        accelerator_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        bare_metal: typing.Optional[builtins.str] = None,
        baseline_ebs_bandwidth_mbps: typing.Optional[typing.Union["LaunchTemplateInstanceRequirementsBaselineEbsBandwidthMbps", typing.Dict[builtins.str, typing.Any]]] = None,
        burstable_performance: typing.Optional[builtins.str] = None,
        cpu_manufacturers: typing.Optional[typing.Sequence[builtins.str]] = None,
        excluded_instance_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        instance_generations: typing.Optional[typing.Sequence[builtins.str]] = None,
        local_storage: typing.Optional[builtins.str] = None,
        local_storage_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        memory_gib_per_vcpu: typing.Optional[typing.Union["LaunchTemplateInstanceRequirementsMemoryGibPerVcpu", typing.Dict[builtins.str, typing.Any]]] = None,
        network_interface_count: typing.Optional[typing.Union["LaunchTemplateInstanceRequirementsNetworkInterfaceCount", typing.Dict[builtins.str, typing.Any]]] = None,
        on_demand_max_price_percentage_over_lowest_price: typing.Optional[jsii.Number] = None,
        require_hibernate_support: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        spot_max_price_percentage_over_lowest_price: typing.Optional[jsii.Number] = None,
        total_local_storage_gb: typing.Optional[typing.Union["LaunchTemplateInstanceRequirementsTotalLocalStorageGb", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param memory_mib: memory_mib block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#memory_mib LaunchTemplate#memory_mib}
        :param vcpu_count: vcpu_count block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#vcpu_count LaunchTemplate#vcpu_count}
        :param accelerator_count: accelerator_count block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#accelerator_count LaunchTemplate#accelerator_count}
        :param accelerator_manufacturers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#accelerator_manufacturers LaunchTemplate#accelerator_manufacturers}.
        :param accelerator_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#accelerator_names LaunchTemplate#accelerator_names}.
        :param accelerator_total_memory_mib: accelerator_total_memory_mib block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#accelerator_total_memory_mib LaunchTemplate#accelerator_total_memory_mib}
        :param accelerator_types: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#accelerator_types LaunchTemplate#accelerator_types}.
        :param bare_metal: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#bare_metal LaunchTemplate#bare_metal}.
        :param baseline_ebs_bandwidth_mbps: baseline_ebs_bandwidth_mbps block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#baseline_ebs_bandwidth_mbps LaunchTemplate#baseline_ebs_bandwidth_mbps}
        :param burstable_performance: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#burstable_performance LaunchTemplate#burstable_performance}.
        :param cpu_manufacturers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#cpu_manufacturers LaunchTemplate#cpu_manufacturers}.
        :param excluded_instance_types: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#excluded_instance_types LaunchTemplate#excluded_instance_types}.
        :param instance_generations: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#instance_generations LaunchTemplate#instance_generations}.
        :param local_storage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#local_storage LaunchTemplate#local_storage}.
        :param local_storage_types: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#local_storage_types LaunchTemplate#local_storage_types}.
        :param memory_gib_per_vcpu: memory_gib_per_vcpu block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#memory_gib_per_vcpu LaunchTemplate#memory_gib_per_vcpu}
        :param network_interface_count: network_interface_count block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#network_interface_count LaunchTemplate#network_interface_count}
        :param on_demand_max_price_percentage_over_lowest_price: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#on_demand_max_price_percentage_over_lowest_price LaunchTemplate#on_demand_max_price_percentage_over_lowest_price}.
        :param require_hibernate_support: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#require_hibernate_support LaunchTemplate#require_hibernate_support}.
        :param spot_max_price_percentage_over_lowest_price: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#spot_max_price_percentage_over_lowest_price LaunchTemplate#spot_max_price_percentage_over_lowest_price}.
        :param total_local_storage_gb: total_local_storage_gb block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#total_local_storage_gb LaunchTemplate#total_local_storage_gb}
        '''
        if isinstance(memory_mib, dict):
            memory_mib = LaunchTemplateInstanceRequirementsMemoryMib(**memory_mib)
        if isinstance(vcpu_count, dict):
            vcpu_count = LaunchTemplateInstanceRequirementsVcpuCount(**vcpu_count)
        if isinstance(accelerator_count, dict):
            accelerator_count = LaunchTemplateInstanceRequirementsAcceleratorCount(**accelerator_count)
        if isinstance(accelerator_total_memory_mib, dict):
            accelerator_total_memory_mib = LaunchTemplateInstanceRequirementsAcceleratorTotalMemoryMib(**accelerator_total_memory_mib)
        if isinstance(baseline_ebs_bandwidth_mbps, dict):
            baseline_ebs_bandwidth_mbps = LaunchTemplateInstanceRequirementsBaselineEbsBandwidthMbps(**baseline_ebs_bandwidth_mbps)
        if isinstance(memory_gib_per_vcpu, dict):
            memory_gib_per_vcpu = LaunchTemplateInstanceRequirementsMemoryGibPerVcpu(**memory_gib_per_vcpu)
        if isinstance(network_interface_count, dict):
            network_interface_count = LaunchTemplateInstanceRequirementsNetworkInterfaceCount(**network_interface_count)
        if isinstance(total_local_storage_gb, dict):
            total_local_storage_gb = LaunchTemplateInstanceRequirementsTotalLocalStorageGb(**total_local_storage_gb)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f8457f019b0a039cf717b8de08872e0510da42ddc21aabed9ec3a915a9d045d)
            check_type(argname="argument memory_mib", value=memory_mib, expected_type=type_hints["memory_mib"])
            check_type(argname="argument vcpu_count", value=vcpu_count, expected_type=type_hints["vcpu_count"])
            check_type(argname="argument accelerator_count", value=accelerator_count, expected_type=type_hints["accelerator_count"])
            check_type(argname="argument accelerator_manufacturers", value=accelerator_manufacturers, expected_type=type_hints["accelerator_manufacturers"])
            check_type(argname="argument accelerator_names", value=accelerator_names, expected_type=type_hints["accelerator_names"])
            check_type(argname="argument accelerator_total_memory_mib", value=accelerator_total_memory_mib, expected_type=type_hints["accelerator_total_memory_mib"])
            check_type(argname="argument accelerator_types", value=accelerator_types, expected_type=type_hints["accelerator_types"])
            check_type(argname="argument bare_metal", value=bare_metal, expected_type=type_hints["bare_metal"])
            check_type(argname="argument baseline_ebs_bandwidth_mbps", value=baseline_ebs_bandwidth_mbps, expected_type=type_hints["baseline_ebs_bandwidth_mbps"])
            check_type(argname="argument burstable_performance", value=burstable_performance, expected_type=type_hints["burstable_performance"])
            check_type(argname="argument cpu_manufacturers", value=cpu_manufacturers, expected_type=type_hints["cpu_manufacturers"])
            check_type(argname="argument excluded_instance_types", value=excluded_instance_types, expected_type=type_hints["excluded_instance_types"])
            check_type(argname="argument instance_generations", value=instance_generations, expected_type=type_hints["instance_generations"])
            check_type(argname="argument local_storage", value=local_storage, expected_type=type_hints["local_storage"])
            check_type(argname="argument local_storage_types", value=local_storage_types, expected_type=type_hints["local_storage_types"])
            check_type(argname="argument memory_gib_per_vcpu", value=memory_gib_per_vcpu, expected_type=type_hints["memory_gib_per_vcpu"])
            check_type(argname="argument network_interface_count", value=network_interface_count, expected_type=type_hints["network_interface_count"])
            check_type(argname="argument on_demand_max_price_percentage_over_lowest_price", value=on_demand_max_price_percentage_over_lowest_price, expected_type=type_hints["on_demand_max_price_percentage_over_lowest_price"])
            check_type(argname="argument require_hibernate_support", value=require_hibernate_support, expected_type=type_hints["require_hibernate_support"])
            check_type(argname="argument spot_max_price_percentage_over_lowest_price", value=spot_max_price_percentage_over_lowest_price, expected_type=type_hints["spot_max_price_percentage_over_lowest_price"])
            check_type(argname="argument total_local_storage_gb", value=total_local_storage_gb, expected_type=type_hints["total_local_storage_gb"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "memory_mib": memory_mib,
            "vcpu_count": vcpu_count,
        }
        if accelerator_count is not None:
            self._values["accelerator_count"] = accelerator_count
        if accelerator_manufacturers is not None:
            self._values["accelerator_manufacturers"] = accelerator_manufacturers
        if accelerator_names is not None:
            self._values["accelerator_names"] = accelerator_names
        if accelerator_total_memory_mib is not None:
            self._values["accelerator_total_memory_mib"] = accelerator_total_memory_mib
        if accelerator_types is not None:
            self._values["accelerator_types"] = accelerator_types
        if bare_metal is not None:
            self._values["bare_metal"] = bare_metal
        if baseline_ebs_bandwidth_mbps is not None:
            self._values["baseline_ebs_bandwidth_mbps"] = baseline_ebs_bandwidth_mbps
        if burstable_performance is not None:
            self._values["burstable_performance"] = burstable_performance
        if cpu_manufacturers is not None:
            self._values["cpu_manufacturers"] = cpu_manufacturers
        if excluded_instance_types is not None:
            self._values["excluded_instance_types"] = excluded_instance_types
        if instance_generations is not None:
            self._values["instance_generations"] = instance_generations
        if local_storage is not None:
            self._values["local_storage"] = local_storage
        if local_storage_types is not None:
            self._values["local_storage_types"] = local_storage_types
        if memory_gib_per_vcpu is not None:
            self._values["memory_gib_per_vcpu"] = memory_gib_per_vcpu
        if network_interface_count is not None:
            self._values["network_interface_count"] = network_interface_count
        if on_demand_max_price_percentage_over_lowest_price is not None:
            self._values["on_demand_max_price_percentage_over_lowest_price"] = on_demand_max_price_percentage_over_lowest_price
        if require_hibernate_support is not None:
            self._values["require_hibernate_support"] = require_hibernate_support
        if spot_max_price_percentage_over_lowest_price is not None:
            self._values["spot_max_price_percentage_over_lowest_price"] = spot_max_price_percentage_over_lowest_price
        if total_local_storage_gb is not None:
            self._values["total_local_storage_gb"] = total_local_storage_gb

    @builtins.property
    def memory_mib(self) -> "LaunchTemplateInstanceRequirementsMemoryMib":
        '''memory_mib block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#memory_mib LaunchTemplate#memory_mib}
        '''
        result = self._values.get("memory_mib")
        assert result is not None, "Required property 'memory_mib' is missing"
        return typing.cast("LaunchTemplateInstanceRequirementsMemoryMib", result)

    @builtins.property
    def vcpu_count(self) -> "LaunchTemplateInstanceRequirementsVcpuCount":
        '''vcpu_count block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#vcpu_count LaunchTemplate#vcpu_count}
        '''
        result = self._values.get("vcpu_count")
        assert result is not None, "Required property 'vcpu_count' is missing"
        return typing.cast("LaunchTemplateInstanceRequirementsVcpuCount", result)

    @builtins.property
    def accelerator_count(
        self,
    ) -> typing.Optional["LaunchTemplateInstanceRequirementsAcceleratorCount"]:
        '''accelerator_count block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#accelerator_count LaunchTemplate#accelerator_count}
        '''
        result = self._values.get("accelerator_count")
        return typing.cast(typing.Optional["LaunchTemplateInstanceRequirementsAcceleratorCount"], result)

    @builtins.property
    def accelerator_manufacturers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#accelerator_manufacturers LaunchTemplate#accelerator_manufacturers}.'''
        result = self._values.get("accelerator_manufacturers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def accelerator_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#accelerator_names LaunchTemplate#accelerator_names}.'''
        result = self._values.get("accelerator_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def accelerator_total_memory_mib(
        self,
    ) -> typing.Optional["LaunchTemplateInstanceRequirementsAcceleratorTotalMemoryMib"]:
        '''accelerator_total_memory_mib block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#accelerator_total_memory_mib LaunchTemplate#accelerator_total_memory_mib}
        '''
        result = self._values.get("accelerator_total_memory_mib")
        return typing.cast(typing.Optional["LaunchTemplateInstanceRequirementsAcceleratorTotalMemoryMib"], result)

    @builtins.property
    def accelerator_types(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#accelerator_types LaunchTemplate#accelerator_types}.'''
        result = self._values.get("accelerator_types")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def bare_metal(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#bare_metal LaunchTemplate#bare_metal}.'''
        result = self._values.get("bare_metal")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def baseline_ebs_bandwidth_mbps(
        self,
    ) -> typing.Optional["LaunchTemplateInstanceRequirementsBaselineEbsBandwidthMbps"]:
        '''baseline_ebs_bandwidth_mbps block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#baseline_ebs_bandwidth_mbps LaunchTemplate#baseline_ebs_bandwidth_mbps}
        '''
        result = self._values.get("baseline_ebs_bandwidth_mbps")
        return typing.cast(typing.Optional["LaunchTemplateInstanceRequirementsBaselineEbsBandwidthMbps"], result)

    @builtins.property
    def burstable_performance(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#burstable_performance LaunchTemplate#burstable_performance}.'''
        result = self._values.get("burstable_performance")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cpu_manufacturers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#cpu_manufacturers LaunchTemplate#cpu_manufacturers}.'''
        result = self._values.get("cpu_manufacturers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def excluded_instance_types(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#excluded_instance_types LaunchTemplate#excluded_instance_types}.'''
        result = self._values.get("excluded_instance_types")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def instance_generations(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#instance_generations LaunchTemplate#instance_generations}.'''
        result = self._values.get("instance_generations")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def local_storage(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#local_storage LaunchTemplate#local_storage}.'''
        result = self._values.get("local_storage")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def local_storage_types(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#local_storage_types LaunchTemplate#local_storage_types}.'''
        result = self._values.get("local_storage_types")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def memory_gib_per_vcpu(
        self,
    ) -> typing.Optional["LaunchTemplateInstanceRequirementsMemoryGibPerVcpu"]:
        '''memory_gib_per_vcpu block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#memory_gib_per_vcpu LaunchTemplate#memory_gib_per_vcpu}
        '''
        result = self._values.get("memory_gib_per_vcpu")
        return typing.cast(typing.Optional["LaunchTemplateInstanceRequirementsMemoryGibPerVcpu"], result)

    @builtins.property
    def network_interface_count(
        self,
    ) -> typing.Optional["LaunchTemplateInstanceRequirementsNetworkInterfaceCount"]:
        '''network_interface_count block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#network_interface_count LaunchTemplate#network_interface_count}
        '''
        result = self._values.get("network_interface_count")
        return typing.cast(typing.Optional["LaunchTemplateInstanceRequirementsNetworkInterfaceCount"], result)

    @builtins.property
    def on_demand_max_price_percentage_over_lowest_price(
        self,
    ) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#on_demand_max_price_percentage_over_lowest_price LaunchTemplate#on_demand_max_price_percentage_over_lowest_price}.'''
        result = self._values.get("on_demand_max_price_percentage_over_lowest_price")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def require_hibernate_support(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#require_hibernate_support LaunchTemplate#require_hibernate_support}.'''
        result = self._values.get("require_hibernate_support")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def spot_max_price_percentage_over_lowest_price(
        self,
    ) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#spot_max_price_percentage_over_lowest_price LaunchTemplate#spot_max_price_percentage_over_lowest_price}.'''
        result = self._values.get("spot_max_price_percentage_over_lowest_price")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def total_local_storage_gb(
        self,
    ) -> typing.Optional["LaunchTemplateInstanceRequirementsTotalLocalStorageGb"]:
        '''total_local_storage_gb block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#total_local_storage_gb LaunchTemplate#total_local_storage_gb}
        '''
        result = self._values.get("total_local_storage_gb")
        return typing.cast(typing.Optional["LaunchTemplateInstanceRequirementsTotalLocalStorageGb"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LaunchTemplateInstanceRequirements(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.launchTemplate.LaunchTemplateInstanceRequirementsAcceleratorCount",
    jsii_struct_bases=[],
    name_mapping={"max": "max", "min": "min"},
)
class LaunchTemplateInstanceRequirementsAcceleratorCount:
    def __init__(
        self,
        *,
        max: typing.Optional[jsii.Number] = None,
        min: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#max LaunchTemplate#max}.
        :param min: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#min LaunchTemplate#min}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b6a798202add089fc06a4a1bd243ddd2125563a5e49ed9270196c3f308adee8)
            check_type(argname="argument max", value=max, expected_type=type_hints["max"])
            check_type(argname="argument min", value=min, expected_type=type_hints["min"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if max is not None:
            self._values["max"] = max
        if min is not None:
            self._values["min"] = min

    @builtins.property
    def max(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#max LaunchTemplate#max}.'''
        result = self._values.get("max")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#min LaunchTemplate#min}.'''
        result = self._values.get("min")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LaunchTemplateInstanceRequirementsAcceleratorCount(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LaunchTemplateInstanceRequirementsAcceleratorCountOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.launchTemplate.LaunchTemplateInstanceRequirementsAcceleratorCountOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__380b29d2eb7bd4bf7be142fa4611449806b7bc6f306c984da3de823a2abf6102)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMax")
    def reset_max(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMax", []))

    @jsii.member(jsii_name="resetMin")
    def reset_min(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMin", []))

    @builtins.property
    @jsii.member(jsii_name="maxInput")
    def max_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxInput"))

    @builtins.property
    @jsii.member(jsii_name="minInput")
    def min_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minInput"))

    @builtins.property
    @jsii.member(jsii_name="max")
    def max(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "max"))

    @max.setter
    def max(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2d117198b540e41624c69e8889d8537df0bbd561ae5c4c1e3821301fb08790f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "max", value)

    @builtins.property
    @jsii.member(jsii_name="min")
    def min(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "min"))

    @min.setter
    def min(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1dda5fa8d3055b691fd618064ffd0002a2c8cc06529e456dfa574ee508fefab6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "min", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LaunchTemplateInstanceRequirementsAcceleratorCount]:
        return typing.cast(typing.Optional[LaunchTemplateInstanceRequirementsAcceleratorCount], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LaunchTemplateInstanceRequirementsAcceleratorCount],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ee08c4da7a3bb691a3e0a64a9ab643285bbb486c148a9f3bfcd86ca1a2e64ee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.launchTemplate.LaunchTemplateInstanceRequirementsAcceleratorTotalMemoryMib",
    jsii_struct_bases=[],
    name_mapping={"max": "max", "min": "min"},
)
class LaunchTemplateInstanceRequirementsAcceleratorTotalMemoryMib:
    def __init__(
        self,
        *,
        max: typing.Optional[jsii.Number] = None,
        min: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#max LaunchTemplate#max}.
        :param min: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#min LaunchTemplate#min}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d05d33e5a07d4419a8630c97d6d2f3c6aff341568c4dc3b2e00f850a884a1121)
            check_type(argname="argument max", value=max, expected_type=type_hints["max"])
            check_type(argname="argument min", value=min, expected_type=type_hints["min"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if max is not None:
            self._values["max"] = max
        if min is not None:
            self._values["min"] = min

    @builtins.property
    def max(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#max LaunchTemplate#max}.'''
        result = self._values.get("max")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#min LaunchTemplate#min}.'''
        result = self._values.get("min")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LaunchTemplateInstanceRequirementsAcceleratorTotalMemoryMib(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LaunchTemplateInstanceRequirementsAcceleratorTotalMemoryMibOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.launchTemplate.LaunchTemplateInstanceRequirementsAcceleratorTotalMemoryMibOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__94f753a9f54c71d6937d413d588c400a878c0f19f331ee6900c8e552597f48ed)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMax")
    def reset_max(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMax", []))

    @jsii.member(jsii_name="resetMin")
    def reset_min(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMin", []))

    @builtins.property
    @jsii.member(jsii_name="maxInput")
    def max_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxInput"))

    @builtins.property
    @jsii.member(jsii_name="minInput")
    def min_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minInput"))

    @builtins.property
    @jsii.member(jsii_name="max")
    def max(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "max"))

    @max.setter
    def max(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__71b4c140a502c72586cacb61191de5261c42e0f1be1b1f1423aad50783ea1274)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "max", value)

    @builtins.property
    @jsii.member(jsii_name="min")
    def min(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "min"))

    @min.setter
    def min(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db46514aa7bac365bc006c6314897c2bdb200ca552c120ecc6e99a2252e4795a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "min", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LaunchTemplateInstanceRequirementsAcceleratorTotalMemoryMib]:
        return typing.cast(typing.Optional[LaunchTemplateInstanceRequirementsAcceleratorTotalMemoryMib], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LaunchTemplateInstanceRequirementsAcceleratorTotalMemoryMib],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2c51f8a7ee12cc31f6d6bf92c3349643c8c86e2044b2554558f385b5d0f0b8f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.launchTemplate.LaunchTemplateInstanceRequirementsBaselineEbsBandwidthMbps",
    jsii_struct_bases=[],
    name_mapping={"max": "max", "min": "min"},
)
class LaunchTemplateInstanceRequirementsBaselineEbsBandwidthMbps:
    def __init__(
        self,
        *,
        max: typing.Optional[jsii.Number] = None,
        min: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#max LaunchTemplate#max}.
        :param min: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#min LaunchTemplate#min}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20188ccb8c6623490ccd725c9a437100596250cb0fb6d85a29a7a5157f35e6c5)
            check_type(argname="argument max", value=max, expected_type=type_hints["max"])
            check_type(argname="argument min", value=min, expected_type=type_hints["min"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if max is not None:
            self._values["max"] = max
        if min is not None:
            self._values["min"] = min

    @builtins.property
    def max(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#max LaunchTemplate#max}.'''
        result = self._values.get("max")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#min LaunchTemplate#min}.'''
        result = self._values.get("min")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LaunchTemplateInstanceRequirementsBaselineEbsBandwidthMbps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LaunchTemplateInstanceRequirementsBaselineEbsBandwidthMbpsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.launchTemplate.LaunchTemplateInstanceRequirementsBaselineEbsBandwidthMbpsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cb52ab11ad9c09e098e5210161ba6df49137cc4d8cbc74c1927b9fa2f8528da8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMax")
    def reset_max(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMax", []))

    @jsii.member(jsii_name="resetMin")
    def reset_min(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMin", []))

    @builtins.property
    @jsii.member(jsii_name="maxInput")
    def max_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxInput"))

    @builtins.property
    @jsii.member(jsii_name="minInput")
    def min_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minInput"))

    @builtins.property
    @jsii.member(jsii_name="max")
    def max(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "max"))

    @max.setter
    def max(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53d0f095820d91e593dfa8536acca826b0d1ebd692eeaa4f94ef66c350927a31)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "max", value)

    @builtins.property
    @jsii.member(jsii_name="min")
    def min(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "min"))

    @min.setter
    def min(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e0b9fa9655ab3b7e74dc1bd1cac0948b572b3f2b343682350d1d9e8d9ac3515)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "min", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LaunchTemplateInstanceRequirementsBaselineEbsBandwidthMbps]:
        return typing.cast(typing.Optional[LaunchTemplateInstanceRequirementsBaselineEbsBandwidthMbps], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LaunchTemplateInstanceRequirementsBaselineEbsBandwidthMbps],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7997bc1f97e18303601a3f9cef7e04e77bb66b245fabccaef4b64de1a5b20bd3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.launchTemplate.LaunchTemplateInstanceRequirementsMemoryGibPerVcpu",
    jsii_struct_bases=[],
    name_mapping={"max": "max", "min": "min"},
)
class LaunchTemplateInstanceRequirementsMemoryGibPerVcpu:
    def __init__(
        self,
        *,
        max: typing.Optional[jsii.Number] = None,
        min: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#max LaunchTemplate#max}.
        :param min: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#min LaunchTemplate#min}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0acd62f11701b125a31266e304ed97306d0143f1adc40fef1a90c8d9d710660a)
            check_type(argname="argument max", value=max, expected_type=type_hints["max"])
            check_type(argname="argument min", value=min, expected_type=type_hints["min"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if max is not None:
            self._values["max"] = max
        if min is not None:
            self._values["min"] = min

    @builtins.property
    def max(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#max LaunchTemplate#max}.'''
        result = self._values.get("max")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#min LaunchTemplate#min}.'''
        result = self._values.get("min")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LaunchTemplateInstanceRequirementsMemoryGibPerVcpu(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LaunchTemplateInstanceRequirementsMemoryGibPerVcpuOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.launchTemplate.LaunchTemplateInstanceRequirementsMemoryGibPerVcpuOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__852249a066bb8449717d494e4e0fe2f981a73e977cbfc27e73ff2fd4e137eb09)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMax")
    def reset_max(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMax", []))

    @jsii.member(jsii_name="resetMin")
    def reset_min(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMin", []))

    @builtins.property
    @jsii.member(jsii_name="maxInput")
    def max_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxInput"))

    @builtins.property
    @jsii.member(jsii_name="minInput")
    def min_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minInput"))

    @builtins.property
    @jsii.member(jsii_name="max")
    def max(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "max"))

    @max.setter
    def max(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__16b0c4b3a4c9f82ad186dbaeb004df4cd64ce851498600d2e352680381043539)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "max", value)

    @builtins.property
    @jsii.member(jsii_name="min")
    def min(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "min"))

    @min.setter
    def min(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0aabbfe3c5cd10c4608ed1a56f5bd32a5645e557e72f4535234429ea0d28b2b3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "min", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LaunchTemplateInstanceRequirementsMemoryGibPerVcpu]:
        return typing.cast(typing.Optional[LaunchTemplateInstanceRequirementsMemoryGibPerVcpu], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LaunchTemplateInstanceRequirementsMemoryGibPerVcpu],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a30925864ad1583621a3d372eddf7acce6c719a2274cd178bfa5d0b4bd1f3254)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.launchTemplate.LaunchTemplateInstanceRequirementsMemoryMib",
    jsii_struct_bases=[],
    name_mapping={"min": "min", "max": "max"},
)
class LaunchTemplateInstanceRequirementsMemoryMib:
    def __init__(
        self,
        *,
        min: jsii.Number,
        max: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param min: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#min LaunchTemplate#min}.
        :param max: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#max LaunchTemplate#max}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8cb9c6d69786f3a8a54dbdc4890afaec006be177a03e6044f868031e6bdced0)
            check_type(argname="argument min", value=min, expected_type=type_hints["min"])
            check_type(argname="argument max", value=max, expected_type=type_hints["max"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "min": min,
        }
        if max is not None:
            self._values["max"] = max

    @builtins.property
    def min(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#min LaunchTemplate#min}.'''
        result = self._values.get("min")
        assert result is not None, "Required property 'min' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def max(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#max LaunchTemplate#max}.'''
        result = self._values.get("max")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LaunchTemplateInstanceRequirementsMemoryMib(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LaunchTemplateInstanceRequirementsMemoryMibOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.launchTemplate.LaunchTemplateInstanceRequirementsMemoryMibOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1a93b3df3c7e78b09251e0c16b9151255f43c36314742654ee22b1d164e33feb)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMax")
    def reset_max(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMax", []))

    @builtins.property
    @jsii.member(jsii_name="maxInput")
    def max_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxInput"))

    @builtins.property
    @jsii.member(jsii_name="minInput")
    def min_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minInput"))

    @builtins.property
    @jsii.member(jsii_name="max")
    def max(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "max"))

    @max.setter
    def max(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18efe0511d9f70cc0ac5ea111b6284bf006281c41065cfbfc057f32abdf809e1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "max", value)

    @builtins.property
    @jsii.member(jsii_name="min")
    def min(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "min"))

    @min.setter
    def min(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3dd308aa80a13e0ee95d6568f10238a11f48073c1be2071a813080756ff357b7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "min", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LaunchTemplateInstanceRequirementsMemoryMib]:
        return typing.cast(typing.Optional[LaunchTemplateInstanceRequirementsMemoryMib], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LaunchTemplateInstanceRequirementsMemoryMib],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c43316b2707279abd2138e1d02d0e3094cfc3c7ec39f1271a21399c0ebfd7fd5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.launchTemplate.LaunchTemplateInstanceRequirementsNetworkInterfaceCount",
    jsii_struct_bases=[],
    name_mapping={"max": "max", "min": "min"},
)
class LaunchTemplateInstanceRequirementsNetworkInterfaceCount:
    def __init__(
        self,
        *,
        max: typing.Optional[jsii.Number] = None,
        min: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#max LaunchTemplate#max}.
        :param min: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#min LaunchTemplate#min}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac60803915a802756beaa5c3bdfb00ebeaa785ceba24504e10c19da9a162540f)
            check_type(argname="argument max", value=max, expected_type=type_hints["max"])
            check_type(argname="argument min", value=min, expected_type=type_hints["min"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if max is not None:
            self._values["max"] = max
        if min is not None:
            self._values["min"] = min

    @builtins.property
    def max(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#max LaunchTemplate#max}.'''
        result = self._values.get("max")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#min LaunchTemplate#min}.'''
        result = self._values.get("min")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LaunchTemplateInstanceRequirementsNetworkInterfaceCount(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LaunchTemplateInstanceRequirementsNetworkInterfaceCountOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.launchTemplate.LaunchTemplateInstanceRequirementsNetworkInterfaceCountOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d7eec6e3ee782e85ac4668243cabeb060e08ea32f5d83605f76ec6f58ea4eace)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMax")
    def reset_max(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMax", []))

    @jsii.member(jsii_name="resetMin")
    def reset_min(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMin", []))

    @builtins.property
    @jsii.member(jsii_name="maxInput")
    def max_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxInput"))

    @builtins.property
    @jsii.member(jsii_name="minInput")
    def min_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minInput"))

    @builtins.property
    @jsii.member(jsii_name="max")
    def max(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "max"))

    @max.setter
    def max(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c6eda9cf8f9ff82172e0c35966a756349680c77b07fa9072a3a5bd5724ea290)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "max", value)

    @builtins.property
    @jsii.member(jsii_name="min")
    def min(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "min"))

    @min.setter
    def min(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49de90c3085e5b1699694ffb1502774741d972235633843d2040659552fc8554)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "min", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LaunchTemplateInstanceRequirementsNetworkInterfaceCount]:
        return typing.cast(typing.Optional[LaunchTemplateInstanceRequirementsNetworkInterfaceCount], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LaunchTemplateInstanceRequirementsNetworkInterfaceCount],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1514e7b8c0a83b58b49bcfd3e44fc2e6cdb3ce85643473422d55d63ba43b13f4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LaunchTemplateInstanceRequirementsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.launchTemplate.LaunchTemplateInstanceRequirementsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a3b2dac7fc47ec0509301b7891c111802b55647a221759c455b124e8ba988070)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAcceleratorCount")
    def put_accelerator_count(
        self,
        *,
        max: typing.Optional[jsii.Number] = None,
        min: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#max LaunchTemplate#max}.
        :param min: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#min LaunchTemplate#min}.
        '''
        value = LaunchTemplateInstanceRequirementsAcceleratorCount(max=max, min=min)

        return typing.cast(None, jsii.invoke(self, "putAcceleratorCount", [value]))

    @jsii.member(jsii_name="putAcceleratorTotalMemoryMib")
    def put_accelerator_total_memory_mib(
        self,
        *,
        max: typing.Optional[jsii.Number] = None,
        min: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#max LaunchTemplate#max}.
        :param min: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#min LaunchTemplate#min}.
        '''
        value = LaunchTemplateInstanceRequirementsAcceleratorTotalMemoryMib(
            max=max, min=min
        )

        return typing.cast(None, jsii.invoke(self, "putAcceleratorTotalMemoryMib", [value]))

    @jsii.member(jsii_name="putBaselineEbsBandwidthMbps")
    def put_baseline_ebs_bandwidth_mbps(
        self,
        *,
        max: typing.Optional[jsii.Number] = None,
        min: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#max LaunchTemplate#max}.
        :param min: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#min LaunchTemplate#min}.
        '''
        value = LaunchTemplateInstanceRequirementsBaselineEbsBandwidthMbps(
            max=max, min=min
        )

        return typing.cast(None, jsii.invoke(self, "putBaselineEbsBandwidthMbps", [value]))

    @jsii.member(jsii_name="putMemoryGibPerVcpu")
    def put_memory_gib_per_vcpu(
        self,
        *,
        max: typing.Optional[jsii.Number] = None,
        min: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#max LaunchTemplate#max}.
        :param min: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#min LaunchTemplate#min}.
        '''
        value = LaunchTemplateInstanceRequirementsMemoryGibPerVcpu(max=max, min=min)

        return typing.cast(None, jsii.invoke(self, "putMemoryGibPerVcpu", [value]))

    @jsii.member(jsii_name="putMemoryMib")
    def put_memory_mib(
        self,
        *,
        min: jsii.Number,
        max: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param min: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#min LaunchTemplate#min}.
        :param max: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#max LaunchTemplate#max}.
        '''
        value = LaunchTemplateInstanceRequirementsMemoryMib(min=min, max=max)

        return typing.cast(None, jsii.invoke(self, "putMemoryMib", [value]))

    @jsii.member(jsii_name="putNetworkInterfaceCount")
    def put_network_interface_count(
        self,
        *,
        max: typing.Optional[jsii.Number] = None,
        min: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#max LaunchTemplate#max}.
        :param min: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#min LaunchTemplate#min}.
        '''
        value = LaunchTemplateInstanceRequirementsNetworkInterfaceCount(
            max=max, min=min
        )

        return typing.cast(None, jsii.invoke(self, "putNetworkInterfaceCount", [value]))

    @jsii.member(jsii_name="putTotalLocalStorageGb")
    def put_total_local_storage_gb(
        self,
        *,
        max: typing.Optional[jsii.Number] = None,
        min: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#max LaunchTemplate#max}.
        :param min: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#min LaunchTemplate#min}.
        '''
        value = LaunchTemplateInstanceRequirementsTotalLocalStorageGb(max=max, min=min)

        return typing.cast(None, jsii.invoke(self, "putTotalLocalStorageGb", [value]))

    @jsii.member(jsii_name="putVcpuCount")
    def put_vcpu_count(
        self,
        *,
        min: jsii.Number,
        max: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param min: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#min LaunchTemplate#min}.
        :param max: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#max LaunchTemplate#max}.
        '''
        value = LaunchTemplateInstanceRequirementsVcpuCount(min=min, max=max)

        return typing.cast(None, jsii.invoke(self, "putVcpuCount", [value]))

    @jsii.member(jsii_name="resetAcceleratorCount")
    def reset_accelerator_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAcceleratorCount", []))

    @jsii.member(jsii_name="resetAcceleratorManufacturers")
    def reset_accelerator_manufacturers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAcceleratorManufacturers", []))

    @jsii.member(jsii_name="resetAcceleratorNames")
    def reset_accelerator_names(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAcceleratorNames", []))

    @jsii.member(jsii_name="resetAcceleratorTotalMemoryMib")
    def reset_accelerator_total_memory_mib(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAcceleratorTotalMemoryMib", []))

    @jsii.member(jsii_name="resetAcceleratorTypes")
    def reset_accelerator_types(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAcceleratorTypes", []))

    @jsii.member(jsii_name="resetBareMetal")
    def reset_bare_metal(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBareMetal", []))

    @jsii.member(jsii_name="resetBaselineEbsBandwidthMbps")
    def reset_baseline_ebs_bandwidth_mbps(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBaselineEbsBandwidthMbps", []))

    @jsii.member(jsii_name="resetBurstablePerformance")
    def reset_burstable_performance(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBurstablePerformance", []))

    @jsii.member(jsii_name="resetCpuManufacturers")
    def reset_cpu_manufacturers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCpuManufacturers", []))

    @jsii.member(jsii_name="resetExcludedInstanceTypes")
    def reset_excluded_instance_types(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExcludedInstanceTypes", []))

    @jsii.member(jsii_name="resetInstanceGenerations")
    def reset_instance_generations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceGenerations", []))

    @jsii.member(jsii_name="resetLocalStorage")
    def reset_local_storage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocalStorage", []))

    @jsii.member(jsii_name="resetLocalStorageTypes")
    def reset_local_storage_types(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocalStorageTypes", []))

    @jsii.member(jsii_name="resetMemoryGibPerVcpu")
    def reset_memory_gib_per_vcpu(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMemoryGibPerVcpu", []))

    @jsii.member(jsii_name="resetNetworkInterfaceCount")
    def reset_network_interface_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworkInterfaceCount", []))

    @jsii.member(jsii_name="resetOnDemandMaxPricePercentageOverLowestPrice")
    def reset_on_demand_max_price_percentage_over_lowest_price(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOnDemandMaxPricePercentageOverLowestPrice", []))

    @jsii.member(jsii_name="resetRequireHibernateSupport")
    def reset_require_hibernate_support(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequireHibernateSupport", []))

    @jsii.member(jsii_name="resetSpotMaxPricePercentageOverLowestPrice")
    def reset_spot_max_price_percentage_over_lowest_price(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSpotMaxPricePercentageOverLowestPrice", []))

    @jsii.member(jsii_name="resetTotalLocalStorageGb")
    def reset_total_local_storage_gb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTotalLocalStorageGb", []))

    @builtins.property
    @jsii.member(jsii_name="acceleratorCount")
    def accelerator_count(
        self,
    ) -> LaunchTemplateInstanceRequirementsAcceleratorCountOutputReference:
        return typing.cast(LaunchTemplateInstanceRequirementsAcceleratorCountOutputReference, jsii.get(self, "acceleratorCount"))

    @builtins.property
    @jsii.member(jsii_name="acceleratorTotalMemoryMib")
    def accelerator_total_memory_mib(
        self,
    ) -> LaunchTemplateInstanceRequirementsAcceleratorTotalMemoryMibOutputReference:
        return typing.cast(LaunchTemplateInstanceRequirementsAcceleratorTotalMemoryMibOutputReference, jsii.get(self, "acceleratorTotalMemoryMib"))

    @builtins.property
    @jsii.member(jsii_name="baselineEbsBandwidthMbps")
    def baseline_ebs_bandwidth_mbps(
        self,
    ) -> LaunchTemplateInstanceRequirementsBaselineEbsBandwidthMbpsOutputReference:
        return typing.cast(LaunchTemplateInstanceRequirementsBaselineEbsBandwidthMbpsOutputReference, jsii.get(self, "baselineEbsBandwidthMbps"))

    @builtins.property
    @jsii.member(jsii_name="memoryGibPerVcpu")
    def memory_gib_per_vcpu(
        self,
    ) -> LaunchTemplateInstanceRequirementsMemoryGibPerVcpuOutputReference:
        return typing.cast(LaunchTemplateInstanceRequirementsMemoryGibPerVcpuOutputReference, jsii.get(self, "memoryGibPerVcpu"))

    @builtins.property
    @jsii.member(jsii_name="memoryMib")
    def memory_mib(self) -> LaunchTemplateInstanceRequirementsMemoryMibOutputReference:
        return typing.cast(LaunchTemplateInstanceRequirementsMemoryMibOutputReference, jsii.get(self, "memoryMib"))

    @builtins.property
    @jsii.member(jsii_name="networkInterfaceCount")
    def network_interface_count(
        self,
    ) -> LaunchTemplateInstanceRequirementsNetworkInterfaceCountOutputReference:
        return typing.cast(LaunchTemplateInstanceRequirementsNetworkInterfaceCountOutputReference, jsii.get(self, "networkInterfaceCount"))

    @builtins.property
    @jsii.member(jsii_name="totalLocalStorageGb")
    def total_local_storage_gb(
        self,
    ) -> "LaunchTemplateInstanceRequirementsTotalLocalStorageGbOutputReference":
        return typing.cast("LaunchTemplateInstanceRequirementsTotalLocalStorageGbOutputReference", jsii.get(self, "totalLocalStorageGb"))

    @builtins.property
    @jsii.member(jsii_name="vcpuCount")
    def vcpu_count(
        self,
    ) -> "LaunchTemplateInstanceRequirementsVcpuCountOutputReference":
        return typing.cast("LaunchTemplateInstanceRequirementsVcpuCountOutputReference", jsii.get(self, "vcpuCount"))

    @builtins.property
    @jsii.member(jsii_name="acceleratorCountInput")
    def accelerator_count_input(
        self,
    ) -> typing.Optional[LaunchTemplateInstanceRequirementsAcceleratorCount]:
        return typing.cast(typing.Optional[LaunchTemplateInstanceRequirementsAcceleratorCount], jsii.get(self, "acceleratorCountInput"))

    @builtins.property
    @jsii.member(jsii_name="acceleratorManufacturersInput")
    def accelerator_manufacturers_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "acceleratorManufacturersInput"))

    @builtins.property
    @jsii.member(jsii_name="acceleratorNamesInput")
    def accelerator_names_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "acceleratorNamesInput"))

    @builtins.property
    @jsii.member(jsii_name="acceleratorTotalMemoryMibInput")
    def accelerator_total_memory_mib_input(
        self,
    ) -> typing.Optional[LaunchTemplateInstanceRequirementsAcceleratorTotalMemoryMib]:
        return typing.cast(typing.Optional[LaunchTemplateInstanceRequirementsAcceleratorTotalMemoryMib], jsii.get(self, "acceleratorTotalMemoryMibInput"))

    @builtins.property
    @jsii.member(jsii_name="acceleratorTypesInput")
    def accelerator_types_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "acceleratorTypesInput"))

    @builtins.property
    @jsii.member(jsii_name="bareMetalInput")
    def bare_metal_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bareMetalInput"))

    @builtins.property
    @jsii.member(jsii_name="baselineEbsBandwidthMbpsInput")
    def baseline_ebs_bandwidth_mbps_input(
        self,
    ) -> typing.Optional[LaunchTemplateInstanceRequirementsBaselineEbsBandwidthMbps]:
        return typing.cast(typing.Optional[LaunchTemplateInstanceRequirementsBaselineEbsBandwidthMbps], jsii.get(self, "baselineEbsBandwidthMbpsInput"))

    @builtins.property
    @jsii.member(jsii_name="burstablePerformanceInput")
    def burstable_performance_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "burstablePerformanceInput"))

    @builtins.property
    @jsii.member(jsii_name="cpuManufacturersInput")
    def cpu_manufacturers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "cpuManufacturersInput"))

    @builtins.property
    @jsii.member(jsii_name="excludedInstanceTypesInput")
    def excluded_instance_types_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "excludedInstanceTypesInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceGenerationsInput")
    def instance_generations_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "instanceGenerationsInput"))

    @builtins.property
    @jsii.member(jsii_name="localStorageInput")
    def local_storage_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "localStorageInput"))

    @builtins.property
    @jsii.member(jsii_name="localStorageTypesInput")
    def local_storage_types_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "localStorageTypesInput"))

    @builtins.property
    @jsii.member(jsii_name="memoryGibPerVcpuInput")
    def memory_gib_per_vcpu_input(
        self,
    ) -> typing.Optional[LaunchTemplateInstanceRequirementsMemoryGibPerVcpu]:
        return typing.cast(typing.Optional[LaunchTemplateInstanceRequirementsMemoryGibPerVcpu], jsii.get(self, "memoryGibPerVcpuInput"))

    @builtins.property
    @jsii.member(jsii_name="memoryMibInput")
    def memory_mib_input(
        self,
    ) -> typing.Optional[LaunchTemplateInstanceRequirementsMemoryMib]:
        return typing.cast(typing.Optional[LaunchTemplateInstanceRequirementsMemoryMib], jsii.get(self, "memoryMibInput"))

    @builtins.property
    @jsii.member(jsii_name="networkInterfaceCountInput")
    def network_interface_count_input(
        self,
    ) -> typing.Optional[LaunchTemplateInstanceRequirementsNetworkInterfaceCount]:
        return typing.cast(typing.Optional[LaunchTemplateInstanceRequirementsNetworkInterfaceCount], jsii.get(self, "networkInterfaceCountInput"))

    @builtins.property
    @jsii.member(jsii_name="onDemandMaxPricePercentageOverLowestPriceInput")
    def on_demand_max_price_percentage_over_lowest_price_input(
        self,
    ) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "onDemandMaxPricePercentageOverLowestPriceInput"))

    @builtins.property
    @jsii.member(jsii_name="requireHibernateSupportInput")
    def require_hibernate_support_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "requireHibernateSupportInput"))

    @builtins.property
    @jsii.member(jsii_name="spotMaxPricePercentageOverLowestPriceInput")
    def spot_max_price_percentage_over_lowest_price_input(
        self,
    ) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "spotMaxPricePercentageOverLowestPriceInput"))

    @builtins.property
    @jsii.member(jsii_name="totalLocalStorageGbInput")
    def total_local_storage_gb_input(
        self,
    ) -> typing.Optional["LaunchTemplateInstanceRequirementsTotalLocalStorageGb"]:
        return typing.cast(typing.Optional["LaunchTemplateInstanceRequirementsTotalLocalStorageGb"], jsii.get(self, "totalLocalStorageGbInput"))

    @builtins.property
    @jsii.member(jsii_name="vcpuCountInput")
    def vcpu_count_input(
        self,
    ) -> typing.Optional["LaunchTemplateInstanceRequirementsVcpuCount"]:
        return typing.cast(typing.Optional["LaunchTemplateInstanceRequirementsVcpuCount"], jsii.get(self, "vcpuCountInput"))

    @builtins.property
    @jsii.member(jsii_name="acceleratorManufacturers")
    def accelerator_manufacturers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "acceleratorManufacturers"))

    @accelerator_manufacturers.setter
    def accelerator_manufacturers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3729dd4b2be2a8af6439303b054b77ef9bfe45c634f216e97d74a94a8f0da587)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "acceleratorManufacturers", value)

    @builtins.property
    @jsii.member(jsii_name="acceleratorNames")
    def accelerator_names(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "acceleratorNames"))

    @accelerator_names.setter
    def accelerator_names(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d2a787f11c10b85d5c3d66dfa7438a6d9e78c18479a6148be3dad5b9a2dfc7e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "acceleratorNames", value)

    @builtins.property
    @jsii.member(jsii_name="acceleratorTypes")
    def accelerator_types(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "acceleratorTypes"))

    @accelerator_types.setter
    def accelerator_types(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c6804e09f1cf6c2a2ce8f5f4e92317e719934c1c37757fa0db14ecb47555264)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "acceleratorTypes", value)

    @builtins.property
    @jsii.member(jsii_name="bareMetal")
    def bare_metal(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bareMetal"))

    @bare_metal.setter
    def bare_metal(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d00cc1fddb1e740fbeff8fd9e2dbfbc9ad61543de6d9813c62d23a7c8be80d8a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bareMetal", value)

    @builtins.property
    @jsii.member(jsii_name="burstablePerformance")
    def burstable_performance(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "burstablePerformance"))

    @burstable_performance.setter
    def burstable_performance(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6770fb529720a09c5e5b7b6dd17063f83300787ae2a1c2425224efb9fabaa019)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "burstablePerformance", value)

    @builtins.property
    @jsii.member(jsii_name="cpuManufacturers")
    def cpu_manufacturers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "cpuManufacturers"))

    @cpu_manufacturers.setter
    def cpu_manufacturers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09f44d66810a54877609a834cdb70cb1a9f9eb8239d1cf891626a7388144690d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpuManufacturers", value)

    @builtins.property
    @jsii.member(jsii_name="excludedInstanceTypes")
    def excluded_instance_types(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "excludedInstanceTypes"))

    @excluded_instance_types.setter
    def excluded_instance_types(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf7e42e2b5f7b947108d604fac78dd543eb53a1eca4f12e24ae354112c338322)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "excludedInstanceTypes", value)

    @builtins.property
    @jsii.member(jsii_name="instanceGenerations")
    def instance_generations(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "instanceGenerations"))

    @instance_generations.setter
    def instance_generations(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0331204cd3c45c3a6150675ec0d2e0e99a9e4d1ef2069b047852993a1433074a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceGenerations", value)

    @builtins.property
    @jsii.member(jsii_name="localStorage")
    def local_storage(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "localStorage"))

    @local_storage.setter
    def local_storage(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e594b289d68e216e382236abbf6740f3d062960291eb5ac5781f3713c1e6ed81)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "localStorage", value)

    @builtins.property
    @jsii.member(jsii_name="localStorageTypes")
    def local_storage_types(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "localStorageTypes"))

    @local_storage_types.setter
    def local_storage_types(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fcc7524b102e0108f4a47c1dbec2f2a324bd088fb2f1da283fcca023fe5d72e5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "localStorageTypes", value)

    @builtins.property
    @jsii.member(jsii_name="onDemandMaxPricePercentageOverLowestPrice")
    def on_demand_max_price_percentage_over_lowest_price(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "onDemandMaxPricePercentageOverLowestPrice"))

    @on_demand_max_price_percentage_over_lowest_price.setter
    def on_demand_max_price_percentage_over_lowest_price(
        self,
        value: jsii.Number,
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f3847a1ed4685bad15ae5ffbe3316781f36f99b63ddd1317560de254f5d85093)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "onDemandMaxPricePercentageOverLowestPrice", value)

    @builtins.property
    @jsii.member(jsii_name="requireHibernateSupport")
    def require_hibernate_support(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "requireHibernateSupport"))

    @require_hibernate_support.setter
    def require_hibernate_support(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__328e2eab9826979a4e8e079855e6b100112f0e906878d530e49a0018ccabdfa3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requireHibernateSupport", value)

    @builtins.property
    @jsii.member(jsii_name="spotMaxPricePercentageOverLowestPrice")
    def spot_max_price_percentage_over_lowest_price(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "spotMaxPricePercentageOverLowestPrice"))

    @spot_max_price_percentage_over_lowest_price.setter
    def spot_max_price_percentage_over_lowest_price(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7a985566e293659665fc55eb05b33414dd3501babf35f54e12df3888e0d3da2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "spotMaxPricePercentageOverLowestPrice", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LaunchTemplateInstanceRequirements]:
        return typing.cast(typing.Optional[LaunchTemplateInstanceRequirements], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LaunchTemplateInstanceRequirements],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__681ed963193840ea53c9a6aba7ae101c37277cbf5202eb1320b7ee6562f584d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.launchTemplate.LaunchTemplateInstanceRequirementsTotalLocalStorageGb",
    jsii_struct_bases=[],
    name_mapping={"max": "max", "min": "min"},
)
class LaunchTemplateInstanceRequirementsTotalLocalStorageGb:
    def __init__(
        self,
        *,
        max: typing.Optional[jsii.Number] = None,
        min: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#max LaunchTemplate#max}.
        :param min: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#min LaunchTemplate#min}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0882ba1df259250c98833dbfcb3f53ca75fd02605f6f5c3a1280e8bb8575f723)
            check_type(argname="argument max", value=max, expected_type=type_hints["max"])
            check_type(argname="argument min", value=min, expected_type=type_hints["min"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if max is not None:
            self._values["max"] = max
        if min is not None:
            self._values["min"] = min

    @builtins.property
    def max(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#max LaunchTemplate#max}.'''
        result = self._values.get("max")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#min LaunchTemplate#min}.'''
        result = self._values.get("min")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LaunchTemplateInstanceRequirementsTotalLocalStorageGb(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LaunchTemplateInstanceRequirementsTotalLocalStorageGbOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.launchTemplate.LaunchTemplateInstanceRequirementsTotalLocalStorageGbOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0649571b73946846f7057e7a973efae73dc54bc1e7ec1c19df973fd57cadcb8b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMax")
    def reset_max(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMax", []))

    @jsii.member(jsii_name="resetMin")
    def reset_min(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMin", []))

    @builtins.property
    @jsii.member(jsii_name="maxInput")
    def max_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxInput"))

    @builtins.property
    @jsii.member(jsii_name="minInput")
    def min_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minInput"))

    @builtins.property
    @jsii.member(jsii_name="max")
    def max(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "max"))

    @max.setter
    def max(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a911ce38ac98dd86da2d3934207d412ed9af302f0dc17bc2d55a8210d5fc176d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "max", value)

    @builtins.property
    @jsii.member(jsii_name="min")
    def min(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "min"))

    @min.setter
    def min(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5a58be4ceb7a219d411fdda44d0912a2f128b53795fea012ccd98993f7ff2be)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "min", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LaunchTemplateInstanceRequirementsTotalLocalStorageGb]:
        return typing.cast(typing.Optional[LaunchTemplateInstanceRequirementsTotalLocalStorageGb], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LaunchTemplateInstanceRequirementsTotalLocalStorageGb],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7bde4783836071a54f25afc3e2d5c2303120371d4ff79df1ece9c7551c8b69e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.launchTemplate.LaunchTemplateInstanceRequirementsVcpuCount",
    jsii_struct_bases=[],
    name_mapping={"min": "min", "max": "max"},
)
class LaunchTemplateInstanceRequirementsVcpuCount:
    def __init__(
        self,
        *,
        min: jsii.Number,
        max: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param min: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#min LaunchTemplate#min}.
        :param max: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#max LaunchTemplate#max}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe9791c3c8e700956dd5e44ce955d6e2e1f98263926390e147d0dc57a612cb25)
            check_type(argname="argument min", value=min, expected_type=type_hints["min"])
            check_type(argname="argument max", value=max, expected_type=type_hints["max"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "min": min,
        }
        if max is not None:
            self._values["max"] = max

    @builtins.property
    def min(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#min LaunchTemplate#min}.'''
        result = self._values.get("min")
        assert result is not None, "Required property 'min' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def max(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#max LaunchTemplate#max}.'''
        result = self._values.get("max")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LaunchTemplateInstanceRequirementsVcpuCount(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LaunchTemplateInstanceRequirementsVcpuCountOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.launchTemplate.LaunchTemplateInstanceRequirementsVcpuCountOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__73b401ac4da410aa9c24cdb81a965e4d9d6fa045b485568cfacc1f2c86ec0453)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMax")
    def reset_max(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMax", []))

    @builtins.property
    @jsii.member(jsii_name="maxInput")
    def max_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxInput"))

    @builtins.property
    @jsii.member(jsii_name="minInput")
    def min_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minInput"))

    @builtins.property
    @jsii.member(jsii_name="max")
    def max(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "max"))

    @max.setter
    def max(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9bac5f752f9534460e4c4c871b2b60601fd76bf7c95240626511c0a334b041b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "max", value)

    @builtins.property
    @jsii.member(jsii_name="min")
    def min(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "min"))

    @min.setter
    def min(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bcccfe9783dfa294d71742c00a07764436fd4423594b113f428af264898de306)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "min", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LaunchTemplateInstanceRequirementsVcpuCount]:
        return typing.cast(typing.Optional[LaunchTemplateInstanceRequirementsVcpuCount], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LaunchTemplateInstanceRequirementsVcpuCount],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__945b0d283848e06a1e89f369e837f080d89594695c9cfcca6d4b55701a1e5870)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.launchTemplate.LaunchTemplateLicenseSpecification",
    jsii_struct_bases=[],
    name_mapping={"license_configuration_arn": "licenseConfigurationArn"},
)
class LaunchTemplateLicenseSpecification:
    def __init__(self, *, license_configuration_arn: builtins.str) -> None:
        '''
        :param license_configuration_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#license_configuration_arn LaunchTemplate#license_configuration_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a752a77ac939e70e9a078322047b6ad51baeb4fce4859a4fe424458870c24d52)
            check_type(argname="argument license_configuration_arn", value=license_configuration_arn, expected_type=type_hints["license_configuration_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "license_configuration_arn": license_configuration_arn,
        }

    @builtins.property
    def license_configuration_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#license_configuration_arn LaunchTemplate#license_configuration_arn}.'''
        result = self._values.get("license_configuration_arn")
        assert result is not None, "Required property 'license_configuration_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LaunchTemplateLicenseSpecification(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LaunchTemplateLicenseSpecificationList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.launchTemplate.LaunchTemplateLicenseSpecificationList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9600d60e42e7d35e6f1ab35c7c51e8738a3de132be9647168578acd663aa6297)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LaunchTemplateLicenseSpecificationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb3f38e7e4ebc36a25874684dd6fe3a7bf3a629adfb2a93b92545f2f8d2410e6)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LaunchTemplateLicenseSpecificationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ab632f3d3255beca8bac3dfca32d6df24174524bb4f1981b6650cd80f8dee3a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__981d8479c2284f2476c99b8b55c8c341ce366f6ec876f9279aa3ea428d2f2132)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3c871e1c20ca44b9d8b5cb5c42be16bd31321fdc26bbf8e014c9e923d6a735b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LaunchTemplateLicenseSpecification]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LaunchTemplateLicenseSpecification]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LaunchTemplateLicenseSpecification]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c23d4dc521a1e3a51773269966787d9041a22d75b7baf68555cc4ba036075b00)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LaunchTemplateLicenseSpecificationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.launchTemplate.LaunchTemplateLicenseSpecificationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1ba75c8f52ea0068aa88200bbf3d67dcdd4fad2c3852db40796fb56b0be0d35f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="licenseConfigurationArnInput")
    def license_configuration_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "licenseConfigurationArnInput"))

    @builtins.property
    @jsii.member(jsii_name="licenseConfigurationArn")
    def license_configuration_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "licenseConfigurationArn"))

    @license_configuration_arn.setter
    def license_configuration_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40b5a1fc3c214ee8c238b509c8dcad14160c05be0d881e8c6a80b9fc4ab3d914)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "licenseConfigurationArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LaunchTemplateLicenseSpecification, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LaunchTemplateLicenseSpecification, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LaunchTemplateLicenseSpecification, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b0dbdc97a2ef8d18c6d81d0ac519a9a9b87d4cda09005a66b95cf11ce132c56)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.launchTemplate.LaunchTemplateMaintenanceOptions",
    jsii_struct_bases=[],
    name_mapping={"auto_recovery": "autoRecovery"},
)
class LaunchTemplateMaintenanceOptions:
    def __init__(self, *, auto_recovery: typing.Optional[builtins.str] = None) -> None:
        '''
        :param auto_recovery: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#auto_recovery LaunchTemplate#auto_recovery}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__921285fb4b9c7b2ce7f77dc770acc6b805068ebc2d58d793bd24942dbe9f7e51)
            check_type(argname="argument auto_recovery", value=auto_recovery, expected_type=type_hints["auto_recovery"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if auto_recovery is not None:
            self._values["auto_recovery"] = auto_recovery

    @builtins.property
    def auto_recovery(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#auto_recovery LaunchTemplate#auto_recovery}.'''
        result = self._values.get("auto_recovery")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LaunchTemplateMaintenanceOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LaunchTemplateMaintenanceOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.launchTemplate.LaunchTemplateMaintenanceOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f78a654c46a9f888163d80220ae8e34e4b6f8bc0ef68d6f677602248ff102970)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAutoRecovery")
    def reset_auto_recovery(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoRecovery", []))

    @builtins.property
    @jsii.member(jsii_name="autoRecoveryInput")
    def auto_recovery_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "autoRecoveryInput"))

    @builtins.property
    @jsii.member(jsii_name="autoRecovery")
    def auto_recovery(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "autoRecovery"))

    @auto_recovery.setter
    def auto_recovery(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dfc97ecc6fd75af29456eda36702311f779e6b8bf779ae4193f41ff7f77229d3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoRecovery", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LaunchTemplateMaintenanceOptions]:
        return typing.cast(typing.Optional[LaunchTemplateMaintenanceOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LaunchTemplateMaintenanceOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f7dd539be5019f5ac1e188fb1c63125feaea2b218189e2451ca2b5a5a051d9d8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.launchTemplate.LaunchTemplateMetadataOptions",
    jsii_struct_bases=[],
    name_mapping={
        "http_endpoint": "httpEndpoint",
        "http_protocol_ipv6": "httpProtocolIpv6",
        "http_put_response_hop_limit": "httpPutResponseHopLimit",
        "http_tokens": "httpTokens",
        "instance_metadata_tags": "instanceMetadataTags",
    },
)
class LaunchTemplateMetadataOptions:
    def __init__(
        self,
        *,
        http_endpoint: typing.Optional[builtins.str] = None,
        http_protocol_ipv6: typing.Optional[builtins.str] = None,
        http_put_response_hop_limit: typing.Optional[jsii.Number] = None,
        http_tokens: typing.Optional[builtins.str] = None,
        instance_metadata_tags: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param http_endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#http_endpoint LaunchTemplate#http_endpoint}.
        :param http_protocol_ipv6: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#http_protocol_ipv6 LaunchTemplate#http_protocol_ipv6}.
        :param http_put_response_hop_limit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#http_put_response_hop_limit LaunchTemplate#http_put_response_hop_limit}.
        :param http_tokens: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#http_tokens LaunchTemplate#http_tokens}.
        :param instance_metadata_tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#instance_metadata_tags LaunchTemplate#instance_metadata_tags}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__397113e868199d5b7871183769c39c4ede2d3563373a4b7c1818bf3c79caa41b)
            check_type(argname="argument http_endpoint", value=http_endpoint, expected_type=type_hints["http_endpoint"])
            check_type(argname="argument http_protocol_ipv6", value=http_protocol_ipv6, expected_type=type_hints["http_protocol_ipv6"])
            check_type(argname="argument http_put_response_hop_limit", value=http_put_response_hop_limit, expected_type=type_hints["http_put_response_hop_limit"])
            check_type(argname="argument http_tokens", value=http_tokens, expected_type=type_hints["http_tokens"])
            check_type(argname="argument instance_metadata_tags", value=instance_metadata_tags, expected_type=type_hints["instance_metadata_tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if http_endpoint is not None:
            self._values["http_endpoint"] = http_endpoint
        if http_protocol_ipv6 is not None:
            self._values["http_protocol_ipv6"] = http_protocol_ipv6
        if http_put_response_hop_limit is not None:
            self._values["http_put_response_hop_limit"] = http_put_response_hop_limit
        if http_tokens is not None:
            self._values["http_tokens"] = http_tokens
        if instance_metadata_tags is not None:
            self._values["instance_metadata_tags"] = instance_metadata_tags

    @builtins.property
    def http_endpoint(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#http_endpoint LaunchTemplate#http_endpoint}.'''
        result = self._values.get("http_endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def http_protocol_ipv6(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#http_protocol_ipv6 LaunchTemplate#http_protocol_ipv6}.'''
        result = self._values.get("http_protocol_ipv6")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def http_put_response_hop_limit(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#http_put_response_hop_limit LaunchTemplate#http_put_response_hop_limit}.'''
        result = self._values.get("http_put_response_hop_limit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def http_tokens(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#http_tokens LaunchTemplate#http_tokens}.'''
        result = self._values.get("http_tokens")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance_metadata_tags(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#instance_metadata_tags LaunchTemplate#instance_metadata_tags}.'''
        result = self._values.get("instance_metadata_tags")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LaunchTemplateMetadataOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LaunchTemplateMetadataOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.launchTemplate.LaunchTemplateMetadataOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e2c8e4e1055f5c9bc8f0fea4fbd5c453eeaa9f7b938b3cdb2cb7f618de2ef5b9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetHttpEndpoint")
    def reset_http_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpEndpoint", []))

    @jsii.member(jsii_name="resetHttpProtocolIpv6")
    def reset_http_protocol_ipv6(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpProtocolIpv6", []))

    @jsii.member(jsii_name="resetHttpPutResponseHopLimit")
    def reset_http_put_response_hop_limit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpPutResponseHopLimit", []))

    @jsii.member(jsii_name="resetHttpTokens")
    def reset_http_tokens(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpTokens", []))

    @jsii.member(jsii_name="resetInstanceMetadataTags")
    def reset_instance_metadata_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceMetadataTags", []))

    @builtins.property
    @jsii.member(jsii_name="httpEndpointInput")
    def http_endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "httpEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="httpProtocolIpv6Input")
    def http_protocol_ipv6_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "httpProtocolIpv6Input"))

    @builtins.property
    @jsii.member(jsii_name="httpPutResponseHopLimitInput")
    def http_put_response_hop_limit_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "httpPutResponseHopLimitInput"))

    @builtins.property
    @jsii.member(jsii_name="httpTokensInput")
    def http_tokens_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "httpTokensInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceMetadataTagsInput")
    def instance_metadata_tags_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceMetadataTagsInput"))

    @builtins.property
    @jsii.member(jsii_name="httpEndpoint")
    def http_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "httpEndpoint"))

    @http_endpoint.setter
    def http_endpoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4fa8eaf408dda81fdfd20528d3124881ae441864f60ca7a53a809b980bb21426)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="httpProtocolIpv6")
    def http_protocol_ipv6(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "httpProtocolIpv6"))

    @http_protocol_ipv6.setter
    def http_protocol_ipv6(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14129f70b2f8ab0d81fbedebf11048c89714ff2b56c2c57c3bdc7022de255825)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpProtocolIpv6", value)

    @builtins.property
    @jsii.member(jsii_name="httpPutResponseHopLimit")
    def http_put_response_hop_limit(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "httpPutResponseHopLimit"))

    @http_put_response_hop_limit.setter
    def http_put_response_hop_limit(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7c97c300b6f709acb69879091a38f6b8cd8d669adebde89379e00e5f4c55147)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpPutResponseHopLimit", value)

    @builtins.property
    @jsii.member(jsii_name="httpTokens")
    def http_tokens(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "httpTokens"))

    @http_tokens.setter
    def http_tokens(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4823c498b7ab559ab44d11b6b735feddc7d28f6802463b6628b002f2f6a4ee48)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpTokens", value)

    @builtins.property
    @jsii.member(jsii_name="instanceMetadataTags")
    def instance_metadata_tags(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceMetadataTags"))

    @instance_metadata_tags.setter
    def instance_metadata_tags(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26631dbc0bf0ecaf2c968c9e79ad36a77631736c80e5c103ffa14c8028f85890)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceMetadataTags", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LaunchTemplateMetadataOptions]:
        return typing.cast(typing.Optional[LaunchTemplateMetadataOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LaunchTemplateMetadataOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__192f112b95fd12737a79799b09e9c09f23288c29703cc6f49c007f3dbbc4abda)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.launchTemplate.LaunchTemplateMonitoring",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled"},
)
class LaunchTemplateMonitoring:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#enabled LaunchTemplate#enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02a31ef33866d7ec8e405454827f01452583d562256a35190e1b500b011244bc)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#enabled LaunchTemplate#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LaunchTemplateMonitoring(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LaunchTemplateMonitoringOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.launchTemplate.LaunchTemplateMonitoringOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6abb3c432760751a80fe2ca2ec4dbe559459d0e1c60e4832043ec211093224f2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8593ca801c227b4b51298951f1d4be8d7faa7f852f81bfa0c6d7f9b2f2420e80)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LaunchTemplateMonitoring]:
        return typing.cast(typing.Optional[LaunchTemplateMonitoring], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[LaunchTemplateMonitoring]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b5799d931fd9e585d4430dd9346b2aededa0036f39d3e4dcec65a344d74ba4b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.launchTemplate.LaunchTemplateNetworkInterfaces",
    jsii_struct_bases=[],
    name_mapping={
        "associate_carrier_ip_address": "associateCarrierIpAddress",
        "associate_public_ip_address": "associatePublicIpAddress",
        "delete_on_termination": "deleteOnTermination",
        "description": "description",
        "device_index": "deviceIndex",
        "interface_type": "interfaceType",
        "ipv4_address_count": "ipv4AddressCount",
        "ipv4_addresses": "ipv4Addresses",
        "ipv4_prefix_count": "ipv4PrefixCount",
        "ipv4_prefixes": "ipv4Prefixes",
        "ipv6_address_count": "ipv6AddressCount",
        "ipv6_addresses": "ipv6Addresses",
        "ipv6_prefix_count": "ipv6PrefixCount",
        "ipv6_prefixes": "ipv6Prefixes",
        "network_card_index": "networkCardIndex",
        "network_interface_id": "networkInterfaceId",
        "private_ip_address": "privateIpAddress",
        "security_groups": "securityGroups",
        "subnet_id": "subnetId",
    },
)
class LaunchTemplateNetworkInterfaces:
    def __init__(
        self,
        *,
        associate_carrier_ip_address: typing.Optional[builtins.str] = None,
        associate_public_ip_address: typing.Optional[builtins.str] = None,
        delete_on_termination: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        device_index: typing.Optional[jsii.Number] = None,
        interface_type: typing.Optional[builtins.str] = None,
        ipv4_address_count: typing.Optional[jsii.Number] = None,
        ipv4_addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
        ipv4_prefix_count: typing.Optional[jsii.Number] = None,
        ipv4_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
        ipv6_address_count: typing.Optional[jsii.Number] = None,
        ipv6_addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
        ipv6_prefix_count: typing.Optional[jsii.Number] = None,
        ipv6_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
        network_card_index: typing.Optional[jsii.Number] = None,
        network_interface_id: typing.Optional[builtins.str] = None,
        private_ip_address: typing.Optional[builtins.str] = None,
        security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        subnet_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param associate_carrier_ip_address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#associate_carrier_ip_address LaunchTemplate#associate_carrier_ip_address}.
        :param associate_public_ip_address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#associate_public_ip_address LaunchTemplate#associate_public_ip_address}.
        :param delete_on_termination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#delete_on_termination LaunchTemplate#delete_on_termination}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#description LaunchTemplate#description}.
        :param device_index: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#device_index LaunchTemplate#device_index}.
        :param interface_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#interface_type LaunchTemplate#interface_type}.
        :param ipv4_address_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#ipv4_address_count LaunchTemplate#ipv4_address_count}.
        :param ipv4_addresses: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#ipv4_addresses LaunchTemplate#ipv4_addresses}.
        :param ipv4_prefix_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#ipv4_prefix_count LaunchTemplate#ipv4_prefix_count}.
        :param ipv4_prefixes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#ipv4_prefixes LaunchTemplate#ipv4_prefixes}.
        :param ipv6_address_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#ipv6_address_count LaunchTemplate#ipv6_address_count}.
        :param ipv6_addresses: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#ipv6_addresses LaunchTemplate#ipv6_addresses}.
        :param ipv6_prefix_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#ipv6_prefix_count LaunchTemplate#ipv6_prefix_count}.
        :param ipv6_prefixes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#ipv6_prefixes LaunchTemplate#ipv6_prefixes}.
        :param network_card_index: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#network_card_index LaunchTemplate#network_card_index}.
        :param network_interface_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#network_interface_id LaunchTemplate#network_interface_id}.
        :param private_ip_address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#private_ip_address LaunchTemplate#private_ip_address}.
        :param security_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#security_groups LaunchTemplate#security_groups}.
        :param subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#subnet_id LaunchTemplate#subnet_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__704ec35ed869aee50d4799b705b7a87c66b91e39e483d7020a77cc7f524a82fb)
            check_type(argname="argument associate_carrier_ip_address", value=associate_carrier_ip_address, expected_type=type_hints["associate_carrier_ip_address"])
            check_type(argname="argument associate_public_ip_address", value=associate_public_ip_address, expected_type=type_hints["associate_public_ip_address"])
            check_type(argname="argument delete_on_termination", value=delete_on_termination, expected_type=type_hints["delete_on_termination"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument device_index", value=device_index, expected_type=type_hints["device_index"])
            check_type(argname="argument interface_type", value=interface_type, expected_type=type_hints["interface_type"])
            check_type(argname="argument ipv4_address_count", value=ipv4_address_count, expected_type=type_hints["ipv4_address_count"])
            check_type(argname="argument ipv4_addresses", value=ipv4_addresses, expected_type=type_hints["ipv4_addresses"])
            check_type(argname="argument ipv4_prefix_count", value=ipv4_prefix_count, expected_type=type_hints["ipv4_prefix_count"])
            check_type(argname="argument ipv4_prefixes", value=ipv4_prefixes, expected_type=type_hints["ipv4_prefixes"])
            check_type(argname="argument ipv6_address_count", value=ipv6_address_count, expected_type=type_hints["ipv6_address_count"])
            check_type(argname="argument ipv6_addresses", value=ipv6_addresses, expected_type=type_hints["ipv6_addresses"])
            check_type(argname="argument ipv6_prefix_count", value=ipv6_prefix_count, expected_type=type_hints["ipv6_prefix_count"])
            check_type(argname="argument ipv6_prefixes", value=ipv6_prefixes, expected_type=type_hints["ipv6_prefixes"])
            check_type(argname="argument network_card_index", value=network_card_index, expected_type=type_hints["network_card_index"])
            check_type(argname="argument network_interface_id", value=network_interface_id, expected_type=type_hints["network_interface_id"])
            check_type(argname="argument private_ip_address", value=private_ip_address, expected_type=type_hints["private_ip_address"])
            check_type(argname="argument security_groups", value=security_groups, expected_type=type_hints["security_groups"])
            check_type(argname="argument subnet_id", value=subnet_id, expected_type=type_hints["subnet_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if associate_carrier_ip_address is not None:
            self._values["associate_carrier_ip_address"] = associate_carrier_ip_address
        if associate_public_ip_address is not None:
            self._values["associate_public_ip_address"] = associate_public_ip_address
        if delete_on_termination is not None:
            self._values["delete_on_termination"] = delete_on_termination
        if description is not None:
            self._values["description"] = description
        if device_index is not None:
            self._values["device_index"] = device_index
        if interface_type is not None:
            self._values["interface_type"] = interface_type
        if ipv4_address_count is not None:
            self._values["ipv4_address_count"] = ipv4_address_count
        if ipv4_addresses is not None:
            self._values["ipv4_addresses"] = ipv4_addresses
        if ipv4_prefix_count is not None:
            self._values["ipv4_prefix_count"] = ipv4_prefix_count
        if ipv4_prefixes is not None:
            self._values["ipv4_prefixes"] = ipv4_prefixes
        if ipv6_address_count is not None:
            self._values["ipv6_address_count"] = ipv6_address_count
        if ipv6_addresses is not None:
            self._values["ipv6_addresses"] = ipv6_addresses
        if ipv6_prefix_count is not None:
            self._values["ipv6_prefix_count"] = ipv6_prefix_count
        if ipv6_prefixes is not None:
            self._values["ipv6_prefixes"] = ipv6_prefixes
        if network_card_index is not None:
            self._values["network_card_index"] = network_card_index
        if network_interface_id is not None:
            self._values["network_interface_id"] = network_interface_id
        if private_ip_address is not None:
            self._values["private_ip_address"] = private_ip_address
        if security_groups is not None:
            self._values["security_groups"] = security_groups
        if subnet_id is not None:
            self._values["subnet_id"] = subnet_id

    @builtins.property
    def associate_carrier_ip_address(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#associate_carrier_ip_address LaunchTemplate#associate_carrier_ip_address}.'''
        result = self._values.get("associate_carrier_ip_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def associate_public_ip_address(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#associate_public_ip_address LaunchTemplate#associate_public_ip_address}.'''
        result = self._values.get("associate_public_ip_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete_on_termination(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#delete_on_termination LaunchTemplate#delete_on_termination}.'''
        result = self._values.get("delete_on_termination")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#description LaunchTemplate#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def device_index(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#device_index LaunchTemplate#device_index}.'''
        result = self._values.get("device_index")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def interface_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#interface_type LaunchTemplate#interface_type}.'''
        result = self._values.get("interface_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ipv4_address_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#ipv4_address_count LaunchTemplate#ipv4_address_count}.'''
        result = self._values.get("ipv4_address_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ipv4_addresses(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#ipv4_addresses LaunchTemplate#ipv4_addresses}.'''
        result = self._values.get("ipv4_addresses")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def ipv4_prefix_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#ipv4_prefix_count LaunchTemplate#ipv4_prefix_count}.'''
        result = self._values.get("ipv4_prefix_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ipv4_prefixes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#ipv4_prefixes LaunchTemplate#ipv4_prefixes}.'''
        result = self._values.get("ipv4_prefixes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def ipv6_address_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#ipv6_address_count LaunchTemplate#ipv6_address_count}.'''
        result = self._values.get("ipv6_address_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ipv6_addresses(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#ipv6_addresses LaunchTemplate#ipv6_addresses}.'''
        result = self._values.get("ipv6_addresses")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def ipv6_prefix_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#ipv6_prefix_count LaunchTemplate#ipv6_prefix_count}.'''
        result = self._values.get("ipv6_prefix_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ipv6_prefixes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#ipv6_prefixes LaunchTemplate#ipv6_prefixes}.'''
        result = self._values.get("ipv6_prefixes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def network_card_index(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#network_card_index LaunchTemplate#network_card_index}.'''
        result = self._values.get("network_card_index")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def network_interface_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#network_interface_id LaunchTemplate#network_interface_id}.'''
        result = self._values.get("network_interface_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def private_ip_address(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#private_ip_address LaunchTemplate#private_ip_address}.'''
        result = self._values.get("private_ip_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def security_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#security_groups LaunchTemplate#security_groups}.'''
        result = self._values.get("security_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def subnet_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#subnet_id LaunchTemplate#subnet_id}.'''
        result = self._values.get("subnet_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LaunchTemplateNetworkInterfaces(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LaunchTemplateNetworkInterfacesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.launchTemplate.LaunchTemplateNetworkInterfacesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__379ace02d87811867d800d325e258c7923b36311ae595e9314fb0f24ef614be3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LaunchTemplateNetworkInterfacesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9cb0f3268618c11b8e92ba033c7ff74e0a933eae36aa3fa59fca3a2f23cbb4d9)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LaunchTemplateNetworkInterfacesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc4c70ce7d0db92ffd55e4cdac848eeed169b8335af98e69aceb1abdc4e5c55a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__19dc70c462daed4cab84a56d7f23f7a89cf198fe92c23222b0661658275fc1c4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c0340c11ab98cedd9b4490609a0234afa428bd7000a56ef417ef49f92c93e01f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LaunchTemplateNetworkInterfaces]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LaunchTemplateNetworkInterfaces]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LaunchTemplateNetworkInterfaces]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92054e8d40338a2ea6e2d126ba653c3c74e96f9ca783581fc9d10207e98f6961)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LaunchTemplateNetworkInterfacesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.launchTemplate.LaunchTemplateNetworkInterfacesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__98884d30b6fc05c003803bf58cf7de48a5fbf316950608dd24d39694d7706887)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAssociateCarrierIpAddress")
    def reset_associate_carrier_ip_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAssociateCarrierIpAddress", []))

    @jsii.member(jsii_name="resetAssociatePublicIpAddress")
    def reset_associate_public_ip_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAssociatePublicIpAddress", []))

    @jsii.member(jsii_name="resetDeleteOnTermination")
    def reset_delete_on_termination(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeleteOnTermination", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetDeviceIndex")
    def reset_device_index(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeviceIndex", []))

    @jsii.member(jsii_name="resetInterfaceType")
    def reset_interface_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInterfaceType", []))

    @jsii.member(jsii_name="resetIpv4AddressCount")
    def reset_ipv4_address_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpv4AddressCount", []))

    @jsii.member(jsii_name="resetIpv4Addresses")
    def reset_ipv4_addresses(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpv4Addresses", []))

    @jsii.member(jsii_name="resetIpv4PrefixCount")
    def reset_ipv4_prefix_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpv4PrefixCount", []))

    @jsii.member(jsii_name="resetIpv4Prefixes")
    def reset_ipv4_prefixes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpv4Prefixes", []))

    @jsii.member(jsii_name="resetIpv6AddressCount")
    def reset_ipv6_address_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpv6AddressCount", []))

    @jsii.member(jsii_name="resetIpv6Addresses")
    def reset_ipv6_addresses(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpv6Addresses", []))

    @jsii.member(jsii_name="resetIpv6PrefixCount")
    def reset_ipv6_prefix_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpv6PrefixCount", []))

    @jsii.member(jsii_name="resetIpv6Prefixes")
    def reset_ipv6_prefixes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpv6Prefixes", []))

    @jsii.member(jsii_name="resetNetworkCardIndex")
    def reset_network_card_index(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworkCardIndex", []))

    @jsii.member(jsii_name="resetNetworkInterfaceId")
    def reset_network_interface_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworkInterfaceId", []))

    @jsii.member(jsii_name="resetPrivateIpAddress")
    def reset_private_ip_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateIpAddress", []))

    @jsii.member(jsii_name="resetSecurityGroups")
    def reset_security_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecurityGroups", []))

    @jsii.member(jsii_name="resetSubnetId")
    def reset_subnet_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubnetId", []))

    @builtins.property
    @jsii.member(jsii_name="associateCarrierIpAddressInput")
    def associate_carrier_ip_address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "associateCarrierIpAddressInput"))

    @builtins.property
    @jsii.member(jsii_name="associatePublicIpAddressInput")
    def associate_public_ip_address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "associatePublicIpAddressInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteOnTerminationInput")
    def delete_on_termination_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteOnTerminationInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="deviceIndexInput")
    def device_index_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "deviceIndexInput"))

    @builtins.property
    @jsii.member(jsii_name="interfaceTypeInput")
    def interface_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "interfaceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="ipv4AddressCountInput")
    def ipv4_address_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ipv4AddressCountInput"))

    @builtins.property
    @jsii.member(jsii_name="ipv4AddressesInput")
    def ipv4_addresses_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "ipv4AddressesInput"))

    @builtins.property
    @jsii.member(jsii_name="ipv4PrefixCountInput")
    def ipv4_prefix_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ipv4PrefixCountInput"))

    @builtins.property
    @jsii.member(jsii_name="ipv4PrefixesInput")
    def ipv4_prefixes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "ipv4PrefixesInput"))

    @builtins.property
    @jsii.member(jsii_name="ipv6AddressCountInput")
    def ipv6_address_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ipv6AddressCountInput"))

    @builtins.property
    @jsii.member(jsii_name="ipv6AddressesInput")
    def ipv6_addresses_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "ipv6AddressesInput"))

    @builtins.property
    @jsii.member(jsii_name="ipv6PrefixCountInput")
    def ipv6_prefix_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ipv6PrefixCountInput"))

    @builtins.property
    @jsii.member(jsii_name="ipv6PrefixesInput")
    def ipv6_prefixes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "ipv6PrefixesInput"))

    @builtins.property
    @jsii.member(jsii_name="networkCardIndexInput")
    def network_card_index_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "networkCardIndexInput"))

    @builtins.property
    @jsii.member(jsii_name="networkInterfaceIdInput")
    def network_interface_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkInterfaceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="privateIpAddressInput")
    def private_ip_address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateIpAddressInput"))

    @builtins.property
    @jsii.member(jsii_name="securityGroupsInput")
    def security_groups_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetIdInput")
    def subnet_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subnetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="associateCarrierIpAddress")
    def associate_carrier_ip_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "associateCarrierIpAddress"))

    @associate_carrier_ip_address.setter
    def associate_carrier_ip_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57131392d8e93ddb7465b5fab700ebab6b92f9f6cd9fccbdca993b094f4ef78d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "associateCarrierIpAddress", value)

    @builtins.property
    @jsii.member(jsii_name="associatePublicIpAddress")
    def associate_public_ip_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "associatePublicIpAddress"))

    @associate_public_ip_address.setter
    def associate_public_ip_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da47563914824900a5d5bc8d524ae6e40f4a2bb1236e656a6500b53f332135f9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "associatePublicIpAddress", value)

    @builtins.property
    @jsii.member(jsii_name="deleteOnTermination")
    def delete_on_termination(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deleteOnTermination"))

    @delete_on_termination.setter
    def delete_on_termination(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e4a8e9d2548730beddc56d1d6f1ff40f82ba74d23b22a3ce411dd24653bc13e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deleteOnTermination", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be7e53ad06a26ef72cb5eb66559e4ed39e25ff521b4f2caec39d10652420fd7a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="deviceIndex")
    def device_index(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "deviceIndex"))

    @device_index.setter
    def device_index(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49bc10c515f7b80dacd9514812824b32e2da1434c00bd6e0df12ad41d39669bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deviceIndex", value)

    @builtins.property
    @jsii.member(jsii_name="interfaceType")
    def interface_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "interfaceType"))

    @interface_type.setter
    def interface_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17c840581e642395912a4a6cd9e7061c9d6bfea52fa9c5e51f5fbe01c605d7e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "interfaceType", value)

    @builtins.property
    @jsii.member(jsii_name="ipv4AddressCount")
    def ipv4_address_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ipv4AddressCount"))

    @ipv4_address_count.setter
    def ipv4_address_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__588d6ff98a957a4ee920b5b561c3ecde7d264938918aa2b8a4b58c525b3fc746)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipv4AddressCount", value)

    @builtins.property
    @jsii.member(jsii_name="ipv4Addresses")
    def ipv4_addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "ipv4Addresses"))

    @ipv4_addresses.setter
    def ipv4_addresses(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2af803e6e1bdcf6e23e6b526719605503eb826e51ffe38265697f5bd59dd8b94)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipv4Addresses", value)

    @builtins.property
    @jsii.member(jsii_name="ipv4PrefixCount")
    def ipv4_prefix_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ipv4PrefixCount"))

    @ipv4_prefix_count.setter
    def ipv4_prefix_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f32c510550dbec8932cd17efe900cbdcb3114c7350273799c6019afe4eb6a418)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipv4PrefixCount", value)

    @builtins.property
    @jsii.member(jsii_name="ipv4Prefixes")
    def ipv4_prefixes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "ipv4Prefixes"))

    @ipv4_prefixes.setter
    def ipv4_prefixes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__deb928a9f576987a5b2d72c902b90f9ea934317db441f72f2f9f91d24041c760)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipv4Prefixes", value)

    @builtins.property
    @jsii.member(jsii_name="ipv6AddressCount")
    def ipv6_address_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ipv6AddressCount"))

    @ipv6_address_count.setter
    def ipv6_address_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d4c8578d14efc78783932dfe232e0a66c0f48efc0bebb3e17bf9d92b1567169)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipv6AddressCount", value)

    @builtins.property
    @jsii.member(jsii_name="ipv6Addresses")
    def ipv6_addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "ipv6Addresses"))

    @ipv6_addresses.setter
    def ipv6_addresses(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef505199fc6235cbff5f45806c1eb75e1eacb393bdc2450c3c4d413af33d04e2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipv6Addresses", value)

    @builtins.property
    @jsii.member(jsii_name="ipv6PrefixCount")
    def ipv6_prefix_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ipv6PrefixCount"))

    @ipv6_prefix_count.setter
    def ipv6_prefix_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4d3cc0e914ceef9e21947809e390ae21237b80d68d14edfdc0be0a3cc1a0334)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipv6PrefixCount", value)

    @builtins.property
    @jsii.member(jsii_name="ipv6Prefixes")
    def ipv6_prefixes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "ipv6Prefixes"))

    @ipv6_prefixes.setter
    def ipv6_prefixes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25467bbf4b09a1240dc90e82daf8ec5310e930af5475bd24fb7f86891c5a4007)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipv6Prefixes", value)

    @builtins.property
    @jsii.member(jsii_name="networkCardIndex")
    def network_card_index(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "networkCardIndex"))

    @network_card_index.setter
    def network_card_index(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f8b1519a726c3ce3260a433b3a09b54fbf5b114391b13984813c9cc91ca3eb7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkCardIndex", value)

    @builtins.property
    @jsii.member(jsii_name="networkInterfaceId")
    def network_interface_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "networkInterfaceId"))

    @network_interface_id.setter
    def network_interface_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67eb5065110e1b91c94091fe6f987242d191090dea68f0ea34ba1863d1db20b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkInterfaceId", value)

    @builtins.property
    @jsii.member(jsii_name="privateIpAddress")
    def private_ip_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateIpAddress"))

    @private_ip_address.setter
    def private_ip_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4158faaf8faaa6a4e8d356f324245735b33b8be19c60e6023c058b7d55be68ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateIpAddress", value)

    @builtins.property
    @jsii.member(jsii_name="securityGroups")
    def security_groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "securityGroups"))

    @security_groups.setter
    def security_groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5312a3c2069ad1dc1d16722e2299c3991c44727ab28637145a34ebe4e2146f7e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroups", value)

    @builtins.property
    @jsii.member(jsii_name="subnetId")
    def subnet_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subnetId"))

    @subnet_id.setter
    def subnet_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62ea3dc0fa7ae218daeb090fc064d02f2cded1a275143125e1b72ae897f0ad1b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LaunchTemplateNetworkInterfaces, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LaunchTemplateNetworkInterfaces, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LaunchTemplateNetworkInterfaces, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f60580ff5f0b08420bdda3d5af1ad57368b840a9185a67cdf5cb607efd518ed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.launchTemplate.LaunchTemplatePlacement",
    jsii_struct_bases=[],
    name_mapping={
        "affinity": "affinity",
        "availability_zone": "availabilityZone",
        "group_name": "groupName",
        "host_id": "hostId",
        "host_resource_group_arn": "hostResourceGroupArn",
        "partition_number": "partitionNumber",
        "spread_domain": "spreadDomain",
        "tenancy": "tenancy",
    },
)
class LaunchTemplatePlacement:
    def __init__(
        self,
        *,
        affinity: typing.Optional[builtins.str] = None,
        availability_zone: typing.Optional[builtins.str] = None,
        group_name: typing.Optional[builtins.str] = None,
        host_id: typing.Optional[builtins.str] = None,
        host_resource_group_arn: typing.Optional[builtins.str] = None,
        partition_number: typing.Optional[jsii.Number] = None,
        spread_domain: typing.Optional[builtins.str] = None,
        tenancy: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param affinity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#affinity LaunchTemplate#affinity}.
        :param availability_zone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#availability_zone LaunchTemplate#availability_zone}.
        :param group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#group_name LaunchTemplate#group_name}.
        :param host_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#host_id LaunchTemplate#host_id}.
        :param host_resource_group_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#host_resource_group_arn LaunchTemplate#host_resource_group_arn}.
        :param partition_number: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#partition_number LaunchTemplate#partition_number}.
        :param spread_domain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#spread_domain LaunchTemplate#spread_domain}.
        :param tenancy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#tenancy LaunchTemplate#tenancy}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__391b1674b1668c2d6c6906c7e10615823ade0746b7f5e79432d97f410a03bed2)
            check_type(argname="argument affinity", value=affinity, expected_type=type_hints["affinity"])
            check_type(argname="argument availability_zone", value=availability_zone, expected_type=type_hints["availability_zone"])
            check_type(argname="argument group_name", value=group_name, expected_type=type_hints["group_name"])
            check_type(argname="argument host_id", value=host_id, expected_type=type_hints["host_id"])
            check_type(argname="argument host_resource_group_arn", value=host_resource_group_arn, expected_type=type_hints["host_resource_group_arn"])
            check_type(argname="argument partition_number", value=partition_number, expected_type=type_hints["partition_number"])
            check_type(argname="argument spread_domain", value=spread_domain, expected_type=type_hints["spread_domain"])
            check_type(argname="argument tenancy", value=tenancy, expected_type=type_hints["tenancy"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if affinity is not None:
            self._values["affinity"] = affinity
        if availability_zone is not None:
            self._values["availability_zone"] = availability_zone
        if group_name is not None:
            self._values["group_name"] = group_name
        if host_id is not None:
            self._values["host_id"] = host_id
        if host_resource_group_arn is not None:
            self._values["host_resource_group_arn"] = host_resource_group_arn
        if partition_number is not None:
            self._values["partition_number"] = partition_number
        if spread_domain is not None:
            self._values["spread_domain"] = spread_domain
        if tenancy is not None:
            self._values["tenancy"] = tenancy

    @builtins.property
    def affinity(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#affinity LaunchTemplate#affinity}.'''
        result = self._values.get("affinity")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def availability_zone(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#availability_zone LaunchTemplate#availability_zone}.'''
        result = self._values.get("availability_zone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def group_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#group_name LaunchTemplate#group_name}.'''
        result = self._values.get("group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def host_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#host_id LaunchTemplate#host_id}.'''
        result = self._values.get("host_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def host_resource_group_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#host_resource_group_arn LaunchTemplate#host_resource_group_arn}.'''
        result = self._values.get("host_resource_group_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def partition_number(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#partition_number LaunchTemplate#partition_number}.'''
        result = self._values.get("partition_number")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def spread_domain(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#spread_domain LaunchTemplate#spread_domain}.'''
        result = self._values.get("spread_domain")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tenancy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#tenancy LaunchTemplate#tenancy}.'''
        result = self._values.get("tenancy")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LaunchTemplatePlacement(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LaunchTemplatePlacementOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.launchTemplate.LaunchTemplatePlacementOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cfa58230c3cbc4f8e1a9c78e81858160b240589e0c08feaa7d974d967c047a5e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAffinity")
    def reset_affinity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAffinity", []))

    @jsii.member(jsii_name="resetAvailabilityZone")
    def reset_availability_zone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAvailabilityZone", []))

    @jsii.member(jsii_name="resetGroupName")
    def reset_group_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroupName", []))

    @jsii.member(jsii_name="resetHostId")
    def reset_host_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostId", []))

    @jsii.member(jsii_name="resetHostResourceGroupArn")
    def reset_host_resource_group_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostResourceGroupArn", []))

    @jsii.member(jsii_name="resetPartitionNumber")
    def reset_partition_number(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPartitionNumber", []))

    @jsii.member(jsii_name="resetSpreadDomain")
    def reset_spread_domain(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSpreadDomain", []))

    @jsii.member(jsii_name="resetTenancy")
    def reset_tenancy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTenancy", []))

    @builtins.property
    @jsii.member(jsii_name="affinityInput")
    def affinity_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "affinityInput"))

    @builtins.property
    @jsii.member(jsii_name="availabilityZoneInput")
    def availability_zone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "availabilityZoneInput"))

    @builtins.property
    @jsii.member(jsii_name="groupNameInput")
    def group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "groupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="hostIdInput")
    def host_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostIdInput"))

    @builtins.property
    @jsii.member(jsii_name="hostResourceGroupArnInput")
    def host_resource_group_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostResourceGroupArnInput"))

    @builtins.property
    @jsii.member(jsii_name="partitionNumberInput")
    def partition_number_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "partitionNumberInput"))

    @builtins.property
    @jsii.member(jsii_name="spreadDomainInput")
    def spread_domain_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "spreadDomainInput"))

    @builtins.property
    @jsii.member(jsii_name="tenancyInput")
    def tenancy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tenancyInput"))

    @builtins.property
    @jsii.member(jsii_name="affinity")
    def affinity(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "affinity"))

    @affinity.setter
    def affinity(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75cb08815ee669126b0625f8efcf2bb56bd91bff2339a4d61ef22ea85790b41e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "affinity", value)

    @builtins.property
    @jsii.member(jsii_name="availabilityZone")
    def availability_zone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "availabilityZone"))

    @availability_zone.setter
    def availability_zone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a51963d71db7147cf4ceb3f21ab3bec709b50df69b294034e517f6d2db7781ac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availabilityZone", value)

    @builtins.property
    @jsii.member(jsii_name="groupName")
    def group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "groupName"))

    @group_name.setter
    def group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e4b9864d60ae07246f1f0f581faba84285d0a007323f610852a8621fae05a25)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupName", value)

    @builtins.property
    @jsii.member(jsii_name="hostId")
    def host_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostId"))

    @host_id.setter
    def host_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ff555c5e9fadea15c2d1dbeb738f55d1c2737e5e8e4ef41661d0ee7c4ffc4cd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostId", value)

    @builtins.property
    @jsii.member(jsii_name="hostResourceGroupArn")
    def host_resource_group_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostResourceGroupArn"))

    @host_resource_group_arn.setter
    def host_resource_group_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32b16982d29af566584ee6e604d0cbcf5eec6518a8fda075296072e1409dc0f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostResourceGroupArn", value)

    @builtins.property
    @jsii.member(jsii_name="partitionNumber")
    def partition_number(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "partitionNumber"))

    @partition_number.setter
    def partition_number(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__edd7d569c055b1e4d1b5aa1469dd084042fd7404757ac2d71000a8c098490e02)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "partitionNumber", value)

    @builtins.property
    @jsii.member(jsii_name="spreadDomain")
    def spread_domain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "spreadDomain"))

    @spread_domain.setter
    def spread_domain(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44f8db1e579c79b54cdff276bcd2e9694c9c773b19ecd009f819a662101fcee4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "spreadDomain", value)

    @builtins.property
    @jsii.member(jsii_name="tenancy")
    def tenancy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tenancy"))

    @tenancy.setter
    def tenancy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2af01b5048bd07e6f70767cf2bd064a9fe930b128f33994aa15293f263a329b0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tenancy", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LaunchTemplatePlacement]:
        return typing.cast(typing.Optional[LaunchTemplatePlacement], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[LaunchTemplatePlacement]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__30a814ecc9cbea4c80390e8a377ec826483ab7dba4d97cf5ed41eafe068cce63)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.launchTemplate.LaunchTemplatePrivateDnsNameOptions",
    jsii_struct_bases=[],
    name_mapping={
        "enable_resource_name_dns_aaaa_record": "enableResourceNameDnsAaaaRecord",
        "enable_resource_name_dns_a_record": "enableResourceNameDnsARecord",
        "hostname_type": "hostnameType",
    },
)
class LaunchTemplatePrivateDnsNameOptions:
    def __init__(
        self,
        *,
        enable_resource_name_dns_aaaa_record: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_resource_name_dns_a_record: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        hostname_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enable_resource_name_dns_aaaa_record: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#enable_resource_name_dns_aaaa_record LaunchTemplate#enable_resource_name_dns_aaaa_record}.
        :param enable_resource_name_dns_a_record: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#enable_resource_name_dns_a_record LaunchTemplate#enable_resource_name_dns_a_record}.
        :param hostname_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#hostname_type LaunchTemplate#hostname_type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef1eaffef792e66dd497e5f9ba88af78485f240e993ab91ee046d280d8710a0e)
            check_type(argname="argument enable_resource_name_dns_aaaa_record", value=enable_resource_name_dns_aaaa_record, expected_type=type_hints["enable_resource_name_dns_aaaa_record"])
            check_type(argname="argument enable_resource_name_dns_a_record", value=enable_resource_name_dns_a_record, expected_type=type_hints["enable_resource_name_dns_a_record"])
            check_type(argname="argument hostname_type", value=hostname_type, expected_type=type_hints["hostname_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if enable_resource_name_dns_aaaa_record is not None:
            self._values["enable_resource_name_dns_aaaa_record"] = enable_resource_name_dns_aaaa_record
        if enable_resource_name_dns_a_record is not None:
            self._values["enable_resource_name_dns_a_record"] = enable_resource_name_dns_a_record
        if hostname_type is not None:
            self._values["hostname_type"] = hostname_type

    @builtins.property
    def enable_resource_name_dns_aaaa_record(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#enable_resource_name_dns_aaaa_record LaunchTemplate#enable_resource_name_dns_aaaa_record}.'''
        result = self._values.get("enable_resource_name_dns_aaaa_record")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def enable_resource_name_dns_a_record(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#enable_resource_name_dns_a_record LaunchTemplate#enable_resource_name_dns_a_record}.'''
        result = self._values.get("enable_resource_name_dns_a_record")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def hostname_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#hostname_type LaunchTemplate#hostname_type}.'''
        result = self._values.get("hostname_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LaunchTemplatePrivateDnsNameOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LaunchTemplatePrivateDnsNameOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.launchTemplate.LaunchTemplatePrivateDnsNameOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1fa2f72cba68572ae26ac52e617076478761eda439c8a80374f810e37b3ba0fa)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEnableResourceNameDnsAaaaRecord")
    def reset_enable_resource_name_dns_aaaa_record(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableResourceNameDnsAaaaRecord", []))

    @jsii.member(jsii_name="resetEnableResourceNameDnsARecord")
    def reset_enable_resource_name_dns_a_record(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableResourceNameDnsARecord", []))

    @jsii.member(jsii_name="resetHostnameType")
    def reset_hostname_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostnameType", []))

    @builtins.property
    @jsii.member(jsii_name="enableResourceNameDnsAaaaRecordInput")
    def enable_resource_name_dns_aaaa_record_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableResourceNameDnsAaaaRecordInput"))

    @builtins.property
    @jsii.member(jsii_name="enableResourceNameDnsARecordInput")
    def enable_resource_name_dns_a_record_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableResourceNameDnsARecordInput"))

    @builtins.property
    @jsii.member(jsii_name="hostnameTypeInput")
    def hostname_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostnameTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="enableResourceNameDnsAaaaRecord")
    def enable_resource_name_dns_aaaa_record(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enableResourceNameDnsAaaaRecord"))

    @enable_resource_name_dns_aaaa_record.setter
    def enable_resource_name_dns_aaaa_record(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__381cab04d5a01b52e27f201e77e8d828fd216ac0026505de1ce80e6548bd872b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableResourceNameDnsAaaaRecord", value)

    @builtins.property
    @jsii.member(jsii_name="enableResourceNameDnsARecord")
    def enable_resource_name_dns_a_record(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enableResourceNameDnsARecord"))

    @enable_resource_name_dns_a_record.setter
    def enable_resource_name_dns_a_record(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd503fd6c1702739feaf54794df4382acf4defae8f82b8bbacde0a56ec868230)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableResourceNameDnsARecord", value)

    @builtins.property
    @jsii.member(jsii_name="hostnameType")
    def hostname_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostnameType"))

    @hostname_type.setter
    def hostname_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a56b8c36c6d8ad23a44d811242f35e320c8082dd354e02f6117828ae611e0fc4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostnameType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LaunchTemplatePrivateDnsNameOptions]:
        return typing.cast(typing.Optional[LaunchTemplatePrivateDnsNameOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LaunchTemplatePrivateDnsNameOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0db3ec24a84d1db7e9e088f028172a79ec96ed95323f7337d1c2e07cf1af1e8f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.launchTemplate.LaunchTemplateTagSpecifications",
    jsii_struct_bases=[],
    name_mapping={"resource_type": "resourceType", "tags": "tags"},
)
class LaunchTemplateTagSpecifications:
    def __init__(
        self,
        *,
        resource_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param resource_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#resource_type LaunchTemplate#resource_type}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#tags LaunchTemplate#tags}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06901b3f5646f7eeadc2e2447bef060530ccf2a771c5abc573a057e0b719088a)
            check_type(argname="argument resource_type", value=resource_type, expected_type=type_hints["resource_type"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if resource_type is not None:
            self._values["resource_type"] = resource_type
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def resource_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#resource_type LaunchTemplate#resource_type}.'''
        result = self._values.get("resource_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/launch_template#tags LaunchTemplate#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LaunchTemplateTagSpecifications(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LaunchTemplateTagSpecificationsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.launchTemplate.LaunchTemplateTagSpecificationsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__46478445d7cc2d30588f1cb6e105878f9467883ab0b33b4078ec79598ce5f290)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LaunchTemplateTagSpecificationsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__302e76514e050d9ede77d775864a5ebcb26ddf28e30967b3d19a7d12dbd016d2)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LaunchTemplateTagSpecificationsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f313371bc6ff14acb541c965ee5fe602ca1c43a2abe578a8dded2319e9ec74a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a3be1f31cea2d381e9a4ae83b7f74796ea8f346a9f74774ed0f0cea5f653f8c8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__88adbdc03198f2134feafdb05b6abea7c2d94b3647e1d0239ee85ac7d889d989)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LaunchTemplateTagSpecifications]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LaunchTemplateTagSpecifications]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LaunchTemplateTagSpecifications]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f34810e575438cf5e43632496ef3a527c6b473ac7f23bd1cc56654824c23d85)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LaunchTemplateTagSpecificationsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.launchTemplate.LaunchTemplateTagSpecificationsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__768db6e75c6b2b7bf5b929025c16a5805aab5fd325b05d6b68e6e4b8c74ac771)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetResourceType")
    def reset_resource_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourceType", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @builtins.property
    @jsii.member(jsii_name="resourceTypeInput")
    def resource_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceType")
    def resource_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceType"))

    @resource_type.setter
    def resource_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9994567e425d0d01d4a15fc92743d5a8de53bbe2a0193bfc091e943ca574a82d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceType", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c758e7fd4a31c5aa17d9fd4d37f4f30c79512170cc338a51f96b153ba2c6fa31)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LaunchTemplateTagSpecifications, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LaunchTemplateTagSpecifications, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LaunchTemplateTagSpecifications, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91d5fa2333b58ed1e46e6905e5b92c4b69f45cb112caefc1d057f7b1ee3c1a2c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "LaunchTemplate",
    "LaunchTemplateBlockDeviceMappings",
    "LaunchTemplateBlockDeviceMappingsEbs",
    "LaunchTemplateBlockDeviceMappingsEbsOutputReference",
    "LaunchTemplateBlockDeviceMappingsList",
    "LaunchTemplateBlockDeviceMappingsOutputReference",
    "LaunchTemplateCapacityReservationSpecification",
    "LaunchTemplateCapacityReservationSpecificationCapacityReservationTarget",
    "LaunchTemplateCapacityReservationSpecificationCapacityReservationTargetOutputReference",
    "LaunchTemplateCapacityReservationSpecificationOutputReference",
    "LaunchTemplateConfig",
    "LaunchTemplateCpuOptions",
    "LaunchTemplateCpuOptionsOutputReference",
    "LaunchTemplateCreditSpecification",
    "LaunchTemplateCreditSpecificationOutputReference",
    "LaunchTemplateElasticGpuSpecifications",
    "LaunchTemplateElasticGpuSpecificationsList",
    "LaunchTemplateElasticGpuSpecificationsOutputReference",
    "LaunchTemplateElasticInferenceAccelerator",
    "LaunchTemplateElasticInferenceAcceleratorOutputReference",
    "LaunchTemplateEnclaveOptions",
    "LaunchTemplateEnclaveOptionsOutputReference",
    "LaunchTemplateHibernationOptions",
    "LaunchTemplateHibernationOptionsOutputReference",
    "LaunchTemplateIamInstanceProfile",
    "LaunchTemplateIamInstanceProfileOutputReference",
    "LaunchTemplateInstanceMarketOptions",
    "LaunchTemplateInstanceMarketOptionsOutputReference",
    "LaunchTemplateInstanceMarketOptionsSpotOptions",
    "LaunchTemplateInstanceMarketOptionsSpotOptionsOutputReference",
    "LaunchTemplateInstanceRequirements",
    "LaunchTemplateInstanceRequirementsAcceleratorCount",
    "LaunchTemplateInstanceRequirementsAcceleratorCountOutputReference",
    "LaunchTemplateInstanceRequirementsAcceleratorTotalMemoryMib",
    "LaunchTemplateInstanceRequirementsAcceleratorTotalMemoryMibOutputReference",
    "LaunchTemplateInstanceRequirementsBaselineEbsBandwidthMbps",
    "LaunchTemplateInstanceRequirementsBaselineEbsBandwidthMbpsOutputReference",
    "LaunchTemplateInstanceRequirementsMemoryGibPerVcpu",
    "LaunchTemplateInstanceRequirementsMemoryGibPerVcpuOutputReference",
    "LaunchTemplateInstanceRequirementsMemoryMib",
    "LaunchTemplateInstanceRequirementsMemoryMibOutputReference",
    "LaunchTemplateInstanceRequirementsNetworkInterfaceCount",
    "LaunchTemplateInstanceRequirementsNetworkInterfaceCountOutputReference",
    "LaunchTemplateInstanceRequirementsOutputReference",
    "LaunchTemplateInstanceRequirementsTotalLocalStorageGb",
    "LaunchTemplateInstanceRequirementsTotalLocalStorageGbOutputReference",
    "LaunchTemplateInstanceRequirementsVcpuCount",
    "LaunchTemplateInstanceRequirementsVcpuCountOutputReference",
    "LaunchTemplateLicenseSpecification",
    "LaunchTemplateLicenseSpecificationList",
    "LaunchTemplateLicenseSpecificationOutputReference",
    "LaunchTemplateMaintenanceOptions",
    "LaunchTemplateMaintenanceOptionsOutputReference",
    "LaunchTemplateMetadataOptions",
    "LaunchTemplateMetadataOptionsOutputReference",
    "LaunchTemplateMonitoring",
    "LaunchTemplateMonitoringOutputReference",
    "LaunchTemplateNetworkInterfaces",
    "LaunchTemplateNetworkInterfacesList",
    "LaunchTemplateNetworkInterfacesOutputReference",
    "LaunchTemplatePlacement",
    "LaunchTemplatePlacementOutputReference",
    "LaunchTemplatePrivateDnsNameOptions",
    "LaunchTemplatePrivateDnsNameOptionsOutputReference",
    "LaunchTemplateTagSpecifications",
    "LaunchTemplateTagSpecificationsList",
    "LaunchTemplateTagSpecificationsOutputReference",
]

publication.publish()

def _typecheckingstub__d0470f207412cb167faa928dd6ec400239ba967a5d726981daff67fb008b33b8(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    block_device_mappings: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LaunchTemplateBlockDeviceMappings, typing.Dict[builtins.str, typing.Any]]]]] = None,
    capacity_reservation_specification: typing.Optional[typing.Union[LaunchTemplateCapacityReservationSpecification, typing.Dict[builtins.str, typing.Any]]] = None,
    cpu_options: typing.Optional[typing.Union[LaunchTemplateCpuOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    credit_specification: typing.Optional[typing.Union[LaunchTemplateCreditSpecification, typing.Dict[builtins.str, typing.Any]]] = None,
    default_version: typing.Optional[jsii.Number] = None,
    description: typing.Optional[builtins.str] = None,
    disable_api_stop: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    disable_api_termination: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ebs_optimized: typing.Optional[builtins.str] = None,
    elastic_gpu_specifications: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LaunchTemplateElasticGpuSpecifications, typing.Dict[builtins.str, typing.Any]]]]] = None,
    elastic_inference_accelerator: typing.Optional[typing.Union[LaunchTemplateElasticInferenceAccelerator, typing.Dict[builtins.str, typing.Any]]] = None,
    enclave_options: typing.Optional[typing.Union[LaunchTemplateEnclaveOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    hibernation_options: typing.Optional[typing.Union[LaunchTemplateHibernationOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    iam_instance_profile: typing.Optional[typing.Union[LaunchTemplateIamInstanceProfile, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    image_id: typing.Optional[builtins.str] = None,
    instance_initiated_shutdown_behavior: typing.Optional[builtins.str] = None,
    instance_market_options: typing.Optional[typing.Union[LaunchTemplateInstanceMarketOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    instance_requirements: typing.Optional[typing.Union[LaunchTemplateInstanceRequirements, typing.Dict[builtins.str, typing.Any]]] = None,
    instance_type: typing.Optional[builtins.str] = None,
    kernel_id: typing.Optional[builtins.str] = None,
    key_name: typing.Optional[builtins.str] = None,
    license_specification: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LaunchTemplateLicenseSpecification, typing.Dict[builtins.str, typing.Any]]]]] = None,
    maintenance_options: typing.Optional[typing.Union[LaunchTemplateMaintenanceOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    metadata_options: typing.Optional[typing.Union[LaunchTemplateMetadataOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    monitoring: typing.Optional[typing.Union[LaunchTemplateMonitoring, typing.Dict[builtins.str, typing.Any]]] = None,
    name: typing.Optional[builtins.str] = None,
    name_prefix: typing.Optional[builtins.str] = None,
    network_interfaces: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LaunchTemplateNetworkInterfaces, typing.Dict[builtins.str, typing.Any]]]]] = None,
    placement: typing.Optional[typing.Union[LaunchTemplatePlacement, typing.Dict[builtins.str, typing.Any]]] = None,
    private_dns_name_options: typing.Optional[typing.Union[LaunchTemplatePrivateDnsNameOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    ram_disk_id: typing.Optional[builtins.str] = None,
    security_group_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tag_specifications: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LaunchTemplateTagSpecifications, typing.Dict[builtins.str, typing.Any]]]]] = None,
    update_default_version: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    user_data: typing.Optional[builtins.str] = None,
    vpc_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
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

def _typecheckingstub__bde12f9bd6fc9f77a76aacb1ea1830fadc85ad3c463e23974d682a4efce46774(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LaunchTemplateBlockDeviceMappings, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c036765e0274fa46aee9719df2d45de6892f4023be58ae045e594d2a85200786(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LaunchTemplateElasticGpuSpecifications, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f12a1bc7e0ea7259c260bf4380bc79aafa776200d9178cbc1d05305dfe1ff184(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LaunchTemplateLicenseSpecification, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8778b09eaec1830690cca41dfaaa59f633a32578460dc99a648de4772e0c054b(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LaunchTemplateNetworkInterfaces, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__853919fb79eabaf8a5f887a4a71d76cb4ed897ecfce24667184b653b125bd99d(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LaunchTemplateTagSpecifications, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4559e3ce7f9d9f897bf8512487632f790ef6ae165f7bca55078d6a167666c7cc(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7e914bafa8f31fe20a4ffa290cceb470201240f6f2419bdd484ba098bf42cc0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9a2141580710a2f0a51745ad9bf72f4d60097ebca04083e9c4a9a82063b11e1(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__efb5f7c734499b17cf2cc05803d0bacd0233f73ba26fd73edd520ac777f212f8(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c426201ed3599c2aef4eaf9df0f87dfb0fcc88c43821e79fd76b8eea846faab2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5aeab1788f2156b906dd2c939ac370fb323f4688f58cc495dc410e0486ae2450(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79ca8d99502ee10a3bf3bb3a77876434b0897b9b1606b831ffc8c649c148e534(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__902fd9c5cb76741508c99b42b86f4fbf4a1475484505e5438532acbdf3346c92(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82a5e5215195bc7b2be2ddcf3794ca737372efd75145069ff4be29f9ba211a7b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39c9e70123250a416454a0ea5b750d2aeaf34569afee619c91f5034056fd8f01(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d178dd21963f2b24e231bfcdf7c2c60ad9fbfba2669b21ba9657280f2e54a1f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a656dbbc81bfa5e607c8ab4f35191b4c0fd557dc66b9ebaf3501261dc57ba8f0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d71257311c82cbd4ba496307a78b79ddfe51d7fa165c15534c40a1024477393(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__758331a3236117c94645153819fc470c15928324519bff1a26056f996dd3966e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9210b48f682385fd160e167d0d2f406a7a24e095e94d09d9a195f81765e9f714(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72c20db47193864194e94983168089de27d7949749cef189cd3010581e9f71ab(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6d55a3b550c48f1a0c007e10d0c070a7935901a708a2dd0a98c46740f38babc(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3954be3f86317a8fffe24666a6d2b29b07359bd5dd70de3583113aeeb1b4cb7(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__627bf7e8296d7d33206faa59b4a49a704ac1bbee7e683ff82e59ebfc18c3a170(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f3a1b84763a2e6b5db7b89af787349002a0cf127a068128beac5d9d193f2f2d(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6abe3b45efee3f1d547bd9fbdce5d9da58f6c3ad2770b684beab536236c19919(
    *,
    device_name: typing.Optional[builtins.str] = None,
    ebs: typing.Optional[typing.Union[LaunchTemplateBlockDeviceMappingsEbs, typing.Dict[builtins.str, typing.Any]]] = None,
    no_device: typing.Optional[builtins.str] = None,
    virtual_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82d54e2898f7a02489de9a607f8ee28ffb148a0869af5360d0bc3a80b5c40545(
    *,
    delete_on_termination: typing.Optional[builtins.str] = None,
    encrypted: typing.Optional[builtins.str] = None,
    iops: typing.Optional[jsii.Number] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    snapshot_id: typing.Optional[builtins.str] = None,
    throughput: typing.Optional[jsii.Number] = None,
    volume_size: typing.Optional[jsii.Number] = None,
    volume_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__761b4bc1d6b32644519d919be53ac3751e59a8d587e346ddaaebbb61f0f0195c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3bb9ef6965d31623006966973cce6f58b66600f3499dac8d3c3264347c70edfc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6094b1f082c1899dcf4fe4c676bb0c7de019ccc948a9819ba0d6e15cbdbb1481(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__345495ce39e2785758252d3356bb76da80e6838a124e3b9ff677f14de955ceb9(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7a480a560d05e892c0b016f136f840a544988271e6c3e3877bbef8593b32183(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__291c4c6f01517aaf324274ab7d777c37d2ef9095a992ff5c75e1c6ebe9873366(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ba36c664f3798a445d409b24a7fda555c10dd1f14069d2085426085c0fd0c5e(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__784cae271a58339148460db47a1d65e854b2f3ed44d29d26c27dec1533e95172(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12ff0e463b14f4e542bb8abd3556e00826c467581263f3bc9e63f649ceef4107(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5bfa9df2bcd15f7ec3796d09f6c8f71f772ac5b1a02853359e409c299dc3c6c(
    value: typing.Optional[LaunchTemplateBlockDeviceMappingsEbs],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de27766becdfc5b93c46e7c6d01090c39a80f8b70bc8f5e5793f226c0cfeb421(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2961dde1c5517e326e589526f1a8b4e4b3f86216f2d6c10ae760473616802933(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ccd22f4d78ebff3b56b656c7186ef741471a4e346d3675d3074ace0656773e8b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__480a551086dbe6d867cf3f8811872e8de069721b47355e3bb6f1f5df337c9e62(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09d52645fae0b863c296fd667912169390a7c6e922c6bf54b42d0932f887ace1(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dbcb31f038735cf9cccbdcee36d23b630c647a3c1835c60e9bb3839a0063a08b(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LaunchTemplateBlockDeviceMappings]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25b4ff7b5a85bfa47c1f8b705efd51ae601c298447fa5e3d20ab003a1ee0070b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a4402ea582a9d8e5850e1b86ff06fb9cd661abb305ce3d4a85eac149696b098(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__145f56bfd39894290e4b0bb66599f810af830031795109e4dcbaa1594f1eb6df(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b91547071acc58d056347d431aa5a5dc183106170e097a70ffe7e5a274a8603(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__858cd6a9b3314fdd286980c8aa76fa19048ffb5a2d5adae377e939dc00b67268(
    value: typing.Optional[typing.Union[LaunchTemplateBlockDeviceMappings, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62193771ae313af4090564e8796213a59581230a7c3936af428d4637da8375bd(
    *,
    capacity_reservation_preference: typing.Optional[builtins.str] = None,
    capacity_reservation_target: typing.Optional[typing.Union[LaunchTemplateCapacityReservationSpecificationCapacityReservationTarget, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61efb44ae748820ad8961342c3eb8229dd7ae92d9bdacbf85725ae8fa3a3d4c0(
    *,
    capacity_reservation_id: typing.Optional[builtins.str] = None,
    capacity_reservation_resource_group_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__835ba0d542bc5b87fc32559306e0441b6a226a4a9e3e39d75f566b0ad3c9d10f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ffe04bc09de317c86c1fcf3262d86aca00252dcc0c6309bc5261e19886f5200c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02745dccbb0de89ecd38cc29aa465a5af2a1ac5a2ff16e3ced1ad14be9fec49a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ebff3557d14f128e4ade22bc738f7427105736e98f13ffafff13e244829d4479(
    value: typing.Optional[LaunchTemplateCapacityReservationSpecificationCapacityReservationTarget],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff9b7094a1fcdfc47adab9a41d0f0e0e5fe541d574e0c66b3732df2abcc3129d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5a744b87edce96d2ddbc852c8ed65fe1cd15ac6535fc31a72a48c1cf12649a4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c630dd386b16ad3f79ff934c37178b7ade413d4c20b81ca04f1c75d71e467ff2(
    value: typing.Optional[LaunchTemplateCapacityReservationSpecification],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5bb06656946ef75df102afcb0b4a7723d3f54f3c484f13b789bcabacb86368e2(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    block_device_mappings: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LaunchTemplateBlockDeviceMappings, typing.Dict[builtins.str, typing.Any]]]]] = None,
    capacity_reservation_specification: typing.Optional[typing.Union[LaunchTemplateCapacityReservationSpecification, typing.Dict[builtins.str, typing.Any]]] = None,
    cpu_options: typing.Optional[typing.Union[LaunchTemplateCpuOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    credit_specification: typing.Optional[typing.Union[LaunchTemplateCreditSpecification, typing.Dict[builtins.str, typing.Any]]] = None,
    default_version: typing.Optional[jsii.Number] = None,
    description: typing.Optional[builtins.str] = None,
    disable_api_stop: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    disable_api_termination: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ebs_optimized: typing.Optional[builtins.str] = None,
    elastic_gpu_specifications: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LaunchTemplateElasticGpuSpecifications, typing.Dict[builtins.str, typing.Any]]]]] = None,
    elastic_inference_accelerator: typing.Optional[typing.Union[LaunchTemplateElasticInferenceAccelerator, typing.Dict[builtins.str, typing.Any]]] = None,
    enclave_options: typing.Optional[typing.Union[LaunchTemplateEnclaveOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    hibernation_options: typing.Optional[typing.Union[LaunchTemplateHibernationOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    iam_instance_profile: typing.Optional[typing.Union[LaunchTemplateIamInstanceProfile, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    image_id: typing.Optional[builtins.str] = None,
    instance_initiated_shutdown_behavior: typing.Optional[builtins.str] = None,
    instance_market_options: typing.Optional[typing.Union[LaunchTemplateInstanceMarketOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    instance_requirements: typing.Optional[typing.Union[LaunchTemplateInstanceRequirements, typing.Dict[builtins.str, typing.Any]]] = None,
    instance_type: typing.Optional[builtins.str] = None,
    kernel_id: typing.Optional[builtins.str] = None,
    key_name: typing.Optional[builtins.str] = None,
    license_specification: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LaunchTemplateLicenseSpecification, typing.Dict[builtins.str, typing.Any]]]]] = None,
    maintenance_options: typing.Optional[typing.Union[LaunchTemplateMaintenanceOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    metadata_options: typing.Optional[typing.Union[LaunchTemplateMetadataOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    monitoring: typing.Optional[typing.Union[LaunchTemplateMonitoring, typing.Dict[builtins.str, typing.Any]]] = None,
    name: typing.Optional[builtins.str] = None,
    name_prefix: typing.Optional[builtins.str] = None,
    network_interfaces: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LaunchTemplateNetworkInterfaces, typing.Dict[builtins.str, typing.Any]]]]] = None,
    placement: typing.Optional[typing.Union[LaunchTemplatePlacement, typing.Dict[builtins.str, typing.Any]]] = None,
    private_dns_name_options: typing.Optional[typing.Union[LaunchTemplatePrivateDnsNameOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    ram_disk_id: typing.Optional[builtins.str] = None,
    security_group_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tag_specifications: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LaunchTemplateTagSpecifications, typing.Dict[builtins.str, typing.Any]]]]] = None,
    update_default_version: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    user_data: typing.Optional[builtins.str] = None,
    vpc_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3821d62ebcc8a437ec1e8e1b08bad8e8140e9b7279369e3d739cd764b900b36c(
    *,
    core_count: typing.Optional[jsii.Number] = None,
    threads_per_core: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a1b03755352ad65764746171f906c7ee8f6f9a1eea9469cd61a37756c806534(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b856e0b70260e1dc7c83973a2bbe3b12d255635901f99ad770efca6a22ddf10a(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8bf0e5797b346014a316eed87b75941bfc4104ece916af9edee5b216ba6a2b09(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b7ab34adfa6d654b51d538458f20813053c59a81c31b4a6c7df7abacc3d7082(
    value: typing.Optional[LaunchTemplateCpuOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7999115e17091a9ddaaeae011e07d4cf65d07effff3a9ad80d614b9e72d40f39(
    *,
    cpu_credits: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09d5810a51f64e54cb259c6aad922b474d01ed56fbe2ea34e95495b299419e34(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6e23da63b390818205e681cf0536e2b2e98dc7e52185afa512ceb5dbee71dc9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cdfcec7af0051d6e1a883d11698307ec02e7a6ec84eb8c71c228ec4a5e445942(
    value: typing.Optional[LaunchTemplateCreditSpecification],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3fea3586fc475da8574bcd06a8ddb22672ffc60f64b5baa44d2e61523f5a035(
    *,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30aeeeb925bb1652cb99598aff0c5ff3cf0c3d1dbeb168dffe4aa3925781096c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c486bfa7d686f2c9b88f269a084267310fb8760eff16ebb377eccf0f00f57ac9(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__387e7ee519fa4582155bc70c5dffae6a377a1eaeb1366b4f4a8601bbffea4299(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f2578d3a8abaad6bf93a9f9700cfea11a4886a627399b7a7e8c584c5d5f2c24(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87a11d02d4a96477112aa05bbdb965d6d1d2252671d77eb9067ce32fc8592e39(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__442ea892ba1d0a9482b7f9187a75911d388e624fa2ac3a197c9d19393cd1ac0c(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LaunchTemplateElasticGpuSpecifications]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a81f70736341d7d575138f6ee8a6aefb4f4221a513d4a62d7ea7a9e134c322f6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d231a0d5ca28941516c0fd698ca764c1961bdd4c746226043a304ca5c6e56e1b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e21d9f7aec4c4d272daa862fc4c0f8a730f28e7def9f51479a6f48cb10096253(
    value: typing.Optional[typing.Union[LaunchTemplateElasticGpuSpecifications, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3e3173f1c88b6cdb59709a5fa299a070d3fd77bc97282a16be00e51e7153171(
    *,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00933cf4bd28fa99da9a5915851da3e3c4bef809ae46ef06d2413f9d33638799(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7369eeb24dbeed199dc0b03e76171342f70fee1e9b503eb92f8f5499dcf5c7cb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5208ad541a2ff42ec9d0472df5ad3cc9becbdf24386f84f7e47fed98d3bfcca8(
    value: typing.Optional[LaunchTemplateElasticInferenceAccelerator],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f02f0e38e951218e042a3be6d57210a4a16d26607ee67ba5708b7518c2409100(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9dadecdfacf3f9ff44d7610897d2a22b1da7ae3ca7efe87f5a2d882f2f610d07(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3e184d13fe920a555bb7b34d224d37b6e94f0dab91f9f39e1cde0e1c264ba54(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed40a24685a0222baedee215e29fce2ee9e58d04ca2704b722d7024e3e1db68b(
    value: typing.Optional[LaunchTemplateEnclaveOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60970343b4cc3a3adf99ee3f0da4a99d9603bad2643737d7a20c47d407e22293(
    *,
    configured: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__178948ca0485650d4674f5bc9186a5212823c88aab15d4a0fdc67dcdcbe6776f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33aa1cb651b2792cd58a624250a228318aac672b4e69b784c7beb9f0d56c244d(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__912616f9e53fca614c9b78b9269a8b97c5629df6397a9e0949cba0e7168ff803(
    value: typing.Optional[LaunchTemplateHibernationOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1df29693a0a28e146b745d8797ee7e9481d867a28df9a96160eeb32e42b1378a(
    *,
    arn: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4fc04aeefbf55b51b56a42b5099a2d8b18c6bb1985f5befcabbd6c4de7ff309(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51606d7136d1cfddc7085ffda57b0ad04d8c5ebfe3ed85330b13f536bef8eb5c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d324c7626334669715f012b3ed3ed14df539b53a010f4e9c5f9fc78425c62985(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af2817f69148d098f8ba77a902bbd247c3a46950e588136f0f5144eca7f4ddb7(
    value: typing.Optional[LaunchTemplateIamInstanceProfile],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4cc9bd83dc3d052fb4c5c6997a559e225fd8f7cea8c45deb1c8fc9bbbfc327ae(
    *,
    market_type: typing.Optional[builtins.str] = None,
    spot_options: typing.Optional[typing.Union[LaunchTemplateInstanceMarketOptionsSpotOptions, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a691eb5315c0269badb1c023434aa869f97593eaddeb3e291b062fb684af8e2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36441bd509eecd79e0c6dac3ba845579506799a4e7a694b9be8c8c7a9faf4d99(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0174fe7cdacf31e9a60e7e7d63653a43f8367f319dcc11a10360b140ff8ca603(
    value: typing.Optional[LaunchTemplateInstanceMarketOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9be6f6d5f5ff3d177a3cc9e587bab78addb78bfa1e8ed1ec99cf48d71e694f8(
    *,
    block_duration_minutes: typing.Optional[jsii.Number] = None,
    instance_interruption_behavior: typing.Optional[builtins.str] = None,
    max_price: typing.Optional[builtins.str] = None,
    spot_instance_type: typing.Optional[builtins.str] = None,
    valid_until: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a80d6f60dfb179691d04918aca242144cda05e08ac1ccbca444d48d61bc8cdc(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96fb75b8933cfd143ec4cb8118958f20f50f721009c7df6c5c45807a014812b6(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7833ee9acbcb5d732346f239e97e35376e649ddbfc507fd39a6423ba1611a8ae(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af3804236b9e83a8039ace2dcbd6df78909d417a464b96c7d98fcca2bea431f6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8cee3f92a4fed3e89edcac154dbe457aaa3130ac65b13211a866ff63fcc7cd4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2495312cf363a8b098e095f104372c54cecfb55786e68c87bebbfcc68ad405a9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b55f57b3797ced4cb973c45b287fa07b33d12607a788a7120d8cec4d4a2dd953(
    value: typing.Optional[LaunchTemplateInstanceMarketOptionsSpotOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f8457f019b0a039cf717b8de08872e0510da42ddc21aabed9ec3a915a9d045d(
    *,
    memory_mib: typing.Union[LaunchTemplateInstanceRequirementsMemoryMib, typing.Dict[builtins.str, typing.Any]],
    vcpu_count: typing.Union[LaunchTemplateInstanceRequirementsVcpuCount, typing.Dict[builtins.str, typing.Any]],
    accelerator_count: typing.Optional[typing.Union[LaunchTemplateInstanceRequirementsAcceleratorCount, typing.Dict[builtins.str, typing.Any]]] = None,
    accelerator_manufacturers: typing.Optional[typing.Sequence[builtins.str]] = None,
    accelerator_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    accelerator_total_memory_mib: typing.Optional[typing.Union[LaunchTemplateInstanceRequirementsAcceleratorTotalMemoryMib, typing.Dict[builtins.str, typing.Any]]] = None,
    accelerator_types: typing.Optional[typing.Sequence[builtins.str]] = None,
    bare_metal: typing.Optional[builtins.str] = None,
    baseline_ebs_bandwidth_mbps: typing.Optional[typing.Union[LaunchTemplateInstanceRequirementsBaselineEbsBandwidthMbps, typing.Dict[builtins.str, typing.Any]]] = None,
    burstable_performance: typing.Optional[builtins.str] = None,
    cpu_manufacturers: typing.Optional[typing.Sequence[builtins.str]] = None,
    excluded_instance_types: typing.Optional[typing.Sequence[builtins.str]] = None,
    instance_generations: typing.Optional[typing.Sequence[builtins.str]] = None,
    local_storage: typing.Optional[builtins.str] = None,
    local_storage_types: typing.Optional[typing.Sequence[builtins.str]] = None,
    memory_gib_per_vcpu: typing.Optional[typing.Union[LaunchTemplateInstanceRequirementsMemoryGibPerVcpu, typing.Dict[builtins.str, typing.Any]]] = None,
    network_interface_count: typing.Optional[typing.Union[LaunchTemplateInstanceRequirementsNetworkInterfaceCount, typing.Dict[builtins.str, typing.Any]]] = None,
    on_demand_max_price_percentage_over_lowest_price: typing.Optional[jsii.Number] = None,
    require_hibernate_support: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    spot_max_price_percentage_over_lowest_price: typing.Optional[jsii.Number] = None,
    total_local_storage_gb: typing.Optional[typing.Union[LaunchTemplateInstanceRequirementsTotalLocalStorageGb, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b6a798202add089fc06a4a1bd243ddd2125563a5e49ed9270196c3f308adee8(
    *,
    max: typing.Optional[jsii.Number] = None,
    min: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__380b29d2eb7bd4bf7be142fa4611449806b7bc6f306c984da3de823a2abf6102(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2d117198b540e41624c69e8889d8537df0bbd561ae5c4c1e3821301fb08790f(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1dda5fa8d3055b691fd618064ffd0002a2c8cc06529e456dfa574ee508fefab6(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ee08c4da7a3bb691a3e0a64a9ab643285bbb486c148a9f3bfcd86ca1a2e64ee(
    value: typing.Optional[LaunchTemplateInstanceRequirementsAcceleratorCount],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d05d33e5a07d4419a8630c97d6d2f3c6aff341568c4dc3b2e00f850a884a1121(
    *,
    max: typing.Optional[jsii.Number] = None,
    min: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94f753a9f54c71d6937d413d588c400a878c0f19f331ee6900c8e552597f48ed(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71b4c140a502c72586cacb61191de5261c42e0f1be1b1f1423aad50783ea1274(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db46514aa7bac365bc006c6314897c2bdb200ca552c120ecc6e99a2252e4795a(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2c51f8a7ee12cc31f6d6bf92c3349643c8c86e2044b2554558f385b5d0f0b8f(
    value: typing.Optional[LaunchTemplateInstanceRequirementsAcceleratorTotalMemoryMib],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20188ccb8c6623490ccd725c9a437100596250cb0fb6d85a29a7a5157f35e6c5(
    *,
    max: typing.Optional[jsii.Number] = None,
    min: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb52ab11ad9c09e098e5210161ba6df49137cc4d8cbc74c1927b9fa2f8528da8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53d0f095820d91e593dfa8536acca826b0d1ebd692eeaa4f94ef66c350927a31(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e0b9fa9655ab3b7e74dc1bd1cac0948b572b3f2b343682350d1d9e8d9ac3515(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7997bc1f97e18303601a3f9cef7e04e77bb66b245fabccaef4b64de1a5b20bd3(
    value: typing.Optional[LaunchTemplateInstanceRequirementsBaselineEbsBandwidthMbps],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0acd62f11701b125a31266e304ed97306d0143f1adc40fef1a90c8d9d710660a(
    *,
    max: typing.Optional[jsii.Number] = None,
    min: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__852249a066bb8449717d494e4e0fe2f981a73e977cbfc27e73ff2fd4e137eb09(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16b0c4b3a4c9f82ad186dbaeb004df4cd64ce851498600d2e352680381043539(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0aabbfe3c5cd10c4608ed1a56f5bd32a5645e557e72f4535234429ea0d28b2b3(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a30925864ad1583621a3d372eddf7acce6c719a2274cd178bfa5d0b4bd1f3254(
    value: typing.Optional[LaunchTemplateInstanceRequirementsMemoryGibPerVcpu],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8cb9c6d69786f3a8a54dbdc4890afaec006be177a03e6044f868031e6bdced0(
    *,
    min: jsii.Number,
    max: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a93b3df3c7e78b09251e0c16b9151255f43c36314742654ee22b1d164e33feb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18efe0511d9f70cc0ac5ea111b6284bf006281c41065cfbfc057f32abdf809e1(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3dd308aa80a13e0ee95d6568f10238a11f48073c1be2071a813080756ff357b7(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c43316b2707279abd2138e1d02d0e3094cfc3c7ec39f1271a21399c0ebfd7fd5(
    value: typing.Optional[LaunchTemplateInstanceRequirementsMemoryMib],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac60803915a802756beaa5c3bdfb00ebeaa785ceba24504e10c19da9a162540f(
    *,
    max: typing.Optional[jsii.Number] = None,
    min: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7eec6e3ee782e85ac4668243cabeb060e08ea32f5d83605f76ec6f58ea4eace(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c6eda9cf8f9ff82172e0c35966a756349680c77b07fa9072a3a5bd5724ea290(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49de90c3085e5b1699694ffb1502774741d972235633843d2040659552fc8554(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1514e7b8c0a83b58b49bcfd3e44fc2e6cdb3ce85643473422d55d63ba43b13f4(
    value: typing.Optional[LaunchTemplateInstanceRequirementsNetworkInterfaceCount],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3b2dac7fc47ec0509301b7891c111802b55647a221759c455b124e8ba988070(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3729dd4b2be2a8af6439303b054b77ef9bfe45c634f216e97d74a94a8f0da587(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d2a787f11c10b85d5c3d66dfa7438a6d9e78c18479a6148be3dad5b9a2dfc7e(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c6804e09f1cf6c2a2ce8f5f4e92317e719934c1c37757fa0db14ecb47555264(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d00cc1fddb1e740fbeff8fd9e2dbfbc9ad61543de6d9813c62d23a7c8be80d8a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6770fb529720a09c5e5b7b6dd17063f83300787ae2a1c2425224efb9fabaa019(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09f44d66810a54877609a834cdb70cb1a9f9eb8239d1cf891626a7388144690d(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf7e42e2b5f7b947108d604fac78dd543eb53a1eca4f12e24ae354112c338322(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0331204cd3c45c3a6150675ec0d2e0e99a9e4d1ef2069b047852993a1433074a(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e594b289d68e216e382236abbf6740f3d062960291eb5ac5781f3713c1e6ed81(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fcc7524b102e0108f4a47c1dbec2f2a324bd088fb2f1da283fcca023fe5d72e5(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3847a1ed4685bad15ae5ffbe3316781f36f99b63ddd1317560de254f5d85093(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__328e2eab9826979a4e8e079855e6b100112f0e906878d530e49a0018ccabdfa3(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7a985566e293659665fc55eb05b33414dd3501babf35f54e12df3888e0d3da2(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__681ed963193840ea53c9a6aba7ae101c37277cbf5202eb1320b7ee6562f584d0(
    value: typing.Optional[LaunchTemplateInstanceRequirements],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0882ba1df259250c98833dbfcb3f53ca75fd02605f6f5c3a1280e8bb8575f723(
    *,
    max: typing.Optional[jsii.Number] = None,
    min: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0649571b73946846f7057e7a973efae73dc54bc1e7ec1c19df973fd57cadcb8b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a911ce38ac98dd86da2d3934207d412ed9af302f0dc17bc2d55a8210d5fc176d(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5a58be4ceb7a219d411fdda44d0912a2f128b53795fea012ccd98993f7ff2be(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7bde4783836071a54f25afc3e2d5c2303120371d4ff79df1ece9c7551c8b69e6(
    value: typing.Optional[LaunchTemplateInstanceRequirementsTotalLocalStorageGb],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe9791c3c8e700956dd5e44ce955d6e2e1f98263926390e147d0dc57a612cb25(
    *,
    min: jsii.Number,
    max: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73b401ac4da410aa9c24cdb81a965e4d9d6fa045b485568cfacc1f2c86ec0453(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9bac5f752f9534460e4c4c871b2b60601fd76bf7c95240626511c0a334b041b(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bcccfe9783dfa294d71742c00a07764436fd4423594b113f428af264898de306(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__945b0d283848e06a1e89f369e837f080d89594695c9cfcca6d4b55701a1e5870(
    value: typing.Optional[LaunchTemplateInstanceRequirementsVcpuCount],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a752a77ac939e70e9a078322047b6ad51baeb4fce4859a4fe424458870c24d52(
    *,
    license_configuration_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9600d60e42e7d35e6f1ab35c7c51e8738a3de132be9647168578acd663aa6297(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb3f38e7e4ebc36a25874684dd6fe3a7bf3a629adfb2a93b92545f2f8d2410e6(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ab632f3d3255beca8bac3dfca32d6df24174524bb4f1981b6650cd80f8dee3a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__981d8479c2284f2476c99b8b55c8c341ce366f6ec876f9279aa3ea428d2f2132(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c871e1c20ca44b9d8b5cb5c42be16bd31321fdc26bbf8e014c9e923d6a735b6(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c23d4dc521a1e3a51773269966787d9041a22d75b7baf68555cc4ba036075b00(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LaunchTemplateLicenseSpecification]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ba75c8f52ea0068aa88200bbf3d67dcdd4fad2c3852db40796fb56b0be0d35f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40b5a1fc3c214ee8c238b509c8dcad14160c05be0d881e8c6a80b9fc4ab3d914(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b0dbdc97a2ef8d18c6d81d0ac519a9a9b87d4cda09005a66b95cf11ce132c56(
    value: typing.Optional[typing.Union[LaunchTemplateLicenseSpecification, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__921285fb4b9c7b2ce7f77dc770acc6b805068ebc2d58d793bd24942dbe9f7e51(
    *,
    auto_recovery: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f78a654c46a9f888163d80220ae8e34e4b6f8bc0ef68d6f677602248ff102970(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dfc97ecc6fd75af29456eda36702311f779e6b8bf779ae4193f41ff7f77229d3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7dd539be5019f5ac1e188fb1c63125feaea2b218189e2451ca2b5a5a051d9d8(
    value: typing.Optional[LaunchTemplateMaintenanceOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__397113e868199d5b7871183769c39c4ede2d3563373a4b7c1818bf3c79caa41b(
    *,
    http_endpoint: typing.Optional[builtins.str] = None,
    http_protocol_ipv6: typing.Optional[builtins.str] = None,
    http_put_response_hop_limit: typing.Optional[jsii.Number] = None,
    http_tokens: typing.Optional[builtins.str] = None,
    instance_metadata_tags: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2c8e4e1055f5c9bc8f0fea4fbd5c453eeaa9f7b938b3cdb2cb7f618de2ef5b9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4fa8eaf408dda81fdfd20528d3124881ae441864f60ca7a53a809b980bb21426(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14129f70b2f8ab0d81fbedebf11048c89714ff2b56c2c57c3bdc7022de255825(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7c97c300b6f709acb69879091a38f6b8cd8d669adebde89379e00e5f4c55147(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4823c498b7ab559ab44d11b6b735feddc7d28f6802463b6628b002f2f6a4ee48(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26631dbc0bf0ecaf2c968c9e79ad36a77631736c80e5c103ffa14c8028f85890(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__192f112b95fd12737a79799b09e9c09f23288c29703cc6f49c007f3dbbc4abda(
    value: typing.Optional[LaunchTemplateMetadataOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02a31ef33866d7ec8e405454827f01452583d562256a35190e1b500b011244bc(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6abb3c432760751a80fe2ca2ec4dbe559459d0e1c60e4832043ec211093224f2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8593ca801c227b4b51298951f1d4be8d7faa7f852f81bfa0c6d7f9b2f2420e80(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b5799d931fd9e585d4430dd9346b2aededa0036f39d3e4dcec65a344d74ba4b(
    value: typing.Optional[LaunchTemplateMonitoring],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__704ec35ed869aee50d4799b705b7a87c66b91e39e483d7020a77cc7f524a82fb(
    *,
    associate_carrier_ip_address: typing.Optional[builtins.str] = None,
    associate_public_ip_address: typing.Optional[builtins.str] = None,
    delete_on_termination: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    device_index: typing.Optional[jsii.Number] = None,
    interface_type: typing.Optional[builtins.str] = None,
    ipv4_address_count: typing.Optional[jsii.Number] = None,
    ipv4_addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
    ipv4_prefix_count: typing.Optional[jsii.Number] = None,
    ipv4_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
    ipv6_address_count: typing.Optional[jsii.Number] = None,
    ipv6_addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
    ipv6_prefix_count: typing.Optional[jsii.Number] = None,
    ipv6_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
    network_card_index: typing.Optional[jsii.Number] = None,
    network_interface_id: typing.Optional[builtins.str] = None,
    private_ip_address: typing.Optional[builtins.str] = None,
    security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    subnet_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__379ace02d87811867d800d325e258c7923b36311ae595e9314fb0f24ef614be3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9cb0f3268618c11b8e92ba033c7ff74e0a933eae36aa3fa59fca3a2f23cbb4d9(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc4c70ce7d0db92ffd55e4cdac848eeed169b8335af98e69aceb1abdc4e5c55a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19dc70c462daed4cab84a56d7f23f7a89cf198fe92c23222b0661658275fc1c4(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0340c11ab98cedd9b4490609a0234afa428bd7000a56ef417ef49f92c93e01f(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92054e8d40338a2ea6e2d126ba653c3c74e96f9ca783581fc9d10207e98f6961(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LaunchTemplateNetworkInterfaces]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98884d30b6fc05c003803bf58cf7de48a5fbf316950608dd24d39694d7706887(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57131392d8e93ddb7465b5fab700ebab6b92f9f6cd9fccbdca993b094f4ef78d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da47563914824900a5d5bc8d524ae6e40f4a2bb1236e656a6500b53f332135f9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e4a8e9d2548730beddc56d1d6f1ff40f82ba74d23b22a3ce411dd24653bc13e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be7e53ad06a26ef72cb5eb66559e4ed39e25ff521b4f2caec39d10652420fd7a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49bc10c515f7b80dacd9514812824b32e2da1434c00bd6e0df12ad41d39669bc(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17c840581e642395912a4a6cd9e7061c9d6bfea52fa9c5e51f5fbe01c605d7e0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__588d6ff98a957a4ee920b5b561c3ecde7d264938918aa2b8a4b58c525b3fc746(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2af803e6e1bdcf6e23e6b526719605503eb826e51ffe38265697f5bd59dd8b94(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f32c510550dbec8932cd17efe900cbdcb3114c7350273799c6019afe4eb6a418(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__deb928a9f576987a5b2d72c902b90f9ea934317db441f72f2f9f91d24041c760(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d4c8578d14efc78783932dfe232e0a66c0f48efc0bebb3e17bf9d92b1567169(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef505199fc6235cbff5f45806c1eb75e1eacb393bdc2450c3c4d413af33d04e2(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4d3cc0e914ceef9e21947809e390ae21237b80d68d14edfdc0be0a3cc1a0334(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25467bbf4b09a1240dc90e82daf8ec5310e930af5475bd24fb7f86891c5a4007(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f8b1519a726c3ce3260a433b3a09b54fbf5b114391b13984813c9cc91ca3eb7(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67eb5065110e1b91c94091fe6f987242d191090dea68f0ea34ba1863d1db20b6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4158faaf8faaa6a4e8d356f324245735b33b8be19c60e6023c058b7d55be68ae(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5312a3c2069ad1dc1d16722e2299c3991c44727ab28637145a34ebe4e2146f7e(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62ea3dc0fa7ae218daeb090fc064d02f2cded1a275143125e1b72ae897f0ad1b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f60580ff5f0b08420bdda3d5af1ad57368b840a9185a67cdf5cb607efd518ed(
    value: typing.Optional[typing.Union[LaunchTemplateNetworkInterfaces, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__391b1674b1668c2d6c6906c7e10615823ade0746b7f5e79432d97f410a03bed2(
    *,
    affinity: typing.Optional[builtins.str] = None,
    availability_zone: typing.Optional[builtins.str] = None,
    group_name: typing.Optional[builtins.str] = None,
    host_id: typing.Optional[builtins.str] = None,
    host_resource_group_arn: typing.Optional[builtins.str] = None,
    partition_number: typing.Optional[jsii.Number] = None,
    spread_domain: typing.Optional[builtins.str] = None,
    tenancy: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfa58230c3cbc4f8e1a9c78e81858160b240589e0c08feaa7d974d967c047a5e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75cb08815ee669126b0625f8efcf2bb56bd91bff2339a4d61ef22ea85790b41e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a51963d71db7147cf4ceb3f21ab3bec709b50df69b294034e517f6d2db7781ac(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e4b9864d60ae07246f1f0f581faba84285d0a007323f610852a8621fae05a25(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ff555c5e9fadea15c2d1dbeb738f55d1c2737e5e8e4ef41661d0ee7c4ffc4cd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32b16982d29af566584ee6e604d0cbcf5eec6518a8fda075296072e1409dc0f8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__edd7d569c055b1e4d1b5aa1469dd084042fd7404757ac2d71000a8c098490e02(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44f8db1e579c79b54cdff276bcd2e9694c9c773b19ecd009f819a662101fcee4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2af01b5048bd07e6f70767cf2bd064a9fe930b128f33994aa15293f263a329b0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30a814ecc9cbea4c80390e8a377ec826483ab7dba4d97cf5ed41eafe068cce63(
    value: typing.Optional[LaunchTemplatePlacement],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef1eaffef792e66dd497e5f9ba88af78485f240e993ab91ee046d280d8710a0e(
    *,
    enable_resource_name_dns_aaaa_record: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    enable_resource_name_dns_a_record: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    hostname_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1fa2f72cba68572ae26ac52e617076478761eda439c8a80374f810e37b3ba0fa(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__381cab04d5a01b52e27f201e77e8d828fd216ac0026505de1ce80e6548bd872b(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd503fd6c1702739feaf54794df4382acf4defae8f82b8bbacde0a56ec868230(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a56b8c36c6d8ad23a44d811242f35e320c8082dd354e02f6117828ae611e0fc4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0db3ec24a84d1db7e9e088f028172a79ec96ed95323f7337d1c2e07cf1af1e8f(
    value: typing.Optional[LaunchTemplatePrivateDnsNameOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06901b3f5646f7eeadc2e2447bef060530ccf2a771c5abc573a057e0b719088a(
    *,
    resource_type: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46478445d7cc2d30588f1cb6e105878f9467883ab0b33b4078ec79598ce5f290(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__302e76514e050d9ede77d775864a5ebcb26ddf28e30967b3d19a7d12dbd016d2(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f313371bc6ff14acb541c965ee5fe602ca1c43a2abe578a8dded2319e9ec74a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3be1f31cea2d381e9a4ae83b7f74796ea8f346a9f74774ed0f0cea5f653f8c8(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88adbdc03198f2134feafdb05b6abea7c2d94b3647e1d0239ee85ac7d889d989(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f34810e575438cf5e43632496ef3a527c6b473ac7f23bd1cc56654824c23d85(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LaunchTemplateTagSpecifications]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__768db6e75c6b2b7bf5b929025c16a5805aab5fd325b05d6b68e6e4b8c74ac771(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9994567e425d0d01d4a15fc92743d5a8de53bbe2a0193bfc091e943ca574a82d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c758e7fd4a31c5aa17d9fd4d37f4f30c79512170cc338a51f96b153ba2c6fa31(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91d5fa2333b58ed1e46e6905e5b92c4b69f45cb112caefc1d057f7b1ee3c1a2c(
    value: typing.Optional[typing.Union[LaunchTemplateTagSpecifications, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
