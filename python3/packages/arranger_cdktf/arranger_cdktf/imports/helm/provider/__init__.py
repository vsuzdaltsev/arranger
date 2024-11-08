'''
# `provider`

Refer to the Terraform Registry for docs: [`helm`](https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs).
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


class HelmProvider(
    _cdktf_9a9027ec.TerraformProvider,
    metaclass=jsii.JSIIMeta,
    jsii_type="helm.provider.HelmProvider",
):
    '''Represents a {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs helm}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        alias: typing.Optional[builtins.str] = None,
        burst_limit: typing.Optional[jsii.Number] = None,
        debug: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        experiments: typing.Optional[typing.Union["HelmProviderExperiments", typing.Dict[builtins.str, typing.Any]]] = None,
        helm_driver: typing.Optional[builtins.str] = None,
        kubernetes: typing.Optional[typing.Union["HelmProviderKubernetes", typing.Dict[builtins.str, typing.Any]]] = None,
        plugins_path: typing.Optional[builtins.str] = None,
        registry: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HelmProviderRegistry", typing.Dict[builtins.str, typing.Any]]]]] = None,
        registry_config_path: typing.Optional[builtins.str] = None,
        repository_cache: typing.Optional[builtins.str] = None,
        repository_config_path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs helm} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param alias: Alias name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#alias HelmProvider#alias}
        :param burst_limit: Helm burst limit. Increase this if you have a cluster with many CRDs. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#burst_limit HelmProvider#burst_limit}
        :param debug: Debug indicates whether or not Helm is running in Debug mode. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#debug HelmProvider#debug}
        :param experiments: experiments block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#experiments HelmProvider#experiments}
        :param helm_driver: The backend storage driver. Values are: configmap, secret, memory, sql. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#helm_driver HelmProvider#helm_driver}
        :param kubernetes: kubernetes block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#kubernetes HelmProvider#kubernetes}
        :param plugins_path: The path to the helm plugins directory. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#plugins_path HelmProvider#plugins_path}
        :param registry: registry block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#registry HelmProvider#registry}
        :param registry_config_path: The path to the registry config file. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#registry_config_path HelmProvider#registry_config_path}
        :param repository_cache: The path to the file containing cached repository indexes. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#repository_cache HelmProvider#repository_cache}
        :param repository_config_path: The path to the file containing repository names and URLs. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#repository_config_path HelmProvider#repository_config_path}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2495ed1772653b3f79ff7a4891c9c0ea2c38eba632749230264cb6f8f82d879d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = HelmProviderConfig(
            alias=alias,
            burst_limit=burst_limit,
            debug=debug,
            experiments=experiments,
            helm_driver=helm_driver,
            kubernetes=kubernetes,
            plugins_path=plugins_path,
            registry=registry,
            registry_config_path=registry_config_path,
            repository_cache=repository_cache,
            repository_config_path=repository_config_path,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="generateConfigForImport")
    @builtins.classmethod
    def generate_config_for_import(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        import_to_id: builtins.str,
        import_from_id: builtins.str,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    ) -> _cdktf_9a9027ec.ImportableResource:
        '''Generates CDKTF code for importing a HelmProvider resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the HelmProvider to import.
        :param import_from_id: The id of the existing HelmProvider that should be imported. Refer to the {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the HelmProvider to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c18d84be9fb923640e0091c5120aebe79aea481f49dc708b3fc91f5b7a54853)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="resetAlias")
    def reset_alias(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlias", []))

    @jsii.member(jsii_name="resetBurstLimit")
    def reset_burst_limit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBurstLimit", []))

    @jsii.member(jsii_name="resetDebug")
    def reset_debug(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDebug", []))

    @jsii.member(jsii_name="resetExperiments")
    def reset_experiments(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExperiments", []))

    @jsii.member(jsii_name="resetHelmDriver")
    def reset_helm_driver(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHelmDriver", []))

    @jsii.member(jsii_name="resetKubernetes")
    def reset_kubernetes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKubernetes", []))

    @jsii.member(jsii_name="resetPluginsPath")
    def reset_plugins_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPluginsPath", []))

    @jsii.member(jsii_name="resetRegistry")
    def reset_registry(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegistry", []))

    @jsii.member(jsii_name="resetRegistryConfigPath")
    def reset_registry_config_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegistryConfigPath", []))

    @jsii.member(jsii_name="resetRepositoryCache")
    def reset_repository_cache(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRepositoryCache", []))

    @jsii.member(jsii_name="resetRepositoryConfigPath")
    def reset_repository_config_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRepositoryConfigPath", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.member(jsii_name="synthesizeHclAttributes")
    def _synthesize_hcl_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeHclAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="aliasInput")
    def alias_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aliasInput"))

    @builtins.property
    @jsii.member(jsii_name="burstLimitInput")
    def burst_limit_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "burstLimitInput"))

    @builtins.property
    @jsii.member(jsii_name="debugInput")
    def debug_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "debugInput"))

    @builtins.property
    @jsii.member(jsii_name="experimentsInput")
    def experiments_input(self) -> typing.Optional["HelmProviderExperiments"]:
        return typing.cast(typing.Optional["HelmProviderExperiments"], jsii.get(self, "experimentsInput"))

    @builtins.property
    @jsii.member(jsii_name="helmDriverInput")
    def helm_driver_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "helmDriverInput"))

    @builtins.property
    @jsii.member(jsii_name="kubernetesInput")
    def kubernetes_input(self) -> typing.Optional["HelmProviderKubernetes"]:
        return typing.cast(typing.Optional["HelmProviderKubernetes"], jsii.get(self, "kubernetesInput"))

    @builtins.property
    @jsii.member(jsii_name="pluginsPathInput")
    def plugins_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pluginsPathInput"))

    @builtins.property
    @jsii.member(jsii_name="registryConfigPathInput")
    def registry_config_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "registryConfigPathInput"))

    @builtins.property
    @jsii.member(jsii_name="registryInput")
    def registry_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HelmProviderRegistry"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HelmProviderRegistry"]]], jsii.get(self, "registryInput"))

    @builtins.property
    @jsii.member(jsii_name="repositoryCacheInput")
    def repository_cache_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "repositoryCacheInput"))

    @builtins.property
    @jsii.member(jsii_name="repositoryConfigPathInput")
    def repository_config_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "repositoryConfigPathInput"))

    @builtins.property
    @jsii.member(jsii_name="alias")
    def alias(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alias"))

    @alias.setter
    def alias(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7225ff5bbbae9f2d37ee7993a0d0ea8528833bb10d6aea4160c5862f75192239)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alias", value)

    @builtins.property
    @jsii.member(jsii_name="burstLimit")
    def burst_limit(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "burstLimit"))

    @burst_limit.setter
    def burst_limit(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2a5c313a99cb56b5f7e6f958d2b7f762b89ea5b585970277b2380f93a973bf9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "burstLimit", value)

    @builtins.property
    @jsii.member(jsii_name="debug")
    def debug(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "debug"))

    @debug.setter
    def debug(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9b929c460b2da9d33b5d58b5f5b90f4f518965ad1de55467b16a8b3ed951063)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "debug", value)

    @builtins.property
    @jsii.member(jsii_name="experiments")
    def experiments(self) -> typing.Optional["HelmProviderExperiments"]:
        return typing.cast(typing.Optional["HelmProviderExperiments"], jsii.get(self, "experiments"))

    @experiments.setter
    def experiments(self, value: typing.Optional["HelmProviderExperiments"]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2ecd03e82bbfc793026fdd1ee5a1baec6c61ac93fab473e9227e878a1ac6998)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "experiments", value)

    @builtins.property
    @jsii.member(jsii_name="helmDriver")
    def helm_driver(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "helmDriver"))

    @helm_driver.setter
    def helm_driver(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01a2b891927f3c7538daffcf09a803eecf29b4b76fbb1cd79571a4e24bf9e55d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "helmDriver", value)

    @builtins.property
    @jsii.member(jsii_name="kubernetes")
    def kubernetes(self) -> typing.Optional["HelmProviderKubernetes"]:
        return typing.cast(typing.Optional["HelmProviderKubernetes"], jsii.get(self, "kubernetes"))

    @kubernetes.setter
    def kubernetes(self, value: typing.Optional["HelmProviderKubernetes"]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__adbea2384180725f1274e0661e4edfcf20733af6855fb766e3c38ca49465fe7d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kubernetes", value)

    @builtins.property
    @jsii.member(jsii_name="pluginsPath")
    def plugins_path(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pluginsPath"))

    @plugins_path.setter
    def plugins_path(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d47cb21ce389fb6bce570c0a11704d92be7258744836c9290f3feb7b331e6133)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pluginsPath", value)

    @builtins.property
    @jsii.member(jsii_name="registry")
    def registry(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HelmProviderRegistry"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HelmProviderRegistry"]]], jsii.get(self, "registry"))

    @registry.setter
    def registry(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HelmProviderRegistry"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b76a8cf330d660a9b063b19c5c4580eccab055f59fdb4d01ebaf8f6d7b128d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "registry", value)

    @builtins.property
    @jsii.member(jsii_name="registryConfigPath")
    def registry_config_path(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "registryConfigPath"))

    @registry_config_path.setter
    def registry_config_path(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b2ee131efc769f51d3849985efa7cc28406cf9c20b0a894b6e35b2ce51a29de)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "registryConfigPath", value)

    @builtins.property
    @jsii.member(jsii_name="repositoryCache")
    def repository_cache(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "repositoryCache"))

    @repository_cache.setter
    def repository_cache(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52be2cf5ff2b3c40f06cfec26730709c26bfaab020d65e343799f58da668922f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repositoryCache", value)

    @builtins.property
    @jsii.member(jsii_name="repositoryConfigPath")
    def repository_config_path(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "repositoryConfigPath"))

    @repository_config_path.setter
    def repository_config_path(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7829de03a03172c8d52d149743a006d998bc6c8090f4606af7c87a0e0c2966cb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repositoryConfigPath", value)


@jsii.data_type(
    jsii_type="helm.provider.HelmProviderConfig",
    jsii_struct_bases=[],
    name_mapping={
        "alias": "alias",
        "burst_limit": "burstLimit",
        "debug": "debug",
        "experiments": "experiments",
        "helm_driver": "helmDriver",
        "kubernetes": "kubernetes",
        "plugins_path": "pluginsPath",
        "registry": "registry",
        "registry_config_path": "registryConfigPath",
        "repository_cache": "repositoryCache",
        "repository_config_path": "repositoryConfigPath",
    },
)
class HelmProviderConfig:
    def __init__(
        self,
        *,
        alias: typing.Optional[builtins.str] = None,
        burst_limit: typing.Optional[jsii.Number] = None,
        debug: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        experiments: typing.Optional[typing.Union["HelmProviderExperiments", typing.Dict[builtins.str, typing.Any]]] = None,
        helm_driver: typing.Optional[builtins.str] = None,
        kubernetes: typing.Optional[typing.Union["HelmProviderKubernetes", typing.Dict[builtins.str, typing.Any]]] = None,
        plugins_path: typing.Optional[builtins.str] = None,
        registry: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HelmProviderRegistry", typing.Dict[builtins.str, typing.Any]]]]] = None,
        registry_config_path: typing.Optional[builtins.str] = None,
        repository_cache: typing.Optional[builtins.str] = None,
        repository_config_path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param alias: Alias name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#alias HelmProvider#alias}
        :param burst_limit: Helm burst limit. Increase this if you have a cluster with many CRDs. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#burst_limit HelmProvider#burst_limit}
        :param debug: Debug indicates whether or not Helm is running in Debug mode. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#debug HelmProvider#debug}
        :param experiments: experiments block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#experiments HelmProvider#experiments}
        :param helm_driver: The backend storage driver. Values are: configmap, secret, memory, sql. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#helm_driver HelmProvider#helm_driver}
        :param kubernetes: kubernetes block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#kubernetes HelmProvider#kubernetes}
        :param plugins_path: The path to the helm plugins directory. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#plugins_path HelmProvider#plugins_path}
        :param registry: registry block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#registry HelmProvider#registry}
        :param registry_config_path: The path to the registry config file. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#registry_config_path HelmProvider#registry_config_path}
        :param repository_cache: The path to the file containing cached repository indexes. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#repository_cache HelmProvider#repository_cache}
        :param repository_config_path: The path to the file containing repository names and URLs. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#repository_config_path HelmProvider#repository_config_path}
        '''
        if isinstance(experiments, dict):
            experiments = HelmProviderExperiments(**experiments)
        if isinstance(kubernetes, dict):
            kubernetes = HelmProviderKubernetes(**kubernetes)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99f989c297f979d73515516d88629c30cd2a466bbe7c08926c5b51293885cba8)
            check_type(argname="argument alias", value=alias, expected_type=type_hints["alias"])
            check_type(argname="argument burst_limit", value=burst_limit, expected_type=type_hints["burst_limit"])
            check_type(argname="argument debug", value=debug, expected_type=type_hints["debug"])
            check_type(argname="argument experiments", value=experiments, expected_type=type_hints["experiments"])
            check_type(argname="argument helm_driver", value=helm_driver, expected_type=type_hints["helm_driver"])
            check_type(argname="argument kubernetes", value=kubernetes, expected_type=type_hints["kubernetes"])
            check_type(argname="argument plugins_path", value=plugins_path, expected_type=type_hints["plugins_path"])
            check_type(argname="argument registry", value=registry, expected_type=type_hints["registry"])
            check_type(argname="argument registry_config_path", value=registry_config_path, expected_type=type_hints["registry_config_path"])
            check_type(argname="argument repository_cache", value=repository_cache, expected_type=type_hints["repository_cache"])
            check_type(argname="argument repository_config_path", value=repository_config_path, expected_type=type_hints["repository_config_path"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if alias is not None:
            self._values["alias"] = alias
        if burst_limit is not None:
            self._values["burst_limit"] = burst_limit
        if debug is not None:
            self._values["debug"] = debug
        if experiments is not None:
            self._values["experiments"] = experiments
        if helm_driver is not None:
            self._values["helm_driver"] = helm_driver
        if kubernetes is not None:
            self._values["kubernetes"] = kubernetes
        if plugins_path is not None:
            self._values["plugins_path"] = plugins_path
        if registry is not None:
            self._values["registry"] = registry
        if registry_config_path is not None:
            self._values["registry_config_path"] = registry_config_path
        if repository_cache is not None:
            self._values["repository_cache"] = repository_cache
        if repository_config_path is not None:
            self._values["repository_config_path"] = repository_config_path

    @builtins.property
    def alias(self) -> typing.Optional[builtins.str]:
        '''Alias name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#alias HelmProvider#alias}
        '''
        result = self._values.get("alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def burst_limit(self) -> typing.Optional[jsii.Number]:
        '''Helm burst limit. Increase this if you have a cluster with many CRDs.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#burst_limit HelmProvider#burst_limit}
        '''
        result = self._values.get("burst_limit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def debug(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Debug indicates whether or not Helm is running in Debug mode.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#debug HelmProvider#debug}
        '''
        result = self._values.get("debug")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def experiments(self) -> typing.Optional["HelmProviderExperiments"]:
        '''experiments block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#experiments HelmProvider#experiments}
        '''
        result = self._values.get("experiments")
        return typing.cast(typing.Optional["HelmProviderExperiments"], result)

    @builtins.property
    def helm_driver(self) -> typing.Optional[builtins.str]:
        '''The backend storage driver. Values are: configmap, secret, memory, sql.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#helm_driver HelmProvider#helm_driver}
        '''
        result = self._values.get("helm_driver")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kubernetes(self) -> typing.Optional["HelmProviderKubernetes"]:
        '''kubernetes block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#kubernetes HelmProvider#kubernetes}
        '''
        result = self._values.get("kubernetes")
        return typing.cast(typing.Optional["HelmProviderKubernetes"], result)

    @builtins.property
    def plugins_path(self) -> typing.Optional[builtins.str]:
        '''The path to the helm plugins directory.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#plugins_path HelmProvider#plugins_path}
        '''
        result = self._values.get("plugins_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def registry(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HelmProviderRegistry"]]]:
        '''registry block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#registry HelmProvider#registry}
        '''
        result = self._values.get("registry")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HelmProviderRegistry"]]], result)

    @builtins.property
    def registry_config_path(self) -> typing.Optional[builtins.str]:
        '''The path to the registry config file.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#registry_config_path HelmProvider#registry_config_path}
        '''
        result = self._values.get("registry_config_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def repository_cache(self) -> typing.Optional[builtins.str]:
        '''The path to the file containing cached repository indexes.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#repository_cache HelmProvider#repository_cache}
        '''
        result = self._values.get("repository_cache")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def repository_config_path(self) -> typing.Optional[builtins.str]:
        '''The path to the file containing repository names and URLs.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#repository_config_path HelmProvider#repository_config_path}
        '''
        result = self._values.get("repository_config_path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HelmProviderConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="helm.provider.HelmProviderExperiments",
    jsii_struct_bases=[],
    name_mapping={"manifest": "manifest"},
)
class HelmProviderExperiments:
    def __init__(
        self,
        *,
        manifest: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param manifest: Enable full diff by storing the rendered manifest in the state. This has similar limitations as when using helm install --dry-run. See https://helm.sh/docs/chart_best_practices/custom_resource_definitions/#install-a-crd-declaration-before-using-the-resource Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#manifest HelmProvider#manifest}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a47a79ec456a26e703a622b5da875b495b5eba76a61f6e3022aa768061f1459a)
            check_type(argname="argument manifest", value=manifest, expected_type=type_hints["manifest"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if manifest is not None:
            self._values["manifest"] = manifest

    @builtins.property
    def manifest(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Enable full diff by storing the rendered manifest in the state.

        This has similar limitations as when using helm install --dry-run. See https://helm.sh/docs/chart_best_practices/custom_resource_definitions/#install-a-crd-declaration-before-using-the-resource

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#manifest HelmProvider#manifest}
        '''
        result = self._values.get("manifest")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HelmProviderExperiments(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="helm.provider.HelmProviderKubernetes",
    jsii_struct_bases=[],
    name_mapping={
        "client_certificate": "clientCertificate",
        "client_key": "clientKey",
        "cluster_ca_certificate": "clusterCaCertificate",
        "config_context": "configContext",
        "config_context_auth_info": "configContextAuthInfo",
        "config_context_cluster": "configContextCluster",
        "config_path": "configPath",
        "config_paths": "configPaths",
        "exec": "exec",
        "host": "host",
        "insecure": "insecure",
        "password": "password",
        "proxy_url": "proxyUrl",
        "tls_server_name": "tlsServerName",
        "token": "token",
        "username": "username",
    },
)
class HelmProviderKubernetes:
    def __init__(
        self,
        *,
        client_certificate: typing.Optional[builtins.str] = None,
        client_key: typing.Optional[builtins.str] = None,
        cluster_ca_certificate: typing.Optional[builtins.str] = None,
        config_context: typing.Optional[builtins.str] = None,
        config_context_auth_info: typing.Optional[builtins.str] = None,
        config_context_cluster: typing.Optional[builtins.str] = None,
        config_path: typing.Optional[builtins.str] = None,
        config_paths: typing.Optional[typing.Sequence[builtins.str]] = None,
        exec: typing.Optional[typing.Union["HelmProviderKubernetesExec", typing.Dict[builtins.str, typing.Any]]] = None,
        host: typing.Optional[builtins.str] = None,
        insecure: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        password: typing.Optional[builtins.str] = None,
        proxy_url: typing.Optional[builtins.str] = None,
        tls_server_name: typing.Optional[builtins.str] = None,
        token: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param client_certificate: PEM-encoded client certificate for TLS authentication. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#client_certificate HelmProvider#client_certificate}
        :param client_key: PEM-encoded client certificate key for TLS authentication. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#client_key HelmProvider#client_key}
        :param cluster_ca_certificate: PEM-encoded root certificates bundle for TLS authentication. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#cluster_ca_certificate HelmProvider#cluster_ca_certificate}
        :param config_context: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#config_context HelmProvider#config_context}.
        :param config_context_auth_info: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#config_context_auth_info HelmProvider#config_context_auth_info}.
        :param config_context_cluster: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#config_context_cluster HelmProvider#config_context_cluster}.
        :param config_path: Path to the kube config file. Can be set with KUBE_CONFIG_PATH. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#config_path HelmProvider#config_path}
        :param config_paths: A list of paths to kube config files. Can be set with KUBE_CONFIG_PATHS environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#config_paths HelmProvider#config_paths}
        :param exec: exec block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#exec HelmProvider#exec}
        :param host: The hostname (in form of URI) of Kubernetes master. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#host HelmProvider#host}
        :param insecure: Whether server should be accessed without verifying the TLS certificate. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#insecure HelmProvider#insecure}
        :param password: The password to use for HTTP basic authentication when accessing the Kubernetes master endpoint. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#password HelmProvider#password}
        :param proxy_url: URL to the proxy to be used for all API requests. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#proxy_url HelmProvider#proxy_url}
        :param tls_server_name: Server name passed to the server for SNI and is used in the client to check server certificates against. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#tls_server_name HelmProvider#tls_server_name}
        :param token: Token to authenticate an service account. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#token HelmProvider#token}
        :param username: The username to use for HTTP basic authentication when accessing the Kubernetes master endpoint. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#username HelmProvider#username}
        '''
        if isinstance(exec, dict):
            exec = HelmProviderKubernetesExec(**exec)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__37e457508720e9cdf067b071b25cb64e43a9a82a1d85be65423e3e10ba8e2fc3)
            check_type(argname="argument client_certificate", value=client_certificate, expected_type=type_hints["client_certificate"])
            check_type(argname="argument client_key", value=client_key, expected_type=type_hints["client_key"])
            check_type(argname="argument cluster_ca_certificate", value=cluster_ca_certificate, expected_type=type_hints["cluster_ca_certificate"])
            check_type(argname="argument config_context", value=config_context, expected_type=type_hints["config_context"])
            check_type(argname="argument config_context_auth_info", value=config_context_auth_info, expected_type=type_hints["config_context_auth_info"])
            check_type(argname="argument config_context_cluster", value=config_context_cluster, expected_type=type_hints["config_context_cluster"])
            check_type(argname="argument config_path", value=config_path, expected_type=type_hints["config_path"])
            check_type(argname="argument config_paths", value=config_paths, expected_type=type_hints["config_paths"])
            check_type(argname="argument exec", value=exec, expected_type=type_hints["exec"])
            check_type(argname="argument host", value=host, expected_type=type_hints["host"])
            check_type(argname="argument insecure", value=insecure, expected_type=type_hints["insecure"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument proxy_url", value=proxy_url, expected_type=type_hints["proxy_url"])
            check_type(argname="argument tls_server_name", value=tls_server_name, expected_type=type_hints["tls_server_name"])
            check_type(argname="argument token", value=token, expected_type=type_hints["token"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if client_certificate is not None:
            self._values["client_certificate"] = client_certificate
        if client_key is not None:
            self._values["client_key"] = client_key
        if cluster_ca_certificate is not None:
            self._values["cluster_ca_certificate"] = cluster_ca_certificate
        if config_context is not None:
            self._values["config_context"] = config_context
        if config_context_auth_info is not None:
            self._values["config_context_auth_info"] = config_context_auth_info
        if config_context_cluster is not None:
            self._values["config_context_cluster"] = config_context_cluster
        if config_path is not None:
            self._values["config_path"] = config_path
        if config_paths is not None:
            self._values["config_paths"] = config_paths
        if exec is not None:
            self._values["exec"] = exec
        if host is not None:
            self._values["host"] = host
        if insecure is not None:
            self._values["insecure"] = insecure
        if password is not None:
            self._values["password"] = password
        if proxy_url is not None:
            self._values["proxy_url"] = proxy_url
        if tls_server_name is not None:
            self._values["tls_server_name"] = tls_server_name
        if token is not None:
            self._values["token"] = token
        if username is not None:
            self._values["username"] = username

    @builtins.property
    def client_certificate(self) -> typing.Optional[builtins.str]:
        '''PEM-encoded client certificate for TLS authentication.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#client_certificate HelmProvider#client_certificate}
        '''
        result = self._values.get("client_certificate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_key(self) -> typing.Optional[builtins.str]:
        '''PEM-encoded client certificate key for TLS authentication.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#client_key HelmProvider#client_key}
        '''
        result = self._values.get("client_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cluster_ca_certificate(self) -> typing.Optional[builtins.str]:
        '''PEM-encoded root certificates bundle for TLS authentication.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#cluster_ca_certificate HelmProvider#cluster_ca_certificate}
        '''
        result = self._values.get("cluster_ca_certificate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def config_context(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#config_context HelmProvider#config_context}.'''
        result = self._values.get("config_context")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def config_context_auth_info(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#config_context_auth_info HelmProvider#config_context_auth_info}.'''
        result = self._values.get("config_context_auth_info")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def config_context_cluster(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#config_context_cluster HelmProvider#config_context_cluster}.'''
        result = self._values.get("config_context_cluster")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def config_path(self) -> typing.Optional[builtins.str]:
        '''Path to the kube config file. Can be set with KUBE_CONFIG_PATH.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#config_path HelmProvider#config_path}
        '''
        result = self._values.get("config_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def config_paths(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of paths to kube config files. Can be set with KUBE_CONFIG_PATHS environment variable.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#config_paths HelmProvider#config_paths}
        '''
        result = self._values.get("config_paths")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def exec(self) -> typing.Optional["HelmProviderKubernetesExec"]:
        '''exec block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#exec HelmProvider#exec}
        '''
        result = self._values.get("exec")
        return typing.cast(typing.Optional["HelmProviderKubernetesExec"], result)

    @builtins.property
    def host(self) -> typing.Optional[builtins.str]:
        '''The hostname (in form of URI) of Kubernetes master.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#host HelmProvider#host}
        '''
        result = self._values.get("host")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def insecure(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether server should be accessed without verifying the TLS certificate.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#insecure HelmProvider#insecure}
        '''
        result = self._values.get("insecure")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''The password to use for HTTP basic authentication when accessing the Kubernetes master endpoint.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#password HelmProvider#password}
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def proxy_url(self) -> typing.Optional[builtins.str]:
        '''URL to the proxy to be used for all API requests.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#proxy_url HelmProvider#proxy_url}
        '''
        result = self._values.get("proxy_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tls_server_name(self) -> typing.Optional[builtins.str]:
        '''Server name passed to the server for SNI and is used in the client to check server certificates against.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#tls_server_name HelmProvider#tls_server_name}
        '''
        result = self._values.get("tls_server_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def token(self) -> typing.Optional[builtins.str]:
        '''Token to authenticate an service account.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#token HelmProvider#token}
        '''
        result = self._values.get("token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''The username to use for HTTP basic authentication when accessing the Kubernetes master endpoint.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#username HelmProvider#username}
        '''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HelmProviderKubernetes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="helm.provider.HelmProviderKubernetesExec",
    jsii_struct_bases=[],
    name_mapping={
        "api_version": "apiVersion",
        "command": "command",
        "args": "args",
        "env": "env",
    },
)
class HelmProviderKubernetesExec:
    def __init__(
        self,
        *,
        api_version: builtins.str,
        command: builtins.str,
        args: typing.Optional[typing.Sequence[builtins.str]] = None,
        env: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param api_version: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#api_version HelmProvider#api_version}.
        :param command: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#command HelmProvider#command}.
        :param args: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#args HelmProvider#args}.
        :param env: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#env HelmProvider#env}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd37ba6e977b38b0ddfdffac069ea6db5c1efb2f719fb6bb0a6acfed7ffb4191)
            check_type(argname="argument api_version", value=api_version, expected_type=type_hints["api_version"])
            check_type(argname="argument command", value=command, expected_type=type_hints["command"])
            check_type(argname="argument args", value=args, expected_type=type_hints["args"])
            check_type(argname="argument env", value=env, expected_type=type_hints["env"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api_version": api_version,
            "command": command,
        }
        if args is not None:
            self._values["args"] = args
        if env is not None:
            self._values["env"] = env

    @builtins.property
    def api_version(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#api_version HelmProvider#api_version}.'''
        result = self._values.get("api_version")
        assert result is not None, "Required property 'api_version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def command(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#command HelmProvider#command}.'''
        result = self._values.get("command")
        assert result is not None, "Required property 'command' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def args(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#args HelmProvider#args}.'''
        result = self._values.get("args")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def env(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#env HelmProvider#env}.'''
        result = self._values.get("env")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HelmProviderKubernetesExec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="helm.provider.HelmProviderRegistry",
    jsii_struct_bases=[],
    name_mapping={"password": "password", "url": "url", "username": "username"},
)
class HelmProviderRegistry:
    def __init__(
        self,
        *,
        password: builtins.str,
        url: builtins.str,
        username: builtins.str,
    ) -> None:
        '''
        :param password: The password to use for the OCI HTTP basic authentication when accessing the Kubernetes master endpoint. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#password HelmProvider#password}
        :param url: OCI URL in form of oci://host:port or oci://host. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#url HelmProvider#url}
        :param username: The username to use for the OCI HTTP basic authentication when accessing the Kubernetes master endpoint. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#username HelmProvider#username}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94dc7f0cd8e2ceba59f6de7a72c10c3dced9fbaa3103afc057e06492f181d9f1)
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "password": password,
            "url": url,
            "username": username,
        }

    @builtins.property
    def password(self) -> builtins.str:
        '''The password to use for the OCI HTTP basic authentication when accessing the Kubernetes master endpoint.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#password HelmProvider#password}
        '''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def url(self) -> builtins.str:
        '''OCI URL in form of oci://host:port or oci://host.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#url HelmProvider#url}
        '''
        result = self._values.get("url")
        assert result is not None, "Required property 'url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def username(self) -> builtins.str:
        '''The username to use for the OCI HTTP basic authentication when accessing the Kubernetes master endpoint.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/helm/2.16.1/docs#username HelmProvider#username}
        '''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HelmProviderRegistry(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "HelmProvider",
    "HelmProviderConfig",
    "HelmProviderExperiments",
    "HelmProviderKubernetes",
    "HelmProviderKubernetesExec",
    "HelmProviderRegistry",
]

publication.publish()

def _typecheckingstub__2495ed1772653b3f79ff7a4891c9c0ea2c38eba632749230264cb6f8f82d879d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    alias: typing.Optional[builtins.str] = None,
    burst_limit: typing.Optional[jsii.Number] = None,
    debug: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    experiments: typing.Optional[typing.Union[HelmProviderExperiments, typing.Dict[builtins.str, typing.Any]]] = None,
    helm_driver: typing.Optional[builtins.str] = None,
    kubernetes: typing.Optional[typing.Union[HelmProviderKubernetes, typing.Dict[builtins.str, typing.Any]]] = None,
    plugins_path: typing.Optional[builtins.str] = None,
    registry: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HelmProviderRegistry, typing.Dict[builtins.str, typing.Any]]]]] = None,
    registry_config_path: typing.Optional[builtins.str] = None,
    repository_cache: typing.Optional[builtins.str] = None,
    repository_config_path: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c18d84be9fb923640e0091c5120aebe79aea481f49dc708b3fc91f5b7a54853(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7225ff5bbbae9f2d37ee7993a0d0ea8528833bb10d6aea4160c5862f75192239(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2a5c313a99cb56b5f7e6f958d2b7f762b89ea5b585970277b2380f93a973bf9(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9b929c460b2da9d33b5d58b5f5b90f4f518965ad1de55467b16a8b3ed951063(
    value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2ecd03e82bbfc793026fdd1ee5a1baec6c61ac93fab473e9227e878a1ac6998(
    value: typing.Optional[HelmProviderExperiments],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01a2b891927f3c7538daffcf09a803eecf29b4b76fbb1cd79571a4e24bf9e55d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__adbea2384180725f1274e0661e4edfcf20733af6855fb766e3c38ca49465fe7d(
    value: typing.Optional[HelmProviderKubernetes],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d47cb21ce389fb6bce570c0a11704d92be7258744836c9290f3feb7b331e6133(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b76a8cf330d660a9b063b19c5c4580eccab055f59fdb4d01ebaf8f6d7b128d0(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HelmProviderRegistry]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b2ee131efc769f51d3849985efa7cc28406cf9c20b0a894b6e35b2ce51a29de(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52be2cf5ff2b3c40f06cfec26730709c26bfaab020d65e343799f58da668922f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7829de03a03172c8d52d149743a006d998bc6c8090f4606af7c87a0e0c2966cb(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99f989c297f979d73515516d88629c30cd2a466bbe7c08926c5b51293885cba8(
    *,
    alias: typing.Optional[builtins.str] = None,
    burst_limit: typing.Optional[jsii.Number] = None,
    debug: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    experiments: typing.Optional[typing.Union[HelmProviderExperiments, typing.Dict[builtins.str, typing.Any]]] = None,
    helm_driver: typing.Optional[builtins.str] = None,
    kubernetes: typing.Optional[typing.Union[HelmProviderKubernetes, typing.Dict[builtins.str, typing.Any]]] = None,
    plugins_path: typing.Optional[builtins.str] = None,
    registry: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HelmProviderRegistry, typing.Dict[builtins.str, typing.Any]]]]] = None,
    registry_config_path: typing.Optional[builtins.str] = None,
    repository_cache: typing.Optional[builtins.str] = None,
    repository_config_path: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a47a79ec456a26e703a622b5da875b495b5eba76a61f6e3022aa768061f1459a(
    *,
    manifest: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37e457508720e9cdf067b071b25cb64e43a9a82a1d85be65423e3e10ba8e2fc3(
    *,
    client_certificate: typing.Optional[builtins.str] = None,
    client_key: typing.Optional[builtins.str] = None,
    cluster_ca_certificate: typing.Optional[builtins.str] = None,
    config_context: typing.Optional[builtins.str] = None,
    config_context_auth_info: typing.Optional[builtins.str] = None,
    config_context_cluster: typing.Optional[builtins.str] = None,
    config_path: typing.Optional[builtins.str] = None,
    config_paths: typing.Optional[typing.Sequence[builtins.str]] = None,
    exec: typing.Optional[typing.Union[HelmProviderKubernetesExec, typing.Dict[builtins.str, typing.Any]]] = None,
    host: typing.Optional[builtins.str] = None,
    insecure: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    password: typing.Optional[builtins.str] = None,
    proxy_url: typing.Optional[builtins.str] = None,
    tls_server_name: typing.Optional[builtins.str] = None,
    token: typing.Optional[builtins.str] = None,
    username: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd37ba6e977b38b0ddfdffac069ea6db5c1efb2f719fb6bb0a6acfed7ffb4191(
    *,
    api_version: builtins.str,
    command: builtins.str,
    args: typing.Optional[typing.Sequence[builtins.str]] = None,
    env: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94dc7f0cd8e2ceba59f6de7a72c10c3dced9fbaa3103afc057e06492f181d9f1(
    *,
    password: builtins.str,
    url: builtins.str,
    username: builtins.str,
) -> None:
    """Type checking stubs"""
    pass
