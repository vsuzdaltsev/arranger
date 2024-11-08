'''
# `aws_opsworks_nodejs_app_layer`

Refer to the Terraform Registory for docs: [`aws_opsworks_nodejs_app_layer`](https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer).
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


class OpsworksNodejsAppLayer(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.opsworksNodejsAppLayer.OpsworksNodejsAppLayer",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer aws_opsworks_nodejs_app_layer}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        stack_id: builtins.str,
        auto_assign_elastic_ips: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        auto_assign_public_ips: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        auto_healing: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        cloudwatch_configuration: typing.Optional[typing.Union["OpsworksNodejsAppLayerCloudwatchConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        custom_configure_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
        custom_deploy_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
        custom_instance_profile_arn: typing.Optional[builtins.str] = None,
        custom_json: typing.Optional[builtins.str] = None,
        custom_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        custom_setup_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
        custom_shutdown_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
        custom_undeploy_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
        drain_elb_on_shutdown: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        ebs_volume: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["OpsworksNodejsAppLayerEbsVolume", typing.Dict[builtins.str, typing.Any]]]]] = None,
        elastic_load_balancer: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        install_updates_on_boot: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        instance_shutdown_timeout: typing.Optional[jsii.Number] = None,
        load_based_auto_scaling: typing.Optional[typing.Union["OpsworksNodejsAppLayerLoadBasedAutoScaling", typing.Dict[builtins.str, typing.Any]]] = None,
        name: typing.Optional[builtins.str] = None,
        nodejs_version: typing.Optional[builtins.str] = None,
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
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer aws_opsworks_nodejs_app_layer} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param stack_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#stack_id OpsworksNodejsAppLayer#stack_id}.
        :param auto_assign_elastic_ips: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#auto_assign_elastic_ips OpsworksNodejsAppLayer#auto_assign_elastic_ips}.
        :param auto_assign_public_ips: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#auto_assign_public_ips OpsworksNodejsAppLayer#auto_assign_public_ips}.
        :param auto_healing: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#auto_healing OpsworksNodejsAppLayer#auto_healing}.
        :param cloudwatch_configuration: cloudwatch_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#cloudwatch_configuration OpsworksNodejsAppLayer#cloudwatch_configuration}
        :param custom_configure_recipes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#custom_configure_recipes OpsworksNodejsAppLayer#custom_configure_recipes}.
        :param custom_deploy_recipes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#custom_deploy_recipes OpsworksNodejsAppLayer#custom_deploy_recipes}.
        :param custom_instance_profile_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#custom_instance_profile_arn OpsworksNodejsAppLayer#custom_instance_profile_arn}.
        :param custom_json: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#custom_json OpsworksNodejsAppLayer#custom_json}.
        :param custom_security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#custom_security_group_ids OpsworksNodejsAppLayer#custom_security_group_ids}.
        :param custom_setup_recipes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#custom_setup_recipes OpsworksNodejsAppLayer#custom_setup_recipes}.
        :param custom_shutdown_recipes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#custom_shutdown_recipes OpsworksNodejsAppLayer#custom_shutdown_recipes}.
        :param custom_undeploy_recipes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#custom_undeploy_recipes OpsworksNodejsAppLayer#custom_undeploy_recipes}.
        :param drain_elb_on_shutdown: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#drain_elb_on_shutdown OpsworksNodejsAppLayer#drain_elb_on_shutdown}.
        :param ebs_volume: ebs_volume block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#ebs_volume OpsworksNodejsAppLayer#ebs_volume}
        :param elastic_load_balancer: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#elastic_load_balancer OpsworksNodejsAppLayer#elastic_load_balancer}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#id OpsworksNodejsAppLayer#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param install_updates_on_boot: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#install_updates_on_boot OpsworksNodejsAppLayer#install_updates_on_boot}.
        :param instance_shutdown_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#instance_shutdown_timeout OpsworksNodejsAppLayer#instance_shutdown_timeout}.
        :param load_based_auto_scaling: load_based_auto_scaling block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#load_based_auto_scaling OpsworksNodejsAppLayer#load_based_auto_scaling}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#name OpsworksNodejsAppLayer#name}.
        :param nodejs_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#nodejs_version OpsworksNodejsAppLayer#nodejs_version}.
        :param system_packages: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#system_packages OpsworksNodejsAppLayer#system_packages}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#tags OpsworksNodejsAppLayer#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#tags_all OpsworksNodejsAppLayer#tags_all}.
        :param use_ebs_optimized_instances: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#use_ebs_optimized_instances OpsworksNodejsAppLayer#use_ebs_optimized_instances}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eed4c0305a72ab06d063e1eb51d755e87c61f6c1165dfe9ff3d3d51b542f1095)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = OpsworksNodejsAppLayerConfig(
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
            nodejs_version=nodejs_version,
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
        log_streams: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["OpsworksNodejsAppLayerCloudwatchConfigurationLogStreams", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#enabled OpsworksNodejsAppLayer#enabled}.
        :param log_streams: log_streams block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#log_streams OpsworksNodejsAppLayer#log_streams}
        '''
        value = OpsworksNodejsAppLayerCloudwatchConfiguration(
            enabled=enabled, log_streams=log_streams
        )

        return typing.cast(None, jsii.invoke(self, "putCloudwatchConfiguration", [value]))

    @jsii.member(jsii_name="putEbsVolume")
    def put_ebs_volume(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["OpsworksNodejsAppLayerEbsVolume", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27fcccb135d9176198499ce2393b707f6fd140c121da4dd94bb0fdd3ee2c02a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putEbsVolume", [value]))

    @jsii.member(jsii_name="putLoadBasedAutoScaling")
    def put_load_based_auto_scaling(
        self,
        *,
        downscaling: typing.Optional[typing.Union["OpsworksNodejsAppLayerLoadBasedAutoScalingDownscaling", typing.Dict[builtins.str, typing.Any]]] = None,
        enable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        upscaling: typing.Optional[typing.Union["OpsworksNodejsAppLayerLoadBasedAutoScalingUpscaling", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param downscaling: downscaling block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#downscaling OpsworksNodejsAppLayer#downscaling}
        :param enable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#enable OpsworksNodejsAppLayer#enable}.
        :param upscaling: upscaling block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#upscaling OpsworksNodejsAppLayer#upscaling}
        '''
        value = OpsworksNodejsAppLayerLoadBasedAutoScaling(
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

    @jsii.member(jsii_name="resetNodejsVersion")
    def reset_nodejs_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNodejsVersion", []))

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
    ) -> "OpsworksNodejsAppLayerCloudwatchConfigurationOutputReference":
        return typing.cast("OpsworksNodejsAppLayerCloudwatchConfigurationOutputReference", jsii.get(self, "cloudwatchConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="ebsVolume")
    def ebs_volume(self) -> "OpsworksNodejsAppLayerEbsVolumeList":
        return typing.cast("OpsworksNodejsAppLayerEbsVolumeList", jsii.get(self, "ebsVolume"))

    @builtins.property
    @jsii.member(jsii_name="loadBasedAutoScaling")
    def load_based_auto_scaling(
        self,
    ) -> "OpsworksNodejsAppLayerLoadBasedAutoScalingOutputReference":
        return typing.cast("OpsworksNodejsAppLayerLoadBasedAutoScalingOutputReference", jsii.get(self, "loadBasedAutoScaling"))

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
    ) -> typing.Optional["OpsworksNodejsAppLayerCloudwatchConfiguration"]:
        return typing.cast(typing.Optional["OpsworksNodejsAppLayerCloudwatchConfiguration"], jsii.get(self, "cloudwatchConfigurationInput"))

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
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["OpsworksNodejsAppLayerEbsVolume"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["OpsworksNodejsAppLayerEbsVolume"]]], jsii.get(self, "ebsVolumeInput"))

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
    ) -> typing.Optional["OpsworksNodejsAppLayerLoadBasedAutoScaling"]:
        return typing.cast(typing.Optional["OpsworksNodejsAppLayerLoadBasedAutoScaling"], jsii.get(self, "loadBasedAutoScalingInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="nodejsVersionInput")
    def nodejs_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nodejsVersionInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__79b12bc360771a747c71acd657b0bd34dc7ead4ad3ef3844d4e2b97076356e41)
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
            type_hints = typing.get_type_hints(_typecheckingstub__235ee2161cb7825941e88ee35728fa932391c59efa061f6a11cd09b412e34702)
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
            type_hints = typing.get_type_hints(_typecheckingstub__38f721d43d68f523cecec0cbe365f91d90e3aff087a99f4cc0abcc82599b62de)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoHealing", value)

    @builtins.property
    @jsii.member(jsii_name="customConfigureRecipes")
    def custom_configure_recipes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "customConfigureRecipes"))

    @custom_configure_recipes.setter
    def custom_configure_recipes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73d177e76cfb906d55237e50418f1cd05b9a9d87a85eea5a9025bf38d5d0216c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customConfigureRecipes", value)

    @builtins.property
    @jsii.member(jsii_name="customDeployRecipes")
    def custom_deploy_recipes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "customDeployRecipes"))

    @custom_deploy_recipes.setter
    def custom_deploy_recipes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c64352ed5cc0c594c4cd88f09c81ba2dd5b45e840a64caef1d76cd0d9bd9d9a6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customDeployRecipes", value)

    @builtins.property
    @jsii.member(jsii_name="customInstanceProfileArn")
    def custom_instance_profile_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customInstanceProfileArn"))

    @custom_instance_profile_arn.setter
    def custom_instance_profile_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3bd65db2e196d09c8754e0d8ddcef4efa81b18130cb7a68c69446404b44f6c8f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customInstanceProfileArn", value)

    @builtins.property
    @jsii.member(jsii_name="customJson")
    def custom_json(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customJson"))

    @custom_json.setter
    def custom_json(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40705be7ac421ae614c418beebdfef215fd0925c5c66f3dd25643ff8084dd67e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customJson", value)

    @builtins.property
    @jsii.member(jsii_name="customSecurityGroupIds")
    def custom_security_group_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "customSecurityGroupIds"))

    @custom_security_group_ids.setter
    def custom_security_group_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a464bd31739534eb6f54238d47bc33343ce24033c6edfc2f48183448f92dbbc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customSecurityGroupIds", value)

    @builtins.property
    @jsii.member(jsii_name="customSetupRecipes")
    def custom_setup_recipes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "customSetupRecipes"))

    @custom_setup_recipes.setter
    def custom_setup_recipes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20dfef3bf568095a43fc22370d7c843bd61e590e8e69474c6ae84826853c315f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customSetupRecipes", value)

    @builtins.property
    @jsii.member(jsii_name="customShutdownRecipes")
    def custom_shutdown_recipes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "customShutdownRecipes"))

    @custom_shutdown_recipes.setter
    def custom_shutdown_recipes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0aefc6ccdc116c16bf7fe69a2bebb55b7fac31b5ca7869bb3cd7ed6f5020f7b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customShutdownRecipes", value)

    @builtins.property
    @jsii.member(jsii_name="customUndeployRecipes")
    def custom_undeploy_recipes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "customUndeployRecipes"))

    @custom_undeploy_recipes.setter
    def custom_undeploy_recipes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92bf3095343d082ce2d1c2cea99d976904738d643912f8aee31cb1e8ea47475f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ce0653ee862b4a02400c82ce7f6c32e2787976e5da6fa022b45b849d813d691a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "drainElbOnShutdown", value)

    @builtins.property
    @jsii.member(jsii_name="elasticLoadBalancer")
    def elastic_load_balancer(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "elasticLoadBalancer"))

    @elastic_load_balancer.setter
    def elastic_load_balancer(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b1c98af478ed44ed16d69c0487175afdefd500c8d06dc6dbb40839e18837bb5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "elasticLoadBalancer", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea809f5f94a30e91ef1f8aa7fdb58a91d062ab41e69fec65de5758941cc3075c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c682ebbfbec17430700e15cc5fb41080503725c5084ef58dfa92d32187395e25)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "installUpdatesOnBoot", value)

    @builtins.property
    @jsii.member(jsii_name="instanceShutdownTimeout")
    def instance_shutdown_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "instanceShutdownTimeout"))

    @instance_shutdown_timeout.setter
    def instance_shutdown_timeout(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7bc36c97ae56226a6a61e7e499632534821bbc1cb896c32288ece63ac315df15)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceShutdownTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e674ec3836cba91a719201c04670f4199b4a88613a4e822bc810a93ca75be199)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="nodejsVersion")
    def nodejs_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nodejsVersion"))

    @nodejs_version.setter
    def nodejs_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60820d8a6a6edd6584cc2a232a2af6689d6756d450fc25a1b3dd115ae8ce3c97)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nodejsVersion", value)

    @builtins.property
    @jsii.member(jsii_name="stackId")
    def stack_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "stackId"))

    @stack_id.setter
    def stack_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e92f6021885d2e9bf537fb5ba889c6c36bb9b4a0fa33e49158e57d0eebea92af)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stackId", value)

    @builtins.property
    @jsii.member(jsii_name="systemPackages")
    def system_packages(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "systemPackages"))

    @system_packages.setter
    def system_packages(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__849520ffbedfa911ca71f79553ac4220e4d98207543c9a9127bf9e01f2e446b3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "systemPackages", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c95c5b09b1d3743969d659ed4eb63f0bce1329a1e86dbe65238c1f5ad4dca208)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c6d206ea8b4713e89df6eff83409aa1fe04f1288b366dc49225aab3c55ee0358)
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
            type_hints = typing.get_type_hints(_typecheckingstub__da21d4777a467f457ba46b9759d763eba7356ca0fa32682fe09b786ff291b9f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useEbsOptimizedInstances", value)


@jsii.data_type(
    jsii_type="aws.opsworksNodejsAppLayer.OpsworksNodejsAppLayerCloudwatchConfiguration",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "log_streams": "logStreams"},
)
class OpsworksNodejsAppLayerCloudwatchConfiguration:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        log_streams: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["OpsworksNodejsAppLayerCloudwatchConfigurationLogStreams", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#enabled OpsworksNodejsAppLayer#enabled}.
        :param log_streams: log_streams block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#log_streams OpsworksNodejsAppLayer#log_streams}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__813091b01870332fb93c7338d4545275895351bd5162773ead356560d378ce05)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#enabled OpsworksNodejsAppLayer#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def log_streams(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["OpsworksNodejsAppLayerCloudwatchConfigurationLogStreams"]]]:
        '''log_streams block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#log_streams OpsworksNodejsAppLayer#log_streams}
        '''
        result = self._values.get("log_streams")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["OpsworksNodejsAppLayerCloudwatchConfigurationLogStreams"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OpsworksNodejsAppLayerCloudwatchConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.opsworksNodejsAppLayer.OpsworksNodejsAppLayerCloudwatchConfigurationLogStreams",
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
class OpsworksNodejsAppLayerCloudwatchConfigurationLogStreams:
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
        :param file: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#file OpsworksNodejsAppLayer#file}.
        :param log_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#log_group_name OpsworksNodejsAppLayer#log_group_name}.
        :param batch_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#batch_count OpsworksNodejsAppLayer#batch_count}.
        :param batch_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#batch_size OpsworksNodejsAppLayer#batch_size}.
        :param buffer_duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#buffer_duration OpsworksNodejsAppLayer#buffer_duration}.
        :param datetime_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#datetime_format OpsworksNodejsAppLayer#datetime_format}.
        :param encoding: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#encoding OpsworksNodejsAppLayer#encoding}.
        :param file_fingerprint_lines: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#file_fingerprint_lines OpsworksNodejsAppLayer#file_fingerprint_lines}.
        :param initial_position: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#initial_position OpsworksNodejsAppLayer#initial_position}.
        :param multiline_start_pattern: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#multiline_start_pattern OpsworksNodejsAppLayer#multiline_start_pattern}.
        :param time_zone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#time_zone OpsworksNodejsAppLayer#time_zone}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d289ecd3735cae31a678aa2d5f2c04a29038f59f90e8de1ceb613bcd995b629)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#file OpsworksNodejsAppLayer#file}.'''
        result = self._values.get("file")
        assert result is not None, "Required property 'file' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def log_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#log_group_name OpsworksNodejsAppLayer#log_group_name}.'''
        result = self._values.get("log_group_name")
        assert result is not None, "Required property 'log_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def batch_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#batch_count OpsworksNodejsAppLayer#batch_count}.'''
        result = self._values.get("batch_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def batch_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#batch_size OpsworksNodejsAppLayer#batch_size}.'''
        result = self._values.get("batch_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def buffer_duration(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#buffer_duration OpsworksNodejsAppLayer#buffer_duration}.'''
        result = self._values.get("buffer_duration")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def datetime_format(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#datetime_format OpsworksNodejsAppLayer#datetime_format}.'''
        result = self._values.get("datetime_format")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encoding(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#encoding OpsworksNodejsAppLayer#encoding}.'''
        result = self._values.get("encoding")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def file_fingerprint_lines(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#file_fingerprint_lines OpsworksNodejsAppLayer#file_fingerprint_lines}.'''
        result = self._values.get("file_fingerprint_lines")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def initial_position(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#initial_position OpsworksNodejsAppLayer#initial_position}.'''
        result = self._values.get("initial_position")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def multiline_start_pattern(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#multiline_start_pattern OpsworksNodejsAppLayer#multiline_start_pattern}.'''
        result = self._values.get("multiline_start_pattern")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def time_zone(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#time_zone OpsworksNodejsAppLayer#time_zone}.'''
        result = self._values.get("time_zone")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OpsworksNodejsAppLayerCloudwatchConfigurationLogStreams(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OpsworksNodejsAppLayerCloudwatchConfigurationLogStreamsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.opsworksNodejsAppLayer.OpsworksNodejsAppLayerCloudwatchConfigurationLogStreamsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7b4b1a84787524d0c811860f54dd94ba6ac55aefa19c91ee884159d5f63cc2dd)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "OpsworksNodejsAppLayerCloudwatchConfigurationLogStreamsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__51113f213d42d808780e41a0f2926d556d632c89118911596e36abfd6117a021)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("OpsworksNodejsAppLayerCloudwatchConfigurationLogStreamsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ea1c18c064f06e62bb2fec1f58eb6739755e44207cc57b661f3b48b556ad350)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a096d3f3961551f335434ceb426e9677ecb4b2c73f42a7bf98f6f43aec89d9cf)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e317c78e712a5cbff66e3f8d3d25a3797f955db5bde86d5670f364091e1583f0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[OpsworksNodejsAppLayerCloudwatchConfigurationLogStreams]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[OpsworksNodejsAppLayerCloudwatchConfigurationLogStreams]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[OpsworksNodejsAppLayerCloudwatchConfigurationLogStreams]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__beebe2be3b4c838a2e4eea3384e2d8fa2df468c50aa9c6663feb306ab65d319c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OpsworksNodejsAppLayerCloudwatchConfigurationLogStreamsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.opsworksNodejsAppLayer.OpsworksNodejsAppLayerCloudwatchConfigurationLogStreamsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7f67a6517c3f397991d8b35c7d1f0a8ea3c7f102433c7b3fddd31b21f53f1804)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d7d3016f7859aac6775d97b8f9c4370233447b2d799289de4e830aaca21be1ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "batchCount", value)

    @builtins.property
    @jsii.member(jsii_name="batchSize")
    def batch_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "batchSize"))

    @batch_size.setter
    def batch_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03416b38bf0e46936b5f56682b9d6f35e1d84c068739b5781fcd189da1c55550)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "batchSize", value)

    @builtins.property
    @jsii.member(jsii_name="bufferDuration")
    def buffer_duration(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "bufferDuration"))

    @buffer_duration.setter
    def buffer_duration(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a24e30c9e46e4a6f90a763699dc6f8bda2b2d15cd00f7ea7456b4eeae7bafd0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bufferDuration", value)

    @builtins.property
    @jsii.member(jsii_name="datetimeFormat")
    def datetime_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datetimeFormat"))

    @datetime_format.setter
    def datetime_format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27d870d87d80ceda15cce6151ad80008650eb1d0863a095b8668375be03004de)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datetimeFormat", value)

    @builtins.property
    @jsii.member(jsii_name="encoding")
    def encoding(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "encoding"))

    @encoding.setter
    def encoding(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e5c54004c361b49b3e67e5a587ff89fdb260285701304fd6bbf82d711b5feb5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encoding", value)

    @builtins.property
    @jsii.member(jsii_name="file")
    def file(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "file"))

    @file.setter
    def file(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ab788ac7342d49510999765d02e9e130a08f5d603da39c3eaf78d77d2af908a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "file", value)

    @builtins.property
    @jsii.member(jsii_name="fileFingerprintLines")
    def file_fingerprint_lines(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fileFingerprintLines"))

    @file_fingerprint_lines.setter
    def file_fingerprint_lines(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7da84af0788477376d503f8d1e91fedd49ad74d0d51c2675754dc6738a641d08)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileFingerprintLines", value)

    @builtins.property
    @jsii.member(jsii_name="initialPosition")
    def initial_position(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "initialPosition"))

    @initial_position.setter
    def initial_position(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb9301ab77f7349cf0c55452197602e3ee30b4394f79d6985d0171b308d6c1b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "initialPosition", value)

    @builtins.property
    @jsii.member(jsii_name="logGroupName")
    def log_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logGroupName"))

    @log_group_name.setter
    def log_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef4e80c521dae2298b4d10f5e8dbe4f594fb5945de14552d24eda76a2a07fcde)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="multilineStartPattern")
    def multiline_start_pattern(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "multilineStartPattern"))

    @multiline_start_pattern.setter
    def multiline_start_pattern(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8d6fa6fc2b0d21f0dfe4e6647a2e0ca35cec49afea3cd934b5828812d92d08a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "multilineStartPattern", value)

    @builtins.property
    @jsii.member(jsii_name="timeZone")
    def time_zone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timeZone"))

    @time_zone.setter
    def time_zone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3aa32268d1ee64cc10202b373bb4455c397043a5a603eb9f40c7a32dbe0fceb7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeZone", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[OpsworksNodejsAppLayerCloudwatchConfigurationLogStreams, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[OpsworksNodejsAppLayerCloudwatchConfigurationLogStreams, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[OpsworksNodejsAppLayerCloudwatchConfigurationLogStreams, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d44fd09434a6cbead30a5705c10d891c2eab3bce046cb8a97c7a91c2d6cc3831)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OpsworksNodejsAppLayerCloudwatchConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.opsworksNodejsAppLayer.OpsworksNodejsAppLayerCloudwatchConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__643bce9f636293d37d572ac351987ffd5776cb434ec9aee9e3edc3fe52ff43ee)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putLogStreams")
    def put_log_streams(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[OpsworksNodejsAppLayerCloudwatchConfigurationLogStreams, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15f89fab7f286341580cf9de60ae77085c87c0f4a2c85d928ec3736444d9d6b8)
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
    ) -> OpsworksNodejsAppLayerCloudwatchConfigurationLogStreamsList:
        return typing.cast(OpsworksNodejsAppLayerCloudwatchConfigurationLogStreamsList, jsii.get(self, "logStreams"))

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
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[OpsworksNodejsAppLayerCloudwatchConfigurationLogStreams]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[OpsworksNodejsAppLayerCloudwatchConfigurationLogStreams]]], jsii.get(self, "logStreamsInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__08f722b36ba06cbead8615c0d925fe40cc27b7340347f656aadfe8af9edf6ed4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[OpsworksNodejsAppLayerCloudwatchConfiguration]:
        return typing.cast(typing.Optional[OpsworksNodejsAppLayerCloudwatchConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OpsworksNodejsAppLayerCloudwatchConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c5e8e3ac938f0eb52384f6875eff820d1409ad119bf590ed983d603b6d625fb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.opsworksNodejsAppLayer.OpsworksNodejsAppLayerConfig",
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
        "nodejs_version": "nodejsVersion",
        "system_packages": "systemPackages",
        "tags": "tags",
        "tags_all": "tagsAll",
        "use_ebs_optimized_instances": "useEbsOptimizedInstances",
    },
)
class OpsworksNodejsAppLayerConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        cloudwatch_configuration: typing.Optional[typing.Union[OpsworksNodejsAppLayerCloudwatchConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
        custom_configure_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
        custom_deploy_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
        custom_instance_profile_arn: typing.Optional[builtins.str] = None,
        custom_json: typing.Optional[builtins.str] = None,
        custom_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        custom_setup_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
        custom_shutdown_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
        custom_undeploy_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
        drain_elb_on_shutdown: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        ebs_volume: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["OpsworksNodejsAppLayerEbsVolume", typing.Dict[builtins.str, typing.Any]]]]] = None,
        elastic_load_balancer: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        install_updates_on_boot: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        instance_shutdown_timeout: typing.Optional[jsii.Number] = None,
        load_based_auto_scaling: typing.Optional[typing.Union["OpsworksNodejsAppLayerLoadBasedAutoScaling", typing.Dict[builtins.str, typing.Any]]] = None,
        name: typing.Optional[builtins.str] = None,
        nodejs_version: typing.Optional[builtins.str] = None,
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
        :param stack_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#stack_id OpsworksNodejsAppLayer#stack_id}.
        :param auto_assign_elastic_ips: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#auto_assign_elastic_ips OpsworksNodejsAppLayer#auto_assign_elastic_ips}.
        :param auto_assign_public_ips: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#auto_assign_public_ips OpsworksNodejsAppLayer#auto_assign_public_ips}.
        :param auto_healing: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#auto_healing OpsworksNodejsAppLayer#auto_healing}.
        :param cloudwatch_configuration: cloudwatch_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#cloudwatch_configuration OpsworksNodejsAppLayer#cloudwatch_configuration}
        :param custom_configure_recipes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#custom_configure_recipes OpsworksNodejsAppLayer#custom_configure_recipes}.
        :param custom_deploy_recipes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#custom_deploy_recipes OpsworksNodejsAppLayer#custom_deploy_recipes}.
        :param custom_instance_profile_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#custom_instance_profile_arn OpsworksNodejsAppLayer#custom_instance_profile_arn}.
        :param custom_json: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#custom_json OpsworksNodejsAppLayer#custom_json}.
        :param custom_security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#custom_security_group_ids OpsworksNodejsAppLayer#custom_security_group_ids}.
        :param custom_setup_recipes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#custom_setup_recipes OpsworksNodejsAppLayer#custom_setup_recipes}.
        :param custom_shutdown_recipes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#custom_shutdown_recipes OpsworksNodejsAppLayer#custom_shutdown_recipes}.
        :param custom_undeploy_recipes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#custom_undeploy_recipes OpsworksNodejsAppLayer#custom_undeploy_recipes}.
        :param drain_elb_on_shutdown: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#drain_elb_on_shutdown OpsworksNodejsAppLayer#drain_elb_on_shutdown}.
        :param ebs_volume: ebs_volume block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#ebs_volume OpsworksNodejsAppLayer#ebs_volume}
        :param elastic_load_balancer: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#elastic_load_balancer OpsworksNodejsAppLayer#elastic_load_balancer}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#id OpsworksNodejsAppLayer#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param install_updates_on_boot: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#install_updates_on_boot OpsworksNodejsAppLayer#install_updates_on_boot}.
        :param instance_shutdown_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#instance_shutdown_timeout OpsworksNodejsAppLayer#instance_shutdown_timeout}.
        :param load_based_auto_scaling: load_based_auto_scaling block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#load_based_auto_scaling OpsworksNodejsAppLayer#load_based_auto_scaling}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#name OpsworksNodejsAppLayer#name}.
        :param nodejs_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#nodejs_version OpsworksNodejsAppLayer#nodejs_version}.
        :param system_packages: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#system_packages OpsworksNodejsAppLayer#system_packages}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#tags OpsworksNodejsAppLayer#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#tags_all OpsworksNodejsAppLayer#tags_all}.
        :param use_ebs_optimized_instances: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#use_ebs_optimized_instances OpsworksNodejsAppLayer#use_ebs_optimized_instances}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(cloudwatch_configuration, dict):
            cloudwatch_configuration = OpsworksNodejsAppLayerCloudwatchConfiguration(**cloudwatch_configuration)
        if isinstance(load_based_auto_scaling, dict):
            load_based_auto_scaling = OpsworksNodejsAppLayerLoadBasedAutoScaling(**load_based_auto_scaling)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2880c2366e114f838b7b8a00022df852a19be1a01766aaf9bc79ceba15d8674)
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
            check_type(argname="argument nodejs_version", value=nodejs_version, expected_type=type_hints["nodejs_version"])
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
        if nodejs_version is not None:
            self._values["nodejs_version"] = nodejs_version
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#stack_id OpsworksNodejsAppLayer#stack_id}.'''
        result = self._values.get("stack_id")
        assert result is not None, "Required property 'stack_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def auto_assign_elastic_ips(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#auto_assign_elastic_ips OpsworksNodejsAppLayer#auto_assign_elastic_ips}.'''
        result = self._values.get("auto_assign_elastic_ips")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def auto_assign_public_ips(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#auto_assign_public_ips OpsworksNodejsAppLayer#auto_assign_public_ips}.'''
        result = self._values.get("auto_assign_public_ips")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def auto_healing(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#auto_healing OpsworksNodejsAppLayer#auto_healing}.'''
        result = self._values.get("auto_healing")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def cloudwatch_configuration(
        self,
    ) -> typing.Optional[OpsworksNodejsAppLayerCloudwatchConfiguration]:
        '''cloudwatch_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#cloudwatch_configuration OpsworksNodejsAppLayer#cloudwatch_configuration}
        '''
        result = self._values.get("cloudwatch_configuration")
        return typing.cast(typing.Optional[OpsworksNodejsAppLayerCloudwatchConfiguration], result)

    @builtins.property
    def custom_configure_recipes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#custom_configure_recipes OpsworksNodejsAppLayer#custom_configure_recipes}.'''
        result = self._values.get("custom_configure_recipes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def custom_deploy_recipes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#custom_deploy_recipes OpsworksNodejsAppLayer#custom_deploy_recipes}.'''
        result = self._values.get("custom_deploy_recipes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def custom_instance_profile_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#custom_instance_profile_arn OpsworksNodejsAppLayer#custom_instance_profile_arn}.'''
        result = self._values.get("custom_instance_profile_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_json(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#custom_json OpsworksNodejsAppLayer#custom_json}.'''
        result = self._values.get("custom_json")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#custom_security_group_ids OpsworksNodejsAppLayer#custom_security_group_ids}.'''
        result = self._values.get("custom_security_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def custom_setup_recipes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#custom_setup_recipes OpsworksNodejsAppLayer#custom_setup_recipes}.'''
        result = self._values.get("custom_setup_recipes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def custom_shutdown_recipes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#custom_shutdown_recipes OpsworksNodejsAppLayer#custom_shutdown_recipes}.'''
        result = self._values.get("custom_shutdown_recipes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def custom_undeploy_recipes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#custom_undeploy_recipes OpsworksNodejsAppLayer#custom_undeploy_recipes}.'''
        result = self._values.get("custom_undeploy_recipes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def drain_elb_on_shutdown(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#drain_elb_on_shutdown OpsworksNodejsAppLayer#drain_elb_on_shutdown}.'''
        result = self._values.get("drain_elb_on_shutdown")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def ebs_volume(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["OpsworksNodejsAppLayerEbsVolume"]]]:
        '''ebs_volume block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#ebs_volume OpsworksNodejsAppLayer#ebs_volume}
        '''
        result = self._values.get("ebs_volume")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["OpsworksNodejsAppLayerEbsVolume"]]], result)

    @builtins.property
    def elastic_load_balancer(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#elastic_load_balancer OpsworksNodejsAppLayer#elastic_load_balancer}.'''
        result = self._values.get("elastic_load_balancer")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#id OpsworksNodejsAppLayer#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def install_updates_on_boot(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#install_updates_on_boot OpsworksNodejsAppLayer#install_updates_on_boot}.'''
        result = self._values.get("install_updates_on_boot")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def instance_shutdown_timeout(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#instance_shutdown_timeout OpsworksNodejsAppLayer#instance_shutdown_timeout}.'''
        result = self._values.get("instance_shutdown_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def load_based_auto_scaling(
        self,
    ) -> typing.Optional["OpsworksNodejsAppLayerLoadBasedAutoScaling"]:
        '''load_based_auto_scaling block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#load_based_auto_scaling OpsworksNodejsAppLayer#load_based_auto_scaling}
        '''
        result = self._values.get("load_based_auto_scaling")
        return typing.cast(typing.Optional["OpsworksNodejsAppLayerLoadBasedAutoScaling"], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#name OpsworksNodejsAppLayer#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def nodejs_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#nodejs_version OpsworksNodejsAppLayer#nodejs_version}.'''
        result = self._values.get("nodejs_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def system_packages(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#system_packages OpsworksNodejsAppLayer#system_packages}.'''
        result = self._values.get("system_packages")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#tags OpsworksNodejsAppLayer#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#tags_all OpsworksNodejsAppLayer#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def use_ebs_optimized_instances(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#use_ebs_optimized_instances OpsworksNodejsAppLayer#use_ebs_optimized_instances}.'''
        result = self._values.get("use_ebs_optimized_instances")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OpsworksNodejsAppLayerConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.opsworksNodejsAppLayer.OpsworksNodejsAppLayerEbsVolume",
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
class OpsworksNodejsAppLayerEbsVolume:
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
        :param mount_point: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#mount_point OpsworksNodejsAppLayer#mount_point}.
        :param number_of_disks: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#number_of_disks OpsworksNodejsAppLayer#number_of_disks}.
        :param size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#size OpsworksNodejsAppLayer#size}.
        :param encrypted: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#encrypted OpsworksNodejsAppLayer#encrypted}.
        :param iops: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#iops OpsworksNodejsAppLayer#iops}.
        :param raid_level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#raid_level OpsworksNodejsAppLayer#raid_level}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#type OpsworksNodejsAppLayer#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43cbebaa0f0f1d007e025dfed05af9072e8ac9e91a043950331d03effda6dfc8)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#mount_point OpsworksNodejsAppLayer#mount_point}.'''
        result = self._values.get("mount_point")
        assert result is not None, "Required property 'mount_point' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def number_of_disks(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#number_of_disks OpsworksNodejsAppLayer#number_of_disks}.'''
        result = self._values.get("number_of_disks")
        assert result is not None, "Required property 'number_of_disks' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def size(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#size OpsworksNodejsAppLayer#size}.'''
        result = self._values.get("size")
        assert result is not None, "Required property 'size' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def encrypted(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#encrypted OpsworksNodejsAppLayer#encrypted}.'''
        result = self._values.get("encrypted")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def iops(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#iops OpsworksNodejsAppLayer#iops}.'''
        result = self._values.get("iops")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def raid_level(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#raid_level OpsworksNodejsAppLayer#raid_level}.'''
        result = self._values.get("raid_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#type OpsworksNodejsAppLayer#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OpsworksNodejsAppLayerEbsVolume(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OpsworksNodejsAppLayerEbsVolumeList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.opsworksNodejsAppLayer.OpsworksNodejsAppLayerEbsVolumeList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__73b3e051d37958a57bb5d037bdf686dcc06b2b0f98d00f856c4957ae5e9b23de)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "OpsworksNodejsAppLayerEbsVolumeOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8413c5b39fd1344915f8411b60d7ef27eb53ce5838ff8aca67014a23714fe4d6)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("OpsworksNodejsAppLayerEbsVolumeOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54183ab099e5ff569060f7003f0dd23e4ccc379864848cafa006aa19dcee177d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__41321833905eea7b8617d47509dbfb746994dfd98d7bf6ae916cf92cf0069dcd)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0442bc56be77ddfc551f12a45793a57ef1f91b2719fd64980722d887f13280dc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[OpsworksNodejsAppLayerEbsVolume]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[OpsworksNodejsAppLayerEbsVolume]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[OpsworksNodejsAppLayerEbsVolume]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__10603e4c74f0e9c71f36721516c154f2b4005cd197135cf776f4de54dab4d3c4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OpsworksNodejsAppLayerEbsVolumeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.opsworksNodejsAppLayer.OpsworksNodejsAppLayerEbsVolumeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__553337f806663b290445806af3f36e91821e0dbc2d30d827b5c781abd6b0b86c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d783e5209d54aa1204095f408c3148167135b02a9f5216e058932009606e84e2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encrypted", value)

    @builtins.property
    @jsii.member(jsii_name="iops")
    def iops(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "iops"))

    @iops.setter
    def iops(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b469bb3d77a8d187bb28810edf4a2ac10b07f4aece4b8ffa2370de97b4f988cc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iops", value)

    @builtins.property
    @jsii.member(jsii_name="mountPoint")
    def mount_point(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mountPoint"))

    @mount_point.setter
    def mount_point(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a810be19d5b2efbb80a5ff646b56020d4879cdcb31e24d4549017e222b66aaae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mountPoint", value)

    @builtins.property
    @jsii.member(jsii_name="numberOfDisks")
    def number_of_disks(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "numberOfDisks"))

    @number_of_disks.setter
    def number_of_disks(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a48e9436351b262f5fccc7b0d52d9b0b017e4ee12bcd0abfa1667866e3f2169c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "numberOfDisks", value)

    @builtins.property
    @jsii.member(jsii_name="raidLevel")
    def raid_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "raidLevel"))

    @raid_level.setter
    def raid_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38425d57e8dd8dc220792b9d794ad8efe464d82f39d6be6fd181802ec1001828)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "raidLevel", value)

    @builtins.property
    @jsii.member(jsii_name="size")
    def size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "size"))

    @size.setter
    def size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3dfff4b3dc088f9700326b66e605f3a3a7645c1456d06ac06e8bcbfe4bd7f26b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "size", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d195282fd06f2291d18b211fb71ae588badbb445c450ef8f4787dd83a13ef7e3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[OpsworksNodejsAppLayerEbsVolume, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[OpsworksNodejsAppLayerEbsVolume, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[OpsworksNodejsAppLayerEbsVolume, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__48bfe97b54c7a8255db1399c26f7e6f8c85c7e42a8a9a278d13497e4a0a47b19)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.opsworksNodejsAppLayer.OpsworksNodejsAppLayerLoadBasedAutoScaling",
    jsii_struct_bases=[],
    name_mapping={
        "downscaling": "downscaling",
        "enable": "enable",
        "upscaling": "upscaling",
    },
)
class OpsworksNodejsAppLayerLoadBasedAutoScaling:
    def __init__(
        self,
        *,
        downscaling: typing.Optional[typing.Union["OpsworksNodejsAppLayerLoadBasedAutoScalingDownscaling", typing.Dict[builtins.str, typing.Any]]] = None,
        enable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        upscaling: typing.Optional[typing.Union["OpsworksNodejsAppLayerLoadBasedAutoScalingUpscaling", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param downscaling: downscaling block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#downscaling OpsworksNodejsAppLayer#downscaling}
        :param enable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#enable OpsworksNodejsAppLayer#enable}.
        :param upscaling: upscaling block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#upscaling OpsworksNodejsAppLayer#upscaling}
        '''
        if isinstance(downscaling, dict):
            downscaling = OpsworksNodejsAppLayerLoadBasedAutoScalingDownscaling(**downscaling)
        if isinstance(upscaling, dict):
            upscaling = OpsworksNodejsAppLayerLoadBasedAutoScalingUpscaling(**upscaling)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20713f5a9b7a34ee139f9f6c3d38d7d441ba67746b43e1f7b63885707447059b)
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
    ) -> typing.Optional["OpsworksNodejsAppLayerLoadBasedAutoScalingDownscaling"]:
        '''downscaling block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#downscaling OpsworksNodejsAppLayer#downscaling}
        '''
        result = self._values.get("downscaling")
        return typing.cast(typing.Optional["OpsworksNodejsAppLayerLoadBasedAutoScalingDownscaling"], result)

    @builtins.property
    def enable(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#enable OpsworksNodejsAppLayer#enable}.'''
        result = self._values.get("enable")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def upscaling(
        self,
    ) -> typing.Optional["OpsworksNodejsAppLayerLoadBasedAutoScalingUpscaling"]:
        '''upscaling block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#upscaling OpsworksNodejsAppLayer#upscaling}
        '''
        result = self._values.get("upscaling")
        return typing.cast(typing.Optional["OpsworksNodejsAppLayerLoadBasedAutoScalingUpscaling"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OpsworksNodejsAppLayerLoadBasedAutoScaling(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.opsworksNodejsAppLayer.OpsworksNodejsAppLayerLoadBasedAutoScalingDownscaling",
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
class OpsworksNodejsAppLayerLoadBasedAutoScalingDownscaling:
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
        :param alarms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#alarms OpsworksNodejsAppLayer#alarms}.
        :param cpu_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#cpu_threshold OpsworksNodejsAppLayer#cpu_threshold}.
        :param ignore_metrics_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#ignore_metrics_time OpsworksNodejsAppLayer#ignore_metrics_time}.
        :param instance_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#instance_count OpsworksNodejsAppLayer#instance_count}.
        :param load_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#load_threshold OpsworksNodejsAppLayer#load_threshold}.
        :param memory_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#memory_threshold OpsworksNodejsAppLayer#memory_threshold}.
        :param thresholds_wait_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#thresholds_wait_time OpsworksNodejsAppLayer#thresholds_wait_time}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27342de2ad98446d4ad46d512af909551f48ff6b04e8032fc9ffaa1f90fbb982)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#alarms OpsworksNodejsAppLayer#alarms}.'''
        result = self._values.get("alarms")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def cpu_threshold(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#cpu_threshold OpsworksNodejsAppLayer#cpu_threshold}.'''
        result = self._values.get("cpu_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ignore_metrics_time(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#ignore_metrics_time OpsworksNodejsAppLayer#ignore_metrics_time}.'''
        result = self._values.get("ignore_metrics_time")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def instance_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#instance_count OpsworksNodejsAppLayer#instance_count}.'''
        result = self._values.get("instance_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def load_threshold(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#load_threshold OpsworksNodejsAppLayer#load_threshold}.'''
        result = self._values.get("load_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def memory_threshold(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#memory_threshold OpsworksNodejsAppLayer#memory_threshold}.'''
        result = self._values.get("memory_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def thresholds_wait_time(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#thresholds_wait_time OpsworksNodejsAppLayer#thresholds_wait_time}.'''
        result = self._values.get("thresholds_wait_time")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OpsworksNodejsAppLayerLoadBasedAutoScalingDownscaling(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OpsworksNodejsAppLayerLoadBasedAutoScalingDownscalingOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.opsworksNodejsAppLayer.OpsworksNodejsAppLayerLoadBasedAutoScalingDownscalingOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__40336f98960b40e585e2e7bcf958aa06b71392c6145f2edd64b3676ede1015ab)
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
            type_hints = typing.get_type_hints(_typecheckingstub__40c9d294fef2f300780dfa4c4ed63e54268a343f0973aa7727f378231c2daa91)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alarms", value)

    @builtins.property
    @jsii.member(jsii_name="cpuThreshold")
    def cpu_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "cpuThreshold"))

    @cpu_threshold.setter
    def cpu_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72104655cf7cb282c5de5c3c36be60591398ce3c086ab5c97123495d01d47410)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpuThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="ignoreMetricsTime")
    def ignore_metrics_time(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ignoreMetricsTime"))

    @ignore_metrics_time.setter
    def ignore_metrics_time(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__491924ea4353869e4ac0a746442e486464ca51b74d835ed97d0efa92c4c32e00)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ignoreMetricsTime", value)

    @builtins.property
    @jsii.member(jsii_name="instanceCount")
    def instance_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "instanceCount"))

    @instance_count.setter
    def instance_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97f47beceab35d522c68e342146d596910fe0ff6b61cd598877d4a7ea5d3c342)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceCount", value)

    @builtins.property
    @jsii.member(jsii_name="loadThreshold")
    def load_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "loadThreshold"))

    @load_threshold.setter
    def load_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c67da5c2a289297985ff87490d4abbb74e19ebeddb177b20cfe44283b91ad6c8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loadThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="memoryThreshold")
    def memory_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "memoryThreshold"))

    @memory_threshold.setter
    def memory_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f28572cd334fc469f6279e713523b74b50eed32d37bf624c2f56c24442dc7971)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memoryThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="thresholdsWaitTime")
    def thresholds_wait_time(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "thresholdsWaitTime"))

    @thresholds_wait_time.setter
    def thresholds_wait_time(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6297676d2fc4506f2ac2a91af0822d30bf8a27fbf385e151db35dd0197dc9313)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "thresholdsWaitTime", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[OpsworksNodejsAppLayerLoadBasedAutoScalingDownscaling]:
        return typing.cast(typing.Optional[OpsworksNodejsAppLayerLoadBasedAutoScalingDownscaling], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OpsworksNodejsAppLayerLoadBasedAutoScalingDownscaling],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2cd23d93218a7670e6d507709c50302aa5eca1f5e93ef1901c79b134893f9fb0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OpsworksNodejsAppLayerLoadBasedAutoScalingOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.opsworksNodejsAppLayer.OpsworksNodejsAppLayerLoadBasedAutoScalingOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8018d6d3a48de0469fb93a97ee9aee9e820e077cc5bf8112032b6f8494effeb4)
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
        :param alarms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#alarms OpsworksNodejsAppLayer#alarms}.
        :param cpu_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#cpu_threshold OpsworksNodejsAppLayer#cpu_threshold}.
        :param ignore_metrics_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#ignore_metrics_time OpsworksNodejsAppLayer#ignore_metrics_time}.
        :param instance_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#instance_count OpsworksNodejsAppLayer#instance_count}.
        :param load_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#load_threshold OpsworksNodejsAppLayer#load_threshold}.
        :param memory_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#memory_threshold OpsworksNodejsAppLayer#memory_threshold}.
        :param thresholds_wait_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#thresholds_wait_time OpsworksNodejsAppLayer#thresholds_wait_time}.
        '''
        value = OpsworksNodejsAppLayerLoadBasedAutoScalingDownscaling(
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
        :param alarms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#alarms OpsworksNodejsAppLayer#alarms}.
        :param cpu_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#cpu_threshold OpsworksNodejsAppLayer#cpu_threshold}.
        :param ignore_metrics_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#ignore_metrics_time OpsworksNodejsAppLayer#ignore_metrics_time}.
        :param instance_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#instance_count OpsworksNodejsAppLayer#instance_count}.
        :param load_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#load_threshold OpsworksNodejsAppLayer#load_threshold}.
        :param memory_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#memory_threshold OpsworksNodejsAppLayer#memory_threshold}.
        :param thresholds_wait_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#thresholds_wait_time OpsworksNodejsAppLayer#thresholds_wait_time}.
        '''
        value = OpsworksNodejsAppLayerLoadBasedAutoScalingUpscaling(
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
    ) -> OpsworksNodejsAppLayerLoadBasedAutoScalingDownscalingOutputReference:
        return typing.cast(OpsworksNodejsAppLayerLoadBasedAutoScalingDownscalingOutputReference, jsii.get(self, "downscaling"))

    @builtins.property
    @jsii.member(jsii_name="upscaling")
    def upscaling(
        self,
    ) -> "OpsworksNodejsAppLayerLoadBasedAutoScalingUpscalingOutputReference":
        return typing.cast("OpsworksNodejsAppLayerLoadBasedAutoScalingUpscalingOutputReference", jsii.get(self, "upscaling"))

    @builtins.property
    @jsii.member(jsii_name="downscalingInput")
    def downscaling_input(
        self,
    ) -> typing.Optional[OpsworksNodejsAppLayerLoadBasedAutoScalingDownscaling]:
        return typing.cast(typing.Optional[OpsworksNodejsAppLayerLoadBasedAutoScalingDownscaling], jsii.get(self, "downscalingInput"))

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
    ) -> typing.Optional["OpsworksNodejsAppLayerLoadBasedAutoScalingUpscaling"]:
        return typing.cast(typing.Optional["OpsworksNodejsAppLayerLoadBasedAutoScalingUpscaling"], jsii.get(self, "upscalingInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__bffa0d33336ece0ed300bacd75b23c6adaec38dbcae499be39dbaabaa9c19bdb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enable", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[OpsworksNodejsAppLayerLoadBasedAutoScaling]:
        return typing.cast(typing.Optional[OpsworksNodejsAppLayerLoadBasedAutoScaling], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OpsworksNodejsAppLayerLoadBasedAutoScaling],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c4465354f5ba50266e48252e28072052c23a89abd09b5be416569b905af36ba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.opsworksNodejsAppLayer.OpsworksNodejsAppLayerLoadBasedAutoScalingUpscaling",
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
class OpsworksNodejsAppLayerLoadBasedAutoScalingUpscaling:
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
        :param alarms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#alarms OpsworksNodejsAppLayer#alarms}.
        :param cpu_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#cpu_threshold OpsworksNodejsAppLayer#cpu_threshold}.
        :param ignore_metrics_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#ignore_metrics_time OpsworksNodejsAppLayer#ignore_metrics_time}.
        :param instance_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#instance_count OpsworksNodejsAppLayer#instance_count}.
        :param load_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#load_threshold OpsworksNodejsAppLayer#load_threshold}.
        :param memory_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#memory_threshold OpsworksNodejsAppLayer#memory_threshold}.
        :param thresholds_wait_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#thresholds_wait_time OpsworksNodejsAppLayer#thresholds_wait_time}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f38cc328cd934c9e0e9baee8075e5a1cca87dcb37f12fa8c87b6c2928ce7534)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#alarms OpsworksNodejsAppLayer#alarms}.'''
        result = self._values.get("alarms")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def cpu_threshold(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#cpu_threshold OpsworksNodejsAppLayer#cpu_threshold}.'''
        result = self._values.get("cpu_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ignore_metrics_time(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#ignore_metrics_time OpsworksNodejsAppLayer#ignore_metrics_time}.'''
        result = self._values.get("ignore_metrics_time")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def instance_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#instance_count OpsworksNodejsAppLayer#instance_count}.'''
        result = self._values.get("instance_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def load_threshold(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#load_threshold OpsworksNodejsAppLayer#load_threshold}.'''
        result = self._values.get("load_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def memory_threshold(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#memory_threshold OpsworksNodejsAppLayer#memory_threshold}.'''
        result = self._values.get("memory_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def thresholds_wait_time(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_nodejs_app_layer#thresholds_wait_time OpsworksNodejsAppLayer#thresholds_wait_time}.'''
        result = self._values.get("thresholds_wait_time")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OpsworksNodejsAppLayerLoadBasedAutoScalingUpscaling(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OpsworksNodejsAppLayerLoadBasedAutoScalingUpscalingOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.opsworksNodejsAppLayer.OpsworksNodejsAppLayerLoadBasedAutoScalingUpscalingOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9ff17b8fd421524b94266a1f965775534aaa5240cb033536b72f621dd5785cb9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__58e05a08a47117a8846af7824309bb6d8b771df3d7ad9ba1e800295930bdb796)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alarms", value)

    @builtins.property
    @jsii.member(jsii_name="cpuThreshold")
    def cpu_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "cpuThreshold"))

    @cpu_threshold.setter
    def cpu_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d99691541aed37a3b62f823f1cfe801ca17cff8a18130b9013a2390520c0a944)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpuThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="ignoreMetricsTime")
    def ignore_metrics_time(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ignoreMetricsTime"))

    @ignore_metrics_time.setter
    def ignore_metrics_time(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0014c48d7fff96bf44bb24b383893bc382bd273e1e308929b5a96944f061b45c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ignoreMetricsTime", value)

    @builtins.property
    @jsii.member(jsii_name="instanceCount")
    def instance_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "instanceCount"))

    @instance_count.setter
    def instance_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f2482bc5c440134ad98bab47b0dd39a3b34ea9801fdcf6080d071d6dd0332e3e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceCount", value)

    @builtins.property
    @jsii.member(jsii_name="loadThreshold")
    def load_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "loadThreshold"))

    @load_threshold.setter
    def load_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c438d60422b3d6246ef47da77cb38a66a802b1fcf1d3856fb76cb8051d07fa28)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loadThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="memoryThreshold")
    def memory_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "memoryThreshold"))

    @memory_threshold.setter
    def memory_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6fc95b8d3e1a3f804c253370b47b6b568c3f75524013138c50a144e184b83c54)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memoryThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="thresholdsWaitTime")
    def thresholds_wait_time(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "thresholdsWaitTime"))

    @thresholds_wait_time.setter
    def thresholds_wait_time(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2754846577699ce5efc7cc4b64c5ad855604f17632196be9b5301d4c0747be4d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "thresholdsWaitTime", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[OpsworksNodejsAppLayerLoadBasedAutoScalingUpscaling]:
        return typing.cast(typing.Optional[OpsworksNodejsAppLayerLoadBasedAutoScalingUpscaling], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OpsworksNodejsAppLayerLoadBasedAutoScalingUpscaling],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7de24f955bcb4d51ff2544e504aee316ee58e5b6729108a4654f3c4b5aca32ed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "OpsworksNodejsAppLayer",
    "OpsworksNodejsAppLayerCloudwatchConfiguration",
    "OpsworksNodejsAppLayerCloudwatchConfigurationLogStreams",
    "OpsworksNodejsAppLayerCloudwatchConfigurationLogStreamsList",
    "OpsworksNodejsAppLayerCloudwatchConfigurationLogStreamsOutputReference",
    "OpsworksNodejsAppLayerCloudwatchConfigurationOutputReference",
    "OpsworksNodejsAppLayerConfig",
    "OpsworksNodejsAppLayerEbsVolume",
    "OpsworksNodejsAppLayerEbsVolumeList",
    "OpsworksNodejsAppLayerEbsVolumeOutputReference",
    "OpsworksNodejsAppLayerLoadBasedAutoScaling",
    "OpsworksNodejsAppLayerLoadBasedAutoScalingDownscaling",
    "OpsworksNodejsAppLayerLoadBasedAutoScalingDownscalingOutputReference",
    "OpsworksNodejsAppLayerLoadBasedAutoScalingOutputReference",
    "OpsworksNodejsAppLayerLoadBasedAutoScalingUpscaling",
    "OpsworksNodejsAppLayerLoadBasedAutoScalingUpscalingOutputReference",
]

