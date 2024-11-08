'''
# `aws_emr_cluster`

Refer to the Terraform Registory for docs: [`aws_emr_cluster`](https://www.terraform.io/docs/providers/aws/r/emr_cluster).
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


class EmrCluster(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.emrCluster.EmrCluster",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster aws_emr_cluster}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        release_label: builtins.str,
        service_role: builtins.str,
        additional_info: typing.Optional[builtins.str] = None,
        applications: typing.Optional[typing.Sequence[builtins.str]] = None,
        autoscaling_role: typing.Optional[builtins.str] = None,
        auto_termination_policy: typing.Optional[typing.Union["EmrClusterAutoTerminationPolicy", typing.Dict[builtins.str, typing.Any]]] = None,
        bootstrap_action: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EmrClusterBootstrapAction", typing.Dict[builtins.str, typing.Any]]]]] = None,
        configurations: typing.Optional[builtins.str] = None,
        configurations_json: typing.Optional[builtins.str] = None,
        core_instance_fleet: typing.Optional[typing.Union["EmrClusterCoreInstanceFleet", typing.Dict[builtins.str, typing.Any]]] = None,
        core_instance_group: typing.Optional[typing.Union["EmrClusterCoreInstanceGroup", typing.Dict[builtins.str, typing.Any]]] = None,
        custom_ami_id: typing.Optional[builtins.str] = None,
        ebs_root_volume_size: typing.Optional[jsii.Number] = None,
        ec2_attributes: typing.Optional[typing.Union["EmrClusterEc2Attributes", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        keep_job_flow_alive_when_no_steps: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        kerberos_attributes: typing.Optional[typing.Union["EmrClusterKerberosAttributes", typing.Dict[builtins.str, typing.Any]]] = None,
        list_steps_states: typing.Optional[typing.Sequence[builtins.str]] = None,
        log_encryption_kms_key_id: typing.Optional[builtins.str] = None,
        log_uri: typing.Optional[builtins.str] = None,
        master_instance_fleet: typing.Optional[typing.Union["EmrClusterMasterInstanceFleet", typing.Dict[builtins.str, typing.Any]]] = None,
        master_instance_group: typing.Optional[typing.Union["EmrClusterMasterInstanceGroup", typing.Dict[builtins.str, typing.Any]]] = None,
        scale_down_behavior: typing.Optional[builtins.str] = None,
        security_configuration: typing.Optional[builtins.str] = None,
        step: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EmrClusterStep", typing.Dict[builtins.str, typing.Any]]]]] = None,
        step_concurrency_level: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        termination_protection: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        visible_to_all_users: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster aws_emr_cluster} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#name EmrCluster#name}.
        :param release_label: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#release_label EmrCluster#release_label}.
        :param service_role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#service_role EmrCluster#service_role}.
        :param additional_info: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#additional_info EmrCluster#additional_info}.
        :param applications: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#applications EmrCluster#applications}.
        :param autoscaling_role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#autoscaling_role EmrCluster#autoscaling_role}.
        :param auto_termination_policy: auto_termination_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#auto_termination_policy EmrCluster#auto_termination_policy}
        :param bootstrap_action: bootstrap_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#bootstrap_action EmrCluster#bootstrap_action}
        :param configurations: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#configurations EmrCluster#configurations}.
        :param configurations_json: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#configurations_json EmrCluster#configurations_json}.
        :param core_instance_fleet: core_instance_fleet block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#core_instance_fleet EmrCluster#core_instance_fleet}
        :param core_instance_group: core_instance_group block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#core_instance_group EmrCluster#core_instance_group}
        :param custom_ami_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#custom_ami_id EmrCluster#custom_ami_id}.
        :param ebs_root_volume_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#ebs_root_volume_size EmrCluster#ebs_root_volume_size}.
        :param ec2_attributes: ec2_attributes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#ec2_attributes EmrCluster#ec2_attributes}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#id EmrCluster#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param keep_job_flow_alive_when_no_steps: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#keep_job_flow_alive_when_no_steps EmrCluster#keep_job_flow_alive_when_no_steps}.
        :param kerberos_attributes: kerberos_attributes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#kerberos_attributes EmrCluster#kerberos_attributes}
        :param list_steps_states: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#list_steps_states EmrCluster#list_steps_states}.
        :param log_encryption_kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#log_encryption_kms_key_id EmrCluster#log_encryption_kms_key_id}.
        :param log_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#log_uri EmrCluster#log_uri}.
        :param master_instance_fleet: master_instance_fleet block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#master_instance_fleet EmrCluster#master_instance_fleet}
        :param master_instance_group: master_instance_group block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#master_instance_group EmrCluster#master_instance_group}
        :param scale_down_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#scale_down_behavior EmrCluster#scale_down_behavior}.
        :param security_configuration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#security_configuration EmrCluster#security_configuration}.
        :param step: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#step EmrCluster#step}.
        :param step_concurrency_level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#step_concurrency_level EmrCluster#step_concurrency_level}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#tags EmrCluster#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#tags_all EmrCluster#tags_all}.
        :param termination_protection: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#termination_protection EmrCluster#termination_protection}.
        :param visible_to_all_users: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#visible_to_all_users EmrCluster#visible_to_all_users}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__decd9d60ae973c9fadffaacebb1de0c0526ef015418985036906fdcf7a5e4966)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = EmrClusterConfig(
            name=name,
            release_label=release_label,
            service_role=service_role,
            additional_info=additional_info,
            applications=applications,
            autoscaling_role=autoscaling_role,
            auto_termination_policy=auto_termination_policy,
            bootstrap_action=bootstrap_action,
            configurations=configurations,
            configurations_json=configurations_json,
            core_instance_fleet=core_instance_fleet,
            core_instance_group=core_instance_group,
            custom_ami_id=custom_ami_id,
            ebs_root_volume_size=ebs_root_volume_size,
            ec2_attributes=ec2_attributes,
            id=id,
            keep_job_flow_alive_when_no_steps=keep_job_flow_alive_when_no_steps,
            kerberos_attributes=kerberos_attributes,
            list_steps_states=list_steps_states,
            log_encryption_kms_key_id=log_encryption_kms_key_id,
            log_uri=log_uri,
            master_instance_fleet=master_instance_fleet,
            master_instance_group=master_instance_group,
            scale_down_behavior=scale_down_behavior,
            security_configuration=security_configuration,
            step=step,
            step_concurrency_level=step_concurrency_level,
            tags=tags,
            tags_all=tags_all,
            termination_protection=termination_protection,
            visible_to_all_users=visible_to_all_users,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAutoTerminationPolicy")
    def put_auto_termination_policy(
        self,
        *,
        idle_timeout: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param idle_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#idle_timeout EmrCluster#idle_timeout}.
        '''
        value = EmrClusterAutoTerminationPolicy(idle_timeout=idle_timeout)

        return typing.cast(None, jsii.invoke(self, "putAutoTerminationPolicy", [value]))

    @jsii.member(jsii_name="putBootstrapAction")
    def put_bootstrap_action(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EmrClusterBootstrapAction", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__edf9614b79c795c421df622d4c5cd5f1e3f1b88dd63f984a80c0b4ba9c0d7478)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putBootstrapAction", [value]))

    @jsii.member(jsii_name="putCoreInstanceFleet")
    def put_core_instance_fleet(
        self,
        *,
        instance_type_configs: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EmrClusterCoreInstanceFleetInstanceTypeConfigs", typing.Dict[builtins.str, typing.Any]]]]] = None,
        launch_specifications: typing.Optional[typing.Union["EmrClusterCoreInstanceFleetLaunchSpecifications", typing.Dict[builtins.str, typing.Any]]] = None,
        name: typing.Optional[builtins.str] = None,
        target_on_demand_capacity: typing.Optional[jsii.Number] = None,
        target_spot_capacity: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param instance_type_configs: instance_type_configs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#instance_type_configs EmrCluster#instance_type_configs}
        :param launch_specifications: launch_specifications block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#launch_specifications EmrCluster#launch_specifications}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#name EmrCluster#name}.
        :param target_on_demand_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#target_on_demand_capacity EmrCluster#target_on_demand_capacity}.
        :param target_spot_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#target_spot_capacity EmrCluster#target_spot_capacity}.
        '''
        value = EmrClusterCoreInstanceFleet(
            instance_type_configs=instance_type_configs,
            launch_specifications=launch_specifications,
            name=name,
            target_on_demand_capacity=target_on_demand_capacity,
            target_spot_capacity=target_spot_capacity,
        )

        return typing.cast(None, jsii.invoke(self, "putCoreInstanceFleet", [value]))

    @jsii.member(jsii_name="putCoreInstanceGroup")
    def put_core_instance_group(
        self,
        *,
        instance_type: builtins.str,
        autoscaling_policy: typing.Optional[builtins.str] = None,
        bid_price: typing.Optional[builtins.str] = None,
        ebs_config: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EmrClusterCoreInstanceGroupEbsConfig", typing.Dict[builtins.str, typing.Any]]]]] = None,
        instance_count: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param instance_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#instance_type EmrCluster#instance_type}.
        :param autoscaling_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#autoscaling_policy EmrCluster#autoscaling_policy}.
        :param bid_price: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#bid_price EmrCluster#bid_price}.
        :param ebs_config: ebs_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#ebs_config EmrCluster#ebs_config}
        :param instance_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#instance_count EmrCluster#instance_count}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#name EmrCluster#name}.
        '''
        value = EmrClusterCoreInstanceGroup(
            instance_type=instance_type,
            autoscaling_policy=autoscaling_policy,
            bid_price=bid_price,
            ebs_config=ebs_config,
            instance_count=instance_count,
            name=name,
        )

        return typing.cast(None, jsii.invoke(self, "putCoreInstanceGroup", [value]))

    @jsii.member(jsii_name="putEc2Attributes")
    def put_ec2_attributes(
        self,
        *,
        instance_profile: builtins.str,
        additional_master_security_groups: typing.Optional[builtins.str] = None,
        additional_slave_security_groups: typing.Optional[builtins.str] = None,
        emr_managed_master_security_group: typing.Optional[builtins.str] = None,
        emr_managed_slave_security_group: typing.Optional[builtins.str] = None,
        key_name: typing.Optional[builtins.str] = None,
        service_access_security_group: typing.Optional[builtins.str] = None,
        subnet_id: typing.Optional[builtins.str] = None,
        subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param instance_profile: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#instance_profile EmrCluster#instance_profile}.
        :param additional_master_security_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#additional_master_security_groups EmrCluster#additional_master_security_groups}.
        :param additional_slave_security_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#additional_slave_security_groups EmrCluster#additional_slave_security_groups}.
        :param emr_managed_master_security_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#emr_managed_master_security_group EmrCluster#emr_managed_master_security_group}.
        :param emr_managed_slave_security_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#emr_managed_slave_security_group EmrCluster#emr_managed_slave_security_group}.
        :param key_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#key_name EmrCluster#key_name}.
        :param service_access_security_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#service_access_security_group EmrCluster#service_access_security_group}.
        :param subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#subnet_id EmrCluster#subnet_id}.
        :param subnet_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#subnet_ids EmrCluster#subnet_ids}.
        '''
        value = EmrClusterEc2Attributes(
            instance_profile=instance_profile,
            additional_master_security_groups=additional_master_security_groups,
            additional_slave_security_groups=additional_slave_security_groups,
            emr_managed_master_security_group=emr_managed_master_security_group,
            emr_managed_slave_security_group=emr_managed_slave_security_group,
            key_name=key_name,
            service_access_security_group=service_access_security_group,
            subnet_id=subnet_id,
            subnet_ids=subnet_ids,
        )

        return typing.cast(None, jsii.invoke(self, "putEc2Attributes", [value]))

    @jsii.member(jsii_name="putKerberosAttributes")
    def put_kerberos_attributes(
        self,
        *,
        kdc_admin_password: builtins.str,
        realm: builtins.str,
        ad_domain_join_password: typing.Optional[builtins.str] = None,
        ad_domain_join_user: typing.Optional[builtins.str] = None,
        cross_realm_trust_principal_password: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param kdc_admin_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#kdc_admin_password EmrCluster#kdc_admin_password}.
        :param realm: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#realm EmrCluster#realm}.
        :param ad_domain_join_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#ad_domain_join_password EmrCluster#ad_domain_join_password}.
        :param ad_domain_join_user: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#ad_domain_join_user EmrCluster#ad_domain_join_user}.
        :param cross_realm_trust_principal_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#cross_realm_trust_principal_password EmrCluster#cross_realm_trust_principal_password}.
        '''
        value = EmrClusterKerberosAttributes(
            kdc_admin_password=kdc_admin_password,
            realm=realm,
            ad_domain_join_password=ad_domain_join_password,
            ad_domain_join_user=ad_domain_join_user,
            cross_realm_trust_principal_password=cross_realm_trust_principal_password,
        )

        return typing.cast(None, jsii.invoke(self, "putKerberosAttributes", [value]))

    @jsii.member(jsii_name="putMasterInstanceFleet")
    def put_master_instance_fleet(
        self,
        *,
        instance_type_configs: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EmrClusterMasterInstanceFleetInstanceTypeConfigs", typing.Dict[builtins.str, typing.Any]]]]] = None,
        launch_specifications: typing.Optional[typing.Union["EmrClusterMasterInstanceFleetLaunchSpecifications", typing.Dict[builtins.str, typing.Any]]] = None,
        name: typing.Optional[builtins.str] = None,
        target_on_demand_capacity: typing.Optional[jsii.Number] = None,
        target_spot_capacity: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param instance_type_configs: instance_type_configs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#instance_type_configs EmrCluster#instance_type_configs}
        :param launch_specifications: launch_specifications block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#launch_specifications EmrCluster#launch_specifications}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#name EmrCluster#name}.
        :param target_on_demand_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#target_on_demand_capacity EmrCluster#target_on_demand_capacity}.
        :param target_spot_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#target_spot_capacity EmrCluster#target_spot_capacity}.
        '''
        value = EmrClusterMasterInstanceFleet(
            instance_type_configs=instance_type_configs,
            launch_specifications=launch_specifications,
            name=name,
            target_on_demand_capacity=target_on_demand_capacity,
            target_spot_capacity=target_spot_capacity,
        )

        return typing.cast(None, jsii.invoke(self, "putMasterInstanceFleet", [value]))

    @jsii.member(jsii_name="putMasterInstanceGroup")
    def put_master_instance_group(
        self,
        *,
        instance_type: builtins.str,
        bid_price: typing.Optional[builtins.str] = None,
        ebs_config: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EmrClusterMasterInstanceGroupEbsConfig", typing.Dict[builtins.str, typing.Any]]]]] = None,
        instance_count: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param instance_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#instance_type EmrCluster#instance_type}.
        :param bid_price: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#bid_price EmrCluster#bid_price}.
        :param ebs_config: ebs_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#ebs_config EmrCluster#ebs_config}
        :param instance_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#instance_count EmrCluster#instance_count}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#name EmrCluster#name}.
        '''
        value = EmrClusterMasterInstanceGroup(
            instance_type=instance_type,
            bid_price=bid_price,
            ebs_config=ebs_config,
            instance_count=instance_count,
            name=name,
        )

        return typing.cast(None, jsii.invoke(self, "putMasterInstanceGroup", [value]))

    @jsii.member(jsii_name="putStep")
    def put_step(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EmrClusterStep", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a266b4811b6f47399d607f9b5755b01ed5ed3ef0a172173322b165647f2a8623)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putStep", [value]))

    @jsii.member(jsii_name="resetAdditionalInfo")
    def reset_additional_info(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdditionalInfo", []))

    @jsii.member(jsii_name="resetApplications")
    def reset_applications(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApplications", []))

    @jsii.member(jsii_name="resetAutoscalingRole")
    def reset_autoscaling_role(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoscalingRole", []))

    @jsii.member(jsii_name="resetAutoTerminationPolicy")
    def reset_auto_termination_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoTerminationPolicy", []))

    @jsii.member(jsii_name="resetBootstrapAction")
    def reset_bootstrap_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBootstrapAction", []))

    @jsii.member(jsii_name="resetConfigurations")
    def reset_configurations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfigurations", []))

    @jsii.member(jsii_name="resetConfigurationsJson")
    def reset_configurations_json(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfigurationsJson", []))

    @jsii.member(jsii_name="resetCoreInstanceFleet")
    def reset_core_instance_fleet(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCoreInstanceFleet", []))

    @jsii.member(jsii_name="resetCoreInstanceGroup")
    def reset_core_instance_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCoreInstanceGroup", []))

    @jsii.member(jsii_name="resetCustomAmiId")
    def reset_custom_ami_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomAmiId", []))

    @jsii.member(jsii_name="resetEbsRootVolumeSize")
    def reset_ebs_root_volume_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEbsRootVolumeSize", []))

    @jsii.member(jsii_name="resetEc2Attributes")
    def reset_ec2_attributes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEc2Attributes", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetKeepJobFlowAliveWhenNoSteps")
    def reset_keep_job_flow_alive_when_no_steps(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeepJobFlowAliveWhenNoSteps", []))

    @jsii.member(jsii_name="resetKerberosAttributes")
    def reset_kerberos_attributes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKerberosAttributes", []))

    @jsii.member(jsii_name="resetListStepsStates")
    def reset_list_steps_states(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetListStepsStates", []))

    @jsii.member(jsii_name="resetLogEncryptionKmsKeyId")
    def reset_log_encryption_kms_key_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogEncryptionKmsKeyId", []))

    @jsii.member(jsii_name="resetLogUri")
    def reset_log_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogUri", []))

    @jsii.member(jsii_name="resetMasterInstanceFleet")
    def reset_master_instance_fleet(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMasterInstanceFleet", []))

    @jsii.member(jsii_name="resetMasterInstanceGroup")
    def reset_master_instance_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMasterInstanceGroup", []))

    @jsii.member(jsii_name="resetScaleDownBehavior")
    def reset_scale_down_behavior(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScaleDownBehavior", []))

    @jsii.member(jsii_name="resetSecurityConfiguration")
    def reset_security_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecurityConfiguration", []))

    @jsii.member(jsii_name="resetStep")
    def reset_step(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStep", []))

    @jsii.member(jsii_name="resetStepConcurrencyLevel")
    def reset_step_concurrency_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStepConcurrencyLevel", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetTerminationProtection")
    def reset_termination_protection(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTerminationProtection", []))

    @jsii.member(jsii_name="resetVisibleToAllUsers")
    def reset_visible_to_all_users(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVisibleToAllUsers", []))

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
    @jsii.member(jsii_name="autoTerminationPolicy")
    def auto_termination_policy(
        self,
    ) -> "EmrClusterAutoTerminationPolicyOutputReference":
        return typing.cast("EmrClusterAutoTerminationPolicyOutputReference", jsii.get(self, "autoTerminationPolicy"))

    @builtins.property
    @jsii.member(jsii_name="bootstrapAction")
    def bootstrap_action(self) -> "EmrClusterBootstrapActionList":
        return typing.cast("EmrClusterBootstrapActionList", jsii.get(self, "bootstrapAction"))

    @builtins.property
    @jsii.member(jsii_name="clusterState")
    def cluster_state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterState"))

    @builtins.property
    @jsii.member(jsii_name="coreInstanceFleet")
    def core_instance_fleet(self) -> "EmrClusterCoreInstanceFleetOutputReference":
        return typing.cast("EmrClusterCoreInstanceFleetOutputReference", jsii.get(self, "coreInstanceFleet"))

    @builtins.property
    @jsii.member(jsii_name="coreInstanceGroup")
    def core_instance_group(self) -> "EmrClusterCoreInstanceGroupOutputReference":
        return typing.cast("EmrClusterCoreInstanceGroupOutputReference", jsii.get(self, "coreInstanceGroup"))

    @builtins.property
    @jsii.member(jsii_name="ec2Attributes")
    def ec2_attributes(self) -> "EmrClusterEc2AttributesOutputReference":
        return typing.cast("EmrClusterEc2AttributesOutputReference", jsii.get(self, "ec2Attributes"))

    @builtins.property
    @jsii.member(jsii_name="kerberosAttributes")
    def kerberos_attributes(self) -> "EmrClusterKerberosAttributesOutputReference":
        return typing.cast("EmrClusterKerberosAttributesOutputReference", jsii.get(self, "kerberosAttributes"))

    @builtins.property
    @jsii.member(jsii_name="masterInstanceFleet")
    def master_instance_fleet(self) -> "EmrClusterMasterInstanceFleetOutputReference":
        return typing.cast("EmrClusterMasterInstanceFleetOutputReference", jsii.get(self, "masterInstanceFleet"))

    @builtins.property
    @jsii.member(jsii_name="masterInstanceGroup")
    def master_instance_group(self) -> "EmrClusterMasterInstanceGroupOutputReference":
        return typing.cast("EmrClusterMasterInstanceGroupOutputReference", jsii.get(self, "masterInstanceGroup"))

    @builtins.property
    @jsii.member(jsii_name="masterPublicDns")
    def master_public_dns(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "masterPublicDns"))

    @builtins.property
    @jsii.member(jsii_name="step")
    def step(self) -> "EmrClusterStepList":
        return typing.cast("EmrClusterStepList", jsii.get(self, "step"))

    @builtins.property
    @jsii.member(jsii_name="additionalInfoInput")
    def additional_info_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "additionalInfoInput"))

    @builtins.property
    @jsii.member(jsii_name="applicationsInput")
    def applications_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "applicationsInput"))

    @builtins.property
    @jsii.member(jsii_name="autoscalingRoleInput")
    def autoscaling_role_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "autoscalingRoleInput"))

    @builtins.property
    @jsii.member(jsii_name="autoTerminationPolicyInput")
    def auto_termination_policy_input(
        self,
    ) -> typing.Optional["EmrClusterAutoTerminationPolicy"]:
        return typing.cast(typing.Optional["EmrClusterAutoTerminationPolicy"], jsii.get(self, "autoTerminationPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="bootstrapActionInput")
    def bootstrap_action_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EmrClusterBootstrapAction"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EmrClusterBootstrapAction"]]], jsii.get(self, "bootstrapActionInput"))

    @builtins.property
    @jsii.member(jsii_name="configurationsInput")
    def configurations_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "configurationsInput"))

    @builtins.property
    @jsii.member(jsii_name="configurationsJsonInput")
    def configurations_json_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "configurationsJsonInput"))

    @builtins.property
    @jsii.member(jsii_name="coreInstanceFleetInput")
    def core_instance_fleet_input(
        self,
    ) -> typing.Optional["EmrClusterCoreInstanceFleet"]:
        return typing.cast(typing.Optional["EmrClusterCoreInstanceFleet"], jsii.get(self, "coreInstanceFleetInput"))

    @builtins.property
    @jsii.member(jsii_name="coreInstanceGroupInput")
    def core_instance_group_input(
        self,
    ) -> typing.Optional["EmrClusterCoreInstanceGroup"]:
        return typing.cast(typing.Optional["EmrClusterCoreInstanceGroup"], jsii.get(self, "coreInstanceGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="customAmiIdInput")
    def custom_ami_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customAmiIdInput"))

    @builtins.property
    @jsii.member(jsii_name="ebsRootVolumeSizeInput")
    def ebs_root_volume_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ebsRootVolumeSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="ec2AttributesInput")
    def ec2_attributes_input(self) -> typing.Optional["EmrClusterEc2Attributes"]:
        return typing.cast(typing.Optional["EmrClusterEc2Attributes"], jsii.get(self, "ec2AttributesInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="keepJobFlowAliveWhenNoStepsInput")
    def keep_job_flow_alive_when_no_steps_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "keepJobFlowAliveWhenNoStepsInput"))

    @builtins.property
    @jsii.member(jsii_name="kerberosAttributesInput")
    def kerberos_attributes_input(
        self,
    ) -> typing.Optional["EmrClusterKerberosAttributes"]:
        return typing.cast(typing.Optional["EmrClusterKerberosAttributes"], jsii.get(self, "kerberosAttributesInput"))

    @builtins.property
    @jsii.member(jsii_name="listStepsStatesInput")
    def list_steps_states_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "listStepsStatesInput"))

    @builtins.property
    @jsii.member(jsii_name="logEncryptionKmsKeyIdInput")
    def log_encryption_kms_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logEncryptionKmsKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="logUriInput")
    def log_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logUriInput"))

    @builtins.property
    @jsii.member(jsii_name="masterInstanceFleetInput")
    def master_instance_fleet_input(
        self,
    ) -> typing.Optional["EmrClusterMasterInstanceFleet"]:
        return typing.cast(typing.Optional["EmrClusterMasterInstanceFleet"], jsii.get(self, "masterInstanceFleetInput"))

    @builtins.property
    @jsii.member(jsii_name="masterInstanceGroupInput")
    def master_instance_group_input(
        self,
    ) -> typing.Optional["EmrClusterMasterInstanceGroup"]:
        return typing.cast(typing.Optional["EmrClusterMasterInstanceGroup"], jsii.get(self, "masterInstanceGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="releaseLabelInput")
    def release_label_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "releaseLabelInput"))

    @builtins.property
    @jsii.member(jsii_name="scaleDownBehaviorInput")
    def scale_down_behavior_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scaleDownBehaviorInput"))

    @builtins.property
    @jsii.member(jsii_name="securityConfigurationInput")
    def security_configuration_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "securityConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceRoleInput")
    def service_role_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceRoleInput"))

    @builtins.property
    @jsii.member(jsii_name="stepConcurrencyLevelInput")
    def step_concurrency_level_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "stepConcurrencyLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="stepInput")
    def step_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EmrClusterStep"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EmrClusterStep"]]], jsii.get(self, "stepInput"))

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
    @jsii.member(jsii_name="terminationProtectionInput")
    def termination_protection_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "terminationProtectionInput"))

    @builtins.property
    @jsii.member(jsii_name="visibleToAllUsersInput")
    def visible_to_all_users_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "visibleToAllUsersInput"))

    @builtins.property
    @jsii.member(jsii_name="additionalInfo")
    def additional_info(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "additionalInfo"))

    @additional_info.setter
    def additional_info(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce6fcc38891a7ea94b37d44e44a0f3dc388fd972a4dca728cc55afd8d3b31769)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "additionalInfo", value)

    @builtins.property
    @jsii.member(jsii_name="applications")
    def applications(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "applications"))

    @applications.setter
    def applications(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__47fe81e4597ddb012564aa0dacaf580e4001fdbd3d67277563f7b381711d192c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applications", value)

    @builtins.property
    @jsii.member(jsii_name="autoscalingRole")
    def autoscaling_role(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "autoscalingRole"))

    @autoscaling_role.setter
    def autoscaling_role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__adcebc8984ac8e544b44c0c8164d6cbf5017968b244ce7dd855f2f4f11d4b498)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoscalingRole", value)

    @builtins.property
    @jsii.member(jsii_name="configurations")
    def configurations(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "configurations"))

    @configurations.setter
    def configurations(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b8ec072e8bd2325a11b3e44093adea00f67e8a95df73f0b9ca33dcfffef2c0a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configurations", value)

    @builtins.property
    @jsii.member(jsii_name="configurationsJson")
    def configurations_json(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "configurationsJson"))

    @configurations_json.setter
    def configurations_json(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__453067d9493b77778d130e5ae8e0b022c5c5683af4d5e11f35234310ce136001)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configurationsJson", value)

    @builtins.property
    @jsii.member(jsii_name="customAmiId")
    def custom_ami_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customAmiId"))

    @custom_ami_id.setter
    def custom_ami_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c877a8903592920550444f292d857b2ec76fee9a58bcbf2f36739e891dfa116)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customAmiId", value)

    @builtins.property
    @jsii.member(jsii_name="ebsRootVolumeSize")
    def ebs_root_volume_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ebsRootVolumeSize"))

    @ebs_root_volume_size.setter
    def ebs_root_volume_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__393245633c5f390f74cb462852e16e6e8c25598b1528c3efbd07883b6dd5d313)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ebsRootVolumeSize", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4be5cf26116bd7ae069ac7ddbc8072858e2b8198db4907615228bb8f595a18e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="keepJobFlowAliveWhenNoSteps")
    def keep_job_flow_alive_when_no_steps(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "keepJobFlowAliveWhenNoSteps"))

    @keep_job_flow_alive_when_no_steps.setter
    def keep_job_flow_alive_when_no_steps(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__118f556527576bebd4b5e13abf8c08c39a19278f2364d3c24b2eee62eac817d9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keepJobFlowAliveWhenNoSteps", value)

    @builtins.property
    @jsii.member(jsii_name="listStepsStates")
    def list_steps_states(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "listStepsStates"))

    @list_steps_states.setter
    def list_steps_states(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__244fc3f8219371f28e5e944bcc1d7b468e811ca9b991604acfdae24168f8cfbc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "listStepsStates", value)

    @builtins.property
    @jsii.member(jsii_name="logEncryptionKmsKeyId")
    def log_encryption_kms_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logEncryptionKmsKeyId"))

    @log_encryption_kms_key_id.setter
    def log_encryption_kms_key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a4f5d84e0a9e20820cc1d4ec64563e4cfcc6311b744a3c763ff0699e100a858)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logEncryptionKmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="logUri")
    def log_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logUri"))

    @log_uri.setter
    def log_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9dca4f75ff968b7ef7b47ca992c485ed518cf35302765d25307a0e822eba6933)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logUri", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9dbe351442b6d62742b372ab1e1bef91f89fd29eb00453109fcba65b61ad27b7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="releaseLabel")
    def release_label(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "releaseLabel"))

    @release_label.setter
    def release_label(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2fa41776a0809bcdf9e643ca5e55a7f97a60a458252dc5a56a151ba81832d764)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "releaseLabel", value)

    @builtins.property
    @jsii.member(jsii_name="scaleDownBehavior")
    def scale_down_behavior(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scaleDownBehavior"))

    @scale_down_behavior.setter
    def scale_down_behavior(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b79b5142c20e6fa1eae89e453bf5e2ffad9c9cb5fec3a39c63d17e4936c4a3f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scaleDownBehavior", value)

    @builtins.property
    @jsii.member(jsii_name="securityConfiguration")
    def security_configuration(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "securityConfiguration"))

    @security_configuration.setter
    def security_configuration(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cdad73f2fd0d2b7c0c099b509cd6699f7d1a6540f0e8546cef73200d3753ee81)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="serviceRole")
    def service_role(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceRole"))

    @service_role.setter
    def service_role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c1845077f1b032010fee8a360f1c44c5eb00154fafa5161cd54306e0e85f05f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceRole", value)

    @builtins.property
    @jsii.member(jsii_name="stepConcurrencyLevel")
    def step_concurrency_level(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "stepConcurrencyLevel"))

    @step_concurrency_level.setter
    def step_concurrency_level(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a700b06929ad929c9e6a6d531746d6aa8235f238e774004c41478903ce20a9bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stepConcurrencyLevel", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1e095a85480fe0c2dae28fa4a1d84cfe42259d28277b76a616d820c561b4dc3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0df33ff28fe7bfd82490c25c1f1823cb54094cbe28d25db90f58e49fd18fe60)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)

    @builtins.property
    @jsii.member(jsii_name="terminationProtection")
    def termination_protection(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "terminationProtection"))

    @termination_protection.setter
    def termination_protection(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72014be48fdfc85b15f8cabe696deccdc5bc9e107276f058f1ffff2310145855)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terminationProtection", value)

    @builtins.property
    @jsii.member(jsii_name="visibleToAllUsers")
    def visible_to_all_users(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "visibleToAllUsers"))

    @visible_to_all_users.setter
    def visible_to_all_users(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c170dc350316990e67c408397c1b035c352e1871a9f5bef33073a521d4589240)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "visibleToAllUsers", value)


