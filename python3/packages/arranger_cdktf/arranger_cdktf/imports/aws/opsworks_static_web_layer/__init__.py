'''
# `aws_opsworks_static_web_layer`

Refer to the Terraform Registory for docs: [`aws_opsworks_static_web_layer`](https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer).
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


class OpsworksStaticWebLayer(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.opsworksStaticWebLayer.OpsworksStaticWebLayer",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer aws_opsworks_static_web_layer}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        stack_id: builtins.str,
        auto_assign_elastic_ips: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        auto_assign_public_ips: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        auto_healing: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        cloudwatch_configuration: typing.Optional[typing.Union["OpsworksStaticWebLayerCloudwatchConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        custom_configure_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
        custom_deploy_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
        custom_instance_profile_arn: typing.Optional[builtins.str] = None,
        custom_json: typing.Optional[builtins.str] = None,
        custom_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        custom_setup_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
        custom_shutdown_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
        custom_undeploy_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
        drain_elb_on_shutdown: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        ebs_volume: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["OpsworksStaticWebLayerEbsVolume", typing.Dict[builtins.str, typing.Any]]]]] = None,
        elastic_load_balancer: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        install_updates_on_boot: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        instance_shutdown_timeout: typing.Optional[jsii.Number] = None,
        load_based_auto_scaling: typing.Optional[typing.Union["OpsworksStaticWebLayerLoadBasedAutoScaling", typing.Dict[builtins.str, typing.Any]]] = None,
        name: typing.Optional[builtins.str] = None,
        system_packages: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        use_ebs_optimized_instances: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer aws_opsworks_static_web_layer} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param stack_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#stack_id OpsworksStaticWebLayer#stack_id}.
        :param auto_assign_elastic_ips: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#auto_assign_elastic_ips OpsworksStaticWebLayer#auto_assign_elastic_ips}.
        :param auto_assign_public_ips: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#auto_assign_public_ips OpsworksStaticWebLayer#auto_assign_public_ips}.
        :param auto_healing: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#auto_healing OpsworksStaticWebLayer#auto_healing}.
        :param cloudwatch_configuration: cloudwatch_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#cloudwatch_configuration OpsworksStaticWebLayer#cloudwatch_configuration}
        :param custom_configure_recipes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#custom_configure_recipes OpsworksStaticWebLayer#custom_configure_recipes}.
        :param custom_deploy_recipes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#custom_deploy_recipes OpsworksStaticWebLayer#custom_deploy_recipes}.
        :param custom_instance_profile_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#custom_instance_profile_arn OpsworksStaticWebLayer#custom_instance_profile_arn}.
        :param custom_json: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#custom_json OpsworksStaticWebLayer#custom_json}.
        :param custom_security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#custom_security_group_ids OpsworksStaticWebLayer#custom_security_group_ids}.
        :param custom_setup_recipes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#custom_setup_recipes OpsworksStaticWebLayer#custom_setup_recipes}.
        :param custom_shutdown_recipes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#custom_shutdown_recipes OpsworksStaticWebLayer#custom_shutdown_recipes}.
        :param custom_undeploy_recipes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#custom_undeploy_recipes OpsworksStaticWebLayer#custom_undeploy_recipes}.
        :param drain_elb_on_shutdown: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#drain_elb_on_shutdown OpsworksStaticWebLayer#drain_elb_on_shutdown}.
        :param ebs_volume: ebs_volume block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#ebs_volume OpsworksStaticWebLayer#ebs_volume}
        :param elastic_load_balancer: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#elastic_load_balancer OpsworksStaticWebLayer#elastic_load_balancer}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#id OpsworksStaticWebLayer#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param install_updates_on_boot: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#install_updates_on_boot OpsworksStaticWebLayer#install_updates_on_boot}.
        :param instance_shutdown_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#instance_shutdown_timeout OpsworksStaticWebLayer#instance_shutdown_timeout}.
        :param load_based_auto_scaling: load_based_auto_scaling block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#load_based_auto_scaling OpsworksStaticWebLayer#load_based_auto_scaling}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#name OpsworksStaticWebLayer#name}.
        :param system_packages: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#system_packages OpsworksStaticWebLayer#system_packages}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#tags OpsworksStaticWebLayer#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#tags_all OpsworksStaticWebLayer#tags_all}.
        :param use_ebs_optimized_instances: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#use_ebs_optimized_instances OpsworksStaticWebLayer#use_ebs_optimized_instances}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__34cd8e29790ce1a5a0a6511a74b1517321bf06023c318ebb058ed398e2ac4bd6)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = OpsworksStaticWebLayerConfig(
            stack_id=stack_id,
            auto_assign_elastic_ips=auto_assign_elastic_ips,
            auto_assign_public_ips=auto_assign_public_ips,
            auto_healing=auto_healing,
            cloudwatch_configuration=cloudwatch_configuration,
            custom_configure_recipes=custom_configure_recipes,
            custom_deploy_recipes=custom_deploy_recipes,
            custom_instance_profile_arn=custom_instance_profile_arn,
            custom_json=custom_json,
            custom_security_group_ids=custom_security_group_ids,
            custom_setup_recipes=custom_setup_recipes,
            custom_shutdown_recipes=custom_shutdown_recipes,
            custom_undeploy_recipes=custom_undeploy_recipes,
            drain_elb_on_shutdown=drain_elb_on_shutdown,
            ebs_volume=ebs_volume,
            elastic_load_balancer=elastic_load_balancer,
            id=id,
            install_updates_on_boot=install_updates_on_boot,
            instance_shutdown_timeout=instance_shutdown_timeout,
            load_based_auto_scaling=load_based_auto_scaling,
            name=name,
            system_packages=system_packages,
            tags=tags,
            tags_all=tags_all,
            use_ebs_optimized_instances=use_ebs_optimized_instances,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putCloudwatchConfiguration")
    def put_cloudwatch_configuration(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        log_streams: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["OpsworksStaticWebLayerCloudwatchConfigurationLogStreams", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#enabled OpsworksStaticWebLayer#enabled}.
        :param log_streams: log_streams block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#log_streams OpsworksStaticWebLayer#log_streams}
        '''
        value = OpsworksStaticWebLayerCloudwatchConfiguration(
            enabled=enabled, log_streams=log_streams
        )

        return typing.cast(None, jsii.invoke(self, "putCloudwatchConfiguration", [value]))

    @jsii.member(jsii_name="putEbsVolume")
    def put_ebs_volume(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["OpsworksStaticWebLayerEbsVolume", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1232f89f388d7bf75a8eb6a3985912fbc40b42bc09fa39ccdbf360fbbb0c56a0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putEbsVolume", [value]))

    @jsii.member(jsii_name="putLoadBasedAutoScaling")
    def put_load_based_auto_scaling(
        self,
        *,
        downscaling: typing.Optional[typing.Union["OpsworksStaticWebLayerLoadBasedAutoScalingDownscaling", typing.Dict[builtins.str, typing.Any]]] = None,
        enable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        upscaling: typing.Optional[typing.Union["OpsworksStaticWebLayerLoadBasedAutoScalingUpscaling", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param downscaling: downscaling block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#downscaling OpsworksStaticWebLayer#downscaling}
        :param enable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#enable OpsworksStaticWebLayer#enable}.
        :param upscaling: upscaling block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#upscaling OpsworksStaticWebLayer#upscaling}
        '''
        value = OpsworksStaticWebLayerLoadBasedAutoScaling(
            downscaling=downscaling, enable=enable, upscaling=upscaling
        )

        return typing.cast(None, jsii.invoke(self, "putLoadBasedAutoScaling", [value]))

    @jsii.member(jsii_name="resetAutoAssignElasticIps")
    def reset_auto_assign_elastic_ips(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoAssignElasticIps", []))

    @jsii.member(jsii_name="resetAutoAssignPublicIps")
    def reset_auto_assign_public_ips(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoAssignPublicIps", []))

    @jsii.member(jsii_name="resetAutoHealing")
    def reset_auto_healing(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoHealing", []))

    @jsii.member(jsii_name="resetCloudwatchConfiguration")
    def reset_cloudwatch_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudwatchConfiguration", []))

    @jsii.member(jsii_name="resetCustomConfigureRecipes")
    def reset_custom_configure_recipes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomConfigureRecipes", []))

    @jsii.member(jsii_name="resetCustomDeployRecipes")
    def reset_custom_deploy_recipes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomDeployRecipes", []))

    @jsii.member(jsii_name="resetCustomInstanceProfileArn")
    def reset_custom_instance_profile_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomInstanceProfileArn", []))

    @jsii.member(jsii_name="resetCustomJson")
    def reset_custom_json(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomJson", []))

    @jsii.member(jsii_name="resetCustomSecurityGroupIds")
    def reset_custom_security_group_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomSecurityGroupIds", []))

    @jsii.member(jsii_name="resetCustomSetupRecipes")
    def reset_custom_setup_recipes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomSetupRecipes", []))

    @jsii.member(jsii_name="resetCustomShutdownRecipes")
    def reset_custom_shutdown_recipes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomShutdownRecipes", []))

    @jsii.member(jsii_name="resetCustomUndeployRecipes")
    def reset_custom_undeploy_recipes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomUndeployRecipes", []))

    @jsii.member(jsii_name="resetDrainElbOnShutdown")
    def reset_drain_elb_on_shutdown(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDrainElbOnShutdown", []))

    @jsii.member(jsii_name="resetEbsVolume")
    def reset_ebs_volume(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEbsVolume", []))

    @jsii.member(jsii_name="resetElasticLoadBalancer")
    def reset_elastic_load_balancer(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetElasticLoadBalancer", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetInstallUpdatesOnBoot")
    def reset_install_updates_on_boot(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstallUpdatesOnBoot", []))

    @jsii.member(jsii_name="resetInstanceShutdownTimeout")
    def reset_instance_shutdown_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceShutdownTimeout", []))

    @jsii.member(jsii_name="resetLoadBasedAutoScaling")
    def reset_load_based_auto_scaling(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoadBasedAutoScaling", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetSystemPackages")
    def reset_system_packages(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSystemPackages", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetUseEbsOptimizedInstances")
    def reset_use_ebs_optimized_instances(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUseEbsOptimizedInstances", []))

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
    @jsii.member(jsii_name="cloudwatchConfiguration")
    def cloudwatch_configuration(
        self,
    ) -> "OpsworksStaticWebLayerCloudwatchConfigurationOutputReference":
        return typing.cast("OpsworksStaticWebLayerCloudwatchConfigurationOutputReference", jsii.get(self, "cloudwatchConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="ebsVolume")
    def ebs_volume(self) -> "OpsworksStaticWebLayerEbsVolumeList":
        return typing.cast("OpsworksStaticWebLayerEbsVolumeList", jsii.get(self, "ebsVolume"))

    @builtins.property
    @jsii.member(jsii_name="loadBasedAutoScaling")
    def load_based_auto_scaling(
        self,
    ) -> "OpsworksStaticWebLayerLoadBasedAutoScalingOutputReference":
        return typing.cast("OpsworksStaticWebLayerLoadBasedAutoScalingOutputReference", jsii.get(self, "loadBasedAutoScaling"))

    @builtins.property
    @jsii.member(jsii_name="autoAssignElasticIpsInput")
    def auto_assign_elastic_ips_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "autoAssignElasticIpsInput"))

    @builtins.property
    @jsii.member(jsii_name="autoAssignPublicIpsInput")
    def auto_assign_public_ips_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "autoAssignPublicIpsInput"))

    @builtins.property
    @jsii.member(jsii_name="autoHealingInput")
    def auto_healing_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "autoHealingInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchConfigurationInput")
    def cloudwatch_configuration_input(
        self,
    ) -> typing.Optional["OpsworksStaticWebLayerCloudwatchConfiguration"]:
        return typing.cast(typing.Optional["OpsworksStaticWebLayerCloudwatchConfiguration"], jsii.get(self, "cloudwatchConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="customConfigureRecipesInput")
    def custom_configure_recipes_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "customConfigureRecipesInput"))

    @builtins.property
    @jsii.member(jsii_name="customDeployRecipesInput")
    def custom_deploy_recipes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "customDeployRecipesInput"))

    @builtins.property
    @jsii.member(jsii_name="customInstanceProfileArnInput")
    def custom_instance_profile_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customInstanceProfileArnInput"))

    @builtins.property
    @jsii.member(jsii_name="customJsonInput")
    def custom_json_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customJsonInput"))

    @builtins.property
    @jsii.member(jsii_name="customSecurityGroupIdsInput")
    def custom_security_group_ids_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "customSecurityGroupIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="customSetupRecipesInput")
    def custom_setup_recipes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "customSetupRecipesInput"))

    @builtins.property
    @jsii.member(jsii_name="customShutdownRecipesInput")
    def custom_shutdown_recipes_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "customShutdownRecipesInput"))

    @builtins.property
    @jsii.member(jsii_name="customUndeployRecipesInput")
    def custom_undeploy_recipes_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "customUndeployRecipesInput"))

    @builtins.property
    @jsii.member(jsii_name="drainElbOnShutdownInput")
    def drain_elb_on_shutdown_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "drainElbOnShutdownInput"))

    @builtins.property
    @jsii.member(jsii_name="ebsVolumeInput")
    def ebs_volume_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["OpsworksStaticWebLayerEbsVolume"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["OpsworksStaticWebLayerEbsVolume"]]], jsii.get(self, "ebsVolumeInput"))

    @builtins.property
    @jsii.member(jsii_name="elasticLoadBalancerInput")
    def elastic_load_balancer_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "elasticLoadBalancerInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="installUpdatesOnBootInput")
    def install_updates_on_boot_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "installUpdatesOnBootInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceShutdownTimeoutInput")
    def instance_shutdown_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "instanceShutdownTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="loadBasedAutoScalingInput")
    def load_based_auto_scaling_input(
        self,
    ) -> typing.Optional["OpsworksStaticWebLayerLoadBasedAutoScaling"]:
        return typing.cast(typing.Optional["OpsworksStaticWebLayerLoadBasedAutoScaling"], jsii.get(self, "loadBasedAutoScalingInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="stackIdInput")
    def stack_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stackIdInput"))

    @builtins.property
    @jsii.member(jsii_name="systemPackagesInput")
    def system_packages_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "systemPackagesInput"))

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
    @jsii.member(jsii_name="useEbsOptimizedInstancesInput")
    def use_ebs_optimized_instances_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "useEbsOptimizedInstancesInput"))

    @builtins.property
    @jsii.member(jsii_name="autoAssignElasticIps")
    def auto_assign_elastic_ips(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "autoAssignElasticIps"))

    @auto_assign_elastic_ips.setter
    def auto_assign_elastic_ips(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0652d2d0fa7cd75e3a0a34eeab204e9297e0718340fb2f4f2b755ae852c23c7d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoAssignElasticIps", value)

    @builtins.property
    @jsii.member(jsii_name="autoAssignPublicIps")
    def auto_assign_public_ips(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "autoAssignPublicIps"))

    @auto_assign_public_ips.setter
    def auto_assign_public_ips(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc10888f550e4cd99390020b5d5403c7c4699461e1cb26637048ed695f1aa4be)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoAssignPublicIps", value)

    @builtins.property
    @jsii.member(jsii_name="autoHealing")
    def auto_healing(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "autoHealing"))

    @auto_healing.setter
    def auto_healing(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8602efc775cd9fcc5a5bbb845ce4e4444854eae180c96c89a926f88e8acb2d73)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoHealing", value)

    @builtins.property
    @jsii.member(jsii_name="customConfigureRecipes")
    def custom_configure_recipes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "customConfigureRecipes"))

    @custom_configure_recipes.setter
    def custom_configure_recipes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54326cdcfd29ba52f22babe0089f511bb395def474401782debb6e2974e21e1f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customConfigureRecipes", value)

    @builtins.property
    @jsii.member(jsii_name="customDeployRecipes")
    def custom_deploy_recipes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "customDeployRecipes"))

    @custom_deploy_recipes.setter
    def custom_deploy_recipes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91cc3062df1ca1343cd3b4f58f11eb34aec91ffee6adcbc8ac96569a8eb7f682)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customDeployRecipes", value)

    @builtins.property
    @jsii.member(jsii_name="customInstanceProfileArn")
    def custom_instance_profile_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customInstanceProfileArn"))

    @custom_instance_profile_arn.setter
    def custom_instance_profile_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ec808980b828c1b8c790d82cba282401bd4bdaaf75fe5eca7dcd35b7665af62)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customInstanceProfileArn", value)

    @builtins.property
    @jsii.member(jsii_name="customJson")
    def custom_json(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customJson"))

    @custom_json.setter
    def custom_json(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23ef6435fea9eb934c534d5fe118b25289aeaa4e26f06bc7fb3b8aa7c409572d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customJson", value)

    @builtins.property
    @jsii.member(jsii_name="customSecurityGroupIds")
    def custom_security_group_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "customSecurityGroupIds"))

    @custom_security_group_ids.setter
    def custom_security_group_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39f64750701e3df7b2b68b2bc6817af517892ef1483f0b79d579f12ad386b819)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customSecurityGroupIds", value)

    @builtins.property
    @jsii.member(jsii_name="customSetupRecipes")
    def custom_setup_recipes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "customSetupRecipes"))

    @custom_setup_recipes.setter
    def custom_setup_recipes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b0482ddef8c835458aece2e1ebc257f830ea9856a0df95907ace96e85c1b564)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customSetupRecipes", value)

    @builtins.property
    @jsii.member(jsii_name="customShutdownRecipes")
    def custom_shutdown_recipes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "customShutdownRecipes"))

    @custom_shutdown_recipes.setter
    def custom_shutdown_recipes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__37bff78a526fee41f2420546a18b3a8d2c557d4697764c1bd81cc5833fef4e88)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customShutdownRecipes", value)

    @builtins.property
    @jsii.member(jsii_name="customUndeployRecipes")
    def custom_undeploy_recipes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "customUndeployRecipes"))

    @custom_undeploy_recipes.setter
    def custom_undeploy_recipes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2356128ca1fafdf47ccbbac7a093da84b49bc2703d07ac85b77ae96884558073)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customUndeployRecipes", value)

    @builtins.property
    @jsii.member(jsii_name="drainElbOnShutdown")
    def drain_elb_on_shutdown(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "drainElbOnShutdown"))

    @drain_elb_on_shutdown.setter
    def drain_elb_on_shutdown(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fcd9ae1c7bbdca8ea118e61f88866371999e7d41eb036006ff976a55de393e64)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "drainElbOnShutdown", value)

    @builtins.property
    @jsii.member(jsii_name="elasticLoadBalancer")
    def elastic_load_balancer(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "elasticLoadBalancer"))

    @elastic_load_balancer.setter
    def elastic_load_balancer(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__480e13853a75d1a0a478c380c9bd0ffa393f911583f14550b83afe9a5935dda9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "elasticLoadBalancer", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d2355697ce0da89d1eeaa553a3ca97370026a905232cbbf05e3b7f7c1ae9170)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="installUpdatesOnBoot")
    def install_updates_on_boot(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "installUpdatesOnBoot"))

    @install_updates_on_boot.setter
    def install_updates_on_boot(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c2abf78e9b767f119ab8e422c7da91a14d6c172e31292e9c063fe51c570d0488)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "installUpdatesOnBoot", value)

    @builtins.property
    @jsii.member(jsii_name="instanceShutdownTimeout")
    def instance_shutdown_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "instanceShutdownTimeout"))

    @instance_shutdown_timeout.setter
    def instance_shutdown_timeout(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ce5d843927341eff70bfe711a5e4317b34d78d8bcb836283917eed621e028af)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceShutdownTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1596f97f98d93b646cdfb53f8523811416c1b83be85235dfdb65c47cbcbbec1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="stackId")
    def stack_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "stackId"))

    @stack_id.setter
    def stack_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d8ab20ef4ecd608e22113f5a57860a6e6aad557a6f6ed0fe33c696288610695)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stackId", value)

    @builtins.property
    @jsii.member(jsii_name="systemPackages")
    def system_packages(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "systemPackages"))

    @system_packages.setter
    def system_packages(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1dd75e8710062efc6fbd127511a6fb252cf9a3a326bb3ffa76c5f8a57d410e15)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "systemPackages", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__215556b174c331aeb47c7fd70d97beecc55ea0565ddc6fcc32d163c2f91bacbe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2cb2b05c51cb7c852549d9c7d0c378ed69bf2be2c9cf6d9d4d87931763106832)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)

    @builtins.property
    @jsii.member(jsii_name="useEbsOptimizedInstances")
    def use_ebs_optimized_instances(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "useEbsOptimizedInstances"))

    @use_ebs_optimized_instances.setter
    def use_ebs_optimized_instances(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f8dc5ad7775566841bf401de527ecbd5ea4d2ffe2d57075cb2487038951d148)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useEbsOptimizedInstances", value)


@jsii.data_type(
    jsii_type="aws.opsworksStaticWebLayer.OpsworksStaticWebLayerCloudwatchConfiguration",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "log_streams": "logStreams"},
)
class OpsworksStaticWebLayerCloudwatchConfiguration:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        log_streams: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["OpsworksStaticWebLayerCloudwatchConfigurationLogStreams", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#enabled OpsworksStaticWebLayer#enabled}.
        :param log_streams: log_streams block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#log_streams OpsworksStaticWebLayer#log_streams}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17398267f2aff499769822bb91ff03f24fc726b8b9af26ad87b581d5efd4306e)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument log_streams", value=log_streams, expected_type=type_hints["log_streams"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled
        if log_streams is not None:
            self._values["log_streams"] = log_streams

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#enabled OpsworksStaticWebLayer#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def log_streams(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["OpsworksStaticWebLayerCloudwatchConfigurationLogStreams"]]]:
        '''log_streams block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#log_streams OpsworksStaticWebLayer#log_streams}
        '''
        result = self._values.get("log_streams")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["OpsworksStaticWebLayerCloudwatchConfigurationLogStreams"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OpsworksStaticWebLayerCloudwatchConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.opsworksStaticWebLayer.OpsworksStaticWebLayerCloudwatchConfigurationLogStreams",
    jsii_struct_bases=[],
    name_mapping={
        "file": "file",
        "log_group_name": "logGroupName",
        "batch_count": "batchCount",
        "batch_size": "batchSize",
        "buffer_duration": "bufferDuration",
        "datetime_format": "datetimeFormat",
        "encoding": "encoding",
        "file_fingerprint_lines": "fileFingerprintLines",
        "initial_position": "initialPosition",
        "multiline_start_pattern": "multilineStartPattern",
        "time_zone": "timeZone",
    },
)
class OpsworksStaticWebLayerCloudwatchConfigurationLogStreams:
    def __init__(
        self,
        *,
        file: builtins.str,
        log_group_name: builtins.str,
        batch_count: typing.Optional[jsii.Number] = None,
        batch_size: typing.Optional[jsii.Number] = None,
        buffer_duration: typing.Optional[jsii.Number] = None,
        datetime_format: typing.Optional[builtins.str] = None,
        encoding: typing.Optional[builtins.str] = None,
        file_fingerprint_lines: typing.Optional[builtins.str] = None,
        initial_position: typing.Optional[builtins.str] = None,
        multiline_start_pattern: typing.Optional[builtins.str] = None,
        time_zone: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param file: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#file OpsworksStaticWebLayer#file}.
        :param log_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#log_group_name OpsworksStaticWebLayer#log_group_name}.
        :param batch_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#batch_count OpsworksStaticWebLayer#batch_count}.
        :param batch_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#batch_size OpsworksStaticWebLayer#batch_size}.
        :param buffer_duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#buffer_duration OpsworksStaticWebLayer#buffer_duration}.
        :param datetime_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#datetime_format OpsworksStaticWebLayer#datetime_format}.
        :param encoding: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#encoding OpsworksStaticWebLayer#encoding}.
        :param file_fingerprint_lines: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#file_fingerprint_lines OpsworksStaticWebLayer#file_fingerprint_lines}.
        :param initial_position: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#initial_position OpsworksStaticWebLayer#initial_position}.
        :param multiline_start_pattern: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#multiline_start_pattern OpsworksStaticWebLayer#multiline_start_pattern}.
        :param time_zone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#time_zone OpsworksStaticWebLayer#time_zone}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e148b7ddb3ca057a3fe3544d3f12cc965077862c51c67a908e0c3357a492dd8)
            check_type(argname="argument file", value=file, expected_type=type_hints["file"])
            check_type(argname="argument log_group_name", value=log_group_name, expected_type=type_hints["log_group_name"])
            check_type(argname="argument batch_count", value=batch_count, expected_type=type_hints["batch_count"])
            check_type(argname="argument batch_size", value=batch_size, expected_type=type_hints["batch_size"])
            check_type(argname="argument buffer_duration", value=buffer_duration, expected_type=type_hints["buffer_duration"])
            check_type(argname="argument datetime_format", value=datetime_format, expected_type=type_hints["datetime_format"])
            check_type(argname="argument encoding", value=encoding, expected_type=type_hints["encoding"])
            check_type(argname="argument file_fingerprint_lines", value=file_fingerprint_lines, expected_type=type_hints["file_fingerprint_lines"])
            check_type(argname="argument initial_position", value=initial_position, expected_type=type_hints["initial_position"])
            check_type(argname="argument multiline_start_pattern", value=multiline_start_pattern, expected_type=type_hints["multiline_start_pattern"])
            check_type(argname="argument time_zone", value=time_zone, expected_type=type_hints["time_zone"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "file": file,
            "log_group_name": log_group_name,
        }
        if batch_count is not None:
            self._values["batch_count"] = batch_count
        if batch_size is not None:
            self._values["batch_size"] = batch_size
        if buffer_duration is not None:
            self._values["buffer_duration"] = buffer_duration
        if datetime_format is not None:
            self._values["datetime_format"] = datetime_format
        if encoding is not None:
            self._values["encoding"] = encoding
        if file_fingerprint_lines is not None:
            self._values["file_fingerprint_lines"] = file_fingerprint_lines
        if initial_position is not None:
            self._values["initial_position"] = initial_position
        if multiline_start_pattern is not None:
            self._values["multiline_start_pattern"] = multiline_start_pattern
        if time_zone is not None:
            self._values["time_zone"] = time_zone

    @builtins.property
    def file(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#file OpsworksStaticWebLayer#file}.'''
        result = self._values.get("file")
        assert result is not None, "Required property 'file' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def log_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#log_group_name OpsworksStaticWebLayer#log_group_name}.'''
        result = self._values.get("log_group_name")
        assert result is not None, "Required property 'log_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def batch_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#batch_count OpsworksStaticWebLayer#batch_count}.'''
        result = self._values.get("batch_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def batch_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#batch_size OpsworksStaticWebLayer#batch_size}.'''
        result = self._values.get("batch_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def buffer_duration(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#buffer_duration OpsworksStaticWebLayer#buffer_duration}.'''
        result = self._values.get("buffer_duration")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def datetime_format(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#datetime_format OpsworksStaticWebLayer#datetime_format}.'''
        result = self._values.get("datetime_format")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encoding(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#encoding OpsworksStaticWebLayer#encoding}.'''
        result = self._values.get("encoding")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def file_fingerprint_lines(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#file_fingerprint_lines OpsworksStaticWebLayer#file_fingerprint_lines}.'''
        result = self._values.get("file_fingerprint_lines")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def initial_position(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#initial_position OpsworksStaticWebLayer#initial_position}.'''
        result = self._values.get("initial_position")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def multiline_start_pattern(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#multiline_start_pattern OpsworksStaticWebLayer#multiline_start_pattern}.'''
        result = self._values.get("multiline_start_pattern")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def time_zone(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#time_zone OpsworksStaticWebLayer#time_zone}.'''
        result = self._values.get("time_zone")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OpsworksStaticWebLayerCloudwatchConfigurationLogStreams(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OpsworksStaticWebLayerCloudwatchConfigurationLogStreamsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.opsworksStaticWebLayer.OpsworksStaticWebLayerCloudwatchConfigurationLogStreamsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ad1a49fa6949db3e9bbfdc7f9b0ca12a1735a5e1a84662f86e3a00f251275666)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "OpsworksStaticWebLayerCloudwatchConfigurationLogStreamsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bda01e22d1c99fbff386b7dd5c978479d8b58734fd30508b3eaa9c9ce486ecec)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("OpsworksStaticWebLayerCloudwatchConfigurationLogStreamsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__47c1b5c57ee6d6bddc46972539e2a94ce90b9650c1e30418785fcf27dd516121)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d0170f45823a50b1931500d6e0f7d7c1e1b03fcb6f600ba5212ebee3cb42425d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ec3a2c190ef51c74eca300db0818ff59e1b98c8a31374875e52a9e23aeb7e21f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[OpsworksStaticWebLayerCloudwatchConfigurationLogStreams]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[OpsworksStaticWebLayerCloudwatchConfigurationLogStreams]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[OpsworksStaticWebLayerCloudwatchConfigurationLogStreams]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7801125daea46bb8eb9667ff76fa6bf9acb2d502eeca99cede40be3f93813994)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OpsworksStaticWebLayerCloudwatchConfigurationLogStreamsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.opsworksStaticWebLayer.OpsworksStaticWebLayerCloudwatchConfigurationLogStreamsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a3dd965c06a72c7b287a41f59d5444b2e4b5a788f4caa408a037871139c22771)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetBatchCount")
    def reset_batch_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBatchCount", []))

    @jsii.member(jsii_name="resetBatchSize")
    def reset_batch_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBatchSize", []))

    @jsii.member(jsii_name="resetBufferDuration")
    def reset_buffer_duration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBufferDuration", []))

    @jsii.member(jsii_name="resetDatetimeFormat")
    def reset_datetime_format(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatetimeFormat", []))

    @jsii.member(jsii_name="resetEncoding")
    def reset_encoding(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncoding", []))

    @jsii.member(jsii_name="resetFileFingerprintLines")
    def reset_file_fingerprint_lines(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFileFingerprintLines", []))

    @jsii.member(jsii_name="resetInitialPosition")
    def reset_initial_position(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInitialPosition", []))

    @jsii.member(jsii_name="resetMultilineStartPattern")
    def reset_multiline_start_pattern(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMultilineStartPattern", []))

    @jsii.member(jsii_name="resetTimeZone")
    def reset_time_zone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeZone", []))

    @builtins.property
    @jsii.member(jsii_name="batchCountInput")
    def batch_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "batchCountInput"))

    @builtins.property
    @jsii.member(jsii_name="batchSizeInput")
    def batch_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "batchSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="bufferDurationInput")
    def buffer_duration_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "bufferDurationInput"))

    @builtins.property
    @jsii.member(jsii_name="datetimeFormatInput")
    def datetime_format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datetimeFormatInput"))

    @builtins.property
    @jsii.member(jsii_name="encodingInput")
    def encoding_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "encodingInput"))

    @builtins.property
    @jsii.member(jsii_name="fileFingerprintLinesInput")
    def file_fingerprint_lines_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fileFingerprintLinesInput"))

    @builtins.property
    @jsii.member(jsii_name="fileInput")
    def file_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fileInput"))

    @builtins.property
    @jsii.member(jsii_name="initialPositionInput")
    def initial_position_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "initialPositionInput"))

    @builtins.property
    @jsii.member(jsii_name="logGroupNameInput")
    def log_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="multilineStartPatternInput")
    def multiline_start_pattern_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "multilineStartPatternInput"))

    @builtins.property
    @jsii.member(jsii_name="timeZoneInput")
    def time_zone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timeZoneInput"))

    @builtins.property
    @jsii.member(jsii_name="batchCount")
    def batch_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "batchCount"))

    @batch_count.setter
    def batch_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6844b2c983719d23a9620bcb70c6fc7aa19a6e6b45fdd4950ae11436b840e8b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "batchCount", value)

    @builtins.property
    @jsii.member(jsii_name="batchSize")
    def batch_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "batchSize"))

    @batch_size.setter
    def batch_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed72fcc77cfb946db2ae187ef7b1c5cfb6f6f19a7b13a72b91bf0ee6d2faebc5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "batchSize", value)

    @builtins.property
    @jsii.member(jsii_name="bufferDuration")
    def buffer_duration(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "bufferDuration"))

    @buffer_duration.setter
    def buffer_duration(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c560849f55e6a08cc4b76d407805192d615f9b2c87c6e6e0194b8878f71787c8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bufferDuration", value)

    @builtins.property
    @jsii.member(jsii_name="datetimeFormat")
    def datetime_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datetimeFormat"))

    @datetime_format.setter
    def datetime_format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c7e2a7ea37276c896a5eaf009372dc93caa0a8b6ec3d789f929c504244a47e3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datetimeFormat", value)

    @builtins.property
    @jsii.member(jsii_name="encoding")
    def encoding(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "encoding"))

    @encoding.setter
    def encoding(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dcfd6de257661ff11769fe1fc75429489b5781f6fecf8c6636d01feb86de9242)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encoding", value)

    @builtins.property
    @jsii.member(jsii_name="file")
    def file(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "file"))

    @file.setter
    def file(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__843d1e272cc18f2972217766387cd35c75c166df7dedccc68cb375e130cb59b9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "file", value)

    @builtins.property
    @jsii.member(jsii_name="fileFingerprintLines")
    def file_fingerprint_lines(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fileFingerprintLines"))

    @file_fingerprint_lines.setter
    def file_fingerprint_lines(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e306219d72012de7eafcb7e948f21d88b2dd72c6bac42c73800bd20cd316685)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileFingerprintLines", value)

    @builtins.property
    @jsii.member(jsii_name="initialPosition")
    def initial_position(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "initialPosition"))

    @initial_position.setter
    def initial_position(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0e1583dd9f1b5340e47f4ab9e0541006528abd3a5d7d12c8c20fd51d1bff7c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "initialPosition", value)

    @builtins.property
    @jsii.member(jsii_name="logGroupName")
    def log_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logGroupName"))

    @log_group_name.setter
    def log_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3590e4a5ed85592afe9be4955a7a3fd3783ec85d000c5001891d087d1cae22f6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="multilineStartPattern")
    def multiline_start_pattern(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "multilineStartPattern"))

    @multiline_start_pattern.setter
    def multiline_start_pattern(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97ce6945d1c0b3336a53e8d9f5534e25bb4126537b36c9764e47b0ea9b57a68c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "multilineStartPattern", value)

    @builtins.property
    @jsii.member(jsii_name="timeZone")
    def time_zone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timeZone"))

    @time_zone.setter
    def time_zone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c90edd693fb8940e9372abb2508d3e820a7f246a47a3b15601253cd1ec339af9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeZone", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[OpsworksStaticWebLayerCloudwatchConfigurationLogStreams, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[OpsworksStaticWebLayerCloudwatchConfigurationLogStreams, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[OpsworksStaticWebLayerCloudwatchConfigurationLogStreams, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5e1eeea204c3197ecbfe2cc4a36e7889c25268868461a8e5683b2353fb29ee5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OpsworksStaticWebLayerCloudwatchConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.opsworksStaticWebLayer.OpsworksStaticWebLayerCloudwatchConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__40e4972f02b88f2c5be148f751265f1487ca015fc32510ce86abda49984cec09)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putLogStreams")
    def put_log_streams(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[OpsworksStaticWebLayerCloudwatchConfigurationLogStreams, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9993903d16ba22f3ece6470cb3af96fc085c281931dbb4c8d13d127fc8ec225d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLogStreams", [value]))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetLogStreams")
    def reset_log_streams(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogStreams", []))

    @builtins.property
    @jsii.member(jsii_name="logStreams")
    def log_streams(
        self,
    ) -> OpsworksStaticWebLayerCloudwatchConfigurationLogStreamsList:
        return typing.cast(OpsworksStaticWebLayerCloudwatchConfigurationLogStreamsList, jsii.get(self, "logStreams"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="logStreamsInput")
    def log_streams_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[OpsworksStaticWebLayerCloudwatchConfigurationLogStreams]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[OpsworksStaticWebLayerCloudwatchConfigurationLogStreams]]], jsii.get(self, "logStreamsInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__68570b2b1e55852af7c4b3ae4902d5e9365d31dcd6ca5fed41a5af0d31ccdc56)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[OpsworksStaticWebLayerCloudwatchConfiguration]:
        return typing.cast(typing.Optional[OpsworksStaticWebLayerCloudwatchConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OpsworksStaticWebLayerCloudwatchConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2bbe3503fb7d2f5d01c2ee6a704c0683c10973904eebcf146786003762864896)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.opsworksStaticWebLayer.OpsworksStaticWebLayerConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "stack_id": "stackId",
        "auto_assign_elastic_ips": "autoAssignElasticIps",
        "auto_assign_public_ips": "autoAssignPublicIps",
        "auto_healing": "autoHealing",
        "cloudwatch_configuration": "cloudwatchConfiguration",
        "custom_configure_recipes": "customConfigureRecipes",
        "custom_deploy_recipes": "customDeployRecipes",
        "custom_instance_profile_arn": "customInstanceProfileArn",
        "custom_json": "customJson",
        "custom_security_group_ids": "customSecurityGroupIds",
        "custom_setup_recipes": "customSetupRecipes",
        "custom_shutdown_recipes": "customShutdownRecipes",
        "custom_undeploy_recipes": "customUndeployRecipes",
        "drain_elb_on_shutdown": "drainElbOnShutdown",
        "ebs_volume": "ebsVolume",
        "elastic_load_balancer": "elasticLoadBalancer",
        "id": "id",
        "install_updates_on_boot": "installUpdatesOnBoot",
        "instance_shutdown_timeout": "instanceShutdownTimeout",
        "load_based_auto_scaling": "loadBasedAutoScaling",
        "name": "name",
        "system_packages": "systemPackages",
        "tags": "tags",
        "tags_all": "tagsAll",
        "use_ebs_optimized_instances": "useEbsOptimizedInstances",
    },
)
class OpsworksStaticWebLayerConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        stack_id: builtins.str,
        auto_assign_elastic_ips: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        auto_assign_public_ips: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        auto_healing: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        cloudwatch_configuration: typing.Optional[typing.Union[OpsworksStaticWebLayerCloudwatchConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
        custom_configure_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
        custom_deploy_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
        custom_instance_profile_arn: typing.Optional[builtins.str] = None,
        custom_json: typing.Optional[builtins.str] = None,
        custom_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        custom_setup_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
        custom_shutdown_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
        custom_undeploy_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
        drain_elb_on_shutdown: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        ebs_volume: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["OpsworksStaticWebLayerEbsVolume", typing.Dict[builtins.str, typing.Any]]]]] = None,
        elastic_load_balancer: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        install_updates_on_boot: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        instance_shutdown_timeout: typing.Optional[jsii.Number] = None,
        load_based_auto_scaling: typing.Optional[typing.Union["OpsworksStaticWebLayerLoadBasedAutoScaling", typing.Dict[builtins.str, typing.Any]]] = None,
        name: typing.Optional[builtins.str] = None,
        system_packages: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        use_ebs_optimized_instances: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param stack_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#stack_id OpsworksStaticWebLayer#stack_id}.
        :param auto_assign_elastic_ips: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#auto_assign_elastic_ips OpsworksStaticWebLayer#auto_assign_elastic_ips}.
        :param auto_assign_public_ips: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#auto_assign_public_ips OpsworksStaticWebLayer#auto_assign_public_ips}.
        :param auto_healing: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#auto_healing OpsworksStaticWebLayer#auto_healing}.
        :param cloudwatch_configuration: cloudwatch_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#cloudwatch_configuration OpsworksStaticWebLayer#cloudwatch_configuration}
        :param custom_configure_recipes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#custom_configure_recipes OpsworksStaticWebLayer#custom_configure_recipes}.
        :param custom_deploy_recipes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#custom_deploy_recipes OpsworksStaticWebLayer#custom_deploy_recipes}.
        :param custom_instance_profile_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#custom_instance_profile_arn OpsworksStaticWebLayer#custom_instance_profile_arn}.
        :param custom_json: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#custom_json OpsworksStaticWebLayer#custom_json}.
        :param custom_security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#custom_security_group_ids OpsworksStaticWebLayer#custom_security_group_ids}.
        :param custom_setup_recipes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#custom_setup_recipes OpsworksStaticWebLayer#custom_setup_recipes}.
        :param custom_shutdown_recipes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#custom_shutdown_recipes OpsworksStaticWebLayer#custom_shutdown_recipes}.
        :param custom_undeploy_recipes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#custom_undeploy_recipes OpsworksStaticWebLayer#custom_undeploy_recipes}.
        :param drain_elb_on_shutdown: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#drain_elb_on_shutdown OpsworksStaticWebLayer#drain_elb_on_shutdown}.
        :param ebs_volume: ebs_volume block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#ebs_volume OpsworksStaticWebLayer#ebs_volume}
        :param elastic_load_balancer: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#elastic_load_balancer OpsworksStaticWebLayer#elastic_load_balancer}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#id OpsworksStaticWebLayer#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param install_updates_on_boot: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#install_updates_on_boot OpsworksStaticWebLayer#install_updates_on_boot}.
        :param instance_shutdown_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#instance_shutdown_timeout OpsworksStaticWebLayer#instance_shutdown_timeout}.
        :param load_based_auto_scaling: load_based_auto_scaling block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#load_based_auto_scaling OpsworksStaticWebLayer#load_based_auto_scaling}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#name OpsworksStaticWebLayer#name}.
        :param system_packages: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#system_packages OpsworksStaticWebLayer#system_packages}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#tags OpsworksStaticWebLayer#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#tags_all OpsworksStaticWebLayer#tags_all}.
        :param use_ebs_optimized_instances: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#use_ebs_optimized_instances OpsworksStaticWebLayer#use_ebs_optimized_instances}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(cloudwatch_configuration, dict):
            cloudwatch_configuration = OpsworksStaticWebLayerCloudwatchConfiguration(**cloudwatch_configuration)
        if isinstance(load_based_auto_scaling, dict):
            load_based_auto_scaling = OpsworksStaticWebLayerLoadBasedAutoScaling(**load_based_auto_scaling)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab3a39e768a56bc9f2af522d6899df999969b8cfad86dc5e13a8964c8babd719)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument stack_id", value=stack_id, expected_type=type_hints["stack_id"])
            check_type(argname="argument auto_assign_elastic_ips", value=auto_assign_elastic_ips, expected_type=type_hints["auto_assign_elastic_ips"])
            check_type(argname="argument auto_assign_public_ips", value=auto_assign_public_ips, expected_type=type_hints["auto_assign_public_ips"])
            check_type(argname="argument auto_healing", value=auto_healing, expected_type=type_hints["auto_healing"])
            check_type(argname="argument cloudwatch_configuration", value=cloudwatch_configuration, expected_type=type_hints["cloudwatch_configuration"])
            check_type(argname="argument custom_configure_recipes", value=custom_configure_recipes, expected_type=type_hints["custom_configure_recipes"])
            check_type(argname="argument custom_deploy_recipes", value=custom_deploy_recipes, expected_type=type_hints["custom_deploy_recipes"])
            check_type(argname="argument custom_instance_profile_arn", value=custom_instance_profile_arn, expected_type=type_hints["custom_instance_profile_arn"])
            check_type(argname="argument custom_json", value=custom_json, expected_type=type_hints["custom_json"])
            check_type(argname="argument custom_security_group_ids", value=custom_security_group_ids, expected_type=type_hints["custom_security_group_ids"])
            check_type(argname="argument custom_setup_recipes", value=custom_setup_recipes, expected_type=type_hints["custom_setup_recipes"])
            check_type(argname="argument custom_shutdown_recipes", value=custom_shutdown_recipes, expected_type=type_hints["custom_shutdown_recipes"])
            check_type(argname="argument custom_undeploy_recipes", value=custom_undeploy_recipes, expected_type=type_hints["custom_undeploy_recipes"])
            check_type(argname="argument drain_elb_on_shutdown", value=drain_elb_on_shutdown, expected_type=type_hints["drain_elb_on_shutdown"])
            check_type(argname="argument ebs_volume", value=ebs_volume, expected_type=type_hints["ebs_volume"])
            check_type(argname="argument elastic_load_balancer", value=elastic_load_balancer, expected_type=type_hints["elastic_load_balancer"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument install_updates_on_boot", value=install_updates_on_boot, expected_type=type_hints["install_updates_on_boot"])
            check_type(argname="argument instance_shutdown_timeout", value=instance_shutdown_timeout, expected_type=type_hints["instance_shutdown_timeout"])
            check_type(argname="argument load_based_auto_scaling", value=load_based_auto_scaling, expected_type=type_hints["load_based_auto_scaling"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument system_packages", value=system_packages, expected_type=type_hints["system_packages"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument use_ebs_optimized_instances", value=use_ebs_optimized_instances, expected_type=type_hints["use_ebs_optimized_instances"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "stack_id": stack_id,
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
        if auto_assign_elastic_ips is not None:
            self._values["auto_assign_elastic_ips"] = auto_assign_elastic_ips
        if auto_assign_public_ips is not None:
            self._values["auto_assign_public_ips"] = auto_assign_public_ips
        if auto_healing is not None:
            self._values["auto_healing"] = auto_healing
        if cloudwatch_configuration is not None:
            self._values["cloudwatch_configuration"] = cloudwatch_configuration
        if custom_configure_recipes is not None:
            self._values["custom_configure_recipes"] = custom_configure_recipes
        if custom_deploy_recipes is not None:
            self._values["custom_deploy_recipes"] = custom_deploy_recipes
        if custom_instance_profile_arn is not None:
            self._values["custom_instance_profile_arn"] = custom_instance_profile_arn
        if custom_json is not None:
            self._values["custom_json"] = custom_json
        if custom_security_group_ids is not None:
            self._values["custom_security_group_ids"] = custom_security_group_ids
        if custom_setup_recipes is not None:
            self._values["custom_setup_recipes"] = custom_setup_recipes
        if custom_shutdown_recipes is not None:
            self._values["custom_shutdown_recipes"] = custom_shutdown_recipes
        if custom_undeploy_recipes is not None:
            self._values["custom_undeploy_recipes"] = custom_undeploy_recipes
        if drain_elb_on_shutdown is not None:
            self._values["drain_elb_on_shutdown"] = drain_elb_on_shutdown
        if ebs_volume is not None:
            self._values["ebs_volume"] = ebs_volume
        if elastic_load_balancer is not None:
            self._values["elastic_load_balancer"] = elastic_load_balancer
        if id is not None:
            self._values["id"] = id
        if install_updates_on_boot is not None:
            self._values["install_updates_on_boot"] = install_updates_on_boot
        if instance_shutdown_timeout is not None:
            self._values["instance_shutdown_timeout"] = instance_shutdown_timeout
        if load_based_auto_scaling is not None:
            self._values["load_based_auto_scaling"] = load_based_auto_scaling
        if name is not None:
            self._values["name"] = name
        if system_packages is not None:
            self._values["system_packages"] = system_packages
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if use_ebs_optimized_instances is not None:
            self._values["use_ebs_optimized_instances"] = use_ebs_optimized_instances

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
    def stack_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#stack_id OpsworksStaticWebLayer#stack_id}.'''
        result = self._values.get("stack_id")
        assert result is not None, "Required property 'stack_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def auto_assign_elastic_ips(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#auto_assign_elastic_ips OpsworksStaticWebLayer#auto_assign_elastic_ips}.'''
        result = self._values.get("auto_assign_elastic_ips")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def auto_assign_public_ips(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#auto_assign_public_ips OpsworksStaticWebLayer#auto_assign_public_ips}.'''
        result = self._values.get("auto_assign_public_ips")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def auto_healing(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#auto_healing OpsworksStaticWebLayer#auto_healing}.'''
        result = self._values.get("auto_healing")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def cloudwatch_configuration(
        self,
    ) -> typing.Optional[OpsworksStaticWebLayerCloudwatchConfiguration]:
        '''cloudwatch_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#cloudwatch_configuration OpsworksStaticWebLayer#cloudwatch_configuration}
        '''
        result = self._values.get("cloudwatch_configuration")
        return typing.cast(typing.Optional[OpsworksStaticWebLayerCloudwatchConfiguration], result)

    @builtins.property
    def custom_configure_recipes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#custom_configure_recipes OpsworksStaticWebLayer#custom_configure_recipes}.'''
        result = self._values.get("custom_configure_recipes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def custom_deploy_recipes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#custom_deploy_recipes OpsworksStaticWebLayer#custom_deploy_recipes}.'''
        result = self._values.get("custom_deploy_recipes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def custom_instance_profile_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#custom_instance_profile_arn OpsworksStaticWebLayer#custom_instance_profile_arn}.'''
        result = self._values.get("custom_instance_profile_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_json(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#custom_json OpsworksStaticWebLayer#custom_json}.'''
        result = self._values.get("custom_json")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#custom_security_group_ids OpsworksStaticWebLayer#custom_security_group_ids}.'''
        result = self._values.get("custom_security_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def custom_setup_recipes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#custom_setup_recipes OpsworksStaticWebLayer#custom_setup_recipes}.'''
        result = self._values.get("custom_setup_recipes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def custom_shutdown_recipes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#custom_shutdown_recipes OpsworksStaticWebLayer#custom_shutdown_recipes}.'''
        result = self._values.get("custom_shutdown_recipes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def custom_undeploy_recipes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#custom_undeploy_recipes OpsworksStaticWebLayer#custom_undeploy_recipes}.'''
        result = self._values.get("custom_undeploy_recipes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def drain_elb_on_shutdown(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#drain_elb_on_shutdown OpsworksStaticWebLayer#drain_elb_on_shutdown}.'''
        result = self._values.get("drain_elb_on_shutdown")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def ebs_volume(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["OpsworksStaticWebLayerEbsVolume"]]]:
        '''ebs_volume block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#ebs_volume OpsworksStaticWebLayer#ebs_volume}
        '''
        result = self._values.get("ebs_volume")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["OpsworksStaticWebLayerEbsVolume"]]], result)

    @builtins.property
    def elastic_load_balancer(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#elastic_load_balancer OpsworksStaticWebLayer#elastic_load_balancer}.'''
        result = self._values.get("elastic_load_balancer")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#id OpsworksStaticWebLayer#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def install_updates_on_boot(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#install_updates_on_boot OpsworksStaticWebLayer#install_updates_on_boot}.'''
        result = self._values.get("install_updates_on_boot")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def instance_shutdown_timeout(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#instance_shutdown_timeout OpsworksStaticWebLayer#instance_shutdown_timeout}.'''
        result = self._values.get("instance_shutdown_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def load_based_auto_scaling(
        self,
    ) -> typing.Optional["OpsworksStaticWebLayerLoadBasedAutoScaling"]:
        '''load_based_auto_scaling block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#load_based_auto_scaling OpsworksStaticWebLayer#load_based_auto_scaling}
        '''
        result = self._values.get("load_based_auto_scaling")
        return typing.cast(typing.Optional["OpsworksStaticWebLayerLoadBasedAutoScaling"], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#name OpsworksStaticWebLayer#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def system_packages(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#system_packages OpsworksStaticWebLayer#system_packages}.'''
        result = self._values.get("system_packages")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#tags OpsworksStaticWebLayer#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#tags_all OpsworksStaticWebLayer#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def use_ebs_optimized_instances(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#use_ebs_optimized_instances OpsworksStaticWebLayer#use_ebs_optimized_instances}.'''
        result = self._values.get("use_ebs_optimized_instances")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OpsworksStaticWebLayerConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.opsworksStaticWebLayer.OpsworksStaticWebLayerEbsVolume",
    jsii_struct_bases=[],
    name_mapping={
        "mount_point": "mountPoint",
        "number_of_disks": "numberOfDisks",
        "size": "size",
        "encrypted": "encrypted",
        "iops": "iops",
        "raid_level": "raidLevel",
        "type": "type",
    },
)
class OpsworksStaticWebLayerEbsVolume:
    def __init__(
        self,
        *,
        mount_point: builtins.str,
        number_of_disks: jsii.Number,
        size: jsii.Number,
        encrypted: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        iops: typing.Optional[jsii.Number] = None,
        raid_level: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param mount_point: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#mount_point OpsworksStaticWebLayer#mount_point}.
        :param number_of_disks: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#number_of_disks OpsworksStaticWebLayer#number_of_disks}.
        :param size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#size OpsworksStaticWebLayer#size}.
        :param encrypted: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#encrypted OpsworksStaticWebLayer#encrypted}.
        :param iops: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#iops OpsworksStaticWebLayer#iops}.
        :param raid_level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#raid_level OpsworksStaticWebLayer#raid_level}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#type OpsworksStaticWebLayer#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf310fd7162d4d95a6f53e11d92138b2bcb802e02794aee8f8942d0a9feb6808)
            check_type(argname="argument mount_point", value=mount_point, expected_type=type_hints["mount_point"])
            check_type(argname="argument number_of_disks", value=number_of_disks, expected_type=type_hints["number_of_disks"])
            check_type(argname="argument size", value=size, expected_type=type_hints["size"])
            check_type(argname="argument encrypted", value=encrypted, expected_type=type_hints["encrypted"])
            check_type(argname="argument iops", value=iops, expected_type=type_hints["iops"])
            check_type(argname="argument raid_level", value=raid_level, expected_type=type_hints["raid_level"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "mount_point": mount_point,
            "number_of_disks": number_of_disks,
            "size": size,
        }
        if encrypted is not None:
            self._values["encrypted"] = encrypted
        if iops is not None:
            self._values["iops"] = iops
        if raid_level is not None:
            self._values["raid_level"] = raid_level
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def mount_point(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#mount_point OpsworksStaticWebLayer#mount_point}.'''
        result = self._values.get("mount_point")
        assert result is not None, "Required property 'mount_point' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def number_of_disks(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#number_of_disks OpsworksStaticWebLayer#number_of_disks}.'''
        result = self._values.get("number_of_disks")
        assert result is not None, "Required property 'number_of_disks' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def size(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#size OpsworksStaticWebLayer#size}.'''
        result = self._values.get("size")
        assert result is not None, "Required property 'size' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def encrypted(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#encrypted OpsworksStaticWebLayer#encrypted}.'''
        result = self._values.get("encrypted")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def iops(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#iops OpsworksStaticWebLayer#iops}.'''
        result = self._values.get("iops")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def raid_level(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#raid_level OpsworksStaticWebLayer#raid_level}.'''
        result = self._values.get("raid_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#type OpsworksStaticWebLayer#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OpsworksStaticWebLayerEbsVolume(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OpsworksStaticWebLayerEbsVolumeList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.opsworksStaticWebLayer.OpsworksStaticWebLayerEbsVolumeList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9172885f3ed43db4fa8992ac2a7a3c4528744ca0e43af95e7f4c7a861e1b3044)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "OpsworksStaticWebLayerEbsVolumeOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c7d34a08c5a608c8b3f7e44ddbc347efe4593138be0c233e40576b3ab63020b)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("OpsworksStaticWebLayerEbsVolumeOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e1827f3d07fbd3eeaaf9b713e4cc12e04b2139e2572fbcc70dc60446f3d6ade)
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
            type_hints = typing.get_type_hints(_typecheckingstub__722b345f6e7b25f0ef245df80756ea95b054a7c26735b70ad511154a49e9939e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0559de6122641c0ba05f73a17228a6ceaca8ce3427c0dcca4cbc739e0970c79a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[OpsworksStaticWebLayerEbsVolume]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[OpsworksStaticWebLayerEbsVolume]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[OpsworksStaticWebLayerEbsVolume]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__36acceac66bb1f6ba48fbe52175352409abb9d193a7b985dd853c931ac2e26ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OpsworksStaticWebLayerEbsVolumeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.opsworksStaticWebLayer.OpsworksStaticWebLayerEbsVolumeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e24f88e777d15820a820ba9ff20b261ec8be623ebaba776af5e53ebd4a540f88)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetEncrypted")
    def reset_encrypted(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncrypted", []))

    @jsii.member(jsii_name="resetIops")
    def reset_iops(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIops", []))

    @jsii.member(jsii_name="resetRaidLevel")
    def reset_raid_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRaidLevel", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

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
    @jsii.member(jsii_name="mountPointInput")
    def mount_point_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mountPointInput"))

    @builtins.property
    @jsii.member(jsii_name="numberOfDisksInput")
    def number_of_disks_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "numberOfDisksInput"))

    @builtins.property
    @jsii.member(jsii_name="raidLevelInput")
    def raid_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "raidLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="sizeInput")
    def size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sizeInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__662c4fe69ff9025c6435230e704dfb3a44853f56034b45a14ff0c07e0de36184)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encrypted", value)

    @builtins.property
    @jsii.member(jsii_name="iops")
    def iops(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "iops"))

    @iops.setter
    def iops(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6894a7779ae266baec6ff87ef3cb47c117c5c675aa7b9b343464bd1a8aa0a49d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iops", value)

    @builtins.property
    @jsii.member(jsii_name="mountPoint")
    def mount_point(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mountPoint"))

    @mount_point.setter
    def mount_point(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97531942695dcfd6e2a62ad0cd1105135e6a667a20eb58a2e9ae007f8a98c993)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mountPoint", value)

    @builtins.property
    @jsii.member(jsii_name="numberOfDisks")
    def number_of_disks(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "numberOfDisks"))

    @number_of_disks.setter
    def number_of_disks(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40a5dd0a92903649fd746e0bccdee609da085894172e042950b5364c090c85b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "numberOfDisks", value)

    @builtins.property
    @jsii.member(jsii_name="raidLevel")
    def raid_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "raidLevel"))

    @raid_level.setter
    def raid_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ee62404c6e3375fbeb1909dc7368f9502091b332d05f975f40de7ec4f51cde1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "raidLevel", value)

    @builtins.property
    @jsii.member(jsii_name="size")
    def size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "size"))

    @size.setter
    def size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15fe00b3a21521771138d531ff08e8177a4d978d917da155fff0b3fd2a8f2cdb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "size", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6619d87db0358f8d49d4d5ec9259592c90cdad0b7bd762a00d637a75d0243c70)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[OpsworksStaticWebLayerEbsVolume, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[OpsworksStaticWebLayerEbsVolume, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[OpsworksStaticWebLayerEbsVolume, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af57f1d8e71a73fca498e655104499d38b35be4c4a233817f7ccc7d4eb2f2a32)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.opsworksStaticWebLayer.OpsworksStaticWebLayerLoadBasedAutoScaling",
    jsii_struct_bases=[],
    name_mapping={
        "downscaling": "downscaling",
        "enable": "enable",
        "upscaling": "upscaling",
    },
)
class OpsworksStaticWebLayerLoadBasedAutoScaling:
    def __init__(
        self,
        *,
        downscaling: typing.Optional[typing.Union["OpsworksStaticWebLayerLoadBasedAutoScalingDownscaling", typing.Dict[builtins.str, typing.Any]]] = None,
        enable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        upscaling: typing.Optional[typing.Union["OpsworksStaticWebLayerLoadBasedAutoScalingUpscaling", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param downscaling: downscaling block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#downscaling OpsworksStaticWebLayer#downscaling}
        :param enable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#enable OpsworksStaticWebLayer#enable}.
        :param upscaling: upscaling block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#upscaling OpsworksStaticWebLayer#upscaling}
        '''
        if isinstance(downscaling, dict):
            downscaling = OpsworksStaticWebLayerLoadBasedAutoScalingDownscaling(**downscaling)
        if isinstance(upscaling, dict):
            upscaling = OpsworksStaticWebLayerLoadBasedAutoScalingUpscaling(**upscaling)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f96aa322c083e10f4dcbed0267223a14d8b5ba8702341a3dee3516808c30dfc)
            check_type(argname="argument downscaling", value=downscaling, expected_type=type_hints["downscaling"])
            check_type(argname="argument enable", value=enable, expected_type=type_hints["enable"])
            check_type(argname="argument upscaling", value=upscaling, expected_type=type_hints["upscaling"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if downscaling is not None:
            self._values["downscaling"] = downscaling
        if enable is not None:
            self._values["enable"] = enable
        if upscaling is not None:
            self._values["upscaling"] = upscaling

    @builtins.property
    def downscaling(
        self,
    ) -> typing.Optional["OpsworksStaticWebLayerLoadBasedAutoScalingDownscaling"]:
        '''downscaling block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#downscaling OpsworksStaticWebLayer#downscaling}
        '''
        result = self._values.get("downscaling")
        return typing.cast(typing.Optional["OpsworksStaticWebLayerLoadBasedAutoScalingDownscaling"], result)

    @builtins.property
    def enable(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#enable OpsworksStaticWebLayer#enable}.'''
        result = self._values.get("enable")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def upscaling(
        self,
    ) -> typing.Optional["OpsworksStaticWebLayerLoadBasedAutoScalingUpscaling"]:
        '''upscaling block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#upscaling OpsworksStaticWebLayer#upscaling}
        '''
        result = self._values.get("upscaling")
        return typing.cast(typing.Optional["OpsworksStaticWebLayerLoadBasedAutoScalingUpscaling"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OpsworksStaticWebLayerLoadBasedAutoScaling(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.opsworksStaticWebLayer.OpsworksStaticWebLayerLoadBasedAutoScalingDownscaling",
    jsii_struct_bases=[],
    name_mapping={
        "alarms": "alarms",
        "cpu_threshold": "cpuThreshold",
        "ignore_metrics_time": "ignoreMetricsTime",
        "instance_count": "instanceCount",
        "load_threshold": "loadThreshold",
        "memory_threshold": "memoryThreshold",
        "thresholds_wait_time": "thresholdsWaitTime",
    },
)
class OpsworksStaticWebLayerLoadBasedAutoScalingDownscaling:
    def __init__(
        self,
        *,
        alarms: typing.Optional[typing.Sequence[builtins.str]] = None,
        cpu_threshold: typing.Optional[jsii.Number] = None,
        ignore_metrics_time: typing.Optional[jsii.Number] = None,
        instance_count: typing.Optional[jsii.Number] = None,
        load_threshold: typing.Optional[jsii.Number] = None,
        memory_threshold: typing.Optional[jsii.Number] = None,
        thresholds_wait_time: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param alarms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#alarms OpsworksStaticWebLayer#alarms}.
        :param cpu_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#cpu_threshold OpsworksStaticWebLayer#cpu_threshold}.
        :param ignore_metrics_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#ignore_metrics_time OpsworksStaticWebLayer#ignore_metrics_time}.
        :param instance_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#instance_count OpsworksStaticWebLayer#instance_count}.
        :param load_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#load_threshold OpsworksStaticWebLayer#load_threshold}.
        :param memory_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#memory_threshold OpsworksStaticWebLayer#memory_threshold}.
        :param thresholds_wait_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#thresholds_wait_time OpsworksStaticWebLayer#thresholds_wait_time}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a5497a28c771abc8e4903f2bc216a05c4846d899d5bfba84fee3ca2e1f2c4d6)
            check_type(argname="argument alarms", value=alarms, expected_type=type_hints["alarms"])
            check_type(argname="argument cpu_threshold", value=cpu_threshold, expected_type=type_hints["cpu_threshold"])
            check_type(argname="argument ignore_metrics_time", value=ignore_metrics_time, expected_type=type_hints["ignore_metrics_time"])
            check_type(argname="argument instance_count", value=instance_count, expected_type=type_hints["instance_count"])
            check_type(argname="argument load_threshold", value=load_threshold, expected_type=type_hints["load_threshold"])
            check_type(argname="argument memory_threshold", value=memory_threshold, expected_type=type_hints["memory_threshold"])
            check_type(argname="argument thresholds_wait_time", value=thresholds_wait_time, expected_type=type_hints["thresholds_wait_time"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if alarms is not None:
            self._values["alarms"] = alarms
        if cpu_threshold is not None:
            self._values["cpu_threshold"] = cpu_threshold
        if ignore_metrics_time is not None:
            self._values["ignore_metrics_time"] = ignore_metrics_time
        if instance_count is not None:
            self._values["instance_count"] = instance_count
        if load_threshold is not None:
            self._values["load_threshold"] = load_threshold
        if memory_threshold is not None:
            self._values["memory_threshold"] = memory_threshold
        if thresholds_wait_time is not None:
            self._values["thresholds_wait_time"] = thresholds_wait_time

    @builtins.property
    def alarms(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#alarms OpsworksStaticWebLayer#alarms}.'''
        result = self._values.get("alarms")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def cpu_threshold(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#cpu_threshold OpsworksStaticWebLayer#cpu_threshold}.'''
        result = self._values.get("cpu_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ignore_metrics_time(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#ignore_metrics_time OpsworksStaticWebLayer#ignore_metrics_time}.'''
        result = self._values.get("ignore_metrics_time")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def instance_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#instance_count OpsworksStaticWebLayer#instance_count}.'''
        result = self._values.get("instance_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def load_threshold(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#load_threshold OpsworksStaticWebLayer#load_threshold}.'''
        result = self._values.get("load_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def memory_threshold(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#memory_threshold OpsworksStaticWebLayer#memory_threshold}.'''
        result = self._values.get("memory_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def thresholds_wait_time(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#thresholds_wait_time OpsworksStaticWebLayer#thresholds_wait_time}.'''
        result = self._values.get("thresholds_wait_time")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OpsworksStaticWebLayerLoadBasedAutoScalingDownscaling(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OpsworksStaticWebLayerLoadBasedAutoScalingDownscalingOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.opsworksStaticWebLayer.OpsworksStaticWebLayerLoadBasedAutoScalingDownscalingOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9cc2fe3f381eafcfa47c1230e7a5c60c2459ae3d050921c8f15ca53224969fbd)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAlarms")
    def reset_alarms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlarms", []))

    @jsii.member(jsii_name="resetCpuThreshold")
    def reset_cpu_threshold(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCpuThreshold", []))

    @jsii.member(jsii_name="resetIgnoreMetricsTime")
    def reset_ignore_metrics_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIgnoreMetricsTime", []))

    @jsii.member(jsii_name="resetInstanceCount")
    def reset_instance_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceCount", []))

    @jsii.member(jsii_name="resetLoadThreshold")
    def reset_load_threshold(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoadThreshold", []))

    @jsii.member(jsii_name="resetMemoryThreshold")
    def reset_memory_threshold(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMemoryThreshold", []))

    @jsii.member(jsii_name="resetThresholdsWaitTime")
    def reset_thresholds_wait_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetThresholdsWaitTime", []))

    @builtins.property
    @jsii.member(jsii_name="alarmsInput")
    def alarms_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "alarmsInput"))

    @builtins.property
    @jsii.member(jsii_name="cpuThresholdInput")
    def cpu_threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "cpuThresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="ignoreMetricsTimeInput")
    def ignore_metrics_time_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ignoreMetricsTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceCountInput")
    def instance_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "instanceCountInput"))

    @builtins.property
    @jsii.member(jsii_name="loadThresholdInput")
    def load_threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "loadThresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="memoryThresholdInput")
    def memory_threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "memoryThresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="thresholdsWaitTimeInput")
    def thresholds_wait_time_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "thresholdsWaitTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="alarms")
    def alarms(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "alarms"))

    @alarms.setter
    def alarms(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d30bcd5aecfe4844a4f3c653111eb570f32cbc84d6f0b1d9d25770d509704c7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alarms", value)

    @builtins.property
    @jsii.member(jsii_name="cpuThreshold")
    def cpu_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "cpuThreshold"))

    @cpu_threshold.setter
    def cpu_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd337c64d408b5cee6e6261c5e4aa71477633da66e5786209cd6322c7cc56532)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpuThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="ignoreMetricsTime")
    def ignore_metrics_time(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ignoreMetricsTime"))

    @ignore_metrics_time.setter
    def ignore_metrics_time(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68e691347931919dd97c018d3e8ec4eeced335b9c573c9828117b8fe99ea2de4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ignoreMetricsTime", value)

    @builtins.property
    @jsii.member(jsii_name="instanceCount")
    def instance_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "instanceCount"))

    @instance_count.setter
    def instance_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4bf7ce4d0aa5ef3cc150f43da5e0fd3bc26158e60a3984fa02be5cfaacbc8edf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceCount", value)

    @builtins.property
    @jsii.member(jsii_name="loadThreshold")
    def load_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "loadThreshold"))

    @load_threshold.setter
    def load_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__65a36221378ac5eda2e315e8214b3bea9e7258a2aaec2557f9f21ad4dd99653b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loadThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="memoryThreshold")
    def memory_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "memoryThreshold"))

    @memory_threshold.setter
    def memory_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f02adf3c2738c25ecdcb0a77b0a4b09d8e8f4f9b3574f0153277fca20583da4b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memoryThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="thresholdsWaitTime")
    def thresholds_wait_time(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "thresholdsWaitTime"))

    @thresholds_wait_time.setter
    def thresholds_wait_time(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4bf3370705e6d77bb41748b0dd5a4c218fcfd1647dc3e94690feb79924733e4c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "thresholdsWaitTime", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[OpsworksStaticWebLayerLoadBasedAutoScalingDownscaling]:
        return typing.cast(typing.Optional[OpsworksStaticWebLayerLoadBasedAutoScalingDownscaling], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OpsworksStaticWebLayerLoadBasedAutoScalingDownscaling],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ade9fe24a96ff588d2acbe0c2d23735a7bd3c85f34866bc2861da653fa06876)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OpsworksStaticWebLayerLoadBasedAutoScalingOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.opsworksStaticWebLayer.OpsworksStaticWebLayerLoadBasedAutoScalingOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2b6583658b74ea1dd89bc97ee0ae07d97c00b50475302492c325a03eda7d6f2e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDownscaling")
    def put_downscaling(
        self,
        *,
        alarms: typing.Optional[typing.Sequence[builtins.str]] = None,
        cpu_threshold: typing.Optional[jsii.Number] = None,
        ignore_metrics_time: typing.Optional[jsii.Number] = None,
        instance_count: typing.Optional[jsii.Number] = None,
        load_threshold: typing.Optional[jsii.Number] = None,
        memory_threshold: typing.Optional[jsii.Number] = None,
        thresholds_wait_time: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param alarms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#alarms OpsworksStaticWebLayer#alarms}.
        :param cpu_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#cpu_threshold OpsworksStaticWebLayer#cpu_threshold}.
        :param ignore_metrics_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#ignore_metrics_time OpsworksStaticWebLayer#ignore_metrics_time}.
        :param instance_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#instance_count OpsworksStaticWebLayer#instance_count}.
        :param load_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#load_threshold OpsworksStaticWebLayer#load_threshold}.
        :param memory_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#memory_threshold OpsworksStaticWebLayer#memory_threshold}.
        :param thresholds_wait_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#thresholds_wait_time OpsworksStaticWebLayer#thresholds_wait_time}.
        '''
        value = OpsworksStaticWebLayerLoadBasedAutoScalingDownscaling(
            alarms=alarms,
            cpu_threshold=cpu_threshold,
            ignore_metrics_time=ignore_metrics_time,
            instance_count=instance_count,
            load_threshold=load_threshold,
            memory_threshold=memory_threshold,
            thresholds_wait_time=thresholds_wait_time,
        )

        return typing.cast(None, jsii.invoke(self, "putDownscaling", [value]))

    @jsii.member(jsii_name="putUpscaling")
    def put_upscaling(
        self,
        *,
        alarms: typing.Optional[typing.Sequence[builtins.str]] = None,
        cpu_threshold: typing.Optional[jsii.Number] = None,
        ignore_metrics_time: typing.Optional[jsii.Number] = None,
        instance_count: typing.Optional[jsii.Number] = None,
        load_threshold: typing.Optional[jsii.Number] = None,
        memory_threshold: typing.Optional[jsii.Number] = None,
        thresholds_wait_time: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param alarms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#alarms OpsworksStaticWebLayer#alarms}.
        :param cpu_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#cpu_threshold OpsworksStaticWebLayer#cpu_threshold}.
        :param ignore_metrics_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#ignore_metrics_time OpsworksStaticWebLayer#ignore_metrics_time}.
        :param instance_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#instance_count OpsworksStaticWebLayer#instance_count}.
        :param load_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#load_threshold OpsworksStaticWebLayer#load_threshold}.
        :param memory_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#memory_threshold OpsworksStaticWebLayer#memory_threshold}.
        :param thresholds_wait_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#thresholds_wait_time OpsworksStaticWebLayer#thresholds_wait_time}.
        '''
        value = OpsworksStaticWebLayerLoadBasedAutoScalingUpscaling(
            alarms=alarms,
            cpu_threshold=cpu_threshold,
            ignore_metrics_time=ignore_metrics_time,
            instance_count=instance_count,
            load_threshold=load_threshold,
            memory_threshold=memory_threshold,
            thresholds_wait_time=thresholds_wait_time,
        )

        return typing.cast(None, jsii.invoke(self, "putUpscaling", [value]))

    @jsii.member(jsii_name="resetDownscaling")
    def reset_downscaling(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDownscaling", []))

    @jsii.member(jsii_name="resetEnable")
    def reset_enable(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnable", []))

    @jsii.member(jsii_name="resetUpscaling")
    def reset_upscaling(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpscaling", []))

    @builtins.property
    @jsii.member(jsii_name="downscaling")
    def downscaling(
        self,
    ) -> OpsworksStaticWebLayerLoadBasedAutoScalingDownscalingOutputReference:
        return typing.cast(OpsworksStaticWebLayerLoadBasedAutoScalingDownscalingOutputReference, jsii.get(self, "downscaling"))

    @builtins.property
    @jsii.member(jsii_name="upscaling")
    def upscaling(
        self,
    ) -> "OpsworksStaticWebLayerLoadBasedAutoScalingUpscalingOutputReference":
        return typing.cast("OpsworksStaticWebLayerLoadBasedAutoScalingUpscalingOutputReference", jsii.get(self, "upscaling"))

    @builtins.property
    @jsii.member(jsii_name="downscalingInput")
    def downscaling_input(
        self,
    ) -> typing.Optional[OpsworksStaticWebLayerLoadBasedAutoScalingDownscaling]:
        return typing.cast(typing.Optional[OpsworksStaticWebLayerLoadBasedAutoScalingDownscaling], jsii.get(self, "downscalingInput"))

    @builtins.property
    @jsii.member(jsii_name="enableInput")
    def enable_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableInput"))

    @builtins.property
    @jsii.member(jsii_name="upscalingInput")
    def upscaling_input(
        self,
    ) -> typing.Optional["OpsworksStaticWebLayerLoadBasedAutoScalingUpscaling"]:
        return typing.cast(typing.Optional["OpsworksStaticWebLayerLoadBasedAutoScalingUpscaling"], jsii.get(self, "upscalingInput"))

    @builtins.property
    @jsii.member(jsii_name="enable")
    def enable(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enable"))

    @enable.setter
    def enable(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a460962d926baa73b29053136983b199ff5f8a15ea21097dbbba4e045c7cce94)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enable", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[OpsworksStaticWebLayerLoadBasedAutoScaling]:
        return typing.cast(typing.Optional[OpsworksStaticWebLayerLoadBasedAutoScaling], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OpsworksStaticWebLayerLoadBasedAutoScaling],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7eef1ec37acd3c07269a1923b4efe90e10b3dd3cd95d2909797e4d9a2702cec9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.opsworksStaticWebLayer.OpsworksStaticWebLayerLoadBasedAutoScalingUpscaling",
    jsii_struct_bases=[],
    name_mapping={
        "alarms": "alarms",
        "cpu_threshold": "cpuThreshold",
        "ignore_metrics_time": "ignoreMetricsTime",
        "instance_count": "instanceCount",
        "load_threshold": "loadThreshold",
        "memory_threshold": "memoryThreshold",
        "thresholds_wait_time": "thresholdsWaitTime",
    },
)
class OpsworksStaticWebLayerLoadBasedAutoScalingUpscaling:
    def __init__(
        self,
        *,
        alarms: typing.Optional[typing.Sequence[builtins.str]] = None,
        cpu_threshold: typing.Optional[jsii.Number] = None,
        ignore_metrics_time: typing.Optional[jsii.Number] = None,
        instance_count: typing.Optional[jsii.Number] = None,
        load_threshold: typing.Optional[jsii.Number] = None,
        memory_threshold: typing.Optional[jsii.Number] = None,
        thresholds_wait_time: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param alarms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#alarms OpsworksStaticWebLayer#alarms}.
        :param cpu_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#cpu_threshold OpsworksStaticWebLayer#cpu_threshold}.
        :param ignore_metrics_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#ignore_metrics_time OpsworksStaticWebLayer#ignore_metrics_time}.
        :param instance_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#instance_count OpsworksStaticWebLayer#instance_count}.
        :param load_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#load_threshold OpsworksStaticWebLayer#load_threshold}.
        :param memory_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#memory_threshold OpsworksStaticWebLayer#memory_threshold}.
        :param thresholds_wait_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#thresholds_wait_time OpsworksStaticWebLayer#thresholds_wait_time}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e38233cd2376b857625f81b4eb1c90a3f011a7013ead6de416ed6cb154f1b47)
            check_type(argname="argument alarms", value=alarms, expected_type=type_hints["alarms"])
            check_type(argname="argument cpu_threshold", value=cpu_threshold, expected_type=type_hints["cpu_threshold"])
            check_type(argname="argument ignore_metrics_time", value=ignore_metrics_time, expected_type=type_hints["ignore_metrics_time"])
            check_type(argname="argument instance_count", value=instance_count, expected_type=type_hints["instance_count"])
            check_type(argname="argument load_threshold", value=load_threshold, expected_type=type_hints["load_threshold"])
            check_type(argname="argument memory_threshold", value=memory_threshold, expected_type=type_hints["memory_threshold"])
            check_type(argname="argument thresholds_wait_time", value=thresholds_wait_time, expected_type=type_hints["thresholds_wait_time"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if alarms is not None:
            self._values["alarms"] = alarms
        if cpu_threshold is not None:
            self._values["cpu_threshold"] = cpu_threshold
        if ignore_metrics_time is not None:
            self._values["ignore_metrics_time"] = ignore_metrics_time
        if instance_count is not None:
            self._values["instance_count"] = instance_count
        if load_threshold is not None:
            self._values["load_threshold"] = load_threshold
        if memory_threshold is not None:
            self._values["memory_threshold"] = memory_threshold
        if thresholds_wait_time is not None:
            self._values["thresholds_wait_time"] = thresholds_wait_time

    @builtins.property
    def alarms(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#alarms OpsworksStaticWebLayer#alarms}.'''
        result = self._values.get("alarms")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def cpu_threshold(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#cpu_threshold OpsworksStaticWebLayer#cpu_threshold}.'''
        result = self._values.get("cpu_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ignore_metrics_time(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#ignore_metrics_time OpsworksStaticWebLayer#ignore_metrics_time}.'''
        result = self._values.get("ignore_metrics_time")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def instance_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#instance_count OpsworksStaticWebLayer#instance_count}.'''
        result = self._values.get("instance_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def load_threshold(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#load_threshold OpsworksStaticWebLayer#load_threshold}.'''
        result = self._values.get("load_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def memory_threshold(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#memory_threshold OpsworksStaticWebLayer#memory_threshold}.'''
        result = self._values.get("memory_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def thresholds_wait_time(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_static_web_layer#thresholds_wait_time OpsworksStaticWebLayer#thresholds_wait_time}.'''
        result = self._values.get("thresholds_wait_time")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OpsworksStaticWebLayerLoadBasedAutoScalingUpscaling(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OpsworksStaticWebLayerLoadBasedAutoScalingUpscalingOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.opsworksStaticWebLayer.OpsworksStaticWebLayerLoadBasedAutoScalingUpscalingOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b8520e62c6d2e3d0e46319694be70e04d5afd874a95d0710cdfe07cf7e99a389)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAlarms")
    def reset_alarms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlarms", []))

    @jsii.member(jsii_name="resetCpuThreshold")
    def reset_cpu_threshold(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCpuThreshold", []))

    @jsii.member(jsii_name="resetIgnoreMetricsTime")
    def reset_ignore_metrics_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIgnoreMetricsTime", []))

    @jsii.member(jsii_name="resetInstanceCount")
    def reset_instance_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceCount", []))

    @jsii.member(jsii_name="resetLoadThreshold")
    def reset_load_threshold(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoadThreshold", []))

    @jsii.member(jsii_name="resetMemoryThreshold")
    def reset_memory_threshold(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMemoryThreshold", []))

    @jsii.member(jsii_name="resetThresholdsWaitTime")
    def reset_thresholds_wait_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetThresholdsWaitTime", []))

    @builtins.property
    @jsii.member(jsii_name="alarmsInput")
    def alarms_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "alarmsInput"))

    @builtins.property
    @jsii.member(jsii_name="cpuThresholdInput")
    def cpu_threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "cpuThresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="ignoreMetricsTimeInput")
    def ignore_metrics_time_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ignoreMetricsTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceCountInput")
    def instance_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "instanceCountInput"))

    @builtins.property
    @jsii.member(jsii_name="loadThresholdInput")
    def load_threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "loadThresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="memoryThresholdInput")
    def memory_threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "memoryThresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="thresholdsWaitTimeInput")
    def thresholds_wait_time_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "thresholdsWaitTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="alarms")
    def alarms(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "alarms"))

    @alarms.setter
    def alarms(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42436763a06e8540149a7b41d0cfe60cd8f013ae93a1dcfb93b779b1a35e47ca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alarms", value)

    @builtins.property
    @jsii.member(jsii_name="cpuThreshold")
    def cpu_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "cpuThreshold"))

    @cpu_threshold.setter
    def cpu_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1233440d98b001fa2e4aa43774f98e71b24ffb3ec04773357c42e4b9b3d098c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpuThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="ignoreMetricsTime")
    def ignore_metrics_time(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ignoreMetricsTime"))

    @ignore_metrics_time.setter
    def ignore_metrics_time(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__748b78f1d2ee5ab6cc1663d2435f82ce506c1c9a2a37a1aa2567ab04ca8ce34f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ignoreMetricsTime", value)

    @builtins.property
    @jsii.member(jsii_name="instanceCount")
    def instance_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "instanceCount"))

    @instance_count.setter
    def instance_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20e73cef76f30251066d75649f5566882f9004edcc435ec430349b7626c4d20a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceCount", value)

    @builtins.property
    @jsii.member(jsii_name="loadThreshold")
    def load_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "loadThreshold"))

    @load_threshold.setter
    def load_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7110d9815060ac43d714830ff16b6994a22df38c3571249bdbe7f213ef4cbe6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loadThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="memoryThreshold")
    def memory_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "memoryThreshold"))

    @memory_threshold.setter
    def memory_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a8c66cf9f01e8d9e50dac1d3c7dcd2e01193f5ccd47db2677a538237630d238)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memoryThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="thresholdsWaitTime")
    def thresholds_wait_time(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "thresholdsWaitTime"))

    @thresholds_wait_time.setter
    def thresholds_wait_time(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2e878f20ba5a45b146fc166ec33c7908ad286a81fa89ffde8be79ea28ad6f32)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "thresholdsWaitTime", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[OpsworksStaticWebLayerLoadBasedAutoScalingUpscaling]:
        return typing.cast(typing.Optional[OpsworksStaticWebLayerLoadBasedAutoScalingUpscaling], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OpsworksStaticWebLayerLoadBasedAutoScalingUpscaling],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2498f828aee5b01397b0cf9471e55d550b0475fe95a94b8a4869a3e1983d2fa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "OpsworksStaticWebLayer",
    "OpsworksStaticWebLayerCloudwatchConfiguration",
    "OpsworksStaticWebLayerCloudwatchConfigurationLogStreams",
    "OpsworksStaticWebLayerCloudwatchConfigurationLogStreamsList",
    "OpsworksStaticWebLayerCloudwatchConfigurationLogStreamsOutputReference",
    "OpsworksStaticWebLayerCloudwatchConfigurationOutputReference",
    "OpsworksStaticWebLayerConfig",
    "OpsworksStaticWebLayerEbsVolume",
    "OpsworksStaticWebLayerEbsVolumeList",
    "OpsworksStaticWebLayerEbsVolumeOutputReference",
    "OpsworksStaticWebLayerLoadBasedAutoScaling",
    "OpsworksStaticWebLayerLoadBasedAutoScalingDownscaling",
    "OpsworksStaticWebLayerLoadBasedAutoScalingDownscalingOutputReference",
    "OpsworksStaticWebLayerLoadBasedAutoScalingOutputReference",
    "OpsworksStaticWebLayerLoadBasedAutoScalingUpscaling",
    "OpsworksStaticWebLayerLoadBasedAutoScalingUpscalingOutputReference",
]

publication.publish()

def _typecheckingstub__34cd8e29790ce1a5a0a6511a74b1517321bf06023c318ebb058ed398e2ac4bd6(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    stack_id: builtins.str,
    auto_assign_elastic_ips: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    auto_assign_public_ips: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    auto_healing: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    cloudwatch_configuration: typing.Optional[typing.Union[OpsworksStaticWebLayerCloudwatchConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    custom_configure_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
    custom_deploy_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
    custom_instance_profile_arn: typing.Optional[builtins.str] = None,
    custom_json: typing.Optional[builtins.str] = None,
    custom_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    custom_setup_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
    custom_shutdown_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
    custom_undeploy_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
    drain_elb_on_shutdown: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ebs_volume: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[OpsworksStaticWebLayerEbsVolume, typing.Dict[builtins.str, typing.Any]]]]] = None,
    elastic_load_balancer: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    install_updates_on_boot: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    instance_shutdown_timeout: typing.Optional[jsii.Number] = None,
    load_based_auto_scaling: typing.Optional[typing.Union[OpsworksStaticWebLayerLoadBasedAutoScaling, typing.Dict[builtins.str, typing.Any]]] = None,
    name: typing.Optional[builtins.str] = None,
    system_packages: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    use_ebs_optimized_instances: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
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

def _typecheckingstub__1232f89f388d7bf75a8eb6a3985912fbc40b42bc09fa39ccdbf360fbbb0c56a0(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[OpsworksStaticWebLayerEbsVolume, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0652d2d0fa7cd75e3a0a34eeab204e9297e0718340fb2f4f2b755ae852c23c7d(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc10888f550e4cd99390020b5d5403c7c4699461e1cb26637048ed695f1aa4be(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8602efc775cd9fcc5a5bbb845ce4e4444854eae180c96c89a926f88e8acb2d73(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54326cdcfd29ba52f22babe0089f511bb395def474401782debb6e2974e21e1f(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91cc3062df1ca1343cd3b4f58f11eb34aec91ffee6adcbc8ac96569a8eb7f682(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ec808980b828c1b8c790d82cba282401bd4bdaaf75fe5eca7dcd35b7665af62(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23ef6435fea9eb934c534d5fe118b25289aeaa4e26f06bc7fb3b8aa7c409572d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39f64750701e3df7b2b68b2bc6817af517892ef1483f0b79d579f12ad386b819(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b0482ddef8c835458aece2e1ebc257f830ea9856a0df95907ace96e85c1b564(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37bff78a526fee41f2420546a18b3a8d2c557d4697764c1bd81cc5833fef4e88(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2356128ca1fafdf47ccbbac7a093da84b49bc2703d07ac85b77ae96884558073(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fcd9ae1c7bbdca8ea118e61f88866371999e7d41eb036006ff976a55de393e64(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__480e13853a75d1a0a478c380c9bd0ffa393f911583f14550b83afe9a5935dda9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d2355697ce0da89d1eeaa553a3ca97370026a905232cbbf05e3b7f7c1ae9170(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2abf78e9b767f119ab8e422c7da91a14d6c172e31292e9c063fe51c570d0488(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ce5d843927341eff70bfe711a5e4317b34d78d8bcb836283917eed621e028af(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1596f97f98d93b646cdfb53f8523811416c1b83be85235dfdb65c47cbcbbec1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d8ab20ef4ecd608e22113f5a57860a6e6aad557a6f6ed0fe33c696288610695(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1dd75e8710062efc6fbd127511a6fb252cf9a3a326bb3ffa76c5f8a57d410e15(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__215556b174c331aeb47c7fd70d97beecc55ea0565ddc6fcc32d163c2f91bacbe(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2cb2b05c51cb7c852549d9c7d0c378ed69bf2be2c9cf6d9d4d87931763106832(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f8dc5ad7775566841bf401de527ecbd5ea4d2ffe2d57075cb2487038951d148(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17398267f2aff499769822bb91ff03f24fc726b8b9af26ad87b581d5efd4306e(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    log_streams: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[OpsworksStaticWebLayerCloudwatchConfigurationLogStreams, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e148b7ddb3ca057a3fe3544d3f12cc965077862c51c67a908e0c3357a492dd8(
    *,
    file: builtins.str,
    log_group_name: builtins.str,
    batch_count: typing.Optional[jsii.Number] = None,
    batch_size: typing.Optional[jsii.Number] = None,
    buffer_duration: typing.Optional[jsii.Number] = None,
    datetime_format: typing.Optional[builtins.str] = None,
    encoding: typing.Optional[builtins.str] = None,
    file_fingerprint_lines: typing.Optional[builtins.str] = None,
    initial_position: typing.Optional[builtins.str] = None,
    multiline_start_pattern: typing.Optional[builtins.str] = None,
    time_zone: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad1a49fa6949db3e9bbfdc7f9b0ca12a1735a5e1a84662f86e3a00f251275666(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bda01e22d1c99fbff386b7dd5c978479d8b58734fd30508b3eaa9c9ce486ecec(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47c1b5c57ee6d6bddc46972539e2a94ce90b9650c1e30418785fcf27dd516121(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0170f45823a50b1931500d6e0f7d7c1e1b03fcb6f600ba5212ebee3cb42425d(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec3a2c190ef51c74eca300db0818ff59e1b98c8a31374875e52a9e23aeb7e21f(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7801125daea46bb8eb9667ff76fa6bf9acb2d502eeca99cede40be3f93813994(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[OpsworksStaticWebLayerCloudwatchConfigurationLogStreams]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3dd965c06a72c7b287a41f59d5444b2e4b5a788f4caa408a037871139c22771(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6844b2c983719d23a9620bcb70c6fc7aa19a6e6b45fdd4950ae11436b840e8b(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed72fcc77cfb946db2ae187ef7b1c5cfb6f6f19a7b13a72b91bf0ee6d2faebc5(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c560849f55e6a08cc4b76d407805192d615f9b2c87c6e6e0194b8878f71787c8(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c7e2a7ea37276c896a5eaf009372dc93caa0a8b6ec3d789f929c504244a47e3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dcfd6de257661ff11769fe1fc75429489b5781f6fecf8c6636d01feb86de9242(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__843d1e272cc18f2972217766387cd35c75c166df7dedccc68cb375e130cb59b9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e306219d72012de7eafcb7e948f21d88b2dd72c6bac42c73800bd20cd316685(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0e1583dd9f1b5340e47f4ab9e0541006528abd3a5d7d12c8c20fd51d1bff7c9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3590e4a5ed85592afe9be4955a7a3fd3783ec85d000c5001891d087d1cae22f6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97ce6945d1c0b3336a53e8d9f5534e25bb4126537b36c9764e47b0ea9b57a68c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c90edd693fb8940e9372abb2508d3e820a7f246a47a3b15601253cd1ec339af9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5e1eeea204c3197ecbfe2cc4a36e7889c25268868461a8e5683b2353fb29ee5(
    value: typing.Optional[typing.Union[OpsworksStaticWebLayerCloudwatchConfigurationLogStreams, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40e4972f02b88f2c5be148f751265f1487ca015fc32510ce86abda49984cec09(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9993903d16ba22f3ece6470cb3af96fc085c281931dbb4c8d13d127fc8ec225d(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[OpsworksStaticWebLayerCloudwatchConfigurationLogStreams, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68570b2b1e55852af7c4b3ae4902d5e9365d31dcd6ca5fed41a5af0d31ccdc56(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2bbe3503fb7d2f5d01c2ee6a704c0683c10973904eebcf146786003762864896(
    value: typing.Optional[OpsworksStaticWebLayerCloudwatchConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab3a39e768a56bc9f2af522d6899df999969b8cfad86dc5e13a8964c8babd719(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    stack_id: builtins.str,
    auto_assign_elastic_ips: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    auto_assign_public_ips: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    auto_healing: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    cloudwatch_configuration: typing.Optional[typing.Union[OpsworksStaticWebLayerCloudwatchConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    custom_configure_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
    custom_deploy_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
    custom_instance_profile_arn: typing.Optional[builtins.str] = None,
    custom_json: typing.Optional[builtins.str] = None,
    custom_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    custom_setup_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
    custom_shutdown_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
    custom_undeploy_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
    drain_elb_on_shutdown: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ebs_volume: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[OpsworksStaticWebLayerEbsVolume, typing.Dict[builtins.str, typing.Any]]]]] = None,
    elastic_load_balancer: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    install_updates_on_boot: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    instance_shutdown_timeout: typing.Optional[jsii.Number] = None,
    load_based_auto_scaling: typing.Optional[typing.Union[OpsworksStaticWebLayerLoadBasedAutoScaling, typing.Dict[builtins.str, typing.Any]]] = None,
    name: typing.Optional[builtins.str] = None,
    system_packages: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    use_ebs_optimized_instances: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf310fd7162d4d95a6f53e11d92138b2bcb802e02794aee8f8942d0a9feb6808(
    *,
    mount_point: builtins.str,
    number_of_disks: jsii.Number,
    size: jsii.Number,
    encrypted: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    iops: typing.Optional[jsii.Number] = None,
    raid_level: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9172885f3ed43db4fa8992ac2a7a3c4528744ca0e43af95e7f4c7a861e1b3044(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c7d34a08c5a608c8b3f7e44ddbc347efe4593138be0c233e40576b3ab63020b(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e1827f3d07fbd3eeaaf9b713e4cc12e04b2139e2572fbcc70dc60446f3d6ade(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__722b345f6e7b25f0ef245df80756ea95b054a7c26735b70ad511154a49e9939e(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0559de6122641c0ba05f73a17228a6ceaca8ce3427c0dcca4cbc739e0970c79a(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36acceac66bb1f6ba48fbe52175352409abb9d193a7b985dd853c931ac2e26ae(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[OpsworksStaticWebLayerEbsVolume]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e24f88e777d15820a820ba9ff20b261ec8be623ebaba776af5e53ebd4a540f88(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__662c4fe69ff9025c6435230e704dfb3a44853f56034b45a14ff0c07e0de36184(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6894a7779ae266baec6ff87ef3cb47c117c5c675aa7b9b343464bd1a8aa0a49d(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97531942695dcfd6e2a62ad0cd1105135e6a667a20eb58a2e9ae007f8a98c993(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40a5dd0a92903649fd746e0bccdee609da085894172e042950b5364c090c85b1(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ee62404c6e3375fbeb1909dc7368f9502091b332d05f975f40de7ec4f51cde1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15fe00b3a21521771138d531ff08e8177a4d978d917da155fff0b3fd2a8f2cdb(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6619d87db0358f8d49d4d5ec9259592c90cdad0b7bd762a00d637a75d0243c70(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af57f1d8e71a73fca498e655104499d38b35be4c4a233817f7ccc7d4eb2f2a32(
    value: typing.Optional[typing.Union[OpsworksStaticWebLayerEbsVolume, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f96aa322c083e10f4dcbed0267223a14d8b5ba8702341a3dee3516808c30dfc(
    *,
    downscaling: typing.Optional[typing.Union[OpsworksStaticWebLayerLoadBasedAutoScalingDownscaling, typing.Dict[builtins.str, typing.Any]]] = None,
    enable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    upscaling: typing.Optional[typing.Union[OpsworksStaticWebLayerLoadBasedAutoScalingUpscaling, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a5497a28c771abc8e4903f2bc216a05c4846d899d5bfba84fee3ca2e1f2c4d6(
    *,
    alarms: typing.Optional[typing.Sequence[builtins.str]] = None,
    cpu_threshold: typing.Optional[jsii.Number] = None,
    ignore_metrics_time: typing.Optional[jsii.Number] = None,
    instance_count: typing.Optional[jsii.Number] = None,
    load_threshold: typing.Optional[jsii.Number] = None,
    memory_threshold: typing.Optional[jsii.Number] = None,
    thresholds_wait_time: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9cc2fe3f381eafcfa47c1230e7a5c60c2459ae3d050921c8f15ca53224969fbd(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d30bcd5aecfe4844a4f3c653111eb570f32cbc84d6f0b1d9d25770d509704c7(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd337c64d408b5cee6e6261c5e4aa71477633da66e5786209cd6322c7cc56532(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68e691347931919dd97c018d3e8ec4eeced335b9c573c9828117b8fe99ea2de4(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4bf7ce4d0aa5ef3cc150f43da5e0fd3bc26158e60a3984fa02be5cfaacbc8edf(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65a36221378ac5eda2e315e8214b3bea9e7258a2aaec2557f9f21ad4dd99653b(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f02adf3c2738c25ecdcb0a77b0a4b09d8e8f4f9b3574f0153277fca20583da4b(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4bf3370705e6d77bb41748b0dd5a4c218fcfd1647dc3e94690feb79924733e4c(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ade9fe24a96ff588d2acbe0c2d23735a7bd3c85f34866bc2861da653fa06876(
    value: typing.Optional[OpsworksStaticWebLayerLoadBasedAutoScalingDownscaling],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b6583658b74ea1dd89bc97ee0ae07d97c00b50475302492c325a03eda7d6f2e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a460962d926baa73b29053136983b199ff5f8a15ea21097dbbba4e045c7cce94(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7eef1ec37acd3c07269a1923b4efe90e10b3dd3cd95d2909797e4d9a2702cec9(
    value: typing.Optional[OpsworksStaticWebLayerLoadBasedAutoScaling],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e38233cd2376b857625f81b4eb1c90a3f011a7013ead6de416ed6cb154f1b47(
    *,
    alarms: typing.Optional[typing.Sequence[builtins.str]] = None,
    cpu_threshold: typing.Optional[jsii.Number] = None,
    ignore_metrics_time: typing.Optional[jsii.Number] = None,
    instance_count: typing.Optional[jsii.Number] = None,
    load_threshold: typing.Optional[jsii.Number] = None,
    memory_threshold: typing.Optional[jsii.Number] = None,
    thresholds_wait_time: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8520e62c6d2e3d0e46319694be70e04d5afd874a95d0710cdfe07cf7e99a389(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42436763a06e8540149a7b41d0cfe60cd8f013ae93a1dcfb93b779b1a35e47ca(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1233440d98b001fa2e4aa43774f98e71b24ffb3ec04773357c42e4b9b3d098c(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__748b78f1d2ee5ab6cc1663d2435f82ce506c1c9a2a37a1aa2567ab04ca8ce34f(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20e73cef76f30251066d75649f5566882f9004edcc435ec430349b7626c4d20a(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7110d9815060ac43d714830ff16b6994a22df38c3571249bdbe7f213ef4cbe6(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a8c66cf9f01e8d9e50dac1d3c7dcd2e01193f5ccd47db2677a538237630d238(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2e878f20ba5a45b146fc166ec33c7908ad286a81fa89ffde8be79ea28ad6f32(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2498f828aee5b01397b0cf9471e55d550b0475fe95a94b8a4869a3e1983d2fa(
    value: typing.Optional[OpsworksStaticWebLayerLoadBasedAutoScalingUpscaling],
) -> None:
    """Type checking stubs"""
    pass
