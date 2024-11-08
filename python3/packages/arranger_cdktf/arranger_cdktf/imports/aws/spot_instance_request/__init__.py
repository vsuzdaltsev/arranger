'''
# `aws_spot_instance_request`

Refer to the Terraform Registory for docs: [`aws_spot_instance_request`](https://www.terraform.io/docs/providers/aws/r/spot_instance_request).
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


class SpotInstanceRequest(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.spotInstanceRequest.SpotInstanceRequest",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request aws_spot_instance_request}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        ami: typing.Optional[builtins.str] = None,
        associate_public_ip_address: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        availability_zone: typing.Optional[builtins.str] = None,
        block_duration_minutes: typing.Optional[jsii.Number] = None,
        capacity_reservation_specification: typing.Optional[typing.Union["SpotInstanceRequestCapacityReservationSpecification", typing.Dict[builtins.str, typing.Any]]] = None,
        cpu_core_count: typing.Optional[jsii.Number] = None,
        cpu_threads_per_core: typing.Optional[jsii.Number] = None,
        credit_specification: typing.Optional[typing.Union["SpotInstanceRequestCreditSpecification", typing.Dict[builtins.str, typing.Any]]] = None,
        disable_api_stop: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        disable_api_termination: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        ebs_block_device: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SpotInstanceRequestEbsBlockDevice", typing.Dict[builtins.str, typing.Any]]]]] = None,
        ebs_optimized: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enclave_options: typing.Optional[typing.Union["SpotInstanceRequestEnclaveOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        ephemeral_block_device: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SpotInstanceRequestEphemeralBlockDevice", typing.Dict[builtins.str, typing.Any]]]]] = None,
        fetch_password_data: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        hibernation: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        host_id: typing.Optional[builtins.str] = None,
        host_resource_group_arn: typing.Optional[builtins.str] = None,
        iam_instance_profile: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        instance_initiated_shutdown_behavior: typing.Optional[builtins.str] = None,
        instance_interruption_behavior: typing.Optional[builtins.str] = None,
        instance_type: typing.Optional[builtins.str] = None,
        ipv6_address_count: typing.Optional[jsii.Number] = None,
        ipv6_addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
        key_name: typing.Optional[builtins.str] = None,
        launch_group: typing.Optional[builtins.str] = None,
        launch_template: typing.Optional[typing.Union["SpotInstanceRequestLaunchTemplate", typing.Dict[builtins.str, typing.Any]]] = None,
        maintenance_options: typing.Optional[typing.Union["SpotInstanceRequestMaintenanceOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        metadata_options: typing.Optional[typing.Union["SpotInstanceRequestMetadataOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        monitoring: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        network_interface: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SpotInstanceRequestNetworkInterface", typing.Dict[builtins.str, typing.Any]]]]] = None,
        placement_group: typing.Optional[builtins.str] = None,
        placement_partition_number: typing.Optional[jsii.Number] = None,
        private_dns_name_options: typing.Optional[typing.Union["SpotInstanceRequestPrivateDnsNameOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        private_ip: typing.Optional[builtins.str] = None,
        root_block_device: typing.Optional[typing.Union["SpotInstanceRequestRootBlockDevice", typing.Dict[builtins.str, typing.Any]]] = None,
        secondary_private_ips: typing.Optional[typing.Sequence[builtins.str]] = None,
        security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        source_dest_check: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        spot_price: typing.Optional[builtins.str] = None,
        spot_type: typing.Optional[builtins.str] = None,
        subnet_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tenancy: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["SpotInstanceRequestTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        user_data: typing.Optional[builtins.str] = None,
        user_data_base64: typing.Optional[builtins.str] = None,
        user_data_replace_on_change: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        valid_from: typing.Optional[builtins.str] = None,
        valid_until: typing.Optional[builtins.str] = None,
        volume_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        vpc_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        wait_for_fulfillment: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request aws_spot_instance_request} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param ami: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#ami SpotInstanceRequest#ami}.
        :param associate_public_ip_address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#associate_public_ip_address SpotInstanceRequest#associate_public_ip_address}.
        :param availability_zone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#availability_zone SpotInstanceRequest#availability_zone}.
        :param block_duration_minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#block_duration_minutes SpotInstanceRequest#block_duration_minutes}.
        :param capacity_reservation_specification: capacity_reservation_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#capacity_reservation_specification SpotInstanceRequest#capacity_reservation_specification}
        :param cpu_core_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#cpu_core_count SpotInstanceRequest#cpu_core_count}.
        :param cpu_threads_per_core: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#cpu_threads_per_core SpotInstanceRequest#cpu_threads_per_core}.
        :param credit_specification: credit_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#credit_specification SpotInstanceRequest#credit_specification}
        :param disable_api_stop: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#disable_api_stop SpotInstanceRequest#disable_api_stop}.
        :param disable_api_termination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#disable_api_termination SpotInstanceRequest#disable_api_termination}.
        :param ebs_block_device: ebs_block_device block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#ebs_block_device SpotInstanceRequest#ebs_block_device}
        :param ebs_optimized: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#ebs_optimized SpotInstanceRequest#ebs_optimized}.
        :param enclave_options: enclave_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#enclave_options SpotInstanceRequest#enclave_options}
        :param ephemeral_block_device: ephemeral_block_device block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#ephemeral_block_device SpotInstanceRequest#ephemeral_block_device}
        :param fetch_password_data: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#get_password_data SpotInstanceRequest#get_password_data}.
        :param hibernation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#hibernation SpotInstanceRequest#hibernation}.
        :param host_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#host_id SpotInstanceRequest#host_id}.
        :param host_resource_group_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#host_resource_group_arn SpotInstanceRequest#host_resource_group_arn}.
        :param iam_instance_profile: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#iam_instance_profile SpotInstanceRequest#iam_instance_profile}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#id SpotInstanceRequest#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param instance_initiated_shutdown_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#instance_initiated_shutdown_behavior SpotInstanceRequest#instance_initiated_shutdown_behavior}.
        :param instance_interruption_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#instance_interruption_behavior SpotInstanceRequest#instance_interruption_behavior}.
        :param instance_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#instance_type SpotInstanceRequest#instance_type}.
        :param ipv6_address_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#ipv6_address_count SpotInstanceRequest#ipv6_address_count}.
        :param ipv6_addresses: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#ipv6_addresses SpotInstanceRequest#ipv6_addresses}.
        :param key_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#key_name SpotInstanceRequest#key_name}.
        :param launch_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#launch_group SpotInstanceRequest#launch_group}.
        :param launch_template: launch_template block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#launch_template SpotInstanceRequest#launch_template}
        :param maintenance_options: maintenance_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#maintenance_options SpotInstanceRequest#maintenance_options}
        :param metadata_options: metadata_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#metadata_options SpotInstanceRequest#metadata_options}
        :param monitoring: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#monitoring SpotInstanceRequest#monitoring}.
        :param network_interface: network_interface block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#network_interface SpotInstanceRequest#network_interface}
        :param placement_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#placement_group SpotInstanceRequest#placement_group}.
        :param placement_partition_number: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#placement_partition_number SpotInstanceRequest#placement_partition_number}.
        :param private_dns_name_options: private_dns_name_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#private_dns_name_options SpotInstanceRequest#private_dns_name_options}
        :param private_ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#private_ip SpotInstanceRequest#private_ip}.
        :param root_block_device: root_block_device block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#root_block_device SpotInstanceRequest#root_block_device}
        :param secondary_private_ips: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#secondary_private_ips SpotInstanceRequest#secondary_private_ips}.
        :param security_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#security_groups SpotInstanceRequest#security_groups}.
        :param source_dest_check: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#source_dest_check SpotInstanceRequest#source_dest_check}.
        :param spot_price: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#spot_price SpotInstanceRequest#spot_price}.
        :param spot_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#spot_type SpotInstanceRequest#spot_type}.
        :param subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#subnet_id SpotInstanceRequest#subnet_id}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#tags SpotInstanceRequest#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#tags_all SpotInstanceRequest#tags_all}.
        :param tenancy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#tenancy SpotInstanceRequest#tenancy}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#timeouts SpotInstanceRequest#timeouts}
        :param user_data: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#user_data SpotInstanceRequest#user_data}.
        :param user_data_base64: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#user_data_base64 SpotInstanceRequest#user_data_base64}.
        :param user_data_replace_on_change: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#user_data_replace_on_change SpotInstanceRequest#user_data_replace_on_change}.
        :param valid_from: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#valid_from SpotInstanceRequest#valid_from}.
        :param valid_until: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#valid_until SpotInstanceRequest#valid_until}.
        :param volume_tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#volume_tags SpotInstanceRequest#volume_tags}.
        :param vpc_security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#vpc_security_group_ids SpotInstanceRequest#vpc_security_group_ids}.
        :param wait_for_fulfillment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#wait_for_fulfillment SpotInstanceRequest#wait_for_fulfillment}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25ea7dd1d51135d82eccce6caca2a8c8842ffb0c070bfd3aa088422f16e3446d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = SpotInstanceRequestConfig(
            ami=ami,
            associate_public_ip_address=associate_public_ip_address,
            availability_zone=availability_zone,
            block_duration_minutes=block_duration_minutes,
            capacity_reservation_specification=capacity_reservation_specification,
            cpu_core_count=cpu_core_count,
            cpu_threads_per_core=cpu_threads_per_core,
            credit_specification=credit_specification,
            disable_api_stop=disable_api_stop,
            disable_api_termination=disable_api_termination,
            ebs_block_device=ebs_block_device,
            ebs_optimized=ebs_optimized,
            enclave_options=enclave_options,
            ephemeral_block_device=ephemeral_block_device,
            fetch_password_data=fetch_password_data,
            hibernation=hibernation,
            host_id=host_id,
            host_resource_group_arn=host_resource_group_arn,
            iam_instance_profile=iam_instance_profile,
            id=id,
            instance_initiated_shutdown_behavior=instance_initiated_shutdown_behavior,
            instance_interruption_behavior=instance_interruption_behavior,
            instance_type=instance_type,
            ipv6_address_count=ipv6_address_count,
            ipv6_addresses=ipv6_addresses,
            key_name=key_name,
            launch_group=launch_group,
            launch_template=launch_template,
            maintenance_options=maintenance_options,
            metadata_options=metadata_options,
            monitoring=monitoring,
            network_interface=network_interface,
            placement_group=placement_group,
            placement_partition_number=placement_partition_number,
            private_dns_name_options=private_dns_name_options,
            private_ip=private_ip,
            root_block_device=root_block_device,
            secondary_private_ips=secondary_private_ips,
            security_groups=security_groups,
            source_dest_check=source_dest_check,
            spot_price=spot_price,
            spot_type=spot_type,
            subnet_id=subnet_id,
            tags=tags,
            tags_all=tags_all,
            tenancy=tenancy,
            timeouts=timeouts,
            user_data=user_data,
            user_data_base64=user_data_base64,
            user_data_replace_on_change=user_data_replace_on_change,
            valid_from=valid_from,
            valid_until=valid_until,
            volume_tags=volume_tags,
            vpc_security_group_ids=vpc_security_group_ids,
            wait_for_fulfillment=wait_for_fulfillment,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putCapacityReservationSpecification")
    def put_capacity_reservation_specification(
        self,
        *,
        capacity_reservation_preference: typing.Optional[builtins.str] = None,
        capacity_reservation_target: typing.Optional[typing.Union["SpotInstanceRequestCapacityReservationSpecificationCapacityReservationTarget", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param capacity_reservation_preference: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#capacity_reservation_preference SpotInstanceRequest#capacity_reservation_preference}.
        :param capacity_reservation_target: capacity_reservation_target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#capacity_reservation_target SpotInstanceRequest#capacity_reservation_target}
        '''
        value = SpotInstanceRequestCapacityReservationSpecification(
            capacity_reservation_preference=capacity_reservation_preference,
            capacity_reservation_target=capacity_reservation_target,
        )

        return typing.cast(None, jsii.invoke(self, "putCapacityReservationSpecification", [value]))

    @jsii.member(jsii_name="putCreditSpecification")
    def put_credit_specification(
        self,
        *,
        cpu_credits: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cpu_credits: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#cpu_credits SpotInstanceRequest#cpu_credits}.
        '''
        value = SpotInstanceRequestCreditSpecification(cpu_credits=cpu_credits)

        return typing.cast(None, jsii.invoke(self, "putCreditSpecification", [value]))

    @jsii.member(jsii_name="putEbsBlockDevice")
    def put_ebs_block_device(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SpotInstanceRequestEbsBlockDevice", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c7c5af28b5968250405d798a2b3a9d27933abb50b78c3f81735749389a795a4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putEbsBlockDevice", [value]))

    @jsii.member(jsii_name="putEnclaveOptions")
    def put_enclave_options(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#enabled SpotInstanceRequest#enabled}.
        '''
        value = SpotInstanceRequestEnclaveOptions(enabled=enabled)

        return typing.cast(None, jsii.invoke(self, "putEnclaveOptions", [value]))

    @jsii.member(jsii_name="putEphemeralBlockDevice")
    def put_ephemeral_block_device(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SpotInstanceRequestEphemeralBlockDevice", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1da975b60399bbb9ff8e2ad351a84b68dee671e0812fa83d4a76e0e26f5194d8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putEphemeralBlockDevice", [value]))

    @jsii.member(jsii_name="putLaunchTemplate")
    def put_launch_template(
        self,
        *,
        id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#id SpotInstanceRequest#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#name SpotInstanceRequest#name}.
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#version SpotInstanceRequest#version}.
        '''
        value = SpotInstanceRequestLaunchTemplate(id=id, name=name, version=version)

        return typing.cast(None, jsii.invoke(self, "putLaunchTemplate", [value]))

    @jsii.member(jsii_name="putMaintenanceOptions")
    def put_maintenance_options(
        self,
        *,
        auto_recovery: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param auto_recovery: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#auto_recovery SpotInstanceRequest#auto_recovery}.
        '''
        value = SpotInstanceRequestMaintenanceOptions(auto_recovery=auto_recovery)

        return typing.cast(None, jsii.invoke(self, "putMaintenanceOptions", [value]))

    @jsii.member(jsii_name="putMetadataOptions")
    def put_metadata_options(
        self,
        *,
        http_endpoint: typing.Optional[builtins.str] = None,
        http_put_response_hop_limit: typing.Optional[jsii.Number] = None,
        http_tokens: typing.Optional[builtins.str] = None,
        instance_metadata_tags: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param http_endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#http_endpoint SpotInstanceRequest#http_endpoint}.
        :param http_put_response_hop_limit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#http_put_response_hop_limit SpotInstanceRequest#http_put_response_hop_limit}.
        :param http_tokens: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#http_tokens SpotInstanceRequest#http_tokens}.
        :param instance_metadata_tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#instance_metadata_tags SpotInstanceRequest#instance_metadata_tags}.
        '''
        value = SpotInstanceRequestMetadataOptions(
            http_endpoint=http_endpoint,
            http_put_response_hop_limit=http_put_response_hop_limit,
            http_tokens=http_tokens,
            instance_metadata_tags=instance_metadata_tags,
        )

        return typing.cast(None, jsii.invoke(self, "putMetadataOptions", [value]))

    @jsii.member(jsii_name="putNetworkInterface")
    def put_network_interface(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SpotInstanceRequestNetworkInterface", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a002308f66e4cc08f67ad66ed7011b96da8bb68be771de2cabe7a60d1cf167e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNetworkInterface", [value]))

    @jsii.member(jsii_name="putPrivateDnsNameOptions")
    def put_private_dns_name_options(
        self,
        *,
        enable_resource_name_dns_aaaa_record: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_resource_name_dns_a_record: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        hostname_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enable_resource_name_dns_aaaa_record: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#enable_resource_name_dns_aaaa_record SpotInstanceRequest#enable_resource_name_dns_aaaa_record}.
        :param enable_resource_name_dns_a_record: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#enable_resource_name_dns_a_record SpotInstanceRequest#enable_resource_name_dns_a_record}.
        :param hostname_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#hostname_type SpotInstanceRequest#hostname_type}.
        '''
        value = SpotInstanceRequestPrivateDnsNameOptions(
            enable_resource_name_dns_aaaa_record=enable_resource_name_dns_aaaa_record,
            enable_resource_name_dns_a_record=enable_resource_name_dns_a_record,
            hostname_type=hostname_type,
        )

        return typing.cast(None, jsii.invoke(self, "putPrivateDnsNameOptions", [value]))

    @jsii.member(jsii_name="putRootBlockDevice")
    def put_root_block_device(
        self,
        *,
        delete_on_termination: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        encrypted: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        iops: typing.Optional[jsii.Number] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        throughput: typing.Optional[jsii.Number] = None,
        volume_size: typing.Optional[jsii.Number] = None,
        volume_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param delete_on_termination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#delete_on_termination SpotInstanceRequest#delete_on_termination}.
        :param encrypted: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#encrypted SpotInstanceRequest#encrypted}.
        :param iops: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#iops SpotInstanceRequest#iops}.
        :param kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#kms_key_id SpotInstanceRequest#kms_key_id}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#tags SpotInstanceRequest#tags}.
        :param throughput: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#throughput SpotInstanceRequest#throughput}.
        :param volume_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#volume_size SpotInstanceRequest#volume_size}.
        :param volume_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#volume_type SpotInstanceRequest#volume_type}.
        '''
        value = SpotInstanceRequestRootBlockDevice(
            delete_on_termination=delete_on_termination,
            encrypted=encrypted,
            iops=iops,
            kms_key_id=kms_key_id,
            tags=tags,
            throughput=throughput,
            volume_size=volume_size,
            volume_type=volume_type,
        )

        return typing.cast(None, jsii.invoke(self, "putRootBlockDevice", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#create SpotInstanceRequest#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#delete SpotInstanceRequest#delete}.
        '''
        value = SpotInstanceRequestTimeouts(create=create, delete=delete)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAmi")
    def reset_ami(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAmi", []))

    @jsii.member(jsii_name="resetAssociatePublicIpAddress")
    def reset_associate_public_ip_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAssociatePublicIpAddress", []))

    @jsii.member(jsii_name="resetAvailabilityZone")
    def reset_availability_zone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAvailabilityZone", []))

    @jsii.member(jsii_name="resetBlockDurationMinutes")
    def reset_block_duration_minutes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBlockDurationMinutes", []))

    @jsii.member(jsii_name="resetCapacityReservationSpecification")
    def reset_capacity_reservation_specification(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCapacityReservationSpecification", []))

    @jsii.member(jsii_name="resetCpuCoreCount")
    def reset_cpu_core_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCpuCoreCount", []))

    @jsii.member(jsii_name="resetCpuThreadsPerCore")
    def reset_cpu_threads_per_core(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCpuThreadsPerCore", []))

    @jsii.member(jsii_name="resetCreditSpecification")
    def reset_credit_specification(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreditSpecification", []))

    @jsii.member(jsii_name="resetDisableApiStop")
    def reset_disable_api_stop(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisableApiStop", []))

    @jsii.member(jsii_name="resetDisableApiTermination")
    def reset_disable_api_termination(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisableApiTermination", []))

    @jsii.member(jsii_name="resetEbsBlockDevice")
    def reset_ebs_block_device(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEbsBlockDevice", []))

    @jsii.member(jsii_name="resetEbsOptimized")
    def reset_ebs_optimized(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEbsOptimized", []))

    @jsii.member(jsii_name="resetEnclaveOptions")
    def reset_enclave_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnclaveOptions", []))

    @jsii.member(jsii_name="resetEphemeralBlockDevice")
    def reset_ephemeral_block_device(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEphemeralBlockDevice", []))

    @jsii.member(jsii_name="resetFetchPasswordData")
    def reset_fetch_password_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFetchPasswordData", []))

    @jsii.member(jsii_name="resetHibernation")
    def reset_hibernation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHibernation", []))

    @jsii.member(jsii_name="resetHostId")
    def reset_host_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostId", []))

    @jsii.member(jsii_name="resetHostResourceGroupArn")
    def reset_host_resource_group_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostResourceGroupArn", []))

    @jsii.member(jsii_name="resetIamInstanceProfile")
    def reset_iam_instance_profile(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIamInstanceProfile", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetInstanceInitiatedShutdownBehavior")
    def reset_instance_initiated_shutdown_behavior(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceInitiatedShutdownBehavior", []))

    @jsii.member(jsii_name="resetInstanceInterruptionBehavior")
    def reset_instance_interruption_behavior(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceInterruptionBehavior", []))

    @jsii.member(jsii_name="resetInstanceType")
    def reset_instance_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceType", []))

    @jsii.member(jsii_name="resetIpv6AddressCount")
    def reset_ipv6_address_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpv6AddressCount", []))

    @jsii.member(jsii_name="resetIpv6Addresses")
    def reset_ipv6_addresses(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpv6Addresses", []))

    @jsii.member(jsii_name="resetKeyName")
    def reset_key_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyName", []))

    @jsii.member(jsii_name="resetLaunchGroup")
    def reset_launch_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLaunchGroup", []))

    @jsii.member(jsii_name="resetLaunchTemplate")
    def reset_launch_template(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLaunchTemplate", []))

    @jsii.member(jsii_name="resetMaintenanceOptions")
    def reset_maintenance_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaintenanceOptions", []))

    @jsii.member(jsii_name="resetMetadataOptions")
    def reset_metadata_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetadataOptions", []))

    @jsii.member(jsii_name="resetMonitoring")
    def reset_monitoring(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMonitoring", []))

    @jsii.member(jsii_name="resetNetworkInterface")
    def reset_network_interface(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworkInterface", []))

    @jsii.member(jsii_name="resetPlacementGroup")
    def reset_placement_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPlacementGroup", []))

    @jsii.member(jsii_name="resetPlacementPartitionNumber")
    def reset_placement_partition_number(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPlacementPartitionNumber", []))

    @jsii.member(jsii_name="resetPrivateDnsNameOptions")
    def reset_private_dns_name_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateDnsNameOptions", []))

    @jsii.member(jsii_name="resetPrivateIp")
    def reset_private_ip(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateIp", []))

    @jsii.member(jsii_name="resetRootBlockDevice")
    def reset_root_block_device(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRootBlockDevice", []))

    @jsii.member(jsii_name="resetSecondaryPrivateIps")
    def reset_secondary_private_ips(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecondaryPrivateIps", []))

    @jsii.member(jsii_name="resetSecurityGroups")
    def reset_security_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecurityGroups", []))

    @jsii.member(jsii_name="resetSourceDestCheck")
    def reset_source_dest_check(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceDestCheck", []))

    @jsii.member(jsii_name="resetSpotPrice")
    def reset_spot_price(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSpotPrice", []))

    @jsii.member(jsii_name="resetSpotType")
    def reset_spot_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSpotType", []))

    @jsii.member(jsii_name="resetSubnetId")
    def reset_subnet_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubnetId", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetTenancy")
    def reset_tenancy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTenancy", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetUserData")
    def reset_user_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserData", []))

    @jsii.member(jsii_name="resetUserDataBase64")
    def reset_user_data_base64(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserDataBase64", []))

    @jsii.member(jsii_name="resetUserDataReplaceOnChange")
    def reset_user_data_replace_on_change(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserDataReplaceOnChange", []))

    @jsii.member(jsii_name="resetValidFrom")
    def reset_valid_from(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValidFrom", []))

    @jsii.member(jsii_name="resetValidUntil")
    def reset_valid_until(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValidUntil", []))

    @jsii.member(jsii_name="resetVolumeTags")
    def reset_volume_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVolumeTags", []))

    @jsii.member(jsii_name="resetVpcSecurityGroupIds")
    def reset_vpc_security_group_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVpcSecurityGroupIds", []))

    @jsii.member(jsii_name="resetWaitForFulfillment")
    def reset_wait_for_fulfillment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWaitForFulfillment", []))

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
    @jsii.member(jsii_name="capacityReservationSpecification")
    def capacity_reservation_specification(
        self,
    ) -> "SpotInstanceRequestCapacityReservationSpecificationOutputReference":
        return typing.cast("SpotInstanceRequestCapacityReservationSpecificationOutputReference", jsii.get(self, "capacityReservationSpecification"))

    @builtins.property
    @jsii.member(jsii_name="creditSpecification")
    def credit_specification(
        self,
    ) -> "SpotInstanceRequestCreditSpecificationOutputReference":
        return typing.cast("SpotInstanceRequestCreditSpecificationOutputReference", jsii.get(self, "creditSpecification"))

    @builtins.property
    @jsii.member(jsii_name="ebsBlockDevice")
    def ebs_block_device(self) -> "SpotInstanceRequestEbsBlockDeviceList":
        return typing.cast("SpotInstanceRequestEbsBlockDeviceList", jsii.get(self, "ebsBlockDevice"))

    @builtins.property
    @jsii.member(jsii_name="enclaveOptions")
    def enclave_options(self) -> "SpotInstanceRequestEnclaveOptionsOutputReference":
        return typing.cast("SpotInstanceRequestEnclaveOptionsOutputReference", jsii.get(self, "enclaveOptions"))

    @builtins.property
    @jsii.member(jsii_name="ephemeralBlockDevice")
    def ephemeral_block_device(self) -> "SpotInstanceRequestEphemeralBlockDeviceList":
        return typing.cast("SpotInstanceRequestEphemeralBlockDeviceList", jsii.get(self, "ephemeralBlockDevice"))

    @builtins.property
    @jsii.member(jsii_name="instanceState")
    def instance_state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceState"))

    @builtins.property
    @jsii.member(jsii_name="launchTemplate")
    def launch_template(self) -> "SpotInstanceRequestLaunchTemplateOutputReference":
        return typing.cast("SpotInstanceRequestLaunchTemplateOutputReference", jsii.get(self, "launchTemplate"))

    @builtins.property
    @jsii.member(jsii_name="maintenanceOptions")
    def maintenance_options(
        self,
    ) -> "SpotInstanceRequestMaintenanceOptionsOutputReference":
        return typing.cast("SpotInstanceRequestMaintenanceOptionsOutputReference", jsii.get(self, "maintenanceOptions"))

    @builtins.property
    @jsii.member(jsii_name="metadataOptions")
    def metadata_options(self) -> "SpotInstanceRequestMetadataOptionsOutputReference":
        return typing.cast("SpotInstanceRequestMetadataOptionsOutputReference", jsii.get(self, "metadataOptions"))

    @builtins.property
    @jsii.member(jsii_name="networkInterface")
    def network_interface(self) -> "SpotInstanceRequestNetworkInterfaceList":
        return typing.cast("SpotInstanceRequestNetworkInterfaceList", jsii.get(self, "networkInterface"))

    @builtins.property
    @jsii.member(jsii_name="outpostArn")
    def outpost_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "outpostArn"))

    @builtins.property
    @jsii.member(jsii_name="passwordData")
    def password_data(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "passwordData"))

    @builtins.property
    @jsii.member(jsii_name="primaryNetworkInterfaceId")
    def primary_network_interface_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "primaryNetworkInterfaceId"))

    @builtins.property
    @jsii.member(jsii_name="privateDns")
    def private_dns(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateDns"))

    @builtins.property
    @jsii.member(jsii_name="privateDnsNameOptions")
    def private_dns_name_options(
        self,
    ) -> "SpotInstanceRequestPrivateDnsNameOptionsOutputReference":
        return typing.cast("SpotInstanceRequestPrivateDnsNameOptionsOutputReference", jsii.get(self, "privateDnsNameOptions"))

    @builtins.property
    @jsii.member(jsii_name="publicDns")
    def public_dns(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publicDns"))

    @builtins.property
    @jsii.member(jsii_name="publicIp")
    def public_ip(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publicIp"))

    @builtins.property
    @jsii.member(jsii_name="rootBlockDevice")
    def root_block_device(self) -> "SpotInstanceRequestRootBlockDeviceOutputReference":
        return typing.cast("SpotInstanceRequestRootBlockDeviceOutputReference", jsii.get(self, "rootBlockDevice"))

    @builtins.property
    @jsii.member(jsii_name="spotBidStatus")
    def spot_bid_status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "spotBidStatus"))

    @builtins.property
    @jsii.member(jsii_name="spotInstanceId")
    def spot_instance_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "spotInstanceId"))

    @builtins.property
    @jsii.member(jsii_name="spotRequestState")
    def spot_request_state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "spotRequestState"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "SpotInstanceRequestTimeoutsOutputReference":
        return typing.cast("SpotInstanceRequestTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="amiInput")
    def ami_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "amiInput"))

    @builtins.property
    @jsii.member(jsii_name="associatePublicIpAddressInput")
    def associate_public_ip_address_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "associatePublicIpAddressInput"))

    @builtins.property
    @jsii.member(jsii_name="availabilityZoneInput")
    def availability_zone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "availabilityZoneInput"))

    @builtins.property
    @jsii.member(jsii_name="blockDurationMinutesInput")
    def block_duration_minutes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "blockDurationMinutesInput"))

    @builtins.property
    @jsii.member(jsii_name="capacityReservationSpecificationInput")
    def capacity_reservation_specification_input(
        self,
    ) -> typing.Optional["SpotInstanceRequestCapacityReservationSpecification"]:
        return typing.cast(typing.Optional["SpotInstanceRequestCapacityReservationSpecification"], jsii.get(self, "capacityReservationSpecificationInput"))

    @builtins.property
    @jsii.member(jsii_name="cpuCoreCountInput")
    def cpu_core_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "cpuCoreCountInput"))

    @builtins.property
    @jsii.member(jsii_name="cpuThreadsPerCoreInput")
    def cpu_threads_per_core_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "cpuThreadsPerCoreInput"))

    @builtins.property
    @jsii.member(jsii_name="creditSpecificationInput")
    def credit_specification_input(
        self,
    ) -> typing.Optional["SpotInstanceRequestCreditSpecification"]:
        return typing.cast(typing.Optional["SpotInstanceRequestCreditSpecification"], jsii.get(self, "creditSpecificationInput"))

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
    @jsii.member(jsii_name="ebsBlockDeviceInput")
    def ebs_block_device_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SpotInstanceRequestEbsBlockDevice"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SpotInstanceRequestEbsBlockDevice"]]], jsii.get(self, "ebsBlockDeviceInput"))

    @builtins.property
    @jsii.member(jsii_name="ebsOptimizedInput")
    def ebs_optimized_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "ebsOptimizedInput"))

    @builtins.property
    @jsii.member(jsii_name="enclaveOptionsInput")
    def enclave_options_input(
        self,
    ) -> typing.Optional["SpotInstanceRequestEnclaveOptions"]:
        return typing.cast(typing.Optional["SpotInstanceRequestEnclaveOptions"], jsii.get(self, "enclaveOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="ephemeralBlockDeviceInput")
    def ephemeral_block_device_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SpotInstanceRequestEphemeralBlockDevice"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SpotInstanceRequestEphemeralBlockDevice"]]], jsii.get(self, "ephemeralBlockDeviceInput"))

    @builtins.property
    @jsii.member(jsii_name="fetchPasswordDataInput")
    def fetch_password_data_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "fetchPasswordDataInput"))

    @builtins.property
    @jsii.member(jsii_name="hibernationInput")
    def hibernation_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "hibernationInput"))

    @builtins.property
    @jsii.member(jsii_name="hostIdInput")
    def host_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostIdInput"))

    @builtins.property
    @jsii.member(jsii_name="hostResourceGroupArnInput")
    def host_resource_group_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostResourceGroupArnInput"))

    @builtins.property
    @jsii.member(jsii_name="iamInstanceProfileInput")
    def iam_instance_profile_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "iamInstanceProfileInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceInitiatedShutdownBehaviorInput")
    def instance_initiated_shutdown_behavior_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceInitiatedShutdownBehaviorInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceInterruptionBehaviorInput")
    def instance_interruption_behavior_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceInterruptionBehaviorInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceTypeInput")
    def instance_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="ipv6AddressCountInput")
    def ipv6_address_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ipv6AddressCountInput"))

    @builtins.property
    @jsii.member(jsii_name="ipv6AddressesInput")
    def ipv6_addresses_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "ipv6AddressesInput"))

    @builtins.property
    @jsii.member(jsii_name="keyNameInput")
    def key_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyNameInput"))

    @builtins.property
    @jsii.member(jsii_name="launchGroupInput")
    def launch_group_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "launchGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="launchTemplateInput")
    def launch_template_input(
        self,
    ) -> typing.Optional["SpotInstanceRequestLaunchTemplate"]:
        return typing.cast(typing.Optional["SpotInstanceRequestLaunchTemplate"], jsii.get(self, "launchTemplateInput"))

    @builtins.property
    @jsii.member(jsii_name="maintenanceOptionsInput")
    def maintenance_options_input(
        self,
    ) -> typing.Optional["SpotInstanceRequestMaintenanceOptions"]:
        return typing.cast(typing.Optional["SpotInstanceRequestMaintenanceOptions"], jsii.get(self, "maintenanceOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="metadataOptionsInput")
    def metadata_options_input(
        self,
    ) -> typing.Optional["SpotInstanceRequestMetadataOptions"]:
        return typing.cast(typing.Optional["SpotInstanceRequestMetadataOptions"], jsii.get(self, "metadataOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="monitoringInput")
    def monitoring_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "monitoringInput"))

    @builtins.property
    @jsii.member(jsii_name="networkInterfaceInput")
    def network_interface_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SpotInstanceRequestNetworkInterface"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SpotInstanceRequestNetworkInterface"]]], jsii.get(self, "networkInterfaceInput"))

    @builtins.property
    @jsii.member(jsii_name="placementGroupInput")
    def placement_group_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "placementGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="placementPartitionNumberInput")
    def placement_partition_number_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "placementPartitionNumberInput"))

    @builtins.property
    @jsii.member(jsii_name="privateDnsNameOptionsInput")
    def private_dns_name_options_input(
        self,
    ) -> typing.Optional["SpotInstanceRequestPrivateDnsNameOptions"]:
        return typing.cast(typing.Optional["SpotInstanceRequestPrivateDnsNameOptions"], jsii.get(self, "privateDnsNameOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="privateIpInput")
    def private_ip_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateIpInput"))

    @builtins.property
    @jsii.member(jsii_name="rootBlockDeviceInput")
    def root_block_device_input(
        self,
    ) -> typing.Optional["SpotInstanceRequestRootBlockDevice"]:
        return typing.cast(typing.Optional["SpotInstanceRequestRootBlockDevice"], jsii.get(self, "rootBlockDeviceInput"))

    @builtins.property
    @jsii.member(jsii_name="secondaryPrivateIpsInput")
    def secondary_private_ips_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "secondaryPrivateIpsInput"))

    @builtins.property
    @jsii.member(jsii_name="securityGroupsInput")
    def security_groups_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceDestCheckInput")
    def source_dest_check_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "sourceDestCheckInput"))

    @builtins.property
    @jsii.member(jsii_name="spotPriceInput")
    def spot_price_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "spotPriceInput"))

    @builtins.property
    @jsii.member(jsii_name="spotTypeInput")
    def spot_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "spotTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetIdInput")
    def subnet_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subnetIdInput"))

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
    @jsii.member(jsii_name="tenancyInput")
    def tenancy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tenancyInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["SpotInstanceRequestTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["SpotInstanceRequestTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="userDataBase64Input")
    def user_data_base64_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userDataBase64Input"))

    @builtins.property
    @jsii.member(jsii_name="userDataInput")
    def user_data_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userDataInput"))

    @builtins.property
    @jsii.member(jsii_name="userDataReplaceOnChangeInput")
    def user_data_replace_on_change_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "userDataReplaceOnChangeInput"))

    @builtins.property
    @jsii.member(jsii_name="validFromInput")
    def valid_from_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "validFromInput"))

    @builtins.property
    @jsii.member(jsii_name="validUntilInput")
    def valid_until_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "validUntilInput"))

    @builtins.property
    @jsii.member(jsii_name="volumeTagsInput")
    def volume_tags_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "volumeTagsInput"))

    @builtins.property
    @jsii.member(jsii_name="vpcSecurityGroupIdsInput")
    def vpc_security_group_ids_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "vpcSecurityGroupIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="waitForFulfillmentInput")
    def wait_for_fulfillment_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "waitForFulfillmentInput"))

    @builtins.property
    @jsii.member(jsii_name="ami")
    def ami(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ami"))

    @ami.setter
    def ami(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__182b53f86c7b5156dcc95d10cf8292ca8dfe2efa92a1f5a56f67f7b5fb05fbd7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ami", value)

    @builtins.property
    @jsii.member(jsii_name="associatePublicIpAddress")
    def associate_public_ip_address(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "associatePublicIpAddress"))

    @associate_public_ip_address.setter
    def associate_public_ip_address(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ac2fa63b20b5b772d4b30634b7c9efc26342739ec1439c6cbfeae9ac2bdb8d6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "associatePublicIpAddress", value)

    @builtins.property
    @jsii.member(jsii_name="availabilityZone")
    def availability_zone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "availabilityZone"))

    @availability_zone.setter
    def availability_zone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4ce12b17b0376fbd5fe38c90ada79b82ce473ac9aeeb096d030fb4da5af32d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availabilityZone", value)

    @builtins.property
    @jsii.member(jsii_name="blockDurationMinutes")
    def block_duration_minutes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "blockDurationMinutes"))

    @block_duration_minutes.setter
    def block_duration_minutes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7dbfc636165504c887300da45cb103da42dc62515ba5379690a7c5e94a461a4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "blockDurationMinutes", value)

    @builtins.property
    @jsii.member(jsii_name="cpuCoreCount")
    def cpu_core_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "cpuCoreCount"))

    @cpu_core_count.setter
    def cpu_core_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b73dc530974b9ba18f3083557856d4cd63243cceb42bfdcd8fcd2efaf9ab4cd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpuCoreCount", value)

    @builtins.property
    @jsii.member(jsii_name="cpuThreadsPerCore")
    def cpu_threads_per_core(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "cpuThreadsPerCore"))

    @cpu_threads_per_core.setter
    def cpu_threads_per_core(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d63c81d404735cd6c986c71b6ab1813656009d50f179eade3148a2bda4d61039)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpuThreadsPerCore", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__906e29a235f7d3473eb047a188f56da1263bdcdba2a1a0bf831b43db0d3c3e87)
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
            type_hints = typing.get_type_hints(_typecheckingstub__bfff62e582a7238b1cde671d447128bf0c12419f869379a4b9a14ca482023f6f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableApiTermination", value)

    @builtins.property
    @jsii.member(jsii_name="ebsOptimized")
    def ebs_optimized(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "ebsOptimized"))

    @ebs_optimized.setter
    def ebs_optimized(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__575eed9637b9d7f394ca033f8e0a67e69693611ba57f92db69cd12304c5b4e78)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ebsOptimized", value)

    @builtins.property
    @jsii.member(jsii_name="fetchPasswordData")
    def fetch_password_data(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "fetchPasswordData"))

    @fetch_password_data.setter
    def fetch_password_data(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0288801e82b5ffc7ca3a96a00432098aa97e926f1410362aa053af8934ddca1f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fetchPasswordData", value)

    @builtins.property
    @jsii.member(jsii_name="hibernation")
    def hibernation(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "hibernation"))

    @hibernation.setter
    def hibernation(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb3e45944d2852715e060f3097048d0c12983b9de1a66a24217d7655d49fb79f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hibernation", value)

    @builtins.property
    @jsii.member(jsii_name="hostId")
    def host_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostId"))

    @host_id.setter
    def host_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b4afef057bae9d76daee52d750671df9fcf93e67964ae5dcd5e02b4fb2a820c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostId", value)

    @builtins.property
    @jsii.member(jsii_name="hostResourceGroupArn")
    def host_resource_group_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostResourceGroupArn"))

    @host_resource_group_arn.setter
    def host_resource_group_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e589a4cd78082ee1138bb6776ab6f782e46fa42d184d2c3aab2e1ce13ab1a4f0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostResourceGroupArn", value)

    @builtins.property
    @jsii.member(jsii_name="iamInstanceProfile")
    def iam_instance_profile(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "iamInstanceProfile"))

    @iam_instance_profile.setter
    def iam_instance_profile(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2be21761676471da55c278ddb70ea9e1b4866dac06bc20c7f104d4592d596e4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iamInstanceProfile", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e660632944fb773681ad2de576827caf0ba87093b5e927939f9ff67d52cbc6cf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="instanceInitiatedShutdownBehavior")
    def instance_initiated_shutdown_behavior(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceInitiatedShutdownBehavior"))

    @instance_initiated_shutdown_behavior.setter
    def instance_initiated_shutdown_behavior(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__88277119fd2f3feb077c0f6a9334cfb9789443b51f1ae26feb7b49844ba9f442)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceInitiatedShutdownBehavior", value)

    @builtins.property
    @jsii.member(jsii_name="instanceInterruptionBehavior")
    def instance_interruption_behavior(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceInterruptionBehavior"))

    @instance_interruption_behavior.setter
    def instance_interruption_behavior(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39e499c03221c9cca8c75dd807379de463e884ab29335beb7beb7ed617826f7a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceInterruptionBehavior", value)

    @builtins.property
    @jsii.member(jsii_name="instanceType")
    def instance_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceType"))

    @instance_type.setter
    def instance_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57ef8df493d52ffd14205ed3b810c5f754967d6a5d3e15df3bd73bc7b776c62d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceType", value)

    @builtins.property
    @jsii.member(jsii_name="ipv6AddressCount")
    def ipv6_address_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ipv6AddressCount"))

    @ipv6_address_count.setter
    def ipv6_address_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__508c91e20ad825bba97bfe7073d9b706a2a684580737d4e0bf305e257dc043e4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipv6AddressCount", value)

    @builtins.property
    @jsii.member(jsii_name="ipv6Addresses")
    def ipv6_addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "ipv6Addresses"))

    @ipv6_addresses.setter
    def ipv6_addresses(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__996d5834e3831763ea41c5675c14f684c6842874ea1327f818b09a58a0260aaf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipv6Addresses", value)

    @builtins.property
    @jsii.member(jsii_name="keyName")
    def key_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyName"))

    @key_name.setter
    def key_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14f96b4d879f552fb24ed3408bab2c67b306d2b8b4f04ad0b9db4564c94b203b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyName", value)

    @builtins.property
    @jsii.member(jsii_name="launchGroup")
    def launch_group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "launchGroup"))

    @launch_group.setter
    def launch_group(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__867903f29a9c80452a38d65dce39fe410353a3ca1dd054149cae7d595cae0814)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "launchGroup", value)

    @builtins.property
    @jsii.member(jsii_name="monitoring")
    def monitoring(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "monitoring"))

    @monitoring.setter
    def monitoring(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1786aceda2a9257d385621efab8d2baaed871d1d24d790332a97531e14d21acb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "monitoring", value)

    @builtins.property
    @jsii.member(jsii_name="placementGroup")
    def placement_group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "placementGroup"))

    @placement_group.setter
    def placement_group(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a115e3e1b68650cc470380a96bee704824fb2abc6b5a63ecc6589361d0280804)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "placementGroup", value)

    @builtins.property
    @jsii.member(jsii_name="placementPartitionNumber")
    def placement_partition_number(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "placementPartitionNumber"))

    @placement_partition_number.setter
    def placement_partition_number(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac5815e205e57684085e04c297c791dace2c57bc2db59cd7f674956dd4a30709)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "placementPartitionNumber", value)

    @builtins.property
    @jsii.member(jsii_name="privateIp")
    def private_ip(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateIp"))

    @private_ip.setter
    def private_ip(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3566d9970b84df6c7248a3a366f4db4c9af00052716159d0c083939164a97288)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateIp", value)

    @builtins.property
    @jsii.member(jsii_name="secondaryPrivateIps")
    def secondary_private_ips(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "secondaryPrivateIps"))

    @secondary_private_ips.setter
    def secondary_private_ips(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d030a08f7408ed782c7b6dc1260f5741e6ec0a5d6a0c3696331039415f07afc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secondaryPrivateIps", value)

    @builtins.property
    @jsii.member(jsii_name="securityGroups")
    def security_groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "securityGroups"))

    @security_groups.setter
    def security_groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b9309a9a46b20c2abd72fee01a58baf1f4769e40f5ef6b01db285fe0492e2e5a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroups", value)

    @builtins.property
    @jsii.member(jsii_name="sourceDestCheck")
    def source_dest_check(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "sourceDestCheck"))

    @source_dest_check.setter
    def source_dest_check(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70be4526538199668d949e05763ead00e7c87b544cda6b596362606d3cfe1537)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceDestCheck", value)

    @builtins.property
    @jsii.member(jsii_name="spotPrice")
    def spot_price(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "spotPrice"))

    @spot_price.setter
    def spot_price(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c9a415deea11aa3d3b313ab49a8774a05c449853344cfa32f8ef6a894dd938e1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "spotPrice", value)

    @builtins.property
    @jsii.member(jsii_name="spotType")
    def spot_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "spotType"))

    @spot_type.setter
    def spot_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__923fc0a07b1db51126f585646201a723cb3a35f70f60a696bcb283e911f5dc9a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "spotType", value)

    @builtins.property
    @jsii.member(jsii_name="subnetId")
    def subnet_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subnetId"))

    @subnet_id.setter
    def subnet_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__768d91fc4a33d180f1c7c193d95ad7f3ac4654dc63db596cbc4c848d9520a9ba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetId", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f59101e1e596058735fb225299a06713cdec64973b4aaf54f33ca6d341a5c47f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d75d4631cd2eaf31b511a874c034eddecbbaf72032555431772e0e8dd13b70f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)

    @builtins.property
    @jsii.member(jsii_name="tenancy")
    def tenancy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tenancy"))

    @tenancy.setter
    def tenancy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2533851e9c5f66e4bf9996582123ef73c1ee11c4c39f52e6360b912ecc586d8d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tenancy", value)

    @builtins.property
    @jsii.member(jsii_name="userData")
    def user_data(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userData"))

    @user_data.setter
    def user_data(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3de817635d31a2a2213c4b47df3d6081642f4e296c260ea589aae1bb735e3bd1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userData", value)

    @builtins.property
    @jsii.member(jsii_name="userDataBase64")
    def user_data_base64(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userDataBase64"))

    @user_data_base64.setter
    def user_data_base64(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__671a106cf39e77ddbfe6feb3d3763f994a21f85c724eb9d2ab4dc8c681bb9c18)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userDataBase64", value)

    @builtins.property
    @jsii.member(jsii_name="userDataReplaceOnChange")
    def user_data_replace_on_change(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "userDataReplaceOnChange"))

    @user_data_replace_on_change.setter
    def user_data_replace_on_change(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__046eb88ac82edf7c740130d087cca435b0da9ebf8091e2156be14e30123cf8d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userDataReplaceOnChange", value)

    @builtins.property
    @jsii.member(jsii_name="validFrom")
    def valid_from(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "validFrom"))

    @valid_from.setter
    def valid_from(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2dbcba76945a76a60592bc4815caf8384b816f8ed030eb1b4d86176535cf8e8a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "validFrom", value)

    @builtins.property
    @jsii.member(jsii_name="validUntil")
    def valid_until(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "validUntil"))

    @valid_until.setter
    def valid_until(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66fc6970806e5b56a655aa3239e2fe87c51e0bf4c6d8f751311637ade3af77b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "validUntil", value)

    @builtins.property
    @jsii.member(jsii_name="volumeTags")
    def volume_tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "volumeTags"))

    @volume_tags.setter
    def volume_tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5fddbeeca69d843de21529c29f9c09cba370c88404a47cb9b8a783dff8261f00)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeTags", value)

    @builtins.property
    @jsii.member(jsii_name="vpcSecurityGroupIds")
    def vpc_security_group_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "vpcSecurityGroupIds"))

    @vpc_security_group_ids.setter
    def vpc_security_group_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad369ab838cb2dfc845f13ba890d359d51ca84021c1f62fec5065e7f0e9d7596)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcSecurityGroupIds", value)

    @builtins.property
    @jsii.member(jsii_name="waitForFulfillment")
    def wait_for_fulfillment(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "waitForFulfillment"))

    @wait_for_fulfillment.setter
    def wait_for_fulfillment(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b0b29defa5f86ac71a91e0cfd9419de1cb4b3cd2d25e632478ccfe99950da74)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "waitForFulfillment", value)


