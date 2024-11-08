'''
# `provider`

Refer to the Terraform Registory for docs: [`kubernetes`](https://www.terraform.io/docs/providers/kubernetes).
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


class KubernetesProvider(
    _cdktf_9a9027ec.TerraformProvider,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.provider.KubernetesProvider",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/kubernetes kubernetes}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        alias: typing.Optional[builtins.str] = None,
        client_certificate: typing.Optional[builtins.str] = None,
        client_key: typing.Optional[builtins.str] = None,
        cluster_ca_certificate: typing.Optional[builtins.str] = None,
        config_context: typing.Optional[builtins.str] = None,
        config_context_auth_info: typing.Optional[builtins.str] = None,
        config_context_cluster: typing.Optional[builtins.str] = None,
        config_path: typing.Optional[builtins.str] = None,
        config_paths: typing.Optional[typing.Sequence[builtins.str]] = None,
        exec: typing.Optional[typing.Union["KubernetesProviderExec", typing.Dict[builtins.str, typing.Any]]] = None,
        experiments: typing.Optional[typing.Union["KubernetesProviderExperiments", typing.Dict[builtins.str, typing.Any]]] = None,
        host: typing.Optional[builtins.str] = None,
        ignore_annotations: typing.Optional[typing.Sequence[builtins.str]] = None,
        ignore_labels: typing.Optional[typing.Sequence[builtins.str]] = None,
        insecure: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        password: typing.Optional[builtins.str] = None,
        proxy_url: typing.Optional[builtins.str] = None,
        token: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/kubernetes kubernetes} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param alias: Alias name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes#alias KubernetesProvider#alias}
        :param client_certificate: PEM-encoded client certificate for TLS authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes#client_certificate KubernetesProvider#client_certificate}
        :param client_key: PEM-encoded client certificate key for TLS authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes#client_key KubernetesProvider#client_key}
        :param cluster_ca_certificate: PEM-encoded root certificates bundle for TLS authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes#cluster_ca_certificate KubernetesProvider#cluster_ca_certificate}
        :param config_context: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes#config_context KubernetesProvider#config_context}.
        :param config_context_auth_info: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes#config_context_auth_info KubernetesProvider#config_context_auth_info}.
        :param config_context_cluster: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes#config_context_cluster KubernetesProvider#config_context_cluster}.
        :param config_path: Path to the kube config file. Can be set with KUBE_CONFIG_PATH. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes#config_path KubernetesProvider#config_path}
        :param config_paths: A list of paths to kube config files. Can be set with KUBE_CONFIG_PATHS environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes#config_paths KubernetesProvider#config_paths}
        :param exec: exec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes#exec KubernetesProvider#exec}
        :param experiments: experiments block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes#experiments KubernetesProvider#experiments}
        :param host: The hostname (in form of URI) of Kubernetes master. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes#host KubernetesProvider#host}
        :param ignore_annotations: List of Kubernetes metadata annotations to ignore across all resources handled by this provider for situations where external systems are managing certain resource annotations. Each item is a regular expression. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes#ignore_annotations KubernetesProvider#ignore_annotations}
        :param ignore_labels: List of Kubernetes metadata labels to ignore across all resources handled by this provider for situations where external systems are managing certain resource labels. Each item is a regular expression. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes#ignore_labels KubernetesProvider#ignore_labels}
        :param insecure: Whether server should be accessed without verifying the TLS certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes#insecure KubernetesProvider#insecure}
        :param password: The password to use for HTTP basic authentication when accessing the Kubernetes master endpoint. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes#password KubernetesProvider#password}
        :param proxy_url: URL to the proxy to be used for all API requests. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes#proxy_url KubernetesProvider#proxy_url}
        :param token: Token to authenticate an service account. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes#token KubernetesProvider#token}
        :param username: The username to use for HTTP basic authentication when accessing the Kubernetes master endpoint. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes#username KubernetesProvider#username}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4295596c0ba0e9def41a82553dd7d1904ba7303f56d65faa88effdb142bcabb4)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = KubernetesProviderConfig(
            alias=alias,
            client_certificate=client_certificate,
            client_key=client_key,
            cluster_ca_certificate=cluster_ca_certificate,
            config_context=config_context,
            config_context_auth_info=config_context_auth_info,
            config_context_cluster=config_context_cluster,
            config_path=config_path,
            config_paths=config_paths,
            exec=exec,
            experiments=experiments,
            host=host,
            ignore_annotations=ignore_annotations,
            ignore_labels=ignore_labels,
            insecure=insecure,
            password=password,
            proxy_url=proxy_url,
            token=token,
            username=username,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="resetAlias")
    def reset_alias(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlias", []))

    @jsii.member(jsii_name="resetClientCertificate")
    def reset_client_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientCertificate", []))

    @jsii.member(jsii_name="resetClientKey")
    def reset_client_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientKey", []))

    @jsii.member(jsii_name="resetClusterCaCertificate")
    def reset_cluster_ca_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClusterCaCertificate", []))

    @jsii.member(jsii_name="resetConfigContext")
    def reset_config_context(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfigContext", []))

    @jsii.member(jsii_name="resetConfigContextAuthInfo")
    def reset_config_context_auth_info(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfigContextAuthInfo", []))

    @jsii.member(jsii_name="resetConfigContextCluster")
    def reset_config_context_cluster(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfigContextCluster", []))

    @jsii.member(jsii_name="resetConfigPath")
    def reset_config_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfigPath", []))

    @jsii.member(jsii_name="resetConfigPaths")
    def reset_config_paths(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfigPaths", []))

    @jsii.member(jsii_name="resetExec")
    def reset_exec(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExec", []))

    @jsii.member(jsii_name="resetExperiments")
    def reset_experiments(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExperiments", []))

    @jsii.member(jsii_name="resetHost")
    def reset_host(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHost", []))

    @jsii.member(jsii_name="resetIgnoreAnnotations")
    def reset_ignore_annotations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIgnoreAnnotations", []))

    @jsii.member(jsii_name="resetIgnoreLabels")
    def reset_ignore_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIgnoreLabels", []))

    @jsii.member(jsii_name="resetInsecure")
    def reset_insecure(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInsecure", []))

    @jsii.member(jsii_name="resetPassword")
    def reset_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassword", []))

    @jsii.member(jsii_name="resetProxyUrl")
    def reset_proxy_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProxyUrl", []))

    @jsii.member(jsii_name="resetToken")
    def reset_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetToken", []))

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
    @jsii.member(jsii_name="aliasInput")
    def alias_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aliasInput"))

    @builtins.property
    @jsii.member(jsii_name="clientCertificateInput")
    def client_certificate_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientCertificateInput"))

    @builtins.property
    @jsii.member(jsii_name="clientKeyInput")
    def client_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterCaCertificateInput")
    def cluster_ca_certificate_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterCaCertificateInput"))

    @builtins.property
    @jsii.member(jsii_name="configContextAuthInfoInput")
    def config_context_auth_info_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "configContextAuthInfoInput"))

    @builtins.property
    @jsii.member(jsii_name="configContextClusterInput")
    def config_context_cluster_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "configContextClusterInput"))

    @builtins.property
    @jsii.member(jsii_name="configContextInput")
    def config_context_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "configContextInput"))

    @builtins.property
    @jsii.member(jsii_name="configPathInput")
    def config_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "configPathInput"))

    @builtins.property
    @jsii.member(jsii_name="configPathsInput")
    def config_paths_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "configPathsInput"))

    @builtins.property
    @jsii.member(jsii_name="execInput")
    def exec_input(self) -> typing.Optional["KubernetesProviderExec"]:
        return typing.cast(typing.Optional["KubernetesProviderExec"], jsii.get(self, "execInput"))

    @builtins.property
    @jsii.member(jsii_name="experimentsInput")
    def experiments_input(self) -> typing.Optional["KubernetesProviderExperiments"]:
        return typing.cast(typing.Optional["KubernetesProviderExperiments"], jsii.get(self, "experimentsInput"))

    @builtins.property
    @jsii.member(jsii_name="hostInput")
    def host_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostInput"))

    @builtins.property
    @jsii.member(jsii_name="ignoreAnnotationsInput")
    def ignore_annotations_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "ignoreAnnotationsInput"))

    @builtins.property
    @jsii.member(jsii_name="ignoreLabelsInput")
    def ignore_labels_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "ignoreLabelsInput"))

    @builtins.property
    @jsii.member(jsii_name="insecureInput")
    def insecure_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "insecureInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="proxyUrlInput")
    def proxy_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "proxyUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenInput")
    def token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="alias")
    def alias(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alias"))

    @alias.setter
    def alias(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e56488ede1dd1625045554281a8bfce1b5b46781fcfb7f2edf1baeaf69ff56ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alias", value)

    @builtins.property
    @jsii.member(jsii_name="clientCertificate")
    def client_certificate(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientCertificate"))

    @client_certificate.setter
    def client_certificate(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20ea782de59bc5f1f0dfe303f5331c31ac5e819fe9d5c6aa7cda78958e2c6dbe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientCertificate", value)

    @builtins.property
    @jsii.member(jsii_name="clientKey")
    def client_key(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientKey"))

    @client_key.setter
    def client_key(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3bf979a0700291142960d6bb41e736579859556c14983896a0689e424a32d478)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientKey", value)

    @builtins.property
    @jsii.member(jsii_name="clusterCaCertificate")
    def cluster_ca_certificate(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterCaCertificate"))

    @cluster_ca_certificate.setter
    def cluster_ca_certificate(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__597d82d8b1b2db7a8d7d639b9bc119b87ab6f4db79cbe0108b5b36c5802ffedc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterCaCertificate", value)

    @builtins.property
    @jsii.member(jsii_name="configContext")
    def config_context(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "configContext"))

    @config_context.setter
    def config_context(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1922a1885aa8cff7c78613d94af565df6cf269c153c09ca9c4913d26ebf99321)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configContext", value)

    @builtins.property
    @jsii.member(jsii_name="configContextAuthInfo")
    def config_context_auth_info(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "configContextAuthInfo"))

    @config_context_auth_info.setter
    def config_context_auth_info(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a84a6aed95bcf5ec7aea5fd99070f715f5f82f1411fb7e84e89e35dc19a84966)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configContextAuthInfo", value)

    @builtins.property
    @jsii.member(jsii_name="configContextCluster")
    def config_context_cluster(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "configContextCluster"))

    @config_context_cluster.setter
    def config_context_cluster(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eef255451037083fe933dbfbb85d0df5ff3776c4dfcfa0d234a796b60e2b2fbc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configContextCluster", value)

    @builtins.property
    @jsii.member(jsii_name="configPath")
    def config_path(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "configPath"))

    @config_path.setter
    def config_path(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb438842f634035d8ea1843be477b4979ec9805abf6b55b1fd65d51a1ec0eeab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configPath", value)

    @builtins.property
    @jsii.member(jsii_name="configPaths")
    def config_paths(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "configPaths"))

    @config_paths.setter
    def config_paths(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1274e3cf9913292022f8745f4a596e12e1da14d487d5e98c03fcd46671c49df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configPaths", value)

    @builtins.property
    @jsii.member(jsii_name="exec")
    def exec(self) -> typing.Optional["KubernetesProviderExec"]:
        return typing.cast(typing.Optional["KubernetesProviderExec"], jsii.get(self, "exec"))

    @exec.setter
    def exec(self, value: typing.Optional["KubernetesProviderExec"]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__48e12a4f39389c082617eb174dd0c19f66b708e513e0a5a7505d87886631148f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exec", value)

    @builtins.property
    @jsii.member(jsii_name="experiments")
    def experiments(self) -> typing.Optional["KubernetesProviderExperiments"]:
        return typing.cast(typing.Optional["KubernetesProviderExperiments"], jsii.get(self, "experiments"))

    @experiments.setter
    def experiments(
        self,
        value: typing.Optional["KubernetesProviderExperiments"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__088ee8fad9aeac6803ed7422bbbe5f20285a98ff503edcc107af151e62206b35)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "experiments", value)

    @builtins.property
    @jsii.member(jsii_name="host")
    def host(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "host"))

    @host.setter
    def host(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e196593702476df2e0ccf58223f7d1d6419109d8505a30a4dd5c181789562ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "host", value)

    @builtins.property
    @jsii.member(jsii_name="ignoreAnnotations")
    def ignore_annotations(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "ignoreAnnotations"))

    @ignore_annotations.setter
    def ignore_annotations(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84871c3e48b95337a331e5eda31f47e423b7723d18d09b7acaf6fb6b4acc092d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ignoreAnnotations", value)

    @builtins.property
    @jsii.member(jsii_name="ignoreLabels")
    def ignore_labels(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "ignoreLabels"))

    @ignore_labels.setter
    def ignore_labels(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e970592d4014c36aa8d6f07699420244862728bfd7c00986cbe3dc3e527e0fcd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ignoreLabels", value)

    @builtins.property
    @jsii.member(jsii_name="insecure")
    def insecure(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "insecure"))

    @insecure.setter
    def insecure(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b37527674cf5c3bb097554278640b4e43112c94b37f55e54148983e61c14b47)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "insecure", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "password"))

    @password.setter
    def password(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b23e64780433fe2653c142bd2d702dd52c38141270beeb10f0dede75f46a08d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="proxyUrl")
    def proxy_url(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "proxyUrl"))

    @proxy_url.setter
    def proxy_url(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__390026d5f05624451ab72a3b4026db587ca44ef5e01d54ea197a20b30e9fe7a1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "proxyUrl", value)

    @builtins.property
    @jsii.member(jsii_name="token")
    def token(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "token"))

    @token.setter
    def token(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d09e014f06c6110a609bb067fcf75e2de7e1de371bb2c8a9b93bad30b45276d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "token", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "username"))

    @username.setter
    def username(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__226d9121e9ff9fc1682f7ddb512a99e1b8cfea090cc4b1272833b689376eb6ef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)


@jsii.data_type(
    jsii_type="kubernetes.provider.KubernetesProviderConfig",
    jsii_struct_bases=[],
    name_mapping={
        "alias": "alias",
        "client_certificate": "clientCertificate",
        "client_key": "clientKey",
        "cluster_ca_certificate": "clusterCaCertificate",
        "config_context": "configContext",
        "config_context_auth_info": "configContextAuthInfo",
        "config_context_cluster": "configContextCluster",
        "config_path": "configPath",
        "config_paths": "configPaths",
        "exec": "exec",
        "experiments": "experiments",
        "host": "host",
        "ignore_annotations": "ignoreAnnotations",
        "ignore_labels": "ignoreLabels",
        "insecure": "insecure",
        "password": "password",
        "proxy_url": "proxyUrl",
        "token": "token",
        "username": "username",
    },
)
class KubernetesProviderConfig:
    def __init__(
        self,
        *,
        alias: typing.Optional[builtins.str] = None,
        client_certificate: typing.Optional[builtins.str] = None,
        client_key: typing.Optional[builtins.str] = None,
        cluster_ca_certificate: typing.Optional[builtins.str] = None,
        config_context: typing.Optional[builtins.str] = None,
        config_context_auth_info: typing.Optional[builtins.str] = None,
        config_context_cluster: typing.Optional[builtins.str] = None,
        config_path: typing.Optional[builtins.str] = None,
        config_paths: typing.Optional[typing.Sequence[builtins.str]] = None,
        exec: typing.Optional[typing.Union["KubernetesProviderExec", typing.Dict[builtins.str, typing.Any]]] = None,
        experiments: typing.Optional[typing.Union["KubernetesProviderExperiments", typing.Dict[builtins.str, typing.Any]]] = None,
        host: typing.Optional[builtins.str] = None,
        ignore_annotations: typing.Optional[typing.Sequence[builtins.str]] = None,
        ignore_labels: typing.Optional[typing.Sequence[builtins.str]] = None,
        insecure: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        password: typing.Optional[builtins.str] = None,
        proxy_url: typing.Optional[builtins.str] = None,
        token: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param alias: Alias name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes#alias KubernetesProvider#alias}
        :param client_certificate: PEM-encoded client certificate for TLS authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes#client_certificate KubernetesProvider#client_certificate}
        :param client_key: PEM-encoded client certificate key for TLS authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes#client_key KubernetesProvider#client_key}
        :param cluster_ca_certificate: PEM-encoded root certificates bundle for TLS authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes#cluster_ca_certificate KubernetesProvider#cluster_ca_certificate}
        :param config_context: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes#config_context KubernetesProvider#config_context}.
        :param config_context_auth_info: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes#config_context_auth_info KubernetesProvider#config_context_auth_info}.
        :param config_context_cluster: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes#config_context_cluster KubernetesProvider#config_context_cluster}.
        :param config_path: Path to the kube config file. Can be set with KUBE_CONFIG_PATH. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes#config_path KubernetesProvider#config_path}
        :param config_paths: A list of paths to kube config files. Can be set with KUBE_CONFIG_PATHS environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes#config_paths KubernetesProvider#config_paths}
        :param exec: exec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes#exec KubernetesProvider#exec}
        :param experiments: experiments block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes#experiments KubernetesProvider#experiments}
        :param host: The hostname (in form of URI) of Kubernetes master. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes#host KubernetesProvider#host}
        :param ignore_annotations: List of Kubernetes metadata annotations to ignore across all resources handled by this provider for situations where external systems are managing certain resource annotations. Each item is a regular expression. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes#ignore_annotations KubernetesProvider#ignore_annotations}
        :param ignore_labels: List of Kubernetes metadata labels to ignore across all resources handled by this provider for situations where external systems are managing certain resource labels. Each item is a regular expression. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes#ignore_labels KubernetesProvider#ignore_labels}
        :param insecure: Whether server should be accessed without verifying the TLS certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes#insecure KubernetesProvider#insecure}
        :param password: The password to use for HTTP basic authentication when accessing the Kubernetes master endpoint. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes#password KubernetesProvider#password}
        :param proxy_url: URL to the proxy to be used for all API requests. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes#proxy_url KubernetesProvider#proxy_url}
        :param token: Token to authenticate an service account. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes#token KubernetesProvider#token}
        :param username: The username to use for HTTP basic authentication when accessing the Kubernetes master endpoint. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes#username KubernetesProvider#username}
        '''
        if isinstance(exec, dict):
            exec = KubernetesProviderExec(**exec)
        if isinstance(experiments, dict):
            experiments = KubernetesProviderExperiments(**experiments)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dafa5f247742dbe21f39f8fc1d0973df6b7d5bb3ec7723cb5fb32787f0f625d0)
            check_type(argname="argument alias", value=alias, expected_type=type_hints["alias"])
            check_type(argname="argument client_certificate", value=client_certificate, expected_type=type_hints["client_certificate"])
            check_type(argname="argument client_key", value=client_key, expected_type=type_hints["client_key"])
            check_type(argname="argument cluster_ca_certificate", value=cluster_ca_certificate, expected_type=type_hints["cluster_ca_certificate"])
            check_type(argname="argument config_context", value=config_context, expected_type=type_hints["config_context"])
            check_type(argname="argument config_context_auth_info", value=config_context_auth_info, expected_type=type_hints["config_context_auth_info"])
            check_type(argname="argument config_context_cluster", value=config_context_cluster, expected_type=type_hints["config_context_cluster"])
            check_type(argname="argument config_path", value=config_path, expected_type=type_hints["config_path"])
            check_type(argname="argument config_paths", value=config_paths, expected_type=type_hints["config_paths"])
            check_type(argname="argument exec", value=exec, expected_type=type_hints["exec"])
            check_type(argname="argument experiments", value=experiments, expected_type=type_hints["experiments"])
            check_type(argname="argument host", value=host, expected_type=type_hints["host"])
            check_type(argname="argument ignore_annotations", value=ignore_annotations, expected_type=type_hints["ignore_annotations"])
            check_type(argname="argument ignore_labels", value=ignore_labels, expected_type=type_hints["ignore_labels"])
            check_type(argname="argument insecure", value=insecure, expected_type=type_hints["insecure"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument proxy_url", value=proxy_url, expected_type=type_hints["proxy_url"])
            check_type(argname="argument token", value=token, expected_type=type_hints["token"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if alias is not None:
            self._values["alias"] = alias
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
        if experiments is not None:
            self._values["experiments"] = experiments
        if host is not None:
            self._values["host"] = host
        if ignore_annotations is not None:
            self._values["ignore_annotations"] = ignore_annotations
        if ignore_labels is not None:
            self._values["ignore_labels"] = ignore_labels
        if insecure is not None:
            self._values["insecure"] = insecure
        if password is not None:
            self._values["password"] = password
        if proxy_url is not None:
            self._values["proxy_url"] = proxy_url
        if token is not None:
            self._values["token"] = token
        if username is not None:
            self._values["username"] = username

    @builtins.property
    def alias(self) -> typing.Optional[builtins.str]:
        '''Alias name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes#alias KubernetesProvider#alias}
        '''
        result = self._values.get("alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_certificate(self) -> typing.Optional[builtins.str]:
        '''PEM-encoded client certificate for TLS authentication.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes#client_certificate KubernetesProvider#client_certificate}
        '''
        result = self._values.get("client_certificate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_key(self) -> typing.Optional[builtins.str]:
        '''PEM-encoded client certificate key for TLS authentication.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes#client_key KubernetesProvider#client_key}
        '''
        result = self._values.get("client_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cluster_ca_certificate(self) -> typing.Optional[builtins.str]:
        '''PEM-encoded root certificates bundle for TLS authentication.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes#cluster_ca_certificate KubernetesProvider#cluster_ca_certificate}
        '''
        result = self._values.get("cluster_ca_certificate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def config_context(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes#config_context KubernetesProvider#config_context}.'''
        result = self._values.get("config_context")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def config_context_auth_info(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes#config_context_auth_info KubernetesProvider#config_context_auth_info}.'''
        result = self._values.get("config_context_auth_info")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def config_context_cluster(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes#config_context_cluster KubernetesProvider#config_context_cluster}.'''
        result = self._values.get("config_context_cluster")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def config_path(self) -> typing.Optional[builtins.str]:
        '''Path to the kube config file. Can be set with KUBE_CONFIG_PATH.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes#config_path KubernetesProvider#config_path}
        '''
        result = self._values.get("config_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def config_paths(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of paths to kube config files. Can be set with KUBE_CONFIG_PATHS environment variable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes#config_paths KubernetesProvider#config_paths}
        '''
        result = self._values.get("config_paths")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def exec(self) -> typing.Optional["KubernetesProviderExec"]:
        '''exec block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes#exec KubernetesProvider#exec}
        '''
        result = self._values.get("exec")
        return typing.cast(typing.Optional["KubernetesProviderExec"], result)

    @builtins.property
    def experiments(self) -> typing.Optional["KubernetesProviderExperiments"]:
        '''experiments block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes#experiments KubernetesProvider#experiments}
        '''
        result = self._values.get("experiments")
        return typing.cast(typing.Optional["KubernetesProviderExperiments"], result)

    @builtins.property
    def host(self) -> typing.Optional[builtins.str]:
        '''The hostname (in form of URI) of Kubernetes master.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes#host KubernetesProvider#host}
        '''
        result = self._values.get("host")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ignore_annotations(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of Kubernetes metadata annotations to ignore across all resources handled by this provider for situations where external systems are managing certain resource annotations.

        Each item is a regular expression.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes#ignore_annotations KubernetesProvider#ignore_annotations}
        '''
        result = self._values.get("ignore_annotations")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def ignore_labels(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of Kubernetes metadata labels to ignore across all resources handled by this provider for situations where external systems are managing certain resource labels.

        Each item is a regular expression.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes#ignore_labels KubernetesProvider#ignore_labels}
        '''
        result = self._values.get("ignore_labels")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def insecure(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether server should be accessed without verifying the TLS certificate.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes#insecure KubernetesProvider#insecure}
        '''
        result = self._values.get("insecure")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''The password to use for HTTP basic authentication when accessing the Kubernetes master endpoint.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes#password KubernetesProvider#password}
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def proxy_url(self) -> typing.Optional[builtins.str]:
        '''URL to the proxy to be used for all API requests.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes#proxy_url KubernetesProvider#proxy_url}
        '''
        result = self._values.get("proxy_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def token(self) -> typing.Optional[builtins.str]:
        '''Token to authenticate an service account.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes#token KubernetesProvider#token}
        '''
        result = self._values.get("token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''The username to use for HTTP basic authentication when accessing the Kubernetes master endpoint.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes#username KubernetesProvider#username}
        '''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubernetesProviderConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kubernetes.provider.KubernetesProviderExec",
    jsii_struct_bases=[],
    name_mapping={
        "api_version": "apiVersion",
        "command": "command",
        "args": "args",
        "env": "env",
    },
)
class KubernetesProviderExec:
    def __init__(
        self,
        *,
        api_version: builtins.str,
        command: builtins.str,
        args: typing.Optional[typing.Sequence[builtins.str]] = None,
        env: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param api_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes#api_version KubernetesProvider#api_version}.
        :param command: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes#command KubernetesProvider#command}.
        :param args: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes#args KubernetesProvider#args}.
        :param env: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes#env KubernetesProvider#env}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f996b06f16db06fa73c395cf8387f02102133787799238c438379388d3b58e61)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes#api_version KubernetesProvider#api_version}.'''
        result = self._values.get("api_version")
        assert result is not None, "Required property 'api_version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def command(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes#command KubernetesProvider#command}.'''
        result = self._values.get("command")
        assert result is not None, "Required property 'command' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def args(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes#args KubernetesProvider#args}.'''
        result = self._values.get("args")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def env(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes#env KubernetesProvider#env}.'''
        result = self._values.get("env")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubernetesProviderExec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kubernetes.provider.KubernetesProviderExperiments",
    jsii_struct_bases=[],
    name_mapping={"manifest_resource": "manifestResource"},
)
class KubernetesProviderExperiments:
    def __init__(
        self,
        *,
        manifest_resource: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param manifest_resource: Enable the ``kubernetes_manifest`` resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes#manifest_resource KubernetesProvider#manifest_resource}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__71b0d5062b581fafd9bbe1d2f2ec55fdde646d35bdb13af6640869bf0508d756)
            check_type(argname="argument manifest_resource", value=manifest_resource, expected_type=type_hints["manifest_resource"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if manifest_resource is not None:
            self._values["manifest_resource"] = manifest_resource

    @builtins.property
    def manifest_resource(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Enable the ``kubernetes_manifest`` resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes#manifest_resource KubernetesProvider#manifest_resource}
        '''
        result = self._values.get("manifest_resource")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubernetesProviderExperiments(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "KubernetesProvider",
    "KubernetesProviderConfig",
    "KubernetesProviderExec",
    "KubernetesProviderExperiments",
]

publication.publish()

def _typecheckingstub__4295596c0ba0e9def41a82553dd7d1904ba7303f56d65faa88effdb142bcabb4(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    alias: typing.Optional[builtins.str] = None,
    client_certificate: typing.Optional[builtins.str] = None,
    client_key: typing.Optional[builtins.str] = None,
    cluster_ca_certificate: typing.Optional[builtins.str] = None,
    config_context: typing.Optional[builtins.str] = None,
    config_context_auth_info: typing.Optional[builtins.str] = None,
    config_context_cluster: typing.Optional[builtins.str] = None,
    config_path: typing.Optional[builtins.str] = None,
    config_paths: typing.Optional[typing.Sequence[builtins.str]] = None,
    exec: typing.Optional[typing.Union[KubernetesProviderExec, typing.Dict[builtins.str, typing.Any]]] = None,
    experiments: typing.Optional[typing.Union[KubernetesProviderExperiments, typing.Dict[builtins.str, typing.Any]]] = None,
    host: typing.Optional[builtins.str] = None,
    ignore_annotations: typing.Optional[typing.Sequence[builtins.str]] = None,
    ignore_labels: typing.Optional[typing.Sequence[builtins.str]] = None,
    insecure: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    password: typing.Optional[builtins.str] = None,
    proxy_url: typing.Optional[builtins.str] = None,
    token: typing.Optional[builtins.str] = None,
    username: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e56488ede1dd1625045554281a8bfce1b5b46781fcfb7f2edf1baeaf69ff56ae(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20ea782de59bc5f1f0dfe303f5331c31ac5e819fe9d5c6aa7cda78958e2c6dbe(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3bf979a0700291142960d6bb41e736579859556c14983896a0689e424a32d478(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__597d82d8b1b2db7a8d7d639b9bc119b87ab6f4db79cbe0108b5b36c5802ffedc(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1922a1885aa8cff7c78613d94af565df6cf269c153c09ca9c4913d26ebf99321(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a84a6aed95bcf5ec7aea5fd99070f715f5f82f1411fb7e84e89e35dc19a84966(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eef255451037083fe933dbfbb85d0df5ff3776c4dfcfa0d234a796b60e2b2fbc(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb438842f634035d8ea1843be477b4979ec9805abf6b55b1fd65d51a1ec0eeab(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1274e3cf9913292022f8745f4a596e12e1da14d487d5e98c03fcd46671c49df(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48e12a4f39389c082617eb174dd0c19f66b708e513e0a5a7505d87886631148f(
    value: typing.Optional[KubernetesProviderExec],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__088ee8fad9aeac6803ed7422bbbe5f20285a98ff503edcc107af151e62206b35(
    value: typing.Optional[KubernetesProviderExperiments],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e196593702476df2e0ccf58223f7d1d6419109d8505a30a4dd5c181789562ce(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84871c3e48b95337a331e5eda31f47e423b7723d18d09b7acaf6fb6b4acc092d(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e970592d4014c36aa8d6f07699420244862728bfd7c00986cbe3dc3e527e0fcd(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b37527674cf5c3bb097554278640b4e43112c94b37f55e54148983e61c14b47(
    value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b23e64780433fe2653c142bd2d702dd52c38141270beeb10f0dede75f46a08d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__390026d5f05624451ab72a3b4026db587ca44ef5e01d54ea197a20b30e9fe7a1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d09e014f06c6110a609bb067fcf75e2de7e1de371bb2c8a9b93bad30b45276d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__226d9121e9ff9fc1682f7ddb512a99e1b8cfea090cc4b1272833b689376eb6ef(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dafa5f247742dbe21f39f8fc1d0973df6b7d5bb3ec7723cb5fb32787f0f625d0(
    *,
    alias: typing.Optional[builtins.str] = None,
    client_certificate: typing.Optional[builtins.str] = None,
    client_key: typing.Optional[builtins.str] = None,
    cluster_ca_certificate: typing.Optional[builtins.str] = None,
    config_context: typing.Optional[builtins.str] = None,
    config_context_auth_info: typing.Optional[builtins.str] = None,
    config_context_cluster: typing.Optional[builtins.str] = None,
    config_path: typing.Optional[builtins.str] = None,
    config_paths: typing.Optional[typing.Sequence[builtins.str]] = None,
    exec: typing.Optional[typing.Union[KubernetesProviderExec, typing.Dict[builtins.str, typing.Any]]] = None,
    experiments: typing.Optional[typing.Union[KubernetesProviderExperiments, typing.Dict[builtins.str, typing.Any]]] = None,
    host: typing.Optional[builtins.str] = None,
    ignore_annotations: typing.Optional[typing.Sequence[builtins.str]] = None,
    ignore_labels: typing.Optional[typing.Sequence[builtins.str]] = None,
    insecure: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    password: typing.Optional[builtins.str] = None,
    proxy_url: typing.Optional[builtins.str] = None,
    token: typing.Optional[builtins.str] = None,
    username: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f996b06f16db06fa73c395cf8387f02102133787799238c438379388d3b58e61(
    *,
    api_version: builtins.str,
    command: builtins.str,
    args: typing.Optional[typing.Sequence[builtins.str]] = None,
    env: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71b0d5062b581fafd9bbe1d2f2ec55fdde646d35bdb13af6640869bf0508d756(
    *,
    manifest_resource: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass
