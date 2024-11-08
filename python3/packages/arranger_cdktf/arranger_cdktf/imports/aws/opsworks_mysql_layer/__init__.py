'''
# `aws_opsworks_mysql_layer`

Refer to the Terraform Registory for docs: [`aws_opsworks_mysql_layer`](https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer).
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


class OpsworksMysqlLayer(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.opsworksMysqlLayer.OpsworksMysqlLayer",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer aws_opsworks_mysql_layer}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        stack_id: builtins.str,
        auto_assign_elastic_ips: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        auto_assign_public_ips: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        auto_healing: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        cloudwatch_configuration: typing.Optional[typing.Union["OpsworksMysqlLayerCloudwatchConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        custom_configure_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
        custom_deploy_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
        custom_instance_profile_arn: typing.Optional[builtins.str] = None,
        custom_json: typing.Optional[builtins.str] = None,
        custom_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        custom_setup_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
        custom_shutdown_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
        custom_undeploy_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
        drain_elb_on_shutdown: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        ebs_volume: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["OpsworksMysqlLayerEbsVolume", typing.Dict[builtins.str, typing.Any]]]]] = None,
        elastic_load_balancer: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        install_updates_on_boot: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        instance_shutdown_timeout: typing.Optional[jsii.Number] = None,
        load_based_auto_scaling: typing.Optional[typing.Union["OpsworksMysqlLayerLoadBasedAutoScaling", typing.Dict[builtins.str, typing.Any]]] = None,
        name: typing.Optional[builtins.str] = None,
        root_password: typing.Optional[builtins.str] = None,
        root_password_on_all_instances: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
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
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer aws_opsworks_mysql_layer} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param stack_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#stack_id OpsworksMysqlLayer#stack_id}.
        :param auto_assign_elastic_ips: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#auto_assign_elastic_ips OpsworksMysqlLayer#auto_assign_elastic_ips}.
        :param auto_assign_public_ips: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#auto_assign_public_ips OpsworksMysqlLayer#auto_assign_public_ips}.
        :param auto_healing: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#auto_healing OpsworksMysqlLayer#auto_healing}.
        :param cloudwatch_configuration: cloudwatch_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#cloudwatch_configuration OpsworksMysqlLayer#cloudwatch_configuration}
        :param custom_configure_recipes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#custom_configure_recipes OpsworksMysqlLayer#custom_configure_recipes}.
        :param custom_deploy_recipes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#custom_deploy_recipes OpsworksMysqlLayer#custom_deploy_recipes}.
        :param custom_instance_profile_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#custom_instance_profile_arn OpsworksMysqlLayer#custom_instance_profile_arn}.
        :param custom_json: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#custom_json OpsworksMysqlLayer#custom_json}.
        :param custom_security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#custom_security_group_ids OpsworksMysqlLayer#custom_security_group_ids}.
        :param custom_setup_recipes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#custom_setup_recipes OpsworksMysqlLayer#custom_setup_recipes}.
        :param custom_shutdown_recipes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#custom_shutdown_recipes OpsworksMysqlLayer#custom_shutdown_recipes}.
        :param custom_undeploy_recipes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#custom_undeploy_recipes OpsworksMysqlLayer#custom_undeploy_recipes}.
        :param drain_elb_on_shutdown: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#drain_elb_on_shutdown OpsworksMysqlLayer#drain_elb_on_shutdown}.
        :param ebs_volume: ebs_volume block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#ebs_volume OpsworksMysqlLayer#ebs_volume}
        :param elastic_load_balancer: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#elastic_load_balancer OpsworksMysqlLayer#elastic_load_balancer}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#id OpsworksMysqlLayer#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param install_updates_on_boot: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#install_updates_on_boot OpsworksMysqlLayer#install_updates_on_boot}.
        :param instance_shutdown_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#instance_shutdown_timeout OpsworksMysqlLayer#instance_shutdown_timeout}.
        :param load_based_auto_scaling: load_based_auto_scaling block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#load_based_auto_scaling OpsworksMysqlLayer#load_based_auto_scaling}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#name OpsworksMysqlLayer#name}.
        :param root_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#root_password OpsworksMysqlLayer#root_password}.
        :param root_password_on_all_instances: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#root_password_on_all_instances OpsworksMysqlLayer#root_password_on_all_instances}.
        :param system_packages: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#system_packages OpsworksMysqlLayer#system_packages}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#tags OpsworksMysqlLayer#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#tags_all OpsworksMysqlLayer#tags_all}.
        :param use_ebs_optimized_instances: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#use_ebs_optimized_instances OpsworksMysqlLayer#use_ebs_optimized_instances}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cdb9a1b3d67b2e0dc2c706cba6fc354ac5a3f09ea93b088ab8ffb37b20c3acce)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = OpsworksMysqlLayerConfig(
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
            root_password=root_password,
            root_password_on_all_instances=root_password_on_all_instances,
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
        log_streams: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["OpsworksMysqlLayerCloudwatchConfigurationLogStreams", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#enabled OpsworksMysqlLayer#enabled}.
        :param log_streams: log_streams block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#log_streams OpsworksMysqlLayer#log_streams}
        '''
        value = OpsworksMysqlLayerCloudwatchConfiguration(
            enabled=enabled, log_streams=log_streams
        )

        return typing.cast(None, jsii.invoke(self, "putCloudwatchConfiguration", [value]))

    @jsii.member(jsii_name="putEbsVolume")
    def put_ebs_volume(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["OpsworksMysqlLayerEbsVolume", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__239003639b2f989d9fd224dba230767abdfee817f493a7904eee46ea6b6e9d1b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putEbsVolume", [value]))

    @jsii.member(jsii_name="putLoadBasedAutoScaling")
    def put_load_based_auto_scaling(
        self,
        *,
        downscaling: typing.Optional[typing.Union["OpsworksMysqlLayerLoadBasedAutoScalingDownscaling", typing.Dict[builtins.str, typing.Any]]] = None,
        enable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        upscaling: typing.Optional[typing.Union["OpsworksMysqlLayerLoadBasedAutoScalingUpscaling", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param downscaling: downscaling block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#downscaling OpsworksMysqlLayer#downscaling}
        :param enable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#enable OpsworksMysqlLayer#enable}.
        :param upscaling: upscaling block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#upscaling OpsworksMysqlLayer#upscaling}
        '''
        value = OpsworksMysqlLayerLoadBasedAutoScaling(
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

    @jsii.member(jsii_name="resetRootPassword")
    def reset_root_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRootPassword", []))

    @jsii.member(jsii_name="resetRootPasswordOnAllInstances")
    def reset_root_password_on_all_instances(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRootPasswordOnAllInstances", []))

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
    ) -> "OpsworksMysqlLayerCloudwatchConfigurationOutputReference":
        return typing.cast("OpsworksMysqlLayerCloudwatchConfigurationOutputReference", jsii.get(self, "cloudwatchConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="ebsVolume")
    def ebs_volume(self) -> "OpsworksMysqlLayerEbsVolumeList":
        return typing.cast("OpsworksMysqlLayerEbsVolumeList", jsii.get(self, "ebsVolume"))

    @builtins.property
    @jsii.member(jsii_name="loadBasedAutoScaling")
    def load_based_auto_scaling(
        self,
    ) -> "OpsworksMysqlLayerLoadBasedAutoScalingOutputReference":
        return typing.cast("OpsworksMysqlLayerLoadBasedAutoScalingOutputReference", jsii.get(self, "loadBasedAutoScaling"))

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
    ) -> typing.Optional["OpsworksMysqlLayerCloudwatchConfiguration"]:
        return typing.cast(typing.Optional["OpsworksMysqlLayerCloudwatchConfiguration"], jsii.get(self, "cloudwatchConfigurationInput"))

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
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["OpsworksMysqlLayerEbsVolume"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["OpsworksMysqlLayerEbsVolume"]]], jsii.get(self, "ebsVolumeInput"))

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
    ) -> typing.Optional["OpsworksMysqlLayerLoadBasedAutoScaling"]:
        return typing.cast(typing.Optional["OpsworksMysqlLayerLoadBasedAutoScaling"], jsii.get(self, "loadBasedAutoScalingInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="rootPasswordInput")
    def root_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rootPasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="rootPasswordOnAllInstancesInput")
    def root_password_on_all_instances_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "rootPasswordOnAllInstancesInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__234df9bcce070c34d49b519bbd6b028ce1758b74a5e178e7d12d0c2475173d01)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a817d56de1b486ba461401b94bbaf3a284d2685ab266a0ccc7a50ac5a493a7a0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__012ce681e5184ce2b873cd92355fe4251d10b27bd067089bbc6d66aaec885fc9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoHealing", value)

    @builtins.property
    @jsii.member(jsii_name="customConfigureRecipes")
    def custom_configure_recipes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "customConfigureRecipes"))

    @custom_configure_recipes.setter
    def custom_configure_recipes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a75d3c9301fac8ff0c99980a1794dae3831d8ed92e93e0f75d90db3df25f50f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customConfigureRecipes", value)

    @builtins.property
    @jsii.member(jsii_name="customDeployRecipes")
    def custom_deploy_recipes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "customDeployRecipes"))

    @custom_deploy_recipes.setter
    def custom_deploy_recipes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__786187a80eb377029e662eb8f031546bb8256c9fa9a2cb5770755173eab70206)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customDeployRecipes", value)

    @builtins.property
    @jsii.member(jsii_name="customInstanceProfileArn")
    def custom_instance_profile_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customInstanceProfileArn"))

    @custom_instance_profile_arn.setter
    def custom_instance_profile_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e39e4457853121c0ff66d6fede21b95b0837b5a68d3fe752baa9ba20b09b77ef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customInstanceProfileArn", value)

    @builtins.property
    @jsii.member(jsii_name="customJson")
    def custom_json(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customJson"))

    @custom_json.setter
    def custom_json(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c977a6a384eb076695531b4997b0f413b2931a424eb12d3d592e30c8f3ca4af)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customJson", value)

    @builtins.property
    @jsii.member(jsii_name="customSecurityGroupIds")
    def custom_security_group_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "customSecurityGroupIds"))

    @custom_security_group_ids.setter
    def custom_security_group_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c14b7597461266405ebec8ed90920047a81bde00d02d2f20ebd7225b5f6bfe7a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customSecurityGroupIds", value)

    @builtins.property
    @jsii.member(jsii_name="customSetupRecipes")
    def custom_setup_recipes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "customSetupRecipes"))

    @custom_setup_recipes.setter
    def custom_setup_recipes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23ccc958a0d7996ef0c8cf1c396a644412cb8af1e31c1b8ad0a63426fce84211)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customSetupRecipes", value)

    @builtins.property
    @jsii.member(jsii_name="customShutdownRecipes")
    def custom_shutdown_recipes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "customShutdownRecipes"))

    @custom_shutdown_recipes.setter
    def custom_shutdown_recipes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2a916c79db101cfa05bf872d33065e77b1471aa1962f46767f14f5bed697768)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customShutdownRecipes", value)

    @builtins.property
    @jsii.member(jsii_name="customUndeployRecipes")
    def custom_undeploy_recipes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "customUndeployRecipes"))

    @custom_undeploy_recipes.setter
    def custom_undeploy_recipes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__322f0ac015a4d32fea159b52670470db510cde6bc4d32043a90bddf069cae3c2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__af7cebb6934cf5d802f63aaa9f1acdb55a36c8519e91052daf8e757564555133)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "drainElbOnShutdown", value)

    @builtins.property
    @jsii.member(jsii_name="elasticLoadBalancer")
    def elastic_load_balancer(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "elasticLoadBalancer"))

    @elastic_load_balancer.setter
    def elastic_load_balancer(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1d1efcf14b49da116d49fe51e1ba139b554c36038f4bb21b058b135c4d05dbe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "elasticLoadBalancer", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab29e6d663535e4867d084531a9ff44e5ac59de0ed75fe730502ef8f769d14b9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3293c2d5709277052921524c47081d6c822d954e4aea8ac4714194cdef21ce83)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "installUpdatesOnBoot", value)

    @builtins.property
    @jsii.member(jsii_name="instanceShutdownTimeout")
    def instance_shutdown_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "instanceShutdownTimeout"))

    @instance_shutdown_timeout.setter
    def instance_shutdown_timeout(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__325e08df082418815f785dcf5e5f757d668ccd749a79df12a5f19e5657e8477c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceShutdownTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__883a1f37db38c5bfc266f42cee40f78cd721a375e75059a507199f47ee2155cd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="rootPassword")
    def root_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rootPassword"))

    @root_password.setter
    def root_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ea8163d0b62aa2f771a584cc7add1f5b3a8b0bd3ad5bed0f112cea6f7345986)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rootPassword", value)

    @builtins.property
    @jsii.member(jsii_name="rootPasswordOnAllInstances")
    def root_password_on_all_instances(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "rootPasswordOnAllInstances"))

    @root_password_on_all_instances.setter
    def root_password_on_all_instances(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76f79e4dc1911eea210a79444a3360a6e2fca39dca321a0c694c20b740f1245f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rootPasswordOnAllInstances", value)

    @builtins.property
    @jsii.member(jsii_name="stackId")
    def stack_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "stackId"))

    @stack_id.setter
    def stack_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc3a15650a79d3c64970d8e79256fb6619f65dc0b2fbde062fd1f6d857ddf977)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stackId", value)

    @builtins.property
    @jsii.member(jsii_name="systemPackages")
    def system_packages(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "systemPackages"))

    @system_packages.setter
    def system_packages(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f43141caa6aafa3fc9558d49755facab1789a24479a81f1cdc930b2db3f6f76)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "systemPackages", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d4755aeebeebc3e6838c4ca2b1e703d8c58728a9e794b7cea4b44572d1be0c0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__636246bde80e118cc6ccf84faf8e02b92608116c9e2cb4cfa841772a9b004ddd)
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
            type_hints = typing.get_type_hints(_typecheckingstub__bdeaaa3deec9fa62cba5b4383ca2f802fe72e13fffcece4aa0b85cea98949b72)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useEbsOptimizedInstances", value)


@jsii.data_type(
    jsii_type="aws.opsworksMysqlLayer.OpsworksMysqlLayerCloudwatchConfiguration",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "log_streams": "logStreams"},
)
class OpsworksMysqlLayerCloudwatchConfiguration:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        log_streams: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["OpsworksMysqlLayerCloudwatchConfigurationLogStreams", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#enabled OpsworksMysqlLayer#enabled}.
        :param log_streams: log_streams block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#log_streams OpsworksMysqlLayer#log_streams}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c6c485f89c10df8ec048309758e84c3aaf77ab59e58bb5df6111c408b4ef87f4)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#enabled OpsworksMysqlLayer#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def log_streams(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["OpsworksMysqlLayerCloudwatchConfigurationLogStreams"]]]:
        '''log_streams block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#log_streams OpsworksMysqlLayer#log_streams}
        '''
        result = self._values.get("log_streams")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["OpsworksMysqlLayerCloudwatchConfigurationLogStreams"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OpsworksMysqlLayerCloudwatchConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.opsworksMysqlLayer.OpsworksMysqlLayerCloudwatchConfigurationLogStreams",
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
class OpsworksMysqlLayerCloudwatchConfigurationLogStreams:
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
        :param file: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#file OpsworksMysqlLayer#file}.
        :param log_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#log_group_name OpsworksMysqlLayer#log_group_name}.
        :param batch_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#batch_count OpsworksMysqlLayer#batch_count}.
        :param batch_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#batch_size OpsworksMysqlLayer#batch_size}.
        :param buffer_duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#buffer_duration OpsworksMysqlLayer#buffer_duration}.
        :param datetime_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#datetime_format OpsworksMysqlLayer#datetime_format}.
        :param encoding: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#encoding OpsworksMysqlLayer#encoding}.
        :param file_fingerprint_lines: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#file_fingerprint_lines OpsworksMysqlLayer#file_fingerprint_lines}.
        :param initial_position: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#initial_position OpsworksMysqlLayer#initial_position}.
        :param multiline_start_pattern: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#multiline_start_pattern OpsworksMysqlLayer#multiline_start_pattern}.
        :param time_zone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#time_zone OpsworksMysqlLayer#time_zone}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6057034082abc600faebb40e5b714267193ada0dd46544b0854c2dd7c6d61e1a)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#file OpsworksMysqlLayer#file}.'''
        result = self._values.get("file")
        assert result is not None, "Required property 'file' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def log_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#log_group_name OpsworksMysqlLayer#log_group_name}.'''
        result = self._values.get("log_group_name")
        assert result is not None, "Required property 'log_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def batch_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#batch_count OpsworksMysqlLayer#batch_count}.'''
        result = self._values.get("batch_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def batch_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#batch_size OpsworksMysqlLayer#batch_size}.'''
        result = self._values.get("batch_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def buffer_duration(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#buffer_duration OpsworksMysqlLayer#buffer_duration}.'''
        result = self._values.get("buffer_duration")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def datetime_format(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#datetime_format OpsworksMysqlLayer#datetime_format}.'''
        result = self._values.get("datetime_format")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encoding(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#encoding OpsworksMysqlLayer#encoding}.'''
        result = self._values.get("encoding")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def file_fingerprint_lines(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#file_fingerprint_lines OpsworksMysqlLayer#file_fingerprint_lines}.'''
        result = self._values.get("file_fingerprint_lines")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def initial_position(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#initial_position OpsworksMysqlLayer#initial_position}.'''
        result = self._values.get("initial_position")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def multiline_start_pattern(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#multiline_start_pattern OpsworksMysqlLayer#multiline_start_pattern}.'''
        result = self._values.get("multiline_start_pattern")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def time_zone(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#time_zone OpsworksMysqlLayer#time_zone}.'''
        result = self._values.get("time_zone")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OpsworksMysqlLayerCloudwatchConfigurationLogStreams(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OpsworksMysqlLayerCloudwatchConfigurationLogStreamsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.opsworksMysqlLayer.OpsworksMysqlLayerCloudwatchConfigurationLogStreamsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__336205c8dcec55256f71dc339b924aa2ee8ae519f2037836f4afce9d95f5e63a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "OpsworksMysqlLayerCloudwatchConfigurationLogStreamsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45fb013de9881483c38a99c5ad8152fccf132f9a03d77e5d5598bdff7ed1ad36)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("OpsworksMysqlLayerCloudwatchConfigurationLogStreamsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6bd12eab857482ab82ed3d65346daa51319fa4873154f79f16c2b10c4aa75f9b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a8ec47a904f1a15a4a98a8ca29bf4720af773a04685a70893f3e9d552e0092e4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5d93ed4896e1972fb23c91fd804940012ea15857d4ffd0d5c971ea81a4642254)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[OpsworksMysqlLayerCloudwatchConfigurationLogStreams]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[OpsworksMysqlLayerCloudwatchConfigurationLogStreams]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[OpsworksMysqlLayerCloudwatchConfigurationLogStreams]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b023e0ef0dc459c1d6f59147e6eacf3c8395e401ba8084478cf4af4ba303f4ad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OpsworksMysqlLayerCloudwatchConfigurationLogStreamsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.opsworksMysqlLayer.OpsworksMysqlLayerCloudwatchConfigurationLogStreamsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0b239cda1dc3e159eb6fa73a44ba4b70d82764cb073f363dbee020102a6d61e3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5dec10ea3925a51e5ba62e05276249eab2854f631e35f36748a9df28e144ee79)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "batchCount", value)

    @builtins.property
    @jsii.member(jsii_name="batchSize")
    def batch_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "batchSize"))

    @batch_size.setter
    def batch_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a72073c372d8a55e0909e036e126f962f85bc0e1e4a731443dd784fc504f32b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "batchSize", value)

    @builtins.property
    @jsii.member(jsii_name="bufferDuration")
    def buffer_duration(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "bufferDuration"))

    @buffer_duration.setter
    def buffer_duration(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__258b5e8a7b2f217e41e3658384c0353fa044b0b3264acf0677363baf4ec53582)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bufferDuration", value)

    @builtins.property
    @jsii.member(jsii_name="datetimeFormat")
    def datetime_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datetimeFormat"))

    @datetime_format.setter
    def datetime_format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__777b09560feab44750c2bde0ee6972f360a1784fdd162e98942efb76341919ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datetimeFormat", value)

    @builtins.property
    @jsii.member(jsii_name="encoding")
    def encoding(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "encoding"))

    @encoding.setter
    def encoding(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2fd5cbaf8c0dbc30c83c8f3b5c04e386ce06cd86b41051b1b5fd99a6742c52fa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encoding", value)

    @builtins.property
    @jsii.member(jsii_name="file")
    def file(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "file"))

    @file.setter
    def file(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9db7eae28ccace5183275774b166ec3fe7e126d81d6601395b4c00d5eb2923cf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "file", value)

    @builtins.property
    @jsii.member(jsii_name="fileFingerprintLines")
    def file_fingerprint_lines(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fileFingerprintLines"))

    @file_fingerprint_lines.setter
    def file_fingerprint_lines(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b74aa12bdad968df36076de06f6182ac6332ba6c087a71787537c593f798be9c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileFingerprintLines", value)

    @builtins.property
    @jsii.member(jsii_name="initialPosition")
    def initial_position(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "initialPosition"))

    @initial_position.setter
    def initial_position(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e366c48f68c4e8cee36635ca848e26351ed362e76d60bacac2200cd9c5ff966f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "initialPosition", value)

    @builtins.property
    @jsii.member(jsii_name="logGroupName")
    def log_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logGroupName"))

    @log_group_name.setter
    def log_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7df5dfbf18d4c8e513ab3af521e66f0060ac74298a1ac3aabd4c10f9997d299)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="multilineStartPattern")
    def multiline_start_pattern(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "multilineStartPattern"))

    @multiline_start_pattern.setter
    def multiline_start_pattern(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee351fc48880e87c0ed894f6b2cdbd25d8f1f0e6af4c356162edb74c98694f0b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "multilineStartPattern", value)

    @builtins.property
    @jsii.member(jsii_name="timeZone")
    def time_zone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timeZone"))

    @time_zone.setter
    def time_zone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa1ca4baf7acb2be27480b14f3c8c956c6172491545a54e7bd0afe39bd863b55)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeZone", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[OpsworksMysqlLayerCloudwatchConfigurationLogStreams, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[OpsworksMysqlLayerCloudwatchConfigurationLogStreams, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[OpsworksMysqlLayerCloudwatchConfigurationLogStreams, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d42532516b4a57e3f217b18876a1742acf24c340131b4cc814dba47bc88e404)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OpsworksMysqlLayerCloudwatchConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.opsworksMysqlLayer.OpsworksMysqlLayerCloudwatchConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4f6c65bd4340574fcb1986c0e287abf95025630a49d49f97d3edeeb9d3b489b2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putLogStreams")
    def put_log_streams(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[OpsworksMysqlLayerCloudwatchConfigurationLogStreams, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__145a344b6aacef6192286a3d7ac68177cc2640e1d388be9a94e0fd27d5ccf5bc)
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
    def log_streams(self) -> OpsworksMysqlLayerCloudwatchConfigurationLogStreamsList:
        return typing.cast(OpsworksMysqlLayerCloudwatchConfigurationLogStreamsList, jsii.get(self, "logStreams"))

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
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[OpsworksMysqlLayerCloudwatchConfigurationLogStreams]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[OpsworksMysqlLayerCloudwatchConfigurationLogStreams]]], jsii.get(self, "logStreamsInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__9398ff096d2bce94425601ec7ea227bfff4ffacef773e63560a77e1326b5e358)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[OpsworksMysqlLayerCloudwatchConfiguration]:
        return typing.cast(typing.Optional[OpsworksMysqlLayerCloudwatchConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OpsworksMysqlLayerCloudwatchConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f570aad238f8ce7b96f64ad9a0c5757cb97f80097d21828f72b707a0ca0f02ed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.opsworksMysqlLayer.OpsworksMysqlLayerConfig",
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
        "root_password": "rootPassword",
        "root_password_on_all_instances": "rootPasswordOnAllInstances",
        "system_packages": "systemPackages",
        "tags": "tags",
        "tags_all": "tagsAll",
        "use_ebs_optimized_instances": "useEbsOptimizedInstances",
    },
)
class OpsworksMysqlLayerConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        cloudwatch_configuration: typing.Optional[typing.Union[OpsworksMysqlLayerCloudwatchConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
        custom_configure_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
        custom_deploy_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
        custom_instance_profile_arn: typing.Optional[builtins.str] = None,
        custom_json: typing.Optional[builtins.str] = None,
        custom_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        custom_setup_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
        custom_shutdown_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
        custom_undeploy_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
        drain_elb_on_shutdown: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        ebs_volume: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["OpsworksMysqlLayerEbsVolume", typing.Dict[builtins.str, typing.Any]]]]] = None,
        elastic_load_balancer: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        install_updates_on_boot: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        instance_shutdown_timeout: typing.Optional[jsii.Number] = None,
        load_based_auto_scaling: typing.Optional[typing.Union["OpsworksMysqlLayerLoadBasedAutoScaling", typing.Dict[builtins.str, typing.Any]]] = None,
        name: typing.Optional[builtins.str] = None,
        root_password: typing.Optional[builtins.str] = None,
        root_password_on_all_instances: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
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
        :param stack_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#stack_id OpsworksMysqlLayer#stack_id}.
        :param auto_assign_elastic_ips: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#auto_assign_elastic_ips OpsworksMysqlLayer#auto_assign_elastic_ips}.
        :param auto_assign_public_ips: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#auto_assign_public_ips OpsworksMysqlLayer#auto_assign_public_ips}.
        :param auto_healing: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#auto_healing OpsworksMysqlLayer#auto_healing}.
        :param cloudwatch_configuration: cloudwatch_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#cloudwatch_configuration OpsworksMysqlLayer#cloudwatch_configuration}
        :param custom_configure_recipes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#custom_configure_recipes OpsworksMysqlLayer#custom_configure_recipes}.
        :param custom_deploy_recipes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#custom_deploy_recipes OpsworksMysqlLayer#custom_deploy_recipes}.
        :param custom_instance_profile_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#custom_instance_profile_arn OpsworksMysqlLayer#custom_instance_profile_arn}.
        :param custom_json: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#custom_json OpsworksMysqlLayer#custom_json}.
        :param custom_security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#custom_security_group_ids OpsworksMysqlLayer#custom_security_group_ids}.
        :param custom_setup_recipes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#custom_setup_recipes OpsworksMysqlLayer#custom_setup_recipes}.
        :param custom_shutdown_recipes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#custom_shutdown_recipes OpsworksMysqlLayer#custom_shutdown_recipes}.
        :param custom_undeploy_recipes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#custom_undeploy_recipes OpsworksMysqlLayer#custom_undeploy_recipes}.
        :param drain_elb_on_shutdown: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#drain_elb_on_shutdown OpsworksMysqlLayer#drain_elb_on_shutdown}.
        :param ebs_volume: ebs_volume block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#ebs_volume OpsworksMysqlLayer#ebs_volume}
        :param elastic_load_balancer: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#elastic_load_balancer OpsworksMysqlLayer#elastic_load_balancer}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#id OpsworksMysqlLayer#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param install_updates_on_boot: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#install_updates_on_boot OpsworksMysqlLayer#install_updates_on_boot}.
        :param instance_shutdown_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#instance_shutdown_timeout OpsworksMysqlLayer#instance_shutdown_timeout}.
        :param load_based_auto_scaling: load_based_auto_scaling block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#load_based_auto_scaling OpsworksMysqlLayer#load_based_auto_scaling}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#name OpsworksMysqlLayer#name}.
        :param root_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#root_password OpsworksMysqlLayer#root_password}.
        :param root_password_on_all_instances: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#root_password_on_all_instances OpsworksMysqlLayer#root_password_on_all_instances}.
        :param system_packages: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#system_packages OpsworksMysqlLayer#system_packages}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#tags OpsworksMysqlLayer#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#tags_all OpsworksMysqlLayer#tags_all}.
        :param use_ebs_optimized_instances: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#use_ebs_optimized_instances OpsworksMysqlLayer#use_ebs_optimized_instances}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(cloudwatch_configuration, dict):
            cloudwatch_configuration = OpsworksMysqlLayerCloudwatchConfiguration(**cloudwatch_configuration)
        if isinstance(load_based_auto_scaling, dict):
            load_based_auto_scaling = OpsworksMysqlLayerLoadBasedAutoScaling(**load_based_auto_scaling)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__71f87611d29c8f2b166162f9f3bcd35ce678c3230fa177294283969450ea9e15)
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
            check_type(argname="argument root_password", value=root_password, expected_type=type_hints["root_password"])
            check_type(argname="argument root_password_on_all_instances", value=root_password_on_all_instances, expected_type=type_hints["root_password_on_all_instances"])
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
        if root_password is not None:
            self._values["root_password"] = root_password
        if root_password_on_all_instances is not None:
            self._values["root_password_on_all_instances"] = root_password_on_all_instances
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#stack_id OpsworksMysqlLayer#stack_id}.'''
        result = self._values.get("stack_id")
        assert result is not None, "Required property 'stack_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def auto_assign_elastic_ips(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#auto_assign_elastic_ips OpsworksMysqlLayer#auto_assign_elastic_ips}.'''
        result = self._values.get("auto_assign_elastic_ips")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def auto_assign_public_ips(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#auto_assign_public_ips OpsworksMysqlLayer#auto_assign_public_ips}.'''
        result = self._values.get("auto_assign_public_ips")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def auto_healing(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#auto_healing OpsworksMysqlLayer#auto_healing}.'''
        result = self._values.get("auto_healing")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def cloudwatch_configuration(
        self,
    ) -> typing.Optional[OpsworksMysqlLayerCloudwatchConfiguration]:
        '''cloudwatch_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#cloudwatch_configuration OpsworksMysqlLayer#cloudwatch_configuration}
        '''
        result = self._values.get("cloudwatch_configuration")
        return typing.cast(typing.Optional[OpsworksMysqlLayerCloudwatchConfiguration], result)

    @builtins.property
    def custom_configure_recipes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#custom_configure_recipes OpsworksMysqlLayer#custom_configure_recipes}.'''
        result = self._values.get("custom_configure_recipes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def custom_deploy_recipes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#custom_deploy_recipes OpsworksMysqlLayer#custom_deploy_recipes}.'''
        result = self._values.get("custom_deploy_recipes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def custom_instance_profile_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#custom_instance_profile_arn OpsworksMysqlLayer#custom_instance_profile_arn}.'''
        result = self._values.get("custom_instance_profile_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_json(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#custom_json OpsworksMysqlLayer#custom_json}.'''
        result = self._values.get("custom_json")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#custom_security_group_ids OpsworksMysqlLayer#custom_security_group_ids}.'''
        result = self._values.get("custom_security_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def custom_setup_recipes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#custom_setup_recipes OpsworksMysqlLayer#custom_setup_recipes}.'''
        result = self._values.get("custom_setup_recipes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def custom_shutdown_recipes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#custom_shutdown_recipes OpsworksMysqlLayer#custom_shutdown_recipes}.'''
        result = self._values.get("custom_shutdown_recipes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def custom_undeploy_recipes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#custom_undeploy_recipes OpsworksMysqlLayer#custom_undeploy_recipes}.'''
        result = self._values.get("custom_undeploy_recipes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def drain_elb_on_shutdown(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#drain_elb_on_shutdown OpsworksMysqlLayer#drain_elb_on_shutdown}.'''
        result = self._values.get("drain_elb_on_shutdown")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def ebs_volume(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["OpsworksMysqlLayerEbsVolume"]]]:
        '''ebs_volume block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#ebs_volume OpsworksMysqlLayer#ebs_volume}
        '''
        result = self._values.get("ebs_volume")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["OpsworksMysqlLayerEbsVolume"]]], result)

    @builtins.property
    def elastic_load_balancer(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#elastic_load_balancer OpsworksMysqlLayer#elastic_load_balancer}.'''
        result = self._values.get("elastic_load_balancer")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#id OpsworksMysqlLayer#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def install_updates_on_boot(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#install_updates_on_boot OpsworksMysqlLayer#install_updates_on_boot}.'''
        result = self._values.get("install_updates_on_boot")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def instance_shutdown_timeout(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#instance_shutdown_timeout OpsworksMysqlLayer#instance_shutdown_timeout}.'''
        result = self._values.get("instance_shutdown_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def load_based_auto_scaling(
        self,
    ) -> typing.Optional["OpsworksMysqlLayerLoadBasedAutoScaling"]:
        '''load_based_auto_scaling block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#load_based_auto_scaling OpsworksMysqlLayer#load_based_auto_scaling}
        '''
        result = self._values.get("load_based_auto_scaling")
        return typing.cast(typing.Optional["OpsworksMysqlLayerLoadBasedAutoScaling"], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#name OpsworksMysqlLayer#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def root_password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#root_password OpsworksMysqlLayer#root_password}.'''
        result = self._values.get("root_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def root_password_on_all_instances(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#root_password_on_all_instances OpsworksMysqlLayer#root_password_on_all_instances}.'''
        result = self._values.get("root_password_on_all_instances")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def system_packages(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#system_packages OpsworksMysqlLayer#system_packages}.'''
        result = self._values.get("system_packages")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#tags OpsworksMysqlLayer#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#tags_all OpsworksMysqlLayer#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def use_ebs_optimized_instances(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#use_ebs_optimized_instances OpsworksMysqlLayer#use_ebs_optimized_instances}.'''
        result = self._values.get("use_ebs_optimized_instances")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OpsworksMysqlLayerConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.opsworksMysqlLayer.OpsworksMysqlLayerEbsVolume",
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
class OpsworksMysqlLayerEbsVolume:
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
        :param mount_point: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#mount_point OpsworksMysqlLayer#mount_point}.
        :param number_of_disks: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#number_of_disks OpsworksMysqlLayer#number_of_disks}.
        :param size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#size OpsworksMysqlLayer#size}.
        :param encrypted: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#encrypted OpsworksMysqlLayer#encrypted}.
        :param iops: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#iops OpsworksMysqlLayer#iops}.
        :param raid_level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#raid_level OpsworksMysqlLayer#raid_level}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#type OpsworksMysqlLayer#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__743b81a21c9e9af66af8d5368ba13827296d14616a17234a67c75fdf80a9ffc1)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#mount_point OpsworksMysqlLayer#mount_point}.'''
        result = self._values.get("mount_point")
        assert result is not None, "Required property 'mount_point' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def number_of_disks(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#number_of_disks OpsworksMysqlLayer#number_of_disks}.'''
        result = self._values.get("number_of_disks")
        assert result is not None, "Required property 'number_of_disks' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def size(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#size OpsworksMysqlLayer#size}.'''
        result = self._values.get("size")
        assert result is not None, "Required property 'size' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def encrypted(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#encrypted OpsworksMysqlLayer#encrypted}.'''
        result = self._values.get("encrypted")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def iops(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#iops OpsworksMysqlLayer#iops}.'''
        result = self._values.get("iops")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def raid_level(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#raid_level OpsworksMysqlLayer#raid_level}.'''
        result = self._values.get("raid_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#type OpsworksMysqlLayer#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OpsworksMysqlLayerEbsVolume(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OpsworksMysqlLayerEbsVolumeList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.opsworksMysqlLayer.OpsworksMysqlLayerEbsVolumeList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__22f2402dcd310003dd6b416387012dee0ce91c0a4fef066221fd84c356301dfc)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "OpsworksMysqlLayerEbsVolumeOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e2d28303e162c94e442983779ce287f2b6c990789c2d14a19a7a0e7b2324af9)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("OpsworksMysqlLayerEbsVolumeOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a6951d5f98431972d680b7b6c65e869468eadee353604941e65b05a583fc537)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f1e065e0ce3486f4ef97309e94963ff92d2f98e925edc8633b7cdd2a9c547858)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e318b03baf44b3a5ee3144791a656bb5b7bf2cf68d1204351dedd582e95ef594)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[OpsworksMysqlLayerEbsVolume]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[OpsworksMysqlLayerEbsVolume]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[OpsworksMysqlLayerEbsVolume]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a959e17146fff44f0ed06d70d7551a43b0b1ee90ceaafff791963f88fb049775)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OpsworksMysqlLayerEbsVolumeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.opsworksMysqlLayer.OpsworksMysqlLayerEbsVolumeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__36dd349ec332b33487bc46882e0d0dc8409298b53514bf5a21cc8a2805c9e7f2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5c75bb236b03c4904373791ba8e93df7ffd07bd7608671389ce5ac1fd6a24b18)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encrypted", value)

    @builtins.property
    @jsii.member(jsii_name="iops")
    def iops(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "iops"))

    @iops.setter
    def iops(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ef40d35b2d1d14c1bd07510d03ac36d54a45d3e19df52de6bf2975a3e18b161)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iops", value)

    @builtins.property
    @jsii.member(jsii_name="mountPoint")
    def mount_point(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mountPoint"))

    @mount_point.setter
    def mount_point(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64b47d0a47525e01ab3cdcf6ffaabb960cb49c0a7109062eb81c106ca8517bd0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mountPoint", value)

    @builtins.property
    @jsii.member(jsii_name="numberOfDisks")
    def number_of_disks(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "numberOfDisks"))

    @number_of_disks.setter
    def number_of_disks(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a86126e6019f2ee26592c4f4e085db744390bff255255dbd374bf19098912ad6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "numberOfDisks", value)

    @builtins.property
    @jsii.member(jsii_name="raidLevel")
    def raid_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "raidLevel"))

    @raid_level.setter
    def raid_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d24b0fb41c5c5c6f4d9b0e67bbeaba5fba265b686a544346388a738b889ca3f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "raidLevel", value)

    @builtins.property
    @jsii.member(jsii_name="size")
    def size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "size"))

    @size.setter
    def size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de1ad4876e948f06c46b5e2fdf85fda479fd7e8ec84956dab77f6810bf066f48)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "size", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d07764c385b646ca1be54260e2b54af3a25205b542553ef3cd2a1d61874944ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[OpsworksMysqlLayerEbsVolume, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[OpsworksMysqlLayerEbsVolume, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[OpsworksMysqlLayerEbsVolume, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__83eb8d14720b99c220d528ce22af8397001ebd7a98420178e0d5aa2748e06e4f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.opsworksMysqlLayer.OpsworksMysqlLayerLoadBasedAutoScaling",
    jsii_struct_bases=[],
    name_mapping={
        "downscaling": "downscaling",
        "enable": "enable",
        "upscaling": "upscaling",
    },
)
class OpsworksMysqlLayerLoadBasedAutoScaling:
    def __init__(
        self,
        *,
        downscaling: typing.Optional[typing.Union["OpsworksMysqlLayerLoadBasedAutoScalingDownscaling", typing.Dict[builtins.str, typing.Any]]] = None,
        enable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        upscaling: typing.Optional[typing.Union["OpsworksMysqlLayerLoadBasedAutoScalingUpscaling", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param downscaling: downscaling block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#downscaling OpsworksMysqlLayer#downscaling}
        :param enable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#enable OpsworksMysqlLayer#enable}.
        :param upscaling: upscaling block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#upscaling OpsworksMysqlLayer#upscaling}
        '''
        if isinstance(downscaling, dict):
            downscaling = OpsworksMysqlLayerLoadBasedAutoScalingDownscaling(**downscaling)
        if isinstance(upscaling, dict):
            upscaling = OpsworksMysqlLayerLoadBasedAutoScalingUpscaling(**upscaling)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__120968f620c3ff032b925f191a0c36fc8006f780a7103db1b4fc67c3b00a09cf)
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
    ) -> typing.Optional["OpsworksMysqlLayerLoadBasedAutoScalingDownscaling"]:
        '''downscaling block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#downscaling OpsworksMysqlLayer#downscaling}
        '''
        result = self._values.get("downscaling")
        return typing.cast(typing.Optional["OpsworksMysqlLayerLoadBasedAutoScalingDownscaling"], result)

    @builtins.property
    def enable(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#enable OpsworksMysqlLayer#enable}.'''
        result = self._values.get("enable")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def upscaling(
        self,
    ) -> typing.Optional["OpsworksMysqlLayerLoadBasedAutoScalingUpscaling"]:
        '''upscaling block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#upscaling OpsworksMysqlLayer#upscaling}
        '''
        result = self._values.get("upscaling")
        return typing.cast(typing.Optional["OpsworksMysqlLayerLoadBasedAutoScalingUpscaling"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OpsworksMysqlLayerLoadBasedAutoScaling(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.opsworksMysqlLayer.OpsworksMysqlLayerLoadBasedAutoScalingDownscaling",
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
class OpsworksMysqlLayerLoadBasedAutoScalingDownscaling:
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
        :param alarms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#alarms OpsworksMysqlLayer#alarms}.
        :param cpu_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#cpu_threshold OpsworksMysqlLayer#cpu_threshold}.
        :param ignore_metrics_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#ignore_metrics_time OpsworksMysqlLayer#ignore_metrics_time}.
        :param instance_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#instance_count OpsworksMysqlLayer#instance_count}.
        :param load_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#load_threshold OpsworksMysqlLayer#load_threshold}.
        :param memory_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#memory_threshold OpsworksMysqlLayer#memory_threshold}.
        :param thresholds_wait_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#thresholds_wait_time OpsworksMysqlLayer#thresholds_wait_time}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__90ac789d3b34ee47340ce18cbf946dae6282d6c5cb8886b30da07cab66dcd4b4)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#alarms OpsworksMysqlLayer#alarms}.'''
        result = self._values.get("alarms")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def cpu_threshold(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#cpu_threshold OpsworksMysqlLayer#cpu_threshold}.'''
        result = self._values.get("cpu_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ignore_metrics_time(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#ignore_metrics_time OpsworksMysqlLayer#ignore_metrics_time}.'''
        result = self._values.get("ignore_metrics_time")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def instance_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#instance_count OpsworksMysqlLayer#instance_count}.'''
        result = self._values.get("instance_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def load_threshold(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#load_threshold OpsworksMysqlLayer#load_threshold}.'''
        result = self._values.get("load_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def memory_threshold(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#memory_threshold OpsworksMysqlLayer#memory_threshold}.'''
        result = self._values.get("memory_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def thresholds_wait_time(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#thresholds_wait_time OpsworksMysqlLayer#thresholds_wait_time}.'''
        result = self._values.get("thresholds_wait_time")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OpsworksMysqlLayerLoadBasedAutoScalingDownscaling(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OpsworksMysqlLayerLoadBasedAutoScalingDownscalingOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.opsworksMysqlLayer.OpsworksMysqlLayerLoadBasedAutoScalingDownscalingOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__604ceb1479f2ae96ffb9b2f9935ca2909711e543d43f3f5ac69ce2ae402bf74d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a261c09d89856acd9ef10e9ab892b8e25685a5997d4b1b38855f264004935f78)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alarms", value)

    @builtins.property
    @jsii.member(jsii_name="cpuThreshold")
    def cpu_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "cpuThreshold"))

    @cpu_threshold.setter
    def cpu_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2290846eb092c450644edacd766b9f21cbec63a11669f8103a92a6bac7c71f3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpuThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="ignoreMetricsTime")
    def ignore_metrics_time(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ignoreMetricsTime"))

    @ignore_metrics_time.setter
    def ignore_metrics_time(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__732d09d0eb72530b2532ded07bc737759a1634899f9ee23fbedd28846969ff80)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ignoreMetricsTime", value)

    @builtins.property
    @jsii.member(jsii_name="instanceCount")
    def instance_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "instanceCount"))

    @instance_count.setter
    def instance_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8166b92ecc7930d5f038e00fd29b6c8444d3ab1ca4aba9bc670d66737130463c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceCount", value)

    @builtins.property
    @jsii.member(jsii_name="loadThreshold")
    def load_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "loadThreshold"))

    @load_threshold.setter
    def load_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c90045e63e75127d0727dc99ca47db83c309abb6f412ec2b0a2b6dc83186cebf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loadThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="memoryThreshold")
    def memory_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "memoryThreshold"))

    @memory_threshold.setter
    def memory_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__927b97e7d6cc168bc172c814606c1f29f6c9a157d5fb8a7a609b0ade493da398)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memoryThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="thresholdsWaitTime")
    def thresholds_wait_time(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "thresholdsWaitTime"))

    @thresholds_wait_time.setter
    def thresholds_wait_time(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f91cd216cd3723359f80dd5386fdf564b31a1f33c0c15565a9d7cc256dab296)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "thresholdsWaitTime", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[OpsworksMysqlLayerLoadBasedAutoScalingDownscaling]:
        return typing.cast(typing.Optional[OpsworksMysqlLayerLoadBasedAutoScalingDownscaling], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OpsworksMysqlLayerLoadBasedAutoScalingDownscaling],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c93df7d9a0da1d6cbd4658640265005573ffbd1c9c812fe234f3dc3957dbf0e3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OpsworksMysqlLayerLoadBasedAutoScalingOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.opsworksMysqlLayer.OpsworksMysqlLayerLoadBasedAutoScalingOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__81138d3561cbe7084ea360f1e18c1c953d2873e552ccdf50bd92bbb0ca6ed9d2)
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
        :param alarms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#alarms OpsworksMysqlLayer#alarms}.
        :param cpu_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#cpu_threshold OpsworksMysqlLayer#cpu_threshold}.
        :param ignore_metrics_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#ignore_metrics_time OpsworksMysqlLayer#ignore_metrics_time}.
        :param instance_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#instance_count OpsworksMysqlLayer#instance_count}.
        :param load_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#load_threshold OpsworksMysqlLayer#load_threshold}.
        :param memory_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#memory_threshold OpsworksMysqlLayer#memory_threshold}.
        :param thresholds_wait_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#thresholds_wait_time OpsworksMysqlLayer#thresholds_wait_time}.
        '''
        value = OpsworksMysqlLayerLoadBasedAutoScalingDownscaling(
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
        :param alarms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#alarms OpsworksMysqlLayer#alarms}.
        :param cpu_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#cpu_threshold OpsworksMysqlLayer#cpu_threshold}.
        :param ignore_metrics_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#ignore_metrics_time OpsworksMysqlLayer#ignore_metrics_time}.
        :param instance_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#instance_count OpsworksMysqlLayer#instance_count}.
        :param load_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#load_threshold OpsworksMysqlLayer#load_threshold}.
        :param memory_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#memory_threshold OpsworksMysqlLayer#memory_threshold}.
        :param thresholds_wait_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#thresholds_wait_time OpsworksMysqlLayer#thresholds_wait_time}.
        '''
        value = OpsworksMysqlLayerLoadBasedAutoScalingUpscaling(
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
    ) -> OpsworksMysqlLayerLoadBasedAutoScalingDownscalingOutputReference:
        return typing.cast(OpsworksMysqlLayerLoadBasedAutoScalingDownscalingOutputReference, jsii.get(self, "downscaling"))

    @builtins.property
    @jsii.member(jsii_name="upscaling")
    def upscaling(
        self,
    ) -> "OpsworksMysqlLayerLoadBasedAutoScalingUpscalingOutputReference":
        return typing.cast("OpsworksMysqlLayerLoadBasedAutoScalingUpscalingOutputReference", jsii.get(self, "upscaling"))

    @builtins.property
    @jsii.member(jsii_name="downscalingInput")
    def downscaling_input(
        self,
    ) -> typing.Optional[OpsworksMysqlLayerLoadBasedAutoScalingDownscaling]:
        return typing.cast(typing.Optional[OpsworksMysqlLayerLoadBasedAutoScalingDownscaling], jsii.get(self, "downscalingInput"))

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
    ) -> typing.Optional["OpsworksMysqlLayerLoadBasedAutoScalingUpscaling"]:
        return typing.cast(typing.Optional["OpsworksMysqlLayerLoadBasedAutoScalingUpscaling"], jsii.get(self, "upscalingInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__9741763827d3ac1201c396134edb384ae5e3a6edd52c0ef42313ea4fc0d35131)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enable", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[OpsworksMysqlLayerLoadBasedAutoScaling]:
        return typing.cast(typing.Optional[OpsworksMysqlLayerLoadBasedAutoScaling], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OpsworksMysqlLayerLoadBasedAutoScaling],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9a5cab098965c8eb7f11a814e2130fa44fd00d2eb28f994a0ac47e68b04f775)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.opsworksMysqlLayer.OpsworksMysqlLayerLoadBasedAutoScalingUpscaling",
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
class OpsworksMysqlLayerLoadBasedAutoScalingUpscaling:
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
        :param alarms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#alarms OpsworksMysqlLayer#alarms}.
        :param cpu_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#cpu_threshold OpsworksMysqlLayer#cpu_threshold}.
        :param ignore_metrics_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#ignore_metrics_time OpsworksMysqlLayer#ignore_metrics_time}.
        :param instance_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#instance_count OpsworksMysqlLayer#instance_count}.
        :param load_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#load_threshold OpsworksMysqlLayer#load_threshold}.
        :param memory_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#memory_threshold OpsworksMysqlLayer#memory_threshold}.
        :param thresholds_wait_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#thresholds_wait_time OpsworksMysqlLayer#thresholds_wait_time}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f7debb8c7f3ff69387bf5d0fb6b215f16e5e491424bcdc8bc5b316d1e5a90be2)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#alarms OpsworksMysqlLayer#alarms}.'''
        result = self._values.get("alarms")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def cpu_threshold(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#cpu_threshold OpsworksMysqlLayer#cpu_threshold}.'''
        result = self._values.get("cpu_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ignore_metrics_time(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#ignore_metrics_time OpsworksMysqlLayer#ignore_metrics_time}.'''
        result = self._values.get("ignore_metrics_time")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def instance_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#instance_count OpsworksMysqlLayer#instance_count}.'''
        result = self._values.get("instance_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def load_threshold(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#load_threshold OpsworksMysqlLayer#load_threshold}.'''
        result = self._values.get("load_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def memory_threshold(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#memory_threshold OpsworksMysqlLayer#memory_threshold}.'''
        result = self._values.get("memory_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def thresholds_wait_time(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer#thresholds_wait_time OpsworksMysqlLayer#thresholds_wait_time}.'''
        result = self._values.get("thresholds_wait_time")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OpsworksMysqlLayerLoadBasedAutoScalingUpscaling(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OpsworksMysqlLayerLoadBasedAutoScalingUpscalingOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.opsworksMysqlLayer.OpsworksMysqlLayerLoadBasedAutoScalingUpscalingOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1eb71416b60ac8120d65319d1765d85e7b9c16187f851128b52955a1c664f5d2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__33330d05cea8d2e01f174478d573acc7505baec6d4048cb3ecf336e42f8bbdb6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alarms", value)

    @builtins.property
    @jsii.member(jsii_name="cpuThreshold")
    def cpu_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "cpuThreshold"))

    @cpu_threshold.setter
    def cpu_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d9a90e1fbcc8cb64ba82979b8dfb1e2b612e64a68096d092c14e199bac3758c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpuThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="ignoreMetricsTime")
    def ignore_metrics_time(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ignoreMetricsTime"))

    @ignore_metrics_time.setter
    def ignore_metrics_time(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c8886402d5b2c8e0b2b8f213a1300dbf328420d7ec402aa50858670f14352bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ignoreMetricsTime", value)

    @builtins.property
    @jsii.member(jsii_name="instanceCount")
    def instance_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "instanceCount"))

    @instance_count.setter
    def instance_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bfb6f1d607c2e2b1ed971a05a27699d6b3d7ac64d91c6d1a90c98e0d94a985d5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceCount", value)

    @builtins.property
    @jsii.member(jsii_name="loadThreshold")
    def load_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "loadThreshold"))

    @load_threshold.setter
    def load_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__def49000206875d4a7a6c623eeaff04813b59ac0ba029c4fcaa811350be329c3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loadThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="memoryThreshold")
    def memory_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "memoryThreshold"))

    @memory_threshold.setter
    def memory_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__31cc0c0b7f4b86ebf57ca13b7a58a931e84890de45c492a92b7be652258418ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memoryThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="thresholdsWaitTime")
    def thresholds_wait_time(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "thresholdsWaitTime"))

    @thresholds_wait_time.setter
    def thresholds_wait_time(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3093bf5498745c55b063ea59270e54710c8c81d8da58cce495d34587142e7840)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "thresholdsWaitTime", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[OpsworksMysqlLayerLoadBasedAutoScalingUpscaling]:
        return typing.cast(typing.Optional[OpsworksMysqlLayerLoadBasedAutoScalingUpscaling], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OpsworksMysqlLayerLoadBasedAutoScalingUpscaling],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bbeef42f25e6e20b2ed26b4c526ae3746e17f696abe6fd86dae8a074500952d5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "OpsworksMysqlLayer",
    "OpsworksMysqlLayerCloudwatchConfiguration",
    "OpsworksMysqlLayerCloudwatchConfigurationLogStreams",
    "OpsworksMysqlLayerCloudwatchConfigurationLogStreamsList",
    "OpsworksMysqlLayerCloudwatchConfigurationLogStreamsOutputReference",
    "OpsworksMysqlLayerCloudwatchConfigurationOutputReference",
    "OpsworksMysqlLayerConfig",
    "OpsworksMysqlLayerEbsVolume",
    "OpsworksMysqlLayerEbsVolumeList",
    "OpsworksMysqlLayerEbsVolumeOutputReference",
    "OpsworksMysqlLayerLoadBasedAutoScaling",
    "OpsworksMysqlLayerLoadBasedAutoScalingDownscaling",
    "OpsworksMysqlLayerLoadBasedAutoScalingDownscalingOutputReference",
    "OpsworksMysqlLayerLoadBasedAutoScalingOutputReference",
    "OpsworksMysqlLayerLoadBasedAutoScalingUpscaling",
    "OpsworksMysqlLayerLoadBasedAutoScalingUpscalingOutputReference",
]

publication.publish()

def _typecheckingstub__cdb9a1b3d67b2e0dc2c706cba6fc354ac5a3f09ea93b088ab8ffb37b20c3acce(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    stack_id: builtins.str,
    auto_assign_elastic_ips: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    auto_assign_public_ips: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    auto_healing: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    cloudwatch_configuration: typing.Optional[typing.Union[OpsworksMysqlLayerCloudwatchConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    custom_configure_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
    custom_deploy_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
    custom_instance_profile_arn: typing.Optional[builtins.str] = None,
    custom_json: typing.Optional[builtins.str] = None,
    custom_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    custom_setup_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
    custom_shutdown_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
    custom_undeploy_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
    drain_elb_on_shutdown: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ebs_volume: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[OpsworksMysqlLayerEbsVolume, typing.Dict[builtins.str, typing.Any]]]]] = None,
    elastic_load_balancer: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    install_updates_on_boot: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    instance_shutdown_timeout: typing.Optional[jsii.Number] = None,
    load_based_auto_scaling: typing.Optional[typing.Union[OpsworksMysqlLayerLoadBasedAutoScaling, typing.Dict[builtins.str, typing.Any]]] = None,
    name: typing.Optional[builtins.str] = None,
    root_password: typing.Optional[builtins.str] = None,
    root_password_on_all_instances: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
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

def _typecheckingstub__239003639b2f989d9fd224dba230767abdfee817f493a7904eee46ea6b6e9d1b(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[OpsworksMysqlLayerEbsVolume, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__234df9bcce070c34d49b519bbd6b028ce1758b74a5e178e7d12d0c2475173d01(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a817d56de1b486ba461401b94bbaf3a284d2685ab266a0ccc7a50ac5a493a7a0(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__012ce681e5184ce2b873cd92355fe4251d10b27bd067089bbc6d66aaec885fc9(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a75d3c9301fac8ff0c99980a1794dae3831d8ed92e93e0f75d90db3df25f50f(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__786187a80eb377029e662eb8f031546bb8256c9fa9a2cb5770755173eab70206(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e39e4457853121c0ff66d6fede21b95b0837b5a68d3fe752baa9ba20b09b77ef(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c977a6a384eb076695531b4997b0f413b2931a424eb12d3d592e30c8f3ca4af(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c14b7597461266405ebec8ed90920047a81bde00d02d2f20ebd7225b5f6bfe7a(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23ccc958a0d7996ef0c8cf1c396a644412cb8af1e31c1b8ad0a63426fce84211(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2a916c79db101cfa05bf872d33065e77b1471aa1962f46767f14f5bed697768(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__322f0ac015a4d32fea159b52670470db510cde6bc4d32043a90bddf069cae3c2(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af7cebb6934cf5d802f63aaa9f1acdb55a36c8519e91052daf8e757564555133(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1d1efcf14b49da116d49fe51e1ba139b554c36038f4bb21b058b135c4d05dbe(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab29e6d663535e4867d084531a9ff44e5ac59de0ed75fe730502ef8f769d14b9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3293c2d5709277052921524c47081d6c822d954e4aea8ac4714194cdef21ce83(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__325e08df082418815f785dcf5e5f757d668ccd749a79df12a5f19e5657e8477c(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__883a1f37db38c5bfc266f42cee40f78cd721a375e75059a507199f47ee2155cd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ea8163d0b62aa2f771a584cc7add1f5b3a8b0bd3ad5bed0f112cea6f7345986(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76f79e4dc1911eea210a79444a3360a6e2fca39dca321a0c694c20b740f1245f(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc3a15650a79d3c64970d8e79256fb6619f65dc0b2fbde062fd1f6d857ddf977(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f43141caa6aafa3fc9558d49755facab1789a24479a81f1cdc930b2db3f6f76(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d4755aeebeebc3e6838c4ca2b1e703d8c58728a9e794b7cea4b44572d1be0c0(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__636246bde80e118cc6ccf84faf8e02b92608116c9e2cb4cfa841772a9b004ddd(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bdeaaa3deec9fa62cba5b4383ca2f802fe72e13fffcece4aa0b85cea98949b72(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6c485f89c10df8ec048309758e84c3aaf77ab59e58bb5df6111c408b4ef87f4(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    log_streams: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[OpsworksMysqlLayerCloudwatchConfigurationLogStreams, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6057034082abc600faebb40e5b714267193ada0dd46544b0854c2dd7c6d61e1a(
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

def _typecheckingstub__336205c8dcec55256f71dc339b924aa2ee8ae519f2037836f4afce9d95f5e63a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45fb013de9881483c38a99c5ad8152fccf132f9a03d77e5d5598bdff7ed1ad36(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6bd12eab857482ab82ed3d65346daa51319fa4873154f79f16c2b10c4aa75f9b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8ec47a904f1a15a4a98a8ca29bf4720af773a04685a70893f3e9d552e0092e4(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d93ed4896e1972fb23c91fd804940012ea15857d4ffd0d5c971ea81a4642254(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b023e0ef0dc459c1d6f59147e6eacf3c8395e401ba8084478cf4af4ba303f4ad(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[OpsworksMysqlLayerCloudwatchConfigurationLogStreams]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b239cda1dc3e159eb6fa73a44ba4b70d82764cb073f363dbee020102a6d61e3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5dec10ea3925a51e5ba62e05276249eab2854f631e35f36748a9df28e144ee79(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a72073c372d8a55e0909e036e126f962f85bc0e1e4a731443dd784fc504f32b(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__258b5e8a7b2f217e41e3658384c0353fa044b0b3264acf0677363baf4ec53582(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__777b09560feab44750c2bde0ee6972f360a1784fdd162e98942efb76341919ce(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2fd5cbaf8c0dbc30c83c8f3b5c04e386ce06cd86b41051b1b5fd99a6742c52fa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9db7eae28ccace5183275774b166ec3fe7e126d81d6601395b4c00d5eb2923cf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b74aa12bdad968df36076de06f6182ac6332ba6c087a71787537c593f798be9c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e366c48f68c4e8cee36635ca848e26351ed362e76d60bacac2200cd9c5ff966f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7df5dfbf18d4c8e513ab3af521e66f0060ac74298a1ac3aabd4c10f9997d299(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee351fc48880e87c0ed894f6b2cdbd25d8f1f0e6af4c356162edb74c98694f0b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa1ca4baf7acb2be27480b14f3c8c956c6172491545a54e7bd0afe39bd863b55(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d42532516b4a57e3f217b18876a1742acf24c340131b4cc814dba47bc88e404(
    value: typing.Optional[typing.Union[OpsworksMysqlLayerCloudwatchConfigurationLogStreams, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f6c65bd4340574fcb1986c0e287abf95025630a49d49f97d3edeeb9d3b489b2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__145a344b6aacef6192286a3d7ac68177cc2640e1d388be9a94e0fd27d5ccf5bc(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[OpsworksMysqlLayerCloudwatchConfigurationLogStreams, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9398ff096d2bce94425601ec7ea227bfff4ffacef773e63560a77e1326b5e358(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f570aad238f8ce7b96f64ad9a0c5757cb97f80097d21828f72b707a0ca0f02ed(
    value: typing.Optional[OpsworksMysqlLayerCloudwatchConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71f87611d29c8f2b166162f9f3bcd35ce678c3230fa177294283969450ea9e15(
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
    cloudwatch_configuration: typing.Optional[typing.Union[OpsworksMysqlLayerCloudwatchConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    custom_configure_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
    custom_deploy_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
    custom_instance_profile_arn: typing.Optional[builtins.str] = None,
    custom_json: typing.Optional[builtins.str] = None,
    custom_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    custom_setup_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
    custom_shutdown_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
    custom_undeploy_recipes: typing.Optional[typing.Sequence[builtins.str]] = None,
    drain_elb_on_shutdown: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ebs_volume: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[OpsworksMysqlLayerEbsVolume, typing.Dict[builtins.str, typing.Any]]]]] = None,
    elastic_load_balancer: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    install_updates_on_boot: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    instance_shutdown_timeout: typing.Optional[jsii.Number] = None,
    load_based_auto_scaling: typing.Optional[typing.Union[OpsworksMysqlLayerLoadBasedAutoScaling, typing.Dict[builtins.str, typing.Any]]] = None,
    name: typing.Optional[builtins.str] = None,
    root_password: typing.Optional[builtins.str] = None,
    root_password_on_all_instances: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    system_packages: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    use_ebs_optimized_instances: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__743b81a21c9e9af66af8d5368ba13827296d14616a17234a67c75fdf80a9ffc1(
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

def _typecheckingstub__22f2402dcd310003dd6b416387012dee0ce91c0a4fef066221fd84c356301dfc(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e2d28303e162c94e442983779ce287f2b6c990789c2d14a19a7a0e7b2324af9(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a6951d5f98431972d680b7b6c65e869468eadee353604941e65b05a583fc537(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1e065e0ce3486f4ef97309e94963ff92d2f98e925edc8633b7cdd2a9c547858(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e318b03baf44b3a5ee3144791a656bb5b7bf2cf68d1204351dedd582e95ef594(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a959e17146fff44f0ed06d70d7551a43b0b1ee90ceaafff791963f88fb049775(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[OpsworksMysqlLayerEbsVolume]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36dd349ec332b33487bc46882e0d0dc8409298b53514bf5a21cc8a2805c9e7f2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c75bb236b03c4904373791ba8e93df7ffd07bd7608671389ce5ac1fd6a24b18(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ef40d35b2d1d14c1bd07510d03ac36d54a45d3e19df52de6bf2975a3e18b161(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64b47d0a47525e01ab3cdcf6ffaabb960cb49c0a7109062eb81c106ca8517bd0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a86126e6019f2ee26592c4f4e085db744390bff255255dbd374bf19098912ad6(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d24b0fb41c5c5c6f4d9b0e67bbeaba5fba265b686a544346388a738b889ca3f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de1ad4876e948f06c46b5e2fdf85fda479fd7e8ec84956dab77f6810bf066f48(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d07764c385b646ca1be54260e2b54af3a25205b542553ef3cd2a1d61874944ae(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83eb8d14720b99c220d528ce22af8397001ebd7a98420178e0d5aa2748e06e4f(
    value: typing.Optional[typing.Union[OpsworksMysqlLayerEbsVolume, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__120968f620c3ff032b925f191a0c36fc8006f780a7103db1b4fc67c3b00a09cf(
    *,
    downscaling: typing.Optional[typing.Union[OpsworksMysqlLayerLoadBasedAutoScalingDownscaling, typing.Dict[builtins.str, typing.Any]]] = None,
    enable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    upscaling: typing.Optional[typing.Union[OpsworksMysqlLayerLoadBasedAutoScalingUpscaling, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90ac789d3b34ee47340ce18cbf946dae6282d6c5cb8886b30da07cab66dcd4b4(
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

def _typecheckingstub__604ceb1479f2ae96ffb9b2f9935ca2909711e543d43f3f5ac69ce2ae402bf74d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a261c09d89856acd9ef10e9ab892b8e25685a5997d4b1b38855f264004935f78(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2290846eb092c450644edacd766b9f21cbec63a11669f8103a92a6bac7c71f3(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__732d09d0eb72530b2532ded07bc737759a1634899f9ee23fbedd28846969ff80(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8166b92ecc7930d5f038e00fd29b6c8444d3ab1ca4aba9bc670d66737130463c(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c90045e63e75127d0727dc99ca47db83c309abb6f412ec2b0a2b6dc83186cebf(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__927b97e7d6cc168bc172c814606c1f29f6c9a157d5fb8a7a609b0ade493da398(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f91cd216cd3723359f80dd5386fdf564b31a1f33c0c15565a9d7cc256dab296(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c93df7d9a0da1d6cbd4658640265005573ffbd1c9c812fe234f3dc3957dbf0e3(
    value: typing.Optional[OpsworksMysqlLayerLoadBasedAutoScalingDownscaling],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81138d3561cbe7084ea360f1e18c1c953d2873e552ccdf50bd92bbb0ca6ed9d2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9741763827d3ac1201c396134edb384ae5e3a6edd52c0ef42313ea4fc0d35131(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9a5cab098965c8eb7f11a814e2130fa44fd00d2eb28f994a0ac47e68b04f775(
    value: typing.Optional[OpsworksMysqlLayerLoadBasedAutoScaling],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7debb8c7f3ff69387bf5d0fb6b215f16e5e491424bcdc8bc5b316d1e5a90be2(
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

def _typecheckingstub__1eb71416b60ac8120d65319d1765d85e7b9c16187f851128b52955a1c664f5d2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33330d05cea8d2e01f174478d573acc7505baec6d4048cb3ecf336e42f8bbdb6(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d9a90e1fbcc8cb64ba82979b8dfb1e2b612e64a68096d092c14e199bac3758c(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c8886402d5b2c8e0b2b8f213a1300dbf328420d7ec402aa50858670f14352bc(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bfb6f1d607c2e2b1ed971a05a27699d6b3d7ac64d91c6d1a90c98e0d94a985d5(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__def49000206875d4a7a6c623eeaff04813b59ac0ba029c4fcaa811350be329c3(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31cc0c0b7f4b86ebf57ca13b7a58a931e84890de45c492a92b7be652258418ab(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3093bf5498745c55b063ea59270e54710c8c81d8da58cce495d34587142e7840(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bbeef42f25e6e20b2ed26b4c526ae3746e17f696abe6fd86dae8a074500952d5(
    value: typing.Optional[OpsworksMysqlLayerLoadBasedAutoScalingUpscaling],
) -> None:
    """Type checking stubs"""
    pass
