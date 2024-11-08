'''
# `kubernetes_pod_security_policy_v1beta1`

Refer to the Terraform Registory for docs: [`kubernetes_pod_security_policy_v1beta1`](https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1).
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


class PodSecurityPolicyV1Beta1(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1 kubernetes_pod_security_policy_v1beta1}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        metadata: typing.Union["PodSecurityPolicyV1Beta1Metadata", typing.Dict[builtins.str, typing.Any]],
        spec: typing.Union["PodSecurityPolicyV1Beta1Spec", typing.Dict[builtins.str, typing.Any]],
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1 kubernetes_pod_security_policy_v1beta1} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param metadata: metadata block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#metadata PodSecurityPolicyV1Beta1#metadata}
        :param spec: spec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#spec PodSecurityPolicyV1Beta1#spec}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#id PodSecurityPolicyV1Beta1#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9679c31c9723b516c52d280faa70e2cb64dd7a408bedd8e57161d52c8d7dbbb1)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = PodSecurityPolicyV1Beta1Config(
            metadata=metadata,
            spec=spec,
            id=id,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putMetadata")
    def put_metadata(
        self,
        *,
        annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param annotations: An unstructured key value map stored with the podsecuritypolicy that may be used to store arbitrary metadata. More info: http://kubernetes.io/docs/user-guide/annotations Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#annotations PodSecurityPolicyV1Beta1#annotations}
        :param labels: Map of string keys and values that can be used to organize and categorize (scope and select) the podsecuritypolicy. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#labels PodSecurityPolicyV1Beta1#labels}
        :param name: Name of the podsecuritypolicy, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#name PodSecurityPolicyV1Beta1#name}
        '''
        value = PodSecurityPolicyV1Beta1Metadata(
            annotations=annotations, labels=labels, name=name
        )

        return typing.cast(None, jsii.invoke(self, "putMetadata", [value]))

    @jsii.member(jsii_name="putSpec")
    def put_spec(
        self,
        *,
        fs_group: typing.Union["PodSecurityPolicyV1Beta1SpecFsGroup", typing.Dict[builtins.str, typing.Any]],
        run_as_user: typing.Union["PodSecurityPolicyV1Beta1SpecRunAsUser", typing.Dict[builtins.str, typing.Any]],
        supplemental_groups: typing.Union["PodSecurityPolicyV1Beta1SpecSupplementalGroups", typing.Dict[builtins.str, typing.Any]],
        allowed_capabilities: typing.Optional[typing.Sequence[builtins.str]] = None,
        allowed_flex_volumes: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PodSecurityPolicyV1Beta1SpecAllowedFlexVolumes", typing.Dict[builtins.str, typing.Any]]]]] = None,
        allowed_host_paths: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PodSecurityPolicyV1Beta1SpecAllowedHostPaths", typing.Dict[builtins.str, typing.Any]]]]] = None,
        allowed_proc_mount_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        allowed_unsafe_sysctls: typing.Optional[typing.Sequence[builtins.str]] = None,
        allow_privilege_escalation: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        default_add_capabilities: typing.Optional[typing.Sequence[builtins.str]] = None,
        default_allow_privilege_escalation: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        forbidden_sysctls: typing.Optional[typing.Sequence[builtins.str]] = None,
        host_ipc: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        host_network: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        host_pid: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        host_ports: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PodSecurityPolicyV1Beta1SpecHostPorts", typing.Dict[builtins.str, typing.Any]]]]] = None,
        privileged: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        read_only_root_filesystem: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        required_drop_capabilities: typing.Optional[typing.Sequence[builtins.str]] = None,
        run_as_group: typing.Optional[typing.Union["PodSecurityPolicyV1Beta1SpecRunAsGroup", typing.Dict[builtins.str, typing.Any]]] = None,
        se_linux: typing.Optional[typing.Union["PodSecurityPolicyV1Beta1SpecSeLinux", typing.Dict[builtins.str, typing.Any]]] = None,
        volumes: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param fs_group: fs_group block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#fs_group PodSecurityPolicyV1Beta1#fs_group}
        :param run_as_user: run_as_user block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#run_as_user PodSecurityPolicyV1Beta1#run_as_user}
        :param supplemental_groups: supplemental_groups block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#supplemental_groups PodSecurityPolicyV1Beta1#supplemental_groups}
        :param allowed_capabilities: allowedCapabilities is a list of capabilities that can be requested to add to the container. Capabilities in this field may be added at the pod author's discretion. You must not list a capability in both allowedCapabilities and requiredDropCapabilities. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#allowed_capabilities PodSecurityPolicyV1Beta1#allowed_capabilities}
        :param allowed_flex_volumes: allowed_flex_volumes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#allowed_flex_volumes PodSecurityPolicyV1Beta1#allowed_flex_volumes}
        :param allowed_host_paths: allowed_host_paths block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#allowed_host_paths PodSecurityPolicyV1Beta1#allowed_host_paths}
        :param allowed_proc_mount_types: AllowedProcMountTypes is an allowlist of allowed ProcMountTypes. Empty or nil indicates that only the DefaultProcMountType may be used. This requires the ProcMountType feature flag to be enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#allowed_proc_mount_types PodSecurityPolicyV1Beta1#allowed_proc_mount_types}
        :param allowed_unsafe_sysctls: allowedUnsafeSysctls is a list of explicitly allowed unsafe sysctls, defaults to none. Each entry is either a plain sysctl name or ends in "*" in which case it is considered as a prefix of allowed sysctls. Single * means all unsafe sysctls are allowed. Kubelet has to allowlist all allowed unsafe sysctls explicitly to avoid rejection. Examples: e.g. "foo/*" allows "foo/bar", "foo/baz", etc. e.g. "foo.*" allows "foo.bar", "foo.baz", etc. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#allowed_unsafe_sysctls PodSecurityPolicyV1Beta1#allowed_unsafe_sysctls}
        :param allow_privilege_escalation: allowPrivilegeEscalation determines if a pod can request to allow privilege escalation. If unspecified, defaults to true. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#allow_privilege_escalation PodSecurityPolicyV1Beta1#allow_privilege_escalation}
        :param default_add_capabilities: defaultAddCapabilities is the default set of capabilities that will be added to the container unless the pod spec specifically drops the capability. You may not list a capability in both defaultAddCapabilities and requiredDropCapabilities. Capabilities added here are implicitly allowed, and need not be included in the allowedCapabilities list. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#default_add_capabilities PodSecurityPolicyV1Beta1#default_add_capabilities}
        :param default_allow_privilege_escalation: defaultAllowPrivilegeEscalation controls the default setting for whether a process can gain more privileges than its parent process. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#default_allow_privilege_escalation PodSecurityPolicyV1Beta1#default_allow_privilege_escalation}
        :param forbidden_sysctls: forbiddenSysctls is a list of explicitly forbidden sysctls, defaults to none. Each entry is either a plain sysctl name or ends in "*" in which case it is considered as a prefix of forbidden sysctls. Single * means all sysctls are forbidden. Examples: e.g. "foo/*" forbids "foo/bar", "foo/baz", etc. e.g. "foo.*" forbids "foo.bar", "foo.baz", etc. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#forbidden_sysctls PodSecurityPolicyV1Beta1#forbidden_sysctls}
        :param host_ipc: hostIPC determines if the policy allows the use of HostIPC in the pod spec. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#host_ipc PodSecurityPolicyV1Beta1#host_ipc}
        :param host_network: hostNetwork determines if the policy allows the use of HostNetwork in the pod spec. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#host_network PodSecurityPolicyV1Beta1#host_network}
        :param host_pid: hostPID determines if the policy allows the use of HostPID in the pod spec. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#host_pid PodSecurityPolicyV1Beta1#host_pid}
        :param host_ports: host_ports block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#host_ports PodSecurityPolicyV1Beta1#host_ports}
        :param privileged: privileged determines if a pod can request to be run as privileged. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#privileged PodSecurityPolicyV1Beta1#privileged}
        :param read_only_root_filesystem: readOnlyRootFilesystem when set to true will force containers to run with a read only root file system. If the container specifically requests to run with a non-read only root file system the PSP should deny the pod. If set to false the container may run with a read only root file system if it wishes but it will not be forced to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#read_only_root_filesystem PodSecurityPolicyV1Beta1#read_only_root_filesystem}
        :param required_drop_capabilities: requiredDropCapabilities are the capabilities that will be dropped from the container. These are required to be dropped and cannot be added. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#required_drop_capabilities PodSecurityPolicyV1Beta1#required_drop_capabilities}
        :param run_as_group: run_as_group block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#run_as_group PodSecurityPolicyV1Beta1#run_as_group}
        :param se_linux: se_linux block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#se_linux PodSecurityPolicyV1Beta1#se_linux}
        :param volumes: volumes is an allowlist of volume plugins. Empty indicates that no volumes may be used. To allow all volumes you may use '*'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#volumes PodSecurityPolicyV1Beta1#volumes}
        '''
        value = PodSecurityPolicyV1Beta1Spec(
            fs_group=fs_group,
            run_as_user=run_as_user,
            supplemental_groups=supplemental_groups,
            allowed_capabilities=allowed_capabilities,
            allowed_flex_volumes=allowed_flex_volumes,
            allowed_host_paths=allowed_host_paths,
            allowed_proc_mount_types=allowed_proc_mount_types,
            allowed_unsafe_sysctls=allowed_unsafe_sysctls,
            allow_privilege_escalation=allow_privilege_escalation,
            default_add_capabilities=default_add_capabilities,
            default_allow_privilege_escalation=default_allow_privilege_escalation,
            forbidden_sysctls=forbidden_sysctls,
            host_ipc=host_ipc,
            host_network=host_network,
            host_pid=host_pid,
            host_ports=host_ports,
            privileged=privileged,
            read_only_root_filesystem=read_only_root_filesystem,
            required_drop_capabilities=required_drop_capabilities,
            run_as_group=run_as_group,
            se_linux=se_linux,
            volumes=volumes,
        )

        return typing.cast(None, jsii.invoke(self, "putSpec", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="metadata")
    def metadata(self) -> "PodSecurityPolicyV1Beta1MetadataOutputReference":
        return typing.cast("PodSecurityPolicyV1Beta1MetadataOutputReference", jsii.get(self, "metadata"))

    @builtins.property
    @jsii.member(jsii_name="spec")
    def spec(self) -> "PodSecurityPolicyV1Beta1SpecOutputReference":
        return typing.cast("PodSecurityPolicyV1Beta1SpecOutputReference", jsii.get(self, "spec"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="metadataInput")
    def metadata_input(self) -> typing.Optional["PodSecurityPolicyV1Beta1Metadata"]:
        return typing.cast(typing.Optional["PodSecurityPolicyV1Beta1Metadata"], jsii.get(self, "metadataInput"))

    @builtins.property
    @jsii.member(jsii_name="specInput")
    def spec_input(self) -> typing.Optional["PodSecurityPolicyV1Beta1Spec"]:
        return typing.cast(typing.Optional["PodSecurityPolicyV1Beta1Spec"], jsii.get(self, "specInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0347391f35c50b6c2ccf6677f55d0d25804fde75b6dce3a26c16856000a2dcb3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)


@jsii.data_type(
    jsii_type="kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1Config",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "metadata": "metadata",
        "spec": "spec",
        "id": "id",
    },
)
class PodSecurityPolicyV1Beta1Config(_cdktf_9a9027ec.TerraformMetaArguments):
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
        metadata: typing.Union["PodSecurityPolicyV1Beta1Metadata", typing.Dict[builtins.str, typing.Any]],
        spec: typing.Union["PodSecurityPolicyV1Beta1Spec", typing.Dict[builtins.str, typing.Any]],
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param metadata: metadata block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#metadata PodSecurityPolicyV1Beta1#metadata}
        :param spec: spec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#spec PodSecurityPolicyV1Beta1#spec}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#id PodSecurityPolicyV1Beta1#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(metadata, dict):
            metadata = PodSecurityPolicyV1Beta1Metadata(**metadata)
        if isinstance(spec, dict):
            spec = PodSecurityPolicyV1Beta1Spec(**spec)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b944da6757e8082a6ff12861b1ff0f85ab63c57afe28cbe91a29fbe1a2fdf3c8)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument spec", value=spec, expected_type=type_hints["spec"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "metadata": metadata,
            "spec": spec,
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
        if id is not None:
            self._values["id"] = id

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
    def metadata(self) -> "PodSecurityPolicyV1Beta1Metadata":
        '''metadata block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#metadata PodSecurityPolicyV1Beta1#metadata}
        '''
        result = self._values.get("metadata")
        assert result is not None, "Required property 'metadata' is missing"
        return typing.cast("PodSecurityPolicyV1Beta1Metadata", result)

    @builtins.property
    def spec(self) -> "PodSecurityPolicyV1Beta1Spec":
        '''spec block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#spec PodSecurityPolicyV1Beta1#spec}
        '''
        result = self._values.get("spec")
        assert result is not None, "Required property 'spec' is missing"
        return typing.cast("PodSecurityPolicyV1Beta1Spec", result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#id PodSecurityPolicyV1Beta1#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PodSecurityPolicyV1Beta1Config(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1Metadata",
    jsii_struct_bases=[],
    name_mapping={"annotations": "annotations", "labels": "labels", "name": "name"},
)
class PodSecurityPolicyV1Beta1Metadata:
    def __init__(
        self,
        *,
        annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param annotations: An unstructured key value map stored with the podsecuritypolicy that may be used to store arbitrary metadata. More info: http://kubernetes.io/docs/user-guide/annotations Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#annotations PodSecurityPolicyV1Beta1#annotations}
        :param labels: Map of string keys and values that can be used to organize and categorize (scope and select) the podsecuritypolicy. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#labels PodSecurityPolicyV1Beta1#labels}
        :param name: Name of the podsecuritypolicy, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#name PodSecurityPolicyV1Beta1#name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b329507f84f1b10c617c56ecd37c8158224f559278ee847f7fec805cceedd001)
            check_type(argname="argument annotations", value=annotations, expected_type=type_hints["annotations"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if annotations is not None:
            self._values["annotations"] = annotations
        if labels is not None:
            self._values["labels"] = labels
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def annotations(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''An unstructured key value map stored with the podsecuritypolicy that may be used to store arbitrary metadata.

        More info: http://kubernetes.io/docs/user-guide/annotations

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#annotations PodSecurityPolicyV1Beta1#annotations}
        '''
        result = self._values.get("annotations")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Map of string keys and values that can be used to organize and categorize (scope and select) the podsecuritypolicy.

        May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#labels PodSecurityPolicyV1Beta1#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the podsecuritypolicy, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#name PodSecurityPolicyV1Beta1#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PodSecurityPolicyV1Beta1Metadata(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PodSecurityPolicyV1Beta1MetadataOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1MetadataOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d2f148d05095f822f0a934c8884e29df8c3d983f01ea9ce50609474b65a12f44)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAnnotations")
    def reset_annotations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAnnotations", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @builtins.property
    @jsii.member(jsii_name="generation")
    def generation(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "generation"))

    @builtins.property
    @jsii.member(jsii_name="resourceVersion")
    def resource_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceVersion"))

    @builtins.property
    @jsii.member(jsii_name="uid")
    def uid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uid"))

    @builtins.property
    @jsii.member(jsii_name="annotationsInput")
    def annotations_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "annotationsInput"))

    @builtins.property
    @jsii.member(jsii_name="labelsInput")
    def labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "labelsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="annotations")
    def annotations(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "annotations"))

    @annotations.setter
    def annotations(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1406501757a30deaec4413d25160121da72005816a123c7329ab7020b3d48f90)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "annotations", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__377424566de947b9f69668660ed4ea5c725b3b9632cfebfff629ff54d22fbfd7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a90150b7e3765f33e71082f2ffb7ef8f2bbccf856d66409942170966aaa79508)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[PodSecurityPolicyV1Beta1Metadata]:
        return typing.cast(typing.Optional[PodSecurityPolicyV1Beta1Metadata], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PodSecurityPolicyV1Beta1Metadata],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__489784eb9e052fdf0f8c07e63fdebaf42f07446cdb68b891b0ade5ba039e8045)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1Spec",
    jsii_struct_bases=[],
    name_mapping={
        "fs_group": "fsGroup",
        "run_as_user": "runAsUser",
        "supplemental_groups": "supplementalGroups",
        "allowed_capabilities": "allowedCapabilities",
        "allowed_flex_volumes": "allowedFlexVolumes",
        "allowed_host_paths": "allowedHostPaths",
        "allowed_proc_mount_types": "allowedProcMountTypes",
        "allowed_unsafe_sysctls": "allowedUnsafeSysctls",
        "allow_privilege_escalation": "allowPrivilegeEscalation",
        "default_add_capabilities": "defaultAddCapabilities",
        "default_allow_privilege_escalation": "defaultAllowPrivilegeEscalation",
        "forbidden_sysctls": "forbiddenSysctls",
        "host_ipc": "hostIpc",
        "host_network": "hostNetwork",
        "host_pid": "hostPid",
        "host_ports": "hostPorts",
        "privileged": "privileged",
        "read_only_root_filesystem": "readOnlyRootFilesystem",
        "required_drop_capabilities": "requiredDropCapabilities",
        "run_as_group": "runAsGroup",
        "se_linux": "seLinux",
        "volumes": "volumes",
    },
)
class PodSecurityPolicyV1Beta1Spec:
    def __init__(
        self,
        *,
        fs_group: typing.Union["PodSecurityPolicyV1Beta1SpecFsGroup", typing.Dict[builtins.str, typing.Any]],
        run_as_user: typing.Union["PodSecurityPolicyV1Beta1SpecRunAsUser", typing.Dict[builtins.str, typing.Any]],
        supplemental_groups: typing.Union["PodSecurityPolicyV1Beta1SpecSupplementalGroups", typing.Dict[builtins.str, typing.Any]],
        allowed_capabilities: typing.Optional[typing.Sequence[builtins.str]] = None,
        allowed_flex_volumes: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PodSecurityPolicyV1Beta1SpecAllowedFlexVolumes", typing.Dict[builtins.str, typing.Any]]]]] = None,
        allowed_host_paths: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PodSecurityPolicyV1Beta1SpecAllowedHostPaths", typing.Dict[builtins.str, typing.Any]]]]] = None,
        allowed_proc_mount_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        allowed_unsafe_sysctls: typing.Optional[typing.Sequence[builtins.str]] = None,
        allow_privilege_escalation: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        default_add_capabilities: typing.Optional[typing.Sequence[builtins.str]] = None,
        default_allow_privilege_escalation: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        forbidden_sysctls: typing.Optional[typing.Sequence[builtins.str]] = None,
        host_ipc: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        host_network: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        host_pid: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        host_ports: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PodSecurityPolicyV1Beta1SpecHostPorts", typing.Dict[builtins.str, typing.Any]]]]] = None,
        privileged: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        read_only_root_filesystem: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        required_drop_capabilities: typing.Optional[typing.Sequence[builtins.str]] = None,
        run_as_group: typing.Optional[typing.Union["PodSecurityPolicyV1Beta1SpecRunAsGroup", typing.Dict[builtins.str, typing.Any]]] = None,
        se_linux: typing.Optional[typing.Union["PodSecurityPolicyV1Beta1SpecSeLinux", typing.Dict[builtins.str, typing.Any]]] = None,
        volumes: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param fs_group: fs_group block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#fs_group PodSecurityPolicyV1Beta1#fs_group}
        :param run_as_user: run_as_user block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#run_as_user PodSecurityPolicyV1Beta1#run_as_user}
        :param supplemental_groups: supplemental_groups block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#supplemental_groups PodSecurityPolicyV1Beta1#supplemental_groups}
        :param allowed_capabilities: allowedCapabilities is a list of capabilities that can be requested to add to the container. Capabilities in this field may be added at the pod author's discretion. You must not list a capability in both allowedCapabilities and requiredDropCapabilities. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#allowed_capabilities PodSecurityPolicyV1Beta1#allowed_capabilities}
        :param allowed_flex_volumes: allowed_flex_volumes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#allowed_flex_volumes PodSecurityPolicyV1Beta1#allowed_flex_volumes}
        :param allowed_host_paths: allowed_host_paths block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#allowed_host_paths PodSecurityPolicyV1Beta1#allowed_host_paths}
        :param allowed_proc_mount_types: AllowedProcMountTypes is an allowlist of allowed ProcMountTypes. Empty or nil indicates that only the DefaultProcMountType may be used. This requires the ProcMountType feature flag to be enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#allowed_proc_mount_types PodSecurityPolicyV1Beta1#allowed_proc_mount_types}
        :param allowed_unsafe_sysctls: allowedUnsafeSysctls is a list of explicitly allowed unsafe sysctls, defaults to none. Each entry is either a plain sysctl name or ends in "*" in which case it is considered as a prefix of allowed sysctls. Single * means all unsafe sysctls are allowed. Kubelet has to allowlist all allowed unsafe sysctls explicitly to avoid rejection. Examples: e.g. "foo/*" allows "foo/bar", "foo/baz", etc. e.g. "foo.*" allows "foo.bar", "foo.baz", etc. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#allowed_unsafe_sysctls PodSecurityPolicyV1Beta1#allowed_unsafe_sysctls}
        :param allow_privilege_escalation: allowPrivilegeEscalation determines if a pod can request to allow privilege escalation. If unspecified, defaults to true. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#allow_privilege_escalation PodSecurityPolicyV1Beta1#allow_privilege_escalation}
        :param default_add_capabilities: defaultAddCapabilities is the default set of capabilities that will be added to the container unless the pod spec specifically drops the capability. You may not list a capability in both defaultAddCapabilities and requiredDropCapabilities. Capabilities added here are implicitly allowed, and need not be included in the allowedCapabilities list. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#default_add_capabilities PodSecurityPolicyV1Beta1#default_add_capabilities}
        :param default_allow_privilege_escalation: defaultAllowPrivilegeEscalation controls the default setting for whether a process can gain more privileges than its parent process. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#default_allow_privilege_escalation PodSecurityPolicyV1Beta1#default_allow_privilege_escalation}
        :param forbidden_sysctls: forbiddenSysctls is a list of explicitly forbidden sysctls, defaults to none. Each entry is either a plain sysctl name or ends in "*" in which case it is considered as a prefix of forbidden sysctls. Single * means all sysctls are forbidden. Examples: e.g. "foo/*" forbids "foo/bar", "foo/baz", etc. e.g. "foo.*" forbids "foo.bar", "foo.baz", etc. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#forbidden_sysctls PodSecurityPolicyV1Beta1#forbidden_sysctls}
        :param host_ipc: hostIPC determines if the policy allows the use of HostIPC in the pod spec. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#host_ipc PodSecurityPolicyV1Beta1#host_ipc}
        :param host_network: hostNetwork determines if the policy allows the use of HostNetwork in the pod spec. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#host_network PodSecurityPolicyV1Beta1#host_network}
        :param host_pid: hostPID determines if the policy allows the use of HostPID in the pod spec. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#host_pid PodSecurityPolicyV1Beta1#host_pid}
        :param host_ports: host_ports block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#host_ports PodSecurityPolicyV1Beta1#host_ports}
        :param privileged: privileged determines if a pod can request to be run as privileged. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#privileged PodSecurityPolicyV1Beta1#privileged}
        :param read_only_root_filesystem: readOnlyRootFilesystem when set to true will force containers to run with a read only root file system. If the container specifically requests to run with a non-read only root file system the PSP should deny the pod. If set to false the container may run with a read only root file system if it wishes but it will not be forced to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#read_only_root_filesystem PodSecurityPolicyV1Beta1#read_only_root_filesystem}
        :param required_drop_capabilities: requiredDropCapabilities are the capabilities that will be dropped from the container. These are required to be dropped and cannot be added. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#required_drop_capabilities PodSecurityPolicyV1Beta1#required_drop_capabilities}
        :param run_as_group: run_as_group block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#run_as_group PodSecurityPolicyV1Beta1#run_as_group}
        :param se_linux: se_linux block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#se_linux PodSecurityPolicyV1Beta1#se_linux}
        :param volumes: volumes is an allowlist of volume plugins. Empty indicates that no volumes may be used. To allow all volumes you may use '*'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#volumes PodSecurityPolicyV1Beta1#volumes}
        '''
        if isinstance(fs_group, dict):
            fs_group = PodSecurityPolicyV1Beta1SpecFsGroup(**fs_group)
        if isinstance(run_as_user, dict):
            run_as_user = PodSecurityPolicyV1Beta1SpecRunAsUser(**run_as_user)
        if isinstance(supplemental_groups, dict):
            supplemental_groups = PodSecurityPolicyV1Beta1SpecSupplementalGroups(**supplemental_groups)
        if isinstance(run_as_group, dict):
            run_as_group = PodSecurityPolicyV1Beta1SpecRunAsGroup(**run_as_group)
        if isinstance(se_linux, dict):
            se_linux = PodSecurityPolicyV1Beta1SpecSeLinux(**se_linux)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b61e14c7c2c8179b7a7d038205493a603f4b4986bd14a63066f6a2ca268809c1)
            check_type(argname="argument fs_group", value=fs_group, expected_type=type_hints["fs_group"])
            check_type(argname="argument run_as_user", value=run_as_user, expected_type=type_hints["run_as_user"])
            check_type(argname="argument supplemental_groups", value=supplemental_groups, expected_type=type_hints["supplemental_groups"])
            check_type(argname="argument allowed_capabilities", value=allowed_capabilities, expected_type=type_hints["allowed_capabilities"])
            check_type(argname="argument allowed_flex_volumes", value=allowed_flex_volumes, expected_type=type_hints["allowed_flex_volumes"])
            check_type(argname="argument allowed_host_paths", value=allowed_host_paths, expected_type=type_hints["allowed_host_paths"])
            check_type(argname="argument allowed_proc_mount_types", value=allowed_proc_mount_types, expected_type=type_hints["allowed_proc_mount_types"])
            check_type(argname="argument allowed_unsafe_sysctls", value=allowed_unsafe_sysctls, expected_type=type_hints["allowed_unsafe_sysctls"])
            check_type(argname="argument allow_privilege_escalation", value=allow_privilege_escalation, expected_type=type_hints["allow_privilege_escalation"])
            check_type(argname="argument default_add_capabilities", value=default_add_capabilities, expected_type=type_hints["default_add_capabilities"])
            check_type(argname="argument default_allow_privilege_escalation", value=default_allow_privilege_escalation, expected_type=type_hints["default_allow_privilege_escalation"])
            check_type(argname="argument forbidden_sysctls", value=forbidden_sysctls, expected_type=type_hints["forbidden_sysctls"])
            check_type(argname="argument host_ipc", value=host_ipc, expected_type=type_hints["host_ipc"])
            check_type(argname="argument host_network", value=host_network, expected_type=type_hints["host_network"])
            check_type(argname="argument host_pid", value=host_pid, expected_type=type_hints["host_pid"])
            check_type(argname="argument host_ports", value=host_ports, expected_type=type_hints["host_ports"])
            check_type(argname="argument privileged", value=privileged, expected_type=type_hints["privileged"])
            check_type(argname="argument read_only_root_filesystem", value=read_only_root_filesystem, expected_type=type_hints["read_only_root_filesystem"])
            check_type(argname="argument required_drop_capabilities", value=required_drop_capabilities, expected_type=type_hints["required_drop_capabilities"])
            check_type(argname="argument run_as_group", value=run_as_group, expected_type=type_hints["run_as_group"])
            check_type(argname="argument se_linux", value=se_linux, expected_type=type_hints["se_linux"])
            check_type(argname="argument volumes", value=volumes, expected_type=type_hints["volumes"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "fs_group": fs_group,
            "run_as_user": run_as_user,
            "supplemental_groups": supplemental_groups,
        }
        if allowed_capabilities is not None:
            self._values["allowed_capabilities"] = allowed_capabilities
        if allowed_flex_volumes is not None:
            self._values["allowed_flex_volumes"] = allowed_flex_volumes
        if allowed_host_paths is not None:
            self._values["allowed_host_paths"] = allowed_host_paths
        if allowed_proc_mount_types is not None:
            self._values["allowed_proc_mount_types"] = allowed_proc_mount_types
        if allowed_unsafe_sysctls is not None:
            self._values["allowed_unsafe_sysctls"] = allowed_unsafe_sysctls
        if allow_privilege_escalation is not None:
            self._values["allow_privilege_escalation"] = allow_privilege_escalation
        if default_add_capabilities is not None:
            self._values["default_add_capabilities"] = default_add_capabilities
        if default_allow_privilege_escalation is not None:
            self._values["default_allow_privilege_escalation"] = default_allow_privilege_escalation
        if forbidden_sysctls is not None:
            self._values["forbidden_sysctls"] = forbidden_sysctls
        if host_ipc is not None:
            self._values["host_ipc"] = host_ipc
        if host_network is not None:
            self._values["host_network"] = host_network
        if host_pid is not None:
            self._values["host_pid"] = host_pid
        if host_ports is not None:
            self._values["host_ports"] = host_ports
        if privileged is not None:
            self._values["privileged"] = privileged
        if read_only_root_filesystem is not None:
            self._values["read_only_root_filesystem"] = read_only_root_filesystem
        if required_drop_capabilities is not None:
            self._values["required_drop_capabilities"] = required_drop_capabilities
        if run_as_group is not None:
            self._values["run_as_group"] = run_as_group
        if se_linux is not None:
            self._values["se_linux"] = se_linux
        if volumes is not None:
            self._values["volumes"] = volumes

    @builtins.property
    def fs_group(self) -> "PodSecurityPolicyV1Beta1SpecFsGroup":
        '''fs_group block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#fs_group PodSecurityPolicyV1Beta1#fs_group}
        '''
        result = self._values.get("fs_group")
        assert result is not None, "Required property 'fs_group' is missing"
        return typing.cast("PodSecurityPolicyV1Beta1SpecFsGroup", result)

    @builtins.property
    def run_as_user(self) -> "PodSecurityPolicyV1Beta1SpecRunAsUser":
        '''run_as_user block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#run_as_user PodSecurityPolicyV1Beta1#run_as_user}
        '''
        result = self._values.get("run_as_user")
        assert result is not None, "Required property 'run_as_user' is missing"
        return typing.cast("PodSecurityPolicyV1Beta1SpecRunAsUser", result)

    @builtins.property
    def supplemental_groups(self) -> "PodSecurityPolicyV1Beta1SpecSupplementalGroups":
        '''supplemental_groups block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#supplemental_groups PodSecurityPolicyV1Beta1#supplemental_groups}
        '''
        result = self._values.get("supplemental_groups")
        assert result is not None, "Required property 'supplemental_groups' is missing"
        return typing.cast("PodSecurityPolicyV1Beta1SpecSupplementalGroups", result)

    @builtins.property
    def allowed_capabilities(self) -> typing.Optional[typing.List[builtins.str]]:
        '''allowedCapabilities is a list of capabilities that can be requested to add to the container.

        Capabilities in this field may be added at the pod author's discretion. You must not list a capability in both allowedCapabilities and requiredDropCapabilities.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#allowed_capabilities PodSecurityPolicyV1Beta1#allowed_capabilities}
        '''
        result = self._values.get("allowed_capabilities")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def allowed_flex_volumes(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PodSecurityPolicyV1Beta1SpecAllowedFlexVolumes"]]]:
        '''allowed_flex_volumes block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#allowed_flex_volumes PodSecurityPolicyV1Beta1#allowed_flex_volumes}
        '''
        result = self._values.get("allowed_flex_volumes")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PodSecurityPolicyV1Beta1SpecAllowedFlexVolumes"]]], result)

    @builtins.property
    def allowed_host_paths(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PodSecurityPolicyV1Beta1SpecAllowedHostPaths"]]]:
        '''allowed_host_paths block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#allowed_host_paths PodSecurityPolicyV1Beta1#allowed_host_paths}
        '''
        result = self._values.get("allowed_host_paths")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PodSecurityPolicyV1Beta1SpecAllowedHostPaths"]]], result)

    @builtins.property
    def allowed_proc_mount_types(self) -> typing.Optional[typing.List[builtins.str]]:
        '''AllowedProcMountTypes is an allowlist of allowed ProcMountTypes.

        Empty or nil indicates that only the DefaultProcMountType may be used. This requires the ProcMountType feature flag to be enabled.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#allowed_proc_mount_types PodSecurityPolicyV1Beta1#allowed_proc_mount_types}
        '''
        result = self._values.get("allowed_proc_mount_types")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def allowed_unsafe_sysctls(self) -> typing.Optional[typing.List[builtins.str]]:
        '''allowedUnsafeSysctls is a list of explicitly allowed unsafe sysctls, defaults to none.

        Each entry is either a plain sysctl name or ends in "*" in which case it is considered as a prefix of allowed sysctls. Single * means all unsafe sysctls are allowed. Kubelet has to allowlist all allowed unsafe sysctls explicitly to avoid rejection.

        Examples: e.g. "foo/*" allows "foo/bar", "foo/baz", etc. e.g. "foo.*" allows "foo.bar", "foo.baz", etc.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#allowed_unsafe_sysctls PodSecurityPolicyV1Beta1#allowed_unsafe_sysctls}
        '''
        result = self._values.get("allowed_unsafe_sysctls")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def allow_privilege_escalation(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''allowPrivilegeEscalation determines if a pod can request to allow privilege escalation. If unspecified, defaults to true.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#allow_privilege_escalation PodSecurityPolicyV1Beta1#allow_privilege_escalation}
        '''
        result = self._values.get("allow_privilege_escalation")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def default_add_capabilities(self) -> typing.Optional[typing.List[builtins.str]]:
        '''defaultAddCapabilities is the default set of capabilities that will be added to the container unless the pod spec specifically drops the capability.

        You may not list a capability in both defaultAddCapabilities and requiredDropCapabilities. Capabilities added here are implicitly allowed, and need not be included in the allowedCapabilities list.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#default_add_capabilities PodSecurityPolicyV1Beta1#default_add_capabilities}
        '''
        result = self._values.get("default_add_capabilities")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def default_allow_privilege_escalation(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''defaultAllowPrivilegeEscalation controls the default setting for whether a process can gain more privileges than its parent process.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#default_allow_privilege_escalation PodSecurityPolicyV1Beta1#default_allow_privilege_escalation}
        '''
        result = self._values.get("default_allow_privilege_escalation")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def forbidden_sysctls(self) -> typing.Optional[typing.List[builtins.str]]:
        '''forbiddenSysctls is a list of explicitly forbidden sysctls, defaults to none.

        Each entry is either a plain sysctl name or ends in "*" in which case it is considered as a prefix of forbidden sysctls. Single * means all sysctls are forbidden.

        Examples: e.g. "foo/*" forbids "foo/bar", "foo/baz", etc. e.g. "foo.*" forbids "foo.bar", "foo.baz", etc.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#forbidden_sysctls PodSecurityPolicyV1Beta1#forbidden_sysctls}
        '''
        result = self._values.get("forbidden_sysctls")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def host_ipc(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''hostIPC determines if the policy allows the use of HostIPC in the pod spec.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#host_ipc PodSecurityPolicyV1Beta1#host_ipc}
        '''
        result = self._values.get("host_ipc")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def host_network(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''hostNetwork determines if the policy allows the use of HostNetwork in the pod spec.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#host_network PodSecurityPolicyV1Beta1#host_network}
        '''
        result = self._values.get("host_network")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def host_pid(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''hostPID determines if the policy allows the use of HostPID in the pod spec.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#host_pid PodSecurityPolicyV1Beta1#host_pid}
        '''
        result = self._values.get("host_pid")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def host_ports(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PodSecurityPolicyV1Beta1SpecHostPorts"]]]:
        '''host_ports block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#host_ports PodSecurityPolicyV1Beta1#host_ports}
        '''
        result = self._values.get("host_ports")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PodSecurityPolicyV1Beta1SpecHostPorts"]]], result)

    @builtins.property
    def privileged(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''privileged determines if a pod can request to be run as privileged.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#privileged PodSecurityPolicyV1Beta1#privileged}
        '''
        result = self._values.get("privileged")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def read_only_root_filesystem(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''readOnlyRootFilesystem when set to true will force containers to run with a read only root file system.

        If the container specifically requests to run with a non-read only root file system the PSP should deny the pod. If set to false the container may run with a read only root file system if it wishes but it will not be forced to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#read_only_root_filesystem PodSecurityPolicyV1Beta1#read_only_root_filesystem}
        '''
        result = self._values.get("read_only_root_filesystem")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def required_drop_capabilities(self) -> typing.Optional[typing.List[builtins.str]]:
        '''requiredDropCapabilities are the capabilities that will be dropped from the container.

        These are required to be dropped and cannot be added.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#required_drop_capabilities PodSecurityPolicyV1Beta1#required_drop_capabilities}
        '''
        result = self._values.get("required_drop_capabilities")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def run_as_group(self) -> typing.Optional["PodSecurityPolicyV1Beta1SpecRunAsGroup"]:
        '''run_as_group block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#run_as_group PodSecurityPolicyV1Beta1#run_as_group}
        '''
        result = self._values.get("run_as_group")
        return typing.cast(typing.Optional["PodSecurityPolicyV1Beta1SpecRunAsGroup"], result)

    @builtins.property
    def se_linux(self) -> typing.Optional["PodSecurityPolicyV1Beta1SpecSeLinux"]:
        '''se_linux block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#se_linux PodSecurityPolicyV1Beta1#se_linux}
        '''
        result = self._values.get("se_linux")
        return typing.cast(typing.Optional["PodSecurityPolicyV1Beta1SpecSeLinux"], result)

    @builtins.property
    def volumes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''volumes is an allowlist of volume plugins.

        Empty indicates that no volumes may be used. To allow all volumes you may use '*'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#volumes PodSecurityPolicyV1Beta1#volumes}
        '''
        result = self._values.get("volumes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PodSecurityPolicyV1Beta1Spec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecAllowedFlexVolumes",
    jsii_struct_bases=[],
    name_mapping={"driver": "driver"},
)
class PodSecurityPolicyV1Beta1SpecAllowedFlexVolumes:
    def __init__(self, *, driver: builtins.str) -> None:
        '''
        :param driver: driver is the name of the Flexvolume driver. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#driver PodSecurityPolicyV1Beta1#driver}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e758f6185a95ddaa55061e0e12dd5822af1084fe7d22b85230823d6edbbdfa7c)
            check_type(argname="argument driver", value=driver, expected_type=type_hints["driver"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "driver": driver,
        }

    @builtins.property
    def driver(self) -> builtins.str:
        '''driver is the name of the Flexvolume driver.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#driver PodSecurityPolicyV1Beta1#driver}
        '''
        result = self._values.get("driver")
        assert result is not None, "Required property 'driver' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PodSecurityPolicyV1Beta1SpecAllowedFlexVolumes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PodSecurityPolicyV1Beta1SpecAllowedFlexVolumesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecAllowedFlexVolumesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__13138564d0498df938411b766f6ccf653d8215fa6501c110d282124ecfcf0064)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "PodSecurityPolicyV1Beta1SpecAllowedFlexVolumesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed59c846ed70f5853448249c83fb43e1b86f5b066fa5dd89de07f59dcf1a48fd)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PodSecurityPolicyV1Beta1SpecAllowedFlexVolumesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62cd89d46c23349e10655727a851377e030c91cbc6430bb6d56de527f4f3142b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4edb7fa83e56c96c33ce9097a493bb5695cb965cbf8d6c88dd060dc9fa3b60b0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__adbda02882194591551946248324cc10e53ec8210066b44757f1d5c2ac77c09b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecAllowedFlexVolumes]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecAllowedFlexVolumes]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecAllowedFlexVolumes]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__317e62346b94868856f765ea61092e908fc067c5558d548a58d478c95b55849b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PodSecurityPolicyV1Beta1SpecAllowedFlexVolumesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecAllowedFlexVolumesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__14d0cbb75a8fddd8f1c25d0ccfe4348a476b488fcd4c0f50d9e04322f3c813cc)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="driverInput")
    def driver_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "driverInput"))

    @builtins.property
    @jsii.member(jsii_name="driver")
    def driver(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "driver"))

    @driver.setter
    def driver(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e26ec60608a776050a80cfe9f3bedaa666386eab0493976c5b39d6005566bb7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "driver", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecAllowedFlexVolumes, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecAllowedFlexVolumes, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecAllowedFlexVolumes, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f769d50494d9df9ed1dbe3e51e225ebcc81016c5953b1ad2b7538b10064aca8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecAllowedHostPaths",
    jsii_struct_bases=[],
    name_mapping={"path_prefix": "pathPrefix", "read_only": "readOnly"},
)
class PodSecurityPolicyV1Beta1SpecAllowedHostPaths:
    def __init__(
        self,
        *,
        path_prefix: builtins.str,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param path_prefix: pathPrefix is the path prefix that the host volume must match. It does not support ``*``. Trailing slashes are trimmed when validating the path prefix with a host path. Examples: ``/foo`` would allow ``/foo``, ``/foo/`` and ``/foo/bar`` ``/foo`` would not allow ``/food`` or ``/etc/foo`` Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#path_prefix PodSecurityPolicyV1Beta1#path_prefix}
        :param read_only: when set to true, will allow host volumes matching the pathPrefix only if all volume mounts are readOnly. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#read_only PodSecurityPolicyV1Beta1#read_only}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb594c584b0396fbf2a8c74de72ae632981d051f530d2070e70e48f693b9a209)
            check_type(argname="argument path_prefix", value=path_prefix, expected_type=type_hints["path_prefix"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "path_prefix": path_prefix,
        }
        if read_only is not None:
            self._values["read_only"] = read_only

    @builtins.property
    def path_prefix(self) -> builtins.str:
        '''pathPrefix is the path prefix that the host volume must match.

        It does not support ``*``. Trailing slashes are trimmed when validating the path prefix with a host path.

        Examples: ``/foo`` would allow ``/foo``, ``/foo/`` and ``/foo/bar`` ``/foo`` would not allow ``/food`` or ``/etc/foo``

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#path_prefix PodSecurityPolicyV1Beta1#path_prefix}
        '''
        result = self._values.get("path_prefix")
        assert result is not None, "Required property 'path_prefix' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def read_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''when set to true, will allow host volumes matching the pathPrefix only if all volume mounts are readOnly.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#read_only PodSecurityPolicyV1Beta1#read_only}
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PodSecurityPolicyV1Beta1SpecAllowedHostPaths(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PodSecurityPolicyV1Beta1SpecAllowedHostPathsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecAllowedHostPathsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8f2e8c77fb12313aeca9682dd09713749ec009490d794d56319df624453db38e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "PodSecurityPolicyV1Beta1SpecAllowedHostPathsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0b4644f082260ce66eb67a9c31a4bf2165c508a0e8d9d1a1f255ca0c9c17642)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PodSecurityPolicyV1Beta1SpecAllowedHostPathsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c1c09ce3c8f70e286e72cffbc07c27d47d388324dd4fab03ada3013645a0b05)
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
            type_hints = typing.get_type_hints(_typecheckingstub__310bc7034cb4c1c2ae77780d2cf7e0cb26c3f23163af8cde3c6dffc1853b9c72)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3e1b8f9f9f340663a038f7ebc0199efa2327b728d90c7116fd9423dfcd4a90a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecAllowedHostPaths]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecAllowedHostPaths]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecAllowedHostPaths]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43aeb9f61099d8218201893ef50d53c4a0798cf102fcdc900e58674334001ed2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PodSecurityPolicyV1Beta1SpecAllowedHostPathsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecAllowedHostPathsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__05b63e181cd8be5b450e1d03779187755dcd3aed30fd137ca52937e4b358a5d0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetReadOnly")
    def reset_read_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadOnly", []))

    @builtins.property
    @jsii.member(jsii_name="pathPrefixInput")
    def path_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="readOnlyInput")
    def read_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "readOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="pathPrefix")
    def path_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pathPrefix"))

    @path_prefix.setter
    def path_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61b258ca7fed612ae34c0a9e7c3dc62c61fef6d4cdd0468a4b72d0390cb6341e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pathPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="readOnly")
    def read_only(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "readOnly"))

    @read_only.setter
    def read_only(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d9867db59cc84adca816b3095598041ddb55fe1f7b44d20777d5eb21e324966)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readOnly", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecAllowedHostPaths, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecAllowedHostPaths, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecAllowedHostPaths, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ccc6b48756de47d4b7d2415bd1c3677f74696591a4182cbed2d355c1c436d0bb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecFsGroup",
    jsii_struct_bases=[],
    name_mapping={"rule": "rule", "range": "range"},
)
class PodSecurityPolicyV1Beta1SpecFsGroup:
    def __init__(
        self,
        *,
        rule: builtins.str,
        range: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PodSecurityPolicyV1Beta1SpecFsGroupRange", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param rule: rule is the strategy that will dictate what FSGroup is used in the SecurityContext. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#rule PodSecurityPolicyV1Beta1#rule}
        :param range: range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#range PodSecurityPolicyV1Beta1#range}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab23dc0bbcd53640ea3de5acc31f185bc76bb8892d151026a6139d008f37b537)
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
            check_type(argname="argument range", value=range, expected_type=type_hints["range"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "rule": rule,
        }
        if range is not None:
            self._values["range"] = range

    @builtins.property
    def rule(self) -> builtins.str:
        '''rule is the strategy that will dictate what FSGroup is used in the SecurityContext.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#rule PodSecurityPolicyV1Beta1#rule}
        '''
        result = self._values.get("rule")
        assert result is not None, "Required property 'rule' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def range(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PodSecurityPolicyV1Beta1SpecFsGroupRange"]]]:
        '''range block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#range PodSecurityPolicyV1Beta1#range}
        '''
        result = self._values.get("range")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PodSecurityPolicyV1Beta1SpecFsGroupRange"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PodSecurityPolicyV1Beta1SpecFsGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PodSecurityPolicyV1Beta1SpecFsGroupOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecFsGroupOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__98a386e51a7f60a7b4092b72dd131d2b42ba4854bab5c8d175ca8bd9dd6f6aa0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putRange")
    def put_range(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PodSecurityPolicyV1Beta1SpecFsGroupRange", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a1e5252fc88b78c419563859486b2bd4fd0e92ec1998e730df6fa19d9b64c1a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRange", [value]))

    @jsii.member(jsii_name="resetRange")
    def reset_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRange", []))

    @builtins.property
    @jsii.member(jsii_name="range")
    def range(self) -> "PodSecurityPolicyV1Beta1SpecFsGroupRangeList":
        return typing.cast("PodSecurityPolicyV1Beta1SpecFsGroupRangeList", jsii.get(self, "range"))

    @builtins.property
    @jsii.member(jsii_name="rangeInput")
    def range_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PodSecurityPolicyV1Beta1SpecFsGroupRange"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PodSecurityPolicyV1Beta1SpecFsGroupRange"]]], jsii.get(self, "rangeInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleInput")
    def rule_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ruleInput"))

    @builtins.property
    @jsii.member(jsii_name="rule")
    def rule(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rule"))

    @rule.setter
    def rule(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b1c91d2368c41055883e9608678a1813cb5d0c2d645fdfcb518f4edba5417d5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rule", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[PodSecurityPolicyV1Beta1SpecFsGroup]:
        return typing.cast(typing.Optional[PodSecurityPolicyV1Beta1SpecFsGroup], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PodSecurityPolicyV1Beta1SpecFsGroup],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f585e0e82e8e55046a54d2b0bc0dbd178327776464245ac040d7b4364ef0e71)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecFsGroupRange",
    jsii_struct_bases=[],
    name_mapping={"max": "max", "min": "min"},
)
class PodSecurityPolicyV1Beta1SpecFsGroupRange:
    def __init__(self, *, max: jsii.Number, min: jsii.Number) -> None:
        '''
        :param max: max is the end of the range, inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#max PodSecurityPolicyV1Beta1#max}
        :param min: min is the start of the range, inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#min PodSecurityPolicyV1Beta1#min}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__035f665808a3de7623c9fd738cdb0780028efbe105a20eede15e68519495a9d3)
            check_type(argname="argument max", value=max, expected_type=type_hints["max"])
            check_type(argname="argument min", value=min, expected_type=type_hints["min"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "max": max,
            "min": min,
        }

    @builtins.property
    def max(self) -> jsii.Number:
        '''max is the end of the range, inclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#max PodSecurityPolicyV1Beta1#max}
        '''
        result = self._values.get("max")
        assert result is not None, "Required property 'max' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def min(self) -> jsii.Number:
        '''min is the start of the range, inclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#min PodSecurityPolicyV1Beta1#min}
        '''
        result = self._values.get("min")
        assert result is not None, "Required property 'min' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PodSecurityPolicyV1Beta1SpecFsGroupRange(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PodSecurityPolicyV1Beta1SpecFsGroupRangeList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecFsGroupRangeList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e3ab584b174d4b5530a8fc9cd6e2b57f7e2222406388607c4fc348b1e1eeb66f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "PodSecurityPolicyV1Beta1SpecFsGroupRangeOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0293fffe7fea6d32759603f5cbd1197b26ec250cf07725850eb1bbe23a1dd5c)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PodSecurityPolicyV1Beta1SpecFsGroupRangeOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ae18bcd54fcb1b441b39e6f3371836db6145b8bd2242d2453c067718b4c1490)
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
            type_hints = typing.get_type_hints(_typecheckingstub__82cdb739948e45b0065d4c251274599ebc0e76eb17096270c9b6f8353133002c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c84c7b45a93976ee754e4d6a5f16a0285bb3b9fe902daebe63b5f3d4e395f878)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecFsGroupRange]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecFsGroupRange]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecFsGroupRange]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c78c62a22d7b7e2952ae88eeb07e5e953c763ddfb037d38dee715164886ddb0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PodSecurityPolicyV1Beta1SpecFsGroupRangeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecFsGroupRangeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__edb28452c44da514143c66a9e9e86d259eac639f6ac4f29064b40f9d1df18fdf)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

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
            type_hints = typing.get_type_hints(_typecheckingstub__4ffe5fa1b52a7ed828aaf193681a07c2f39cb5bcabf5a8d46602d1705d56dfc5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "max", value)

    @builtins.property
    @jsii.member(jsii_name="min")
    def min(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "min"))

    @min.setter
    def min(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c65ce87c53751c839c19ce42709baa3a8ab44e9a398e9e35b80f18529d88b25d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "min", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecFsGroupRange, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecFsGroupRange, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecFsGroupRange, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de4b1a90341682c469a97c919d29add13a5e99eee1ebb114ec2e6fcf7b0181b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecHostPorts",
    jsii_struct_bases=[],
    name_mapping={"max": "max", "min": "min"},
)
class PodSecurityPolicyV1Beta1SpecHostPorts:
    def __init__(self, *, max: jsii.Number, min: jsii.Number) -> None:
        '''
        :param max: max is the end of the range, inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#max PodSecurityPolicyV1Beta1#max}
        :param min: min is the start of the range, inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#min PodSecurityPolicyV1Beta1#min}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e673e42b07be435acc8800820468a07e95d7d8b1dc332dcf7b0d4d289d880714)
            check_type(argname="argument max", value=max, expected_type=type_hints["max"])
            check_type(argname="argument min", value=min, expected_type=type_hints["min"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "max": max,
            "min": min,
        }

    @builtins.property
    def max(self) -> jsii.Number:
        '''max is the end of the range, inclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#max PodSecurityPolicyV1Beta1#max}
        '''
        result = self._values.get("max")
        assert result is not None, "Required property 'max' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def min(self) -> jsii.Number:
        '''min is the start of the range, inclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#min PodSecurityPolicyV1Beta1#min}
        '''
        result = self._values.get("min")
        assert result is not None, "Required property 'min' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PodSecurityPolicyV1Beta1SpecHostPorts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PodSecurityPolicyV1Beta1SpecHostPortsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecHostPortsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e8a1b8241ec20d1eeeabdbf235b5d5d13818d8ac13c48eb69bf32cae325594dc)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "PodSecurityPolicyV1Beta1SpecHostPortsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__964f173a0406ca5acf54f9c109f169143b38dc5c85961143440a41e461bf75f8)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PodSecurityPolicyV1Beta1SpecHostPortsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b206df2cc58937abe2c1ac07b9679c777821bc56eb08d6f8dc45ce6a7705d82)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ef9a88ebe40693479d7b1925b9a09da873bfc4e4dcc4bbbe32717759a7b14fb8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ff0bfbfb03ab331942963faef3b85937f8eb3eef2947bc05b51bbe18e41449b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecHostPorts]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecHostPorts]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecHostPorts]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7ce68d19a0e94c0bcc279a7175c4146fa5658648d30fd0917af967d991831ba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PodSecurityPolicyV1Beta1SpecHostPortsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecHostPortsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__207668b0d32cd36bba4041e22286c7e79bc726f40525deaf5ff6cdd142ab1c39)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

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
            type_hints = typing.get_type_hints(_typecheckingstub__1c5294a3f2fac9cade1c7bff7b55443d3d294b686aead53c0b8a1e1a72f416cc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "max", value)

    @builtins.property
    @jsii.member(jsii_name="min")
    def min(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "min"))

    @min.setter
    def min(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b1c35ce6a7e661546fb6d77729099f03c0442dfc1c9add032310a1e6d09475a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "min", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecHostPorts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecHostPorts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecHostPorts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b91e19404e74980d151599c68fb7ee00e51623f9176f860667397e25ceffb013)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PodSecurityPolicyV1Beta1SpecOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4c0645436f469c6bc03bb01321199773c6713ae4e66b44bc209e4d65235ab2a5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAllowedFlexVolumes")
    def put_allowed_flex_volumes(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PodSecurityPolicyV1Beta1SpecAllowedFlexVolumes, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e61f2b67036eff3aac28cda43e86475a6ad7473491a9f84d7a208563317fde4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAllowedFlexVolumes", [value]))

    @jsii.member(jsii_name="putAllowedHostPaths")
    def put_allowed_host_paths(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PodSecurityPolicyV1Beta1SpecAllowedHostPaths, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cda26d0aeaa98464401d498a4efd4d2269d6e504b3c07704088d4fe2cf5b0fda)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAllowedHostPaths", [value]))

    @jsii.member(jsii_name="putFsGroup")
    def put_fs_group(
        self,
        *,
        rule: builtins.str,
        range: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PodSecurityPolicyV1Beta1SpecFsGroupRange, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param rule: rule is the strategy that will dictate what FSGroup is used in the SecurityContext. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#rule PodSecurityPolicyV1Beta1#rule}
        :param range: range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#range PodSecurityPolicyV1Beta1#range}
        '''
        value = PodSecurityPolicyV1Beta1SpecFsGroup(rule=rule, range=range)

        return typing.cast(None, jsii.invoke(self, "putFsGroup", [value]))

    @jsii.member(jsii_name="putHostPorts")
    def put_host_ports(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PodSecurityPolicyV1Beta1SpecHostPorts, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2de3745f0f6784c55399e630e5a25580d2b8de6278573eb2c7693acde52059dd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putHostPorts", [value]))

    @jsii.member(jsii_name="putRunAsGroup")
    def put_run_as_group(
        self,
        *,
        rule: builtins.str,
        range: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PodSecurityPolicyV1Beta1SpecRunAsGroupRange", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param rule: rule is the strategy that will dictate the allowable RunAsGroup values that may be set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#rule PodSecurityPolicyV1Beta1#rule}
        :param range: range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#range PodSecurityPolicyV1Beta1#range}
        '''
        value = PodSecurityPolicyV1Beta1SpecRunAsGroup(rule=rule, range=range)

        return typing.cast(None, jsii.invoke(self, "putRunAsGroup", [value]))

    @jsii.member(jsii_name="putRunAsUser")
    def put_run_as_user(
        self,
        *,
        rule: builtins.str,
        range: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PodSecurityPolicyV1Beta1SpecRunAsUserRange", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param rule: rule is the strategy that will dictate the allowable RunAsUser values that may be set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#rule PodSecurityPolicyV1Beta1#rule}
        :param range: range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#range PodSecurityPolicyV1Beta1#range}
        '''
        value = PodSecurityPolicyV1Beta1SpecRunAsUser(rule=rule, range=range)

        return typing.cast(None, jsii.invoke(self, "putRunAsUser", [value]))

    @jsii.member(jsii_name="putSeLinux")
    def put_se_linux(
        self,
        *,
        rule: builtins.str,
        se_linux_options: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptions", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param rule: rule is the strategy that will dictate the allowable labels that may be set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#rule PodSecurityPolicyV1Beta1#rule}
        :param se_linux_options: se_linux_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#se_linux_options PodSecurityPolicyV1Beta1#se_linux_options}
        '''
        value = PodSecurityPolicyV1Beta1SpecSeLinux(
            rule=rule, se_linux_options=se_linux_options
        )

        return typing.cast(None, jsii.invoke(self, "putSeLinux", [value]))

    @jsii.member(jsii_name="putSupplementalGroups")
    def put_supplemental_groups(
        self,
        *,
        rule: builtins.str,
        range: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PodSecurityPolicyV1Beta1SpecSupplementalGroupsRange", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param rule: rule is the strategy that will dictate what supplemental groups is used in the SecurityContext. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#rule PodSecurityPolicyV1Beta1#rule}
        :param range: range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#range PodSecurityPolicyV1Beta1#range}
        '''
        value = PodSecurityPolicyV1Beta1SpecSupplementalGroups(rule=rule, range=range)

        return typing.cast(None, jsii.invoke(self, "putSupplementalGroups", [value]))

    @jsii.member(jsii_name="resetAllowedCapabilities")
    def reset_allowed_capabilities(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedCapabilities", []))

    @jsii.member(jsii_name="resetAllowedFlexVolumes")
    def reset_allowed_flex_volumes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedFlexVolumes", []))

    @jsii.member(jsii_name="resetAllowedHostPaths")
    def reset_allowed_host_paths(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedHostPaths", []))

    @jsii.member(jsii_name="resetAllowedProcMountTypes")
    def reset_allowed_proc_mount_types(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedProcMountTypes", []))

    @jsii.member(jsii_name="resetAllowedUnsafeSysctls")
    def reset_allowed_unsafe_sysctls(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedUnsafeSysctls", []))

    @jsii.member(jsii_name="resetAllowPrivilegeEscalation")
    def reset_allow_privilege_escalation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowPrivilegeEscalation", []))

    @jsii.member(jsii_name="resetDefaultAddCapabilities")
    def reset_default_add_capabilities(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultAddCapabilities", []))

    @jsii.member(jsii_name="resetDefaultAllowPrivilegeEscalation")
    def reset_default_allow_privilege_escalation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultAllowPrivilegeEscalation", []))

    @jsii.member(jsii_name="resetForbiddenSysctls")
    def reset_forbidden_sysctls(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForbiddenSysctls", []))

    @jsii.member(jsii_name="resetHostIpc")
    def reset_host_ipc(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostIpc", []))

    @jsii.member(jsii_name="resetHostNetwork")
    def reset_host_network(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostNetwork", []))

    @jsii.member(jsii_name="resetHostPid")
    def reset_host_pid(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostPid", []))

    @jsii.member(jsii_name="resetHostPorts")
    def reset_host_ports(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostPorts", []))

    @jsii.member(jsii_name="resetPrivileged")
    def reset_privileged(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivileged", []))

    @jsii.member(jsii_name="resetReadOnlyRootFilesystem")
    def reset_read_only_root_filesystem(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadOnlyRootFilesystem", []))

    @jsii.member(jsii_name="resetRequiredDropCapabilities")
    def reset_required_drop_capabilities(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequiredDropCapabilities", []))

    @jsii.member(jsii_name="resetRunAsGroup")
    def reset_run_as_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRunAsGroup", []))

    @jsii.member(jsii_name="resetSeLinux")
    def reset_se_linux(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSeLinux", []))

    @jsii.member(jsii_name="resetVolumes")
    def reset_volumes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVolumes", []))

    @builtins.property
    @jsii.member(jsii_name="allowedFlexVolumes")
    def allowed_flex_volumes(
        self,
    ) -> PodSecurityPolicyV1Beta1SpecAllowedFlexVolumesList:
        return typing.cast(PodSecurityPolicyV1Beta1SpecAllowedFlexVolumesList, jsii.get(self, "allowedFlexVolumes"))

    @builtins.property
    @jsii.member(jsii_name="allowedHostPaths")
    def allowed_host_paths(self) -> PodSecurityPolicyV1Beta1SpecAllowedHostPathsList:
        return typing.cast(PodSecurityPolicyV1Beta1SpecAllowedHostPathsList, jsii.get(self, "allowedHostPaths"))

    @builtins.property
    @jsii.member(jsii_name="fsGroup")
    def fs_group(self) -> PodSecurityPolicyV1Beta1SpecFsGroupOutputReference:
        return typing.cast(PodSecurityPolicyV1Beta1SpecFsGroupOutputReference, jsii.get(self, "fsGroup"))

    @builtins.property
    @jsii.member(jsii_name="hostPorts")
    def host_ports(self) -> PodSecurityPolicyV1Beta1SpecHostPortsList:
        return typing.cast(PodSecurityPolicyV1Beta1SpecHostPortsList, jsii.get(self, "hostPorts"))

    @builtins.property
    @jsii.member(jsii_name="runAsGroup")
    def run_as_group(self) -> "PodSecurityPolicyV1Beta1SpecRunAsGroupOutputReference":
        return typing.cast("PodSecurityPolicyV1Beta1SpecRunAsGroupOutputReference", jsii.get(self, "runAsGroup"))

    @builtins.property
    @jsii.member(jsii_name="runAsUser")
    def run_as_user(self) -> "PodSecurityPolicyV1Beta1SpecRunAsUserOutputReference":
        return typing.cast("PodSecurityPolicyV1Beta1SpecRunAsUserOutputReference", jsii.get(self, "runAsUser"))

    @builtins.property
    @jsii.member(jsii_name="seLinux")
    def se_linux(self) -> "PodSecurityPolicyV1Beta1SpecSeLinuxOutputReference":
        return typing.cast("PodSecurityPolicyV1Beta1SpecSeLinuxOutputReference", jsii.get(self, "seLinux"))

    @builtins.property
    @jsii.member(jsii_name="supplementalGroups")
    def supplemental_groups(
        self,
    ) -> "PodSecurityPolicyV1Beta1SpecSupplementalGroupsOutputReference":
        return typing.cast("PodSecurityPolicyV1Beta1SpecSupplementalGroupsOutputReference", jsii.get(self, "supplementalGroups"))

    @builtins.property
    @jsii.member(jsii_name="allowedCapabilitiesInput")
    def allowed_capabilities_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedCapabilitiesInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedFlexVolumesInput")
    def allowed_flex_volumes_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecAllowedFlexVolumes]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecAllowedFlexVolumes]]], jsii.get(self, "allowedFlexVolumesInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedHostPathsInput")
    def allowed_host_paths_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecAllowedHostPaths]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecAllowedHostPaths]]], jsii.get(self, "allowedHostPathsInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedProcMountTypesInput")
    def allowed_proc_mount_types_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedProcMountTypesInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedUnsafeSysctlsInput")
    def allowed_unsafe_sysctls_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedUnsafeSysctlsInput"))

    @builtins.property
    @jsii.member(jsii_name="allowPrivilegeEscalationInput")
    def allow_privilege_escalation_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "allowPrivilegeEscalationInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultAddCapabilitiesInput")
    def default_add_capabilities_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "defaultAddCapabilitiesInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultAllowPrivilegeEscalationInput")
    def default_allow_privilege_escalation_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "defaultAllowPrivilegeEscalationInput"))

    @builtins.property
    @jsii.member(jsii_name="forbiddenSysctlsInput")
    def forbidden_sysctls_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "forbiddenSysctlsInput"))

    @builtins.property
    @jsii.member(jsii_name="fsGroupInput")
    def fs_group_input(self) -> typing.Optional[PodSecurityPolicyV1Beta1SpecFsGroup]:
        return typing.cast(typing.Optional[PodSecurityPolicyV1Beta1SpecFsGroup], jsii.get(self, "fsGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="hostIpcInput")
    def host_ipc_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "hostIpcInput"))

    @builtins.property
    @jsii.member(jsii_name="hostNetworkInput")
    def host_network_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "hostNetworkInput"))

    @builtins.property
    @jsii.member(jsii_name="hostPidInput")
    def host_pid_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "hostPidInput"))

    @builtins.property
    @jsii.member(jsii_name="hostPortsInput")
    def host_ports_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecHostPorts]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecHostPorts]]], jsii.get(self, "hostPortsInput"))

    @builtins.property
    @jsii.member(jsii_name="privilegedInput")
    def privileged_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "privilegedInput"))

    @builtins.property
    @jsii.member(jsii_name="readOnlyRootFilesystemInput")
    def read_only_root_filesystem_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "readOnlyRootFilesystemInput"))

    @builtins.property
    @jsii.member(jsii_name="requiredDropCapabilitiesInput")
    def required_drop_capabilities_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "requiredDropCapabilitiesInput"))

    @builtins.property
    @jsii.member(jsii_name="runAsGroupInput")
    def run_as_group_input(
        self,
    ) -> typing.Optional["PodSecurityPolicyV1Beta1SpecRunAsGroup"]:
        return typing.cast(typing.Optional["PodSecurityPolicyV1Beta1SpecRunAsGroup"], jsii.get(self, "runAsGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="runAsUserInput")
    def run_as_user_input(
        self,
    ) -> typing.Optional["PodSecurityPolicyV1Beta1SpecRunAsUser"]:
        return typing.cast(typing.Optional["PodSecurityPolicyV1Beta1SpecRunAsUser"], jsii.get(self, "runAsUserInput"))

    @builtins.property
    @jsii.member(jsii_name="seLinuxInput")
    def se_linux_input(self) -> typing.Optional["PodSecurityPolicyV1Beta1SpecSeLinux"]:
        return typing.cast(typing.Optional["PodSecurityPolicyV1Beta1SpecSeLinux"], jsii.get(self, "seLinuxInput"))

    @builtins.property
    @jsii.member(jsii_name="supplementalGroupsInput")
    def supplemental_groups_input(
        self,
    ) -> typing.Optional["PodSecurityPolicyV1Beta1SpecSupplementalGroups"]:
        return typing.cast(typing.Optional["PodSecurityPolicyV1Beta1SpecSupplementalGroups"], jsii.get(self, "supplementalGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="volumesInput")
    def volumes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "volumesInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedCapabilities")
    def allowed_capabilities(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedCapabilities"))

    @allowed_capabilities.setter
    def allowed_capabilities(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__def9c2c457d799e7621ee923cbb10760395d59600dc385a8058d63bd32e49b13)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedCapabilities", value)

    @builtins.property
    @jsii.member(jsii_name="allowedProcMountTypes")
    def allowed_proc_mount_types(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedProcMountTypes"))

    @allowed_proc_mount_types.setter
    def allowed_proc_mount_types(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4c840d3237d0f67590ef7cd6fe91a65fde64fb3f027ee39f3d6b6e0f3d97f4c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedProcMountTypes", value)

    @builtins.property
    @jsii.member(jsii_name="allowedUnsafeSysctls")
    def allowed_unsafe_sysctls(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedUnsafeSysctls"))

    @allowed_unsafe_sysctls.setter
    def allowed_unsafe_sysctls(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0cc88f9a70db9b86db47a531156106a0eba067314cc6ec61dacc0936e92348c7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedUnsafeSysctls", value)

    @builtins.property
    @jsii.member(jsii_name="allowPrivilegeEscalation")
    def allow_privilege_escalation(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "allowPrivilegeEscalation"))

    @allow_privilege_escalation.setter
    def allow_privilege_escalation(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92fb3c783a2d421e3963accf213c18878879f7b709784c9ee8f72a61c6cf5628)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowPrivilegeEscalation", value)

    @builtins.property
    @jsii.member(jsii_name="defaultAddCapabilities")
    def default_add_capabilities(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "defaultAddCapabilities"))

    @default_add_capabilities.setter
    def default_add_capabilities(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ff6f90c8520a2c8f57a09ca39bf3a8e18f1b5f222060c9c24d542b071b3844b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultAddCapabilities", value)

    @builtins.property
    @jsii.member(jsii_name="defaultAllowPrivilegeEscalation")
    def default_allow_privilege_escalation(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "defaultAllowPrivilegeEscalation"))

    @default_allow_privilege_escalation.setter
    def default_allow_privilege_escalation(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b98dc0c3ef17d390feee74c5101c78bdba2328e1e09e7fe8183be79813bf81b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultAllowPrivilegeEscalation", value)

    @builtins.property
    @jsii.member(jsii_name="forbiddenSysctls")
    def forbidden_sysctls(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "forbiddenSysctls"))

    @forbidden_sysctls.setter
    def forbidden_sysctls(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d596ddc6b14f3abfbfe294a6ed4b38b2885df3faaf82c804d2fc2b24b1a4cefc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forbiddenSysctls", value)

    @builtins.property
    @jsii.member(jsii_name="hostIpc")
    def host_ipc(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "hostIpc"))

    @host_ipc.setter
    def host_ipc(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__420967365de8159088a100892a1fe9a4dae922443d5ceec703589ace7cb1f55e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostIpc", value)

    @builtins.property
    @jsii.member(jsii_name="hostNetwork")
    def host_network(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "hostNetwork"))

    @host_network.setter
    def host_network(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8dde3dfcfac34a8eefa6f58bc06b7f50249a490d386dc5cc199fe6cc090f41d6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostNetwork", value)

    @builtins.property
    @jsii.member(jsii_name="hostPid")
    def host_pid(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "hostPid"))

    @host_pid.setter
    def host_pid(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__31bf21ad795bd8f27948e00aac11d8099b25a2584ce9eb8dba5393585d370fe4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostPid", value)

    @builtins.property
    @jsii.member(jsii_name="privileged")
    def privileged(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "privileged"))

    @privileged.setter
    def privileged(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d89b79e88c85fd3fb9b383a8b0e220d6ed06bf33edf64f0df68ee6c6c4abcf57)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privileged", value)

    @builtins.property
    @jsii.member(jsii_name="readOnlyRootFilesystem")
    def read_only_root_filesystem(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "readOnlyRootFilesystem"))

    @read_only_root_filesystem.setter
    def read_only_root_filesystem(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9bad9dd964352b1a7cdb270b21004bf7590ccc9dcb84a873c932917b8d2b711a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readOnlyRootFilesystem", value)

    @builtins.property
    @jsii.member(jsii_name="requiredDropCapabilities")
    def required_drop_capabilities(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "requiredDropCapabilities"))

    @required_drop_capabilities.setter
    def required_drop_capabilities(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0dc69c924b02cdc777874ecc82abe9572a13ecf476472a892fbe08605083c2f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requiredDropCapabilities", value)

    @builtins.property
    @jsii.member(jsii_name="volumes")
    def volumes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "volumes"))

    @volumes.setter
    def volumes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66c2f8e3d98929f6130f3ade10caf454ee0c60e77daca582caf997f60f9b2580)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumes", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[PodSecurityPolicyV1Beta1Spec]:
        return typing.cast(typing.Optional[PodSecurityPolicyV1Beta1Spec], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PodSecurityPolicyV1Beta1Spec],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97ce050ec475a64012760e4984cf694db4d48c39b1d6f75d20a84632e146e5c0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecRunAsGroup",
    jsii_struct_bases=[],
    name_mapping={"rule": "rule", "range": "range"},
)
class PodSecurityPolicyV1Beta1SpecRunAsGroup:
    def __init__(
        self,
        *,
        rule: builtins.str,
        range: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PodSecurityPolicyV1Beta1SpecRunAsGroupRange", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param rule: rule is the strategy that will dictate the allowable RunAsGroup values that may be set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#rule PodSecurityPolicyV1Beta1#rule}
        :param range: range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#range PodSecurityPolicyV1Beta1#range}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2432bea86c47cb15cf84d350249403eeb3d588788162cd69a1aa25967011a6e)
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
            check_type(argname="argument range", value=range, expected_type=type_hints["range"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "rule": rule,
        }
        if range is not None:
            self._values["range"] = range

    @builtins.property
    def rule(self) -> builtins.str:
        '''rule is the strategy that will dictate the allowable RunAsGroup values that may be set.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#rule PodSecurityPolicyV1Beta1#rule}
        '''
        result = self._values.get("rule")
        assert result is not None, "Required property 'rule' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def range(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PodSecurityPolicyV1Beta1SpecRunAsGroupRange"]]]:
        '''range block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#range PodSecurityPolicyV1Beta1#range}
        '''
        result = self._values.get("range")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PodSecurityPolicyV1Beta1SpecRunAsGroupRange"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PodSecurityPolicyV1Beta1SpecRunAsGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PodSecurityPolicyV1Beta1SpecRunAsGroupOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecRunAsGroupOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9b3ae1e258c552ba126b79517629c86184fdc6ad0d3e68917b5ccdc5dee0d340)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putRange")
    def put_range(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PodSecurityPolicyV1Beta1SpecRunAsGroupRange", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c522fdf477860e72b6d11417010d129d7eb03940a1344fbce1e8db9718e50255)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRange", [value]))

    @jsii.member(jsii_name="resetRange")
    def reset_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRange", []))

    @builtins.property
    @jsii.member(jsii_name="range")
    def range(self) -> "PodSecurityPolicyV1Beta1SpecRunAsGroupRangeList":
        return typing.cast("PodSecurityPolicyV1Beta1SpecRunAsGroupRangeList", jsii.get(self, "range"))

    @builtins.property
    @jsii.member(jsii_name="rangeInput")
    def range_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PodSecurityPolicyV1Beta1SpecRunAsGroupRange"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PodSecurityPolicyV1Beta1SpecRunAsGroupRange"]]], jsii.get(self, "rangeInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleInput")
    def rule_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ruleInput"))

    @builtins.property
    @jsii.member(jsii_name="rule")
    def rule(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rule"))

    @rule.setter
    def rule(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f928418614ffc8d9824d9b54c2b3e9ceab6574afa427ced1a13b63f36e1ed2e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rule", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[PodSecurityPolicyV1Beta1SpecRunAsGroup]:
        return typing.cast(typing.Optional[PodSecurityPolicyV1Beta1SpecRunAsGroup], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PodSecurityPolicyV1Beta1SpecRunAsGroup],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa525469c8dde413690f9c87f7006fffcfaae1322ef6896490fcf7da4fe7e7f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecRunAsGroupRange",
    jsii_struct_bases=[],
    name_mapping={"max": "max", "min": "min"},
)
class PodSecurityPolicyV1Beta1SpecRunAsGroupRange:
    def __init__(self, *, max: jsii.Number, min: jsii.Number) -> None:
        '''
        :param max: max is the end of the range, inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#max PodSecurityPolicyV1Beta1#max}
        :param min: min is the start of the range, inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#min PodSecurityPolicyV1Beta1#min}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b077256f1933878fe23950d4560fa44b9e80b7c87190cd6ca2bb7e59820e1853)
            check_type(argname="argument max", value=max, expected_type=type_hints["max"])
            check_type(argname="argument min", value=min, expected_type=type_hints["min"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "max": max,
            "min": min,
        }

    @builtins.property
    def max(self) -> jsii.Number:
        '''max is the end of the range, inclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#max PodSecurityPolicyV1Beta1#max}
        '''
        result = self._values.get("max")
        assert result is not None, "Required property 'max' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def min(self) -> jsii.Number:
        '''min is the start of the range, inclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#min PodSecurityPolicyV1Beta1#min}
        '''
        result = self._values.get("min")
        assert result is not None, "Required property 'min' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PodSecurityPolicyV1Beta1SpecRunAsGroupRange(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PodSecurityPolicyV1Beta1SpecRunAsGroupRangeList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecRunAsGroupRangeList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a2f3de545ecb1e7f1d4b2ef53c9a3dd16dee6c95b337957b01f73c7d19ed59ac)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "PodSecurityPolicyV1Beta1SpecRunAsGroupRangeOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__658e576cb549ea298314ab0fe03de0ac169900200c11176641f5ff0ce3f1811e)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PodSecurityPolicyV1Beta1SpecRunAsGroupRangeOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__adfee24749dd5f2005b2821563ae5574adb071f0050121fcaf1e6984b1ff94e8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__34ca9444f56e65a5206ed27829e331ca0b2b963143d367bed9c67a32708d2df2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ed20f6b0794c0174ac9ffaccfb4f9318f649449ec5ba4aff05bf544f8df28d38)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecRunAsGroupRange]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecRunAsGroupRange]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecRunAsGroupRange]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e042432bc02eb723ef5f2b6885634d505ae43391ae0257a603ec5fcfa8191d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PodSecurityPolicyV1Beta1SpecRunAsGroupRangeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecRunAsGroupRangeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1f3c21ef5ff321c7cb44f4752024b4bc630e8cb4fad86d8e1fe3c6399025524a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

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
            type_hints = typing.get_type_hints(_typecheckingstub__cee69491d2855dbe310928c41f58b027ae8de01b477d364a15b0de4b3ac6f815)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "max", value)

    @builtins.property
    @jsii.member(jsii_name="min")
    def min(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "min"))

    @min.setter
    def min(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a6cbf6858f6e002414916ca7dd6e4dca0744592a26a37a646bea9a531ef7f74)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "min", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecRunAsGroupRange, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecRunAsGroupRange, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecRunAsGroupRange, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e55a06e5debd7cd9d826e7b1a1f6b40e11f8209cccf658f1faf0c38113efddcd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecRunAsUser",
    jsii_struct_bases=[],
    name_mapping={"rule": "rule", "range": "range"},
)
class PodSecurityPolicyV1Beta1SpecRunAsUser:
    def __init__(
        self,
        *,
        rule: builtins.str,
        range: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PodSecurityPolicyV1Beta1SpecRunAsUserRange", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param rule: rule is the strategy that will dictate the allowable RunAsUser values that may be set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#rule PodSecurityPolicyV1Beta1#rule}
        :param range: range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#range PodSecurityPolicyV1Beta1#range}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dac18dec4ff7a97e8fec29b1c68957ac5cb0a94fd891840b981ba46aa80460c1)
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
            check_type(argname="argument range", value=range, expected_type=type_hints["range"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "rule": rule,
        }
        if range is not None:
            self._values["range"] = range

    @builtins.property
    def rule(self) -> builtins.str:
        '''rule is the strategy that will dictate the allowable RunAsUser values that may be set.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#rule PodSecurityPolicyV1Beta1#rule}
        '''
        result = self._values.get("rule")
        assert result is not None, "Required property 'rule' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def range(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PodSecurityPolicyV1Beta1SpecRunAsUserRange"]]]:
        '''range block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#range PodSecurityPolicyV1Beta1#range}
        '''
        result = self._values.get("range")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PodSecurityPolicyV1Beta1SpecRunAsUserRange"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PodSecurityPolicyV1Beta1SpecRunAsUser(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PodSecurityPolicyV1Beta1SpecRunAsUserOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecRunAsUserOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3e72c00560bb4b63d0187aea071f66695f65822e70e7d2e538c91025e5cd0c90)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putRange")
    def put_range(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PodSecurityPolicyV1Beta1SpecRunAsUserRange", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc7b30a5854a28d28108649235c4a6754f2327cb2ceb72ad7c959540ac0533c3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRange", [value]))

    @jsii.member(jsii_name="resetRange")
    def reset_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRange", []))

    @builtins.property
    @jsii.member(jsii_name="range")
    def range(self) -> "PodSecurityPolicyV1Beta1SpecRunAsUserRangeList":
        return typing.cast("PodSecurityPolicyV1Beta1SpecRunAsUserRangeList", jsii.get(self, "range"))

    @builtins.property
    @jsii.member(jsii_name="rangeInput")
    def range_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PodSecurityPolicyV1Beta1SpecRunAsUserRange"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PodSecurityPolicyV1Beta1SpecRunAsUserRange"]]], jsii.get(self, "rangeInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleInput")
    def rule_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ruleInput"))

    @builtins.property
    @jsii.member(jsii_name="rule")
    def rule(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rule"))

    @rule.setter
    def rule(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27d6eeab1ebdcf66967a57436c2eaaf29bd0b4c5872d6e151b147c3d79266d23)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rule", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[PodSecurityPolicyV1Beta1SpecRunAsUser]:
        return typing.cast(typing.Optional[PodSecurityPolicyV1Beta1SpecRunAsUser], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PodSecurityPolicyV1Beta1SpecRunAsUser],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe537a0cd3644eb9b1f1d9ce1224f33958234ceb8329808af5314342f2bdac12)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecRunAsUserRange",
    jsii_struct_bases=[],
    name_mapping={"max": "max", "min": "min"},
)
class PodSecurityPolicyV1Beta1SpecRunAsUserRange:
    def __init__(self, *, max: jsii.Number, min: jsii.Number) -> None:
        '''
        :param max: max is the end of the range, inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#max PodSecurityPolicyV1Beta1#max}
        :param min: min is the start of the range, inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#min PodSecurityPolicyV1Beta1#min}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb2887341e4db9a47ca5da7149703b366f80f3137b76a6986df4bf5c2914e130)
            check_type(argname="argument max", value=max, expected_type=type_hints["max"])
            check_type(argname="argument min", value=min, expected_type=type_hints["min"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "max": max,
            "min": min,
        }

    @builtins.property
    def max(self) -> jsii.Number:
        '''max is the end of the range, inclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#max PodSecurityPolicyV1Beta1#max}
        '''
        result = self._values.get("max")
        assert result is not None, "Required property 'max' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def min(self) -> jsii.Number:
        '''min is the start of the range, inclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#min PodSecurityPolicyV1Beta1#min}
        '''
        result = self._values.get("min")
        assert result is not None, "Required property 'min' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PodSecurityPolicyV1Beta1SpecRunAsUserRange(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PodSecurityPolicyV1Beta1SpecRunAsUserRangeList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecRunAsUserRangeList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__08a28cd155217e8aced1594df3cae9bc4785456b778065c359680e3e76bf1952)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "PodSecurityPolicyV1Beta1SpecRunAsUserRangeOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63d57b9a5fe4963cdf44364557d0553090242ab94b7bc581882ea8988281eba8)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PodSecurityPolicyV1Beta1SpecRunAsUserRangeOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d6c8ea1ed102d6ad14586a1ac752c50ab4e6bb6b3386fbdee03539f271e7581)
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
            type_hints = typing.get_type_hints(_typecheckingstub__303a9405f8ccdf4bfa9b64aab85bb6ebcc13263a58d5082116e80cbe0a0b9261)
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
            type_hints = typing.get_type_hints(_typecheckingstub__642637c17fa9ebec245761272eabbb7ba8529fbc97f459a18f1358dbc41bcb35)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecRunAsUserRange]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecRunAsUserRange]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecRunAsUserRange]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d022ed9f85c8a7e43299dc028e5eb29a44f66a1bd4e2947771bd837150f9163)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PodSecurityPolicyV1Beta1SpecRunAsUserRangeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecRunAsUserRangeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__82f63331d60aefd31240f0761142be5a12c082ddd6168d8188cfc44952430b4f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

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
            type_hints = typing.get_type_hints(_typecheckingstub__d120e94b0c456130eea6e28a5aa943663a8d44ec78e612f976283278c5fd5bfb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "max", value)

    @builtins.property
    @jsii.member(jsii_name="min")
    def min(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "min"))

    @min.setter
    def min(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d920144e799511c71bd1f1305b42a8bb89e025e4836f5ba120ab618b716b800)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "min", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecRunAsUserRange, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecRunAsUserRange, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecRunAsUserRange, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94a2c34b06c553dfc0dca71ea7da40c5395731789273fe918f157554938fb76e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecSeLinux",
    jsii_struct_bases=[],
    name_mapping={"rule": "rule", "se_linux_options": "seLinuxOptions"},
)
class PodSecurityPolicyV1Beta1SpecSeLinux:
    def __init__(
        self,
        *,
        rule: builtins.str,
        se_linux_options: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptions", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param rule: rule is the strategy that will dictate the allowable labels that may be set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#rule PodSecurityPolicyV1Beta1#rule}
        :param se_linux_options: se_linux_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#se_linux_options PodSecurityPolicyV1Beta1#se_linux_options}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1549fde0988773880f4462d671925092e25ec613d7ac3167ccdaa7288699658e)
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
            check_type(argname="argument se_linux_options", value=se_linux_options, expected_type=type_hints["se_linux_options"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "rule": rule,
        }
        if se_linux_options is not None:
            self._values["se_linux_options"] = se_linux_options

    @builtins.property
    def rule(self) -> builtins.str:
        '''rule is the strategy that will dictate the allowable labels that may be set.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#rule PodSecurityPolicyV1Beta1#rule}
        '''
        result = self._values.get("rule")
        assert result is not None, "Required property 'rule' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def se_linux_options(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptions"]]]:
        '''se_linux_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#se_linux_options PodSecurityPolicyV1Beta1#se_linux_options}
        '''
        result = self._values.get("se_linux_options")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptions"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PodSecurityPolicyV1Beta1SpecSeLinux(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PodSecurityPolicyV1Beta1SpecSeLinuxOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecSeLinuxOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8fdeace9d4c6ba2ae8df0a9be311d30a27613869444cc777e132fc604b188349)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putSeLinuxOptions")
    def put_se_linux_options(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptions", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3df8ab0b5ba1e2c154247f81a12edd8afc4df9b7afdb65e7a02533ce36efad41)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSeLinuxOptions", [value]))

    @jsii.member(jsii_name="resetSeLinuxOptions")
    def reset_se_linux_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSeLinuxOptions", []))

    @builtins.property
    @jsii.member(jsii_name="seLinuxOptions")
    def se_linux_options(
        self,
    ) -> "PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptionsList":
        return typing.cast("PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptionsList", jsii.get(self, "seLinuxOptions"))

    @builtins.property
    @jsii.member(jsii_name="ruleInput")
    def rule_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ruleInput"))

    @builtins.property
    @jsii.member(jsii_name="seLinuxOptionsInput")
    def se_linux_options_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptions"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptions"]]], jsii.get(self, "seLinuxOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="rule")
    def rule(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rule"))

    @rule.setter
    def rule(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__027f456a7d0a61bc95e3fd51b9004b59ff5d9cd65602e1af91f6e5508af0abf7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rule", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[PodSecurityPolicyV1Beta1SpecSeLinux]:
        return typing.cast(typing.Optional[PodSecurityPolicyV1Beta1SpecSeLinux], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PodSecurityPolicyV1Beta1SpecSeLinux],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4861a93b71d077ec67bb0383d51bc8256b10c02ed82a1eb06984a508917c7f7a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptions",
    jsii_struct_bases=[],
    name_mapping={"level": "level", "role": "role", "type": "type", "user": "user"},
)
class PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptions:
    def __init__(
        self,
        *,
        level: builtins.str,
        role: builtins.str,
        type: builtins.str,
        user: builtins.str,
    ) -> None:
        '''
        :param level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#level PodSecurityPolicyV1Beta1#level}.
        :param role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#role PodSecurityPolicyV1Beta1#role}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#type PodSecurityPolicyV1Beta1#type}.
        :param user: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#user PodSecurityPolicyV1Beta1#user}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9dcc787dc0959ef7bde9bfd4aeb6c5c0a63c334d3824ba1ad336ff85e8e0965d)
            check_type(argname="argument level", value=level, expected_type=type_hints["level"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument user", value=user, expected_type=type_hints["user"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "level": level,
            "role": role,
            "type": type,
            "user": user,
        }

    @builtins.property
    def level(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#level PodSecurityPolicyV1Beta1#level}.'''
        result = self._values.get("level")
        assert result is not None, "Required property 'level' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#role PodSecurityPolicyV1Beta1#role}.'''
        result = self._values.get("role")
        assert result is not None, "Required property 'role' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#type PodSecurityPolicyV1Beta1#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#user PodSecurityPolicyV1Beta1#user}.'''
        result = self._values.get("user")
        assert result is not None, "Required property 'user' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptionsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptionsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1f91234cae43822460ad932f9c1b00a72fd65373619eb201c8205add6bc7d326)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2e9cbdbea6b24a4cbe36cc502621992564e2a39b3977165e1780dea378efd02)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c40c937367b6cee4498524577404eb9949e36298e761ec16d4a26999b1003ba7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a7194304d83cca12fb5d37b01140e6455fb004ac89ba019ec7420eec202b1ee8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__da80a5d1ec542eb3b25abb5ca0c953afabc3f19bc378e048c57210df877019c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e74f9c63e1bbe171ac9ef622206902db5e59da41224e448df7a5531c5c6bd76)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cfe323ad5b45b69b6d43eabbea939a51625f3612c676d73ab770adc9ff1c2a32)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="levelInput")
    def level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "levelInput"))

    @builtins.property
    @jsii.member(jsii_name="roleInput")
    def role_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="userInput")
    def user_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userInput"))

    @builtins.property
    @jsii.member(jsii_name="level")
    def level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "level"))

    @level.setter
    def level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0775584d9fa105211fbc4872c6f6c052bb1cf1c9ff052ffea917a36f6478207)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "level", value)

    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "role"))

    @role.setter
    def role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef4e5bbe91f684bd23d2f48094beac98b85b349047310dc4e40e6d5914317209)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "role", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91f8f1b107159924d7473abadfad7336e99757061ced97c5e4e78ea001bbde44)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="user")
    def user(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "user"))

    @user.setter
    def user(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03e9dd5a1309f57ba3826e47bd53061b9ed6909e52507875034e49e245cbd537)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "user", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptions, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptions, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptions, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0909c219e9be1bfc7c16d92013a841fc546dc1a7076eb6131bf8563fb66c2632)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecSupplementalGroups",
    jsii_struct_bases=[],
    name_mapping={"rule": "rule", "range": "range"},
)
class PodSecurityPolicyV1Beta1SpecSupplementalGroups:
    def __init__(
        self,
        *,
        rule: builtins.str,
        range: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PodSecurityPolicyV1Beta1SpecSupplementalGroupsRange", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param rule: rule is the strategy that will dictate what supplemental groups is used in the SecurityContext. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#rule PodSecurityPolicyV1Beta1#rule}
        :param range: range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#range PodSecurityPolicyV1Beta1#range}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2e6996552af4a4ef1fcd931dac9f0df639474b4965fdb3077eaa81883722b95)
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
            check_type(argname="argument range", value=range, expected_type=type_hints["range"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "rule": rule,
        }
        if range is not None:
            self._values["range"] = range

    @builtins.property
    def rule(self) -> builtins.str:
        '''rule is the strategy that will dictate what supplemental groups is used in the SecurityContext.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#rule PodSecurityPolicyV1Beta1#rule}
        '''
        result = self._values.get("rule")
        assert result is not None, "Required property 'rule' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def range(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PodSecurityPolicyV1Beta1SpecSupplementalGroupsRange"]]]:
        '''range block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#range PodSecurityPolicyV1Beta1#range}
        '''
        result = self._values.get("range")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PodSecurityPolicyV1Beta1SpecSupplementalGroupsRange"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PodSecurityPolicyV1Beta1SpecSupplementalGroups(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PodSecurityPolicyV1Beta1SpecSupplementalGroupsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecSupplementalGroupsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__45e18a86979495f3883dd1d01a5e33552e3e2adefc5f0ea23da6de4748305e3e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putRange")
    def put_range(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PodSecurityPolicyV1Beta1SpecSupplementalGroupsRange", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f07c5ce86cc21db906f8f6f5417a6f11c348e70ec57646be440f1db6048a7fe6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRange", [value]))

    @jsii.member(jsii_name="resetRange")
    def reset_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRange", []))

    @builtins.property
    @jsii.member(jsii_name="range")
    def range(self) -> "PodSecurityPolicyV1Beta1SpecSupplementalGroupsRangeList":
        return typing.cast("PodSecurityPolicyV1Beta1SpecSupplementalGroupsRangeList", jsii.get(self, "range"))

    @builtins.property
    @jsii.member(jsii_name="rangeInput")
    def range_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PodSecurityPolicyV1Beta1SpecSupplementalGroupsRange"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PodSecurityPolicyV1Beta1SpecSupplementalGroupsRange"]]], jsii.get(self, "rangeInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleInput")
    def rule_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ruleInput"))

    @builtins.property
    @jsii.member(jsii_name="rule")
    def rule(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rule"))

    @rule.setter
    def rule(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59a665676d22346134476c9e4d70afe1a466b0530f97b27fa5d602bd47581c90)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rule", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PodSecurityPolicyV1Beta1SpecSupplementalGroups]:
        return typing.cast(typing.Optional[PodSecurityPolicyV1Beta1SpecSupplementalGroups], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PodSecurityPolicyV1Beta1SpecSupplementalGroups],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__31aca35e359df7b6bdbe29bf31bdd983fc8266ed02899c0606e7f2010d3cae5c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecSupplementalGroupsRange",
    jsii_struct_bases=[],
    name_mapping={"max": "max", "min": "min"},
)
class PodSecurityPolicyV1Beta1SpecSupplementalGroupsRange:
    def __init__(self, *, max: jsii.Number, min: jsii.Number) -> None:
        '''
        :param max: max is the end of the range, inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#max PodSecurityPolicyV1Beta1#max}
        :param min: min is the start of the range, inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#min PodSecurityPolicyV1Beta1#min}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43818df29b71b8e699bdd20dea0c212457ed758bbc38ef3d88c44b3694ca8d56)
            check_type(argname="argument max", value=max, expected_type=type_hints["max"])
            check_type(argname="argument min", value=min, expected_type=type_hints["min"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "max": max,
            "min": min,
        }

    @builtins.property
    def max(self) -> jsii.Number:
        '''max is the end of the range, inclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#max PodSecurityPolicyV1Beta1#max}
        '''
        result = self._values.get("max")
        assert result is not None, "Required property 'max' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def min(self) -> jsii.Number:
        '''min is the start of the range, inclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#min PodSecurityPolicyV1Beta1#min}
        '''
        result = self._values.get("min")
        assert result is not None, "Required property 'min' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PodSecurityPolicyV1Beta1SpecSupplementalGroupsRange(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PodSecurityPolicyV1Beta1SpecSupplementalGroupsRangeList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecSupplementalGroupsRangeList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e46eefdedb85f1b0714084c5c6d61a5099ff6d395681c32a03aff7fd2e569408)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "PodSecurityPolicyV1Beta1SpecSupplementalGroupsRangeOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c87db8c7f8d09d5cca8c389ec2db0418b0d7ed0d6bdd22da94ad3348a87a7de)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PodSecurityPolicyV1Beta1SpecSupplementalGroupsRangeOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1460a25f53bcbffb7d571c15dd9787e8e04e38357d52e9e3bb2a800e673c372)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5540b54497d089d23d1c8114bb8b827b2cd24cf86aa59d471f1b4e40743e3294)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f19e15b4b49314519cd4f8906bc6fa3f54d4814878819f7e898d31ade887a5a9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecSupplementalGroupsRange]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecSupplementalGroupsRange]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecSupplementalGroupsRange]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7072c9a21a4729b93cebb925072568f1e6044ffcd5bd0575b7e1dad5b48e813f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PodSecurityPolicyV1Beta1SpecSupplementalGroupsRangeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecSupplementalGroupsRangeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__fcb7e6968504a712d811e81c5b650eb2ce6576eaa25a3d8ed2833e2d8ccbdaa4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

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
            type_hints = typing.get_type_hints(_typecheckingstub__e45b89de81603d93cd80e110a86853b6263baca3041a2d7048da4e9ef8bd7cf9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "max", value)

    @builtins.property
    @jsii.member(jsii_name="min")
    def min(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "min"))

    @min.setter
    def min(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7c51a285ee9bdd9817958fe6ed4e952f3982dadd9d161e55ae18fdbcb972e1a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "min", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecSupplementalGroupsRange, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecSupplementalGroupsRange, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecSupplementalGroupsRange, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c21ccc6f684d25a28bd583acbc635f4145c74cc68dfe7a3a8bf45ea90e2e188e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "PodSecurityPolicyV1Beta1",
    "PodSecurityPolicyV1Beta1Config",
    "PodSecurityPolicyV1Beta1Metadata",
    "PodSecurityPolicyV1Beta1MetadataOutputReference",
    "PodSecurityPolicyV1Beta1Spec",
    "PodSecurityPolicyV1Beta1SpecAllowedFlexVolumes",
    "PodSecurityPolicyV1Beta1SpecAllowedFlexVolumesList",
    "PodSecurityPolicyV1Beta1SpecAllowedFlexVolumesOutputReference",
    "PodSecurityPolicyV1Beta1SpecAllowedHostPaths",
    "PodSecurityPolicyV1Beta1SpecAllowedHostPathsList",
    "PodSecurityPolicyV1Beta1SpecAllowedHostPathsOutputReference",
    "PodSecurityPolicyV1Beta1SpecFsGroup",
    "PodSecurityPolicyV1Beta1SpecFsGroupOutputReference",
    "PodSecurityPolicyV1Beta1SpecFsGroupRange",
    "PodSecurityPolicyV1Beta1SpecFsGroupRangeList",
    "PodSecurityPolicyV1Beta1SpecFsGroupRangeOutputReference",
    "PodSecurityPolicyV1Beta1SpecHostPorts",
    "PodSecurityPolicyV1Beta1SpecHostPortsList",
    "PodSecurityPolicyV1Beta1SpecHostPortsOutputReference",
    "PodSecurityPolicyV1Beta1SpecOutputReference",
    "PodSecurityPolicyV1Beta1SpecRunAsGroup",
    "PodSecurityPolicyV1Beta1SpecRunAsGroupOutputReference",
    "PodSecurityPolicyV1Beta1SpecRunAsGroupRange",
    "PodSecurityPolicyV1Beta1SpecRunAsGroupRangeList",
    "PodSecurityPolicyV1Beta1SpecRunAsGroupRangeOutputReference",
    "PodSecurityPolicyV1Beta1SpecRunAsUser",
    "PodSecurityPolicyV1Beta1SpecRunAsUserOutputReference",
    "PodSecurityPolicyV1Beta1SpecRunAsUserRange",
    "PodSecurityPolicyV1Beta1SpecRunAsUserRangeList",
    "PodSecurityPolicyV1Beta1SpecRunAsUserRangeOutputReference",
    "PodSecurityPolicyV1Beta1SpecSeLinux",
    "PodSecurityPolicyV1Beta1SpecSeLinuxOutputReference",
    "PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptions",
    "PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptionsList",
    "PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptionsOutputReference",
    "PodSecurityPolicyV1Beta1SpecSupplementalGroups",
    "PodSecurityPolicyV1Beta1SpecSupplementalGroupsOutputReference",
    "PodSecurityPolicyV1Beta1SpecSupplementalGroupsRange",
    "PodSecurityPolicyV1Beta1SpecSupplementalGroupsRangeList",
    "PodSecurityPolicyV1Beta1SpecSupplementalGroupsRangeOutputReference",
]

publication.publish()

def _typecheckingstub__9679c31c9723b516c52d280faa70e2cb64dd7a408bedd8e57161d52c8d7dbbb1(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    metadata: typing.Union[PodSecurityPolicyV1Beta1Metadata, typing.Dict[builtins.str, typing.Any]],
    spec: typing.Union[PodSecurityPolicyV1Beta1Spec, typing.Dict[builtins.str, typing.Any]],
    id: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__0347391f35c50b6c2ccf6677f55d0d25804fde75b6dce3a26c16856000a2dcb3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b944da6757e8082a6ff12861b1ff0f85ab63c57afe28cbe91a29fbe1a2fdf3c8(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    metadata: typing.Union[PodSecurityPolicyV1Beta1Metadata, typing.Dict[builtins.str, typing.Any]],
    spec: typing.Union[PodSecurityPolicyV1Beta1Spec, typing.Dict[builtins.str, typing.Any]],
    id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b329507f84f1b10c617c56ecd37c8158224f559278ee847f7fec805cceedd001(
    *,
    annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2f148d05095f822f0a934c8884e29df8c3d983f01ea9ce50609474b65a12f44(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1406501757a30deaec4413d25160121da72005816a123c7329ab7020b3d48f90(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__377424566de947b9f69668660ed4ea5c725b3b9632cfebfff629ff54d22fbfd7(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a90150b7e3765f33e71082f2ffb7ef8f2bbccf856d66409942170966aaa79508(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__489784eb9e052fdf0f8c07e63fdebaf42f07446cdb68b891b0ade5ba039e8045(
    value: typing.Optional[PodSecurityPolicyV1Beta1Metadata],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b61e14c7c2c8179b7a7d038205493a603f4b4986bd14a63066f6a2ca268809c1(
    *,
    fs_group: typing.Union[PodSecurityPolicyV1Beta1SpecFsGroup, typing.Dict[builtins.str, typing.Any]],
    run_as_user: typing.Union[PodSecurityPolicyV1Beta1SpecRunAsUser, typing.Dict[builtins.str, typing.Any]],
    supplemental_groups: typing.Union[PodSecurityPolicyV1Beta1SpecSupplementalGroups, typing.Dict[builtins.str, typing.Any]],
    allowed_capabilities: typing.Optional[typing.Sequence[builtins.str]] = None,
    allowed_flex_volumes: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PodSecurityPolicyV1Beta1SpecAllowedFlexVolumes, typing.Dict[builtins.str, typing.Any]]]]] = None,
    allowed_host_paths: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PodSecurityPolicyV1Beta1SpecAllowedHostPaths, typing.Dict[builtins.str, typing.Any]]]]] = None,
    allowed_proc_mount_types: typing.Optional[typing.Sequence[builtins.str]] = None,
    allowed_unsafe_sysctls: typing.Optional[typing.Sequence[builtins.str]] = None,
    allow_privilege_escalation: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    default_add_capabilities: typing.Optional[typing.Sequence[builtins.str]] = None,
    default_allow_privilege_escalation: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    forbidden_sysctls: typing.Optional[typing.Sequence[builtins.str]] = None,
    host_ipc: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    host_network: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    host_pid: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    host_ports: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PodSecurityPolicyV1Beta1SpecHostPorts, typing.Dict[builtins.str, typing.Any]]]]] = None,
    privileged: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    read_only_root_filesystem: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    required_drop_capabilities: typing.Optional[typing.Sequence[builtins.str]] = None,
    run_as_group: typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecRunAsGroup, typing.Dict[builtins.str, typing.Any]]] = None,
    se_linux: typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecSeLinux, typing.Dict[builtins.str, typing.Any]]] = None,
    volumes: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e758f6185a95ddaa55061e0e12dd5822af1084fe7d22b85230823d6edbbdfa7c(
    *,
    driver: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13138564d0498df938411b766f6ccf653d8215fa6501c110d282124ecfcf0064(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed59c846ed70f5853448249c83fb43e1b86f5b066fa5dd89de07f59dcf1a48fd(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62cd89d46c23349e10655727a851377e030c91cbc6430bb6d56de527f4f3142b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4edb7fa83e56c96c33ce9097a493bb5695cb965cbf8d6c88dd060dc9fa3b60b0(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__adbda02882194591551946248324cc10e53ec8210066b44757f1d5c2ac77c09b(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__317e62346b94868856f765ea61092e908fc067c5558d548a58d478c95b55849b(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecAllowedFlexVolumes]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14d0cbb75a8fddd8f1c25d0ccfe4348a476b488fcd4c0f50d9e04322f3c813cc(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e26ec60608a776050a80cfe9f3bedaa666386eab0493976c5b39d6005566bb7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f769d50494d9df9ed1dbe3e51e225ebcc81016c5953b1ad2b7538b10064aca8(
    value: typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecAllowedFlexVolumes, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb594c584b0396fbf2a8c74de72ae632981d051f530d2070e70e48f693b9a209(
    *,
    path_prefix: builtins.str,
    read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f2e8c77fb12313aeca9682dd09713749ec009490d794d56319df624453db38e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0b4644f082260ce66eb67a9c31a4bf2165c508a0e8d9d1a1f255ca0c9c17642(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c1c09ce3c8f70e286e72cffbc07c27d47d388324dd4fab03ada3013645a0b05(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__310bc7034cb4c1c2ae77780d2cf7e0cb26c3f23163af8cde3c6dffc1853b9c72(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e1b8f9f9f340663a038f7ebc0199efa2327b728d90c7116fd9423dfcd4a90a2(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43aeb9f61099d8218201893ef50d53c4a0798cf102fcdc900e58674334001ed2(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecAllowedHostPaths]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05b63e181cd8be5b450e1d03779187755dcd3aed30fd137ca52937e4b358a5d0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61b258ca7fed612ae34c0a9e7c3dc62c61fef6d4cdd0468a4b72d0390cb6341e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d9867db59cc84adca816b3095598041ddb55fe1f7b44d20777d5eb21e324966(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ccc6b48756de47d4b7d2415bd1c3677f74696591a4182cbed2d355c1c436d0bb(
    value: typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecAllowedHostPaths, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab23dc0bbcd53640ea3de5acc31f185bc76bb8892d151026a6139d008f37b537(
    *,
    rule: builtins.str,
    range: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PodSecurityPolicyV1Beta1SpecFsGroupRange, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98a386e51a7f60a7b4092b72dd131d2b42ba4854bab5c8d175ca8bd9dd6f6aa0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a1e5252fc88b78c419563859486b2bd4fd0e92ec1998e730df6fa19d9b64c1a(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PodSecurityPolicyV1Beta1SpecFsGroupRange, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b1c91d2368c41055883e9608678a1813cb5d0c2d645fdfcb518f4edba5417d5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f585e0e82e8e55046a54d2b0bc0dbd178327776464245ac040d7b4364ef0e71(
    value: typing.Optional[PodSecurityPolicyV1Beta1SpecFsGroup],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__035f665808a3de7623c9fd738cdb0780028efbe105a20eede15e68519495a9d3(
    *,
    max: jsii.Number,
    min: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3ab584b174d4b5530a8fc9cd6e2b57f7e2222406388607c4fc348b1e1eeb66f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0293fffe7fea6d32759603f5cbd1197b26ec250cf07725850eb1bbe23a1dd5c(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ae18bcd54fcb1b441b39e6f3371836db6145b8bd2242d2453c067718b4c1490(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82cdb739948e45b0065d4c251274599ebc0e76eb17096270c9b6f8353133002c(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c84c7b45a93976ee754e4d6a5f16a0285bb3b9fe902daebe63b5f3d4e395f878(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c78c62a22d7b7e2952ae88eeb07e5e953c763ddfb037d38dee715164886ddb0(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecFsGroupRange]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__edb28452c44da514143c66a9e9e86d259eac639f6ac4f29064b40f9d1df18fdf(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ffe5fa1b52a7ed828aaf193681a07c2f39cb5bcabf5a8d46602d1705d56dfc5(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c65ce87c53751c839c19ce42709baa3a8ab44e9a398e9e35b80f18529d88b25d(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de4b1a90341682c469a97c919d29add13a5e99eee1ebb114ec2e6fcf7b0181b4(
    value: typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecFsGroupRange, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e673e42b07be435acc8800820468a07e95d7d8b1dc332dcf7b0d4d289d880714(
    *,
    max: jsii.Number,
    min: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8a1b8241ec20d1eeeabdbf235b5d5d13818d8ac13c48eb69bf32cae325594dc(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__964f173a0406ca5acf54f9c109f169143b38dc5c85961143440a41e461bf75f8(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b206df2cc58937abe2c1ac07b9679c777821bc56eb08d6f8dc45ce6a7705d82(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef9a88ebe40693479d7b1925b9a09da873bfc4e4dcc4bbbe32717759a7b14fb8(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff0bfbfb03ab331942963faef3b85937f8eb3eef2947bc05b51bbe18e41449b6(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7ce68d19a0e94c0bcc279a7175c4146fa5658648d30fd0917af967d991831ba(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecHostPorts]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__207668b0d32cd36bba4041e22286c7e79bc726f40525deaf5ff6cdd142ab1c39(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c5294a3f2fac9cade1c7bff7b55443d3d294b686aead53c0b8a1e1a72f416cc(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b1c35ce6a7e661546fb6d77729099f03c0442dfc1c9add032310a1e6d09475a(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b91e19404e74980d151599c68fb7ee00e51623f9176f860667397e25ceffb013(
    value: typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecHostPorts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c0645436f469c6bc03bb01321199773c6713ae4e66b44bc209e4d65235ab2a5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e61f2b67036eff3aac28cda43e86475a6ad7473491a9f84d7a208563317fde4(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PodSecurityPolicyV1Beta1SpecAllowedFlexVolumes, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cda26d0aeaa98464401d498a4efd4d2269d6e504b3c07704088d4fe2cf5b0fda(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PodSecurityPolicyV1Beta1SpecAllowedHostPaths, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2de3745f0f6784c55399e630e5a25580d2b8de6278573eb2c7693acde52059dd(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PodSecurityPolicyV1Beta1SpecHostPorts, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__def9c2c457d799e7621ee923cbb10760395d59600dc385a8058d63bd32e49b13(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4c840d3237d0f67590ef7cd6fe91a65fde64fb3f027ee39f3d6b6e0f3d97f4c(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0cc88f9a70db9b86db47a531156106a0eba067314cc6ec61dacc0936e92348c7(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92fb3c783a2d421e3963accf213c18878879f7b709784c9ee8f72a61c6cf5628(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ff6f90c8520a2c8f57a09ca39bf3a8e18f1b5f222060c9c24d542b071b3844b(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b98dc0c3ef17d390feee74c5101c78bdba2328e1e09e7fe8183be79813bf81b(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d596ddc6b14f3abfbfe294a6ed4b38b2885df3faaf82c804d2fc2b24b1a4cefc(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__420967365de8159088a100892a1fe9a4dae922443d5ceec703589ace7cb1f55e(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8dde3dfcfac34a8eefa6f58bc06b7f50249a490d386dc5cc199fe6cc090f41d6(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31bf21ad795bd8f27948e00aac11d8099b25a2584ce9eb8dba5393585d370fe4(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d89b79e88c85fd3fb9b383a8b0e220d6ed06bf33edf64f0df68ee6c6c4abcf57(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9bad9dd964352b1a7cdb270b21004bf7590ccc9dcb84a873c932917b8d2b711a(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0dc69c924b02cdc777874ecc82abe9572a13ecf476472a892fbe08605083c2f(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66c2f8e3d98929f6130f3ade10caf454ee0c60e77daca582caf997f60f9b2580(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97ce050ec475a64012760e4984cf694db4d48c39b1d6f75d20a84632e146e5c0(
    value: typing.Optional[PodSecurityPolicyV1Beta1Spec],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2432bea86c47cb15cf84d350249403eeb3d588788162cd69a1aa25967011a6e(
    *,
    rule: builtins.str,
    range: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PodSecurityPolicyV1Beta1SpecRunAsGroupRange, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b3ae1e258c552ba126b79517629c86184fdc6ad0d3e68917b5ccdc5dee0d340(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c522fdf477860e72b6d11417010d129d7eb03940a1344fbce1e8db9718e50255(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PodSecurityPolicyV1Beta1SpecRunAsGroupRange, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f928418614ffc8d9824d9b54c2b3e9ceab6574afa427ced1a13b63f36e1ed2e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa525469c8dde413690f9c87f7006fffcfaae1322ef6896490fcf7da4fe7e7f7(
    value: typing.Optional[PodSecurityPolicyV1Beta1SpecRunAsGroup],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b077256f1933878fe23950d4560fa44b9e80b7c87190cd6ca2bb7e59820e1853(
    *,
    max: jsii.Number,
    min: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2f3de545ecb1e7f1d4b2ef53c9a3dd16dee6c95b337957b01f73c7d19ed59ac(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__658e576cb549ea298314ab0fe03de0ac169900200c11176641f5ff0ce3f1811e(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__adfee24749dd5f2005b2821563ae5574adb071f0050121fcaf1e6984b1ff94e8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34ca9444f56e65a5206ed27829e331ca0b2b963143d367bed9c67a32708d2df2(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed20f6b0794c0174ac9ffaccfb4f9318f649449ec5ba4aff05bf544f8df28d38(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e042432bc02eb723ef5f2b6885634d505ae43391ae0257a603ec5fcfa8191d2(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecRunAsGroupRange]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f3c21ef5ff321c7cb44f4752024b4bc630e8cb4fad86d8e1fe3c6399025524a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cee69491d2855dbe310928c41f58b027ae8de01b477d364a15b0de4b3ac6f815(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a6cbf6858f6e002414916ca7dd6e4dca0744592a26a37a646bea9a531ef7f74(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e55a06e5debd7cd9d826e7b1a1f6b40e11f8209cccf658f1faf0c38113efddcd(
    value: typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecRunAsGroupRange, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dac18dec4ff7a97e8fec29b1c68957ac5cb0a94fd891840b981ba46aa80460c1(
    *,
    rule: builtins.str,
    range: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PodSecurityPolicyV1Beta1SpecRunAsUserRange, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e72c00560bb4b63d0187aea071f66695f65822e70e7d2e538c91025e5cd0c90(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc7b30a5854a28d28108649235c4a6754f2327cb2ceb72ad7c959540ac0533c3(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PodSecurityPolicyV1Beta1SpecRunAsUserRange, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27d6eeab1ebdcf66967a57436c2eaaf29bd0b4c5872d6e151b147c3d79266d23(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe537a0cd3644eb9b1f1d9ce1224f33958234ceb8329808af5314342f2bdac12(
    value: typing.Optional[PodSecurityPolicyV1Beta1SpecRunAsUser],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb2887341e4db9a47ca5da7149703b366f80f3137b76a6986df4bf5c2914e130(
    *,
    max: jsii.Number,
    min: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08a28cd155217e8aced1594df3cae9bc4785456b778065c359680e3e76bf1952(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63d57b9a5fe4963cdf44364557d0553090242ab94b7bc581882ea8988281eba8(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d6c8ea1ed102d6ad14586a1ac752c50ab4e6bb6b3386fbdee03539f271e7581(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__303a9405f8ccdf4bfa9b64aab85bb6ebcc13263a58d5082116e80cbe0a0b9261(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__642637c17fa9ebec245761272eabbb7ba8529fbc97f459a18f1358dbc41bcb35(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d022ed9f85c8a7e43299dc028e5eb29a44f66a1bd4e2947771bd837150f9163(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecRunAsUserRange]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82f63331d60aefd31240f0761142be5a12c082ddd6168d8188cfc44952430b4f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d120e94b0c456130eea6e28a5aa943663a8d44ec78e612f976283278c5fd5bfb(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d920144e799511c71bd1f1305b42a8bb89e025e4836f5ba120ab618b716b800(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94a2c34b06c553dfc0dca71ea7da40c5395731789273fe918f157554938fb76e(
    value: typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecRunAsUserRange, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1549fde0988773880f4462d671925092e25ec613d7ac3167ccdaa7288699658e(
    *,
    rule: builtins.str,
    se_linux_options: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptions, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8fdeace9d4c6ba2ae8df0a9be311d30a27613869444cc777e132fc604b188349(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3df8ab0b5ba1e2c154247f81a12edd8afc4df9b7afdb65e7a02533ce36efad41(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptions, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__027f456a7d0a61bc95e3fd51b9004b59ff5d9cd65602e1af91f6e5508af0abf7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4861a93b71d077ec67bb0383d51bc8256b10c02ed82a1eb06984a508917c7f7a(
    value: typing.Optional[PodSecurityPolicyV1Beta1SpecSeLinux],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9dcc787dc0959ef7bde9bfd4aeb6c5c0a63c334d3824ba1ad336ff85e8e0965d(
    *,
    level: builtins.str,
    role: builtins.str,
    type: builtins.str,
    user: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f91234cae43822460ad932f9c1b00a72fd65373619eb201c8205add6bc7d326(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2e9cbdbea6b24a4cbe36cc502621992564e2a39b3977165e1780dea378efd02(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c40c937367b6cee4498524577404eb9949e36298e761ec16d4a26999b1003ba7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7194304d83cca12fb5d37b01140e6455fb004ac89ba019ec7420eec202b1ee8(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da80a5d1ec542eb3b25abb5ca0c953afabc3f19bc378e048c57210df877019c5(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e74f9c63e1bbe171ac9ef622206902db5e59da41224e448df7a5531c5c6bd76(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptions]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfe323ad5b45b69b6d43eabbea939a51625f3612c676d73ab770adc9ff1c2a32(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0775584d9fa105211fbc4872c6f6c052bb1cf1c9ff052ffea917a36f6478207(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef4e5bbe91f684bd23d2f48094beac98b85b349047310dc4e40e6d5914317209(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91f8f1b107159924d7473abadfad7336e99757061ced97c5e4e78ea001bbde44(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03e9dd5a1309f57ba3826e47bd53061b9ed6909e52507875034e49e245cbd537(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0909c219e9be1bfc7c16d92013a841fc546dc1a7076eb6131bf8563fb66c2632(
    value: typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptions, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2e6996552af4a4ef1fcd931dac9f0df639474b4965fdb3077eaa81883722b95(
    *,
    rule: builtins.str,
    range: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PodSecurityPolicyV1Beta1SpecSupplementalGroupsRange, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45e18a86979495f3883dd1d01a5e33552e3e2adefc5f0ea23da6de4748305e3e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f07c5ce86cc21db906f8f6f5417a6f11c348e70ec57646be440f1db6048a7fe6(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PodSecurityPolicyV1Beta1SpecSupplementalGroupsRange, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59a665676d22346134476c9e4d70afe1a466b0530f97b27fa5d602bd47581c90(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31aca35e359df7b6bdbe29bf31bdd983fc8266ed02899c0606e7f2010d3cae5c(
    value: typing.Optional[PodSecurityPolicyV1Beta1SpecSupplementalGroups],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43818df29b71b8e699bdd20dea0c212457ed758bbc38ef3d88c44b3694ca8d56(
    *,
    max: jsii.Number,
    min: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e46eefdedb85f1b0714084c5c6d61a5099ff6d395681c32a03aff7fd2e569408(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c87db8c7f8d09d5cca8c389ec2db0418b0d7ed0d6bdd22da94ad3348a87a7de(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1460a25f53bcbffb7d571c15dd9787e8e04e38357d52e9e3bb2a800e673c372(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5540b54497d089d23d1c8114bb8b827b2cd24cf86aa59d471f1b4e40743e3294(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f19e15b4b49314519cd4f8906bc6fa3f54d4814878819f7e898d31ade887a5a9(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7072c9a21a4729b93cebb925072568f1e6044ffcd5bd0575b7e1dad5b48e813f(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecSupplementalGroupsRange]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fcb7e6968504a712d811e81c5b650eb2ce6576eaa25a3d8ed2833e2d8ccbdaa4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e45b89de81603d93cd80e110a86853b6263baca3041a2d7048da4e9ef8bd7cf9(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7c51a285ee9bdd9817958fe6ed4e952f3982dadd9d161e55ae18fdbcb972e1a(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c21ccc6f684d25a28bd583acbc635f4145c74cc68dfe7a3a8bf45ea90e2e188e(
    value: typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecSupplementalGroupsRange, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
