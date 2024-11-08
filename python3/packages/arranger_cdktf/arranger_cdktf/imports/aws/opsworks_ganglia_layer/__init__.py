'''
# `aws_opsworks_ganglia_layer`

Refer to the Terraform Registory for docs: [`aws_opsworks_ganglia_layer`](https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer).
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


class OpsworksGangliaLayer(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.opsworksGangliaLayer.OpsworksGangliaLayer",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer aws_opsworks_ganglia_layer}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        password: builtins.str,
        stack_id: builtins.str,
        auto_assign_elastic_ips: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        auto_assign_public_ips: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        auto_healing: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        cloudwatch_configuration: typing.Optional[typing.Union["OpsworksGangliaLayerCloudwatchConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        custom_configure_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
        custom_deploy_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
        custom_instance_profile_arn: typing.Optional[builtins.str] = None,
        custom_json: typing.Optional[builtins.str] = None,
        custom_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        custom_setup_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
        custom_shutdown_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
        custom_undeploy_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
        drain_elb_on_shutdown: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        ebs_volume: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["OpsworksGangliaLayerEbsVolume", typing.Dict[builtins.str, typing.Any]]]]] = None,
        elastic_load_balancer: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        install_updates_on_boot: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        instance_shutdown_timeout: typing.Optional[jsii.Number] = None,
        load_based_auto_scaling: typing.Optional[typing.Union["OpsworksGangliaLayerLoadBasedAutoScaling", typing.Dict[builtins.str, typing.Any]]] = None,
        name: typing.Optional[builtins.str] = None,
        system_packages: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        url: typing.Optional[builtins.str] = None,
        use_ebs_optimized_instances: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        username: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer aws_opsworks_ganglia_layer} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#password OpsworksGangliaLayer#password}.
        :param stack_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#stack_id OpsworksGangliaLayer#stack_id}.
        :param auto_assign_elastic_ips: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#auto_assign_elastic_ips OpsworksGangliaLayer#auto_assign_elastic_ips}.
        :param auto_assign_public_ips: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#auto_assign_public_ips OpsworksGangliaLayer#auto_assign_public_ips}.
        :param auto_healing: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#auto_healing OpsworksGangliaLayer#auto_healing}.
        :param cloudwatch_configuration: cloudwatch_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#cloudwatch_configuration OpsworksGangliaLayer#cloudwatch_configuration}
        :param custom_configure_recipes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#custom_configure_recipes OpsworksGangliaLayer#custom_configure_recipes}.
        :param custom_deploy_recipes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#custom_deploy_recipes OpsworksGangliaLayer#custom_deploy_recipes}.
        :param custom_instance_profile_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#custom_instance_profile_arn OpsworksGangliaLayer#custom_instance_profile_arn}.
        :param custom_json: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#custom_json OpsworksGangliaLayer#custom_json}.
        :param custom_security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#custom_security_group_ids OpsworksGangliaLayer#custom_security_group_ids}.
        :param custom_setup_recipes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#custom_setup_recipes OpsworksGangliaLayer#custom_setup_recipes}.
        :param custom_shutdown_recipes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#custom_shutdown_recipes OpsworksGangliaLayer#custom_shutdown_recipes}.
        :param custom_undeploy_recipes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#custom_undeploy_recipes OpsworksGangliaLayer#custom_undeploy_recipes}.
        :param drain_elb_on_shutdown: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#drain_elb_on_shutdown OpsworksGangliaLayer#drain_elb_on_shutdown}.
        :param ebs_volume: ebs_volume block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#ebs_volume OpsworksGangliaLayer#ebs_volume}
        :param elastic_load_balancer: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#elastic_load_balancer OpsworksGangliaLayer#elastic_load_balancer}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#id OpsworksGangliaLayer#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param install_updates_on_boot: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#install_updates_on_boot OpsworksGangliaLayer#install_updates_on_boot}.
        :param instance_shutdown_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#instance_shutdown_timeout OpsworksGangliaLayer#instance_shutdown_timeout}.
        :param load_based_auto_scaling: load_based_auto_scaling block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#load_based_auto_scaling OpsworksGangliaLayer#load_based_auto_scaling}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#name OpsworksGangliaLayer#name}.
        :param system_packages: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#system_packages OpsworksGangliaLayer#system_packages}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#tags OpsworksGangliaLayer#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#tags_all OpsworksGangliaLayer#tags_all}.
        :param url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#url OpsworksGangliaLayer#url}.
        :param use_ebs_optimized_instances: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#use_ebs_optimized_instances OpsworksGangliaLayer#use_ebs_optimized_instances}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#username OpsworksGangliaLayer#username}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12d054284f2c4a19c4df92154e7c8579478fda0b760c0ee73fbd4a24e779b1e4)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = OpsworksGangliaLayerConfig(
            password=password,
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
            url=url,
            use_ebs_optimized_instances=use_ebs_optimized_instances,
            username=username,
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
        log_streams: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["OpsworksGangliaLayerCloudwatchConfigurationLogStreams", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#enabled OpsworksGangliaLayer#enabled}.
        :param log_streams: log_streams block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#log_streams OpsworksGangliaLayer#log_streams}
        '''
        value = OpsworksGangliaLayerCloudwatchConfiguration(
            enabled=enabled, log_streams=log_streams
        )

        return typing.cast(None, jsii.invoke(self, "putCloudwatchConfiguration", [value]))

    @jsii.member(jsii_name="putEbsVolume")
    def put_ebs_volume(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["OpsworksGangliaLayerEbsVolume", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f80361d41676e118b337b6eaafb3064a5d9098748c351b3124e379cd052b9fa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putEbsVolume", [value]))

    @jsii.member(jsii_name="putLoadBasedAutoScaling")
    def put_load_based_auto_scaling(
        self,
        *,
        downscaling: typing.Optional[typing.Union["OpsworksGangliaLayerLoadBasedAutoScalingDownscaling", typing.Dict[builtins.str, typing.Any]]] = None,
        enable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        upscaling: typing.Optional[typing.Union["OpsworksGangliaLayerLoadBasedAutoScalingUpscaling", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param downscaling: downscaling block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#downscaling OpsworksGangliaLayer#downscaling}
        :param enable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#enable OpsworksGangliaLayer#enable}.
        :param upscaling: upscaling block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#upscaling OpsworksGangliaLayer#upscaling}
        '''
        value = OpsworksGangliaLayerLoadBasedAutoScaling(
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

    @jsii.member(jsii_name="resetUrl")
    def reset_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUrl", []))

    @jsii.member(jsii_name="resetUseEbsOptimizedInstances")
    def reset_use_ebs_optimized_instances(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUseEbsOptimizedInstances", []))

    @jsii.member(jsii_name="resetUsername")
    def reset_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsername", []))

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
    ) -> "OpsworksGangliaLayerCloudwatchConfigurationOutputReference":
        return typing.cast("OpsworksGangliaLayerCloudwatchConfigurationOutputReference", jsii.get(self, "cloudwatchConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="ebsVolume")
    def ebs_volume(self) -> "OpsworksGangliaLayerEbsVolumeList":
        return typing.cast("OpsworksGangliaLayerEbsVolumeList", jsii.get(self, "ebsVolume"))

    @builtins.property
    @jsii.member(jsii_name="loadBasedAutoScaling")
    def load_based_auto_scaling(
        self,
    ) -> "OpsworksGangliaLayerLoadBasedAutoScalingOutputReference":
        return typing.cast("OpsworksGangliaLayerLoadBasedAutoScalingOutputReference", jsii.get(self, "loadBasedAutoScaling"))

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
    ) -> typing.Optional["OpsworksGangliaLayerCloudwatchConfiguration"]:
        return typing.cast(typing.Optional["OpsworksGangliaLayerCloudwatchConfiguration"], jsii.get(self, "cloudwatchConfigurationInput"))

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
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["OpsworksGangliaLayerEbsVolume"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["OpsworksGangliaLayerEbsVolume"]]], jsii.get(self, "ebsVolumeInput"))

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
    ) -> typing.Optional["OpsworksGangliaLayerLoadBasedAutoScaling"]:
        return typing.cast(typing.Optional["OpsworksGangliaLayerLoadBasedAutoScaling"], jsii.get(self, "loadBasedAutoScalingInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

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
    @jsii.member(jsii_name="urlInput")
    def url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlInput"))

    @builtins.property
    @jsii.member(jsii_name="useEbsOptimizedInstancesInput")
    def use_ebs_optimized_instances_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "useEbsOptimizedInstancesInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__6b67780b6b8682e64818807e39e3a52b64d541dd12412a39b4f2e7041254425e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e529c74f1dccd10749de8795fbf62e8ce1d9e8e6728c41714352968f0c63bc9e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__dfd64b6538dd1c3222fa1bcd292a4ed8835d3303e4ff56bd03b51a995c32c12c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoHealing", value)

    @builtins.property
    @jsii.member(jsii_name="customConfigureRecipes")
    def custom_configure_recipes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "customConfigureRecipes"))

    @custom_configure_recipes.setter
    def custom_configure_recipes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__096de7b88b7cca22bdc72f0ab619baefc9890e655f776826ef45f2292d1db07d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customConfigureRecipes", value)

    @builtins.property
    @jsii.member(jsii_name="customDeployRecipes")
    def custom_deploy_recipes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "customDeployRecipes"))

    @custom_deploy_recipes.setter
    def custom_deploy_recipes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93f783d6d9bb13f29eb47d392782b477472d1c80f4fa165b3455ea1ffd3e6392)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customDeployRecipes", value)

    @builtins.property
    @jsii.member(jsii_name="customInstanceProfileArn")
    def custom_instance_profile_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customInstanceProfileArn"))

    @custom_instance_profile_arn.setter
    def custom_instance_profile_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__69b7e3b4c94cebc58baae2f0f2db4f163afb72da76c0307ae02f9feda20dac82)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customInstanceProfileArn", value)

    @builtins.property
    @jsii.member(jsii_name="customJson")
    def custom_json(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customJson"))

    @custom_json.setter
    def custom_json(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92b7b00c762da0f5855ee138ca9201ae8a1565a2a115566957c68653b2b19950)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customJson", value)

    @builtins.property
    @jsii.member(jsii_name="customSecurityGroupIds")
    def custom_security_group_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "customSecurityGroupIds"))

    @custom_security_group_ids.setter
    def custom_security_group_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2989d55fed501091cad6c9d89990e710e7d966ee896d88e2f1d226f07641b971)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customSecurityGroupIds", value)

    @builtins.property
    @jsii.member(jsii_name="customSetupRecipes")
    def custom_setup_recipes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "customSetupRecipes"))

    @custom_setup_recipes.setter
    def custom_setup_recipes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__824b2a5948f3ae08ec61a6cef7e6cc14e3614373cca29466d900843116070f7b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customSetupRecipes", value)

    @builtins.property
    @jsii.member(jsii_name="customShutdownRecipes")
    def custom_shutdown_recipes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "customShutdownRecipes"))

    @custom_shutdown_recipes.setter
    def custom_shutdown_recipes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d49d973900ff1f26e1900584620c5e7277483bdb8aa444fc9c13e12952cd907)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customShutdownRecipes", value)

    @builtins.property
    @jsii.member(jsii_name="customUndeployRecipes")
    def custom_undeploy_recipes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "customUndeployRecipes"))

    @custom_undeploy_recipes.setter
    def custom_undeploy_recipes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__707f7ca60520481abbdefe79ae66526d698478fe1c72ff12e00fb54d4953cc82)
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
            type_hints = typing.get_type_hints(_typecheckingstub__920e3728eafd41138a7c0fb55eec19feab4ffff9716ade76f3aa0c9d2adc942c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "drainElbOnShutdown", value)

    @builtins.property
    @jsii.member(jsii_name="elasticLoadBalancer")
    def elastic_load_balancer(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "elasticLoadBalancer"))

    @elastic_load_balancer.setter
    def elastic_load_balancer(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2736d5bdcb5d8d8993ea8a9056db0b9d82adbaf3704ef4d28c051ffde494bb9e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "elasticLoadBalancer", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ef9479c72139e15311bf553c3aff750c6ce7e628d64cdc4b9980288107d03fb)
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
            type_hints = typing.get_type_hints(_typecheckingstub__baefc0486aef5fa4da8e8591bbee16b5264002fe85ec6e4880d6d3e43aa83ff6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "installUpdatesOnBoot", value)

    @builtins.property
    @jsii.member(jsii_name="instanceShutdownTimeout")
    def instance_shutdown_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "instanceShutdownTimeout"))

    @instance_shutdown_timeout.setter
    def instance_shutdown_timeout(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3a03ca6f373ceda2f00d3574b4659ad42643f9c58af1cfa10303290c4871956)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceShutdownTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff3804a834d6495bcff0422762f71307c94a4da1c28ad451d2c32404f2d12590)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70936c25cdb04a81209781be2e3ade2d4cfe2fc1e53977607a57356cdf8acf52)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="stackId")
    def stack_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "stackId"))

    @stack_id.setter
    def stack_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__531a323ac9c079d5ced07632f97e1ad2d2b4cbcc500cf9e27b05851a877dfcc6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stackId", value)

    @builtins.property
    @jsii.member(jsii_name="systemPackages")
    def system_packages(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "systemPackages"))

    @system_packages.setter
    def system_packages(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09a5a001a3ca7128e884188f91268fdc81513dca090e5d5b8d8583416d3ebbf8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "systemPackages", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d623259445d87a6d88a579c356f0d6609ac204761fe573542171274cef9f9b25)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__addd2b97806670154a0c1903695c14f1b88192f5812a2bace4e0e23e552b8b5c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @url.setter
    def url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7bb600dbb08836cbe5ede4bf133d00d2a4287b0faf8a56825972616bf3fb2037)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__bb479b548ff600faa8de8c73f986491dab9a98ab3396f064eef69f2394fbace4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useEbsOptimizedInstances", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93abdde4cfe1e9799634fdda586074064b9daf07786b0ce93638f6f4fea11bc7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)


@jsii.data_type(
    jsii_type="aws.opsworksGangliaLayer.OpsworksGangliaLayerCloudwatchConfiguration",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "log_streams": "logStreams"},
)
class OpsworksGangliaLayerCloudwatchConfiguration:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        log_streams: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["OpsworksGangliaLayerCloudwatchConfigurationLogStreams", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#enabled OpsworksGangliaLayer#enabled}.
        :param log_streams: log_streams block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#log_streams OpsworksGangliaLayer#log_streams}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b965a76a1a8f74560f76c05c88db7da4c8cf7f2779313bf8de8f16e2894d8374)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#enabled OpsworksGangliaLayer#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def log_streams(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["OpsworksGangliaLayerCloudwatchConfigurationLogStreams"]]]:
        '''log_streams block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#log_streams OpsworksGangliaLayer#log_streams}
        '''
        result = self._values.get("log_streams")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["OpsworksGangliaLayerCloudwatchConfigurationLogStreams"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OpsworksGangliaLayerCloudwatchConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.opsworksGangliaLayer.OpsworksGangliaLayerCloudwatchConfigurationLogStreams",
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
class OpsworksGangliaLayerCloudwatchConfigurationLogStreams:
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
        :param file: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#file OpsworksGangliaLayer#file}.
        :param log_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#log_group_name OpsworksGangliaLayer#log_group_name}.
        :param batch_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#batch_count OpsworksGangliaLayer#batch_count}.
        :param batch_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#batch_size OpsworksGangliaLayer#batch_size}.
        :param buffer_duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#buffer_duration OpsworksGangliaLayer#buffer_duration}.
        :param datetime_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#datetime_format OpsworksGangliaLayer#datetime_format}.
        :param encoding: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#encoding OpsworksGangliaLayer#encoding}.
        :param file_fingerprint_lines: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#file_fingerprint_lines OpsworksGangliaLayer#file_fingerprint_lines}.
        :param initial_position: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#initial_position OpsworksGangliaLayer#initial_position}.
        :param multiline_start_pattern: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#multiline_start_pattern OpsworksGangliaLayer#multiline_start_pattern}.
        :param time_zone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#time_zone OpsworksGangliaLayer#time_zone}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__310bb3a4cc2b8a3daf043e2bd92569ae46e8890df886bc4c0b13cd9d1559b092)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#file OpsworksGangliaLayer#file}.'''
        result = self._values.get("file")
        assert result is not None, "Required property 'file' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def log_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#log_group_name OpsworksGangliaLayer#log_group_name}.'''
        result = self._values.get("log_group_name")
        assert result is not None, "Required property 'log_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def batch_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#batch_count OpsworksGangliaLayer#batch_count}.'''
        result = self._values.get("batch_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def batch_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#batch_size OpsworksGangliaLayer#batch_size}.'''
        result = self._values.get("batch_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def buffer_duration(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#buffer_duration OpsworksGangliaLayer#buffer_duration}.'''
        result = self._values.get("buffer_duration")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def datetime_format(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#datetime_format OpsworksGangliaLayer#datetime_format}.'''
        result = self._values.get("datetime_format")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encoding(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#encoding OpsworksGangliaLayer#encoding}.'''
        result = self._values.get("encoding")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def file_fingerprint_lines(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#file_fingerprint_lines OpsworksGangliaLayer#file_fingerprint_lines}.'''
        result = self._values.get("file_fingerprint_lines")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def initial_position(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#initial_position OpsworksGangliaLayer#initial_position}.'''
        result = self._values.get("initial_position")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def multiline_start_pattern(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#multiline_start_pattern OpsworksGangliaLayer#multiline_start_pattern}.'''
        result = self._values.get("multiline_start_pattern")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def time_zone(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#time_zone OpsworksGangliaLayer#time_zone}.'''
        result = self._values.get("time_zone")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OpsworksGangliaLayerCloudwatchConfigurationLogStreams(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OpsworksGangliaLayerCloudwatchConfigurationLogStreamsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.opsworksGangliaLayer.OpsworksGangliaLayerCloudwatchConfigurationLogStreamsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__92458f68457346ef082b31946fa47357b2b1c2a45f299d6e1fb226bd8bce4983)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "OpsworksGangliaLayerCloudwatchConfigurationLogStreamsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f0a9139e475d1d69bdfbc939d3044efb4400e4fa021b5e9e7b70073a7e4a6ea2)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("OpsworksGangliaLayerCloudwatchConfigurationLogStreamsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__46b78a14c8a3af4eacfa4efe9bde18aa5204eff0a3e6bcdc05dec0aa045da7ed)
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
            type_hints = typing.get_type_hints(_typecheckingstub__84543c07e91b5231f99b392e8e5968b2fd89af7028ddd2cf080c90502d38c1c1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5426ada6e55ad3d77aef199f2903b3773766747ea4230cf2ceb947144616eb9b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[OpsworksGangliaLayerCloudwatchConfigurationLogStreams]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[OpsworksGangliaLayerCloudwatchConfigurationLogStreams]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[OpsworksGangliaLayerCloudwatchConfigurationLogStreams]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6037c276b21f675163c19ca4bbbb807cd182e8bc5b9d6a7323d76c33e98153c0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OpsworksGangliaLayerCloudwatchConfigurationLogStreamsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.opsworksGangliaLayer.OpsworksGangliaLayerCloudwatchConfigurationLogStreamsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__116e59ff35e494a29ec47529c5ea5149a989ee8e35d96534c3373c08cfa15737)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6c066daf3041cd83da3668fe980a673667bd18927bcbb4e27ead6cbf87416e14)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "batchCount", value)

    @builtins.property
    @jsii.member(jsii_name="batchSize")
    def batch_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "batchSize"))

    @batch_size.setter
    def batch_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e29f97999a9025942ffed925f2527e0499428ded7f0e14efb0a04f32107de244)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "batchSize", value)

    @builtins.property
    @jsii.member(jsii_name="bufferDuration")
    def buffer_duration(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "bufferDuration"))

    @buffer_duration.setter
    def buffer_duration(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__caea327e32489f3b864fcb947a0eb41ddb16291977afff666d41d9ffca823a99)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bufferDuration", value)

    @builtins.property
    @jsii.member(jsii_name="datetimeFormat")
    def datetime_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datetimeFormat"))

    @datetime_format.setter
    def datetime_format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a8dfa1490466acd35877b0c8abba5159a2654cb49805f7c84817a1525974799)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datetimeFormat", value)

    @builtins.property
    @jsii.member(jsii_name="encoding")
    def encoding(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "encoding"))

    @encoding.setter
    def encoding(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__36895d386fb8fccee0b6b7124e02f1a2165aa526104c3b5e1af1e10bfe815064)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encoding", value)

    @builtins.property
    @jsii.member(jsii_name="file")
    def file(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "file"))

    @file.setter
    def file(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40087d099f3345e6c5f949fbadfc7e8b9ceee0886f5dd5c28f13928074956360)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "file", value)

    @builtins.property
    @jsii.member(jsii_name="fileFingerprintLines")
    def file_fingerprint_lines(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fileFingerprintLines"))

    @file_fingerprint_lines.setter
    def file_fingerprint_lines(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c06e1d7546d04cc14dac745aa4b4f24124eb96595ecbb875cdf7a76a32493928)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileFingerprintLines", value)

    @builtins.property
    @jsii.member(jsii_name="initialPosition")
    def initial_position(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "initialPosition"))

    @initial_position.setter
    def initial_position(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bbfe5c7e5e7ee7255d5576412529e26bcdce66a0e5e639b9bdec00bfff597b54)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "initialPosition", value)

    @builtins.property
    @jsii.member(jsii_name="logGroupName")
    def log_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logGroupName"))

    @log_group_name.setter
    def log_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b967ddc8e3ddd6715e4dcabe2fe8b3a85446f6ff75e06c3c5048bd6e1e7f114e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="multilineStartPattern")
    def multiline_start_pattern(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "multilineStartPattern"))

    @multiline_start_pattern.setter
    def multiline_start_pattern(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e623f7d0cbb2197ae979bd55c026b6a109a24581fda8ed9de2ecaa38b05d7b10)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "multilineStartPattern", value)

    @builtins.property
    @jsii.member(jsii_name="timeZone")
    def time_zone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timeZone"))

    @time_zone.setter
    def time_zone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8822b4a95877af73f01dca28b7ecc0d424080f16ce8238192227deb7cba2869d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeZone", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[OpsworksGangliaLayerCloudwatchConfigurationLogStreams, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[OpsworksGangliaLayerCloudwatchConfigurationLogStreams, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[OpsworksGangliaLayerCloudwatchConfigurationLogStreams, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d337418483981119caba4d8a683ac24de2d4aab540eede53367ee15920d8216e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OpsworksGangliaLayerCloudwatchConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.opsworksGangliaLayer.OpsworksGangliaLayerCloudwatchConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__383acc1d1e25bb5028a5f94e70ade6948e7c891f17877e41fc74f62e526fc8d9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putLogStreams")
    def put_log_streams(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[OpsworksGangliaLayerCloudwatchConfigurationLogStreams, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__88b6074e48fcbaa8f28b1965a1832ea0a5017aa5bd36797401bc6c79483093bf)
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
    def log_streams(self) -> OpsworksGangliaLayerCloudwatchConfigurationLogStreamsList:
        return typing.cast(OpsworksGangliaLayerCloudwatchConfigurationLogStreamsList, jsii.get(self, "logStreams"))

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
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[OpsworksGangliaLayerCloudwatchConfigurationLogStreams]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[OpsworksGangliaLayerCloudwatchConfigurationLogStreams]]], jsii.get(self, "logStreamsInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__7aa2f061d437bc657058414d03784d49d634eec9f9e5b84fd42d532ee66ab5c1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[OpsworksGangliaLayerCloudwatchConfiguration]:
        return typing.cast(typing.Optional[OpsworksGangliaLayerCloudwatchConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OpsworksGangliaLayerCloudwatchConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7aa78ddcc7b7fc288b00c6118135bbcfbd3c90c5b961115ff4a665489e590b1e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.opsworksGangliaLayer.OpsworksGangliaLayerConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "password": "password",
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
        "url": "url",
        "use_ebs_optimized_instances": "useEbsOptimizedInstances",
        "username": "username",
    },
)
class OpsworksGangliaLayerConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        password: builtins.str,
        stack_id: builtins.str,
        auto_assign_elastic_ips: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        auto_assign_public_ips: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        auto_healing: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        cloudwatch_configuration: typing.Optional[typing.Union[OpsworksGangliaLayerCloudwatchConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
        custom_configure_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
        custom_deploy_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
        custom_instance_profile_arn: typing.Optional[builtins.str] = None,
        custom_json: typing.Optional[builtins.str] = None,
        custom_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        custom_setup_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
        custom_shutdown_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
        custom_undeploy_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
        drain_elb_on_shutdown: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        ebs_volume: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["OpsworksGangliaLayerEbsVolume", typing.Dict[builtins.str, typing.Any]]]]] = None,
        elastic_load_balancer: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        install_updates_on_boot: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        instance_shutdown_timeout: typing.Optional[jsii.Number] = None,
        load_based_auto_scaling: typing.Optional[typing.Union["OpsworksGangliaLayerLoadBasedAutoScaling", typing.Dict[builtins.str, typing.Any]]] = None,
        name: typing.Optional[builtins.str] = None,
        system_packages: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        url: typing.Optional[builtins.str] = None,
        use_ebs_optimized_instances: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#password OpsworksGangliaLayer#password}.
        :param stack_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#stack_id OpsworksGangliaLayer#stack_id}.
        :param auto_assign_elastic_ips: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#auto_assign_elastic_ips OpsworksGangliaLayer#auto_assign_elastic_ips}.
        :param auto_assign_public_ips: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#auto_assign_public_ips OpsworksGangliaLayer#auto_assign_public_ips}.
        :param auto_healing: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#auto_healing OpsworksGangliaLayer#auto_healing}.
        :param cloudwatch_configuration: cloudwatch_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#cloudwatch_configuration OpsworksGangliaLayer#cloudwatch_configuration}
        :param custom_configure_recipes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#custom_configure_recipes OpsworksGangliaLayer#custom_configure_recipes}.
        :param custom_deploy_recipes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#custom_deploy_recipes OpsworksGangliaLayer#custom_deploy_recipes}.
        :param custom_instance_profile_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#custom_instance_profile_arn OpsworksGangliaLayer#custom_instance_profile_arn}.
        :param custom_json: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#custom_json OpsworksGangliaLayer#custom_json}.
        :param custom_security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#custom_security_group_ids OpsworksGangliaLayer#custom_security_group_ids}.
        :param custom_setup_recipes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#custom_setup_recipes OpsworksGangliaLayer#custom_setup_recipes}.
        :param custom_shutdown_recipes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#custom_shutdown_recipes OpsworksGangliaLayer#custom_shutdown_recipes}.
        :param custom_undeploy_recipes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#custom_undeploy_recipes OpsworksGangliaLayer#custom_undeploy_recipes}.
        :param drain_elb_on_shutdown: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#drain_elb_on_shutdown OpsworksGangliaLayer#drain_elb_on_shutdown}.
        :param ebs_volume: ebs_volume block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#ebs_volume OpsworksGangliaLayer#ebs_volume}
        :param elastic_load_balancer: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#elastic_load_balancer OpsworksGangliaLayer#elastic_load_balancer}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#id OpsworksGangliaLayer#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param install_updates_on_boot: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#install_updates_on_boot OpsworksGangliaLayer#install_updates_on_boot}.
        :param instance_shutdown_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#instance_shutdown_timeout OpsworksGangliaLayer#instance_shutdown_timeout}.
        :param load_based_auto_scaling: load_based_auto_scaling block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#load_based_auto_scaling OpsworksGangliaLayer#load_based_auto_scaling}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#name OpsworksGangliaLayer#name}.
        :param system_packages: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#system_packages OpsworksGangliaLayer#system_packages}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#tags OpsworksGangliaLayer#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#tags_all OpsworksGangliaLayer#tags_all}.
        :param url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#url OpsworksGangliaLayer#url}.
        :param use_ebs_optimized_instances: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#use_ebs_optimized_instances OpsworksGangliaLayer#use_ebs_optimized_instances}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#username OpsworksGangliaLayer#username}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(cloudwatch_configuration, dict):
            cloudwatch_configuration = OpsworksGangliaLayerCloudwatchConfiguration(**cloudwatch_configuration)
        if isinstance(load_based_auto_scaling, dict):
            load_based_auto_scaling = OpsworksGangliaLayerLoadBasedAutoScaling(**load_based_auto_scaling)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4f057a75f7b1d442392235641fa820d4415b097e423b8bb0525ff0f97aab9fc)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
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
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            check_type(argname="argument use_ebs_optimized_instances", value=use_ebs_optimized_instances, expected_type=type_hints["use_ebs_optimized_instances"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "password": password,
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
        if url is not None:
            self._values["url"] = url
        if use_ebs_optimized_instances is not None:
            self._values["use_ebs_optimized_instances"] = use_ebs_optimized_instances
        if username is not None:
            self._values["username"] = username

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
    def password(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#password OpsworksGangliaLayer#password}.'''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def stack_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#stack_id OpsworksGangliaLayer#stack_id}.'''
        result = self._values.get("stack_id")
        assert result is not None, "Required property 'stack_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def auto_assign_elastic_ips(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#auto_assign_elastic_ips OpsworksGangliaLayer#auto_assign_elastic_ips}.'''
        result = self._values.get("auto_assign_elastic_ips")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def auto_assign_public_ips(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#auto_assign_public_ips OpsworksGangliaLayer#auto_assign_public_ips}.'''
        result = self._values.get("auto_assign_public_ips")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def auto_healing(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#auto_healing OpsworksGangliaLayer#auto_healing}.'''
        result = self._values.get("auto_healing")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def cloudwatch_configuration(
        self,
    ) -> typing.Optional[OpsworksGangliaLayerCloudwatchConfiguration]:
        '''cloudwatch_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#cloudwatch_configuration OpsworksGangliaLayer#cloudwatch_configuration}
        '''
        result = self._values.get("cloudwatch_configuration")
        return typing.cast(typing.Optional[OpsworksGangliaLayerCloudwatchConfiguration], result)

    @builtins.property
    def custom_configure_recipes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#custom_configure_recipes OpsworksGangliaLayer#custom_configure_recipes}.'''
        result = self._values.get("custom_configure_recipes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def custom_deploy_recipes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#custom_deploy_recipes OpsworksGangliaLayer#custom_deploy_recipes}.'''
        result = self._values.get("custom_deploy_recipes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def custom_instance_profile_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#custom_instance_profile_arn OpsworksGangliaLayer#custom_instance_profile_arn}.'''
        result = self._values.get("custom_instance_profile_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_json(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#custom_json OpsworksGangliaLayer#custom_json}.'''
        result = self._values.get("custom_json")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#custom_security_group_ids OpsworksGangliaLayer#custom_security_group_ids}.'''
        result = self._values.get("custom_security_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def custom_setup_recipes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#custom_setup_recipes OpsworksGangliaLayer#custom_setup_recipes}.'''
        result = self._values.get("custom_setup_recipes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def custom_shutdown_recipes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#custom_shutdown_recipes OpsworksGangliaLayer#custom_shutdown_recipes}.'''
        result = self._values.get("custom_shutdown_recipes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def custom_undeploy_recipes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#custom_undeploy_recipes OpsworksGangliaLayer#custom_undeploy_recipes}.'''
        result = self._values.get("custom_undeploy_recipes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def drain_elb_on_shutdown(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#drain_elb_on_shutdown OpsworksGangliaLayer#drain_elb_on_shutdown}.'''
        result = self._values.get("drain_elb_on_shutdown")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def ebs_volume(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["OpsworksGangliaLayerEbsVolume"]]]:
        '''ebs_volume block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#ebs_volume OpsworksGangliaLayer#ebs_volume}
        '''
        result = self._values.get("ebs_volume")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["OpsworksGangliaLayerEbsVolume"]]], result)

    @builtins.property
    def elastic_load_balancer(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#elastic_load_balancer OpsworksGangliaLayer#elastic_load_balancer}.'''
        result = self._values.get("elastic_load_balancer")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#id OpsworksGangliaLayer#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def install_updates_on_boot(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#install_updates_on_boot OpsworksGangliaLayer#install_updates_on_boot}.'''
        result = self._values.get("install_updates_on_boot")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def instance_shutdown_timeout(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#instance_shutdown_timeout OpsworksGangliaLayer#instance_shutdown_timeout}.'''
        result = self._values.get("instance_shutdown_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def load_based_auto_scaling(
        self,
    ) -> typing.Optional["OpsworksGangliaLayerLoadBasedAutoScaling"]:
        '''load_based_auto_scaling block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#load_based_auto_scaling OpsworksGangliaLayer#load_based_auto_scaling}
        '''
        result = self._values.get("load_based_auto_scaling")
        return typing.cast(typing.Optional["OpsworksGangliaLayerLoadBasedAutoScaling"], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#name OpsworksGangliaLayer#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def system_packages(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#system_packages OpsworksGangliaLayer#system_packages}.'''
        result = self._values.get("system_packages")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#tags OpsworksGangliaLayer#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#tags_all OpsworksGangliaLayer#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#url OpsworksGangliaLayer#url}.'''
        result = self._values.get("url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def use_ebs_optimized_instances(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#use_ebs_optimized_instances OpsworksGangliaLayer#use_ebs_optimized_instances}.'''
        result = self._values.get("use_ebs_optimized_instances")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#username OpsworksGangliaLayer#username}.'''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OpsworksGangliaLayerConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.opsworksGangliaLayer.OpsworksGangliaLayerEbsVolume",
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
class OpsworksGangliaLayerEbsVolume:
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
        :param mount_point: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#mount_point OpsworksGangliaLayer#mount_point}.
        :param number_of_disks: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#number_of_disks OpsworksGangliaLayer#number_of_disks}.
        :param size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#size OpsworksGangliaLayer#size}.
        :param encrypted: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#encrypted OpsworksGangliaLayer#encrypted}.
        :param iops: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#iops OpsworksGangliaLayer#iops}.
        :param raid_level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#raid_level OpsworksGangliaLayer#raid_level}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#type OpsworksGangliaLayer#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b73a5ab79260392b913bb7926df0a1fae6cdfe84c76ca31837978b0154cf0017)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#mount_point OpsworksGangliaLayer#mount_point}.'''
        result = self._values.get("mount_point")
        assert result is not None, "Required property 'mount_point' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def number_of_disks(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#number_of_disks OpsworksGangliaLayer#number_of_disks}.'''
        result = self._values.get("number_of_disks")
        assert result is not None, "Required property 'number_of_disks' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def size(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#size OpsworksGangliaLayer#size}.'''
        result = self._values.get("size")
        assert result is not None, "Required property 'size' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def encrypted(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#encrypted OpsworksGangliaLayer#encrypted}.'''
        result = self._values.get("encrypted")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def iops(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#iops OpsworksGangliaLayer#iops}.'''
        result = self._values.get("iops")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def raid_level(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#raid_level OpsworksGangliaLayer#raid_level}.'''
        result = self._values.get("raid_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#type OpsworksGangliaLayer#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OpsworksGangliaLayerEbsVolume(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OpsworksGangliaLayerEbsVolumeList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.opsworksGangliaLayer.OpsworksGangliaLayerEbsVolumeList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__02f8a2ad8acab6217f225b6b12865b87a1a16329caefc99456b508041179f07f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "OpsworksGangliaLayerEbsVolumeOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f05809a9eb3abbed056d19e65787ff5fd286748bb149e92494f2ef25a218a76)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("OpsworksGangliaLayerEbsVolumeOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17e3d0d8d4c92e62b8a9e61cddbb28d26bb6942118c24049638d0eff053b576b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__08d1c19bb7d16c0273e4706e5c35bff1fd7c4c611385b2788d7b313e410fdd7d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b3808459bf903579eaccf3ed40f16319310fae9931ea330790ca5054863470e2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[OpsworksGangliaLayerEbsVolume]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[OpsworksGangliaLayerEbsVolume]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[OpsworksGangliaLayerEbsVolume]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72cbfd65f3e52ac94b6390a5843abc73c5eb109d13885848431a0633084ceb95)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OpsworksGangliaLayerEbsVolumeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.opsworksGangliaLayer.OpsworksGangliaLayerEbsVolumeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b2ce56b16228f72ba62541f06a7abe2c1761b49eb24125ee990c2d089c9ec332)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f1b6f79d5120b719939bcde794794ff695d85740501392beab93e46b5533f460)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encrypted", value)

    @builtins.property
    @jsii.member(jsii_name="iops")
    def iops(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "iops"))

    @iops.setter
    def iops(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__178cc8049cb2e3fb81b7a26efbf7c2fe001f1ab31779ebc0823e7030426bf721)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iops", value)

    @builtins.property
    @jsii.member(jsii_name="mountPoint")
    def mount_point(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mountPoint"))

    @mount_point.setter
    def mount_point(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a850cd5532f5ed7bdf540328651ee32617842439f185da7127f99eddf658ac3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mountPoint", value)

    @builtins.property
    @jsii.member(jsii_name="numberOfDisks")
    def number_of_disks(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "numberOfDisks"))

    @number_of_disks.setter
    def number_of_disks(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8b35275b6713809852173de4f19cb7a601a3b27102ad9d4c2e3b4edf91268b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "numberOfDisks", value)

    @builtins.property
    @jsii.member(jsii_name="raidLevel")
    def raid_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "raidLevel"))

    @raid_level.setter
    def raid_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a04fbd39de3f13da8266810b7385e9c888ffe6209d6cecb1efb8ef89eaee0462)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "raidLevel", value)

    @builtins.property
    @jsii.member(jsii_name="size")
    def size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "size"))

    @size.setter
    def size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01274e3fbcd450bcdec79164f5ba8a96de701aee605a37ef41c94ae593b15188)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "size", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ebe47bbeca71fed8f0374a851953ce5db33d56069a7a348b5fd89ecd7a935835)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[OpsworksGangliaLayerEbsVolume, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[OpsworksGangliaLayerEbsVolume, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[OpsworksGangliaLayerEbsVolume, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9b73d7ee6cfe511fe11457f32bd9541608100af8d94ea5e9bc4bd4f8ed497a6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.opsworksGangliaLayer.OpsworksGangliaLayerLoadBasedAutoScaling",
    jsii_struct_bases=[],
    name_mapping={
        "downscaling": "downscaling",
        "enable": "enable",
        "upscaling": "upscaling",
    },
)
class OpsworksGangliaLayerLoadBasedAutoScaling:
    def __init__(
        self,
        *,
        downscaling: typing.Optional[typing.Union["OpsworksGangliaLayerLoadBasedAutoScalingDownscaling", typing.Dict[builtins.str, typing.Any]]] = None,
        enable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        upscaling: typing.Optional[typing.Union["OpsworksGangliaLayerLoadBasedAutoScalingUpscaling", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param downscaling: downscaling block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#downscaling OpsworksGangliaLayer#downscaling}
        :param enable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#enable OpsworksGangliaLayer#enable}.
        :param upscaling: upscaling block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#upscaling OpsworksGangliaLayer#upscaling}
        '''
        if isinstance(downscaling, dict):
            downscaling = OpsworksGangliaLayerLoadBasedAutoScalingDownscaling(**downscaling)
        if isinstance(upscaling, dict):
            upscaling = OpsworksGangliaLayerLoadBasedAutoScalingUpscaling(**upscaling)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0007f45f989d57bb4081b5183aedff91d535e0eb9ab2f39e59aef30e38f266f4)
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
    ) -> typing.Optional["OpsworksGangliaLayerLoadBasedAutoScalingDownscaling"]:
        '''downscaling block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#downscaling OpsworksGangliaLayer#downscaling}
        '''
        result = self._values.get("downscaling")
        return typing.cast(typing.Optional["OpsworksGangliaLayerLoadBasedAutoScalingDownscaling"], result)

    @builtins.property
    def enable(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#enable OpsworksGangliaLayer#enable}.'''
        result = self._values.get("enable")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def upscaling(
        self,
    ) -> typing.Optional["OpsworksGangliaLayerLoadBasedAutoScalingUpscaling"]:
        '''upscaling block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#upscaling OpsworksGangliaLayer#upscaling}
        '''
        result = self._values.get("upscaling")
        return typing.cast(typing.Optional["OpsworksGangliaLayerLoadBasedAutoScalingUpscaling"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OpsworksGangliaLayerLoadBasedAutoScaling(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.opsworksGangliaLayer.OpsworksGangliaLayerLoadBasedAutoScalingDownscaling",
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
class OpsworksGangliaLayerLoadBasedAutoScalingDownscaling:
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
        :param alarms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#alarms OpsworksGangliaLayer#alarms}.
        :param cpu_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#cpu_threshold OpsworksGangliaLayer#cpu_threshold}.
        :param ignore_metrics_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#ignore_metrics_time OpsworksGangliaLayer#ignore_metrics_time}.
        :param instance_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#instance_count OpsworksGangliaLayer#instance_count}.
        :param load_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#load_threshold OpsworksGangliaLayer#load_threshold}.
        :param memory_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#memory_threshold OpsworksGangliaLayer#memory_threshold}.
        :param thresholds_wait_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#thresholds_wait_time OpsworksGangliaLayer#thresholds_wait_time}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ddcd045f8a9659e52681eb871d24f3782aa596c4b922657b8746422f6b93f628)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#alarms OpsworksGangliaLayer#alarms}.'''
        result = self._values.get("alarms")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def cpu_threshold(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#cpu_threshold OpsworksGangliaLayer#cpu_threshold}.'''
        result = self._values.get("cpu_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ignore_metrics_time(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#ignore_metrics_time OpsworksGangliaLayer#ignore_metrics_time}.'''
        result = self._values.get("ignore_metrics_time")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def instance_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#instance_count OpsworksGangliaLayer#instance_count}.'''
        result = self._values.get("instance_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def load_threshold(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#load_threshold OpsworksGangliaLayer#load_threshold}.'''
        result = self._values.get("load_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def memory_threshold(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#memory_threshold OpsworksGangliaLayer#memory_threshold}.'''
        result = self._values.get("memory_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def thresholds_wait_time(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#thresholds_wait_time OpsworksGangliaLayer#thresholds_wait_time}.'''
        result = self._values.get("thresholds_wait_time")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OpsworksGangliaLayerLoadBasedAutoScalingDownscaling(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OpsworksGangliaLayerLoadBasedAutoScalingDownscalingOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.opsworksGangliaLayer.OpsworksGangliaLayerLoadBasedAutoScalingDownscalingOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c1e66e84af9b29638e33319e0ba80bf5c4f55c36e12573bd2616c704f80fd89f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__729967760e3ff365c5403a5b66f212c8b27c115bcdd88a1703e1400a311217b2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alarms", value)

    @builtins.property
    @jsii.member(jsii_name="cpuThreshold")
    def cpu_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "cpuThreshold"))

    @cpu_threshold.setter
    def cpu_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df603b0fe382770702f83cf4b88d41f69dbb3d9e6e9beb27cbdfafc5c5a1e992)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpuThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="ignoreMetricsTime")
    def ignore_metrics_time(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ignoreMetricsTime"))

    @ignore_metrics_time.setter
    def ignore_metrics_time(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__816431ec9a627ee39784005c0f1bc24e4a7214e4b297172bc151abb8f6e55853)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ignoreMetricsTime", value)

    @builtins.property
    @jsii.member(jsii_name="instanceCount")
    def instance_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "instanceCount"))

    @instance_count.setter
    def instance_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4393e3bc59cf98561ba15449eb1841b34fec4037855ee0ccf68039b2971369b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceCount", value)

    @builtins.property
    @jsii.member(jsii_name="loadThreshold")
    def load_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "loadThreshold"))

    @load_threshold.setter
    def load_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__feb01b943c4fba07e302014ed86ddc0817328a7facdea76ef7f3e84c4ce6bdd3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loadThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="memoryThreshold")
    def memory_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "memoryThreshold"))

    @memory_threshold.setter
    def memory_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23640c5d546792afb6bcbca16a7701e09af6c3523618c7d93028f5b562c01dda)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memoryThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="thresholdsWaitTime")
    def thresholds_wait_time(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "thresholdsWaitTime"))

    @thresholds_wait_time.setter
    def thresholds_wait_time(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__36bc2ec455301bb34e410618c63869a715db0ae9084151652831ae4ce7c2ece1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "thresholdsWaitTime", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[OpsworksGangliaLayerLoadBasedAutoScalingDownscaling]:
        return typing.cast(typing.Optional[OpsworksGangliaLayerLoadBasedAutoScalingDownscaling], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OpsworksGangliaLayerLoadBasedAutoScalingDownscaling],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f5f86d784acc4736fa3e4e6928375d3114d130387cd7845d548f7f276fa6f13)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OpsworksGangliaLayerLoadBasedAutoScalingOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.opsworksGangliaLayer.OpsworksGangliaLayerLoadBasedAutoScalingOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b4a67c44c3ff64dbdaec7852821972c2af47dfb5a8cb046542241d121ecfeaa5)
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
        :param alarms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#alarms OpsworksGangliaLayer#alarms}.
        :param cpu_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#cpu_threshold OpsworksGangliaLayer#cpu_threshold}.
        :param ignore_metrics_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#ignore_metrics_time OpsworksGangliaLayer#ignore_metrics_time}.
        :param instance_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#instance_count OpsworksGangliaLayer#instance_count}.
        :param load_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#load_threshold OpsworksGangliaLayer#load_threshold}.
        :param memory_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#memory_threshold OpsworksGangliaLayer#memory_threshold}.
        :param thresholds_wait_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#thresholds_wait_time OpsworksGangliaLayer#thresholds_wait_time}.
        '''
        value = OpsworksGangliaLayerLoadBasedAutoScalingDownscaling(
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
        :param alarms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#alarms OpsworksGangliaLayer#alarms}.
        :param cpu_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#cpu_threshold OpsworksGangliaLayer#cpu_threshold}.
        :param ignore_metrics_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#ignore_metrics_time OpsworksGangliaLayer#ignore_metrics_time}.
        :param instance_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#instance_count OpsworksGangliaLayer#instance_count}.
        :param load_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#load_threshold OpsworksGangliaLayer#load_threshold}.
        :param memory_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#memory_threshold OpsworksGangliaLayer#memory_threshold}.
        :param thresholds_wait_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#thresholds_wait_time OpsworksGangliaLayer#thresholds_wait_time}.
        '''
        value = OpsworksGangliaLayerLoadBasedAutoScalingUpscaling(
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
    ) -> OpsworksGangliaLayerLoadBasedAutoScalingDownscalingOutputReference:
        return typing.cast(OpsworksGangliaLayerLoadBasedAutoScalingDownscalingOutputReference, jsii.get(self, "downscaling"))

    @builtins.property
    @jsii.member(jsii_name="upscaling")
    def upscaling(
        self,
    ) -> "OpsworksGangliaLayerLoadBasedAutoScalingUpscalingOutputReference":
        return typing.cast("OpsworksGangliaLayerLoadBasedAutoScalingUpscalingOutputReference", jsii.get(self, "upscaling"))

    @builtins.property
    @jsii.member(jsii_name="downscalingInput")
    def downscaling_input(
        self,
    ) -> typing.Optional[OpsworksGangliaLayerLoadBasedAutoScalingDownscaling]:
        return typing.cast(typing.Optional[OpsworksGangliaLayerLoadBasedAutoScalingDownscaling], jsii.get(self, "downscalingInput"))

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
    ) -> typing.Optional["OpsworksGangliaLayerLoadBasedAutoScalingUpscaling"]:
        return typing.cast(typing.Optional["OpsworksGangliaLayerLoadBasedAutoScalingUpscaling"], jsii.get(self, "upscalingInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__f0da2150f8de1cd1db97e1f37823a747b95aff801da799455db7ca6ef3da3478)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enable", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[OpsworksGangliaLayerLoadBasedAutoScaling]:
        return typing.cast(typing.Optional[OpsworksGangliaLayerLoadBasedAutoScaling], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OpsworksGangliaLayerLoadBasedAutoScaling],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ec7fcfdfe3bae644592f75832abbf14f008200dbe26fb95829ec1944789604e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.opsworksGangliaLayer.OpsworksGangliaLayerLoadBasedAutoScalingUpscaling",
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
class OpsworksGangliaLayerLoadBasedAutoScalingUpscaling:
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
        :param alarms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#alarms OpsworksGangliaLayer#alarms}.
        :param cpu_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#cpu_threshold OpsworksGangliaLayer#cpu_threshold}.
        :param ignore_metrics_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#ignore_metrics_time OpsworksGangliaLayer#ignore_metrics_time}.
        :param instance_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#instance_count OpsworksGangliaLayer#instance_count}.
        :param load_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#load_threshold OpsworksGangliaLayer#load_threshold}.
        :param memory_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#memory_threshold OpsworksGangliaLayer#memory_threshold}.
        :param thresholds_wait_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#thresholds_wait_time OpsworksGangliaLayer#thresholds_wait_time}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__48f4752c57122e3102e8917cc66f6fe078e655874dcf1076c9065c0e804af843)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#alarms OpsworksGangliaLayer#alarms}.'''
        result = self._values.get("alarms")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def cpu_threshold(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#cpu_threshold OpsworksGangliaLayer#cpu_threshold}.'''
        result = self._values.get("cpu_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ignore_metrics_time(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#ignore_metrics_time OpsworksGangliaLayer#ignore_metrics_time}.'''
        result = self._values.get("ignore_metrics_time")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def instance_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#instance_count OpsworksGangliaLayer#instance_count}.'''
        result = self._values.get("instance_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def load_threshold(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#load_threshold OpsworksGangliaLayer#load_threshold}.'''
        result = self._values.get("load_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def memory_threshold(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#memory_threshold OpsworksGangliaLayer#memory_threshold}.'''
        result = self._values.get("memory_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def thresholds_wait_time(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_ganglia_layer#thresholds_wait_time OpsworksGangliaLayer#thresholds_wait_time}.'''
        result = self._values.get("thresholds_wait_time")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OpsworksGangliaLayerLoadBasedAutoScalingUpscaling(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OpsworksGangliaLayerLoadBasedAutoScalingUpscalingOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.opsworksGangliaLayer.OpsworksGangliaLayerLoadBasedAutoScalingUpscalingOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e00d108e6a49de3c5d61c9d81fd4a4d111cf0c4ae9bbc45d19b1d9ace571482d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__955655e60792d33d748ba29e144a8811ab9102021d05d0e2ffc334970c967969)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alarms", value)

    @builtins.property
    @jsii.member(jsii_name="cpuThreshold")
    def cpu_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "cpuThreshold"))

    @cpu_threshold.setter
    def cpu_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66abc90a5bb23703efd3b50b2ae1bd184b9187436220084b504d1aa7fe3a0efd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpuThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="ignoreMetricsTime")
    def ignore_metrics_time(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ignoreMetricsTime"))

    @ignore_metrics_time.setter
    def ignore_metrics_time(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__83b05fa3d1d88b0e00941e66c10902b8388a8c6ba21bec3e11eee89e0509997f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ignoreMetricsTime", value)

    @builtins.property
    @jsii.member(jsii_name="instanceCount")
    def instance_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "instanceCount"))

    @instance_count.setter
    def instance_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f312d55633e27ae0f6d534ca997b7017c95981e8b833a0f8300296c7f2fd0c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceCount", value)

    @builtins.property
    @jsii.member(jsii_name="loadThreshold")
    def load_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "loadThreshold"))

    @load_threshold.setter
    def load_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f3b2e2fd15d9371bb9e861ac7b3e37cd7a1bf40dd3f700a7717ac6cec7f8ca7d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loadThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="memoryThreshold")
    def memory_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "memoryThreshold"))

    @memory_threshold.setter
    def memory_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5dfad35109474c185db2e008e0509b1ce3aec73c9ee5f60062e6830c975abee3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memoryThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="thresholdsWaitTime")
    def thresholds_wait_time(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "thresholdsWaitTime"))

    @thresholds_wait_time.setter
    def thresholds_wait_time(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca46ed3bcac94a4735d5c0d172d76e8b1b4defe38eced6d3743129332ffb053b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "thresholdsWaitTime", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[OpsworksGangliaLayerLoadBasedAutoScalingUpscaling]:
        return typing.cast(typing.Optional[OpsworksGangliaLayerLoadBasedAutoScalingUpscaling], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OpsworksGangliaLayerLoadBasedAutoScalingUpscaling],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58a043de2ce15ed28a01fbee074b0996ecc4d999f1ba610f9fbfe8e70f25cf73)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "OpsworksGangliaLayer",
    "OpsworksGangliaLayerCloudwatchConfiguration",
    "OpsworksGangliaLayerCloudwatchConfigurationLogStreams",
    "OpsworksGangliaLayerCloudwatchConfigurationLogStreamsList",
    "OpsworksGangliaLayerCloudwatchConfigurationLogStreamsOutputReference",
    "OpsworksGangliaLayerCloudwatchConfigurationOutputReference",
    "OpsworksGangliaLayerConfig",
    "OpsworksGangliaLayerEbsVolume",
    "OpsworksGangliaLayerEbsVolumeList",
    "OpsworksGangliaLayerEbsVolumeOutputReference",
    "OpsworksGangliaLayerLoadBasedAutoScaling",
    "OpsworksGangliaLayerLoadBasedAutoScalingDownscaling",
    "OpsworksGangliaLayerLoadBasedAutoScalingDownscalingOutputReference",
    "OpsworksGangliaLayerLoadBasedAutoScalingOutputReference",
    "OpsworksGangliaLayerLoadBasedAutoScalingUpscaling",
    "OpsworksGangliaLayerLoadBasedAutoScalingUpscalingOutputReference",
]

publication.publish()

def _typecheckingstub__12d054284f2c4a19c4df92154e7c8579478fda0b760c0ee73fbd4a24e779b1e4(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    password: builtins.str,
    stack_id: builtins.str,
    auto_assign_elastic_ips: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    auto_assign_public_ips: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    auto_healing: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    cloudwatch_configuration: typing.Optional[typing.Union[OpsworksGangliaLayerCloudwatchConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    custom_configure_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
    custom_deploy_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
    custom_instance_profile_arn: typing.Optional[builtins.str] = None,
    custom_json: typing.Optional[builtins.str] = None,
    custom_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    custom_setup_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
    custom_shutdown_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
    custom_undeploy_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
    drain_elb_on_shutdown: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ebs_volume: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[OpsworksGangliaLayerEbsVolume, typing.Dict[builtins.str, typing.Any]]]]] = None,
    elastic_load_balancer: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    install_updates_on_boot: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    instance_shutdown_timeout: typing.Optional[jsii.Number] = None,
    load_based_auto_scaling: typing.Optional[typing.Union[OpsworksGangliaLayerLoadBasedAutoScaling, typing.Dict[builtins.str, typing.Any]]] = None,
    name: typing.Optional[builtins.str] = None,
    system_packages: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    url: typing.Optional[builtins.str] = None,
    use_ebs_optimized_instances: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    username: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__9f80361d41676e118b337b6eaafb3064a5d9098748c351b3124e379cd052b9fa(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[OpsworksGangliaLayerEbsVolume, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b67780b6b8682e64818807e39e3a52b64d541dd12412a39b4f2e7041254425e(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e529c74f1dccd10749de8795fbf62e8ce1d9e8e6728c41714352968f0c63bc9e(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dfd64b6538dd1c3222fa1bcd292a4ed8835d3303e4ff56bd03b51a995c32c12c(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__096de7b88b7cca22bdc72f0ab619baefc9890e655f776826ef45f2292d1db07d(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93f783d6d9bb13f29eb47d392782b477472d1c80f4fa165b3455ea1ffd3e6392(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69b7e3b4c94cebc58baae2f0f2db4f163afb72da76c0307ae02f9feda20dac82(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92b7b00c762da0f5855ee138ca9201ae8a1565a2a115566957c68653b2b19950(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2989d55fed501091cad6c9d89990e710e7d966ee896d88e2f1d226f07641b971(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__824b2a5948f3ae08ec61a6cef7e6cc14e3614373cca29466d900843116070f7b(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d49d973900ff1f26e1900584620c5e7277483bdb8aa444fc9c13e12952cd907(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__707f7ca60520481abbdefe79ae66526d698478fe1c72ff12e00fb54d4953cc82(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__920e3728eafd41138a7c0fb55eec19feab4ffff9716ade76f3aa0c9d2adc942c(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2736d5bdcb5d8d8993ea8a9056db0b9d82adbaf3704ef4d28c051ffde494bb9e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ef9479c72139e15311bf553c3aff750c6ce7e628d64cdc4b9980288107d03fb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__baefc0486aef5fa4da8e8591bbee16b5264002fe85ec6e4880d6d3e43aa83ff6(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3a03ca6f373ceda2f00d3574b4659ad42643f9c58af1cfa10303290c4871956(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff3804a834d6495bcff0422762f71307c94a4da1c28ad451d2c32404f2d12590(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70936c25cdb04a81209781be2e3ade2d4cfe2fc1e53977607a57356cdf8acf52(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__531a323ac9c079d5ced07632f97e1ad2d2b4cbcc500cf9e27b05851a877dfcc6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09a5a001a3ca7128e884188f91268fdc81513dca090e5d5b8d8583416d3ebbf8(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d623259445d87a6d88a579c356f0d6609ac204761fe573542171274cef9f9b25(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__addd2b97806670154a0c1903695c14f1b88192f5812a2bace4e0e23e552b8b5c(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7bb600dbb08836cbe5ede4bf133d00d2a4287b0faf8a56825972616bf3fb2037(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb479b548ff600faa8de8c73f986491dab9a98ab3396f064eef69f2394fbace4(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93abdde4cfe1e9799634fdda586074064b9daf07786b0ce93638f6f4fea11bc7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b965a76a1a8f74560f76c05c88db7da4c8cf7f2779313bf8de8f16e2894d8374(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    log_streams: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[OpsworksGangliaLayerCloudwatchConfigurationLogStreams, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__310bb3a4cc2b8a3daf043e2bd92569ae46e8890df886bc4c0b13cd9d1559b092(
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

def _typecheckingstub__92458f68457346ef082b31946fa47357b2b1c2a45f299d6e1fb226bd8bce4983(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0a9139e475d1d69bdfbc939d3044efb4400e4fa021b5e9e7b70073a7e4a6ea2(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46b78a14c8a3af4eacfa4efe9bde18aa5204eff0a3e6bcdc05dec0aa045da7ed(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84543c07e91b5231f99b392e8e5968b2fd89af7028ddd2cf080c90502d38c1c1(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5426ada6e55ad3d77aef199f2903b3773766747ea4230cf2ceb947144616eb9b(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6037c276b21f675163c19ca4bbbb807cd182e8bc5b9d6a7323d76c33e98153c0(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[OpsworksGangliaLayerCloudwatchConfigurationLogStreams]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__116e59ff35e494a29ec47529c5ea5149a989ee8e35d96534c3373c08cfa15737(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c066daf3041cd83da3668fe980a673667bd18927bcbb4e27ead6cbf87416e14(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e29f97999a9025942ffed925f2527e0499428ded7f0e14efb0a04f32107de244(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__caea327e32489f3b864fcb947a0eb41ddb16291977afff666d41d9ffca823a99(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a8dfa1490466acd35877b0c8abba5159a2654cb49805f7c84817a1525974799(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36895d386fb8fccee0b6b7124e02f1a2165aa526104c3b5e1af1e10bfe815064(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40087d099f3345e6c5f949fbadfc7e8b9ceee0886f5dd5c28f13928074956360(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c06e1d7546d04cc14dac745aa4b4f24124eb96595ecbb875cdf7a76a32493928(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bbfe5c7e5e7ee7255d5576412529e26bcdce66a0e5e639b9bdec00bfff597b54(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b967ddc8e3ddd6715e4dcabe2fe8b3a85446f6ff75e06c3c5048bd6e1e7f114e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e623f7d0cbb2197ae979bd55c026b6a109a24581fda8ed9de2ecaa38b05d7b10(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8822b4a95877af73f01dca28b7ecc0d424080f16ce8238192227deb7cba2869d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d337418483981119caba4d8a683ac24de2d4aab540eede53367ee15920d8216e(
    value: typing.Optional[typing.Union[OpsworksGangliaLayerCloudwatchConfigurationLogStreams, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__383acc1d1e25bb5028a5f94e70ade6948e7c891f17877e41fc74f62e526fc8d9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88b6074e48fcbaa8f28b1965a1832ea0a5017aa5bd36797401bc6c79483093bf(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[OpsworksGangliaLayerCloudwatchConfigurationLogStreams, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7aa2f061d437bc657058414d03784d49d634eec9f9e5b84fd42d532ee66ab5c1(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7aa78ddcc7b7fc288b00c6118135bbcfbd3c90c5b961115ff4a665489e590b1e(
    value: typing.Optional[OpsworksGangliaLayerCloudwatchConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4f057a75f7b1d442392235641fa820d4415b097e423b8bb0525ff0f97aab9fc(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    password: builtins.str,
    stack_id: builtins.str,
    auto_assign_elastic_ips: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    auto_assign_public_ips: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    auto_healing: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    cloudwatch_configuration: typing.Optional[typing.Union[OpsworksGangliaLayerCloudwatchConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    custom_configure_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
    custom_deploy_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
    custom_instance_profile_arn: typing.Optional[builtins.str] = None,
    custom_json: typing.Optional[builtins.str] = None,
    custom_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    custom_setup_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
    custom_shutdown_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
    custom_undeploy_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
    drain_elb_on_shutdown: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ebs_volume: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[OpsworksGangliaLayerEbsVolume, typing.Dict[builtins.str, typing.Any]]]]] = None,
    elastic_load_balancer: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    install_updates_on_boot: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    instance_shutdown_timeout: typing.Optional[jsii.Number] = None,
    load_based_auto_scaling: typing.Optional[typing.Union[OpsworksGangliaLayerLoadBasedAutoScaling, typing.Dict[builtins.str, typing.Any]]] = None,
    name: typing.Optional[builtins.str] = None,
    system_packages: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    url: typing.Optional[builtins.str] = None,
    use_ebs_optimized_instances: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    username: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b73a5ab79260392b913bb7926df0a1fae6cdfe84c76ca31837978b0154cf0017(
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

def _typecheckingstub__02f8a2ad8acab6217f225b6b12865b87a1a16329caefc99456b508041179f07f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f05809a9eb3abbed056d19e65787ff5fd286748bb149e92494f2ef25a218a76(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17e3d0d8d4c92e62b8a9e61cddbb28d26bb6942118c24049638d0eff053b576b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08d1c19bb7d16c0273e4706e5c35bff1fd7c4c611385b2788d7b313e410fdd7d(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3808459bf903579eaccf3ed40f16319310fae9931ea330790ca5054863470e2(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72cbfd65f3e52ac94b6390a5843abc73c5eb109d13885848431a0633084ceb95(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[OpsworksGangliaLayerEbsVolume]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2ce56b16228f72ba62541f06a7abe2c1761b49eb24125ee990c2d089c9ec332(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1b6f79d5120b719939bcde794794ff695d85740501392beab93e46b5533f460(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__178cc8049cb2e3fb81b7a26efbf7c2fe001f1ab31779ebc0823e7030426bf721(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a850cd5532f5ed7bdf540328651ee32617842439f185da7127f99eddf658ac3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8b35275b6713809852173de4f19cb7a601a3b27102ad9d4c2e3b4edf91268b4(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a04fbd39de3f13da8266810b7385e9c888ffe6209d6cecb1efb8ef89eaee0462(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01274e3fbcd450bcdec79164f5ba8a96de701aee605a37ef41c94ae593b15188(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ebe47bbeca71fed8f0374a851953ce5db33d56069a7a348b5fd89ecd7a935835(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9b73d7ee6cfe511fe11457f32bd9541608100af8d94ea5e9bc4bd4f8ed497a6(
    value: typing.Optional[typing.Union[OpsworksGangliaLayerEbsVolume, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0007f45f989d57bb4081b5183aedff91d535e0eb9ab2f39e59aef30e38f266f4(
    *,
    downscaling: typing.Optional[typing.Union[OpsworksGangliaLayerLoadBasedAutoScalingDownscaling, typing.Dict[builtins.str, typing.Any]]] = None,
    enable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    upscaling: typing.Optional[typing.Union[OpsworksGangliaLayerLoadBasedAutoScalingUpscaling, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ddcd045f8a9659e52681eb871d24f3782aa596c4b922657b8746422f6b93f628(
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

def _typecheckingstub__c1e66e84af9b29638e33319e0ba80bf5c4f55c36e12573bd2616c704f80fd89f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__729967760e3ff365c5403a5b66f212c8b27c115bcdd88a1703e1400a311217b2(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df603b0fe382770702f83cf4b88d41f69dbb3d9e6e9beb27cbdfafc5c5a1e992(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__816431ec9a627ee39784005c0f1bc24e4a7214e4b297172bc151abb8f6e55853(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4393e3bc59cf98561ba15449eb1841b34fec4037855ee0ccf68039b2971369b(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__feb01b943c4fba07e302014ed86ddc0817328a7facdea76ef7f3e84c4ce6bdd3(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23640c5d546792afb6bcbca16a7701e09af6c3523618c7d93028f5b562c01dda(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36bc2ec455301bb34e410618c63869a715db0ae9084151652831ae4ce7c2ece1(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f5f86d784acc4736fa3e4e6928375d3114d130387cd7845d548f7f276fa6f13(
    value: typing.Optional[OpsworksGangliaLayerLoadBasedAutoScalingDownscaling],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4a67c44c3ff64dbdaec7852821972c2af47dfb5a8cb046542241d121ecfeaa5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0da2150f8de1cd1db97e1f37823a747b95aff801da799455db7ca6ef3da3478(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ec7fcfdfe3bae644592f75832abbf14f008200dbe26fb95829ec1944789604e(
    value: typing.Optional[OpsworksGangliaLayerLoadBasedAutoScaling],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48f4752c57122e3102e8917cc66f6fe078e655874dcf1076c9065c0e804af843(
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

def _typecheckingstub__e00d108e6a49de3c5d61c9d81fd4a4d111cf0c4ae9bbc45d19b1d9ace571482d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__955655e60792d33d748ba29e144a8811ab9102021d05d0e2ffc334970c967969(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66abc90a5bb23703efd3b50b2ae1bd184b9187436220084b504d1aa7fe3a0efd(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83b05fa3d1d88b0e00941e66c10902b8388a8c6ba21bec3e11eee89e0509997f(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f312d55633e27ae0f6d534ca997b7017c95981e8b833a0f8300296c7f2fd0c6(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3b2e2fd15d9371bb9e861ac7b3e37cd7a1bf40dd3f700a7717ac6cec7f8ca7d(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5dfad35109474c185db2e008e0509b1ce3aec73c9ee5f60062e6830c975abee3(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca46ed3bcac94a4735d5c0d172d76e8b1b4defe38eced6d3743129332ffb053b(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58a043de2ce15ed28a01fbee074b0996ecc4d999f1ba610f9fbfe8e70f25cf73(
    value: typing.Optional[OpsworksGangliaLayerLoadBasedAutoScalingUpscaling],
) -> None:
    """Type checking stubs"""
    pass