@jsii.data_type(
    jsii_type="aws.emrCluster.EmrClusterAutoTerminationPolicy",
    jsii_struct_bases=[],
    name_mapping={"idle_timeout": "idleTimeout"},
)
class EmrClusterAutoTerminationPolicy:
    def __init__(self, *, idle_timeout: typing.Optional[jsii.Number] = None) -> None:
        '''
        :param idle_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#idle_timeout EmrCluster#idle_timeout}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f2a1904cfd52d1c8bacf02d44fc40eb5be4bb776925e4a6bc9c08871ade3275e)
            check_type(argname="argument idle_timeout", value=idle_timeout, expected_type=type_hints["idle_timeout"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if idle_timeout is not None:
            self._values["idle_timeout"] = idle_timeout

    @builtins.property
    def idle_timeout(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#idle_timeout EmrCluster#idle_timeout}.'''
        result = self._values.get("idle_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmrClusterAutoTerminationPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EmrClusterAutoTerminationPolicyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.emrCluster.EmrClusterAutoTerminationPolicyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3fb77bbce036f13a3d9b756eb7d0b65f68c70487d10c30d09ca0fd87119c8f8c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetIdleTimeout")
    def reset_idle_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdleTimeout", []))

    @builtins.property
    @jsii.member(jsii_name="idleTimeoutInput")
    def idle_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "idleTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="idleTimeout")
    def idle_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "idleTimeout"))

    @idle_timeout.setter
    def idle_timeout(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2a1c91ee4fa69fa76bc51531384f2d116058b427005133692aa958e49ff778d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "idleTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[EmrClusterAutoTerminationPolicy]:
        return typing.cast(typing.Optional[EmrClusterAutoTerminationPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EmrClusterAutoTerminationPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5708caa6df564d26078771f300fa5bc601eb89d08cf7137df4770d9493458455)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.emrCluster.EmrClusterBootstrapAction",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "path": "path", "args": "args"},
)
class EmrClusterBootstrapAction:
    def __init__(
        self,
        *,
        name: builtins.str,
        path: builtins.str,
        args: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#name EmrCluster#name}.
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#path EmrCluster#path}.
        :param args: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#args EmrCluster#args}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68c04741d0dda2d1401d0a2b27db34a1fa05e837ccd846b9c9c5a7cc66b5ca75)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument args", value=args, expected_type=type_hints["args"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "path": path,
        }
        if args is not None:
            self._values["args"] = args

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#name EmrCluster#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#path EmrCluster#path}.'''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def args(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#args EmrCluster#args}.'''
        result = self._values.get("args")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmrClusterBootstrapAction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EmrClusterBootstrapActionList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.emrCluster.EmrClusterBootstrapActionList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1721b89362240c326825086e166901c44421400772c7043acf311d5a70267de4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "EmrClusterBootstrapActionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad02f0a2349c5740635cbbec835a57ca3990273986bf628ca036066a614ed94f)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EmrClusterBootstrapActionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e497ffac6bcaa7f882769be9bfc05e2a65fad95225c467e4fedee3245bfc9b7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f340330493eed7a0b980032094813047e31f39481db3867948eac4ff3b8708b5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__30b46b2d54bf0883b370944e019cf0d7e2a8d4a9f7d28cb93c741baafab63bb1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterBootstrapAction]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterBootstrapAction]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterBootstrapAction]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1236045e2ac747c9d287696f24bee14919c1385ff9def432444222e76538b5f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EmrClusterBootstrapActionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.emrCluster.EmrClusterBootstrapActionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__00b51f5d216009e1b03c1ea3187dd4a644765bd2df1ad1ed681feabfb90611ea)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetArgs")
    def reset_args(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetArgs", []))

    @builtins.property
    @jsii.member(jsii_name="argsInput")
    def args_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "argsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="args")
    def args(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "args"))

    @args.setter
    def args(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80c113d78146151404b06cb2812327fd2d4a65c7d11b9643d590a9f6e3a2308f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "args", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0d87ba6829b0c43e0e2cec7a9a5b7841bb819d7d822b93ecd2e65d44c59941d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__88f2c12e0e4ee51b2b608756fd072ec29620fd029971ac3e8d170c458e1fb209)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EmrClusterBootstrapAction, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EmrClusterBootstrapAction, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EmrClusterBootstrapAction, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3a98bfce395876c6eb87d50cb73bfabc99bee4a0e9d9af39b9168075137fbc6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.emrCluster.EmrClusterConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "name": "name",
        "release_label": "releaseLabel",
        "service_role": "serviceRole",
        "additional_info": "additionalInfo",
        "applications": "applications",
        "autoscaling_role": "autoscalingRole",
        "auto_termination_policy": "autoTerminationPolicy",
        "bootstrap_action": "bootstrapAction",
        "configurations": "configurations",
        "configurations_json": "configurationsJson",
        "core_instance_fleet": "coreInstanceFleet",
        "core_instance_group": "coreInstanceGroup",
        "custom_ami_id": "customAmiId",
        "ebs_root_volume_size": "ebsRootVolumeSize",
        "ec2_attributes": "ec2Attributes",
        "id": "id",
        "keep_job_flow_alive_when_no_steps": "keepJobFlowAliveWhenNoSteps",
        "kerberos_attributes": "kerberosAttributes",
        "list_steps_states": "listStepsStates",
        "log_encryption_kms_key_id": "logEncryptionKmsKeyId",
        "log_uri": "logUri",
        "master_instance_fleet": "masterInstanceFleet",
        "master_instance_group": "masterInstanceGroup",
        "scale_down_behavior": "scaleDownBehavior",
        "security_configuration": "securityConfiguration",
        "step": "step",
        "step_concurrency_level": "stepConcurrencyLevel",
        "tags": "tags",
        "tags_all": "tagsAll",
        "termination_protection": "terminationProtection",
        "visible_to_all_users": "visibleToAllUsers",
    },
)
class EmrClusterConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        name: builtins.str,
        release_label: builtins.str,
        service_role: builtins.str,
        additional_info: typing.Optional[builtins.str] = None,
        applications: typing.Optional[typing.Sequence[builtins.str]] = None,
        autoscaling_role: typing.Optional[builtins.str] = None,
        auto_termination_policy: typing.Optional[typing.Union[EmrClusterAutoTerminationPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
        bootstrap_action: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EmrClusterBootstrapAction, typing.Dict[builtins.str, typing.Any]]]]] = None,
        configurations: typing.Optional[builtins.str] = None,
        configurations_json: typing.Optional[builtins.str] = None,
        core_instance_fleet: typing.Optional[typing.Union["EmrClusterCoreInstanceFleet", typing.Dict[builtins.str, typing.Any]]] = None,
        core_instance_group: typing.Optional[typing.Union["EmrClusterCoreInstanceGroup", typing.Dict[builtins.str, typing.Any]]] = None,
        custom_ami_id: typing.Optional[builtins.str] = None,
        ebs_root_volume_size: typing.Optional[jsii.Number] = None,
        ec2_attributes: typing.Optional[typing.Union["EmrClusterEc2Attributes", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        keep_job_flow_alive_when_no_steps: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        kerberos_attributes: typing.Optional[typing.Union["EmrClusterKerberosAttributes", typing.Dict[builtins.str, typing.Any]]] = None,
        list_steps_states: typing.Optional[typing.Sequence[builtins.str]] = None,
        log_encryption_kms_key_id: typing.Optional[builtins.str] = None,
        log_uri: typing.Optional[builtins.str] = None,
        master_instance_fleet: typing.Optional[typing.Union["EmrClusterMasterInstanceFleet", typing.Dict[builtins.str, typing.Any]]] = None,
        master_instance_group: typing.Optional[typing.Union["EmrClusterMasterInstanceGroup", typing.Dict[builtins.str, typing.Any]]] = None,
        scale_down_behavior: typing.Optional[builtins.str] = None,
        security_configuration: typing.Optional[builtins.str] = None,
        step: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EmrClusterStep", typing.Dict[builtins.str, typing.Any]]]]] = None,
        step_concurrency_level: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        termination_protection: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        visible_to_all_users: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#name EmrCluster#name}.
        :param release_label: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#release_label EmrCluster#release_label}.
        :param service_role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#service_role EmrCluster#service_role}.
        :param additional_info: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#additional_info EmrCluster#additional_info}.
        :param applications: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#applications EmrCluster#applications}.
        :param autoscaling_role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#autoscaling_role EmrCluster#autoscaling_role}.
        :param auto_termination_policy: auto_termination_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#auto_termination_policy EmrCluster#auto_termination_policy}
        :param bootstrap_action: bootstrap_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#bootstrap_action EmrCluster#bootstrap_action}
        :param configurations: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#configurations EmrCluster#configurations}.
        :param configurations_json: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#configurations_json EmrCluster#configurations_json}.
        :param core_instance_fleet: core_instance_fleet block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#core_instance_fleet EmrCluster#core_instance_fleet}
        :param core_instance_group: core_instance_group block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#core_instance_group EmrCluster#core_instance_group}
        :param custom_ami_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#custom_ami_id EmrCluster#custom_ami_id}.
        :param ebs_root_volume_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#ebs_root_volume_size EmrCluster#ebs_root_volume_size}.
        :param ec2_attributes: ec2_attributes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#ec2_attributes EmrCluster#ec2_attributes}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#id EmrCluster#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param keep_job_flow_alive_when_no_steps: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#keep_job_flow_alive_when_no_steps EmrCluster#keep_job_flow_alive_when_no_steps}.
        :param kerberos_attributes: kerberos_attributes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#kerberos_attributes EmrCluster#kerberos_attributes}
        :param list_steps_states: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#list_steps_states EmrCluster#list_steps_states}.
        :param log_encryption_kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#log_encryption_kms_key_id EmrCluster#log_encryption_kms_key_id}.
        :param log_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#log_uri EmrCluster#log_uri}.
        :param master_instance_fleet: master_instance_fleet block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#master_instance_fleet EmrCluster#master_instance_fleet}
        :param master_instance_group: master_instance_group block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#master_instance_group EmrCluster#master_instance_group}
        :param scale_down_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#scale_down_behavior EmrCluster#scale_down_behavior}.
        :param security_configuration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#security_configuration EmrCluster#security_configuration}.
        :param step: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#step EmrCluster#step}.
        :param step_concurrency_level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#step_concurrency_level EmrCluster#step_concurrency_level}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#tags EmrCluster#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#tags_all EmrCluster#tags_all}.
        :param termination_protection: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#termination_protection EmrCluster#termination_protection}.
        :param visible_to_all_users: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#visible_to_all_users EmrCluster#visible_to_all_users}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(auto_termination_policy, dict):
            auto_termination_policy = EmrClusterAutoTerminationPolicy(**auto_termination_policy)
        if isinstance(core_instance_fleet, dict):
            core_instance_fleet = EmrClusterCoreInstanceFleet(**core_instance_fleet)
        if isinstance(core_instance_group, dict):
            core_instance_group = EmrClusterCoreInstanceGroup(**core_instance_group)
        if isinstance(ec2_attributes, dict):
            ec2_attributes = EmrClusterEc2Attributes(**ec2_attributes)
        if isinstance(kerberos_attributes, dict):
            kerberos_attributes = EmrClusterKerberosAttributes(**kerberos_attributes)
        if isinstance(master_instance_fleet, dict):
            master_instance_fleet = EmrClusterMasterInstanceFleet(**master_instance_fleet)
        if isinstance(master_instance_group, dict):
            master_instance_group = EmrClusterMasterInstanceGroup(**master_instance_group)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__282119b5c3f4cc2badbb7b6569b212950a7071deeca1bc29bdda4ced3d0eaa24)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument release_label", value=release_label, expected_type=type_hints["release_label"])
            check_type(argname="argument service_role", value=service_role, expected_type=type_hints["service_role"])
            check_type(argname="argument additional_info", value=additional_info, expected_type=type_hints["additional_info"])
            check_type(argname="argument applications", value=applications, expected_type=type_hints["applications"])
            check_type(argname="argument autoscaling_role", value=autoscaling_role, expected_type=type_hints["autoscaling_role"])
            check_type(argname="argument auto_termination_policy", value=auto_termination_policy, expected_type=type_hints["auto_termination_policy"])
            check_type(argname="argument bootstrap_action", value=bootstrap_action, expected_type=type_hints["bootstrap_action"])
            check_type(argname="argument configurations", value=configurations, expected_type=type_hints["configurations"])
            check_type(argname="argument configurations_json", value=configurations_json, expected_type=type_hints["configurations_json"])
            check_type(argname="argument core_instance_fleet", value=core_instance_fleet, expected_type=type_hints["core_instance_fleet"])
            check_type(argname="argument core_instance_group", value=core_instance_group, expected_type=type_hints["core_instance_group"])
            check_type(argname="argument custom_ami_id", value=custom_ami_id, expected_type=type_hints["custom_ami_id"])
            check_type(argname="argument ebs_root_volume_size", value=ebs_root_volume_size, expected_type=type_hints["ebs_root_volume_size"])
            check_type(argname="argument ec2_attributes", value=ec2_attributes, expected_type=type_hints["ec2_attributes"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument keep_job_flow_alive_when_no_steps", value=keep_job_flow_alive_when_no_steps, expected_type=type_hints["keep_job_flow_alive_when_no_steps"])
            check_type(argname="argument kerberos_attributes", value=kerberos_attributes, expected_type=type_hints["kerberos_attributes"])
            check_type(argname="argument list_steps_states", value=list_steps_states, expected_type=type_hints["list_steps_states"])
            check_type(argname="argument log_encryption_kms_key_id", value=log_encryption_kms_key_id, expected_type=type_hints["log_encryption_kms_key_id"])
            check_type(argname="argument log_uri", value=log_uri, expected_type=type_hints["log_uri"])
            check_type(argname="argument master_instance_fleet", value=master_instance_fleet, expected_type=type_hints["master_instance_fleet"])
            check_type(argname="argument master_instance_group", value=master_instance_group, expected_type=type_hints["master_instance_group"])
            check_type(argname="argument scale_down_behavior", value=scale_down_behavior, expected_type=type_hints["scale_down_behavior"])
            check_type(argname="argument security_configuration", value=security_configuration, expected_type=type_hints["security_configuration"])
            check_type(argname="argument step", value=step, expected_type=type_hints["step"])
            check_type(argname="argument step_concurrency_level", value=step_concurrency_level, expected_type=type_hints["step_concurrency_level"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument termination_protection", value=termination_protection, expected_type=type_hints["termination_protection"])
            check_type(argname="argument visible_to_all_users", value=visible_to_all_users, expected_type=type_hints["visible_to_all_users"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "release_label": release_label,
            "service_role": service_role,
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
        if additional_info is not None:
            self._values["additional_info"] = additional_info
        if applications is not None:
            self._values["applications"] = applications
        if autoscaling_role is not None:
            self._values["autoscaling_role"] = autoscaling_role
        if auto_termination_policy is not None:
            self._values["auto_termination_policy"] = auto_termination_policy
        if bootstrap_action is not None:
            self._values["bootstrap_action"] = bootstrap_action
        if configurations is not None:
            self._values["configurations"] = configurations
        if configurations_json is not None:
            self._values["configurations_json"] = configurations_json
        if core_instance_fleet is not None:
            self._values["core_instance_fleet"] = core_instance_fleet
        if core_instance_group is not None:
            self._values["core_instance_group"] = core_instance_group
        if custom_ami_id is not None:
            self._values["custom_ami_id"] = custom_ami_id
        if ebs_root_volume_size is not None:
            self._values["ebs_root_volume_size"] = ebs_root_volume_size
        if ec2_attributes is not None:
            self._values["ec2_attributes"] = ec2_attributes
        if id is not None:
            self._values["id"] = id
        if keep_job_flow_alive_when_no_steps is not None:
            self._values["keep_job_flow_alive_when_no_steps"] = keep_job_flow_alive_when_no_steps
        if kerberos_attributes is not None:
            self._values["kerberos_attributes"] = kerberos_attributes
        if list_steps_states is not None:
            self._values["list_steps_states"] = list_steps_states
        if log_encryption_kms_key_id is not None:
            self._values["log_encryption_kms_key_id"] = log_encryption_kms_key_id
        if log_uri is not None:
            self._values["log_uri"] = log_uri
        if master_instance_fleet is not None:
            self._values["master_instance_fleet"] = master_instance_fleet
        if master_instance_group is not None:
            self._values["master_instance_group"] = master_instance_group
        if scale_down_behavior is not None:
            self._values["scale_down_behavior"] = scale_down_behavior
        if security_configuration is not None:
            self._values["security_configuration"] = security_configuration
        if step is not None:
            self._values["step"] = step
        if step_concurrency_level is not None:
            self._values["step_concurrency_level"] = step_concurrency_level
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if termination_protection is not None:
            self._values["termination_protection"] = termination_protection
        if visible_to_all_users is not None:
            self._values["visible_to_all_users"] = visible_to_all_users

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
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#name EmrCluster#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def release_label(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#release_label EmrCluster#release_label}.'''
        result = self._values.get("release_label")
        assert result is not None, "Required property 'release_label' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_role(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#service_role EmrCluster#service_role}.'''
        result = self._values.get("service_role")
        assert result is not None, "Required property 'service_role' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def additional_info(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#additional_info EmrCluster#additional_info}.'''
        result = self._values.get("additional_info")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def applications(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#applications EmrCluster#applications}.'''
        result = self._values.get("applications")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def autoscaling_role(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#autoscaling_role EmrCluster#autoscaling_role}.'''
        result = self._values.get("autoscaling_role")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def auto_termination_policy(
        self,
    ) -> typing.Optional[EmrClusterAutoTerminationPolicy]:
        '''auto_termination_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#auto_termination_policy EmrCluster#auto_termination_policy}
        '''
        result = self._values.get("auto_termination_policy")
        return typing.cast(typing.Optional[EmrClusterAutoTerminationPolicy], result)

    @builtins.property
    def bootstrap_action(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterBootstrapAction]]]:
        '''bootstrap_action block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#bootstrap_action EmrCluster#bootstrap_action}
        '''
        result = self._values.get("bootstrap_action")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterBootstrapAction]]], result)

    @builtins.property
    def configurations(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#configurations EmrCluster#configurations}.'''
        result = self._values.get("configurations")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def configurations_json(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#configurations_json EmrCluster#configurations_json}.'''
        result = self._values.get("configurations_json")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def core_instance_fleet(self) -> typing.Optional["EmrClusterCoreInstanceFleet"]:
        '''core_instance_fleet block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#core_instance_fleet EmrCluster#core_instance_fleet}
        '''
        result = self._values.get("core_instance_fleet")
        return typing.cast(typing.Optional["EmrClusterCoreInstanceFleet"], result)

    @builtins.property
    def core_instance_group(self) -> typing.Optional["EmrClusterCoreInstanceGroup"]:
        '''core_instance_group block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#core_instance_group EmrCluster#core_instance_group}
        '''
        result = self._values.get("core_instance_group")
        return typing.cast(typing.Optional["EmrClusterCoreInstanceGroup"], result)

    @builtins.property
    def custom_ami_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#custom_ami_id EmrCluster#custom_ami_id}.'''
        result = self._values.get("custom_ami_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ebs_root_volume_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#ebs_root_volume_size EmrCluster#ebs_root_volume_size}.'''
        result = self._values.get("ebs_root_volume_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ec2_attributes(self) -> typing.Optional["EmrClusterEc2Attributes"]:
        '''ec2_attributes block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#ec2_attributes EmrCluster#ec2_attributes}
        '''
        result = self._values.get("ec2_attributes")
        return typing.cast(typing.Optional["EmrClusterEc2Attributes"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#id EmrCluster#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def keep_job_flow_alive_when_no_steps(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#keep_job_flow_alive_when_no_steps EmrCluster#keep_job_flow_alive_when_no_steps}.'''
        result = self._values.get("keep_job_flow_alive_when_no_steps")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def kerberos_attributes(self) -> typing.Optional["EmrClusterKerberosAttributes"]:
        '''kerberos_attributes block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#kerberos_attributes EmrCluster#kerberos_attributes}
        '''
        result = self._values.get("kerberos_attributes")
        return typing.cast(typing.Optional["EmrClusterKerberosAttributes"], result)

    @builtins.property
    def list_steps_states(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#list_steps_states EmrCluster#list_steps_states}.'''
        result = self._values.get("list_steps_states")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def log_encryption_kms_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#log_encryption_kms_key_id EmrCluster#log_encryption_kms_key_id}.'''
        result = self._values.get("log_encryption_kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_uri(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#log_uri EmrCluster#log_uri}.'''
        result = self._values.get("log_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def master_instance_fleet(self) -> typing.Optional["EmrClusterMasterInstanceFleet"]:
        '''master_instance_fleet block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#master_instance_fleet EmrCluster#master_instance_fleet}
        '''
        result = self._values.get("master_instance_fleet")
        return typing.cast(typing.Optional["EmrClusterMasterInstanceFleet"], result)

    @builtins.property
    def master_instance_group(self) -> typing.Optional["EmrClusterMasterInstanceGroup"]:
        '''master_instance_group block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#master_instance_group EmrCluster#master_instance_group}
        '''
        result = self._values.get("master_instance_group")
        return typing.cast(typing.Optional["EmrClusterMasterInstanceGroup"], result)

    @builtins.property
    def scale_down_behavior(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#scale_down_behavior EmrCluster#scale_down_behavior}.'''
        result = self._values.get("scale_down_behavior")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def security_configuration(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#security_configuration EmrCluster#security_configuration}.'''
        result = self._values.get("security_configuration")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def step(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EmrClusterStep"]]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#step EmrCluster#step}.'''
        result = self._values.get("step")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EmrClusterStep"]]], result)

    @builtins.property
    def step_concurrency_level(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#step_concurrency_level EmrCluster#step_concurrency_level}.'''
        result = self._values.get("step_concurrency_level")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#tags EmrCluster#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#tags_all EmrCluster#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def termination_protection(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#termination_protection EmrCluster#termination_protection}.'''
        result = self._values.get("termination_protection")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def visible_to_all_users(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#visible_to_all_users EmrCluster#visible_to_all_users}.'''
        result = self._values.get("visible_to_all_users")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmrClusterConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.emrCluster.EmrClusterCoreInstanceFleet",
    jsii_struct_bases=[],
    name_mapping={
        "instance_type_configs": "instanceTypeConfigs",
        "launch_specifications": "launchSpecifications",
        "name": "name",
        "target_on_demand_capacity": "targetOnDemandCapacity",
        "target_spot_capacity": "targetSpotCapacity",
    },
)
class EmrClusterCoreInstanceFleet:
    def __init__(
        self,
        *,
        instance_type_configs: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EmrClusterCoreInstanceFleetInstanceTypeConfigs", typing.Dict[builtins.str, typing.Any]]]]] = None,
        launch_specifications: typing.Optional[typing.Union["EmrClusterCoreInstanceFleetLaunchSpecifications", typing.Dict[builtins.str, typing.Any]]] = None,
        name: typing.Optional[builtins.str] = None,
        target_on_demand_capacity: typing.Optional[jsii.Number] = None,
        target_spot_capacity: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param instance_type_configs: instance_type_configs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#instance_type_configs EmrCluster#instance_type_configs}
        :param launch_specifications: launch_specifications block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#launch_specifications EmrCluster#launch_specifications}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#name EmrCluster#name}.
        :param target_on_demand_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#target_on_demand_capacity EmrCluster#target_on_demand_capacity}.
        :param target_spot_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#target_spot_capacity EmrCluster#target_spot_capacity}.
        '''
        if isinstance(launch_specifications, dict):
            launch_specifications = EmrClusterCoreInstanceFleetLaunchSpecifications(**launch_specifications)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c8b6de47dc972386f6bdd9adfd14f6bb9cea8fecf7c619692e6b892bdf7a33e)
            check_type(argname="argument instance_type_configs", value=instance_type_configs, expected_type=type_hints["instance_type_configs"])
            check_type(argname="argument launch_specifications", value=launch_specifications, expected_type=type_hints["launch_specifications"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument target_on_demand_capacity", value=target_on_demand_capacity, expected_type=type_hints["target_on_demand_capacity"])
            check_type(argname="argument target_spot_capacity", value=target_spot_capacity, expected_type=type_hints["target_spot_capacity"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
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
    def instance_type_configs(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EmrClusterCoreInstanceFleetInstanceTypeConfigs"]]]:
        '''instance_type_configs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#instance_type_configs EmrCluster#instance_type_configs}
        '''
        result = self._values.get("instance_type_configs")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EmrClusterCoreInstanceFleetInstanceTypeConfigs"]]], result)

    @builtins.property
    def launch_specifications(
        self,
    ) -> typing.Optional["EmrClusterCoreInstanceFleetLaunchSpecifications"]:
        '''launch_specifications block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#launch_specifications EmrCluster#launch_specifications}
        '''
        result = self._values.get("launch_specifications")
        return typing.cast(typing.Optional["EmrClusterCoreInstanceFleetLaunchSpecifications"], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#name EmrCluster#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_on_demand_capacity(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#target_on_demand_capacity EmrCluster#target_on_demand_capacity}.'''
        result = self._values.get("target_on_demand_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def target_spot_capacity(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#target_spot_capacity EmrCluster#target_spot_capacity}.'''
        result = self._values.get("target_spot_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmrClusterCoreInstanceFleet(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.emrCluster.EmrClusterCoreInstanceFleetInstanceTypeConfigs",
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
class EmrClusterCoreInstanceFleetInstanceTypeConfigs:
    def __init__(
        self,
        *,
        instance_type: builtins.str,
        bid_price: typing.Optional[builtins.str] = None,
        bid_price_as_percentage_of_on_demand_price: typing.Optional[jsii.Number] = None,
        configurations: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EmrClusterCoreInstanceFleetInstanceTypeConfigsConfigurations", typing.Dict[builtins.str, typing.Any]]]]] = None,
        ebs_config: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EmrClusterCoreInstanceFleetInstanceTypeConfigsEbsConfig", typing.Dict[builtins.str, typing.Any]]]]] = None,
        weighted_capacity: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param instance_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#instance_type EmrCluster#instance_type}.
        :param bid_price: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#bid_price EmrCluster#bid_price}.
        :param bid_price_as_percentage_of_on_demand_price: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#bid_price_as_percentage_of_on_demand_price EmrCluster#bid_price_as_percentage_of_on_demand_price}.
        :param configurations: configurations block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#configurations EmrCluster#configurations}
        :param ebs_config: ebs_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#ebs_config EmrCluster#ebs_config}
        :param weighted_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#weighted_capacity EmrCluster#weighted_capacity}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c6914a8d43c41217051cb416426c502d16cce8db87c9f9e04926c8a4c2e41b54)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#instance_type EmrCluster#instance_type}.'''
        result = self._values.get("instance_type")
        assert result is not None, "Required property 'instance_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bid_price(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#bid_price EmrCluster#bid_price}.'''
        result = self._values.get("bid_price")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bid_price_as_percentage_of_on_demand_price(
        self,
    ) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#bid_price_as_percentage_of_on_demand_price EmrCluster#bid_price_as_percentage_of_on_demand_price}.'''
        result = self._values.get("bid_price_as_percentage_of_on_demand_price")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def configurations(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EmrClusterCoreInstanceFleetInstanceTypeConfigsConfigurations"]]]:
        '''configurations block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#configurations EmrCluster#configurations}
        '''
        result = self._values.get("configurations")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EmrClusterCoreInstanceFleetInstanceTypeConfigsConfigurations"]]], result)

    @builtins.property
    def ebs_config(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EmrClusterCoreInstanceFleetInstanceTypeConfigsEbsConfig"]]]:
        '''ebs_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#ebs_config EmrCluster#ebs_config}
        '''
        result = self._values.get("ebs_config")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EmrClusterCoreInstanceFleetInstanceTypeConfigsEbsConfig"]]], result)

    @builtins.property
    def weighted_capacity(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#weighted_capacity EmrCluster#weighted_capacity}.'''
        result = self._values.get("weighted_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmrClusterCoreInstanceFleetInstanceTypeConfigs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.emrCluster.EmrClusterCoreInstanceFleetInstanceTypeConfigsConfigurations",
    jsii_struct_bases=[],
    name_mapping={"classification": "classification", "properties": "properties"},
)
class EmrClusterCoreInstanceFleetInstanceTypeConfigsConfigurations:
    def __init__(
        self,
        *,
        classification: typing.Optional[builtins.str] = None,
        properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param classification: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#classification EmrCluster#classification}.
        :param properties: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#properties EmrCluster#properties}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5905decadb215eea36ba30d6af82ba34ab49ec8f2a14a89211b4708a34d21a28)
            check_type(argname="argument classification", value=classification, expected_type=type_hints["classification"])
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if classification is not None:
            self._values["classification"] = classification
        if properties is not None:
            self._values["properties"] = properties

    @builtins.property
    def classification(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#classification EmrCluster#classification}.'''
        result = self._values.get("classification")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def properties(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#properties EmrCluster#properties}.'''
        result = self._values.get("properties")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmrClusterCoreInstanceFleetInstanceTypeConfigsConfigurations(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EmrClusterCoreInstanceFleetInstanceTypeConfigsConfigurationsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.emrCluster.EmrClusterCoreInstanceFleetInstanceTypeConfigsConfigurationsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__03f48ff30d5e4f56087e1eec11437b63ce70b087446cfd3ba078d93c1316965d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EmrClusterCoreInstanceFleetInstanceTypeConfigsConfigurationsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d77fbdae8a7a1c6ba64046526236574534547b1d87cc861add049653195b7667)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EmrClusterCoreInstanceFleetInstanceTypeConfigsConfigurationsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3bf2c108be5808a20b074389cfdfb87f9e97bc313feeefc0e1297f28a7be60d4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__99bd9b2621c8b5b14bdc848334b56f95c4571eaf5f6aee50a661ac0b75b7315b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f3018f38db392d153f149122a79cb723840411496bcecbb04ba475b3bd76ce11)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterCoreInstanceFleetInstanceTypeConfigsConfigurations]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterCoreInstanceFleetInstanceTypeConfigsConfigurations]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterCoreInstanceFleetInstanceTypeConfigsConfigurations]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a4154ac926a25a6fa7cea4b992a249f8385573ec096028be7f39dee67d363df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EmrClusterCoreInstanceFleetInstanceTypeConfigsConfigurationsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.emrCluster.EmrClusterCoreInstanceFleetInstanceTypeConfigsConfigurationsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__caa2d9d1c3d39f3400cd1b9875b273792a2e46bee26ed3b5a4e965a4754c6f6d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__33efd3afedbb979b01434b213a6c2df7d5d18f40ef72b2ed5abb0c650ae8ca56)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "classification", value)

    @builtins.property
    @jsii.member(jsii_name="properties")
    def properties(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "properties"))

    @properties.setter
    def properties(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0debe8f93b5ac914b708ff93621264834b4d13131ca855a85bb85f5ceb095493)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "properties", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EmrClusterCoreInstanceFleetInstanceTypeConfigsConfigurations, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EmrClusterCoreInstanceFleetInstanceTypeConfigsConfigurations, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EmrClusterCoreInstanceFleetInstanceTypeConfigsConfigurations, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57028a26d3dcdcd3e03fd72d85a6e8baf913b3688641f816ca3d4129160e4e4c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.emrCluster.EmrClusterCoreInstanceFleetInstanceTypeConfigsEbsConfig",
    jsii_struct_bases=[],
    name_mapping={
        "size": "size",
        "type": "type",
        "iops": "iops",
        "volumes_per_instance": "volumesPerInstance",
    },
)
class EmrClusterCoreInstanceFleetInstanceTypeConfigsEbsConfig:
    def __init__(
        self,
        *,
        size: jsii.Number,
        type: builtins.str,
        iops: typing.Optional[jsii.Number] = None,
        volumes_per_instance: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#size EmrCluster#size}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#type EmrCluster#type}.
        :param iops: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#iops EmrCluster#iops}.
        :param volumes_per_instance: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#volumes_per_instance EmrCluster#volumes_per_instance}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9098f1b36ff37cb986723c6edfb1706c84734f4ac69171244e82ba07ee4beb1d)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#size EmrCluster#size}.'''
        result = self._values.get("size")
        assert result is not None, "Required property 'size' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#type EmrCluster#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def iops(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#iops EmrCluster#iops}.'''
        result = self._values.get("iops")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def volumes_per_instance(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#volumes_per_instance EmrCluster#volumes_per_instance}.'''
        result = self._values.get("volumes_per_instance")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmrClusterCoreInstanceFleetInstanceTypeConfigsEbsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EmrClusterCoreInstanceFleetInstanceTypeConfigsEbsConfigList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.emrCluster.EmrClusterCoreInstanceFleetInstanceTypeConfigsEbsConfigList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__af1aff2fc0b119786dba85a4c5ceac5beaa4a4f48ce2a4c5271c6f962f30a5e1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EmrClusterCoreInstanceFleetInstanceTypeConfigsEbsConfigOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4615a212c3a135e4a810e34e267ea69777bd3d88020686884d1f9ba48431066c)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EmrClusterCoreInstanceFleetInstanceTypeConfigsEbsConfigOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c71c66f298cb2e99f475a096ebb623d633e084b52d677829961092900f681672)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0ffc9526d23a6485a6eb0c982e8ab8f82b6efe0e7b42f68ebcc9621ce3c6703e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__bdf43164a0a2c377c49fb35e3843b9dc55ebcf50df5c5940043b24549987df45)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterCoreInstanceFleetInstanceTypeConfigsEbsConfig]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterCoreInstanceFleetInstanceTypeConfigsEbsConfig]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterCoreInstanceFleetInstanceTypeConfigsEbsConfig]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1fa2c8d45f8f6b66bb1dccedfb011a8abece2ad8ade941a262073157ee6e9fc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EmrClusterCoreInstanceFleetInstanceTypeConfigsEbsConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.emrCluster.EmrClusterCoreInstanceFleetInstanceTypeConfigsEbsConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ee23aae122b20f4a05bf1ac6c1264cc25c9d2cbd56e1b27cc47c75f7c100ec07)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4235a098cbe2da14d7ff23ede9c8a08250909cbb951fb30fd501d3e1d18bde5e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iops", value)

    @builtins.property
    @jsii.member(jsii_name="size")
    def size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "size"))

    @size.setter
    def size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__46591c8bd1349f280e76e2d68393c3e1793923d907142bf0bde5a887c4b0a361)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "size", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dcea8f3da30373fa275458019cf58d6f33a91ea8cf93a61d0d8a2c1ca01e36a6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="volumesPerInstance")
    def volumes_per_instance(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "volumesPerInstance"))

    @volumes_per_instance.setter
    def volumes_per_instance(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a4dd1e365e809be93d441adb0e78586a8849acd9383a313df9dfb5008c857e7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumesPerInstance", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EmrClusterCoreInstanceFleetInstanceTypeConfigsEbsConfig, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EmrClusterCoreInstanceFleetInstanceTypeConfigsEbsConfig, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EmrClusterCoreInstanceFleetInstanceTypeConfigsEbsConfig, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9424a15398ea01ab60ca57855ff1fc43a4f2d18bc8f9b62ae4655ab1b834d7f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EmrClusterCoreInstanceFleetInstanceTypeConfigsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.emrCluster.EmrClusterCoreInstanceFleetInstanceTypeConfigsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__448419ae3285dd15b7cbffc65bd851c984ef17ad9dcac4a3dec41246369e71a2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EmrClusterCoreInstanceFleetInstanceTypeConfigsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__548d359e936e9c92dace12cd2cf0b27c25b59d557730b8187875c252926c5571)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EmrClusterCoreInstanceFleetInstanceTypeConfigsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d51b611c1682da8d40fae6cbadcfa33bee074eabca540b72d6f8776ac4e03039)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e717b0fdc3d4a4277c1e9b9b2d4b08d09a20bee9b8f5284eac1e259677894121)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c3f5203b3c0218f2820f1ca9517a7aad251968752a2350be41798762ff2b9838)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterCoreInstanceFleetInstanceTypeConfigs]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterCoreInstanceFleetInstanceTypeConfigs]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterCoreInstanceFleetInstanceTypeConfigs]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__682a491197093f0cf8abb5c7414c7a7439ac66ca30c795dec67c25223be6398c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EmrClusterCoreInstanceFleetInstanceTypeConfigsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.emrCluster.EmrClusterCoreInstanceFleetInstanceTypeConfigsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__882f8977cb369d96ed90c009094a557203db07d51a68de2e31529aafa9e3dc8c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putConfigurations")
    def put_configurations(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EmrClusterCoreInstanceFleetInstanceTypeConfigsConfigurations, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b95f737edfbcbdba2dbccd30a9f6f884b2905d4c9d6f79d25124a6d0a0baea3f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putConfigurations", [value]))

    @jsii.member(jsii_name="putEbsConfig")
    def put_ebs_config(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EmrClusterCoreInstanceFleetInstanceTypeConfigsEbsConfig, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4519fd3e7840c87f685e1b202289833267898fef6357731d2c05f2fc677da30f)
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
    def configurations(
        self,
    ) -> EmrClusterCoreInstanceFleetInstanceTypeConfigsConfigurationsList:
        return typing.cast(EmrClusterCoreInstanceFleetInstanceTypeConfigsConfigurationsList, jsii.get(self, "configurations"))

    @builtins.property
    @jsii.member(jsii_name="ebsConfig")
    def ebs_config(self) -> EmrClusterCoreInstanceFleetInstanceTypeConfigsEbsConfigList:
        return typing.cast(EmrClusterCoreInstanceFleetInstanceTypeConfigsEbsConfigList, jsii.get(self, "ebsConfig"))

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
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterCoreInstanceFleetInstanceTypeConfigsConfigurations]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterCoreInstanceFleetInstanceTypeConfigsConfigurations]]], jsii.get(self, "configurationsInput"))

    @builtins.property
    @jsii.member(jsii_name="ebsConfigInput")
    def ebs_config_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterCoreInstanceFleetInstanceTypeConfigsEbsConfig]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterCoreInstanceFleetInstanceTypeConfigsEbsConfig]]], jsii.get(self, "ebsConfigInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__59a41709911c2fa0135ae4ff8644430129af8be624bda8c183c2f0a077e002d1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bidPrice", value)

    @builtins.property
    @jsii.member(jsii_name="bidPriceAsPercentageOfOnDemandPrice")
    def bid_price_as_percentage_of_on_demand_price(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "bidPriceAsPercentageOfOnDemandPrice"))

    @bid_price_as_percentage_of_on_demand_price.setter
    def bid_price_as_percentage_of_on_demand_price(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3b2ae5609f01913506eac91e9ee3bfee0720edefdf0331acaa0ec044ac890a6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bidPriceAsPercentageOfOnDemandPrice", value)

    @builtins.property
    @jsii.member(jsii_name="instanceType")
    def instance_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceType"))

    @instance_type.setter
    def instance_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b29424db561a4412bc5960f58861eea1de9df319471be88002ab576aa07bba49)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceType", value)

    @builtins.property
    @jsii.member(jsii_name="weightedCapacity")
    def weighted_capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "weightedCapacity"))

    @weighted_capacity.setter
    def weighted_capacity(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53ad4200fafa58999af50d9c0bb79d80400a25d5b85a18282b2852aef07e662a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "weightedCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EmrClusterCoreInstanceFleetInstanceTypeConfigs, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EmrClusterCoreInstanceFleetInstanceTypeConfigs, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EmrClusterCoreInstanceFleetInstanceTypeConfigs, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf56f7c51f0ec88050b6c04101dc6517249a49c83a2cf9dec2a5ac201968b6d1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.emrCluster.EmrClusterCoreInstanceFleetLaunchSpecifications",
    jsii_struct_bases=[],
    name_mapping={
        "on_demand_specification": "onDemandSpecification",
        "spot_specification": "spotSpecification",
    },
)
class EmrClusterCoreInstanceFleetLaunchSpecifications:
    def __init__(
        self,
        *,
        on_demand_specification: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EmrClusterCoreInstanceFleetLaunchSpecificationsOnDemandSpecification", typing.Dict[builtins.str, typing.Any]]]]] = None,
        spot_specification: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EmrClusterCoreInstanceFleetLaunchSpecificationsSpotSpecification", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param on_demand_specification: on_demand_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#on_demand_specification EmrCluster#on_demand_specification}
        :param spot_specification: spot_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#spot_specification EmrCluster#spot_specification}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e2604fab7f7d4824d1093b0c21263658597f4a64e2a597376c7403f697fdbcb)
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
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EmrClusterCoreInstanceFleetLaunchSpecificationsOnDemandSpecification"]]]:
        '''on_demand_specification block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#on_demand_specification EmrCluster#on_demand_specification}
        '''
        result = self._values.get("on_demand_specification")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EmrClusterCoreInstanceFleetLaunchSpecificationsOnDemandSpecification"]]], result)

    @builtins.property
    def spot_specification(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EmrClusterCoreInstanceFleetLaunchSpecificationsSpotSpecification"]]]:
        '''spot_specification block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#spot_specification EmrCluster#spot_specification}
        '''
        result = self._values.get("spot_specification")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EmrClusterCoreInstanceFleetLaunchSpecificationsSpotSpecification"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmrClusterCoreInstanceFleetLaunchSpecifications(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.emrCluster.EmrClusterCoreInstanceFleetLaunchSpecificationsOnDemandSpecification",
    jsii_struct_bases=[],
    name_mapping={"allocation_strategy": "allocationStrategy"},
)
class EmrClusterCoreInstanceFleetLaunchSpecificationsOnDemandSpecification:
    def __init__(self, *, allocation_strategy: builtins.str) -> None:
        '''
        :param allocation_strategy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#allocation_strategy EmrCluster#allocation_strategy}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c95f4bdffb8cf166811663dfc1852c08b1411fc6e9a645fa244ef058f630a2b)
            check_type(argname="argument allocation_strategy", value=allocation_strategy, expected_type=type_hints["allocation_strategy"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "allocation_strategy": allocation_strategy,
        }

    @builtins.property
    def allocation_strategy(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#allocation_strategy EmrCluster#allocation_strategy}.'''
        result = self._values.get("allocation_strategy")
        assert result is not None, "Required property 'allocation_strategy' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmrClusterCoreInstanceFleetLaunchSpecificationsOnDemandSpecification(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EmrClusterCoreInstanceFleetLaunchSpecificationsOnDemandSpecificationList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.emrCluster.EmrClusterCoreInstanceFleetLaunchSpecificationsOnDemandSpecificationList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__03454b942830d233578457e1da787e7cdf9f8ec5d306003c0d2c2b9f31654fc7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EmrClusterCoreInstanceFleetLaunchSpecificationsOnDemandSpecificationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7932e8290bb4dcb5cc48c95c2dfd57b9b3ecc48b1c223159f1426543b2517d3a)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EmrClusterCoreInstanceFleetLaunchSpecificationsOnDemandSpecificationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e28f6aaab7d6155c86a89882edc43e4e575bafe5e51d3914d6d243dedb02bb29)
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
            type_hints = typing.get_type_hints(_typecheckingstub__22532de53650504c2ebd7ad9053bdfba3272ef29a72dfc6180667a749350cc5f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8548b99f33d347093b1ba54248fe19e7d16043f2b9f208c318334f3d6b3e23d3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterCoreInstanceFleetLaunchSpecificationsOnDemandSpecification]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterCoreInstanceFleetLaunchSpecificationsOnDemandSpecification]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterCoreInstanceFleetLaunchSpecificationsOnDemandSpecification]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0dffe4674148086c6a1d6028f7d8b77851a5930533c570fcc5b7c4268b68a16)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EmrClusterCoreInstanceFleetLaunchSpecificationsOnDemandSpecificationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.emrCluster.EmrClusterCoreInstanceFleetLaunchSpecificationsOnDemandSpecificationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__78df058fd7d560caffca20936ea9fc6792efeeec7f9bc8322f525606e1ad3383)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a852f5b81b89663f109b66f74f0856af5909d15f36df227c33bb93e5aed0dc72)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allocationStrategy", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EmrClusterCoreInstanceFleetLaunchSpecificationsOnDemandSpecification, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EmrClusterCoreInstanceFleetLaunchSpecificationsOnDemandSpecification, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EmrClusterCoreInstanceFleetLaunchSpecificationsOnDemandSpecification, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dcab4ec59eeb10b1d785072d3cdb2232fb0597622ccf534639237dcb87c4591a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EmrClusterCoreInstanceFleetLaunchSpecificationsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.emrCluster.EmrClusterCoreInstanceFleetLaunchSpecificationsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3659729a677a39060832e753568ab169086b8d6fbed426a382f809052c382bfc)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putOnDemandSpecification")
    def put_on_demand_specification(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EmrClusterCoreInstanceFleetLaunchSpecificationsOnDemandSpecification, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f112f87b722d472b1a70c45aa628e5b8b2b252c7e8952077969404c863cdb59)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putOnDemandSpecification", [value]))

    @jsii.member(jsii_name="putSpotSpecification")
    def put_spot_specification(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EmrClusterCoreInstanceFleetLaunchSpecificationsSpotSpecification", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__662f54f39c1322786b5b61dcc7fb21c4592e8e696daa1ccb060a2401c6c764fc)
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
    ) -> EmrClusterCoreInstanceFleetLaunchSpecificationsOnDemandSpecificationList:
        return typing.cast(EmrClusterCoreInstanceFleetLaunchSpecificationsOnDemandSpecificationList, jsii.get(self, "onDemandSpecification"))

    @builtins.property
    @jsii.member(jsii_name="spotSpecification")
    def spot_specification(
        self,
    ) -> "EmrClusterCoreInstanceFleetLaunchSpecificationsSpotSpecificationList":
        return typing.cast("EmrClusterCoreInstanceFleetLaunchSpecificationsSpotSpecificationList", jsii.get(self, "spotSpecification"))

    @builtins.property
    @jsii.member(jsii_name="onDemandSpecificationInput")
    def on_demand_specification_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterCoreInstanceFleetLaunchSpecificationsOnDemandSpecification]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterCoreInstanceFleetLaunchSpecificationsOnDemandSpecification]]], jsii.get(self, "onDemandSpecificationInput"))

    @builtins.property
    @jsii.member(jsii_name="spotSpecificationInput")
    def spot_specification_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EmrClusterCoreInstanceFleetLaunchSpecificationsSpotSpecification"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EmrClusterCoreInstanceFleetLaunchSpecificationsSpotSpecification"]]], jsii.get(self, "spotSpecificationInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[EmrClusterCoreInstanceFleetLaunchSpecifications]:
        return typing.cast(typing.Optional[EmrClusterCoreInstanceFleetLaunchSpecifications], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EmrClusterCoreInstanceFleetLaunchSpecifications],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b8449968a7651077c139e814bc5e6ac5f1a2a6274c23625959ad1195ef4986b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.emrCluster.EmrClusterCoreInstanceFleetLaunchSpecificationsSpotSpecification",
    jsii_struct_bases=[],
    name_mapping={
        "allocation_strategy": "allocationStrategy",
        "timeout_action": "timeoutAction",
        "timeout_duration_minutes": "timeoutDurationMinutes",
        "block_duration_minutes": "blockDurationMinutes",
    },
)
class EmrClusterCoreInstanceFleetLaunchSpecificationsSpotSpecification:
    def __init__(
        self,
        *,
        allocation_strategy: builtins.str,
        timeout_action: builtins.str,
        timeout_duration_minutes: jsii.Number,
        block_duration_minutes: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param allocation_strategy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#allocation_strategy EmrCluster#allocation_strategy}.
        :param timeout_action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#timeout_action EmrCluster#timeout_action}.
        :param timeout_duration_minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#timeout_duration_minutes EmrCluster#timeout_duration_minutes}.
        :param block_duration_minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#block_duration_minutes EmrCluster#block_duration_minutes}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c87529476e33a0481bef9f5fc1cf4b28a16e39f2935e81c120ca258b156c100d)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#allocation_strategy EmrCluster#allocation_strategy}.'''
        result = self._values.get("allocation_strategy")
        assert result is not None, "Required property 'allocation_strategy' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def timeout_action(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#timeout_action EmrCluster#timeout_action}.'''
        result = self._values.get("timeout_action")
        assert result is not None, "Required property 'timeout_action' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def timeout_duration_minutes(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#timeout_duration_minutes EmrCluster#timeout_duration_minutes}.'''
        result = self._values.get("timeout_duration_minutes")
        assert result is not None, "Required property 'timeout_duration_minutes' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def block_duration_minutes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#block_duration_minutes EmrCluster#block_duration_minutes}.'''
        result = self._values.get("block_duration_minutes")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmrClusterCoreInstanceFleetLaunchSpecificationsSpotSpecification(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EmrClusterCoreInstanceFleetLaunchSpecificationsSpotSpecificationList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.emrCluster.EmrClusterCoreInstanceFleetLaunchSpecificationsSpotSpecificationList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__67457fd6780e0705d9b4aa4c5a108c46e05a89b2156fb6f63889353819785b1e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EmrClusterCoreInstanceFleetLaunchSpecificationsSpotSpecificationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b3ab9a2456398bf9d32f5765addc85d48fe8dbb3815259c2bd52b231bf279e2)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EmrClusterCoreInstanceFleetLaunchSpecificationsSpotSpecificationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__51a66cf716f6e0cbbcefbccea933af420c399f8bac79717585402f9a77906ce0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__af5fb0cb5812d60f49ea4094d3916763164223890bf56703250d8fd7622c3524)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5eb7c5b9369335bfcc9026577d370a677b5961b34d357f8f7d3735df1ccc28f5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterCoreInstanceFleetLaunchSpecificationsSpotSpecification]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterCoreInstanceFleetLaunchSpecificationsSpotSpecification]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterCoreInstanceFleetLaunchSpecificationsSpotSpecification]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ef6707eca39aa0b3fd6c65e5d7839f59c7d8b42b45d966e5899b6ba04ab7f74)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EmrClusterCoreInstanceFleetLaunchSpecificationsSpotSpecificationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.emrCluster.EmrClusterCoreInstanceFleetLaunchSpecificationsSpotSpecificationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7510d5eff4eb48eb31d2cced6d41785851056be4d12a9c9fb1ef0605bd3062f2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6bd71c6138c4dfdebef1a7cf47ec05d2fa8b80a238a60d9b070d81e1e0b8a136)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allocationStrategy", value)

    @builtins.property
    @jsii.member(jsii_name="blockDurationMinutes")
    def block_duration_minutes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "blockDurationMinutes"))

    @block_duration_minutes.setter
    def block_duration_minutes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b6aaed56bc28d24a96d892363418974d695ff4f0e7b96d111d71508d19ce1d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "blockDurationMinutes", value)

    @builtins.property
    @jsii.member(jsii_name="timeoutAction")
    def timeout_action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timeoutAction"))

    @timeout_action.setter
    def timeout_action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__587777a78200dccab2a29fd0e522368efe2ad2b99bddbb1d7d44404f4bf092bf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeoutAction", value)

    @builtins.property
    @jsii.member(jsii_name="timeoutDurationMinutes")
    def timeout_duration_minutes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "timeoutDurationMinutes"))

    @timeout_duration_minutes.setter
    def timeout_duration_minutes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f0f495f7cff55c34fd12a094ee749d7809feeec72ab119da6cc10d1b612cd1d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeoutDurationMinutes", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EmrClusterCoreInstanceFleetLaunchSpecificationsSpotSpecification, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EmrClusterCoreInstanceFleetLaunchSpecificationsSpotSpecification, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EmrClusterCoreInstanceFleetLaunchSpecificationsSpotSpecification, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62afb0423afc3c3de5e0e7d6e74aca29cf79ec75af9a3612fef08752558aca5d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EmrClusterCoreInstanceFleetOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.emrCluster.EmrClusterCoreInstanceFleetOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0be4904c71099b13990146489541f865931eedc494bc744a5eb9942bb76589fe)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putInstanceTypeConfigs")
    def put_instance_type_configs(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EmrClusterCoreInstanceFleetInstanceTypeConfigs, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__668d125342b1e7f447ae046b5268510135081bc38003b314502caa44baa248f5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putInstanceTypeConfigs", [value]))

    @jsii.member(jsii_name="putLaunchSpecifications")
    def put_launch_specifications(
        self,
        *,
        on_demand_specification: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EmrClusterCoreInstanceFleetLaunchSpecificationsOnDemandSpecification, typing.Dict[builtins.str, typing.Any]]]]] = None,
        spot_specification: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EmrClusterCoreInstanceFleetLaunchSpecificationsSpotSpecification, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param on_demand_specification: on_demand_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#on_demand_specification EmrCluster#on_demand_specification}
        :param spot_specification: spot_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#spot_specification EmrCluster#spot_specification}
        '''
        value = EmrClusterCoreInstanceFleetLaunchSpecifications(
            on_demand_specification=on_demand_specification,
            spot_specification=spot_specification,
        )

        return typing.cast(None, jsii.invoke(self, "putLaunchSpecifications", [value]))

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

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="instanceTypeConfigs")
    def instance_type_configs(
        self,
    ) -> EmrClusterCoreInstanceFleetInstanceTypeConfigsList:
        return typing.cast(EmrClusterCoreInstanceFleetInstanceTypeConfigsList, jsii.get(self, "instanceTypeConfigs"))

    @builtins.property
    @jsii.member(jsii_name="launchSpecifications")
    def launch_specifications(
        self,
    ) -> EmrClusterCoreInstanceFleetLaunchSpecificationsOutputReference:
        return typing.cast(EmrClusterCoreInstanceFleetLaunchSpecificationsOutputReference, jsii.get(self, "launchSpecifications"))

    @builtins.property
    @jsii.member(jsii_name="provisionedOnDemandCapacity")
    def provisioned_on_demand_capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "provisionedOnDemandCapacity"))

    @builtins.property
    @jsii.member(jsii_name="provisionedSpotCapacity")
    def provisioned_spot_capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "provisionedSpotCapacity"))

    @builtins.property
    @jsii.member(jsii_name="instanceTypeConfigsInput")
    def instance_type_configs_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterCoreInstanceFleetInstanceTypeConfigs]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterCoreInstanceFleetInstanceTypeConfigs]]], jsii.get(self, "instanceTypeConfigsInput"))

    @builtins.property
    @jsii.member(jsii_name="launchSpecificationsInput")
    def launch_specifications_input(
        self,
    ) -> typing.Optional[EmrClusterCoreInstanceFleetLaunchSpecifications]:
        return typing.cast(typing.Optional[EmrClusterCoreInstanceFleetLaunchSpecifications], jsii.get(self, "launchSpecificationsInput"))

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
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0be01ab04b9d1456ae7858f11751838c9cdc702d84fa6b56e1045613f11b1e6a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="targetOnDemandCapacity")
    def target_on_demand_capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "targetOnDemandCapacity"))

    @target_on_demand_capacity.setter
    def target_on_demand_capacity(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49b67487b16b52c54b07d37d3ea0f352d4eed709b21714fb24aa47ddf7d47f95)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetOnDemandCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="targetSpotCapacity")
    def target_spot_capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "targetSpotCapacity"))

    @target_spot_capacity.setter
    def target_spot_capacity(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a35a5033c7ec3bd62d1b7286982ce9e287600752f80b555bdba6f01d80b4fc7b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetSpotCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[EmrClusterCoreInstanceFleet]:
        return typing.cast(typing.Optional[EmrClusterCoreInstanceFleet], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EmrClusterCoreInstanceFleet],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45d97cdbd4afd381e238bd79083167e136d23c0bef30be0c70296563de783d21)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.emrCluster.EmrClusterCoreInstanceGroup",
    jsii_struct_bases=[],
    name_mapping={
        "instance_type": "instanceType",
        "autoscaling_policy": "autoscalingPolicy",
        "bid_price": "bidPrice",
        "ebs_config": "ebsConfig",
        "instance_count": "instanceCount",
        "name": "name",
    },
)
class EmrClusterCoreInstanceGroup:
    def __init__(
        self,
        *,
        instance_type: builtins.str,
        autoscaling_policy: typing.Optional[builtins.str] = None,
        bid_price: typing.Optional[builtins.str] = None,
        ebs_config: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EmrClusterCoreInstanceGroupEbsConfig", typing.Dict[builtins.str, typing.Any]]]]] = None,
        instance_count: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param instance_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#instance_type EmrCluster#instance_type}.
        :param autoscaling_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#autoscaling_policy EmrCluster#autoscaling_policy}.
        :param bid_price: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#bid_price EmrCluster#bid_price}.
        :param ebs_config: ebs_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#ebs_config EmrCluster#ebs_config}
        :param instance_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#instance_count EmrCluster#instance_count}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#name EmrCluster#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b5e37e894931cf18337e773de08466eb3444675726e598c3a98265d6bc78f88)
            check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
            check_type(argname="argument autoscaling_policy", value=autoscaling_policy, expected_type=type_hints["autoscaling_policy"])
            check_type(argname="argument bid_price", value=bid_price, expected_type=type_hints["bid_price"])
            check_type(argname="argument ebs_config", value=ebs_config, expected_type=type_hints["ebs_config"])
            check_type(argname="argument instance_count", value=instance_count, expected_type=type_hints["instance_count"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "instance_type": instance_type,
        }
        if autoscaling_policy is not None:
            self._values["autoscaling_policy"] = autoscaling_policy
        if bid_price is not None:
            self._values["bid_price"] = bid_price
        if ebs_config is not None:
            self._values["ebs_config"] = ebs_config
        if instance_count is not None:
            self._values["instance_count"] = instance_count
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def instance_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#instance_type EmrCluster#instance_type}.'''
        result = self._values.get("instance_type")
        assert result is not None, "Required property 'instance_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def autoscaling_policy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#autoscaling_policy EmrCluster#autoscaling_policy}.'''
        result = self._values.get("autoscaling_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bid_price(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#bid_price EmrCluster#bid_price}.'''
        result = self._values.get("bid_price")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ebs_config(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EmrClusterCoreInstanceGroupEbsConfig"]]]:
        '''ebs_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#ebs_config EmrCluster#ebs_config}
        '''
        result = self._values.get("ebs_config")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EmrClusterCoreInstanceGroupEbsConfig"]]], result)

    @builtins.property
    def instance_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#instance_count EmrCluster#instance_count}.'''
        result = self._values.get("instance_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#name EmrCluster#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmrClusterCoreInstanceGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.emrCluster.EmrClusterCoreInstanceGroupEbsConfig",
    jsii_struct_bases=[],
    name_mapping={
        "size": "size",
        "type": "type",
        "iops": "iops",
        "throughput": "throughput",
        "volumes_per_instance": "volumesPerInstance",
    },
)
class EmrClusterCoreInstanceGroupEbsConfig:
    def __init__(
        self,
        *,
        size: jsii.Number,
        type: builtins.str,
        iops: typing.Optional[jsii.Number] = None,
        throughput: typing.Optional[jsii.Number] = None,
        volumes_per_instance: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#size EmrCluster#size}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#type EmrCluster#type}.
        :param iops: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#iops EmrCluster#iops}.
        :param throughput: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#throughput EmrCluster#throughput}.
        :param volumes_per_instance: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#volumes_per_instance EmrCluster#volumes_per_instance}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e9b4ebbe5e96cbd218e9c9aa34910fb6e9d2ebd2692946d68f4570054bd5081)
            check_type(argname="argument size", value=size, expected_type=type_hints["size"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument iops", value=iops, expected_type=type_hints["iops"])
            check_type(argname="argument throughput", value=throughput, expected_type=type_hints["throughput"])
            check_type(argname="argument volumes_per_instance", value=volumes_per_instance, expected_type=type_hints["volumes_per_instance"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "size": size,
            "type": type,
        }
        if iops is not None:
            self._values["iops"] = iops
        if throughput is not None:
            self._values["throughput"] = throughput
        if volumes_per_instance is not None:
            self._values["volumes_per_instance"] = volumes_per_instance

    @builtins.property
    def size(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#size EmrCluster#size}.'''
        result = self._values.get("size")
        assert result is not None, "Required property 'size' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#type EmrCluster#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def iops(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#iops EmrCluster#iops}.'''
        result = self._values.get("iops")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def throughput(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#throughput EmrCluster#throughput}.'''
        result = self._values.get("throughput")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def volumes_per_instance(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#volumes_per_instance EmrCluster#volumes_per_instance}.'''
        result = self._values.get("volumes_per_instance")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmrClusterCoreInstanceGroupEbsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EmrClusterCoreInstanceGroupEbsConfigList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.emrCluster.EmrClusterCoreInstanceGroupEbsConfigList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2db1c18673190ee44da6a64503867a557c8ce2689e776414bccc4ae6f82cf690)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EmrClusterCoreInstanceGroupEbsConfigOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__871bd41641aa0dfb2ace534d3ddf64758804d47b366761ab9cf2adb1755116f6)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EmrClusterCoreInstanceGroupEbsConfigOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8fea8ba69632b572b580895d652a25e50f4537020f7c62cf0a7661aa7c260f57)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2efcb3473ed7c9f3d2ef9a2f3ec705ddfe9a550432e1042bffb945947e905346)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0eba3a507ea317b57706d8f76514864b420379bb7e8aac5eb4e85167fae2bf00)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterCoreInstanceGroupEbsConfig]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterCoreInstanceGroupEbsConfig]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterCoreInstanceGroupEbsConfig]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8dab02188e91468a267bc54f2ca12fc7394138ff88c3bfc975b7a9aafcfb02f6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EmrClusterCoreInstanceGroupEbsConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.emrCluster.EmrClusterCoreInstanceGroupEbsConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__37492773cda16114c1927d2cd3dcb29329de7f82c5df71c955c104e7bd613bcc)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetIops")
    def reset_iops(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIops", []))

    @jsii.member(jsii_name="resetThroughput")
    def reset_throughput(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetThroughput", []))

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
    @jsii.member(jsii_name="throughputInput")
    def throughput_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "throughputInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__69ee95635f5ef73f7d69d6090245201fc1815317646a6af0d4259400980bda86)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iops", value)

    @builtins.property
    @jsii.member(jsii_name="size")
    def size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "size"))

    @size.setter
    def size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__793c8e832ff25c0cce9436a7b6b7d35c854c008b0634491e095f5972bdc6074c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "size", value)

    @builtins.property
    @jsii.member(jsii_name="throughput")
    def throughput(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "throughput"))

    @throughput.setter
    def throughput(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eda1919e81d8688fddfe92063d97f5d56066d1c348aff200a2cab767c3bfe97c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "throughput", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09081b4930f1da7e1e542b30e21660698ec9206cbba20340c55f038a813261c0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="volumesPerInstance")
    def volumes_per_instance(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "volumesPerInstance"))

    @volumes_per_instance.setter
    def volumes_per_instance(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5adf807fab68dd64c2de4ec54ca72113d5a8abe24a10c08f0b07b3b3a4b4a093)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumesPerInstance", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EmrClusterCoreInstanceGroupEbsConfig, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EmrClusterCoreInstanceGroupEbsConfig, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EmrClusterCoreInstanceGroupEbsConfig, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60cce777c5ce246a191f5c2c9c6ed5d9b32b584456a275a333a61e75f5cd5d6a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EmrClusterCoreInstanceGroupOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.emrCluster.EmrClusterCoreInstanceGroupOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__783eb64cc7f13374825fd5bea5267893549559d8f73fd2f5c96e4d983e40334e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putEbsConfig")
    def put_ebs_config(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EmrClusterCoreInstanceGroupEbsConfig, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__172b16e0dd911fb0e725bc4abc4590a0bce83e0a7b2664917cbfbcf3bec17863)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putEbsConfig", [value]))

    @jsii.member(jsii_name="resetAutoscalingPolicy")
    def reset_autoscaling_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoscalingPolicy", []))

    @jsii.member(jsii_name="resetBidPrice")
    def reset_bid_price(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBidPrice", []))

    @jsii.member(jsii_name="resetEbsConfig")
    def reset_ebs_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEbsConfig", []))

    @jsii.member(jsii_name="resetInstanceCount")
    def reset_instance_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceCount", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @builtins.property
    @jsii.member(jsii_name="ebsConfig")
    def ebs_config(self) -> EmrClusterCoreInstanceGroupEbsConfigList:
        return typing.cast(EmrClusterCoreInstanceGroupEbsConfigList, jsii.get(self, "ebsConfig"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="autoscalingPolicyInput")
    def autoscaling_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "autoscalingPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="bidPriceInput")
    def bid_price_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bidPriceInput"))

    @builtins.property
    @jsii.member(jsii_name="ebsConfigInput")
    def ebs_config_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterCoreInstanceGroupEbsConfig]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterCoreInstanceGroupEbsConfig]]], jsii.get(self, "ebsConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceCountInput")
    def instance_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "instanceCountInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceTypeInput")
    def instance_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="autoscalingPolicy")
    def autoscaling_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "autoscalingPolicy"))

    @autoscaling_policy.setter
    def autoscaling_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87cb4a75a378fa78b6e992b138ab894bc1251a628e5f83d81bd894e19b955c21)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoscalingPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="bidPrice")
    def bid_price(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bidPrice"))

    @bid_price.setter
    def bid_price(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ddea35efc158764592764123754e34e7819adc5f2a093ea7acaf557559a7c2e5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bidPrice", value)

    @builtins.property
    @jsii.member(jsii_name="instanceCount")
    def instance_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "instanceCount"))

    @instance_count.setter
    def instance_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ea598f486ed32854e79aa5b4517bedd4d850e22f034a7338426e7a9fd76db8c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceCount", value)

    @builtins.property
    @jsii.member(jsii_name="instanceType")
    def instance_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceType"))

    @instance_type.setter
    def instance_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f1242513934cb2003422a870293af36374798374ad80f657f9d8772fad5fcfc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceType", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__466be93c1b0464f017fa39c782bbb26b2f9cdafb86ac43ae98fa0232aefe6e3a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[EmrClusterCoreInstanceGroup]:
        return typing.cast(typing.Optional[EmrClusterCoreInstanceGroup], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EmrClusterCoreInstanceGroup],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e53e23e15057a0c953b715fd14c3cc920daa7e2f3e557c57de5a930fc974ea91)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.emrCluster.EmrClusterEc2Attributes",
    jsii_struct_bases=[],
    name_mapping={
        "instance_profile": "instanceProfile",
        "additional_master_security_groups": "additionalMasterSecurityGroups",
        "additional_slave_security_groups": "additionalSlaveSecurityGroups",
        "emr_managed_master_security_group": "emrManagedMasterSecurityGroup",
        "emr_managed_slave_security_group": "emrManagedSlaveSecurityGroup",
        "key_name": "keyName",
        "service_access_security_group": "serviceAccessSecurityGroup",
        "subnet_id": "subnetId",
        "subnet_ids": "subnetIds",
    },
)
class EmrClusterEc2Attributes:
    def __init__(
        self,
        *,
        instance_profile: builtins.str,
        additional_master_security_groups: typing.Optional[builtins.str] = None,
        additional_slave_security_groups: typing.Optional[builtins.str] = None,
        emr_managed_master_security_group: typing.Optional[builtins.str] = None,
        emr_managed_slave_security_group: typing.Optional[builtins.str] = None,
        key_name: typing.Optional[builtins.str] = None,
        service_access_security_group: typing.Optional[builtins.str] = None,
        subnet_id: typing.Optional[builtins.str] = None,
        subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param instance_profile: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#instance_profile EmrCluster#instance_profile}.
        :param additional_master_security_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#additional_master_security_groups EmrCluster#additional_master_security_groups}.
        :param additional_slave_security_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#additional_slave_security_groups EmrCluster#additional_slave_security_groups}.
        :param emr_managed_master_security_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#emr_managed_master_security_group EmrCluster#emr_managed_master_security_group}.
        :param emr_managed_slave_security_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#emr_managed_slave_security_group EmrCluster#emr_managed_slave_security_group}.
        :param key_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#key_name EmrCluster#key_name}.
        :param service_access_security_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#service_access_security_group EmrCluster#service_access_security_group}.
        :param subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#subnet_id EmrCluster#subnet_id}.
        :param subnet_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#subnet_ids EmrCluster#subnet_ids}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c714a1d96045fde09de957dbc43c1eb332a588732bcf1e96e81056135e493ee0)
            check_type(argname="argument instance_profile", value=instance_profile, expected_type=type_hints["instance_profile"])
            check_type(argname="argument additional_master_security_groups", value=additional_master_security_groups, expected_type=type_hints["additional_master_security_groups"])
            check_type(argname="argument additional_slave_security_groups", value=additional_slave_security_groups, expected_type=type_hints["additional_slave_security_groups"])
            check_type(argname="argument emr_managed_master_security_group", value=emr_managed_master_security_group, expected_type=type_hints["emr_managed_master_security_group"])
            check_type(argname="argument emr_managed_slave_security_group", value=emr_managed_slave_security_group, expected_type=type_hints["emr_managed_slave_security_group"])
            check_type(argname="argument key_name", value=key_name, expected_type=type_hints["key_name"])
            check_type(argname="argument service_access_security_group", value=service_access_security_group, expected_type=type_hints["service_access_security_group"])
            check_type(argname="argument subnet_id", value=subnet_id, expected_type=type_hints["subnet_id"])
            check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "instance_profile": instance_profile,
        }
        if additional_master_security_groups is not None:
            self._values["additional_master_security_groups"] = additional_master_security_groups
        if additional_slave_security_groups is not None:
            self._values["additional_slave_security_groups"] = additional_slave_security_groups
        if emr_managed_master_security_group is not None:
            self._values["emr_managed_master_security_group"] = emr_managed_master_security_group
        if emr_managed_slave_security_group is not None:
            self._values["emr_managed_slave_security_group"] = emr_managed_slave_security_group
        if key_name is not None:
            self._values["key_name"] = key_name
        if service_access_security_group is not None:
            self._values["service_access_security_group"] = service_access_security_group
        if subnet_id is not None:
            self._values["subnet_id"] = subnet_id
        if subnet_ids is not None:
            self._values["subnet_ids"] = subnet_ids

    @builtins.property
    def instance_profile(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#instance_profile EmrCluster#instance_profile}.'''
        result = self._values.get("instance_profile")
        assert result is not None, "Required property 'instance_profile' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def additional_master_security_groups(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#additional_master_security_groups EmrCluster#additional_master_security_groups}.'''
        result = self._values.get("additional_master_security_groups")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def additional_slave_security_groups(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#additional_slave_security_groups EmrCluster#additional_slave_security_groups}.'''
        result = self._values.get("additional_slave_security_groups")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def emr_managed_master_security_group(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#emr_managed_master_security_group EmrCluster#emr_managed_master_security_group}.'''
        result = self._values.get("emr_managed_master_security_group")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def emr_managed_slave_security_group(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#emr_managed_slave_security_group EmrCluster#emr_managed_slave_security_group}.'''
        result = self._values.get("emr_managed_slave_security_group")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#key_name EmrCluster#key_name}.'''
        result = self._values.get("key_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service_access_security_group(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#service_access_security_group EmrCluster#service_access_security_group}.'''
        result = self._values.get("service_access_security_group")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subnet_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#subnet_id EmrCluster#subnet_id}.'''
        result = self._values.get("subnet_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#subnet_ids EmrCluster#subnet_ids}.'''
        result = self._values.get("subnet_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmrClusterEc2Attributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EmrClusterEc2AttributesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.emrCluster.EmrClusterEc2AttributesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__589486f98e545a53e230510e19f8017f7db1a6f5e70d3d5faa97e39b8260fa60)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAdditionalMasterSecurityGroups")
    def reset_additional_master_security_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdditionalMasterSecurityGroups", []))

    @jsii.member(jsii_name="resetAdditionalSlaveSecurityGroups")
    def reset_additional_slave_security_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdditionalSlaveSecurityGroups", []))

    @jsii.member(jsii_name="resetEmrManagedMasterSecurityGroup")
    def reset_emr_managed_master_security_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmrManagedMasterSecurityGroup", []))

    @jsii.member(jsii_name="resetEmrManagedSlaveSecurityGroup")
    def reset_emr_managed_slave_security_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmrManagedSlaveSecurityGroup", []))

    @jsii.member(jsii_name="resetKeyName")
    def reset_key_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyName", []))

    @jsii.member(jsii_name="resetServiceAccessSecurityGroup")
    def reset_service_access_security_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceAccessSecurityGroup", []))

    @jsii.member(jsii_name="resetSubnetId")
    def reset_subnet_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubnetId", []))

    @jsii.member(jsii_name="resetSubnetIds")
    def reset_subnet_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubnetIds", []))

    @builtins.property
    @jsii.member(jsii_name="additionalMasterSecurityGroupsInput")
    def additional_master_security_groups_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "additionalMasterSecurityGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="additionalSlaveSecurityGroupsInput")
    def additional_slave_security_groups_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "additionalSlaveSecurityGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="emrManagedMasterSecurityGroupInput")
    def emr_managed_master_security_group_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "emrManagedMasterSecurityGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="emrManagedSlaveSecurityGroupInput")
    def emr_managed_slave_security_group_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "emrManagedSlaveSecurityGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceProfileInput")
    def instance_profile_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceProfileInput"))

    @builtins.property
    @jsii.member(jsii_name="keyNameInput")
    def key_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyNameInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceAccessSecurityGroupInput")
    def service_access_security_group_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceAccessSecurityGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetIdInput")
    def subnet_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subnetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetIdsInput")
    def subnet_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "subnetIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="additionalMasterSecurityGroups")
    def additional_master_security_groups(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "additionalMasterSecurityGroups"))

    @additional_master_security_groups.setter
    def additional_master_security_groups(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35131523c00b78a6e299d17791e6e718a0a8ff7fbe95bfa52ccc711621eaac0e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "additionalMasterSecurityGroups", value)

    @builtins.property
    @jsii.member(jsii_name="additionalSlaveSecurityGroups")
    def additional_slave_security_groups(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "additionalSlaveSecurityGroups"))

    @additional_slave_security_groups.setter
    def additional_slave_security_groups(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b0a2a4bd312c8e33ca3821fff1421857df834e4f164e2e9969b545a3e712074)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "additionalSlaveSecurityGroups", value)

    @builtins.property
    @jsii.member(jsii_name="emrManagedMasterSecurityGroup")
    def emr_managed_master_security_group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "emrManagedMasterSecurityGroup"))

    @emr_managed_master_security_group.setter
    def emr_managed_master_security_group(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c00065462362bfc885e942f67ffcb9d37ac1aa814b21d69bc88b90b7e081dee6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "emrManagedMasterSecurityGroup", value)

    @builtins.property
    @jsii.member(jsii_name="emrManagedSlaveSecurityGroup")
    def emr_managed_slave_security_group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "emrManagedSlaveSecurityGroup"))

    @emr_managed_slave_security_group.setter
    def emr_managed_slave_security_group(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af4c4fa18e32bc3f82c3d61e40f36d773cd363a8a03ab258c57e9a622ad580b7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "emrManagedSlaveSecurityGroup", value)

    @builtins.property
    @jsii.member(jsii_name="instanceProfile")
    def instance_profile(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceProfile"))

    @instance_profile.setter
    def instance_profile(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__603c7adec7fd4785c5318212a99d05c5e742d5474a065a8c2378d39b04bacd64)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceProfile", value)

    @builtins.property
    @jsii.member(jsii_name="keyName")
    def key_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyName"))

    @key_name.setter
    def key_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c9d12148b78702687b240d0b7b49a1ae8588dc15018ded1f3660b40b32212250)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyName", value)

    @builtins.property
    @jsii.member(jsii_name="serviceAccessSecurityGroup")
    def service_access_security_group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceAccessSecurityGroup"))

    @service_access_security_group.setter
    def service_access_security_group(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff9d248133a6ab6612bc91445f051696b86e677539b686e997ee242e089d75cc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceAccessSecurityGroup", value)

    @builtins.property
    @jsii.member(jsii_name="subnetId")
    def subnet_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subnetId"))

    @subnet_id.setter
    def subnet_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__154a0d958a4ba371a85ee9267dd37d3548008294ef38b4e973222e62d29ecd6f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetId", value)

    @builtins.property
    @jsii.member(jsii_name="subnetIds")
    def subnet_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subnetIds"))

    @subnet_ids.setter
    def subnet_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__806f5263dad650365dd30c8a007542321c11749ec8aeb70168ba0d5d44dfd9d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetIds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[EmrClusterEc2Attributes]:
        return typing.cast(typing.Optional[EmrClusterEc2Attributes], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[EmrClusterEc2Attributes]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__941009b14ba6af6df6bbd51ddb4ca0a409e77ac1c197cbaf352fbf33cee425ba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.emrCluster.EmrClusterKerberosAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "kdc_admin_password": "kdcAdminPassword",
        "realm": "realm",
        "ad_domain_join_password": "adDomainJoinPassword",
        "ad_domain_join_user": "adDomainJoinUser",
        "cross_realm_trust_principal_password": "crossRealmTrustPrincipalPassword",
    },
)
class EmrClusterKerberosAttributes:
    def __init__(
        self,
        *,
        kdc_admin_password: builtins.str,
        realm: builtins.str,
        ad_domain_join_password: typing.Optional[builtins.str] = None,
        ad_domain_join_user: typing.Optional[builtins.str] = None,
        cross_realm_trust_principal_password: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param kdc_admin_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#kdc_admin_password EmrCluster#kdc_admin_password}.
        :param realm: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#realm EmrCluster#realm}.
        :param ad_domain_join_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#ad_domain_join_password EmrCluster#ad_domain_join_password}.
        :param ad_domain_join_user: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#ad_domain_join_user EmrCluster#ad_domain_join_user}.
        :param cross_realm_trust_principal_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#cross_realm_trust_principal_password EmrCluster#cross_realm_trust_principal_password}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c4a64b4c24c141525a777ea68288caf2ebc343c2ce8a4553d26a614a6349306)
            check_type(argname="argument kdc_admin_password", value=kdc_admin_password, expected_type=type_hints["kdc_admin_password"])
            check_type(argname="argument realm", value=realm, expected_type=type_hints["realm"])
            check_type(argname="argument ad_domain_join_password", value=ad_domain_join_password, expected_type=type_hints["ad_domain_join_password"])
            check_type(argname="argument ad_domain_join_user", value=ad_domain_join_user, expected_type=type_hints["ad_domain_join_user"])
            check_type(argname="argument cross_realm_trust_principal_password", value=cross_realm_trust_principal_password, expected_type=type_hints["cross_realm_trust_principal_password"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "kdc_admin_password": kdc_admin_password,
            "realm": realm,
        }
        if ad_domain_join_password is not None:
            self._values["ad_domain_join_password"] = ad_domain_join_password
        if ad_domain_join_user is not None:
            self._values["ad_domain_join_user"] = ad_domain_join_user
        if cross_realm_trust_principal_password is not None:
            self._values["cross_realm_trust_principal_password"] = cross_realm_trust_principal_password

    @builtins.property
    def kdc_admin_password(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#kdc_admin_password EmrCluster#kdc_admin_password}.'''
        result = self._values.get("kdc_admin_password")
        assert result is not None, "Required property 'kdc_admin_password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def realm(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#realm EmrCluster#realm}.'''
        result = self._values.get("realm")
        assert result is not None, "Required property 'realm' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ad_domain_join_password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#ad_domain_join_password EmrCluster#ad_domain_join_password}.'''
        result = self._values.get("ad_domain_join_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ad_domain_join_user(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#ad_domain_join_user EmrCluster#ad_domain_join_user}.'''
        result = self._values.get("ad_domain_join_user")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cross_realm_trust_principal_password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#cross_realm_trust_principal_password EmrCluster#cross_realm_trust_principal_password}.'''
        result = self._values.get("cross_realm_trust_principal_password")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmrClusterKerberosAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EmrClusterKerberosAttributesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.emrCluster.EmrClusterKerberosAttributesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b7a2463b71bb99a3582994b6b296830575ab54897c18425df563baf5c4d5297f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAdDomainJoinPassword")
    def reset_ad_domain_join_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdDomainJoinPassword", []))

    @jsii.member(jsii_name="resetAdDomainJoinUser")
    def reset_ad_domain_join_user(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdDomainJoinUser", []))

    @jsii.member(jsii_name="resetCrossRealmTrustPrincipalPassword")
    def reset_cross_realm_trust_principal_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCrossRealmTrustPrincipalPassword", []))

    @builtins.property
    @jsii.member(jsii_name="adDomainJoinPasswordInput")
    def ad_domain_join_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "adDomainJoinPasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="adDomainJoinUserInput")
    def ad_domain_join_user_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "adDomainJoinUserInput"))

    @builtins.property
    @jsii.member(jsii_name="crossRealmTrustPrincipalPasswordInput")
    def cross_realm_trust_principal_password_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "crossRealmTrustPrincipalPasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="kdcAdminPasswordInput")
    def kdc_admin_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kdcAdminPasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="realmInput")
    def realm_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "realmInput"))

    @builtins.property
    @jsii.member(jsii_name="adDomainJoinPassword")
    def ad_domain_join_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "adDomainJoinPassword"))

    @ad_domain_join_password.setter
    def ad_domain_join_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7878fbb6e2057732c204bdf907aa31deb644aa739985f68f2013ebfa7f8c9912)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adDomainJoinPassword", value)

    @builtins.property
    @jsii.member(jsii_name="adDomainJoinUser")
    def ad_domain_join_user(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "adDomainJoinUser"))

    @ad_domain_join_user.setter
    def ad_domain_join_user(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b88657ad7d5b006d927723eafe768ed25c09de18c2caaa23d10bc9bfbf818536)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adDomainJoinUser", value)

    @builtins.property
    @jsii.member(jsii_name="crossRealmTrustPrincipalPassword")
    def cross_realm_trust_principal_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "crossRealmTrustPrincipalPassword"))

    @cross_realm_trust_principal_password.setter
    def cross_realm_trust_principal_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e547854a5afa281e3e80501ce80fc885261fd89e0ca242702f29a5a4a54b28ad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "crossRealmTrustPrincipalPassword", value)

    @builtins.property
    @jsii.member(jsii_name="kdcAdminPassword")
    def kdc_admin_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kdcAdminPassword"))

    @kdc_admin_password.setter
    def kdc_admin_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa47730885f968697b281f3ef5277c076c79ace9e8cd82f2fc19e7e0fd10abb4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kdcAdminPassword", value)

    @builtins.property
    @jsii.member(jsii_name="realm")
    def realm(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "realm"))

    @realm.setter
    def realm(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a0f65a49525883eb615d11bcde336c7c5d027adfc3994eb37d84da60599e857)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "realm", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[EmrClusterKerberosAttributes]:
        return typing.cast(typing.Optional[EmrClusterKerberosAttributes], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EmrClusterKerberosAttributes],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2dd0597847185099feec5ddf3dae03dc7da00385cfec266f746ab09fcc3a6209)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.emrCluster.EmrClusterMasterInstanceFleet",
    jsii_struct_bases=[],
    name_mapping={
        "instance_type_configs": "instanceTypeConfigs",
        "launch_specifications": "launchSpecifications",
        "name": "name",
        "target_on_demand_capacity": "targetOnDemandCapacity",
        "target_spot_capacity": "targetSpotCapacity",
    },
)
class EmrClusterMasterInstanceFleet:
    def __init__(
        self,
        *,
        instance_type_configs: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EmrClusterMasterInstanceFleetInstanceTypeConfigs", typing.Dict[builtins.str, typing.Any]]]]] = None,
        launch_specifications: typing.Optional[typing.Union["EmrClusterMasterInstanceFleetLaunchSpecifications", typing.Dict[builtins.str, typing.Any]]] = None,
        name: typing.Optional[builtins.str] = None,
        target_on_demand_capacity: typing.Optional[jsii.Number] = None,
        target_spot_capacity: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param instance_type_configs: instance_type_configs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#instance_type_configs EmrCluster#instance_type_configs}
        :param launch_specifications: launch_specifications block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#launch_specifications EmrCluster#launch_specifications}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#name EmrCluster#name}.
        :param target_on_demand_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#target_on_demand_capacity EmrCluster#target_on_demand_capacity}.
        :param target_spot_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#target_spot_capacity EmrCluster#target_spot_capacity}.
        '''
        if isinstance(launch_specifications, dict):
            launch_specifications = EmrClusterMasterInstanceFleetLaunchSpecifications(**launch_specifications)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1790a99ce31cdf8fd668f1dea8a46766192cda8f1192f6acebe40e99a1e4c66e)
            check_type(argname="argument instance_type_configs", value=instance_type_configs, expected_type=type_hints["instance_type_configs"])
            check_type(argname="argument launch_specifications", value=launch_specifications, expected_type=type_hints["launch_specifications"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument target_on_demand_capacity", value=target_on_demand_capacity, expected_type=type_hints["target_on_demand_capacity"])
            check_type(argname="argument target_spot_capacity", value=target_spot_capacity, expected_type=type_hints["target_spot_capacity"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
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
    def instance_type_configs(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EmrClusterMasterInstanceFleetInstanceTypeConfigs"]]]:
        '''instance_type_configs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#instance_type_configs EmrCluster#instance_type_configs}
        '''
        result = self._values.get("instance_type_configs")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EmrClusterMasterInstanceFleetInstanceTypeConfigs"]]], result)

    @builtins.property
    def launch_specifications(
        self,
    ) -> typing.Optional["EmrClusterMasterInstanceFleetLaunchSpecifications"]:
        '''launch_specifications block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#launch_specifications EmrCluster#launch_specifications}
        '''
        result = self._values.get("launch_specifications")
        return typing.cast(typing.Optional["EmrClusterMasterInstanceFleetLaunchSpecifications"], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#name EmrCluster#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_on_demand_capacity(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#target_on_demand_capacity EmrCluster#target_on_demand_capacity}.'''
        result = self._values.get("target_on_demand_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def target_spot_capacity(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#target_spot_capacity EmrCluster#target_spot_capacity}.'''
        result = self._values.get("target_spot_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmrClusterMasterInstanceFleet(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.emrCluster.EmrClusterMasterInstanceFleetInstanceTypeConfigs",
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
class EmrClusterMasterInstanceFleetInstanceTypeConfigs:
    def __init__(
        self,
        *,
        instance_type: builtins.str,
        bid_price: typing.Optional[builtins.str] = None,
        bid_price_as_percentage_of_on_demand_price: typing.Optional[jsii.Number] = None,
        configurations: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EmrClusterMasterInstanceFleetInstanceTypeConfigsConfigurations", typing.Dict[builtins.str, typing.Any]]]]] = None,
        ebs_config: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EmrClusterMasterInstanceFleetInstanceTypeConfigsEbsConfig", typing.Dict[builtins.str, typing.Any]]]]] = None,
        weighted_capacity: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param instance_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#instance_type EmrCluster#instance_type}.
        :param bid_price: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#bid_price EmrCluster#bid_price}.
        :param bid_price_as_percentage_of_on_demand_price: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#bid_price_as_percentage_of_on_demand_price EmrCluster#bid_price_as_percentage_of_on_demand_price}.
        :param configurations: configurations block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#configurations EmrCluster#configurations}
        :param ebs_config: ebs_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#ebs_config EmrCluster#ebs_config}
        :param weighted_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#weighted_capacity EmrCluster#weighted_capacity}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__825da669fcd287ead738f04513a2bb1df8a957f326f38f6019370a3897d66b92)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#instance_type EmrCluster#instance_type}.'''
        result = self._values.get("instance_type")
        assert result is not None, "Required property 'instance_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bid_price(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#bid_price EmrCluster#bid_price}.'''
        result = self._values.get("bid_price")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bid_price_as_percentage_of_on_demand_price(
        self,
    ) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#bid_price_as_percentage_of_on_demand_price EmrCluster#bid_price_as_percentage_of_on_demand_price}.'''
        result = self._values.get("bid_price_as_percentage_of_on_demand_price")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def configurations(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EmrClusterMasterInstanceFleetInstanceTypeConfigsConfigurations"]]]:
        '''configurations block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#configurations EmrCluster#configurations}
        '''
        result = self._values.get("configurations")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EmrClusterMasterInstanceFleetInstanceTypeConfigsConfigurations"]]], result)

    @builtins.property
    def ebs_config(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EmrClusterMasterInstanceFleetInstanceTypeConfigsEbsConfig"]]]:
        '''ebs_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#ebs_config EmrCluster#ebs_config}
        '''
        result = self._values.get("ebs_config")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EmrClusterMasterInstanceFleetInstanceTypeConfigsEbsConfig"]]], result)

    @builtins.property
    def weighted_capacity(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#weighted_capacity EmrCluster#weighted_capacity}.'''
        result = self._values.get("weighted_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmrClusterMasterInstanceFleetInstanceTypeConfigs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.emrCluster.EmrClusterMasterInstanceFleetInstanceTypeConfigsConfigurations",
    jsii_struct_bases=[],
    name_mapping={"classification": "classification", "properties": "properties"},
)
class EmrClusterMasterInstanceFleetInstanceTypeConfigsConfigurations:
    def __init__(
        self,
        *,
        classification: typing.Optional[builtins.str] = None,
        properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param classification: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#classification EmrCluster#classification}.
        :param properties: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#properties EmrCluster#properties}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d94859863cef2afd6c70c73d3cd2e52bb1130eb37e7fb8a22134daa3a45344bb)
            check_type(argname="argument classification", value=classification, expected_type=type_hints["classification"])
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if classification is not None:
            self._values["classification"] = classification
        if properties is not None:
            self._values["properties"] = properties

    @builtins.property
    def classification(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#classification EmrCluster#classification}.'''
        result = self._values.get("classification")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def properties(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#properties EmrCluster#properties}.'''
        result = self._values.get("properties")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmrClusterMasterInstanceFleetInstanceTypeConfigsConfigurations(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EmrClusterMasterInstanceFleetInstanceTypeConfigsConfigurationsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.emrCluster.EmrClusterMasterInstanceFleetInstanceTypeConfigsConfigurationsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__26a2ce27f94fb0cee470f091e45ab59813d19d64096d31a645c39d99f11a3c5d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EmrClusterMasterInstanceFleetInstanceTypeConfigsConfigurationsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ebc5f8bc91f9494787f6127cb770cdcea83536c9c3da00906d10ec1ae4007c8)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EmrClusterMasterInstanceFleetInstanceTypeConfigsConfigurationsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0bd095d3378d71865bad547a23f396efbdfae2da6be6dc54a4a4c0f5f0661c7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e27ba71480cb1b6c81fc4a7248d4fbdbc271b95d74809bc1ba375ad6f5bd7361)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b7d8a485de4104aa24d199bcaf44d83ca162df1cbf0a20f4690befa6ac80bbe2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterMasterInstanceFleetInstanceTypeConfigsConfigurations]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterMasterInstanceFleetInstanceTypeConfigsConfigurations]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterMasterInstanceFleetInstanceTypeConfigsConfigurations]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bcf9fed9d23448b98b759d9fe0447e335d6d54f4b85b1b4f0c06285f3dc676c7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EmrClusterMasterInstanceFleetInstanceTypeConfigsConfigurationsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.emrCluster.EmrClusterMasterInstanceFleetInstanceTypeConfigsConfigurationsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__919bacbe29a5e1d4e684be74264c76530ca51b592b373af4dfa64350ea23c05e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__499f926244d9d11c372383e67217d69a3320d1b46332aed9e200e777f507376a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "classification", value)

    @builtins.property
    @jsii.member(jsii_name="properties")
    def properties(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "properties"))

    @properties.setter
    def properties(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__51528b808136500772908bb9d1231bc0bb1524b098bdd3c9482ceb0364b76d0b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "properties", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EmrClusterMasterInstanceFleetInstanceTypeConfigsConfigurations, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EmrClusterMasterInstanceFleetInstanceTypeConfigsConfigurations, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EmrClusterMasterInstanceFleetInstanceTypeConfigsConfigurations, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4de8cd1de0c270bc507a9e99961e20af977549b2dc78845c82636529ba9916cb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.emrCluster.EmrClusterMasterInstanceFleetInstanceTypeConfigsEbsConfig",
    jsii_struct_bases=[],
    name_mapping={
        "size": "size",
        "type": "type",
        "iops": "iops",
        "volumes_per_instance": "volumesPerInstance",
    },
)
class EmrClusterMasterInstanceFleetInstanceTypeConfigsEbsConfig:
    def __init__(
        self,
        *,
        size: jsii.Number,
        type: builtins.str,
        iops: typing.Optional[jsii.Number] = None,
        volumes_per_instance: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#size EmrCluster#size}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#type EmrCluster#type}.
        :param iops: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#iops EmrCluster#iops}.
        :param volumes_per_instance: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#volumes_per_instance EmrCluster#volumes_per_instance}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f34a09b20451391499d716f9f34863d74b8a3813d88265b0417338e92b7c7dec)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#size EmrCluster#size}.'''
        result = self._values.get("size")
        assert result is not None, "Required property 'size' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#type EmrCluster#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def iops(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#iops EmrCluster#iops}.'''
        result = self._values.get("iops")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def volumes_per_instance(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#volumes_per_instance EmrCluster#volumes_per_instance}.'''
        result = self._values.get("volumes_per_instance")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmrClusterMasterInstanceFleetInstanceTypeConfigsEbsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EmrClusterMasterInstanceFleetInstanceTypeConfigsEbsConfigList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.emrCluster.EmrClusterMasterInstanceFleetInstanceTypeConfigsEbsConfigList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3162a7b295f458e6344daa17129265a4ee10bbc6d808fe4a513338d342cdd78f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EmrClusterMasterInstanceFleetInstanceTypeConfigsEbsConfigOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bdff6a35f33b72787bddc11a5bf08754004d8b7812997f6e044ceeb30e2c83a7)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EmrClusterMasterInstanceFleetInstanceTypeConfigsEbsConfigOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__913e81fede2d4f09de7dcddbe27ebd43e7844582cc22446ab1b1ae94ea71f591)
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
            type_hints = typing.get_type_hints(_typecheckingstub__bce074c3e6c744ecf9bd23a2344888f2e070bf14c449649f6e58d023bdabd0ae)
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
            type_hints = typing.get_type_hints(_typecheckingstub__98eec36e57e16dcf78d29d24bf6e416b5f50e1f1def714af696bddcfb3857e33)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterMasterInstanceFleetInstanceTypeConfigsEbsConfig]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterMasterInstanceFleetInstanceTypeConfigsEbsConfig]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterMasterInstanceFleetInstanceTypeConfigsEbsConfig]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__203258d89e7837e217c0d535b27cc562cccd492bcb68b17f29eec4d3c448ccdc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EmrClusterMasterInstanceFleetInstanceTypeConfigsEbsConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.emrCluster.EmrClusterMasterInstanceFleetInstanceTypeConfigsEbsConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2622d52e30d7452ab103e94ec34a2017747871182b6fcee87422cc9fe4c7433e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1b0a1d0b2ab0ad58d4fddf41aa0dcd3f897c1fa8dbc362486b98175af48ff71a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iops", value)

    @builtins.property
    @jsii.member(jsii_name="size")
    def size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "size"))

    @size.setter
    def size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f0a524d45c0a6bf9220b079bbeb083677d7eda321a60f560ffd1ca929fe77107)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "size", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75eb42cf09a4e56c9ff148a4d85f5b33e94e15e1409dd868b7a03c161aaf2b3b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="volumesPerInstance")
    def volumes_per_instance(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "volumesPerInstance"))

    @volumes_per_instance.setter
    def volumes_per_instance(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8df6ec79fa23aa962c9d94d393cced94ee803da703e0a58f33c1e0eae0e8c918)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumesPerInstance", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EmrClusterMasterInstanceFleetInstanceTypeConfigsEbsConfig, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EmrClusterMasterInstanceFleetInstanceTypeConfigsEbsConfig, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EmrClusterMasterInstanceFleetInstanceTypeConfigsEbsConfig, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2186dd206fd139218d786b443b921cbe13dd45166cc9b7430883f3d6ea6b4b9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EmrClusterMasterInstanceFleetInstanceTypeConfigsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.emrCluster.EmrClusterMasterInstanceFleetInstanceTypeConfigsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__03cc9bd11ea3a4b38aab663c24a0c92ea71fe447073bcc1da19e52e967523507)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EmrClusterMasterInstanceFleetInstanceTypeConfigsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c7038b903117d77f719ee6aa20f5d6ba447cae4b94b5549aa4fd348ea197042)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EmrClusterMasterInstanceFleetInstanceTypeConfigsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fee8ddd79b130078c3f5929d40ae98d153f5b1b7ae621f7febead8dc86c17279)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e96ede4e70e0b1fdba40c7ae7b0f082fd5ccf13d63c2d8502e30b65535c00307)
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
            type_hints = typing.get_type_hints(_typecheckingstub__93a664d6c8a86c5a908e9417e49d008a02a49ce473f1b66ed8775c4387970b23)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterMasterInstanceFleetInstanceTypeConfigs]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterMasterInstanceFleetInstanceTypeConfigs]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterMasterInstanceFleetInstanceTypeConfigs]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb4fb98cfebaafcb8d3cc4d53f28449c6a1365e536ddb183b6a7aafc4b6f53e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EmrClusterMasterInstanceFleetInstanceTypeConfigsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.emrCluster.EmrClusterMasterInstanceFleetInstanceTypeConfigsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ad2cbeadfd51876c0420f10695540c4bb9ca0c3e81ba2da9259cce2aa58badb1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putConfigurations")
    def put_configurations(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EmrClusterMasterInstanceFleetInstanceTypeConfigsConfigurations, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f98938e118434104a9a205ace0c111ebfe1e294f97112d15d72b7e6a640838c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putConfigurations", [value]))

    @jsii.member(jsii_name="putEbsConfig")
    def put_ebs_config(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EmrClusterMasterInstanceFleetInstanceTypeConfigsEbsConfig, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26bece380cf2e7c3a88fd9107003fb2f3a52395b1873c49ce78d5d8fd09d2c55)
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
    def configurations(
        self,
    ) -> EmrClusterMasterInstanceFleetInstanceTypeConfigsConfigurationsList:
        return typing.cast(EmrClusterMasterInstanceFleetInstanceTypeConfigsConfigurationsList, jsii.get(self, "configurations"))

    @builtins.property
    @jsii.member(jsii_name="ebsConfig")
    def ebs_config(
        self,
    ) -> EmrClusterMasterInstanceFleetInstanceTypeConfigsEbsConfigList:
        return typing.cast(EmrClusterMasterInstanceFleetInstanceTypeConfigsEbsConfigList, jsii.get(self, "ebsConfig"))

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
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterMasterInstanceFleetInstanceTypeConfigsConfigurations]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterMasterInstanceFleetInstanceTypeConfigsConfigurations]]], jsii.get(self, "configurationsInput"))

    @builtins.property
    @jsii.member(jsii_name="ebsConfigInput")
    def ebs_config_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterMasterInstanceFleetInstanceTypeConfigsEbsConfig]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterMasterInstanceFleetInstanceTypeConfigsEbsConfig]]], jsii.get(self, "ebsConfigInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__f2f174490b9eb3b79d6d80416e644c16cc7d246ac2c46e030f2db3c7e7940503)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bidPrice", value)

    @builtins.property
    @jsii.member(jsii_name="bidPriceAsPercentageOfOnDemandPrice")
    def bid_price_as_percentage_of_on_demand_price(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "bidPriceAsPercentageOfOnDemandPrice"))

    @bid_price_as_percentage_of_on_demand_price.setter
    def bid_price_as_percentage_of_on_demand_price(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__207c5e500fc1e4d2c75ea4102da9569aeec607cd72c82bb48289aecc0f5a5f06)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bidPriceAsPercentageOfOnDemandPrice", value)

    @builtins.property
    @jsii.member(jsii_name="instanceType")
    def instance_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceType"))

    @instance_type.setter
    def instance_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__88c4f1ea2f6bdae8cfab92d2679b9b55a5e648eac94b782f19b7f06ec6bd81af)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceType", value)

    @builtins.property
    @jsii.member(jsii_name="weightedCapacity")
    def weighted_capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "weightedCapacity"))

    @weighted_capacity.setter
    def weighted_capacity(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05e24754e9bc19004b7d6d23a6ddcb25d1ccf4df7239834cf2846ab4b3131d78)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "weightedCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EmrClusterMasterInstanceFleetInstanceTypeConfigs, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EmrClusterMasterInstanceFleetInstanceTypeConfigs, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EmrClusterMasterInstanceFleetInstanceTypeConfigs, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d0fae32d76322690a0e4c3f1e07fcfe5f9e62feefc01b966e1d274f2f6de834)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.emrCluster.EmrClusterMasterInstanceFleetLaunchSpecifications",
    jsii_struct_bases=[],
    name_mapping={
        "on_demand_specification": "onDemandSpecification",
        "spot_specification": "spotSpecification",
    },
)
class EmrClusterMasterInstanceFleetLaunchSpecifications:
    def __init__(
        self,
        *,
        on_demand_specification: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EmrClusterMasterInstanceFleetLaunchSpecificationsOnDemandSpecification", typing.Dict[builtins.str, typing.Any]]]]] = None,
        spot_specification: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EmrClusterMasterInstanceFleetLaunchSpecificationsSpotSpecification", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param on_demand_specification: on_demand_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#on_demand_specification EmrCluster#on_demand_specification}
        :param spot_specification: spot_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#spot_specification EmrCluster#spot_specification}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dcca71c5c9ecbdbeed25b12e928347f4662a30879d7ebd04a5f3b8d966d239b5)
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
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EmrClusterMasterInstanceFleetLaunchSpecificationsOnDemandSpecification"]]]:
        '''on_demand_specification block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#on_demand_specification EmrCluster#on_demand_specification}
        '''
        result = self._values.get("on_demand_specification")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EmrClusterMasterInstanceFleetLaunchSpecificationsOnDemandSpecification"]]], result)

    @builtins.property
    def spot_specification(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EmrClusterMasterInstanceFleetLaunchSpecificationsSpotSpecification"]]]:
        '''spot_specification block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#spot_specification EmrCluster#spot_specification}
        '''
        result = self._values.get("spot_specification")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EmrClusterMasterInstanceFleetLaunchSpecificationsSpotSpecification"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmrClusterMasterInstanceFleetLaunchSpecifications(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.emrCluster.EmrClusterMasterInstanceFleetLaunchSpecificationsOnDemandSpecification",
    jsii_struct_bases=[],
    name_mapping={"allocation_strategy": "allocationStrategy"},
)
class EmrClusterMasterInstanceFleetLaunchSpecificationsOnDemandSpecification:
    def __init__(self, *, allocation_strategy: builtins.str) -> None:
        '''
        :param allocation_strategy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#allocation_strategy EmrCluster#allocation_strategy}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9fe57d31acc35eea0fb4ec15f98a2e0061c14627d2220ce6e5b6e4c0e9db3b6)
            check_type(argname="argument allocation_strategy", value=allocation_strategy, expected_type=type_hints["allocation_strategy"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "allocation_strategy": allocation_strategy,
        }

    @builtins.property
    def allocation_strategy(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#allocation_strategy EmrCluster#allocation_strategy}.'''
        result = self._values.get("allocation_strategy")
        assert result is not None, "Required property 'allocation_strategy' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmrClusterMasterInstanceFleetLaunchSpecificationsOnDemandSpecification(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EmrClusterMasterInstanceFleetLaunchSpecificationsOnDemandSpecificationList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.emrCluster.EmrClusterMasterInstanceFleetLaunchSpecificationsOnDemandSpecificationList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a336c352691190d3e938a4acac4c11275285db51907c4c86770b5cb45bb0f3f7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EmrClusterMasterInstanceFleetLaunchSpecificationsOnDemandSpecificationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__83a524100a49705053f310064cb849da2cd257c9accd7c9d9c557de3c73ec70b)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EmrClusterMasterInstanceFleetLaunchSpecificationsOnDemandSpecificationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45ca8effbe073c99ddf82fa12dec1b8180018dd4d217f0ec5c7d40523e13b6f1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__750ab82cbc71742d6ae00cc63028f55b4cbe2758d3f80ef06fdf6c62adf151bc)
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
            type_hints = typing.get_type_hints(_typecheckingstub__477f9c9317e63f497ab9c42a984591c8e66eb10347d18eaba9e364d0f1aded22)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterMasterInstanceFleetLaunchSpecificationsOnDemandSpecification]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterMasterInstanceFleetLaunchSpecificationsOnDemandSpecification]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterMasterInstanceFleetLaunchSpecificationsOnDemandSpecification]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__287480b6589487d7d3586db110075498d963dc3245a52cdc3ebbe0cf3e3d2da2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EmrClusterMasterInstanceFleetLaunchSpecificationsOnDemandSpecificationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.emrCluster.EmrClusterMasterInstanceFleetLaunchSpecificationsOnDemandSpecificationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5fadec13ddea0bbedfef4fc617f6cbcb1a1ac028f9dae6a85c76dcee6d2a8144)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ff8f9d997d04969454a8d40380b090c45ebe60c852ab36cb9a1317cfbff51e4e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allocationStrategy", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EmrClusterMasterInstanceFleetLaunchSpecificationsOnDemandSpecification, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EmrClusterMasterInstanceFleetLaunchSpecificationsOnDemandSpecification, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EmrClusterMasterInstanceFleetLaunchSpecificationsOnDemandSpecification, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__266abf712fc7546f2a7285a382fe08f18b01b97b7a6686de7b8ffed0adb3094d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EmrClusterMasterInstanceFleetLaunchSpecificationsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.emrCluster.EmrClusterMasterInstanceFleetLaunchSpecificationsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__433bf52d79be47ea07e00a55dcf53c651c051b6fa3b229c259a25f5998dbee49)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putOnDemandSpecification")
    def put_on_demand_specification(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EmrClusterMasterInstanceFleetLaunchSpecificationsOnDemandSpecification, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c591114075e122e7f941e5cfc0d4c8f570c1b276f16b349d85c96a769de23dda)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putOnDemandSpecification", [value]))

    @jsii.member(jsii_name="putSpotSpecification")
    def put_spot_specification(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EmrClusterMasterInstanceFleetLaunchSpecificationsSpotSpecification", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1b64377d237c146149d7cfcba130bf945a49894aa92cafe00fc531620aa8ad7)
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
    ) -> EmrClusterMasterInstanceFleetLaunchSpecificationsOnDemandSpecificationList:
        return typing.cast(EmrClusterMasterInstanceFleetLaunchSpecificationsOnDemandSpecificationList, jsii.get(self, "onDemandSpecification"))

    @builtins.property
    @jsii.member(jsii_name="spotSpecification")
    def spot_specification(
        self,
    ) -> "EmrClusterMasterInstanceFleetLaunchSpecificationsSpotSpecificationList":
        return typing.cast("EmrClusterMasterInstanceFleetLaunchSpecificationsSpotSpecificationList", jsii.get(self, "spotSpecification"))

    @builtins.property
    @jsii.member(jsii_name="onDemandSpecificationInput")
    def on_demand_specification_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterMasterInstanceFleetLaunchSpecificationsOnDemandSpecification]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterMasterInstanceFleetLaunchSpecificationsOnDemandSpecification]]], jsii.get(self, "onDemandSpecificationInput"))

    @builtins.property
    @jsii.member(jsii_name="spotSpecificationInput")
    def spot_specification_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EmrClusterMasterInstanceFleetLaunchSpecificationsSpotSpecification"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EmrClusterMasterInstanceFleetLaunchSpecificationsSpotSpecification"]]], jsii.get(self, "spotSpecificationInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[EmrClusterMasterInstanceFleetLaunchSpecifications]:
        return typing.cast(typing.Optional[EmrClusterMasterInstanceFleetLaunchSpecifications], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EmrClusterMasterInstanceFleetLaunchSpecifications],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3c7f8c181ef3cdefd91ba7e5601354e0c722449c010829540178be64b1809d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.emrCluster.EmrClusterMasterInstanceFleetLaunchSpecificationsSpotSpecification",
    jsii_struct_bases=[],
    name_mapping={
        "allocation_strategy": "allocationStrategy",
        "timeout_action": "timeoutAction",
        "timeout_duration_minutes": "timeoutDurationMinutes",
        "block_duration_minutes": "blockDurationMinutes",
    },
)
class EmrClusterMasterInstanceFleetLaunchSpecificationsSpotSpecification:
    def __init__(
        self,
        *,
        allocation_strategy: builtins.str,
        timeout_action: builtins.str,
        timeout_duration_minutes: jsii.Number,
        block_duration_minutes: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param allocation_strategy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#allocation_strategy EmrCluster#allocation_strategy}.
        :param timeout_action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#timeout_action EmrCluster#timeout_action}.
        :param timeout_duration_minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#timeout_duration_minutes EmrCluster#timeout_duration_minutes}.
        :param block_duration_minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#block_duration_minutes EmrCluster#block_duration_minutes}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ea4fa0ee87959293213ea000e1136f350ce2c83f15ad8941de45d0668f33d34)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#allocation_strategy EmrCluster#allocation_strategy}.'''
        result = self._values.get("allocation_strategy")
        assert result is not None, "Required property 'allocation_strategy' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def timeout_action(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#timeout_action EmrCluster#timeout_action}.'''
        result = self._values.get("timeout_action")
        assert result is not None, "Required property 'timeout_action' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def timeout_duration_minutes(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#timeout_duration_minutes EmrCluster#timeout_duration_minutes}.'''
        result = self._values.get("timeout_duration_minutes")
        assert result is not None, "Required property 'timeout_duration_minutes' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def block_duration_minutes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#block_duration_minutes EmrCluster#block_duration_minutes}.'''
        result = self._values.get("block_duration_minutes")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmrClusterMasterInstanceFleetLaunchSpecificationsSpotSpecification(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EmrClusterMasterInstanceFleetLaunchSpecificationsSpotSpecificationList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.emrCluster.EmrClusterMasterInstanceFleetLaunchSpecificationsSpotSpecificationList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c56b548cd432e142ece643c949f308dea8fdbd6308f89b8e41770153516126f4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EmrClusterMasterInstanceFleetLaunchSpecificationsSpotSpecificationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__443c0f11db0a2841236da754ddfef9e79a3b34155fc66210ed3f303ef3cc8a26)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EmrClusterMasterInstanceFleetLaunchSpecificationsSpotSpecificationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__208da9334de51a8bab6347e16904083fc0dcf830bbff34090b5392534c37718d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0d96cf8c9d878a0449c4e362ac73623439cbe12040fdeec953f9b4d137173cdf)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7241aeab5c4f669d15b885e3345f16db0988ab34385d5c7256de328de813266c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterMasterInstanceFleetLaunchSpecificationsSpotSpecification]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterMasterInstanceFleetLaunchSpecificationsSpotSpecification]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterMasterInstanceFleetLaunchSpecificationsSpotSpecification]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ebdc419611d36c51214f0853e4a2df5515a28bed72985f874ad7ea6f5bd6bd0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EmrClusterMasterInstanceFleetLaunchSpecificationsSpotSpecificationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.emrCluster.EmrClusterMasterInstanceFleetLaunchSpecificationsSpotSpecificationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d78edb9807653d2af06ff97e1ae7852566ce0fddbda2612504ae14f98058df24)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2ec528411788fc1cbf157d2a89d8c8983719a93bb8b91447dbf46e25a3299797)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allocationStrategy", value)

    @builtins.property
    @jsii.member(jsii_name="blockDurationMinutes")
    def block_duration_minutes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "blockDurationMinutes"))

    @block_duration_minutes.setter
    def block_duration_minutes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68f876e1f7f07f720ef584354375c7e77ecd9a896a8916de637dddb49c2c9e70)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "blockDurationMinutes", value)

    @builtins.property
    @jsii.member(jsii_name="timeoutAction")
    def timeout_action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timeoutAction"))

    @timeout_action.setter
    def timeout_action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__847f78bb65d6cf8e9fa9e2fb2a089adfcd18f4ce433569483311e5701ea8f35b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeoutAction", value)

    @builtins.property
    @jsii.member(jsii_name="timeoutDurationMinutes")
    def timeout_duration_minutes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "timeoutDurationMinutes"))

    @timeout_duration_minutes.setter
    def timeout_duration_minutes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77b4311b883f239a52972024a1c5776249cc0d4acdafcf5262c824b4e552a6d6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeoutDurationMinutes", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EmrClusterMasterInstanceFleetLaunchSpecificationsSpotSpecification, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EmrClusterMasterInstanceFleetLaunchSpecificationsSpotSpecification, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EmrClusterMasterInstanceFleetLaunchSpecificationsSpotSpecification, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c720af5f15aadefafafb5f1feb11a0ad79bce966297b78956347f25e2266944d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EmrClusterMasterInstanceFleetOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.emrCluster.EmrClusterMasterInstanceFleetOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4f190b9a11bf189aa18ff4fb94c9ce343461aba2886ba11582b137cfe749b800)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putInstanceTypeConfigs")
    def put_instance_type_configs(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EmrClusterMasterInstanceFleetInstanceTypeConfigs, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ae839171324b3b41d8a9cce486be64874f83c7eb56477175c83c0f47162db8e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putInstanceTypeConfigs", [value]))

    @jsii.member(jsii_name="putLaunchSpecifications")
    def put_launch_specifications(
        self,
        *,
        on_demand_specification: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EmrClusterMasterInstanceFleetLaunchSpecificationsOnDemandSpecification, typing.Dict[builtins.str, typing.Any]]]]] = None,
        spot_specification: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EmrClusterMasterInstanceFleetLaunchSpecificationsSpotSpecification, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param on_demand_specification: on_demand_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#on_demand_specification EmrCluster#on_demand_specification}
        :param spot_specification: spot_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#spot_specification EmrCluster#spot_specification}
        '''
        value = EmrClusterMasterInstanceFleetLaunchSpecifications(
            on_demand_specification=on_demand_specification,
            spot_specification=spot_specification,
        )

        return typing.cast(None, jsii.invoke(self, "putLaunchSpecifications", [value]))

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

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="instanceTypeConfigs")
    def instance_type_configs(
        self,
    ) -> EmrClusterMasterInstanceFleetInstanceTypeConfigsList:
        return typing.cast(EmrClusterMasterInstanceFleetInstanceTypeConfigsList, jsii.get(self, "instanceTypeConfigs"))

    @builtins.property
    @jsii.member(jsii_name="launchSpecifications")
    def launch_specifications(
        self,
    ) -> EmrClusterMasterInstanceFleetLaunchSpecificationsOutputReference:
        return typing.cast(EmrClusterMasterInstanceFleetLaunchSpecificationsOutputReference, jsii.get(self, "launchSpecifications"))

    @builtins.property
    @jsii.member(jsii_name="provisionedOnDemandCapacity")
    def provisioned_on_demand_capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "provisionedOnDemandCapacity"))

    @builtins.property
    @jsii.member(jsii_name="provisionedSpotCapacity")
    def provisioned_spot_capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "provisionedSpotCapacity"))

    @builtins.property
    @jsii.member(jsii_name="instanceTypeConfigsInput")
    def instance_type_configs_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterMasterInstanceFleetInstanceTypeConfigs]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterMasterInstanceFleetInstanceTypeConfigs]]], jsii.get(self, "instanceTypeConfigsInput"))

    @builtins.property
    @jsii.member(jsii_name="launchSpecificationsInput")
    def launch_specifications_input(
        self,
    ) -> typing.Optional[EmrClusterMasterInstanceFleetLaunchSpecifications]:
        return typing.cast(typing.Optional[EmrClusterMasterInstanceFleetLaunchSpecifications], jsii.get(self, "launchSpecificationsInput"))

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
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__add177c1f3f5651a57847c9625b6a052ab43697d9b2302b043d7fcb0feffd237)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="targetOnDemandCapacity")
    def target_on_demand_capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "targetOnDemandCapacity"))

    @target_on_demand_capacity.setter
    def target_on_demand_capacity(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c46fa63349d8920e3f844b7bb94de1804f2964cd05a4067264ca025bfa218d17)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetOnDemandCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="targetSpotCapacity")
    def target_spot_capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "targetSpotCapacity"))

    @target_spot_capacity.setter
    def target_spot_capacity(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__495b8858b3f980dc938a0a3c553f4b206a090837803d627f8239b668284e1842)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetSpotCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[EmrClusterMasterInstanceFleet]:
        return typing.cast(typing.Optional[EmrClusterMasterInstanceFleet], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EmrClusterMasterInstanceFleet],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__481eebdafcc093e7683abaff47ff9ab98a437f3911b5e2a17999656137da812a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.emrCluster.EmrClusterMasterInstanceGroup",
    jsii_struct_bases=[],
    name_mapping={
        "instance_type": "instanceType",
        "bid_price": "bidPrice",
        "ebs_config": "ebsConfig",
        "instance_count": "instanceCount",
        "name": "name",
    },
)
class EmrClusterMasterInstanceGroup:
    def __init__(
        self,
        *,
        instance_type: builtins.str,
        bid_price: typing.Optional[builtins.str] = None,
        ebs_config: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EmrClusterMasterInstanceGroupEbsConfig", typing.Dict[builtins.str, typing.Any]]]]] = None,
        instance_count: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param instance_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#instance_type EmrCluster#instance_type}.
        :param bid_price: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#bid_price EmrCluster#bid_price}.
        :param ebs_config: ebs_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#ebs_config EmrCluster#ebs_config}
        :param instance_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#instance_count EmrCluster#instance_count}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#name EmrCluster#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__48a338805c18799177c2f8263901816811b02aecad3a48f073eeb820e794923d)
            check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
            check_type(argname="argument bid_price", value=bid_price, expected_type=type_hints["bid_price"])
            check_type(argname="argument ebs_config", value=ebs_config, expected_type=type_hints["ebs_config"])
            check_type(argname="argument instance_count", value=instance_count, expected_type=type_hints["instance_count"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "instance_type": instance_type,
        }
        if bid_price is not None:
            self._values["bid_price"] = bid_price
        if ebs_config is not None:
            self._values["ebs_config"] = ebs_config
        if instance_count is not None:
            self._values["instance_count"] = instance_count
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def instance_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#instance_type EmrCluster#instance_type}.'''
        result = self._values.get("instance_type")
        assert result is not None, "Required property 'instance_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bid_price(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#bid_price EmrCluster#bid_price}.'''
        result = self._values.get("bid_price")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ebs_config(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EmrClusterMasterInstanceGroupEbsConfig"]]]:
        '''ebs_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#ebs_config EmrCluster#ebs_config}
        '''
        result = self._values.get("ebs_config")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EmrClusterMasterInstanceGroupEbsConfig"]]], result)

    @builtins.property
    def instance_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#instance_count EmrCluster#instance_count}.'''
        result = self._values.get("instance_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#name EmrCluster#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmrClusterMasterInstanceGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.emrCluster.EmrClusterMasterInstanceGroupEbsConfig",
    jsii_struct_bases=[],
    name_mapping={
        "size": "size",
        "type": "type",
        "iops": "iops",
        "throughput": "throughput",
        "volumes_per_instance": "volumesPerInstance",
    },
)
class EmrClusterMasterInstanceGroupEbsConfig:
    def __init__(
        self,
        *,
        size: jsii.Number,
        type: builtins.str,
        iops: typing.Optional[jsii.Number] = None,
        throughput: typing.Optional[jsii.Number] = None,
        volumes_per_instance: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#size EmrCluster#size}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#type EmrCluster#type}.
        :param iops: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#iops EmrCluster#iops}.
        :param throughput: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#throughput EmrCluster#throughput}.
        :param volumes_per_instance: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#volumes_per_instance EmrCluster#volumes_per_instance}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__251342fdb6ad1b68c27fc86c03d0ae3e58a334962c520984f253e7a08f72cb56)
            check_type(argname="argument size", value=size, expected_type=type_hints["size"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument iops", value=iops, expected_type=type_hints["iops"])
            check_type(argname="argument throughput", value=throughput, expected_type=type_hints["throughput"])
            check_type(argname="argument volumes_per_instance", value=volumes_per_instance, expected_type=type_hints["volumes_per_instance"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "size": size,
            "type": type,
        }
        if iops is not None:
            self._values["iops"] = iops
        if throughput is not None:
            self._values["throughput"] = throughput
        if volumes_per_instance is not None:
            self._values["volumes_per_instance"] = volumes_per_instance

    @builtins.property
    def size(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#size EmrCluster#size}.'''
        result = self._values.get("size")
        assert result is not None, "Required property 'size' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#type EmrCluster#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def iops(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#iops EmrCluster#iops}.'''
        result = self._values.get("iops")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def throughput(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#throughput EmrCluster#throughput}.'''
        result = self._values.get("throughput")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def volumes_per_instance(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#volumes_per_instance EmrCluster#volumes_per_instance}.'''
        result = self._values.get("volumes_per_instance")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmrClusterMasterInstanceGroupEbsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EmrClusterMasterInstanceGroupEbsConfigList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.emrCluster.EmrClusterMasterInstanceGroupEbsConfigList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cb9e6ba005de8796ac794292d8d6d66cbebbdc1f95bf12db4d2c183863730bf6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EmrClusterMasterInstanceGroupEbsConfigOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eda630a0bac158903bb26248b0fef030ba8676aa6662df62f300bc47308a7908)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EmrClusterMasterInstanceGroupEbsConfigOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40ffe6ad87cde8cbd7400d595d4dbf627e442e17bea217e31ab6d116c4e57c74)
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
            type_hints = typing.get_type_hints(_typecheckingstub__042efbc2848794584a8d96adf5659cf2cfc782e023a0396abfb427acb45d0388)
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
            type_hints = typing.get_type_hints(_typecheckingstub__398233e80c94396e7aee46ffa0ef34a7fe5bb8502b67793d961cf08520a77e82)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterMasterInstanceGroupEbsConfig]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterMasterInstanceGroupEbsConfig]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterMasterInstanceGroupEbsConfig]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58d40f8a393d51a1f36b5ca378cea00e4411dedb05fc5bd25a4a509f38ac2a32)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EmrClusterMasterInstanceGroupEbsConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.emrCluster.EmrClusterMasterInstanceGroupEbsConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d19282512b4f200c1491b0cf57db1ef7f5ce25c7e8872d7f63a41b7987b4e86d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetIops")
    def reset_iops(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIops", []))

    @jsii.member(jsii_name="resetThroughput")
    def reset_throughput(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetThroughput", []))

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
    @jsii.member(jsii_name="throughputInput")
    def throughput_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "throughputInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__462c62ff7429f995a08f89d6ab3fedc6ac54fb5cc1f0e516f769a034b74d8002)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iops", value)

    @builtins.property
    @jsii.member(jsii_name="size")
    def size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "size"))

    @size.setter
    def size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a485a0bb70bb07bc95463834f86101261d11de2d5526153dd130d7e6712a436b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "size", value)

    @builtins.property
    @jsii.member(jsii_name="throughput")
    def throughput(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "throughput"))

    @throughput.setter
    def throughput(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e9bd0efca8afe0d5535f6472843622ea4e18941bc19968187574f9e6689ed3b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "throughput", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef7775b6a3a53820a7ed6597dd53c29071276de81c5a051fff6d00955bcef7a9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="volumesPerInstance")
    def volumes_per_instance(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "volumesPerInstance"))

    @volumes_per_instance.setter
    def volumes_per_instance(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c27a2f79c18b2db146319480f9fbb7b0e8b894d6b74bed17c2ea9bff289fd221)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumesPerInstance", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EmrClusterMasterInstanceGroupEbsConfig, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EmrClusterMasterInstanceGroupEbsConfig, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EmrClusterMasterInstanceGroupEbsConfig, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1ed7c824c77c6944211fa8b7177b0d764548f20665aa4290f69f0826dc3596e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EmrClusterMasterInstanceGroupOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.emrCluster.EmrClusterMasterInstanceGroupOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__00a70e55f332612c847b65864528fd60a94940c0aec59ba3cef6d3d0bfe60e16)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putEbsConfig")
    def put_ebs_config(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EmrClusterMasterInstanceGroupEbsConfig, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0624268d40d9ae7c0c5d15913a40cb8c38ae4222bbbecdff4231a7640f717c29)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putEbsConfig", [value]))

    @jsii.member(jsii_name="resetBidPrice")
    def reset_bid_price(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBidPrice", []))

    @jsii.member(jsii_name="resetEbsConfig")
    def reset_ebs_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEbsConfig", []))

    @jsii.member(jsii_name="resetInstanceCount")
    def reset_instance_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceCount", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @builtins.property
    @jsii.member(jsii_name="ebsConfig")
    def ebs_config(self) -> EmrClusterMasterInstanceGroupEbsConfigList:
        return typing.cast(EmrClusterMasterInstanceGroupEbsConfigList, jsii.get(self, "ebsConfig"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="bidPriceInput")
    def bid_price_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bidPriceInput"))

    @builtins.property
    @jsii.member(jsii_name="ebsConfigInput")
    def ebs_config_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterMasterInstanceGroupEbsConfig]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterMasterInstanceGroupEbsConfig]]], jsii.get(self, "ebsConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceCountInput")
    def instance_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "instanceCountInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceTypeInput")
    def instance_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="bidPrice")
    def bid_price(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bidPrice"))

    @bid_price.setter
    def bid_price(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b9bc6ee2d4f2a9ab58b82ba4a57cf6b7b67b1ebbfc397fcd12395b660baa13fb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bidPrice", value)

    @builtins.property
    @jsii.member(jsii_name="instanceCount")
    def instance_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "instanceCount"))

    @instance_count.setter
    def instance_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__48920a169e5df260b1401262b57bc21f95fd29595af59461fdc780ce4e856907)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceCount", value)

    @builtins.property
    @jsii.member(jsii_name="instanceType")
    def instance_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceType"))

    @instance_type.setter
    def instance_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a70242e130f36f9949da9c3c8c18db08a7563cef07e15a9e85d4fd1482d04130)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceType", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b15e6146975cc86ac205cd95487322ec6fe57a21f880b07dac7c26cfc350a9dd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[EmrClusterMasterInstanceGroup]:
        return typing.cast(typing.Optional[EmrClusterMasterInstanceGroup], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EmrClusterMasterInstanceGroup],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b7b583aea0a71ee07d98fa21517e297634f20e3f2ca8319069f74818a4c9131)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.emrCluster.EmrClusterStep",
    jsii_struct_bases=[],
    name_mapping={
        "action_on_failure": "actionOnFailure",
        "hadoop_jar_step": "hadoopJarStep",
        "name": "name",
    },
)
class EmrClusterStep:
    def __init__(
        self,
        *,
        action_on_failure: typing.Optional[builtins.str] = None,
        hadoop_jar_step: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EmrClusterStepHadoopJarStep", typing.Dict[builtins.str, typing.Any]]]]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param action_on_failure: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#action_on_failure EmrCluster#action_on_failure}.
        :param hadoop_jar_step: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#hadoop_jar_step EmrCluster#hadoop_jar_step}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#name EmrCluster#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__595ac141d9ce989f273d94077a483e7f1dc6af0a756b2df97aa8a43cc7f5a084)
            check_type(argname="argument action_on_failure", value=action_on_failure, expected_type=type_hints["action_on_failure"])
            check_type(argname="argument hadoop_jar_step", value=hadoop_jar_step, expected_type=type_hints["hadoop_jar_step"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if action_on_failure is not None:
            self._values["action_on_failure"] = action_on_failure
        if hadoop_jar_step is not None:
            self._values["hadoop_jar_step"] = hadoop_jar_step
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def action_on_failure(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#action_on_failure EmrCluster#action_on_failure}.'''
        result = self._values.get("action_on_failure")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def hadoop_jar_step(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EmrClusterStepHadoopJarStep"]]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#hadoop_jar_step EmrCluster#hadoop_jar_step}.'''
        result = self._values.get("hadoop_jar_step")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EmrClusterStepHadoopJarStep"]]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#name EmrCluster#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmrClusterStep(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.emrCluster.EmrClusterStepHadoopJarStep",
    jsii_struct_bases=[],
    name_mapping={
        "args": "args",
        "jar": "jar",
        "main_class": "mainClass",
        "properties": "properties",
    },
)
class EmrClusterStepHadoopJarStep:
    def __init__(
        self,
        *,
        args: typing.Optional[typing.Sequence[builtins.str]] = None,
        jar: typing.Optional[builtins.str] = None,
        main_class: typing.Optional[builtins.str] = None,
        properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param args: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#args EmrCluster#args}.
        :param jar: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#jar EmrCluster#jar}.
        :param main_class: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#main_class EmrCluster#main_class}.
        :param properties: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#properties EmrCluster#properties}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6be43cee477e6a633659509196237210e9b963db1fe853c9f6ca655d30ac95f7)
            check_type(argname="argument args", value=args, expected_type=type_hints["args"])
            check_type(argname="argument jar", value=jar, expected_type=type_hints["jar"])
            check_type(argname="argument main_class", value=main_class, expected_type=type_hints["main_class"])
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if args is not None:
            self._values["args"] = args
        if jar is not None:
            self._values["jar"] = jar
        if main_class is not None:
            self._values["main_class"] = main_class
        if properties is not None:
            self._values["properties"] = properties

    @builtins.property
    def args(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#args EmrCluster#args}.'''
        result = self._values.get("args")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def jar(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#jar EmrCluster#jar}.'''
        result = self._values.get("jar")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def main_class(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#main_class EmrCluster#main_class}.'''
        result = self._values.get("main_class")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def properties(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#properties EmrCluster#properties}.'''
        result = self._values.get("properties")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmrClusterStepHadoopJarStep(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EmrClusterStepHadoopJarStepList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.emrCluster.EmrClusterStepHadoopJarStepList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__320e3b3f595e110971c96833ee1f397f316b7f1538652d61fb712674a7994439)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "EmrClusterStepHadoopJarStepOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3bf40705c43be7aac869f343976301dfec5c2b41600e90b301f1ca5b0a6b3f2)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EmrClusterStepHadoopJarStepOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01a1969f7d94c5742ac674243b9d55115cfc9162ad985b1791ba2b9bb2c57ab6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9dd6d3dbd29bbaa3e51304684938e2cddaa408bd87ef34e11177a7e78e2129cc)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c1861f729c429d2989acf544a354c5e77db5f68847fb3ecd5e8daa5ee8eda825)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterStepHadoopJarStep]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterStepHadoopJarStep]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterStepHadoopJarStep]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__262e3a798af3eb11f1a97e8039fbbc7bbc7c88424cb246b2bbc2874468179f9e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EmrClusterStepHadoopJarStepOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.emrCluster.EmrClusterStepHadoopJarStepOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__594dca53128ada41f5ffb0b2dbd5b5f6885fee77e7e67e38f0ca040f3a10eed9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetArgs")
    def reset_args(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetArgs", []))

    @jsii.member(jsii_name="resetJar")
    def reset_jar(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJar", []))

    @jsii.member(jsii_name="resetMainClass")
    def reset_main_class(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMainClass", []))

    @jsii.member(jsii_name="resetProperties")
    def reset_properties(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProperties", []))

    @builtins.property
    @jsii.member(jsii_name="argsInput")
    def args_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "argsInput"))

    @builtins.property
    @jsii.member(jsii_name="jarInput")
    def jar_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "jarInput"))

    @builtins.property
    @jsii.member(jsii_name="mainClassInput")
    def main_class_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mainClassInput"))

    @builtins.property
    @jsii.member(jsii_name="propertiesInput")
    def properties_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "propertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="args")
    def args(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "args"))

    @args.setter
    def args(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__28b6964c2fe11e90739c9c4ec3241721f0f7f92b6b5059dc8af0d448de34ee0f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "args", value)

    @builtins.property
    @jsii.member(jsii_name="jar")
    def jar(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "jar"))

    @jar.setter
    def jar(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__801c148beda5d5c7389664b2fed1d02226132bb0c466a236febad7a6cce76f28)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jar", value)

    @builtins.property
    @jsii.member(jsii_name="mainClass")
    def main_class(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mainClass"))

    @main_class.setter
    def main_class(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7eecfae2ed2c2534b92cc00d882de126df2a7bc35627617face054cf4d54f8ad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mainClass", value)

    @builtins.property
    @jsii.member(jsii_name="properties")
    def properties(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "properties"))

    @properties.setter
    def properties(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__027d1b266ab8ce4b9d897f8a62a78adaad5f05e0ecfa5f8f72a2b97e3efadb0a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "properties", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EmrClusterStepHadoopJarStep, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EmrClusterStepHadoopJarStep, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EmrClusterStepHadoopJarStep, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58831eb703d1527f0dc49bfccc65c5773e7ffe14e05ac7b8bb6b4fd760113d80)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EmrClusterStepList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.emrCluster.EmrClusterStepList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e5042f2b18dff3332848d0fdbfdced25878f76d0a9f80a95e1cdf248405699ab)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "EmrClusterStepOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aeaecc585fe3236b2bdaef711600388f3760620aa4508294d31cc486c2b379a6)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EmrClusterStepOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb60a3ff5da358404c845b47d7fd04cbc0669740727526af865db6ac3b6fa272)
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
            type_hints = typing.get_type_hints(_typecheckingstub__98bf5a535538b0ada9884b20366439e8e185ce2024e9b15d170866cbe139905a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__44b11d694c8b714ae40ef471b7ce7c9b1e3d7cfd3e77cba38b9a05eda517a73c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterStep]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterStep]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterStep]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f602ac2805dfb4ac9246f826ebcb8df4478e049de5abda1f6196fe2985a59be7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EmrClusterStepOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.emrCluster.EmrClusterStepOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__896eb17e42db7fad186ce80fb16a6f78791f7eda159aa82947e865efa3149bad)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putHadoopJarStep")
    def put_hadoop_jar_step(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EmrClusterStepHadoopJarStep, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05bd32ba8b4903bc046f43aff00841e38dd47dd59b5807c15b3026d896fc12a4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putHadoopJarStep", [value]))

    @jsii.member(jsii_name="resetActionOnFailure")
    def reset_action_on_failure(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetActionOnFailure", []))

    @jsii.member(jsii_name="resetHadoopJarStep")
    def reset_hadoop_jar_step(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHadoopJarStep", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @builtins.property
    @jsii.member(jsii_name="hadoopJarStep")
    def hadoop_jar_step(self) -> EmrClusterStepHadoopJarStepList:
        return typing.cast(EmrClusterStepHadoopJarStepList, jsii.get(self, "hadoopJarStep"))

    @builtins.property
    @jsii.member(jsii_name="actionOnFailureInput")
    def action_on_failure_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionOnFailureInput"))

    @builtins.property
    @jsii.member(jsii_name="hadoopJarStepInput")
    def hadoop_jar_step_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterStepHadoopJarStep]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterStepHadoopJarStep]]], jsii.get(self, "hadoopJarStepInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="actionOnFailure")
    def action_on_failure(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "actionOnFailure"))

    @action_on_failure.setter
    def action_on_failure(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af6644a8db874dc3de8d7a27a839d3813adf95a3119e82c7cf6b95e433069f83)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "actionOnFailure", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ebe1677597af760a911ad6d8c36ab139375d4f5ebd39116a12eaf85b803c61f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EmrClusterStep, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EmrClusterStep, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EmrClusterStep, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64e58d28d7b606fa6d450dafdf43f087c5d6667b2f1b6951a6df9f3f29f229d8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "EmrCluster",
    "EmrClusterAutoTerminationPolicy",
    "EmrClusterAutoTerminationPolicyOutputReference",
    "EmrClusterBootstrapAction",
    "EmrClusterBootstrapActionList",
    "EmrClusterBootstrapActionOutputReference",
    "EmrClusterConfig",
    "EmrClusterCoreInstanceFleet",
    "EmrClusterCoreInstanceFleetInstanceTypeConfigs",
    "EmrClusterCoreInstanceFleetInstanceTypeConfigsConfigurations",
    "EmrClusterCoreInstanceFleetInstanceTypeConfigsConfigurationsList",
    "EmrClusterCoreInstanceFleetInstanceTypeConfigsConfigurationsOutputReference",
    "EmrClusterCoreInstanceFleetInstanceTypeConfigsEbsConfig",
    "EmrClusterCoreInstanceFleetInstanceTypeConfigsEbsConfigList",
    "EmrClusterCoreInstanceFleetInstanceTypeConfigsEbsConfigOutputReference",
    "EmrClusterCoreInstanceFleetInstanceTypeConfigsList",
    "EmrClusterCoreInstanceFleetInstanceTypeConfigsOutputReference",
    "EmrClusterCoreInstanceFleetLaunchSpecifications",
    "EmrClusterCoreInstanceFleetLaunchSpecificationsOnDemandSpecification",
    "EmrClusterCoreInstanceFleetLaunchSpecificationsOnDemandSpecificationList",
    "EmrClusterCoreInstanceFleetLaunchSpecificationsOnDemandSpecificationOutputReference",
    "EmrClusterCoreInstanceFleetLaunchSpecificationsOutputReference",
    "EmrClusterCoreInstanceFleetLaunchSpecificationsSpotSpecification",
    "EmrClusterCoreInstanceFleetLaunchSpecificationsSpotSpecificationList",
    "EmrClusterCoreInstanceFleetLaunchSpecificationsSpotSpecificationOutputReference",
    "EmrClusterCoreInstanceFleetOutputReference",
    "EmrClusterCoreInstanceGroup",
    "EmrClusterCoreInstanceGroupEbsConfig",
    "EmrClusterCoreInstanceGroupEbsConfigList",
    "EmrClusterCoreInstanceGroupEbsConfigOutputReference",
    "EmrClusterCoreInstanceGroupOutputReference",
    "EmrClusterEc2Attributes",
    "EmrClusterEc2AttributesOutputReference",
    "EmrClusterKerberosAttributes",
    "EmrClusterKerberosAttributesOutputReference",
    "EmrClusterMasterInstanceFleet",
    "EmrClusterMasterInstanceFleetInstanceTypeConfigs",
    "EmrClusterMasterInstanceFleetInstanceTypeConfigsConfigurations",
    "EmrClusterMasterInstanceFleetInstanceTypeConfigsConfigurationsList",
    "EmrClusterMasterInstanceFleetInstanceTypeConfigsConfigurationsOutputReference",
    "EmrClusterMasterInstanceFleetInstanceTypeConfigsEbsConfig",
    "EmrClusterMasterInstanceFleetInstanceTypeConfigsEbsConfigList",
    "EmrClusterMasterInstanceFleetInstanceTypeConfigsEbsConfigOutputReference",
    "EmrClusterMasterInstanceFleetInstanceTypeConfigsList",
    "EmrClusterMasterInstanceFleetInstanceTypeConfigsOutputReference",
    "EmrClusterMasterInstanceFleetLaunchSpecifications",
    "EmrClusterMasterInstanceFleetLaunchSpecificationsOnDemandSpecification",
    "EmrClusterMasterInstanceFleetLaunchSpecificationsOnDemandSpecificationList",
    "EmrClusterMasterInstanceFleetLaunchSpecificationsOnDemandSpecificationOutputReference",
    "EmrClusterMasterInstanceFleetLaunchSpecificationsOutputReference",
    "EmrClusterMasterInstanceFleetLaunchSpecificationsSpotSpecification",
    "EmrClusterMasterInstanceFleetLaunchSpecificationsSpotSpecificationList",
    "EmrClusterMasterInstanceFleetLaunchSpecificationsSpotSpecificationOutputReference",
    "EmrClusterMasterInstanceFleetOutputReference",
    "EmrClusterMasterInstanceGroup",
    "EmrClusterMasterInstanceGroupEbsConfig",
    "EmrClusterMasterInstanceGroupEbsConfigList",
    "EmrClusterMasterInstanceGroupEbsConfigOutputReference",
    "EmrClusterMasterInstanceGroupOutputReference",
    "EmrClusterStep",
    "EmrClusterStepHadoopJarStep",
    "EmrClusterStepHadoopJarStepList",
    "EmrClusterStepHadoopJarStepOutputReference",
    "EmrClusterStepList",
    "EmrClusterStepOutputReference",
]

publication.publish()

def _typecheckingstub__decd9d60ae973c9fadffaacebb1de0c0526ef015418985036906fdcf7a5e4966(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    release_label: builtins.str,
    service_role: builtins.str,
    additional_info: typing.Optional[builtins.str] = None,
    applications: typing.Optional[typing.Sequence[builtins.str]] = None,
    autoscaling_role: typing.Optional[builtins.str] = None,
    auto_termination_policy: typing.Optional[typing.Union[EmrClusterAutoTerminationPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    bootstrap_action: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EmrClusterBootstrapAction, typing.Dict[builtins.str, typing.Any]]]]] = None,
    configurations: typing.Optional[builtins.str] = None,
    configurations_json: typing.Optional[builtins.str] = None,
    core_instance_fleet: typing.Optional[typing.Union[EmrClusterCoreInstanceFleet, typing.Dict[builtins.str, typing.Any]]] = None,
    core_instance_group: typing.Optional[typing.Union[EmrClusterCoreInstanceGroup, typing.Dict[builtins.str, typing.Any]]] = None,
    custom_ami_id: typing.Optional[builtins.str] = None,
    ebs_root_volume_size: typing.Optional[jsii.Number] = None,
    ec2_attributes: typing.Optional[typing.Union[EmrClusterEc2Attributes, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    keep_job_flow_alive_when_no_steps: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    kerberos_attributes: typing.Optional[typing.Union[EmrClusterKerberosAttributes, typing.Dict[builtins.str, typing.Any]]] = None,
    list_steps_states: typing.Optional[typing.Sequence[builtins.str]] = None,
    log_encryption_kms_key_id: typing.Optional[builtins.str] = None,
    log_uri: typing.Optional[builtins.str] = None,
    master_instance_fleet: typing.Optional[typing.Union[EmrClusterMasterInstanceFleet, typing.Dict[builtins.str, typing.Any]]] = None,
    master_instance_group: typing.Optional[typing.Union[EmrClusterMasterInstanceGroup, typing.Dict[builtins.str, typing.Any]]] = None,
    scale_down_behavior: typing.Optional[builtins.str] = None,
    security_configuration: typing.Optional[builtins.str] = None,
    step: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EmrClusterStep, typing.Dict[builtins.str, typing.Any]]]]] = None,
    step_concurrency_level: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    termination_protection: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    visible_to_all_users: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
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