@jsii.data_type(
    jsii_type="aws.spotInstanceRequest.SpotInstanceRequestCapacityReservationSpecification",
    jsii_struct_bases=[],
    name_mapping={
        "capacity_reservation_preference": "capacityReservationPreference",
        "capacity_reservation_target": "capacityReservationTarget",
    },
)
class SpotInstanceRequestCapacityReservationSpecification:
    def __init__(
        self,
        *,
        capacity_reservation_preference: typing.Optional[builtins.str] = None,
        capacity_reservation_target: typing.Optional[typing.Union["SpotInstanceRequestCapacityReservationSpecificationCapacityReservationTarget", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param capacity_reservation_preference: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#capacity_reservation_preference SpotInstanceRequest#capacity_reservation_preference}.
        :param capacity_reservation_target: capacity_reservation_target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#capacity_reservation_target SpotInstanceRequest#capacity_reservation_target}
        '''
        if isinstance(capacity_reservation_target, dict):
            capacity_reservation_target = SpotInstanceRequestCapacityReservationSpecificationCapacityReservationTarget(**capacity_reservation_target)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e6c692a08eb8853820728c6b38efcae4dd708789049cca8eeeb3b5d0a0ff222)
            check_type(argname="argument capacity_reservation_preference", value=capacity_reservation_preference, expected_type=type_hints["capacity_reservation_preference"])
            check_type(argname="argument capacity_reservation_target", value=capacity_reservation_target, expected_type=type_hints["capacity_reservation_target"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if capacity_reservation_preference is not None:
            self._values["capacity_reservation_preference"] = capacity_reservation_preference
        if capacity_reservation_target is not None:
            self._values["capacity_reservation_target"] = capacity_reservation_target

    @builtins.property
    def capacity_reservation_preference(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#capacity_reservation_preference SpotInstanceRequest#capacity_reservation_preference}.'''
        result = self._values.get("capacity_reservation_preference")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def capacity_reservation_target(
        self,
    ) -> typing.Optional["SpotInstanceRequestCapacityReservationSpecificationCapacityReservationTarget"]:
        '''capacity_reservation_target block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#capacity_reservation_target SpotInstanceRequest#capacity_reservation_target}
        '''
        result = self._values.get("capacity_reservation_target")
        return typing.cast(typing.Optional["SpotInstanceRequestCapacityReservationSpecificationCapacityReservationTarget"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SpotInstanceRequestCapacityReservationSpecification(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.spotInstanceRequest.SpotInstanceRequestCapacityReservationSpecificationCapacityReservationTarget",
    jsii_struct_bases=[],
    name_mapping={
        "capacity_reservation_id": "capacityReservationId",
        "capacity_reservation_resource_group_arn": "capacityReservationResourceGroupArn",
    },
)
class SpotInstanceRequestCapacityReservationSpecificationCapacityReservationTarget:
    def __init__(
        self,
        *,
        capacity_reservation_id: typing.Optional[builtins.str] = None,
        capacity_reservation_resource_group_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param capacity_reservation_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#capacity_reservation_id SpotInstanceRequest#capacity_reservation_id}.
        :param capacity_reservation_resource_group_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#capacity_reservation_resource_group_arn SpotInstanceRequest#capacity_reservation_resource_group_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7673c17457331e0fed6e1f8468ae8dbe83ada5c9229fdac24bfdb2b45f504843)
            check_type(argname="argument capacity_reservation_id", value=capacity_reservation_id, expected_type=type_hints["capacity_reservation_id"])
            check_type(argname="argument capacity_reservation_resource_group_arn", value=capacity_reservation_resource_group_arn, expected_type=type_hints["capacity_reservation_resource_group_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if capacity_reservation_id is not None:
            self._values["capacity_reservation_id"] = capacity_reservation_id
        if capacity_reservation_resource_group_arn is not None:
            self._values["capacity_reservation_resource_group_arn"] = capacity_reservation_resource_group_arn

    @builtins.property
    def capacity_reservation_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#capacity_reservation_id SpotInstanceRequest#capacity_reservation_id}.'''
        result = self._values.get("capacity_reservation_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def capacity_reservation_resource_group_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#capacity_reservation_resource_group_arn SpotInstanceRequest#capacity_reservation_resource_group_arn}.'''
        result = self._values.get("capacity_reservation_resource_group_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SpotInstanceRequestCapacityReservationSpecificationCapacityReservationTarget(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SpotInstanceRequestCapacityReservationSpecificationCapacityReservationTargetOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.spotInstanceRequest.SpotInstanceRequestCapacityReservationSpecificationCapacityReservationTargetOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__fba7fc93adcc4725fb031196c31ff2bd5c1db79805db60bd2509e06a78a909d7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9b442a3490e5979d150afe94485aa46e704ef813dd833b857253579458555437)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "capacityReservationId", value)

    @builtins.property
    @jsii.member(jsii_name="capacityReservationResourceGroupArn")
    def capacity_reservation_resource_group_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "capacityReservationResourceGroupArn"))

    @capacity_reservation_resource_group_arn.setter
    def capacity_reservation_resource_group_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c892d45b1f4ede7710ef682daecca0cbb2baf34cf6fd17c7cfce43649bf222f0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "capacityReservationResourceGroupArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SpotInstanceRequestCapacityReservationSpecificationCapacityReservationTarget]:
        return typing.cast(typing.Optional[SpotInstanceRequestCapacityReservationSpecificationCapacityReservationTarget], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SpotInstanceRequestCapacityReservationSpecificationCapacityReservationTarget],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2fb82879285e6f8d1574be347ff7a89a5a666caae462a546ee27c3270e7bf099)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SpotInstanceRequestCapacityReservationSpecificationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.spotInstanceRequest.SpotInstanceRequestCapacityReservationSpecificationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a7dd9c42729bd67b9a38ec3099fb8db80fdc838e4cda19aec33748783a7f5555)
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
        :param capacity_reservation_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#capacity_reservation_id SpotInstanceRequest#capacity_reservation_id}.
        :param capacity_reservation_resource_group_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#capacity_reservation_resource_group_arn SpotInstanceRequest#capacity_reservation_resource_group_arn}.
        '''
        value = SpotInstanceRequestCapacityReservationSpecificationCapacityReservationTarget(
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
    ) -> SpotInstanceRequestCapacityReservationSpecificationCapacityReservationTargetOutputReference:
        return typing.cast(SpotInstanceRequestCapacityReservationSpecificationCapacityReservationTargetOutputReference, jsii.get(self, "capacityReservationTarget"))

    @builtins.property
    @jsii.member(jsii_name="capacityReservationPreferenceInput")
    def capacity_reservation_preference_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "capacityReservationPreferenceInput"))

    @builtins.property
    @jsii.member(jsii_name="capacityReservationTargetInput")
    def capacity_reservation_target_input(
        self,
    ) -> typing.Optional[SpotInstanceRequestCapacityReservationSpecificationCapacityReservationTarget]:
        return typing.cast(typing.Optional[SpotInstanceRequestCapacityReservationSpecificationCapacityReservationTarget], jsii.get(self, "capacityReservationTargetInput"))

    @builtins.property
    @jsii.member(jsii_name="capacityReservationPreference")
    def capacity_reservation_preference(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "capacityReservationPreference"))

    @capacity_reservation_preference.setter
    def capacity_reservation_preference(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e385f10f7c53e00992612e3d45e325154636cc5a806d83b5f4e2f971173c91ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "capacityReservationPreference", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SpotInstanceRequestCapacityReservationSpecification]:
        return typing.cast(typing.Optional[SpotInstanceRequestCapacityReservationSpecification], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SpotInstanceRequestCapacityReservationSpecification],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a905a7919ea9d2bfc88162aa5aa2895721c27a44c700e506f639c45e4662868)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.spotInstanceRequest.SpotInstanceRequestConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "ami": "ami",
        "associate_public_ip_address": "associatePublicIpAddress",
        "availability_zone": "availabilityZone",
        "block_duration_minutes": "blockDurationMinutes",
        "capacity_reservation_specification": "capacityReservationSpecification",
        "cpu_core_count": "cpuCoreCount",
        "cpu_threads_per_core": "cpuThreadsPerCore",
        "credit_specification": "creditSpecification",
        "disable_api_stop": "disableApiStop",
        "disable_api_termination": "disableApiTermination",
        "ebs_block_device": "ebsBlockDevice",
        "ebs_optimized": "ebsOptimized",
        "enclave_options": "enclaveOptions",
        "ephemeral_block_device": "ephemeralBlockDevice",
        "fetch_password_data": "fetchPasswordData",
        "hibernation": "hibernation",
        "host_id": "hostId",
        "host_resource_group_arn": "hostResourceGroupArn",
        "iam_instance_profile": "iamInstanceProfile",
        "id": "id",
        "instance_initiated_shutdown_behavior": "instanceInitiatedShutdownBehavior",
        "instance_interruption_behavior": "instanceInterruptionBehavior",
        "instance_type": "instanceType",
        "ipv6_address_count": "ipv6AddressCount",
        "ipv6_addresses": "ipv6Addresses",
        "key_name": "keyName",
        "launch_group": "launchGroup",
        "launch_template": "launchTemplate",
        "maintenance_options": "maintenanceOptions",
        "metadata_options": "metadataOptions",
        "monitoring": "monitoring",
        "network_interface": "networkInterface",
        "placement_group": "placementGroup",
        "placement_partition_number": "placementPartitionNumber",
        "private_dns_name_options": "privateDnsNameOptions",
        "private_ip": "privateIp",
        "root_block_device": "rootBlockDevice",
        "secondary_private_ips": "secondaryPrivateIps",
        "security_groups": "securityGroups",
        "source_dest_check": "sourceDestCheck",
        "spot_price": "spotPrice",
        "spot_type": "spotType",
        "subnet_id": "subnetId",
        "tags": "tags",
        "tags_all": "tagsAll",
        "tenancy": "tenancy",
        "timeouts": "timeouts",
        "user_data": "userData",
        "user_data_base64": "userDataBase64",
        "user_data_replace_on_change": "userDataReplaceOnChange",
        "valid_from": "validFrom",
        "valid_until": "validUntil",
        "volume_tags": "volumeTags",
        "vpc_security_group_ids": "vpcSecurityGroupIds",
        "wait_for_fulfillment": "waitForFulfillment",
    },
)
class SpotInstanceRequestConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        ami: typing.Optional[builtins.str] = None,
        associate_public_ip_address: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        availability_zone: typing.Optional[builtins.str] = None,
        block_duration_minutes: typing.Optional[jsii.Number] = None,
        capacity_reservation_specification: typing.Optional[typing.Union[SpotInstanceRequestCapacityReservationSpecification, typing.Dict[builtins.str, typing.Any]]] = None,
        cpu_core_count: typing.Optional[jsii.Number] = None,
        cpu_threads_per_core: typing.Optional[jsii.Number] = None,
        credit_specification: typing.Optional[typing.Union["SpotInstanceRequestCreditSpecification", typing.Dict[builtins.str, typing.Any]]] = None,
        disable_api_stop: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        disable_api_termination: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        ebs_block_device: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SpotInstanceRequestEbsBlockDevice", typing.Dict[builtins.str, typing.Any]]]]] = None,
        ebs_optimized: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enclave_options: typing.Optional[typing.Union["SpotInstanceRequestEnclaveOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        ephemeral_block_device: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SpotInstanceRequestEphemeralBlockDevice", typing.Dict[builtins.str, typing.Any]]]]] = None,
        fetch_password_data: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        hibernation: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        host_id: typing.Optional[builtins.str] = None,
        host_resource_group_arn: typing.Optional[builtins.str] = None,
        iam_instance_profile: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        instance_initiated_shutdown_behavior: typing.Optional[builtins.str] = None,
        instance_interruption_behavior: typing.Optional[builtins.str] = None,
        instance_type: typing.Optional[builtins.str] = None,
        ipv6_address_count: typing.Optional[jsii.Number] = None,
        ipv6_addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
        key_name: typing.Optional[builtins.str] = None,
        launch_group: typing.Optional[builtins.str] = None,
        launch_template: typing.Optional[typing.Union["SpotInstanceRequestLaunchTemplate", typing.Dict[builtins.str, typing.Any]]] = None,
        maintenance_options: typing.Optional[typing.Union["SpotInstanceRequestMaintenanceOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        metadata_options: typing.Optional[typing.Union["SpotInstanceRequestMetadataOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        monitoring: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        network_interface: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SpotInstanceRequestNetworkInterface", typing.Dict[builtins.str, typing.Any]]]]] = None,
        placement_group: typing.Optional[builtins.str] = None,
        placement_partition_number: typing.Optional[jsii.Number] = None,
        private_dns_name_options: typing.Optional[typing.Union["SpotInstanceRequestPrivateDnsNameOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        private_ip: typing.Optional[builtins.str] = None,
        root_block_device: typing.Optional[typing.Union["SpotInstanceRequestRootBlockDevice", typing.Dict[builtins.str, typing.Any]]] = None,
        secondary_private_ips: typing.Optional[typing.Sequence[builtins.str]] = None,
        security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        source_dest_check: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        spot_price: typing.Optional[builtins.str] = None,
        spot_type: typing.Optional[builtins.str] = None,
        subnet_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tenancy: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["SpotInstanceRequestTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        user_data: typing.Optional[builtins.str] = None,
        user_data_base64: typing.Optional[builtins.str] = None,
        user_data_replace_on_change: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        valid_from: typing.Optional[builtins.str] = None,
        valid_until: typing.Optional[builtins.str] = None,
        volume_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        vpc_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        wait_for_fulfillment: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param ami: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#ami SpotInstanceRequest#ami}.
        :param associate_public_ip_address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#associate_public_ip_address SpotInstanceRequest#associate_public_ip_address}.
        :param availability_zone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#availability_zone SpotInstanceRequest#availability_zone}.
        :param block_duration_minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#block_duration_minutes SpotInstanceRequest#block_duration_minutes}.
        :param capacity_reservation_specification: capacity_reservation_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#capacity_reservation_specification SpotInstanceRequest#capacity_reservation_specification}
        :param cpu_core_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#cpu_core_count SpotInstanceRequest#cpu_core_count}.
        :param cpu_threads_per_core: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#cpu_threads_per_core SpotInstanceRequest#cpu_threads_per_core}.
        :param credit_specification: credit_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#credit_specification SpotInstanceRequest#credit_specification}
        :param disable_api_stop: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#disable_api_stop SpotInstanceRequest#disable_api_stop}.
        :param disable_api_termination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#disable_api_termination SpotInstanceRequest#disable_api_termination}.
        :param ebs_block_device: ebs_block_device block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#ebs_block_device SpotInstanceRequest#ebs_block_device}
        :param ebs_optimized: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#ebs_optimized SpotInstanceRequest#ebs_optimized}.
        :param enclave_options: enclave_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#enclave_options SpotInstanceRequest#enclave_options}
        :param ephemeral_block_device: ephemeral_block_device block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#ephemeral_block_device SpotInstanceRequest#ephemeral_block_device}
        :param fetch_password_data: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#get_password_data SpotInstanceRequest#get_password_data}.
        :param hibernation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#hibernation SpotInstanceRequest#hibernation}.
        :param host_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#host_id SpotInstanceRequest#host_id}.
        :param host_resource_group_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#host_resource_group_arn SpotInstanceRequest#host_resource_group_arn}.
        :param iam_instance_profile: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#iam_instance_profile SpotInstanceRequest#iam_instance_profile}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#id SpotInstanceRequest#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param instance_initiated_shutdown_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#instance_initiated_shutdown_behavior SpotInstanceRequest#instance_initiated_shutdown_behavior}.
        :param instance_interruption_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#instance_interruption_behavior SpotInstanceRequest#instance_interruption_behavior}.
        :param instance_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#instance_type SpotInstanceRequest#instance_type}.
        :param ipv6_address_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#ipv6_address_count SpotInstanceRequest#ipv6_address_count}.
        :param ipv6_addresses: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#ipv6_addresses SpotInstanceRequest#ipv6_addresses}.
        :param key_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#key_name SpotInstanceRequest#key_name}.
        :param launch_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#launch_group SpotInstanceRequest#launch_group}.
        :param launch_template: launch_template block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#launch_template SpotInstanceRequest#launch_template}
        :param maintenance_options: maintenance_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#maintenance_options SpotInstanceRequest#maintenance_options}
        :param metadata_options: metadata_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#metadata_options SpotInstanceRequest#metadata_options}
        :param monitoring: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#monitoring SpotInstanceRequest#monitoring}.
        :param network_interface: network_interface block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#network_interface SpotInstanceRequest#network_interface}
        :param placement_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#placement_group SpotInstanceRequest#placement_group}.
        :param placement_partition_number: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#placement_partition_number SpotInstanceRequest#placement_partition_number}.
        :param private_dns_name_options: private_dns_name_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#private_dns_name_options SpotInstanceRequest#private_dns_name_options}
        :param private_ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#private_ip SpotInstanceRequest#private_ip}.
        :param root_block_device: root_block_device block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#root_block_device SpotInstanceRequest#root_block_device}
        :param secondary_private_ips: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#secondary_private_ips SpotInstanceRequest#secondary_private_ips}.
        :param security_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#security_groups SpotInstanceRequest#security_groups}.
        :param source_dest_check: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#source_dest_check SpotInstanceRequest#source_dest_check}.
        :param spot_price: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#spot_price SpotInstanceRequest#spot_price}.
        :param spot_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#spot_type SpotInstanceRequest#spot_type}.
        :param subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#subnet_id SpotInstanceRequest#subnet_id}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#tags SpotInstanceRequest#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#tags_all SpotInstanceRequest#tags_all}.
        :param tenancy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#tenancy SpotInstanceRequest#tenancy}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#timeouts SpotInstanceRequest#timeouts}
        :param user_data: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#user_data SpotInstanceRequest#user_data}.
        :param user_data_base64: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#user_data_base64 SpotInstanceRequest#user_data_base64}.
        :param user_data_replace_on_change: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#user_data_replace_on_change SpotInstanceRequest#user_data_replace_on_change}.
        :param valid_from: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#valid_from SpotInstanceRequest#valid_from}.
        :param valid_until: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#valid_until SpotInstanceRequest#valid_until}.
        :param volume_tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#volume_tags SpotInstanceRequest#volume_tags}.
        :param vpc_security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#vpc_security_group_ids SpotInstanceRequest#vpc_security_group_ids}.
        :param wait_for_fulfillment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#wait_for_fulfillment SpotInstanceRequest#wait_for_fulfillment}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(capacity_reservation_specification, dict):
            capacity_reservation_specification = SpotInstanceRequestCapacityReservationSpecification(**capacity_reservation_specification)
        if isinstance(credit_specification, dict):
            credit_specification = SpotInstanceRequestCreditSpecification(**credit_specification)
        if isinstance(enclave_options, dict):
            enclave_options = SpotInstanceRequestEnclaveOptions(**enclave_options)
        if isinstance(launch_template, dict):
            launch_template = SpotInstanceRequestLaunchTemplate(**launch_template)
        if isinstance(maintenance_options, dict):
            maintenance_options = SpotInstanceRequestMaintenanceOptions(**maintenance_options)
        if isinstance(metadata_options, dict):
            metadata_options = SpotInstanceRequestMetadataOptions(**metadata_options)
        if isinstance(private_dns_name_options, dict):
            private_dns_name_options = SpotInstanceRequestPrivateDnsNameOptions(**private_dns_name_options)
        if isinstance(root_block_device, dict):
            root_block_device = SpotInstanceRequestRootBlockDevice(**root_block_device)
        if isinstance(timeouts, dict):
            timeouts = SpotInstanceRequestTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2603250aaba1895da385b33179b9cc410e3d20fd73a968763f51db324c598ac6)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument ami", value=ami, expected_type=type_hints["ami"])
            check_type(argname="argument associate_public_ip_address", value=associate_public_ip_address, expected_type=type_hints["associate_public_ip_address"])
            check_type(argname="argument availability_zone", value=availability_zone, expected_type=type_hints["availability_zone"])
            check_type(argname="argument block_duration_minutes", value=block_duration_minutes, expected_type=type_hints["block_duration_minutes"])
            check_type(argname="argument capacity_reservation_specification", value=capacity_reservation_specification, expected_type=type_hints["capacity_reservation_specification"])
            check_type(argname="argument cpu_core_count", value=cpu_core_count, expected_type=type_hints["cpu_core_count"])
            check_type(argname="argument cpu_threads_per_core", value=cpu_threads_per_core, expected_type=type_hints["cpu_threads_per_core"])
            check_type(argname="argument credit_specification", value=credit_specification, expected_type=type_hints["credit_specification"])
            check_type(argname="argument disable_api_stop", value=disable_api_stop, expected_type=type_hints["disable_api_stop"])
            check_type(argname="argument disable_api_termination", value=disable_api_termination, expected_type=type_hints["disable_api_termination"])
            check_type(argname="argument ebs_block_device", value=ebs_block_device, expected_type=type_hints["ebs_block_device"])
            check_type(argname="argument ebs_optimized", value=ebs_optimized, expected_type=type_hints["ebs_optimized"])
            check_type(argname="argument enclave_options", value=enclave_options, expected_type=type_hints["enclave_options"])
            check_type(argname="argument ephemeral_block_device", value=ephemeral_block_device, expected_type=type_hints["ephemeral_block_device"])
            check_type(argname="argument fetch_password_data", value=fetch_password_data, expected_type=type_hints["fetch_password_data"])
            check_type(argname="argument hibernation", value=hibernation, expected_type=type_hints["hibernation"])
            check_type(argname="argument host_id", value=host_id, expected_type=type_hints["host_id"])
            check_type(argname="argument host_resource_group_arn", value=host_resource_group_arn, expected_type=type_hints["host_resource_group_arn"])
            check_type(argname="argument iam_instance_profile", value=iam_instance_profile, expected_type=type_hints["iam_instance_profile"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument instance_initiated_shutdown_behavior", value=instance_initiated_shutdown_behavior, expected_type=type_hints["instance_initiated_shutdown_behavior"])
            check_type(argname="argument instance_interruption_behavior", value=instance_interruption_behavior, expected_type=type_hints["instance_interruption_behavior"])
            check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
            check_type(argname="argument ipv6_address_count", value=ipv6_address_count, expected_type=type_hints["ipv6_address_count"])
            check_type(argname="argument ipv6_addresses", value=ipv6_addresses, expected_type=type_hints["ipv6_addresses"])
            check_type(argname="argument key_name", value=key_name, expected_type=type_hints["key_name"])
            check_type(argname="argument launch_group", value=launch_group, expected_type=type_hints["launch_group"])
            check_type(argname="argument launch_template", value=launch_template, expected_type=type_hints["launch_template"])
            check_type(argname="argument maintenance_options", value=maintenance_options, expected_type=type_hints["maintenance_options"])
            check_type(argname="argument metadata_options", value=metadata_options, expected_type=type_hints["metadata_options"])
            check_type(argname="argument monitoring", value=monitoring, expected_type=type_hints["monitoring"])
            check_type(argname="argument network_interface", value=network_interface, expected_type=type_hints["network_interface"])
            check_type(argname="argument placement_group", value=placement_group, expected_type=type_hints["placement_group"])
            check_type(argname="argument placement_partition_number", value=placement_partition_number, expected_type=type_hints["placement_partition_number"])
            check_type(argname="argument private_dns_name_options", value=private_dns_name_options, expected_type=type_hints["private_dns_name_options"])
            check_type(argname="argument private_ip", value=private_ip, expected_type=type_hints["private_ip"])
            check_type(argname="argument root_block_device", value=root_block_device, expected_type=type_hints["root_block_device"])
            check_type(argname="argument secondary_private_ips", value=secondary_private_ips, expected_type=type_hints["secondary_private_ips"])
            check_type(argname="argument security_groups", value=security_groups, expected_type=type_hints["security_groups"])
            check_type(argname="argument source_dest_check", value=source_dest_check, expected_type=type_hints["source_dest_check"])
            check_type(argname="argument spot_price", value=spot_price, expected_type=type_hints["spot_price"])
            check_type(argname="argument spot_type", value=spot_type, expected_type=type_hints["spot_type"])
            check_type(argname="argument subnet_id", value=subnet_id, expected_type=type_hints["subnet_id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument tenancy", value=tenancy, expected_type=type_hints["tenancy"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument user_data", value=user_data, expected_type=type_hints["user_data"])
            check_type(argname="argument user_data_base64", value=user_data_base64, expected_type=type_hints["user_data_base64"])
            check_type(argname="argument user_data_replace_on_change", value=user_data_replace_on_change, expected_type=type_hints["user_data_replace_on_change"])
            check_type(argname="argument valid_from", value=valid_from, expected_type=type_hints["valid_from"])
            check_type(argname="argument valid_until", value=valid_until, expected_type=type_hints["valid_until"])
            check_type(argname="argument volume_tags", value=volume_tags, expected_type=type_hints["volume_tags"])
            check_type(argname="argument vpc_security_group_ids", value=vpc_security_group_ids, expected_type=type_hints["vpc_security_group_ids"])
            check_type(argname="argument wait_for_fulfillment", value=wait_for_fulfillment, expected_type=type_hints["wait_for_fulfillment"])
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
        if ami is not None:
            self._values["ami"] = ami
        if associate_public_ip_address is not None:
            self._values["associate_public_ip_address"] = associate_public_ip_address
        if availability_zone is not None:
            self._values["availability_zone"] = availability_zone
        if block_duration_minutes is not None:
            self._values["block_duration_minutes"] = block_duration_minutes
        if capacity_reservation_specification is not None:
            self._values["capacity_reservation_specification"] = capacity_reservation_specification
        if cpu_core_count is not None:
            self._values["cpu_core_count"] = cpu_core_count
        if cpu_threads_per_core is not None:
            self._values["cpu_threads_per_core"] = cpu_threads_per_core
        if credit_specification is not None:
            self._values["credit_specification"] = credit_specification
        if disable_api_stop is not None:
            self._values["disable_api_stop"] = disable_api_stop
        if disable_api_termination is not None:
            self._values["disable_api_termination"] = disable_api_termination
        if ebs_block_device is not None:
            self._values["ebs_block_device"] = ebs_block_device
        if ebs_optimized is not None:
            self._values["ebs_optimized"] = ebs_optimized
        if enclave_options is not None:
            self._values["enclave_options"] = enclave_options
        if ephemeral_block_device is not None:
            self._values["ephemeral_block_device"] = ephemeral_block_device
        if fetch_password_data is not None:
            self._values["fetch_password_data"] = fetch_password_data
        if hibernation is not None:
            self._values["hibernation"] = hibernation
        if host_id is not None:
            self._values["host_id"] = host_id
        if host_resource_group_arn is not None:
            self._values["host_resource_group_arn"] = host_resource_group_arn
        if iam_instance_profile is not None:
            self._values["iam_instance_profile"] = iam_instance_profile
        if id is not None:
            self._values["id"] = id
        if instance_initiated_shutdown_behavior is not None:
            self._values["instance_initiated_shutdown_behavior"] = instance_initiated_shutdown_behavior
        if instance_interruption_behavior is not None:
            self._values["instance_interruption_behavior"] = instance_interruption_behavior
        if instance_type is not None:
            self._values["instance_type"] = instance_type
        if ipv6_address_count is not None:
            self._values["ipv6_address_count"] = ipv6_address_count
        if ipv6_addresses is not None:
            self._values["ipv6_addresses"] = ipv6_addresses
        if key_name is not None:
            self._values["key_name"] = key_name
        if launch_group is not None:
            self._values["launch_group"] = launch_group
        if launch_template is not None:
            self._values["launch_template"] = launch_template
        if maintenance_options is not None:
            self._values["maintenance_options"] = maintenance_options
        if metadata_options is not None:
            self._values["metadata_options"] = metadata_options
        if monitoring is not None:
            self._values["monitoring"] = monitoring
        if network_interface is not None:
            self._values["network_interface"] = network_interface
        if placement_group is not None:
            self._values["placement_group"] = placement_group
        if placement_partition_number is not None:
            self._values["placement_partition_number"] = placement_partition_number
        if private_dns_name_options is not None:
            self._values["private_dns_name_options"] = private_dns_name_options
        if private_ip is not None:
            self._values["private_ip"] = private_ip
        if root_block_device is not None:
            self._values["root_block_device"] = root_block_device
        if secondary_private_ips is not None:
            self._values["secondary_private_ips"] = secondary_private_ips
        if security_groups is not None:
            self._values["security_groups"] = security_groups
        if source_dest_check is not None:
            self._values["source_dest_check"] = source_dest_check
        if spot_price is not None:
            self._values["spot_price"] = spot_price
        if spot_type is not None:
            self._values["spot_type"] = spot_type
        if subnet_id is not None:
            self._values["subnet_id"] = subnet_id
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if tenancy is not None:
            self._values["tenancy"] = tenancy
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if user_data is not None:
            self._values["user_data"] = user_data
        if user_data_base64 is not None:
            self._values["user_data_base64"] = user_data_base64
        if user_data_replace_on_change is not None:
            self._values["user_data_replace_on_change"] = user_data_replace_on_change
        if valid_from is not None:
            self._values["valid_from"] = valid_from
        if valid_until is not None:
            self._values["valid_until"] = valid_until
        if volume_tags is not None:
            self._values["volume_tags"] = volume_tags
        if vpc_security_group_ids is not None:
            self._values["vpc_security_group_ids"] = vpc_security_group_ids
        if wait_for_fulfillment is not None:
            self._values["wait_for_fulfillment"] = wait_for_fulfillment

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
    def ami(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#ami SpotInstanceRequest#ami}.'''
        result = self._values.get("ami")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def associate_public_ip_address(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#associate_public_ip_address SpotInstanceRequest#associate_public_ip_address}.'''
        result = self._values.get("associate_public_ip_address")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def availability_zone(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#availability_zone SpotInstanceRequest#availability_zone}.'''
        result = self._values.get("availability_zone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def block_duration_minutes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#block_duration_minutes SpotInstanceRequest#block_duration_minutes}.'''
        result = self._values.get("block_duration_minutes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def capacity_reservation_specification(
        self,
    ) -> typing.Optional[SpotInstanceRequestCapacityReservationSpecification]:
        '''capacity_reservation_specification block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#capacity_reservation_specification SpotInstanceRequest#capacity_reservation_specification}
        '''
        result = self._values.get("capacity_reservation_specification")
        return typing.cast(typing.Optional[SpotInstanceRequestCapacityReservationSpecification], result)

    @builtins.property
    def cpu_core_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#cpu_core_count SpotInstanceRequest#cpu_core_count}.'''
        result = self._values.get("cpu_core_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def cpu_threads_per_core(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#cpu_threads_per_core SpotInstanceRequest#cpu_threads_per_core}.'''
        result = self._values.get("cpu_threads_per_core")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def credit_specification(
        self,
    ) -> typing.Optional["SpotInstanceRequestCreditSpecification"]:
        '''credit_specification block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#credit_specification SpotInstanceRequest#credit_specification}
        '''
        result = self._values.get("credit_specification")
        return typing.cast(typing.Optional["SpotInstanceRequestCreditSpecification"], result)

    @builtins.property
    def disable_api_stop(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#disable_api_stop SpotInstanceRequest#disable_api_stop}.'''
        result = self._values.get("disable_api_stop")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def disable_api_termination(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#disable_api_termination SpotInstanceRequest#disable_api_termination}.'''
        result = self._values.get("disable_api_termination")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def ebs_block_device(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SpotInstanceRequestEbsBlockDevice"]]]:
        '''ebs_block_device block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#ebs_block_device SpotInstanceRequest#ebs_block_device}
        '''
        result = self._values.get("ebs_block_device")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SpotInstanceRequestEbsBlockDevice"]]], result)

    @builtins.property
    def ebs_optimized(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#ebs_optimized SpotInstanceRequest#ebs_optimized}.'''
        result = self._values.get("ebs_optimized")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def enclave_options(self) -> typing.Optional["SpotInstanceRequestEnclaveOptions"]:
        '''enclave_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#enclave_options SpotInstanceRequest#enclave_options}
        '''
        result = self._values.get("enclave_options")
        return typing.cast(typing.Optional["SpotInstanceRequestEnclaveOptions"], result)

    @builtins.property
    def ephemeral_block_device(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SpotInstanceRequestEphemeralBlockDevice"]]]:
        '''ephemeral_block_device block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#ephemeral_block_device SpotInstanceRequest#ephemeral_block_device}
        '''
        result = self._values.get("ephemeral_block_device")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SpotInstanceRequestEphemeralBlockDevice"]]], result)

    @builtins.property
    def fetch_password_data(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#get_password_data SpotInstanceRequest#get_password_data}.'''
        result = self._values.get("fetch_password_data")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def hibernation(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#hibernation SpotInstanceRequest#hibernation}.'''
        result = self._values.get("hibernation")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def host_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#host_id SpotInstanceRequest#host_id}.'''
        result = self._values.get("host_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def host_resource_group_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#host_resource_group_arn SpotInstanceRequest#host_resource_group_arn}.'''
        result = self._values.get("host_resource_group_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def iam_instance_profile(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#iam_instance_profile SpotInstanceRequest#iam_instance_profile}.'''
        result = self._values.get("iam_instance_profile")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#id SpotInstanceRequest#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance_initiated_shutdown_behavior(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#instance_initiated_shutdown_behavior SpotInstanceRequest#instance_initiated_shutdown_behavior}.'''
        result = self._values.get("instance_initiated_shutdown_behavior")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance_interruption_behavior(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#instance_interruption_behavior SpotInstanceRequest#instance_interruption_behavior}.'''
        result = self._values.get("instance_interruption_behavior")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#instance_type SpotInstanceRequest#instance_type}.'''
        result = self._values.get("instance_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ipv6_address_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#ipv6_address_count SpotInstanceRequest#ipv6_address_count}.'''
        result = self._values.get("ipv6_address_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ipv6_addresses(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#ipv6_addresses SpotInstanceRequest#ipv6_addresses}.'''
        result = self._values.get("ipv6_addresses")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def key_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#key_name SpotInstanceRequest#key_name}.'''
        result = self._values.get("key_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def launch_group(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#launch_group SpotInstanceRequest#launch_group}.'''
        result = self._values.get("launch_group")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def launch_template(self) -> typing.Optional["SpotInstanceRequestLaunchTemplate"]:
        '''launch_template block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#launch_template SpotInstanceRequest#launch_template}
        '''
        result = self._values.get("launch_template")
        return typing.cast(typing.Optional["SpotInstanceRequestLaunchTemplate"], result)

    @builtins.property
    def maintenance_options(
        self,
    ) -> typing.Optional["SpotInstanceRequestMaintenanceOptions"]:
        '''maintenance_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#maintenance_options SpotInstanceRequest#maintenance_options}
        '''
        result = self._values.get("maintenance_options")
        return typing.cast(typing.Optional["SpotInstanceRequestMaintenanceOptions"], result)

    @builtins.property
    def metadata_options(self) -> typing.Optional["SpotInstanceRequestMetadataOptions"]:
        '''metadata_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#metadata_options SpotInstanceRequest#metadata_options}
        '''
        result = self._values.get("metadata_options")
        return typing.cast(typing.Optional["SpotInstanceRequestMetadataOptions"], result)

    @builtins.property
    def monitoring(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#monitoring SpotInstanceRequest#monitoring}.'''
        result = self._values.get("monitoring")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def network_interface(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SpotInstanceRequestNetworkInterface"]]]:
        '''network_interface block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#network_interface SpotInstanceRequest#network_interface}
        '''
        result = self._values.get("network_interface")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SpotInstanceRequestNetworkInterface"]]], result)

    @builtins.property
    def placement_group(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#placement_group SpotInstanceRequest#placement_group}.'''
        result = self._values.get("placement_group")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def placement_partition_number(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#placement_partition_number SpotInstanceRequest#placement_partition_number}.'''
        result = self._values.get("placement_partition_number")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def private_dns_name_options(
        self,
    ) -> typing.Optional["SpotInstanceRequestPrivateDnsNameOptions"]:
        '''private_dns_name_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#private_dns_name_options SpotInstanceRequest#private_dns_name_options}
        '''
        result = self._values.get("private_dns_name_options")
        return typing.cast(typing.Optional["SpotInstanceRequestPrivateDnsNameOptions"], result)

    @builtins.property
    def private_ip(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#private_ip SpotInstanceRequest#private_ip}.'''
        result = self._values.get("private_ip")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def root_block_device(
        self,
    ) -> typing.Optional["SpotInstanceRequestRootBlockDevice"]:
        '''root_block_device block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#root_block_device SpotInstanceRequest#root_block_device}
        '''
        result = self._values.get("root_block_device")
        return typing.cast(typing.Optional["SpotInstanceRequestRootBlockDevice"], result)

    @builtins.property
    def secondary_private_ips(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#secondary_private_ips SpotInstanceRequest#secondary_private_ips}.'''
        result = self._values.get("secondary_private_ips")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def security_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#security_groups SpotInstanceRequest#security_groups}.'''
        result = self._values.get("security_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def source_dest_check(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#source_dest_check SpotInstanceRequest#source_dest_check}.'''
        result = self._values.get("source_dest_check")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def spot_price(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#spot_price SpotInstanceRequest#spot_price}.'''
        result = self._values.get("spot_price")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def spot_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#spot_type SpotInstanceRequest#spot_type}.'''
        result = self._values.get("spot_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subnet_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#subnet_id SpotInstanceRequest#subnet_id}.'''
        result = self._values.get("subnet_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#tags SpotInstanceRequest#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#tags_all SpotInstanceRequest#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tenancy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#tenancy SpotInstanceRequest#tenancy}.'''
        result = self._values.get("tenancy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["SpotInstanceRequestTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#timeouts SpotInstanceRequest#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["SpotInstanceRequestTimeouts"], result)

    @builtins.property
    def user_data(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#user_data SpotInstanceRequest#user_data}.'''
        result = self._values.get("user_data")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_data_base64(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#user_data_base64 SpotInstanceRequest#user_data_base64}.'''
        result = self._values.get("user_data_base64")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_data_replace_on_change(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#user_data_replace_on_change SpotInstanceRequest#user_data_replace_on_change}.'''
        result = self._values.get("user_data_replace_on_change")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def valid_from(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#valid_from SpotInstanceRequest#valid_from}.'''
        result = self._values.get("valid_from")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def valid_until(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#valid_until SpotInstanceRequest#valid_until}.'''
        result = self._values.get("valid_until")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def volume_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#volume_tags SpotInstanceRequest#volume_tags}.'''
        result = self._values.get("volume_tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def vpc_security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#vpc_security_group_ids SpotInstanceRequest#vpc_security_group_ids}.'''
        result = self._values.get("vpc_security_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def wait_for_fulfillment(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#wait_for_fulfillment SpotInstanceRequest#wait_for_fulfillment}.'''
        result = self._values.get("wait_for_fulfillment")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SpotInstanceRequestConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.spotInstanceRequest.SpotInstanceRequestCreditSpecification",
    jsii_struct_bases=[],
    name_mapping={"cpu_credits": "cpuCredits"},
)
class SpotInstanceRequestCreditSpecification:
    def __init__(self, *, cpu_credits: typing.Optional[builtins.str] = None) -> None:
        '''
        :param cpu_credits: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#cpu_credits SpotInstanceRequest#cpu_credits}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f01d9e27c68776cac4783bf2aa6b32242f8ec92351f2ff6cdb8be29ab50004f5)
            check_type(argname="argument cpu_credits", value=cpu_credits, expected_type=type_hints["cpu_credits"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if cpu_credits is not None:
            self._values["cpu_credits"] = cpu_credits

    @builtins.property
    def cpu_credits(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#cpu_credits SpotInstanceRequest#cpu_credits}.'''
        result = self._values.get("cpu_credits")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SpotInstanceRequestCreditSpecification(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SpotInstanceRequestCreditSpecificationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.spotInstanceRequest.SpotInstanceRequestCreditSpecificationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4d3087ce8852c04b986df030cb6353ffd63be860b6c47081d51a58759e03daf6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__25bb8c85bdaefa3499ab51de09844545367ff35f31ab520f6291a842a8bf4b03)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpuCredits", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SpotInstanceRequestCreditSpecification]:
        return typing.cast(typing.Optional[SpotInstanceRequestCreditSpecification], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SpotInstanceRequestCreditSpecification],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4eace2a65eb0c22771b673e0b0db9e43743ca11b00da0bd9eae396ee29205b84)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.spotInstanceRequest.SpotInstanceRequestEbsBlockDevice",
    jsii_struct_bases=[],
    name_mapping={
        "device_name": "deviceName",
        "delete_on_termination": "deleteOnTermination",
        "encrypted": "encrypted",
        "iops": "iops",
        "kms_key_id": "kmsKeyId",
        "snapshot_id": "snapshotId",
        "tags": "tags",
        "throughput": "throughput",
        "volume_size": "volumeSize",
        "volume_type": "volumeType",
    },
)
class SpotInstanceRequestEbsBlockDevice:
    def __init__(
        self,
        *,
        device_name: builtins.str,
        delete_on_termination: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        encrypted: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        iops: typing.Optional[jsii.Number] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        snapshot_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        throughput: typing.Optional[jsii.Number] = None,
        volume_size: typing.Optional[jsii.Number] = None,
        volume_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param device_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#device_name SpotInstanceRequest#device_name}.
        :param delete_on_termination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#delete_on_termination SpotInstanceRequest#delete_on_termination}.
        :param encrypted: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#encrypted SpotInstanceRequest#encrypted}.
        :param iops: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#iops SpotInstanceRequest#iops}.
        :param kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#kms_key_id SpotInstanceRequest#kms_key_id}.
        :param snapshot_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#snapshot_id SpotInstanceRequest#snapshot_id}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#tags SpotInstanceRequest#tags}.
        :param throughput: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#throughput SpotInstanceRequest#throughput}.
        :param volume_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#volume_size SpotInstanceRequest#volume_size}.
        :param volume_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#volume_type SpotInstanceRequest#volume_type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc8c3a14338c02affe16e702866edfc6902ec707eea2202ddb2e761751deb197)
            check_type(argname="argument device_name", value=device_name, expected_type=type_hints["device_name"])
            check_type(argname="argument delete_on_termination", value=delete_on_termination, expected_type=type_hints["delete_on_termination"])
            check_type(argname="argument encrypted", value=encrypted, expected_type=type_hints["encrypted"])
            check_type(argname="argument iops", value=iops, expected_type=type_hints["iops"])
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            check_type(argname="argument snapshot_id", value=snapshot_id, expected_type=type_hints["snapshot_id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument throughput", value=throughput, expected_type=type_hints["throughput"])
            check_type(argname="argument volume_size", value=volume_size, expected_type=type_hints["volume_size"])
            check_type(argname="argument volume_type", value=volume_type, expected_type=type_hints["volume_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "device_name": device_name,
        }
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
        if tags is not None:
            self._values["tags"] = tags
        if throughput is not None:
            self._values["throughput"] = throughput
        if volume_size is not None:
            self._values["volume_size"] = volume_size
        if volume_type is not None:
            self._values["volume_type"] = volume_type

    @builtins.property
    def device_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#device_name SpotInstanceRequest#device_name}.'''
        result = self._values.get("device_name")
        assert result is not None, "Required property 'device_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def delete_on_termination(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#delete_on_termination SpotInstanceRequest#delete_on_termination}.'''
        result = self._values.get("delete_on_termination")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def encrypted(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#encrypted SpotInstanceRequest#encrypted}.'''
        result = self._values.get("encrypted")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def iops(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#iops SpotInstanceRequest#iops}.'''
        result = self._values.get("iops")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#kms_key_id SpotInstanceRequest#kms_key_id}.'''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def snapshot_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#snapshot_id SpotInstanceRequest#snapshot_id}.'''
        result = self._values.get("snapshot_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#tags SpotInstanceRequest#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def throughput(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#throughput SpotInstanceRequest#throughput}.'''
        result = self._values.get("throughput")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def volume_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#volume_size SpotInstanceRequest#volume_size}.'''
        result = self._values.get("volume_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def volume_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#volume_type SpotInstanceRequest#volume_type}.'''
        result = self._values.get("volume_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SpotInstanceRequestEbsBlockDevice(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SpotInstanceRequestEbsBlockDeviceList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.spotInstanceRequest.SpotInstanceRequestEbsBlockDeviceList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7eaf757afe4edb513d6c685bcafbfb50f17d32e561a5d305904eef377596f962)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "SpotInstanceRequestEbsBlockDeviceOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6760f6d41506153545069bc7f8af362597640d3f5d2335f19df98cd8e7ca5f27)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SpotInstanceRequestEbsBlockDeviceOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3634a17bedee982dd57da45b280a7a0a09f4ecdc6f8d18e5c5c2bbe113cfd914)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d68cef748ac76a07b5b8862522076d0fe9cd950f9b0c3878c0911f56b96edbd1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c3cc78b3284b8e5ff23bfdfbbcbe3c1a4b7b4413593edf11a41e01e473f884e5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SpotInstanceRequestEbsBlockDevice]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SpotInstanceRequestEbsBlockDevice]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SpotInstanceRequestEbsBlockDevice]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1cdf11af7b05bbd5fa4f23fb0b52dfe17fede1c9b2e878ff5464e5a8b7ee9a6c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SpotInstanceRequestEbsBlockDeviceOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.spotInstanceRequest.SpotInstanceRequestEbsBlockDeviceOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__58cc8dc06c9c5556df34630afc621e2e233ba251307ce10559de91efbf28d013)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

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

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

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
    @jsii.member(jsii_name="volumeId")
    def volume_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "volumeId"))

    @builtins.property
    @jsii.member(jsii_name="deleteOnTerminationInput")
    def delete_on_termination_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "deleteOnTerminationInput"))

    @builtins.property
    @jsii.member(jsii_name="deviceNameInput")
    def device_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deviceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptedInput")
    def encrypted_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "encryptedInput"))

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
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

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
    def delete_on_termination(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "deleteOnTermination"))

    @delete_on_termination.setter
    def delete_on_termination(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ddd96ad5d48605cf34a32c51ced2c8bd4955858a92a3cabcb6829259b9ae9ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deleteOnTermination", value)

    @builtins.property
    @jsii.member(jsii_name="deviceName")
    def device_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deviceName"))

    @device_name.setter
    def device_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c110075e4cc7b17498fa8af2f249aa476dbf993f9da6fb4f7d4c6bae1d3ff4d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deviceName", value)

    @builtins.property
    @jsii.member(jsii_name="encrypted")
    def encrypted(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "encrypted"))

    @encrypted.setter
    def encrypted(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4bbf77c7aadf00ee5e6a19665494286ff98146a7c7bb8448838924a8ea05a67d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encrypted", value)

    @builtins.property
    @jsii.member(jsii_name="iops")
    def iops(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "iops"))

    @iops.setter
    def iops(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6cf06f3911d80963454a111d13fb9ce58f8620cdb6b666f2ad5c9f318ddc5dd4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iops", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09480438bbdd1c881dfb081b32017dc98deb85732f3ad13e17bd13d40e4025d4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="snapshotId")
    def snapshot_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "snapshotId"))

    @snapshot_id.setter
    def snapshot_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__366716ce64288c39f08b97118f07ac217a975612aa54cebcb63cfcf1e98bc055)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snapshotId", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b17a86ac30e09bc0469b69282d6aa85659a79e95463b02723bb06204cf5c11d3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="throughput")
    def throughput(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "throughput"))

    @throughput.setter
    def throughput(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7828111dc93427b202e943b5033815153caaa19a4ab840241e584cb556591a0c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "throughput", value)

    @builtins.property
    @jsii.member(jsii_name="volumeSize")
    def volume_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "volumeSize"))

    @volume_size.setter
    def volume_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__597ecc3fed45ff6c94a884892e4fbf82d72a9df14700731d888f1c708612835a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeSize", value)

    @builtins.property
    @jsii.member(jsii_name="volumeType")
    def volume_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "volumeType"))

    @volume_type.setter
    def volume_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__523cb2fe49e11abcabf056eeaf2334105f9e674b3a5f5566d92f99922c9c6b4a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SpotInstanceRequestEbsBlockDevice, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SpotInstanceRequestEbsBlockDevice, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SpotInstanceRequestEbsBlockDevice, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d7efa953f1877349631fcefab5c337f39817d73d83036d69d6813a52e9b47cd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.spotInstanceRequest.SpotInstanceRequestEnclaveOptions",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled"},
)
class SpotInstanceRequestEnclaveOptions:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#enabled SpotInstanceRequest#enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08cdadfe3625ad91a38f81a19a72b801c27af060b8e482dc37585a7695df0fc9)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#enabled SpotInstanceRequest#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SpotInstanceRequestEnclaveOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SpotInstanceRequestEnclaveOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.spotInstanceRequest.SpotInstanceRequestEnclaveOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__212741adc100ffc730c7a7f5269ff6c8529b555f3155a00464928dd9f198543d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__61807d5e111b027e8b23102419ace8a0119b92bee2cda8b904e7b456c23d7a4b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SpotInstanceRequestEnclaveOptions]:
        return typing.cast(typing.Optional[SpotInstanceRequestEnclaveOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SpotInstanceRequestEnclaveOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13222cc0e526231401bbe4a4e239f782790c6f794c18fe77d9d00ad32fde49d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.spotInstanceRequest.SpotInstanceRequestEphemeralBlockDevice",
    jsii_struct_bases=[],
    name_mapping={
        "device_name": "deviceName",
        "no_device": "noDevice",
        "virtual_name": "virtualName",
    },
)
class SpotInstanceRequestEphemeralBlockDevice:
    def __init__(
        self,
        *,
        device_name: builtins.str,
        no_device: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        virtual_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param device_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#device_name SpotInstanceRequest#device_name}.
        :param no_device: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#no_device SpotInstanceRequest#no_device}.
        :param virtual_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#virtual_name SpotInstanceRequest#virtual_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b8b9f9c704d54d304d637aba753688009d2f34f89bef9626f247885fca93247)
            check_type(argname="argument device_name", value=device_name, expected_type=type_hints["device_name"])
            check_type(argname="argument no_device", value=no_device, expected_type=type_hints["no_device"])
            check_type(argname="argument virtual_name", value=virtual_name, expected_type=type_hints["virtual_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "device_name": device_name,
        }
        if no_device is not None:
            self._values["no_device"] = no_device
        if virtual_name is not None:
            self._values["virtual_name"] = virtual_name

    @builtins.property
    def device_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#device_name SpotInstanceRequest#device_name}.'''
        result = self._values.get("device_name")
        assert result is not None, "Required property 'device_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def no_device(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#no_device SpotInstanceRequest#no_device}.'''
        result = self._values.get("no_device")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def virtual_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#virtual_name SpotInstanceRequest#virtual_name}.'''
        result = self._values.get("virtual_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SpotInstanceRequestEphemeralBlockDevice(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SpotInstanceRequestEphemeralBlockDeviceList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.spotInstanceRequest.SpotInstanceRequestEphemeralBlockDeviceList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0a0c335a6f08b446d659f9e3d76a4f48aadb9c18596f13a5609d9ff788b6ff9a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "SpotInstanceRequestEphemeralBlockDeviceOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__208f2fc0a560d367cc5fdb30bacb062f421b8fd4699171be0def12e01af1ec4c)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SpotInstanceRequestEphemeralBlockDeviceOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c2b132bdb5e9e11b3124aae04002cd869b2073917838f9904afaa2ab3f8a1c5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a8f50e01a524c485706826455cbe8dea4fbdd4d300af3c3c79edcd7f6e137b78)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d960132322f177877288a3776b80e8dd70221f8a826e3359112baed57cf93843)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SpotInstanceRequestEphemeralBlockDevice]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SpotInstanceRequestEphemeralBlockDevice]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SpotInstanceRequestEphemeralBlockDevice]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d444305b3a2b3bb049118a4b51ba4a1ad6f4d7e93ff4a5a08092110b9c79585)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SpotInstanceRequestEphemeralBlockDeviceOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.spotInstanceRequest.SpotInstanceRequestEphemeralBlockDeviceOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0976a31e9c3f97c04ec712ae968962e4efa3e473263609bff6c05d9f68292d0f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetNoDevice")
    def reset_no_device(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNoDevice", []))

    @jsii.member(jsii_name="resetVirtualName")
    def reset_virtual_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVirtualName", []))

    @builtins.property
    @jsii.member(jsii_name="deviceNameInput")
    def device_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deviceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="noDeviceInput")
    def no_device_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "noDeviceInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__133a750cfbd9d36163ff45877d1ce92a75e0710d010121ddc97e64fabcd2eeb3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deviceName", value)

    @builtins.property
    @jsii.member(jsii_name="noDevice")
    def no_device(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "noDevice"))

    @no_device.setter
    def no_device(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da1f7f8e79ed1f41709aee03ddb1b76443b20a3645fd078e5f859a095a2d9520)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "noDevice", value)

    @builtins.property
    @jsii.member(jsii_name="virtualName")
    def virtual_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "virtualName"))

    @virtual_name.setter
    def virtual_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8d7b19086836e4d0de355184e3e81e5b6bf39c47835f5c8f94256eae3d255f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SpotInstanceRequestEphemeralBlockDevice, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SpotInstanceRequestEphemeralBlockDevice, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SpotInstanceRequestEphemeralBlockDevice, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__420e189daeb046f94cb84289225fb8ac89f16c65b92f19d14197a37edb160c45)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.spotInstanceRequest.SpotInstanceRequestLaunchTemplate",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "name": "name", "version": "version"},
)
class SpotInstanceRequestLaunchTemplate:
    def __init__(
        self,
        *,
        id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#id SpotInstanceRequest#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#name SpotInstanceRequest#name}.
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#version SpotInstanceRequest#version}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7469d461fa7079233db94028ca43c6ceead9470c68b0c391e71b1663a3bd4025)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id
        if name is not None:
            self._values["name"] = name
        if version is not None:
            self._values["version"] = version

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#id SpotInstanceRequest#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#name SpotInstanceRequest#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#version SpotInstanceRequest#version}.'''
        result = self._values.get("version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SpotInstanceRequestLaunchTemplate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SpotInstanceRequestLaunchTemplateOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.spotInstanceRequest.SpotInstanceRequestLaunchTemplateOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e1f48e972c6e4bb2f70b205112551396100f7a1f1e80e16087d92aff088ec56c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetVersion")
    def reset_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVersion", []))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="versionInput")
    def version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bcb447a886ef558020ad5f9e5acb398ac234e8996591205fb7160bfc6819fb74)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ea82f72bd2edd696b4112e23c39431fb50a6fac79a973ad856627d910f4b6d9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72e3284e9850db2750c54dd08de70da9b81736064296868970897277018fe501)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SpotInstanceRequestLaunchTemplate]:
        return typing.cast(typing.Optional[SpotInstanceRequestLaunchTemplate], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SpotInstanceRequestLaunchTemplate],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e85082d4ad44e09a442ede6d13086f6ae8846fdcda26265e03e0246ab00e3b9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.spotInstanceRequest.SpotInstanceRequestMaintenanceOptions",
    jsii_struct_bases=[],
    name_mapping={"auto_recovery": "autoRecovery"},
)
class SpotInstanceRequestMaintenanceOptions:
    def __init__(self, *, auto_recovery: typing.Optional[builtins.str] = None) -> None:
        '''
        :param auto_recovery: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#auto_recovery SpotInstanceRequest#auto_recovery}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12826429a97ff07ee728166cea15bad545df63da140673029debc57c3f3cd09d)
            check_type(argname="argument auto_recovery", value=auto_recovery, expected_type=type_hints["auto_recovery"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if auto_recovery is not None:
            self._values["auto_recovery"] = auto_recovery

    @builtins.property
    def auto_recovery(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#auto_recovery SpotInstanceRequest#auto_recovery}.'''
        result = self._values.get("auto_recovery")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SpotInstanceRequestMaintenanceOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SpotInstanceRequestMaintenanceOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.spotInstanceRequest.SpotInstanceRequestMaintenanceOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3cef8368235b362b6fc52482e2bc7a33e6ac8f4cf9ccef94865dc7ab9011be59)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c008efa7e7d2436107a9fe8c376ff4824d3e776afa9c3d6877a451c1efb2839d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoRecovery", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SpotInstanceRequestMaintenanceOptions]:
        return typing.cast(typing.Optional[SpotInstanceRequestMaintenanceOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SpotInstanceRequestMaintenanceOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32964d4c2a186c8dc2aa4687ca090b0d227fc9ed03a638e259dd49f4d55308ba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.spotInstanceRequest.SpotInstanceRequestMetadataOptions",
    jsii_struct_bases=[],
    name_mapping={
        "http_endpoint": "httpEndpoint",
        "http_put_response_hop_limit": "httpPutResponseHopLimit",
        "http_tokens": "httpTokens",
        "instance_metadata_tags": "instanceMetadataTags",
    },
)
class SpotInstanceRequestMetadataOptions:
    def __init__(
        self,
        *,
        http_endpoint: typing.Optional[builtins.str] = None,
        http_put_response_hop_limit: typing.Optional[jsii.Number] = None,
        http_tokens: typing.Optional[builtins.str] = None,
        instance_metadata_tags: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param http_endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#http_endpoint SpotInstanceRequest#http_endpoint}.
        :param http_put_response_hop_limit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#http_put_response_hop_limit SpotInstanceRequest#http_put_response_hop_limit}.
        :param http_tokens: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#http_tokens SpotInstanceRequest#http_tokens}.
        :param instance_metadata_tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#instance_metadata_tags SpotInstanceRequest#instance_metadata_tags}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d0020c1ace79b7db4fb0215b9be49e8e0f44923ec6ee18f9f59ff72552f86d0)
            check_type(argname="argument http_endpoint", value=http_endpoint, expected_type=type_hints["http_endpoint"])
            check_type(argname="argument http_put_response_hop_limit", value=http_put_response_hop_limit, expected_type=type_hints["http_put_response_hop_limit"])
            check_type(argname="argument http_tokens", value=http_tokens, expected_type=type_hints["http_tokens"])
            check_type(argname="argument instance_metadata_tags", value=instance_metadata_tags, expected_type=type_hints["instance_metadata_tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if http_endpoint is not None:
            self._values["http_endpoint"] = http_endpoint
        if http_put_response_hop_limit is not None:
            self._values["http_put_response_hop_limit"] = http_put_response_hop_limit
        if http_tokens is not None:
            self._values["http_tokens"] = http_tokens
        if instance_metadata_tags is not None:
            self._values["instance_metadata_tags"] = instance_metadata_tags

    @builtins.property
    def http_endpoint(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#http_endpoint SpotInstanceRequest#http_endpoint}.'''
        result = self._values.get("http_endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def http_put_response_hop_limit(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#http_put_response_hop_limit SpotInstanceRequest#http_put_response_hop_limit}.'''
        result = self._values.get("http_put_response_hop_limit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def http_tokens(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#http_tokens SpotInstanceRequest#http_tokens}.'''
        result = self._values.get("http_tokens")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance_metadata_tags(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#instance_metadata_tags SpotInstanceRequest#instance_metadata_tags}.'''
        result = self._values.get("instance_metadata_tags")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SpotInstanceRequestMetadataOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SpotInstanceRequestMetadataOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.spotInstanceRequest.SpotInstanceRequestMetadataOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5ca4eb2f73e76e6a0c01486515a40cb602e257dcd4fbb7edf99423dc75e15f11)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetHttpEndpoint")
    def reset_http_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpEndpoint", []))

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
            type_hints = typing.get_type_hints(_typecheckingstub__b766de8c2216e4d7a9235facb4595206788aebade0e08b61cb78b420a6100db7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="httpPutResponseHopLimit")
    def http_put_response_hop_limit(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "httpPutResponseHopLimit"))

    @http_put_response_hop_limit.setter
    def http_put_response_hop_limit(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29f65185bc783ff223ed45c9da3e0705991628898d4dd69b6f9ce4944cd5a824)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpPutResponseHopLimit", value)

    @builtins.property
    @jsii.member(jsii_name="httpTokens")
    def http_tokens(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "httpTokens"))

    @http_tokens.setter
    def http_tokens(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6410b750c6d025e0fcb1040b6b57704a3ac6894159ddf0f7e0d436458b3c6d7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpTokens", value)

    @builtins.property
    @jsii.member(jsii_name="instanceMetadataTags")
    def instance_metadata_tags(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceMetadataTags"))

    @instance_metadata_tags.setter
    def instance_metadata_tags(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d36e90e63b7a121c2c578db8bf6161623273af24b1b6a1768ceec980f301810f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceMetadataTags", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SpotInstanceRequestMetadataOptions]:
        return typing.cast(typing.Optional[SpotInstanceRequestMetadataOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SpotInstanceRequestMetadataOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a31e17f76630c1e7dba8738f17b3c567e1ccdf99ac25873bc588a2e7210f58c1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.spotInstanceRequest.SpotInstanceRequestNetworkInterface",
    jsii_struct_bases=[],
    name_mapping={
        "device_index": "deviceIndex",
        "network_interface_id": "networkInterfaceId",
        "delete_on_termination": "deleteOnTermination",
        "network_card_index": "networkCardIndex",
    },
)
class SpotInstanceRequestNetworkInterface:
    def __init__(
        self,
        *,
        device_index: jsii.Number,
        network_interface_id: builtins.str,
        delete_on_termination: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        network_card_index: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param device_index: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#device_index SpotInstanceRequest#device_index}.
        :param network_interface_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#network_interface_id SpotInstanceRequest#network_interface_id}.
        :param delete_on_termination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#delete_on_termination SpotInstanceRequest#delete_on_termination}.
        :param network_card_index: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#network_card_index SpotInstanceRequest#network_card_index}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d26723a85e43ffa26c5fc268d5a8af19e8ed0f179aeb2dbbc07aa55b2b58166)
            check_type(argname="argument device_index", value=device_index, expected_type=type_hints["device_index"])
            check_type(argname="argument network_interface_id", value=network_interface_id, expected_type=type_hints["network_interface_id"])
            check_type(argname="argument delete_on_termination", value=delete_on_termination, expected_type=type_hints["delete_on_termination"])
            check_type(argname="argument network_card_index", value=network_card_index, expected_type=type_hints["network_card_index"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "device_index": device_index,
            "network_interface_id": network_interface_id,
        }
        if delete_on_termination is not None:
            self._values["delete_on_termination"] = delete_on_termination
        if network_card_index is not None:
            self._values["network_card_index"] = network_card_index

    @builtins.property
    def device_index(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#device_index SpotInstanceRequest#device_index}.'''
        result = self._values.get("device_index")
        assert result is not None, "Required property 'device_index' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def network_interface_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#network_interface_id SpotInstanceRequest#network_interface_id}.'''
        result = self._values.get("network_interface_id")
        assert result is not None, "Required property 'network_interface_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def delete_on_termination(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#delete_on_termination SpotInstanceRequest#delete_on_termination}.'''
        result = self._values.get("delete_on_termination")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def network_card_index(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#network_card_index SpotInstanceRequest#network_card_index}.'''
        result = self._values.get("network_card_index")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SpotInstanceRequestNetworkInterface(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SpotInstanceRequestNetworkInterfaceList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.spotInstanceRequest.SpotInstanceRequestNetworkInterfaceList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ee585565799e51d9bbe617daccfeecd0b6cbb2fe602f6920384fc7248089c398)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "SpotInstanceRequestNetworkInterfaceOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a182a3acf21d8ac2b5466cc66d06b6c9c868b0c05cc71b3a4d3d8d528e436cd)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SpotInstanceRequestNetworkInterfaceOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b99ba8201dc2dfdcf99d187ca6e706be438d6090e2ed5e509dc9cc1bd7585d08)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f79496f3b137c7d380e95e334884b9d6c6a99c3238dd608011d8e76e7a3e5607)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c473318dd7de892bad81105a75e049e5724c5ba394d302edd136ddafda175b2f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SpotInstanceRequestNetworkInterface]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SpotInstanceRequestNetworkInterface]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SpotInstanceRequestNetworkInterface]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__356cdee787f5d750da2bbae1fdaa0aa383efa6c0809a3fec1f144127b671f580)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SpotInstanceRequestNetworkInterfaceOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.spotInstanceRequest.SpotInstanceRequestNetworkInterfaceOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b6412bcf6d4d67dab5efa1a6928f2e03e25613027880c748d68bfe1493bedc54)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDeleteOnTermination")
    def reset_delete_on_termination(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeleteOnTermination", []))

    @jsii.member(jsii_name="resetNetworkCardIndex")
    def reset_network_card_index(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworkCardIndex", []))

    @builtins.property
    @jsii.member(jsii_name="deleteOnTerminationInput")
    def delete_on_termination_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "deleteOnTerminationInput"))

    @builtins.property
    @jsii.member(jsii_name="deviceIndexInput")
    def device_index_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "deviceIndexInput"))

    @builtins.property
    @jsii.member(jsii_name="networkCardIndexInput")
    def network_card_index_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "networkCardIndexInput"))

    @builtins.property
    @jsii.member(jsii_name="networkInterfaceIdInput")
    def network_interface_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkInterfaceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteOnTermination")
    def delete_on_termination(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "deleteOnTermination"))

    @delete_on_termination.setter
    def delete_on_termination(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f7151b76c5f73856b1af401b8a694d12b94cca69b7aa686919664a5bdab8e6e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deleteOnTermination", value)

    @builtins.property
    @jsii.member(jsii_name="deviceIndex")
    def device_index(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "deviceIndex"))

    @device_index.setter
    def device_index(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6529ce4fb893de43753eee385f3fedc38ece2191f68d1506a5bae4841cd37e18)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deviceIndex", value)

    @builtins.property
    @jsii.member(jsii_name="networkCardIndex")
    def network_card_index(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "networkCardIndex"))

    @network_card_index.setter
    def network_card_index(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__963386f89e1ffaade92f2702f0506be70009685db8d7e7943902466fe527de1d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkCardIndex", value)

    @builtins.property
    @jsii.member(jsii_name="networkInterfaceId")
    def network_interface_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "networkInterfaceId"))

    @network_interface_id.setter
    def network_interface_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9fee919787dc7f28e4424f2be802754760fdca718936c063ee8ac74faa635be)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkInterfaceId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SpotInstanceRequestNetworkInterface, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SpotInstanceRequestNetworkInterface, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SpotInstanceRequestNetworkInterface, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ef9b189fc7b4a1ee9a99d590f55a6c2fbdab7db8e01cc1bc42fa522c4724c39)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.spotInstanceRequest.SpotInstanceRequestPrivateDnsNameOptions",
    jsii_struct_bases=[],
    name_mapping={
        "enable_resource_name_dns_aaaa_record": "enableResourceNameDnsAaaaRecord",
        "enable_resource_name_dns_a_record": "enableResourceNameDnsARecord",
        "hostname_type": "hostnameType",
    },
)
class SpotInstanceRequestPrivateDnsNameOptions:
    def __init__(
        self,
        *,
        enable_resource_name_dns_aaaa_record: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_resource_name_dns_a_record: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        hostname_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enable_resource_name_dns_aaaa_record: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#enable_resource_name_dns_aaaa_record SpotInstanceRequest#enable_resource_name_dns_aaaa_record}.
        :param enable_resource_name_dns_a_record: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#enable_resource_name_dns_a_record SpotInstanceRequest#enable_resource_name_dns_a_record}.
        :param hostname_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#hostname_type SpotInstanceRequest#hostname_type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4cf8b3311b814ebd1527b3b54b693d2d9f228f9e765b08a6fa2d0d65b6d3237)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#enable_resource_name_dns_aaaa_record SpotInstanceRequest#enable_resource_name_dns_aaaa_record}.'''
        result = self._values.get("enable_resource_name_dns_aaaa_record")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def enable_resource_name_dns_a_record(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#enable_resource_name_dns_a_record SpotInstanceRequest#enable_resource_name_dns_a_record}.'''
        result = self._values.get("enable_resource_name_dns_a_record")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def hostname_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#hostname_type SpotInstanceRequest#hostname_type}.'''
        result = self._values.get("hostname_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SpotInstanceRequestPrivateDnsNameOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SpotInstanceRequestPrivateDnsNameOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.spotInstanceRequest.SpotInstanceRequestPrivateDnsNameOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__815b86437db9fd63fd45b54aafaf35f466c0f7fe8015de2c40085bc060511d7f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1f9860056bfb1906dd10397b32dae1592d7da824915a5da0fa8e4ef45e8b0d0d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3e45bf7b97b80facc860bbd6f2e51eba87864727aa1a904ed486cd0aaf9b346a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableResourceNameDnsARecord", value)

    @builtins.property
    @jsii.member(jsii_name="hostnameType")
    def hostname_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostnameType"))

    @hostname_type.setter
    def hostname_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66de66197c5b8bb64cebf7316f8dafd5d9034cecb233179e6df985aec1b0e067)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostnameType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SpotInstanceRequestPrivateDnsNameOptions]:
        return typing.cast(typing.Optional[SpotInstanceRequestPrivateDnsNameOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SpotInstanceRequestPrivateDnsNameOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c9f0e65e917456c9426830a0a5cf0278b41141f28f418c319de30f99b72f27b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.spotInstanceRequest.SpotInstanceRequestRootBlockDevice",
    jsii_struct_bases=[],
    name_mapping={
        "delete_on_termination": "deleteOnTermination",
        "encrypted": "encrypted",
        "iops": "iops",
        "kms_key_id": "kmsKeyId",
        "tags": "tags",
        "throughput": "throughput",
        "volume_size": "volumeSize",
        "volume_type": "volumeType",
    },
)
class SpotInstanceRequestRootBlockDevice:
    def __init__(
        self,
        *,
        delete_on_termination: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        encrypted: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        iops: typing.Optional[jsii.Number] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        throughput: typing.Optional[jsii.Number] = None,
        volume_size: typing.Optional[jsii.Number] = None,
        volume_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param delete_on_termination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#delete_on_termination SpotInstanceRequest#delete_on_termination}.
        :param encrypted: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#encrypted SpotInstanceRequest#encrypted}.
        :param iops: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#iops SpotInstanceRequest#iops}.
        :param kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#kms_key_id SpotInstanceRequest#kms_key_id}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#tags SpotInstanceRequest#tags}.
        :param throughput: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#throughput SpotInstanceRequest#throughput}.
        :param volume_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#volume_size SpotInstanceRequest#volume_size}.
        :param volume_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#volume_type SpotInstanceRequest#volume_type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1e4fe5d198dbb2503594e0f0c28a59fd2b60b6d899306077e5b3aae9578569a)
            check_type(argname="argument delete_on_termination", value=delete_on_termination, expected_type=type_hints["delete_on_termination"])
            check_type(argname="argument encrypted", value=encrypted, expected_type=type_hints["encrypted"])
            check_type(argname="argument iops", value=iops, expected_type=type_hints["iops"])
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
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
        if tags is not None:
            self._values["tags"] = tags
        if throughput is not None:
            self._values["throughput"] = throughput
        if volume_size is not None:
            self._values["volume_size"] = volume_size
        if volume_type is not None:
            self._values["volume_type"] = volume_type

    @builtins.property
    def delete_on_termination(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#delete_on_termination SpotInstanceRequest#delete_on_termination}.'''
        result = self._values.get("delete_on_termination")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def encrypted(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#encrypted SpotInstanceRequest#encrypted}.'''
        result = self._values.get("encrypted")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def iops(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#iops SpotInstanceRequest#iops}.'''
        result = self._values.get("iops")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#kms_key_id SpotInstanceRequest#kms_key_id}.'''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#tags SpotInstanceRequest#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def throughput(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#throughput SpotInstanceRequest#throughput}.'''
        result = self._values.get("throughput")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def volume_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#volume_size SpotInstanceRequest#volume_size}.'''
        result = self._values.get("volume_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def volume_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#volume_type SpotInstanceRequest#volume_type}.'''
        result = self._values.get("volume_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SpotInstanceRequestRootBlockDevice(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SpotInstanceRequestRootBlockDeviceOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.spotInstanceRequest.SpotInstanceRequestRootBlockDeviceOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c02a2cb345215cb609138f52a2149814aed5d8bb729e37897dd8b8189cce63d9)
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

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

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
    @jsii.member(jsii_name="deviceName")
    def device_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deviceName"))

    @builtins.property
    @jsii.member(jsii_name="volumeId")
    def volume_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "volumeId"))

    @builtins.property
    @jsii.member(jsii_name="deleteOnTerminationInput")
    def delete_on_termination_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "deleteOnTerminationInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptedInput")
    def encrypted_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "encryptedInput"))

    @builtins.property
    @jsii.member(jsii_name="iopsInput")
    def iops_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "iopsInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyIdInput")
    def kms_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

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
    def delete_on_termination(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "deleteOnTermination"))

    @delete_on_termination.setter
    def delete_on_termination(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__082d17c02e845a1c6cf6f043a1edc9c3ee57535931bc5739b0b89d24e583c2f6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deleteOnTermination", value)

    @builtins.property
    @jsii.member(jsii_name="encrypted")
    def encrypted(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "encrypted"))

    @encrypted.setter
    def encrypted(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84d389e6c75fbfe24b77fa9d95d60a20cd4b1b3756b54638bd27808c8cd4f5b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encrypted", value)

    @builtins.property
    @jsii.member(jsii_name="iops")
    def iops(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "iops"))

    @iops.setter
    def iops(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1dcc9c34e6c4d848b8ea51baecadadc8066125861df58c85023ce926aa5ea047)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iops", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d606e00fb8fcd6f2b41c406c997abd509721fbf920771582610f7902e6a5add)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b1f73071519e10f50dc5d37e2dffcfc4808fc80dbe0355c1c9e40f13ac2a29e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="throughput")
    def throughput(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "throughput"))

    @throughput.setter
    def throughput(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3aa939d5a825ad1965d914a9ee23b2e94ae8deb6e7ce06cfe0c1f06a14f002e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "throughput", value)

    @builtins.property
    @jsii.member(jsii_name="volumeSize")
    def volume_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "volumeSize"))

    @volume_size.setter
    def volume_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a1c3f12cea9ff71f0b0c13098559a714d55f510e8c6bae9e4248621800f5365)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeSize", value)

    @builtins.property
    @jsii.member(jsii_name="volumeType")
    def volume_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "volumeType"))

    @volume_type.setter
    def volume_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4cd817adbead474af10e0d160f9240b096813b5f2fa10a7dafd0c9982f0d4f81)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SpotInstanceRequestRootBlockDevice]:
        return typing.cast(typing.Optional[SpotInstanceRequestRootBlockDevice], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SpotInstanceRequestRootBlockDevice],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96d522c576bfec11b177551a4ed7c1dd3dc597d9f74aa8e8def8d741d7cc8f78)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.spotInstanceRequest.SpotInstanceRequestTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete"},
)
class SpotInstanceRequestTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#create SpotInstanceRequest#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#delete SpotInstanceRequest#delete}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e22d1c5b4199ba8006e952b6cae10617c5653b5a2a2a588022857bdd127de30)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#create SpotInstanceRequest#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/spot_instance_request#delete SpotInstanceRequest#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SpotInstanceRequestTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SpotInstanceRequestTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.spotInstanceRequest.SpotInstanceRequestTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__02ef9e8835281cda38dff8139c3b04b8c2e2182fb1a15a3768802026c5805fdf)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8861f60ae8fea2d895b68a75580db4d68f3233e2c27ccffc861cf6dab0d1da46)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0dce9ea19e1466778fb48f09f7575b2a7d39bfc1b898c80eef8a4580d450cda1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SpotInstanceRequestTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SpotInstanceRequestTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SpotInstanceRequestTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d45cc4c336f7f55d24eebfee06e4f7b0aba0f61fdd27e38cae62cf668e5bde75)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "SpotInstanceRequest",
    "SpotInstanceRequestCapacityReservationSpecification",
    "SpotInstanceRequestCapacityReservationSpecificationCapacityReservationTarget",
    "SpotInstanceRequestCapacityReservationSpecificationCapacityReservationTargetOutputReference",
    "SpotInstanceRequestCapacityReservationSpecificationOutputReference",
    "SpotInstanceRequestConfig",
    "SpotInstanceRequestCreditSpecification",
    "SpotInstanceRequestCreditSpecificationOutputReference",
    "SpotInstanceRequestEbsBlockDevice",
    "SpotInstanceRequestEbsBlockDeviceList",
    "SpotInstanceRequestEbsBlockDeviceOutputReference",
    "SpotInstanceRequestEnclaveOptions",
    "SpotInstanceRequestEnclaveOptionsOutputReference",
    "SpotInstanceRequestEphemeralBlockDevice",
    "SpotInstanceRequestEphemeralBlockDeviceList",
    "SpotInstanceRequestEphemeralBlockDeviceOutputReference",
    "SpotInstanceRequestLaunchTemplate",
    "SpotInstanceRequestLaunchTemplateOutputReference",
    "SpotInstanceRequestMaintenanceOptions",
    "SpotInstanceRequestMaintenanceOptionsOutputReference",
    "SpotInstanceRequestMetadataOptions",
    "SpotInstanceRequestMetadataOptionsOutputReference",
    "SpotInstanceRequestNetworkInterface",
    "SpotInstanceRequestNetworkInterfaceList",
    "SpotInstanceRequestNetworkInterfaceOutputReference",
    "SpotInstanceRequestPrivateDnsNameOptions",
    "SpotInstanceRequestPrivateDnsNameOptionsOutputReference",
    "SpotInstanceRequestRootBlockDevice",
    "SpotInstanceRequestRootBlockDeviceOutputReference",
    "SpotInstanceRequestTimeouts",
    "SpotInstanceRequestTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__25ea7dd1d51135d82eccce6caca2a8c8842ffb0c070bfd3aa088422f16e3446d(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    ami: typing.Optional[builtins.str] = None,
    associate_public_ip_address: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    availability_zone: typing.Optional[builtins.str] = None,
    block_duration_minutes: typing.Optional[jsii.Number] = None,
    capacity_reservation_specification: typing.Optional[typing.Union[SpotInstanceRequestCapacityReservationSpecification, typing.Dict[builtins.str, typing.Any]]] = None,
    cpu_core_count: typing.Optional[jsii.Number] = None,
    cpu_threads_per_core: typing.Optional[jsii.Number] = None,
    credit_specification: typing.Optional[typing.Union[SpotInstanceRequestCreditSpecification, typing.Dict[builtins.str, typing.Any]]] = None,
    disable_api_stop: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    disable_api_termination: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ebs_block_device: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SpotInstanceRequestEbsBlockDevice, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ebs_optimized: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    enclave_options: typing.Optional[typing.Union[SpotInstanceRequestEnclaveOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    ephemeral_block_device: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SpotInstanceRequestEphemeralBlockDevice, typing.Dict[builtins.str, typing.Any]]]]] = None,
    fetch_password_data: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    hibernation: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    host_id: typing.Optional[builtins.str] = None,
    host_resource_group_arn: typing.Optional[builtins.str] = None,
    iam_instance_profile: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    instance_initiated_shutdown_behavior: typing.Optional[builtins.str] = None,
    instance_interruption_behavior: typing.Optional[builtins.str] = None,
    instance_type: typing.Optional[builtins.str] = None,
    ipv6_address_count: typing.Optional[jsii.Number] = None,
    ipv6_addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
    key_name: typing.Optional[builtins.str] = None,
    launch_group: typing.Optional[builtins.str] = None,
    launch_template: typing.Optional[typing.Union[SpotInstanceRequestLaunchTemplate, typing.Dict[builtins.str, typing.Any]]] = None,
    maintenance_options: typing.Optional[typing.Union[SpotInstanceRequestMaintenanceOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    metadata_options: typing.Optional[typing.Union[SpotInstanceRequestMetadataOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    monitoring: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    network_interface: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SpotInstanceRequestNetworkInterface, typing.Dict[builtins.str, typing.Any]]]]] = None,
    placement_group: typing.Optional[builtins.str] = None,
    placement_partition_number: typing.Optional[jsii.Number] = None,
    private_dns_name_options: typing.Optional[typing.Union[SpotInstanceRequestPrivateDnsNameOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    private_ip: typing.Optional[builtins.str] = None,
    root_block_device: typing.Optional[typing.Union[SpotInstanceRequestRootBlockDevice, typing.Dict[builtins.str, typing.Any]]] = None,
    secondary_private_ips: typing.Optional[typing.Sequence[builtins.str]] = None,
    security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    source_dest_check: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    spot_price: typing.Optional[builtins.str] = None,
    spot_type: typing.Optional[builtins.str] = None,
    subnet_id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tenancy: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[SpotInstanceRequestTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    user_data: typing.Optional[builtins.str] = None,
    user_data_base64: typing.Optional[builtins.str] = None,
    user_data_replace_on_change: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    valid_from: typing.Optional[builtins.str] = None,
    valid_until: typing.Optional[builtins.str] = None,
    volume_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    vpc_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    wait_for_fulfillment: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
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

def _typecheckingstub__8c7c5af28b5968250405d798a2b3a9d27933abb50b78c3f81735749389a795a4(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SpotInstanceRequestEbsBlockDevice, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1da975b60399bbb9ff8e2ad351a84b68dee671e0812fa83d4a76e0e26f5194d8(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SpotInstanceRequestEphemeralBlockDevice, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a002308f66e4cc08f67ad66ed7011b96da8bb68be771de2cabe7a60d1cf167e(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SpotInstanceRequestNetworkInterface, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__182b53f86c7b5156dcc95d10cf8292ca8dfe2efa92a1f5a56f67f7b5fb05fbd7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ac2fa63b20b5b772d4b30634b7c9efc26342739ec1439c6cbfeae9ac2bdb8d6(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4ce12b17b0376fbd5fe38c90ada79b82ce473ac9aeeb096d030fb4da5af32d2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7dbfc636165504c887300da45cb103da42dc62515ba5379690a7c5e94a461a4(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b73dc530974b9ba18f3083557856d4cd63243cceb42bfdcd8fcd2efaf9ab4cd(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d63c81d404735cd6c986c71b6ab1813656009d50f179eade3148a2bda4d61039(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__906e29a235f7d3473eb047a188f56da1263bdcdba2a1a0bf831b43db0d3c3e87(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bfff62e582a7238b1cde671d447128bf0c12419f869379a4b9a14ca482023f6f(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__575eed9637b9d7f394ca033f8e0a67e69693611ba57f92db69cd12304c5b4e78(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0288801e82b5ffc7ca3a96a00432098aa97e926f1410362aa053af8934ddca1f(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb3e45944d2852715e060f3097048d0c12983b9de1a66a24217d7655d49fb79f(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b4afef057bae9d76daee52d750671df9fcf93e67964ae5dcd5e02b4fb2a820c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e589a4cd78082ee1138bb6776ab6f782e46fa42d184d2c3aab2e1ce13ab1a4f0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2be21761676471da55c278ddb70ea9e1b4866dac06bc20c7f104d4592d596e4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e660632944fb773681ad2de576827caf0ba87093b5e927939f9ff67d52cbc6cf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88277119fd2f3feb077c0f6a9334cfb9789443b51f1ae26feb7b49844ba9f442(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39e499c03221c9cca8c75dd807379de463e884ab29335beb7beb7ed617826f7a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57ef8df493d52ffd14205ed3b810c5f754967d6a5d3e15df3bd73bc7b776c62d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__508c91e20ad825bba97bfe7073d9b706a2a684580737d4e0bf305e257dc043e4(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__996d5834e3831763ea41c5675c14f684c6842874ea1327f818b09a58a0260aaf(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14f96b4d879f552fb24ed3408bab2c67b306d2b8b4f04ad0b9db4564c94b203b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__867903f29a9c80452a38d65dce39fe410353a3ca1dd054149cae7d595cae0814(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1786aceda2a9257d385621efab8d2baaed871d1d24d790332a97531e14d21acb(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a115e3e1b68650cc470380a96bee704824fb2abc6b5a63ecc6589361d0280804(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac5815e205e57684085e04c297c791dace2c57bc2db59cd7f674956dd4a30709(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3566d9970b84df6c7248a3a366f4db4c9af00052716159d0c083939164a97288(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d030a08f7408ed782c7b6dc1260f5741e6ec0a5d6a0c3696331039415f07afc(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9309a9a46b20c2abd72fee01a58baf1f4769e40f5ef6b01db285fe0492e2e5a(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70be4526538199668d949e05763ead00e7c87b544cda6b596362606d3cfe1537(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9a415deea11aa3d3b313ab49a8774a05c449853344cfa32f8ef6a894dd938e1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__923fc0a07b1db51126f585646201a723cb3a35f70f60a696bcb283e911f5dc9a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__768d91fc4a33d180f1c7c193d95ad7f3ac4654dc63db596cbc4c848d9520a9ba(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f59101e1e596058735fb225299a06713cdec64973b4aaf54f33ca6d341a5c47f(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d75d4631cd2eaf31b511a874c034eddecbbaf72032555431772e0e8dd13b70f(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2533851e9c5f66e4bf9996582123ef73c1ee11c4c39f52e6360b912ecc586d8d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3de817635d31a2a2213c4b47df3d6081642f4e296c260ea589aae1bb735e3bd1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__671a106cf39e77ddbfe6feb3d3763f994a21f85c724eb9d2ab4dc8c681bb9c18(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__046eb88ac82edf7c740130d087cca435b0da9ebf8091e2156be14e30123cf8d0(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2dbcba76945a76a60592bc4815caf8384b816f8ed030eb1b4d86176535cf8e8a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66fc6970806e5b56a655aa3239e2fe87c51e0bf4c6d8f751311637ade3af77b8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5fddbeeca69d843de21529c29f9c09cba370c88404a47cb9b8a783dff8261f00(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad369ab838cb2dfc845f13ba890d359d51ca84021c1f62fec5065e7f0e9d7596(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b0b29defa5f86ac71a91e0cfd9419de1cb4b3cd2d25e632478ccfe99950da74(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e6c692a08eb8853820728c6b38efcae4dd708789049cca8eeeb3b5d0a0ff222(
    *,
    capacity_reservation_preference: typing.Optional[builtins.str] = None,
    capacity_reservation_target: typing.Optional[typing.Union[SpotInstanceRequestCapacityReservationSpecificationCapacityReservationTarget, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7673c17457331e0fed6e1f8468ae8dbe83ada5c9229fdac24bfdb2b45f504843(
    *,
    capacity_reservation_id: typing.Optional[builtins.str] = None,
    capacity_reservation_resource_group_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fba7fc93adcc4725fb031196c31ff2bd5c1db79805db60bd2509e06a78a909d7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b442a3490e5979d150afe94485aa46e704ef813dd833b857253579458555437(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c892d45b1f4ede7710ef682daecca0cbb2baf34cf6fd17c7cfce43649bf222f0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2fb82879285e6f8d1574be347ff7a89a5a666caae462a546ee27c3270e7bf099(
    value: typing.Optional[SpotInstanceRequestCapacityReservationSpecificationCapacityReservationTarget],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7dd9c42729bd67b9a38ec3099fb8db80fdc838e4cda19aec33748783a7f5555(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e385f10f7c53e00992612e3d45e325154636cc5a806d83b5f4e2f971173c91ab(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a905a7919ea9d2bfc88162aa5aa2895721c27a44c700e506f639c45e4662868(
    value: typing.Optional[SpotInstanceRequestCapacityReservationSpecification],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2603250aaba1895da385b33179b9cc410e3d20fd73a968763f51db324c598ac6(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ami: typing.Optional[builtins.str] = None,
    associate_public_ip_address: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    availability_zone: typing.Optional[builtins.str] = None,
    block_duration_minutes: typing.Optional[jsii.Number] = None,
    capacity_reservation_specification: typing.Optional[typing.Union[SpotInstanceRequestCapacityReservationSpecification, typing.Dict[builtins.str, typing.Any]]] = None,
    cpu_core_count: typing.Optional[jsii.Number] = None,
    cpu_threads_per_core: typing.Optional[jsii.Number] = None,
    credit_specification: typing.Optional[typing.Union[SpotInstanceRequestCreditSpecification, typing.Dict[builtins.str, typing.Any]]] = None,
    disable_api_stop: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    disable_api_termination: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ebs_block_device: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SpotInstanceRequestEbsBlockDevice, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ebs_optimized: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    enclave_options: typing.Optional[typing.Union[SpotInstanceRequestEnclaveOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    ephemeral_block_device: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SpotInstanceRequestEphemeralBlockDevice, typing.Dict[builtins.str, typing.Any]]]]] = None,
    fetch_password_data: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    hibernation: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    host_id: typing.Optional[builtins.str] = None,
    host_resource_group_arn: typing.Optional[builtins.str] = None,
    iam_instance_profile: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    instance_initiated_shutdown_behavior: typing.Optional[builtins.str] = None,
    instance_interruption_behavior: typing.Optional[builtins.str] = None,
    instance_type: typing.Optional[builtins.str] = None,
    ipv6_address_count: typing.Optional[jsii.Number] = None,
    ipv6_addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
    key_name: typing.Optional[builtins.str] = None,
    launch_group: typing.Optional[builtins.str] = None,
    launch_template: typing.Optional[typing.Union[SpotInstanceRequestLaunchTemplate, typing.Dict[builtins.str, typing.Any]]] = None,
    maintenance_options: typing.Optional[typing.Union[SpotInstanceRequestMaintenanceOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    metadata_options: typing.Optional[typing.Union[SpotInstanceRequestMetadataOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    monitoring: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    network_interface: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SpotInstanceRequestNetworkInterface, typing.Dict[builtins.str, typing.Any]]]]] = None,
    placement_group: typing.Optional[builtins.str] = None,
    placement_partition_number: typing.Optional[jsii.Number] = None,
    private_dns_name_options: typing.Optional[typing.Union[SpotInstanceRequestPrivateDnsNameOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    private_ip: typing.Optional[builtins.str] = None,
    root_block_device: typing.Optional[typing.Union[SpotInstanceRequestRootBlockDevice, typing.Dict[builtins.str, typing.Any]]] = None,
    secondary_private_ips: typing.Optional[typing.Sequence[builtins.str]] = None,
    security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    source_dest_check: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    spot_price: typing.Optional[builtins.str] = None,
    spot_type: typing.Optional[builtins.str] = None,
    subnet_id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tenancy: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[SpotInstanceRequestTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    user_data: typing.Optional[builtins.str] = None,
    user_data_base64: typing.Optional[builtins.str] = None,
    user_data_replace_on_change: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    valid_from: typing.Optional[builtins.str] = None,
    valid_until: typing.Optional[builtins.str] = None,
    volume_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    vpc_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    wait_for_fulfillment: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f01d9e27c68776cac4783bf2aa6b32242f8ec92351f2ff6cdb8be29ab50004f5(
    *,
    cpu_credits: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d3087ce8852c04b986df030cb6353ffd63be860b6c47081d51a58759e03daf6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25bb8c85bdaefa3499ab51de09844545367ff35f31ab520f6291a842a8bf4b03(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4eace2a65eb0c22771b673e0b0db9e43743ca11b00da0bd9eae396ee29205b84(
    value: typing.Optional[SpotInstanceRequestCreditSpecification],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc8c3a14338c02affe16e702866edfc6902ec707eea2202ddb2e761751deb197(
    *,
    device_name: builtins.str,
    delete_on_termination: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    encrypted: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    iops: typing.Optional[jsii.Number] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    snapshot_id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    throughput: typing.Optional[jsii.Number] = None,
    volume_size: typing.Optional[jsii.Number] = None,
    volume_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7eaf757afe4edb513d6c685bcafbfb50f17d32e561a5d305904eef377596f962(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6760f6d41506153545069bc7f8af362597640d3f5d2335f19df98cd8e7ca5f27(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3634a17bedee982dd57da45b280a7a0a09f4ecdc6f8d18e5c5c2bbe113cfd914(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d68cef748ac76a07b5b8862522076d0fe9cd950f9b0c3878c0911f56b96edbd1(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3cc78b3284b8e5ff23bfdfbbcbe3c1a4b7b4413593edf11a41e01e473f884e5(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1cdf11af7b05bbd5fa4f23fb0b52dfe17fede1c9b2e878ff5464e5a8b7ee9a6c(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SpotInstanceRequestEbsBlockDevice]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58cc8dc06c9c5556df34630afc621e2e233ba251307ce10559de91efbf28d013(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ddd96ad5d48605cf34a32c51ced2c8bd4955858a92a3cabcb6829259b9ae9ec(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c110075e4cc7b17498fa8af2f249aa476dbf993f9da6fb4f7d4c6bae1d3ff4d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4bbf77c7aadf00ee5e6a19665494286ff98146a7c7bb8448838924a8ea05a67d(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6cf06f3911d80963454a111d13fb9ce58f8620cdb6b666f2ad5c9f318ddc5dd4(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09480438bbdd1c881dfb081b32017dc98deb85732f3ad13e17bd13d40e4025d4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__366716ce64288c39f08b97118f07ac217a975612aa54cebcb63cfcf1e98bc055(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b17a86ac30e09bc0469b69282d6aa85659a79e95463b02723bb06204cf5c11d3(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7828111dc93427b202e943b5033815153caaa19a4ab840241e584cb556591a0c(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__597ecc3fed45ff6c94a884892e4fbf82d72a9df14700731d888f1c708612835a(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__523cb2fe49e11abcabf056eeaf2334105f9e674b3a5f5566d92f99922c9c6b4a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d7efa953f1877349631fcefab5c337f39817d73d83036d69d6813a52e9b47cd(
    value: typing.Optional[typing.Union[SpotInstanceRequestEbsBlockDevice, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08cdadfe3625ad91a38f81a19a72b801c27af060b8e482dc37585a7695df0fc9(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__212741adc100ffc730c7a7f5269ff6c8529b555f3155a00464928dd9f198543d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61807d5e111b027e8b23102419ace8a0119b92bee2cda8b904e7b456c23d7a4b(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13222cc0e526231401bbe4a4e239f782790c6f794c18fe77d9d00ad32fde49d2(
    value: typing.Optional[SpotInstanceRequestEnclaveOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b8b9f9c704d54d304d637aba753688009d2f34f89bef9626f247885fca93247(
    *,
    device_name: builtins.str,
    no_device: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    virtual_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a0c335a6f08b446d659f9e3d76a4f48aadb9c18596f13a5609d9ff788b6ff9a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__208f2fc0a560d367cc5fdb30bacb062f421b8fd4699171be0def12e01af1ec4c(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c2b132bdb5e9e11b3124aae04002cd869b2073917838f9904afaa2ab3f8a1c5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8f50e01a524c485706826455cbe8dea4fbdd4d300af3c3c79edcd7f6e137b78(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d960132322f177877288a3776b80e8dd70221f8a826e3359112baed57cf93843(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d444305b3a2b3bb049118a4b51ba4a1ad6f4d7e93ff4a5a08092110b9c79585(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SpotInstanceRequestEphemeralBlockDevice]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0976a31e9c3f97c04ec712ae968962e4efa3e473263609bff6c05d9f68292d0f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__133a750cfbd9d36163ff45877d1ce92a75e0710d010121ddc97e64fabcd2eeb3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da1f7f8e79ed1f41709aee03ddb1b76443b20a3645fd078e5f859a095a2d9520(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8d7b19086836e4d0de355184e3e81e5b6bf39c47835f5c8f94256eae3d255f8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__420e189daeb046f94cb84289225fb8ac89f16c65b92f19d14197a37edb160c45(
    value: typing.Optional[typing.Union[SpotInstanceRequestEphemeralBlockDevice, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7469d461fa7079233db94028ca43c6ceead9470c68b0c391e71b1663a3bd4025(
    *,
    id: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1f48e972c6e4bb2f70b205112551396100f7a1f1e80e16087d92aff088ec56c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bcb447a886ef558020ad5f9e5acb398ac234e8996591205fb7160bfc6819fb74(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ea82f72bd2edd696b4112e23c39431fb50a6fac79a973ad856627d910f4b6d9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72e3284e9850db2750c54dd08de70da9b81736064296868970897277018fe501(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e85082d4ad44e09a442ede6d13086f6ae8846fdcda26265e03e0246ab00e3b9(
    value: typing.Optional[SpotInstanceRequestLaunchTemplate],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12826429a97ff07ee728166cea15bad545df63da140673029debc57c3f3cd09d(
    *,
    auto_recovery: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3cef8368235b362b6fc52482e2bc7a33e6ac8f4cf9ccef94865dc7ab9011be59(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c008efa7e7d2436107a9fe8c376ff4824d3e776afa9c3d6877a451c1efb2839d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32964d4c2a186c8dc2aa4687ca090b0d227fc9ed03a638e259dd49f4d55308ba(
    value: typing.Optional[SpotInstanceRequestMaintenanceOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d0020c1ace79b7db4fb0215b9be49e8e0f44923ec6ee18f9f59ff72552f86d0(
    *,
    http_endpoint: typing.Optional[builtins.str] = None,
    http_put_response_hop_limit: typing.Optional[jsii.Number] = None,
    http_tokens: typing.Optional[builtins.str] = None,
    instance_metadata_tags: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ca4eb2f73e76e6a0c01486515a40cb602e257dcd4fbb7edf99423dc75e15f11(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b766de8c2216e4d7a9235facb4595206788aebade0e08b61cb78b420a6100db7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29f65185bc783ff223ed45c9da3e0705991628898d4dd69b6f9ce4944cd5a824(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6410b750c6d025e0fcb1040b6b57704a3ac6894159ddf0f7e0d436458b3c6d7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d36e90e63b7a121c2c578db8bf6161623273af24b1b6a1768ceec980f301810f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a31e17f76630c1e7dba8738f17b3c567e1ccdf99ac25873bc588a2e7210f58c1(
    value: typing.Optional[SpotInstanceRequestMetadataOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d26723a85e43ffa26c5fc268d5a8af19e8ed0f179aeb2dbbc07aa55b2b58166(
    *,
    device_index: jsii.Number,
    network_interface_id: builtins.str,
    delete_on_termination: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    network_card_index: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee585565799e51d9bbe617daccfeecd0b6cbb2fe602f6920384fc7248089c398(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a182a3acf21d8ac2b5466cc66d06b6c9c868b0c05cc71b3a4d3d8d528e436cd(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b99ba8201dc2dfdcf99d187ca6e706be438d6090e2ed5e509dc9cc1bd7585d08(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f79496f3b137c7d380e95e334884b9d6c6a99c3238dd608011d8e76e7a3e5607(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c473318dd7de892bad81105a75e049e5724c5ba394d302edd136ddafda175b2f(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__356cdee787f5d750da2bbae1fdaa0aa383efa6c0809a3fec1f144127b671f580(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SpotInstanceRequestNetworkInterface]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6412bcf6d4d67dab5efa1a6928f2e03e25613027880c748d68bfe1493bedc54(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7151b76c5f73856b1af401b8a694d12b94cca69b7aa686919664a5bdab8e6e0(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6529ce4fb893de43753eee385f3fedc38ece2191f68d1506a5bae4841cd37e18(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__963386f89e1ffaade92f2702f0506be70009685db8d7e7943902466fe527de1d(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9fee919787dc7f28e4424f2be802754760fdca718936c063ee8ac74faa635be(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ef9b189fc7b4a1ee9a99d590f55a6c2fbdab7db8e01cc1bc42fa522c4724c39(
    value: typing.Optional[typing.Union[SpotInstanceRequestNetworkInterface, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4cf8b3311b814ebd1527b3b54b693d2d9f228f9e765b08a6fa2d0d65b6d3237(
    *,
    enable_resource_name_dns_aaaa_record: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    enable_resource_name_dns_a_record: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    hostname_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__815b86437db9fd63fd45b54aafaf35f466c0f7fe8015de2c40085bc060511d7f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f9860056bfb1906dd10397b32dae1592d7da824915a5da0fa8e4ef45e8b0d0d(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e45bf7b97b80facc860bbd6f2e51eba87864727aa1a904ed486cd0aaf9b346a(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66de66197c5b8bb64cebf7316f8dafd5d9034cecb233179e6df985aec1b0e067(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c9f0e65e917456c9426830a0a5cf0278b41141f28f418c319de30f99b72f27b(
    value: typing.Optional[SpotInstanceRequestPrivateDnsNameOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1e4fe5d198dbb2503594e0f0c28a59fd2b60b6d899306077e5b3aae9578569a(
    *,
    delete_on_termination: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    encrypted: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    iops: typing.Optional[jsii.Number] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    throughput: typing.Optional[jsii.Number] = None,
    volume_size: typing.Optional[jsii.Number] = None,
    volume_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c02a2cb345215cb609138f52a2149814aed5d8bb729e37897dd8b8189cce63d9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__082d17c02e845a1c6cf6f043a1edc9c3ee57535931bc5739b0b89d24e583c2f6(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84d389e6c75fbfe24b77fa9d95d60a20cd4b1b3756b54638bd27808c8cd4f5b1(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1dcc9c34e6c4d848b8ea51baecadadc8066125861df58c85023ce926aa5ea047(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d606e00fb8fcd6f2b41c406c997abd509721fbf920771582610f7902e6a5add(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b1f73071519e10f50dc5d37e2dffcfc4808fc80dbe0355c1c9e40f13ac2a29e(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3aa939d5a825ad1965d914a9ee23b2e94ae8deb6e7ce06cfe0c1f06a14f002e0(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a1c3f12cea9ff71f0b0c13098559a714d55f510e8c6bae9e4248621800f5365(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4cd817adbead474af10e0d160f9240b096813b5f2fa10a7dafd0c9982f0d4f81(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96d522c576bfec11b177551a4ed7c1dd3dc597d9f74aa8e8def8d741d7cc8f78(
    value: typing.Optional[SpotInstanceRequestRootBlockDevice],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e22d1c5b4199ba8006e952b6cae10617c5653b5a2a2a588022857bdd127de30(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02ef9e8835281cda38dff8139c3b04b8c2e2182fb1a15a3768802026c5805fdf(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8861f60ae8fea2d895b68a75580db4d68f3233e2c27ccffc861cf6dab0d1da46(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0dce9ea19e1466778fb48f09f7575b2a7d39bfc1b898c80eef8a4580d450cda1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d45cc4c336f7f55d24eebfee06e4f7b0aba0f61fdd27e38cae62cf668e5bde75(
    value: typing.Optional[typing.Union[SpotInstanceRequestTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