publication.publish()

def _typecheckingstub__eed4c0305a72ab06d063e1eb51d755e87c61f6c1165dfe9ff3d3d51b542f1095(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    stack_id: builtins.str,
    auto_assign_elastic_ips: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    auto_assign_public_ips: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    auto_healing: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    cloudwatch_configuration: typing.Optional[typing.Union[OpsworksNodejsAppLayerCloudwatchConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    custom_configure_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
    custom_deploy_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
    custom_instance_profile_arn: typing.Optional[builtins.str] = None,
    custom_json: typing.Optional[builtins.str] = None,
    custom_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    custom_setup_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
    custom_shutdown_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
    custom_undeploy_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
    drain_elb_on_shutdown: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ebs_volume: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[OpsworksNodejsAppLayerEbsVolume, typing.Dict[builtins.str, typing.Any]]]]] = None,
    elastic_load_balancer: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    install_updates_on_boot: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    instance_shutdown_timeout: typing.Optional[jsii.Number] = None,
    load_based_auto_scaling: typing.Optional[typing.Union[OpsworksNodejsAppLayerLoadBasedAutoScaling, typing.Dict[builtins.str, typing.Any]]] = None,
    name: typing.Optional[builtins.str] = None,
    nodejs_version: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__27fcccb135d9176198499ce2393b707f6fd140c121da4dd94bb0fdd3ee2c02a2(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[OpsworksNodejsAppLayerEbsVolume, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79b12bc360771a747c71acd657b0bd34dc7ead4ad3ef3844d4e2b97076356e41(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__235ee2161cb7825941e88ee35728fa932391c59efa061f6a11cd09b412e34702(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38f721d43d68f523cecec0cbe365f91d90e3aff087a99f4cc0abcc82599b62de(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73d177e76cfb906d55237e50418f1cd05b9a9d87a85eea5a9025bf38d5d0216c(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c64352ed5cc0c594c4cd88f09c81ba2dd5b45e840a64caef1d76cd0d9bd9d9a6(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3bd65db2e196d09c8754e0d8ddcef4efa81b18130cb7a68c69446404b44f6c8f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40705be7ac421ae614c418beebdfef215fd0925c5c66f3dd25643ff8084dd67e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a464bd31739534eb6f54238d47bc33343ce24033c6edfc2f48183448f92dbbc(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20dfef3bf568095a43fc22370d7c843bd61e590e8e69474c6ae84826853c315f(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0aefc6ccdc116c16bf7fe69a2bebb55b7fac31b5ca7869bb3cd7ed6f5020f7b(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92bf3095343d082ce2d1c2cea99d976904738d643912f8aee31cb1e8ea47475f(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce0653ee862b4a02400c82ce7f6c32e2787976e5da6fa022b45b849d813d691a(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b1c98af478ed44ed16d69c0487175afdefd500c8d06dc6dbb40839e18837bb5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea809f5f94a30e91ef1f8aa7fdb58a91d062ab41e69fec65de5758941cc3075c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c682ebbfbec17430700e15cc5fb41080503725c5084ef58dfa92d32187395e25(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7bc36c97ae56226a6a61e7e499632534821bbc1cb896c32288ece63ac315df15(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e674ec3836cba91a719201c04670f4199b4a88613a4e822bc810a93ca75be199(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60820d8a6a6edd6584cc2a232a2af6689d6756d450fc25a1b3dd115ae8ce3c97(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e92f6021885d2e9bf537fb5ba889c6c36bb9b4a0fa33e49158e57d0eebea92af(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__849520ffbedfa911ca71f79553ac4220e4d98207543c9a9127bf9e01f2e446b3(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c95c5b09b1d3743969d659ed4eb63f0bce1329a1e86dbe65238c1f5ad4dca208(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6d206ea8b4713e89df6eff83409aa1fe04f1288b366dc49225aab3c55ee0358(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da21d4777a467f457ba46b9759d763eba7356ca0fa32682fe09b786ff291b9f8(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__813091b01870332fb93c7338d4545275895351bd5162773ead356560d378ce05(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    log_streams: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[OpsworksNodejsAppLayerCloudwatchConfigurationLogStreams, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d289ecd3735cae31a678aa2d5f2c04a29038f59f90e8de1ceb613bcd995b629(
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

def _typecheckingstub__7b4b1a84787524d0c811860f54dd94ba6ac55aefa19c91ee884159d5f63cc2dd(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51113f213d42d808780e41a0f2926d556d632c89118911596e36abfd6117a021(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ea1c18c064f06e62bb2fec1f58eb6739755e44207cc57b661f3b48b556ad350(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a096d3f3961551f335434ceb426e9677ecb4b2c73f42a7bf98f6f43aec89d9cf(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e317c78e712a5cbff66e3f8d3d25a3797f955db5bde86d5670f364091e1583f0(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__beebe2be3b4c838a2e4eea3384e2d8fa2df468c50aa9c6663feb306ab65d319c(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[OpsworksNodejsAppLayerCloudwatchConfigurationLogStreams]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f67a6517c3f397991d8b35c7d1f0a8ea3c7f102433c7b3fddd31b21f53f1804(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7d3016f7859aac6775d97b8f9c4370233447b2d799289de4e830aaca21be1ce(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03416b38bf0e46936b5f56682b9d6f35e1d84c068739b5781fcd189da1c55550(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a24e30c9e46e4a6f90a763699dc6f8bda2b2d15cd00f7ea7456b4eeae7bafd0(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27d870d87d80ceda15cce6151ad80008650eb1d0863a095b8668375be03004de(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e5c54004c361b49b3e67e5a587ff89fdb260285701304fd6bbf82d711b5feb5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ab788ac7342d49510999765d02e9e130a08f5d603da39c3eaf78d77d2af908a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7da84af0788477376d503f8d1e91fedd49ad74d0d51c2675754dc6738a641d08(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb9301ab77f7349cf0c55452197602e3ee30b4394f79d6985d0171b308d6c1b4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef4e80c521dae2298b4d10f5e8dbe4f594fb5945de14552d24eda76a2a07fcde(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8d6fa6fc2b0d21f0dfe4e6647a2e0ca35cec49afea3cd934b5828812d92d08a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3aa32268d1ee64cc10202b373bb4455c397043a5a603eb9f40c7a32dbe0fceb7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d44fd09434a6cbead30a5705c10d891c2eab3bce046cb8a97c7a91c2d6cc3831(
    value: typing.Optional[typing.Union[OpsworksNodejsAppLayerCloudwatchConfigurationLogStreams, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__643bce9f636293d37d572ac351987ffd5776cb434ec9aee9e3edc3fe52ff43ee(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15f89fab7f286341580cf9de60ae77085c87c0f4a2c85d928ec3736444d9d6b8(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[OpsworksNodejsAppLayerCloudwatchConfigurationLogStreams, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08f722b36ba06cbead8615c0d925fe40cc27b7340347f656aadfe8af9edf6ed4(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c5e8e3ac938f0eb52384f6875eff820d1409ad119bf590ed983d603b6d625fb(
    value: typing.Optional[OpsworksNodejsAppLayerCloudwatchConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2880c2366e114f838b7b8a00022df852a19be1a01766aaf9bc79ceba15d8674(
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
    cloudwatch_configuration: typing.Optional[typing.Union[OpsworksNodejsAppLayerCloudwatchConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    custom_configure_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
    custom_deploy_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
    custom_instance_profile_arn: typing.Optional[builtins.str] = None,
    custom_json: typing.Optional[builtins.str] = None,
    custom_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    custom_setup_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
    custom_shutdown_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
    custom_undeploy_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
    drain_elb_on_shutdown: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ebs_volume: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[OpsworksNodejsAppLayerEbsVolume, typing.Dict[builtins.str, typing.Any]]]]] = None,
    elastic_load_balancer: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    install_updates_on_boot: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    instance_shutdown_timeout: typing.Optional[jsii.Number] = None,
    load_based_auto_scaling: typing.Optional[typing.Union[OpsworksNodejsAppLayerLoadBasedAutoScaling, typing.Dict[builtins.str, typing.Any]]] = None,
    name: typing.Optional[builtins.str] = None,
    nodejs_version: typing.Optional[builtins.str] = None,
    system_packages: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    use_ebs_optimized_instances: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43cbebaa0f0f1d007e025dfed05af9072e8ac9e91a043950331d03effda6dfc8(
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

def _typecheckingstub__73b3e051d37958a57bb5d037bdf686dcc06b2b0f98d00f856c4957ae5e9b23de(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8413c5b39fd1344915f8411b60d7ef27eb53ce5838ff8aca67014a23714fe4d6(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54183ab099e5ff569060f7003f0dd23e4ccc379864848cafa006aa19dcee177d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41321833905eea7b8617d47509dbfb746994dfd98d7bf6ae916cf92cf0069dcd(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0442bc56be77ddfc551f12a45793a57ef1f91b2719fd64980722d887f13280dc(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10603e4c74f0e9c71f36721516c154f2b4005cd197135cf776f4de54dab4d3c4(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[OpsworksNodejsAppLayerEbsVolume]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__553337f806663b290445806af3f36e91821e0dbc2d30d827b5c781abd6b0b86c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d783e5209d54aa1204095f408c3148167135b02a9f5216e058932009606e84e2(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b469bb3d77a8d187bb28810edf4a2ac10b07f4aece4b8ffa2370de97b4f988cc(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a810be19d5b2efbb80a5ff646b56020d4879cdcb31e24d4549017e222b66aaae(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a48e9436351b262f5fccc7b0d52d9b0b017e4ee12bcd0abfa1667866e3f2169c(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38425d57e8dd8dc220792b9d794ad8efe464d82f39d6be6fd181802ec1001828(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3dfff4b3dc088f9700326b66e605f3a3a7645c1456d06ac06e8bcbfe4bd7f26b(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d195282fd06f2291d18b211fb71ae588badbb445c450ef8f4787dd83a13ef7e3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48bfe97b54c7a8255db1399c26f7e6f8c85c7e42a8a9a278d13497e4a0a47b19(
    value: typing.Optional[typing.Union[OpsworksNodejsAppLayerEbsVolume, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20713f5a9b7a34ee139f9f6c3d38d7d441ba67746b43e1f7b63885707447059b(
    *,
    downscaling: typing.Optional[typing.Union[OpsworksNodejsAppLayerLoadBasedAutoScalingDownscaling, typing.Dict[builtins.str, typing.Any]]] = None,
    enable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    upscaling: typing.Optional[typing.Union[OpsworksNodejsAppLayerLoadBasedAutoScalingUpscaling, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27342de2ad98446d4ad46d512af909551f48ff6b04e8032fc9ffaa1f90fbb982(
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

def _typecheckingstub__40336f98960b40e585e2e7bcf958aa06b71392c6145f2edd64b3676ede1015ab(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40c9d294fef2f300780dfa4c4ed63e54268a343f0973aa7727f378231c2daa91(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72104655cf7cb282c5de5c3c36be60591398ce3c086ab5c97123495d01d47410(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__491924ea4353869e4ac0a746442e486464ca51b74d835ed97d0efa92c4c32e00(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97f47beceab35d522c68e342146d596910fe0ff6b61cd598877d4a7ea5d3c342(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c67da5c2a289297985ff87490d4abbb74e19ebeddb177b20cfe44283b91ad6c8(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f28572cd334fc469f6279e713523b74b50eed32d37bf624c2f56c24442dc7971(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6297676d2fc4506f2ac2a91af0822d30bf8a27fbf385e151db35dd0197dc9313(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2cd23d93218a7670e6d507709c50302aa5eca1f5e93ef1901c79b134893f9fb0(
    value: typing.Optional[OpsworksNodejsAppLayerLoadBasedAutoScalingDownscaling],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8018d6d3a48de0469fb93a97ee9aee9e820e077cc5bf8112032b6f8494effeb4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bffa0d33336ece0ed300bacd75b23c6adaec38dbcae499be39dbaabaa9c19bdb(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c4465354f5ba50266e48252e28072052c23a89abd09b5be416569b905af36ba(
    value: typing.Optional[OpsworksNodejsAppLayerLoadBasedAutoScaling],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f38cc328cd934c9e0e9baee8075e5a1cca87dcb37f12fa8c87b6c2928ce7534(
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

def _typecheckingstub__9ff17b8fd421524b94266a1f965775534aaa5240cb033536b72f621dd5785cb9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58e05a08a47117a8846af7824309bb6d8b771df3d7ad9ba1e800295930bdb796(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d99691541aed37a3b62f823f1cfe801ca17cff8a18130b9013a2390520c0a944(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0014c48d7fff96bf44bb24b383893bc382bd273e1e308929b5a96944f061b45c(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2482bc5c440134ad98bab47b0dd39a3b34ea9801fdcf6080d071d6dd0332e3e(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c438d60422b3d6246ef47da77cb38a66a802b1fcf1d3856fb76cb8051d07fa28(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6fc95b8d3e1a3f804c253370b47b6b568c3f75524013138c50a144e184b83c54(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2754846577699ce5efc7cc4b64c5ad855604f17632196be9b5301d4c0747be4d(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7de24f955bcb4d51ff2544e504aee316ee58e5b6729108a4654f3c4b5aca32ed(
    value: typing.Optional[OpsworksNodejsAppLayerLoadBasedAutoScalingUpscaling],
) -> None:
    """Type checking stubs"""
    pass
