'''
# `aws_instance`

Refer to the Terraform Registory for docs: [`aws_instance`](https://www.terraform.io/docs/providers/aws/r/instance).
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


class Instance(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.instance.Instance",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/instance aws_instance}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        ami: typing.Optional[builtins.str] = None,
        associate_public_ip_address: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        availability_zone: typing.Optional[builtins.str] = None,
        capacity_reservation_specification: typing.Optional[typing.Union["InstanceCapacityReservationSpecification", typing.Dict[builtins.str, typing.Any]]] = None,
        cpu_core_count: typing.Optional[jsii.Number] = None,
        cpu_threads_per_core: typing.Optional[jsii.Number] = None,
        credit_specification: typing.Optional[typing.Union["InstanceCreditSpecification", typing.Dict[builtins.str, typing.Any]]] = None,
        disable_api_stop: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        disable_api_termination: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        ebs_block_device: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["InstanceEbsBlockDevice", typing.Dict[builtins.str, typing.Any]]]]] = None,
        ebs_optimized: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enclave_options: typing.Optional[typing.Union["InstanceEnclaveOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        ephemeral_block_device: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["InstanceEphemeralBlockDevice", typing.Dict[builtins.str, typing.Any]]]]] = None,
        fetch_password_data: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        hibernation: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        host_id: typing.Optional[builtins.str] = None,
        host_resource_group_arn: typing.Optional[builtins.str] = None,
        iam_instance_profile: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        instance_initiated_shutdown_behavior: typing.Optional[builtins.str] = None,
        instance_type: typing.Optional[builtins.str] = None,
        ipv6_address_count: typing.Optional[jsii.Number] = None,
        ipv6_addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
        key_name: typing.Optional[builtins.str] = None,
        launch_template: typing.Optional[typing.Union["InstanceLaunchTemplate", typing.Dict[builtins.str, typing.Any]]] = None,
        maintenance_options: typing.Optional[typing.Union["InstanceMaintenanceOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        metadata_options: typing.Optional[typing.Union["InstanceMetadataOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        monitoring: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        network_interface: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["InstanceNetworkInterface", typing.Dict[builtins.str, typing.Any]]]]] = None,
        placement_group: typing.Optional[builtins.str] = None,
        placement_partition_number: typing.Optional[jsii.Number] = None,
        private_dns_name_options: typing.Optional[typing.Union["InstancePrivateDnsNameOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        private_ip: typing.Optional[builtins.str] = None,
        root_block_device: typing.Optional[typing.Union["InstanceRootBlockDevice", typing.Dict[builtins.str, typing.Any]]] = None,
        secondary_private_ips: typing.Optional[typing.Sequence[builtins.str]] = None,
        security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        source_dest_check: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        subnet_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tenancy: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["InstanceTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        user_data: typing.Optional[builtins.str] = None,
        user_data_base64: typing.Optional[builtins.str] = None,
        user_data_replace_on_change: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        volume_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        vpc_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/instance aws_instance} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param ami: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#ami Instance#ami}.
        :param associate_public_ip_address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#associate_public_ip_address Instance#associate_public_ip_address}.
        :param availability_zone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#availability_zone Instance#availability_zone}.
        :param capacity_reservation_specification: capacity_reservation_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#capacity_reservation_specification Instance#capacity_reservation_specification}
        :param cpu_core_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#cpu_core_count Instance#cpu_core_count}.
        :param cpu_threads_per_core: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#cpu_threads_per_core Instance#cpu_threads_per_core}.
        :param credit_specification: credit_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#credit_specification Instance#credit_specification}
        :param disable_api_stop: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#disable_api_stop Instance#disable_api_stop}.
        :param disable_api_termination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#disable_api_termination Instance#disable_api_termination}.
        :param ebs_block_device: ebs_block_device block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#ebs_block_device Instance#ebs_block_device}
        :param ebs_optimized: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#ebs_optimized Instance#ebs_optimized}.
        :param enclave_options: enclave_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#enclave_options Instance#enclave_options}
        :param ephemeral_block_device: ephemeral_block_device block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#ephemeral_block_device Instance#ephemeral_block_device}
        :param fetch_password_data: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#get_password_data Instance#get_password_data}.
        :param hibernation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#hibernation Instance#hibernation}.
        :param host_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#host_id Instance#host_id}.
        :param host_resource_group_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#host_resource_group_arn Instance#host_resource_group_arn}.
        :param iam_instance_profile: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#iam_instance_profile Instance#iam_instance_profile}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#id Instance#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param instance_initiated_shutdown_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#instance_initiated_shutdown_behavior Instance#instance_initiated_shutdown_behavior}.
        :param instance_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#instance_type Instance#instance_type}.
        :param ipv6_address_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#ipv6_address_count Instance#ipv6_address_count}.
        :param ipv6_addresses: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#ipv6_addresses Instance#ipv6_addresses}.
        :param key_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#key_name Instance#key_name}.
        :param launch_template: launch_template block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#launch_template Instance#launch_template}
        :param maintenance_options: maintenance_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#maintenance_options Instance#maintenance_options}
        :param metadata_options: metadata_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#metadata_options Instance#metadata_options}
        :param monitoring: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#monitoring Instance#monitoring}.
        :param network_interface: network_interface block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#network_interface Instance#network_interface}
        :param placement_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#placement_group Instance#placement_group}.
        :param placement_partition_number: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#placement_partition_number Instance#placement_partition_number}.
        :param private_dns_name_options: private_dns_name_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#private_dns_name_options Instance#private_dns_name_options}
        :param private_ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#private_ip Instance#private_ip}.
        :param root_block_device: root_block_device block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#root_block_device Instance#root_block_device}
        :param secondary_private_ips: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#secondary_private_ips Instance#secondary_private_ips}.
        :param security_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#security_groups Instance#security_groups}.
        :param source_dest_check: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#source_dest_check Instance#source_dest_check}.
        :param subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#subnet_id Instance#subnet_id}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#tags Instance#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#tags_all Instance#tags_all}.
        :param tenancy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#tenancy Instance#tenancy}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#timeouts Instance#timeouts}
        :param user_data: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#user_data Instance#user_data}.
        :param user_data_base64: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#user_data_base64 Instance#user_data_base64}.
        :param user_data_replace_on_change: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#user_data_replace_on_change Instance#user_data_replace_on_change}.
        :param volume_tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#volume_tags Instance#volume_tags}.
        :param vpc_security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#vpc_security_group_ids Instance#vpc_security_group_ids}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e8d55dc87293dc31cb0e6b2998b30d68cbef4b407d3ecccbd6d98097ead1ebf)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = InstanceConfig(
            ami=ami,
            associate_public_ip_address=associate_public_ip_address,
            availability_zone=availability_zone,
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
            instance_type=instance_type,
            ipv6_address_count=ipv6_address_count,
            ipv6_addresses=ipv6_addresses,
            key_name=key_name,
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
            subnet_id=subnet_id,
            tags=tags,
            tags_all=tags_all,
            tenancy=tenancy,
            timeouts=timeouts,
            user_data=user_data,
            user_data_base64=user_data_base64,
            user_data_replace_on_change=user_data_replace_on_change,
            volume_tags=volume_tags,
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

    @jsii.member(jsii_name="putCapacityReservationSpecification")
    def put_capacity_reservation_specification(
        self,
        *,
        capacity_reservation_preference: typing.Optional[builtins.str] = None,
        capacity_reservation_target: typing.Optional[typing.Union["InstanceCapacityReservationSpecificationCapacityReservationTarget", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param capacity_reservation_preference: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#capacity_reservation_preference Instance#capacity_reservation_preference}.
        :param capacity_reservation_target: capacity_reservation_target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#capacity_reservation_target Instance#capacity_reservation_target}
        '''
        value = InstanceCapacityReservationSpecification(
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
        :param cpu_credits: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#cpu_credits Instance#cpu_credits}.
        '''
        value = InstanceCreditSpecification(cpu_credits=cpu_credits)

        return typing.cast(None, jsii.invoke(self, "putCreditSpecification", [value]))

    @jsii.member(jsii_name="putEbsBlockDevice")
    def put_ebs_block_device(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["InstanceEbsBlockDevice", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__693f73f01597266ce5944c40fa45b198793e60fd15463228ac5709605a08ef6c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putEbsBlockDevice", [value]))

    @jsii.member(jsii_name="putEnclaveOptions")
    def put_enclave_options(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#enabled Instance#enabled}.
        '''
        value = InstanceEnclaveOptions(enabled=enabled)

        return typing.cast(None, jsii.invoke(self, "putEnclaveOptions", [value]))

    @jsii.member(jsii_name="putEphemeralBlockDevice")
    def put_ephemeral_block_device(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["InstanceEphemeralBlockDevice", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__593555a4452d5eddb688153f85ee7c06d6bbc2622a7937959587485a6dd02ce2)
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
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#id Instance#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#name Instance#name}.
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#version Instance#version}.
        '''
        value = InstanceLaunchTemplate(id=id, name=name, version=version)

        return typing.cast(None, jsii.invoke(self, "putLaunchTemplate", [value]))

    @jsii.member(jsii_name="putMaintenanceOptions")
    def put_maintenance_options(
        self,
        *,
        auto_recovery: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param auto_recovery: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#auto_recovery Instance#auto_recovery}.
        '''
        value = InstanceMaintenanceOptions(auto_recovery=auto_recovery)

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
        :param http_endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#http_endpoint Instance#http_endpoint}.
        :param http_put_response_hop_limit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#http_put_response_hop_limit Instance#http_put_response_hop_limit}.
        :param http_tokens: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#http_tokens Instance#http_tokens}.
        :param instance_metadata_tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#instance_metadata_tags Instance#instance_metadata_tags}.
        '''
        value = InstanceMetadataOptions(
            http_endpoint=http_endpoint,
            http_put_response_hop_limit=http_put_response_hop_limit,
            http_tokens=http_tokens,
            instance_metadata_tags=instance_metadata_tags,
        )

        return typing.cast(None, jsii.invoke(self, "putMetadataOptions", [value]))

    @jsii.member(jsii_name="putNetworkInterface")
    def put_network_interface(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["InstanceNetworkInterface", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__867d20f81a8001062ca64661b5f9df466060cf0a802bf25a6a2ce0b020b73195)
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
        :param enable_resource_name_dns_aaaa_record: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#enable_resource_name_dns_aaaa_record Instance#enable_resource_name_dns_aaaa_record}.
        :param enable_resource_name_dns_a_record: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#enable_resource_name_dns_a_record Instance#enable_resource_name_dns_a_record}.
        :param hostname_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#hostname_type Instance#hostname_type}.
        '''
        value = InstancePrivateDnsNameOptions(
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
        :param delete_on_termination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#delete_on_termination Instance#delete_on_termination}.
        :param encrypted: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#encrypted Instance#encrypted}.
        :param iops: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#iops Instance#iops}.
        :param kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#kms_key_id Instance#kms_key_id}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#tags Instance#tags}.
        :param throughput: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#throughput Instance#throughput}.
        :param volume_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#volume_size Instance#volume_size}.
        :param volume_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#volume_type Instance#volume_type}.
        '''
        value = InstanceRootBlockDevice(
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
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#create Instance#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#delete Instance#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#update Instance#update}.
        '''
        value = InstanceTimeouts(create=create, delete=delete, update=update)

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

    @jsii.member(jsii_name="resetVolumeTags")
    def reset_volume_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVolumeTags", []))

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
    @jsii.member(jsii_name="capacityReservationSpecification")
    def capacity_reservation_specification(
        self,
    ) -> "InstanceCapacityReservationSpecificationOutputReference":
        return typing.cast("InstanceCapacityReservationSpecificationOutputReference", jsii.get(self, "capacityReservationSpecification"))

    @builtins.property
    @jsii.member(jsii_name="creditSpecification")
    def credit_specification(self) -> "InstanceCreditSpecificationOutputReference":
        return typing.cast("InstanceCreditSpecificationOutputReference", jsii.get(self, "creditSpecification"))

    @builtins.property
    @jsii.member(jsii_name="ebsBlockDevice")
    def ebs_block_device(self) -> "InstanceEbsBlockDeviceList":
        return typing.cast("InstanceEbsBlockDeviceList", jsii.get(self, "ebsBlockDevice"))

    @builtins.property
    @jsii.member(jsii_name="enclaveOptions")
    def enclave_options(self) -> "InstanceEnclaveOptionsOutputReference":
        return typing.cast("InstanceEnclaveOptionsOutputReference", jsii.get(self, "enclaveOptions"))

    @builtins.property
    @jsii.member(jsii_name="ephemeralBlockDevice")
    def ephemeral_block_device(self) -> "InstanceEphemeralBlockDeviceList":
        return typing.cast("InstanceEphemeralBlockDeviceList", jsii.get(self, "ephemeralBlockDevice"))

    @builtins.property
    @jsii.member(jsii_name="instanceState")
    def instance_state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceState"))

    @builtins.property
    @jsii.member(jsii_name="launchTemplate")
    def launch_template(self) -> "InstanceLaunchTemplateOutputReference":
        return typing.cast("InstanceLaunchTemplateOutputReference", jsii.get(self, "launchTemplate"))

    @builtins.property
    @jsii.member(jsii_name="maintenanceOptions")
    def maintenance_options(self) -> "InstanceMaintenanceOptionsOutputReference":
        return typing.cast("InstanceMaintenanceOptionsOutputReference", jsii.get(self, "maintenanceOptions"))

    @builtins.property
    @jsii.member(jsii_name="metadataOptions")
    def metadata_options(self) -> "InstanceMetadataOptionsOutputReference":
        return typing.cast("InstanceMetadataOptionsOutputReference", jsii.get(self, "metadataOptions"))

    @builtins.property
    @jsii.member(jsii_name="networkInterface")
    def network_interface(self) -> "InstanceNetworkInterfaceList":
        return typing.cast("InstanceNetworkInterfaceList", jsii.get(self, "networkInterface"))

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
    ) -> "InstancePrivateDnsNameOptionsOutputReference":
        return typing.cast("InstancePrivateDnsNameOptionsOutputReference", jsii.get(self, "privateDnsNameOptions"))

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
    def root_block_device(self) -> "InstanceRootBlockDeviceOutputReference":
        return typing.cast("InstanceRootBlockDeviceOutputReference", jsii.get(self, "rootBlockDevice"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "InstanceTimeoutsOutputReference":
        return typing.cast("InstanceTimeoutsOutputReference", jsii.get(self, "timeouts"))

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
    @jsii.member(jsii_name="capacityReservationSpecificationInput")
    def capacity_reservation_specification_input(
        self,
    ) -> typing.Optional["InstanceCapacityReservationSpecification"]:
        return typing.cast(typing.Optional["InstanceCapacityReservationSpecification"], jsii.get(self, "capacityReservationSpecificationInput"))

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
    ) -> typing.Optional["InstanceCreditSpecification"]:
        return typing.cast(typing.Optional["InstanceCreditSpecification"], jsii.get(self, "creditSpecificationInput"))

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
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["InstanceEbsBlockDevice"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["InstanceEbsBlockDevice"]]], jsii.get(self, "ebsBlockDeviceInput"))

    @builtins.property
    @jsii.member(jsii_name="ebsOptimizedInput")
    def ebs_optimized_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "ebsOptimizedInput"))

    @builtins.property
    @jsii.member(jsii_name="enclaveOptionsInput")
    def enclave_options_input(self) -> typing.Optional["InstanceEnclaveOptions"]:
        return typing.cast(typing.Optional["InstanceEnclaveOptions"], jsii.get(self, "enclaveOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="ephemeralBlockDeviceInput")
    def ephemeral_block_device_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["InstanceEphemeralBlockDevice"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["InstanceEphemeralBlockDevice"]]], jsii.get(self, "ephemeralBlockDeviceInput"))

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
    @jsii.member(jsii_name="launchTemplateInput")
    def launch_template_input(self) -> typing.Optional["InstanceLaunchTemplate"]:
        return typing.cast(typing.Optional["InstanceLaunchTemplate"], jsii.get(self, "launchTemplateInput"))

    @builtins.property
    @jsii.member(jsii_name="maintenanceOptionsInput")
    def maintenance_options_input(
        self,
    ) -> typing.Optional["InstanceMaintenanceOptions"]:
        return typing.cast(typing.Optional["InstanceMaintenanceOptions"], jsii.get(self, "maintenanceOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="metadataOptionsInput")
    def metadata_options_input(self) -> typing.Optional["InstanceMetadataOptions"]:
        return typing.cast(typing.Optional["InstanceMetadataOptions"], jsii.get(self, "metadataOptionsInput"))

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
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["InstanceNetworkInterface"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["InstanceNetworkInterface"]]], jsii.get(self, "networkInterfaceInput"))

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
    ) -> typing.Optional["InstancePrivateDnsNameOptions"]:
        return typing.cast(typing.Optional["InstancePrivateDnsNameOptions"], jsii.get(self, "privateDnsNameOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="privateIpInput")
    def private_ip_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateIpInput"))

    @builtins.property
    @jsii.member(jsii_name="rootBlockDeviceInput")
    def root_block_device_input(self) -> typing.Optional["InstanceRootBlockDevice"]:
        return typing.cast(typing.Optional["InstanceRootBlockDevice"], jsii.get(self, "rootBlockDeviceInput"))

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
    ) -> typing.Optional[typing.Union["InstanceTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["InstanceTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

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
    @jsii.member(jsii_name="ami")
    def ami(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ami"))

    @ami.setter
    def ami(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01a0b9d394ae027f05619b363c59f24a2582ad2570326668fdd2603a4d9dd9ae)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d2bebd1eec6c8417d3152b4bd78f034b4178855fbd9a1aa41b5a584ca8a39311)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "associatePublicIpAddress", value)

    @builtins.property
    @jsii.member(jsii_name="availabilityZone")
    def availability_zone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "availabilityZone"))

    @availability_zone.setter
    def availability_zone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f27f005ee936668dd0c3ec9cf19128c6c082c7c70e5978fc6685bd37eb459328)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availabilityZone", value)

    @builtins.property
    @jsii.member(jsii_name="cpuCoreCount")
    def cpu_core_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "cpuCoreCount"))

    @cpu_core_count.setter
    def cpu_core_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fbab0ad5f392e66baaa47daf67761eed3d1f0336c9f47e13a8f26f9e70eaabe4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpuCoreCount", value)

    @builtins.property
    @jsii.member(jsii_name="cpuThreadsPerCore")
    def cpu_threads_per_core(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "cpuThreadsPerCore"))

    @cpu_threads_per_core.setter
    def cpu_threads_per_core(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b6673f1e29d387f7c991cc5072af21f028e4a2243e1c2629a8c7f545c0c3310)
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
            type_hints = typing.get_type_hints(_typecheckingstub__dd1e1c6d01926603b6f1fd8ba9f98ccc479206ba6a5787c269afa43dd857bd81)
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
            type_hints = typing.get_type_hints(_typecheckingstub__35ce2cba45fe76dc1b9dd7114e0981a6f5956e97ffe3aabb9dc820def66037a4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__060e74062f59aefee1b461885289b77f1a87d3b601f831e3713c66758891fec4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e2ab6e2d8cbb15b056f36a1423de0e5d5196283f485c2abfde1c283ef5ea26ac)
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
            type_hints = typing.get_type_hints(_typecheckingstub__bb3363fba13424721335a2b986fd3256ebf7d64de6434c26262f63a8bb1451a9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hibernation", value)

    @builtins.property
    @jsii.member(jsii_name="hostId")
    def host_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostId"))

    @host_id.setter
    def host_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f31be7c8c821bef709ad4a46d3b9152e72fc3f3e4c9a1807f63adac302cfb407)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostId", value)

    @builtins.property
    @jsii.member(jsii_name="hostResourceGroupArn")
    def host_resource_group_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostResourceGroupArn"))

    @host_resource_group_arn.setter
    def host_resource_group_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6e31deecefbf988610f74867879f1a0d5bc6db76ad822b10979738e42d7c6db)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostResourceGroupArn", value)

    @builtins.property
    @jsii.member(jsii_name="iamInstanceProfile")
    def iam_instance_profile(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "iamInstanceProfile"))

    @iam_instance_profile.setter
    def iam_instance_profile(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6e2cfcf5ffb2f1ef39297839896005fef7475ce855a67de6265e07687a102d3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iamInstanceProfile", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27b633a6c515b844c84fef4b49df9ce0aa0f313518082fab19da1bfe3f4bafa0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="instanceInitiatedShutdownBehavior")
    def instance_initiated_shutdown_behavior(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceInitiatedShutdownBehavior"))

    @instance_initiated_shutdown_behavior.setter
    def instance_initiated_shutdown_behavior(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__105364139b6ff4bbd3ca15ab648077727b77d0f7f1e9f86ba534ebd98aee5803)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceInitiatedShutdownBehavior", value)

    @builtins.property
    @jsii.member(jsii_name="instanceType")
    def instance_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceType"))

    @instance_type.setter
    def instance_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ef12c81496a03ea882cb304e3c01ab0c6f2220bdd97b75ed74612f7ae51cd04)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceType", value)

    @builtins.property
    @jsii.member(jsii_name="ipv6AddressCount")
    def ipv6_address_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ipv6AddressCount"))

    @ipv6_address_count.setter
    def ipv6_address_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66f9cf4fc2ffe0a337c347c8e53d1afa83d895378443695ecde97ae102dc1573)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipv6AddressCount", value)

    @builtins.property
    @jsii.member(jsii_name="ipv6Addresses")
    def ipv6_addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "ipv6Addresses"))

    @ipv6_addresses.setter
    def ipv6_addresses(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a2ea71aa9ed1eba27d797babe42c32de859c27324e8deb5c12929f7ca717fb9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipv6Addresses", value)

    @builtins.property
    @jsii.member(jsii_name="keyName")
    def key_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyName"))

    @key_name.setter
    def key_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__189bb180f738517b66a627d2c31fbfe4cad32642c5d03f0a533339bc9df84ee3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyName", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__027bd2d926b379ee3763b1d39a99d8622539c7b5ba88d3953bd3137258236ff9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "monitoring", value)

    @builtins.property
    @jsii.member(jsii_name="placementGroup")
    def placement_group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "placementGroup"))

    @placement_group.setter
    def placement_group(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ecf7f8c59d6d95dc01afc4c660cafe9960ccf3f8e719be6dfe16c922876d7521)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "placementGroup", value)

    @builtins.property
    @jsii.member(jsii_name="placementPartitionNumber")
    def placement_partition_number(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "placementPartitionNumber"))

    @placement_partition_number.setter
    def placement_partition_number(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c7bafd652431837fb9fbc73bdf55f07a82e211990cb7c6d9cf1a3aee56baeeb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "placementPartitionNumber", value)

    @builtins.property
    @jsii.member(jsii_name="privateIp")
    def private_ip(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateIp"))

    @private_ip.setter
    def private_ip(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__642b496bff52c044839005e1c11dea51787d00584dfdc70a309e4d7a9c68ce3e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateIp", value)

    @builtins.property
    @jsii.member(jsii_name="secondaryPrivateIps")
    def secondary_private_ips(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "secondaryPrivateIps"))

    @secondary_private_ips.setter
    def secondary_private_ips(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f475721baf9376560ac7e9ededbe1e7174605a9f5c65cacebb73b19b422968c7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secondaryPrivateIps", value)

    @builtins.property
    @jsii.member(jsii_name="securityGroups")
    def security_groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "securityGroups"))

    @security_groups.setter
    def security_groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06553c8be05181c04f89a7b65530e9fd671dfe3292e173b9fd594994500ea8ef)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a29eef2281b0b0a64bdef23d94b9056b3e8e2aa0295fe80c10453efeca66954c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceDestCheck", value)

    @builtins.property
    @jsii.member(jsii_name="subnetId")
    def subnet_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subnetId"))

    @subnet_id.setter
    def subnet_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5a9fab4949504867be73302b56f908fe5c91b7dc88379baaf5835ef4cc7e7ad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetId", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db19e627ab731257267605e4392faf1387a1ec5c70cda89c66c8007791960f29)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68cea80e70fc41846c08b429828201dcd374d65976eb5d0c5aef173c703e3b19)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)

    @builtins.property
    @jsii.member(jsii_name="tenancy")
    def tenancy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tenancy"))

    @tenancy.setter
    def tenancy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c2a5ff9fbce38b50061ef4b6f9f88c761d9811670bf8024a23512d5f46faef0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tenancy", value)

    @builtins.property
    @jsii.member(jsii_name="userData")
    def user_data(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userData"))

    @user_data.setter
    def user_data(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f7ecd2fbdfec2b4bed3aaa37e3d25b452a158cae1701d4b7c7bba29993fc55e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userData", value)

    @builtins.property
    @jsii.member(jsii_name="userDataBase64")
    def user_data_base64(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userDataBase64"))

    @user_data_base64.setter
    def user_data_base64(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__994bcaacde8405ae2b0816cc884e4c364671f8c5cd3e0adfaaea9bbdbbada2ea)
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
            type_hints = typing.get_type_hints(_typecheckingstub__20e6f0a09ae3b3d31fa7427939a218a5aa5bfa5d9347c00432dbe27f1294279a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userDataReplaceOnChange", value)

    @builtins.property
    @jsii.member(jsii_name="volumeTags")
    def volume_tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "volumeTags"))

    @volume_tags.setter
    def volume_tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ec77a33ee37e0962bb285a3dd9d66587c72dc302423b988be618bd02d9e7465)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeTags", value)

    @builtins.property
    @jsii.member(jsii_name="vpcSecurityGroupIds")
    def vpc_security_group_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "vpcSecurityGroupIds"))

    @vpc_security_group_ids.setter
    def vpc_security_group_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a19cac030142e395fda2170e631c8db9537cde6c1940f3482e55ff8835762961)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcSecurityGroupIds", value)