def _typecheckingstub__edf9614b79c795c421df622d4c5cd5f1e3f1b88dd63f984a80c0b4ba9c0d7478(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EmrClusterBootstrapAction, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a266b4811b6f47399d607f9b5755b01ed5ed3ef0a172173322b165647f2a8623(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EmrClusterStep, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce6fcc38891a7ea94b37d44e44a0f3dc388fd972a4dca728cc55afd8d3b31769(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47fe81e4597ddb012564aa0dacaf580e4001fdbd3d67277563f7b381711d192c(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__adcebc8984ac8e544b44c0c8164d6cbf5017968b244ce7dd855f2f4f11d4b498(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b8ec072e8bd2325a11b3e44093adea00f67e8a95df73f0b9ca33dcfffef2c0a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__453067d9493b77778d130e5ae8e0b022c5c5683af4d5e11f35234310ce136001(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c877a8903592920550444f292d857b2ec76fee9a58bcbf2f36739e891dfa116(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__393245633c5f390f74cb462852e16e6e8c25598b1528c3efbd07883b6dd5d313(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4be5cf26116bd7ae069ac7ddbc8072858e2b8198db4907615228bb8f595a18e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__118f556527576bebd4b5e13abf8c08c39a19278f2364d3c24b2eee62eac817d9(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__244fc3f8219371f28e5e944bcc1d7b468e811ca9b991604acfdae24168f8cfbc(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a4f5d84e0a9e20820cc1d4ec64563e4cfcc6311b744a3c763ff0699e100a858(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9dca4f75ff968b7ef7b47ca992c485ed518cf35302765d25307a0e822eba6933(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9dbe351442b6d62742b372ab1e1bef91f89fd29eb00453109fcba65b61ad27b7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2fa41776a0809bcdf9e643ca5e55a7f97a60a458252dc5a56a151ba81832d764(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b79b5142c20e6fa1eae89e453bf5e2ffad9c9cb5fec3a39c63d17e4936c4a3f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cdad73f2fd0d2b7c0c099b509cd6699f7d1a6540f0e8546cef73200d3753ee81(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c1845077f1b032010fee8a360f1c44c5eb00154fafa5161cd54306e0e85f05f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a700b06929ad929c9e6a6d531746d6aa8235f238e774004c41478903ce20a9bc(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1e095a85480fe0c2dae28fa4a1d84cfe42259d28277b76a616d820c561b4dc3(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0df33ff28fe7bfd82490c25c1f1823cb54094cbe28d25db90f58e49fd18fe60(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72014be48fdfc85b15f8cabe696deccdc5bc9e107276f058f1ffff2310145855(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c170dc350316990e67c408397c1b035c352e1871a9f5bef33073a521d4589240(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2a1904cfd52d1c8bacf02d44fc40eb5be4bb776925e4a6bc9c08871ade3275e(
    *,
    idle_timeout: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3fb77bbce036f13a3d9b756eb7d0b65f68c70487d10c30d09ca0fd87119c8f8c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2a1c91ee4fa69fa76bc51531384f2d116058b427005133692aa958e49ff778d(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5708caa6df564d26078771f300fa5bc601eb89d08cf7137df4770d9493458455(
    value: typing.Optional[EmrClusterAutoTerminationPolicy],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68c04741d0dda2d1401d0a2b27db34a1fa05e837ccd846b9c9c5a7cc66b5ca75(
    *,
    name: builtins.str,
    path: builtins.str,
    args: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1721b89362240c326825086e166901c44421400772c7043acf311d5a70267de4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad02f0a2349c5740635cbbec835a57ca3990273986bf628ca036066a614ed94f(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e497ffac6bcaa7f882769be9bfc05e2a65fad95225c467e4fedee3245bfc9b7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f340330493eed7a0b980032094813047e31f39481db3867948eac4ff3b8708b5(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30b46b2d54bf0883b370944e019cf0d7e2a8d4a9f7d28cb93c741baafab63bb1(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1236045e2ac747c9d287696f24bee14919c1385ff9def432444222e76538b5f(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterBootstrapAction]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00b51f5d216009e1b03c1ea3187dd4a644765bd2df1ad1ed681feabfb90611ea(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80c113d78146151404b06cb2812327fd2d4a65c7d11b9643d590a9f6e3a2308f(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0d87ba6829b0c43e0e2cec7a9a5b7841bb819d7d822b93ecd2e65d44c59941d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88f2c12e0e4ee51b2b608756fd072ec29620fd029971ac3e8d170c458e1fb209(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3a98bfce395876c6eb87d50cb73bfabc99bee4a0e9d9af39b9168075137fbc6(
    value: typing.Optional[typing.Union[EmrClusterBootstrapAction, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__282119b5c3f4cc2badbb7b6569b212950a7071deeca1bc29bdda4ced3d0eaa24(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: builtins.str,
    release_label: builtins.str,
    service_role: builtins.str,
    additional_info: typing.Optional[builtins.str] = None,
    applications: typing.Optional[typing.Sequence[builtins.str]] = None,
    autoscaling_role: typing.Optional[builtins.str] = None,
    auto_termination_policy: typing.Optional[typing.Union[EmrClusterAutoTerminationPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    bootstrap_action: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EmrClusterBootstrapAction, typing.Dict[builtins.str, typing.Any]]]]] = None,
    configurations: typing.Optional[builtins.str] = None,
    configurations_json: typing.Optional[builtins.str] = None,
    core_instance_fleet: typing.Optional[typing.Union[EmrClusterCoreInstanceFleet, typing.Dict[builtins.str, typing.Any]]] = None,
    core_instance_group: typing.Optional[typing.Union[EmrClusterCoreInstanceGroup, typing.Dict[builtins.str, typing.Any]]] = None,
    custom_ami_id: typing.Optional[builtins.str] = None,
    ebs_root_volume_size: typing.Optional[jsii.Number] = None,
    ec2_attributes: typing.Optional[typing.Union[EmrClusterEc2Attributes, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    keep_job_flow_alive_when_no_steps: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    kerberos_attributes: typing.Optional[typing.Union[EmrClusterKerberosAttributes, typing.Dict[builtins.str, typing.Any]]] = None,
    list_steps_states: typing.Optional[typing.Sequence[builtins.str]] = None,
    log_encryption_kms_key_id: typing.Optional[builtins.str] = None,
    log_uri: typing.Optional[builtins.str] = None,
    master_instance_fleet: typing.Optional[typing.Union[EmrClusterMasterInstanceFleet, typing.Dict[builtins.str, typing.Any]]] = None,
    master_instance_group: typing.Optional[typing.Union[EmrClusterMasterInstanceGroup, typing.Dict[builtins.str, typing.Any]]] = None,
    scale_down_behavior: typing.Optional[builtins.str] = None,
    security_configuration: typing.Optional[builtins.str] = None,
    step: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EmrClusterStep, typing.Dict[builtins.str, typing.Any]]]]] = None,
    step_concurrency_level: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    termination_protection: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    visible_to_all_users: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c8b6de47dc972386f6bdd9adfd14f6bb9cea8fecf7c619692e6b892bdf7a33e(
    *,
    instance_type_configs: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EmrClusterCoreInstanceFleetInstanceTypeConfigs, typing.Dict[builtins.str, typing.Any]]]]] = None,
    launch_specifications: typing.Optional[typing.Union[EmrClusterCoreInstanceFleetLaunchSpecifications, typing.Dict[builtins.str, typing.Any]]] = None,
    name: typing.Optional[builtins.str] = None,
    target_on_demand_capacity: typing.Optional[jsii.Number] = None,
    target_spot_capacity: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6914a8d43c41217051cb416426c502d16cce8db87c9f9e04926c8a4c2e41b54(
    *,
    instance_type: builtins.str,
    bid_price: typing.Optional[builtins.str] = None,
    bid_price_as_percentage_of_on_demand_price: typing.Optional[jsii.Number] = None,
    configurations: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EmrClusterCoreInstanceFleetInstanceTypeConfigsConfigurations, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ebs_config: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EmrClusterCoreInstanceFleetInstanceTypeConfigsEbsConfig, typing.Dict[builtins.str, typing.Any]]]]] = None,
    weighted_capacity: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5905decadb215eea36ba30d6af82ba34ab49ec8f2a14a89211b4708a34d21a28(
    *,
    classification: typing.Optional[builtins.str] = None,
    properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03f48ff30d5e4f56087e1eec11437b63ce70b087446cfd3ba078d93c1316965d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d77fbdae8a7a1c6ba64046526236574534547b1d87cc861add049653195b7667(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3bf2c108be5808a20b074389cfdfb87f9e97bc313feeefc0e1297f28a7be60d4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99bd9b2621c8b5b14bdc848334b56f95c4571eaf5f6aee50a661ac0b75b7315b(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3018f38db392d153f149122a79cb723840411496bcecbb04ba475b3bd76ce11(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a4154ac926a25a6fa7cea4b992a249f8385573ec096028be7f39dee67d363df(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterCoreInstanceFleetInstanceTypeConfigsConfigurations]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__caa2d9d1c3d39f3400cd1b9875b273792a2e46bee26ed3b5a4e965a4754c6f6d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33efd3afedbb979b01434b213a6c2df7d5d18f40ef72b2ed5abb0c650ae8ca56(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0debe8f93b5ac914b708ff93621264834b4d13131ca855a85bb85f5ceb095493(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57028a26d3dcdcd3e03fd72d85a6e8baf913b3688641f816ca3d4129160e4e4c(
    value: typing.Optional[typing.Union[EmrClusterCoreInstanceFleetInstanceTypeConfigsConfigurations, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9098f1b36ff37cb986723c6edfb1706c84734f4ac69171244e82ba07ee4beb1d(
    *,
    size: jsii.Number,
    type: builtins.str,
    iops: typing.Optional[jsii.Number] = None,
    volumes_per_instance: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af1aff2fc0b119786dba85a4c5ceac5beaa4a4f48ce2a4c5271c6f962f30a5e1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4615a212c3a135e4a810e34e267ea69777bd3d88020686884d1f9ba48431066c(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c71c66f298cb2e99f475a096ebb623d633e084b52d677829961092900f681672(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ffc9526d23a6485a6eb0c982e8ab8f82b6efe0e7b42f68ebcc9621ce3c6703e(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bdf43164a0a2c377c49fb35e3843b9dc55ebcf50df5c5940043b24549987df45(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1fa2c8d45f8f6b66bb1dccedfb011a8abece2ad8ade941a262073157ee6e9fc(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterCoreInstanceFleetInstanceTypeConfigsEbsConfig]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee23aae122b20f4a05bf1ac6c1264cc25c9d2cbd56e1b27cc47c75f7c100ec07(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4235a098cbe2da14d7ff23ede9c8a08250909cbb951fb30fd501d3e1d18bde5e(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46591c8bd1349f280e76e2d68393c3e1793923d907142bf0bde5a887c4b0a361(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dcea8f3da30373fa275458019cf58d6f33a91ea8cf93a61d0d8a2c1ca01e36a6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a4dd1e365e809be93d441adb0e78586a8849acd9383a313df9dfb5008c857e7(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9424a15398ea01ab60ca57855ff1fc43a4f2d18bc8f9b62ae4655ab1b834d7f(
    value: typing.Optional[typing.Union[EmrClusterCoreInstanceFleetInstanceTypeConfigsEbsConfig, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__448419ae3285dd15b7cbffc65bd851c984ef17ad9dcac4a3dec41246369e71a2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__548d359e936e9c92dace12cd2cf0b27c25b59d557730b8187875c252926c5571(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d51b611c1682da8d40fae6cbadcfa33bee074eabca540b72d6f8776ac4e03039(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e717b0fdc3d4a4277c1e9b9b2d4b08d09a20bee9b8f5284eac1e259677894121(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3f5203b3c0218f2820f1ca9517a7aad251968752a2350be41798762ff2b9838(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__682a491197093f0cf8abb5c7414c7a7439ac66ca30c795dec67c25223be6398c(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterCoreInstanceFleetInstanceTypeConfigs]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__882f8977cb369d96ed90c009094a557203db07d51a68de2e31529aafa9e3dc8c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b95f737edfbcbdba2dbccd30a9f6f884b2905d4c9d6f79d25124a6d0a0baea3f(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EmrClusterCoreInstanceFleetInstanceTypeConfigsConfigurations, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4519fd3e7840c87f685e1b202289833267898fef6357731d2c05f2fc677da30f(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EmrClusterCoreInstanceFleetInstanceTypeConfigsEbsConfig, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59a41709911c2fa0135ae4ff8644430129af8be624bda8c183c2f0a077e002d1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3b2ae5609f01913506eac91e9ee3bfee0720edefdf0331acaa0ec044ac890a6(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b29424db561a4412bc5960f58861eea1de9df319471be88002ab576aa07bba49(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53ad4200fafa58999af50d9c0bb79d80400a25d5b85a18282b2852aef07e662a(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf56f7c51f0ec88050b6c04101dc6517249a49c83a2cf9dec2a5ac201968b6d1(
    value: typing.Optional[typing.Union[EmrClusterCoreInstanceFleetInstanceTypeConfigs, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e2604fab7f7d4824d1093b0c21263658597f4a64e2a597376c7403f697fdbcb(
    *,
    on_demand_specification: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EmrClusterCoreInstanceFleetLaunchSpecificationsOnDemandSpecification, typing.Dict[builtins.str, typing.Any]]]]] = None,
    spot_specification: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EmrClusterCoreInstanceFleetLaunchSpecificationsSpotSpecification, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c95f4bdffb8cf166811663dfc1852c08b1411fc6e9a645fa244ef058f630a2b(
    *,
    allocation_strategy: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03454b942830d233578457e1da787e7cdf9f8ec5d306003c0d2c2b9f31654fc7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7932e8290bb4dcb5cc48c95c2dfd57b9b3ecc48b1c223159f1426543b2517d3a(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e28f6aaab7d6155c86a89882edc43e4e575bafe5e51d3914d6d243dedb02bb29(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22532de53650504c2ebd7ad9053bdfba3272ef29a72dfc6180667a749350cc5f(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8548b99f33d347093b1ba54248fe19e7d16043f2b9f208c318334f3d6b3e23d3(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0dffe4674148086c6a1d6028f7d8b77851a5930533c570fcc5b7c4268b68a16(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterCoreInstanceFleetLaunchSpecificationsOnDemandSpecification]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78df058fd7d560caffca20936ea9fc6792efeeec7f9bc8322f525606e1ad3383(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a852f5b81b89663f109b66f74f0856af5909d15f36df227c33bb93e5aed0dc72(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dcab4ec59eeb10b1d785072d3cdb2232fb0597622ccf534639237dcb87c4591a(
    value: typing.Optional[typing.Union[EmrClusterCoreInstanceFleetLaunchSpecificationsOnDemandSpecification, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3659729a677a39060832e753568ab169086b8d6fbed426a382f809052c382bfc(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f112f87b722d472b1a70c45aa628e5b8b2b252c7e8952077969404c863cdb59(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EmrClusterCoreInstanceFleetLaunchSpecificationsOnDemandSpecification, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__662f54f39c1322786b5b61dcc7fb21c4592e8e696daa1ccb060a2401c6c764fc(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EmrClusterCoreInstanceFleetLaunchSpecificationsSpotSpecification, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b8449968a7651077c139e814bc5e6ac5f1a2a6274c23625959ad1195ef4986b(
    value: typing.Optional[EmrClusterCoreInstanceFleetLaunchSpecifications],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c87529476e33a0481bef9f5fc1cf4b28a16e39f2935e81c120ca258b156c100d(
    *,
    allocation_strategy: builtins.str,
    timeout_action: builtins.str,
    timeout_duration_minutes: jsii.Number,
    block_duration_minutes: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67457fd6780e0705d9b4aa4c5a108c46e05a89b2156fb6f63889353819785b1e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b3ab9a2456398bf9d32f5765addc85d48fe8dbb3815259c2bd52b231bf279e2(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51a66cf716f6e0cbbcefbccea933af420c399f8bac79717585402f9a77906ce0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af5fb0cb5812d60f49ea4094d3916763164223890bf56703250d8fd7622c3524(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5eb7c5b9369335bfcc9026577d370a677b5961b34d357f8f7d3735df1ccc28f5(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ef6707eca39aa0b3fd6c65e5d7839f59c7d8b42b45d966e5899b6ba04ab7f74(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterCoreInstanceFleetLaunchSpecificationsSpotSpecification]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7510d5eff4eb48eb31d2cced6d41785851056be4d12a9c9fb1ef0605bd3062f2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6bd71c6138c4dfdebef1a7cf47ec05d2fa8b80a238a60d9b070d81e1e0b8a136(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b6aaed56bc28d24a96d892363418974d695ff4f0e7b96d111d71508d19ce1d2(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__587777a78200dccab2a29fd0e522368efe2ad2b99bddbb1d7d44404f4bf092bf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0f495f7cff55c34fd12a094ee749d7809feeec72ab119da6cc10d1b612cd1d2(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62afb0423afc3c3de5e0e7d6e74aca29cf79ec75af9a3612fef08752558aca5d(
    value: typing.Optional[typing.Union[EmrClusterCoreInstanceFleetLaunchSpecificationsSpotSpecification, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0be4904c71099b13990146489541f865931eedc494bc744a5eb9942bb76589fe(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__668d125342b1e7f447ae046b5268510135081bc38003b314502caa44baa248f5(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EmrClusterCoreInstanceFleetInstanceTypeConfigs, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0be01ab04b9d1456ae7858f11751838c9cdc702d84fa6b56e1045613f11b1e6a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49b67487b16b52c54b07d37d3ea0f352d4eed709b21714fb24aa47ddf7d47f95(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a35a5033c7ec3bd62d1b7286982ce9e287600752f80b555bdba6f01d80b4fc7b(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45d97cdbd4afd381e238bd79083167e136d23c0bef30be0c70296563de783d21(
    value: typing.Optional[EmrClusterCoreInstanceFleet],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b5e37e894931cf18337e773de08466eb3444675726e598c3a98265d6bc78f88(
    *,
    instance_type: builtins.str,
    autoscaling_policy: typing.Optional[builtins.str] = None,
    bid_price: typing.Optional[builtins.str] = None,
    ebs_config: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EmrClusterCoreInstanceGroupEbsConfig, typing.Dict[builtins.str, typing.Any]]]]] = None,
    instance_count: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e9b4ebbe5e96cbd218e9c9aa34910fb6e9d2ebd2692946d68f4570054bd5081(
    *,
    size: jsii.Number,
    type: builtins.str,
    iops: typing.Optional[jsii.Number] = None,
    throughput: typing.Optional[jsii.Number] = None,
    volumes_per_instance: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2db1c18673190ee44da6a64503867a557c8ce2689e776414bccc4ae6f82cf690(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__871bd41641aa0dfb2ace534d3ddf64758804d47b366761ab9cf2adb1755116f6(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8fea8ba69632b572b580895d652a25e50f4537020f7c62cf0a7661aa7c260f57(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2efcb3473ed7c9f3d2ef9a2f3ec705ddfe9a550432e1042bffb945947e905346(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0eba3a507ea317b57706d8f76514864b420379bb7e8aac5eb4e85167fae2bf00(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8dab02188e91468a267bc54f2ca12fc7394138ff88c3bfc975b7a9aafcfb02f6(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterCoreInstanceGroupEbsConfig]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37492773cda16114c1927d2cd3dcb29329de7f82c5df71c955c104e7bd613bcc(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69ee95635f5ef73f7d69d6090245201fc1815317646a6af0d4259400980bda86(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__793c8e832ff25c0cce9436a7b6b7d35c854c008b0634491e095f5972bdc6074c(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eda1919e81d8688fddfe92063d97f5d56066d1c348aff200a2cab767c3bfe97c(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09081b4930f1da7e1e542b30e21660698ec9206cbba20340c55f038a813261c0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5adf807fab68dd64c2de4ec54ca72113d5a8abe24a10c08f0b07b3b3a4b4a093(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60cce777c5ce246a191f5c2c9c6ed5d9b32b584456a275a333a61e75f5cd5d6a(
    value: typing.Optional[typing.Union[EmrClusterCoreInstanceGroupEbsConfig, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__783eb64cc7f13374825fd5bea5267893549559d8f73fd2f5c96e4d983e40334e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__172b16e0dd911fb0e725bc4abc4590a0bce83e0a7b2664917cbfbcf3bec17863(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EmrClusterCoreInstanceGroupEbsConfig, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87cb4a75a378fa78b6e992b138ab894bc1251a628e5f83d81bd894e19b955c21(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ddea35efc158764592764123754e34e7819adc5f2a093ea7acaf557559a7c2e5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ea598f486ed32854e79aa5b4517bedd4d850e22f034a7338426e7a9fd76db8c(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f1242513934cb2003422a870293af36374798374ad80f657f9d8772fad5fcfc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__466be93c1b0464f017fa39c782bbb26b2f9cdafb86ac43ae98fa0232aefe6e3a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e53e23e15057a0c953b715fd14c3cc920daa7e2f3e557c57de5a930fc974ea91(
    value: typing.Optional[EmrClusterCoreInstanceGroup],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c714a1d96045fde09de957dbc43c1eb332a588732bcf1e96e81056135e493ee0(
    *,
    instance_profile: builtins.str,
    additional_master_security_groups: typing.Optional[builtins.str] = None,
    additional_slave_security_groups: typing.Optional[builtins.str] = None,
    emr_managed_master_security_group: typing.Optional[builtins.str] = None,
    emr_managed_slave_security_group: typing.Optional[builtins.str] = None,
    key_name: typing.Optional[builtins.str] = None,
    service_access_security_group: typing.Optional[builtins.str] = None,
    subnet_id: typing.Optional[builtins.str] = None,
    subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__589486f98e545a53e230510e19f8017f7db1a6f5e70d3d5faa97e39b8260fa60(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35131523c00b78a6e299d17791e6e718a0a8ff7fbe95bfa52ccc711621eaac0e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b0a2a4bd312c8e33ca3821fff1421857df834e4f164e2e9969b545a3e712074(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c00065462362bfc885e942f67ffcb9d37ac1aa814b21d69bc88b90b7e081dee6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af4c4fa18e32bc3f82c3d61e40f36d773cd363a8a03ab258c57e9a622ad580b7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__603c7adec7fd4785c5318212a99d05c5e742d5474a065a8c2378d39b04bacd64(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9d12148b78702687b240d0b7b49a1ae8588dc15018ded1f3660b40b32212250(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff9d248133a6ab6612bc91445f051696b86e677539b686e997ee242e089d75cc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__154a0d958a4ba371a85ee9267dd37d3548008294ef38b4e973222e62d29ecd6f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__806f5263dad650365dd30c8a007542321c11749ec8aeb70168ba0d5d44dfd9d0(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__941009b14ba6af6df6bbd51ddb4ca0a409e77ac1c197cbaf352fbf33cee425ba(
    value: typing.Optional[EmrClusterEc2Attributes],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c4a64b4c24c141525a777ea68288caf2ebc343c2ce8a4553d26a614a6349306(
    *,
    kdc_admin_password: builtins.str,
    realm: builtins.str,
    ad_domain_join_password: typing.Optional[builtins.str] = None,
    ad_domain_join_user: typing.Optional[builtins.str] = None,
    cross_realm_trust_principal_password: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7a2463b71bb99a3582994b6b296830575ab54897c18425df563baf5c4d5297f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7878fbb6e2057732c204bdf907aa31deb644aa739985f68f2013ebfa7f8c9912(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b88657ad7d5b006d927723eafe768ed25c09de18c2caaa23d10bc9bfbf818536(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e547854a5afa281e3e80501ce80fc885261fd89e0ca242702f29a5a4a54b28ad(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa47730885f968697b281f3ef5277c076c79ace9e8cd82f2fc19e7e0fd10abb4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a0f65a49525883eb615d11bcde336c7c5d027adfc3994eb37d84da60599e857(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2dd0597847185099feec5ddf3dae03dc7da00385cfec266f746ab09fcc3a6209(
    value: typing.Optional[EmrClusterKerberosAttributes],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1790a99ce31cdf8fd668f1dea8a46766192cda8f1192f6acebe40e99a1e4c66e(
    *,
    instance_type_configs: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EmrClusterMasterInstanceFleetInstanceTypeConfigs, typing.Dict[builtins.str, typing.Any]]]]] = None,
    launch_specifications: typing.Optional[typing.Union[EmrClusterMasterInstanceFleetLaunchSpecifications, typing.Dict[builtins.str, typing.Any]]] = None,
    name: typing.Optional[builtins.str] = None,
    target_on_demand_capacity: typing.Optional[jsii.Number] = None,
    target_spot_capacity: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__825da669fcd287ead738f04513a2bb1df8a957f326f38f6019370a3897d66b92(
    *,
    instance_type: builtins.str,
    bid_price: typing.Optional[builtins.str] = None,
    bid_price_as_percentage_of_on_demand_price: typing.Optional[jsii.Number] = None,
    configurations: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EmrClusterMasterInstanceFleetInstanceTypeConfigsConfigurations, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ebs_config: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EmrClusterMasterInstanceFleetInstanceTypeConfigsEbsConfig, typing.Dict[builtins.str, typing.Any]]]]] = None,
    weighted_capacity: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d94859863cef2afd6c70c73d3cd2e52bb1130eb37e7fb8a22134daa3a45344bb(
    *,
    classification: typing.Optional[builtins.str] = None,
    properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26a2ce27f94fb0cee470f091e45ab59813d19d64096d31a645c39d99f11a3c5d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ebc5f8bc91f9494787f6127cb770cdcea83536c9c3da00906d10ec1ae4007c8(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0bd095d3378d71865bad547a23f396efbdfae2da6be6dc54a4a4c0f5f0661c7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e27ba71480cb1b6c81fc4a7248d4fbdbc271b95d74809bc1ba375ad6f5bd7361(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7d8a485de4104aa24d199bcaf44d83ca162df1cbf0a20f4690befa6ac80bbe2(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bcf9fed9d23448b98b759d9fe0447e335d6d54f4b85b1b4f0c06285f3dc676c7(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterMasterInstanceFleetInstanceTypeConfigsConfigurations]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__919bacbe29a5e1d4e684be74264c76530ca51b592b373af4dfa64350ea23c05e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__499f926244d9d11c372383e67217d69a3320d1b46332aed9e200e777f507376a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51528b808136500772908bb9d1231bc0bb1524b098bdd3c9482ceb0364b76d0b(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4de8cd1de0c270bc507a9e99961e20af977549b2dc78845c82636529ba9916cb(
    value: typing.Optional[typing.Union[EmrClusterMasterInstanceFleetInstanceTypeConfigsConfigurations, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f34a09b20451391499d716f9f34863d74b8a3813d88265b0417338e92b7c7dec(
    *,
    size: jsii.Number,
    type: builtins.str,
    iops: typing.Optional[jsii.Number] = None,
    volumes_per_instance: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3162a7b295f458e6344daa17129265a4ee10bbc6d808fe4a513338d342cdd78f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bdff6a35f33b72787bddc11a5bf08754004d8b7812997f6e044ceeb30e2c83a7(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__913e81fede2d4f09de7dcddbe27ebd43e7844582cc22446ab1b1ae94ea71f591(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bce074c3e6c744ecf9bd23a2344888f2e070bf14c449649f6e58d023bdabd0ae(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98eec36e57e16dcf78d29d24bf6e416b5f50e1f1def714af696bddcfb3857e33(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__203258d89e7837e217c0d535b27cc562cccd492bcb68b17f29eec4d3c448ccdc(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterMasterInstanceFleetInstanceTypeConfigsEbsConfig]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2622d52e30d7452ab103e94ec34a2017747871182b6fcee87422cc9fe4c7433e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b0a1d0b2ab0ad58d4fddf41aa0dcd3f897c1fa8dbc362486b98175af48ff71a(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0a524d45c0a6bf9220b079bbeb083677d7eda321a60f560ffd1ca929fe77107(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75eb42cf09a4e56c9ff148a4d85f5b33e94e15e1409dd868b7a03c161aaf2b3b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8df6ec79fa23aa962c9d94d393cced94ee803da703e0a58f33c1e0eae0e8c918(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2186dd206fd139218d786b443b921cbe13dd45166cc9b7430883f3d6ea6b4b9(
    value: typing.Optional[typing.Union[EmrClusterMasterInstanceFleetInstanceTypeConfigsEbsConfig, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03cc9bd11ea3a4b38aab663c24a0c92ea71fe447073bcc1da19e52e967523507(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c7038b903117d77f719ee6aa20f5d6ba447cae4b94b5549aa4fd348ea197042(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fee8ddd79b130078c3f5929d40ae98d153f5b1b7ae621f7febead8dc86c17279(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e96ede4e70e0b1fdba40c7ae7b0f082fd5ccf13d63c2d8502e30b65535c00307(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93a664d6c8a86c5a908e9417e49d008a02a49ce473f1b66ed8775c4387970b23(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb4fb98cfebaafcb8d3cc4d53f28449c6a1365e536ddb183b6a7aafc4b6f53e6(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterMasterInstanceFleetInstanceTypeConfigs]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad2cbeadfd51876c0420f10695540c4bb9ca0c3e81ba2da9259cce2aa58badb1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f98938e118434104a9a205ace0c111ebfe1e294f97112d15d72b7e6a640838c(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EmrClusterMasterInstanceFleetInstanceTypeConfigsConfigurations, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26bece380cf2e7c3a88fd9107003fb2f3a52395b1873c49ce78d5d8fd09d2c55(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EmrClusterMasterInstanceFleetInstanceTypeConfigsEbsConfig, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2f174490b9eb3b79d6d80416e644c16cc7d246ac2c46e030f2db3c7e7940503(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__207c5e500fc1e4d2c75ea4102da9569aeec607cd72c82bb48289aecc0f5a5f06(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88c4f1ea2f6bdae8cfab92d2679b9b55a5e648eac94b782f19b7f06ec6bd81af(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05e24754e9bc19004b7d6d23a6ddcb25d1ccf4df7239834cf2846ab4b3131d78(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d0fae32d76322690a0e4c3f1e07fcfe5f9e62feefc01b966e1d274f2f6de834(
    value: typing.Optional[typing.Union[EmrClusterMasterInstanceFleetInstanceTypeConfigs, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dcca71c5c9ecbdbeed25b12e928347f4662a30879d7ebd04a5f3b8d966d239b5(
    *,
    on_demand_specification: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EmrClusterMasterInstanceFleetLaunchSpecificationsOnDemandSpecification, typing.Dict[builtins.str, typing.Any]]]]] = None,
    spot_specification: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EmrClusterMasterInstanceFleetLaunchSpecificationsSpotSpecification, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9fe57d31acc35eea0fb4ec15f98a2e0061c14627d2220ce6e5b6e4c0e9db3b6(
    *,
    allocation_strategy: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a336c352691190d3e938a4acac4c11275285db51907c4c86770b5cb45bb0f3f7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83a524100a49705053f310064cb849da2cd257c9accd7c9d9c557de3c73ec70b(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45ca8effbe073c99ddf82fa12dec1b8180018dd4d217f0ec5c7d40523e13b6f1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__750ab82cbc71742d6ae00cc63028f55b4cbe2758d3f80ef06fdf6c62adf151bc(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__477f9c9317e63f497ab9c42a984591c8e66eb10347d18eaba9e364d0f1aded22(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__287480b6589487d7d3586db110075498d963dc3245a52cdc3ebbe0cf3e3d2da2(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterMasterInstanceFleetLaunchSpecificationsOnDemandSpecification]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5fadec13ddea0bbedfef4fc617f6cbcb1a1ac028f9dae6a85c76dcee6d2a8144(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff8f9d997d04969454a8d40380b090c45ebe60c852ab36cb9a1317cfbff51e4e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__266abf712fc7546f2a7285a382fe08f18b01b97b7a6686de7b8ffed0adb3094d(
    value: typing.Optional[typing.Union[EmrClusterMasterInstanceFleetLaunchSpecificationsOnDemandSpecification, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__433bf52d79be47ea07e00a55dcf53c651c051b6fa3b229c259a25f5998dbee49(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c591114075e122e7f941e5cfc0d4c8f570c1b276f16b349d85c96a769de23dda(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EmrClusterMasterInstanceFleetLaunchSpecificationsOnDemandSpecification, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1b64377d237c146149d7cfcba130bf945a49894aa92cafe00fc531620aa8ad7(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EmrClusterMasterInstanceFleetLaunchSpecificationsSpotSpecification, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3c7f8c181ef3cdefd91ba7e5601354e0c722449c010829540178be64b1809d2(
    value: typing.Optional[EmrClusterMasterInstanceFleetLaunchSpecifications],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ea4fa0ee87959293213ea000e1136f350ce2c83f15ad8941de45d0668f33d34(
    *,
    allocation_strategy: builtins.str,
    timeout_action: builtins.str,
    timeout_duration_minutes: jsii.Number,
    block_duration_minutes: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c56b548cd432e142ece643c949f308dea8fdbd6308f89b8e41770153516126f4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__443c0f11db0a2841236da754ddfef9e79a3b34155fc66210ed3f303ef3cc8a26(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__208da9334de51a8bab6347e16904083fc0dcf830bbff34090b5392534c37718d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d96cf8c9d878a0449c4e362ac73623439cbe12040fdeec953f9b4d137173cdf(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7241aeab5c4f669d15b885e3345f16db0988ab34385d5c7256de328de813266c(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ebdc419611d36c51214f0853e4a2df5515a28bed72985f874ad7ea6f5bd6bd0(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterMasterInstanceFleetLaunchSpecificationsSpotSpecification]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d78edb9807653d2af06ff97e1ae7852566ce0fddbda2612504ae14f98058df24(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ec528411788fc1cbf157d2a89d8c8983719a93bb8b91447dbf46e25a3299797(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68f876e1f7f07f720ef584354375c7e77ecd9a896a8916de637dddb49c2c9e70(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__847f78bb65d6cf8e9fa9e2fb2a089adfcd18f4ce433569483311e5701ea8f35b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77b4311b883f239a52972024a1c5776249cc0d4acdafcf5262c824b4e552a6d6(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c720af5f15aadefafafb5f1feb11a0ad79bce966297b78956347f25e2266944d(
    value: typing.Optional[typing.Union[EmrClusterMasterInstanceFleetLaunchSpecificationsSpotSpecification, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f190b9a11bf189aa18ff4fb94c9ce343461aba2886ba11582b137cfe749b800(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ae839171324b3b41d8a9cce486be64874f83c7eb56477175c83c0f47162db8e(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EmrClusterMasterInstanceFleetInstanceTypeConfigs, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__add177c1f3f5651a57847c9625b6a052ab43697d9b2302b043d7fcb0feffd237(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c46fa63349d8920e3f844b7bb94de1804f2964cd05a4067264ca025bfa218d17(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__495b8858b3f980dc938a0a3c553f4b206a090837803d627f8239b668284e1842(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__481eebdafcc093e7683abaff47ff9ab98a437f3911b5e2a17999656137da812a(
    value: typing.Optional[EmrClusterMasterInstanceFleet],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48a338805c18799177c2f8263901816811b02aecad3a48f073eeb820e794923d(
    *,
    instance_type: builtins.str,
    bid_price: typing.Optional[builtins.str] = None,
    ebs_config: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EmrClusterMasterInstanceGroupEbsConfig, typing.Dict[builtins.str, typing.Any]]]]] = None,
    instance_count: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__251342fdb6ad1b68c27fc86c03d0ae3e58a334962c520984f253e7a08f72cb56(
    *,
    size: jsii.Number,
    type: builtins.str,
    iops: typing.Optional[jsii.Number] = None,
    throughput: typing.Optional[jsii.Number] = None,
    volumes_per_instance: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb9e6ba005de8796ac794292d8d6d66cbebbdc1f95bf12db4d2c183863730bf6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eda630a0bac158903bb26248b0fef030ba8676aa6662df62f300bc47308a7908(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40ffe6ad87cde8cbd7400d595d4dbf627e442e17bea217e31ab6d116c4e57c74(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__042efbc2848794584a8d96adf5659cf2cfc782e023a0396abfb427acb45d0388(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__398233e80c94396e7aee46ffa0ef34a7fe5bb8502b67793d961cf08520a77e82(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58d40f8a393d51a1f36b5ca378cea00e4411dedb05fc5bd25a4a509f38ac2a32(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterMasterInstanceGroupEbsConfig]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d19282512b4f200c1491b0cf57db1ef7f5ce25c7e8872d7f63a41b7987b4e86d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__462c62ff7429f995a08f89d6ab3fedc6ac54fb5cc1f0e516f769a034b74d8002(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a485a0bb70bb07bc95463834f86101261d11de2d5526153dd130d7e6712a436b(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e9bd0efca8afe0d5535f6472843622ea4e18941bc19968187574f9e6689ed3b(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef7775b6a3a53820a7ed6597dd53c29071276de81c5a051fff6d00955bcef7a9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c27a2f79c18b2db146319480f9fbb7b0e8b894d6b74bed17c2ea9bff289fd221(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1ed7c824c77c6944211fa8b7177b0d764548f20665aa4290f69f0826dc3596e(
    value: typing.Optional[typing.Union[EmrClusterMasterInstanceGroupEbsConfig, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00a70e55f332612c847b65864528fd60a94940c0aec59ba3cef6d3d0bfe60e16(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0624268d40d9ae7c0c5d15913a40cb8c38ae4222bbbecdff4231a7640f717c29(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EmrClusterMasterInstanceGroupEbsConfig, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9bc6ee2d4f2a9ab58b82ba4a57cf6b7b67b1ebbfc397fcd12395b660baa13fb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48920a169e5df260b1401262b57bc21f95fd29595af59461fdc780ce4e856907(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a70242e130f36f9949da9c3c8c18db08a7563cef07e15a9e85d4fd1482d04130(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b15e6146975cc86ac205cd95487322ec6fe57a21f880b07dac7c26cfc350a9dd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b7b583aea0a71ee07d98fa21517e297634f20e3f2ca8319069f74818a4c9131(
    value: typing.Optional[EmrClusterMasterInstanceGroup],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__595ac141d9ce989f273d94077a483e7f1dc6af0a756b2df97aa8a43cc7f5a084(
    *,
    action_on_failure: typing.Optional[builtins.str] = None,
    hadoop_jar_step: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EmrClusterStepHadoopJarStep, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6be43cee477e6a633659509196237210e9b963db1fe853c9f6ca655d30ac95f7(
    *,
    args: typing.Optional[typing.Sequence[builtins.str]] = None,
    jar: typing.Optional[builtins.str] = None,
    main_class: typing.Optional[builtins.str] = None,
    properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__320e3b3f595e110971c96833ee1f397f316b7f1538652d61fb712674a7994439(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3bf40705c43be7aac869f343976301dfec5c2b41600e90b301f1ca5b0a6b3f2(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01a1969f7d94c5742ac674243b9d55115cfc9162ad985b1791ba2b9bb2c57ab6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9dd6d3dbd29bbaa3e51304684938e2cddaa408bd87ef34e11177a7e78e2129cc(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1861f729c429d2989acf544a354c5e77db5f68847fb3ecd5e8daa5ee8eda825(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__262e3a798af3eb11f1a97e8039fbbc7bbc7c88424cb246b2bbc2874468179f9e(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterStepHadoopJarStep]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__594dca53128ada41f5ffb0b2dbd5b5f6885fee77e7e67e38f0ca040f3a10eed9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28b6964c2fe11e90739c9c4ec3241721f0f7f92b6b5059dc8af0d448de34ee0f(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__801c148beda5d5c7389664b2fed1d02226132bb0c466a236febad7a6cce76f28(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7eecfae2ed2c2534b92cc00d882de126df2a7bc35627617face054cf4d54f8ad(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__027d1b266ab8ce4b9d897f8a62a78adaad5f05e0ecfa5f8f72a2b97e3efadb0a(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58831eb703d1527f0dc49bfccc65c5773e7ffe14e05ac7b8bb6b4fd760113d80(
    value: typing.Optional[typing.Union[EmrClusterStepHadoopJarStep, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5042f2b18dff3332848d0fdbfdced25878f76d0a9f80a95e1cdf248405699ab(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aeaecc585fe3236b2bdaef711600388f3760620aa4508294d31cc486c2b379a6(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb60a3ff5da358404c845b47d7fd04cbc0669740727526af865db6ac3b6fa272(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98bf5a535538b0ada9884b20366439e8e185ce2024e9b15d170866cbe139905a(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44b11d694c8b714ae40ef471b7ce7c9b1e3d7cfd3e77cba38b9a05eda517a73c(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f602ac2805dfb4ac9246f826ebcb8df4478e049de5abda1f6196fe2985a59be7(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrClusterStep]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__896eb17e42db7fad186ce80fb16a6f78791f7eda159aa82947e865efa3149bad(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05bd32ba8b4903bc046f43aff00841e38dd47dd59b5807c15b3026d896fc12a4(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EmrClusterStepHadoopJarStep, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af6644a8db874dc3de8d7a27a839d3813adf95a3119e82c7cf6b95e433069f83(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ebe1677597af760a911ad6d8c36ab139375d4f5ebd39116a12eaf85b803c61f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64e58d28d7b606fa6d450dafdf43f087c5d6667b2f1b6951a6df9f3f29f229d8(
    value: typing.Optional[typing.Union[EmrClusterStep, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