@jsii.data_type(
    jsii_type="aws.instance.InstanceCapacityReservationSpecification",
    jsii_struct_bases=[],
    name_mapping={
        "capacity_reservation_preference": "capacityReservationPreference",
        "capacity_reservation_target": "capacityReservationTarget",
    },
)
class InstanceCapacityReservationSpecification:
    def __init__(
        self,
        *,
        capacity_reservation_preference: typing.Optional[builtins.str] = None,
        capacity_reservation_target: typing.Optional[typing.Union["InstanceCapacityReservationSpecificationCapacityReservationTarget", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param capacity_reservation_preference: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#capacity_reservation_preference Instance#capacity_reservation_preference}.
        :param capacity_reservation_target: capacity_reservation_target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#capacity_reservation_target Instance#capacity_reservation_target}
        '''
        if isinstance(capacity_reservation_target, dict):
            capacity_reservation_target = InstanceCapacityReservationSpecificationCapacityReservationTarget(**capacity_reservation_target)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09788016be568da2d6fc0b18cd3ea903553213b3e80808974664edbd57c99b49)
            check_type(argname="argument capacity_reservation_preference", value=capacity_reservation_preference, expected_type=type_hints["capacity_reservation_preference"])
            check_type(argname="argument capacity_reservation_target", value=capacity_reservation_target, expected_type=type_hints["capacity_reservation_target"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if capacity_reservation_preference is not None:
            self._values["capacity_reservation_preference"] = capacity_reservation_preference
        if capacity_reservation_target is not None:
            self._values["capacity_reservation_target"] = capacity_reservation_target

    @builtins.property
    def capacity_reservation_preference(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#capacity_reservation_preference Instance#capacity_reservation_preference}.'''
        result = self._values.get("capacity_reservation_preference")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def capacity_reservation_target(
        self,
    ) -> typing.Optional["InstanceCapacityReservationSpecificationCapacityReservationTarget"]:
        '''capacity_reservation_target block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#capacity_reservation_target Instance#capacity_reservation_target}
        '''
        result = self._values.get("capacity_reservation_target")
        return typing.cast(typing.Optional["InstanceCapacityReservationSpecificationCapacityReservationTarget"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "InstanceCapacityReservationSpecification(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.instance.InstanceCapacityReservationSpecificationCapacityReservationTarget",
    jsii_struct_bases=[],
    name_mapping={
        "capacity_reservation_id": "capacityReservationId",
        "capacity_reservation_resource_group_arn": "capacityReservationResourceGroupArn",
    },
)
class InstanceCapacityReservationSpecificationCapacityReservationTarget:
    def __init__(
        self,
        *,
        capacity_reservation_id: typing.Optional[builtins.str] = None,
        capacity_reservation_resource_group_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param capacity_reservation_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#capacity_reservation_id Instance#capacity_reservation_id}.
        :param capacity_reservation_resource_group_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#capacity_reservation_resource_group_arn Instance#capacity_reservation_resource_group_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b436946f220a61223675395086fd310afe27938ab3fb5c383d7886c1cb5a10de)
            check_type(argname="argument capacity_reservation_id", value=capacity_reservation_id, expected_type=type_hints["capacity_reservation_id"])
            check_type(argname="argument capacity_reservation_resource_group_arn", value=capacity_reservation_resource_group_arn, expected_type=type_hints["capacity_reservation_resource_group_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if capacity_reservation_id is not None:
            self._values["capacity_reservation_id"] = capacity_reservation_id
        if capacity_reservation_resource_group_arn is not None:
            self._values["capacity_reservation_resource_group_arn"] = capacity_reservation_resource_group_arn

    @builtins.property
    def capacity_reservation_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#capacity_reservation_id Instance#capacity_reservation_id}.'''
        result = self._values.get("capacity_reservation_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def capacity_reservation_resource_group_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#capacity_reservation_resource_group_arn Instance#capacity_reservation_resource_group_arn}.'''
        result = self._values.get("capacity_reservation_resource_group_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "InstanceCapacityReservationSpecificationCapacityReservationTarget(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class InstanceCapacityReservationSpecificationCapacityReservationTargetOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.instance.InstanceCapacityReservationSpecificationCapacityReservationTargetOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c2fb16ac548a6468edcc1b999edb2bb5dc4cffa89f21cba50ba7d2b1b31d2556)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c920f1eff8484839c283a5ce13fc0cd66013a40872838217303ae85d9cb1e64d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "capacityReservationId", value)

    @builtins.property
    @jsii.member(jsii_name="capacityReservationResourceGroupArn")
    def capacity_reservation_resource_group_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "capacityReservationResourceGroupArn"))

    @capacity_reservation_resource_group_arn.setter
    def capacity_reservation_resource_group_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__273866d02acaa19952f832b0bbf3f24c07b6e3905e415c8fd5b5c7b40aba7003)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "capacityReservationResourceGroupArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[InstanceCapacityReservationSpecificationCapacityReservationTarget]:
        return typing.cast(typing.Optional[InstanceCapacityReservationSpecificationCapacityReservationTarget], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[InstanceCapacityReservationSpecificationCapacityReservationTarget],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74506afb94bad3395c50c09b9e58b0ab5ae7949914be7efb28f569860cdaa1d8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class InstanceCapacityReservationSpecificationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.instance.InstanceCapacityReservationSpecificationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__11e77cbf9a7b2d7408ea561b392557d16649e714c6a7af3f8519120bc5936c87)
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
        :param capacity_reservation_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#capacity_reservation_id Instance#capacity_reservation_id}.
        :param capacity_reservation_resource_group_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#capacity_reservation_resource_group_arn Instance#capacity_reservation_resource_group_arn}.
        '''
        value = InstanceCapacityReservationSpecificationCapacityReservationTarget(
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
    ) -> InstanceCapacityReservationSpecificationCapacityReservationTargetOutputReference:
        return typing.cast(InstanceCapacityReservationSpecificationCapacityReservationTargetOutputReference, jsii.get(self, "capacityReservationTarget"))

    @builtins.property
    @jsii.member(jsii_name="capacityReservationPreferenceInput")
    def capacity_reservation_preference_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "capacityReservationPreferenceInput"))

    @builtins.property
    @jsii.member(jsii_name="capacityReservationTargetInput")
    def capacity_reservation_target_input(
        self,
    ) -> typing.Optional[InstanceCapacityReservationSpecificationCapacityReservationTarget]:
        return typing.cast(typing.Optional[InstanceCapacityReservationSpecificationCapacityReservationTarget], jsii.get(self, "capacityReservationTargetInput"))

    @builtins.property
    @jsii.member(jsii_name="capacityReservationPreference")
    def capacity_reservation_preference(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "capacityReservationPreference"))

    @capacity_reservation_preference.setter
    def capacity_reservation_preference(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bfd91ed1394abf3d0e7230f2dd77ca33da90f851ef5310694cba56cd88d11ea3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "capacityReservationPreference", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[InstanceCapacityReservationSpecification]:
        return typing.cast(typing.Optional[InstanceCapacityReservationSpecification], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[InstanceCapacityReservationSpecification],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df5e26b003078b39abbafaa7f4c338147f9fa0a5e60ce77036b82b4207c23ce6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.instance.InstanceConfig",
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
        "instance_type": "instanceType",
        "ipv6_address_count": "ipv6AddressCount",
        "ipv6_addresses": "ipv6Addresses",
        "key_name": "keyName",
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
        "subnet_id": "subnetId",
        "tags": "tags",
        "tags_all": "tagsAll",
        "tenancy": "tenancy",
        "timeouts": "timeouts",
        "user_data": "userData",
        "user_data_base64": "userDataBase64",
        "user_data_replace_on_change": "userDataReplaceOnChange",
        "volume_tags": "volumeTags",
        "vpc_security_group_ids": "vpcSecurityGroupIds",
    },
)
class InstanceConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        capacity_reservation_specification: typing.Optional[typing.Union[InstanceCapacityReservationSpecification, typing.Dict[builtins.str, typing.Any]]] = None,
        cpu_core_count: typing.Optional[jsii.Number] = None,
        cpu_threads_per_core: typing.Optional[jsii.Number] = None,
        credit_specification: typing.Optional[typing.Union["InstanceCreditSpecification", typing.Dict[builtins.str, typing.Any]]] = None,
        disable_api_stop: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        disable_api_termination: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        ebs_block_device: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["InstanceEbsBlockDevice", typing.Dict[builtins.str, typing.Any]]]]] = None,
        ebs_optimized: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enclave_options: typing.Optional[typing.Union["InstanceEnclaveOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        ephemeral_block_device: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["InstanceEphemeralBlockDevice", typing.Dict[builtins.str, typing.Any]]]]] = None,
        fetch_password_data: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        hibernation: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        host_id: typing.Optional[builtins.str] = None,
        host_resource_group_arn: typing.Optional[builtins.str] = None,
        iam_instance_profile: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        instance_initiated_shutdown_behavior: typing.Optional[builtins.str] = None,
        instance_type: typing.Optional[builtins.str] = None,
        ipv6_address_count: typing.Optional[jsii.Number] = None,
        ipv6_addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
        key_name: typing.Optional[builtins.str] = None,
        launch_template: typing.Optional[typing.Union["InstanceLaunchTemplate", typing.Dict[builtins.str, typing.Any]]] = None,
        maintenance_options: typing.Optional[typing.Union["InstanceMaintenanceOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        metadata_options: typing.Optional[typing.Union["InstanceMetadataOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        monitoring: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        network_interface: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["InstanceNetworkInterface", typing.Dict[builtins.str, typing.Any]]]]] = None,
        placement_group: typing.Optional[builtins.str] = None,
        placement_partition_number: typing.Optional[jsii.Number] = None,
        private_dns_name_options: typing.Optional[typing.Union["InstancePrivateDnsNameOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        private_ip: typing.Optional[builtins.str] = None,
        root_block_device: typing.Optional[typing.Union["InstanceRootBlockDevice", typing.Dict[builtins.str, typing.Any]]] = None,
        secondary_private_ips: typing.Optional[typing.Sequence[builtins.str]] = None,
        security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        source_dest_check: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        subnet_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tenancy: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["InstanceTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        user_data: typing.Optional[builtins.str] = None,
        user_data_base64: typing.Optional[builtins.str] = None,
        user_data_replace_on_change: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        volume_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
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
        :param ami: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#ami Instance#ami}.
        :param associate_public_ip_address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#associate_public_ip_address Instance#associate_public_ip_address}.
        :param availability_zone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#availability_zone Instance#availability_zone}.
        :param capacity_reservation_specification: capacity_reservation_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#capacity_reservation_specification Instance#capacity_reservation_specification}
        :param cpu_core_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#cpu_core_count Instance#cpu_core_count}.
        :param cpu_threads_per_core: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#cpu_threads_per_core Instance#cpu_threads_per_core}.
        :param credit_specification: credit_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#credit_specification Instance#credit_specification}
        :param disable_api_stop: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#disable_api_stop Instance#disable_api_stop}.
        :param disable_api_termination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#disable_api_termination Instance#disable_api_termination}.
        :param ebs_block_device: ebs_block_device block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#ebs_block_device Instance#ebs_block_device}
        :param ebs_optimized: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#ebs_optimized Instance#ebs_optimized}.
        :param enclave_options: enclave_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#enclave_options Instance#enclave_options}
        :param ephemeral_block_device: ephemeral_block_device block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#ephemeral_block_device Instance#ephemeral_block_device}
        :param fetch_password_data: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#get_password_data Instance#get_password_data}.
        :param hibernation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#hibernation Instance#hibernation}.
        :param host_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#host_id Instance#host_id}.
        :param host_resource_group_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#host_resource_group_arn Instance#host_resource_group_arn}.
        :param iam_instance_profile: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#iam_instance_profile Instance#iam_instance_profile}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#id Instance#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param instance_initiated_shutdown_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#instance_initiated_shutdown_behavior Instance#instance_initiated_shutdown_behavior}.
        :param instance_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#instance_type Instance#instance_type}.
        :param ipv6_address_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#ipv6_address_count Instance#ipv6_address_count}.
        :param ipv6_addresses: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#ipv6_addresses Instance#ipv6_addresses}.
        :param key_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#key_name Instance#key_name}.
        :param launch_template: launch_template block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#launch_template Instance#launch_template}
        :param maintenance_options: maintenance_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#maintenance_options Instance#maintenance_options}
        :param metadata_options: metadata_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#metadata_options Instance#metadata_options}
        :param monitoring: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#monitoring Instance#monitoring}.
        :param network_interface: network_interface block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#network_interface Instance#network_interface}
        :param placement_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#placement_group Instance#placement_group}.
        :param placement_partition_number: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#placement_partition_number Instance#placement_partition_number}.
        :param private_dns_name_options: private_dns_name_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#private_dns_name_options Instance#private_dns_name_options}
        :param private_ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#private_ip Instance#private_ip}.
        :param root_block_device: root_block_device block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#root_block_device Instance#root_block_device}
        :param secondary_private_ips: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#secondary_private_ips Instance#secondary_private_ips}.
        :param security_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#security_groups Instance#security_groups}.
        :param source_dest_check: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#source_dest_check Instance#source_dest_check}.
        :param subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#subnet_id Instance#subnet_id}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#tags Instance#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#tags_all Instance#tags_all}.
        :param tenancy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#tenancy Instance#tenancy}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#timeouts Instance#timeouts}
        :param user_data: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#user_data Instance#user_data}.
        :param user_data_base64: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#user_data_base64 Instance#user_data_base64}.
        :param user_data_replace_on_change: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#user_data_replace_on_change Instance#user_data_replace_on_change}.
        :param volume_tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#volume_tags Instance#volume_tags}.
        :param vpc_security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#vpc_security_group_ids Instance#vpc_security_group_ids}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(capacity_reservation_specification, dict):
            capacity_reservation_specification = InstanceCapacityReservationSpecification(**capacity_reservation_specification)
        if isinstance(credit_specification, dict):
            credit_specification = InstanceCreditSpecification(**credit_specification)
        if isinstance(enclave_options, dict):
            enclave_options = InstanceEnclaveOptions(**enclave_options)
        if isinstance(launch_template, dict):
            launch_template = InstanceLaunchTemplate(**launch_template)
        if isinstance(maintenance_options, dict):
            maintenance_options = InstanceMaintenanceOptions(**maintenance_options)
        if isinstance(metadata_options, dict):
            metadata_options = InstanceMetadataOptions(**metadata_options)
        if isinstance(private_dns_name_options, dict):
            private_dns_name_options = InstancePrivateDnsNameOptions(**private_dns_name_options)
        if isinstance(root_block_device, dict):
            root_block_device = InstanceRootBlockDevice(**root_block_device)
        if isinstance(timeouts, dict):
            timeouts = InstanceTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9d0e398fa56e354f7cace934be4cb4e560cac06ad9f7f33b9b31fe765b0f0cf)
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
            check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
            check_type(argname="argument ipv6_address_count", value=ipv6_address_count, expected_type=type_hints["ipv6_address_count"])
            check_type(argname="argument ipv6_addresses", value=ipv6_addresses, expected_type=type_hints["ipv6_addresses"])
            check_type(argname="argument key_name", value=key_name, expected_type=type_hints["key_name"])
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
            check_type(argname="argument subnet_id", value=subnet_id, expected_type=type_hints["subnet_id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument tenancy", value=tenancy, expected_type=type_hints["tenancy"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument user_data", value=user_data, expected_type=type_hints["user_data"])
            check_type(argname="argument user_data_base64", value=user_data_base64, expected_type=type_hints["user_data_base64"])
            check_type(argname="argument user_data_replace_on_change", value=user_data_replace_on_change, expected_type=type_hints["user_data_replace_on_change"])
            check_type(argname="argument volume_tags", value=volume_tags, expected_type=type_hints["volume_tags"])
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
        if ami is not None:
            self._values["ami"] = ami
        if associate_public_ip_address is not None:
            self._values["associate_public_ip_address"] = associate_public_ip_address
        if availability_zone is not None:
            self._values["availability_zone"] = availability_zone
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
        if instance_type is not None:
            self._values["instance_type"] = instance_type
        if ipv6_address_count is not None:
            self._values["ipv6_address_count"] = ipv6_address_count
        if ipv6_addresses is not None:
            self._values["ipv6_addresses"] = ipv6_addresses
        if key_name is not None:
            self._values["key_name"] = key_name
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
        if volume_tags is not None:
            self._values["volume_tags"] = volume_tags
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
    def ami(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#ami Instance#ami}.'''
        result = self._values.get("ami")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def associate_public_ip_address(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#associate_public_ip_address Instance#associate_public_ip_address}.'''
        result = self._values.get("associate_public_ip_address")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def availability_zone(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#availability_zone Instance#availability_zone}.'''
        result = self._values.get("availability_zone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def capacity_reservation_specification(
        self,
    ) -> typing.Optional[InstanceCapacityReservationSpecification]:
        '''capacity_reservation_specification block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#capacity_reservation_specification Instance#capacity_reservation_specification}
        '''
        result = self._values.get("capacity_reservation_specification")
        return typing.cast(typing.Optional[InstanceCapacityReservationSpecification], result)

    @builtins.property
    def cpu_core_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#cpu_core_count Instance#cpu_core_count}.'''
        result = self._values.get("cpu_core_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def cpu_threads_per_core(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#cpu_threads_per_core Instance#cpu_threads_per_core}.'''
        result = self._values.get("cpu_threads_per_core")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def credit_specification(self) -> typing.Optional["InstanceCreditSpecification"]:
        '''credit_specification block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#credit_specification Instance#credit_specification}
        '''
        result = self._values.get("credit_specification")
        return typing.cast(typing.Optional["InstanceCreditSpecification"], result)

    @builtins.property
    def disable_api_stop(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#disable_api_stop Instance#disable_api_stop}.'''
        result = self._values.get("disable_api_stop")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def disable_api_termination(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#disable_api_termination Instance#disable_api_termination}.'''
        result = self._values.get("disable_api_termination")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def ebs_block_device(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["InstanceEbsBlockDevice"]]]:
        '''ebs_block_device block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#ebs_block_device Instance#ebs_block_device}
        '''
        result = self._values.get("ebs_block_device")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["InstanceEbsBlockDevice"]]], result)

    @builtins.property
    def ebs_optimized(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#ebs_optimized Instance#ebs_optimized}.'''
        result = self._values.get("ebs_optimized")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def enclave_options(self) -> typing.Optional["InstanceEnclaveOptions"]:
        '''enclave_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#enclave_options Instance#enclave_options}
        '''
        result = self._values.get("enclave_options")
        return typing.cast(typing.Optional["InstanceEnclaveOptions"], result)

    @builtins.property
    def ephemeral_block_device(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["InstanceEphemeralBlockDevice"]]]:
        '''ephemeral_block_device block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#ephemeral_block_device Instance#ephemeral_block_device}
        '''
        result = self._values.get("ephemeral_block_device")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["InstanceEphemeralBlockDevice"]]], result)

    @builtins.property
    def fetch_password_data(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#get_password_data Instance#get_password_data}.'''
        result = self._values.get("fetch_password_data")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def hibernation(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#hibernation Instance#hibernation}.'''
        result = self._values.get("hibernation")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def host_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#host_id Instance#host_id}.'''
        result = self._values.get("host_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def host_resource_group_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#host_resource_group_arn Instance#host_resource_group_arn}.'''
        result = self._values.get("host_resource_group_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def iam_instance_profile(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#iam_instance_profile Instance#iam_instance_profile}.'''
        result = self._values.get("iam_instance_profile")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#id Instance#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance_initiated_shutdown_behavior(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#instance_initiated_shutdown_behavior Instance#instance_initiated_shutdown_behavior}.'''
        result = self._values.get("instance_initiated_shutdown_behavior")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#instance_type Instance#instance_type}.'''
        result = self._values.get("instance_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ipv6_address_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#ipv6_address_count Instance#ipv6_address_count}.'''
        result = self._values.get("ipv6_address_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ipv6_addresses(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#ipv6_addresses Instance#ipv6_addresses}.'''
        result = self._values.get("ipv6_addresses")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def key_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#key_name Instance#key_name}.'''
        result = self._values.get("key_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def launch_template(self) -> typing.Optional["InstanceLaunchTemplate"]:
        '''launch_template block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#launch_template Instance#launch_template}
        '''
        result = self._values.get("launch_template")
        return typing.cast(typing.Optional["InstanceLaunchTemplate"], result)

    @builtins.property
    def maintenance_options(self) -> typing.Optional["InstanceMaintenanceOptions"]:
        '''maintenance_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#maintenance_options Instance#maintenance_options}
        '''
        result = self._values.get("maintenance_options")
        return typing.cast(typing.Optional["InstanceMaintenanceOptions"], result)

    @builtins.property
    def metadata_options(self) -> typing.Optional["InstanceMetadataOptions"]:
        '''metadata_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#metadata_options Instance#metadata_options}
        '''
        result = self._values.get("metadata_options")
        return typing.cast(typing.Optional["InstanceMetadataOptions"], result)

    @builtins.property
    def monitoring(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#monitoring Instance#monitoring}.'''
        result = self._values.get("monitoring")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def network_interface(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["InstanceNetworkInterface"]]]:
        '''network_interface block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#network_interface Instance#network_interface}
        '''
        result = self._values.get("network_interface")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["InstanceNetworkInterface"]]], result)

    @builtins.property
    def placement_group(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#placement_group Instance#placement_group}.'''
        result = self._values.get("placement_group")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def placement_partition_number(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#placement_partition_number Instance#placement_partition_number}.'''
        result = self._values.get("placement_partition_number")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def private_dns_name_options(
        self,
    ) -> typing.Optional["InstancePrivateDnsNameOptions"]:
        '''private_dns_name_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#private_dns_name_options Instance#private_dns_name_options}
        '''
        result = self._values.get("private_dns_name_options")
        return typing.cast(typing.Optional["InstancePrivateDnsNameOptions"], result)

    @builtins.property
    def private_ip(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#private_ip Instance#private_ip}.'''
        result = self._values.get("private_ip")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def root_block_device(self) -> typing.Optional["InstanceRootBlockDevice"]:
        '''root_block_device block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#root_block_device Instance#root_block_device}
        '''
        result = self._values.get("root_block_device")
        return typing.cast(typing.Optional["InstanceRootBlockDevice"], result)

    @builtins.property
    def secondary_private_ips(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#secondary_private_ips Instance#secondary_private_ips}.'''
        result = self._values.get("secondary_private_ips")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def security_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#security_groups Instance#security_groups}.'''
        result = self._values.get("security_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def source_dest_check(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#source_dest_check Instance#source_dest_check}.'''
        result = self._values.get("source_dest_check")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def subnet_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#subnet_id Instance#subnet_id}.'''
        result = self._values.get("subnet_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#tags Instance#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#tags_all Instance#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tenancy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#tenancy Instance#tenancy}.'''
        result = self._values.get("tenancy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["InstanceTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#timeouts Instance#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["InstanceTimeouts"], result)

    @builtins.property
    def user_data(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#user_data Instance#user_data}.'''
        result = self._values.get("user_data")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_data_base64(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#user_data_base64 Instance#user_data_base64}.'''
        result = self._values.get("user_data_base64")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_data_replace_on_change(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#user_data_replace_on_change Instance#user_data_replace_on_change}.'''
        result = self._values.get("user_data_replace_on_change")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def volume_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#volume_tags Instance#volume_tags}.'''
        result = self._values.get("volume_tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def vpc_security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#vpc_security_group_ids Instance#vpc_security_group_ids}.'''
        result = self._values.get("vpc_security_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "InstanceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.instance.InstanceCreditSpecification",
    jsii_struct_bases=[],
    name_mapping={"cpu_credits": "cpuCredits"},
)
class InstanceCreditSpecification:
    def __init__(self, *, cpu_credits: typing.Optional[builtins.str] = None) -> None:
        '''
        :param cpu_credits: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#cpu_credits Instance#cpu_credits}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e690b60c8249d5a0bdef6c15a6619348c08a7f044869caa6c5d0635a9c17bc77)
            check_type(argname="argument cpu_credits", value=cpu_credits, expected_type=type_hints["cpu_credits"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if cpu_credits is not None:
            self._values["cpu_credits"] = cpu_credits

    @builtins.property
    def cpu_credits(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#cpu_credits Instance#cpu_credits}.'''
        result = self._values.get("cpu_credits")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "InstanceCreditSpecification(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class InstanceCreditSpecificationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.instance.InstanceCreditSpecificationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__30e56f3d795f832706eba827d57575a8f7ec9180ca5cc9b175ccb747f4afe20e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2b0fabe0f10de70f02418d38c83bd69cffde3bd0fc962069b07662c947ceed18)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpuCredits", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[InstanceCreditSpecification]:
        return typing.cast(typing.Optional[InstanceCreditSpecification], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[InstanceCreditSpecification],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aed6aa854c4da169d9db5720d71836caebdc9d9fbcaaf12692a6794f108b50ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.instance.InstanceEbsBlockDevice",
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
class InstanceEbsBlockDevice:
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
        :param device_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#device_name Instance#device_name}.
        :param delete_on_termination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#delete_on_termination Instance#delete_on_termination}.
        :param encrypted: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#encrypted Instance#encrypted}.
        :param iops: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#iops Instance#iops}.
        :param kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#kms_key_id Instance#kms_key_id}.
        :param snapshot_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#snapshot_id Instance#snapshot_id}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#tags Instance#tags}.
        :param throughput: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#throughput Instance#throughput}.
        :param volume_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#volume_size Instance#volume_size}.
        :param volume_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#volume_type Instance#volume_type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd45affc685598bfe82ffb468c3bb9b7027c7be984f42da93cffc4028163f9be)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#device_name Instance#device_name}.'''
        result = self._values.get("device_name")
        assert result is not None, "Required property 'device_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def delete_on_termination(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#delete_on_termination Instance#delete_on_termination}.'''
        result = self._values.get("delete_on_termination")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def encrypted(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#encrypted Instance#encrypted}.'''
        result = self._values.get("encrypted")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def iops(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#iops Instance#iops}.'''
        result = self._values.get("iops")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#kms_key_id Instance#kms_key_id}.'''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def snapshot_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#snapshot_id Instance#snapshot_id}.'''
        result = self._values.get("snapshot_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#tags Instance#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def throughput(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#throughput Instance#throughput}.'''
        result = self._values.get("throughput")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def volume_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#volume_size Instance#volume_size}.'''
        result = self._values.get("volume_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def volume_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#volume_type Instance#volume_type}.'''
        result = self._values.get("volume_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "InstanceEbsBlockDevice(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class InstanceEbsBlockDeviceList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.instance.InstanceEbsBlockDeviceList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c375cf4614247f22cfcbcc9c5198e01d4512f1b2ed0f8c092e1da67f9188d257)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "InstanceEbsBlockDeviceOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0662b855603257f7fa53335dd90671135f52eb5a044023bda949160aefa0e03a)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("InstanceEbsBlockDeviceOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41f2e542491d8580e728554ffc635501565d604249e2cd63d5c986afb014f4a0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b85b3f5f2728c3bf53d14e0f3c1eef40e20b88ed15dd6d423992bd06b4c40e78)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d96a9b5e7b1246349a5fae202ab9a4e5f9a1bbeca0e38fb1cfafdaa400dcabb6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[InstanceEbsBlockDevice]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[InstanceEbsBlockDevice]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[InstanceEbsBlockDevice]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c81a33d3542f9f137b85454fff058cd4981893dfc3b84d7728e6ccf3a53de66)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class InstanceEbsBlockDeviceOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.instance.InstanceEbsBlockDeviceOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__140d12119bf33c11d2f35437151a8faa78a171db48b58eccb144a90728f554af)
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
            type_hints = typing.get_type_hints(_typecheckingstub__61dbd94ae83723e61652cbf9e3904227acfd7b8bc5f48440bf6c8774e1914626)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deleteOnTermination", value)

    @builtins.property
    @jsii.member(jsii_name="deviceName")
    def device_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deviceName"))

    @device_name.setter
    def device_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e46623a75d9f29947db60dbe069391cc8eba3b097a7870b56a14e72bb5c57272)
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
            type_hints = typing.get_type_hints(_typecheckingstub__147398409818416b7c0a3613c0e02fd18797f0dc2caec106546d05ad6df3bf19)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encrypted", value)

    @builtins.property
    @jsii.member(jsii_name="iops")
    def iops(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "iops"))

    @iops.setter
    def iops(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0de237405562f9c0e1eec91179fec9e5b3775c684eb247ae7342603149609fba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iops", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b655b27881d29de6f0e14768becb1186ea92638eb5759f0e03ca57113a7a827b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="snapshotId")
    def snapshot_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "snapshotId"))

    @snapshot_id.setter
    def snapshot_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ec57ccbdc736f7f44bcdb004fd0e51007415653bfeae745a6bee3f84ea839ba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snapshotId", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8bde32cd7706666e800888791bdcc29fa27f9d77612793ac68273c416bce3e02)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="throughput")
    def throughput(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "throughput"))

    @throughput.setter
    def throughput(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59460812fb0197fd15c5eaea1548e238ccc4184ca314d10a3d000d3dd574fa9b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "throughput", value)

    @builtins.property
    @jsii.member(jsii_name="volumeSize")
    def volume_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "volumeSize"))

    @volume_size.setter
    def volume_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2cc95237f6af43b11ed043526478a2fc00a6a936e41fbe43d07d3a14e0fc3532)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeSize", value)

    @builtins.property
    @jsii.member(jsii_name="volumeType")
    def volume_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "volumeType"))

    @volume_type.setter
    def volume_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f6c280508e1859c6b623bb98eb85f11a573930639cd17e3ad846184db72b79b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[InstanceEbsBlockDevice, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[InstanceEbsBlockDevice, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[InstanceEbsBlockDevice, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__645bd52498c34349cb16e4dbc231ebdf98e567b9ce2d8f9282397f2953927b86)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.instance.InstanceEnclaveOptions",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled"},
)
class InstanceEnclaveOptions:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#enabled Instance#enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d57a17aa778cfbc80e926ba46e5f3497ac71c91c0f168f8dd16c50475c5c162a)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#enabled Instance#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "InstanceEnclaveOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class InstanceEnclaveOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.instance.InstanceEnclaveOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3197806f9867e25b73b128d4c8e6c375354164cd65299cd20aa4ac028d1e9a10)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4a3e25935bd571091217e1ec88dc583fd5ed613e1260bccc97aeacd4f2d2f0be)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[InstanceEnclaveOptions]:
        return typing.cast(typing.Optional[InstanceEnclaveOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[InstanceEnclaveOptions]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b44a6c3ef9c486df1c3de722cc15bf8b200555455e667d8d4a21bc0a7afea7e2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.instance.InstanceEphemeralBlockDevice",
    jsii_struct_bases=[],
    name_mapping={
        "device_name": "deviceName",
        "no_device": "noDevice",
        "virtual_name": "virtualName",
    },
)
class InstanceEphemeralBlockDevice:
    def __init__(
        self,
        *,
        device_name: builtins.str,
        no_device: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        virtual_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param device_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#device_name Instance#device_name}.
        :param no_device: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#no_device Instance#no_device}.
        :param virtual_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#virtual_name Instance#virtual_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5dce1c45f8d2403d8790cc931b39ffb61df956508471ab742581a1d0686993b9)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#device_name Instance#device_name}.'''
        result = self._values.get("device_name")
        assert result is not None, "Required property 'device_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def no_device(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#no_device Instance#no_device}.'''
        result = self._values.get("no_device")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def virtual_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#virtual_name Instance#virtual_name}.'''
        result = self._values.get("virtual_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "InstanceEphemeralBlockDevice(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class InstanceEphemeralBlockDeviceList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.instance.InstanceEphemeralBlockDeviceList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__579ea018d7444e569bf2c4c5e266d09f5cd63ef6bb4e9130d2ccfb88c684fe9d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "InstanceEphemeralBlockDeviceOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56a4d48aa4dd5a382ac0a599403a65c3687747e7a95a7215ad1f352a91bf4555)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("InstanceEphemeralBlockDeviceOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__838f5a1da6eb28995cae96c8e683d709b159873026f5a1be1e590167513b98af)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0029b847ea2acc29eeb86264b5b848ff335a8e3bcf78b65387cc2815932490a1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b293791a2490863af7f3d77562a267bacc65fb2077411571907818fefcc1b2ee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[InstanceEphemeralBlockDevice]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[InstanceEphemeralBlockDevice]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[InstanceEphemeralBlockDevice]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8962556e7ee27ab4f40470e801764ca909f70345345756e3d2327ab0d7f4bbc4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class InstanceEphemeralBlockDeviceOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.instance.InstanceEphemeralBlockDeviceOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9a5f5a07288162851bded77460948ccfef3aea55ef8da3744f3d96dd06d26e77)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b2b690d7b9702558e4ef3e6dcf4abb339c5645c41f9c12afd13acad273c20fe0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d2dbca96218f5aa616a6dca09a3cad6db1cb714063f0207a670412e4224abfc2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "noDevice", value)

    @builtins.property
    @jsii.member(jsii_name="virtualName")
    def virtual_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "virtualName"))

    @virtual_name.setter
    def virtual_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41ac9197d437d7739a96bfa1043b8c5224f4ad1507427a17a2018909e62f51d9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[InstanceEphemeralBlockDevice, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[InstanceEphemeralBlockDevice, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[InstanceEphemeralBlockDevice, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49d4742d0a2039bfef3a49a5b9577dc2a59321ffa771f9de875b10e611d56733)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.instance.InstanceLaunchTemplate",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "name": "name", "version": "version"},
)
class InstanceLaunchTemplate:
    def __init__(
        self,
        *,
        id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#id Instance#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#name Instance#name}.
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#version Instance#version}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0042778c6c497227aeb9b73b0a535fc85e09970f2c957e9e9ff1da46922aad98)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#id Instance#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#name Instance#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#version Instance#version}.'''
        result = self._values.get("version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "InstanceLaunchTemplate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class InstanceLaunchTemplateOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.instance.InstanceLaunchTemplateOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__dc45a46ccc01cac3281f5ab75d45c9c3b69461825d0f56dac6a6c216d8b93fa0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e5b3f66348dc6b9bd08168f596d9e97a7dde907a6be74a3048cb93a2e315d38f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f721f4e1092bd2318dab60ab2da3f3c592ce3950a2917f1bf4bcffea647f3b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a8657eb94160930117756c373c4b9cff66466ffeb625a0a147868037a1c9f31)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[InstanceLaunchTemplate]:
        return typing.cast(typing.Optional[InstanceLaunchTemplate], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[InstanceLaunchTemplate]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f79446a12ab42cd4313a3c6ec0c80403585e39bacc693347ef4beb95f4cbc353)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.instance.InstanceMaintenanceOptions",
    jsii_struct_bases=[],
    name_mapping={"auto_recovery": "autoRecovery"},
)
class InstanceMaintenanceOptions:
    def __init__(self, *, auto_recovery: typing.Optional[builtins.str] = None) -> None:
        '''
        :param auto_recovery: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#auto_recovery Instance#auto_recovery}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96f8560d843674ce96734c6472485e26c5009d3a50c4b3849994a598c9afb4a5)
            check_type(argname="argument auto_recovery", value=auto_recovery, expected_type=type_hints["auto_recovery"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if auto_recovery is not None:
            self._values["auto_recovery"] = auto_recovery

    @builtins.property
    def auto_recovery(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#auto_recovery Instance#auto_recovery}.'''
        result = self._values.get("auto_recovery")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "InstanceMaintenanceOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class InstanceMaintenanceOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.instance.InstanceMaintenanceOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d17370b442f57e438e441651874d7975720fc5e801c5a477fd8d4796cfda61c8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__be2ccc0e56a34e61ec5601005bbcbf8e834c75a923531d7d60bd2b5f46a12ec3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoRecovery", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[InstanceMaintenanceOptions]:
        return typing.cast(typing.Optional[InstanceMaintenanceOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[InstanceMaintenanceOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5362dc72c9002aa9598e1e8af5102e4880dfac29d2d53b5338e4a11c6a5a6cac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.instance.InstanceMetadataOptions",
    jsii_struct_bases=[],
    name_mapping={
        "http_endpoint": "httpEndpoint",
        "http_put_response_hop_limit": "httpPutResponseHopLimit",
        "http_tokens": "httpTokens",
        "instance_metadata_tags": "instanceMetadataTags",
    },
)
class InstanceMetadataOptions:
    def __init__(
        self,
        *,
        http_endpoint: typing.Optional[builtins.str] = None,
        http_put_response_hop_limit: typing.Optional[jsii.Number] = None,
        http_tokens: typing.Optional[builtins.str] = None,
        instance_metadata_tags: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param http_endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#http_endpoint Instance#http_endpoint}.
        :param http_put_response_hop_limit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#http_put_response_hop_limit Instance#http_put_response_hop_limit}.
        :param http_tokens: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#http_tokens Instance#http_tokens}.
        :param instance_metadata_tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#instance_metadata_tags Instance#instance_metadata_tags}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4b45db7f54783aac95e83a5e86491fb6898f6661e54dd279312399b9324dfe4)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#http_endpoint Instance#http_endpoint}.'''
        result = self._values.get("http_endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def http_put_response_hop_limit(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#http_put_response_hop_limit Instance#http_put_response_hop_limit}.'''
        result = self._values.get("http_put_response_hop_limit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def http_tokens(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#http_tokens Instance#http_tokens}.'''
        result = self._values.get("http_tokens")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance_metadata_tags(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#instance_metadata_tags Instance#instance_metadata_tags}.'''
        result = self._values.get("instance_metadata_tags")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "InstanceMetadataOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class InstanceMetadataOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.instance.InstanceMetadataOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9a4bde2f0377012e596d6c0d68f254d7ff535bfef48c70981debce8e63cdccb2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ceaa6b00c5f4deece90a12a710c9d0ffe2092d340d1cc71429c1936ab5d71f5e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="httpPutResponseHopLimit")
    def http_put_response_hop_limit(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "httpPutResponseHopLimit"))

    @http_put_response_hop_limit.setter
    def http_put_response_hop_limit(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8da27750cf69b66d1b512d3bae4c3e82cf5230cde82c60be59318d82bb343541)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpPutResponseHopLimit", value)

    @builtins.property
    @jsii.member(jsii_name="httpTokens")
    def http_tokens(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "httpTokens"))

    @http_tokens.setter
    def http_tokens(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c80bb7961821ac398534528fb625769b7db96dfd1a215290460a4720da22b50b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpTokens", value)

    @builtins.property
    @jsii.member(jsii_name="instanceMetadataTags")
    def instance_metadata_tags(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceMetadataTags"))

    @instance_metadata_tags.setter
    def instance_metadata_tags(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d15b84c0b3498cc6d31399ee26ada48c9e42137d049ef59bc5d715f6ca9f4e1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceMetadataTags", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[InstanceMetadataOptions]:
        return typing.cast(typing.Optional[InstanceMetadataOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[InstanceMetadataOptions]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d190291b8c3c17224f55a795b111e8704ebdab6a7095f472c57b87ea77565a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.instance.InstanceNetworkInterface",
    jsii_struct_bases=[],
    name_mapping={
        "device_index": "deviceIndex",
        "network_interface_id": "networkInterfaceId",
        "delete_on_termination": "deleteOnTermination",
        "network_card_index": "networkCardIndex",
    },
)
class InstanceNetworkInterface:
    def __init__(
        self,
        *,
        device_index: jsii.Number,
        network_interface_id: builtins.str,
        delete_on_termination: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        network_card_index: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param device_index: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#device_index Instance#device_index}.
        :param network_interface_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#network_interface_id Instance#network_interface_id}.
        :param delete_on_termination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#delete_on_termination Instance#delete_on_termination}.
        :param network_card_index: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#network_card_index Instance#network_card_index}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56e55429abca02a270b795e01c4288e158862e8199d27cd9ca946c3cc750b57a)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#device_index Instance#device_index}.'''
        result = self._values.get("device_index")
        assert result is not None, "Required property 'device_index' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def network_interface_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#network_interface_id Instance#network_interface_id}.'''
        result = self._values.get("network_interface_id")
        assert result is not None, "Required property 'network_interface_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def delete_on_termination(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#delete_on_termination Instance#delete_on_termination}.'''
        result = self._values.get("delete_on_termination")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def network_card_index(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#network_card_index Instance#network_card_index}.'''
        result = self._values.get("network_card_index")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "InstanceNetworkInterface(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class InstanceNetworkInterfaceList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.instance.InstanceNetworkInterfaceList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__77f9a01254e8bcd46446d41f8e27f6d8a398534b9e314f1d0d4bd70eadc784f4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "InstanceNetworkInterfaceOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8cf3c4b5ca41aa457670e8ebd8c7158db3260915512a4f440cc9962507b60c24)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("InstanceNetworkInterfaceOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1dfdd17b75a4a9b3b88a12deb2531e3d698483db9721472750187b0f9402f05d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__aae02287300e9123322037e7a540886effeeb2caced47355f921d2e676930f6c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__dac553d77cccfc5e574710c5e5277453d8dcc45e8fbda6b10586fc7d64788928)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[InstanceNetworkInterface]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[InstanceNetworkInterface]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[InstanceNetworkInterface]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80c2da2d98cea146e301e5e2617d299fa89c30784ce355676620f9eda78caead)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class InstanceNetworkInterfaceOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.instance.InstanceNetworkInterfaceOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__aa56cca7135b27382b70f93f1c4c370ec76182360e47b7bc0d62ea3fc0dcf9f4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d86836ef4ea5a6f9bb654b7aee1375cb648f423b1d9fcc4b50ed0a27ee3a4aa0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deleteOnTermination", value)

    @builtins.property
    @jsii.member(jsii_name="deviceIndex")
    def device_index(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "deviceIndex"))

    @device_index.setter
    def device_index(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ef61ed9ad22e7decfe53c20f885f4da56f0e04b900e6993c63e07c3b57afa52)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deviceIndex", value)

    @builtins.property
    @jsii.member(jsii_name="networkCardIndex")
    def network_card_index(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "networkCardIndex"))

    @network_card_index.setter
    def network_card_index(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9808b261f3acc5995d4c69b15609d593a62f1c24c8126899f314fb6aa587bc2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkCardIndex", value)

    @builtins.property
    @jsii.member(jsii_name="networkInterfaceId")
    def network_interface_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "networkInterfaceId"))

    @network_interface_id.setter
    def network_interface_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e698f2442bdd28664aab96d0322d0d7a697f7797e192080c0456de68ffdc974a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkInterfaceId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[InstanceNetworkInterface, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[InstanceNetworkInterface, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[InstanceNetworkInterface, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fae936725f98dc037a6c842bb7bc55dedab02fb5aca66900ee156a23dfd8eacd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.instance.InstancePrivateDnsNameOptions",
    jsii_struct_bases=[],
    name_mapping={
        "enable_resource_name_dns_aaaa_record": "enableResourceNameDnsAaaaRecord",
        "enable_resource_name_dns_a_record": "enableResourceNameDnsARecord",
        "hostname_type": "hostnameType",
    },
)
class InstancePrivateDnsNameOptions:
    def __init__(
        self,
        *,
        enable_resource_name_dns_aaaa_record: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_resource_name_dns_a_record: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        hostname_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enable_resource_name_dns_aaaa_record: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#enable_resource_name_dns_aaaa_record Instance#enable_resource_name_dns_aaaa_record}.
        :param enable_resource_name_dns_a_record: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#enable_resource_name_dns_a_record Instance#enable_resource_name_dns_a_record}.
        :param hostname_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#hostname_type Instance#hostname_type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dba4bdb05c25391fdf978b41bf91e4fb4b405bf291876a3d65130b42e62fcb86)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#enable_resource_name_dns_aaaa_record Instance#enable_resource_name_dns_aaaa_record}.'''
        result = self._values.get("enable_resource_name_dns_aaaa_record")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def enable_resource_name_dns_a_record(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#enable_resource_name_dns_a_record Instance#enable_resource_name_dns_a_record}.'''
        result = self._values.get("enable_resource_name_dns_a_record")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def hostname_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#hostname_type Instance#hostname_type}.'''
        result = self._values.get("hostname_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "InstancePrivateDnsNameOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class InstancePrivateDnsNameOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.instance.InstancePrivateDnsNameOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d6e66637eadf12072472daa589322237ca979a504c25a46f8379a26db9fec3d3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__936db1a6f4e2a10822ac3aae56cd0fff177237c1a11b2101ac1751d8a0c8f35b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8715db362c116602c7414e047fcdb0aa33e3f782d4b513e559ff2e74e1ad332d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableResourceNameDnsARecord", value)

    @builtins.property
    @jsii.member(jsii_name="hostnameType")
    def hostname_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostnameType"))

    @hostname_type.setter
    def hostname_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ef96278a92555bb71cab25d2537ffb007f96a048b3e52c68231cb01eeaf2454)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostnameType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[InstancePrivateDnsNameOptions]:
        return typing.cast(typing.Optional[InstancePrivateDnsNameOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[InstancePrivateDnsNameOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f16435124c464bd898bca62093aee123317c4b04318bf5b58d36ff9f7624820)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.instance.InstanceRootBlockDevice",
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
class InstanceRootBlockDevice:
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
        :param delete_on_termination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#delete_on_termination Instance#delete_on_termination}.
        :param encrypted: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#encrypted Instance#encrypted}.
        :param iops: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#iops Instance#iops}.
        :param kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#kms_key_id Instance#kms_key_id}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#tags Instance#tags}.
        :param throughput: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#throughput Instance#throughput}.
        :param volume_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#volume_size Instance#volume_size}.
        :param volume_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#volume_type Instance#volume_type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d8f738287afd9ac9bca22b75f7ba22fc61431d724bd1c3c79763a25cd284d96)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#delete_on_termination Instance#delete_on_termination}.'''
        result = self._values.get("delete_on_termination")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def encrypted(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#encrypted Instance#encrypted}.'''
        result = self._values.get("encrypted")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def iops(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#iops Instance#iops}.'''
        result = self._values.get("iops")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#kms_key_id Instance#kms_key_id}.'''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#tags Instance#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def throughput(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#throughput Instance#throughput}.'''
        result = self._values.get("throughput")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def volume_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#volume_size Instance#volume_size}.'''
        result = self._values.get("volume_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def volume_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#volume_type Instance#volume_type}.'''
        result = self._values.get("volume_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "InstanceRootBlockDevice(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class InstanceRootBlockDeviceOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.instance.InstanceRootBlockDeviceOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ed3ecd19f2cb02fcaa154c28447394da60bfd2163a364cb72860875e8211a9d6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b20f4e63f9adbcb41dfcd992cf13f4cd92c482a8bea4114d3a94bcd6e6214caa)
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
            type_hints = typing.get_type_hints(_typecheckingstub__10737836622e51e5db83d549ce0b49c49561779da59f4a90bccf6cd6af3f7228)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encrypted", value)

    @builtins.property
    @jsii.member(jsii_name="iops")
    def iops(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "iops"))

    @iops.setter
    def iops(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__669e15e4e5558a47a18783e4138a12e26f71e32d0e1f156458f500ca071ca708)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iops", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7ee98652751a5f57a5a928ee9d7043440819a077f5f1be85eb32edd7e3b72a9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ff138e326bc8e8e9d24f20636c35b1c96b90a704b4e3c8a415ee475c43ddd1a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="throughput")
    def throughput(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "throughput"))

    @throughput.setter
    def throughput(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01c7b65ae03df157edd783df82c242642fcfcaa08d8e7c232db6398ae9e9b874)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "throughput", value)

    @builtins.property
    @jsii.member(jsii_name="volumeSize")
    def volume_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "volumeSize"))

    @volume_size.setter
    def volume_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba3e7dd19e72ac72d2cd944a1c748eaca2dbdf9b50d0f55efe192b87b0c41d0f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeSize", value)

    @builtins.property
    @jsii.member(jsii_name="volumeType")
    def volume_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "volumeType"))

    @volume_type.setter
    def volume_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0301d93a98f16bc74b48e17fbbc284297f8040e25bb9983661d2644cad5494cd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[InstanceRootBlockDevice]:
        return typing.cast(typing.Optional[InstanceRootBlockDevice], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[InstanceRootBlockDevice]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dfc76d1996a499b927dcf256c1eca8aed01f179145b3132a5f5869be6826934d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.instance.InstanceTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class InstanceTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#create Instance#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#delete Instance#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#update Instance#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d00ce7e586747846effc2b0aec62e1c122b4e073368bee1d8387479e71cc9bdc)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#create Instance#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#delete Instance#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/instance#update Instance#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "InstanceTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class InstanceTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.instance.InstanceTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__497a88418bfd7a5a6daac7d49ceef3f773a1df22e56e5add5e27dd87ad1bb8e2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__827e6d81199d516d5a61437563e7cc9bf89498098ed6d5289dd61ac66f6cd4ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b4c0e34e82a0c66e7bbe342d28a72dd3852ed9ea5591624766a8649454474de)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53a9454d08969f3e915da02db9b23b06bb076ed474404ca97131ef71373965c3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[InstanceTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[InstanceTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[InstanceTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed19b937cfa5656aaba0cf8ff85896f212e66a9991bfdaae9412bfb05df37f1c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Instance",
    "InstanceCapacityReservationSpecification",
    "InstanceCapacityReservationSpecificationCapacityReservationTarget",
    "InstanceCapacityReservationSpecificationCapacityReservationTargetOutputReference",
    "InstanceCapacityReservationSpecificationOutputReference",
    "InstanceConfig",
    "InstanceCreditSpecification",
    "InstanceCreditSpecificationOutputReference",
    "InstanceEbsBlockDevice",
    "InstanceEbsBlockDeviceList",
    "InstanceEbsBlockDeviceOutputReference",
    "InstanceEnclaveOptions",
    "InstanceEnclaveOptionsOutputReference",
    "InstanceEphemeralBlockDevice",
    "InstanceEphemeralBlockDeviceList",
    "InstanceEphemeralBlockDeviceOutputReference",
    "InstanceLaunchTemplate",
    "InstanceLaunchTemplateOutputReference",
    "InstanceMaintenanceOptions",
    "InstanceMaintenanceOptionsOutputReference",
    "InstanceMetadataOptions",
    "InstanceMetadataOptionsOutputReference",
    "InstanceNetworkInterface",
    "InstanceNetworkInterfaceList",
    "InstanceNetworkInterfaceOutputReference",
    "InstancePrivateDnsNameOptions",
    "InstancePrivateDnsNameOptionsOutputReference",
    "InstanceRootBlockDevice",
    "InstanceRootBlockDeviceOutputReference",
    "InstanceTimeouts",
    "InstanceTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__7e8d55dc87293dc31cb0e6b2998b30d68cbef4b407d3ecccbd6d98097ead1ebf(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    ami: typing.Optional[builtins.str] = None,
    associate_public_ip_address: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    availability_zone: typing.Optional[builtins.str] = None,
    capacity_reservation_specification: typing.Optional[typing.Union[InstanceCapacityReservationSpecification, typing.Dict[builtins.str, typing.Any]]] = None,
    cpu_core_count: typing.Optional[jsii.Number] = None,
    cpu_threads_per_core: typing.Optional[jsii.Number] = None,
    credit_specification: typing.Optional[typing.Union[InstanceCreditSpecification, typing.Dict[builtins.str, typing.Any]]] = None,
    disable_api_stop: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    disable_api_termination: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ebs_block_device: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[InstanceEbsBlockDevice, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ebs_optimized: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    enclave_options: typing.Optional[typing.Union[InstanceEnclaveOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    ephemeral_block_device: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[InstanceEphemeralBlockDevice, typing.Dict[builtins.str, typing.Any]]]]] = None,
    fetch_password_data: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    hibernation: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    host_id: typing.Optional[builtins.str] = None,
    host_resource_group_arn: typing.Optional[builtins.str] = None,
    iam_instance_profile: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    instance_initiated_shutdown_behavior: typing.Optional[builtins.str] = None,
    instance_type: typing.Optional[builtins.str] = None,
    ipv6_address_count: typing.Optional[jsii.Number] = None,
    ipv6_addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
    key_name: typing.Optional[builtins.str] = None,
    launch_template: typing.Optional[typing.Union[InstanceLaunchTemplate, typing.Dict[builtins.str, typing.Any]]] = None,
    maintenance_options: typing.Optional[typing.Union[InstanceMaintenanceOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    metadata_options: typing.Optional[typing.Union[InstanceMetadataOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    monitoring: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    network_interface: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[InstanceNetworkInterface, typing.Dict[builtins.str, typing.Any]]]]] = None,
    placement_group: typing.Optional[builtins.str] = None,
    placement_partition_number: typing.Optional[jsii.Number] = None,
    private_dns_name_options: typing.Optional[typing.Union[InstancePrivateDnsNameOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    private_ip: typing.Optional[builtins.str] = None,
    root_block_device: typing.Optional[typing.Union[InstanceRootBlockDevice, typing.Dict[builtins.str, typing.Any]]] = None,
    secondary_private_ips: typing.Optional[typing.Sequence[builtins.str]] = None,
    security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    source_dest_check: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    subnet_id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tenancy: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[InstanceTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    user_data: typing.Optional[builtins.str] = None,
    user_data_base64: typing.Optional[builtins.str] = None,
    user_data_replace_on_change: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    volume_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
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

def _typecheckingstub__693f73f01597266ce5944c40fa45b198793e60fd15463228ac5709605a08ef6c(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[InstanceEbsBlockDevice, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__593555a4452d5eddb688153f85ee7c06d6bbc2622a7937959587485a6dd02ce2(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[InstanceEphemeralBlockDevice, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__867d20f81a8001062ca64661b5f9df466060cf0a802bf25a6a2ce0b020b73195(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[InstanceNetworkInterface, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01a0b9d394ae027f05619b363c59f24a2582ad2570326668fdd2603a4d9dd9ae(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2bebd1eec6c8417d3152b4bd78f034b4178855fbd9a1aa41b5a584ca8a39311(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f27f005ee936668dd0c3ec9cf19128c6c082c7c70e5978fc6685bd37eb459328(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fbab0ad5f392e66baaa47daf67761eed3d1f0336c9f47e13a8f26f9e70eaabe4(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b6673f1e29d387f7c991cc5072af21f028e4a2243e1c2629a8c7f545c0c3310(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd1e1c6d01926603b6f1fd8ba9f98ccc479206ba6a5787c269afa43dd857bd81(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35ce2cba45fe76dc1b9dd7114e0981a6f5956e97ffe3aabb9dc820def66037a4(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__060e74062f59aefee1b461885289b77f1a87d3b601f831e3713c66758891fec4(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2ab6e2d8cbb15b056f36a1423de0e5d5196283f485c2abfde1c283ef5ea26ac(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb3363fba13424721335a2b986fd3256ebf7d64de6434c26262f63a8bb1451a9(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f31be7c8c821bef709ad4a46d3b9152e72fc3f3e4c9a1807f63adac302cfb407(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6e31deecefbf988610f74867879f1a0d5bc6db76ad822b10979738e42d7c6db(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6e2cfcf5ffb2f1ef39297839896005fef7475ce855a67de6265e07687a102d3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27b633a6c515b844c84fef4b49df9ce0aa0f313518082fab19da1bfe3f4bafa0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__105364139b6ff4bbd3ca15ab648077727b77d0f7f1e9f86ba534ebd98aee5803(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ef12c81496a03ea882cb304e3c01ab0c6f2220bdd97b75ed74612f7ae51cd04(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66f9cf4fc2ffe0a337c347c8e53d1afa83d895378443695ecde97ae102dc1573(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a2ea71aa9ed1eba27d797babe42c32de859c27324e8deb5c12929f7ca717fb9(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__189bb180f738517b66a627d2c31fbfe4cad32642c5d03f0a533339bc9df84ee3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__027bd2d926b379ee3763b1d39a99d8622539c7b5ba88d3953bd3137258236ff9(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ecf7f8c59d6d95dc01afc4c660cafe9960ccf3f8e719be6dfe16c922876d7521(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c7bafd652431837fb9fbc73bdf55f07a82e211990cb7c6d9cf1a3aee56baeeb(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__642b496bff52c044839005e1c11dea51787d00584dfdc70a309e4d7a9c68ce3e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f475721baf9376560ac7e9ededbe1e7174605a9f5c65cacebb73b19b422968c7(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06553c8be05181c04f89a7b65530e9fd671dfe3292e173b9fd594994500ea8ef(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a29eef2281b0b0a64bdef23d94b9056b3e8e2aa0295fe80c10453efeca66954c(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5a9fab4949504867be73302b56f908fe5c91b7dc88379baaf5835ef4cc7e7ad(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db19e627ab731257267605e4392faf1387a1ec5c70cda89c66c8007791960f29(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68cea80e70fc41846c08b429828201dcd374d65976eb5d0c5aef173c703e3b19(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c2a5ff9fbce38b50061ef4b6f9f88c761d9811670bf8024a23512d5f46faef0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f7ecd2fbdfec2b4bed3aaa37e3d25b452a158cae1701d4b7c7bba29993fc55e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__994bcaacde8405ae2b0816cc884e4c364671f8c5cd3e0adfaaea9bbdbbada2ea(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20e6f0a09ae3b3d31fa7427939a218a5aa5bfa5d9347c00432dbe27f1294279a(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ec77a33ee37e0962bb285a3dd9d66587c72dc302423b988be618bd02d9e7465(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a19cac030142e395fda2170e631c8db9537cde6c1940f3482e55ff8835762961(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09788016be568da2d6fc0b18cd3ea903553213b3e80808974664edbd57c99b49(
    *,
    capacity_reservation_preference: typing.Optional[builtins.str] = None,
    capacity_reservation_target: typing.Optional[typing.Union[InstanceCapacityReservationSpecificationCapacityReservationTarget, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b436946f220a61223675395086fd310afe27938ab3fb5c383d7886c1cb5a10de(
    *,
    capacity_reservation_id: typing.Optional[builtins.str] = None,
    capacity_reservation_resource_group_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2fb16ac548a6468edcc1b999edb2bb5dc4cffa89f21cba50ba7d2b1b31d2556(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c920f1eff8484839c283a5ce13fc0cd66013a40872838217303ae85d9cb1e64d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__273866d02acaa19952f832b0bbf3f24c07b6e3905e415c8fd5b5c7b40aba7003(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74506afb94bad3395c50c09b9e58b0ab5ae7949914be7efb28f569860cdaa1d8(
    value: typing.Optional[InstanceCapacityReservationSpecificationCapacityReservationTarget],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11e77cbf9a7b2d7408ea561b392557d16649e714c6a7af3f8519120bc5936c87(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bfd91ed1394abf3d0e7230f2dd77ca33da90f851ef5310694cba56cd88d11ea3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df5e26b003078b39abbafaa7f4c338147f9fa0a5e60ce77036b82b4207c23ce6(
    value: typing.Optional[InstanceCapacityReservationSpecification],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9d0e398fa56e354f7cace934be4cb4e560cac06ad9f7f33b9b31fe765b0f0cf(
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
    capacity_reservation_specification: typing.Optional[typing.Union[InstanceCapacityReservationSpecification, typing.Dict[builtins.str, typing.Any]]] = None,
    cpu_core_count: typing.Optional[jsii.Number] = None,
    cpu_threads_per_core: typing.Optional[jsii.Number] = None,
    credit_specification: typing.Optional[typing.Union[InstanceCreditSpecification, typing.Dict[builtins.str, typing.Any]]] = None,
    disable_api_stop: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    disable_api_termination: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ebs_block_device: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[InstanceEbsBlockDevice, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ebs_optimized: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    enclave_options: typing.Optional[typing.Union[InstanceEnclaveOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    ephemeral_block_device: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[InstanceEphemeralBlockDevice, typing.Dict[builtins.str, typing.Any]]]]] = None,
    fetch_password_data: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    hibernation: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    host_id: typing.Optional[builtins.str] = None,
    host_resource_group_arn: typing.Optional[builtins.str] = None,
    iam_instance_profile: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    instance_initiated_shutdown_behavior: typing.Optional[builtins.str] = None,
    instance_type: typing.Optional[builtins.str] = None,
    ipv6_address_count: typing.Optional[jsii.Number] = None,
    ipv6_addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
    key_name: typing.Optional[builtins.str] = None,
    launch_template: typing.Optional[typing.Union[InstanceLaunchTemplate, typing.Dict[builtins.str, typing.Any]]] = None,
    maintenance_options: typing.Optional[typing.Union[InstanceMaintenanceOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    metadata_options: typing.Optional[typing.Union[InstanceMetadataOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    monitoring: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    network_interface: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[InstanceNetworkInterface, typing.Dict[builtins.str, typing.Any]]]]] = None,
    placement_group: typing.Optional[builtins.str] = None,
    placement_partition_number: typing.Optional[jsii.Number] = None,
    private_dns_name_options: typing.Optional[typing.Union[InstancePrivateDnsNameOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    private_ip: typing.Optional[builtins.str] = None,
    root_block_device: typing.Optional[typing.Union[InstanceRootBlockDevice, typing.Dict[builtins.str, typing.Any]]] = None,
    secondary_private_ips: typing.Optional[typing.Sequence[builtins.str]] = None,
    security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    source_dest_check: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    subnet_id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tenancy: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[InstanceTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    user_data: typing.Optional[builtins.str] = None,
    user_data_base64: typing.Optional[builtins.str] = None,
    user_data_replace_on_change: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    volume_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    vpc_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e690b60c8249d5a0bdef6c15a6619348c08a7f044869caa6c5d0635a9c17bc77(
    *,
    cpu_credits: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30e56f3d795f832706eba827d57575a8f7ec9180ca5cc9b175ccb747f4afe20e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b0fabe0f10de70f02418d38c83bd69cffde3bd0fc962069b07662c947ceed18(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aed6aa854c4da169d9db5720d71836caebdc9d9fbcaaf12692a6794f108b50ec(
    value: typing.Optional[InstanceCreditSpecification],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd45affc685598bfe82ffb468c3bb9b7027c7be984f42da93cffc4028163f9be(
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

def _typecheckingstub__c375cf4614247f22cfcbcc9c5198e01d4512f1b2ed0f8c092e1da67f9188d257(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0662b855603257f7fa53335dd90671135f52eb5a044023bda949160aefa0e03a(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41f2e542491d8580e728554ffc635501565d604249e2cd63d5c986afb014f4a0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b85b3f5f2728c3bf53d14e0f3c1eef40e20b88ed15dd6d423992bd06b4c40e78(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d96a9b5e7b1246349a5fae202ab9a4e5f9a1bbeca0e38fb1cfafdaa400dcabb6(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c81a33d3542f9f137b85454fff058cd4981893dfc3b84d7728e6ccf3a53de66(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[InstanceEbsBlockDevice]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__140d12119bf33c11d2f35437151a8faa78a171db48b58eccb144a90728f554af(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61dbd94ae83723e61652cbf9e3904227acfd7b8bc5f48440bf6c8774e1914626(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e46623a75d9f29947db60dbe069391cc8eba3b097a7870b56a14e72bb5c57272(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__147398409818416b7c0a3613c0e02fd18797f0dc2caec106546d05ad6df3bf19(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0de237405562f9c0e1eec91179fec9e5b3775c684eb247ae7342603149609fba(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b655b27881d29de6f0e14768becb1186ea92638eb5759f0e03ca57113a7a827b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ec57ccbdc736f7f44bcdb004fd0e51007415653bfeae745a6bee3f84ea839ba(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8bde32cd7706666e800888791bdcc29fa27f9d77612793ac68273c416bce3e02(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59460812fb0197fd15c5eaea1548e238ccc4184ca314d10a3d000d3dd574fa9b(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2cc95237f6af43b11ed043526478a2fc00a6a936e41fbe43d07d3a14e0fc3532(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f6c280508e1859c6b623bb98eb85f11a573930639cd17e3ad846184db72b79b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__645bd52498c34349cb16e4dbc231ebdf98e567b9ce2d8f9282397f2953927b86(
    value: typing.Optional[typing.Union[InstanceEbsBlockDevice, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d57a17aa778cfbc80e926ba46e5f3497ac71c91c0f168f8dd16c50475c5c162a(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3197806f9867e25b73b128d4c8e6c375354164cd65299cd20aa4ac028d1e9a10(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a3e25935bd571091217e1ec88dc583fd5ed613e1260bccc97aeacd4f2d2f0be(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b44a6c3ef9c486df1c3de722cc15bf8b200555455e667d8d4a21bc0a7afea7e2(
    value: typing.Optional[InstanceEnclaveOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5dce1c45f8d2403d8790cc931b39ffb61df956508471ab742581a1d0686993b9(
    *,
    device_name: builtins.str,
    no_device: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    virtual_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__579ea018d7444e569bf2c4c5e266d09f5cd63ef6bb4e9130d2ccfb88c684fe9d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56a4d48aa4dd5a382ac0a599403a65c3687747e7a95a7215ad1f352a91bf4555(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__838f5a1da6eb28995cae96c8e683d709b159873026f5a1be1e590167513b98af(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0029b847ea2acc29eeb86264b5b848ff335a8e3bcf78b65387cc2815932490a1(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b293791a2490863af7f3d77562a267bacc65fb2077411571907818fefcc1b2ee(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8962556e7ee27ab4f40470e801764ca909f70345345756e3d2327ab0d7f4bbc4(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[InstanceEphemeralBlockDevice]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a5f5a07288162851bded77460948ccfef3aea55ef8da3744f3d96dd06d26e77(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2b690d7b9702558e4ef3e6dcf4abb339c5645c41f9c12afd13acad273c20fe0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2dbca96218f5aa616a6dca09a3cad6db1cb714063f0207a670412e4224abfc2(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41ac9197d437d7739a96bfa1043b8c5224f4ad1507427a17a2018909e62f51d9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49d4742d0a2039bfef3a49a5b9577dc2a59321ffa771f9de875b10e611d56733(
    value: typing.Optional[typing.Union[InstanceEphemeralBlockDevice, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0042778c6c497227aeb9b73b0a535fc85e09970f2c957e9e9ff1da46922aad98(
    *,
    id: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc45a46ccc01cac3281f5ab75d45c9c3b69461825d0f56dac6a6c216d8b93fa0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5b3f66348dc6b9bd08168f596d9e97a7dde907a6be74a3048cb93a2e315d38f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f721f4e1092bd2318dab60ab2da3f3c592ce3950a2917f1bf4bcffea647f3b4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a8657eb94160930117756c373c4b9cff66466ffeb625a0a147868037a1c9f31(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f79446a12ab42cd4313a3c6ec0c80403585e39bacc693347ef4beb95f4cbc353(
    value: typing.Optional[InstanceLaunchTemplate],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96f8560d843674ce96734c6472485e26c5009d3a50c4b3849994a598c9afb4a5(
    *,
    auto_recovery: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d17370b442f57e438e441651874d7975720fc5e801c5a477fd8d4796cfda61c8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be2ccc0e56a34e61ec5601005bbcbf8e834c75a923531d7d60bd2b5f46a12ec3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5362dc72c9002aa9598e1e8af5102e4880dfac29d2d53b5338e4a11c6a5a6cac(
    value: typing.Optional[InstanceMaintenanceOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4b45db7f54783aac95e83a5e86491fb6898f6661e54dd279312399b9324dfe4(
    *,
    http_endpoint: typing.Optional[builtins.str] = None,
    http_put_response_hop_limit: typing.Optional[jsii.Number] = None,
    http_tokens: typing.Optional[builtins.str] = None,
    instance_metadata_tags: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a4bde2f0377012e596d6c0d68f254d7ff535bfef48c70981debce8e63cdccb2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ceaa6b00c5f4deece90a12a710c9d0ffe2092d340d1cc71429c1936ab5d71f5e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8da27750cf69b66d1b512d3bae4c3e82cf5230cde82c60be59318d82bb343541(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c80bb7961821ac398534528fb625769b7db96dfd1a215290460a4720da22b50b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d15b84c0b3498cc6d31399ee26ada48c9e42137d049ef59bc5d715f6ca9f4e1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d190291b8c3c17224f55a795b111e8704ebdab6a7095f472c57b87ea77565a7(
    value: typing.Optional[InstanceMetadataOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56e55429abca02a270b795e01c4288e158862e8199d27cd9ca946c3cc750b57a(
    *,
    device_index: jsii.Number,
    network_interface_id: builtins.str,
    delete_on_termination: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    network_card_index: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77f9a01254e8bcd46446d41f8e27f6d8a398534b9e314f1d0d4bd70eadc784f4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8cf3c4b5ca41aa457670e8ebd8c7158db3260915512a4f440cc9962507b60c24(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1dfdd17b75a4a9b3b88a12deb2531e3d698483db9721472750187b0f9402f05d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aae02287300e9123322037e7a540886effeeb2caced47355f921d2e676930f6c(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dac553d77cccfc5e574710c5e5277453d8dcc45e8fbda6b10586fc7d64788928(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80c2da2d98cea146e301e5e2617d299fa89c30784ce355676620f9eda78caead(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[InstanceNetworkInterface]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa56cca7135b27382b70f93f1c4c370ec76182360e47b7bc0d62ea3fc0dcf9f4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d86836ef4ea5a6f9bb654b7aee1375cb648f423b1d9fcc4b50ed0a27ee3a4aa0(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ef61ed9ad22e7decfe53c20f885f4da56f0e04b900e6993c63e07c3b57afa52(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9808b261f3acc5995d4c69b15609d593a62f1c24c8126899f314fb6aa587bc2(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e698f2442bdd28664aab96d0322d0d7a697f7797e192080c0456de68ffdc974a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fae936725f98dc037a6c842bb7bc55dedab02fb5aca66900ee156a23dfd8eacd(
    value: typing.Optional[typing.Union[InstanceNetworkInterface, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dba4bdb05c25391fdf978b41bf91e4fb4b405bf291876a3d65130b42e62fcb86(
    *,
    enable_resource_name_dns_aaaa_record: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    enable_resource_name_dns_a_record: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    hostname_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6e66637eadf12072472daa589322237ca979a504c25a46f8379a26db9fec3d3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__936db1a6f4e2a10822ac3aae56cd0fff177237c1a11b2101ac1751d8a0c8f35b(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8715db362c116602c7414e047fcdb0aa33e3f782d4b513e559ff2e74e1ad332d(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ef96278a92555bb71cab25d2537ffb007f96a048b3e52c68231cb01eeaf2454(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f16435124c464bd898bca62093aee123317c4b04318bf5b58d36ff9f7624820(
    value: typing.Optional[InstancePrivateDnsNameOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d8f738287afd9ac9bca22b75f7ba22fc61431d724bd1c3c79763a25cd284d96(
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

def _typecheckingstub__ed3ecd19f2cb02fcaa154c28447394da60bfd2163a364cb72860875e8211a9d6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b20f4e63f9adbcb41dfcd992cf13f4cd92c482a8bea4114d3a94bcd6e6214caa(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10737836622e51e5db83d549ce0b49c49561779da59f4a90bccf6cd6af3f7228(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__669e15e4e5558a47a18783e4138a12e26f71e32d0e1f156458f500ca071ca708(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7ee98652751a5f57a5a928ee9d7043440819a077f5f1be85eb32edd7e3b72a9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ff138e326bc8e8e9d24f20636c35b1c96b90a704b4e3c8a415ee475c43ddd1a(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01c7b65ae03df157edd783df82c242642fcfcaa08d8e7c232db6398ae9e9b874(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba3e7dd19e72ac72d2cd944a1c748eaca2dbdf9b50d0f55efe192b87b0c41d0f(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0301d93a98f16bc74b48e17fbbc284297f8040e25bb9983661d2644cad5494cd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dfc76d1996a499b927dcf256c1eca8aed01f179145b3132a5f5869be6826934d(
    value: typing.Optional[InstanceRootBlockDevice],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d00ce7e586747846effc2b0aec62e1c122b4e073368bee1d8387479e71cc9bdc(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__497a88418bfd7a5a6daac7d49ceef3f773a1df22e56e5add5e27dd87ad1bb8e2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__827e6d81199d516d5a61437563e7cc9bf89498098ed6d5289dd61ac66f6cd4ce(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b4c0e34e82a0c66e7bbe342d28a72dd3852ed9ea5591624766a8649454474de(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53a9454d08969f3e915da02db9b23b06bb076ed474404ca97131ef71373965c3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed19b937cfa5656aaba0cf8ff85896f212e66a9991bfdaae9412bfb05df37f1c(
    value: typing.Optional[typing.Union[InstanceTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
